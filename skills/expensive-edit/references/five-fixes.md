# The five fixes — rules and checks

Source: NaughtyyJuan, "Make Your Edits Look EXPENSIVE (Simple Tricks)"
(youtu.be/i_G9pE89jD8, Feb 2025). Paraphrased. The checks and concrete values are
agent heuristics built on his rules.

## 0. Editor's bias

- **Symptom:** you think it's fire; others say "yeah it's cool".
- **Cause:** you value the effort, and the viewer only sees the result. People who
  never notice this keep making the same cheap edits forever.
- **Check:** watch it cold, at normal speed, on a phone. Note the first moment you'd
  scroll.

## 1. Quality over quantity

- An edit packed with effects does more harm than good. It reads as "made in
  PowerPoint" next to a "million-dollar ad".
- The Apple benchmark: no explosions, no flying 3D text. Clean visuals and intentional
  motion.
- **Checks:**
  - More than one "look" effect (glitch, shake, RGB split, lens flare) in the same
    5-second window → cut down to one.
  - Any effect you can't justify in one sentence → remove it.
  - Lots of different transition types → pick 1–2 and reuse them.

## 2. Fonts

- The wrong font cheapens everything, and the right one polishes it instantly.
- **Rules:**
  - At most 2 families. Pair a display face with a neutral sans.
  - Good, safe choices: Inter / SF Pro / Helvetica Now / Neue Montreal for sans; a
    high-contrast serif (Playfair Display, Editorial New, Instrument Serif) or a
    condensed bold (Bebas Neue, Druk-style) for titles.
  - Avoid: Comic Sans, Papyrus, Impact, default Arial or Times, script fonts used for
    body text, and outline-plus-drop-shadow stacks.
  - Generous letter spacing on small caps labels. Tight tracking on big titles.
  - Small, lowercase, centred captions look more premium than big yellow captions.

## 3. Colour and visual polish

- A flat, lifeless image looks like a school project. A graded one looks like a film.
- **For camera / film footage:** an adjustment layer for brightness, contrast and
  colour balance. Then subtle film grain, halation (a red-orange bloom around
  highlights) and an optional texture overlay (dust, light leak) at low opacity.
- **For transition / motion edits:** a little glow, an S-curve and sharpen. It's less
  about grading and more about making the visuals pop.
- **ffmpeg equivalents** (used by `scripts/finish.py`):
  - S-curve: `curves=master='0/0 0.25/0.20 0.5/0.5 0.75/0.82 1/1'`
  - Glow / halation: blur a copy of the highlights and screen-blend it at 15–30 %
  - Sharpen: `unsharp=5:5:0.6`
  - Grain: `noise=alls=6:allf=t`
  - Vignette: `vignette=PI/8` (subtle; PI/5 is already heavy)

## 4. Sound design

- An edit without SFX misses much of its impact. Compare the same clip with and
  without them.
- **Map:**
  - Movement → whoosh or swish, timed to the peak velocity of the move.
  - Impact (a logo landing, a hard cut on the beat) → bass hit or sub boom.
  - UI movement (a cursor, a card, a toggle) → subtle click or tick.
  - Text appearing → soft swish or pop. Plain kinetic type still needs it.
- Keep SFX under the music and voice. Small sounds matter; they add up to
  "immersive".

## 5. Smooth motion

- Weird, choppy or stiff movement is linear keyframes.
- **Fix:** easy ease on every keyframe, then use the graph editor (speed graph) to
  build a steep start and a long tail. The final pose should settle, not stop dead.
- **Code mapping:**
  - Entries: `expo.out` / `power3.out`, 0.5–0.8 s.
  - Exits: `power2.in`, 0.3–0.5 s.
  - Repositions: `power2.inOut`.
  - Motion blur on fast moves if the tool supports it.
