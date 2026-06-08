"""Run manifest — records what each stage produced so runs are resumable.

A long render (90 clips in the background) must survive interruption. Each stage
appends to the manifest; re-running a stage can skip work that is already done.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Manifest:
    """A small JSON-backed record of stage outputs and approvals."""

    def __init__(self, path: Path, data: dict[str, Any] | None = None) -> None:
        self.path = path
        self.data: dict[str, Any] = data or {"stages": {}, "history": []}

    @classmethod
    def load(cls, path: Path) -> "Manifest":
        if path.exists():
            return cls(path, json.loads(path.read_text(encoding="utf-8")))
        return cls(path)

    def record_stage(self, stage: str, info: dict[str, Any]) -> None:
        """Store the outcome of a stage and append a timestamped history entry."""

        entry = {**info, "completed_at": datetime.now(timezone.utc).isoformat()}
        self.data["stages"][stage] = entry
        self.data["history"].append({"stage": stage, **entry})

    def stage(self, stage: str) -> dict[str, Any] | None:
        return self.data["stages"].get(stage)

    def is_done(self, stage: str) -> bool:
        return stage in self.data["stages"]

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")
