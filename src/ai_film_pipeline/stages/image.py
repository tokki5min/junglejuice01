"""STEP 4-5 — Image generation with a human validation gate.

The three automations the code owns:
  - 동시성: generate several shots in parallel (engine concurrency ceiling).
  - 폴링: providers report done; concurrency helpers wait.
  - 후처리: crop to the target aspect ratio with ffmpeg.

The one thing the code does NOT own: judgment. The stage first renders a small
representative batch (검증 배치). A human approves the look before the full set runs,
so a bad prompt costs 6 images, not 30.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from ..concurrency import map_with_limit
from ..config import PipelineConfig
from ..models import Shot, Storyboard
from ..providers import Provider, build_provider


async def _generate_one(provider: Provider, shot: Shot, images_dir: Path) -> Shot:
    output = images_dir / f"{shot.shot_id}.png"
    extra: dict[str, object] = {}
    if shot.reference_image:
        # Identity lock: feed the matched face/bottle back in as img2img.
        extra["reference_image"] = shot.reference_image
        extra["input_fidelity"] = "high"
    job = await provider.generate(shot.prompt, output, **extra)
    shot.image_path = str(job.output_path)
    return shot


async def generate_images(
    provider: Provider,
    shots: list[Shot],
    images_dir: Path,
    *,
    concurrency: int,
) -> list[Shot]:
    """Generate images for the given shots in parallel, returning updated shots."""

    images_dir.mkdir(parents=True, exist_ok=True)

    async def worker(shot: Shot) -> Shot:
        return await _generate_one(provider, shot, images_dir)

    return await map_with_limit(shots, worker, concurrency)


def select_validation_batch(storyboard: Storyboard, size: int) -> list[Shot]:
    """Pick a representative spread of shots to review before the full run.

    Evenly samples across the storyboard so the batch covers every act.
    """

    shots = storyboard.shots
    if size >= len(shots):
        return list(shots)
    step = len(shots) / size
    return [shots[int(i * step)] for i in range(size)]


def crop_to_aspect(image_path: Path, aspect_ratio: str = "16:9", *, dry_run: bool = False) -> Path:
    """Post-process: center-crop an image to the target aspect ratio via ffmpeg."""

    if dry_run:
        return image_path
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("'ffmpeg' is required for cropping. Install it or skip post-processing.")
    w, h = (int(x) for x in aspect_ratio.split(":"))
    cropped = image_path.with_name(f"{image_path.stem}_crop{image_path.suffix}")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(image_path),
         "-vf", f"crop='min(iw,ih*{w}/{h})':'min(ih,iw*{h}/{w})'", str(cropped)],
        check=True,
    )
    return cropped


async def run(
    config: PipelineConfig,
    storyboard: Storyboard,
    *,
    validation_only: bool = False,
) -> list[Shot]:
    """Generate images for the storyboard.

    With validation_only=True, only the representative batch is rendered — the
    human gate before committing to the full set.
    """

    if config.image_engine is None:
        raise ValueError("No image_engine configured.")
    provider = build_provider(config.image_engine, dry_run=config.dry_run)

    if validation_only:
        shots = select_validation_batch(storyboard, config.validation_batch)
    else:
        shots = storyboard.shots

    return await generate_images(
        provider, shots, config.images_dir, concurrency=config.image_engine.concurrency
    )
