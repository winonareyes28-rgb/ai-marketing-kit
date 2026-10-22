#!/usr/bin/env python3
"""Measure cut pacing of a video with ffmpeg scene detection.

Usage: python3 cut_pacing.py <video> [--threshold 0.3] [--json]
Reports cut count, seconds between cuts, the longest static stretches and a
per-minute cut histogram. Status messages go to stderr.
"""
import argparse
import json
import re
import statistics
import subprocess
import sys


def duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def scene_cuts(path, threshold):
    print(f"Detecting cuts (threshold {threshold})...", file=sys.stderr)
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-an",
         "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        sys.exit(f"ffmpeg failed:\n{proc.stderr[-2000:]}")
    return [float(t) for t in re.findall(r"pts_time:([0-9.]+)", proc.stderr)]


def fmt(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--threshold", type=float, default=0.3,
                    help="scene change sensitivity 0-1 (lower = more cuts)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    total = duration(args.video)
    cuts = scene_cuts(args.video, args.threshold)
    bounds = [0.0] + cuts + [total]
    shots = [(bounds[i], bounds[i + 1] - bounds[i]) for i in range(len(bounds) - 1)]
    lengths = [s[1] for s in shots]
    per_minute = [0] * (int(total // 60) + 1)
    for c in cuts:
        per_minute[int(c // 60)] += 1

    report = {
        "duration_s": round(total, 1),
        "cuts": len(cuts),
        "avg_shot_s": round(statistics.mean(lengths), 2),
        "median_shot_s": round(statistics.median(lengths), 2),
        "longest_shots": [
            {"start": fmt(start), "length_s": round(length, 1)}
            for start, length in sorted(shots, key=lambda s: -s[1])[:5]
        ],
        "cuts_per_minute": per_minute,
    }
    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(f"Duration: {fmt(total)}  Cuts: {report['cuts']}  "
          f"Avg shot: {report['avg_shot_s']}s  Median: {report['median_shot_s']}s")
    print("Longest unchanged stretches (likely attention drops):")
    for s in report["longest_shots"]:
        print(f"  {s['start']}  {s['length_s']}s")
    print("Cuts per minute:")
    for m, n in enumerate(per_minute):
        print(f"  {m:>3}m {'#' * n} {n}")
    print("Note: in-shot moves (zooms, overlays) don't register as cuts; "
          "check long stretches by eye before calling them static.")


if __name__ == "__main__":
    main()
