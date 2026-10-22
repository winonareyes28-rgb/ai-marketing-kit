#!/usr/bin/env python3
"""Expensive finishing pass: S-curve, glow/halation, sharpen, grain, vignette.

Usage: python3 finish.py <in.mp4> <out.mp4> [--look film|pop] [--strength 1.0]
  film  camera footage: gentle S-curve, warm halation, grain, vignette
  pop   motion / transition edits: S-curve, white glow, sharpen, no grain
Audio is copied untouched. Requires ffmpeg.
"""
import argparse
import subprocess
import sys

LOOKS = {
    "film": {
        "curve": "0/0 0.25/0.21 0.5/0.5 0.75/0.80 1/0.97",
        "glow_color": "colorchannelmixer=rr=1:gg=0.55:bb=0.35",  # red-orange halation
        "glow_opacity": 0.22,
        "sharpen": "unsharp=5:5:0.3",
        "grain": 7,
        "vignette": "vignette=PI/8",
    },
    "pop": {
        "curve": "0/0 0.25/0.19 0.5/0.5 0.75/0.83 1/1",
        "glow_color": "null",
        "glow_opacity": 0.18,
        "sharpen": "unsharp=5:5:0.7",
        "grain": 0,
        "vignette": "vignette=PI/10",
    },
}


def build_filter(look, strength):
    p = LOOKS[look]
    glow = min(p["glow_opacity"] * strength, 0.6)
    grain = int(p["grain"] * strength)
    graph = (
        f"[0:v]curves=master='{p['curve']}',{p['sharpen']},split[base][hi];"
        # isolate highlights, blur them, then screen-blend back on for glow/halation
        f"[hi]curves=master='0/0 0.6/0 1/1',{p['glow_color']},gblur=sigma=18[glow];"
        f"[base][glow]blend=all_mode=screen:all_opacity={glow:.2f}"
    )
    if grain:
        graph += f",noise=alls={grain}:allf=t"
    graph += f",{p['vignette']},format=yuv420p[v]"
    return graph


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--look", choices=sorted(LOOKS), default="film")
    ap.add_argument("--strength", type=float, default=1.0,
                    help="scale glow and grain (0.5 subtle, 1.5 heavy)")
    args = ap.parse_args()

    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", args.src,
        "-filter_complex", build_filter(args.look, args.strength),
        "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18",
        "-preset", "medium", "-c:a", "copy", args.dst,
    ]
    print(f"Finishing {args.src} -> {args.dst} (look={args.look})", file=sys.stderr)
    sys.exit(subprocess.run(cmd).returncode)


if __name__ == "__main__":
    main()
