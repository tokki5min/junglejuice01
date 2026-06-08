"""Orchestration — wire the stages together with manifest tracking.

Each function maps to a CLI subcommand. Stages are independent so you can run them
one at a time (the recommended way: review between each), or chain them with the
full `run` after you trust your prompts.
"""

from __future__ import annotations

from pathlib import Path

from .config import PipelineConfig
from .manifest import Manifest
from .models import Storyboard
from .stages import assemble, image, plan, reference, video


def stage_reference(config: PipelineConfig, url: str, *, fps: int | None = None) -> list[Path]:
    """Download a reference and extract frames; record frame count."""

    frames = reference.run(
        url,
        config.assets_dir / "reference.mp4",
        config.frames_dir,
        fps=fps or config.fps_capture,
        dry_run=config.dry_run,
    )
    manifest = Manifest.load(config.manifest_path)
    manifest.record_stage("reference", {"url": url, "frames": len(frames)})
    manifest.save()
    return frames


def stage_plan(config: PipelineConfig, reference_notes: str, *, shot_count: int = 30) -> Storyboard:
    """Generate a storyboard and record where it was written."""

    storyboard = plan.run(config, reference_notes, shot_count=shot_count, dry_run=config.dry_run)
    manifest = Manifest.load(config.manifest_path)
    manifest.record_stage("plan", {"shots": len(storyboard.shots), "storyboard": str(config.storyboard_path)})
    manifest.save()
    return storyboard


async def stage_image(config: PipelineConfig, *, validation_only: bool = False) -> Storyboard:
    """Generate images (or just the validation batch) and persist updated shots."""

    storyboard = Storyboard.load(config.storyboard_path)
    shots = await image.run(config, storyboard, validation_only=validation_only)
    storyboard.save(config.storyboard_path)
    manifest = Manifest.load(config.manifest_path)
    manifest.record_stage(
        "image" if not validation_only else "image-validation",
        {"generated": len(shots), "validation_only": validation_only},
    )
    manifest.save()
    return storyboard


async def stage_video(config: PipelineConfig) -> Storyboard:
    """Animate approved shots across all engines and persist clip paths."""

    storyboard = Storyboard.load(config.storyboard_path)
    shots = [s for s in storyboard.shots if s.image_path]
    await video.run(config, shots)
    storyboard.save(config.storyboard_path)
    manifest = Manifest.load(config.manifest_path)
    manifest.record_stage(
        "video",
        {"engines": [e.name for e in config.video_engines], "shots": len(shots)},
    )
    manifest.save()
    return storyboard


def stage_assemble(config: PipelineConfig, engine: str) -> Path:
    """Assemble the final film for one engine."""

    storyboard = Storyboard.load(config.storyboard_path)
    output = assemble.run(storyboard, engine, config.output_dir, dry_run=config.dry_run)
    manifest = Manifest.load(config.manifest_path)
    manifest.record_stage("assemble", {"engine": engine, "output": str(output)})
    manifest.save()
    return output


async def run_full(config: PipelineConfig, url: str, reference_notes: str, *, shot_count: int = 30) -> Path:
    """Run every stage end to end. Best used only after prompts are trusted."""

    stage_reference(config, url)
    stage_plan(config, reference_notes, shot_count=shot_count)
    await stage_image(config, validation_only=False)
    storyboard = await stage_video(config)
    engine = config.video_engines[0].name if config.video_engines else "default"
    del storyboard
    return stage_assemble(config, engine)
