#!/usr/bin/env python3
"""Build a shot sequence: trim clips to the same length and stitch them.

Usage:
  python3 shot_sequence.py out.mp4 clip1.mp4 clip2.mp4 ... [--length 1.0]
  python3 shot_sequence.py out.mp4 clips... --bpm 120 --beats 2   # 2 beats per clip
  options: --start 0.5 (seconds into each clip to begin; or per-clip "clip.mp4@2.3")
           --music song.mp3 [--music-start 12.0]  lay a track under the sequence
           --size 1920x1080 --fps 30
Clips are scaled/cropped to one size so they concatenate cleanly. Requires ffmpeg.
"""
import argparse
import subprocess
import sys


def parse_clip(arg, default_start):
    path, sep, start = arg.rpartition("@")
    if sep and start.replace(".", "", 1).isdigit():
        return path, float(start)
    return arg, default_start


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("clips", nargs="+")
    ap.add_argument("--length", type=float, default=1.0, help="seconds per clip")
    ap.add_argument("--bpm", type=float, help="derive clip length from tempo")
    ap.add_argument("--beats", type=float, default=2, help="beats per clip with --bpm")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--music")
    ap.add_argument("--music-start", type=float, default=0.0)
    ap.add_argument("--size", default="1920x1080")
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    length = args.beats * 60.0 / args.bpm if args.bpm else args.length
    w, h = args.size.split("x")
    clips = [parse_clip(c, args.start) for c in args.clips]

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    for path, start in clips:
        cmd += ["-ss", f"{start:.3f}", "-t", f"{length:.3f}", "-i", path]
    if args.music:
        cmd += ["-ss", f"{args.music_start:.3f}", "-i", args.music]

    parts = []
    for i in range(len(clips)):
        parts.append(
            f"[{i}:v]scale={w}:{h}:force_original_aspect_ratio=increase,"
            f"crop={w}:{h},fps={args.fps},setsar=1,"
            f"trim=duration={length:.3f},setpts=PTS-STARTPTS[v{i}]"
        )
    joined = "".join(f"[v{i}]" for i in range(len(clips)))
    parts.append(f"{joined}concat=n={len(clips)}:v=1:a=0,format=yuv420p[v]")
    cmd += ["-filter_complex", ";".join(parts), "-map", "[v]"]

    total = length * len(clips)
    if args.music:
        cmd += ["-map", f"{len(clips)}:a", "-af", f"afade=t=out:st={max(total - 0.5, 0):.3f}:d=0.5",
                "-t", f"{total:.3f}", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-c:v", "libx264", "-crf", "18", "-preset", "medium", args.out]

    print(f"{len(clips)} clips x {length:.3f}s = {total:.2f}s -> {args.out}", file=sys.stderr)
    sys.exit(subprocess.run(cmd).returncode)


if __name__ == "__main__":
    main()
