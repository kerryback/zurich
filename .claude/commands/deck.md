---
description: Export a rendered deck to PDF with the global deck skill
argument-hint: <session number or filename>
allowed-tools: Bash(bash ~/.claude/skills/deck/assets/deck-to-pdf.sh:*)
---

Export the deck `$1` by running, from the project root:

```
# every deck -- mint, a 1280x720 (16:9) canvas
bash ~/.claude/skills/deck/assets/deck-to-pdf.sh $1 --root docs --out pdf --size 1920x1080
```

Every deck here is on the same canvas, so `--size` is the same for all of them.
Check the deck's front matter if you are unsure: `width`/`height` there are the
canvas, and `--size` is 1.5x it for 16:9 (see below).

Those three flags are all this repo contributes. Everything else — loose name
matching, re-rendering a stale deck, serving the site over HTTP, mirroring the
result — lives in the global `deck` skill at `~/.claude/skills/deck/`, so it
stays the same across every repo. Do not reimplement any of it here, and if the
export itself needs fixing, fix it there.

`--root docs` is the rendered site and `--out pdf` is the tracked copy; the
script mirrors each PDF into `docs/pdf/` so it is live on the served site
without a full re-render. The whole `pdf` folder is in the `resources:` list in
`_quarto.yml`, so a later `quarto render` keeps that copy rather than dropping
it. Commit both.

The `--size` override is the reason this file exists. The skill's 1920x1200
default is 16:10 — deliberately taller than a 1920x1080 deck, to give back the
margin decktape drops. Every deck here sets `margin: 0`, so there is no margin
to give back and a 16:10 viewport would just letterbox the slides with bands of
page either side. Match the deck's own aspect ratio instead:

| Deck | Theme | Canvas | `--size` | Page |
|---|---|---|---|---|
| Every deck | `mint.scss` | 1280x720, 16:9 | 1920x1080 | 1440x810pt |

The multiple (1.5x) only sets the raster resolution; the aspect ratio is what has
to match. A deck built on another canvas gets a second row here.

Name a deck by its filename: `/deck curriculum` or `/deck tools`. Omit `$1` to export every deck
that is currently rendered under `docs/`. If the name matches nothing the script
lists what it found; relay that list. Report where the PDF landed and its page
count.
