---
name: expensive-edit
description: >-
  Use when a user says their edit looks cheap, amateur, cluttered, flat or
  "like PowerPoint" and wants it to look expensive, premium, clean or
  Apple-like — for short-form edits, motion-design / text-animation edits,
  transition edits, promos and reels. Covers the cheap-edit audit (too many
  effects, wrong font, flat colour, no sound design, stiff motion), font
  pairing, an ffmpeg finishing pass (S-curve, glow, sharpen, grain,
  halation, vignette), sound design for motion and text, and easing.
  Triggers: "make my edit look expensive", "why does my edit look cheap",
  "make it look premium", "clean Apple style edit", "my edit looks
  amateur", "edit like NaughtyyJuan". Retention planning for long YouTube
  videos is addictive-editing; cinematic vlogs are cinematic-vlog-edit.
---

# Expensive Edit

From NaughtyyJuan's "Make Your Edits Look EXPENSIVE (Simple Tricks)" (1M views, 5
min). **Expensive edits aren't about doing more. They're about doing less, but
better.** Think of Apple ads: clean, simple visuals with intentional motion, and they
can be recreated in any software.

Read `references/five-fixes.md` for the rules and checks. Read
`references/juan-style-guide.md` when the user wants his look specifically.

## Step 0 — Beat the editor's bias

You made it, so you know how much effort went in. The viewer doesn't care about
that. "It's cool" from a friend means it isn't. Review the edit as a stranger would:
watch it once without stopping, then note every moment that feels busy, cheap, stiff
or silent. When auditing a user's edit, say what you saw plainly. Don't praise
effort.

## The five fixes (run as an audit, in this order)

1. **Quality over quantity.** For every effect, ask: *do I really need this, or am I
   adding it because I'm bored?* Cut anything that doesn't carry meaning.
2. **Fonts.** The wrong font is the fastest way to look cheap. Use at most 2
   families: one clean sans for body and captions, one display face (an elegant serif
   or a condensed bold) for titles. No novelty fonts and no default fonts.
3. **Colour and visual polish.** A flat image looks like a school project. Fix it in
   an adjustment layer: brightness, contrast, colour balance. Then add a little film
   grain, halation and an overlay. For transition / motion edits: glow, an S-curve
   and sharpen. The aim is better-looking visuals, not a heavy "grade".
   `scripts/finish.py` does this pass with ffmpeg.
4. **Sound design.** An edit with no SFX is missing most of its impact. Use whooshes
   on motion, bass hits on impact and subtle clicks on UI moves. Even plain text
   should get a soft swish as it appears; it tricks the brain into reading the edit
   as polished.
5. **Smooth motion.** Choppy, stiff movement comes from linear keyframes. Use easy
   ease, then shape the graph editor into a strong ease-out (fast start, long settle).
   In code (HyperFrames/GSAP), use `power3.out`/`expo.out` for entries and
   `power2.inOut` for moves. Never use linear, except for constant drifts.

## Workflow

1. **Get the edit**: a video file, a description, or a project to build.
2. **Audit** it with the five fixes. For each issue give the timestamp, what's cheap
   about it and the exact fix. Rank the issues by how much they cheapen the result;
   clutter and fonts usually come first.
3. **Apply** what can be automated:
   - Finishing pass: `python3 scripts/finish.py in.mp4 out.mp4 --look film|pop`
     (requires ffmpeg).
   - Captions, cuts and render → `youtube-edit-kit`. Motion/text animation builds →
     HyperFrames via `ad-video`, with the font and easing rules above.
   - SFX: name the type and where it goes (whoosh at 0:03 slide-in, bass hit at 0:07
     logo). Use the user's library and never invent file names.
4. **Show before/after** frames when you've changed the look, and get the user's OK
   before rendering the final.
