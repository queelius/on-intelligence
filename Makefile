# Makefile for On Intelligence and Its Specification
# Nonfiction: algorithmic information theory and computational eternalism.

PDFLATEX = pdflatex -interaction=nonstopmode
BIBTEX   = bibtex

MAIN     = on-intelligence
TEX      = $(MAIN).tex
PDF      = $(MAIN).pdf
EPUB        = $(MAIN).epub
KINDLE_EPUB = $(MAIN)-kindle.epub
COVER       = kdp/cover-front.jpg
DEPS     = $(TEX) $(wildcard chapters/*.tex) $(wildcard figures/*.tex)

AUX_EXTS    = aux log out toc bbl blg lof lot fls fdb_latexmk synctex.gz
# tex4ebook / tex4ht intermediates left in the working dir by `make epub`
TEX4HT_EXTS = 4ct 4tc idv lg xref tmp ncx opf css dvi html

.DEFAULT_GOAL := pdf

.PHONY: pdf check epub epub-kindle wordcount clean distclean help

# PDF build: latexmk reruns pdflatex until the TOC and cross-references converge,
# so there is no fixed pass count to maintain (a reflow can need three passes).
pdf: $(PDF)

$(PDF): $(DEPS)
	latexmk -pdf -pdflatex="$(PDFLATEX) %O %S" $(TEX)
	@echo "PDF built: $(PDF) ($$(pdfinfo $(PDF) 2>/dev/null | awk '/Pages/ {print $$2}') pages)"

# Quick single-pass compile
check: $(DEPS)
	$(PDFLATEX) $(TEX)
	@echo "Quick compile done (run 'make pdf' for full build)"

# EPUB, general edition (reflowable) for SVG-capable stores (Apple Books, Kobo,
# Google Play), in two stages:
#   1. tex4ebook renders the LaTeX to EPUB3. Math and the TikZ diagrams become SVG
#      (crisp and scalable, with the LaTeX kept as img alt-text), footnotes become
#      EPUB3 popup notes, and chapters split into separate XHTML files.
#   2. calibre (ebook-convert) normalizes that into a valid EPUB3: a dedicated nav
#      document, sanitized XHTML, cover and metadata, preserving the SVG math,
#      figures, and popup footnotes. (Do NOT drop --epub-version 3: without it
#      calibre emits EPUB2-flavoured XHTML where epub:type footnotes are invalid.)
#   3. add_ncx.py injects a legacy NCX (derived from the nav doc) that some Kindle
#      converter paths rely on, while keeping the EPUB3 epubcheck-valid.
#   4. canonical_layout.py consolidates calibre's split layout (OPF/NCX/cover/CSS
#      at the ZIP root, content in OEBPS/) into a single OEBPS/ folder. Kindle
#      Previewer 3's KFX unpacker rejects the split layout (E21017 "problem while
#      unpacking" -> spurious E21027 "more than one opf file").
# NOTE: Amazon's reflowable Kindle format does NOT accept SVG. For KDP, build the
# Kindle edition instead (`make epub-kindle`), which rasterizes the SVG to PNG.
# Requires: tex4ebook (TeX Live) and calibre (ebook-convert).
epub: $(EPUB)

$(EPUB): $(DEPS) $(COVER) scripts/add_ncx.py scripts/canonical_layout.py
	tex4ebook -f epub3 $(TEX)
	ebook-convert $(EPUB) $(MAIN)-normalized.epub \
		--epub-version 3 \
		--cover=$(COVER) \
		--title="On Intelligence and Its Specifications" \
		--authors="Alex Towell" \
		--language=en \
		--preserve-cover-aspect-ratio \
		--no-default-epub-cover
	mv -f $(MAIN)-normalized.epub $(EPUB)
	python3 scripts/add_ncx.py $(EPUB)
	python3 scripts/canonical_layout.py $(EPUB) $(EPUB)
	@echo "EPUB built: $(EPUB) ($$(du -h $(EPUB) 2>/dev/null | cut -f1))"

# Kindle edition (for Amazon KDP): rasterize the SVG math/figures in the general
# EPUB to PNG (2.5x, white background, display size preserved), since Amazon's
# reflowable Kindle converter rejects SVG. Upload $(KINDLE_EPUB) to KDP; keep
# $(EPUB) for the SVG-capable stores. Requires: rsvg-convert (librsvg), python3+Pillow.
epub-kindle: $(KINDLE_EPUB)

$(KINDLE_EPUB): $(EPUB) scripts/svg2png_epub.py scripts/canonical_layout.py
	python3 scripts/svg2png_epub.py $(EPUB) $(KINDLE_EPUB) 2.5
	python3 scripts/canonical_layout.py $(KINDLE_EPUB) $(KINDLE_EPUB)
	@echo "Kindle EPUB built: $(KINDLE_EPUB) ($$(du -h $(KINDLE_EPUB) 2>/dev/null | cut -f1))"

# Word count
wordcount:
	@printf "%-35s " "Multitudes:"
	@if command -v detex >/dev/null 2>&1; then \
		detex $(TEX) 2>/dev/null | wc -w | tr -d ' '; \
	else \
		cat chapters/*.tex 2>/dev/null | wc -w | tr -d ' '; \
	fi

# Clean
clean:
	@for ext in $(AUX_EXTS) $(TEX4HT_EXTS); do rm -f *.$$ext; done
	@rm -f chapters/*.aux
	@rm -f $(MAIN)*.svg $(MAIN)*.xhtml $(MAIN)-normalized.epub
	@rm -rf $(MAIN)-epub3
	@echo "Cleaned auxiliary files (outputs preserved)"

distclean: clean
	rm -f $(PDF) $(EPUB) $(KINDLE_EPUB)
	@echo "Cleaned all build artifacts"

help:
	@echo "On Intelligence and Its Specification -- Build System"
	@echo ""
	@echo "  make pdf         Build print PDF (latexmk, converges refs/TOC; default)"
	@echo "  make check       Quick single-pass compile"
	@echo "  make epub        Build general EPUB (SVG math/figures) for Apple Books, Kobo, Google Play"
	@echo "  make epub-kindle Build Kindle EPUB (PNG math/figures) for Amazon KDP"
	@echo "  make wordcount   Word count"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated files"
	@echo "  make help        Show this message"
