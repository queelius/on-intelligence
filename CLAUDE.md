# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Title:** *On Intelligence and Its Specifications*

**Thesis:** There is a beautiful mathematical theory of optimal intelligence (Bayesian inference + Solomonoff induction + expected utility maximization = AIXI). There are messy real systems that approximate it (LLMs). The gap between them is where AI safety lives. To reason responsibly about AI in 2026, the reader needs both sides.

**Audience:** Determined but lay readers. Math is used where it has to be, conceptually explained first, then formalized. Diagrams carry most of the conceptual weight. Closer to a Penguin science book than to a textbook.

**Current status:** Complete and published. 17 chapters, 4 parts, 214 pages. Paperback on Amazon KDP (2026); reflowable EPUB built via `make epub`. The prior philosophical framing was extracted to the sibling project `../multitudes/`.

**Structure:** 17 chapters across 4 parts.

- **Part I: Prediction (Chs 1–4).** Bayes, the prior problem, description and probability, Solomonoff induction.
- **Part II: Decision (Chs 5–8).** The agent, reinforcement learning, generalization (inductive biases, NNs, sample efficiency), AIXI.
- **Part III: The Specification Problem (Chs 9–12).** Reward modeling, inner alignment, why optimization is dangerous (orthogonality, instrumental convergence, capability amplifies misspecification), mitigations and their limits (light treatment of the three buckets: limit / uncertain / observable).
- **Part IV: Reality (Chs 13–17).** Large language models (what a base model is: prediction, transformer biases, the Solomonoff connection), reward and reasoning (RLHF, RLVR, GOFAI verifiers, inference-time search), the gap, what's ahead (Ch 16: the trajectory, scaling honestly, the jagged edge, recursive self-improvement, the burden-has-shifted stand), and the finale (Ch 17: *Teaching Sand to Think*), which fuses the conceptual stand (prediction is intelligence; real minds; no magic substrate) with the stakes and the CoT-Goodhart material.

**Length:** No fixed word-count target. The book is sized by what the material warrants; completeness and clarity govern, not a ceiling. (Per-chapter figures in `lore/outline.md` are descriptive pacing guides, not budgets.)

Pedagogical move: Parts I-III develop the theory in clean settings (including the alignment problem treated pedagogically). Part IV moves to messy practice.

## Lore Bible

| Document | Function |
|---|---|
| `lore/outline.md` | 17-chapter outline (4 parts), role of each chapter, drafting order. |
| `lore/themes.md` | Thesis, central themes, what the book is and is not, voice, the committed stand, relationship to other work. |
| `lore/direction.md` | Format, audience, tone, pedagogy, diagram principle, comparable works, KDP considerations. |
| `lore/math-grounding.md` | Mathematical reference: Cox, Kraft, Solomonoff, dominance, RL, utility theory, AIXI. |

## Key Constraints

**The mathematics must be real.** Bayes is Bayes; Cox is Cox; Solomonoff is Solomonoff. No hand-waving, no informal arguments dressed up as theorems. Where the book sketches a proof, the sketch must point to the real result.

**Diagrams must do the work.** This is a lay-audience book. Every equation gets a diagram. Every algorithm gets a diagram. Every concept that can be visualized should be. Diagrams are designed alongside the prose, not bolted on.

**The gap is the destination.** Each chapter in Part I and Part II is doing pedagogical work *toward* the gap that Part III makes explicit. The reader who finishes Part II should be ready to see the gap unaided when LLMs are introduced.

**The closing must be substantial and honest.** The finale (Ch 17, *Teaching Sand to Think*) is the destination. It takes the committed stand (prediction is intelligence; real minds; the trajectory's burden has shifted) and carries the stakes (the gap arriving at our most important instrument). Ch 16 (*What's Ahead*) sets it up with the trajectory. The finale earns its conclusions from the math and the situation, states the stand plainly, and does not preach or hype.

**Voice must match Worldlines.** Direct address. The Towell voice rules apply: no em-dashes, no hype, plain and honest. See `~/.claude/CLAUDE.md` and the soul plugin for details.

## LaTeX Conventions

- Math mode for all symbols: $K(x)$, $M(x)$, $\sum$, $\to$. No raw unicode for mathematical notation in body text.
- Inline math: `$...$`. Display math: `$$...$$` or `\begin{equation}...\end{equation}`.
- Theorem environments where formal precision is being claimed.
- Diagrams: TikZ. Consistent visual style (palette, fonts, primitives). Same aesthetic as Worldlines.

## Voice Rules

- **No em-dashes.** Use commas, periods, colons, or parentheses.
- **First person and second person.** "You" addressing the reader; "I" only where the author makes a personal statement (sparingly).
- **Plain and direct.** Short sentences. Period for emphasis.
- **No hype.** Corporate buffer language and signaling phrases are banned. See the soul plugin's banned-phrase list.
- **Earned conclusions.** The math earns the claim. Build, do not declare.
- **Treat the reader as intelligent and willing to work.**

## Drafting Workflow

The book is drafted with the worldsmith plugin assisting. The lore docs in `lore/` are the foundation:

- `lore/outline.md`: chapter structure, role of each chapter, salvage plan.
- `lore/themes.md`: thesis, voice, position.
- `lore/direction.md`: format, audience, pedagogy, diagrams.
- `lore/math-grounding.md`: mathematical reference (needs updating).

Chapter-specific docs (e.g., `lore/aixi.md`, `lore/llms.md`, `lore/safety.md`) can be added as drafting proceeds, especially for Part III chapters.

**Drafting order (proposed):**

1. Ch 1 (Bayes), to establish the voice for the lay audience.
2. Ch 4 (Solomonoff), since the strongest existing material (current Ch 2–5) maps closely there.
3. Fill in Ch 2, 3 to complete Part I.
4. Part II in sequence (Ch 5–8).
5. Part III in sequence (Ch 9–11).
6. Ch 12 (substantial closing) last, once both sides of the gap are in hand.

## Repository Structure

```
on-intelligence/
├── on-intelligence.tex       # main LaTeX file
├── chapters/                 # the 25 chapter / frontmatter / backmatter .tex files
├── lore/                     # editorial bible: outline, themes, direction, math-grounding
├── figures/                  # TikZ diagrams (most are inline in the chapters)
├── kdp/                      # cover assets (front + print-ready full-wrap PDF) + kdp.local.md
├── docs/                     # editorial review and integration records
├── scripts/                  # render_tikz.py (TikZ -> PNG for the pandoc eBook build)
├── Makefile                  # build system (PDF via latexmk, EPUB via pandoc)
├── CITATION.cff              # citation metadata
└── .zenodo.json              # Zenodo DOI metadata
```

## Note on the pivot

The book began as a philosophical companion to *Worldlines* with a moral arc in Part II (grace as the chosen response to cosmic indifference). The technical material (AIT, Solomonoff, the library of programs, the observer-as-substructure framing) was the strongest part, and the author restructured around it, pointing it at a concrete destination (AI safety understood mathematically). That became this published book.

The original philosophical framing (its draft chapters and lore bible) was extracted into a separate sibling project, `../multitudes/` (*Multitudes: The Indifference of Measure*, a Volume II to *Worldlines*), where the moral / computational-eternalism arc can become its own book.
