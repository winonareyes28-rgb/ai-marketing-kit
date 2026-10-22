# NaughtyyJuan — visual style guide

Observed from the storyboard frames of the source video (one sampled frame about
every 5 s, about 60 frames). This is the aesthetic layer only; the five fixes apply
to any style.

## Structure

- **Cold open on the pain:** short lowercase text cards ("bc u made it", "making the
  same") interleaved with moody B-roll, then the title card.
- **Title card:** gold serif caps ("MAKE YOUR EDITS LOOK") overlapped by a large
  italic script word ("*Expensive*") with a soft glow, on black. Small gold signature
  line below: "a video by naughtyyjuan".
- The talking points are mostly **text-led**: voiceover over B-roll and kinetic type,
  with almost no face-cam.

## Canvas and framing

- Alternates between three flat backgrounds: **black**, **pure white** and a **deep
  bottle green** (≈ `#1f4a33`). Each is a clean stage for one element.
- Clips are often shown as **floating rounded-corner cards** (≈ 16–24 px radius) on
  the white or green canvas, sometimes as 2–3 tiles side by side, or as a tilted 3D
  card for product shots.
- Full-bleed B-roll is moody and warm: macro details (a clock, a record needle, a
  typewriter, masks), low light, red/amber practicals, grain and halation.

## Typography

- Captions: small, lowercase, centred, white on dark or black on white, in a clean
  geometric sans. Usually 2–5 words ("expensive that feels?", "alr before we ju").
- Word swaps and mid-word reveals: a word types or wipes in ("sou|less").
- Emphasis callouts: bold caps with one word coloured ("**LINK** IN BIO" with LINK in
  red), or a heavy condensed word over a close-up ("WHAT?").
- Asides in italic with asterisks: "*act like this edit is trash*".

## Motion

- Ease-out entries everywhere. Smooth card slides and scale-ins. A 3D tilt drift on
  UI and phone mockups.
- He demos the graph editor himself (a steep ease-out curve). Motion is part of the
  brand.
- Before/after shown as a side-by-side card pair.

## Sound

- Swish on every caption entry, bass hits on title and impact beats, clicks on UI.
- A hip-hop track under the outro.

## HyperFrames build notes

- Tokens: `--bg-black: #000`, `--bg-white: #fff`, `--bg-green: #1f4a33`,
  `--gold: #e8b04a`, `--accent-red: #e0342b`.
- Cards: `border-radius: 20px; overflow: hidden`, a soft shadow on white only.
- Entries: GSAP `expo.out`, 0.6 s, from `y: 40, scale: 0.96, opacity: 0`. Cue a swish
  SFX at the same time.
