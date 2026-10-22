#!/usr/bin/env python3
"""Estimate a song's BPM and find its dips (natural scene-change points).

Usage: python3 music_scout.py <song.mp3|wav> [--dips 8] [--json]
BPM is an onset-autocorrelation estimate: double-check half/double tempo by ear.
A "dip" is a stretch where loudness drops well below the song's running level
(breakdowns, drop-outs, pre-drop gaps). Requires ffmpeg and numpy.
"""
import argparse
import json
import subprocess
import sys

import numpy as np

SR = 22050
HOP = 512


def load(path):
    raw = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path,
         "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, dtype=np.float32)


def frame_rms(x):
    n = len(x) // HOP
    frames = x[: n * HOP].reshape(n, HOP)
    return np.sqrt((frames ** 2).mean(axis=1) + 1e-12)


def estimate_bpm(x):
    # spectral-flux onset envelope, then autocorrelation over 70-180 BPM
    win = 2048
    n = (len(x) - win) // HOP
    if n < 10:
        return None
    idx = np.arange(win)[None, :] + HOP * np.arange(n)[:, None]
    spec = np.abs(np.fft.rfft(x[idx] * np.hanning(win), axis=1))
    flux = np.maximum(np.diff(np.log1p(spec), axis=0), 0).sum(axis=1)
    flux -= flux.mean()
    ac = np.correlate(flux, flux, mode="full")[len(flux) - 1:]
    fps = SR / HOP
    lags = np.arange(len(ac))
    bpm = 60.0 * fps / np.maximum(lags, 1)
    mask = (bpm >= 70) & (bpm <= 180)
    best = int(lags[mask][np.argmax(ac[mask])])
    # parabolic interpolation around the peak for sub-frame lag precision
    if 0 < best < len(ac) - 1:
        a, b, c = ac[best - 1], ac[best], ac[best + 1]
        denom = a - 2 * b + c
        if denom:
            best = best + 0.5 * (a - c) / denom
    return round(60.0 * fps / best, 1)


def moving_avg(v, k):
    # reflect padding so the song's start and end aren't mistaken for dips
    k = max(k, 1)
    padded = np.pad(v, (k // 2, k - 1 - k // 2), mode="reflect")
    return np.convolve(padded, np.ones(k) / k, mode="valid")


def find_dips(x, count):
    fps = SR / HOP
    db = 20 * np.log10(frame_rms(x))
    k = int(0.5 * fps)  # 0.5 s smoothing
    smooth = moving_avg(db, k)
    k8 = int(8 * fps)  # 8 s running level
    level = moving_avg(db, k8)
    drop = level - smooth
    edge = int(1.5 * fps)  # a "dip" at the very start/end is not a usable cut point
    drop[:edge] = 0
    drop[-edge:] = 0
    dips, min_gap = [], int(4 * fps)
    for j in np.argsort(-drop):
        if drop[j] < 6 or len(dips) >= count:
            break
        if all(abs(j - d) > min_gap for d in dips):
            dips.append(j)
    out = []
    for j in sorted(dips):
        t = j / fps
        out.append({"time": f"{int(t // 60)}:{t % 60:05.2f}", "seconds": round(t, 2),
                    "drop_db": round(float(drop[j]), 1)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("song")
    ap.add_argument("--dips", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    print(f"Analysing {args.song}...", file=sys.stderr)
    x = load(args.song)
    bpm = estimate_bpm(x)
    dips = find_dips(x, args.dips)
    report = {"duration_s": round(len(x) / SR, 1), "bpm_estimate": bpm, "dips": dips}
    if bpm:
        report["seconds_per_beat"] = round(60 / bpm, 3)
        report["seconds_per_bar_4_4"] = round(240 / bpm, 3)
    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(f"Duration {report['duration_s']}s · BPM ~{bpm} "
          f"(beat {report.get('seconds_per_beat')}s, bar {report.get('seconds_per_bar_4_4')}s)")
    print("Dips (cut scene changes here):")
    for d in dips:
        print(f"  {d['time']}  -{d['drop_db']} dB")


if __name__ == "__main__":
    main()
