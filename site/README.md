# mesabo.github.io — source

Personal profile site for **Messou Franck Junior Aboya**. Generated from `.jemdoc` source files using [jemdoc](http://jemdoc.jaboc.net/) (Python 3 fork from [wsshin/jemdoc_mathjax](https://github.com/wsshin/jemdoc_mathjax)).

## Local preview

```bash
make            # build all pages into build/
make serve      # start http://localhost:8000
make clean      # remove build/
```

The build is currently running on http://localhost:8765 (started by Claude during scaffolding). Stop it with `kill <PID>` if it's still running, or use `make serve` to start a fresh one.

## Edit a page

1. Edit the corresponding `.jemdoc` file:
   - `index.jemdoc` — about / hero
   - `publications.jemdoc`
   - `research.jemdoc`
   - `experiences.jemdoc`
   - `awards.jemdoc`
   - `other.jemdoc` — open-source, mentorship, **trips & photos**
2. Run `make` to regenerate.
3. Refresh browser.

## Add photos to a trip (5 per row)

Each trip is a section in `other.jemdoc`. Drop new photos as **PNG or PDF** (per project policy) into `assets/photos/<trip-name>/`, then edit the corresponding `<section class="trip">` block in `other.jemdoc` to replace `placeholder` cells with real `<a><img></a>` cells. Use sips for resizing:

```bash
sips -Z 1400 -s format png input.jpg --out assets/photos/<trip>/02.png
```

## Add a new trip

Copy a `<section class="trip">` block in `other.jemdoc`, change the title and date, add 1–5 image cells (rest as `placeholder`), and create the matching `assets/photos/<trip>/` folder.

## Style

CSS in `mysite.css`. Palette ported from `Profile/researcher/style.css`:
- Accent: `#6f3bd0` (purple)
- Body font: Crimson Pro (serif) via Google Fonts
- Heading sans: Inter
- Mobile breakpoint: 720px (menu collapses; photo grid drops to 3 columns)

## Deploy to mesabo.github.io

The repo `mesabo/mesabo.github.io` does not exist yet. Two-step setup:

1. Create the repo on GitHub:
   ```bash
   gh repo create mesabo/mesabo.github.io --public --description "Personal profile of Messou Franck Junior Aboya"
   ```
2. Deploy:
   ```bash
   make deploy
   ```
   This force-pushes `build/` to `main`. GitHub Pages picks it up automatically and serves at https://mesabo.github.io within ~1 minute.

⚠️ **`make deploy` force-pushes** — only run when you are happy with the local preview. Source of truth is this `Profile/site/` directory inside the private Scholarship repo; `mesabo/mesabo.github.io` is a deploy target.

## Files

```
site/
├── MENU                  shared sidebar nav
├── mysite.conf           jemdoc config (CSS hook, menu templates)
├── mysite.css            custom styles (palette + layout + gallery)
├── *.jemdoc              page sources (6 pages)
├── Makefile
├── tools/
│   ├── jemdoc            jemdoc Python script (vendored)
│   └── jemdoc-default.css default jemdoc CSS
├── assets/
│   ├── photo.png         hero avatar
│   ├── cv/               4 downloadable CV variants
│   ├── papers/           figure placeholders (replace with real teaser figures later)
│   └── photos/<trip>/    trip photo galleries (PNG only)
└── build/                generated HTML — what gets deployed
```
