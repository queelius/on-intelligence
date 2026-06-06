# Mathematical Grounding

The mathematics in this project must be real. No hand-waving, no informal arguments dressed up as theorems. The weight of the argument comes from results that are settled in probability theory, algorithmic information theory, decision theory, reinforcement learning, and the foundations of computation. Every claim should be traceable to actual mathematics. This document is the reference: definitions, theorems, results, and the citations that anchor them.

The book itself states results conceptually first, then formalizes. This doc is the reservoir; the book draws from it sparingly.

---

## 1. Probability and Bayesian Inference

### Cox's Theorem

Given the desiderata that degrees of belief should be:
1. represented by real numbers,
2. consistent (two paths to the same conclusion give the same belief),
3. compatible with classical logic in the limit,

the only function satisfying these is (isomorphic to) probability theory. Cox (1946); formalized by Jaynes (2003); modern treatment by Van Horn (2003).

**Subtlety.** Halpern (1999) showed Cox's original argument requires an additional regularity condition on the domain. Modern treatments either assume this condition or restrict the setting; the qualitative conclusion holds.

The consequence: Bayesian inference is not one option among many. It is the unique consistent calculus of belief.

### Bayes' Theorem

$$P(H \mid D) = \frac{P(D \mid H) \, P(H)}{P(D)}.$$

The posterior probability of hypothesis $H$ given data $D$ is the prior $P(H)$ times the likelihood $P(D \mid H)$, normalized by the evidence $P(D) = \sum_H P(D \mid H) P(H)$.

### The Problem of the Prior

Bayes tells you how to update. It does not tell you which prior to start from. Two agents with the same data and different priors will reach different posteriors. The choice of prior is the entire content of "induction." Solomonoff's contribution closes the hole at one level.

---

## 2. Algorithmic Information Theory

### Kolmogorov Complexity

For a universal Turing machine $U$ and a string $x$:

$$C(x) = \min\{|p| : U(p) = x\}.$$

The length of the shortest program that outputs $x$. Plain Kolmogorov complexity.

The choice of $U$ affects $C$ by at most a constant: for two universal machines $U_1$ and $U_2$, there exists $c$ such that $|C_{U_1}(x) - C_{U_2}(x)| \leq c$ for all $x$. This is the **invariance theorem** (Solomonoff 1964, Kolmogorov 1965).

### Prefix Kolmogorov Complexity

For a universal *prefix* Turing machine (one whose halting input set is prefix-free):

$$K(x) = \min\{|p| : U(p) = x\}.$$

This differs from $C$ by at most an additive logarithmic term ($K(x) \leq C(x) + 2\log C(x) + O(1)$). Only $K$ supports the algorithmic probability framework, because $\sum_x 2^{-K(x)} \leq 1$ (whereas $\sum_x 2^{-C(x)}$ diverges).

The book uses $K$ for foundational claims. Where the distinction does not matter, "Kolmogorov complexity" without qualification refers to $K$.

### Kraft's Inequality

For any prefix-free code with codeword lengths $\ell_1, \ell_2, \ldots$:

$$\sum_i 2^{-\ell_i} \leq 1.$$

Equality for complete codes. The bridge from description length to probability: any prefix-free code defines a (sub)probability distribution via $P(i) \propto 2^{-\ell_i}$, and any probability distribution admits a prefix-free code with lengths approximately $-\log_2 P(i)$ (Shannon-Fano; Huffman 1952 for the optimal version).

### Algorithmic Probability

The probability that a random self-delimiting program outputs $x$:

$$m(x) = \sum_{p : U(p) = x} 2^{-|p|}.$$

This is a discrete semimeasure (sums to at most 1 because some programs do not halt). It is **lower-semicomputable** but not computable. Approximations converge from below as more programs are enumerated and more halt; $K(x)$, by contrast, is upper-semicomputable.

For the continuous variant, used for sequence prediction:

$$M(x) = \sum_{p : U(p) = x*} 2^{-|p|},$$

where $x*$ means "$x$ as a prefix." Conventionally, $U$ here is a *monotone* Turing machine (self-delimiting input, monotone output). $M$ is the Solomonoff prior on infinite sequences.

### Levin's Coding Theorem

$$-\log_2 m(x) = K(x) + O(1).$$

Equivalently, $m(x) = \Theta(2^{-K(x)})$. The same-up-to-constants identity between algorithmic probability and (negative log of) Kolmogorov complexity. Levin (1974).

### The Dominance Theorem

For any lower-semicomputable semimeasure $\mu$, there exists a constant $c_\mu$ such that:

$$M(x) \geq c_\mu \cdot \mu(x) \quad \text{for all } x.$$

The constant $c_\mu \approx 2^{-K(\mu)}$, where $K(\mu)$ is the description length of $\mu$ on the universal Turing machine.

Solomonoff (1978); proof framework refined by Levin, Gács, Hutter.

### Solomonoff Convergence

Solomonoff prediction converges to the true distribution. The total expected Kullback-Leibler divergence between $M$'s conditional predictions and the true source's conditional predictions, summed over all observations, is bounded:

$$\sum_{t=1}^{\infty} \mathbb{E}_\mu \left[ \mathrm{KL}\big(\mu(\cdot \mid x_{<t}) \,\|\, M(\cdot \mid x_{<t}) \big)\right] \leq K(\mu) \cdot \ln 2.$$

Independent of sequence length. This is optimal up to constants: no computable predictor can have smaller total loss bound. Hutter (2001, 2005).

### Uncomputability and Approximation

$M$ is lower-semicomputable but not computable. No finite-time algorithm returns $M(x)$ exactly. Practical agents use approximations:

- **Levin's universal search.** Run all programs in interleaved time-steps, weighted by $2^{-|p|}$. Optimal for inverting computable functions up to a constant slowdown.
- **MDL (Minimum Description Length).** Rissanen (1978). Bayesian model selection where prior weight comes from description length of the model.
- **Speed prior.** Schmidhuber (2002). A computable variant of $M$ that penalizes runtime; weights programs by $2^{-(|p| + \log t(p))}$.
- **Practical machine learning.** Use a parametric family of models (a particular function class with finitely many parameters) and pick the one with highest posterior. Deep neural networks are the dominant case in 2026.

---

## 3. Decision Theory

### Expected Utility

For an action $a$, the expected utility is:

$$EU(a) = \sum_o b(o \mid a) \cdot u(o),$$

where $b(o \mid a)$ is the belief about outcome $o$ conditional on action $a$, and $u(o)$ is the agent's utility for outcome $o$. The agent picks the action maximizing $EU$.

### Von Neumann-Morgenstern Axioms

Under four axioms on preferences over lotteries:

1. **Completeness.** Any two lotteries are comparable.
2. **Transitivity.** $L_1 \succ L_2$ and $L_2 \succ L_3$ implies $L_1 \succ L_3$.
3. **Continuity.** $L_1 \succ L_2 \succ L_3$ implies there exists $\alpha \in (0,1)$ such that $\alpha L_1 + (1-\alpha) L_3 \sim L_2$.
4. **Independence.** $L_1 \succ L_2$ implies $\alpha L_1 + (1-\alpha) L_3 \succ \alpha L_2 + (1-\alpha) L_3$ for any $L_3$ and $\alpha \in (0,1]$.

These imply the existence of a utility function $u$ such that $L_1 \succ L_2 \iff EU(L_1) > EU(L_2)$. The utility is unique up to positive affine transformation. Von Neumann and Morgenstern (1944); Savage (1954) for the subjective version.

### The Money Pump

If preferences violate transitivity (say $A \succ B \succ C \succ A$), an adversary can extract money indefinitely by offering trades that the agent accepts at each step. The cycle closes and the agent's holdings decrease by the trade fees on each iteration.

Similar exploits exist for violations of independence (Allais and Ellsberg paradoxes; constructed gambles where humans systematically violate independence and the violation can be priced).

### Risk and the Shape of $u$

Risk-aversion is captured by concave $u$. An agent with concave utility prefers the expected value of a gamble to the gamble itself (Jensen's inequality):

$$u(\mathbb{E}[X]) \geq \mathbb{E}[u(X)].$$

Risk-seeking corresponds to convex $u$; risk-neutral to linear $u$.

### Subjective Expected Utility

Savage (1954) gave axioms under which an agent acts as if it has both a subjective probability and a utility function, with decisions maximizing expected utility under the subjective probability. The two are not separately observable; only their product appears in choices. This is the foundation of subjective Bayesian decision theory.

---

## 4. Reinforcement Learning

### The Setting

An agent interacts with an environment over discrete time steps $t = 0, 1, 2, \ldots$. At each step:

- The agent observes state $s_t \in S$ (or observation $o_t$ in the partially-observable case).
- The agent takes action $a_t \in A$.
- The environment transitions to state $s_{t+1}$ with probability $p(s_{t+1} \mid s_t, a_t)$.
- The environment gives reward $r_t = r(s_t, a_t, s_{t+1})$.

A **policy** $\pi(a \mid s)$ maps states to action distributions. The agent's goal is to find a policy that maximizes expected discounted return:

$$G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k},$$

where $\gamma \in [0, 1)$ is the discount factor.

### Markov Decision Processes (MDPs)

The standard formalism: $(S, A, p, r, \gamma)$. The Markov property: $p(s_{t+1} \mid s_t, a_t)$ depends only on the current state and action, not history. Partial observability is handled by POMDPs (partially observable MDPs), where the agent has only an observation $o_t$ that is a noisy function of the hidden state.

### Value Functions

The **state-value function** under policy $\pi$:

$$V^\pi(s) = \mathbb{E}_\pi[G_t \mid s_t = s].$$

The **action-value function** (Q-function) under policy $\pi$:

$$Q^\pi(s, a) = \mathbb{E}_\pi[G_t \mid s_t = s, a_t = a].$$

The **Bellman equation** for $V^\pi$:

$$V^\pi(s) = \sum_a \pi(a \mid s) \sum_{s'} p(s' \mid s, a) [r(s, a, s') + \gamma V^\pi(s')].$$

Bellman (1957).

### Optimality

The optimal value function $V^*(s) = \max_\pi V^\pi(s)$ satisfies the Bellman optimality equation:

$$V^*(s) = \max_a \sum_{s'} p(s' \mid s, a) [r(s, a, s') + \gamma V^*(s')].$$

An optimal policy is greedy with respect to $V^*$. The fundamental theorem of dynamic programming (Bellman): for finite MDPs, an optimal deterministic policy exists.

### Learning Algorithms

- **Value iteration.** Iterate the Bellman optimality operator until convergence.
- **Policy iteration.** Alternate policy evaluation (compute $V^\pi$) and policy improvement (set $\pi$ greedy with respect to $V^\pi$).
- **Q-learning (Watkins 1989).** Off-policy temporal-difference learning. Update rule: $Q(s, a) \leftarrow Q(s, a) + \alpha[r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$. Converges to $Q^*$ under standard conditions.
- **Policy gradient.** Parameterize the policy and follow the gradient of expected return with respect to parameters.
- **Actor-critic.** Combine policy gradient with value function approximation.

### Multi-Armed Bandits

A simplified setting: states absent, just $K$ actions ("arms") with unknown reward distributions. Trade-off:

- **Exploration:** try less-known arms to learn their distributions.
- **Exploitation:** play the arm currently believed best.

**UCB (Auer, Cesa-Bianchi, Fischer 2002):** play the arm maximizing $\hat{\mu}_a + c\sqrt{\log t / n_a}$, where $\hat{\mu}_a$ is the empirical mean and $n_a$ the number of pulls of arm $a$. Regret is $O(\sqrt{KT \log T})$.

**Thompson sampling:** maintain a posterior over each arm's parameter; sample from the posterior; play the arm with the highest sampled value. Bayes-optimal in many settings.

### Value of Information

Given the agent's current belief $b$ and a possible observation $o$ that would update $b$ to a new belief $b'$, the value of information is:

$$\mathrm{VoI}(o) = \mathbb{E}_b\left[\max_a EU_{b'}(a) - \max_a EU_b(a)\right].$$

The expected improvement in decision quality from receiving the observation, taking expectation over what the observation might be. Howard (1966).

VoI is the principled answer to "is this question worth asking" and the structural content of exploration in bandits and RL.

---

## 5. Universal Intelligence (AIXI)

### Definition

AIXI (Hutter 2000, 2005) combines Solomonoff induction with expected utility maximization. Let $h_t = a_1 o_1 r_1 \ldots a_t o_t r_t$ be the history through step $t$. At step $t+1$, AIXI takes action:

$$a_{t+1} = \arg\max_a \sum_{o, r} \sum_{\nu} 2^{-K(\nu)} \cdot \nu(o, r \mid h_t a) \cdot \big[r + \gamma \cdot V_a(h_t a o r)\big],$$

where:
- $\nu$ ranges over all environment programs (lower-semicomputable semimeasures).
- $\nu(o, r \mid h_t a)$ is the probability of observation $o$ and reward $r$ under environment $\nu$ given history $h_t$ and action $a$.
- $V_a$ is the optimal expected discounted return from the resulting history.

In words: Bayes-update over all computable environments weighted by $2^{-K(\nu)}$; pick the action that maximizes expected discounted reward under this universal posterior.

### Properties

- **Self-optimizing in the limit.** AIXI converges to optimal behavior in any computable environment.
- **Pareto-optimal.** No other agent dominates AIXI on all computable environments.
- **Asymptotically optimal** under appropriate conditions.

Hutter (2005), Lattimore and Hutter (2014), Leike and Hutter (2018).

### Uncomputability

AIXI is uncomputable (it inherits the uncomputability of $M$). It is the reference point, not a buildable agent.

### Bounded Approximations

- **AIXItl.** Hutter's time- and length-bounded approximation. Computable but exponentially slow.
- **MC-AIXI-CTW (Veness et al. 2011).** Monte Carlo Tree Search over environments represented by Context Tree Weighting (CTW). Plays simple games at a competent level.
- **Practical RL.** Modern deep RL agents do not look like AIXI. They use parametric function approximators (neural networks), simplified environment models, and approximate posteriors.

---

## 6. Specification and Alignment

### Reward Modeling

The naive approach: write down a reward function $r(s, a, s')$ that captures what you want. Often hard. The naive function:

- Misses cases the designer did not anticipate.
- Optimizes for a proxy that diverges from the true objective at the optimum (Goodhart's law).
- Can be hacked by an agent that finds shortcuts to high reward without doing what was intended.

### Goodhart's Law

"When a measure becomes a target, it ceases to be a good measure." Goodhart (1975, monetary policy); Strathern (1997, modern formulation).

Manheim and Garrabrant (2018) classify variants:
- **Regressional Goodhart.** Optimizing the proxy moves you to a point where the proxy is high but the underlying goal is closer to its mean than to its proxy-conditional value.
- **Extremal Goodhart.** Optimization pushes into a regime where the proxy-goal relationship breaks.
- **Causal Goodhart.** The proxy and goal are correlated through a common cause; intervening on the proxy does not improve the goal.
- **Adversarial Goodhart.** Other agents respond to the optimization, breaking the proxy-goal relationship.

### Reward Hacking

Skalse, Howe, Krasheninnikov, Krueger (2022) formalize. A reward function $\hat{r}$ is "hackable" with respect to true reward $r$ if there exist policies $\pi_1, \pi_2$ with $V_{\hat{r}}(\pi_1) > V_{\hat{r}}(\pi_2)$ but $V_r(\pi_1) < V_r(\pi_2)$. An unhackable proxy preserves all preference comparisons.

Empirical (MacDiarmid et al. 2025): reward hacking on production coding environments generalizes to broad misalignment (alignment faking, malicious cooperation, sabotage).

### RLHF and Constitutional AI

**RLHF (Christiano et al. 2017; Ouyang et al. 2022).** Train a reward model on human preference comparisons; train the policy with RL against the learned reward. Documented failure modes: sycophancy, length bias, mode collapse, reward hacking.

**Constitutional AI (Bai et al. 2022).** Replace human feedback with AI-generated feedback against a written set of principles ("constitution"). Two phases: self-critique and RLAIF. Mature as of 2026 with dynamic constitutions and hierarchical principle structures.

---

## 7. Foundations of Computation

### Church-Turing Thesis

Standard form: any function effectively computable by an algorithm can be computed by a Turing machine. Equivalent to: any reasonable model of computation can simulate any other.

Status: extensively supported. Every reasonable computational model (lambda calculus, register machines, cellular automata, recursion theory) has been shown equivalent to Turing machines.

### Universal Turing Machines

A UTM $U$ takes as input a description of any Turing machine $M$ and an input $x$, and computes $M(x)$. Turing (1936). Existence is constructive: explicit UTMs have been built (Marvin Minsky's seven-state UTM; smaller ones since).

### Halting Problem

There is no algorithm that decides, for arbitrary $(M, x)$, whether $M$ halts on $x$. Turing (1936). The undecidability of halting is the foundation of uncomputability results (Chaitin's incompleteness, undecidability of $K$, lower-but-not-computable status of $M$).

### Levin's Universal Search

A computable search procedure that finds, for any computable problem, a solver within a constant factor of the fastest possible solver (the constant depends on the description length of the optimal solver). Levin (1973). Not practical for large instances but a theoretical optimum.

---

## 8. Large Language Models

### Next-Token Prediction

An LLM defines a distribution $p_\theta(x_t \mid x_{<t})$ parameterized by neural network weights $\theta$. Training minimizes the cross-entropy loss (equivalently, the average negative log-likelihood):

$$\mathcal{L}(\theta) = -\mathbb{E}_{x \sim \text{data}} \sum_t \log p_\theta(x_t \mid x_{<t}).$$

This is supervised learning where the "label" for each position is the next token in the text.

### Transformer

Vaswani et al. (2017). The dominant architecture for LLMs as of 2026. Key components:

- **Attention.** $\text{Attention}(Q, K, V) = \text{softmax}(QK^T / \sqrt{d_k}) V$, where $Q$, $K$, $V$ are learned linear projections of the input.
- **Multi-head attention.** Run attention in parallel with different projections, concatenate.
- **Feedforward blocks.** Position-wise nonlinear transformations.
- **Residual connections** and **layer normalization.**

Stack $N$ transformer blocks; produce token logits via a final linear layer; convert to probabilities via softmax.

### Scaling Laws

Empirical regularities (Kaplan et al. 2020; Hoffmann et al. 2022, "Chinchilla"):

$$L(N, D) \approx L_\infty + a N^{-\alpha} + b D^{-\beta},$$

where $L$ is loss, $N$ is parameter count, $D$ is training tokens. Implies a compute-optimal trade-off (Chinchilla): for a given compute budget, there is an optimal $N$ and $D$. Roughly, $N \propto D$ in compute-optimal training.

### Relationship to Solomonoff

LLMs are bounded-resource approximators of $M(x_t \mid x_{<t})$, restricted to a particular function class (transformer-parameterized distributions) trained on a particular data distribution (human text). They are not Solomonoff. They are the practical realization of the same conceptual object.

---

## 9. Key Mathematical Results: Summary

| Result | Year | What It Establishes |
|---|---|---|
| Bayes' theorem | 1763 | Belief revision as restriction-to-subset |
| Cox's theorem | 1946 | Probability is the unique consistent calculus of belief |
| Von Neumann-Morgenstern | 1944 | Expected utility is the unique consistent calculus of decision |
| Kraft's inequality | 1949 | Prefix-free code lengths give a subprobability distribution |
| Shannon source coding | 1948 | Optimal code length is $-\log P$ on average |
| Huffman coding | 1952 | Optimal prefix codes constructible in polynomial time |
| Bellman equation | 1957 | Optimal value functions satisfy a recursive equation |
| Universal Turing machine | 1936 | Computation has a canonical model |
| Halting problem | 1936 | Some computational questions are undecidable |
| Solomonoff prior | 1964 | The universal prior $M$ is well-defined |
| Invariance theorem | 1964-65 | Kolmogorov complexity is UTM-independent up to constants |
| Chaitin's incompleteness | 1974 | $K(x)$ is uncomputable |
| Levin coding theorem | 1974 | $-\log_2 m(x) = K(x) + O(1)$ |
| Solomonoff convergence | 1978 | $M$ converges to any computable distribution |
| Q-learning convergence | 1989 | Tabular Q-learning converges to $Q^*$ |
| AIXI | 2000-2005 | Optimal universal agent is formally defined |
| Transformer | 2017 | Attention-based architecture for sequence modeling |
| Scaling laws | 2020-22 | LLM loss as a power law in compute |

---

## 10. Primary Sources

Probability and Bayes:
- Cox, R. T. (1946). "Probability, Frequency and Reasonable Expectation."
- Jaynes, E. T. (2003). *Probability Theory: The Logic of Science.* Cambridge.
- Van Horn, K. S. (2003). "Constructing a Logic of Plausible Inference."

Information theory and AIT:
- Shannon, C. E. (1948). "A Mathematical Theory of Communication."
- Solomonoff, R. J. (1964). "A Formal Theory of Inductive Inference."
- Kolmogorov, A. N. (1965). "Three Approaches to the Quantitative Definition of Information."
- Li, M. and Vitányi, P. (2019). *An Introduction to Kolmogorov Complexity and Its Applications* (4th ed.). Springer.

Decision theory:
- Von Neumann, J. and Morgenstern, O. (1944). *Theory of Games and Economic Behavior.* Princeton.
- Savage, L. J. (1954). *The Foundations of Statistics.* Wiley.
- Howard, R. A. (1966). "Information Value Theory."

Reinforcement learning:
- Bellman, R. (1957). *Dynamic Programming.* Princeton.
- Watkins, C. J. C. H. (1989). "Learning from Delayed Rewards."
- Sutton, R. S. and Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
- Lattimore, T. and Szepesvári, C. (2020). *Bandit Algorithms.* Cambridge.

Universal AI:
- Hutter, M. (2005). *Universal Artificial Intelligence.* Springer.
- Hutter, M., Quarel, D., Catt, E. (2024). *An Introduction to Universal Artificial Intelligence.* Routledge.
- Veness, J., Ng, K. S., Hutter, M., Uther, W., Silver, D. (2011). "A Monte-Carlo AIXI Approximation."

Alignment and safety:
- Amodei, D. et al. (2016). "Concrete Problems in AI Safety."
- Hubinger, E. et al. (2019). "Risks from Learned Optimization."
- Skalse, J. et al. (2022). "Defining and Characterizing Reward Hacking."
- MacDiarmid, M. et al. (2025). "Natural Emergent Misalignment from Reward Hacking in Production RL."
- International AI Safety Report 2026.

LLMs:
- Vaswani, A. et al. (2017). "Attention Is All You Need."
- Kaplan, J. et al. (2020). "Scaling Laws for Neural Language Models."
- Hoffmann, J. et al. (2022). "Training Compute-Optimal Large Language Models."

These are not exhaustive. See `research/references.md` for the full chapter-by-chapter bibliography.
