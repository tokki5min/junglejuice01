"""Generation engine adapters.

Each provider wraps one external API (image or video). Every provider supports a
`dry_run` mode that writes a tiny placeholder file instead of calling the network,
so the whole pipeline can be exercised end-to-end without API keys. Replace the
`_generate_real` bodies with the actual HTTP calls for your accounts.

The async polling/concurrency logic lives in `concurrency.py`; providers only know
how to (a) start a job and (b) report whether it is done.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import EngineConfig, require_env


@dataclass
class GenerationJob:
    """The result of a single generation request."""

    output_path: Path
    engine: str
    meta: dict[str, Any]


class Provider:
    """Base class for image/video providers.

    Subclasses implement `_generate_real`. The base `generate` dispatches to either
    the real call or the offline stub based on `dry_run`.
    """

    kind = "generic"

    def __init__(self, engine: EngineConfig, *, dry_run: bool = False) -> None:
        self.engine = engine
        self.dry_run = dry_run

    async def generate(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if self.dry_run:
            return await self._generate_stub(prompt, output_path, **kwargs)
        return await self._generate_real(prompt, output_path, **kwargs)

    async def _generate_stub(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:
        """Write a placeholder describing the request that would have been made."""

        await asyncio.sleep(0)  # yield so concurrency is exercised even in stub mode
        payload = {
            "engine": self.engine.name,
            "provider": self.engine.provider,
            "model": self.engine.model,
            "prompt": prompt,
            "params": {**self.engine.params, **kwargs},
        }
        output_path.write_text(_describe(payload), encoding="utf-8")
        return GenerationJob(output_path=output_path, engine=self.engine.name, meta={"stub": True})

    async def _generate_real(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:  # noqa: ARG002
        raise NotImplementedError(
            f"{type(self).__name__} has no real implementation yet. "
            f"Fill in _generate_real or run with --dry-run."
        )


class OpenAIImageProvider(Provider):
    """gpt-image-2 style image generation.

    Real implementation should POST to the images endpoint with `input_fidelity:
    high` and a `reference_image` when locking identity (the tutorial's fix for the
    인물 일관성 problem).
    """

    kind = "image"

    async def _generate_real(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:
        api_key = require_env("OPENAI_API_KEY")  # noqa: F841 — used by the real HTTP call
        raise NotImplementedError(
            "Wire OpenAIImageProvider._generate_real to the images API: submit the prompt "
            "(plus reference_image/input_fidelity for identity lock), then save bytes to output_path."
        )


class ReplicateVideoProvider(Provider):
    """Replicate-hosted video engines (e.g. Kling v2.5).

    Replicate returns a prediction you poll; use concurrency.poll_until for that.
    """

    kind = "video"

    async def _generate_real(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:
        api_key = require_env("REPLICATE_API_TOKEN")  # noqa: F841
        raise NotImplementedError(
            "Wire ReplicateVideoProvider._generate_real: create a prediction, poll_until it "
            "succeeds, download the mp4 to output_path. Prepend 'no music' to the prompt."
        )


class HiggsfieldVideoProvider(Provider):
    """Higgsfield Seedance 2.0 — generates diegetic SFX automatically.

    Remember the 1080p trap: pass resolution explicitly or it silently drops to 720p.
    """

    kind = "video"

    async def _generate_real(self, prompt: str, output_path: Path, **kwargs: Any) -> GenerationJob:
        api_key = require_env("HIGGSFIELD_API_KEY")  # noqa: F841
        raise NotImplementedError(
            "Wire HiggsfieldVideoProvider._generate_real: submit with resolution=1080p, poll, "
            "download to output_path."
        )


_PROVIDERS: dict[str, type[Provider]] = {
    "openai-image": OpenAIImageProvider,
    "replicate-video": ReplicateVideoProvider,
    "higgsfield-video": HiggsfieldVideoProvider,
}


def build_provider(engine: EngineConfig, *, dry_run: bool = False) -> Provider:
    """Instantiate the provider adapter named by an engine config."""

    try:
        provider_cls = _PROVIDERS[engine.provider]
    except KeyError as exc:
        known = ", ".join(sorted(_PROVIDERS))
        raise ValueError(f"Unknown provider '{engine.provider}'. Known providers: {known}") from exc
    return provider_cls(engine, dry_run=dry_run)


def _describe(payload: dict[str, Any]) -> str:
    import json

    return "STUB GENERATION\n" + json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
