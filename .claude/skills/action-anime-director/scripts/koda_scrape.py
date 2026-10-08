import json, sys, time, urllib.request, urllib.parse, os
OUT = sys.argv[1]; MAXPAGES = int(sys.argv[2]) if len(sys.argv) > 2 else 15
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 * (i + 1)); err = e
    print("FAIL", url, err, file=sys.stderr); return None
statuses, cursor = [], None
for p in range(MAXPAGES):
    u = "https://api.fxtwitter.com/2/profile/aimikoda/statuses" + ("?cursor=" + urllib.parse.quote(cursor) if cursor else "")
    d = get(u)
    if not d or not d.get("results"): break
    statuses += d["results"]; cursor = (d.get("cursor") or {}).get("bottom")
    if not cursor: break
    time.sleep(1)
seen, posts = set(), []
for s in statuses:
    if s["id"] in seen: continue
    seen.add(s["id"])
    if (s.get("author") or {}).get("screen_name") != "aimikoda": continue
    entry = {"id": s["id"], "url": s["url"], "created_at": s.get("created_at"), "likes": s.get("likes"),
             "text": s.get("text", ""), "media": [m.get("type") for m in ((s.get("media") or {}).get("all") or [])], "thread": []}
    t = s.get("text", "").lower()
    if any(k in t for k in ["prompt", "seedance", "kling", "midjourney", "veo", "workflow", "sref"]):
        th = get("https://api.fxtwitter.com/2/thread/" + s["id"])
        if th:
            for x in th.get("thread") or []:
                if (x.get("author") or {}).get("screen_name") == "aimikoda" and x["id"] != s["id"]:
                    entry["thread"].append({"id": x["id"], "text": x.get("text", "")})
        time.sleep(1)
    posts.append(entry)
json.dump(posts, open(OUT, "w"), ensure_ascii=False, indent=1)
print("statuses", len(statuses), "posts", len(posts), "with_thread", sum(1 for p in posts if p["thread"]))
if posts: print("range", posts[-1]["created_at"], "->", posts[0]["created_at"])
