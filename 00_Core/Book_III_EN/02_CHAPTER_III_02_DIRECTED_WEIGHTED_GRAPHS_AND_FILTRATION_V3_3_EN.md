# Chapter III.2. Directed Weighted Graphs and Dynamic Execution: From a Static Graph to Resolvent Filtration

The observer of Book I saw only the answers to their questions. Now they are shown the entire connection table at once: a list of nodes and directed arrows with positive weights. It seems there is nothing more to know. Yet the table of weights is silent on what matters most: which arrows add a signal with a plus sign and which invert it with a minus sign, what fraction of its past state each node retains on the next step, and which individual output channels are attached to the vertices. The chapter begins with a lemma proving why a static weight graph alone is insufficient to specify the dynamics of a system uniquely.

In this chapter we construct the mathematical bridge to directed weighted graphs with partial and overlapping vertex-class labellings (`DB-01`). We prove the **lemma on the insufficiency of a static directed weighted graph alone** without transmission signs, retention coefficients, and output-channel bindings (`Lemma III.2.1`), examine the inclusion-exclusion law and dependence of the answer on the domain of definition of a question $\mathrm{Dom}(q)$ on a finite synthetic registry of $40$ vertices that the reader can recount by hand, and prove the conservativity of random-walk resolvent filtration on the full matrix without edge loss (`Proposition III.2.1`).

The classical tools of the chapter are F. Harary's signed graphs, the inclusion-exclusion formula, the Neumann series, and the random-walk resolvent on a directed graph (L. Katz index, 1953; the PageRank core, 1998). The contribution of this book lies in the exact demarcation between *what* is contained in the weight matrix $W$ itself and what additional components of the contract $\Gamma$ are required to pass from a static adjacency table to linear dynamics and mode filtration.

---

## §III.2.1. Why a Matrix of Positive Weights Does Not Yet Define Dynamics: Lemma on the Insufficiency of a Static Graph

Suppose a system is presented as a finite directed weighted graph $G = (V, E, w)$, where $V$ is the set of nodes, $E \subseteq V \times V$ is the set of directed pairs, and $w : E \to \mathbb{Z}_{>0}$ is the positive multiplicity (weight) of the directed connection from the input node to the output node. Is this graph $G$ alone sufficient to determine signal transfer, inertial node memory, and the output response of the system uniquely? The following lemma gives a precise negative answer.

### Lemma III.2.1 (On the Insufficiency of a Static Weighted Graph Without Dynamic Semantics)

*Classical foundation.* Signed graphs (F. Harary, 1953) and commutation conditions for permutation matrices with diagonal and weighted operators. *Contribution of this book:* Proving the insufficiency of an unsigned weight matrix $W$ without transmission signs $\sigma$, retention coefficients $\alpha$, and fixed output-channel bindings.

*Let $G = (V, E, w)$ be a finite directed weighted graph with positive weights $w : E \to \mathbb{Z}_{>0}$. Then:*

1. **Opposite dynamic realizations on the same graph $G$:** *For fixed $V, E, w$, there exist at least two first-order linear dynamical laws*
   $$
   x^{(+)}(t+1) = A^{(+)} x^{(+)}(t), \qquad x^{(-)}(t+1) = A^{(-)} x^{(-)}(t),
   $$
   *whose support and moduli of matrix entries coincide with $(E, w)$ ($|A_{vu}^{(\pm)}| = w(u \to v)$ for $(u \to v) \in E$ and $A_{vu}^{(\pm)} = 0$ otherwise), but which differ by the assignment of edge signs $\sigma : E \to \{+1, -1\}$ (positive transmission versus sign inversion) and generate opposite output responses $x^{(-)}(1) = -x^{(+)}(1)$ on the very same nonzero initial input $x(0)$.*
2. **Non-invariance of dynamics under automorphisms of the static graph with inhomogeneous retention coefficients:** *Let $\pi \in \mathrm{Aut}(G, w)$ be an automorphism of the weighted directed graph preserving all edge weights: $w(\pi(u) \to \pi(v)) = w(u \to v)$. If the nodes are endowed with intrinsic retention coefficients $\alpha : V \to (0,1)$ in the equation*
   $$
   x_v(t+1) = \alpha(v)\,x_v(t) + \sum_{u \to v} \sigma(u \to v)\,w(u \to v)\,x_u(t),
   $$
   *and $\alpha(\pi(v)) \ne \alpha(v)$ for at least one vertex $v \in V$, then the state permutation matrix $P_\pi$ does not commute with the step operator $F = \mathrm{diag}(\alpha) + W_\sigma$: $P_\pi F \ne F P_\pi$, and therefore $\pi$ is not a morphism of the dynamical system.*
3. **Distinction between static graph isomorphism and dynamical morphism under permutation of unequal weights:** *Let two directed weighted graphs $G_1$ and $G_2$ be given on the vertex set $V = \{1, 2, 3\}$ with the same unequal weights $\{w_1, w_2\}$ ($w_1 \ne w_2 > 0$) on a pair of distinct edges out of vertex $1$: in $G_1$ the edge $(1 \to 2)$ has weight $w_1$ and the edge $(1 \to 3)$ has weight $w_2$; in $G_2$ the edge $(1 \to 2)$ has weight $w_2$ and the edge $(1 \to 3)$ has weight $w_1$. Then the graphs $G_1$ and $G_2$ are isomorphic as weighted graphs (via the vertex transposition $\tau = (2\;3)$, which lifts to an isomorphism of the linear dynamics $x(t+1) = W_{G_i} x(t)$), whereas the identity bijection of vertices $\mathrm{id}_V : V \to V$, which preserves the individual binding of output channels $2$ and $3$, is not a morphism of the dynamical systems: $W_{G_1} e_1 = w_1 e_2 + w_2 e_3 \ne w_2 e_2 + w_1 e_3 = W_{G_2} e_1$.*

**Proof (analytical).**
1. Set $\sigma^{(+)}(e) = +1$ and $\sigma^{(-)}(e) = -1$ for all $e \in E$. Then $A^{(-)} = -A^{(+)}$, while $|A_{vu}^{(+)}| = |A_{vu}^{(-)}| = w(u \to v)$ on all edges $e = (u \to v) \in E$. For any initial vector $x(0)$ with $A^{(+)} x(0) \ne 0$, we have $x^{(-)}(1) = A^{(-)} x(0) = -A^{(+)} x(0) = -x^{(+)}(1) \ne x^{(+)}(1)$. In particular, on the two-node graph $V = \{1,2\}$ with a single edge $1 \to 2$ of weight $w(1 \to 2) = 5$ and input $x(0) = (1,0)^{\mathsf{T}}$, we obtain $x^{(+)}(1) = (0, +5)^{\mathsf{T}}$ and $x^{(-)}(1) = (0, -5)^{\mathsf{T}}$.
2. Since $\pi \in \mathrm{Aut}(G, w)$ and the signs $\sigma$ are invariant under $\pi$, the permutation matrix $P_\pi$ commutes with the signed weighted adjacency matrix: $P_\pi W_\sigma = W_\sigma P_\pi$. However, for the diagonal matrix of intrinsic retention coefficients $D_\alpha = \mathrm{diag}(\alpha)$ we have $(P_\pi D_\alpha P_\pi^{-1})_{vv} = \alpha(\pi^{-1}(v))$. Therefore, the commutator $[P_\pi, F] = [P_\pi, D_\alpha + W_\sigma] = [P_\pi, D_\alpha]$ equals zero if and only if $\alpha(\pi(v)) = \alpha(v)$ for all $v \in V$. If $\alpha(2) \ne \alpha(3)$ on a symmetric fork $1 \to 2, 1 \to 3$ with equal weights $w(1 \to 2) = w(1 \to 3) = w_0$, then the transposition $\pi = (2\;3) \in \mathrm{Aut}(G, w)$ violates commutativity: $P_\pi F \ne F P_\pi$.
3. For the graphs $G_1$ and $G_2$ on $V = \{1,2,3\}$ with edges $(1 \to 2), (1 \to 3)$ and weights $(w_1, w_2)$ versus $(w_2, w_1)$ ($w_1 \ne w_2$), the adjacency matrix $W_{G_1}$ maps the basis vector $e_1$ to $w_1 e_2 + w_2 e_3$, whereas the matrix $W_{G_2}$ maps it to $w_2 e_2 + w_1 e_3$. Since $w_1 \ne w_2$, the identity map $\mathrm{id}_V$ does not satisfy the condition $\mathrm{id}_V \circ W_{G_1} = W_{G_2} \circ \mathrm{id}_V$, whereas the permutation $\tau = (2\;3)$ satisfies $P_\tau W_{G_1} = W_{G_2} P_\tau$. Consequently, without fixing which external output functionals are attached to vertices $2$ and $3$, an abstract isomorphism of the graph does not determine the observable response. $\blacksquare$

> **Methodological conclusion.** The claim that "a static graph of positive weights completely determines the dynamics of a system" without explicitly specifying the transmission signs $\sigma(e)$, the internal retention coefficients $\alpha(v)$, and the output-channel map is a category error: it conflates the static graph $G$ with the full operational system $\Gamma$.

---

## §III.2.2. Reconciliation of Overlapping Roles, Unlabelled Vertices, and Question Domain on a Synthetic Graph

By the data traceability rule (`Chapter III.1, §III.1.4`), every quantitative statement about a graph must rest on a fixed primary table and be accompanied by the column name and domain of definition of the filtering predicate. Let us examine the exact combinatorial accounting of overlapping classes on a finite synthetic registry of $40$ vertices that fits into a single table.

Take a directed graph on $40$ vertices numbered $1, \dots, 40$. Two vertices ($39$ and $40$) are auxiliary records: no functional role is assigned to them. The remaining $38$ vertices are labelled with one or two roles out of five: "input", "output", "relay $\alpha$", "relay $\beta$", and "internal". In addition, each row of the table is marked with a binary side attribute: "left" or "right".

### Table III.2.1. Synthetic Role Registry on $40$ Vertices

| Role | Vertices | Count |
| :--- | :--- | :---: |
| input | $1$–$11$ | $11$ |
| output | $12$–$18$ | $7$ |
| relay $\alpha$ | $8, 9, 10$ and $18$–$23$ | $9$ |
| relay $\beta$ | $11$ and $24$–$28$ | $6$ |
| internal | $29$–$38$ | $10$ |
| role unassigned (auxiliary records) | $39, 40$ | $2$ |
| **side "left"** | $1$–$19$, $39$, $40$ | $21$ |
| **side "right"** | $20$–$38$ | $19$ |

### Explanation of the Balance $43 - 5 = 38$ and $38 + 2 = 40$

When working with vertex attribute tables, an apparent contradiction often arises: the sum of role-class cardinalities exceeds the number of labelled vertices. Three combinatorial rules resolve this contradiction completely.

1. **Roles do not form a partition.** The sum of cardinalities of the five role lists equals $11 + 7 + 9 + 6 + 10 = 43$, whereas there are only $38$ labelled vertices. The reason is that exactly five vertices carry two roles simultaneously: three vertices ($8, 9, 10$) belong to "input $\cap$ relay $\alpha$", one vertex ($18$) belongs to "output $\cap$ relay $\alpha$", one vertex ($11$) belongs to "input $\cap$ relay $\beta$", and all triple and higher intersections are empty. The inclusion-exclusion formula gives
   $$
   |\text{input} \cup \text{output} \cup \alpha \cup \beta \cup \text{internal}| = 43 - (3 + 1 + 1) = 38.
   $$
2. **Unlabelled records belong to the table, not to the union of roles.** Together with the two auxiliary vertices, we obtain $38 + 2 = 40$ records. The number $38$ answers the question "how many vertices carry at least one functional role", while the number $40$ answers the question "how many rows are in the table". These are two distinct questions with distinct domains of definition.
3. **The answer to a symmetry question depends on the domain of definition $\mathrm{Dom}(q)$.** Let us ask: are there equally many vertices on the left and right sides? Across all $40$ rows of the table the answer is negative: $21$ on the left versus $19$ on the right. Across the subset of $38$ labelled vertices the answer is affirmative: $19$ on the left ($1$–$19$) versus $19$ on the right ($20$–$38$). The entire apparent asymmetry $21 : 19$ is generated by the two auxiliary records $\{39, 40\}$ outside the role carrier. This is a direct manifestation of the law of `Chapter I.2`: two queries to the very same table yield opposite qualitative conclusions if the domain of definition of the predicate $\mathrm{Dom}(q)$ is not declared prior to counting (`GATE-III02-02`).

---

## §III.2.3. Resolvent Filtration on the Full Graph Versus Threshold Edge Truncation (`0` Loss of Weight Mass)

In the analysis of weighted directed graphs, a crude truncation is frequently applied: all directed arcs with weight below a chosen threshold $\tau$ are deleted from the adjacency matrix for sparsification and "removal of small weights". In the language of Book I (`Chapters I.3` and `I.8`) and Book II (`Chapter II.1`), such threshold zeroing alters the transition carrier itself:
- low-weight arcs that formed the sole bridges between dense components vanish, and a strongly connected graph splits into isolated subsystems;
- individually weak but converging parallel routes are zeroed out before their cumulative contribution is collected at the target vertex.

**Two-triad synthetic benchmark of mass $32$.** Take six vertices $V = (a_1, a_2, a_3, b_1, b_2, b_3)$. Within each triple, draw a directed triangle cycle $a_1 \to a_2 \to a_3 \to a_1$ and $b_1 \to b_2 \to b_3 \to b_1$ with weight $5$ on each arc, and connect the two triples by a pair of opposite bridge arcs $a_1 \to b_1$ and $b_1 \to a_1$ of unit weight $1$. The total weight mass of the graph is $6 \cdot 5 + 2 \cdot 1 = 32$, and the graph is strongly connected (every vertex reaches every other vertex). Threshold truncation $w < 2$ retains mass $30$ (losing only $2/32 = 1/16 = 6.25\%$ of total weight), yet completely destroys mutual reachability between the clusters $\{a_1,a_2,a_3\}$ and $\{b_1,b_2,b_3\}$, splitting the graph into two disconnected strong components.

To separate fast and slow collective modes without deleting edges, one constructs **conservative resolvent filtration on the full weighted matrix** $W$.

### Proposition III.2.1 (Classical Random-Walk Resolvent on a Directed Graph: Conservativity and Zero Loss of Weight Mass)

*Classical foundation.* Neumann series and the random-walk resolvent on a directed graph (L. Katz index, 1953; PageRank core, 1998). *Contribution of this book:* Contrasting the conservative resolvent $\widetilde{P}_\tau$ (`0` mass loss and preserved strong connectivity) against threshold edge truncation as a carrier substitution.

*Let $W = (w_{vu})_{v,u \in V}$ be the full weight matrix of a finite directed graph ($w_{vu} \ge 0$ is the weight of the arrow $u \to v$) in which every vertex has at least one outgoing arrow: $d_u^{\mathrm{out}} = \sum_{v} w_{vu} > 0$. Denote by $M = \mathbf{1}^{\mathsf{T}} W \mathbf{1}$ the total weight mass, $D_{\mathrm{out}} = \mathrm{diag}(d_u^{\mathrm{out}})$, $P = W D_{\mathrm{out}}^{-1}$ the random-walk transition matrix, and $L = I - P$ the random-walk Laplacian. For a scale $\tau > 0$, set*
$$
\widetilde{P}_\tau = (I + \tau L)^{-1} = (1 - \alpha_\tau)\bigl(I - \alpha_\tau P\bigr)^{-1}, \qquad \alpha_\tau = \frac{\tau}{1+\tau} \in (0,1).
$$
*Then:*

1. **Carrier preservation:** *the operator $\widetilde{P}_\tau$ is constructed from the full matrix $W$ without the threshold projector $w \mapsto w\,\mathbf{1}_{w \ge \tau}$; not a single edge and not a single unit of weight is deleted. In the two-triad benchmark, the mass before and after constructing the filter equals $32$, whereas a threshold $\tau = 2$ lowers it to $30$.*
2. **Mass conservation:** *$\widetilde{P}_\tau$ is entrywise nonnegative and column-stochastic ($\mathbf{1}^{\mathsf{T}} \widetilde{P}_\tau = \mathbf{1}^{\mathsf{T}}$), so the filtered weight matrix $\widetilde{W}_\tau = \widetilde{P}_\tau D_{\mathrm{out}}$ preserves the exact total mass $\mathbf{1}^{\mathsf{T}} \widetilde{W}_\tau \mathbf{1} = M$ for every $\tau > 0$.*
3. **Preservation of cross-cluster reachability:** *if the original graph is strongly connected, all matrix entries of $\widetilde{P}_\tau$ are strictly positive ($(\widetilde{P}_\tau)_{vu} > 0$ for all $u, v \in V$), including pairs of vertices joined solely by minimum-weight routes.*
4. **Spectral attenuation of fast modes (symmetric case):** *if $W = W^{\mathsf{T}}$ and $\mathcal{L}_{\mathrm{sym}} = I - D^{-1/2} W D^{-1/2}$ has eigenmodes $\mathcal{L}_{\mathrm{sym}} \psi_k = \lambda_k \psi_k$ ($0 = \lambda_0 \le \lambda_1 \le \dots \le 2$), then the resolvent $(I + \tau \mathcal{L}_{\mathrm{sym}})^{-1}$ multiplies the amplitude of the $k$-th mode by $\frac{1}{1 + \tau \lambda_k}$: slow coherent modes ($\lambda_k \ll 1$) pass with a factor close to $1$, while oscillatory modes ($\lambda_k \sim 1$) are attenuated without breaking the connectivity of the graph.*

**Proof (analytical).** Item (1) follows from the definition of $\widetilde{P}_\tau$ as a rational matrix function of the full matrix $W$. Equality of the two expressions is verified by direct multiplication: $(1+\tau)(I - \alpha_\tau P) = (1+\tau)I - \tau P = I + \tau(I - P) = I + \tau L$. For item (2): $\mathbf{1}^{\mathsf{T}} P = \mathbf{1}^{\mathsf{T}}$ by definition of $D_{\mathrm{out}}$, and since the spectral radius of a column-stochastic matrix equals $1$, we have $\rho(\alpha_\tau P) = \alpha_\tau < 1$. Hence the Neumann series $\widetilde{P}_\tau = (1-\alpha_\tau)\sum_{k=0}^\infty \alpha_\tau^k P^k$ converges absolutely, is entrywise nonnegative, and satisfies $\mathbf{1}^{\mathsf{T}} \widetilde{P}_\tau = (1-\alpha_\tau)\sum_{k=0}^\infty \alpha_\tau^k \mathbf{1}^{\mathsf{T}} = \mathbf{1}^{\mathsf{T}}$; thus $\mathbf{1}^{\mathsf{T}} \widetilde{W}_\tau \mathbf{1} = \mathbf{1}^{\mathsf{T}} \widetilde{P}_\tau D_{\mathrm{out}} \mathbf{1} = \mathbf{1}^{\mathsf{T}} D_{\mathrm{out}} \mathbf{1} = M$. Item (3): under strong connectivity, for every pair $(v, u)$ there exists a path of length $k \ge 0$ with $(P^k)_{vu} > 0$, which for $\alpha_\tau > 0$ and nonnegative series terms gives $(\widetilde{P}_\tau)_{vu} \ge (1-\alpha_\tau)\alpha_\tau^k (P^k)_{vu} > 0$. Item (4) follows from the spectral theorem for the nonnegative self-adjoint operator $\mathcal{L}_{\mathrm{sym}}$ on $\ell_2(V)$. $\blacksquare$

**Exact rational calculation on the $6$-vertex two-triangle graph with a unit bridge.** For the graph on $V = (a_1, a_2, a_3, b_1, b_2, b_3)$, the out-degrees are $d^{\mathrm{out}} = (6, 5, 5, 6, 5, 5)$, and the first column of the transition matrix $P = W D_{\mathrm{out}}^{-1}$ equals $(0, \frac{5}{6}, 0, \frac{1}{6}, 0, 0)^{\mathsf{T}}$. At scale $\tau = 1$ ($\alpha_\tau = \frac{1}{2}$), exact inversion of the rational matrix $2I_6 - P$ over $\mathbb{Q}$ gives the first column of the resolvent $\widetilde{P}_1 = \frac{1}{2}\bigl(I_6 - \frac{1}{2}P\bigr)^{-1} = (2I_6 - P)^{-1}$:
$$
\widetilde{P}_1(:, a_1) = \left(\frac{344}{611},\; \frac{430}{1833},\; \frac{215}{1833},\; \frac{32}{611},\; \frac{40}{1833},\; \frac{20}{1833}\right)^{\!\mathsf{T}}, \qquad \frac{344}{611} + \frac{430 + 215}{1833} + \frac{32}{611} + \frac{40 + 20}{1833} = 1.
$$
The smallest matrix entry across the entire $6 \times 6$ matrix $\widetilde{P}_1$ equals $\min_{v,u} (\widetilde{P}_1)_{vu} = \frac{5}{1833} > 0$ (transfer from $a_3$ to $b_3$ across the weight-$1$ bridge is strictly positive), and the filtered weight matrix $\widetilde{W}_1 = \widetilde{P}_1 D_{\mathrm{out}}$ preserves the exact total mass $\mathbf{1}^{\mathsf{T}}\widetilde{W}_1\mathbf{1} = 32$ for every rational $\tau > 0$ (`GATE-III02-02`, `GATE-III02-03`).

> **Boundary between direct edges of a single graph and model gluing of two graphs.** Whenever two directed weighted graphs $\mathcal{G}_{\mathrm{I}}$ and $\mathcal{G}_{\mathrm{II}}$ are defined on two independent carriers and linked by a boundary type-matching table $\mathcal{B}_{\mathrm{I \leftrightarrow II}}$, the edge matrix inside each graph $\mathcal{G}_{\mathrm{I}}, \mathcal{G}_{\mathrm{II}}$ belongs to the level of a primary table (`L2`), whereas the inter-graph gluing operator $\mathcal{B}_{\mathrm{I \leftrightarrow II}}$ belongs to the level of a bridge model (`L3`): in the language of `Chapter II.3`, its seam compatibility must be verified explicitly and never conflated with direct edges of a single graph.

---

## §III.2.4. Domain Bridge Passport for `Chapter III.2` (`DB-01`: Directed Weighted Graphs and Resolvent Filtration)

| No. | Passport Row | Content for Bridge `Chapter III.2` (`DB-01`) |
| :---: | :--- | :--- |
| **1** | **Subject and primary data** | Finite directed weighted graphs $G = (V, E, w)$ and tables of overlapping vertex attributes: the $40$-vertex synthetic registry (`Table III.2.1`) and the $6$-vertex two-triad graph of total mass $M = 32$. |
| **2** | **Quantities, scales, and procedure** | State vector $x(t) \in \mathbb{Q}^{|V|}$, full weight matrix $W$, transmission signs $\sigma : E \to \{+1,-1\}$, retention diagonal $D_\alpha = \mathrm{diag}(\alpha)$, and rational random-walk resolvent $\widetilde{P}_\tau = (1-\alpha_\tau)(I - \alpha_\tau P)^{-1}$. |
| **3** | **Split prior to fitting** | The matrix $W$, signs $\sigma$, coefficients $\alpha(v)$, and domain of definition $\mathrm{Dom}(q)$ of every counting predicate are fixed prior to computing responses and filtration. |
| **4** | **Free choices and degrees of freedom** | In `Lemma III.2.1` and `Proposition III.2.1` there are **`0`** fitting parameters; the positive scale parameter $\tau \in \mathbb{Q}_{>0}$ enters explicitly into the definition of the resolvent $\widetilde{P}_\tau$. |
| **5** | **Null and surrogate control** | 1) Sign inversion $\sigma \mapsto -\sigma$ with fixed modulus matrix $W$ (`Lemma III.2.1(1)`); 2) transposition of unequal weights $w_1 \ne w_2$ (`Lemma III.2.1(3)`); 3) hard threshold truncation $w < 2$ (mass drop $32 \to 30$ and split into $2$ components) versus the resolvent $\widetilde{P}_\tau$. |
| **6** | **Pre-specified comparison and full cost** | Verification of inclusion-exclusion $43 - 5 = 38$, $38 + 2 = 40$, side-balance shift $21 : 19 \to 19 : 19$, column stochasticity $\mathbf{1}^{\mathsf{T}}\widetilde{P}_\tau = \mathbf{1}^{\mathsf{T}}$, mass conservation $\mathbf{1}^{\mathsf{T}}\widetilde{W}_\tau\mathbf{1} = 32$, and lower bound $\min \widetilde{P}_1 = 5/1833 > 0$ under exact rational inversion over $\mathbb{Q}$. |
| **7** | **Falsification condition and reproducibility** | Any claim that an unsigned matrix $W$ alone specifies dynamics without $(\sigma, \alpha)$ or that hard thresholding preserves strong connectivity on bridge graphs is refuted by the finite counterexamples `GATE-III02-01..03` in the single-threaded verifier `07_verify_full_book_III_v3_3.jl`. |
| **8** | **Position of the Observer in the bridge ($\Gamma, \iota, \mathcal{O}_\pi$)** | The observer holds the cut $\iota$ (choice of dynamical operator $F = D_\alpha + W_\sigma$ or filter $\widetilde{P}_\tau$ on the full carrier $V$) and the readout procedure $\mathcal{O}_\pi$ (domain $\mathrm{Dom}(q)$ and output-channel binding). The role of an ungluable triple of local descriptions is played by $(W, \sigma, \alpha)$ in `Lemma III.2.1`: knowing any two components without the third leaves dynamic transfer ambiguous. |

---

### What This Chapter Transmits to the Next (`Chapter III.2` $\to$ `Chapter III.3`)

In `Chapter III.2` we saw that even a complete matrix of weighted arrows is not identical to an operating discrimination loop: one must separate the observed carrier, the transmission instrument (edge signs and resolvent), internal memory retention, and the position of the one who fixes the domain of definition $\mathrm{Dom}(q)$ and reads out the answer. Precisely this task—**distinguishing functional roles in the act of cognition and action and analyzing the failures that occur when the witness is glued to the instrument**—was developed in the classical Indian analytical schools (*Sāṃkhya, Yoga, Advaita Vedānta*, and *Pāṇini's* formal grammar). In `Chapter III.3` we construct an exact mathematical bridge for these traditions on the pair graphs $\mathrm{KG}(5,2)$, $J(5,2)$, and the octahedron $O_6$, separating level-`L1` combinatorial theorems from the level-`L4` hermeneutic dictionary.
