"""AI film pipeline — a semi-automated reference→plan→image→video→assemble workflow.

The design principle, straight from the BIOME tutorial: the code owns the
repetition (concurrency, polling, post-processing) and the human owns the judgment
(which cut is good, which is on-brand). Stages are independent and each supports a
dry-run stub so the whole thing is runnable without API keys.
"""

from .config import EngineConfig, PipelineConfig, load_config
from .models import BrandBrief, Shot, Storyboard

__all__ = ["PipelineConfig", "EngineConfig", "load_config", "BrandBrief", "Shot", "Storyboard"]
