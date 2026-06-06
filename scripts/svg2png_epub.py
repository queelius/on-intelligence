#!/usr/bin/env python3
"""Convert the SVG math/figures in an EPUB to raster PNG for Kindle compatibility.

Amazon's reflowable Kindle format does not support SVG (only fixed-layout does),
so KDP's converter rejects the SVG EPUB that tex4ebook produces. This rasterizes
every SVG to a 2.5x PNG (white background, so math stays readable including in
dark mode) and rewrites the <img> references and the OPF manifest, preserving the
original display size via an injected width style. The general (SVG) EPUB remains
the better file for Apple Books / Kobo / Google Play, which handle SVG well.

Usage: svg2png_epub.py IN.epub OUT.epub [zoom]
"""
import os, re, sys, glob, shutil, zipfile, subprocess

SRC  = sys.argv[1] if len(sys.argv) > 1 else "on-intelligence.epub"
OUT  = sys.argv[2] if len(sys.argv) > 2 else "on-intelligence-kindle.epub"
ZOOM = sys.argv[3] if len(sys.argv) > 3 else "2.5"
WORK = "/tmp/svg2png_work"

shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK)
with zipfile.ZipFile(SRC) as z:
    z.extractall(WORK)

def svg_dims(path):
    """Intrinsic width/height in pt from the <svg> root (double or single quote)."""
    head = open(path, encoding="utf-8", errors="ignore").read(2000)
    w = re.search(r"\bwidth=[\"']([0-9.]+)pt", head)
    h = re.search(r"\bheight=[\"']([0-9.]+)pt", head)
    return (w.group(1) if w else None, h.group(1) if h else None)

sizes = {}
svgs = glob.glob(WORK + "/**/*.svg", recursive=True)
for s in svgs:
    base = os.path.basename(s)[:-4]
    sizes[base] = svg_dims(s)
    png = s[:-4] + ".png"
    subprocess.run(["rsvg-convert", "-z", ZOOM, "-b", "white", "-o", png, s], check=True)
    os.remove(s)
print(f"rasterized {len(svgs)} SVG -> PNG at {ZOOM}x")

# Rewrite <img> tags: .svg -> .png, and inject a width style so the higher-density
# PNG still displays at the original size (max-width:100% keeps wide figures on-screen).
img_re = re.compile(r'<img\b[^>]*?\bsrc="([^"]+)\.svg"[^>]*?/?>', re.IGNORECASE)
def fix_img(m):
    tag, base = m.group(0), os.path.basename(m.group(1))
    tag = tag.replace(m.group(1) + ".svg", m.group(1) + ".png")
    w, h = sizes.get(base, (None, None))
    if w and "style=" not in tag:
        style = f' style="max-width:100%;width:{w}pt;height:auto"'
        tag = re.sub(r'\s*/?>\s*$', style + "/>", tag)
    return tag

html_files = glob.glob(WORK + "/**/*.xhtml", recursive=True) + glob.glob(WORK + "/**/*.html", recursive=True)
n_imgs = 0
for x in html_files:
    t = open(x, encoding="utf-8").read()
    t, k = img_re.subn(fix_img, t)
    n_imgs += k
    open(x, "w", encoding="utf-8").write(t)
print(f"rewrote {n_imgs} <img> references across {len(html_files)} documents")

# Replace calibre's inline-SVG cover wrapper (<svg><image xlink:href=.../></svg>)
# with a plain <img>, so no inline SVG remains to trip Kindle's converter.
cover_re = re.compile(
    r'<svg\b[^>]*>\s*<image\b[^>]*?xlink:href="([^"]+)"[^>]*/>\s*</svg>',
    re.IGNORECASE | re.DOTALL)
n_cov = 0
for x in html_files:
    t = open(x, encoding="utf-8").read()
    t, k = cover_re.subn(r'<img src="\1" alt="Cover" style="max-width:100%;height:auto"/>', t)
    if k:
        n_cov += k
        open(x, "w", encoding="utf-8").write(t)
print(f"replaced {n_cov} inline-SVG cover wrapper(s) with <img>")

# Rewrite the OPF manifest: svg hrefs/ids/media-types -> png; drop the svg property.
for o in glob.glob(WORK + "/**/*.opf", recursive=True):
    t = open(o, encoding="utf-8").read()
    t = t.replace(".svg\"", ".png\"").replace("_svg\"", "_png\"").replace("image/svg+xml", "image/png")
    t = t.replace('properties="svg "', 'properties="').replace('properties="svg ', 'properties="')
    t = t.replace(' properties="svg"', '')
    open(o, "w", encoding="utf-8").write(t)

# Repackage: mimetype first and stored, everything else deflated.
if os.path.exists(OUT):
    os.remove(OUT)
with zipfile.ZipFile(OUT, "w") as z:
    mt = os.path.join(WORK, "mimetype")
    if os.path.exists(mt):
        z.write(mt, "mimetype", compress_type=zipfile.ZIP_STORED)
    for root, _, files in os.walk(WORK):
        for fn in files:
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, WORK)
            if rel == "mimetype":
                continue
            z.write(full, rel, compress_type=zipfile.ZIP_DEFLATED)
print("wrote", OUT, f"({os.path.getsize(OUT)//1024} KB)")
