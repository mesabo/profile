# mesabo.github.io

> 🌐 **Live site → https://mesabo.github.io**

Personal profile of **Messou Franck Junior Aboya** — PhD researcher at the [Hosei University](https://www.hosei.ac.jp) [YuLab](https://iist.hosei.ac.jp/2025/10/20/associate-professor-keping-yu-recognized-as-one-of-the-worlds-top-2-scientists-by-stanford-university-and-elsevier-2025-edition/) ([IIST Koganei Campus](https://iist.hosei.ac.jp), Tokyo) working on AI / sLM / LLM methods for smart-grid stability and IoT systems. Also a part-time AI / full-stack engineer.

## ⚠️ This is a deploy target — do not edit here

This repository holds the **generated static HTML, CSS and assets** that GitHub Pages serves at <https://mesabo.github.io>. It is force-pushed from the source repo on every deploy, so any direct edit here will be overwritten on the next push.

## Source repository

Edit the site at: **https://github.com/mesabo/profile**

That repo contains the [jemdoc](http://jemdoc.jaboc.net/) source files (`*.jemdoc`), the shared `MENU` file, the custom `mysite.css` palette, the build scripts, and all the canonical assets (PDFs, photos, CV variants).

```
profile/                       (source — edit here)
└── site/
    ├── *.jemdoc               page sources
    ├── MENU
    ├── mysite.conf, mysite.css
    ├── tools/                 jemdoc + helpers (gallery generator, etc.)
    ├── assets/                photos, CV variants, paper PDFs
    └── build/                 → pushed to THIS repo
```

## Stack

- **[jemdoc](http://jemdoc.jaboc.net/)** (Python 3 fork, vendored) — light text-based markup for academic websites
- Pure HTML + CSS, **no JavaScript framework** (one tiny inline script for the light/dark theme toggle)
- Auto-generated photo galleries (`tools/gen_gallery.py` scans `assets/photos/`)
- Auto-rendered PDF thumbnails for paper architectures (`pdftoppm` during build)
- **Light / dark theme** with system-preference detection and `localStorage` persistence

## Pages

| URL | Content |
|---|---|
| [/](https://mesabo.github.io/) | About — hero, research / engineering focus, highlights |
| [/publications.html](https://mesabo.github.io/publications.html) | 2 Q1 journals + 9 IEEE flagship conference papers + service |
| [/research.html](https://mesabo.github.io/research.html) | PhD project (smart-grid co-optimization) + spectral-reprogramming track |
| [/experiences.html](https://mesabo.github.io/experiences.html) | Education, research, industry (D'isum, JICA), engineering, mentorship + CV downloads |
| [/awards.html](https://mesabo.github.io/awards.html) | VTS 2024 Student Paper Award · JICA 2025 · IEEE ICECET 2026 reviewer |
| [/other.html](https://mesabo.github.io/other.html) | Open-source projects, outreach, conference travels, hobbies |

## Built with

Three muted facet colours used sparingly across the site:

- 🟣 **Purple** — research / academic
- 🩵 **Teal** — engineering / IoT / GPU
- 🟠 **Amber** — recognition / awards

## Contact

- **GitHub** — [@mesabo](https://github.com/mesabo)
- **LinkedIn** — [/in/mesabo](https://www.linkedin.com/in/mesabo/)
- **Google Scholar** — [Franck Junior Aboya Messou](https://scholar.google.com/citations?user=tHBBTIEAAAAJ)
- **Email** — [mesabo18@gmail.com](mailto:mesabo18@gmail.com)
