# Tellsign

A dark, scroll-animated landing page about spotting and reporting online scams, with
three full-screen video "reels" that scrub frame-by-frame as you scroll.

## Features

- **Scroll-scrubbed video reels** (GSAP ScrollTrigger + Lenis smooth scroll). Each clip is
  pinned full-screen and plays as you scroll down, at a capped speed so it never races; the
  scroll slows over a reel but is never fully locked. Scrolling up rewinds instantly and
  resets everything by the top.
- **3D pointer-tilt cards** with a moving light sweep, animated multi-color glows, and
  gradient accents.
- **Quick check tool** that flags common scam "tells" in a pasted message, entirely client-side.
- Dark theme, one bright accent plus secondary brights, accessible reduced-motion fallbacks.

## Run it

Open `index.html` in a browser (it expects the `assets/` folder alongside it). It pulls
Tailwind, Phosphor icons, GSAP, and Lenis from CDNs, so an internet connection is needed.

## Single-file build

`Tellsign-standalone.html` is a self-contained copy with the three videos embedded as
base64, so it can be opened or shared as one file. Regenerate it after editing `index.html`:

```bash
python3 scripts/build_standalone.py
```

## Structure

```
index.html                  # the site
assets/                     # the three reel videos (all-keyframe, 720p, scrub-optimized)
scripts/build_standalone.py # bundles videos into Tellsign-standalone.html
Tellsign-standalone.html    # generated single-file build
```
