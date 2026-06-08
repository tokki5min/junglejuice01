"""Assembly — stitch clips into the final film with ffmpeg.

Concatenates the chosen clips in storyboard order and overlays the endcard
typography with ffmpeg's drawtext (the tutorial's "글자는 코드로" rule — let code do
the lettering, not the image model, so logos don't break).
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from ..models import Storyboard


def _require_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("'ffmpeg' is required for assembly. Install it before running this stage.")


def write_concat_list(clip_paths: list[Path], list_path: Path) -> Path:
    """Write an ffmpeg concat demuxer list file."""

    list_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"file '{path.resolve()}'" for path in clip_paths]
    list_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return list_path


def collect_clips(storyboard: Storyboard, engine: str) -> list[Path]:
    """Gather clip paths for one engine in storyboard order, skipping missing ones."""

    clips: list[Path] = []
    for shot in storyboard.shots:
        path = shot.video_paths.get(engine)
        if path:
            clips.append(Path(path))
    return clips


def concat(clip_paths: list[Path], output: Path, *, dry_run: bool = False) -> Path:
    """Concatenate clips into a single file."""

    output.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        output.write_text("STUB final cut from:\n" + "\n".join(str(p) for p in clip_paths) + "\n", encoding="utf-8")
        return output
    _require_ffmpeg()
    list_path = write_concat_list(clip_paths, output.with_suffix(".txt"))
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_path), "-c", "copy", str(output)],
        check=True,
    )
    return output


def overlay_endcard(video: Path, brand_name: str, slogan: str, output: Path, *, dry_run: bool = False) -> Path:
    """Burn endcard typography over the final frames with ffmpeg drawtext."""

    if dry_run:
        output.write_text(f"STUB endcard: {brand_name} / {slogan} over {video}\n", encoding="utf-8")
        return output
    _require_ffmpeg()
    drawtext = (
        f"drawtext=text='{brand_name}':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=(h-text_h)/2-40,"
        f"drawtext=text='{slogan}':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=(h-text_h)/2+50"
    )
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(video), "-vf", drawtext, "-codec:a", "copy", str(output)],
        check=True,
    )
    return output


def run(storyboard: Storyboard, engine: str, output_dir: Path, *, dry_run: bool = False) -> Path:
    """Assemble the final film for one engine and overlay the endcard."""

    clips = collect_clips(storyboard, engine)
    if not clips:
        raise ValueError(f"No clips found for engine '{engine}'. Run the video stage first.")
    rough = concat(clips, output_dir / f"{engine}_rough.mp4", dry_run=dry_run)
    return overlay_endcard(
        rough, storyboard.brand.name, storyboard.brand.slogan,
        output_dir / f"{engine}_final.mp4", dry_run=dry_run,
    )
