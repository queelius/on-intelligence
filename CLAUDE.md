# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Title:** *On Intelligence and Its Specifications*

**Thesis:** There is a beautiful mathematical theory of optimal intelligence (Bayesian inference + Solomonoff induction + expected utility maximization = AIXI). There are messy real systems that approximate it (LLMs). The gap between them is where AI safety lives. To reason responsibly about AI in 2026, the reader needs both sides.

**Audience:** Determined but lay readers. Math is used where it has to be, conceptually explained first, then formalized. Diagrams carry most of the conceptual weight. Closer to a Penguin science book than to a textbook.

**Current status:** Restructured from a previous philosophical framing. Lore restructured; old lore archived in `lore/archive/`. Some existing chapter material salvageable for the new direction. Drafting against the new outline not yet started.

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
| `lore/outline.md` | 12-chapter outline, salvage plan from prior framing, drafting order. |
| `lore/themes.md` | Thesis, central themes, what the book is and is not, voice, relationship to other work. |
| `lore/direction.md` | Format, audience, tone, pedagogy, diagram principle, comparable works, KDP considerations. |
| `lore/math-grounding.md` | Mathematical reference. Needs updating: drop MWI/CUH/observer-measure (old framing); keep Cox, Kraft, Solomonoff, dominance; add RL, utility theory, AIXI. |
| `lore/archive/` | Old lore from the prior philosophical framing (grace, foundations, implications, etc.). Kept for reference; the math content is salvageable, the philosophical arc is not in the new book. |

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

## Salvage from prior framing

Existing chapter files in `chapters/` belong to the prior framing. Many will be archived; some salvage for the new direction:

| Current file | Status |
|---|---|
| `01_the_question.tex` | Partial salvage; opening framing for new Ch 1. |
| `02_the_library.tex` | Strong salvage; material for new Ch 4 (Solomonoff). |
| `03_the_indexing.tex` | Strong salvage; material for new Ch 1 (Bayes). |
| `04_the_prior.tex` | Salvage; material for new Ch 2 (The Prior Problem). |
| `05_the_optimality.tex` | Salvage; material for new Ch 4 (dominance theorem). |
| `06_the_slip.tex` | Archive (CUH work, not in new book). |
| `07_the_inhabited_library.tex` | Archive. |
| `08_the_observer.tex` | Partial salvage; "What an observer is" section reframes to new Ch 6 / Ch 7. |
| `09_indifference_of_measure.tex` | Archive. |
| `10_continuation.tex` | Archive. |
| `00_preface.tex`, `00_dedication.tex` | Archive; new frontmatter for new book. |
| `98_reading.tex`, `99_about.tex`, `99_also_by.tex` | Update for new book. |

Chapter archival happens incrementally; old chapters move to `chapters/archive/` as new chapters are drafted that supersede them.

## Repository Structure

```
multitudes/
├── multitudes.tex            # Main LaTeX file (will need updating for new structure)
├── chapters/                 # Chapter .tex files (mixed: old framing + new in progress)
│   └── archive/              # Archived chapters from prior framing (planned)
├── lore/                     # Pedagogical documentation (restructured)
│   ├── outline.md            # 12-chapter outline
│   ├── themes.md             # Thesis and voice
│   ├── direction.md          # Format, audience, pedagogy
│   ├── math-grounding.md     # Mathematical reference (needs updating)
│   └── archive/              # Old lore from prior framing
├── figures/                  # TikZ diagrams
├── images/                   # Bitmap images
├── kdp/                      # KDP publishing resources
└── Makefile                  # Build system (PDF, EPUB)
```

## Note on the pivot

The book began as a philosophical companion to *Worldlines* with a moral arc in Part II (grace as the chosen response to cosmic indifference). The moral salvage proved difficult to write at this length, and the author chose to restructure rather than force it. The technical material (AIT, Solomonoff, the library of programs, the observer-as-substructure framing) was the strongest part of the original work; the new direction takes that material as its spine and points it at a more concrete destination (AI safety understood mathematically).

The old framing is preserved in `lore/archive/`. If the moral / philosophical arc becomes its own book later, the material is intact.
