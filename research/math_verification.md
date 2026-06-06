# Math Verification: Part I (Chapters 1-4)

Verification of mathematical, historical, and proof-sketch claims in the four drafted chapters. Each claim is given a status (correct / minor issue / error), notes on subtleties, and suggested edits where applicable. The chapters do not edit themselves; this is a working document for the author.

A general note on style: the chapters target a determined-but-lay audience and the level of precision is generally appropriate. Several technical subtleties (lower-semicomputability, prefix vs. monotone machines, semimeasure normalization, plain vs. prefix Kolmogorov complexity) are deliberately glossed over. Most of these decisions are sound; a few are flagged because they cross into actual inaccuracy or because a footnote would head off objections from a sharp reader.

---

## Chapter 1: Bayes

### Claim 1.1: "Five heads in a row on a fair coin happens once in every thirty-two trials"

**Status:** correct.

$P(\text{HHHHH} \mid \text{fair}) = (1/2)^5 = 1/32 \approx 0.03125$. The wording "once in every thirty-two" is colloquially fine for "with probability 1/32."

### Claim 1.2: Counting argument, prior 1%, posterior 24%

**Status:** correct.

Worked check:
- 10,000 trials. 1% trick means 100 trick-coin trials, 9,900 fair-coin trials.
- Trick trials producing HHHHH: 100 (all of them).
- Fair trials producing HHHHH: $9{,}900 \times (1/32) = 309.375$, rounded to 309.
- Total HHHHH trials: $100 + 309 = 409$.
- Trick fraction within HHHHH: $100/409 \approx 0.2444$.

The chapter says "about twenty-four percent." Correct to the precision claimed.

A nitpick: $9900/32 = 309.375$, not exactly 309. The chapter says "about three hundred and nine," which is honest. Some readers will notice that $100/409$ and $100/409.375$ both round to 24%; no issue.

### Claim 1.3: Bayes' theorem derivation

**Status:** correct. The derivation via counting is clean. The translation from the count formula to $P(D \mid H) P(H) / P(D)$ is standard and accurate.

Minor pedagogical comment: the chapter writes $P(D) = P(H) P(D \mid H) + P(\neg H) P(D \mid \neg H)$. This assumes the partition is $\{H, \neg H\}$, which is fine here but is a special case of marginalization. For two hypotheses this is trivial; for a general partition the reader might wonder. Not worth changing.

### Claim 1.4: Cox's theorem statement and conditions

**Status:** mostly correct, with a known and acknowledged subtlety.

The chapter's three desiderata:
- Degrees of belief are real numbers.
- Two paths to the same conclusion give the same answer.
- The calculus reduces to classical logic when certainty is reached.

This matches Jaynes' presentation (3 desiderata: real numbers + qualitative correspondence + consistency, which the chapter folds into the second and third items). It also matches the form most readers encounter in informal expositions. Cox's original (1946) used slightly different machinery (associativity functional equations + smoothness on plausibility composition), formalized further by Jaynes (2003) and Van Horn (2003).

**Subtle issue:** the chapter footnote says "Cox's original proof has had loose ends tightened by later authors (notably Jaynes and Van Horn)." This is accurate but understates the situation. Joseph Halpern (1999) presented a counterexample showing Cox's theorem, as originally stated, fails on finite domains. The fix requires either:
- assuming a "density" axiom (Paris 1994, used by Van Horn 2003), or
- restricting to infinite domains and accepting some additional regularity.

For a lay audience, the chapter's footnote is reasonable. **Suggested edit (optional):** add a single sentence to the footnote: "A counterexample by Halpern (1999) showed the original argument requires additional regularity (typically a 'density' assumption on the domain); the modern treatments either assume this or restrict the setting accordingly. The qualitative conclusion (consistent belief revision is isomorphic to probability theory) is not in dispute."

This is optional; the book is not a foundations text and the existing footnote is honest about loose ends.

### Claim 1.5: "Strictly, force it to be isomorphic to probability theory, which is the same thing up to renaming"

**Status:** correct. Cox's theorem produces a calculus that is isomorphic to probability theory; the isomorphism is via a monotonic rescaling. "Same thing up to renaming" is a fair lay paraphrase.

### Historical attribution: Cox 1946

**Status:** correct.

R. T. Cox, "Probability, Frequency and Reasonable Expectation," *American Journal of Physics*, vol. 14 (1946), pp. 1-13. The book-length elaboration is *The Algebra of Probable Inference* (Johns Hopkins, 1961). The chapter says "In 1946, the physicist R. T. Cox..." which is right.

### Maxwell epigraph (1850)

**Status:** plausible attribution; verify if cited formally. The Maxwell quote ("The actual science of logic is conversant at present only with things either certain, impossible, or entirely doubtful...") is widely attributed to a 1850 letter from Maxwell to Lewis Campbell. The wording is correct.

---

## Chapter 2: The Prior Problem

### Claim 2.1: Aria's calculation, prior 0.5, posterior ~0.97

**Status:** correct.

$P(\text{trick} \mid \text{HHHHH}) = \frac{1 \cdot 0.5}{1 \cdot 0.5 + (1/32) \cdot 0.5} = \frac{0.5}{0.5 + 0.015625} = \frac{0.5}{0.515625} \approx 0.9697$.

Chapter says "$\approx 0.97$." Correct.

### Claim 2.2: Ben's calculation, prior 0.001, posterior ~0.031

**Status:** correct.

$P(\text{trick} \mid \text{HHHHH}) = \frac{1 \cdot 0.001}{1 \cdot 0.001 + (1/32) \cdot 0.999} = \frac{0.001}{0.001 + 0.03121875} = \frac{0.001}{0.03221875} \approx 0.03104$.

Chapter says "$\approx 0.031$." Correct.

### Claim 2.3: Prior regress as a real argument

**Status:** correct in substance. The Hume connection is handled gracefully (Hume's problem of induction is exactly the problem that no prior is derived from data without itself depending on a prior).

### Claim 2.4: Laplace's principle of insufficient reason and Bertrand's paradox

**Status:** correct.

The chapter notes that the "equally likely outcomes" depend on how the partition is carved up, illustrating with trick-vs-fair vs. bias parameter in $[0,1]$. This is essentially Bertrand's paradox (1889) without naming it; the discussion is accurate.

**Suggested edit (optional):** name Bertrand's paradox in passing or in a footnote, since the reader who Googles will land there immediately. Not necessary.

### Claim 2.5: Maximum entropy depends on the measure

**Status:** correct. Jaynes (1957) introduced maximum entropy as a principle for prior selection; it requires a "measure" on the hypothesis space, and different measures give different MaxEnt priors. The chapter's framing ("good once you have committed to how to describe the hypotheses") is accurate.

### Claim 2.6: Empirical Bayes uses the data twice

**Status:** correct but charitable. The chapter calls EB "a working procedure with real successes" and notes that "it uses the data twice." This is fair; EB is a defensible engineering technique that does not solve the foundational problem.

### Claim 2.7: "For two and a half centuries, the consensus on the prior problem was: priors are subjective."

**Status:** broadly correct. "Two and a half centuries" measured from Bayes (Bayes's essay was published posthumously in 1763 by Richard Price; Laplace developed the framework into the early 1800s). From ~1763 to ~2013 is two and a half centuries; the rhetoric works. The "consensus" is real but had dissenting voices (objective Bayesians: Jeffreys, Jaynes; the universal-prior tradition of Solomonoff; reference priors of Bernardo). The chapter does not need to enumerate these here.

---

## Chapter 3: Description and Probability

### Claim 3.1: Average length 1.75 bits for code $A=0, B=10, C=110, D=111$

**Status:** correct.

$(1/2)(1) + (1/4)(2) + (1/8)(3) + (1/8)(3) = 0.5 + 0.5 + 0.375 + 0.375 = 1.75$.

### Claim 3.2: Prefix-free code definition

**Status:** correct. "No codeword is a prefix of another" is the standard definition. The example showing $A=0, B=01$ is ambiguous is fine.

### Claim 3.3: Kraft's inequality $\sum_i 2^{-\ell_i} \leq 1$ for prefix-free codes

**Status:** correct.

Statement and proof sketch ("each codeword of length $\ell$ uses $2^{-\ell}$ of the unit interval; codewords cannot share full paths from root to leaf; regions do not overlap; total cannot exceed one") is accurate and matches the standard interval / cylinder-set proof.

The Kraft sum for the example: $2^{-1} + 2^{-2} + 2^{-3} + 2^{-3} = 1/2 + 1/4 + 1/8 + 1/8 = 1$. Correct. The chapter notes this means the code is complete.

**Historical attribution:** Kraft's inequality was published by L. G. Kraft in 1949 (MIT master's thesis). The general result for uniquely-decodable (not just prefix) codes is due to McMillan (1956); for the prefix-only case Kraft is the right name. The chapter doesn't name Kraft historically in detail, only states the inequality. This is fine.

### Claim 3.4: "Shannon and Fano gave a recipe in the 1940s. Huffman gave an optimal one in 1952."

**Status:** correct.

- Shannon outlined his coding approach in "A Mathematical Theory of Communication" (1948).
- Fano developed his variant in a 1949 MIT technical report ("The Transmission of Information").
- Huffman published his optimal algorithm in 1952 ("A Method for the Construction of Minimum-Redundancy Codes").

The chapter's "in the 1940s" for Shannon-Fano and "in 1952" for Huffman is right.

### Claim 3.5: $\ell_i \approx -\log_2 P(i)$ relationship

**Status:** correct (with the standard caveat that the approximation comes from $\ell_i$ being an integer). The chapter explicitly acknowledges this: "The approximation comes from $\ell_i$ being an integer; the underlying logarithm is real-valued."

The Shannon source-coding theorem gives the precise statement: for any distribution $P$, there is a prefix-free code with $\sum_i P(i) \ell_i < H(P) + 1$, where $H(P) = -\sum_i P(i) \log_2 P(i)$ is the entropy. Huffman achieves the optimum within one bit per symbol.

### Claim 3.6: Coupling between code lengths and probabilities

**Status:** correct. The bridge $P(i) = 2^{-\ell_i} / \sum_j 2^{-\ell_j}$ from code to probability, and the converse (using Shannon-Fano or Huffman to go from probability to code), is the standard view.

The chapter's choice to call this "coupling" is a stylistic move; it is not standard terminology but it is clear in context.

### Claim 3.7: "Every prefix-free code defines a probability distribution"

**Status:** correct (after normalization, which the chapter handles).

---

## Chapter 4: Solomonoff Induction

### Claim 4.1: Kolmogorov complexity definition

**Status:** correct (with a glossed-over subtlety).

The chapter defines $K(x)$ as "the length, in bits, of the shortest program that outputs $x$." This is the standard informal definition.

**Subtlety:** the chapter uses $K(x)$ throughout. In the standard literature, $K(x)$ specifically denotes **prefix complexity** (self-delimiting / prefix-free programs), while $C(x)$ (sometimes $K_p$ or $K_{plain}$) denotes **plain Kolmogorov complexity** (programs without prefix-free constraint).

These differ by at most a logarithmic term: $K(x) \leq C(x) + 2 \log_2 C(x) + O(1)$. The semimeasure machinery and the bridge to $M(x)$ require the prefix variant; $\sum_x 2^{-K(x)} \leq 1$ holds for prefix $K$ but $\sum_x 2^{-C(x)}$ diverges.

The chapter implicitly uses prefix complexity because it goes on to use $\sum_x M(x) \leq 1$. This is consistent with what Hutter, Li & Vitanyi call $K(x)$ in modern texts. For a lay audience, the conflation is acceptable. The chapter does not need to introduce both notations.

**Suggested edit (optional):** add a footnote where $K(x)$ is first introduced: "Technical note: for the rest of the chapter we use the version of $K(x)$ that counts programs in a self-delimiting (prefix-free) format. This differs from the simplest version by at most a logarithmic correction, but it is the version that connects to the universal prior below."

### Claim 4.2: $K(x)$ is uncomputable

**Status:** correct. The chapter does not name "Chaitin's incompleteness theorem" explicitly, but it does note that "you cannot tell in advance which programs halt (the halting problem); for any given program, you cannot decide whether it will eventually produce $x$ or run forever without doing so." This is the right gloss.

The full claim (Chaitin 1974, ish): there is a constant $L$ such that no consistent formal system can prove $K(x) > L$ for any specific $x$, even though almost all strings have $K(x) > L$. The chapter does not need to state this. The reference to the halting problem connection is sufficient at the lay level.

### Claim 4.3: Universal Turing machine and invariance theorem

**Status:** correct in substance. Two minor issues to consider.

The chapter says: "In 1936, Alan Turing showed that such a machine exists." This is the right citation (Turing 1936, "On Computable Numbers, with an application to the Entscheidungsproblem"). Correct.

The chapter says: "Different universal machines exist, but for our purposes they are interchangeable: anything you can do on machine $U_1$, you can do on machine $U_2$ with a small extra cost (the cost of a translator program from one to the other). This is the invariance theorem."

The standard statement is: for any two universal machines $U_1$ and $U_2$, there is a constant $c$ such that $|K_{U_1}(x) - K_{U_2}(x)| \leq c$ for all $x$. The chapter's "small extra cost (the cost of a translator program)" is a reasonable lay paraphrase. The invariance theorem is attributed to Solomonoff (1964) and independently Kolmogorov (1965). The chapter does not attribute it; the lay-level statement is fine.

### Claim 4.4: Universal prior $M(x) = \sum_{p: U(p) = x*} 2^{-|p|}$

**Status:** correct in substance, with one technical issue.

The notation $x*$ (the chapter says "with possibly more after") is the standard notation for "x as a prefix of the output." The formula matches the **continuous** algorithmic probability, which is what one wants for sequence prediction (predicting "what comes after the observed prefix").

**Technical issue:** the chapter says "A standard technical setup makes $U$ a *prefix* machine: it reads programs in a self-delimiting way, so the set of valid programs is prefix-free." 

In the modern literature there are two related but distinct constructions:
1. **Discrete algorithmic probability** $m(x) = \sum_{p: U(p) = x} 2^{-|p|}$ over a **prefix** machine (program is self-delimiting, output is exactly $x$).
2. **Continuous algorithmic probability** $M(x) = \sum_{p: U(p) = x*} 2^{-|p|}$ over a **monotone** machine (input read sequentially, output may be infinite, and $x*$ means "$x$ is a prefix of the output").

The chapter uses the continuous formula but calls $U$ a "prefix machine." Strictly, for the continuous case, $U$ is monotone (with the program tape read in a self-delimiting manner, often called a monotone Turing machine). Both setups give the same intuition (Kraft-style bound), but the technical machinery is different.

**For a lay audience:** this is almost certainly too fine a point to put in the body text. However, a careful reader from a CS background will catch it. **Suggested edits (one of):**
- (Minimal) drop the word "prefix" in "Make $U$ a *prefix* machine" and replace with "self-delimiting" or "with a standard self-delimiting input convention," which is true for both setups.
- (Footnote) note that for the continuous version of $M$ used here, the technical machinery is a *monotone* Turing machine with self-delimiting input; the prefix-machine variant gives the closely related discrete algorithmic probability $m(x)$. Refer the reader to Li & Vitanyi 2019, Ch. 4 for details.
- (Sweep under the rug) leave as is, on the grounds that the lay audience will not notice and the CS reader will forgive the imprecision because the qualitative bound is right. This is defensible but a tighter alternative exists.

### Claim 4.5: $\sum_x M(x) \leq 1$ (semimeasure property)

**Status:** correct. The reason given ("Kraft then guarantees that the total weight is bounded") is the right intuition.

The reason this is a semimeasure ($\leq 1$, not $= 1$) is that some programs do not halt, so probability "leaks out." This is glossed in the chapter as Kraft, which is fine. A reader who wants more detail can find it in Li & Vitanyi.

### Claim 4.6: $M(x) \geq 2^{-K(x)}$

**Status:** correct. The chapter notes that the shortest program contributing to $M(x)$ has length $K(x)$, so $M(x)$ includes the term $2^{-K(x)}$. This gives the lower bound. The chapter notes that the full $M(x)$ may be larger because of contributions from longer programs.

The matching upper bound (the **coding theorem** of Levin 1974) says $-\log_2 M(x) = K(x) + O(1)$. The chapter gestures at this ("$M(x)$ and $2^{-K(x)}$ are within a constant factor of each other") but does not name the coding theorem. This is a fair pedagogical choice; the coding theorem is one of the deepest results in AIT and naming it adds friction without illumination at this level.

### Claim 4.7: "Solomonoff defined this in the 1960s"

**Status:** correct.

Solomonoff's first technical report on inductive inference was 1960; the full development was published in "A Formal Theory of Inductive Inference," Parts I and II, in *Information and Control* in 1964. The phrase "in the 1960s" is accurate. Kolmogorov independently arrived at related ideas in 1963-65; Chaitin independently in 1965-69. The chapter does not need to distinguish; "Solomonoff" gets the right attribution for the universal prior.

### Claim 4.8: Dominance theorem $M(x) \geq c_\mu \cdot \mu(x)$

**Status:** correct in substance with one subtlety.

The chapter says: "if $\mu$ is computable (or, more precisely, lower-semicomputable as a semimeasure), then there is a constant $c_\mu$..."

This is the right qualifier. The standard statement: $M$ is a universal lower-semicomputable semimeasure, meaning that for every lower-semicomputable semimeasure $\mu$, there exists a constant $c_\mu > 0$ such that $M(x) \geq c_\mu \cdot \mu(x)$ for all $x$. The constant satisfies $c_\mu \approx 2^{-K(\mu)}$, where $K(\mu)$ is the prefix complexity of $\mu$ as a program.

For computable measures (a proper subset of lower-semicomputable semimeasures), the same dominance holds. The chapter's "or, more precisely, lower-semicomputable as a semimeasure" is a clean way to state the technical condition without unpacking it. This is good craft.

**Subtlety:** the chapter does not state what $c_\mu$ is. The fact that $c_\mu \approx 2^{-K(\mu)}$ is what makes the dominance theorem do real work: simple $\mu$ get large constants, complex $\mu$ get small constants. This means: $M$ catches up quickly to simple computable distributions and slowly to complex ones, in proportion to how complex they are. **Suggested edit (optional):** add a sentence noting that the constant $c_\mu$ depends on the complexity of $\mu$ (small for simple $\mu$, exponentially small for complex $\mu$), so $M$ catches up to simple distributions faster than to complex ones.

### Claim 4.9: Convergence interpretation

**Status:** correct.

The chapter says: "the predictions of $M$ converge to the predictions of $\mu$ as data accumulates. After enough observations, $M$ and $\mu$ make essentially the same predictions about what comes next, regardless of which $\mu$ is at work."

The technical statement: for any lower-semicomputable $\mu$, the total expected Kullback-Leibler divergence between the conditional predictions of $M$ and $\mu$ summed over all observations is bounded by $K(\mu) \cdot \ln 2$ (Solomonoff 1978, Hutter 2001, Hutter 2005). This is a strong convergence result: the total prediction error is finite and bounded by a constant.

The chapter's "essentially the same predictions" is a reasonable lay paraphrase.

### Claim 4.10: $M$ is uncomputable; approximable from below

**Status:** correct.

The chapter says: "You can approximate $M(x)$ from below."

This is the right statement. $M$ is **lower-semicomputable**: there is a computable monotone increasing sequence converging to $M(x)$ from below. (It is not just non-computable; it is not even upper-semicomputable, because that would give a computable approximation from both sides, which would make $M$ computable, which it is not.)

The chapter does not use the term "lower-semicomputable" in the body, which is the right call for a lay audience. The intuition ("approximate from below by running programs and summing") is right.

Aside: the lore document `math-grounding.md` line 68 says "It is upper-semicomputable but not computable" for the discrete $m(x)$, and line 87 says "$M$ is upper-semicomputable but not computable." **Both are errors in the lore.** The correct statement is **lower-semicomputable**. ($K(x)$ is upper-semicomputable; $M(x)$ and $m(x)$ are lower-semicomputable. The asymmetry is what makes the coding theorem $M(x) \approx 2^{-K(x)}$ non-trivial.) This does not affect the chapter, only the reference document; recommend correcting the lore.

### Claim 4.11: "This is not a flaw in the definition. It is what makes $M$ universal."

**Status:** correct in spirit. The intuition is right: any computable prior must fall short of universality somewhere, because the class of lower-semicomputable semimeasures is strictly larger than the class of computable ones, and $M$ dominates the larger class.

The chapter's phrasing is slightly informal but lay-appropriate. A more formal statement (which the chapter wisely does not give): if any prior $P$ were computable and universal, it would dominate itself and every lower-semicomputable semimeasure, including the ones not in the computable class. But then we could diagonalize: construct a lower-semicomputable semimeasure $\mu$ that grows faster than $P$ on suitable inputs, contradicting dominance.

### Claim 4.12: Solomonoff induction conditional formula

**Status:** correct.

$M(\text{next bit} = b \mid x) = M(xb) / M(x)$ is the standard conditional probability formula. The chapter is right that the predictor's belief about the next bit is well-defined given the universal prior and the standard Bayes machinery.

### Claim 4.13: Chaitin epigraph quote

**Status:** correctly attributed. Chaitin's *Algorithmic Information Theory* (Cambridge University Press, 1987) does contain similar statements crediting Kolmogorov for the "satisfactory definition of randomness." The exact wording of the quote should be cross-checked against the book before publication (Chaitin's actual phrase in the preface is close to this but may differ in punctuation). Recommend the author verify against a hard copy if available.

---

## Cross-cutting Notes

### On the four chapters as a unit

The math arc is tight. Ch 1 establishes Bayes and Cox; Ch 2 surfaces the prior problem; Ch 3 builds the bridge between description and probability; Ch 4 takes the bridge to its limit and closes the prior gap (modulo uncomputability). This is exactly the pedagogical sequence the lore documents call for, and the math hangs together.

The substantive claims are all correct in spirit and almost all correct in detail. The flagged issues are:

1. **Chapter 1, footnote on Cox.** Could acknowledge Halpern's counterexample explicitly. Optional.
2. **Chapter 4, prefix vs. monotone machines for $M(x)$.** The chapter calls $U$ a "prefix machine" while using the continuous formula. Either drop the qualifier or note the distinction.
3. **Chapter 4, no explicit footnote on the prefix-vs-plain $K$ distinction.** Could add a footnote; defensible to omit.
4. **Lore document error (not chapter error).** The math-grounding.md file says $m(x)$ and $M(x)$ are "upper-semicomputable." This is backwards; they are lower-semicomputable. $K(x)$ is upper-semicomputable. The chapter text is correct; only the reference document is wrong.

### On historical attributions

All historical attributions are correct:
- Cox 1946: yes.
- Shannon 1948, Fano 1949, Huffman 1952: yes (the chapter's "in the 1940s" for Shannon-Fano and "in 1952" for Huffman is precise enough).
- Kraft 1949: not named in chapter; correct attribution.
- Turing 1936: yes.
- Solomonoff "in the 1960s": yes (1960 preprint, 1964 *Information and Control* papers).
- Kolmogorov 1965: not named in chapter; correct date.
- Chaitin 1974 incompleteness: not named in chapter; correct date.

### On voice and accessibility

The voice carries through: plain, direct, no em-dashes, no hype. The diagrams are well-conceived. The pacing is right; each chapter teaches one idea well and refers forward to the next.

The choice to gloss technical distinctions (prefix vs. monotone, plain vs. prefix $K$, lower- vs. upper-semicomputable) is sound. The audience is "determined but lay," not graduate students in computer science. The chapters give the right amount of math: enough to make the claims precise, not so much that a non-specialist drowns.

### On what could be tightened (summary)

Of the four chapters, Ch 4 has the most technical surface area and accordingly the most opportunities for minor imprecision. The two specific edits worth considering:

1. Ch 4, around the universal prior definition: replace "prefix machine" with "self-delimiting" or add a footnote about the monotone-machine setup. (Substantive but small.)
2. Ch 4, dominance constant: a sentence noting $c_\mu \approx 2^{-K(\mu)}$ would help the careful reader understand why "$M$ catches up to whatever computable process is actually at work" is a real claim (because $\mu$ is what is at work, $K(\mu)$ is bounded, and so the catch-up is fast).

Everything else is at most a stylistic adjustment.

---

## Sources

- [Cox's theorem (Wikipedia)](https://en.wikipedia.org/wiki/Cox's_theorem)
- [Cox's Theorem and the Jaynesian Interpretation of Probability (Terenin & Draper 2017, arXiv)](https://arxiv.org/pdf/1507.06597)
- [Stats.org.uk Cox theorem guide](https://www.stats.org.uk/cox-theorems/)
- [Constructing a logic of plausible inference: a guide to Cox's theorem (Van Horn 2003)](https://gwern.net/doc/statistics/bayes/2003-horn.pdf)
- [Cox's theorem revisited (Halpern, JAIR)](https://dl.acm.org/doi/abs/10.5555/3013545.3013557)
- [A Counter Example to Theorems of Cox and Fine (Halpern, arXiv)](https://arxiv.org/pdf/1105.5450)
- [Algorithmic probability (Scholarpedia)](http://www.scholarpedia.org/article/Algorithmic_probability)
- [Solomonoff's theory of inductive inference (Wikipedia)](https://en.wikipedia.org/wiki/Solomonoff's_theory_of_inductive_inference)
- [Algorithmic probability (Wikipedia)](https://en.wikipedia.org/wiki/Algorithmic_probability)
- [Kolmogorov complexity (Wikipedia)](https://en.wikipedia.org/wiki/Kolmogorov_complexity)
- [Algorithmic information theory (Scholarpedia)](http://www.scholarpedia.org/article/Algorithmic_information_theory)
- [Ray Solomonoff obituary (Vitanyi, CWI)](https://homepages.cwi.nl/~paulv/obituary.html)
- [Kraft-McMillan inequality (Wikipedia)](https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality)
- [Shannon-Fano coding (Wikipedia)](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding)
- [Huffman coding (Wikipedia)](https://en.wikipedia.org/wiki/Huffman_coding)
- [On Computable Numbers (Turing 1936, full text)](https://people.math.ethz.ch/~halorenz/4students/Literatur/TuringFullText.pdf)
- [Chaitin's incompleteness theorem (Baez)](https://johncarlosbaez.wordpress.com/2011/10/06/chaitins-theorem-and-the-surprise-examination-paradox/)
- [How Incomputable Is Kolmogorov Complexity? (Vitanyi, arXiv)](https://arxiv.org/pdf/2002.07674)
- [On the computability of Solomonoff induction and AIXI (Leike & Hutter, TCS)](https://www.sciencedirect.com/science/article/pii/S0304397517308502)
