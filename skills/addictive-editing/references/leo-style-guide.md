# Learn By Leo — visual style guide

Observed from the storyboard frames of the source video (one sampled frame every
~5 s, 180 frames). Use this when the user wants "the Leo look". The four pillars
apply to any style; this file is only the aesthetic.

## Canvas

- **Dark charcoal grid background** (≈ `#1c1c1e`–`#232326` with faint grid lines at
  ≈ 4–6 % lighter, ~60 px cells). Almost every motion graphic sits on it, so it works
  as the video's "home" surface and keeps continuity between graphics.
- Slight vignette; cool, low-key lighting overall.

## A-roll

- Medium close-up, centred, in a dark room with **purple/blue ambient practical
  light** and a warm candle/lamp accent behind. Shallow depth of field, mic in frame.
- **Punch-in zooms** to a tight face crop on key lines; cut back out afterwards.
- Face-cam is a minority of screen time (≈ 25 % of sampled frames).

## Signature motion graphics

1. **Tilted 3D editor timelines.** Screen recordings of the Premiere timeline shown
   in perspective, with the camera drifting across them. Clips are colour-coded
   (pink/magenta, green, blue, yellow). Audio tracks are lit up as **glowing neon
   green/magenta bars**. Segments are tinted full-height (red = problem, green =
   solution) with labels.
2. **Pillar chapter cards.** White Greek columns rising from the grid, one per
   section, labelled "1.) THE HARD TRUTH", "2.) HEALTHY VARIETY OF VISUALS"… in italic
   bold caps. The same scene returns at each chapter with the next pillar raised.
   This works as a recurring progress motif.
3. **Cartoon viewer avatar.** A flat-shaded character ("the viewer") whose
   expression changes (neutral, smug, annoyed) to act out how the audience feels.
4. **Hand-drawn white squiggle maps.** Loose white strokes connecting small labels
   ("captions", "wiggle", "big zoom", "zoom/pan"), animated on, with the key words
   turning cyan.
5. **Generic UI icons.** A light-blue image placeholder, a "text" tile, a film-strip
   with scissors, a cursor clicking or dragging. Concepts are shown as simple UI
   objects.
6. **Real-world examples in context.** Screenshots of YouTube pages, analytics
   dashboards and other creators' clips, framed as the actual UI and hue-shifted
   red/green to judge them.
7. **Diagram metaphors.** A balance scale (ENTERTAINMENT vs AUTHENTICITY), an iceberg
   (sound effects above, music below), labelled A-ROLL / B-ROLL blocks.

## Typography

- **Headline:** bold geometric sans in ALL CAPS, white (Josefin Sans / Montserrat
  feel), large and centred, often with a soft glow or drop shadow. Examples:
  "ATTENTION", "MOTION GRAPHICS", "ENGAGEMENT SPICE".
- **Keyword colour:** one word recoloured to carry meaning: red for bad ("SLOW",
  "BORING", "CONFUSING", "obnoxious"), green or lime for good ("SUPERPOWER",
  "ESSENTIAL"). Red **strikethrough** over a rejected idea ("~~captions just~~ to
  jack up the visual variety", "~~distraction~~ ~~rough edges~~").
- **Captions:** sparse, lowercase or sentence case, white, centred on the grid or
  over footage. 1–3 words, or one short sentence on its own text card.
- Bullet lists appear line by line ("- MORE CLEAR", "- FASTER").

## Motion and sound pairing

- Every element enters with motion (slide, scale-up, draw-on) plus a whoosh or pop.
  Nothing hard-pops in silently.
- Slow perspective drift on every still and every timeline recording.
- Music plays as stacked stems on the timeline. Drops land on chapter or topic
  changes. The ending fades into a solid green end-screen frame.

## HyperFrames build notes

When building these beats as HyperFrames compositions (via the `ad-video` /
`hyperframes` route):
- Make the grid background one shared CSS layer so every scene uses the same canvas.
- Do the perspective-tilt moves with CSS `perspective` plus a GSAP-animated
  `rotateX/rotateY`, eased slow.
- Make keyword colours tokens: `--bad: #e5332a`, `--good: #4ade80`,
  `--accent: #22d3ee`, `--text: #ffffff`.
- Cue a whoosh or pop SFX at every element entry.
