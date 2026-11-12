# Chapter III.1. How to Construct a Domain Bridge: Data, Scales, Control Experiments, and Falsification

Books I and II constructed a closed deductive core of the metatheory of the observer. In Book I we began with the operational contract of observation $\Gamma$, the four-state scene $S_4 = \mathbb{F}_2^2$, partial actions with an explicit refusal threshold $\bot$, minimal Moore–Nerode memory of future distinctions (`Chapter I.3`), feedback cost (`Chapter I.4`), sign involution (`Chapter I.5`), three graphs on the six non-constant affine questions ($3K_2$, the octahedron $O_6$, and the cycle $C_6$ in `Chapter I.6`), oracle-free Hankel windows (`Chapter I.8`), and the cohomological gluing obstruction $\kappa = x_0 \oplus c_0 \oplus b_0 \in H^1(\mathcal{N}(O_6); \mathbb{F}_2)$ around the four hollow faces of the chessboard octahedron (`Chapter I.9`). In Book II these finite constructions were extended in four directions: linear Ho–Kalman memory and continuous continuation via jets and the Cayley transform (`Chapters II.1–II.2`), chain complexes with torsion, coverings, the group $W(B_3) = \mathrm{Aut}(O_6)$, and modular octonions $\mathrm{Oct}(\mathbb{F}_2)$ with the Paige loop $M_{120}$ (`Chapters II.3–II.5`), the quantum Walsh–Bloch bridge on $S_4$, the $64$ Hoggar lines, and the Peres–Mermin square (`Chapters II.6–II.7`), Whitney cochain forms, rational `SOS` certificates on Fano flags, and Lawvere's diagonal theorem on the internal limit of self-description (`Chapters II.8–II.9`).

Across all eighteen chapters of the first two volumes, every statement was proved within an explicitly specified mathematical structure and did not depend on any external corpus or applied registry. **Book III** opens the next contour of work. It answers the question: **under what exact, verifiable, and falsifiable conditions can a mathematical construction of Books I–II be linked to an external mathematical, algorithmic, or philological subject—a directed weighted graph with overlapping vertex classes, a classical philosophical-grammatical treatise, an oracle-free multigraph of large prime cofactors, or a hidden Markov model of symbol sequences?**

---

## §III.1.1. Similarity of Pattern Is Not Yet a Bridge: The Law of Two Explicitly Typed Arrows $(\iota, \mathcal{O}_\pi)$

Imagine a typical research situation. In one problem, while analyzing projections of multidimensional tables, a two-dimensional configuration of three centered directions is discovered; in another, while reading a classical treatise, a triad of functional roles is discussed; in a third, a graph of twelve edges isomorphic to the octahedron $O_6$ arises on six objects.

By itself, a coincidence in the number of vertices (`3`, `6`, `7`, `8`, `10`, `24`, or `120`) proves nothing whatsoever:
- from the fact that three centered vectors lie in a single two-dimensional plane, it neither follows that they form an equilateral triangle nor that an ancient author had the same linear operation in mind;
- from the fact that twelve edges of an octahedron $O_6$ can be drawn on six elements, it does not follow that the same transition operators act in the graph-theoretic or textual object under study, or that the same parity obstruction $\kappa = 1$ arises as on the scene $S_4$;
- from the fact that an internal feature in the parameters of a model correlates with a vocabulary of "observation" or "self-report", it in no way follows that this internal vector $v \in X$ has become the extra-object observer position $\mathcal{O} \notin X$ (`Introduction`, `Chapter II.9`).

Does this mean that structural parallels between different fields are useless? On the contrary: a structural parallel is often what first suggests a new research question. Yet in order to turn a heuristic conjecture into a testable mathematical or applied statement, one must stop leaping from a theorem to external tables with a single silent symbol "$\leftrightarrow$". Between the mathematical core of Books I–II and an external subject domain, Book III **always writes out two separate, explicitly typed arrows**:

$$
\boxed{\text{Mathematical Core of Books I–II}}
\;\xrightarrow{\;\iota\;}\;
\boxed{\text{Formal Domain Model }(S, A)}
\;\xrightarrow{\;\mathcal{O}_\pi \text{ or } K_\pi\;}\;
\boxed{\text{Primary Tables and Verification Comparison } D}.
$$

Let us examine the exact meaning of each of these two arrows:
1. **First arrow ($\iota$ — model encoding and choice of structure):** the researcher explicitly declares which specific objects and attributes of the external domain are mapped to elements of the carrier $S$, what counts as an admissible action $a \in A$, and which mathematical predicate from Books I–II is selected on this carrier. Without an explicitly exhibited arrow $\iota$, the same verbal label ("memory", "phase", "twist", "role") becomes imperceptibly attached to different mathematical objects.
2. **Second arrow ($\mathcal{O}_\pi$ or $K_\pi$ — procedural contract of reading and comparison):** the researcher explicitly specifies the observation procedure under a fixed protocol $\pi$—the reference scale, numerical precision, threshold filtering rules, checksum of the primary table, surrogate (null) control, and exact falsification criterion. Without the second arrow, the mathematical construction remains enclosed within the model and yields not a single testable consequence about the external subject.

```text
  TWO-ARROW DIAGRAM OF A DOMAIN BRIDGE IN BOOK III

  [Mathematical Core of Books I-II]       [Formal Domain Model]                [Primary Tables and Control]
   Scene S_4, octahedron O_6, Hankel rank, Model states S,                      Observation records d in D,
   cocycle w in Z^1(N; F_2), charge kappa  probe regimes A                      scale unit, null control
                  |                                        |                                  ^
                  |  Arrow 1: encoding choice iota         |  Arrow 2: readout O_pi / K_pi    |
                  +--------------------------------------->+----------------------------------+
                                                           |
                                            (Independent test and falsification:
                                             comparison at points x_* outside fitting nodes!)
```
**Fig. III.1.1.** Two-arrow contract of a domain bridge.  
A mathematical theorem lives in the left block and holds unconditionally under its axioms; a substantive statement about an external subject arises only as the composition of the model choice $\iota$ and the readout map $\mathcal{O}_\pi$, tested at held-out points $x_*$ against a surrogate control.

---

## §III.1.2. Typing of Deterministic and Stochastic Readout and Monotonicity of Information Coarse-Graining

Let us formalize the second arrow of the bridge in the language of partial actions and channels from Books I and II.

> **Definition III.1.1 (Deterministic Observation Map and Stochastic Markov Kernel of Readout).**  
> In a given domain problem, let $S$ be the set of states of the formal model of the subject, $A$ be the set of admissible probe actions or protocol settings, and $D$ be the alphabet of possible output records (including the chosen scale, precision, and an explicit refusal marker $\bot$).
> 1. A **deterministic readout protocol** $\pi$ is specified by an evaluation map
>    $$
>    \mathcal{O}_\pi : S \times A \longrightarrow D, \qquad (s, a) \longmapsto d = \mathcal{O}_\pi(s, a).
>    $$
> 2. A **stochastic readout protocol** (in the presence of random perturbations, sampling variance, or probabilistic sampling) is specified by a Markov transition kernel $K_\pi : S \times A \leadsto D$, assigning to each pair $(s, a) \in S \times A$ a probability distribution $K_\pi(\cdot \mid s, a)$ on the space of records $D$:
>    $$
>    K_\pi(d \mid s, a) \ge 0, \qquad \sum_{d \in D} K_\pi(d \mid s, a) = 1 \quad \forall (s, a) \in S \times A.
>    $$

Three methodological rules follow immediately from this definition:
- **Observation is essentially binary in $(s, a)$:** a record $d \in D$ belongs not to "the state $s$ in itself", but to the pair $(s, a)$ within the chosen protocol $\pi$. Two states $s_1 \ne s_2 \in S$ that yield an identical response $\mathcal{O}_\pi(s_1, a_1) = \mathcal{O}_\pi(s_2, a_1)$ under one regime $a_1$ may diverge under another admissible intervention $a_2 \in A$ (just as on the scene $S_4$ in `Chapter I.1`, a single question $q_x$ identifies states in pairs, and only the addition of a second question or a step shift separates all four points).
- **An inverse map $\mathcal{O}_\pi^{-1}$ does not exist in general:** from a single output table $D$ one cannot "reconstruct a unique internal mechanism $s \in S$" until a separating family of regimes from $A$ has been exhibited and injectivity of the induced map into the quotient by future answers has been proved (`Chapter I.3`).
- **Monotonicity of information coarse-Graining:** if post-processing (rounding, aggregation into a summary table, or dropping columns) $g : D \to D'$ acts on the space of raw records $D$, then the composition $(g \circ \mathcal{O}_\pi)(s, a) = g(\mathcal{O}_\pi(s, a))$ (or the pushforward kernel $(g_* K_\pi)(d' \mid s, a) = \sum_{d \in g^{-1}(d')} K_\pi(d \mid s, a)$ in the category of finite stochastic kernels $\mathbf{FinStoch}$) **cannot separate** any pair of states $s_1, s_2 \in S$ already identified prior to post-processing:
  $$
  K_\pi(\cdot \mid s_1, a) = K_\pi(\cdot \mid s_2, a) \implies (g_* K_\pi)(\cdot \mid s_1, a) = (g_* K_\pi)(\cdot \mid s_2, a).
  $$
  No subsequent statistical repackaging or diagram creates a new distinction in the data if that distinction was erased at the protocol's input.

---

## §III.1.3. Why Agreement at Finitely Many Nodes and Local Slices Does Not Prove a Global Law

In applied work one frequently encounters the temptation to take a finite set of values $y_1, \dots, y_n$ at nodes $x_1, \dots, x_n$ (or two local coordinate slices of a linear operator), fit a formula $P(x)$ passing through those points, and proclaim $P(x)$ a "universal law". Let us show by an elementary algebraic proposition why agreement at support nodes and diagonal slices proves nothing by itself without verification at held-out points $x_* \notin \{x_1, \dots, x_n\}$ and without accounting for cross-blocks.

> **Proposition III.1.1 (Infinite Family of Polynomial Continuations and Non-Recoverability of Matrix Rank from Two Diagonal Slices).**  
> *Classical foundation.* Quotient of the polynomial ring $K[x]$ by the ideal of Lagrange interpolation nodes and rank properties of block matrix slices under orthogonal projections. *Contribution of this book:* Combining the polynomial continuation torsor $P_c(x)$ and the rank-$1$ slice counterexample $P_i A P_i$ over $\mathbb{Q}$ and $\mathbb{F}_2$ into a unified algebraic falsification test for domain bridges.
> 1. **Family of continuations across a finite node set:** Let pairwise distinct nodes $x_1, \dots, x_n \in K$ be given over an arbitrary field $K$, together with a polynomial $P(x) \in K[x]$ taking the values $y_i = P(x_i)$ at these nodes ($i = 1, \dots, n$). For each parameter $c \in K$, set:
>    $$
>    P_c(x) = P(x) + c \prod_{i=1}^n (x - x_i).
>    $$
>    Then at all support nodes the values of the entire family coincide ($P_c(x_i) = P(x_i) = y_i$ for all $c \in K$), whereas at any test point $x_* \in K \setminus \{x_1, \dots, x_n\}$ outside the support nodes, the difference $P_c(x_*) - P(x_*) = c \prod_{i=1}^n (x_* - x_i)$ sweeps out **the entire field $K$** as $c \in K$ varies.
> 2. **Rational witness inside and outside the support interval:** Over the field $K = \mathbb{Q}$ for two nodes $x_1 = 0$ and $x_2 = 1$, the polynomials $P(x) = 0$ and $Q(x) = P_1(x) = x(x - 1)$ coincide identically on $\{0, 1\}$ ($P(0) = Q(0) = 0$, $P(1) = Q(1) = 0$), but diverge both **between** the nodes ($P(1/2) = 0 \ne -1/4 = Q(1/2)$) and **outside** the support set ($P(2) = 0 \ne 2 = Q(2)$).
> 3. **Non-recoverability of global rank from two complementary orthogonal slices:** Over the field $K = \mathbb{Q}$ and over the finite field $K = \mathbb{F}_2$, there exist a matrix $A \in K^{4 \times 4}$ and a pair of complementary rank-$2$ projectors $P_1 = \mathrm{diag}(1,1,0,0)$ and $P_2 = \mathrm{diag}(0,0,1,1)$ ($P_1 + P_2 = I_4$, $P_1 P_2 = 0$) such that both local diagonal slices have rank $1$, whereas the full operator has strictly larger rank $2$:
>    $$
>    A = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \qquad \mathrm{rk}_K(P_1 A P_1) = \mathrm{rk}_K(P_2 A P_2) = 1 < 2 = \mathrm{rk}_K(A).
>    $$

**Proof.**  
1–2. Substituting $x = x_j$ ($1 \le j \le n$), the factor $(x_j - x_j)$ in the product $\prod_{i=1}^n (x - x_i)$ vanishes, whence $P_c(x_j) = y_j$. Conversely, if $x_* \notin \{x_1, \dots, x_n\}$, then every factor $x_* - x_i \ne 0$ in the field $K$. Since a field has no zero divisors, the product $u = \prod_{i=1}^n (x_* - x_i) \in K \setminus \{0\}$ is invertible in $K$, and for any prescribed value $y_* \in K$ the unique choice $c = (y_* - P(x_*)) u^{-1} \in K$ yields $P_c(x_*) = y_*$. The values for $Q(x) = x(x-1)$ at $\{0, 1, 1/2, 2\}$ are verified by direct substitution.  
3. For the matrix $A$ above, the slice $P_1 A P_1 = e_{11}$ and the slice $P_2 A P_2 = e_{34}$ each contain a single nonzero entry $1$, so $\mathrm{rk}_K(P_1 A P_1) = \mathrm{rk}_K(P_2 A P_2) = 1$ over every field $K$. In the full matrix $A$, however, the first row $(1,0,1,0)$ and the third row $(0,1,0,1)$ are linearly independent over both $\mathbb{Q}$ and $\mathbb{F}_2$, while the second and fourth rows vanish, whence $\mathrm{rk}_{\mathbb{Q}}(A) = \mathrm{rk}_{\mathbb{F}_2}(A) = 2$: the coupling resides in the off-diagonal blocks $P_1 A P_2$ and $P_2 A P_1$, which are invisible inside each diagonal slice taken separately. $\blacksquare$

> **Corollary on Scale Units and Degrees-of-Freedom Budget.**  
> 1. Under an affine rescaling of the input coordinate $x \mapsto \lambda x$ ($\lambda \in K^\times$), the leading coefficient transforms as $c \mapsto \lambda^{-n} c$: substituting a numerical parameter $c$ without fixing the scale unit changes all off-node predictions of the model.
> 2. In order for a finite number of evaluations at nodes $x_1, \dots, x_n$ to determine a function $P$ uniquely, the degree bound $\deg P < n$ (or the Hankel operator rank condition $\operatorname{rank} \mathcal{H} \le r$ in `Theorem II.1.2` for window width $2r$) must be **fixed in the model contract prior to inspecting the table**, and verification must be performed at held-out points $x_* \notin \{x_1, \dots, x_n\}$ that did not participate in fitting the coefficients.

---

## §III.1.4. Eight Mandatory Passport Rows for Every Domain Bridge

To prevent any blurring of boundaries between a proved theorem, a count on a primary table, and a historical-philosophical interpretation, every domain comparison in Book III is audited against **eight mandatory rows of the domain bridge passport** (across the four epistemic levels **`L1` — mathematical core**, **`L2` — primary source or table**, **`L3` — passported bridge model**, **`L4` — dictionary of interpretations `REG-INTERP`**):

1. **Subject and primary data:** what specifically is studied, from what canonical source or synthetic benchmark it is specified, and the inclusion and filtering rules for records; a formal model, a historical text, a readout procedure, and a table of numbers are never conflated under a single name.
2. **Quantities, scales, and procedure ($\mathcal{O}_\pi$):** what specifically is computed or read out, in what integer counts or dimensionless rational fractions, and with what exactness; how a measured zero differs from an absent answer ($\bot$).
3. **Split prior to fitting (`train / val / test`):** which data or definitions are fixed prior to constructing the map, and which test points or check identities are held out for blind verification without target leakage.
4. **Free choices and degrees of freedom:** how many parameters, features, slices, cycles, templates, and thresholds were selected by the researcher; **manual selection of the best slice or best feature after inspecting the table counts toward the degrees-of-freedom budget** even when it is not stored in a parameter vector.
5. **Null and surrogate control:** what is produced by a random, permuted, or degenerate baseline mechanism on the same carrier that preserves low-level invariants of the subject (vertex in-degrees and out-degrees of a multigraph, class cardinalities, marginal symbol frequencies).
6. **Pre-specified comparison and full cost:** the target invariant, continuation horizon, and full budget of memory and computation steps (including table sizes and the cost of matrix inversion or search); significance on a slice selected by maximum (`post hoc`) is never equated with testing a pre-fixed predicate.
7. **Falsification condition and reproducibility:** what concrete finite counterexample or discrepancy will compel rejection of the proposed bridge, how to reproduce the calculation in single-threaded exact arithmetic, and which negative or degenerate cases are included in the test.
8. **Position of the Observer in the bridge ($\Gamma, \iota, \mathcal{O}_\pi$):** who specifically occupies the extra-object position of applying the contract $\mathcal{O} \notin X$ (setting the cut $\iota$ and reading $\mathcal{O}_\pi$), what constitutes the internal state carrier $X$, which distinctions are erased in the readout kernel $\ker \mathcal{O}_\pi$, and which non-gluable configuration of contexts plays the role of a hollow face of the chessboard octahedron $O_6$ (`Theorem I.9.3a`) or the odd cycle of the Möbius strip $M_5$.

Whenever in a given direction some of these eight rows are closed by an exact proof while others belong to textual hermeneutics, the result receives its exact level in the hierarchy (`L1–L4`) together with an explicit statement of its domain of validity.

---

## §III.1.5. Three Illustrative Examples of the Filter in Action: How One Carrier Yields Different Graphs, Where a Bridge Works, and Where a Bridge Is Rejected

Let us demonstrate the operation of our two-arrow contract on three concrete examples that are verified in the volume's test suite.

### Example 1. How Choosing a Question on the Same Five-Element Role Set $\Lambda_5$ Generates Two Different Graphs: the Petersen Graph $\mathrm{KG}(5,2)$ and the Line Graph $L(K_5) = J(5,2)$

In stanzas `12` and `32` of the classical treatise *Sāṃkhya-kārikā*, two three-element lists of functions are enumerated:
- in `SK 12`, three functions of the *guṇas* are named: illumination/clarity (*prakāśa*), activity/impulsion (*pravṛtti*), and restraint/limitation (*niyama*):
  $$
  G = \{\text{prakāśa},\; \text{pravṛtti},\; \text{niyama}\};
  $$
- in `SK 32`, three operations of the thirteenfold instrument (*karaṇa*) are named: seizing/grasping (*āharaṇa*), holding/retaining (*dhāraṇa*), and illuminating/manifesting (*prakāśana / prakāśa*):
  $$
  K = \{\text{āharaṇa},\; \text{dhāraṇa},\; \text{prakāśa}\}.
  $$

Let us trace all arrows here with complete transparency:
1. **Arrow $\iota_1$ (set-theoretic modeling decision):** the researcher makes the explicit decision to identify the terms *prakāśa* (`SK 12`) and *prakāśana / prakāśa* (`SK 32`) into a single common formal label $P_{\mathrm{light}}$, obtaining from two triples $|G| = |K| = 3$ with a one-element intersection $G \cap K = \{P_{\mathrm{light}}\}$ a five-element alphabet of role labels:
   $$
   \Lambda_5 = G \cup K = \{A, D, P_{\mathrm{light}}, V, N\}, \qquad |\Lambda_5| = 3 + 3 - 1 = 5.
   $$
   Note immediately: this is an explicit modeling decision $\iota_1$, which does not erase the philological difference between the contexts of stanzas `12` and `32`.
2. **Arrow $\iota_2$ (choice of a binary question on pairs of roles):** let us pass from the $5$ labels to the set of all two-element subsets $V_{10} = \binom{\Lambda_5}{2}$ of cardinality $\binom{5}{2} = 10$. Which graph do these $10$ vertices form? Exactly as with the six affine questions of the scene $S_4$ in `Theorem I.6.1`, **the answer depends entirely on which question we ask of a pair of vertices $\{u, v\} \subset V_{10}$**:
   - if we join by an edge **disjoint** pairs ($u \cap v = \varnothing$), then on the $10$ vertices there arises the $3$-regular **Kneser graph $\mathrm{KG}(5,2)$ (the Petersen graph)**: it has $15$ edges, diameter $2$, girth $5$, and clique number $\omega(\mathrm{KG}(5,2)) = 2$ (triangle-free); moreover, as proved in `Theorem III.3.1`, its $5$-dimensional eigenspace $\ker(A_{\mathrm{KG}} - I_{10})$ is isometrically intertwined with the $2$-chain space $C_2(M_5)$ of the minimal $5$-face triangulation of the Möbius strip $M_5$ by the polynomial identity $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$;
   - if instead on the exact same $10$ vertices we join by an edge pairs having a **one-element intersection** ($|u \cap v| = 1$), there arises its complement, the $6$-regular **line graph of the complete five-vertex graph $L(K_5) = J(5,2)$ (the Johnson graph)**: it has $30$ edges ($15 + 30 = \binom{10}{2} = 45$), the same diameter $2$, but girth $3$ and clique number $\omega(L(K_5)) = 4$.

This example illustrates the first commandment of Book III: neither the Petersen graph $\mathrm{KG}(5,2)$ nor the Johnson graph $L(K_5)$ is "hidden inside the ancient text as a ready-made blueprint"—they are generated by **our choice of adjacency predicate** on the pair set $\binom{\Lambda_5}{2}$.

### Example 2. Positive Benchmark of a Working Domain Bridge: Random-Walk Resolvent Filtration Versus Hard Thresholding of Weak Bridges (`Chapter III.2`)

As a positive benchmark of a two-arrow bridge passing all eight rows of the passport, consider route filtration on a finite directed weighted graph of six vertices (two dense three-vertex cycles of combined weight $30$ linked by a pair of directed unit-weight bridges $w = 1$ of total mass $M = 32$, analyzed in detail in `Chapter III.2`):
- **Arrow $\iota$:** the table of directed edge multiplicities is encoded by the full column-stochastic transition matrix $P = W D_{\mathrm{out}}^{-1}$ and the conservative random-walk resolvent $\widetilde{P}_\tau = (1 - \alpha_\tau)(I - \alpha_\tau P)^{-1}$ with $\alpha_\tau = \frac{\tau}{1 + \tau}$, without deleting small-weight edges.
- **Arrow $\mathcal{O}_\pi$:** the protocol measures total preserved weight mass $\mathbf{1}^{\mathsf{T}} \widetilde{W}_\tau \mathbf{1}$, column stochasticity $\mathbf{1}^{\mathsf{T}} \widetilde{P}_\tau = \mathbf{1}^{\mathsf{T}}$, and minimum cross-cluster reachability $\min_{u,v}(\widetilde{P}_1)_{uv}$ against hard threshold truncation $w < 2$.
- **Testable consequence and falsification:** `Proposition III.2.1` predicts in advance that hard threshold truncation $w < 2$ discards both bridge edges (dropping total mass from $32$ to $30$) and breaks strong connectivity into two isolated components (zeroing all cross-cluster transitions), whereas the exact rational resolvent $\widetilde{P}_1 = \frac{1}{2}(I_6 - \frac{1}{2}P)^{-1}$ over $\mathbb{Q}$ preserves $100\%$ of the weight mass ($\mathbf{1}^{\mathsf{T}} \widetilde{W}_1 \mathbf{1} = 32$) and maintains strictly positive cross-cluster reachability ($\min_{u,v}(\widetilde{P}_1)_{uv} = 5/1833 > 0$), attenuating multi-step paths by the geometric factor $\alpha_\tau^k$ without altering the underlying carrier.

### Example 3. Negative Benchmark (Rejected Bridge): Why the Seven-Vertex Linear Path $P_7$ Does Not Form the Fano Projective Plane $\mathrm{PG}(2,2)$

Let us now show how the eight-row passport filters out false identifications based on the coincidence of a single vertex count $|V| = 7$. One often encounters attempts to identify a linear seven-step scale or simple path $P_7 = (v_1 - v_2 - \dots - v_7)$ on seven consecutive nodes (or a six-vertex path $P_6$ together with one distinguished apex) directly with the seven points of the Fano projective plane $\mathrm{PG}(2,2) = \mathbb{P}^2(\mathbb{F}_2)$ from `Chapter I.6` and `Chapter II.5`. Let us pass this hypothesis through our filter:
1. In `Theorem I.6.3` and `Theorem II.5.1`, the Fano plane $\mathrm{PG}(2,2)$ is defined by a set of $7$ points together with a system of **$7$ lines** (triples of points) among all $\binom{7}{3} = 35$ possible triples, satisfying the projective axiom: any two distinct points lie on a unique common line, any two lines intersect in a unique point, and the automorphism group $\mathrm{GL}_3(\mathbb{F}_2)$ of order $168$ acts **transitively** on all $7$ points and $21$ flags (all $7$ points are structurally equivalent and admit neither "endpoints" nor a distinguished "center").
2. In the seven-vertex linear path $P_7$, by contrast, the structure is incompatible with $\mathrm{PG}(2,2)$ across three invariants simultaneously: $P_7$ has two degree-$1$ endpoints and five degree-$2$ interior vertices, only $6$ consecutive triples $(v_i, v_{i+1}, v_{i+2})$ instead of $7$ projective lines (with distant vertices such as $v_1$ and $v_7$ sharing no local triple at all), and an automorphism group $\mathrm{Aut}(P_7) \cong C_2$ of order $2$ rather than $168$ (and likewise for the disjoint union $P_6 \sqcup \{v_7\}$, whose automorphism group has order $2 \ne 168$). No bijection $V(P_7) \to \mathrm{PG}(2,2)$ maps the local triples of the path onto the $7$ projective lines or intertwines the symmetry group actions (`GATE-III01-03`).
3. **Filter verdict:** a coincidence of cardinalities $|V| = 7$ without preservation of the incidence relation and automorphism group does not form a morphism (`Chapter I.6`, `Chapter II.1`). The hypothesis "linear $7$-node path $P_7 \cong \mathrm{PG}(2,2)$" is **rejected** and recorded as the canonical negative benchmark.

---

## §III.1.6. Five-Beat Shift of the Observer Window in Domain Bridges, Five Bridges `DB-01..DB-05`, and Passport of Chapter `III.1`

The two-arrow diagram $(\iota, \mathcal{O}_\pi)$ directly extends the two methodological mechanisms of Books I–II:

1. **Five-Beat Shift of the Observer Window in a domain problem:** (1) the researcher separates the object under study and their own position $\mathcal{O} \notin S$ from the chosen model code $\iota$ and readout window $\mathcal{O}_\pi$; (2) exhibits a shadow pair $(s, t) \in \ker \mathcal{O}_\pi$ ($s \ne t$, such as the polynomials $P(x)=0$ and $Q(x)=x(x-1)$ on nodes $\{0,1\}$, or two matrices with identical diagonal slices $P_i A P_i$); (3) applies a held-out test or a new admissible action $a_* \in A$ outside the fitting support ($x_* = 1/2$, an off-diagonal probe, or a cross-cluster connectivity check at $w = 1$); (4) performs a three-way check with a null surrogate control while preserving degenerate cases; (5) fixes the extended contract or rejects the invalid bridge.
2. **Three Solution-Count Regimes $|\mathcal{R}| \in \{1, >1, 0\}$ under bridge verification:**
   - **$|\mathcal{R}| = 1$ (forced canonical invariant):** once $(\iota, \mathcal{O}_\pi)$ are fixed, the tested invariant or morphism is determined uniquely with zero fitting degrees of freedom (exact conservation of total weight mass $M = 32$ by the resolvent $\widetilde{P}_\tau$ in `Example 2` above);
   - **$|\mathcal{R}| > 1$ (torsor of continuations or relabellings):** the observations on the support window admit a family of equally valid solutions ($P_c(x) = P(x) + c\prod(x-x_i)$ in `Proposition III.1.1`, the choice of $\mathrm{KG}(5,2)$ versus $J(5,2)$ in `Example 1`, hidden-state permutation $\mathfrak{S}_m$ without an external anchor in `Chapter III.4`);
   - **$|\mathcal{R}| = 0$ (strict obstruction and bridge falsification):** no morphism preserving the declared operations and incidences exists (the rejected bridge $P_7 \not\cong \mathrm{PG}(2,2)$ in `Example 3`, or the non-gluable holonomy of the Möbius strip $M_5$).

Across Chapters `III.2–III.4`, this filter is applied systematically to five passported domain bridges (denoted by the codes **`DB-01..DB-05`**, in exact one-to-one alignment with the summary registry of `Table III.4.1`):

| Bridge Code | Subject Domain | Primary Verification Question of the Passport | Where Analyzed in Book III |
| :--- | :--- | :--- | :---: |
| **`DB-01`. Directed Weighted Graphs and Filtration** | Directed multigraphs, overlapping roles, and random-walk resolvent | Why does a static weight graph fail to specify dynamics without signs $\sigma$ and constants $\alpha$, and how does the resolvent preserve $100\%$ of mass without severing weak bridges? | `III.2`, Appendix `PM` |
| **`DB-02`. Role Schemes of *Sāṃkhya* and *Advaita*** | Texts `SK, YS, MK, BSB`, mirror code, and pair graphs $\mathrm{KG}(5,2), J(5,2), M_5$ | Where lies strict pair combinatorics and the gluing of two octahedra $O_6$, and where lies primary-source philology and the dictionary `L4`? | `III.3 (§§III.3.1–III.3.3)` |
| **`DB-03`. Pāṇini's Six Case Roles (*kāraka*)** | *Aṣṭādhyāyī* `1.4.23–55`, circulant $C_6(1,2) \cong O_6$, and dipole algebra | How do six case axes decompose $O_6 = C_6 \sqcup 2C_3$, and why does a single $6$-cycle span dimension $3/9$ whereas two non-collinear $6$-cycles span all $9/9$ in $\mathrm{End}(V_-)$? | `III.3 (§III.3.4)` |
| **`DB-04`. Oracle-Free Cofactor Merging** | Congruence of squares $X^2 \equiv Y^2 \pmod N$ and cofactor-graph cyclomatic rank | How do cycles of partial relations in the multigraph $\mathcal{G}_{\mathrm{LP}}$ generate a square congruence without consulting the secret factors $(p,q)$? | `III.4 (§III.4.2)` |
| **`DB-05`. Gauge Symmetry of Hidden Markov Models** | Hidden Markov models on unlabelled symbol sequences $\Sigma^T$ and group $\mathfrak{S}_m$ | Why does $\mathfrak{S}_m$ likelihood invariance forbid unique recovery of the external semantics of hidden states without a bilingual anchor? | `III.4 (§III.4.3)` |

Let us conclude the introductory chapter with its own eight-row passport.

### Domain Bridge Passport of Chapter `III.1`

| No. | Passport Row | Contents for the Methodological Filter of Chapter `III.1` |
| :---: | :--- | :--- |
| `1` | **Subject and primary data** | Two-arrow transfer diagrams $(\iota, \mathcal{O}_\pi)$ between the mathematical core of Books I–II and the five domain bridges `DB-01..DB-05`. |
| `2` | **Quantities, scales, and procedure** | Deterministic evaluation maps $\mathcal{O}_\pi : S \times A \to D$, stochastic kernels $K_\pi(d \mid s,a)$ in $\mathbf{FinStoch}$, interpolation families $P_c(x)$, and orthogonal slices $P_i A P_i$ over a field $K$. |
| `3` | **Split prior to fitting** | Strict separation of support fitting nodes $\{x_1, \dots, x_n\}$ and held-out test points $x_* \notin \{x_1, \dots, x_n\}$, as well as diagonal slices $P_i A P_i$ and cross-blocks (`Proposition III.1.1`). |
| `4` | **Free choices and degrees of freedom** | Free parameter $c \in K$ in the family $P_c(x) = P(x) + c\prod_{i=1}^n(x-x_i)$, off-diagonal entries of $A$, and choice of adjacency predicate ($u \cap v = \varnothing$ versus $|u \cap v| = 1$) on $\binom{\Lambda_5}{2}$. |
| `5` | **Null and surrogate control** | Polynomial $Q(x) = x(x-1)$ versus $P(x) = 0$ on nodes $\{0,1\}$; rank-$2$ operator with rank-$1$ diagonal slices; complementary graph $L(K_5) = J(5,2)$ (`30` edges, $\omega = 4$) versus $\mathrm{KG}(5,2)$ (`15` edges, $\omega = 2$) on the same `10` pairs. |
| `6` | **Pre-specified comparison and full cost** | Testing at points $x_* = 1/2$ (`-1/4 != 0`) and $x_* = 2$ (`2 != 0`), exact rank computation over $\mathbb{Q}$ and $\mathbb{F}_2$, accounting for the scaling law $c \mapsto \lambda^{-n} c$, and prohibition of silent isomorphisms based on vertex count alone. |
| `7` | **Falsification condition and reproducibility** | Any bridge lacking an explicit arrow $\iota$, lacking a surrogate control, or diverging at held-out points $x_*$ is rejected (as the identification $P_7 \cong \mathrm{PG}(2,2)$ is rejected). Single-threaded gates `GATE-III01-01..03` in `07_verify_full_book_III_v3_3.jl`. |
| `8` | **Position of the Observer in the bridge ($\Gamma, \iota, \mathcal{O}_\pi$)** | The observer $\mathcal{O} \notin S$ holds both arrows of the bridge: selects the model encoding $\iota$ and probe regime $a \in A$, reads $d = \mathcal{O}_\pi(s,a)$, tracks the gluing kernel $\ker \mathcal{O}_\pi$, and checks whether local contexts form a non-gluable configuration ($\kappa = 1$). |
