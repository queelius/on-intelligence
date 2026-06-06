# Makefile for On Intelligence and Its Specification
# Nonfiction: algorithmic information theory and computational eternalism.

PDFLATEX = pdflatex -interaction=nonstopmode -shell-escape
BIBTEX   = bibtex

MAIN     = on-intelligence
TEX      = $(MAIN).tex
PDF      = $(MAIN).pdf
EPUB     = $(MAIN).epub
DEPS     = $(TEX) $(wildcard chapters/*.tex) $(wildcard figures/*.tex)

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

# EPUB
epub: $(EPUB)

$(EPUB): $(DEPS)
	pandoc $(TEX) \
		-o $(EPUB) \
		--toc \
		--toc-depth=2 \
		--split-level=2 \
		--mathml \
		--epub-title-page=true \
		--epub-cover-image=figures/cover.png \
		-M title="On Intelligence and Its Specification" \
		-M author="Alex Towell" \
		-M lang="en-US"
	@echo "EPUB built: $(EPUB)"

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
	@for ext in $(AUX_EXTS); do rm -f *.$$ext; done
	@rm -f chapters/*.aux
	@echo "Cleaned auxiliary files (outputs preserved)"

distclean: clean
	rm -f $(PDF) $(EPUB)
	@echo "Cleaned all build artifacts"

help:
	@echo "On Intelligence and Its Specification -- Build System"
	@echo ""
	@echo "  make pdf         Build PDF (two-pass, default)"
	@echo "  make check       Quick single-pass compile"
	@echo "  make epub        Build EPUB"
	@echo "  make wordcount   Word count"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated files"
	@echo "  make help        Show this message"
