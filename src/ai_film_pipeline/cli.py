"""Command-line interface for the AI film pipeline.

Subcommands map one-to-one to stages so the recommended semi-automated workflow —
run a stage, review the output, then run the next — is the default. The `run`
subcommand chains everything for when prompts are already trusted.

Every stage supports --dry-run, which uses offline stubs (no API keys, no network)
so the whole pipeline is runnable for learning and testing.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from . import pipeline
from .config import PipelineConfig, load_config
from .manifest import Manifest


def _config(args: argparse.Namespace) -> PipelineConfig:
    config = load_config(args.config)
    if getattr(args, "dry_run", False):
        # dry_run is frozen; rebuild with the flag toggled on.
        from dataclasses import replace

        config = replace(config, dry_run=True)
    return config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run an AI film pipeline stage by stage.")
    parser.add_argument("--config", type=Path, default=Path("film.config.json"), help="Path to pipeline JSON config.")
    parser.add_argument("--dry-run", action="store_true", help="Use offline stubs; no API keys or network needed.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ref = sub.add_parser("reference", help="STEP 1: download reference + extract frames")
    p_ref.add_argument("url", help="Reference video URL")
    p_ref.add_argument("--fps", type=int, default=None, help="Frame extraction rate (default from config)")

    p_plan = sub.add_parser("plan", help="STEP 2-3: generate brand brief + storyboard")
    p_plan.add_argument("--notes", default="", help="Reference analysis notes to feed the planner")
    p_plan.add_argument("--shots", type=int, default=30, help="Number of shots")

    p_img = sub.add_parser("image", help="STEP 4-5: generate images")
    p_img.add_argument("--validate", action="store_true", help="Only render the representative validation batch")

    sub.add_parser("video", help="STEP 6-7: animate shots across all engines")

    p_asm = sub.add_parser("assemble", help="Assemble final film for one engine")
    p_asm.add_argument("--engine", required=True, help="Engine name to assemble")

    p_run = sub.add_parser("run", help="Run all stages end to end")
    p_run.add_argument("url", help="Reference video URL")
    p_run.add_argument("--notes", default="", help="Reference analysis notes")
    p_run.add_argument("--shots", type=int, default=30, help="Number of shots")

    sub.add_parser("status", help="Print the run manifest")
    return parser


def _cmd_status(config: PipelineConfig) -> int:
    manifest = Manifest.load(config.manifest_path)
    print(json.dumps(manifest.data, ensure_ascii=False, indent=2))
    return 0


def main() -> None:
    args = build_parser().parse_args()
    config = _config(args)

    if args.command == "reference":
        frames = pipeline.stage_reference(config, args.url, fps=args.fps)
        print(f"Extracted {len(frames)} frames to {config.frames_dir}")
    elif args.command == "plan":
        storyboard = pipeline.stage_plan(config, args.notes, shot_count=args.shots)
        print(f"Wrote {len(storyboard.shots)}-shot storyboard to {config.storyboard_path}")
    elif args.command == "image":
        storyboard = asyncio.run(pipeline.stage_image(config, validation_only=args.validate))
        done = sum(1 for s in storyboard.shots if s.image_path)
        scope = "validation batch" if args.validate else "all shots"
        print(f"Generated images ({scope}); {done} shots now have images. Review before continuing.")
    elif args.command == "video":
        storyboard = asyncio.run(pipeline.stage_video(config))
        print(f"Animated shots across {len(config.video_engines)} engine(s) into {config.clips_dir}")
    elif args.command == "assemble":
        output = pipeline.stage_assemble(config, args.engine)
        print(f"Assembled final film: {output}")
    elif args.command == "run":
        output = asyncio.run(pipeline.run_full(config, args.url, args.notes, shot_count=args.shots))
        print(f"Pipeline complete: {output}")
    elif args.command == "status":
        raise SystemExit(_cmd_status(config))
    else:  # pragma: no cover - argparse enforces choices
        raise SystemExit(1)


if __name__ == "__main__":
    main()
