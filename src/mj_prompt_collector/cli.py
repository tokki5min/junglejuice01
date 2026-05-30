"""Daily Midjourney trend prompt collector.

The collector is intentionally selector-driven because gallery/explore pages change
frequently. Configure URLs and selectors in JSON instead of editing code.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from html.parser import HTMLParser
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


DEFAULT_CARD_SELECTORS = [
    "[data-testid*='prompt']",
    "[class*='prompt']",
    "[class*='Prompt']",
    "article",
    "figure",
]
DEFAULT_TEXT_SELECTORS = [
    "[data-testid*='prompt']",
    "[class*='prompt']",
    "[class*='Prompt']",
    "figcaption",
    "p",
]
PROMPT_HINT_ATTRIBUTES = ("aria-label", "title", "alt")
PROMPT_HINT_TAGS = {"article", "figure", "figcaption", "p"}
SELECTOR_SUBSTRING_RE = re.compile(r"\[(?P<attr>class|data-testid)\*=\s*[\"'](?P<value>[^\"']+)[\"']\]")
MIN_PROMPT_LENGTH = 24


@dataclass(frozen=True)
class SourceConfig:
    """Configuration for a single trend source page."""

    name: str
    url: str
    card_selectors: list[str] = field(default_factory=lambda: list(DEFAULT_CARD_SELECTORS))
    text_selectors: list[str] = field(default_factory=lambda: list(DEFAULT_TEXT_SELECTORS))
    wait_for_selector: str | None = None


@dataclass(frozen=True)
class CollectorConfig:
    """Configuration for a collector run."""

    sources: list[SourceConfig]
    output_dir: Path = Path("collected-prompts")
    limit_per_source: int = 50
    headless: bool = True
    storage_state: Path | None = None
    save_html: bool = False
    timezone: str = "UTC"


@dataclass(frozen=True)
class PromptRecord:
    """A normalized prompt discovered from a source."""

    prompt: str
    source_name: str
    source_url: str
    collected_at: str
    prompt_hash: str


def normalize_prompt(text: str) -> str:
    """Normalize page text into a stable prompt string."""

    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^(prompt|프롬프트)\s*[:：-]\s*", "", text, flags=re.IGNORECASE)
    return text.strip(" \t\n\r\"'")


def hash_prompt(prompt: str) -> str:
    """Return a short stable hash for deduplication and filenames."""

    return hashlib.sha256(prompt.lower().encode("utf-8")).hexdigest()[:16]


def load_config(path: Path) -> CollectorConfig:
    """Load collector JSON configuration."""

    raw = json.loads(path.read_text(encoding="utf-8"))
    sources = [
        SourceConfig(
            name=item["name"],
            url=item["url"],
            card_selectors=item.get("card_selectors", list(DEFAULT_CARD_SELECTORS)),
            text_selectors=item.get("text_selectors", list(DEFAULT_TEXT_SELECTORS)),
            wait_for_selector=item.get("wait_for_selector"),
        )
        for item in raw["sources"]
    ]
    storage_state = raw.get("storage_state")
    return CollectorConfig(
        sources=sources,
        output_dir=Path(raw.get("output_dir", "collected-prompts")),
        limit_per_source=int(raw.get("limit_per_source", 50)),
        headless=bool(raw.get("headless", True)),
        storage_state=Path(storage_state) if storage_state else None,
        save_html=bool(raw.get("save_html", False)),
        timezone=raw.get("timezone", "UTC"),
    )


class PromptHTMLParser(HTMLParser):
    """Small dependency-free parser that collects prompt-like text candidates."""

    def __init__(self, source: SourceConfig) -> None:
        super().__init__(convert_charrefs=True)
        selectors = [*source.card_selectors, *source.text_selectors]
        self.capture_tags = {selector.lower() for selector in selectors if selector.isidentifier()} | PROMPT_HINT_TAGS
        self.class_substrings = self._selector_values(selectors, "class") | {"prompt"}
        self.testid_substrings = self._selector_values(selectors, "data-testid") | {"prompt"}
        self.candidates: list[str] = []
        self._capture_stack: list[str] = []
        self._buffer: list[str] = []

    @staticmethod
    def _selector_values(selectors: list[str], attr: str) -> set[str]:
        return {
            match.group("value").lower()
            for selector in selectors
            for match in SELECTOR_SUBSTRING_RE.finditer(selector)
            if match.group("attr") == attr
        }

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name: value for name, value in attrs if value}
        for attr in PROMPT_HINT_ATTRIBUTES:
            value = attrs_dict.get(attr)
            if value:
                self.candidates.append(value)

        class_value = attrs_dict.get("class", "")
        data_testid = attrs_dict.get("data-testid", "")
        class_value = class_value.lower()
        data_testid = data_testid.lower()
        should_capture = (
            tag in self.capture_tags
            or any(value in class_value for value in self.class_substrings)
            or any(value in data_testid for value in self.testid_substrings)
        )
        if should_capture:
            self._capture_stack.append(tag)
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._capture_stack:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._capture_stack and self._capture_stack[-1] == tag:
            text = " ".join(self._buffer).strip()
            if text:
                self.candidates.append(text)
            self._capture_stack.pop()
            self._buffer = []


def extract_prompts_from_html(html: str, source: SourceConfig, collected_at: str) -> list[PromptRecord]:
    """Extract prompt-like text from saved or live HTML."""

    parser = PromptHTMLParser(source)
    parser.feed(html)

    seen: set[str] = set()
    records: list[PromptRecord] = []
    for candidate in parser.candidates:
        prompt = normalize_prompt(candidate)
        if len(prompt) < MIN_PROMPT_LENGTH:
            continue
        prompt_hash = hash_prompt(prompt)
        if prompt_hash in seen:
            continue
        seen.add(prompt_hash)
        records.append(
            PromptRecord(
                prompt=prompt,
                source_name=source.name,
                source_url=source.url,
                collected_at=collected_at,
                prompt_hash=prompt_hash,
            )
        )
    return records


async def collect_source(page: Any, source: SourceConfig, config: CollectorConfig, collected_at: str) -> list[PromptRecord]:
    """Open one configured source page and return extracted prompt records."""

    await page.goto(source.url, wait_until="networkidle")
    if source.wait_for_selector:
        await page.wait_for_selector(source.wait_for_selector, timeout=30_000)
    html = await page.content()
    if config.save_html:
        html_dir = config.output_dir / "html"
        html_dir.mkdir(parents=True, exist_ok=True)
        safe_name = re.sub(r"[^a-zA-Z0-9_.-]+", "-", source.name).strip("-") or "source"
        (html_dir / f"{safe_name}.html").write_text(html, encoding="utf-8")
    return extract_prompts_from_html(html, source, collected_at)[: config.limit_per_source]


async def collect(config: CollectorConfig) -> list[PromptRecord]:
    """Collect prompts from all configured sources."""

    from playwright.async_api import async_playwright

    collected_at = datetime.now(timezone.utc).isoformat()
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=config.headless)
        context_kwargs: dict[str, Any] = {}
        if config.storage_state:
            context_kwargs["storage_state"] = str(config.storage_state)
        context = await browser.new_context(**context_kwargs)
        page = await context.new_page()
        records: list[PromptRecord] = []
        for source in config.sources:
            records.extend(await collect_source(page, source, config, collected_at))
        await browser.close()
    return dedupe_records(records)


def dedupe_records(records: list[PromptRecord]) -> list[PromptRecord]:
    """Deduplicate records while preserving first-seen ordering."""

    seen: set[str] = set()
    deduped: list[PromptRecord] = []
    for record in records:
        if record.prompt_hash in seen:
            continue
        seen.add(record.prompt_hash)
        deduped.append(record)
    return deduped


def configured_timezone(timezone_name: str) -> ZoneInfo:
    """Resolve a configured timezone, defaulting safely to UTC."""

    try:
        return ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        return ZoneInfo("UTC")


def write_outputs(records: list[PromptRecord], output_dir: Path, timezone_name: str = "UTC") -> Path:
    """Write daily Markdown, JSONL archive, and individual prompt text files."""

    today = datetime.now(configured_timezone(timezone_name)).strftime("%Y-%m-%d")
    day_dir = output_dir / today
    prompt_dir = day_dir / "prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = day_dir / "midjourney-trends.md"
    lines = [f"# Midjourney trend prompts - {today}", ""]
    for index, record in enumerate(records, start=1):
        lines.extend(
            [
                f"## {index}. {record.source_name}",
                "",
                record.prompt,
                "",
                f"- Source: {record.source_url}",
                f"- Collected at: {record.collected_at}",
                f"- Hash: `{record.prompt_hash}`",
                "",
            ]
        )
        (prompt_dir / f"{index:03d}-{record.prompt_hash}.txt").write_text(record.prompt + "\n", encoding="utf-8")

    markdown_path.write_text("\n".join(lines), encoding="utf-8")

    archive_path = output_dir / "archive.jsonl"
    with archive_path.open("a", encoding="utf-8") as archive:
        for record in records:
            archive.write(json.dumps(record.__dict__, ensure_ascii=False) + "\n")

    return markdown_path


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""

    parser = argparse.ArgumentParser(description="Collect Midjourney trend prompts into dated folders.")
    parser.add_argument("--config", type=Path, default=Path("config.json"), help="Path to collector JSON config.")
    parser.add_argument("--dry-run", action="store_true", help="Print extracted prompts without writing files.")
    return parser


async def async_main(args: argparse.Namespace) -> int:
    """Run the collector CLI."""

    config = load_config(args.config)
    records = await collect(config)
    if args.dry_run:
        for record in records:
            print(f"[{record.source_name}] {record.prompt}")
        return 0
    output_path = write_outputs(records, config.output_dir, config.timezone)
    print(f"Wrote {len(records)} prompts to {output_path}")
    return 0


def main() -> None:
    """CLI entry point."""

    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(asyncio.run(async_main(args)))


if __name__ == "__main__":
    main()
