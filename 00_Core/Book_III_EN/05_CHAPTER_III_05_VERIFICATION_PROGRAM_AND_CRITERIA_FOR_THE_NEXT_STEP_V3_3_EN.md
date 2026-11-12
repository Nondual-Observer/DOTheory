# Chapter III.5. Verification Program, Criteria for the Next Step, and General Compendium of the Three Books

In this work, the theory is proposed to be evaluated by two criteria:
1. how transparently and without hidden assumptions its **internal deductive chain** is constructed (whether an independent mathematician can verify every step without appealing to the author's authority);
2. how strictly its **rules for accepting and rejecting new domain bridges** are formulated (whether the theory itself stops false analogies, post-hoc fitting after inspecting tables, and answer leakage from an oracle).

The concluding chapter of the monograph consolidates these rules into a formal, verifiable protocol. In `§III.5.1` we formulate the normative acceptance protocol for a morphism certificate and prove **Theorem `III.5.1`** on the sufficiency of an exhibited morphism and the decidability of observable equivalence on the reachable product $X \times M$, together with **Lemma `III.5.1`** (the discrete Grönwall estimate for approximate dynamical bridges). In `§III.5.2` we write out the matrix of admissible and prohibited epistemic transitions between levels `L1–L4`. Finally, in `§III.5.3` we survey all **`24` constituent parts of the trilogy (`Introduction + 9 chapters of Book I + 9 chapters of Book II + 5 chapters of Book III`, i.e. `23` numbered chapters and the `Introduction`)**, showing how every invariant of the Observer returns and operates within the bridges of Volume III.

---

## §III.5.1. Normative Certificate Acceptance Protocol, Theorem on the Sufficiency of an Exhibited Morphism, and the Grönwall Estimate

To separate the mathematical statement about finite automata and transition systems from the organizational rule governing the checking algorithm, let us first fix the normative definition of an acceptance certificate:

### Definition III.5.1 (Certificate of a Finite Morphism and Normative Checker Protocol)

Let $S_X = (X, \Sigma, x_0, \{\delta_a^X\}_{a \in \Sigma}, q_X : X \to Y)$ and $S_M = (M, \Sigma, m_0, \{\delta_a^M\}_{a \in \Sigma}, q_M : M \to Y)$ be two finite deterministic transition systems sharing a common input action alphabet $\Sigma$ and output response scale $Y$.
1. A **certificate of homomorphic compression (or transfer)** from $S_X$ to $S_M$ is an explicitly exhibited table of a map $\phi : X \to M$ for which three finite conditions are verified:
   - *(preservation of the initial state)* $\phi(x_0) = m_0$;
   - *(intertwining of all transitions)* $\phi(\delta_a^X(x)) = \delta_a^M(\phi(x))$ for all $(x, a) \in X \times \Sigma$;
   - *(preservation of observable responses)* $q_M(\phi(x)) = q_X(x)$ for all $x \in X$.
2. **Normative checker rule (`Checker Protocol`):** an automated verifier is required to reject any submitted certificate $\phi$ if the intertwining condition is violated for at least one pair $(x,a) \in X \times \Sigma$, if output preservation $q_M(\phi(x)) = q_X(x)$ is violated for at least one $x \in X$, or if the checksum in the serialized certificate file is corrupted or the transition tables of the source systems have been altered.

Let us now relate the existence of a morphism $\phi : X \to M$ to the coincidence of all external input–output protocols on words $w \in \Sigma^*$:

### Theorem III.5.1 (Sufficiency of an Exhibited Morphism and Classical Decidability of Equivalence via Traversal of the Reachable Product $X \times M$ (Moore, Hopcroft–Karp))

*Classical foundation.* Equivalence testing and minimization of finite deterministic automata (E. F. Moore, 1956; J. E. Hopcroft and R. M. Karp, 1971). *Contribution of this book:* Contrasting $O(|X|\cdot|\Sigma|)$ verification of an exhibited certificate $\phi : X \to M$, a counterexample to necessity without minimality of $M$, and $X \times M$ traversal.

*Let $S_X$ and $S_M$ be finite deterministic transition systems with $|X| < \infty$, $|M| < \infty$, $|\Sigma| < \infty$, and let $\mathrm{Bhv}_X, \mathrm{Bhv}_M : \Sigma^* \to Y$, $\mathrm{Bhv}_X(w) = q_X(\delta_w^X(x_0))$, $\mathrm{Bhv}_M(w) = q_M(\delta_w^M(m_0))$ be their external input–output word behaviors. Then:*

1. **Sufficiency of an exhibited morphism in time $O(|X|\cdot|\Sigma|)$:** *If a certificate $\phi : X \to M$ is exhibited that satisfies the three conditions of `Definition III.5.1(1)` (verifiable in $|X|\cdot|\Sigma| + |X| + 1$ elementary table lookups), then for every word $w \in \Sigma^*$ of any length $|w| \ge 0$ one has $\phi(\delta_w^X(x_0)) = \delta_w^M(m_0)$, and therefore the external behaviors of the systems coincide identically on the entire infinite word tree $\Sigma^*$:*
   $$
   \mathrm{Bhv}_X(w) = \mathrm{Bhv}_M(w) \qquad \forall\,w \in \Sigma^*.
   $$
2. **Necessity of a morphism only after quotienting by Nerode indistinguishability:** *The converse statement ("$\mathrm{Bhv}_X = \mathrm{Bhv}_M$ implies the existence of a morphism $\phi : X \to M$") is in general **false** for an arbitrary target system $S_M$ with redundant or split states (it suffices to take $S_X$ minimal and in $S_M$ duplicate the initial state into two equivalent states visited alternately on even and odd steps; then no map can send the single state $x_0$ to two distinct states of $M$). However, if the target system $S_M = M_{\min}$ coincides with the minimal Moore–Nerode quotient automaton (`Theorem I.3.1`) and $X$ is restricted to the core reachable from $x_0$, then the equality $\mathrm{Bhv}_X = \mathrm{Bhv}_{M_{\min}}$ is **necessary and sufficient** for the existence of a unique surjective morphism $\phi : X \twoheadrightarrow M_{\min}$.*
3. **Decidability of behavioral equivalence on the reachable subset of the product $X \times M$:** *For any two finite systems $S_X$ and $S_M$ (even when no direct morphism $\phi : X \to M$ exists), the identity $\mathrm{Bhv}_X = \mathrm{Bhv}_M$ is decidable in time $O(|X|\cdot|M|\cdot|\Sigma|)$ by breadth-first traversal of the reachable subset $\mathcal{R} \subseteq X \times M$ from the initial pair $(x_0, m_0)$ under synchronous transitions $\delta_a^{X \times M}(x,m) = (\delta_a^X(x), \delta_a^M(m))$: the equality $\mathrm{Bhv}_X = \mathrm{Bhv}_M$ holds if and only if $q_X(x) = q_M(m)$ throughout the reachable set $\mathcal{R}$ ($|\mathcal{R}| \le |X|\cdot|M|$), and in the event of a discrepancy the shortest distinguishing word $w_{\mathrm{diff}} \in \Sigma^*$ has length $|w_{\mathrm{diff}}| \le |\mathcal{R}| - 1 \le |X|\cdot|M| - 1$ (and when comparing two states within a single system or in the disjoint union $X \sqcup M$, length $\le |X| + |M| - 1$ by Moore's bound).*

**Proof (analytical).**
1. Induction on the length of the word $w \in \Sigma^*$. Base case $w = \varepsilon$: $\phi(\delta_\varepsilon^X(x_0)) = \phi(x_0) = m_0 = \delta_\varepsilon^M(m_0)$. Inductive step for $w = u a$ ($a \in \Sigma$):
   $$
   \phi(\delta_{ua}^X(x_0)) = \phi\bigl(\delta_a^X(\delta_u^X(x_0))\bigr) = \delta_a^M\bigl(\phi(\delta_u^X(x_0))\bigr) = \delta_a^M(\delta_u^M(m_0)) = \delta_{ua}^M(m_0).
   $$
   Applying $q_M$ and the condition $q_M \circ \phi = q_X$ gives $\mathrm{Bhv}_M(w) = q_M(\delta_w^M(m_0)) = q_M(\phi(\delta_w^X(x_0))) = q_X(\delta_w^X(x_0)) = \mathrm{Bhv}_X(w)$.
2. Let $X = \{x_0\}$ with transition $\delta_a^X(x_0) = x_0$ and output $q_X(x_0) = 1$, and let $M = \{m_0, m_1\}$ with transitions $\delta_a^M(m_0) = m_1,\; \delta_a^M(m_1) = m_0$ and outputs $q_M(m_0) = q_M(m_1) = 1$. Then $\mathrm{Bhv}_X(a^k) = 1 = \mathrm{Bhv}_M(a^k)$ for all $k \ge 0$, yet no map $\phi : \{x_0\} \to \{m_0, m_1\}$ can satisfy both $\phi(x_0) = m_0$ and $\phi(\delta_a^X(x_0)) = \phi(x_0) = \delta_a^M(m_0) = m_1 \ne m_0$. Conversely, if $M = M_{\min} = X / {\sim_{\mathrm{Nerode}}}$ (`Chapter I.3`), then the canonical projection $x \mapsto [x]_{\sim}$ is well-defined and forms the unique surjective morphism sought.
3. By definition of the synchronous transition in $X \times M$, for every word $w \in \Sigma^*$ the pair $(\delta_w^X(x_0), \delta_w^M(m_0))$ coincides with $\delta_w^{X \times M}(x_0, m_0) \in \mathcal{R}$. Consequently, the existence of a word $w$ with $\mathrm{Bhv}_X(w) \ne \mathrm{Bhv}_M(w)$ is equivalent to the existence of a reachable vertex $(x,m) \in \mathcal{R}$ with $q_X(x) \ne q_M(m)$, and a shortest path in a finite graph on $|\mathcal{R}|$ vertices contains no simple cycles and has length $\le |\mathcal{R}| - 1$. $\blacksquare$

When a domain bridge connects an exact discrete dynamical law $x_{t+1} = F(x_t)$ with its approximate model $\hat{x}_{t+1} = \widehat{F}(\hat{x}_t)$ under a per-step discrepancy $\|F(\hat{x}_t) - \widehat{F}(\hat{x}_t)\| \le \varepsilon$, the horizon of reliable prediction is governed by the classical discrete Grönwall lemma:

### Lemma III.5.1 (Classical Discrete Grönwall Lemma for an Approximate Dynamical Bridge)

*Classical foundation.* Discrete Grönwall lemma for the linear recurrent inequality $e_{t+1} \le L e_t + \varepsilon$. *Contribution of this book:* Explicit trajectory-divergence budget and logarithmic prediction horizon for approximate dynamical bridges across all three regimes ($L < 1, L = 1, L > 1$).

*Let the map $F : \mathbb{R}^d \to \mathbb{R}^d$ be Lipschitz with constant $L > 0$ ($\|F(x) - F(y)\| \le L\|x - y\|$), and let the approximate step operator $\widehat{F}$ have uniform per-step error $\sup_z \|F(z) - \widehat{F}(z)\| \le \varepsilon$. Then the trajectory error $e_t = \|x_t - \hat{x}_t\|$ at step $t \ge 0$ satisfies the bound:*
$$
\|x_t - \hat{x}_t\| \;\le\; \begin{cases} L^t \|x_0 - \hat{x}_0\| + \varepsilon\,\dfrac{L^t - 1}{L - 1}, & \text{if } L \ne 1, \\[8pt] \|x_0 - \hat{x}_0\| + t\,\varepsilon, & \text{if } L = 1. \end{cases}
$$
*In particular, in the contractive regime ($0 < L < 1$) the error remains uniformly bounded over an infinite horizon by $\frac{\varepsilon}{1 - L}$ as $t \to \infty$, in the neutral regime ($L = 1$) it grows at most linearly as $t\varepsilon$, and in the expansive regime ($L > 1$) the guaranteed accuracy horizon $\|x_t - \hat{x}_t\| \le \Delta_{\max}$ for $x_0 = \hat{x}_0$ is bounded by the logarithmic time $t \le \frac{\ln(1 + (L-1)\Delta_{\max}/\varepsilon)}{\ln L}$.*

**Proof (analytical).** By the triangle inequality and the Lipschitz condition, $e_{t+1} = \|F(x_t) - \widehat{F}(\hat{x}_t)\| \le \|F(x_t) - F(\hat{x}_t)\| + \|F(\hat{x}_t) - \widehat{F}(\hat{x}_t)\| \le L e_t + \varepsilon$. Inductively unrolling the linear recurrent inequality $e_{t} \le L^t e_0 + \varepsilon \sum_{k=0}^{t-1} L^k$ yields both formulas for $L \ne 1$ and $L = 1$. $\blacksquare$

---

## §III.5.2. Matrix of Admissible and Prohibited Transitions Between Levels `L1–L4` and Criteria for the Next Step

In `Chapter III.1` (`§III.1.4`) we fixed a four-level epistemic hierarchy of statements:
- **`L1` (Mathematical core):** theorems, lemmas, and finite counterexamples true within the formal definitions of Books I–III (proved status);
- **`L2` (Direct fact of a primary source or table):** exact counts over immutable tables and critical editions of texts (tables of directed graphs, sūtras and kārikās of `SK, YS, MK, BSB, Aṣṭādhyāyī`) (documented primary fact);
- **`L3` (Domain model and procedural bridge):** two-arrow models $(\iota, \mathcal{O}_\pi)$ with an explicitly written eight-row passport, surrogate control, and falsification condition (testable model);
- **`L4` (Interpretive dictionary `REG-INTERP`):** heuristic comparisons, philosophical parallels, and working hypotheses (interpretive status).

### Table III.5.1. Rules of Transitions Between Levels `L1–L4` in the Verification Program

| Arrow Direction | Transition Status | Condition of Admissibility or Reason for Prohibition |
| :--- | :---: | :--- |
| **`L1` $\to$ `L3`** (applying a core theorem in a domain model) | admissible | Requires exhibiting both arrows $(\iota, \mathcal{O}_\pi)$ and verifying the hypotheses of the theorem on the domain input data. |
| **`L2` $\to$ `L3`** (feeding primary tables into a procedural bridge) | admissible | Requires fixing the split rule prior to fitting (`Row 3` of the passport) and the null surrogate control (`Row 5`). |
| **`L3` $\to$ `L4`** (interpreting a verified bridge in the dictionary) | admissible with downgrade to interpretation | The conclusion must be explicitly marked as an interpretation of level `L4` without reverse transfer back to the core theorem. |
| **`L4` $\to$ `L1`** (passing off a metaphor or dictionary entry as proof of a theorem) | prohibited | Violates the law of independence of the mathematical core from external interpretations (`Chapter III.1, §III.1.4`). |
| **`L3` $\to$ `L1`** (declaring a particular numerical run to be proof of a general theorem) | prohibited | A finite numerical example can provide a counterexample (falsification), but never replaces a universal proof in `L1`. |
| **`L4` $\to$ `L3`** (including an analogy without null control and falsification condition) | prohibited prior to passporting | Transition from `L4` to `L3` is possible only after exhibiting all `8` rows of the passport and passing surrogate control. |

### Three Criteria for the Next Step of Research

Any new extension of the monograph—whether a new domain bridge `DB-06`, a new algorithmic scheme, or a new textual corpus—is admitted into the main compendium only after passing three sequential gates:
1. **Typing and Eight-Row Passport Gate (`Gate 1`):** are the carrier $X$, questions $\mathcal{Q}$, partial actions $\mathcal{A}$ with domains of admissibility $\mathrm{Dom}(T_a)$, both arrows $(\iota, \mathcal{O}_\pi)$, and all `8` rows of the domain bridge passport—including the Observer's position—explicitly exhibited?
2. **Oracle-Free and Surrogate Control Gate (`Gate 2`):** has the absence of answer leakage from the target labelling (`Definition III.4.1`) been verified, and does the claimed property withstand comparison against a permutation or degenerate surrogate control?
3. **Full Cost and Independent Reproducibility Gate (`Gate 3`):** has the full three-component cost budget $(Z_D, Z_C, Z_F)$ been accounted for, and is every finite and matrix calculation reproduced by a single-threaded verifier in exact arithmetic in a single run (for the present chapter, `GATE-III05-01` in `07_verify_full_book_III_v3_3.jl`)?

---

## §III.5.3. Summary Architectural Map of All `24` Parts of the Trilogy (`Introduction` and `23` Chapters of Books I–III) and the Through-Line of the Observer

The monograph consists of **`24` structural parts**—the opening **`Introduction`** and **`23` numbered chapters** (`9` chapters in Book I, `9` chapters in Book II, and `5` chapters in Book III), accompanied by consolidated volume appendices and self-contained single-threaded verifiers.

So that the reader may view the entire construction as a single deductive mechanism, we trace in the summary table below how every invariant of the Observer introduced in the `Introduction` and `Book I` and developed in `Book II` returns and operates in the domain bridges of `Book III`.

### Table III.5.2. Through-Passage of the Observer's Invariants Across All Three Volumes (`24` Parts)

| Observer's Invariant | Introduction in `Book I` (`Introduction + Chapters I.1–I.9`, `10` parts) | Development in `Book II` (`Chapters II.1–II.9`, `9` parts) | Return and Operation in the Domain Bridges of `Book III` (`Chapters III.1–III.5`, `5` parts) |
| :--- | :--- | :--- | :--- |
| **1. Observer's position $\mathcal{O} \notin X$ and operational contract $\Gamma$** | `Introduction`, `Chapter I.1`: distinction between the role specifying the frame of questions and the elements of the frame $X$; the six-tuple $\Gamma$. | `Chapter II.9` (`Theorem II.9.1`): Cantor–Lawvere diagonal theorem on the impossibility of complete internal self-coding of predicates $Y^X$ inside $X$. | `Chapter III.1` (the two arrows $(\iota, \mathcal{O}_\pi)$ and `Row 8` of all passports); `Chapter III.3` (`§III.3.1`: demarcation between the typing condition $\mathcal{O}\notin X$ and Lawvere's diagonal in the bridges of *Sāṃkhya* and *Advaita*). |
| **2. Four-place scene $S_4 = \mathbb{F}_2^2$, partiality $\mathrm{Dom}(T_a)$, and failure marker $\bot$** | `Chapters I.1–I.2`: splitting of the naive pair $a \ne b$ into $S_4 = \{00, 01, 10, 11\}$; separating blockage $x \notin \mathrm{Dom}(T_a)$ from the answer "no"; shadow boundary $\partial_\pi(S)$. | `Chapter II.2`: dyadic refinement tree $D_n$, Stone's theorem, and König's extension lemma; `Chapter II.8`: admissibility barriers in `SOS` certificates. | `Chapter III.2` (side-balance shift $21:19 \to 19:19$ under a change of question domain $\mathrm{Dom}(q)$ on the $40$-vertex registry); `Chapter III.4` (`Theorem III.4.1`: four-place sign table $(\pm 1 \bmod p, \pm 1 \bmod q)$ in cofactor merging `DB-04`). |
| **3. Octahedron $O_6 \cong K_{2,2,2}$ on three axes of opposition** | `Chapters I.2, I.6`: three pairs of mutually exclusive poles $\pi_1, \pi_2, \pi_3$ form $O_6$ ($6$ vertices, $12$ edges, $8$ triangular faces). | `Chapters II.3–II.5`: cellular homology of $O_6$, automorphism group $W(B_3)$ of order $48$, double covers, and the splitting $V_6 = V_+ \oplus V_-$. | `Chapter III.3` (`Lemma III.3.1`: $Q_3 \setminus \{000,111\} \cong O_6$; `Theorem III.3.1(3)`: gluing of two octahedra $O_6(\Lambda_4) \cup O_6(\Lambda_4')$ along $\triangle(ME,MB,EB)$; `Proposition III.3.2`: Pāṇini's $6$ *kāraka* roles on $C_6(1,2) \cong O_6$); `Chapter III.4` (`Lemma III.4.1`: rebuilding the prism $\Pi_6$ into $O_6$). |
| **4. Minimal Moore–Nerode memory $M_{\min}$ and rank of Hankel matrices** | `Chapters I.3, I.8`: quotienting histories by future continuations $\sim_{\mathrm{Nerode}}$, $5$ states of the minimal automaton, and rank of Hankel matrices $H$. | `Chapter II.1`: Ho–Kalman theorem ($\dim M_{\min} = \mathrm{rk}\,\mathcal{H}$), counterexample of observability loss under window truncation, and the Singh–Webber bound. | `Chapter III.2` (full weighted graph and resolvent $\widetilde{P}_\tau$ without threshold edge loss); `Chapter III.4` (`Theorem III.4.1`: cyclomatic rank of the cofactor graph; `Theorem III.4.2`: $\mathfrak{S}_m$ gauge symmetry of HMMs); `Chapter III.5` (`Theorem III.5.1`: morphism certificate on $X \times M$). |
| **5. Full three-component cost $(Z_D, Z_C, Z_F)$ and feedback** | `Chapters I.4–I.5`: discrimination cost $Z_D$, type-consistency cost $Z_C$, and feedback-step cost $Z_F$; irreducibility of each of the three components. | `Chapter II.7`: Cramér–Rao lower bound and information cost; `Chapter II.8`: rational `SOS` stability certificates and Lyapunov functions. | `Chapter III.1` (`Row 6` of all bridge passports); `Chapter III.2` ($100\%$ weight-mass conservation under resolvent filtration) and `Chapter III.5` (`Lemma III.5.1`: discrete Grönwall divergence budget). |
| **6. Checkerboard face splitting $8 = 4 + 4$, parity cocycle $\kappa \in H^1(\mathcal{N}(O_6); \mathbb{F}_2)$, and presheaf $S_w$** | `Chapter I.9` (`Theorems I.9.1–I.9.3a`): $4$ filled and $4$ hollow faces of the octahedron $O_6$, $\dim_{\mathbb{F}_2} H^1(\mathcal{N}(O_6);\mathbb{F}_2) = 3$, absence of a global section $\Gamma(\mathcal{N}(O_6), S_w) = \varnothing$ despite pairwise compatibility on all $12$ edges. | `Chapters II.3, II.6`: Mayer–Vietoris exact sequence, universal coefficient $\mathrm{Ext}^1_{\mathbb{Z}} = 0$, Hoggar's $64$ projective lines, and Kochen–Specker–Mermin contextuality. | `Chapter III.1` (`Proposition III.1.1`: non-recoverability of rank from two diagonal slices); `Chapter III.2` (`Lemma III.2.1`: ungluability of local descriptions $W$, $\sigma$, and $\alpha$); `Chapter III.3` (`Theorem III.3.1(2)`: isometry $\mathcal{F} : C_2(M_5) \to \ker(A_{\mathrm{KG}}-I_{10})$ on the $5$-face Möbius strip $M_5$ with sign character $\chi$ of $D_{10}$). |

### Table III.5.3. Chapter-by-Chapter Registry of Observer Window Shifts ($\Pi_k \to \Pi_{k+1}$) and Solution-Count Regimes ($|\mathcal{R}| \in \{1, >1, 0\}$) Across All `24` Parts of the Trilogy

| No. | Part / Chapter | Prior Window $\Pi_k$ and Shadow Witness $(s,t) \in \ker m_{\mathrm{acc}}$ | New Resolving Invariant $\Pi_{k+1}$ | Governing Solution-Count Regime $|\mathcal{R}|$ |
| :-: | :--- | :--- | :--- | :--- |
| `0` | **`Introduction`** | Unlabelled element identity in $X$ with no position $\mathcal{O}$ | Operational six-tuple $\Gamma$ and typing rule $\mathcal{O} \notin X$ | Typing frame prior to counting solutions |
| `1` | **`Chapter I.1`** | Naive static pair $a \ne b$ without a test-action protocol | Four-place scene $S_4 = \mathbb{F}_2^2$, domain $\mathrm{Dom}(T_a)$, and marker $\bot$ | $|\mathcal{R}| = 0$ under totalization without failure; $|\mathcal{R}| = 1$ for quotient $S_4$ |
| `2` | **`Chapter I.2`** | Single predicate $q : X \to \{0,1\}$ and mute states | Question family $\mathcal{Q}$, cube $Q_3$, and three axes of the octahedron $O_6$ | $|\mathcal{R}| > 1$ inside fibers of $\ker m_{\mathrm{acc}}$; $|\mathcal{R}| = 1$ on $X/{\sim_{\mathcal{Q}}}$ |
| `3` | **`Chapter I.3`** | Instantaneous readout $q(x)$ with no memory of future words | Nerode equivalence $\sim_{\mathrm{Nerode}}$ and minimal quotient automaton $M_{\min}$ | $|\mathcal{R}| = 1$ up to isomorphism of $M_{\min}$ (`5` classes) |
| `4` | **`Chapter I.4`** | Single-number query tally ignoring type check and feedback step | Three-component budget $(Z_D, Z_C, Z_F)$ and information lower bound | $|\mathcal{R}| = 0$ if any of the three components is set to zero in a closed loop |
| `5` | **`Chapter I.5`** | Scalar count blind to traversal orientation and exchange sign | Sign character $\mathrm{sgn}$, cycle parity, and cube involutions | $|\mathcal{R}| = 1$ for $\mathrm{sgn} : \mathfrak{S}_n \to \{\pm 1\}$ ($n \ge 2$) |
| `6` | **`Chapter I.6`** | Planar triangle lacking a third independent axis of opposition | Complete tripartite octahedron $O_6 \cong K_{2,2,2}$ ($6$ vertices, $12$ edges, $8$ faces) | $|\mathcal{R}| > 1$ ($|W(B_3)| = 48$ axis gauges); $|\mathcal{R}| = 1$ for the graph $O_6$ |
| `7` | **`Chapter I.7`** | Finite sequence prefix without continuation rank test | Finite Hankel matrices $H_{m,n}$ and linear recurrence rank | $|\mathcal{R}| > 1$ on an undersized window; $|\mathcal{R}| = 1$ at full window $2r$ |
| `8` | **`Chapter I.8`** | External factor oracle versus polynomial observation window | Oracle-free protocol of observable invariants over rings and graphs | $|\mathcal{R}| > 1$ (shadow residue symmetry prior to nontrivial merge) |
| `9` | **`Chapter I.9`** | Pairwise edge-compatible local sections on $O_6$ | Checkerboard splitting $8 = 4 + 4$, cocycle $\kappa \in H^1(\mathcal{N}(O_6);\mathbb{F}_2)$, presheaf $S_w$ | $|\mathcal{R}| = 0$ for global section when odd charge $\kappa \ne 0$ (`64` cases) |
| `10` | **`Chapter II.1`** | Finite state table without a linear state-space realization | Ho–Kalman realization ($\dim M_{\min} = \mathrm{rk}\,\mathcal{H}$) and window bound $L \ge 2r$ | $|\mathcal{R}| > 1$ ($\mathrm{GL}_r$ basis torsor); $|\mathcal{R}| = 1$ for $\mathrm{rk}\,\mathcal{H} = r$ |
| `11` | **`Chapter II.2`** | Finite Boolean refinement levels $D_n$ without inverse-limit gluing | Inverse limit $\varprojlim X_n$ (König–Stone) on the Cantor cube $\{0,1\}^{\mathbb{N}}$ | $|\mathcal{R}| > 1$ at finite depth; $|\mathcal{R}| \ge 1$ for an infinite branch by König |
| `12` | **`Chapter II.3`** | Pointwise chart agreement without nerve homology | Mayer–Vietoris sequence and universal coefficients on $O_6 \simeq S^2$ | $|\mathcal{R}| = 1$ ($H_2(O_6;\mathbb{Z}) \cong \mathbb{Z}$); $|\mathcal{R}| = 0$ for splitting odd holonomy |
| `13` | **`Chapter II.4`** | Scalar vertex sector $V_+$ on $O_6$ without dipole parity | Decomposition $\Bbbk^6 = V_+ \oplus V_-$ over $W(B_3)$ and double cover $2O \cong \mathrm{GL}_2(\mathbb{F}_3)$ | $|\mathcal{R}| = 0$ for splitting $2O \twoheadrightarrow W(B_3)^+$; $|\mathcal{R}| = 2$ spinor lifts |
| `14` | **`Chapter II.5`** | Real involution $S^2 = +I$ without quarter-period phase shift | Quarter-turn $J^2 = -I$, Cayley–Dickson tower $\mathbb{R}\to\mathbb{C}\to\mathbb{H}\to\mathbb{O}$, and $\mathrm{Oct}(\mathbb{F}_2)$ | $|\mathcal{R}| = 0$ for real eigenvectors of $J$; $|\mathcal{R}| > 1$ ($72$ idempotents) |
| `15` | **`Chapter II.6`** | Commutative Boolean gluing of all measurement contexts | Peres–Mermin square, $64$ Hoggar lines in $\mathbb{C}\mathrm{P}^3$, and Gleason–Busch rule | $|\mathcal{R}| = 0$ for noncontextual coloring; $|\mathcal{R}| = 1$ for $\mathrm{tr}(\rho E)$ |
| `16` | **`Chapter II.7`** | Purely combinatorial count ignoring noisy-channel variance | Fisher information matrix $I(\theta)$, Cramér–Rao bound, and Čencov metric | $|\mathcal{R}| = 1$ up to scalar multiple for the monotone Fisher–Rao metric |
| `17` | **`Chapter II.8`** | Finite-grid trajectory sampling without global certificate | Rational sum-of-squares `SOS` Gram matrices over $\mathbb{Q}$ and Lyapunov barriers | $|\mathcal{R}| > 1$ (convex cone of Gram matrices); $|\mathcal{R}| = 0$ when invariance fails |
| `18` | **`Chapter II.9`** | Attempt to encode all predicates $Y^X$ by elements of $X$ itself | Cantor–Lawvere diagonal theorem and internal subobject classifier $\Omega$ | $|\mathcal{R}| = 0$ when $\mathrm{Fix}(\neg) = \varnothing$; $|\mathcal{R}| \ge 1$ when a fixed point exists |
| `19` | **`Chapter III.1`** | Single-arrow identification of model and domain | Two-arrow bridge $(\iota, \mathcal{O}_\pi)$, $8$-row passport, and levels `L1–L4` | $|\mathcal{R}| > 1$ in family $P_c(x)$ (`Prop. III.1.1`); $|\mathcal{R}| = 0$ for $P_7 \to \mathrm{PG}(2,2)$ |
| `20` | **`Chapter III.2`** | Unsigned weight matrix $W$ or threshold truncation $w < \tau$ | Edge signs $\sigma$, retentions $\alpha$, explicit $\mathrm{Dom}(q)$, and resolvent $\widetilde{P}_\tau$ (`0` mass loss) | $|\mathcal{R}| > 1$ opposite dynamics on one $W$; $|\mathcal{R}| = 1$ for mass $\mathbf{1}^{\mathsf{T}}\widetilde{W}_\tau\mathbf{1} = M$ |
| `21` | **`Chapter III.3`** | Flattening witness and object roles into a single undifferentiated list | Pair graphs $\mathrm{KG}(5,2)$, $J(5,2)$, $M_5$ intertwining, two $O_6$, roots in $\mathfrak{S}_6 / \mathfrak{S}_8$ | $|\mathcal{R}| = 0$ in $\mathfrak{S}_6$ ($r^2=c_6$); $|\mathcal{R}| = 12$ in $\mathfrak{S}_8$ ($r^2=c_8$); $\dim \mathrm{Alg}(g_1,g_2) = 9$ |
| `22` | **`Chapter III.4`** | Isolated partial relations and unlabelled symbol strings $\Sigma^T$ | Cofactor-graph cycles $\mathcal{G}_{\mathrm{LP}}$ ($r_{\mathrm{cyc}}$) and $\mathfrak{S}_m$ orbit of HMM parameters | $|\mathcal{R}| \ge 2^{r_{\mathrm{cyc}}-|B|}$ in parity kernel; $|\mathcal{R}| = m!$ equivalent HMM labellings |
| `23` | **`Chapter III.5`** | Behavioral equivalence claim without an exhibited certificate | Checker protocol $\phi : X \to M$, product traversal $X \times M$, and Grönwall bound | $|\mathcal{R}| = 1$ for minimal $M_{\min}$; $|\mathcal{R}| = 0$ for certain nonminimal targets $M$ |

The task posed in the `Introduction` to Volume I has been completed in full: from the first elementary question of what it means to distinguish two states $a$ and $b$ by means of a finite protocol with partial actions and finite memory, we have proceeded along an unbroken deductive path to rigorous cohomological gluing obstructions, linear and quantum representations, and passported mathematical bridges equipped with an explicit law of self-limitation and falsification.
