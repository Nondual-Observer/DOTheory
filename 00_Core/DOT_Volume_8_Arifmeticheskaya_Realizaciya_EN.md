# Distinction Observable Theory

# Volume 8. Arithmetic realization

The subject of this volume is the arithmetic realization of the carrier. In Volumes 0–7 the carrier was built abstractly: $\mathbb F_2^n$ as the orbit of a self-relation. Here it is shown that this carrier has a canonical concrete instance — the divisor lattice of a number — and that the entire grammar of the scene is realized on it verbatim: a squarefree number yields the cube, the number 30 yields the rank-3 scene with its four relations, and the multiplicities yield a second axis of growth.

The realization is rigorous: this is not an analogy but a finite isomorphism of carriers. The status is marked explicitly — where the isomorphism is proved, where it is a bridge, where it is a horizon.

---

# Section 0. Starting point

The rank-$n$ carrier is $Q_n = \mathbb F_2^n$ (Volume 0), built as the orbit of an involution with complement $\kappa$. This construction is abstract. Arithmetic gives it a concrete body: the divisors of a number. The divisor lattice of a squarefree number is the rank-$n$ carrier verbatim, with the complement $d \mapsto N/d$ in place of $\kappa$. The realization of this instance is the subject of the volume.

---

# Section 1. The number as a carrier of divisors

## §1.1. The carrier and its lattice

For a number $N = p_1^{a_1}\cdots p_r^{a_r}$ the carrier of divisors is

$$
D(N) = \{d \in \mathbb N : d \mid N\}.
$$

Each divisor $d = p_1^{b_1}\cdots p_r^{b_r}$ is given by the exponent vector $(b_1,\dots,b_r)$ with $0 \le b_i \le a_i$. This yields an isomorphism of the carrier with a product of chains (proved):

$$
\boxed{
D(N) \cong \prod_{i=1}^{r}\{0,1,\dots,a_i\}.
}
$$

Divisibility is the coordinatewise order ($d \mid e \Leftrightarrow b_i \le c_i$); meet and join are $\gcd$ and $\mathrm{lcm}$; the lower pole is $1$, the upper is $N$. The covering graph (multiplication or division by a single prime factor) is a product of paths:

$$
(D(N), C_N) \cong P_{a_1+1}\,\square\,\cdots\,\square\,P_{a_r+1}.
$$

## §1.2. Divisor duality

The map

$$
\delta_N(d) = \frac{N}{d}
$$

is an involution ($\delta_N^2 = \operatorname{id}$), order-reversing ($d \mid e \Leftrightarrow \delta_N(e) \mid \delta_N(d)$), interchanging the poles ($1 \leftrightarrow N$). In coordinates it reflects each chain: $b_i \mapsto a_i - b_i$. This is the arithmetic image of the complement $\kappa$ (Volume 0).

---

# Section 2. The squarefree number as a cube

## §2.1. Isomorphism with the cube

For squarefree $N = p_1\cdots p_n$ all $a_i = 1$, and each chain becomes binary. The map $\theta_N(x) = \prod_{i:x_i=1} p_i$ is a bijection $Q_n \to D(N)$ (proved):

$$
\boxed{
D(p_1\cdots p_n) \cong Q_n.
}
$$

## §2.2. Compatibility of the grammar

The isomorphism preserves not only the set of states but the entire grammar of the scene (proved, compatibility theorem):

$$
\boxed{
\begin{aligned}
&\text{poles}: && \theta_N(0^n) = 1, \quad \theta_N(1^n) = N;\\
&\text{weight}: && w(x) = \omega_N(\theta_N(x));\\
&\text{order}: && x \le y \Leftrightarrow \theta_N(x) \mid \theta_N(y);\\
&\text{complement}: && \theta_N(\bar x) = N/\theta_N(x);\\
&\text{covering}: && d_H(x,y) = 1 \Leftrightarrow \{\theta_N(x),\theta_N(y)\} \in C_N.
\end{aligned}
}
$$

Boolean complement is divisor duality, Hamming weight is the number of prime factors, the Hamming step is passage by a single prime factor. Puncturing the poles yields the proper carrier:

$$
D^\circ(N) = D(N)\setminus\{1,N\} \cong U_n.
$$

This is a finite isomorphism, not an analogy. The bridge-reading begins only at the words "arithmetic realization of the Boolean core": a squarefree number carries $n$ independent prime coordinates, a divisor is their state, the conjugate divisor is the complement.

---

# Section 3. The rank-3 scene: the number 30

## §3.1. Avatar of the scene

The first squarefree number of three primes is $30 = 2\cdot3\cdot5$. Its proper carrier (proved):

$$
\boxed{
D^\circ(30) = \{2,3,5,6,10,15\} \cong Q_3\setminus\{000,111\} = U_3.
}
$$

In the basis $(2,3,5)$: the layers are $S_1 = \{2,3,5\}$ (atoms), $S_2 = \{6,10,15\}$ (coatoms); the complement pairs are $2\leftrightarrow15$, $3\leftrightarrow10$, $5\leftrightarrow6$. This is the rank-3 scene of Volume 1 point for point.

![Figure 8.1. The proper divisors of 30 as an octahedral scene](../assets/figures/365.png)

*Figure 8.1. The proper divisors of the number $30 = 2\cdot3\cdot5$ form the rank-3 scene: six divisors, the complement $d \mapsto 30/d$, three axial pairs — the arithmetic realization of the octahedron.*

## §3.2. The four relations

On $D^\circ(30)$ four relations realize the four relations of Volume 1 (each proved):

$$
\boxed{
C_{30}^\circ \cong C_6, \qquad R_{\mathrm{sh}} \cong K_3\sqcup K_3, \qquad R_{\pm} \cong 3K_2, \qquad R_{\mathrm{oct}} \cong K_{2,2,2}.
}
$$

Covering by a single prime factor yields the cycle $C_6$ (relation $R_1$); the within-layer relation yields $K_3\sqcup K_3$ (relation $R_2$); divisor complement yields $3K_2$ — the three $\delta_{30}$ pairs (relation $R_3$); the inter-pair octahedral relation yields $K_{2,2,2}$ (relation $R_1\cup R_2$). The carrier, the puncturing, the layers, the complement pairs, the covering step, the octahedron all coincide — the entire relation-grammar of rank 3.

## §3.3. Axial reading

The quotient by the complement yields three orbits (proved), and after a choice of side

$$
D^\circ(30) \cong I_{30}\times\{-,+\}, \qquad I_{30} = \{\langle2\rangle,\langle3\rangle,\langle5\rangle\}.
$$

Each axis is a pair of an atom and a coatom $(p_i, N/p_i)$ — a manifested prime coordinate and the holding complement. This is the arithmetic image of the three axes of rank 3 (Volume 1) and of the original motif $P = \{a, -a\} \to I$ (Volume 0): three axial invariants, each with two poles. The reading of the three axes as directions has the status of a bridge; the rigorous part is the involution $d\mapsto N/d$ and its three orbits.

---

# Section 4. The active scene and the outer layer

## §4.1. Two objects, coinciding at rank 3

The proper carrier yields the full active scene $U_n = \bigsqcup_{1\le k\le n-1} S_k$ — all interior layers. The outer layer is only atoms and coatoms:

$$
V_n = S_1 \sqcup S_{n-1} = \{p_i\} \sqcup \{N/p_i\}, \qquad |V_n| = 2n.
$$

For $n = 3$ the interior layers are only $S_1, S_2$, and therefore (proved)

$$
U_3 = V_3.
$$

For $n \ge 4$ the inclusion is strict, $V_n \subsetneq U_n$: an interior layer $S_2$ appears that does not lie in the outer one. At rank 4: $D^\circ(210) \cong U_4$ (14 points), whereas $V_4 = \{2,3,5,7,105,70,42,30\}$ (8 points), with the inter-pair relation $(V_4, R_{\mathrm{noncomp}}) \cong K_{2,2,2,2}$ — the graph of the 16-cell.

## §4.2. The coincidence as the cause of the purity of rank 3

That the number 30 fits so exactly into the rank-3 scene is a consequence of the coincidence $U_3 = V_3$: at rank 3 the proper divisor carrier and the outer axial layer are one. At rank 4 they diverge — this is the arithmetic side of the break (Volume 2): the birth of the interior layer is the separation of the full active scene $U_n$ from the outer axial $V_n$.

---

# Section 5. The ladder of primorials

The ladder of carriers is realized by the primorials $N_n = p_1\cdots p_n$ (proved):

$$
\begin{array}{r|r|r|l}
n & N_n & |D^\circ(N_n)| & \text{scene}\\
\hline
1 & 2 & 0 & \text{no proper scene}\\
2 & 6 & 2 & \text{one complement pair}\\
3 & 30 & 6 & \text{first hexad, } U_3 = V_3\\
4 & 210 & 14 & U_4 \ne V_4\\
\end{array}
$$

A primorial is the minimal squarefree number of $n$ primes, and therefore the primorials are the minimal carriers of the ranks. The ladder of primorials realizes the rank-growth of the abstract carrier: rank 1 — two poles without a scene, rank 2 — one pair, rank 3 — the first full scene, rank 4 — the break.

---

# Section 6. The second axis of growth

## §6.1. Rank-growth and depth-growth

The chain extension for general $N$ introduces a distinction that the cube does not carry. The carrier grows in two ways.

Rank-growth — the addition of a new prime factor $N \mapsto N p_{r+1}$: a new binary coordinate $\{0,1\}$ is added, the carrier doubles. This is the lift of Volume 3 — a new axis of distinction.

Depth-growth — the raising of a multiplicity $p_i^{a_i} \mapsto p_i^{a_i+1}$: the coordinate chain lengthens $\{0,\dots,a_i\} \mapsto \{0,\dots,a_i+1\}$, the rank does not change.

$$
\boxed{
\text{rank-growth adds a coordinate (lift); depth-growth lengthens a coordinate.}
}
$$

The Boolean core sees only rank-growth — each coordinate holds only two values. The chain extension adds depth-growth: the passage from binary distinction to many-valued.

## §6.2. The center as a vertex in the depth direction

The duality $\delta_N(d) = N/d$ has a fixed point if and only if $N$ is a perfect square (proved):

$$
\boxed{
\delta_N(d) = d \quad\Longleftrightarrow\quad d^2 = N \quad\Longleftrightarrow\quad d = \sqrt N.
}
$$

In the squarefree case all $a_i = 1$ are odd, there is no fixed point — the center is a centroid outside the vertices (Volume 0, Volume 7). When $N$ is a perfect square (all $a_i$ even) the fixed point is unique and is the vertex $\sqrt N$. Example: $\delta_{36}(6) = 6 = \sqrt{36}$.

This is the arithmetic realization of the question of Volume 7 — when the observer-center is a vertex. In the cube (rank-growth) the center is never a vertex. In the depth direction (multiplicity-growth) the center becomes a vertex exactly for perfect squares. Thus the second axis of growth carries what is absent on the first: the realization of the center by a state.

## §6.3. Status

The chain extension is rigorous as the finite arithmetic of lattices (the product of chains, the covering graph, the duality, the fixed-point criterion — all proved). Its reading as an extension of the theory beyond the binary core is a horizon: the binarity of rank comes from the foundation-forming involution (two sides), whereas depth-growth leads off to many-valued distinction, and the full theory of relations and recoveries on products of chains remains open.

Behind the chain extension lies one more level — the Birkhoff horizon. The carriers form a ladder: Boolean lattices $\subset$ products of chains $\subset$ finite distributive lattices. By Birkhoff's theorem every finite distributive lattice is $L \cong J(P)$ — the lattice of lower ideals (down-sets) of a finite partially ordered set $P$; a product of chains corresponds to a disjoint $P = C_{a_1}\sqcup\cdots\sqcup C_{a_r}$ (the coordinates are independent). Beyond products of chains the coordinates become dependent: when $x \le y$ the ideal containing $y$ must contain $x$, and the state cannot be assembled as an independent profile. This is a third direction of generalization — after rank (a new coordinate) and depth (the lengthening of a coordinate) — the dependence of coordinates. Its status is a horizon: the carrier $J(P)$, the relations and recoveries on it require a separate theory.

---

# Section 7. The second realization: the graph product

The divisor lattice is not the only arithmetic realization of the scene. There is a second, the graph one, and at rank 3 it is more economical. This construction should be held apart from the divisor one: it is built differently and is marked as a model choice, not one forced by the whole of arithmetic.

## §7.1. The graph product of complete graphs

To each prime factor of the number $N = \prod_i p_i$ (with multiplicity) assign a complete graph $K_{p_i}$ and form the Cartesian product

$$
\Gamma(N) = \square_i K_{p_i}.
$$

The vertices are tuples $(v_1,\dots,v_k)$, $v_i \in \{0,\dots,p_i-1\}$; two are adjacent when they differ in exactly one coordinate (complete layers). The number of vertices is the number itself:

$$
|V(\Gamma(N))| = \prod_i p_i = N.
$$

This is a carrier different from the divisor lattice: $\Gamma(N)$ takes $N$ vertices (the number itself), $D(N)$ takes the divisors (of which there are $\prod(a_i+1)$). The assignment $p \mapsto K_p$ is canonical within the corpus but not forced by arithmetic — it is a model choice.

The degree and the residual degree are computed directly (proved). A vertex in coordinate $i$ has $p_i - 1$ neighbors, and therefore

$$
d_\Gamma(N) = \sum_i (p_i - 1).
$$

The complement $\overline{\Gamma(N)}$ in the complete graph $K_N$ has degree

$$
d_{\mathrm{res}}(N) = (N-1) - \sum_i(p_i-1) = \Delta(N) + k - 1, \qquad \Delta(N) := N - \sum_i p_i,
$$

where $k$ is the number of prime factors with multiplicity. The arithmetic quantity $\Delta(N)$ — the excess of the number over the sum of its primes — is recovered from a graph invariant as the residual degree of the complement.

## §7.2. Realization of the rank-3 scene by the number 6

The minimal product of two primes yields the rank-3 scene (proved in the graph model). For $N = 6 = 2\cdot3$ the graph

$$
\Gamma(6) = K_2 \square K_3
$$

is the triangular prism on six vertices $(a,b)$, $a \in \{0,1\}$, $b \in \{0,1,2\}$. The edges split into two types: for fixed $a$ the three vertices give a triangle (two triangles, $2K_3$); for fixed $b$ the two vertices give an edge (three edges, $3K_2$). The complement in $K_6$ joins the vertices differing in both coordinates and is a six-cycle. Hence

$$
\boxed{
\Gamma(6) = 2K_3 \cup 3K_2 \;\,(R_2 \cup R_3), \qquad \overline{\Gamma(6)} \cong C_6 \;\,(R_1), \qquad K_{2,2,2} = \overline{3K_2} \;\,(R_{\mathrm{oct}}).
}
$$

This is the relation-grammar of rank 3 (Volume 1): the covering $C_6$, the layer $K_3\sqcup K_3$, the complement $3K_2$, the octahedron $K_{2,2,2}$. That is, $\Gamma(6)$ is the second arithmetic realization of the rank-3 nucleus.

It is consistent with the first. The coordinates of the prism give the axial reading of §3.3 verbatim: the $K_2$-layers (fixed $b$) are the complement pairs $3K_2$, hence $b$ is the axis (the three axes $I_3$), and $a$ is the pole of the pair ($\{-,+\}$); the $K_3$-layers (fixed $a$) are the two triangles — two shells, and the complement changes $a$. Hence

$$
\Gamma(6) \cong D^\circ(30) \cong I_3 \times \{-,+\}
$$

as a relation-schema: the ternary coordinate is the axis, the binary one is the pole. The rank-3 nucleus is one; the realizations are two.

The subtlety that makes this nontrivial: for one and the same number 6 the two constructions give different ranks. The divisor picture gives rank 2 ($D^\circ(6) = \{2,3\}$, one complement pair), the graph product gives the rank-3 scene on six vertices. There is no contradiction — these are different carriers: $D(6)$ is built on four divisors, $\Gamma(6)$ on six vertices. The divisor realization carries the carrier $Q_n$ (the rank equals the number of distinct primes); the graph one carries the relation-schema on $N$ vertices.

## §7.3. The dyad-triad tower

The graph product builds a ladder in two directions (proved in the graph model). For $N = 2^a 3^b$:

$$
\Gamma(2^a 3^b) = K_2^{\square a} \square K_3^{\square b} = H(a,2) \square H(b,3),
$$

that is, the hypercube $H(a,2) = Q_a$ multiplied by the ternary Hamming graph $H(b,3) = K_3^{\square b}$. The degree is $a + 2b$. The layerwise recursion: fixing one binary coordinate yields $\Gamma_{a-1,b}$, fixing one ternary coordinate yields $\Gamma_{a,b-1}$. Each floor contains both directions of growth.

The dyadic direction (adding $K_2$) is the lift of Volume 3 — a new binary coordinate, $Q_a = K_2^{\square a}$ is our cube. The triadic direction (adding $K_3$) is new: a new ternary coordinate with complete adjacency. It should be distinguished from the depth-growth of §6: there the multiplicity $p^2$ lengthened a coordinate into the chain $\{0,1,2\}$ (the path $P_3$) within the divisor lattice; here the prime 3 gives the complete triangle $K_3$, and $3^2$ gives the product $K_3 \square K_3$, not a chain. The graph product and the divisor multiplicity are different constructions on the same number.

## §7.4. Status and consistency

The graph model $\Gamma(N) = \square K_{p_i}$ is a model choice — canonical within the corpus but not forced by the whole of arithmetic. Within the model the degree and residual identities, the realization $\Gamma(6)$ and the tower $\Gamma(2^a3^b)$ are proved as the finite combinatorics of graphs. This is a realization at the level of an object, not a functor: it does not build a full mapping of arithmetic into the core, and this is its own boundary.

There is no conflict with the divisor realization (§1–§6). The two constructions assign different finite objects to a number — divisors versus vertices — and both carry structures of the theory: the divisor one gives the carrier $Q_n$ and its growth, the graph one gives the relation-schema of rank 3 on $\Gamma(6)$ and the dyad-triad ladder. At rank 3 they converge to one nucleus $I_3\times\{-,+\}$ by different paths, which confirms its realizational invariance.

---

# §8. Summary of Volume 8

The abstract carrier of Volume 0 has a canonical arithmetic instance — the divisor lattice. The realization is rigorous, proved by theorems:

$$
D(N) \cong \prod_i\{0,\dots,a_i\}, \qquad D(p_1\cdots p_n) \cong Q_n,
$$

with full compatibility of the grammar (poles, weight, order, complement $N/d$, covering as the Hamming step). A squarefree number is the cube; the number 30 yields the rank-3 scene with four relations ($C_6$, $K_3\sqcup K_3$, $3K_2$, $K_{2,2,2}$), three axis-pairs and the axial reading $I_3\times\{-,+\}$ — the scene of Volume 1 verbatim.

The active scene $U_n$ (the proper carrier) and the outer axial layer $V_n$ coincide at rank 3 and diverge at rank 4 — the arithmetic side of the break (Volume 2). The ladder of primorials realizes rank-growth.

The chain extension yields a second axis of growth: rank-growth (the lift, a new coordinate) and depth-growth (the lengthening of a coordinate, the passage to many-valued). In the depth direction the center becomes the vertex $\sqrt N$ for perfect squares — the arithmetic realization of the center-vertex of Volume 7.

Besides the divisor one, the rank-3 scene carries a second, graph realization: the graph product $\Gamma(6) = K_2\square K_3$ (the triangular prism) gives the same four relations, and $\Gamma(6) \cong D^\circ(30) \cong I_3\times\{-,+\}$ as a schema. The dyad-triad tower $\Gamma(2^a3^b) = H(a,2)\square H(b,3)$ grows by the addition of $K_2$ (a lift) or of a new ternary coordinate $K_3$. The graph model is a model choice, not a functor; the rank-3 nucleus is one, the realizations are two, which confirms its realizational invariance.

$$
\boxed{
\text{a squarefree number realizes the carrier and the scene; multiplicity opens a second axis of growth, on which the center becomes a vertex.}
}
$$

The readings of this realization, its multiplicative structure and the residue bridge are the subject of the following volume.
