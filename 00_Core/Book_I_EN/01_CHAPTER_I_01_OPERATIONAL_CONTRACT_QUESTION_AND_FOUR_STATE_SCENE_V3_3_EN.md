# Chapter I.1. Operational Contract, Binary Question, and Conditions of the Four-State Scene

Two people take turns asking a single closed box one "yes or no" question each. Together they obtain one of four pairs of answers. Where do these four come from—from the box, or from how the questions themselves are arranged? And what must be agreed upon in advance so that the answer "yes" today means the same thing as "yes" tomorrow? This chapter answers both questions.

The Introduction presented illustrative examples: multi-view projection drawings, a mirror in a room, a lever balance, the exchange *"Are you ready to start? — Yes,"* and two sealed boxes with buttons. They show what conditions give meaning to a binary sign and what four roles form a scene of observation. Let us now translate these conditions into the language of rigorous definitions and theorems, stating all assumptions explicitly and presupposing no pre-given coordinate axis.

The opening chapter of Volume I solves three interconnected problems. First, we fix the exact six-component passport of the **operational contract** $\Gamma$, prove the primacy of a two-class partition over label names, and establish the logical structure of the conditions for a non-degenerate dynamic scene $(Z_D, Z_C, Z_F)$ on finite witness models. Second, we investigate the encounter of **two** binary questions on a shared carrier, separate the emergence of four joint answers from the exact four-element cardinality of the carrier $S_4$ itself, and construct the derived comparison question $\beta(x, c) = x \oplus c$ together with its two equally valid bijective decoders $d_c$ and $d_x$. Third, we derive the universal law of coupling two local systems along a shared interface seam $L \times_K R$, verify the lower bound on the address cost of structural ensemble packaging, and distinguish Belnap's four-valued lattice of two-channel evidence $\mathcal{F}_4$ from the four operational kinds of "zero and emptiness."

---

## §I.1.0. Threshold of the Exact Model: Two-Class Cut, Operational Contract $\Gamma$, and Conditions of a Non-Degenerate Scene

Let us begin with a precise formulation of why an isolated label `1` or "Yes" by itself cannot recover the conditions of an experiment: whenever the family of admissible scenes under consideration contains at least two distinct operational contracts $\Gamma_1 \neq \Gamma_2$ both capable of outputting the answer `1`, the isolated symbol `1` does not determine which contract generated it. We distinguish two elements of the description:
- **the tested domain of candidates** $X$—the set of states or specimens to which the experiment is addressed and which are not exhausted by a single answer;
- **a binary question (reading)** $q : X \twoheadrightarrow V_q$ with a scale of two distinct labels $V_q = \{v_-, v_+\}$ ($v_- \neq v_+$), where both answers are actually attainable on $X$.

As shown by the example of two engineers with cross-connected optical fibers, the pair of labels $\{v_-, v_+\}$ by itself contains neither a privileged algebraic zero nor addition modulo `2`.

> **Theorem I.1.0a (Primacy of the partition over the names of two labels).**  
> *Classical foundation.* Partitioning a set by the kernel of a map $\mathrm{Eq}(q)$ and its invariance under injective renaming of the output scale $\tau \circ q$—elementary set theory. *Contribution of this book:* Primacy of the partition $\mathrm{Eq}(q)$ over answer labels as the opening rule of the operational scene contract, together with a finite counterexample of coarsening under non-injective $\tau$.
> Let $X$ be an arbitrary set and $q : X \twoheadrightarrow V_q$ a surjective map onto a two-element set of labels $V_q$ ($|V_q|=2$). Denote by
> $$\mathrm{Eq}(q) = \{(x, y) \in X \times X \mid q(x) = q(y)\}$$
> the equivalence relation (kernel of the question $q$), and by $\tau : V_q \xrightarrow{\sim} V_q$ the unique non-identity permutation of the two labels. Then:
> 1. $\mathrm{Eq}(\tau \circ q) = \mathrm{Eq}(q)$, and the quotient partition $X / \mathrm{Eq}(q) = \{q^{-1}(v_-), q^{-1}(v_+)\}$ consists of exactly two non-empty disjoint classes, independent of which of the two labels is called `0` and which is called `1`.
> 2. Conversely, if $q' : X \twoheadrightarrow V'_{q'}$ ($|V'_{q'}|=2$) satisfies $\mathrm{Eq}(q') = \mathrm{Eq}(q)$, then there exists a unique bijection $\theta : V_q \xrightarrow{\sim} V'_{q'}$ such that $q' = \theta \circ q$.

*Proof.* Since $\tau : V_q \to V_q$ is bijective, for any $x, y \in X$ the equality $\tau(q(x)) = \tau(q(y))$ is equivalent to $q(x) = q(y)$, whence $\mathrm{Eq}(\tau \circ q) = \mathrm{Eq}(q)$. Surjectivity of $q$ guarantees that both fibers $q^{-1}(v_-)$ and $q^{-1}(v_+)$ are non-empty, and $v_- \neq v_+$ ensures their disjointness. For the second statement, for each $v \in V_q$ choose $x_v \in q^{-1}(v)$ (which exists by surjectivity of $q$) and set $\theta(v) = q'(x_v)$. If $q(x)=v$, then $(x, x_v) \in \mathrm{Eq}(q) = \mathrm{Eq}(q')$, so $q'(x) = q'(x_v) = \theta(q(x))$. Since $q'$ is surjective and $|V_q|=|V'_{q'}|=2$, the map $\theta$ is surjective between two-element sets and hence bijective; uniqueness follows from the surjectivity of $q$. $\square$

Let us summarize in an explicit reference table which constructions of the book depend solely on the cut $\mathrm{Eq}(q)$ itself, and which require an additional choice of algebraic structure on the scale $V_q$:

| Invariant under any bijective scale relabeling $q \mapsto \tau \circ q$ | NOT necessarily preserved under relabeling $q \mapsto \tau \circ q$ |
| :--- | :--- |
| Kernel relation $\mathrm{Eq}(q) \subseteq X \times X$ and quotient partition $X / \mathrm{Eq}(q)$ | Specific label names (`0` or `1`, "green" or "red") of each of the two fibers |
| Joint kernel of a question family $\bigcap_{q \in \mathcal{Q}} \mathrm{Eq}(q)$ and future Nerode equivalence $\sim_\Gamma$ (`Chapter I.3`) | Distinguished "zero" or "neutral" fiber $q^{-1}(0) \subseteq X$ (swapped with $q^{-1}(1)$ under $\tau(b) = 1 \oplus b$) |
| Conditions for descending a deterministic step $T_a$ to quotient memory and cardinality of the minimal automaton $X / {\sim_\Gamma}$ | Arithmetic sum $q(x) + q(y)$, linear dependence of rows, and rank of a numerical Hankel matrix (`Chapter I.8`) |
| Diagonal partition $\{O_0, O_1\}$ of the agreement question $\beta(x,c) = x \oplus c$ on $S_4$ (`§I.1.3`) | Order comparison of answers $q(x) \le q(y)$ and sign of numerical balance (`Chapter I.5`) |

Against the backdrop of the historical survey in the Introduction (`Part I, §2`), we record here three minimal mathematical witnesses for later reference: (1) the involution $F(0)=1,\, F(1)=0$ on $X=\{0,1\}$ has period `2` and $\mathrm{Fix}(F)=\varnothing$ (a stable cycle does not reduce to a fixed point); (2) a reading $q : X \to V_q$ and a step $\sigma : X \to X$ have distinct mapping types (for $X \neq V_q$, the composition $q \circ q$ is ill-typed); (3) on the three rational points $x_0 = 0,\, x_1 = \frac{3}{5},\, x_2 = \frac{6}{5} \in \mathbb{Q}$, the threshold relation $|x - y| \le 1$ is reflexive and symmetric but not transitive ($|x_0 - x_1| = \frac{3}{5} \le 1$, $|x_1 - x_2| = \frac{3}{5} \le 1$, whereas $|x_0 - x_2| = \frac{6}{5} > 1$), in contrast to an exact kernel $\mathrm{Eq}(q)$, which is always an equivalence relation.

In the laboratory scene of two sealed boxes $B_{\text{A}}$ and $B_{\text{B}}$ showing the same current window (`q = green`) and equipped with two buttons $a_1, a_2$ (where on $B_{\text{B}}$ button $a_2$ is locked, while pressing the admissible button $a_1$ leaves $B_{\text{A}}$ green and switches $B_{\text{B}}$ to red), we saw that **the working mathematical observer of the book is the triple $\Gamma_{\text{core}} = (X, \mathcal{Q}, \Omega)$**: the carrier of candidate states $X$, the library of partial questions $\mathcal{Q}$ with domains of applicability $\mathrm{Dom}(q)$, and the library of partial actions and finite protocols $\Omega = (\mathcal{A}, \{\mathrm{Dom}(T_a)\}_{a \in \mathcal{A}}, \Pi)$, while the condition $\mathcal{O} \notin X$ specifies the typing rule of the current description (when a former instrument is included into an extended carrier $X' = X \times M_{\text{instr}}$, the typing boundary moves to the outer frame of the new contract $\Gamma'$). Let us collect all components of the full passport $\Gamma$ and disambiguate the uses of the letter $\Omega$ in a single reference table:

| Component / Symbol | Plain-Language Meaning | Appearance in the Scene of Boxes $B_{\text{A}}, B_{\text{B}}$ | Where It Operates in the Theorems of Book I |
| :---: | :--- | :--- | :--- |
| $X$ (in $\Gamma_{\text{core}}$) | Set of candidate internal states of the scene | Internal mechanism positions beneath the lid | All chapters `I.1–I.9` (carriers $S_4$, $D^2$, $A_6$, $\mathbb{Z}/N\mathbb{Z}$) |
| $\mathcal{Q}$ (in $\Gamma_{\text{core}}$) | Library of partial questions $q : \mathrm{Dom}(q) \to V_q$ with distinct rejection marker $\bot_q \notin V_q$ | Color window `q` on the lid ("green / red") | All chapters `I.1–I.9` (cuts $\mathrm{Eq}(q)$, pullback $T^*$, divisor lattice $D(N)$, slices in nerve $\mathcal{N}$) |
| $\Omega = (\mathcal{A}, \{\mathrm{Dom}(T_a)\}, \Pi)$ (in $\Gamma_{\text{core}}$) | Library (semigroup) of elementary partial actions $T_a : \mathrm{Dom}(T_a) \to X$ with lock marker $\bot_{\mathcal{A}}$ and admissible finite protocols $\Pi$ (words or adaptive trees with `STOP`) | Buttons `a_1, a_2` (on $B_{\text{B}}$ button `a_2` is locked) and the chosen route of pressing them | `Chapters I.1–I.4` (composition of partial steps, Nerode equivalence $\sim_\Gamma$, controller synthesis in `Theorem I.4.2`), `Chapter I.8` (window shift step), `Chapter I.9` (`Corollary I.9.2`) |
| $\Phi$ (external report column) | Final target post-processing of the read protocol record into an output scale $W$ (for scalar recoding of a single scale $V_q \to W$ we write $\Phi_0$) | Rule for transferring readings into a summary ledger | Auxiliary external specification column: used only in the zero-preservation problem under post-processing (`Lemma I.3.2`), does not enter the kernel $\sim_\Gamma$ |
| $\mathcal{O} \notin X$ (typing rule) | Role separation of the contract $(X, \mathcal{Q}, \Omega)$ from elements of the carrier $X$ (see the glossary notes "three meanings of center / four meanings of external" in `Introduction, Part II, §3`) | Shooting and frame-comparison rule in the camera-and-mirror example | Typing discipline throughout the volume; self-description boundary $X \not\twoheadrightarrow \mathcal{P}(X)$ and $|\mathrm{Par}(X,X)| = (n+1)^n$ (`Corollary I.9.2`) |
| **Disambiguating $\Omega$:** $\Omega$ vs. $\Omega_k$ vs. $\Omega_{\mathrm{sub}}$ | 1) $\Omega$ without subscript: library of partial actions and protocols (`I.1, I.4, I.9`);<br>2) $\Omega_1, \Omega_2, \Omega_3 \subset S_4$: two-element state slices in the holonomy loop (`Chapter I.2, §I.2.5`);<br>3) $\Omega_{\mathrm{sub}}$: subobject classifier of a topos in historical notes | In `I.1, I.4, I.9`: bundle of admissible buttons; in `I.2`: three two-point windows on $S_4$ | Prevents confusion between action semigroup $\Omega$, state slices $\Omega_k$, and logical classifier $\Omega_{\mathrm{sub}}$ |

Let us now state the complete definition of the operational contract $\Gamma$ and its working core $\Gamma_{\text{core}} = (X, \mathcal{Q}, \Omega)$.

> **Definition I.1.0 (Operational contract $\Gamma$, its working core $\Gamma_{\text{core}} = (X, \mathcal{Q}, \Omega)$, and observation window $\mathcal{W}$).**  
> An **operational contract of distinction** is a 6-tuple
> $$\Gamma = \bigl(X,\; \mathcal{Q},\; \mathcal{A},\; \{\mathrm{Dom}(T_a)\}_{a \in \mathcal{A}},\; \Pi,\; \Phi\bigr),$$
> in which the first five positions form the **working core of the observer** $\Gamma_{\text{core}} = (X, \mathcal{Q}, \Omega)$ with the library of partial actions and protocols $\Omega = (\mathcal{A}, \{\mathrm{Dom}(T_a)\}_{a \in \mathcal{A}}, \Pi)$ (throughout all theorems of `Chapters I.2–I.9` where external post-processing $\Phi$ is the identity, the contract is written concisely as the triple $\Gamma = (X, \mathcal{Q}, \Omega)$):
> 1. $X$ is a non-empty set of candidate states (the carrier of what is distinguished);
> 2. $\mathcal{Q}$ is a family of admissible questions, where each question $q \in \mathcal{Q}$ is specified by its domain of definition $\mathrm{Dom}(q) \subseteq X$, its answer scale $V_q$ ($|V_q| \ge 2$), and a map $q : \mathrm{Dom}(q) \to V_q$; when an input $x \notin \mathrm{Dom}(q)$ falls outside the question's domain of applicability, a dedicated inapplicability marker $\bot_q \notin V_q$ is returned, **strictly distinct** from any substantive answer $0 \in V_q$ ($\bot_q \neq 0$);
> 3. $\mathcal{A}$ is an alphabet of elementary actions (continuation transitions);
> 4. $\{\mathrm{Dom}(T_a)\}_{a \in \mathcal{A}}$ is a family of domains of admissibility $\mathrm{Dom}(T_a) \subseteq X$ on which transition maps $T_a : \mathrm{Dom}(T_a) \to X$ are defined (an attempt to apply $a$ outside $\mathrm{Dom}(T_a)$ is recorded as an inadmissible step $\bot_{\mathcal{A}}$, not as a "silent identity");
> 5. $\Pi$ is a class of admissible finite protocols (finite words from $\mathcal{A}^*$ or finite adaptive trees selecting the next action $a_{k+1}$ and question $q_{k+1}$ from the read history of answers, including the empty protocol $\varepsilon$ of instantaneous reading without pressing buttons and an explicit halting marker `STOP`);
> 6. $\Phi$ is a rule of target post-processing mapping the read protocol record into a target output scale $W$ with an explicitly specified domain of definition (when a particular task considers scalar recoding of a single output scale $V_q \to W$, we denote it by $\Phi_0$).  
> A fixed sub-bundle $\mathcal{W} = (\mathcal{Q}_0, \mathcal{A}_0, H)$ of questions $\mathcal{Q}_0 \subseteq \mathcal{Q}$, actions $\mathcal{A}_0 \subseteq \mathcal{A}$, and finite protocol-length horizon $H \in \mathbb{Z}_{\ge 0}$ available in a given experiment is called an **observation window** inside the contract $\Gamma$. The entries of $\Gamma$ are **typed specification roles**, not independent state coordinates: the number of slots in the passport never by itself generates $2^6$ states of the carrier $X$.

Let us now separate, in a compact lemma on well-formedness and non-degeneracy, the contract typing rule $(Z_C)$ from the dynamic properties of a nontrivial question $(Z_D)$, carrier motion $(C_{\mathrm{step}})$, and observable answer shift $(Z_F)$.

> **Theorem I.1.0b (Lemma on typing well-formedness $(Z_C)$ and the logical relations among $(Z_D, C_{\mathrm{step}}, Z_F)$).**  
> *Classical foundation.* Boolean conditions on finite maps and pairwise counterexamples of axiom independence—classical axiomatic method. *Contribution of this book:* Exact hierarchy and pairwise independence of the operational triads $(Z_D, Z_C, Z_F)$ and $(C_{\mathrm{div}}, C_{\mathrm{type}}, C_{\mathrm{step}})$ with minimal finite failure witnesses.
> Suppose the typing well-formedness rule $(Z_C) \equiv (C_{\mathrm{type}})$ is fixed on the candidate scene descriptions: the contract is not identified in type with an element of the carrier ($\mathcal{O} \notin X$), and every partial question $q \in \mathcal{Q}$ maps $\mathrm{Dom}(q) \to V_q$ single-valuedly with a separated rejection marker $\bot_q \notin V_q$. Consider three substantive properties on a well-typed contract:
> - $(Z_D) \equiv (C_{\mathrm{div}})$ **Non-degeneracy of distinction:** $|X| \ge 2$ and there exists a question $q \in \mathcal{Q}$ taking at least two distinct values on $\mathrm{Dom}(q)$;
> - $(C_{\mathrm{step}})$ **Nontriviality of carrier step:** there exist an action $a \in \mathcal{A}$ and a state $x \in \mathrm{Dom}(T_a)$ such that $T_a(x) \neq x$;
> - $(Z_F)$ **Observable efficacy of continuation:** there exist $a \in \mathcal{A}$, $q \in \mathcal{Q}$, and a state $x \in \mathrm{Dom}(T_a) \cap \mathrm{Dom}(q)$ such that $T_a(x) \in \mathrm{Dom}(q)$ and $q(T_a(x)) \neq q(x)$.  
> Then two assertions hold:
> 1. **One-way implication $(Z_F) \implies (Z_D) \land (C_{\mathrm{step}})$ and minimal cardinality of hidden motion:** under valid typing $(Z_C)$, condition $(Z_F)$ **strictly implies** both $(Z_D)$ and $(C_{\mathrm{step}})$. The converse implication $(Z_D) \land (Z_C) \implies (Z_F)$ is **false** both for an immobile step $T_a = \mathrm{id}_X$ (already at $|X|=2$) and under nontrivial **hidden motion within one and the same contract $\Gamma$** ($(Z_D) \land (Z_C) \land (C_{\mathrm{step}}) \land \neg(Z_F)$): for a single total binary question and a total step, the minimal carrier of such hidden motion has cardinality $|X| = 3$, because at $|X| = 2$ any distinguishing binary question is bijective and detects every motion.
> 2. **Exact kernel-fiber crossing criterion on the shared domain and pairwise independence of the elementary conditions:** the three elementary conditions $(C_{\mathrm{div}}, C_{\mathrm{type}}, C_{\mathrm{step}})$ are pairwise independent already on the two-element carrier $X=\{0,1\}$, and under $(Z_C)$ the observable shift $(Z_F)$ is equivalent to the existence of $a \in \mathcal{A}$ and $q \in \mathcal{Q}$ such that the shared domain $D_{q,T_a} := \mathrm{Dom}(q) \cap T_a^{-1}(\mathrm{Dom}(q))$ is non-empty and the step $T_a$ **crosses at least one fiber of the kernel $\mathrm{Eq}(q)$ on $D_{q,T_a}$**, i.e., $\exists x \in D_{q,T_a},\; \bigl(x, T_a(x)\bigr) \notin \mathrm{Eq}(q)$. Simultaneous satisfaction of non-degeneracy $|q(D_{q,T_a})| \ge 2$ and motion $\exists x \in D_{q,T_a} : T_a(x) \neq x$ alone fails at $|X| \ge 3$ by the within-fiber motion of Witness `2b`, and inequality of the totalized maps $(q \circ T_a)_\bot \neq q_\bot$ alone fails by Witness `4`, where the maps differ only in their domains while $D_{q,T_a} = \varnothing$.

*Proof.* In (1), given $(Z_C)$ and $(Z_F)$ for a chosen $x \in D_{q,T_a} = \mathrm{Dom}(q) \cap T_a^{-1}(\mathrm{Dom}(q))$, single-valuedness of $q$ and the inequality $q(T_a(x)) \neq q(x)$ imply $T_a(x) \neq x$ ($(C_{\mathrm{step}})$) and $|q(\mathrm{Dom}(q))| \ge 2$ ($(Z_D)$). On $X = \{0, 1\}$, any total question $q : X \to \{0, 1\}$ with $|q(X)| = 2$ is bijective, so $T_a(x) \neq x$ implies $q(T_a(x)) \neq q(x)$ (`0` out of `16` pairs $(q, T)$ satisfy $(Z_D) \land (C_{\mathrm{step}}) \land \neg(Z_F)$). In (2), by definition of $\mathrm{Eq}(q) = \{(x,y) \in \mathrm{Dom}(q)^2 \mid q(x)=q(y)\}$, the condition $x \in D_{q,T_a}$ and $(x, T_a(x)) \notin \mathrm{Eq}(q)$ is symbol-for-symbol equivalent to $x \in \mathrm{Dom}(q) \cap \mathrm{Dom}(T_a)$, $T_a(x) \in \mathrm{Dom}(q)$, and $q(T_a(x)) \neq q(x)$, i.e., $(Z_F)$. Pairwise and triple independence of $(C_{\mathrm{div}}, C_{\mathrm{type}}, C_{\mathrm{step}})$ on $X = \{0,1\}$ is established by Witnesses `1` ($C_{\mathrm{div}} \land C_{\mathrm{type}} \land \neg C_{\mathrm{step}}$), `2a` ($\neg C_{\mathrm{div}} \land C_{\mathrm{type}} \land C_{\mathrm{step}}$), and `3` ($C_{\mathrm{div}} \land \neg C_{\mathrm{type}} \land C_{\mathrm{step}}$), while insufficiency of a within-fiber step and of disjoint domains is shown by Witnesses `2b` and `4` in the table below. $\square$

**Counterexample I.1.0a (Summary table of finite witness models for Theorem `I.1.0b`).**

| Witness and Carrier Size | Model Structure $(X, q, T)$ | Conditions Satisfied | Condition Violated and What It Demonstrates |
| :--- | :--- | :---: | :--- |
| **1. Frozen scene** ($|X|=2$) | $X=\{0,1\}$, $\mathrm{Dom}(q)=\mathrm{Dom}(T)=X$, $q(x)=x$, $T(x)=x$, $\bot_q \notin \{0,1\}$ | $(C_{\mathrm{div}}),\; (C_{\mathrm{type}})$ | Violates $(C_{\mathrm{step}})$ and $(Z_F)$: static distinction without state motion |
| **2a. Blind window** ($|X|=2$)<br>**2b. Hidden motion** ($|X|=3$) | 2a) $X=\{0,1\}$, $q_0(x)\equiv 0$, $T(x)=1-x$;<br>2b) $X=\{0,1,2\}$, $q(0)=q(1)=0,\, q(2)=1$, $T(0)=1,\, T(1)=0,\, T(2)=2$ | 2a) $(C_{\mathrm{type}}),\; (C_{\mathrm{step}})$;<br>2b) $(Z_D),\; (Z_C),\; (C_{\mathrm{step}})$ | 2a violates $(C_{\mathrm{div}})$; in 2b, with $(Z_D) \land (Z_C) \land (C_{\mathrm{step}})$ holding, $T$ swaps `0 ↔ 1` inside the fiber $q^{-1}(0)$, so $q \circ T = q$ and $(Z_F)$ fails |
| **3. Conflation of rejection with scale zero** ($|X|=2$) | $X=\{0,1\}$, $q(x)=x$, $T(x)=1-x$, but in the output register the inapplicability marker $\bot_q$ is encoded by the same symbol `0` as the answer $q(0)=0$ ($\bot_q = 0 \in V_q$) | $(C_{\mathrm{div}}),\; (C_{\mathrm{step}})$ | Violates typing purity $(C_{\mathrm{type}})$: sensor failure is indistinguishable from the substantive answer "no / zero" |
| **4. Disjoint domain of definition** ($|X|=3$) | $X=\{0,1,2\}$, $\mathrm{Dom}(q)=\{0,1\}$ ($q(0)=0, q(1)=1, q_\bot(2)=\bot_q$), $T(0)=2, T(1)=2, T(2)=0$ | $(C_{\mathrm{div}}),\; (C_{\mathrm{type}}),\; (C_{\mathrm{step}})$ and $q_\bot \circ T \neq q_\bot$ | Violates $(Z_F)$: although $q_\bot=(0,1,\bot_q) \neq (\bot_q,\bot_q,0)=(q\circ T)_\bot$, the intersection $\mathrm{Dom}(q) \cap T^{-1}(\mathrm{Dom}(q)) = \varnothing$ is empty |

---

## §I.1.1. Tangible Scene: Four Calibration Cards, Two Binary Questions, and the Birth of the Polar Cell

Above we established that a single substantive binary question cuts the candidate domain $X$ into exactly two non-empty classes. Let us take the next step: **what happens when two binary questions are addressed simultaneously to one and the same tested domain?**

Let us set up a hand-reproducible laboratory scene with an explicit discrete reading model. Place two kinds of specimens on a table—a self-luminous screen standard (`x = 0`) and a matte pigmented card (`x = 1`)—and illuminate the table through one of two fixed filters: daylight (`c = 0`) or evening (`c = 1`). So as not to attribute automatic Boolean laws to continuous color mixing, **we explicitly declare the discrete truth table of a threshold comparison sensor**: the sensor outputs label `0` ("matched to regime calibration") on the pairs `(screen, daylight) = (0,0)` and `(paper, evening) = (1,1)`, and outputs label `1` ("mismatched") on the cross pairs `(0,1)` and `(1,0)`. As long as the filter is not switched, the sensor's answer seems to reside inside the specimen itself; yet as soon as the filter $c$ is switched, both specimens flip their sensor reading to the opposite value. Behind the single window opens the four-element card board $S_4 = \{(0,0), (0,1), (1,0), (1,1)\}$. *(We agree here and throughout the book: the symbol $S_4$ always denotes this four-element state carrier, whereas the symmetric group of permutations on four elements is written in Fraktur as $\mathfrak{S}_4$, $|\mathfrak{S}_4| = 24$.)*

Let us view this four-element carrier through the eyes of a geometer: even on the exact same four points, different adjacency predicates generate non-isomorphic or structurally distinct graphs.

```text
   (a) Polar square K_2 □ K_2 on S_4        (b) Two pairings on S_4
       (edges = flipping exactly one             Antipodal involution σ (2K_2):   Axis exchange swap (2 loops + K_2):
        of the two questions q_x or q_c)         (0,0) <=====> (1,1)              (0,0)↺        (1,1)↺
                                                 (0,1) <=====> (1,0)              (0,1) <-----> (1,0)
        (0,1) -------- (1,1)                     [0 fixed points]                 [2 fixed points]
          |              |
          |  diagonals   |                  (c) Unlabeled cycle C_4 without distinguished axes:
          | of β-fibers  |                      v_1 --- v_2
        (0,0) -------- (1,0)                     |       |     |Aut(C_4)| = 8, whereas preserving each axial
         horizontal: flip x                      v_4 --- v_3   partition Eq(q_x), Eq(q_c) leaves Z_2^2 (4)
         vertical:   flip c
```

**Reader's caption to `Fig. I.1.1`:** three graph-theoretic views of the four-element carrier $S_4 = \{(0,0),(0,1),(1,0),(1,1)\}$. In panel (a), an edge connects states at Hamming distance $d_{\mathrm{H}} = 1$ (flipping exactly one question, $q_x$ horizontally or $q_c$ vertically); forgetting the axis coloring yields the simple cycle $C_4$ with automorphism group $|\mathrm{Aut}(C_4)| = 8$ in panel (c), whereas preserving each axial partition $\mathrm{Eq}(q_x)$ and $\mathrm{Eq}(q_c)$ leaves the subgroup $\mathbb{Z}_2 \times \mathbb{Z}_2$ of order `4`. In panel (b), the antipodal coupling $\sigma(x,c) = (1\oplus x, 1\oplus c)$ yields the graph $2K_2$ without fixed points, whereas the axis reflection $\mathrm{swap}(x,c) = (c,x)$ fixes the agreement diagonal $O_0 = \{(0,0),(1,1)\}$ pointwise and thus provides an exact witness of stepping outside the axial symmetry group of the square.

---

## §I.1.2. Four Naive Traps at the Threshold of Four States

Before proceeding to the proofs, let us highlight four pitfalls into which intuition easily falls upon first meeting a pair of binary questions:
1. **The trap of the word "kernel."** In linear algebra, the kernel of a linear operator $L$ means the zero preimage $\ker L = L^{-1}(0)$, and $\ker L = \{0\}$ is equivalent to injectivity of $L$. On arbitrary sets and monoids this fails: a question $q : X \to V_q$ has no distinguished zero in $V_q$, a single fiber $q^{-1}(b)$ on $S_4$ contains `2` states whereas the kernel relation $\mathrm{Eq}(q) \subseteq S_4 \times S_4$ consists of **`8` ordered pairs**, and triviality of the zero preimage $h^{-1}(0)=\{0\}$ for a homomorphism of commutative monoids **does not imply** its injectivity.
2. **The trap of automatic multiplication $2 \times 2 = 4$.** Two *distinct* surjective binary questions ($\mathrm{Eq}(q_1) \neq \mathrm{Eq}(q_2)$) need not by themselves generate `4` joint answers—on a three-element carrier they can already separate all points while yielding only `3` joint answers; and even when `4` joint answers are realized, the carrier $X$ itself has cardinality `4` only when the joint reading is injective.
3. **The trap of a single decoder.** When the comparison signal $\beta = x \oplus c$ is formed from specimen $x \in \{0,1\}$ and context $c \in \{0,1\}$, the pair $(x,c)$ can be recovered not only from $(\beta, c)$, but with complete symmetry also from $(\beta, x)$.
4. **The trap of conflated foursomes.** The four states of the polar cell $S_4$, the four epistemic statuses of Belnap's two-channel evidence lattice $\mathcal{F}_4 = \{\bot, \mathbf{0}, \mathbf{1}, \top\}$, and the four operational kinds of "zero / emptiness" all have cardinality `4`, but possess completely different algebras.

---

## §I.1.3. Kernel of a Question, Four Faces of the Word "Kernel," and Criterion for the Birth of Four States

> **Definition I.1.1 (Binary question, kernel relation, and single fiber).**  
> Let $\Gamma$ be an operational contract on a carrier $X$.
> 1. A **total nontrivial binary question** on $X$ is a surjective map $q : X \twoheadrightarrow V_q$ onto a two-element set of labels $V_q$ ($|V_q|=2$). If a question is defined only on a proper subset $\mathrm{Dom}(q) \subsetneq X$, its total completion is the map $q_\bot : X \to V_q \sqcup \{\bot_q\}$ setting $q_\bot(x)=\bot_q$ for $x \notin \mathrm{Dom}(q)$.
> 2. The **single fiber** of question $q$ over a label $b \in V_q$ is the subset of the carrier
> $$F_q(b) = q^{-1}(b) = \{x \in \mathrm{Dom}(q) \mid q(x) = b\} \subseteq X.$$
> 3. The **kernel relation** (indistinguishability equivalence on $\mathrm{Dom}(q)$) of question $q$ is the subset of the Cartesian square
> $$\mathrm{Eq}(q) = \{(x, y) \in \mathrm{Dom}(q) \times \mathrm{Dom}(q) \mid q(x) = q(y)\} = \bigsqcup_{b \in V_q} \bigl(F_q(b) \times F_q(b)\bigr)$$
> *(when $\mathrm{Dom}(q) \subsetneq X$ is proper, the equivalence relation on the entire carrier $X$ is the kernel of the totalization $\mathrm{Eq}(q_\bot) = \mathrm{Eq}(q) \sqcup (X \setminus \mathrm{Dom}(q))^2$, grouping out-of-domain points into a separate rejection fiber $\bot_q$)*.

On the four-element carrier $S_4 = \{(0,0),(0,1),(1,0),(1,1)\}$, for the balanced question $q_x(x,c)=x$ of type `2 + 2`, each single fiber $F_{q_x}(0)$ and $F_{q_x}(1)$ consists of **`2` states**, whereas the kernel relation $\mathrm{Eq}(q_x)$ contains $2^2 + 2^2 = \mathbf{8}$ ordered pairs out of the `16` pairs of $S_4 \times S_4$. For an unbalanced binary question of type `1 + 3`, the kernel relation contains $1^2 + 3^2 = \mathbf{10}$ ordered pairs; thus partitions of type `2 + 2` and `1 + 3` are distinguished already by the cardinality of $\mathrm{Eq}(q)$ prior to any algebra.

> **Lemma I.1.1 (Set-theoretic kernel relation versus zero fiber of a group homomorphism).**  
> *Classical foundation.* Canonical factorization of a map through its equivalence kernel and criterion for descending an operation onto a congruence—standard universal algebra. *Contribution of this book:* Separating the set-theoretic pair kernel $\mathrm{Eq}(q)$ from the algebraic zero preimage $\ker_{\mathrm{alg}}(q)$ and explicit failure of quotient descent on the saturating semigroup $(\{0,1,2,3\}, \oplus_{\mathrm{sat}})$.
> 1. For any map of sets $f : X \to Y$ ($X \neq \varnothing$), the kernel relation $\mathrm{Eq}(f) \subseteq X \times X$ is non-empty (it contains the diagonal $\Delta_X = \{(x,x) \mid x \in X\}$), and $f$ is injective if and only if $\mathrm{Eq}(f) = \Delta_X$.
> 2. If $L : G \to H$ is a group homomorphism (or a linear map of modules / vector spaces), then the zero fiber $\ker L = L^{-1}(0_H) \subseteq G$ contains the neutral element $0_G \in \ker L$, so **$\ker L$ is never empty** ($|\ker L| \ge 1$), and the kernel relation is uniquely recovered from the zero fiber: $(x, y) \in \mathrm{Eq}(L) \iff x - y \in \ker L$. In particular, a group homomorphism $L$ is injective if and only if $\ker L = \{0_G\}$.

*Proof.* Item (1) follows from the definition of injectivity $f(x)=f(y) \implies x=y$. In item (2), $L(0_G)=0_H \implies 0_G \in \ker L$, and in a group with inverses the equality $L(x)=L(y)$ is equivalent to $L(x - y) = L(x) - L(y) = 0_H$, i.e., $x - y \in \ker L$. $\square$

**Counterexample I.1.0b (Insufficiency of a singleton zero preimage $h^{-1}(0)=\{0\}$ for injectivity of a commutative monoid homomorphism).** On the finite commutative monoid $M = (\{0, 1, 2\}, \max, 0)$, the saturation map $h : M \to M$ defined by $h(x) = \min(x, 1)$ ($0 \mapsto 0,\, 1 \mapsto 1,\, 2 \mapsto 1$) preserves the neutral element $h(0)=0$ and the operation $h(\max(x,y)) = \max(h(x), h(y))$ across all `9` pairs, and has a singleton zero preimage $h^{-1}(0) = \{0\}$, yet is **not injective** because it collapses $h(1) = h(2) = 1$ ($|\mathrm{Eq}(h)| = 1^2 + 2^2 = 5 > 3 = |\Delta_M|$): without subtraction, a collision over `1` cannot be translated to the fiber over `0`.

Let us now determine precisely when a pair of binary questions generates four joint answers and when the carrier itself has cardinality `4`.

> **Theorem I.1.1 (Criterion for four joint answers versus exact carrier cardinality $|X|=4$).**  
> *Classical foundation.* Joint map into the Cartesian product of two binary scales $\{0,1\}^2$ and counting four intersection cells—elementary finite combinatorics. *Contribution of this book:* Criterion for the birth of the minimal four-state polar cell $S_4$ from a pair of independent binary questions and exact fraction `24/256` of question pairs on a four-point carrier.
> Let $q_1 : X \twoheadrightarrow V_1$ and $q_2 : X \twoheadrightarrow V_2$ be two total nontrivial binary questions on the same carrier $X$ ($|V_1|=|V_2|=2$). Form the joint reading map
> $$q_{12} = (q_1, q_2) : X \longrightarrow V_1 \times V_2, \qquad x \longmapsto \bigl(q_1(x), q_2(x)\bigr).$$
> **Part A (Four classes of joint answers, $|\mathrm{im}(q_{12})| = 4$).** The following three conditions are pairwise equivalent and imply the lower bound $|X| \ge 4$:
> 1. The joint reading $q_{12}$ is surjective onto $V_1 \times V_2$, i.e., $|\mathrm{im}(q_{12})| = 4$.
> 2. All four pairwise intersections of fibers are non-empty:
> $$\forall (u, v) \in V_1 \times V_2 \qquad F_{q_1}(u) \cap F_{q_2}(v) \neq \varnothing.$$
> 3. The intersection of kernel relations $\mathrm{Eq}(q_{12}) = \mathrm{Eq}(q_1) \cap \mathrm{Eq}(q_2)$ partitions the carrier $X$ into exactly **four** equivalence classes ($|X / \mathrm{Eq}(q_{12})| = 4$), invariant under any independent label renamings $\tau_1 \in \mathrm{Aut}(V_1),\, \tau_2 \in \mathrm{Aut}(V_2)$:
> $$\mathrm{Eq}\bigl((\tau_1 \circ q_1,\, \tau_2 \circ q_2)\bigr) = \mathrm{Eq}(q_{12}).$$
> **Part B (Exact four-element cardinality of the carrier itself, $|X| = 4$).** The map $q_{12} : X \to V_1 \times V_2$ is a bijection (and in particular $|X| = 4$ at the level of the underlying set $X$ itself) if and only if the conditions of Part A hold **and in addition** the pair $(q_1, q_2)$ separates points of the carrier $X$ ($\mathrm{Eq}(q_{12}) = \Delta_X$, i.e., each of the four intersections $F_{q_1}(u)\cap F_{q_2}(v)$ is a singleton).

*Proof.* For any pair of labels $(u, v) \in V_1 \times V_2$, the preimage $q_{12}^{-1}(u, v)$ equals $F_{q_1}(u) \cap F_{q_2}(v)$, so $(u,v) \in \mathrm{im}(q_{12}) \iff F_{q_1}(u) \cap F_{q_2}(v) \neq \varnothing$. Since $|V_1 \times V_2| = 4$, the equality $|\mathrm{im}(q_{12})|=4$ is equivalent to non-emptiness of all four intersections, whence $|X| = \sum_{u,v} |F_{q_1}(u)\cap F_{q_2}(v)| \ge 4$. The canonical bijection $X / \mathrm{Eq}(q_{12}) \xrightarrow{\sim} \mathrm{im}(q_{12})$ and the identity $\mathrm{Eq}(q_{12}) = \mathrm{Eq}(q_1) \cap \mathrm{Eq}(q_2)$ yield `(1) <=> (3)` and invariance under $\tau_1 \times \tau_2$. In Part B, bijectivity is equivalent to the conjunction of surjectivity (Part A) and injectivity ($\mathrm{Eq}(q_{12})=\Delta_X$), under which a sum of four integers $\ge 1$ equals `4` if and only if each summand equals `1`. $\square$

**Counterexample I.1.1 (Two opposite failures on `3` and on `5` states).**
1. **Point separation without a fourth joint answer ($|X| = 3$):** on $X_3 = \{a, b, c\}$, the questions $q_1=(0,0,1)$ and $q_2=(0,1,1)$ are surjective, have distinct kernels ($\mathrm{Eq}(q_1) \neq \mathrm{Eq}(q_2)$), and completely separate points ($\mathrm{Eq}(q_{12}) = \Delta_{X_3}$), yet $F_{q_1}(1) \cap F_{q_2}(0) = \varnothing$ and $|\mathrm{im}(q_{12})| = \mathbf{3} < 4$.
2. **All four joint answers without $|X| = 4$ ($|X| = 5$):** on $X_5 = \{s_1, s_2, s_3, s_4, s_5\}$ with $q_{12}(s_1)=q_{12}(s_5)=(0,0),\, q_{12}(s_2)=(0,1),\, q_{12}(s_3)=(1,0),\, q_{12}(s_4)=(1,1)$, all four fiber intersections are non-empty and $|\mathrm{im}(q_{12})| = |X_5 / \mathrm{Eq}(q_{12})| = \mathbf{4}$, yet $|X_5| = \mathbf{5} \neq 4$ because $s_1 \neq s_5$ are merged inside the fiber $F_{q_1}(0)\cap F_{q_2}(0)$.

---

## §I.1.4. The Derived Comparison Question $\beta = x \oplus c$, Two Symmetric Decoders, and the Coupled Whole with a Seam

Suppose the condition of Theorem `I.1.1(A)` is satisfied, and we pass to the four-element quotient carrier $S_4 = X / \mathrm{Eq}(q_{12})$. By itself, the quotient $S_4 \cong V_1 \times V_2$ does not yet contain addition modulo `2`. To write down an algebraic formula comparing the two answers, **we explicitly declare a Boolean encoding** of both scales: fix bijections $\iota_1 : V_1 \xrightarrow{\sim} \mathbb{F}_2$ and $\iota_2 : V_2 \xrightarrow{\sim} \mathbb{F}_2$ ($\mathbb{F}_2 = \{0, 1\}$ with operation $\oplus$) and set $x = \iota_1(q_1(\cdot)) \in \mathbb{F}_2$, $c = \iota_2(q_2(\cdot)) \in \mathbb{F}_2$.

On the encoded cell $S_4 = \mathbb{F}_2 \times \mathbb{F}_2$ arises the **derived binary comparison question**:
$$\beta : S_4 \longrightarrow \mathbb{F}_2, \qquad \beta(x, c) = x \oplus c.$$
Its fiber $O_0 = \beta^{-1}(0) = \{(0,0), (1,1)\}$ forms the **background of agreement** with the chosen reference (uniting pre-signal rest `(0,0)` and saturated resonance with the standard `(1,1)`—neither state contests the regime $c$), while the fiber $O_1 = \beta^{-1}(1) = \{(0,1), (1,0)\}$ singles out the **figure of discrepancy** (a signal flash against a zero reference `(1,0)` and a signal deficit under an active reference `(0,1)`). If the reference itself is switched, $c \mapsto 1 \oplus c$ (or the encoding of one axis is flipped, $\iota_2 \mapsto 1 \oplus \iota_2$), figure and background exchange places ($\beta \mapsto 1 \oplus \beta$), yet the diagonal **quotient partition** $S_4 / \mathrm{Eq}(\beta) = \{O_0, O_1\}$ itself (along with its 8-element kernel relation $\mathrm{Eq}(\beta) = (O_0 \times O_0) \sqcup (O_1 \times O_1)$) remains unchanged: on the unencoded product $V_1 \times V_2$, the two diagonal pairs correspond canonically to the two bijections $V_1 \xrightarrow{\sim} V_2$.

> **Theorem I.1.2 (Address-free erasure, free $\mathbb{Z}_2$-torsor on $\beta$-fibers, and the two symmetric decoders).**  
> *Classical foundation.* The affine group $\mathbb{F}_2^2 \rtimes \mathrm{GL}_2(2)$, free transitive actions ($\mathbb{F}_2$-torsors), and Belnap's four-valued lattice $\mathcal{F}_4$—classical finite algebra and logic. *Contribution of this book:* Simultaneous triad of equally rightful `2+2` partitions $(q_x, q_c, \beta = x \oplus c)$, mutual decoders $d_c, d_x$ on a fixed support, contrast between involutions $\sigma$ (`0` fixed points) and $\mathrm{swap}$ (`2`), and non-coincidence of Boolean difference with scalar difference on $\mathcal{F}_4$.
> Let $S_4 = \mathbb{F}_2^2 = \{(x, c)\}$ and $\beta(x,c) = x \oplus c$ with fibers $O_0 = \{(0,0),(1,1)\}$ and $O_1 = \{(0,1),(1,0)\}$. Then:
> 1. **Address-free loss of distinguishability:** the coordinate projections of each $\beta$-fiber cover the entire scale $\mathbb{F}_2$:
> $$\mathrm{pr}_x(O_0) = \mathrm{pr}_x(O_1) = \{0, 1\}, \qquad \mathrm{pr}_c(O_0) = \mathrm{pr}_c(O_1) = \{0, 1\}.$$
> Neither the single bit $\beta(x,c)$ alone nor the single bit $x$ (or $c$) alone allows recovery of the pair $(x,c)$.
> 2. **Free involution versus axis exchange:** simultaneous negation of both coordinates
> $$\sigma : S_4 \longrightarrow S_4, \qquad \sigma(x, c) = (1 \oplus x,\; 1 \oplus c)$$
> is a fixed-point-free involution ($\sigma^2 = \mathrm{id}_{S_4}$, $\mathrm{Fix}(\sigma) = \varnothing$), preserves the comparison question ($\beta \circ \sigma = \beta$), and turns each fiber $O_0, O_1$ into a free $\mathbb{Z}_2$-torsor. By contrast, coordinate exchange $\mathrm{swap}(x,c) = (c, x)$ also satisfies $\beta \circ \mathrm{swap} = \beta$, but has **two** fixed points $\mathrm{Fix}(\mathrm{swap}) = O_0 = \{(0,0),(1,1)\}$.
> 3. **Two equally valid bijective decoders:** the full state $(x,c) \in S_4$ is bijectively recovered from the comparison signal $\beta$ whenever **either** of the two initial coordinates—the context $c$ or the reading $x$—is retained:
> $$\Phi_c : S_4 \xrightarrow{\;\sim\;} \mathbb{F}_2^2,\quad \Phi_c(x,c) = (x \oplus c,\; c), \qquad d_c(\beta, c) = (\beta \oplus c,\; c);$$
> $$\Phi_x : S_4 \xrightarrow{\;\sim\;} \mathbb{F}_2^2,\quad \Phi_x(x,c) = (x \oplus c,\; x), \qquad d_x(\beta, x) = (x,\; \beta \oplus x).$$
> Moreover, $\Phi_c^{-1} = d_c$, $\Phi_x^{-1} = d_x$, and the three balanced questions $\{q_x, q_c, \beta\}$ are linked by the symmetric identity $x \oplus c \oplus \beta = 0$: any two of them bijectively encode $S_4$.

*Proof.* Item (1) is verified by substituting the points of $O_0$ and $O_1$. In item (2), $\sigma(\sigma(x,c)) = (x,c)$, the equation $1\oplus x = x$ has no solutions in $\mathbb{F}_2$, $\beta(\sigma(x,c)) = (1\oplus x)\oplus(1\oplus c) = x \oplus c$, and $(c,x)=(x,c) \iff x=c$. In item (3), $(u \oplus v) \oplus v = u$ in $\mathbb{F}_2$ implies $d_c(\Phi_c(x,c)) = (x,c)$, $\Phi_c(d_c(\beta,c)) = (\beta,c)$, $d_x(\Phi_x(x,c)) = (x,c)$, and $\Phi_x(d_x(\beta,x)) = (\beta,x)$. $\square$

Let us now see how two local carriers $L$ and $R$ join into a **coupled whole** along a shared interface $K$. The free product of two polar cells $L = S_4$ and $R = S_4$ contains $4 \times 4 = 16$ pairs, whereas requiring a shared seam regime $c_L = c_R \in K = \mathbb{F}_2$ cuts out the fiber product $L \times_K R$ consisting of **`8` compatible states**.

```text
   Seam reading cospan diagram:   L = S_4  --- π_L(x,c_L)=c_L --->  K = F_2  <--- π_R(y,c_R)=c_R ---  R = S_4

   (a) Induced subgraph in Q_4 on the 8 seam vertices      (b) Graph of compatible seam steps Q_3 (8 vertices, 12 edges)
       (only single flips of x or y inside Q_4:                (to the 8 local edges of 2Q_2 are explicitly added 4 dotted
        two disconnected squares 2Q_2, 8 edges!)                synchronous seam flips c: 0 <---> 1 simultaneously in L and R!)

       fiber c = 0 (Q_2, 4 edges)  fiber c = 1 (Q_2, 4 edges)      (0,1,0)-------(1,1,0)
       (0,1,0)---(1,1,0)           (0,1,1)---(1,1,1)               |  :          |  :
          |         |                 |         |                  | (0,1,1)-----+-(1,1,1)
       (0,0,0)---(1,0,0)           (0,0,1)---(1,0,1)              (0,0,0)-------(1,0,0) :
       [a single shift of c_L without c_R leaves the seam!]           :          |  :   |
                                                                     (0,0,1)-----+-(1,0,1)
```

**Reader's caption to `Fig. I.1.2`:** the coupled whole with a seam $V_{\text{seam}} = S_4 \times_{\mathbb{F}_2} S_4 = \{((x,c),(y,c)) \mid x,y,c \in \mathbb{F}_2\}$ (`8` vertices out of the `16` pairs of $S_4 \times S_4$). In panel (a), the induced subgraph of the ambient tesseract $Q_4$ retains only intra-fiber flips of $x$ or $y$ at fixed seam $c$, splitting into two disconnected squares $2Q_2$ (`8` edges): a single flip of $c_L$ without $c_R$ takes every point off the seam. In panel (b), `4` synchronous seam edges of simultaneous switching $c_L = c_R$ (`:`) are explicitly adjoined, assembling the vertices into a connected cube $Q_3$ (`12` edges; the full automorphism group of the uncolored cube has order `48`, preserving the seam fibration with allowed exchange of base and wings gives order `16`, and strictly preserving the seam reading $\pi_K$ leaves `8` symmetries for unordered wings and `4` for ordered wings).

> **Theorem I.1.3 (Coupled whole with a seam $L \times_K R$ and criterion for a compatible step).**  
> *Classical foundation.* The construction $L \times_K R$ is the classical fibered product (pullback) in the category of sets $\mathbf{Set}$, and its universal property is standard. *Contribution of this book:* Reading the pullback as a coupled whole of two observers sharing a seam ($8$ joint states of the cube $Q_3$ inside $16$ pairs of $S_4 \times S_4$) and criterion for unique descent of a compatible pair of steps.
> Let $\pi_L : L \to K$ and $\pi_R : R \to K$ be maps from the left and right state carriers onto a shared seam carrier $K$, and let
> $$L \times_K R = \{(\ell, r) \in L \times R \mid \pi_L(\ell) = \pi_R(r)\}$$
> with structural projections $p_L(\ell, r)=\ell$, $p_R(\ell, r)=r$ and shared seam reading $\pi_K(\ell, r) = \pi_L(\ell) = \pi_R(r)$.
> 1. **Fiberwise cardinality formula:** for finite sets $L, R, K$, the cardinality of the coupled whole equals
> $$|L \times_K R| = \sum_{k \in K} |\pi_L^{-1}(k)| \cdot |\pi_R^{-1}(k)|.$$
> In particular, for $|K|=2$ and balanced readings on 4-element cells ($|\pi_L^{-1}(k)| = |\pi_R^{-1}(k)| = 2$), we have $|L \times_K R| = 2 \cdot (2 \cdot 2) = \mathbf{8}$ versus $|L \times R| = 16$.
> 2. **Universal property of a compatible step:** suppose maps $T_L : L \to L$, $T_R : R \to R$, and a seam evolution $\tau : K \to K$ satisfy the compatibility equations
> $$\pi_L \circ T_L = \tau \circ \pi_L, \qquad \pi_R \circ T_R = \tau \circ \pi_R.$$
> Then there exists a **unique** map $T_L \times_\tau T_R : L \times_K R \to L \times_K R$ such that $p_L \circ (T_L \times_\tau T_R) = T_L \circ p_L$ and $p_R \circ (T_L \times_\tau T_R) = T_R \circ p_R$; it is given by $(T_L \times_\tau T_R)(\ell, r) = (T_L(\ell), T_R(r))$ and satisfies $\pi_K \circ (T_L \times_\tau T_R) = \tau \circ \pi_K$ (in particular, it is a morphism strictly over $K$ in $\mathbf{FinSet}/K$ if and only if $\tau = \mathrm{id}_K$ on the image of $\pi_K$).
> 3. **Seam rupture under an incompatible step:** if for some pair $(\ell_0, r_0) \in L \times_K R$ one has $\pi_L(T_L(\ell_0)) \neq \pi_R(T_R(r_0))$, then $(T_L(\ell_0), T_R(r_0)) \notin L \times_K R$.

*Proof.* The fiber $\pi_K^{-1}(k)$ equals $\pi_L^{-1}(k) \times \pi_R^{-1}(k)$, so summing over $k \in K$ yields item (1). In item (2), when $\pi_L(\ell)=\pi_R(r)$ we have $\pi_L(T_L(\ell)) = \tau(\pi_L(\ell)) = \tau(\pi_R(r)) = \pi_R(T_R(r))$, so $(T_L(\ell), T_R(r)) \in L \times_K R$, and uniqueness follows because $p_L$ and $p_R$ separate points of $L \times_K R \subseteq L \times R$. Item (3) follows directly from the definition of $L \times_K R$. $\square$

---

## §I.1.5. Structural Packaging of an Ensemble, Three Distinct "Negations," and Belnap's Evidence Lattice Versus Four Zeros

Completing the foundation of Chapter I.1, let us assemble four conceptual tools that operate across all subsequent tiers of the book.

### 1. Operator of Structural Packaging of an Ensemble into a Next-Step Unit

When a non-empty candidate ensemble $E \subseteq U$ ($E \in \mathcal{P}^+(U) = \mathcal{P}(U) \setminus \{\varnothing\}$) is singled out inside an ambient carrier $U$ by a protocol $\Pi$, and at the next step must be handled as a single addressable unit without losing its internal composition, we use the typed pair of **packaging and unpacking**:
$$i_{\mathrm{str},\Pi} : \mathcal{P}^+(U) \longrightarrow \mathrm{Unit}_\Pi(U), \qquad \mathcal{U}_\Pi : \mathrm{Unit}_\Pi(U) \longrightarrow \mathcal{P}^+(U), \qquad \mathcal{U}_\Pi\bigl(i_{\mathrm{str},\Pi}[E]\bigr) = E.$$
Four strict safeguards govern this pair:
- **Lower bound on address cost and distinction between $\mathcal{P}^+(U)$ and $\mathcal{P}(U)$:** the existence of a left inverse $\mathcal{U}_\Pi(i_{\mathrm{str},\Pi}[E]) = E$ on a family $\mathcal{E} \subseteq \mathcal{P}^+(U)$ of $N$ distinct unpackable assemblies implies injectivity of $i_{\mathrm{str},\Pi}|_{\mathcal{E}}$, and by the pigeonhole principle $|\mathrm{Unit}_\Pi(U)| \ge N$. For the domain of **non-empty** ensembles $\mathcal{P}^+(S_4)$ there are exactly $|\mathcal{P}^+(S_4)| = 2^4 - 1 = \mathbf{15}$ elements, so in a fixed-length binary code (or for the maximum word length in a self-delimiting/prefix binary code; under variable length with an external free reading boundary, the cost depends on the delimiter convention) their autonomous distinction requires at least $\lceil \log_2 15 \rceil = \mathbf{4}$ address bits. To include the sixteenth—empty—subset $\varnothing \notin \mathcal{P}^+(S_4)$, the domain of the operator and decoder must be explicitly extended to a full pair $i_{\mathrm{full},\Pi} : \mathcal{P}(U) \to \mathrm{Unit}_{\mathrm{full},\Pi}(U)$ with $\mathcal{U}_{\mathrm{full},\Pi}(i_{\mathrm{full},\Pi}[E]) = E$ across all $|\mathcal{P}(S_4)| = \mathbf{16}$ subsets ($\lceil \log_2 16 \rceil = 4$ bits; assigning a single label to distinct assemblies without an external dictionary of capacity $\ge N$ erases $N - 1$ distinctions, while the algorithmic access cost is analyzed in Chapters `I.4` and `I.9`).
- $i_{\mathrm{str},\Pi}[E]$ retains the unpacking route $\mathcal{U}_\Pi$ rather than collapsing the ensemble into a structureless point.
- The notation $i_{\mathrm{str},\Pi}$ **is not the complex imaginary unit** $i \in \mathbb{C}$ ($i^2 = -1$): Chapter `I.1` contains neither the field $\mathbb{C}$ nor multiplication by $-1$.
- **Typed packaging of a syntax tree versus scalar evaluation:** for ordered syntax trees over an operation signature $\Sigma$, a **separate typed tree-packaging operator** $i_{\mathrm{tree}} : \mathrm{Tree}_\Sigma \to \mathrm{Unit}_{\mathrm{tree}}$ with left inverse $\mathcal{U}_{\mathrm{tree}}\bigl(i_{\mathrm{tree}}[\tau]\bigr) = \tau$ is introduced (trees are not plugged directly into the subset domain $\mathcal{P}^+(U)$ of $i_{\mathrm{str},\Pi}$). Then the trees $E_+ = \mathrm{Add}(1,2,3)$ and $E_\times = \mathrm{Mul}(1,2,3)$ remain strictly distinct as packaged structural assemblies ($i_{\mathrm{tree}}[E_+] \neq i_{\mathrm{tree}}[E_\times]$), even though the evaluation homomorphism $\mathrm{eval} : \mathrm{Tree}_\Sigma \to \mathbb{Z}_{>0}$ maps both trees to the same number $1 + 2 + 3 = 6 = 1 \cdot 2 \cdot 3$.

Inside an ensemble $E \subseteq U$, fixing an answer $q(x)=b$ to a partial binary question with passport $\mathfrak{q} \in \mathcal{Q}$ separates **four** disjoint parts of the carrier: the **active fiber** $E \cap F_q(b)$, the **internal shadow of the opposite binary answer** $(E \cap \mathrm{Dom}(q)) \setminus F_q(b)$ (which coincides with the full difference $E \setminus F_q(b)$ if and only if $E \subseteq \mathrm{Dom}(q)$), the **rejection domain of the question inside the ensemble** $E \setminus \mathrm{Dom}(q)$ (returning marker $\bot_q$), and the **external complement of the ensemble** $U \setminus E$, whereas the passport $\mathfrak{q}$ itself belongs to the space of questions $\mathcal{Q}$, not to the state set $U$.

### 2. Three Strictly Distinct "Negations" at the Level of Sets, States, and Weights, and Behavior of the Pullback $T^*$

At the level of the book's exact mathematical model, three non-coinciding operations are distinguished:
1. **Set-theoretic subset complement** $\neg_X A = X \setminus A$ in the Boolean algebra $\mathcal{P}(X)$, where always $A \cap \neg_X A = \varnothing$ and $A \cup \neg_X A = X$.
2. **State-carrier involution** $\sigma : X \to X$ ($\sigma^2 = \mathrm{id}_X$), lifted via the direct image $\sigma_*(A) = \{\sigma(x) \mid x \in A\}$. On $S_4$ with $\sigma(x,c)=(1\oplus x, 1\oplus c)$, for the fiber $O_0 = \{(0,0),(1,1)\}$ we have $\sigma_*(O_0) = O_0 \neq O_1 = S_4 \setminus O_0$: the involution permutes points *inside* $O_0$, whereas complementation sends $O_0$ *outside* into $O_1$.
3. **Additive sign inversion** $v \mapsto -v$ in a module of weights—an operation that appears only in Chapter `I.5`.

Furthermore, for any total transition map $T : X \to X$, taking the preimage $T^*(A) = T^{-1}(A)$ commutes with complementation ($T^*(X \setminus A) = X \setminus T^*(A)$), and for a partial map $T : \mathrm{Dom}(T) \to X$ one has $T^*(X \setminus A) = \mathrm{Dom}(T) \setminus T^{-1}(A)$, whereas the direct image $T_*(A)$ does not commute with complementation.

### 3. Belnap's Four-Valued Evidence Lattice $\mathcal{F}_4$ Versus Four Operational Zeros

Suppose two separate channels of evidence operate in a protocol regarding a proposition $P$: a channel of positive confirmation ($e_+ \in \{0, 1\}$) and a channel of refutation ($e_- \in \{0, 1\}$). They form the **four-element space of Belnap–Dunn epistemic statuses** $\mathcal{F}_4 = \{0, 1\}^2$: $\bot = (0, 0)$ (no information), $\mathbf{0} = (0, 1)$ (pure refutation), $\mathbf{1} = (1, 0)$ (pure confirmation), $\top = (1, 1)$ (conflicting evidence), equipped with the truth order $\le_t$ (with involution $\neg_t(e_+, e_-) = (e_-, e_+)$ fixing both $\bot$ and $\top$) and the information/knowledge order $\le_k$ ($\bot \le_k \mathbf{0}, \mathbf{1} \le_k \top$).

**Counterexample I.1.2 (Collision of scalar weight difference and sufficiency of a pair of support indicators for $\mathcal{F}_4$).** Within Chapter `I.1` itself, the four-valued lattice $\mathcal{F}_4 = \{0, 1\}^2$ is constructed purely combinatorially as a pair of binary support indicators across two channels; if (looking ahead to numerical counters and signed balance in Chapter `I.5`) the channels accumulate multiplicities $(w_+, w_-) \in \mathbb{Z}_{\ge 0}^2$ while the status in $\mathcal{F}_4$ is given by the indicator pair $(\min(w_+,1),\, \min(w_-,1)) \in \{0,1\}^2$, any attempt to compress $(w_+, w_-)$ into a single scalar difference $\Delta w = w_+ - w_- \in \mathbb{Z}$ produces two collisions:
1. Silence $(0, 0) \mapsto \bot$ and symmetric conflict $(1, 1) \mapsto \top$ receive the exact same balance $\Delta w(0,0) = 0 = \Delta w(1,1)$.
2. Asymmetric conflict $(2, 1) \mapsto \top$ ($w_- = 1 > 0$) receives the same difference $\Delta w(2,1) = +1$ as pure confirmation $(1, 0) \mapsto \mathbf{1}$.  
Consequently, a scalar difference loses the presence of two kinds of support: for the static question of whether evidence of each sign is present at all (presence threshold `1` without evidence retraction), it is necessary and sufficient to store **two binary indicators** $(\min(w_+,1),\, \min(w_-,1)) \in \{0,1\}^2$; if, however, the protocol includes threshold accumulation with threshold $> 1$ or the operation of **unit-by-unit retraction (deletion) of a single piece of evidence**, then tracking multiplicities becomes necessary already at threshold `1`, because after deleting one piece of evidence the multiset $\{a\}$ becomes $\varnothing$ (status $0$), whereas $\{a, a\}$ becomes $\{a\}$ (status $1$).

Strict typing forbids conflating the foursome $\mathcal{F}_4$ with the **four operational kinds of "zero and emptiness"**: (1) scale zero $0 \in V_q$; (2) the zero fiber $F_q(0) = q^{-1}(0) \subseteq X$; (3) the empty protocol $w = \varepsilon \in \Pi$; (4) the inapplicability marker $\bot_q \notin V_q$ when $x \notin \mathrm{Dom}(q)$.

Finally, let us draw the exact boundary leading into Chapter `I.2`: on the 4-element carrier $S_4$ there are `4` states, but $2^4 = \mathbf{16}$ labeled Boolean predicates $S_4 \to \{0,1\}$: `2` constant predicates ($\varnothing, S_4$), `8` odd predicates of cardinality `1` and `3`, and exactly $\binom{4}{2} = \mathbf{6}$ **balanced labeled questions** of type `2 + 2`, which upon identifying opposite labelings $\{q, 1\oplus q\}$ form exactly **`3` unlabeled two-class partitions** of type `2 + 2`—the partitions of the questions $q_x$, $q_c$, and $\beta = q_x \oplus q_c$.

---

## §I.1.6. Categorical Anchoring of the Chapter

### Block K-I.1.0. Factorization of a Single Question and Totalization of Rejection in $\mathbf{FinSet}$

- **Category:** $\mathbf{FinSet}$ (finite sets and total maps; for a partial question $q : \mathrm{Dom}(q) \to V_q$, its total completion $q_\bot : X \to V_q \sqcup \{\bot_q\}$ is likewise constructed as a morphism in $\mathbf{FinSet}$, whereas passing to the category of pointed finite sets $\mathbf{FinSet}_*$ requires separately adjoining an external basepoint $X_* = X \sqcup \{*\}$ with $q_\bot(*) = \bot_q$, since the carrier $X$ itself has no distinguished point).
- **Objects:** candidate carrier $X$, label scale $V_q$, and quotient image $\mathrm{im}(q) = q(X) \cong X / \mathrm{Eq}(q)$.
- **Morphisms:** canonical epimorphic projection $\pi_q : X \twoheadrightarrow X / \mathrm{Eq}(q)$ and monomorphic inclusion of realized labels $\iota_q : X / \mathrm{Eq}(q) \hookrightarrow V_q$, yielding the `Epi–Mono` factorization $q = \iota_q \circ \pi_q$.
- **Construction / universal property:** the quotient $X / \mathrm{Eq}(q)$ is the coequalizer of the kernel-pair projections $\mathrm{Eq}(q) \rightrightarrows X$: any map $f : X \to Z$ constant on the fibers of $q$ factors uniquely through $\pi_q$ ($f = \bar{f} \circ \pi_q$).
- **What is preserved:** the partition of the carrier $X$ into indistinguishability classes is invariant under any scale automorphism $\tau \in \mathrm{Aut}(V_q)$, since $\pi_{\tau \circ q} = \pi_q$.
- **Where it breaks / what the construction does NOT claim:** the `Epi–Mono` factorization endows $V_q$ with neither a zero nor a group law, and does not guarantee surjectivity of $q$ onto the entire scale $V_q$ when $\iota_q$ is a proper inclusion ($V_q \setminus \mathrm{im}(q) \neq \varnothing$).

### Block K-I.1.1. Kernel Pair and Intersection of Kernels of Two Questions in $\mathbf{FinSet}$

- **Category:** $\mathbf{FinSet}$ (finite sets and total maps).
- **Objects:** state carrier $X$, scale $V$, and kernel relation $\mathrm{Eq}(q) = X \times_V X = \{(x,y)\in X^2 \mid q(x)=q(y)\}$.
- **Morphisms:** projections $p_1, p_2 : X \times_V X \rightrightarrows X$, canonical epimorphism $\pi_q : X \twoheadrightarrow X/\mathrm{Eq}(q)$, and monomorphism $\iota_q : X/\mathrm{Eq}(q) \hookrightarrow V$ with $q = \iota_q \circ \pi_q$.
- **Construction / universal property:** $\mathrm{Eq}(q)$ is the pullback (`Kernel Pair`) of the morphism $q$ along itself, while $\pi_q : X \twoheadrightarrow X/\mathrm{Eq}(q)$ is the coequalizer of $(p_1, p_2)$; for a pair of questions $(q_1, q_2)$, the joint kernel $\mathrm{Eq}(q_{12})$ is the subobject intersection $\mathrm{Eq}(q_1) \cap \mathrm{Eq}(q_2) \hookrightarrow X \times X$.
- **What is preserved:** the cardinality $|X/\mathrm{Eq}(q_{12})|$ and the universal factorization property are invariant under any target-scale automorphisms $\tau_1 \in \mathrm{Aut}(V_1), \tau_2 \in \mathrm{Aut}(V_2)$.
- **Where it breaks / what the construction does NOT claim:** in the category of commutative monoids $\mathbf{CMon}$, the preimage of the neutral element $h^{-1}(0) = X \times_Y \{0\}$ **does not recover** the kernel pair $X \times_Y X$ (`Counterexample I.1.0b`).

### Block K-I.1.2. Coupled Whole with a Seam (`Pullback`) in $\mathbf{FinSet}/K$ and Equivariant Base Shifts in $\mathbf{FinSet}^{\to}$

- **Category:** $\mathbf{FinSet}/K$ (slice category of finite sets strictly over a fixed seam base $K$ for steps with $\tau = \mathrm{id}_K$) and arrow category $\mathbf{FinSet}^{\to}$ for equivariant transitions with nontrivial base evolution $\tau : K \to K$.
- **Objects:** local carriers over the seam $(\pi_L : L \to K)$ and $(\pi_R : R \to K)$.
- **Morphisms:** in $\mathbf{FinSet}/K$, maps $f : L \to L'$ satisfying the strict triangle $\pi'_L \circ f = \pi_L$ ($\tau = \mathrm{id}_K$); in $\mathbf{FinSet}^{\to}$, commutative squares $(T_L, \tau)$ satisfying $\pi'_L \circ T_L = \tau \circ \pi_L$.
- **Construction / universal property:** the coupled whole $L \times_K R$ is the limit of the cospan $L \xrightarrow{\pi_L} K \xleftarrow{\pi_R} R$ (`Pullback` in $\mathbf{FinSet}$, coinciding with the binary product in $\mathbf{FinSet}/K$): any pair of morphisms $g_L : Z \to L,\, g_R : Z \to R$ satisfying $\pi_L \circ g_L = \pi_R \circ g_R$ factors uniquely through $L \times_K R$.
- **What is preserved:** functoriality of the compatible step $(T_L \times_\tau T_R) \circ (S_L \times_\sigma S_R) = (T_L \circ S_L) \times_{\tau \circ \sigma} (T_R \circ S_R)$ in $\mathbf{FinSet}^{\to}$ (and inside $\mathbf{FinSet}/K$ when $\tau = \sigma = \mathrm{id}_K$) and fiberwise multiplicativity of cardinalities over each $k \in K$.
- **Where it breaks / what the construction does NOT claim:** (i) the limit of the cospan $L \times_K R$ (`8` points for $S_4 \twoheadrightarrow \mathbb{F}_2 \twoheadleftarrow S_4$) must not be confused with the free product $L \times R$ (`16` points), nor with the colimit of the same cospan of surjections (which equals the `2`-point base $K$ itself), nor with the dual pushout of the span of inclusions $S_4 \hookleftarrow \mathbb{F}_2 \hookrightarrow S_4$ (`6` points); (ii) a morphism with $\tau \neq \mathrm{id}_K$ on the active seam image $\mathrm{im}(\pi_K) \subseteq K$ preserves the seam fibration in $\mathbf{FinSet}^{\to}$ but ceases to be a morphism strictly over $K$ in $\mathbf{FinSet}/K$ (whereas values of $\tau$ outside $\mathrm{im}(\pi_K)$ do not affect the induced step on $L \times_K R$); (iii) if local steps $(T_L, T_R)$ violate compatibility on some coupled pair $(\ell_0, r_0) \in L \times_K R$, i.e., $\pi_L(T_L(\ell_0)) \neq \pi_R(T_R(r_0))$, they rupture the seam and do not define a map $L \times_K R \to L \times_K R$.

---

### Historical-Philosophical Note: The Conditioned Manifest in Sāṃkhya and the Superadded Conditioning Factor

1. **Motif of the classical source.** In kārikās `SK 10–11`, classical Sāṃkhya lists the marks distinguishing every specific manifest distinction (*vyakta*) from the unmanifest ground (*avyakta*) and from the witness position (*Puruṣa*, `SK 19–20`): the manifest is conditioned by a cause (*hetumat*), bounded in domain (*avyāpi*), active/mobile (*sakriyam*), plural (*anekam*), supported by a carrier (*āśritam*), marked by a distinguishing characteristic (*liṅgam*), and composite (*sāvayavam*). In the neighboring tradition of Advaita Vedānta (which historically must not be conflated with dualistic Sāṃkhya), a related intuition of contextual conditioning is expressed by the concept of *upādhi*—an extrinsic limiting adjunct: a transparent crystal appears colored next to a hibiscus flower until the second participant in the scene is accounted for.
2. **Rigorous articulation in DOT.** In the present chapter this observation is matched with an exact finite diagram: the answer of the comparison window $\beta(x,c) = x \oplus c$ is born at the encounter of specimen state $x$ and reference context $c$, does not belong to an isolated $x$, and admits unique recovery of the full pair via either of the two symmetric decoders $d_c(\beta,c) = (\beta \oplus c, c)$ and $d_x(\beta,x) = (x, \beta \oplus x)$.
3. **Boundary of the comparison.** The observer's position $\mathcal{O} \notin X$ is a role condition of the contract $\Gamma$, **not** a "fifth element" adjoined to the four-element carrier $S_4$; and neither the four non-empty intersection criterion of Theorem `I.1.1` nor the universal property of the fiber product $L \times_K R$ in Theorem `I.1.3` is deduced from the texts of Sāṃkhya or Advaita.

---

### Transition to Chapter `I.2`

We have fixed the operational contract $\Gamma$, separated the observer's position ($\mathcal{O} \notin X$) from a single flash of the window, established the exact criterion for the birth of the four-state polar cell $S_4$, verified both decoders of the comparison question $\beta = x \oplus c$, and derived the law of coupling two systems along a shared seam $L \times_K R$.

We continue these results in the chapters ahead:
- in the next **Chapter `I.2`**, we incorporate partial transitions with blocking, multivalued relations, and the triangle of switching two-element slices on $S_4$, in order to determine how questions and all $2^4 = 16$ predicates pull back against an action and where nontrivial holonomy arises at the junction of regimes;
- and in **Chapter `I.3`**, we unfold single-step transfer into a multi-step tower and ask how many distinctions of the present memory must retain so as not to lose a single future answer under any admissible sequence of steps.

---

### Verifiability Passport of Chapter `I.1` (`Book I v3.3`)

- **Canonical book node:** `N01` (operational contract $\Gamma$, primacy of two-class partition, conditions $(Z_D, Z_C, Z_F)$ and $(C_{\mathrm{div}}, C_{\mathrm{type}}, C_{\mathrm{step}})$ with the $\mathrm{Eq}(q)$ fiber-crossing criterion, polar cell $S_4$, comparison question $\beta = x \oplus c$, background of agreement $O_0$ vs. figure of discrepancy $O_1$ and both decoders $d_c, d_x$, fibered seam $L \times_K R$, address cost $i_{\mathrm{str},\Pi}$, and Belnap lattice $\mathcal{F}_4$).
- **Exact `Julia 1.12.6` verifications (single-threaded mode, no `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gates `GATE-I01-A` (primacy of $\mathrm{Eq}(q)$, countermodels for $(Z_D, Z_C, Z_F)$ on cardinalities `2` and `3`, saturation homomorphism on the monoid $(\{0,1,2\},\max,0)$ with $h^{-1}(0)=\{0\}$ and $|\mathrm{Eq}(h)|=5$) and `GATE-I01-B` (criterion $|X/\mathrm{Eq}(q_{12})|=4$ on cardinalities `3, 4, 5`, both decoders $d_c, d_x$, fiber product $|S_4 \times_{\mathbb{F}_2} S_4|=8$, symmetry groups `48 / 16 / 8 / 4`, and scalar-difference collision on $\mathcal{F}_4$).
- **Specification index `Lean 4` (`status: planned`, full cards in Appendix `VP`):** `TNR.BookI.E0.partition_relabel`, `TNR.BookI.I01.joint_image_four`, `TNR.BookI.I01.three_state_counterexample`, `TNR.BookI.I01.seam_pullback_step`, `TNR.BookI.I01.relabel_kernel`.
- **Complete 8-point figure passports `Figs. I.1.1–I.1.2` and academic bibliography:** placed in [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
