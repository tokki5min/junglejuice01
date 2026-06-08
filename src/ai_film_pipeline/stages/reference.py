"""STEP 1 — Reference dissection.

Download a reference video with yt-dlp and extract frames with ffmpeg at a high
rate (fps=4 -> one frame every 0.25s) so the editing rhythm becomes visible. The
human then reads the strip and names the rules (cut rhythm, grain, angles, macro)
that every downstream shot inherits.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def _require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise RuntimeError(f"'{name}' is not installed or not on PATH. Install it before running the reference stage.")


def download_reference(url: str, dest: Path, *, dry_run: bool = False) -> Path:
    """Download the reference video to `dest` using yt-dlp."""

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        dest.write_text(f"STUB reference video for {url}\n", encoding="utf-8")
        return dest
    _require_tool("yt-dlp")
    subprocess.run(
        ["yt-dlp", "-f", "mp4", "-o", str(dest), url],
        check=True,
    )
    return dest


def extract_frames(video: Path, frames_dir: Path, *, fps: int = 4, dry_run: bool = False) -> list[Path]:
    """Extract frames at `fps` frames/sec into `frames_dir`."""

    frames_dir.mkdir(parents=True, exist_ok=True)
    pattern = frames_dir / "frame_%05d.jpg"
    if dry_run:
        placeholder = frames_dir / "frame_00001.jpg"
        placeholder.write_text(f"STUB frame from {video} at fps={fps}\n", encoding="utf-8")
        return [placeholder]
    _require_tool("ffmpeg")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(video), "-vf", f"fps={fps}", str(pattern)],
        check=True,
    )
    return sorted(frames_dir.glob("frame_*.jpg"))


def run(url: str, video_path: Path, frames_dir: Path, *, fps: int = 4, dry_run: bool = False) -> list[Path]:
    """Download a reference and extract frames; returns the frame paths."""

    video = download_reference(url, video_path, dry_run=dry_run)
    return extract_frames(video, frames_dir, fps=fps, dry_run=dry_run)
