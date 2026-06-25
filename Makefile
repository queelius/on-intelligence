# Makefile for On Intelligence and Its Specifications
# Nonfiction: the mathematics of optimal intelligence and the specification problem.

PDFLATEX = pdflatex -interaction=nonstopmode

MAIN  = on-intelligence
TEX   = $(MAIN).tex
PDF   = $(MAIN).pdf
EPUB  = $(MAIN)-kindle.epub        # the Kindle eBook published on Amazon KDP
COVER = kdp/cover-front.jpg
BUILD = build
DEPS  = $(TEX) $(wildcard chapters/*.tex) $(wildcard figures/*.tex)

AUX_EXTS = aux log out toc bbl blg lof lot fls fdb_latexmk synctex.gz

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

# Kindle eBook (Amazon KDP). pandoc is the toolchain KDP's KFX converter accepts;
# tex4ebook/calibre output was rejected (E21017 unpack / E21027 "more than one opf").
# pandoc cannot render TikZ, so scripts/render_tikz.py first pre-renders every
# tikzpicture to a transparent PNG (standalone pdflatex + poppler pdftocairo) and
# rewrites the chapters into $(BUILD)/, where each diagram becomes an \includegraphics
# that pandoc carries into the EPUB. The math is left to pandoc --mathml, so it
# reflows as real text, not raster boxes. Run from $(BUILD)/ so the rewritten
# chapters/ and figs/ resolve relative to main.tex.
# Requires: pandoc, a TeX Live with pdflatex, and poppler's pdftocairo.
epub: $(EPUB)

$(EPUB): $(DEPS) $(COVER) scripts/render_tikz.py
	python3 scripts/render_tikz.py
	cp $(TEX) $(BUILD)/main.tex
	cd $(BUILD) && pandoc main.tex -o $(EPUB) \
		--toc --toc-depth=2 --split-level=2 --mathml \
		--epub-cover-image=../$(COVER) \
		-M title="On Intelligence and Its Specifications" \
		-M author="Alex Towell" -M lang="en-US" -M date="2026"
	cp $(BUILD)/$(EPUB) $(EPUB)
	@echo "Kindle EPUB built: $(EPUB) ($$(du -h $(EPUB) 2>/dev/null | cut -f1))"

# Word count
wordcount:
	@printf "%-20s " "On Intelligence:"
	@if command -v detex >/dev/null 2>&1; then \
		detex $(TEX) 2>/dev/null | wc -w | tr -d ' '; \
	else \
		cat chapters/*.tex 2>/dev/null | wc -w | tr -d ' '; \
	fi

# Clean: aux files only (outputs and the build/ figure cache are preserved)
clean:
	@for ext in $(AUX_EXTS); do rm -f *.$$ext; done
	@rm -f chapters/*.aux
	@echo "Cleaned auxiliary files (outputs preserved)"

distclean: clean
	rm -f $(PDF) $(EPUB)
	rm -rf $(BUILD)
	@echo "Cleaned all build artifacts (incl. build/)"

help:
	@echo "On Intelligence and Its Specifications -- Build System"
	@echo ""
	@echo "  make pdf         Build print PDF (latexmk, converges refs/TOC; default)"
	@echo "  make check       Quick single-pass compile"
	@echo "  make epub        Build Kindle eBook via pandoc (MathML math, TikZ rasterized) for Amazon KDP"
	@echo "  make wordcount   Word count"
	@echo "  make clean       Remove auxiliary files (outputs preserved)"
	@echo "  make distclean   Remove all generated files (incl. build/)"
	@echo "  make help        Show this message"
