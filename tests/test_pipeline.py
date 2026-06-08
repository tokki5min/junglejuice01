import asyncio
from pathlib import Path

import pytest

from ai_film_pipeline import EngineConfig, PipelineConfig, Storyboard
from ai_film_pipeline.concurrency import map_with_limit, poll_until
from ai_film_pipeline.stages import image, plan, video, assemble


def test_map_with_limit_preserves_order_and_caps_concurrency() -> None:
    in_flight = 0
    peak = 0

    async def worker(n: int) -> int:
        nonlocal in_flight, peak
        in_flight += 1
        peak = max(peak, in_flight)
        await asyncio.sleep(0.01)
        in_flight -= 1
        return n * 2

    results = asyncio.run(map_with_limit([1, 2, 3, 4, 5], worker, limit=2))
    assert results == [2, 4, 6, 8, 10]
    assert peak <= 2


def test_poll_until_returns_when_ready() -> None:
    calls = {"n": 0}

    async def check() -> str | None:
        calls["n"] += 1
        return "done" if calls["n"] >= 3 else None

    async def fake_sleep(_seconds: float) -> None:
        return None

    result = asyncio.run(poll_until(check, interval=1, timeout=100, sleep=fake_sleep))
    assert result == "done"
    assert calls["n"] == 3


def test_poll_until_times_out() -> None:
    async def check() -> None:
        return None

    async def fake_sleep(_seconds: float) -> None:
        return None

    with pytest.raises(TimeoutError):
        asyncio.run(poll_until(check, interval=1, timeout=2, sleep=fake_sleep))


def test_stub_storyboard_has_spine() -> None:
    storyboard = plan._stub_storyboard(30)
    assert len(storyboard.shots) == 30
    assert all(shot.motif for shot in storyboard.shots)
    assert {shot.act for shot in storyboard.shots} == {"갈망", "야생", "포집", "재생"}


def test_validation_batch_samples_across_storyboard() -> None:
    storyboard = plan._stub_storyboard(30)
    batch = image.select_validation_batch(storyboard, 6)
    assert len(batch) == 6
    # spans first and last acts
    assert batch[0].index == 1
    assert batch[-1].index >= 25


def test_video_prompt_guards_against_music() -> None:
    shot = plan._stub_storyboard(1).shots[0]
    assert video.build_video_prompt(shot).startswith("no music")


def _dry_config(tmp_path: Path) -> PipelineConfig:
    return PipelineConfig(
        project="test",
        output_dir=tmp_path,
        storyboard_path=tmp_path / "storyboard.json",
        image_engine=EngineConfig(name="img", provider="openai-image", concurrency=3),
        video_engines=[EngineConfig(name="kling", provider="replicate-video", concurrency=2)],
        dry_run=True,
    )


def test_full_pipeline_runs_in_dry_run(tmp_path: Path) -> None:
    from ai_film_pipeline import pipeline

    config = _dry_config(tmp_path)
    output = asyncio.run(pipeline.run_full(config, "https://example.test/ref", "fast cuts, 35mm grain", shot_count=8))

    assert output.exists()
    storyboard = Storyboard.load(config.storyboard_path)
    assert len(storyboard.shots) == 8
    assert all(shot.image_path for shot in storyboard.shots)
    assert all(shot.video_paths.get("kling") for shot in storyboard.shots)
    assert config.manifest_path.exists()


def test_assemble_collects_in_order(tmp_path: Path) -> None:
    storyboard = plan._stub_storyboard(3)
    for shot in storyboard.shots:
        shot.video_paths["kling"] = f"/clips/{shot.shot_id}.mp4"
    clips = assemble.collect_clips(storyboard, "kling")
    assert [c.name for c in clips] == ["cut_01.mp4", "cut_02.mp4", "cut_03.mp4"]
