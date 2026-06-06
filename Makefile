# Makefile for On Intelligence and Its Specification
# Nonfiction: algorithmic information theory and computational eternalism.

PDFLATEX = pdflatex -interaction=nonstopmode
BIBTEX   = bibtex

MAIN     = on-intelligence
TEX      = $(MAIN).tex
PDF      = $(MAIN).pdf
EPUB     = $(MAIN).epub
COVER    = kdp/cover-front.jpg
DEPS     = $(TEX) $(wildcard chapters/*.tex) $(wildcard figures/*.tex)

AUX_EXTS    = aux log out toc bbl blg lof lot fls fdb_latexmk synctex.gz
# tex4ebook / tex4ht intermediates left in the working dir by `make epub`
TEX4HT_EXTS = 4ct 4tc idv lg xref tmp ncx opf css dvi html

.DEFAULT_GOAL := pdf

.PHONY: pdf check epub wordcount clean distclean help

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

# EPUB (reflowable, Kindle/KDP-ready) via tex4ebook.
# Math and the TikZ diagrams render to SVG (crisp and scalable on EPUB3
# readers, with the LaTeX kept as img alt-text); footnotes become EPUB3 popup
# notes; chapters split into separate XHTML files. The cover and metadata are
# applied in place with ebook-meta (calibre), which does NOT re-render the
# content, so the tex4ebook output (SVG figures, popup notes) is preserved.
# Requires: tex4ebook (TeX Live) and ebook-meta (calibre). Optional: install
# `tidy` for stricter XHTML validity (KDP re-validates on upload regardless).
epub: $(EPUB)

$(EPUB): $(DEPS) $(COVER)
	tex4ebook -f epub3 $(TEX)
	ebook-meta $(EPUB) \
		--cover=$(COVER) \
		--title="On Intelligence and Its Specifications" \
		--authors="Alex Towell" \
		--language=en
	@echo "EPUB built: $(EPUB) ($$(du -h $(EPUB) 2>/dev/null | cut -f1))"

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
	@rm -f $(MAIN)*.svg $(MAIN)*.xhtml
	@rm -rf $(MAIN)-epub3
	@echo "Cleaned auxiliary files (outputs preserved)"

distclean: clean
	rm -f $(PDF) $(EPUB)
	@echo "Cleaned all build artifacts"

help:
	@echo "On Intelligence and Its Specification -- Build System"
	@echo ""
	@echo "  make pdf         Build print PDF (latexmk, converges refs/TOC; default)"
	@echo "  make check       Quick single-pass compile"
	@echo "  make epub        Build reflowable Kindle EPUB (tex4ebook, SVG math/figures, cover)"
	@echo "  make wordcount   Word count"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated files"
	@echo "  make help        Show this message"
