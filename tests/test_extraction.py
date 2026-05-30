from mj_prompt_collector import SourceConfig, extract_prompts_from_html


def test_extracts_and_deduplicates_prompt_text() -> None:
    html = """
    <html>
      <body>
        <article>
          <p>Prompt: cinematic neon jungle temple, volumetric light, ultra detailed --ar 16:9</p>
        </article>
        <article>
          <p>cinematic neon jungle temple, volumetric light, ultra detailed --ar 16:9</p>
        </article>
        <img alt="editorial portrait of a glass robot in a rainy Seoul street, 35mm film" />
      </body>
    </html>
    """

    source = SourceConfig(name="top-today", url="https://example.test/top")
    records = extract_prompts_from_html(html, source, "2026-05-30T00:00:00+00:00")

    assert [record.prompt for record in records] == [
        "cinematic neon jungle temple, volumetric light, ultra detailed --ar 16:9",
        "editorial portrait of a glass robot in a rainy Seoul street, 35mm film",
    ]
    assert records[0].source_name == "top-today"


def test_ignores_short_ui_text() -> None:
    html = """
    <html>
      <body>
        <article><p>Like</p></article>
        <article><p>Copy prompt</p></article>
      </body>
    </html>
    """

    source = SourceConfig(name="top-week", url="https://example.test/week")

    assert extract_prompts_from_html(html, source, "2026-05-30T00:00:00+00:00") == []
