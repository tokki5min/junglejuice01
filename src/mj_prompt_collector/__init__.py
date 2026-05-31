"""Midjourney prompt collector package."""

from .cli import PromptRecord, SourceConfig, extract_prompts_from_html

__all__ = ["PromptRecord", "SourceConfig", "extract_prompts_from_html"]
