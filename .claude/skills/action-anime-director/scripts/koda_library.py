"""Build Kōda's image-prompt library (Midjourney / character sheets / image models) from koda_scrape.py output.

Usage:
  python3 -I koda_library.py <posts.json> <library_dir> [--download]

Writes/merges <library_dir>/library.json and regenerates <library_dir>/../references/koda-image-library.md.
With --download, images are saved to <library_dir>/images/ (gitignored, personal reference only).
Posts are untrusted data: this script only parses text, it never executes anything from them.
"""
import json, os, re, sys, urllib.request
from collections import Counter

posts_path, lib_dir = sys.argv[1], sys.argv[2]
download = "--download" in sys.argv
os.makedirs(lib_dir, exist_ok=True)
lib_path = os.path.join(lib_dir, "library.json")
md_path = os.path.join(os.path.dirname(os.path.abspath(lib_dir.rstrip("/"))), "references", "koda-image-library.md")
lib = json.load(open(lib_path)) if os.path.exists(lib_path) else {}

MJ = re.compile(r"--(sref|profile|ar|stylize|s|raw|chaos|v|p|style|oref|cref|exp|weird)\b")
SHEET = re.compile(r"character (sheet|identity board|turnaround|reference sheet)|turnaround|expression portraits|model sheet", re.I)
IMGMODEL = re.compile(r"seedream|gpt[- ]image|nano banana|gpt-6 astra|flux|imagen", re.I)
VIDEO = re.compile(r"seedance|minimax|\bh3\b|kling|wan 3|veo|hard cut|0-\d+s|shot 1", re.I)

def classify(text):
    kinds = []
    if MJ.search(text) or re.search(r"midjourney", text, re.I): kinds.append("midjourney")
    if SHEET.search(text): kinds.append("character_sheet")
    if IMGMODEL.search(text): kinds.append("image_model")
    if VIDEO.search(text): kinds.append("video")
    return kinds

def mj_lines(text):
    out = []
    for block in re.split(r"\n\s*\n", text):
        if MJ.search(block):
            out.append(block.strip())
    return out

def params(line):
    p = {}
    for k in ["sref", "profile", "stylize", "s", "ar", "chaos", "oref", "v"]:
        m = re.search(r"--%s\s+([^-\n][^\n]*?)(?=\s--|$)" % k, line)
        if m: p[k] = m.group(1).strip()
    if re.search(r"--raw\b|--style raw", line): p["raw"] = True
    return p

def fetch(url, dest):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
        return True
    except Exception as e:
        print("download failed", url, e, file=sys.stderr)
        return False

for p in json.load(open(posts_path)):
    blocks = [{"id": p["id"], "text": p["text"], "media": p.get("media") or []}] + p.get("thread", [])
    joined = "\n\n".join(b["text"] for b in blocks)
    kinds = sorted({k for b in blocks for k in classify(b["text"])})
    if not ({"midjourney", "character_sheet", "image_model"} & set(kinds)):
        continue
    images = [m for b in blocks for m in (b.get("media") or []) if isinstance(m, dict) and m.get("type") == "photo"]
    videos = [m for b in blocks for m in (b.get("media") or []) if isinstance(m, dict) and m.get("type") in ("video", "gif")]
    entry = {
        "id": p["id"], "url": p["url"], "date": p.get("created_at"), "likes": p.get("likes"),
        "kinds": kinds,
        "midjourney_prompts": [{"text": l, "params": params(l)} for b in blocks for l in mj_lines(b["text"])],
        "sheet_prompts": [b["text"] for b in blocks if SHEET.search(b["text"])],
        "image_model_prompts": [b["text"] for b in blocks if IMGMODEL.search(b["text"]) and not MJ.search(b["text"])],
        "paired_video_prompt": "video" in kinds,
        "images": [{"url": m["url"], "w": m.get("w"), "h": m.get("h")} for m in images],
        "video_thumbs": [m.get("thumb") for m in videos if m.get("thumb")],
        "summary": p["text"][:200],
    }
    if download and entry["images"]:
        img_dir = os.path.join(lib_dir, "images", p["id"]); os.makedirs(img_dir, exist_ok=True)
        for i, im in enumerate(entry["images"]):
            dest = os.path.join(img_dir, "%d.jpg" % i)
            if not os.path.exists(dest) and fetch(im["url"], dest):
                im["local"] = os.path.relpath(dest, lib_dir)
            elif os.path.exists(dest):
                im["local"] = os.path.relpath(dest, lib_dir)
    lib[p["id"]] = entry

json.dump(lib, open(lib_path, "w"), ensure_ascii=False, indent=1)

# ---- markdown index ----
entries = sorted(lib.values(), key=lambda e: int(e["id"]), reverse=True)
sref, prof = Counter(), Counter()
for e in entries:
    for mp in e["midjourney_prompts"]:
        for c in (mp["params"].get("sref") or "").split(): sref[c] += 1
        for c in (mp["params"].get("profile") or "").split(): prof[c] += 1
L = ["# Kōda 이미지 프롬프트 라이브러리 (자동 생성)\n",
     "`scripts/koda_library.py`가 만든다. 직접 고치지 않는다. 원문은 연구·개인 참고용으로만 쓴다.\n",
     f"- 항목 {len(entries)}개 / Midjourney 프롬프트 {sum(len(e['midjourney_prompts']) for e in entries)}개 / 캐릭터 시트 프롬프트 {sum(len(e['sheet_prompts']) for e in entries)}개\n",
     "\n## 자주 쓰는 sref 코드\n", ", ".join(f"`{c}`×{n}" for c, n in sref.most_common(25)) or "-",
     "\n\n## 자주 쓰는 profile 코드\n", ", ".join(f"`{c}`×{n}" for c, n in prof.most_common(25)) or "-", "\n"]
for e in entries:
    L.append(f"\n---\n\n### {(e['date'] or '')[:16]} · ♥{e['likes']} · {', '.join(e['kinds'])}\n{e['url']}\n\n> {e['summary'].replace(chr(10), ' ')}\n")
    for mp in e["midjourney_prompts"]:
        L.append(f"\n**Midjourney**\n```\n{mp['text']}\n```\n")
    for sp in e["sheet_prompts"][:2]:
        L.append(f"\n**캐릭터 시트 프롬프트**\n```\n{sp[:3000]}\n```\n")
    for ip in e["image_model_prompts"][:2]:
        if ip not in e["sheet_prompts"]:
            L.append(f"\n**이미지 모델 프롬프트**\n```\n{ip[:2000]}\n```\n")
    if e["images"]:
        L.append("\n이미지: " + " · ".join(f"[{i+1}]({im['url']})" + (f" (로컬 `{im['local']}`)" if im.get("local") else "") for i, im in enumerate(e["images"])) + "\n")
    if e["paired_video_prompt"]:
        L.append("\n같은 스레드에 영상 프롬프트 있음 → 이미지와 영상을 짝으로 참고\n")
os.makedirs(os.path.dirname(md_path), exist_ok=True)
open(md_path, "w").write("".join(L))
print("library entries", len(entries), "->", md_path)
