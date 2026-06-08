"""STEP 2-3 — Planning: brand brief + 30-shot storyboard.

Claude proposes; the human decides. This stage asks the planner model to turn a
reference analysis into a brand brief and a storyboard with a narrative spine, then
writes a storyboard.json the human can edit before any pixels are generated.

In dry-run (or without ANTHROPIC_API_KEY) it emits a deterministic stub storyboard
so the rest of the pipeline is runnable offline.
"""

from __future__ import annotations

from ..config import PipelineConfig, require_env
from ..models import BrandBrief, Shot, Storyboard

PLANNER_SYSTEM = (
    "You are a commercial film director. Given a reference analysis, propose ONE brand brief "
    "and a storyboard of N shots. Every shot must advance a single narrative spine (a motif that "
    "threads the whole film) so the result reads as one piece, not unrelated pretty frames. "
    "Return strict JSON matching the Storyboard schema."
)


def build_planner_prompt(reference_notes: str, shot_count: int) -> str:
    """Build the user prompt sent to the planner model."""

    return (
        f"Reference analysis:\n{reference_notes}\n\n"
        f"Produce a brand brief (name, slogan, concept, look[]) and exactly {shot_count} shots. "
        f"Each shot needs: index, summary, prompt, act, motif. "
        f"Anchor every prompt to the look rules so the {shot_count} shots stay consistent."
    )


def _stub_storyboard(shot_count: int) -> Storyboard:
    """A deterministic offline storyboard so the pipeline runs without an API key."""

    brand = BrandBrief(
        name="BIOME",
        slogan="Life, restored.",
        concept="성분의 야생에서 피부의 재생까지 — 정수 한 방울의 여정.",
        look=["빠른 컷 리듬", "35mm 그레인", "더치/하이·로우 관능 구도", "촉각적 매크로"],
    )
    motif = "한 방울의 여정"
    acts = ["갈망", "야생", "포집", "재생"]
    shots = [
        Shot(
            index=i,
            summary=f"컷 {i} 플레이스홀더 설명",
            prompt=(
                f"BIOME brand film shot {i}, cinematic 35mm grain, dutch angle macro, "
                f"luxury skincare, single drop of essence motif, --ar 16:9"
            ),
            act=acts[min((i - 1) // 8, len(acts) - 1)],
            motif=motif,
        )
        for i in range(1, shot_count + 1)
    ]
    return Storyboard(brand=brand, shots=shots)


def run(
    config: PipelineConfig,
    reference_notes: str,
    *,
    shot_count: int = 30,
    dry_run: bool = False,
) -> Storyboard:
    """Generate (or stub) a storyboard and save it to config.storyboard_path."""

    if dry_run:
        storyboard = _stub_storyboard(shot_count)
    else:
        storyboard = _generate_with_claude(config, reference_notes, shot_count)
    storyboard.save(config.storyboard_path)
    return storyboard


def _generate_with_claude(config: PipelineConfig, reference_notes: str, shot_count: int) -> Storyboard:
    """Call the Claude API to produce a storyboard.

    Left as a clearly marked integration point: build the request from
    PLANNER_SYSTEM + build_planner_prompt, parse the JSON response into a
    Storyboard. Until wired, it falls back to the stub with a warning.
    """

    require_env("ANTHROPIC_API_KEY")
    raise NotImplementedError(
        "Wire _generate_with_claude to the Anthropic Messages API using PLANNER_SYSTEM and "
        "build_planner_prompt(), then parse the JSON reply via Storyboard.from_dict(). "
        "Run with --dry-run to use the offline stub storyboard."
    )
