#!/usr/bin/env python3
"""Quarto post-render hook.

Quarto preserves the input directory structure under output-dir, so files in
slides/ render to docs/slides/. This copies them one level up so the rendered
decks land directly in docs/ (keeping each deck's _files directory and images/
alongside it, with relative asset paths intact).

docs/slides/ stays in place (and is gitignored) because quarto preview fails
with "No output created" if the output is gone from where it rendered it.
"""
import shutil
from pathlib import Path

src = Path("docs/slides")
dest = Path("docs")

if src.is_dir():
    for item in src.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
    print(f"flattened {src} -> {dest}")
