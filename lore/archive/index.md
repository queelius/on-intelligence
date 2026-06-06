# Index

This document is about a clarification the book needs but has not yet made: the index is itself an abstraction, observer-imposed, parallel to identity. The bookshelf metaphor that has carried the Library through Part I is a working tool. The structure underneath has no bookshelf in it.

## The terminology overload

The word "index" has been doing two jobs.

**Index (Ch 3 sense).** The act of probabilistic restriction. Indexing as activity. The book introduces it in Ch 2 and develops it in Ch 3: indexing = conditioning = $P(\cdot \mid \text{data})$. From Ch 2: *"what you have, when you stand in front of a wall of identical-looking volumes, is a problem of indexing: a way of picking out, from the totality of what could be written, the part that is relevant to where you are."* This is the verb sense. Where am I in the Library? Bayes answers.

**Index (structural sense).** The discrete labels we attach to regions of the Library. Books on shelves. Coordinates. Bitstrings as items in an enumeration. Indexing as apparatus. This is the noun sense. The discrete-items framing the book has used without acknowledging that it is observer-imposed.

This document is about the second sense.

## The mathematical reality

In algorithmic information theory: a universal prefix Turing machine $U$ and the universal distribution

$$M(x) = \sum_{p : U(p) = x} 2^{-|p|}.$$

Programs go in, outputs come out, weighted by description length. No books. No shelves. No indices anywhere in the mathematics.

The "bookshelf" is the librarian's imposition; the structure underneath is program-output space, with whatever internal regularities programs happen to have. Borges' books and Tegmark's discrete mathematical structures are convenient discretizations of a continuous (or at least, undecomposed) substrate.

### The substrate vs U(p): same set, different measure

Set-theoretically, $\{p \in \{0,1\}^*\}$ and $\{U(p) : p \in \{0,1\}^*, p \text{ halts}\}$ are equal. Every bitstring is the output of some halting program (e.g., "print $x$; halt"), and every halting output is a bitstring. What differs is the *measure*.

$\{0,1\}^*$ as a bare set has no natural measure. Every bitstring is just available.

$\{U(p) : p \in \{0,1\}^*\}$ with weighting $2^{-|p|}$ summed over programs producing each output yields the universal prior

$$M(x) = \sum_{p : U(p) = x\star} 2^{-|p|}.$$

The interesting object is the measure, not the set. Strings of the same length get wildly different $M$-values: those with many short descriptions are heavy, those that are algorithmically random are light.

Where computability enters: defining $M$, defining compression as explanation, defining Solomonoff induction. The substrate alone gives passive strings; the UTM gives each string a set of explanations (the programs that produce it).

## The multiverse contains its own generator

The dovetailed generator we use to enumerate $\mathcal{M}$ is itself a small bitstring. Call it $p_{\text{gen}}$. Then:

- $p_{\text{gen}} \in \{0,1\}^*$. It is a bitstring like any other.
- $U(p_{\text{gen}})$ enumerates all of $\mathcal{M}_U$.

The multiverse contains its own generator as a tiny element of itself. The information needed to specify the multiverse is contained in the multiverse, in a few hundred bits. This is one face of the fixed-point property of universal computation: $U$ is universal precisely because some program $U$ can run simulates $U$ running on everything.

Two consequences:

- **Self-describing.** The library knows how to make itself. Specifying the totality is informationally trivial.
- **Recursively enumerable but not necessarily decidable.** We can produce every element by running $p_{\text{gen}}$ and waiting. We cannot in general decide membership for arbitrary $x$ (halting problem).

## Is the library computable?

Infinity is not the obstruction to computability. The natural numbers are infinite and computable. The Fibonacci sequence is infinite and computable. The library's status is layered:

| Object | Computable? |
|---|---|
| The bitstring substrate $\{0,1\}^*$ | Yes, fully. Enumerable; decidable membership. |
| The set of halting outputs $\{U(p) : p \text{ halts}\}$ | Recursively enumerable; not decidable. |
| The universal prior $M(x)$ | Lower-semicomputable; not computable. |
| The Kolmogorov complexity $K(x)$ | Not computable. |

The library is **generable but not surveyable**. We can produce everything in it eventually. We cannot in general answer, for a given element: where is it, how complex is it, how probable is it.

This is itself another argument for index-as-abstraction. If the library were fully computable, one could imagine a canonical index: the algorithm that maps each item to its position. But the navigation tools are uncomputable. There is no algorithm that takes $x$ and returns its canonical position, complexity, or shortest description. The library lacks a *computable canonical* index, full stop. Any index we use is a tool the observer brings.

## Why the bookshelf metaphor anyway

Borges chose it because narrative needs discreteness. So does pedagogy. The metaphor is load-bearing: it makes the totality imaginable and lets the reader hold the picture in mind. Abandoning it would lose the reader before any of the work could be done.

The right move is to use the metaphor, name it as imposition at the points where the imposition matters, and dissolve it fully at the deepest point. The book uses the bookshelf through Part I; Ch 13 in Part II dissolves it, alongside the self.

## Regularities span "books"

The deeper point about why the bookshelf is a tool rather than a feature:

Kolmogorov complexity is, by construction, the shortest description across *all* regularities, not book-by-book. If "book 7" and "book 12" share substructure, $K$ exploits this. The shortest program describing both is much shorter than the sum of programs describing each independently.

Concretely: imagine the Library as a single bitstream. Decomposing it into "books" of fixed length is an arbitrary cut. Different cuts would give different book boundaries, and different compression structures across those boundaries. The actual compression is across the full bitstream, indifferent to any imposed segmentation.

This means: when the book says "you exist at many indices," the underlying truth is more subtle. The pattern that constitutes you might span what the indexing scheme treats as separate items. The indexing is the analytical tool. The multiplicity is not constituted by the indexing.

## Index as compression, parallel to identity

The "I" is a label attached to a region of structure for navigation. The "index" is a label attached to a region of structure for analytical tractability. Both are useful compressions. Neither carves at any underlying joint.

This is the parallel Ch 13 develops:

- **Self.** Compression of a continuing pattern. The brain's self-model. Metzinger, Parfit.
- **Index.** Compression of "address within the Library." The analyst's coordinate scheme. New to this book.

Both arise from the same need: a continuous, fully realized structure has to be made tractable by a finite observer. The observer decomposes the structure into items and attaches labels. The items and labels are not in the structure; they are in the observer's interface to the structure.

The dissolution of self and the dissolution of index are not two separate moves. They are one move applied at two levels of the same apparatus.

## The deepened indifference thesis

The original framing of the book's title: the measure is indifferent over indices.

The deeper framing: the indexing itself is observer-imposed. The structure has even less canonical decomposition than "indifferent over indices" suggested. The bookshelf is a tool the reader brings. The Library itself does not have one.

This is not a separate labeled speculative move. It is a clarification of what Move II (CUH) and the universal-distribution apparatus already commit to. The book's framework, taken seriously, already implies the index-dissolution. Ch 13 makes this explicit.

The deepened thesis does not console. It deepens the indifference. The original framing left room for the reader to think "at least my coordinates are coordinates", that the index, even if I do not know which, is something. The deepened framing removes even that.

## Picture A and Picture B: object vs situated

The framework supports two pictures of the multiverse that the book has not fully separated.

**Picture A: multiverse-as-object.** The static set $\{U(p)\}$ with measure $M$. Viewed from outside, surveying the totality. The book's title and thesis use this picture: indifference of measure over indices.

**Picture B: observer-as-situated.** The observer inside some $U(p)$, with access only to a prefix of their local substructure. The observer forms a posterior over candidate programs; the posterior never collapses; the observer cannot find which $p$ generates them. Even with infinite data, many distinct programs would remain consistent.

| | Picture A | Picture B |
|---|---|---|
| What it describes | Static set with measure | Observer's posterior given prefix |
| Vantage | Outside, surveying totality | Inside, with finite data |
| Status of $p$ | One real $p$; multiverse contains all | Always a posterior; never sharp |
| Status of the index | Observer-imposed on static set | Cannot be retrieved from inside |
| What is indifferent | Measure over outputs | Observer's posterior never resolves |

The pictures are consistent, not in conflict. But Picture B is what applies to any actual reader. The reader is always inside, never outside.

The book's strategy (option A from the discussion): keep Picture A through Part I as the cleaner pedagogical entry. Develop Picture B explicitly in Ch 13, alongside the dissolution of the self. The deeper indifference is not just "the measure has no opinion" but "the observer cannot from inside identify which program generates them, in principle, even with unbounded data."

## Local inference: what observers actually do

The observer's epistemic activity is not global Solomonoff. Global Solomonoff is uncomputable. An observer with finite resources could never run it.

What the observer actually does is **local inference**:

1. Isolate a substructure $s \subset U(p)$ (a cell, an apple, a stellar system).
2. Find a short local program $p_s$ that approximates $s$ well enough for prediction.
3. Compose these local approximations across scales and subsystems.

The "ensemble" the observer maintains is the collection of $p_s$'s: the effective theories at each scale. Not a posterior over global $p$. Science is not a search for the program. It is the construction of a library of local approximations.

The $p_s$'s are not factors of $p$ in any literal sense. They are independent short descriptions of substructures. The cell biologist's model of mitosis is not extracted from the universe's wave function; it is a local theory that captures the cell's behavior with small description. The relation between $p_s$ and $p$ is approximate, mediated by emergence and effective theory.

## Hierarchical decomposability as anthropic constraint

For local inference to be possible, $U(p)$ must have stronger structure than mere computability:

- **Hierarchical decomposability.** Substructures at each scale must be approximable by local short programs. Cells without quarks. Apples without electrons. Each scale has its own short description, independent of the deeper microphysics.
- **Local compressibility at multiple scales.** A substructure $s$ has a $p_s$ such that $|p_s|$ is small compared to deriving $s$ from first principles.
- **Markov-blanket / modular structure.** Subsystems are approximately isolable. The apple's near future depends on apple-plus-local-environment, not on every distant detail.

These are not consequences of computability. A program can produce a perfectly computable universe with none of these properties: globally entangled, locally chaotic, or perfectly homogeneous. The digits of $\pi$ are computable but locally chaotic; an observer "in" $\pi$'s digits could not do science from finite stretches.

Observers exist only in the subset of programs whose $U(p)$ has hierarchical decomposability. The multiverse contains every program; the vast majority do not support observers doing science.

This is anthropic but more substantive than the usual move. "Why is the universe lawful?" is the standard version. The deeper version: "Why is the universe *hierarchically* lawful, with effective theories at each scale that we can find with local effort?" The answer is the same: it has to be, or we are not here to ask. But the answer being the same does not make the constraint vacuous. It is a real restriction on which programs we can inhabit.

This connects to Picture B. The observer doing science is doing local inference, building an ensemble of $p_s$'s, never having access to the global $p$. The self the observer uses to anchor this inference is itself one of the local substructures: a $p_{\text{self}}$, the brain's self-model, a short program that approximates a region of $U(p)$. Self and local theory are the same kind of object. Index, identity, scientific knowledge are all instances of one move: local compression. This is the deepest claim that comes out of the index discussion, and Ch 13 is its natural home.

## Where in the manuscript

### Ch 2: brief note (added)

A short section, "A note on the metaphor", at the end of "From books to programs". Acknowledges that the discreteness is observer-imposed; points forward to Ch 13. Brief flag, not full treatment. Done in this pass.

### Ch 7 (The Inhabited Library): possible nod

When Ch 7 talks about observers being at indices, a sentence could remind the reader that "indices" remains provisional. Optional; the Ch 2 note may suffice. Defer until drafting or revising Ch 7.

### Ch 8 (The Observer): "What an observer is" section

Chapter 8 is titled "The Observer" but never defines what an observer is. A new section between "The Library inside our physics" and "Where am I?" adds the missing definition: observer as substructure of $U(p)$ (or of the wave function); the hierarchical-decomposability requirement; local inference as what observers actually do. This sets up the "where am I?" question that follows and provides the early footing for Ch 13's full dissolution work.

The section keeps to Picture A's language (the static frame) so Part I remains coherent, but introduces the local-inference vocabulary that Ch 13 will use to develop Picture B.

### Ch 13 (The Self / Pattern): major development

This is the chapter where the parallel pays off. The dissolution of self extends to dissolution of the index. The two moves are parallel and arguably one. The chapter's strongest move: the entire apparatus for talking about *where* the self is, is itself a compression. Self and coordinate go together.

This is also where the relationship to Metzinger and Parfit deepens. Metzinger's transparent self-model is not just about the self; it is about the model. The model includes coordinates. The coordinates are part of the model.

### Ch 9 (Indifference of Measure): possibly revisit

Ch 9 currently says the question "where am I?" is left unresolved. The index-as-abstraction observation arguably reframes this. The question does not just lack an answer; it presupposes an indexing scheme that is itself a tool. The deferral becomes less "we do not have a satisfactory theory" and more "the question's form is provisional."

Whether to add this to Ch 9 or save it for Ch 13: leaning toward Ch 13, where the dissolution argument is being built fully. Ch 9 stays as is for now.

## Tone notes

- This is a clarification of what the framework already implies, not a separate metaphysical move. Do not oversell.
- Same humility register as the rest of the book. The framework might be wrong. The index-as-abstraction observation might still be wrong about how it is wrong.
- Avoid the trap of letting "index as abstraction" sound like consolation. It does not console. It dissolves a quiet certainty the reader was carrying.
- Match the dissolution-of-self tone Ch 13 will develop: matter-of-fact, not triumphant. Parfit's voice, not the new-age voice.

## Open questions for drafting

- Does this affect the cascade in `foundations.md`? Worth checking whether the cascade implicitly assumes discrete indices when stating its consequences. Probably yes in the description, not in the substance.
- Does this complicate the Boltzmann brain treatment? The BB hypothesis says "you might be a momentary fluctuation." If "you" and "index" are both abstractions, the BB question becomes "is the local structure of this configuration explainable by a long lawful history or by a momentary fluctuation?" The grammar shifts; the worry remains.
- Does Whitman's "I am large, I contain multitudes" land differently? Maybe. The epigraph already plays on multiplicity. Index-as-abstraction adds: the multitudes are not enumerable items either. Whitman may have meant it metaphorically. The Library makes it literal. The dissolved index makes it more literal still.
