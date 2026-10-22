---
name: cinematic-vlog-edit
description: >-
  Use when a user wants a cinematic, aesthetic vlog or lifestyle / creator
  video that is simple and fast to edit — a shot-sequence hook (several
  same-length clips of one action stitched in motion), sound design on
  every action, music chosen BEFORE filming by BPM and dips, and a quick
  colour pass (light, practicals, colourful props, one-click grade). Also
  plans a 3-chapter story with 2–3 songs. Triggers: "cinematic vlog",
  "make my vlog cinematic", "shot sequence", "edit like Andrew / Casey
  Neistat / Sam Kolder style", "simple cinematic editing", "pick music for
  my video", "find the BPM / drops of this song". Expensive-looking
  motion/text edits are expensive-edit; retention planning for talking-head
  YouTube is addictive-editing.
---

# Cinematic Vlog Edit

From Andrew's "The Power of SIMPLE Editing" (1.2M views, 5 min). There are only three
edits, plus the finishing colour grade, and **less is more**. You don't need
never-seen-before creativity. You need a tight sequence, sound under every action,
music that sets the rhythm, and a clean grade.

Read `references/andrew-method.md` for the full method, the SFX list and the style
notes.

## The method

1. **Shot sequence (the hook).** Film several clips of *one action*, for example the
   morning routine: drawer → toothbrush → shirt → sitting down. Cut them all to the
   **same length** and stitch them so the motion flows from one into the next. It
   moves the story forward fast *and* works as the hook.
   `scripts/shot_sequence.py` trims the clips to equal length (or to a number of
   beats at the song's BPM) and joins them.
2. **Sound design.** Visuals are only half the picture. Every action gets a sound:
   risers into the sequence, air-passing whooshes on whip moves, foley on hands and
   objects. Andrew labels the SFX names on screen ("flute riser", "air passing").
3. **Music: choose it before you film.** Music is the backbone. It sets rhythm, pace,
   emotion and story. Skip lo-fi (stale and overused). Use jazz, house or cinematic
   instead. Check the **BPM** to know the pace you're shooting for, and find the
   **dips** in the song so scene changes land naturally on them, instead of cutting
   the music up unnaturally. `scripts/music_scout.py` estimates the BPM and lists the
   dips.
4. **Colour, "the flavour".** Editing is like baking bread: colour grading is the
   flavour you add once it's baked, and it is what stops the scroll.
   - **On set:** add light (more light, more information), place small practical
     lights in the background for pop, and frame in colourful objects.
   - **In the edit:** one consistent grade, applied with one click (a LUT /
     preset). For a quick look, `../expensive-edit/scripts/finish.py --look film`.

## Workflow

1. **Plan (before filming).** Turn the idea into **3 chapters**. Give each chapter a
   visual sequence and pair the video with **2–3 songs**. Pick the songs first, run
   `music_scout.py` on each, and write the shot list to fit the BPM, e.g. 4 beats per
   clip at 120 BPM = 2 s clips. Say where each dip will carry a scene change.
2. **Edit.** Build the opening shot sequence with `shot_sequence.py` (synced to the
   song with `--bpm` and `--beats`). Lay the music and cut scene changes on the dips.
   Add SFX to every action. Then grade.
3. **Close.** End by talking about the process, so the audience feels part of the
   creative process. Andrew's retention line: "if you made it this far you're part of
   the 20 % — comment that you're the 20 %."
4. Hand off captions and the final render to `youtube-edit-kit`. Get the user's OK
   before the final render.
