#!/usr/bin/env python3
"""Render every tikzpicture to a PNG and rewrite chapters to use \\includegraphics.

The Kindle EPUB is built with pandoc (the toolchain proven on the author's other
KDP titles), but pandoc cannot render TikZ. So we pre-render each tikzpicture to a
transparent high-resolution PNG via a standalone LaTeX compile, then emit modified
chapter sources where each tikzpicture is replaced by an \\includegraphics that
pandoc DOES carry into the EPUB (its surrounding figure/caption/label is kept, so
the figure renders with its caption). Math is left untouched for pandoc --mathml.

Reads:  chapters/*.tex
Writes: build/chapters/*.tex (pandoc-ready) and build/figs/*.png
"""
import os, re, sys, glob, subprocess, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_CH = os.path.join(ROOT, "chapters")
BUILD = os.path.join(ROOT, "build")
OUT_CH = os.path.join(BUILD, "chapters")
FIGS = os.path.join(BUILD, "figs")
DPI = "300"

os.makedirs(OUT_CH, exist_ok=True)
os.makedirs(FIGS, exist_ok=True)

# Minimal standalone preamble: just what the diagrams use (tikz + libraries + math
# + a matching roman font). border gives a little breathing room around the crop.
PREAMBLE = r"""\documentclass[border=4pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, calc, decorations.markings, decorations.pathmorphing, patterns, trees}
\begin{document}
"""

TIKZ_RE = re.compile(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", re.S)

def render(tikz_code, stem):
    """Compile one tikzpicture to a transparent PNG; return True on success."""
    texf = os.path.join(FIGS, stem + ".tex")
    with open(texf, "w") as fh:
        fh.write(PREAMBLE + tikz_code + "\n\\end{document}\n")
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        stem + ".tex"], cwd=FIGS, capture_output=True, text=True)
    pdf = os.path.join(FIGS, stem + ".pdf")
    if r.returncode != 0 or not os.path.exists(pdf):
        log = (r.stdout or "")[-800:]
        print(f"  !! {stem}: pdflatex failed\n{log}")
        return False
    # PDF -> transparent PNG. pdftocairo -transp preserves the standalone's clear
    # background (RGBA); -r DPI sets resolution; -singlefile drops the page suffix.
    subprocess.run(["pdftocairo", "-png", "-r", DPI, "-transp", "-singlefile",
                    stem + ".pdf", stem], cwd=FIGS, check=True)
    # tidy intermediates
    for ext in (".tex", ".pdf", ".aux", ".log"):
        p = os.path.join(FIGS, stem + ext)
        if os.path.exists(p):
            os.remove(p)
    return True

total = 0
for src in sorted(glob.glob(os.path.join(SRC_CH, "*.tex"))):
    name = os.path.basename(src)[:-4]
    text = open(src).read()
    idx = [0]
    def repl(m):
        idx[0] += 1
        stem = f"{name}_{idx[0]}"
        ok = render(m.group(0), stem)
        if not ok:
            return m.group(0)  # leave as-is if render failed (pandoc will drop it)
        return (f"\\includegraphics[width=\\linewidth]{{figs/{stem}.png}}")
    new = TIKZ_RE.sub(repl, text)
    open(os.path.join(OUT_CH, name + ".tex"), "w").write(new)
    if idx[0]:
        print(f"  {name}: rendered {idx[0]} tikzpicture(s)")
        total += idx[0]
print(f"done: {total} diagrams rendered to {FIGS}")
