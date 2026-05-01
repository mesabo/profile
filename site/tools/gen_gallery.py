#!/usr/bin/env python3
"""
Auto-generate the photo gallery in other.jemdoc.

Scans assets/photos/<trip>/ for image files, then replaces everything
between the GALLERY-START / GALLERY-END markers in other.jemdoc with
freshly-rendered <section> blocks.

Trip metadata (title, date, order) lives in assets/photos/_trips.json.
Anything found in assets/photos/ that is NOT in the JSON is appended
at the end with a placeholder title.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
PHOTOS = ROOT / "assets" / "photos"
META = PHOTOS / "_trips.json"
JEMDOC = ROOT / "other.jemdoc"

START_MARKER = "<!-- GALLERY-AUTO-START -->"
END_MARKER = "<!-- GALLERY-AUTO-END -->"
HOBBIES_START = "<!-- HOBBIES-AUTO-START -->"
HOBBIES_END = "<!-- HOBBIES-AUTO-END -->"

IMG_EXTS = {".jpeg", ".jpg", ".png", ".webp", ".gif"}


def list_images(d: Path) -> list[Path]:
    if not d.is_dir():
        return []
    files = [p for p in d.iterdir() if p.suffix.lower() in IMG_EXTS and not p.name.startswith(".")]
    files.sort(key=lambda p: p.name.lower())
    return files


def slug_to_alt(slug: str, n: int) -> str:
    base = slug.replace("_", " ").replace("-", " ")
    return f"{base} — {n}"


def render_trip(meta: dict) -> str:
    slug = meta["dir"]
    folder = PHOTOS / slug
    images = list_images(folder)
    if not images:
        return ""
    title = meta.get("title")
    date = meta.get("date")
    head = ""
    if title:
        date_html = f' <span class="trip-date">{date}</span>' if date else ""
        # title may contain & or — — leave it as-is, jemdoc raw block escapes nothing
        head = f"  <h3>{title}{date_html}</h3>\n"
    cells = []
    for i, img in enumerate(images, 1):
        rel = f"assets/photos/{slug}/{img.name}"
        alt = slug_to_alt(slug, i)
        cells.append(
            f'    <a class="trip-photo" href="{rel}" target="_blank" rel="noopener">'
            f'<img src="{rel}" alt="{alt}" loading="lazy" /></a>'
        )
    return f'<section class="trip">\n{head}  <div class="trip-grid">\n' + "\n".join(cells) + "\n  </div>\n</section>"


def render_section(trips: Iterable[dict]) -> str:
    rendered = [render_trip(t) for t in trips]
    rendered = [r for r in rendered if r]
    return "\n\n".join(rendered)


def replace_block(text: str, start: str, end: str, payload: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"missing markers {start!r} / {end!r} in {JEMDOC}")
    body = f"{start}\n{payload}\n{end}"
    return pattern.sub(body, text)


def main() -> None:
    if not META.exists():
        sys.exit(f"missing {META}")
    cfg = json.loads(META.read_text())
    trips = cfg.get("trips", [])
    known_dirs = {t["dir"] for t in trips}

    # auto-pick up any new folders not in the manifest
    for child in sorted(PHOTOS.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        if child.name not in known_dirs:
            trips.append({"dir": child.name, "title": child.name.replace("_", " "), "date": None, "section": "travels"})

    travels = [t for t in trips if t.get("section") == "travels"]
    hobbies = [t for t in trips if t.get("section") == "hobbies"]

    txt = JEMDOC.read_text()
    txt = replace_block(txt, START_MARKER, END_MARKER, render_section(travels))
    txt = replace_block(txt, HOBBIES_START, HOBBIES_END, render_section(hobbies))
    JEMDOC.write_text(txt)

    travel_count = sum(len(list_images(PHOTOS / t["dir"])) for t in travels)
    hobby_count = sum(len(list_images(PHOTOS / t["dir"])) for t in hobbies)
    print(f"gallery: {len(travels)} trips / {travel_count} photos + hobbies / {hobby_count} photos")


if __name__ == "__main__":
    main()
