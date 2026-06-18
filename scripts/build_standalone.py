#!/usr/bin/env python3
"""Bundle the reel videos into a single self-contained HTML file.

Reads index.html, replaces each `assets/*.mp4` reference with a base64 data URI,
and writes Tellsign-standalone.html next to it.
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
VIDEOS = ["exploding-view", "reel-2", "reel-3"]


def main() -> None:
    html = (ROOT / "index.html").read_text()
    for name in VIDEOS:
        data = (ROOT / "assets" / f"{name}.mp4").read_bytes()
        uri = "data:video/mp4;base64," + base64.b64encode(data).decode()
        html = html.replace(f"assets/{name}.mp4", uri)
    out = ROOT / "Tellsign-standalone.html"
    out.write_text(html)
    print(f"wrote {out} ({out.stat().st_size / 1_000_000:.1f} MB)")


if __name__ == "__main__":
    main()
