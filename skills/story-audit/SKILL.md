---
name: story-audit
description: >-
  Use when a user has a set of their own short-form videos (or scripts) with
  performance numbers and wants to know why the winners won and the losers
  lost. Compares scripts side by side to surface the small, hidden word and
  structure patterns (a single verb, a hook framing, a payoff position) that
  separate high- and low-view videos in that specific channel and niche.
  Triggers: "story audit", "audit my videos", "why did this video flop",
  "why did this one go viral and this didn't", "compare my scripts", "what's
  the difference between my best and worst videos", "find my winning
  pattern". Don't use for writing a new script from scratch, thumbnail
  critique, or paid-ad creative analytics.
---

# Story Audit

Paste in any set of videos — this skill tells you exactly why the winners won and
the losers lost. It is a **comparative diagnosis**, not a generic script review:
every finding must be a difference that shows up in the winners and is absent (or
inverted) in the losers, backed by quoted lines from both sides.

Origin: Kallaway's "Story Audit" method (content.game). He made 11 videos on the same
topic — best 650K views, worst 19 — and couldn't see the difference by reading them.
The audit found one verb: every hook that said *"turn Claude into X"* crushed; every
hook that said *"use Claude to do X"* flopped. Creators are too close to their own
writing to see patterns that small. That is the job of this skill.

Read `references/diagnostic-lenses.md` for the full set of lenses and what to quote
for each. Read `references/report-template.md` for the exact output format.

## Workflow

### G1 — Collect the set

Need **at least 4 videos, ideally 8–20**, with one number per video (views is the
default; use retention, shares or saves if the user cares about those). Same topic or
same format makes the comparison sharper — say so if the set is mixed.

Accept any of these inputs, in this order of preference:

1. **A social-data plugin/connector** (e.g. Sandcastles.ai, which the original method
   uses) — if a connector or MCP tool for the user's account is available, pull the
   videos, transcripts and stats from it. Search the tool list before assuming none.
2. **Video URLs** (TikTok / Reels / Shorts) — for TikTok, run
   `python3 scripts/fetch_tiktok.py <url> [<url> ...]` (from this skill's directory).
   It prints JSON with caption, views, likes, shares, comments, duration and the
   auto-transcript for each video. For other platforms, transcribe with whatever the
   kit has (e.g. faster-whisper via `youtube-edit-kit`) and ask for the view counts.
3. **Pasted scripts + numbers** — fine as is. Ask for the first 3 seconds verbatim if
   the scripts are paraphrased; the hook is where most gaps live.

Normalise each video to: `id · views (or chosen metric) · post date · duration ·
caption · full transcript`. Flag outliers in post date or account size that could
explain the gap on their own (a 2-year-old video vs one from last week), and keep them
in the set but caveat them.

### G2 — Split winners and losers

Sort by the metric. Winners = top third, losers = bottom third, middle third is used
only to confirm a pattern (it should sit in between). With fewer than 6 videos, use
top 2 vs bottom 2. State the split and the cut-off numbers before analysing.

If the metric gap between groups is small (< 2×), say the set may not have a real
signal and that any finding is weak.

### G3 — Diagnose

Go lens by lens through `references/diagnostic-lenses.md`, **starting with the hook
(first sentence)** and working down. For each lens, line up the winner lines and the
loser lines next to each other and look for a difference that is:

- **Consistent** — holds for most winners and most losers (report it as e.g. 5/6 vs 1/5)
- **Specific** — a word, phrase, structure or position you can point to, not a vibe
- **Actionable** — the user could change it in the next script

Hunt small. The highest-value finding is usually tiny: one verb, a "you" vs "I", a
number vs no number, the payoff at second 4 vs second 20. Reject findings that are
true of the whole set, and don't stretch a pattern that only one video shows.

Look for confounds before you conclude: topic, length, post time, trend audio,
whether a winner got an external push (stitch, repost). If a confound explains the gap
better than the script does, say so.

### G4 — Report

Use `references/report-template.md`. Lead with **the one pattern that explains the
most** (the "one verb" finding), then up to 4 supporting patterns ranked by strength,
each with quoted evidence from both sides and a hit rate. End with a rewrite: take the
user's worst video's hook and rewrite it using the winning pattern, plus 3 rules to
follow in the next scripts.

Never invent quotes, views or transcripts. If a transcript is missing or auto-captions
look garbled, say which video and what you couldn't check.

### G5 — Save the patterns (optional)

Offer to save the findings as a short "channel pattern sheet" (markdown) the user can
paste into future scriptwriting prompts. Every channel and niche has its own hidden
patterns — the sheet is the point of running the audit, so re-run it as new videos
come in and update the sheet rather than starting over.
