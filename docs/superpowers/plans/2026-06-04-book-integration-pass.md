# Integration Pass: *On Intelligence and Its Specifications* (full book)

> **SUPERSEDED (2026-06-05).** This record predates the Part IV restructure (the 16-to-17-chapter expansion: new Ch 16 *What's Ahead* and the Ch 17 *Teaching Sand to Think* finale) and the element-5 / coherence / overclaim work. See `2026-06-05-book-integration-pass.md` for the current state. Kept for history.

**Date:** 2026-06-04
**Scope:** `book` (all 16 chapters across 4 Parts plus substantive back matter)
**Plan / review reference:** `docs/superpowers/reviews/2026-06-03-book.md` (full-book multi-agent review, 30 findings)
**HEAD SHA at integration time:** N/A. This project is **not a git repository** (`git rev-parse` reports no work tree). The record is written but **not committed**; see "Versioning note" below.
**Build command:** `latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode -shell-escape %O %S" on-intelligence.tex`

This pass mirrors the Bernoulli Plan 4/8/13/15/18 Task 10 integration pattern: mechanical check, cross-reference map, per-Part totals, running-thread inventory, voice and macro audit, deferred-items list, and polish follow-ups.

---

## 1. Verification Results

| Check | Result | Detail |
|---|---|---|
| Build (latexmk to pdflatex) | **PASS** | exit 0, converges in 3 passes, 196 pages |
| LaTeX errors | **PASS** | 0 |
| Overfull `\hbox` (margin overflow) | **PASS** | 0 |
| Overfull `\vbox` (vertical overflow) | **PASS** | 0 |
| Underfull `\hbox` | **NOTE** | 1 (the "Orthogonality:" section heading, set slightly loose to avoid a former 9.5 pt margin bleed; cosmetic) |
| Multiply-defined labels (active build) | **PASS** | 0 |
| Undefined references | **PASS** | 0 (baseline preserved) |
| Cross-reference integrity | **PASS** | 39 labels unique; 40 `\ref`s all resolve (see section 3) |
| Per-Part page totals | **PASS** | within plausible spec band (see section 2) |
| Word budget vs spec | **N/A** | No fixed word target (author direction, 2026-06-04). Body about 40,055 detex / roughly 35 to 37k prose; recorded for reference, not as a constraint |
| Voice audit (no em-dashes) | **PASS** | 0 em-dashes in typeset output. The three hits in ch 7 are decorative comment-divider lines in the TikZ source (percent-sign comments), not typeset output |
| Hype / buffer language | **PASS** | 1 hit, inside the Sutton "Bitter Lesson" epigraph (ch 13), a verbatim quotation preserved as-is; no authorial-prose hits |
| Macro-leak (raw LaTeX in PDF text) | **PASS** | 0 leaked macros; 0 stray refs (the single `??` is the intentional `mesa-objective: ???` node in `fig:base-mesa`) |
| Running-thread continuity | **PASS** | spine threads run continuously (see section 4) |

**Overall: GREEN.** No blocking integrity failures. One word-budget follow-up and the standing review backlog remain for the polish plan.

---

## 2. Per-Part Page and Word Totals

Page spans from `on-intelligence.toc` (printed page numbers); word counts via `detex | wc -w` per active chapter (note: detex includes figure captions and TikZ label text, so counts run about 10 to 15 percent above pure prose).

| Part | Chapters | Printed pages | Pages | Words (detex) |
|---|---|---|---:|---:|
| I. Prediction | 1 to 4 | 1 to 36 | 36 | 7,204 |
| II. Decision | 5 to 8 | 37 to 78 | 42 | 10,099 |
| III. The Specification Problem | 9 to 12 | 79 to 118 | 40 | 10,397 |
| IV. Reality | 13 to 16 | 119 to 162 | 44 | 12,355 |
| Notes and End Matter | 97, 97b, 98, 99 (x2) | 163 to end | about 26 | 3,344 (97 plus 97b) |
| **Body total (ch 1 to 16)** | | **1 to 162** | **162** | **40,055** |

Preface: 465 words. **No fixed word target** (author direction, 2026-06-04): the book is sized by what the material warrants. The figures above are recorded for reference and pacing, not as a budget. (Prior docs stated 24k to 35k targets; superseded.)

Largest chapters (trim candidates): ch 13 (4,201), ch 11 (3,394), ch 7 (2,959), ch 16 (2,956).

---

## 3. Cross-Reference Map (summary)

Full map produced by `cross-ref-auditor` this pass. Headlines:

- **39 figure labels**, defined exactly once each; **0 multiply-defined** among active files.
- **40 `\ref`s**, every one resolves; **0 `\Cref`/`\autoref`/`\eqref`/`\pageref`**; **0 undefined**.
- No chapter carries a `\label{ch:...}`: chapters are referenced **by typed numeral in prose** (for example, "Chapter 15"), not by `\ref`.
- One cross-chapter `\ref`: ch 11 references `fig:goodhart-curve` (defined ch 9). Resolves. (This is why ch 11 shows 4 refs against 3 local labels.)
- Every defined label is referenced at least once (no orphans).

Per-chapter label counts: ch1=2, ch2=2, ch3=2, ch4=3, ch5=3, ch6=2, ch7=4, ch8=2, ch9=2, ch10=2, ch11=3, ch12=2, ch13=4, ch14=2, ch15=2, ch16=2.

Cross-chapter forward/backward prose references were spot-checked and are subject-matter-correct (for example, ch 12 and ch 16 on the CoT probe; ch 10 to ch 15 on situational awareness). All within range 1 to 16 / I to IV.

---

## 4. Running-Thread Inventory

Spine threads and the chapters that carry them (case-insensitive presence):

| Thread | Chapters |
|---|---|
| Solomonoff | 3, 4, 5, 6, 7, 8, 13, 16 |
| AIXI | 4, 5, 6, 7, 8, 9, 11, 12, 13, 16 |
| "the gap" | 5, 7, 8, 9, 11, 12, 13, 14, 15, 16 |
| Goodhart | 5, 6, 9, 10, 11, 12, 14, 16 |
| specification | 1, 3, 5 to 16 |
| situational awareness | 10, 16 |
| cordon (CoT probe) | 16 |

Continuity is sound. The spine (Bayes, then Solomonoff, then AIXI, then specification, then gap) is introduced where expected and recurs through Part IV. **"Situational awareness" now appears in both ch 10 and ch 16**, the consistency added by this pass's B3 fix (previously it read as a future threshold in ch 10 and a present gradient in ch 16; now both treat it as a contingent, already-present premise cross-referenced to ch 15). "Cordon" is correctly a ch 16-local device.

---

## 5. Fixes Applied This Pass (blocking findings from the review)

All five BLOCKING findings from `2026-06-03-book.md`, plus S9, fixed and verified in-build:

| ID | Fix | Files |
|---|---|---|
| B1 | Chess corrected to $10^{44}$ legal positions (was $10^{120}$ game-tree number); now consistent with ch 7 and the Go position count | `06_reinforcement_learning.tex` |
| B2 | Footnote with the real Solomonoff KL convergence bound $\sum_t \mathbb{E}_\mu[\mathrm{KL}(\mu\|M)] \le K(\mu)\ln 2$ (Hutter 2001/2005), matching `math-grounding.md` section 2 | `04_solomonoff_induction.tex` |
| B3 | Deceptive alignment reframed as a conditional result; situational awareness named as the contingent, load-bearing premise; cross-referenced to ch 15 | `10_inner_alignment.tex` |
| B4 | Footnote making AIXI's $V^*$ fixed-point self-reference explicit, tied to the Bellman optimality equation (ch 6) | `08_aixi.tex` |
| B5 | Footnote making *A Philosophical Note* reachable from the main text (anchored to the Library/$M$ thread) | `04_solomonoff_induction.tex` |
| S9 | Ch 16 caption disambiguates the orange arrow as outer-loop selection (training loop, not per-token loss) | `16_the_stakes.tex` |

Build after fixes: 0 overfull, 0 undefined refs, 196 pp, no errors, no em-dashes.

---

## 6. Known Deferred Items (documented, resolve correctly)

These are intentional or expected; recorded so they are not re-flagged as defects:

1. **Prose-numbered chapter references are not build-verified.** Chapters and Parts are referenced by typed numeral, not `\label{ch:...}` plus `\Cref`. All current references are in range and correct, but a future chapter reordering would require a manual re-check. (Advisory from cross-ref-auditor; maintainability, not a defect.)
2. **Two label collisions with archived files** (`fig:dominance` with `05_the_optimality.tex`; `fig:bayes-counting` with `03_the_indexing.tex`). The archived files are commented out of `on-intelligence.tex` and never compiled, so there is no active collision. Expected; flagged by review as M1/M2.
3. **One underfull `\hbox`**: the "Orthogonality:" heading is set slightly loose, the deliberate trade for eliminating a 9.5 pt margin bleed. Cosmetic.

---

## 7. Open Follow-Ups for the Polish Plan

Carried forward from the review (`2026-06-03-book.md`) and this pass. None block the integration GREEN, but all should be addressed before publication.

**F1. Word budget: withdrawn.** Per author direction (2026-06-04) there is no fixed word-count target; the book may be as large as the material warrants. The earlier over-budget concern and trim-candidate list are withdrawn. Review S7 (ch 14 problem-finding) and the ch 16 length note stand only on their own pedagogical merits, not on a budget.

**F2. Buffer-verb hit, resolved (this pass).** The hype audit's one hit is inside the Sutton "Bitter Lesson" epigraph in ch 13, a verbatim quotation. It is preserved as quoted and is not an authorial voice violation. No action needed; recorded for transparency.

**Substantive review findings not yet fixed (S-series, minus S9):**

- S5: "Secret Agenda 2025" (ch 12) is uncitable; supply arXiv ID or paraphrase.
- S6: METR doubling time. Ch 13 says "seven months", outline says "about 4 months"; verify vs Kwa et al. 2025.
- S8: Betley 2025 "Emergent Misalignment" is in the ch 15 outline but missing from the chapter.
- S13: Ch 15 "LLM results make the formal results load-bearing" inverts the intended direction; check ch 15 and the echo in ch 16.
- S10: Preface omits ch 14 from the Part IV summary.
- S1 to S4, S7, S11, S12, S14: see review for the remaining scope/precision items.

**Minor review findings (M-series):** label hygiene on archived files (M1/M2), citation-precision items (M3 to M10), missing scaling-law diagram (M11). See review for the full list.

**Maintainability:** consider adding `\label{ch:...}` plus `\Cref` for chapters to make cross-chapter references reorder-safe (deferred item 1).

---

## Versioning note

This project is **not under git**. Step 7 of the integration skill (record HEAD SHA, commit the record) could not run. The record is saved to `docs/superpowers/plans/2026-06-04-book-integration-pass.md`. If versioning is wanted, run `git init` and commit the manuscript plus this record; the integration pattern then becomes reproducible against a SHA.

---

*Integration pass executed by the bookwright integrate workflow: mechanical check, cross-ref-auditor map, per-Part totals, running-thread inventory, voice and macro-leak audit. Cross-reference integrity GREEN; build clean; one word-budget follow-up recorded.*
