---
name: addictive-editing
description: >-
  Use when a user wants to plan, audit or improve the EDITING of a YouTube /
  long-form talking-head video for retention — what to show on screen at each
  beat, where to zoom, when to use captions, how to make cuts seamless, which
  sound effects and music moods to use — or wants the "Learn By Leo" editing
  look (dark grid canvas, tilted timeline motion graphics, pillar chapter
  cards, sparse keyword captions). Triggers: "make my editing more
  addictive", "retention editing", "edit plan for this script", "audit my
  editing", "why do people click off my video", "edit like Learn By Leo",
  "add sound design", "what b-roll should go here". The mechanical cut/caption
  render is youtube-edit-kit; short ads are ad-video.
---

# Addictive Editing

A four-pillar editing handbook, from Learn By Leo's "How to edit SO good your
viewers get addicted to your videos" (6M views, 14.5 min). It isn't a list of
tricks. Every choice is judged by one question: **does it serve the experience this
viewer came for, and does it keep their attention without confusing them?**

- Read `references/four-pillars.md` for the full rules, with Leo's reasoning.
- Read `references/leo-style-guide.md` only when the user wants his specific look.
- Read `references/edit-plan-template.md` for the output format.

## The four pillars (summary)

1. **The hard truth: match the viewer's desired experience.** "Hang-out" channels
   (e.g. Sam Sulek: 26 min, 17 cuts, ~90 s between cuts) win on authenticity.
   Entertainment channels (MrBeast) win on stimulation. Cutting every pause boosts
   entertainment but costs authenticity. Decide where the video sits before choosing
   any technique. Breaking the experience the viewer came for is the fastest way to
   lose them.
2. **Healthy variety of visuals.** A change on screen grabs attention. Rotate A-roll
   (short, for important lines said with confidence), B-roll (as much as possible)
   and motion graphics (for anything complex or "essential but boring"). Variety
   without clarity turns into visual mush, so never shorten shots just to shorten
   them. Use in-shot spice instead: slow scale/position/perspective moves, punch-in
   zooms on key lines, and overlays. Captions should be emphasis only, 3 words max
   on screen. To guide the eye on an image: animate the key text or area,
   darken/blur the surroundings, hue-shift (red = bad, yellow/green = good), add
   circles/arrows/underlines, or make the subject glow. Grade the image, add a
   vignette and subtle particles.
3. **Visual continuity.** The editing should be invisible. Nothing appears out of
   nowhere: it animates in, or a sound (shutter, pop) explains its arrival. Across a
   cut, the viewer's focus point must stay in the same place on screen. Use subtle
   full-screen transitions. Break continuity *on purpose* when you want to jolt the
   viewer.
4. **Immersive audio.** Sound design makes every visual hit a second sense. Use a
   whoosh on every movement and a highlight sound on every highlight. Use risers
   (tension, only before a real payoff), hits (release, emphasis) and drones
   (mystery, for dark moods), and don't overuse any of them. Map music by subject:
   split the video at topic changes and give each one a mood (anticipation,
   innovation, ...). Hard-stop the music to spotlight a moment. Fade it out to signal
   a segment ending. Sync the song's drops and pick-ups to topic shifts (problem →
   solution). Use stems to control layers.

## Workflow

### G1 — Get the material

Accept a script, a transcript, a finished video, or a description. For a video file,
transcribe it (reuse `youtube-edit-kit`'s faster-whisper step) and measure pacing:

```bash
python3 scripts/cut_pacing.py <video.mp4> [--threshold 0.3]
```

It reports the number of cuts, the average and median seconds between cuts, the
longest unchanged stretches (likely attention drops), and a per-minute cut histogram.
Requires ffmpeg.

### G2 — Pillar 1: classify the experience (ask if unclear)

Place the video on the **authenticity ↔ entertainment** spectrum from its niche,
format and audience: hang-out / vlog, education / explainer, or high-stimulation
entertainment. Set target pacing ranges from `references/four-pillars.md` §1 and
**state them to the user before planning**. Every later choice is checked against
this.

### G3 — Build the edit plan (or audit)

Go through the script beat by beat (one beat = one idea, usually 3–15 s). For each
beat, decide:

- **Visual:** A-roll / B-roll / motion graphic / screen recording, plus the in-shot
  spice (zoom, move, overlay, focus-guide technique). Any "essential but boring"
  explanation must become a motion graphic.
- **Entry/exit:** how each new element arrives (animation or sound) and where the eye
  is at the cut.
- **SFX:** whoosh / highlight / pop / shutter / riser → hit / drone.
- **Music:** the segment's mood, and where it stops, fades or drops.

For an **audit** of an existing edit, flag the same items as problems: long static
stretches with nothing changing, captions used as filler, jarring eye-line jumps at
cuts, elements popping in with no sound, risers with no payoff, music mood that
doesn't match the segment, and pacing outside the G2 targets.

Use `references/edit-plan-template.md`. Be concrete: name the exact line, the
timestamp and the technique. "Add more b-roll" is not a plan.

### G4 — Hand-off

- Mechanical cuts, captions, SRT, chapters → `youtube-edit-kit`.
- Motion-graphic beats (pillar cards, diagrams, animated stats) → build as HyperFrames
  compositions (see `ad-video` for the HyperFrames route), using
  `references/leo-style-guide.md` if the user wants the Leo look.
- Music and SFX sourcing → the user's library (Epidemic Sound, Envato, freesound.org,
  YouTube Audio Library). Never invent track names. Describe the mood and the search
  term instead (e.g. "anticipation", "innovative").

Don't render or publish anything without the user's go.
