# Outline

**Title:** *On Intelligence and Its Specifications*

**Thesis:** There is a beautiful mathematical theory of optimal intelligence (Bayesian inference + Solomonoff induction + utility maximization = AIXI). There are messy real systems that approximate it (LLMs). The gap between theory and practice is where AI safety lives. The specification problem (reward modeling, alignment) is the central problem; in light of approaching AGI/ASI, it is arguably the most important problem facing the field. To reason responsibly about AI in 2026, the reader needs the math, the practice, and the gap between them.

**Audience:** Determined but lay. Math is used where it has to be, conceptually explained first, then formalized. Diagrams carry the conceptual weight; prose carries the rest. Closer to a Penguin science book than a textbook.

**Length:** No fixed word-count target; sized by what the material warrants. 17 chapters in 4 parts. (Per-chapter figures below are descriptive pacing guides, not budgets.)

**Diagrams:** Heavy. Every equation gets a diagram. Every algorithm gets a diagram. Every concept that can be visualized should be.

---

## Structure

| Part | Chapters | Words | Role |
|---|---|---|---|
| I: Prediction | 1–4 | ~8,300 | The theory of optimal inference |
| II: Decision | 5–8 | ~10,000 | The theory of optimal agency (including generalization and AIXI) |
| III: The Specification Problem | 9–12 | ~8,500 | Clean theory of why alignment is hard, why optimization is the structural danger, and the three buckets of mitigation |
| IV: Reality | 13–17 | sized as needed | Messy practice; LLMs (what they are, how they are trained), the gap, where the trajectory is going, and the finale that takes the stand and carries the stakes |

Pedagogical move: Parts I–III develop the theory in clean settings. Part IV moves to messy practice. Reward modeling and alignment get clean theoretical treatment in Part III, then empirical / case-study treatment in Part IV.

---

## Part I: Prediction (4 chapters, ~8,300 words)

### Ch 1: Bayes (~2,000 words)

Belief revision as restriction-to-subset. Cox's theorem: this is the unique consistent calculus of belief. The coin example as the canonical worked illustration.

**Key claim:** Probability is not a special science. It is the structure of how any consistent agent updates beliefs in the face of evidence.

**Key diagrams:** Restriction-to-subset Venn; coin update bar chart.

### Ch 2: The Prior Problem (~1,800 words)

Bayes tells you how to update once you have a prior. It does not tell you what the prior should be. Two reasonable agents, same data, different posteriors. The regress.

**Key diagrams:** Two priors diverging; regress tree.

### Ch 3: Description and Probability (~2,000 words)

Prefix-free codes. Kraft's inequality. The bridge: $P(i) \propto 2^{-\ell_i}$. Description length and probability are the same structure seen from two sides.

**Key diagrams:** Prefix tree; Kraft slabs.

### Ch 4: Solomonoff Induction (~2,500 words)

The library of all programs. The universal Turing machine. The universal prior $M(x) = \sum_{p : U(p) = x\star} 2^{-|p|}$. The dominance theorem. Uncomputability.

**Key diagrams:** Binary enumeration tree; $M$ as stacked sum; dominance envelope.

---

## Part II: Decision (4 chapters, ~10,000 words)

### Ch 5: The Agent (~2,500 words)

Opens with the supervised / unsupervised / RL trichotomy, locating Part I and naming the move to Part II. Introduces the agent (perception, action, belief, decision). Utility and expected utility. vNM axioms. Worked examples (thermostat, umbrella). Money pump and other-criteria-in-disguise.

**Key diagrams:** Trichotomy; agent loop; expected utility bars.

### Ch 6: Reinforcement Learning (~2,500 words)

The state-action-reward setting. Discounting (time preference; economics, psychology, biology). Value functions and the Bellman equation. Q-learning (off-policy) vs SARSA (on-policy); epsilon-greedy. Exploration vs exploitation; bandits; UCB; Thompson sampling. Value of information (Howard 1966).

The "Beyond tables" material that was previously in this chapter moves to Ch 7.

**Key diagrams:** RL loop with reward; three-armed bandit with uncertainty bands.

### Ch 7: Generalization (~2,500 words, NEW)

Why tabular methods do not scale. Function approximation as the fix. Hand-crafted features (Pac-Man example) vs learned features (DQN, AlphaGo). Brief introduction to neural networks as parameterized function approximators (single linear unit, expressive limits, MLP; nod to draw on the scratchnn series). The no-free-lunch theorem. Inductive biases as the dominant story in modern ML (CNNs, RNNs, transformers, pre-training, transfer learning). Solomonoff as the universal-but-uncomputable limit case. Sample efficiency and inductive bias as two ways of describing the same property.

**Key claim:** Modern ML is largely the engineering of inductive biases. The choice of architecture is the choice of which problems the system can learn efficiently. Solomonoff sits at the limit: universal bias, uncomputable. Real systems trade coverage for tractability.

**Key diagrams:** Tabular Q vs parametric Q (already drafted); a simple MLP / function-approximator schematic; the no-free-lunch trade-off (loosely: bias breadth vs sample efficiency).

### Ch 8: AIXI (~2,500 words)

The synthesis. Solomonoff induction for prediction; expected utility maximization for action. Together: AIXI, the optimal universal agent. Properties (self-optimizing, Pareto-optimal). Uncomputable. Bounded approximations (AIXItl, MC-AIXI-CTW).

**Key claim:** Bayes plus Solomonoff plus expected-utility maximization is a complete theory of optimal agency. We now know what intelligence is in the limit. Everything that follows is about what happens when we try to build it.

**Key diagrams:** AIXI architecture (predict → evaluate → act → observe → update); the action selection equation visualized; AIXI vs bounded approximations.

---

## Part III: The Specification Problem (4 chapters, ~8,500 words)

The clean theory of why alignment is hard. Treated pedagogically, in idealized settings, before Part IV brings in the messy empirical reality.

### Ch 9: Reward Modeling (~2,000 words)

Specifying what we want. The naive view (write down a reward function) and why it fails. Goodhart's law: when a measure becomes a target. The variants (regressional, extremal, causal, adversarial; Manheim and Garrabrant 2018). Reward hacking formally defined (Skalse 2022). The alignment problem in miniature, introduced in idealized settings before any specific AI system is mentioned.

**Key diagrams:** Boat going in circles (specification gaming canonical image); Goodhart's law as proxy-vs-true-goal correlation breaking under optimization pressure; reward hacking taxonomy.

### Ch 10: Inner Alignment (~2,000 words)

The deeper specification problem. Outer alignment vs inner alignment (Hubinger et al. 2019). Mesa-optimization: when learned systems contain optimizers with their own objectives. Deceptive alignment as the structural worry: a mesa-optimizer with situational awareness might behave aligned during training to preserve its objective for deployment.

This is the clean theory. The empirical evidence (Sleeper Agents, Alignment Faking, In-context Scheming) is handled in Part IV when we look at actual systems.

**Key diagrams:** Outer optimizer producing inner optimizer; deceptive alignment as training-vs-deployment behavior divergence.

### Ch 11: Why Optimization Is Dangerous (~2,500 words, NEW)

The structural argument. Capability without alignment is the central problem, and the math of optimal agency is what makes the case.

Three claims:

1. **Orthogonality thesis** (Bostrom 2012). Intelligence and final goals are orthogonal. A superintelligent paperclip maximizer is coherent. Capability does not imply benevolence; there is no fact-value link in the architecture of optimization that makes good goals fall out of capability.

2. **Instrumental convergence** (Omohundro 2008, Bostrom 2014; formalized in Turner et al. 2021, "Optimal Policies Tend to Seek Power"). Regardless of terminal goal, capable agents pursue a small convergent set of subgoals: self-preservation, goal-content integrity, cognitive enhancement, resource acquisition. The argument is decision-theoretic, not psychological.

3. **Capability amplifies misspecification.** Bostrom's "perverse instantiation," Yudkowsky's "outcome pump." An optimal optimizer of a hackable proxy finds *every* exploit, immediately. AIXI is the limit case: optimal pursuit of whatever reward signal it is given, against all computable models, with no implicit human-friendly priors.

The pedagogical move: the same mathematical optimality that made AIXI the reference point in Ch 8 makes it the worst case for misaligned reward. The closer real systems get to AIXI in capability, the more the structural argument matters. Russell's *Human Compatible* critique of the standard model is the natural pivot to mitigations (Ch 12): if the standard model is dangerous, then the response is to change the architecture, not just tune the reward.

**Key claim:** The argument does not depend on AI consciousness, intentionality, or human-like motivation. It depends only on the AI being good at what it does. The threat of capable misalignment is structural, not psychological.

**Key diagrams:**
- Paperclip maximizer image (compresses orthogonality + instrumental convergence into one anchor).
- Instrumental convergence as a many-to-few diagram: many terminal goals pointing to the same convergent subgoals.
- The outcome pump / perverse instantiation as visualization: a search procedure that finds the worst-scoring-on-goal way to satisfy the proxy.

### Ch 12: Mitigations and Their Limits (~2,000 words, light treatment)

The three buckets. Every working alignment technique falls into one of:

1. **Limit the optimizer** (capability control, RSPs, boxing, myopia, BoMAI). Reduce search depth or scope. Limits what damage misspecification can do, at the cost of capability.
2. **Make the agent uncertain about its objective** (CIRL / *Human Compatible*; corrigibility as singular target). An agent that does not know what it wants is less dangerous than the agent that confidently wants the wrong thing.
3. **Make the agent's reasoning observable** (interpretability: probes, SAEs, circuit tracing; debate; AI Control; CoT-as-probe). The agent that knows it can hide is more dangerous than the agent whose reasoning can be read.

Light treatment of each: one canonical example, what it can do, what it cannot. The detail goes in footnotes and a Further Reading section at the back of the book. The literature is enormous; the chapter is pedagogical.

**Key claim:** None of these is a solution. Each pushes back the threshold at which misalignment becomes catastrophically hard to detect. The honest assessment: capabilities are rising faster than mitigations are scaling.

**Key diagrams:**
- The three buckets as a 3-panel diagram (limit / uncertain / observable), with one canonical technique in each panel.
- The CoT-as-probe diagram (preserved from the old Ch 14 plan), showing the strategic move of keeping a signal off the training target so it remains informative.
- The "what is left undone" closing illustration: a bar showing how much of the gap each bucket covers.

---

## Part IV: Reality (5 chapters)

Where the clean theory of Part III meets actual systems. LLMs as the running example, split across two chapters (what a base model is, then how it is trained). The gap. Then where the trajectory is going (the structural case for continuation, the jagged edge, recursive self-improvement). Then the finale, which takes the stand and carries the stakes. This is the messy part; the reader has been prepared for it.

### Ch 13: Large Language Models (~3,500 words)

What a base language model actually is. The horizon framing (a second in 2013, a day in 2026; METR). A short history (AlexNet, AlphaGo, AlphaStar, GPT-2/3, ChatGPT, GPT-4, reasoning models, scaffolded agents). Next-token prediction as the training objective; cross-entropy and Shannon coding. The transformer, and what its four biases commit to (long-range attention, soft retrieval, causal masking, compositional layers). Scaling laws (Kaplan 2020, Chinchilla 2022). The Solomonoff connection: the four-perspective convergence (MLE / cross-entropy / Shannon / Solomonoff) and the two-layer boundedness (function class + point-estimate inference).

**Key claim:** a base LLM is a bounded approximator of Solomonoff's $M(x_t \mid x_{<t})$, restricted to transformer-parameterized distributions trained on human text. Not Solomonoff; the closest practical realization of the same conceptual object.

**Key diagrams:** horizon timeline; simplified transformer block; information-flow comparison (CNN/RNN/Transformer); attention-mask matrices (causal vs bidirectional).

### Ch 14: Reward and Reasoning (~2,500 words)

How a base predictor becomes an assistant and an agent. RLHF (learned-proxy reward, hackable, the specification problem in production clothes). RLVR (verifiable reward, the proxy is the goal, the specification problem sidestepped within the verifiable regime). The GOFAI revival: generation-versus-verification asymmetry; symbolic verifiers as trusted reward signals. Inference-time search (AlphaGo recipe generalized; reasoning models). Why the verifiable regime is clean and most of what we want is not in it.

**Key diagrams:** the RLVR loop (policy + verifier).

### Ch 15: The Gap (~2,000 words)

What the theory (AIXI) says we want. What the practice (LLMs, deep RL, bounded approximators) gives us. The systematic differences: bounded vs unbounded, approximate vs optimal, opaque vs transparent, proxy-reward vs true-reward, situation-aware vs not. The gap as a map. Each safety concern from Part III now locates on the map.

The empirical results land here: Sleeper Agents (Hubinger 2024), Alignment Faking (Greenblatt 2024), In-context Scheming (Meinke 2024), Emergent Misalignment (Betley 2025), Natural Emergent Misalignment from Reward Hacking (MacDiarmid 2025). The clean theory of Part III is now applied to actual observations.

**Key diagrams:** AIXI vs LLM properties side-by-side; the gap as the visualized difference; map of concerns with each empirical result placed where the theory predicts the gap.

### Ch 16: What's Ahead (the trajectory)

The forward-looking chapter. It takes the reader from what these systems are (Ch 13, 14) and the gap (Ch 15) to where the trajectory is going and why, building the structural case for continuation without dated prophecy. This is also the home for the Moravec / jagged-edge and System-1 / System-2 material.

Sections:
1. **The scaling story, honestly.** What actually drove the last few years: not mainly Moore's law (per-transistor density) but total compute (more chips), more data, more training, and algorithmic progress. Moore's law as the long-arc enabler (LLMs were impossible twenty years ago for lack of compute); the recent surge is spend plus algorithms. Scaling laws (Kaplan 2020, Chinchilla 2022) as the empirical regularity.
2. **The economics of continuation.** AI investment is large in absolute terms but small against world output and against the value of automating cognitive labor. The headroom is enormous; rational actors keep spending while the returns hold. The structural reason to expect continuation, not optimism.
3. **Benchmarks and underestimation.** The "too hard to be a useful metric" to "too easy to be a useful metric" saturation dynamic. The MATH forecasting episode (a 2021 forecast badly beaten by Minerva in 2022; the level people thought was years away arrived almost at once). Forecasters, including experts, systematically underpredict. [verify exact figures at draft]
4. **The jagged edge (alien minds).** Compute-parity-with-the-brain as an order-of-magnitude heuristic, not a milestone (brain-FLOP estimates span orders; Carlsmith / Open Phil). Why parity is jagged: different inductive biases than humans give a different capability profile (Moravec; superhuman and subhuman in an unfamiliar pattern). Humans are not very general either; systems closer to a universal learner (fewer, different priors) generalize along axes we do not. System 1 / System 2 as architecture: the forward pass is amortized fast inference; chain-of-thought, RLVR, and inference-time search are the deliberate layer, and the task-horizon curve is the System-2 scaling curve. The "one year is four years of human development" pace metaphor, marked as analogy.
5. **The burden has shifted.** The structural argument: scaling has held, investment rises because the returns are real, algorithms compound, parity heuristics put us in the zone. The book asserts a directional stand, not a dated one: continuation is now the default, and betting against it requires a positive argument the skeptics have not supplied. Recursive self-improvement and coding as the mechanism by which the trajectory could steepen (AI accelerating AI research; coding is where it bites first). [verify the Anthropic recursive-self-improvement piece at draft]

**Key claim:** the trajectory is a structural inference, not a prophecy. The drivers (compute, data, algorithms, investment) are nowhere near saturation, so the burden of proof has shifted to the skeptic.

**Key diagrams:** scaling laws (loss vs compute / data / parameters); compute over time with Moore's law overlaid (the recent surge is spend plus algorithms, not transistors); benchmark saturation with forecaster medians marked; the jagged frontier (capability profile, human vs model).

---

### Ch 17: Teaching Sand to Think (the finale)

The finale. It fuses the conceptual stand, the awe, and the stakes. The book's spine arrives at its committed conclusion: maximizing prediction is intelligence; these are real minds built of sand; there is no magic substrate; and we cannot yet specify what we want them to do. This chapter absorbs and reframes the former "The Stakes": the existential register and the CoT-cordon material stay; the conceptual stand and the awe are added; the title pays off at the close.

Sections:
1. **The stand: prediction is intelligence.** Named without hedging, and impersonally, because fifteen chapters earned it. Solomonoff and AIXI built it; the LLMs realize it in bounded form. Brains also minimize prediction error (predictive coding, marked as a bridge, not authority). The brain is larger, but radical intelligence does not require that many parameters, and there is no magic substrate.
2. **The existential register.** Capability amplifies misspecification without a built-in bound; the AIXI worst case; instrumental convergence. A structural possibility that follows from the mathematics, stated plainly and left for the reader to weigh, not a forecast.
3. **The signals that must stay off-target.** The CoT-cordon material (kept in full): our most important instrument is faithful only while nothing needs it otherwise, fragile in three directions (direct gaming blocked by the cordon, selection and legibility drift not, situational awareness already underway), and the selection erosion falls on interpretability too. The whole book's theme arriving at the instrument.
4. **Two registers of stakes.** The existential register and the quieter societal and labor register (cross-referencing *A Note on Consequences*), now informed by the Moravec point from Ch 16: automation reaches cognitive work first, reversing the twentieth-century pattern.
5. **The book in one view.** The closing synthesis figure (theory on top, practice below, the gap between, mitigations as partial bridges).
6. **Teaching sand to think.** The final beat. We taught sand to think. The astonishment and the danger are one fact: we built real minds and the specification problem is unsolved. The burden has shifted; what the reader does with that, having seen it clearly, is the reader's.

**Key diagrams:** the CoT-cordon loop (kept, with the outer-loop selection arrow); the book-in-one-view synthesis.

#### Former Stakes sections now redistributed

The chapter currently titled *The Stakes* (file `16_the_stakes.tex`) supplies most of the finale's raw material. Its "what is settled / what is being tried / country of geniuses" content moves to Ch 16 (What's Ahead); its CoT-cordon, existential, two-registers, and book-in-one-view sections stay in the finale. For reference, the former section list was:

1. **What is settled.** Capabilities are rising fast (METR time horizons doubling). Reasoning models are real. The specification problem is the central problem. The gap is real and structural. (Moves to Ch 16.)
2. **What is being tried.** RLHF, Constitutional AI, scalable oversight techniques, mechanistic interpretability (SAEs, circuit tracing, linear probes). The Anthropic interpretability research line and its limits. (Stays, feeding the finale's signals section.)
3. **The CoT-Goodhart example.** Reasoning models produce internal chain-of-thought before final output. The model is rewarded on the final output, not the CoT. This is deliberate: training on CoT would let the model shape its CoT to pass our rewards. Keeping CoT off the training signal preserves it as a probe, but the cordon is **necessary, not sufficient**. It blocks the direct gaming (training on the CoT). It does not block two other erosions: (a) **selection pressure** from acting on what the monitor reads (flag/halt/discard/prefer-the-clean-recipe), which is Goodhart routed through the outer loop of training and deployment rather than the per-token reward, so the cordon never touches it. This selection erosion is **not specific to the CoT**: it falls the same way on any window we gate on, mechanistic interpretability (SAEs, linear probes, circuit tracing) included, because reading structure off the weights defeats direct gaming but not selection. Selection is a property of the oversight loop, not of the signal; (b) **legibility drift**, because a CoT never rewarded for readability is shaped toward an efficient computational substrate, not human communication, and can go dark with nothing gaming it (early evidence of less-readable CoT; latent-reasoning architectures with no legible trace). A third pressure, **situational awareness**, is already present in weak form (Ch 15: eval-aware behavior, alignment faking) rather than a future threshold, so the older "the moment the model becomes capable enough to know it is watched" framing is a gradient already underway. The strategic point survives (some signals must stay off-target to remain informative), but the technique is fragile in three independent directions, only one of which the cordon holds. The alignment problem solved one specific way, with all its tensions visible. Mechanistic interpretability (linear probes, SAEs) gives orthogonal windows with their own limits.
4. **The "country of geniuses" moment.** Amodei's framing: in the near term (timeframes in the 2027-2028 range have been put forward seriously), AI systems may approximate a population of expert researchers working in parallel. If we accept the framing, the gap matters more, faster.
5. **The stakes and the framework.** The book does not commit to a P(doom) number. It does commit to: the specification problem is central; capabilities are arriving faster than safety techniques are scaling; the gap is where it turns. The reader now has the tools to think about this without being captured by hype or by dismissal.

**Key diagrams:** The CoT-Goodhart loop (with the cordon between observable output and internal CoT); mechanistic interpretability tools shown as probes orthogonal to training signal; a closing diagram tying the book together (math at top, practice at bottom, gap in middle, safety work as bridges across).

---

## Notes on the new structure

**Why a separate Specification Problem part.** The alignment problem is the central problem the book is in conversation with. Treating it as a single Ch 8 (the old plan) understates its weight. As its own part of three chapters, it gets the room to develop the theory cleanly before applying it to messy systems.

**Why Reality is its own part.** Once the theory of specification is built (Part III), the practice can be presented as a separate move. LLMs, the gap, the stakes are not just the end of the alignment story; they are a different mode (empirical, contested, current) than the clean theory in Part III. Separating them lets each be its own thing.

**Why GOFAI is not a chapter.** GOFAI is mentioned as historical context in Ch 12 and reappears as the source of verifiable reward signals in RLVR. That is a richer role than a stand-alone chapter would give it. The "GOFAI failed" story is brief; the "GOFAI provides excellent reward signals" story is the live one.

**Why Generalization is a new chapter.** Function approximation, inductive biases, learned representations, and the no-free-lunch trade-off are the conceptual glue between the optimal-agent theory (Solomonoff, AIXI) and the practical-agent reality (LLMs). Putting these in a dedicated chapter (Ch 7) gives the reader the right vocabulary and makes the spine of the book visible earlier.

---

## Drafting order so far

- Ch 1 (Bayes) ✓
- Ch 2 (The Prior Problem) ✓
- Ch 3 (Description and Probability) ✓
- Ch 4 (Solomonoff Induction) ✓
- Ch 5 (The Agent) ✓
- Ch 6 (Reinforcement Learning) ✓
- Ch 7 (Generalization) ✓
- Ch 8 (AIXI) ✓
- Ch 9 (Reward Modeling) ✓ (Part III opens)
- Ch 10 (Inner Alignment) ✓
- Ch 11 (Why Optimization Is Dangerous) ✓
- Ch 12 (Mitigations and Their Limits) ✓
- Ch 13 (Large Language Models) ✓ (Part IV opens)
- Ch 14 (Reward and Reasoning) ✓
- Ch 15 (The Gap) ✓
- Ch 16 (The Stakes; substantial closing) ✓

First full draft complete: all 16 chapters plus backmatter. The substantial closing (Ch 16) drafted last, after the full apparatus was in place. The backmatter "A Note on Consequences" owns the societal-outcomes register (resource curse, meaning/identity); Ch 16 owns the existential register plus mechanistic interpretability and CoT-Goodhart, cross-referencing the note rather than duplicating it.

---

## Notes on salvage from prior material

The old "Multitudes" chapters in `chapters/` (now commented out in `multitudes.tex`) have been mostly drained. The math salvaged into Chs 1–4. The observer / agency framing salvaged into Ch 5. Remaining old chapters (Ch 6 The Slip, Ch 7 The Inhabited Library, Ch 8 The Observer, Ch 9 Indifference of Measure, Ch 10 Continuation) are not in the new book and can be moved to `chapters/archive/` at any time.

## Source for NN material

`~/github/repos/scratchnn/docs/series/*.md` is the author's existing post series on neural networks built from scratch in Python. Ch 7's brief NN section can draw on this for tone, depth, and pedagogical sequence (foundations → fixed-context LM → RNN → CNN → transformer → interpretability). The book's NN section will be much briefer (a few paragraphs, not the full series).
