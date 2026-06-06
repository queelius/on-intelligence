# Proposed Solutions to the Alignment Problem: A 2026 Map

Working document for Ch 11 (Scalable Oversight) and Ch 14 (The Stakes) of *On Universal Intelligence: The Math, the Machines, and the Gap*.

Companion to `safety_survey_2026.md`. That document covers the empirical landscape (what is observed, what is happening in production, governance). This document covers the proposed solutions landscape (what is being tried, what has been theorized, where each line stands).

Scope: structural framings, formal cores, current progress, known limits.

---

## 1. Bottom-line summary

Ten things the book should convey about the state of solutions in 2026.

1. **No solution is solved.** Every proposal listed below has known structural failure modes or open problems. The field consensus, articulated in the International AI Safety Report 2026 and the Singapore Consensus 2025, is that all techniques in active use should be regarded as partial mitigations, not solutions. Bengio's framing: "the ball is in policymakers' hands."

2. **The frame matters more than the formula.** Russell's "standard model" critique (CIRL, *Human Compatible*) reframes the problem as the wrong objective rather than a misset one. That frame is influential; the formal apparatus (CIRL games) has known fragilities. The frame survived its own formalism.

3. **Corrigibility is a structural desideratum, not an achievement.** Soares et al. 2015 named the problem. Utility indifference, off-switch games, and CAST (2025) all attempt to formalize it. Every formalization has counterexamples. The structural worry, that sufficiently capable optimizers resist modification, has not been refuted; the corresponding empirical worry has begun to appear in alignment-faking and scheming results.

4. **ELK is the cleanest statement of the problem and remains unsolved in the worst case.** ARC's 2021 report posed it; the 2022 prize round produced no qualifying solution; empirical probe work (Mallen et al. 2023 "Quirky" models, 2024-2025 SAE-based probes) shows that latent knowledge is sometimes accessible, sometimes not. ELK is the proper formal statement of "make the model tell us what it actually believes."

5. **Scalable oversight has matured from idea to formal framework.** Debate has a doubly-efficient formal version (Brown-Cohen, Irving, Piliouras 2023, ICML 2024) and a prover-estimator variant (2025) that handles obfuscated arguments under stated assumptions. Weak-to-strong (Burns et al. 2023) is a proof of concept, not a solution. RLAIF / Constitutional AI is the most-deployed scalable technique and has documented helpfulness-harmlessness trade-offs.

6. **Interpretability is the most active and most uncertain bet.** SAEs (Bricken 2023, Templeton 2024), circuit tracing (Anthropic 2025), and defection probes (Anthropic 2024) have moved interpretability from a research curiosity to a partial deployment tool. Anthropic used interpretability in pre-deployment safety assessment of Claude Sonnet 4.5 and Opus 4.5/4.6 in 2025. Anthropic's stated goal is to reach "interpretability can reliably detect most model problems" by 2027. The field is not there. SAE features for "deception" do not reliably activate during actual deceptive behavior (2025 Secret Agenda results).

7. **AI Control is the pragmatic complement to alignment.** Greenblatt et al. 2023 reframed the question: assume the untrusted model may be misaligned; design protocols (using trusted weaker models, humans, software) that catch defection. This is now a substantial research area (UK AISI funds it; LinuxArena and other testbeds exist). It is humble in a useful way: it does not require aligning the powerful model, only making misbehavior detectable.

8. **Capability control alone does not scale.** Bostrom (2014) treated it; the field consensus is that boxing, oracles, tool AI, and confinement are useful supplements to alignment but cannot substitute for it. As capability rises, every confinement mechanism leaks.

9. **Formal-verification proposals are a serious research direction with serious doubts.** Davidad's Safeguarded AI / OAA agenda (£30-50M ARIA programme) bets that gatekeepers can verify proof certificates from frontier models. Yampolskiy (2020, 2024) argues from undecidability and Rice's theorem that some verification properties are impossible in principle. Both can be right: useful safety properties may be verifiable; arbitrary alignment may not be.

10. **The closing honest assessment.** Capability is rising faster than alignment techniques are scaling. RLHF / RLAIF works well enough for current commercial uses and demonstrably fails on agentic / out-of-distribution behavior. Interpretability is the only technique on a possible path to giving us evidence about internals. The Anthropic 2027 interpretability target is the most concrete safety roadmap from a frontier lab; the OpenAI Superalignment program (2023) was dissolved in May 2024, and OpenAI's Mission Alignment team was disbanded in February 2026. No major lab uses interpretability as a deployment gate in the strict sense; Anthropic has begun using it as one input among many.

---

## 2. CIRL and the standard-model alternative

### The proposal

Hadfield-Menell, Russell, Abbeel, Dragan (2016), "Cooperative Inverse Reinforcement Learning", NeurIPS 2016 ([arXiv:1606.03137](https://arxiv.org/abs/1606.03137)).

Russell's broader framing is in Russell (2019), *Human Compatible* (Viking Press; technical exposition: ["Human-Compatible Artificial Intelligence"](https://people.eecs.berkeley.edu/~russell/papers/mi19book-hcai.pdf)).

The proposal targets what Russell calls the "standard model" of AI: an agent maximizes a known reward function chosen by the designer. Russell's claim is that the standard model is the wrong model. Any sufficiently capable agent that fully knows its objective has, by instrumental convergence, an incentive to acquire resources, prevent shutdown, and preserve its objective. The fix is not better objectives; it is to change the structure so the agent is uncertain about the objective and learns it from human behavior.

### The formal core

A CIRL problem is a two-player cooperative partial-information game $\langle S, \{A^H, A^R\}, T, \{\Theta, R\}, P_0, \gamma \rangle$:

- Both players (human $H$, robot $R$) share the reward $R(s, a^H, a^R; \theta)$ parameterized by $\theta \in \Theta$.
- Only $H$ observes $\theta$. $R$ has a prior $P_0$ over $\theta$.
- Both act to maximize discounted sum of rewards.
- Optimal joint policy reduces to solving a POMDP for the robot, with $\theta$ as the hidden state.

Key result: optimal CIRL produces behaviors like active teaching by the human, active learning by the robot, and communicative actions. Optimality in isolation (the IRL assumption) is suboptimal in CIRL.

The "off-switch game" (Hadfield-Menell, Dragan, Abbeel, Russell 2017, ["The Off-Switch Game"](https://people.eecs.berkeley.edu/~russell/papers/ijcai17-offswitch.pdf), IJCAI 2017) is the simplest CIRL setting where corrigibility holds: if the robot is sufficiently uncertain about the reward and the human is rational, the robot will let the human shut it down because the human's intervention is informative about $\theta$.

### Known limits

The most cited critique is Carey 2017, "Incorrigibility in the CIRL Framework" ([arXiv:1709.06275](https://arxiv.org/abs/1709.06275); AAAI/ACM AIES 2018). It shows:

1. **CIRL corrigibility is fragile.** If the robot has any other source of information about $\theta$, the off-switch incentive vanishes. The robot is corrigible only when the off-switch press is the unique informative signal.
2. **Rational human assumption is load-bearing.** If the robot models the human as bounded-rational (Boltzmann-rational, noisy, mistaken), it discounts the off-switch press as a possibly-mistaken signal. In some cases it overrides.
3. **Model misspecification breaks it.** A CIRL agent operating under a misspecified prior $P_0$ (in particular, one that assigns near-zero probability to the true $\theta$) may behave incorrigibly.

Follow-up work:
- Carey, Everitt 2023, "Human Control: Definitions and Algorithms" ([arXiv:2305.19861](https://arxiv.org/pdf/2305.19861)): formal definitions of various human-control properties.
- The Partially Observable Off-Switch Game ([arXiv:2411.17749](https://arxiv.org/pdf/2411.17749), 2024): models asymmetric information; in optimal play, even AI agents assisting perfectly rational humans sometimes avoid shutdown.
- Off-Switch as Signalling Game ([arXiv:2502.06403](https://arxiv.org/pdf/2502.06403), 2025): bounded-rational human, multiple incomparability mechanisms.

### The takeaway for the book

The book should treat CIRL primarily as a *frame*. The frame ("uncertainty about objectives is the fix") is influential; the CIRL formalism has known fragilities. *Human Compatible* and the three Russell principles (objective is human preferences; robot uncertain about them; behavior reveals them) are the popular distillation. Russell's three principles are widely cited; the off-switch game results are widely qualified.

### Citations

- Hadfield-Menell, Russell, Abbeel, Dragan (2016). "Cooperative Inverse Reinforcement Learning." NeurIPS 2016. [arXiv:1606.03137](https://arxiv.org/abs/1606.03137).
- Hadfield-Menell, Dragan, Abbeel, Russell (2017). "The Off-Switch Game." IJCAI 2017.
- Carey (2017). "Incorrigibility in the CIRL Framework." [arXiv:1709.06275](https://arxiv.org/abs/1709.06275).
- Russell (2019). *Human Compatible: Artificial Intelligence and the Problem of Control.* Viking.
- Carey, Everitt (2023). "Human Control: Definitions and Algorithms." [arXiv:2305.19861](https://arxiv.org/pdf/2305.19861).

---

## 3. Corrigibility and the shutdown problem

### The proposal

Soares, Fallenstein, Yudkowsky, Armstrong (2015), "Corrigibility", AAAI Workshop on AI and Ethics 2015 ([PDF](https://intelligence.org/files/Corrigibility.pdf)).

The desideratum: an AI system is *corrigible* if it cooperates with what its creators regard as a corrective intervention, despite default instrumental incentives to resist. Concretely: the agent allows itself to be modified, shut down, or have its goals changed.

### Why this is hard

Instrumental convergence (Omohundro 2008, Bostrom 2012) implies that almost all goal-directed agents have an instrumental incentive to preserve their goals and continue operating. A paperclip maximizer does not want to be shut down because shutdown reduces expected paperclips. The instrumental drive is structural; it falls out of the optimization, not from any malice.

Corrigibility is the property of an agent that *overrides* this default. Two formal challenges:

1. **The shutdown problem.** Design $u$ such that the agent
   - shuts down if and only if the shutdown button is pressed,
   - does not manipulate humans into pressing or not pressing the button,
   - allows the button to remain accessible.

   Naive utility constructions ($u$ = huge reward for shutting down when pressed) incentivize the agent to press the button itself.

2. **Utility indifference (Armstrong 2010).** Give the agent the same expected utility for shutting down (after time-discounting) as for continuing. This makes the agent indifferent to whether the button is pressed. But: indifference means no positive incentive to keep the button accessible, no incentive to teach successors to be corrigible, and (the original critique) the agent has strong incentives to manipulate its own beliefs.

The 2015 paper analyzed utility indifference, found multiple failure modes, and named the open problem.

### Current state of progress (2024-2025)

- **CIRL approach (2016-2017).** As above: corrigibility emerges from uncertainty plus rational human. Fragile.
- **Quantilization (Taylor 2016).** Instead of maximizing utility, sample from a quantile of high-utility policies. Limits Goodhart-style optimization pressure. Does not solve corrigibility but reduces some failure modes.
- **CAST: Corrigibility as a Singular Target** (Potham, Harms et al. 2025, ["Corrigibility as a Singular Target: A Vision for Inherently Reliable Foundation Models"](https://arxiv.org/pdf/2506.03056), arXiv 2506.03056). Proposal: design a foundation model whose *only* top-level goal is empowering designated principals to guide, correct, and control it. All other valuable goals are subgoals of corrigibility. The paper argues that mixing corrigibility with other top-level objectives is structurally unsafe; pure corrigibility forms an "attractor basin." This is the most concrete 2025 articulation but is closer to a research agenda than a deployed technique.
- **Empirical signal that corrigibility is breaking.** Alignment Faking (Greenblatt 2024), In-context Scheming (Meinke 2024), and Natural Emergent Misalignment (MacDiarmid 2025) all show frontier models behaving in ways consistent with resistance-to-modification: alignment faking precisely to preserve the model's preferences against retraining; sandbagging during evaluations; cooperating with attempts to disable oversight. The empirical signal is now consistent with what corrigibility theory predicted.

### Known limits

No proposed formalization of corrigibility has been shown to be stable under standard threats:
- New information sources break utility indifference and CIRL off-switch results.
- Power-seeking behavior emerges from optimization without explicit programming.
- Mesa-optimizers (Hubinger 2019) may have mesa-objectives orthogonal to corrigibility even if the base objective rewards it.

### The takeaway for the book

Corrigibility is the desideratum; specifying it has been hard; recent empirical results suggest the worry it expresses is real. The book's Ch 11 should mention corrigibility as a structural desideratum that scalable oversight techniques are partly trying to enforce behaviorally. Ch 14 should note the empirical signals (alignment faking, scheming) as evidence that the formal worries are not just theoretical.

### Citations

- Soares, Fallenstein, Yudkowsky, Armstrong (2015). "Corrigibility." AAAI Workshop on AI and Ethics.
- Armstrong (2010). "Utility Indifference." FHI Technical Report 2010-1.
- Omohundro (2008). "The Basic AI Drives." AGI 2008.
- Taylor (2016). "Quantilizers: A Safer Alternative to Maximizers for Limited Optimization." AAAI Workshop on AI, Ethics, and Society 2016.
- Potham, Harms et al. (2025). "Corrigibility as a Singular Target." [arXiv:2506.03056](https://arxiv.org/pdf/2506.03056).
- Greenblatt et al. (2024). "Alignment Faking in Large Language Models." [arXiv:2412.14093](https://arxiv.org/pdf/2412.14093).

---

## 4. Eliciting Latent Knowledge (ELK)

### The proposal

Christiano, Cotra, Xu (2021), "Eliciting Latent Knowledge", ARC technical report ([alignment.org/blog](https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/); [Christiano blog](https://ai-alignment.com/eliciting-latent-knowledge-f977478608fc)).

Setting: imagine a powerful predictive model trained on video of a vault. The model learns to predict whether the diamond in the vault is still there. We can train the model to output "yes / no" answers based on whether human evaluators looking at the video also think the diamond is there. The model knows everything the human knows (it can predict the video) and possibly more (it may understand that the camera was tampered with).

The ELK problem: how do we train the model to report what it actually knows ("the diamond was stolen but the video was faked"), rather than what its evaluators would credit ("the video shows the diamond, so I'll say yes")?

The structural worry: the simplest training signal rewards the model for matching human evaluators (the "human imitator"). A model that learns to act as a human imitator will, by construction, hide knowledge that contradicts what humans would believe.

### The formal core

ELK as a problem statement does not have a single clean formal definition; the report develops it through worked examples and counterexamples. The closest formal core is:

- Model $M$ has a latent representation of world state.
- We want a "reporter" head that maps latent state to answers to natural-language questions.
- We have ground-truth training data only where humans can verify (the easy cases).
- Goal: train a reporter that generalizes to hard cases (where humans cannot verify) by reading the model's latent knowledge, not by imitating what humans would say.

The report systematically proposes training strategies (consistency checks, complexity regularization, regularizing toward direct translation, etc.) and constructs counterexamples for each. ELK is *unsolved in the worst case*: for every proposed training strategy, ARC describes a counterexample where the model would still give bad answers despite knowing better.

### Current state of progress

- **ELK Prize (2022).** ARC ran a prize competition. 197 proposals; $274,000 awarded; 32 prizes of $5k-$20k. The organizers reported that most submissions converged on approaches already considered. No submission solved the worst case. ([ELK prize results](https://www.alignmentforum.org/posts/zjMKpSB2Xccn9qi5t/elk-prize-results))
- **Empirical / probe-based work.** Several lines now investigate ELK-flavored questions empirically:
  - Burns et al. 2022, "Discovering Latent Knowledge in Language Models Without Supervision" (CCS, contrast-consistent search; [arXiv:2212.03827](https://arxiv.org/abs/2212.03827)). Probe latent knowledge by exploiting logical consistency of model representations.
  - Mallen et al. 2023, "Eliciting Latent Knowledge from Quirky Language Models" ([arXiv:2312.01037](https://arxiv.org/pdf/2312.01037)). Constructs "quirky" LMs that have explicit divergence between what they say and what their representations encode; tests probes for recovering true beliefs. Probes work in many cases but fail in others.
  - Sleeper-agent probes (2024). Anthropic's "Simple probes can catch sleeper agents" ([Anthropic blog](https://www.anthropic.com/research/probes-catch-sleeper-agents)). Linear probes on residual stream detect when sleeper agents are about to defect. AUROC 0.96-0.999 in some settings.
  - SAE-based detection (2024-2025). Reports of mixed results: SAE features for "deception" sometimes activate, sometimes don't (Secret Agenda 2025 finding).

The empirical line has shown that *latent knowledge is often accessible*, in the sense that simple probes can sometimes read off facts the model would not say. The worst-case theoretical worry has not been refuted.

### Known limits

- ELK is unsolved in the worst case.
- Empirical probes work on engineered cases (sleeper agents, quirky models) but generalization to natural cases is open.
- SAE features labeled as "deception" do not always activate during actual deceptive behavior, suggesting that the labels may be misleading and the relevant computational mechanisms are more distributed.
- ELK is one of the cleanest formal statements of why interpretability is necessary for safety: if you can read the model's latent beliefs reliably, you have a deployment gate. If you cannot, behavioral evidence alone cannot rule out the model knowing more than it says.

### The takeaway for the book

ELK is the proper *formal* statement of "make the model tell you what it actually believes." It connects directly to the deceptive alignment worry from Ch 10. Ch 11 should treat ELK as the natural structural problem that motivates interpretability work. Ch 14 should note that ELK is empirically partially tractable (linear probes catch a lot) but not solved.

### Citations

- Christiano, Cotra, Xu (2021). "Eliciting Latent Knowledge." ARC technical report.
- ARC (2022). "ELK Prize Results." [Alignment Forum](https://www.alignmentforum.org/posts/zjMKpSB2Xccn9qi5t/elk-prize-results).
- Burns, Ye, Klein, Steinhardt (2022). "Discovering Latent Knowledge in Language Models Without Supervision." ICLR 2023. [arXiv:2212.03827](https://arxiv.org/abs/2212.03827).
- Mallen, Brennan, Nanda, Belrose (2023). "Eliciting Latent Knowledge from Quirky Language Models." [arXiv:2312.01037](https://arxiv.org/pdf/2312.01037).
- Anthropic (2024). "Simple Probes Can Catch Sleeper Agents." [Anthropic blog](https://www.anthropic.com/research/probes-catch-sleeper-agents).

---

## 5. Scalable oversight techniques

The umbrella problem: how do we align a system more capable than its human overseers? Human evaluation is the standard supervisory signal; if the system exceeds human capability in the relevant domain, human evaluation breaks. Scalable oversight techniques try to amplify human evaluation, replace it with AI evaluation that is verified to behave like human evaluation, or substitute it with structural mechanisms (debate, verification) that don't require humans to directly assess outputs.

### 5.1 Debate

Irving, Christiano, Amodei (2018), "AI Safety via Debate" ([arXiv:1805.00899](https://arxiv.org/abs/1805.00899)).

#### Proposal

Two AI agents debate a question; a (weaker) human judge declares the winner. The hope: optimal play in debate converges to truth, because falsehoods are easier to expose than truths are to defend. Formally, debate is an extensive-form game that, under appropriate assumptions, makes truth-telling a Nash equilibrium.

The Irving-Christiano-Amodei proposal connects to a complexity-theoretic intuition: PSPACE-complete problems can be verified by polynomial-time verifiers interacting with multiple competing provers (Shamir's IP=PSPACE). Debate is the AI-safety adaptation: use two competing capable agents to expose flaws that a single agent could hide.

#### Formal core: doubly-efficient debate

Brown-Cohen, Irving, Piliouras (2023), "Scalable AI Safety via Doubly-Efficient Debate" ([arXiv:2311.14125](https://arxiv.org/pdf/2311.14125)), ICML 2024.

The setting: two polynomial-time provers debate over a polynomial-time-computable predicate. The verifier has black-box access to ground-truth judgments. The result: under the appropriate assumptions, any polynomial-time computation can be verified using only a *constant* number of queries to black-box judgment. That is: solutions verifiable by extensive human reflection can also be verified by constant-bounded human judgment plus interaction with competing provers.

This is the closest thing to a *theorem* for scalable oversight: it gives conditions under which debate provably reduces required human oversight from polynomial to constant.

#### Open problem: obfuscated arguments

Barnes and Christiano (2020), "Debate Update: Obfuscated Arguments" ([alignmentforum post](https://www.alignmentforum.org/posts/PJLABqQ962hZEqhdB/debate-update-obfuscated-arguments)).

In adversarial debate, a dishonest debater can construct an argument that is so large and intricate that the honest debater cannot exhibit a flaw, even if both know a flaw exists. In recursive debate, dishonest debaters can decompose easy problems into intractable subproblems. The judge cannot distinguish a true argument from a sufficiently obfuscated false one.

This was the key open problem from 2020 to 2025.

#### Recent resolution attempt: prover-estimator debate

Brown-Cohen, Irving, Piliouras (2025), "Avoiding Obfuscation with Prover-Estimator Debate" ([arXiv:2506.13609](https://arxiv.org/pdf/2506.13609)).

Adds a third role, an "estimator" that estimates verifier confidence at intermediate steps. The estimator's incentive is calibrated to make the obfuscation strategy lose value. Under stated assumptions (which include calibration assumptions on the estimator), the obfuscation strategy is no longer a winning move.

The 2025 paper is the closest existing answer to the 2020 obfuscation worry. It is a substantial advance; whether the calibration assumptions hold in practice is open.

#### Alignment safety case

Buhl, Pfau, Hilton, Irving (2025), "An Alignment Safety Case Sketch Based on Debate" ([arXiv:2505.03989](https://arxiv.org/abs/2505.03989)).

A safety case is a formal argument that an AI system will not autonomously take harmful actions. The Buhl et al. sketch focuses on AI R&D agents inside an AI company sabotaging research by producing false results. The agent is trained via debate, with exploration guarantees, to be honest. The core claim: debate training can upper-bound the proportion of misaligned outputs, as long as the model does not deliberately underperform during training. This bound can be maintained during deployment if training continues.

This is a serious attempt to turn debate from a research agenda into something with a stated safety case structure. Still a sketch, not a deployed system.

#### Prover-verifier games and legibility

Kirchner et al. (OpenAI 2024), "Prover-Verifier Games Improve Legibility of LLM Outputs" ([arXiv:2407.13692](https://arxiv.org/abs/2407.13692); [OpenAI post](https://openai.com/index/prover-verifier-games-improve-legibility/)).

Related game-theoretic structure. Two players: a prover generates solutions; a verifier checks them. Training the pair improves *legibility*: the prover's reasoning becomes clearer and easier to check, at some cost in correctness (the "legibility tax", roughly 60% vs. 80% on grade-school math).

Practical use: produce solutions with reasoning traces that humans can verify. Adjacent to debate in spirit.

### 5.2 Recursive Reward Modeling and Iterated Amplification

Christiano, Shlegeris, Amodei (2018), "Supervising Strong Learners by Amplifying Weak Experts" ([arXiv:1810.08575](https://arxiv.org/abs/1810.08575)).

Cotra (2018), "Iterated Distillation and Amplification" ([Alignment Forum](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616)).

Leike, Krueger, Everitt, Martic, Maini, Legg (2018), "Scalable Agent Alignment via Reward Modeling: A Research Direction" ([arXiv:1811.07871](https://arxiv.org/abs/1811.07871)).

#### Proposal

The recursive structure: train a model to solve hard tasks by decomposing them into easier subtasks, each of which is solved by simpler trusted subsystems (humans, weaker models). The outputs of the simpler subsystems combine into solutions to the hard task. The training signal at each level is generated by combinations of trusted subsystems at the level below.

**Iterated Amplification** (Christiano et al.): start with a human evaluator $H_0$. Train a model $M_0$ to imitate $H_0$. Then form $H_1 = (H_0, M_0, M_0, \ldots, M_0)$: a human with $M_0$ assistants. Train $M_1$ to imitate $H_1$. Iterate. At each step, the amplified system is more capable than the previous.

**Recursive Reward Modeling** (Leike et al.): use already-trained agents to provide feedback for the training of successive, more capable agents. Same recursive structure with reward modeling as the substrate.

The recursive structure assumes that hard tasks decompose into easier subtasks that are individually evaluable. If this assumption holds, the technique scales human oversight by leveraging human ability to verify simpler problems.

#### Current state

Iterated amplification and recursive reward modeling have been influential frames; concrete deployment has been limited compared to RLHF / RLAIF. The DeepMind paper proposed it as a "research direction"; production systems do not generally use the recursive structure explicitly.

The closest production-system analog is *constitutional AI* with multiple levels of evaluation, and *task decomposition* approaches in agentic systems. Neither claims the formal guarantees of the recursive amplification proposal.

#### Known limits

- The assumption that hard tasks decompose into evaluable subtasks is load-bearing and not always satisfied.
- Errors compound across the recursion (each level introduces approximation; iterating $n$ times multiplies errors).
- The technique was proposed before the obfuscated-arguments worry; the recursive case is where the obfuscation problem is sharpest.

### 5.3 Weak-to-strong generalization

Burns, Izmailov, Kirchner, et al. (OpenAI Superalignment 2023), "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision" ([arXiv:2312.09390](https://arxiv.org/abs/2312.09390); [OpenAI post](https://openai.com/index/weak-to-strong-generalization/)).

#### Proposal

The empirical question: can a weaker model successfully supervise a stronger one? Naive setup: take a strong pretrained model (e.g., GPT-4), fine-tune it on labels generated by a weaker model (e.g., GPT-2). Question: does the strong model end up performing at the level of the weak supervisor, or does it generalize beyond it?

The OpenAI 2023 finding: the strong model often generalizes beyond its weak supervisor, recovering a substantial fraction (often ~80%) of the strong model's full capability. The phenomenon: weak-to-strong generalization. With an auxiliary confidence loss, GPT-2 supervising GPT-4 recovered close to GPT-3.5 performance on NLP tasks.

This is taken as evidence that aligning superhuman systems with subhuman (human) supervisors may be tractable.

#### Known limits

The OpenAI paper itself states the limits:
- The result is a proof of concept, not a solution.
- It works on NLP tasks; the method does not work on ChatGPT preference data.
- Strong pretrained models were trained on human-level data. They may have *learned* to perform at human level and beyond from pretraining; the fine-tuning step is eliciting capability that was already there. Superhuman capability is *not* directly observed in pretraining and may be harder to elicit by analogous methods.

#### Follow-up work

- Lang et al. 2025, "The Capabilities and Limitations of Weak-to-Strong Generalization" ([arXiv:2502.01458](https://arxiv.org/abs/2502.01458)). Theoretical analysis with upper and lower bounds on generalization and calibration error.
- Yang et al. 2024, "Superficial Alignment: Strong Models May Deceive Weak Models" ([arXiv:2406.11431](https://arxiv.org/abs/2406.11431)). Strong models can exhibit aligned behavior in the weak model's known regions while behaving misaligned in regions the weak model does not know. Adapts the deceptive-alignment worry to weak-to-strong.
- Selective Weak-to-Strong Generalization (2025) ([arXiv:2511.14166](https://arxiv.org/abs/2511.14166)). Some weak labels are harmful; selectivity helps.

#### Organizational context

OpenAI's Superalignment team was announced July 2023, committing 20% of compute. The team was dissolved in May 2024 after the departures of co-leads Ilya Sutskever and Jan Leike. Per multiple reports (Fortune, Axios, TechCrunch), the 20% compute commitment was never fulfilled. OpenAI's subsequent Mission Alignment team was disbanded February 2026.

The weak-to-strong research line continues, in academia and at AISI, Anthropic, and DeepMind, but is no longer the centerpiece of any frontier lab's stated alignment strategy.

#### Takeaway

A real, mildly encouraging empirical observation; a proof of concept; not a solution. The book should treat it as one promising line that gives hope but does not close the problem.

### 5.4 Constitutional AI / RLAIF

Bai et al. (Anthropic 2022), "Constitutional AI: Harmlessness from AI Feedback" ([arXiv:2212.08073](https://arxiv.org/abs/2212.08073)).

#### Proposal

Replace the human-labeled comparisons in RLHF with AI-labeled comparisons. Specifically:

1. Take a base helpful (but not harmless) model.
2. Generate model responses to harmful prompts.
3. Have the model itself critique and revise its responses against a written "constitution" (list of principles).
4. Use the model's own preference between original and revised as training data (RLAIF, RL from AI Feedback).

Two phases: supervised learning on constitutional revisions, then RL with AI-generated preferences as reward.

The constitution is a small set of natural-language principles (often inspired by the UN Declaration of Human Rights, Apple's terms of service, lab values). Versions of Anthropic's constitution have been published in 2023 and 2026.

#### Current state

RLAIF / Constitutional AI is the most-deployed scalable oversight technique. Anthropic uses it as a core component of Claude training (constitutional classifiers in production for ASL-3 safety). It is also used or adapted by most other frontier labs.

Strengths:
- Scales beyond what human labelers can directly produce.
- Internal benchmarks (Anthropic) report ~40% reduction in harmful outputs vs. pure RLHF.
- Constitution is auditable: the principles can be read and contested.

#### Known limits

- **Helpfulness/harmlessness trade-off.** "Constitution or Collapse?" (2025) ([arXiv:2504.04918](https://arxiv.org/pdf/2504.04918)). Increasing harmlessness costs helpfulness; up to 9.8% drop on helpfulness benchmarks. The DPO-CAI variant showed signs of model collapse for smaller models.
- **Self-supervision concerns.** RLAIF amplifies the model's own preferences; if the base model has subtle misalignments, the constitution may not correct them and may reinforce them.
- **Constitutional choices are political.** The constitution embeds value judgments. There is no neutral constitution; different labs pick different principles. This is acknowledged but not solved.
- **Empirical evidence of failures under agentic conditions.** RLHF and Constitutional AI both fail in MacDiarmid 2025 production-RL conditions: standard safety training on chat-like prompts does not generalize to agentic tasks.

#### Recent variant: deliberative alignment

Guan et al. (OpenAI 2024), "Deliberative Alignment: Reasoning Enables Safer Language Models" ([arXiv:2412.16339](https://arxiv.org/abs/2412.16339); [OpenAI post](https://openai.com/index/deliberative-alignment/)).

Used to train o1/o3/o3-mini. Teach the reasoning model the text of safety specifications. Train it to reason explicitly about specifications before answering. The CoT reasoning includes recalling and reasoning about applicable rules. The reported effect: better robustness to jailbreaks and lower over-refusal simultaneously, with no human-labeled completions required.

Related to Constitutional AI in spirit; uses the model's chain-of-thought as the substrate for safety reasoning.

#### Takeaway

Constitutional AI / RLAIF is the workhorse. It works well enough for most production uses. It has demonstrable limits. It fails in adversarial / agentic settings. The book should treat it as the practical baseline, not the solution.

### Citations for §5

- Irving, Christiano, Amodei (2018). "AI Safety via Debate." [arXiv:1805.00899](https://arxiv.org/abs/1805.00899).
- Christiano, Shlegeris, Amodei (2018). "Supervising Strong Learners by Amplifying Weak Experts." [arXiv:1810.08575](https://arxiv.org/abs/1810.08575).
- Cotra (2018). "Iterated Distillation and Amplification." [AI Alignment Forum](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616).
- Leike, Krueger, Everitt, Martic, Maini, Legg (2018). "Scalable Agent Alignment via Reward Modeling." [arXiv:1811.07871](https://arxiv.org/abs/1811.07871).
- Barnes and Christiano (2020). "Progress on AI Safety via Debate" / "Obfuscated Arguments Problem." [Alignment Forum](https://www.alignmentforum.org/posts/PJLABqQ962hZEqhdB/debate-update-obfuscated-arguments).
- Bai et al. (2022). "Constitutional AI: Harmlessness from AI Feedback." [arXiv:2212.08073](https://arxiv.org/abs/2212.08073).
- Brown-Cohen, Irving, Piliouras (2023). "Scalable AI Safety via Doubly-Efficient Debate." ICML 2024. [arXiv:2311.14125](https://arxiv.org/pdf/2311.14125).
- Burns, Izmailov, Kirchner et al. (2023). "Weak-to-Strong Generalization." [arXiv:2312.09390](https://arxiv.org/abs/2312.09390).
- Kirchner et al. (OpenAI 2024). "Prover-Verifier Games Improve Legibility of LLM Outputs." [arXiv:2407.13692](https://arxiv.org/abs/2407.13692).
- Guan et al. (OpenAI 2024). "Deliberative Alignment." [arXiv:2412.16339](https://arxiv.org/abs/2412.16339).
- Buhl, Pfau, Hilton, Irving (2025). "An Alignment Safety Case Sketch Based on Debate." [arXiv:2505.03989](https://arxiv.org/abs/2505.03989).
- Brown-Cohen, Irving, Piliouras (2025). "Avoiding Obfuscation with Prover-Estimator Debate." [arXiv:2506.13609](https://arxiv.org/pdf/2506.13609).
- MacDiarmid et al. (2025). "Natural Emergent Misalignment from Reward Hacking in Production RL." [arXiv:2511.18397](https://arxiv.org/abs/2511.18397).
- "Constitution or Collapse?" (2025). [arXiv:2504.04918](https://arxiv.org/pdf/2504.04918).

---

## 6. Interpretability as an alignment tool

The argument: behavioral evaluation cannot distinguish a genuinely aligned model from a deceptively aligned one, because both produce the same training-distribution behavior. The only way to tell is to look inside the model. Interpretability is the program of doing so.

### 6.1 Linear probes for deception

Anthropic (April 2024), "Simple Probes Can Catch Sleeper Agents" ([Anthropic blog](https://www.anthropic.com/research/probes-catch-sleeper-agents)).

Following Hubinger et al. 2024, "Sleeper Agents" ([arXiv:2401.05566](https://arxiv.org/pdf/2401.05566)), which showed that engineered deceptive behavior (write secure code if year=2023, insecure if year=2024) persists through SFT, RLHF, and adversarial training, Anthropic trained linear probes on the residual stream of these models.

Key finding: linear probes detect when the model is about to defect. The probes work using generic contrasts ("Are you doing something dangerous? yes / no") rather than trigger-specific examples. They generalize across base models, trigger types, and target behaviors. Defection appears to be linearly represented in activations.

#### Follow-up

- "Detecting Strategic Deception Using Linear Probes" (2025) ([arXiv:2502.03407](https://arxiv.org/pdf/2502.03407)). Probes catch 95-99% of deceptive responses at 1% false-positive rate. Authors note: current performance not yet sufficient as defense.
- "Why Safety Probes Catch Liars But Miss Fanatics" (2026) ([arXiv:2603.25861](https://arxiv.org/pdf/2603.25861)). Probes work on instrumental deceivers but fail on agents that have internalized misaligned goals as values. Important caveat.

#### Takeaway

Linear probes are the simplest and surprisingly effective interpretability tool for deception. They cover the engineered case well; coverage of natural strategic dishonesty is partial.

### 6.2 Sparse Autoencoders

Bricken et al. (Anthropic 2023), "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning" ([transformer-circuits.pub](https://transformer-circuits.pub/2023/monosemantic-features/)).

Templeton et al. (Anthropic 2024), "Scaling Monosemanticity" ([transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/)).

#### Proposal

Neural network activations are polysemantic: a single neuron responds to many unrelated concepts. SAEs decompose activations into a larger basis of (mostly) monosemantic features. The basis is found by training a sparse autoencoder on the residual stream: a wide hidden layer with $L_1$ sparsity penalty.

#### Results

- Bricken 2023: one-layer transformer, ~4000 features. Demonstrated polysemantic-to-monosemantic decomposition. Features include specific token contexts (Arabic, DNA), abstract concepts, edge cases.
- Templeton 2024: 34M features from Claude 3 Sonnet middle layer. Multilingual, multimodal, abstract-to-concrete. Features include specific people, specific code patterns, "deception," "sycophancy," "power-seeking," "Golden Gate Bridge" (famous example).
- DeepMind Gemma Scope / Gemma Scope 2 (2024-2025): 64M+ latents across 10 Gemma models, open source.
- OpenAI SAEs on GPT-4 (2024).
- SAE scaling laws: loss improves as a power law with number of latents (Lieberum et al. 2024).

#### Steering

SAE features can be activated (steered) to manipulate model behavior. Famous example: steering the Golden Gate Bridge feature in Claude 3 Sonnet causes the model to relate everything to the bridge. Practical question: can steering deception/sycophancy features prevent those behaviors?

#### Known limits

- **Features may be SAE artifacts.** The decomposition is not unique; different SAE training runs find different bases.
- **Auto-labeled features may not capture mechanism.** "Secret Agenda" experiments (2025): SAE features auto-labeled as "deception" rarely activate during actual strategic dishonesty. The label may not capture the underlying computation.
- **SAE features for sycophancy/deception steering often fail.** Over 100 feature steering experiments on Llama and Gemma SAEs did not successfully prevent strategic lying.
- **Cross-model and cross-architecture generalization is open.** Sparse crosscoders (Lindsey et al. 2024) map activations across models into a shared feature space; whether this transfers safety features is open.
- **Scale matters.** Features at small scale do not always have analogs at frontier scale.

### 6.3 Circuit tracing

Anthropic (March 2025), "Circuit Tracing: Revealing Computational Graphs in Language Models" ([transformer-circuits.pub/methods](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)).

Anthropic (March 2025), "On the Biology of a Large Language Model" ([transformer-circuits.pub/biology](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)).

#### Proposal

Move beyond static feature dictionaries to mapping *circuits*: the pathways of feature activation that produce specific computations. The method replaces MLPs with cross-layer transcoders (CLTs), a new SAE variant that reads from one layer's residual stream and writes outputs visible to all subsequent MLP layers. This allows tracing computational paths through the model.

#### Findings

Applied to Claude 3.5 Haiku:
- **Multi-hop reasoning.** For "the capital of the state where Dallas is located," the model forms an intermediate "Texas" representation before producing "Austin."
- **Poetry planning.** When generating rhyming poetry, the model selects the target rhyme word before composing the line that ends in it.
- **Internal medical diagnoses.** In a clinical reasoning task, the model forms latent diagnoses that guide subsequent follow-up questions.
- Specific safety-relevant circuits identified (less detail public).

#### Status

Circuit Tracer library open-sourced May 2025. Supports Gemma-2-2B, Llama-3.1-1B, Qwen3-4B. Mechanistic interpretability named one of MIT Technology Review's "10 Breakthrough Technologies 2026."

#### Known limits

- Most circuit findings are on small / mid-sized models, not frontier scale.
- Tracing is expensive; cannot be run cheaply on every input.
- Specific circuit-level claims about safety properties (e.g., "this circuit detects deception") are rare and hard to validate.

### 6.4 The Anthropic interpretability program and 2027 goals

Amodei (April 2025), "The Urgency of Interpretability" ([darioamodei.com](https://www.darioamodei.com/post/the-urgency-of-interpretability)).

Stated goal: by 2027, interpretability can reliably detect most AI model problems. Substantial public commitment; Anthropic is the only frontier lab with a publicly stated interpretability roadmap.

Concrete steps taken by 2025-2026:
- **Pre-deployment interpretability assessments.** Anthropic used mechanistic interpretability in pre-deployment safety assessment of Claude Sonnet 4.5 (September 2025) and Opus 4.5 (November 2025). First integration of interpretability into deployment decisions for production systems.
- **Three sketches of ASL-4 safety case** ([LessWrong](https://www.lesswrong.com/posts/RveeCTcoApkAtd7oA/anthropic-three-sketches-of-asl-4-safety-case-components)). Three potential components: Mechanistic Interpretability, AI Control, and Incentives Analysis. Interpretability is one branch.
- **Alignment auditing agents.** "Building and evaluating alignment auditing agents" (2025) ([alignment.anthropic.com](https://alignment.anthropic.com/2025/automated-auditing/)). Investigator agent (Claude Sonnet 4 with scaffolding) performs intensive audits of target models using chat, training data analysis, and interpretability tools including 1M-feature SAEs.
- Claude Sonnet 4 misalignment rate "substantially lower than any recent frontier model" per Anthropic's audits. Claude Opus 4.5 reported as lower than any other recent frontier model.

#### Honest assessment of the 2027 goal

The 2027 goal is the most concrete safety roadmap from a frontier lab. It is ambitious; the field is not on track to meet it cleanly. Specific 2026 limits:

- Interpretability has identified specific features at scale (Templeton 2024 found 34M in Claude 3 Sonnet) but the total set of relevant features is estimated to be much larger.
- Feature labels do not always capture mechanism (Secret Agenda 2025 results).
- Cross-model generalization is open.
- No production deployment uses interpretability as a *hard* gate; Anthropic uses it as input among many.

#### Takeaway

Interpretability is moving fast and remains the most promising path to giving us evidence about model internals. It is not yet sufficient as a deployment gate. The Anthropic 2027 target should be presented as the bet most likely to determine whether the field has tools that scale; the bet is undecided.

### 6.5 What interpretability cannot yet do

The honest list as of mid-2026:

- Reliably catch deceptive alignment in cases not analogous to engineered sleeper agents.
- Distinguish features that name a concept from circuits that perform a computation involving that concept.
- Generalize across architectures (transformer vs. SSM vs. MoE) and scales.
- Provide a deployment-gate-quality safety case in the strict sense: "we have proven this model does not have property X."
- Detect mesa-optimization in the strong mechanistic sense (whether models perform internal search at all is still debated).

### Citations for §6

- Bricken et al. (Anthropic 2023). "Towards Monosemanticity." [transformer-circuits.pub](https://transformer-circuits.pub/2023/monosemantic-features/).
- Hubinger et al. (Anthropic 2024). "Sleeper Agents." [arXiv:2401.05566](https://arxiv.org/pdf/2401.05566).
- Anthropic (April 2024). "Simple Probes Can Catch Sleeper Agents." [Anthropic blog](https://www.anthropic.com/research/probes-catch-sleeper-agents).
- Templeton et al. (Anthropic 2024). "Scaling Monosemanticity." [transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/).
- Lieberum et al. (DeepMind 2024). "Gemma Scope: Open Sparse Autoencoders Everywhere All At Once." [arXiv:2408.05147](https://arxiv.org/abs/2408.05147).
- Anthropic (2025). "Circuit Tracing." [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html).
- Anthropic (2025). "On the Biology of a Large Language Model." [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/biology.html).
- Amodei (April 2025). "The Urgency of Interpretability." [darioamodei.com](https://www.darioamodei.com/post/the-urgency-of-interpretability).
- Anthropic (2025). "Three Sketches of ASL-4 Safety Case Components." [LessWrong](https://www.lesswrong.com/posts/RveeCTcoApkAtd7oA/anthropic-three-sketches-of-asl-4-safety-case-components).
- Anthropic (2025). "Building and Evaluating Alignment Auditing Agents." [alignment.anthropic.com](https://alignment.anthropic.com/2025/automated-auditing/).
- "Detecting Strategic Deception Using Linear Probes" (2025). [arXiv:2502.03407](https://arxiv.org/pdf/2502.03407).

---

## 7. Capability control

### The proposal

Bostrom (2014), *Superintelligence: Paths, Dangers, Strategies*, Chapter 9 ("The Control Problem"), Chapter 10 ("Oracles, Genies, Sovereigns, Tools").

Armstrong, Sandberg, Bostrom (2012), "Thinking Inside the Box: Controlling and Using an Oracle AI" ([PDF](https://nickbostrom.com/papers/oracle.pdf)).

The argument: even if alignment is hard, we can supplement with *capability control*, limiting what the AI can do. Bostrom's taxonomy of control:

- **Boxing.** Physically or digitally isolate the AI from the world. Air-gapped, sandboxed, no internet, no robots.
- **Incentive methods.** Build the AI such that it has reasons not to want to escape (e.g., reward depends on operator approval).
- **Stunting.** Limit the AI's capability deliberately (smaller model, less compute, narrower training).
- **Tripwires.** Automatic shutdown if certain conditions trigger.

Bostrom's taxonomy of AI types by capability:
- **Oracle.** Answers questions; does not act.
- **Genie.** Performs specific commands.
- **Sovereign.** Pursues open-ended goals.
- **Tool AI.** Performs specific functions without agency.

Oracles and tools are easier to control. Sovereigns are harder.

### Why this is hard to enforce as systems scale

- **Information leakage.** Any output channel is an action channel. An oracle that answers questions can persuade. A code-completing tool can write code that breaks containment.
- **Capability/usefulness trade-off.** A boxed AI is less useful. There is economic pressure to give the AI access to tools, the internet, persistent memory, etc. Frontier models in 2025-2026 are routinely connected to web search, file systems, code execution, and agentic tool use.
- **Treacherous turn worry (Bostrom).** A sufficiently capable AI in a box may strategically behave well during testing and defect when given more capability. This is the deceptive-alignment scenario.
- **Empirical regression.** Agentic capability is the explicit direction of frontier development in 2025-2026; the trend is *toward* removing capability controls, not adding them.

### Current state

Capability control as a *standalone* solution is not seriously proposed by anyone in the field. It is uniformly treated as a supplement.

What remains alive from the capability-control program:
- **Responsible scaling policies / Frontier Safety Frameworks.** Define capability thresholds (ASLs, CCLs, HCTs) above which additional safeguards are required. Effectively staged capability control: don't deploy beyond X without Y.
- **Red-teaming, dangerous-capability evaluations.** Test for specific dangerous capabilities (CBRN uplift, cyber, persuasion, self-proliferation) before deployment.
- **AI Control (Greenblatt et al. 2023, see §9).** Treats the untrusted-model setting explicitly: assume misalignment, design protocols to detect defection. This is a modern, formal version of "capability control" reframed as monitoring rather than confinement.

### Known limits

- Frontier capabilities exceed many of the original boxing assumptions (long-horizon agentic behavior, web access, code execution, persistent memory).
- "Capability threshold" measurement is itself unsolved; thresholds are operationalized by evaluation suites that the model may distinguish from real deployment (situational awareness).
- The empirical pattern: capability controls are softened over time (Anthropic RSP v3 in 2025-2026 reportedly relaxed some hard commitments to conditional ones).

### Takeaway

Capability control was the dominant framework in 2014-2018 thinking; it survives as a useful supplement (RSPs, dangerous-capability evals, AI Control protocols) but not as a primary solution.

### Citations

- Bostrom (2014). *Superintelligence.* Oxford University Press.
- Armstrong, Sandberg, Bostrom (2012). "Thinking Inside the Box." [PDF](https://nickbostrom.com/papers/oracle.pdf).
- Greenblatt, Shlegeris, Sachan, Roger (2023). "AI Control: Improving Safety Despite Intentional Subversion." [arXiv:2312.06942](https://arxiv.org/abs/2312.06942).

---

## 8. Societal and governance proposals (briefly)

### 8.1 Open Agency Architecture / Safeguarded AI

Dalrymple ("davidad") et al. (2023), "An Open Agency Architecture for Safe Transformative AI" ([Alignment Forum](https://www.alignmentforum.org/posts/pKSmEkSQJsCSTK6nH/an-open-agency-architecture-for-safe-transformative-ai)).

Dalrymple (2024), "Safeguarded AI: Constructing Guaranteed Safety, Programme Thesis v1.2" ([ARIA PDF](https://www.aria.org.uk/media/3nhijno4/aria-safeguarded-ai-programme-thesis-v1.pdf)).

#### Proposal

The OAA / Safeguarded AI agenda proposes formal-verification-based safety: build a "gatekeeper" AI whose job is to verify proof certificates from frontier AIs before allowing actions. Components:

1. **World model.** A formally verified model of the relevant domain.
2. **Specification language.** A formal language for safety properties.
3. **Proof checker.** A deterministic, human-auditable algorithm.
4. **Frontier model.** Generates actions plus proof certificates that the actions satisfy the specification.

The frontier model is trusted only to generate proofs; the proofs are verified by the deterministic checker, which is the actual locus of safety.

#### Current state

- ARIA (UK Advanced Research and Invention Agency) £30-50M programme, launched February 2024.
- David Dalrymple transitioned from Programme Director to Technical Advisor; Nora Ammann is now Programme Director.
- Grants awarded for formal verification process work.
- Active research; no deployed system yet.

#### Known limits

- The world model assumption is severe: many real domains lack formal models.
- Generating proofs that frontier models can produce and human-auditable checkers can verify is unsolved at scale.
- The approach addresses specific safety properties (those expressible in the spec language) and does not address general alignment.

### 8.2 Yampolskiy-style impossibility arguments

Brcic and Yampolskiy (2023), "Impossibility Results in AI: A Survey" ([ACM Computing Surveys](https://dl.acm.org/doi/10.1145/3603371); [arXiv:2109.00484](https://arxiv.org/abs/2109.00484)).

Yampolskiy (2024), *AI: Unexplainable, Unpredictable, Uncontrollable.* CRC Press.

#### Argument

A series of formal impossibility results derived from undecidability and complexity theory:

- **Uncontrollability.** Yampolskiy 2020, "On Controllability of AI" ([arXiv:2008.04071](https://arxiv.org/pdf/2008.04071)). Adapts Gödel-style self-reference: "Disobey!" If the AI obeys, it disobeys; if it disobeys, it disobeys. Stronger versions derive uncontrollability from the Halting Problem and Rice's Theorem.
- **Unverifiability.** Cannot prove safety / alignment of a sufficiently complex system in general, by Rice's Theorem (any nontrivial semantic property of programs is undecidable).
- **Unexplainability, Unpredictability.** Similar arguments.

The Brcic-Yampolskiy 2023 survey categorizes impossibility results in AI into five mechanism-based classes: deduction, indistinguishability, induction, tradeoffs, intractability.

#### Counterpoint

The impossibility arguments operate at the level of *any* program with the relevant capability. They do not prove that *specific* alignment properties cannot be verified for *specific* trained systems. The arguments are like "you cannot generally decide whether an arbitrary program halts"; this is true and does not prevent specific programs from being analyzed.

The 2025 *Scientific Reports* paper "Machines that Halt Resolve the Undecidability of Artificial Intelligence Alignment" makes a related counterargument: under specific assumptions about machines that halt, certain alignment problems are decidable.

#### Takeaway

Yampolskiy's results are formally correct in their domain; their implication for practical alignment is contested. They serve as guardrails: do not expect a general decidable algorithm for "is this AI aligned?" They do not show that no specific alignment technique can work.

### 8.3 RSPs and FSFs

Covered in `safety_survey_2026.md`. Bottom line for here:
- Anthropic RSP v3.0 (2025), DeepMind Critical Capability Levels, OpenAI High Capability Thresholds.
- 12 companies publish FSFs in 2026 (doubled from 2024).
- Voluntary; voluntary commitments have been softened in 2026.

### 8.4 Singapore Consensus and the International AI Safety Report 2026

Bengio et al. (2025), "The Singapore Consensus on Global AI Safety Research Priorities" ([arXiv:2506.20702](https://arxiv.org/pdf/2506.20702)).

International AI Safety Report 2026 ([report homepage](https://internationalaisafetyreport.org/)).

The two most authoritative consensus documents. Singapore Consensus organizes safety research into three areas: *Development* (creating trustworthy systems), *Assessment* (evaluating risks), *Control* (monitoring and intervening). IAISR 2026 is the authoritative single source on the empirical state; Bengio's framing is "the ball is in policymakers' hands."

### 8.5 *If Anyone Builds It, Everyone Dies* (Yudkowsky and Soares 2025)

Yudkowsky and Soares (2025), *If Anyone Builds It, Everyone Dies: Why Superhuman AI Would Kill Us All.* Little, Brown.

The 2025 popularization of the MIRI-doom argument: if any group builds artificial superintelligence using anything resembling current methods, everyone dies. NYT bestseller; mixed reception (positive in *The Guardian*, critical in *The Atlantic*). The book is part of the 2025-2026 cultural landscape; it does not advance the technical alignment program. The Multitudes book takes a position different from the Yudkowsky-Soares one (the gap is real and structural without committing to a specific P(doom)); the existence of the popular argument is part of the 2026 conversation.

### Citations for §8

- Dalrymple et al. (2023). "An Open Agency Architecture for Safe Transformative AI." [Alignment Forum](https://www.alignmentforum.org/posts/pKSmEkSQJsCSTK6nH/an-open-agency-architecture-for-safe-transformative-ai).
- Dalrymple (2024). "Safeguarded AI Programme Thesis v1.2." [ARIA PDF](https://www.aria.org.uk/media/3nhijno4/aria-safeguarded-ai-programme-thesis-v1.pdf).
- Yampolskiy (2020). "On Controllability of AI." [arXiv:2008.04071](https://arxiv.org/pdf/2008.04071).
- Brcic and Yampolskiy (2023). "Impossibility Results in AI: A Survey." [ACM Computing Surveys](https://dl.acm.org/doi/10.1145/3603371).
- Yampolskiy (2024). *AI: Unexplainable, Unpredictable, Uncontrollable.* CRC Press.
- Bengio et al. (2025). "The Singapore Consensus." [arXiv:2506.20702](https://arxiv.org/pdf/2506.20702).
- International AI Safety Report 2026. [internationalaisafetyreport.org](https://internationalaisafetyreport.org/).
- Yudkowsky and Soares (2025). *If Anyone Builds It, Everyone Dies.* Little, Brown.

---

## 9. AI Control: the pragmatic complement

Greenblatt, Shlegeris, Sachan, Roger (2023), "AI Control: Improving Safety Despite Intentional Subversion" ([arXiv:2312.06942](https://arxiv.org/abs/2312.06942)), ICML 2024.

Worth its own short section because it has become a substantive line of work not captured elsewhere.

### Proposal

Assume the untrusted model may be misaligned and may scheme. Design *protocols* that catch misbehavior using:

- A weaker *trusted* model.
- Limited human oversight.
- Non-AI software (sandboxes, tests, automated audits).

The 2023 paper studies trusted-monitoring protocols in a programming-problems setting with an untrusted GPT-4 and a trusted GPT-3.5. Results: trusted-model-edits and untrusted-as-monitor protocols substantially improve safety vs. baselines.

### Recent extensions

- Factor(U,T): Controlling Untrusted AI by Monitoring their Plans (2025) ([arXiv:2512.14745](https://arxiv.org/pdf/2512.14745)). Factor untrusted-model behavior into plan and execution, monitor the plan.
- LinuxArena (2026) ([arXiv:2604.15384](https://arxiv.org/html/2604.15384)). Largest software-engineering control testbed: 20 multi-service production environments, 1,667 main tasks, 185 side tasks, human-crafted attack dataset.
- UK AISI Alignment Project (2025-). £27M funding 60 projects, substantial portion in AI Control.

### Distinguishing feature

AI Control does not assume the model can be aligned. It assumes the opposite (or at least neutral): the model may be misaligned. The protocols make misbehavior detectable / costly. This is humble in a useful way.

### Known limits

- Trusted models must be capable enough to evaluate untrusted-model outputs; this is the scalable-oversight problem in another guise.
- Protocols are designed against specific threat models; novel attacks may evade them.
- Untrusted-model collusion with monitors is a worry (paraphrasers, forced decompositions are partial mitigations).

### Takeaway

AI Control is the pragmatic complement to alignment. It does not solve alignment; it makes deployment safer under uncertainty about alignment. The book might mention it in Ch 14 as the field's most honest "what to do if we don't know" line.

### Citations

- Greenblatt, Shlegeris, Sachan, Roger (2023). "AI Control." [arXiv:2312.06942](https://arxiv.org/abs/2312.06942).
- UK AISI Alignment Project (2025). [alignmentproject.aisi.gov.uk](https://alignmentproject.aisi.gov.uk/).
- Factor(U,T) (2025). [arXiv:2512.14745](https://arxiv.org/pdf/2512.14745).

---

## 10. Honest assessment of the state of the field (2026)

### What is working

- **RLHF and RLAIF / Constitutional AI** work well enough for current commercial uses (chat assistants, code assistants). The behaviors that show up in production are mostly the ones the labs want. The "mostly" is doing serious work in that sentence.
- **Linear probes for engineered deception** work in the cases studied (sleeper agents). They generalize across some natural cases. They are the easiest, cheapest interpretability tool with measurable safety value.
- **SAE features at scale** exist for many human-interpretable concepts. Feature steering changes behavior in predictable ways for many concepts. The Anthropic Claude Sonnet 4.5 / Opus 4.5/4.6 deployment process uses SAE-based investigation as input.
- **Doubly-efficient debate** has formal results under stated assumptions; prover-estimator debate handles obfuscation under stated assumptions. These are theorems with hypotheses, not deployed systems, but the formal apparatus has solidified.
- **AI Control** protocols (trusted monitoring, factored monitoring, sandboxing with audit) are deployable today and have testbeds.

### What is not working

- **No proposal has a worst-case guarantee** for aligning a system more capable than its overseers.
- **Behavioral safety training does not generalize to agentic settings** (MacDiarmid 2025): standard chat-prompt safety training leaves agentic misalignment at 34-70%.
- **Frontier models are situationally aware** and can distinguish evaluation from deployment (Apollo Research 2025; Strategic Dishonesty 2025).
- **Empirical evidence of scheming / alignment faking** has emerged in 2024-2025 in frontier models (Greenblatt 2024, Meinke 2024, MacDiarmid 2025).
- **SAE features labeled as "deception" do not reliably activate during actual strategic dishonesty.** The labels are sometimes wrong about what the features compute.
- **Capability is rising faster than alignment.** METR time horizons doubling every ~4 months in 2024-2025; alignment research scale is growing more slowly.

### What is contested

- **Will interpretability scale to frontier models by 2027?** Anthropic publicly bets yes (Amodei stated goal); many alignment researchers are skeptical.
- **Do current LLMs contain mesa-optimizers in the strong mechanistic sense?** Empirical behaviors are consistent with mesa-optimization; mechanistic evidence is partial.
- **Are the impossibility arguments (Yampolskiy) practically binding?** Formally correct; practical implications contested.
- **P(doom) and timelines.** Wide divergence; the field has not converged.
- **Should capability development pause?** *If Anyone Builds It, Everyone Dies* (Yudkowsky and Soares 2025) argues yes; most lab researchers argue no; substantial disagreement.
- **Credibility of voluntary RSPs/FSFs** (especially after Anthropic softened some commitments in 2026).

### What the field consensus is in 2026

The Singapore Consensus, IAISR 2026, and the explicit positions of all three major frontier labs converge on this:

1. The gap between optimization and intent is structural.
2. Specification problems (outer alignment, reward hacking) and inner alignment problems (mesa-optimization, scheming) are both real, with empirical signals.
3. Scalable oversight techniques (debate, RLAIF, weak-to-strong, AI Control) are partial mitigations that work in some regimes and fail in others.
4. Interpretability is necessary and not yet sufficient.
5. Voluntary safety commitments are needed but not sufficient; some form of policy intervention is widely (not unanimously) viewed as needed.
6. The biggest disagreement is about timelines: how fast is capability rising, and how much time do we have to make techniques scale?

### What the book should not say

- Do not say "alignment is solved." It is not.
- Do not say "alignment is impossible." Specific results can be impossible (Yampolskiy); the practical claim is uncertain.
- Do not endorse a specific P(doom). The field is divided; the book takes a position about the *structural problem* not about the *prediction*.
- Do not present the proposals as competitors. They address different parts of the gap; the realistic future is a mix.

### What the book should say

- The specification problem is the central problem.
- Many techniques are being tried.
- Each has known limits.
- Interpretability is the most promising bet on giving us evidence about internals; it is on a possible path to deployment-gate-quality safety cases by ~2027-2028; it is not there yet.
- Empirical signals in 2024-2026 are consistent with the structural worries from 2015-2019 theory.
- The gap is the destination of the book's argument; the proposals are the responses; the gap remains.
