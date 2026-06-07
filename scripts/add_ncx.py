#!/usr/bin/env python3
"""Add a legacy NCX table of contents to a valid EPUB3, generated from its nav doc.

Calibre's --epub-version 3 output is a clean, valid EPUB3 (dedicated nav document,
valid epub:type footnotes) but omits the NCX. Some Kindle/KDP converter paths still
rely on the NCX, and EPUB3 permits an NCX alongside the nav doc for backward
compatibility. This reads the EPUB3 nav document, emits an equivalent toc.ncx
(placed next to the OPF), registers it in the manifest, and points the spine's
toc attribute at it. The result stays a valid EPUB3 (epubcheck clean) and now also
carries the NCX. Idempotent: re-running on a file that already has an NCX is a no-op.

Usage: add_ncx.py FILE.epub
"""
import os, re, sys, html, glob, shutil, zipfile, posixpath

EPUB = sys.argv[1]
WORK = "/tmp/add_ncx_work"

shutil.rmtree(WORK, ignore_errors=True)
os.makedirs(WORK)
with zipfile.ZipFile(EPUB) as z:
    z.extractall(WORK)

opf_path = glob.glob(WORK + "/**/*.opf", recursive=True)[0]
opf_dir = os.path.dirname(opf_path)
opf = open(opf_path, encoding="utf-8").read()

if "application/x-dtbncx+xml" in opf:
    print("NCX already present; nothing to do")
    sys.exit(0)

# Locate the EPUB3 nav document (manifest item with properties="nav").
m = re.search(r'<item\b[^>]*properties="[^"]*\bnav\b[^"]*"[^>]*>', opf)
if not m:
    print("no nav document found; cannot derive NCX"); sys.exit(1)
nav_href = re.search(r'href="([^"]+)"', m.group(0)).group(1)
nav_path = os.path.normpath(os.path.join(opf_dir, nav_href))
nav_dir = os.path.dirname(nav_path)
nav = open(nav_path, encoding="utf-8").read()

# Pull the ordered (href, label) pairs from the toc nav's anchors.
toc = re.search(r'<nav\b[^>]*epub:type="[^"]*\btoc\b[^"]*".*?</nav>', nav, re.S)
block = toc.group(0) if toc else nav
pairs = []
for a in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.S):
    href, label = a.group(1), re.sub(r'<[^>]+>', '', a.group(2))
    label = html.unescape(re.sub(r'\s+', ' ', label)).strip()
    if href and label:
        # Resolve nav-relative href to a path relative to the OPF/NCX directory.
        tgt = os.path.normpath(os.path.join(nav_dir, href.split('#')[0]))
        rel = posixpath.normpath(os.path.relpath(tgt, opf_dir).replace(os.sep, '/'))
        frag = href.split('#', 1)[1] if '#' in href else ''
        pairs.append((rel + ('#' + frag if frag else ''), label))

uid_m = re.search(r'<dc:identifier[^>]*>([^<]+)</dc:identifier>', opf)
uid = uid_m.group(1) if uid_m else "urn:uuid:on-intelligence"
title_m = re.search(r'<dc:title[^>]*>([^<]+)</dc:title>', opf)
title = title_m.group(1) if title_m else "Book"

points = "\n".join(
    f'    <navPoint id="np{i+1}" playOrder="{i+1}">\n'
    f'      <navLabel><text>{html.escape(lbl)}</text></navLabel>\n'
    f'      <content src="{html.escape(href)}"/>\n'
    f'    </navPoint>'
    for i, (href, lbl) in enumerate(pairs))
ncx = (
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
    '  <head>\n'
    f'    <meta name="dtb:uid" content="{html.escape(uid)}"/>\n'
    '    <meta name="dtb:depth" content="1"/>\n'
    '    <meta name="dtb:totalPageCount" content="0"/>\n'
    '    <meta name="dtb:maxPageNumber" content="0"/>\n'
    '  </head>\n'
    f'  <docTitle><text>{html.escape(title)}</text></docTitle>\n'
    f'  <navMap>\n{points}\n  </navMap>\n</ncx>\n')
open(os.path.join(opf_dir, "toc.ncx"), "w", encoding="utf-8").write(ncx)

# Register the NCX in the manifest and point the spine at it.
opf = re.sub(r'(</manifest>)',
             '  <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>\n\\1',
             opf, count=1)
if re.search(r'<spine\b[^>]*\btoc=', opf):
    opf = re.sub(r'(<spine\b[^>]*\btoc=")[^"]*"', r'\g<1>ncx"', opf, count=1)
else:
    opf = re.sub(r'<spine\b', '<spine toc="ncx"', opf, count=1)
open(opf_path, "w", encoding="utf-8").write(opf)

if os.path.exists(EPUB):
    os.remove(EPUB)
with zipfile.ZipFile(EPUB, "w") as z:
    mt = os.path.join(WORK, "mimetype")
    if os.path.exists(mt):
        z.write(mt, "mimetype", compress_type=zipfile.ZIP_STORED)
    for root, _, files in os.walk(WORK):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), WORK)
            if rel == "mimetype":
                continue
            z.write(os.path.join(root, fn), rel, compress_type=zipfile.ZIP_DEFLATED)
print(f"added toc.ncx with {len(pairs)} navPoints to {EPUB}")
