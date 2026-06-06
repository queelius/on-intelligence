# Integration Pass: *On Intelligence and Its Specifications* (full book)

**Date:** 2026-06-05
**Scope:** `book` (17 chapters, 4 parts, plus substantive back matter)
**Supersedes:** `2026-06-04-book-integration-pass.md` (written when the book was 16 chapters, before the Part IV restructure; now stale).
**Review references:** `docs/superpowers/reviews/2026-06-03-book.md` and `docs/superpowers/reviews/2026-06-05-book.md`, plus a structural-coherence audit and an adversarial overclaim audit run 2026-06-05 (results folded into the manuscript; see Changes below).
**HEAD SHA at integration time:** N/A. This project is **not a git repository** (`git rev-parse` reports no work tree). The record is written but not committed; see Versioning note.
**Build command:** `latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -shell-escape %O %S" on-intelligence.tex`

---

## 1. Verification Results

| Check | Result | Detail |
|---|---|---|
| Build (latexmk to pdflatex) | **PASS** | exit 0, converges, 214 pages |
| LaTeX errors | **PASS** | 0 |
| Overfull `\hbox` (margin overflow) | **PASS** | 0 |
| Overfull `\vbox` (vertical overflow) | **PASS** | 0 |
| Underfull `\hbox` | **NOTE** | 2 (cosmetic loose lines; not visible defects) |
| Multiply-defined labels (active build) | **PASS** | 0 |
| Undefined references | **PASS** | 0 |
| Cross-reference integrity | **PASS** | 43 labels unique; 44 `\ref`s all resolve (see section 3) |
| Voice (no em-dashes) | **PASS** | 0 em-dashes across all active files |
| Macro-leak (raw LaTeX in PDF text) | **PASS** | 0 leaked macros; the single `??` is the intentional `mesa-objective: ???` node in `fig:base-mesa` |
| Word budget | **N/A** | No fixed word target (author direction). Figures recorded for reference only. |
| Running-thread continuity | **PASS** | spine threads carry through; the new "second scaling curve" thread runs 14 to 16 to 17 (see section 4) |

**Overall: GREEN.** Build clean, cross-references intact, voice rules hold. No blocking items.

---

## 2. Per-Part Page and Word Totals

Page spans from `on-intelligence.toc`; word counts via `detex | wc -w` (includes figure captions and TikZ label text, so they run above pure prose).

| Part | Chapters | Pages | Words (detex) |
|---|---|---:|---:|
| I. Prediction | 1 to 4 | 36 | 7,204 |
| II. Decision | 5 to 8 | 42 | 10,099 |
| III. The Specification Problem | 9 to 12 | 40 | 10,430 |
| IV. Reality | 13 to 17 | 60 | 17,552 |
| Notes and End Matter | 97, 97b, 98, 99 (x2) | 36 | n/a |
| **Body total (ch 1 to 17)** | | **178** | **45,285** |

Per-chapter (detex): ch13 = 4,240, ch17 = 4,218, ch11 = 3,392, ch14 = 3,332, ch16 = 2,997, ch07 = 2,959, ch15 = 2,765, ch08 = 2,562, ch12 = 2,542, ch05 = 2,414, ch10 = 2,322, ch04 = 2,231, ch09 = 2,174, ch06 = 2,164, ch01 = 1,740, ch03 = 1,645, ch02 = 1,588.

Part IV is now the largest part (60 pp). It carries the two new chapters (Ch 16 *What's Ahead*, Ch 17 *Teaching Sand to Think*) and the expanded Ch 14 (policy gradient plus the second-scaling-curve section).

---

## 3. Cross-Reference Map (summary)

- **43 figure labels**, each defined exactly once; **0 multiply-defined** among active files.
- **44 `\ref`s**, every one resolves; **0 `\Cref`/`\autoref`/`\eqref`/`\pageref`**; **0 undefined**.
- No chapter carries a `\label{ch:...}`: chapters are referenced **by typed numeral in prose** (e.g. "Chapter 16"), not by `\ref`.
- One cross-chapter `\ref`: ch 11 references `fig:goodhart-curve` (defined ch 9). Resolves.
- Ch 16 now defines four figure labels: `fig:math-forecast`, `fig:jagged`, `fig:scaling-law`, `fig:compute-moore` (the last two added this cycle).
- The 16-to-17 renumbering (old "The Stakes" became Ch 17) left no dangling "Chapter 16 means the stakes" prose references; all such references were converted to role-based phrasing ("the final chapter", "what follows") or updated.

---

## 4. Running-Thread Inventory

| Thread | Chapters |
|---|---|
| Solomonoff | 3, 4, 5, 6, 7, 8, 13, 16, 17 |
| AIXI | 4, 5, 6, 7, 8, 9, 11, 12, 13, 17 |
| "the gap" | 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17 |
| Goodhart | 5, 6, 9, 10, 11, 12, 14, 17 |
| situational awareness | 10, 17 |
| second scaling curve (RL) | 14, 16, 17 |
| the stand / prize / "sand" | 1, 9, 11, 16, 17 |

Continuity is sound and improved this cycle. The "second scaling curve" through-line (the action-side-of-AIXI hypothesis) is introduced in Ch 14, used as a trajectory driver in Ch 16, and reaches its climax in Ch 17, so it reads as one idea rather than three scattered mentions. The "where the optimization was spent" principle (inductive bias) is now named explicitly in Ch 16 as one principle spanning Ch 7, Ch 13, and the jagged edge.

---

## 5. Changes Since the Last Pass (2026-06-04)

The book was restructured and expanded substantially after the prior record:

**Structure (16 to 17 chapters).** New **Ch 16, *What's Ahead*** (the trajectory: honest scaling decomposition, economics of continuation, benchmarks and forecaster-underestimation, the jagged edge, the burden-has-shifted stand, recursive self-improvement). The former "The Stakes" became **Ch 17, *Teaching Sand to Think***, the finale, fusing the conceptual stand (prediction is intelligence; real minds; no magic substrate), the upside (the prize), and the stakes (the CoT-cordon material).

**The second-scaling-curve through-line (Ch 14 to 16 to 17).** The hypothesis that large-scale RL scales general competence the way pretraining scaled prediction, framed as the empirical action-half of AIXI. Introduced in a new Ch 14 section, used as a driver in Ch 16, climaxes in Ch 17.

**Coherence pass (structural-audit findings).** Named the "where the optimization was spent" pattern (Ch 16); added connective signposts to Ch 16's section seams; marked the jagged edge as a hinge (shape, not rate); cashed the I. J. Good promise in a new Ch 17 "The prize" section to restore the danger/promise balance.

**Overclaim corrections (adversarial-audit findings).** Corrected a backwards empirical claim in Ch 14 (the RL out-of-distribution generalization sentence now reports the literature honestly as mixed, leaning toward the sharpening view); added hedges on the RL-scaling-curve maturity (younger, may ceiling), re-aimed the AIXI-mapping hedge in Ch 17 to cover the looseness of the analogy, and admitted the physical-experiment rate limit in "The prize."

**Prior review findings fixed.** B1 to B5 (2026-06-03) and S5, S6, S8, S9, S13 were fixed and verified in earlier cycles. S5 (Secret Agenda) gained an arXiv footnote; S6 (METR) states both the 7-month and 4-month doublings; S8 (Betley 2025) added to Ch 15 and Further Reading.

**Other.** Preface rewritten in a more opinionated register. Ch 14 gained a policy-gradient paragraph (PPO/GRPO). Four new figures across the new chapters. Further Reading gained six entries (Steinhardt, Epoch AI, Anthropic RSI, Moravec, Andy Clark, Betley). *A Note on Consequences* gained the Moravec automation-order beat. `direction.md` length/trim line corrected.

---

## 6. Known Deferred Items (documented, resolve correctly)

1. **Prose-numbered chapter references are not build-verified.** Chapters and Parts are referenced by typed numeral, not `\label{ch:...}` plus `\Cref`. All current references are in range and correct, but a future reordering would require a manual re-check. (Maintainability, not a defect.)
2. **Two label collisions with archived files** (`fig:dominance` with `05_the_optimality.tex`; `fig:bayes-counting` with `03_the_indexing.tex`). The archived files are commented out of `on-intelligence.tex` and never compiled, so there is no active collision. Expected.
3. **Two underfull `\hbox`**: cosmetic loose lines, not visible defects.

---

## 7. Open Follow-Ups

None blocking. For a future polish cycle:

- **Minor citation precision** (carried from 2026-06-05 review, all LOW): CoastRunners date is correct at 2016 (verified; a prior review claim of 2017 was wrong); the archived-label rename (item 2 above) if those files are ever touched; optional brain-FLOP and scaling-law footnote tightening already addressed in part.
- **Maintainability:** consider `\label{ch:...}` plus `\Cref` for chapters to make cross-chapter references reorder-safe.
- The speculative second-scaling-curve material has now passed an adversarial overclaim audit; if the RL-generalization literature shifts, the Ch 14 "second scaling curve" cautions and the Ch 17 "other half" hedges are the passages to revisit.

---

## Versioning note

This project is **not under git**. The integration skill's commit step could not run. The record is saved to `docs/superpowers/plans/2026-06-05-book-integration-pass.md`. If versioning is wanted, run `git init` and commit the manuscript plus this record; the integration pattern then becomes reproducible against a SHA.

---

*Integration pass: mechanical check, cross-reference map, per-Part totals, running-thread inventory, voice and macro-leak audit. Cross-reference integrity GREEN; build clean (214 pp); voice rules hold.*
