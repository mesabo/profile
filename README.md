# Profile — source for [mesabo.github.io](https://mesabo.github.io)

> 🌐 **Live site → https://mesabo.github.io**

Personal profile site of **Messou Franck Junior Aboya** — PhD researcher at Hosei University YuLab (AI / sLM / LLM for smart-grid stability and IoT systems), AI / backend engineer, and full-stack engineer.

| | |
|---|---|
| **Live site** | https://mesabo.github.io |
| **Source** (this repo) | https://github.com/mesabo/profile |
| **Deploy target** | https://github.com/mesabo/mesabo.github.io |
| **Built with** | [jemdoc](http://jemdoc.jaboc.net/) |

## Layout

```
Profile/
├── site/                 jemdoc source for the website
│   ├── *.jemdoc          page sources
│   ├── MENU              shared sidebar nav
│   ├── mysite.conf       jemdoc config (HTML5 doctype, CSS hook, menu templates)
│   ├── mysite.css        custom styles
│   ├── Makefile          build + deploy targets
│   ├── tools/
│   │   ├── jemdoc                vendored jemdoc Python script (Python 3 fork)
│   │   ├── jemdoc-default.css    fallback default CSS
│   │   └── gen_gallery.py        auto-generates the photo gallery in other.jemdoc
│   ├── assets/
│   │   ├── photo.png             hero avatar
│   │   ├── cv/                   4 CV variants (AI / SE × EN / JP)
│   │   ├── papers/               canonical PDF figures (one per paper)
│   │   ├── awards/               award certificates
│   │   └── photos/               trip galleries — one folder per trip + _trips.json
│   └── build/                    generated HTML — pushed to mesabo/mesabo.github.io
│
├── ressources/           backup of source-quality assets (photos, certificates, paper masters)
├── AI_EN.pdf, AI_JA.pdf  CV — AI/Backend Engineer (English / Japanese)
└── SE_EN.pdf, SE_JA.pdf  CV — Full-stack Software Engineer (English / Japanese)
```

## Build & deploy

```bash
cd site
make            # build to site/build/
make serve      # local preview at http://localhost:8000
make deploy     # force-push site/build/ to mesabo/mesabo.github.io main
```

Deploy goes to a separate repo: [`mesabo/mesabo.github.io`](https://github.com/mesabo/mesabo.github.io). GitHub Pages serves it.

## Edit a page

1. Edit the matching `.jemdoc` file (e.g. `site/research.jemdoc`).
2. `make` to regenerate.
3. `make deploy` to publish.

## Add photos

Drop new photos into `site/assets/photos/<trip>/`. The next `make` runs `tools/gen_gallery.py`, scans the folder, and rebuilds the gallery automatically — no HTML editing.

To name a new trip, add an entry in `site/assets/photos/_trips.json`. Otherwise the folder name is used.

## Replace a paper architecture

Drop the real PDF over the placeholder in `site/assets/papers/<paper>.pdf`. The PNG thumbnail is auto-rendered by `pdftoppm` during `make` and lives only in `site/build/`.

## Tools required

- `python3` (3.8+)
- `pdftoppm` (from `poppler` — `brew install poppler`)
- `make`
- `gh` CLI (for `make deploy` push auth)

## Multilingual

`fr.jemdoc` and `ja.jemdoc` are placeholder language stubs. The sidebar menu has an English / Français / 日本語 group; only English is currently complete.

## Built with

[jemdoc](http://jemdoc.jaboc.net/) (Python-3 fork from [wsshin/jemdoc_mathjax](https://github.com/wsshin/jemdoc_mathjax)) — light text-based markup for academic websites.
