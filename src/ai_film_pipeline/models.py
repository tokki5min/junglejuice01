"""Core data models for the AI film pipeline.

These mirror the artifacts in the BIOME tutorial: a brand brief, a storyboard of
shots, and the per-shot generation state that flows between stages.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


def slugify(text: str) -> str:
    """Return a filesystem-safe slug for filenames and directories."""

    slug = re.sub(r"[^a-zA-Z0-9_.-]+", "-", text.strip().lower()).strip("-")
    return slug or "untitled"


def short_hash(text: str) -> str:
    """Return a short stable hash for deduplication and filenames."""

    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


@dataclass(frozen=True)
class BrandBrief:
    """The locked creative decision a human makes before any generation.

    The tutorial's STEP 2: Claude proposes options, the human picks one. Once
    chosen, this brief becomes the design spec every downstream shot inherits.
    """

    name: str
    slogan: str
    concept: str
    look: list[str] = field(default_factory=list)
    reference_url: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BrandBrief":
        return cls(
            name=data["name"],
            slogan=data.get("slogan", ""),
            concept=data.get("concept", ""),
            look=list(data.get("look", [])),
            reference_url=data.get("reference_url"),
        )


@dataclass
class Shot:
    """A single cut in the storyboard.

    `prompt` is the generation prompt; `act` and `motif` carry the narrative
    spine ("한 방울의 여정") so the assembled film reads as one piece, not 30
    pretty screensaver frames.
    """

    index: int
    summary: str
    prompt: str
    act: str = ""
    motif: str = ""
    reference_image: str | None = None
    image_path: str | None = None
    video_paths: dict[str, str] = field(default_factory=dict)
    approved: bool = False

    @property
    def shot_id(self) -> str:
        return f"cut_{self.index:02d}"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Shot":
        return cls(
            index=int(data["index"]),
            summary=data.get("summary", ""),
            prompt=data["prompt"],
            act=data.get("act", ""),
            motif=data.get("motif", ""),
            reference_image=data.get("reference_image"),
            image_path=data.get("image_path"),
            video_paths=dict(data.get("video_paths", {})),
            approved=bool(data.get("approved", False)),
        )


@dataclass
class Storyboard:
    """An ordered set of shots plus the brand brief they serve."""

    brand: BrandBrief
    shots: list[Shot]
    aspect_ratio: str = "16:9"
    fps: int = 24

    def to_dict(self) -> dict[str, Any]:
        return {
            "brand": asdict(self.brand),
            "aspect_ratio": self.aspect_ratio,
            "fps": self.fps,
            "shots": [asdict(shot) for shot in self.shots],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Storyboard":
        return cls(
            brand=BrandBrief.from_dict(data["brand"]),
            shots=[Shot.from_dict(item) for item in data.get("shots", [])],
            aspect_ratio=data.get("aspect_ratio", "16:9"),
            fps=int(data.get("fps", 24)),
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "Storyboard":
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))
