"""Configuration loading for the AI film pipeline.

Like the prompt collector, configuration is JSON-driven so engines, concurrency
limits, and output locations can change without editing code. API keys are read
from the environment, never from the config file.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class EngineConfig:
    """A single generation engine (image or video).

    `provider` selects the adapter in `providers.py`. `concurrency` is the engine's
    own parallel-request ceiling (e.g. Higgsfield caps at 8 simultaneous jobs).
    `params` are passed through to the provider unchanged.
    """

    name: str
    provider: str
    model: str = ""
    concurrency: int = 4
    params: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EngineConfig":
        return cls(
            name=data["name"],
            provider=data["provider"],
            model=data.get("model", ""),
            concurrency=int(data.get("concurrency", 4)),
            params=dict(data.get("params", {})),
        )


@dataclass(frozen=True)
class PipelineConfig:
    """Top-level configuration for a pipeline run."""

    project: str
    output_dir: Path = Path("renders")
    storyboard_path: Path = Path("storyboard.json")
    fps_capture: int = 4
    validation_batch: int = 6
    image_engine: EngineConfig | None = None
    video_engines: list[EngineConfig] = field(default_factory=list)
    planner_model: str = "claude-sonnet-4-6"
    dry_run: bool = False

    @property
    def assets_dir(self) -> Path:
        return self.output_dir / "assets"

    @property
    def frames_dir(self) -> Path:
        return self.output_dir / "reference_frames"

    @property
    def images_dir(self) -> Path:
        return self.output_dir / "images"

    @property
    def clips_dir(self) -> Path:
        return self.output_dir / "clips"

    @property
    def manifest_path(self) -> Path:
        return self.output_dir / "manifest.json"


def load_config(path: Path) -> PipelineConfig:
    """Load pipeline JSON configuration."""

    raw = json.loads(path.read_text(encoding="utf-8"))
    image_engine = raw.get("image_engine")
    return PipelineConfig(
        project=raw.get("project", "untitled"),
        output_dir=Path(raw.get("output_dir", "renders")),
        storyboard_path=Path(raw.get("storyboard_path", "storyboard.json")),
        fps_capture=int(raw.get("fps_capture", 4)),
        validation_batch=int(raw.get("validation_batch", 6)),
        image_engine=EngineConfig.from_dict(image_engine) if image_engine else None,
        video_engines=[EngineConfig.from_dict(item) for item in raw.get("video_engines", [])],
        planner_model=raw.get("planner_model", "claude-sonnet-4-6"),
        dry_run=bool(raw.get("dry_run", False)),
    )


def require_env(name: str) -> str:
    """Read a required API key from the environment with a clear error."""

    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Environment variable {name} is not set. Export it before running this stage, "
            f"or pass --dry-run to use the offline stub."
        )
    return value
