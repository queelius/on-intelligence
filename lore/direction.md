# Direction

## Format

LaTeX, book class, similar to Worldlines. Chapters in `chapters/NN_name.tex`. TikZ for diagrams. Same build system (Makefile, pdflatex multi-pass, EPUB via pandoc).

## Audience

Determined but lay readers. Specifically: a reader who is curious about AI, willing to work for understanding, but does not have a formal mathematical background beyond high school algebra. Comparable readers:

- The kind of person who reads Penguin science books (Carroll, Tegmark, Frayn, Greene).
- The educated generalist who has heard of Bayes but never derived it.
- The professional in an adjacent field (programmer, engineer, scientist in another discipline) who wants the conceptual core of AI without slogging through a textbook.
- Policy people, journalists, and students who want to discuss AI responsibly without being captured by hype or doom.

Not the audience: AI researchers (they know this material), pure mathematicians (they want proofs), the casual reader who skims (the book is short but not shallow).

## Tone

Warm. Direct. Honest. The reader is treated as intelligent and willing to work.

- Use "you" to address the reader.
- Use "I" sparingly, where the author is making a personal statement.
- Explain math conceptually first, then formalize. The conceptual explanation does most of the work; the formalism makes it precise.
- When the math is settled, say so. When the field is contested, say so.
- No hedging that becomes hand-wringing. No false certainty either.

## Voice rules

The Towell voice (from `~/.claude/CLAUDE.md` and the soul plugin):

- **No em-dashes.** Use commas, periods, colons, or parentheses.
- **Plain and direct.** Short sentences. Period for emphasis.
- **No hype.** Corporate buffer language and signaling phrases are banned. The soul plugin enforces this with a hook; the full list is there.
- **Earned conclusions.** The math earns the claim. Do not declare; build.
- **No false intimacy.** Warm but not chummy. Direct without performing friendship.

## Pedagogy

The pedagogical commitment: every chapter teaches one or two core ideas. The ideas are introduced through example or visualization first, then named, then formalized. The reader meets the concept before meeting the symbol for it.

Concretely:

1. **Open with a problem.** A concrete situation the reader can hold in mind. The coin trick, the boat going in circles, the chess position, the next-token loop.
2. **Develop the concept.** What is the structure of the problem? What does the solution look like in everyday terms?
3. **Name and formalize.** Now we have a name (Bayes, Solomonoff, Goodhart). Now we have the equation or the algorithm.
4. **Show the consequence.** What does this commit us to? What does it rule out? What does it tell us about real systems?
5. **Diagrams throughout.** The visual track does most of the conceptual lifting.

## Diagrams

**The commitment:** every equation gets a diagram. Every algorithm gets a diagram. Every concept that can be visualized should be.

This is not a stylistic preference. It is a pedagogical commitment to a lay audience. The mathematics will be unfamiliar; the visual track is how the reader builds intuition.

**Implementation:**

- TikZ for all diagrams, like Worldlines. Vector graphics, sharp at any zoom.
- Diagrams are designed alongside the prose, not bolted on. The diagram's caption is part of the chapter's argument.
- Consistent visual style: same fonts, same color palette, same conventions for arrows, boxes, and emphasis. Build a small set of visual primitives and reuse them.
- Some diagrams are static (architectures, trees, side-by-side comparisons). Some animate the argument over multiple panels (showing an update step by step).

**Color palette (proposed):** blue for prediction / theory, red for action / practice / safety concerns, gray for context. Greens, oranges as accents. Print-friendly (book is intended for KDP paperback).

**Typography in diagrams:** match the body text. No system fonts.

**Caption length:** captions are part of the argument. A diagram can have a one-line caption (when the picture speaks) or a paragraph caption (when the picture is making a point that the body text references).

## LaTeX conventions

- Math mode for all symbols: $K(x)$, $M(x)$, $\sum$, $\Omega$, $\to$. No raw unicode for mathematical notation in body text.
- Inline math: `$...$`. Display math: `$$...$$` or `\begin{equation}...\end{equation}`.
- Theorem environments where formal precision is being claimed.
- Diagrams: TikZ, with figure environment and label. Captions descriptive.
- Bibliography: BibTeX, references in `references.bib`. Citations sparing in body text (lay audience); fuller in a recommended-reading section at the back.

## Comparable works

- **Hawkins, *On Intelligence* (2004).** Same title register, different content. Hawkins focused on cortical algorithms; this book focuses on the universal-agent tradition.
- **Hutter, *Universal Artificial Intelligence* (2005).** The technical reference for AIXI. This book covers the same conceptual core for a lay audience.
- **Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018).** The RL textbook. Similar conceptual core, different audience.
- **Sean Carroll, *Something Deeply Hidden* (2019).** Tone reference for explaining technical material to a general reader.
- **Max Tegmark, *Our Mathematical Universe* (2014).** Comparable in scope (ambitious technical claims, lay audience).
- **Daniel Dennett's late work.** Conceptual clarity over technical depth.

## Length and format

- **Length:** No fixed word-count target; sized by what the material warrants. 17 chapters in 4 parts. (Per-chapter figures in `outline.md` are descriptive pacing guides, not budgets.)
- **Format:** book-length nonfiction. KDP paperback (6 x 9 trim).

## KDP considerations

- Cover: similar minimalist design to Worldlines and Clankers. Series-coherent visual identity.
- ISBN, copyright, dedication, preface, table of contents, body, further reading, about the author, "also by Alex Towell."
- Pricing tier consistent with previous books.

## Drafting workflow

The book is drafted with the worldsmith plugin assisting. Lore docs in `lore/` are the foundation:

- `lore/outline.md`: chapter structure, salvage plan, drafting order.
- `lore/themes.md`: thesis, central themes, voice.
- `lore/direction.md`: this document. Format, audience, pedagogy.
- `lore/math-grounding.md`: reference for the mathematical claims. Updates needed: drop the MWI/CUH/observer-measure material (which belonged to the old framing); keep Cox, Kraft, Solomonoff, dominance; add RL, utility theory, AIXI; possibly add LLM / transformer math.

Chapter-specific lore docs (e.g., `lore/aixi.md`, `lore/llms.md`, `lore/safety.md`) can be added as drafting proceeds, especially for the substantial closing chapter.

When drafting, consult: `outline.md` (for the chapter's role and word count), `themes.md` (for thesis and voice), this `direction.md` (for format and pedagogy), `math-grounding.md` (for the math).

## What was archived

The old framing of the book (philosophical companion to Worldlines, with grace / multitudes / indifference of measure thesis) is in `lore/archive/`. The mathematical content was solid; the philosophical / moral arc was the part that did not work at this length. The new direction takes the strongest material (AIT, Solomonoff, the library of programs, the observer-as-substructure framing) and repurposes it as the spine of a technical introduction with a different destination.

Old lore docs in `lore/archive/`:
- `foundations.md`: the old bedrock + cascade. Math salvage; philosophical structure does not transfer.
- `themes.md`: old themes (cosmic indifference, grace).
- `direction.md`: old direction (philosophical nonfiction, Worldlines pair).
- `outline.md`: old 14-chapter outline (two parts).
- `grace.md`: the destination of the old book.
- `implications.md`: what multiplicity does to human concepts.
- `index.md`: the index-as-abstraction work (developed late; partially relevant to new Ch 4–5).
- `apokatastasis.md`, `landing.md`, `information_hazards.md`: late-stage worry docs.

These are kept for reference; if the philosophical / moral arc becomes a separate book later, the material is preserved.
