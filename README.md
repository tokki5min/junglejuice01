# Midjourney Prompt Collector

Midjourney의 Today / Week / Month 같은 트렌드 페이지에서 프롬프트 후보를 매일 수집하고, 날짜별 폴더에 Markdown, JSONL, 개별 `.txt` 파일로 정리하는 자동화 스캐폴드입니다.

> 주의: Midjourney 페이지 구조와 URL은 바뀔 수 있고, 로그인/접근 권한이 필요할 수 있습니다. 이 도구는 CAPTCHA 우회나 권한 없는 수집을 하지 않습니다. 사용 전 Midjourney 약관과 본인 계정의 접근 권한을 확인하세요.

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m playwright install chromium
```

## 설정

```bash
cp config.example.json config.json
```

`config.json`에서 다음을 조정합니다.

- `sources`: 수집할 페이지 이름과 URL
- `limit_per_source`: 소스별 최대 저장 개수
- `output_dir`: 결과 저장 폴더
- `storage_state`: Playwright 로그인 세션 파일 경로
- `card_selectors`, `text_selectors`: 페이지 구조가 바뀌었을 때 프롬프트 영역을 찾는 CSS selector

## 로그인 세션 준비

Midjourney가 로그인된 브라우저 세션을 요구한다면, 로컬에서 Playwright codegen으로 세션을 저장할 수 있습니다.

```bash
mkdir -p auth
python -m playwright codegen --save-storage=auth/midjourney-storage-state.json https://www.midjourney.com/explore
```

브라우저가 열리면 직접 로그인한 뒤 창을 닫습니다. 저장된 `auth/midjourney-storage-state.json`을 `config.json`의 `storage_state`로 지정하면 됩니다.

## 수동 실행

```bash
mj-prompt-collector --config config.json
```

실행 결과는 아래처럼 정리됩니다.

```text
collected-prompts/
  archive.jsonl
  2026-05-30/
    midjourney-trends.md
    prompts/
      001-<hash>.txt
      002-<hash>.txt
```

## 매일 1회 자동 실행

### macOS / Linux cron

```cron
0 9 * * * cd /path/to/repo && . .venv/bin/activate && mj-prompt-collector --config config.json >> collected-prompts/collector.log 2>&1
```

### systemd timer

`~/.config/systemd/user/mj-prompt-collector.service`

```ini
[Unit]
Description=Collect Midjourney trend prompts

[Service]
Type=oneshot
WorkingDirectory=/path/to/repo
ExecStart=/path/to/repo/.venv/bin/mj-prompt-collector --config /path/to/repo/config.json
```

`~/.config/systemd/user/mj-prompt-collector.timer`

```ini
[Unit]
Description=Run Midjourney prompt collector daily

[Timer]
OnCalendar=*-*-* 09:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

활성화:

```bash
systemctl --user daemon-reload
systemctl --user enable --now mj-prompt-collector.timer
```

## 테스트

```bash
python -m pytest
```
