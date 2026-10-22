#!/usr/bin/env python3
"""Fetch caption, stats and auto-transcript for TikTok videos.

Usage: python3 fetch_tiktok.py <url> [<url> ...]
Prints a JSON list to stdout; status messages go to stderr.
Works with full URLs and vt.tiktok.com short links. No API key needed.
"""
import html
import json
import re
import sys
import urllib.request

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
DATA_RE = re.compile(
    r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',
    re.S,
)


def get(url, referer=None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.geturl(), resp.read().decode("utf-8", errors="ignore")


def vtt_to_text(vtt):
    lines = []
    for line in vtt.splitlines():
        line = line.strip()
        if not line or line == "WEBVTT" or "-->" in line or line.isdigit():
            continue
        lines.append(html.unescape(line))
    return " ".join(lines)


def fetch(url):
    final_url, page = get(url)
    match = DATA_RE.search(page)
    if not match:
        raise RuntimeError("no page data (TikTok may be blocking this request)")
    scope = json.loads(match.group(1))["__DEFAULT_SCOPE__"]
    item = scope.get("webapp.video-detail", {}).get("itemInfo", {}).get("itemStruct")
    if not item:
        raise RuntimeError("video data missing (private, deleted or region-locked)")

    transcript = None
    subs = item.get("video", {}).get("subtitleInfos") or []
    english = [s for s in subs if s.get("LanguageCodeName", "").startswith("eng")]
    for sub in english or subs:
        try:
            _, vtt = get(sub["Url"], referer="https://www.tiktok.com/")
            transcript = vtt_to_text(vtt)
            break
        except Exception as exc:  # try the next subtitle track
            print(f"  subtitle fetch failed: {exc}", file=sys.stderr)

    stats = item.get("statsV2") or item.get("stats") or {}
    return {
        "url": final_url.split("?")[0],
        "author": item.get("author", {}).get("uniqueId"),
        "create_time": item.get("createTime"),
        "duration_s": item.get("video", {}).get("duration"),
        "caption": item.get("desc"),
        "views": int(stats.get("playCount", 0)),
        "likes": int(stats.get("diggCount", 0)),
        "comments": int(stats.get("commentCount", 0)),
        "shares": int(stats.get("shareCount", 0)),
        "saves": int(stats.get("collectCount", 0)),
        "transcript": transcript,
    }


def main(urls):
    if not urls:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    results = []
    for url in urls:
        print(f"Fetching {url}", file=sys.stderr)
        try:
            results.append(fetch(url))
        except Exception as exc:
            print(f"  failed: {exc}", file=sys.stderr)
            results.append({"url": url, "error": str(exc)})
    json.dump(results, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main(sys.argv[1:])
