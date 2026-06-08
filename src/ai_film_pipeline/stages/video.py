"""STEP 6-7 — Multi-engine video generation.

The same image is sent to several engines and compared, because each engine has a
different character (Kling: stable; Seedance: auto SFX). Two project-wide rules are
enforced here:
  - 'no music' is prepended to every prompt so BGM never bakes into a clip.
  - Each engine's concurrency ceiling is respected (e.g. Higgsfield = 8).

30 shots x 3 engines = 90 clips run in the background while you sleep.
"""

from __future__ import annotations

from pathlib import Path

from ..concurrency import map_with_limit
from ..config import EngineConfig, PipelineConfig
from ..models import Shot
from ..providers import Provider, build_provider

NO_MUSIC_PREFIX = "no music, no score, no melody. "


def build_video_prompt(shot: Shot) -> str:
    """Prepend the no-music guard so audio stays editable downstream."""

    return f"{NO_MUSIC_PREFIX}{shot.prompt}"


async def _animate_one(provider: Provider, engine: EngineConfig, shot: Shot, clips_dir: Path) -> Shot:
    if not shot.image_path:
        raise ValueError(f"{shot.shot_id} has no image_path; run the image stage first.")
    output = clips_dir / engine.name / f"{shot.shot_id}.mp4"
    job = await provider.generate(
        build_video_prompt(shot),
        output,
        image=shot.image_path,
    )
    shot.video_paths[engine.name] = str(job.output_path)
    return shot


async def animate_with_engine(
    engine: EngineConfig,
    shots: list[Shot],
    clips_dir: Path,
    *,
    dry_run: bool = False,
) -> list[Shot]:
    """Animate all shots with a single engine, honoring its concurrency limit."""

    provider = build_provider(engine, dry_run=dry_run)

    async def worker(shot: Shot) -> Shot:
        return await _animate_one(provider, engine, shot, clips_dir)

    return await map_with_limit(shots, worker, engine.concurrency)


async def run(config: PipelineConfig, shots: list[Shot]) -> list[Shot]:
    """Animate the given shots across every configured video engine."""

    if not config.video_engines:
        raise ValueError("No video_engines configured.")
    for engine in config.video_engines:
        await animate_with_engine(engine, shots, config.clips_dir, dry_run=config.dry_run)
    return shots
