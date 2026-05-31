# Midjourney Prompt Collector

Midjourney의 Today / Week / Month 같은 트렌드 페이지에서 프롬프트 후보를 매일 수집하고, 날짜별 폴더에 Markdown, JSONL, 개별 `.txt` 파일로 정리하는 자동화 스캐폴드입니다.

> 주의: Midjourney 페이지 구조와 URL은 바뀔 수 있고, 로그인/접근 권한이 필요할 수 있습니다. 이 도구는 CAPTCHA 우회나 권한 없는 수집을 하지 않습니다. 사용 전 Midjourney 약관과 본인 계정의 접근 권한을 확인하세요.

## 먼저 확인할 것

설치 명령은 반드시 이 프로젝트 파일이 있는 폴더에서 실행해야 합니다. 터미널에서 아래 파일들이 보여야 정상입니다.

```text
README.md
pyproject.toml
config.example.json
src
tests
```

Windows PowerShell에서는 다음 명령으로 확인합니다.

```powershell
dir
```

macOS/Linux/Git Bash에서는 다음 명령으로 확인합니다.

```bash
ls
```

`pip install -e .` 실행 시 `does not appear to be a Python project`가 나오면 현재 폴더에 `pyproject.toml`이 없는 것입니다. 프로젝트 압축을 푼 실제 폴더로 이동한 뒤 다시 실행하세요.

## 설치 - Windows PowerShell

PowerShell에서는 README의 bash 명령인 `source .venv/bin/activate`를 쓰지 않습니다. 아래 순서대로 한 줄씩 실행하세요.

```powershell
cd C:\workspace\junglejuice01
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m playwright install chromium
copy config.example.json config.json
```

성공하면 프롬프트 앞에 `(.venv)`가 붙습니다.

```text
(.venv) PS C:\workspace\junglejuice01>
```

`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`는 현재 PowerShell 창에서만 임시로 스크립트 실행을 허용합니다. 새 PowerShell 창을 열면 다시 원래 정책으로 돌아갑니다.

### Windows PowerShell에서 자주 나는 오류

#### `source`가 인식되지 않음

`source .venv/bin/activate`는 macOS/Linux/Git Bash 명령입니다. PowerShell에서는 아래를 사용하세요.

```powershell
.\.venv\Scripts\Activate.ps1
```

#### `Activate.ps1 파일을 로드할 수 없습니다`

PowerShell 실행 정책이 가상환경 활성화 스크립트를 막은 것입니다. 현재 창에서만 임시 허용한 뒤 다시 활성화하세요.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

#### `(.venv) PS ...`를 직접 입력해서 `예기치 않은 'PS' 토큰` 오류가 남

`(.venv) PS C:\...>`는 입력하는 명령이 아니라 터미널이 보여주는 상태 표시입니다. 사용자는 `pip install -e .` 같은 명령만 입력하면 됩니다.

#### `does not appear to be a Python project` 오류가 남

현재 폴더에 `pyproject.toml`이 없다는 뜻입니다. 아래 명령으로 파일이 있는지 확인하세요.

```powershell
dir pyproject.toml
```

파일이 없으면 프로젝트 파일을 받은 위치로 이동해야 합니다. 예를 들어 다운로드 폴더에 있다면 다음처럼 이동합니다.

```powershell
cd $HOME\Downloads\junglejuice01
```

## 설치 - macOS / Linux / Git Bash

```bash
cd /path/to/junglejuice01
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m playwright install chromium
cp config.example.json config.json
```

## 설정

`config.json`에서 다음을 조정합니다.

- `sources`: 수집할 페이지 이름과 URL
- `limit_per_source`: 소스별 최대 저장 개수
- `output_dir`: 결과 저장 폴더
- `storage_state`: Playwright 로그인 세션 파일 경로
- `card_selectors`, `text_selectors`: 페이지 구조가 바뀌었을 때 프롬프트 영역을 찾는 CSS selector

## 로그인 세션 준비

Midjourney가 로그인된 브라우저 세션을 요구한다면, 로컬에서 Playwright codegen으로 세션을 저장할 수 있습니다.

### Windows PowerShell

```powershell
mkdir auth
python -m playwright codegen --save-storage=auth\midjourney-storage-state.json https://www.midjourney.com/explore
```

### macOS / Linux / Git Bash

```bash
mkdir -p auth
python -m playwright codegen --save-storage=auth/midjourney-storage-state.json https://www.midjourney.com/explore
```

브라우저가 열리면 직접 로그인한 뒤 창을 닫습니다. 저장된 `auth/midjourney-storage-state.json`을 `config.json`의 `storage_state`로 지정하면 됩니다.

## 수동 실행

가상환경이 켜진 상태에서 실행합니다.

```bash
mj-prompt-collector --config config.json
```

Windows에서 명령을 찾지 못하면 가상환경 안의 실행 파일을 직접 실행할 수 있습니다.

```powershell
.\.venv\Scripts\mj-prompt-collector.exe --config config.json
```

실행 결과는 아래처럼 정리됩니다.

```text
collected-prompts/
  archive.jsonl
  2026-05-31/
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
