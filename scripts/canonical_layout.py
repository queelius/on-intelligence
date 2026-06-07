#!/usr/bin/env python3
"""Repackage an EPUB into the canonical single-folder layout for Kindle Previewer.

Calibre emits a split layout: the OPF, NCX, title page, cover, and CSS sit at the
ZIP root while the chapters and images live in OEBPS/. That is valid EPUB (epubcheck
and kindlegen accept it), but Kindle Previewer 3's newer KFX unpacker trips on it
(E21017 "problem while unpacking") and then misreports E21027 "more than one opf
file." This consolidates everything into a single OEBPS/ folder, with container.xml
pointing at OEBPS/content.opf, and rewrites the relative paths accordingly, the
standard layout pro tools (Sigil) produce and KP3 is tested against.

Usage: canonical_layout.py IN.epub OUT.epub
"""
import os, re, sys, glob, shutil, zipfile, subprocess

SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else SRC
WORK = "/tmp/canon_layout_work"

shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK)
with zipfile.ZipFile(SRC) as z:
    z.extractall(WORK)

oebps = os.path.join(WORK, "OEBPS")
os.makedirs(oebps, exist_ok=True)

# Move every root-level file (except mimetype, which MUST stay at the archive root,
# and META-INF/, which MUST stay put) into OEBPS/ so all content shares one folder.
for name in os.listdir(WORK):
    p = os.path.join(WORK, name)
    if name in ("mimetype", "META-INF", "OEBPS"):
        continue
    if os.path.isfile(p):
        shutil.move(p, os.path.join(oebps, name))

def rewrite(path, subs):
    t = open(path, encoding="utf-8").read()
    for pat, repl in subs:
        t = re.sub(pat, repl, t)
    open(path, "w", encoding="utf-8").write(t)

# container.xml: the OPF is now inside OEBPS/.
container = os.path.join(WORK, "META-INF", "container.xml")
rewrite(container, [(r'full-path="content\.opf"', 'full-path="OEBPS/content.opf"')])

# content.opf and toc.ncx are now inside OEBPS/, so their references to "OEBPS/x"
# become bare "x" (siblings). Root-file refs (cover.jpg, *.css, ...) are already
# bare and are now correct siblings.
for fn in ("content.opf", "toc.ncx"):
    p = os.path.join(oebps, fn)
    if os.path.exists(p):
        rewrite(p, [(r'(href|src)="OEBPS/', r'\1="')])

# Every XHTML/HTML doc is now flat inside OEBPS/, so any "../x" parent reference
# (the chapter/nav files reached the root CSS via ../) collapses to a sibling "x".
for p in glob.glob(oebps + "/*.xhtml") + glob.glob(oebps + "/*.html"):
    rewrite(p, [(r'(href|src)="\.\./', r'\1="')])

# Repackage canonically: mimetype first and STORED (no extra field, so the OCF
# magic sits at offset 38), everything else DEFLATED. Prefer the system `zip`
# (Info-ZIP) implementation: Kindle Previewer's Java unzipper (E21017 "problem
# while unpacking") is pickier than Python's zipfile output, and Info-ZIP is the
# implementation most EPUB tooling targets. Fall back to zipfile if zip is absent.
out_abs = os.path.abspath(OUT)
if os.path.exists(out_abs):
    os.remove(out_abs)
have_zip = shutil.which("zip") is not None
if have_zip:
    subprocess.run(["zip", "-X0", out_abs, "mimetype"], cwd=WORK, check=True,
                   stdout=subprocess.DEVNULL)
    subprocess.run(["zip", "-Xr9D", out_abs, "META-INF", "OEBPS"], cwd=WORK, check=True,
                   stdout=subprocess.DEVNULL)
else:
    with zipfile.ZipFile(out_abs, "w") as z:
        z.write(os.path.join(WORK, "mimetype"), "mimetype", compress_type=zipfile.ZIP_STORED)
        for root, _, files in os.walk(WORK):
            for fn in files:
                rel = os.path.relpath(os.path.join(root, fn), WORK)
                if rel == "mimetype":
                    continue
                z.write(os.path.join(root, fn), rel, compress_type=zipfile.ZIP_DEFLATED)
print(f"repackaged {SRC} -> {OUT} (single OEBPS/ layout, {'system zip' if have_zip else 'zipfile'})")
