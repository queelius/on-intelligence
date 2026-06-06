# Foundations: The Bedrock and the Indexing Problem

The entire argument of this book rests on a small amount of mathematics and an inversion of intuition. The mathematics is not difficult and is, in its core form, settled. The inversion is the work the book does on the reader.

The bedrock is the algorithmic information theory of the 1960s: Solomonoff, Kolmogorov, Chaitin. The inversion: **generation is trivial; indexing is everything.** Once the reader feels that, the rest of the book is consequence.

### The principle of earned axioms

The book derives its bedrock the way Worldlines derives the constancy of $c$. Through everyday inquiry that ends somewhere the reader did not start. Chapter 1 begins with ordinary induction. You observe data; you predict. By Chapter 4 the reader has, without being asked to swallow anything, arrived at the universal prior and the dominance theorem. The mathematics is not imposed. It is the resolution of a puzzle the reader has been led to feel.

The speculative moves, the ones that turn an epistemology into an ontology, are introduced separately, at their natural entry points. Each is *labeled as a speculative move at the moment it enters*. The reader can always trace any conclusion back to bedrock or to a clearly flagged interpretive step. Nothing is hidden behind difficulty.

---

## The Bedrock

The bedrock is a single integrated edifice of probability and computation. It can be stated in three theorems and one definition.

### 1. Bayes' theorem (probability)

The structure of belief revision. Given prior $P(H)$ and likelihood $P(D \mid H)$, the posterior is

$$P(H \mid D) = \frac{P(D \mid H) P(H)}{P(D)}.$$

This is not philosophy. It is the only way to combine prior and likelihood that respects the axioms of probability (Cox's theorem). It tells you nothing about *which* prior to use. That is the entire problem of induction.

### 2. Kraft's inequality (the bridge)

For any prefix-free code over a finite or countable alphabet with codeword lengths $\ell_1, \ell_2, \ldots$:

$$\sum_i 2^{-\ell_i} \leq 1.$$

This is the entire reason "shorter" can be turned into "more probable." A prefix-free code is one in which no codeword is a prefix of another. A code that knows where it ends without external punctuation. Self-delimiting. Kraft says the lengths of such a code can be turned into a probability mass function by $P(i) = 2^{-\ell_i}$ (up to normalization).

Without prefix-free encoding, the sum $\sum_n 2^n \cdot 2^{-n}$ diverges. Prefix-free is exactly what makes "length implies probability" coherent. It is also exactly the structure of self-delimiting computation: a program that knows when it has finished reading its input.

### 3. The universal prior (Solomonoff)

Given a universal prefix Turing machine $U$, the universal prior is

$$M(x) = \sum_{p : U(p) = x*} 2^{-|p|}$$

where $x*$ means "$x$ as a prefix of the output." This is a probability distribution over strings, derived entirely from program lengths.

The deep fact is not the formula. The deep fact is what $M$ does.

### 4. The dominance theorem (optimality)

For any lower-semicomputable semimeasure $\mu$ (any probability distribution over data sequences that can be approximated from below by an algorithm), there exists a constant $c_\mu$ such that

$$M(x) \geq c_\mu \cdot \mu(x) \quad \text{for all } x.$$

Whatever computable distribution is generating your data, $M$ catches up to it. Its predictions converge to the true distribution at the same asymptotic rate as the true distribution itself, up to a multiplicative constant. The universal prior is *contained inside every other reasonable prior, up to a constant.* You cannot do better.

### 5. The invariance theorem (UTM-independence)

The prior $M$ depends on the choice of universal Turing machine. But for any two universal machines $U_1, U_2$, the priors $M_1, M_2$ differ by at most a multiplicative constant determined by the length of the cross-compiler between them:

$$M_1(x) \asymp M_2(x).$$

Asymptotically, the choice of UTM does not matter. The notion of "the universal prior" is well-defined up to a constant, and the constant becomes negligible as data accumulates.

---

## The Inversion: The Library and the Index

This is the book's pivot. It is the equivalent of Worldlines' "the speed of light is the invariant; space and time give." It is meant to leave the reader with an intuition they cannot un-think.

### Generation is trivial

The "generator" for reality, taken as the totality of all computable structures, is essentially a one-line program. Dovetail every program on every input. Equivalently: enumerate all binary strings. The Kolmogorov complexity of "the universe of all possible programs" is small. It is one of the cheapest objects describable.

This is the Library of Babel point, made formal. Borges' library contains every possible 410-page book. Generating it is trivial. The hard problem is locating any *specific* book. The one you wanted, or the one that describes your situation.

### The empty/universal duality

The empty set $\emptyset$ has zero elements. The universal set $V$ has all elements. They are complements. Both are *informationally cheap*: $K(\emptyset) \approx K(V) \approx$ small. The interesting sets, the ones with high $K$, are subsets that are neither trivial nor total. The information lives in the **cut**: the selection, the boundary, the index.

A theory that explains "everything" explains nothing. A theory that explains "nothing" explains nothing. A theory that explains *this* is the only interesting thing. The act of explanation is the act of indexing.

### Indexing is the hard problem

Given the trivial total, the Library, the question is: **where am I in it?** This is the question Bayesian inference has been answering all along, under another name. We update on observations to narrow the index. The simplicity bias is not aesthetic. It is the natural prior on indices, because shorter indices are more probable under Kraft.

Kolmogorov complexity $K(x)$ is exactly *the length of the shortest index that picks out $x$ from the Library*. Solomonoff induction is exactly *optimal indexing under uncertainty about the true index*. The dominance theorem says: this indexing scheme catches up to any other.

### The axiom of choice analog

The axiom of choice asserts that from any collection of nonempty sets, you can select one element from each, without a constructive rule for the selection. The selection exists in the structure even when no algorithm produces it.

The indexing problem is structurally similar. The Library contains every reality. Your reality is one of them. The function "your-index-given-your-observations" exists, but no algorithm computes it in finite time. Solomonoff induction is uncomputable (upper-semicomputable but not computable). You have a choice function (you must, because you live somewhere), but you have no constructive procedure for it. You proceed by approximation.

This is not a defect of the theory. It is a feature of the territory. *Choice exists in the structure; access to choice does not.* The reader who feels this has felt the deepest claim of the book.

### Why this inverts intuition

The naive view: reality is complicated; explaining it is the hard problem; the structure of "everything" is the deep mystery.

The inverted view: **the structure of "everything" is trivial. The deep mystery is your location in it.** What feels metaphysical (what is the universe?) is cheap. What feels practical (where am I?) is the load-bearing problem.

Every speculative move below operates within this inversion. The Mathematical Universe Hypothesis, the Many-Worlds Interpretation, observer-measure questions: these are not different theories of reality. They are different ways of refining the indexing problem.

---

## The Speculative Moves

The bedrock above is mathematics. The moves below are interpretive. Each is a substantive philosophical commitment that the book labels at the moment it enters and treats honestly. They are presented in the order the book introduces them, and the reader can accept or reject each move independently.

### Move I: Church-Turing applied to reality

**Claim:** The universe (or any process producing observable structure) is computable. The Church-Turing thesis, taken not as a claim about effective procedures but as a claim about physics, says the laws of nature are algorithmic.

**What it buys:** The bedrock applies to reality, not just to hypotheses. Solomonoff isn't just "how an ideal agent should learn." It is the right prior over the physical world. Bayesian indexing becomes ontological.

**What it costs:** A genuine metaphysical commitment. If physics involves uncomputable processes (real-valued precision in some load-bearing way, oracle-like quantum effects), the move fails. Most physicists accept it implicitly; few defend it explicitly.

**Burden of evidence:** Every physical process humans have measured has been computable, within the Turing-equivalent class. No experimentally confirmed phenomenon requires uncomputable physics. The negative case (that physics is uncomputable in some load-bearing sense) has no empirical support. Move I is the default empirical position; refusing it requires positive evidence, not just possibility.

**Status in the book:** Introduced in Chapter 6 ("The Slip"). The book takes it but flags it.

### Move II: Computable Universe Hypothesis (Tegmark IV, restricted)

**Claim:** All computable structures exist. The universal prior is not just a measure on hypotheses; it is a measure on *realities*. The Library of Babel is not a metaphor. It is the ontological status of the multiverse.

**What it buys:** A natural account of why we should expect to find ourselves in a "simple" universe. Short programs have higher measure, so observers in low-$K$ realities are more probable a priori. The simplicity bias becomes ontologically grounded rather than epistemically chosen.

**What it costs:** A vastly larger ontology. Realities you do not inhabit are as real as the one you do. The full Tegmark IV (all mathematical structures) has Gödelian issues; restricting to computable structures (CUH) closes those but is still a substantial commitment.

**The simplicity argument (from the cut inversion of Chapter 2):** A theory that says "only this universe exists" must specify *which* universe; the specification is a cut from the Library of computable possibilities, and the cut takes information. A theory that says "all computable structures exist" specifies nothing beyond the generator. By the cut principle, the unrestricted ontology is the informationally simpler one. The intuition that "just one world" is simpler is, by description-length, backwards. This is not a proof (applying a description-length principle to existence itself is a further step), but it inverts the standard Occam objection.

**The "nothing" question:** The classical "why is there something rather than nothing?" might seem to favor nothing as the simpler default. The cut principle does not settle this either way: nothing is the empty set, which (like the universal set) is informationally cheap. Both endpoints are cheap; both are complements of the same kind of thing. What excludes nothing is not simplicity but two other things. *Observation*: we exist, so any theory predicting that nothing exists is immediately falsified by our existence. *Coherence*: the concept of "no possibilities" seems to require a domain of possibilities from which to exclude, which may make "nothing" not fully coherent. The book notes this but does not pretend to resolve it.

**Status in the book:** Introduced in Chapter 6. The book takes it and shows what it implies.

### Move III: Many-Worlds Interpretation

**Claim:** The wavefunction is the complete description. Branching is real. Decoherence produces effectively non-interacting branches, each containing observers who experience definite outcomes.

**What it buys:** A second, independent route to the multiverse, and a stronger one than CUH. The same multiplicity conclusion is reached without invoking Tegmark IV, *and* it is reached from within physics that has already been experimentally confirmed to extraordinary precision. Under MWI, the wave function of the universe is itself a library-like structure: every possible outcome of every quantum event exists in some decoherent branch. The Library that CUH posits philosophically is, under MWI, already in our physics. MWI does not posit a library; it observes one.

**What it costs:** A specific interpretation of QM, but less than the alternatives. MWI is a reading of the unmodified Schrödinger equation; it asks only that no collapse postulate be added. Other interpretations (Copenhagen, Bohmian, GRW) avoid the branching but each adds something the unmodified theory does not require (a collapse mechanism, hidden variables, spontaneous-collapse dynamics). The reader who refuses MWI must adopt one of these positive alternatives. The Born rule (why outcomes have $|\psi|^2$ weight rather than uniform measure on branches) is a standing puzzle MWI must address, with substantial literature.

**Asymmetry with CUH:** CUH is a metaphysical addition. MWI is a refusal to add. Most of the uncomfortable implications the book catalogues in Chapter 8 (Boltzmann-like fluctuations, hellscape branches, dark continuation, versions of you doing or suffering anything physically realizable) are already permitted by MWI alone. CUH adds further structure (the full ontology of computable structures, not just our universe's branches) but is not required for most of the cascade.

**Status in the book:** Introduced in Chapter 8. The book takes it. CUH and MWI together give convergent evidence for the multiverse picture; MWI alone is sufficient for most of what follows.

### Move IV (NOT TAKEN): Observer-measure assumptions

**Drafting note:** The label "Move IV" is internal to these lore docs. The book itself does not refer to a "Move IV" in any chapter prose. The book introduces Moves I, II, III explicitly (in Chapters 6, 6, 8 respectively); the observer-measure ideas (SSA, SIA, the speed prior) are discussed in Chapter 8 without being labeled as a fourth move. This avoids the awkwardness of the book telling the reader "we considered taking a fourth move but didn't." That kind of deliberation is a lore concern, not a reader concern. When drafting or revising any chapter, mention SSA/SIA/speed prior by their content; do not name them as "Move IV" in prose.


**Claim:** "Where am I in the multiverse?" is a question with structure. You can ask: what fraction of observer-moments matching my self-description are in branch $A$ vs branch $B$? The answers depend on assumptions about how observers index themselves.

The two canonical assumptions:

- **Self-Sampling Assumption (SSA):** You are a random observer in your reference class. $P(\text{universe } U) \propto M(U)$.
- **Self-Indication Assumption (SIA):** Your existence is evidence of universes with many observers. $P(\text{universe } U) \propto M(U) \cdot N(U)$.

**What it would buy:** First-person predictions become possible. "What should I expect to observe?" has an answer (given assumptions).

**What it would cost:** A substantive commitment about indexicality. SSA and SIA give different answers in important cases (the Boltzmann brain problem, the doomsday argument, the Sleeping Beauty problem). Neither is forced; both are defensible.

**Status in the book: NOT TAKEN.** The book deliberately stops at three moves (I, II, III). The "where am I?" question is treated as one the framework permits but does not give a unique answer to. The book uses indexical reasoning informally where the reader naturally does, but does not commit to SSA, SIA, the speed prior, or any other formal observer-measure assumption.

The reasoning for this restraint: the book's broader discipline is *not to console with what is not true and not to engineer formal solutions to questions the framework does not actually answer*. Move IV, as deployed in the literature (especially via the speed prior to suppress Boltzmann brains), is an attempt to engineer a particular comfortable conclusion (you are probably an embedded observer with a real past). The book's posture is to accept the framework as it is: yes, you might be a Boltzmann brain; yes, hellscapes exist; the framework permits much that is uncomfortable. The chosen response to this is the project of Part II, not a formal move.

The speed prior and SSA/SIA remain useful as technical references (see math-grounding.md), but the book does not endorse any of them.

---

## The Cascade

The book is structured so that every conclusion in Part II can be traced to one of the bedrock theorems plus one or more clearly labeled speculative moves.

**Bedrock alone** gives:

- Bayesian indexing is well-posed.
- The simplicity bias is mathematical structure, not aesthetic preference.
- Solomonoff is asymptotically optimal among computable learners.
- The choice of UTM is asymptotically irrelevant.

**Bedrock + Move I (Church-Turing)** gives:

- The universal prior applies to reality.
- Optimal learning catches up to whatever the world is doing.

**Bedrock + Moves I, II (CUH)** gives:

- The universal prior is a measure on realities.
- The Library of Babel is the ontological substrate.
- Multiplicity of realities is a structural fact, not a thought experiment.

**Bedrock + Moves I, III (MWI)** *without* CUH already gives most of the cascade:

- The wave function of the universe is itself a library-like structure: every quantum outcome exists in some decoherent branch.
- Multiplicity is in our physics, not just in philosophy.
- Almost all of the uncomfortable implications below (Boltzmann-like fluctuations, hellscape branches, dark quantum continuation, versions of you doing or suffering any physically realizable thing) follow from MWI alone, without invoking CUH.
- This matters because MWI is a refusal to add a postulate to physics already accepted; CUH is a metaphysical addition. The reader who accepts QM but refuses CUH still inherits most of the costs.

**Bedrock + Moves I, II, III** gives the full picture the book commits to:

- A second, independent route to multiplicity (CUH from philosophy of mathematics; MWI from foundations of physics).
- Convergent evidence: the Library shows up in two different traditions arriving at the same kind of structure.
- **The indifference of measure.** The Library contains every reality. The measure on the Library has no preference about which index is yours. You are a class of patterns in the Library, instantiated at many indices, with no privileged self-identification. This is the equivalent of Worldlines' "indifference of geometry," one level deeper.
- The "where am I?" question becomes acute, but the book does not give it a formal answer (Move IV is deliberately not taken).
- The Boltzmann shadow appears, but the book does not engineer it away.
- Quantum immortality, hellscapes, Boltzmann observer-moments with arbitrary memories, and other uncomfortable possibilities are all permitted by the framework. The book catalogues them honestly (Chapter 8) and the chosen response of Part II is the answer the book offers in their place, not a formal move that would dissolve them.

---

## What the Bedrock Does Not Provide

The bedrock and the moves above are silent on:

- **Why there is something rather than nothing.** The Library does not explain why it exists. CUH says all computable structures exist; it does not say why this should be the case. (Discussed more fully under Move II, "The nothing question.")
- **The hard problem of consciousness.** The book brackets this. It is about the structure observers inhabit, not about why structures are observed.
- **The choice of UTM at finite scales.** The invariance theorem makes UTM-choice asymptotically irrelevant. For any finite agent with finite data, the constants matter. This is sometimes called "no free lunch for Solomonoff."
- **Which speculative moves are *correct*.** The book takes them seriously and follows their consequences. It does not claim to have proven any of them.
- **Whether the indexing problem has a solution we can access.** The choice function exists; we approximate it. There is no procedure that converges to "the true index" in finite time on bounded resources.
- **First-person indexical probabilities across the multiverse.** The book deliberately stops at three moves. Moves III and CUH (Move II) give multiplicity; the book does not take a fourth move that would commit to a specific indexical assumption (SSA, SIA, the speed prior, etc.). The "where am I?" question is treated as open. The Boltzmann brain hypothesis is treated as one of many uncomfortable possibilities the framework permits, not a problem to be resolved by adjusting priors.
- **The coherence of mathematics itself.** The book presupposes that mathematics is coherent in the standard sense (no contradiction, separable from incompleteness in Gödel's sense). No contradiction in mathematics has been found in over a century of foundational work, but this is an empirical claim about the practice of mathematics, not a proof. If mathematics turns out to be incoherent in some load-bearing sense, the concept of "computable structure" may fail to pick out anything determinate, and the framework dissolves. The book takes coherence as a working assumption and flags it here.

These are the honest limits. The reader who follows the cascade should always be able to ask: "Which axiom does this conclusion rest on?" and "Which speculative move is being made?" The answers should always be visible.

---

## The Discipline

The book's discipline:

1. **Bedrock is bedrock.** Mathematical theorems are presented as theorems. They are not negotiable.
2. **Speculation is labeled.** Each interpretive move is flagged at its entry. The reader is never asked to confuse mathematics with metaphysics.
3. **The cascade is traceable.** Every conclusion can be unwound to its source: a theorem, a move, or both.
4. **The indexing inversion is the spine.** Generation is trivial. Indexing is everything. The book returns to this whenever the math threatens to feel abstract.
5. **The reader is never alone with difficulty.** If a step is hard, the book pauses. If a step is interpretive, the book labels it. The reader who follows from Chapter 1 has all the tools by Chapter 7. What remains is to see what they build.
