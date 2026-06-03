# Distinction Observable Theory

# Volume 9. The arithmetic structure beyond the cube

The subject of this volume is the structure that the abstract carrier does not carry but that the arithmetic realization (Volume 8) lays bare. On the divisor lattice there is a multiplicative operation, a recovery discipline for readings, and a second carrier — the residues — connected to the divisors through the greatest common divisor. And on the rank-3 scene there is a horizontal algebra $\mathfrak{sl}_3$, complementary to the vertical $\mathfrak{sl}_2$ of the observer.

This volume adds to the theory what was not present in the abstract volumes. The status is marked explicitly: where it is rigorous arithmetic, where a bridge, where a horizon.

---

# Section 0. Starting point

The abstract carrier (Volume 0) carried order, complement, boundary, rotation — an additive-order structure. The arithmetic realization (Volume 8) carries beyond this: divisors can be multiplied, readings carry recovery data, and residue classes project onto the divisors. These layers — the multiplicative, the recovery, the residue — are the subject of the volume.

---

# Section 1. The multiplicative monoid

## §1.1. Partial multiplication

On the carrier of divisors there is an operation absent from the abstract carrier — multiplication. It is partial: the product remains in the carrier only under a capacity condition (proved):

$$
\boxed{
d \odot_N e = de \quad\text{if}\quad \eta_N(d) + \eta_N(e) \le (a_1,\dots,a_r) \text{ coordinatewise.}
}
$$

The structure $(D(N), \odot_N, 1)$ is a partial commutative monoid with unit $1$ (proved: commutativity, unit, associativity wherever defined). In the squarefree case the operation is defined exactly when $\gcd(d,e) = 1$ (disjoint prime supports), and then $d \odot_N e = \mathrm{lcm}(d,e)$.

## §1.2. Complement pairs as maximal products

The product of a divisor with its complement is the upper pole (proved):

$$
\boxed{
d \odot_N \frac{N}{d} = N,
}
$$

and if $d \odot_N e = N$, then $e = N/d$. The complement pairs are the maximal admissible products — the only pairs whose product attains the pole. The three complement pairs of the number 30 ($2\odot15$, $3\odot10$, $5\odot6$, all equal to 30) are the three axes of rank 3, read multiplicatively.

## §1.3. The leakage boundary

Multiplication requires the full carrier as the boundary of closure. On the active scene $D^\circ(N) = D(N)\setminus\{1,N\}$ it does not close: inputs from the active scene can give the pole (for example $2 \odot_{30} 15 = 30 \notin D^\circ$). The lower pole is not attained under direct multiplication ($d, e > 1 \Rightarrow de > 1$). Therefore

$$
\odot_N : D^\circ(N) \times D^\circ(N) \dashrightarrow D(N),
$$

and not into $D^\circ(N)$. This gives a multiplicative cause for the poles: the upper pole is where the products of complements close up. The puncturing removes the poles from the active scene, but the multiplicative closure keeps them as a boundary — what is removed from the scene is not annihilated in the carrier (Volume 0).

---

# Section 2. The recovery discipline

## §2.1. Reading and recovery

On the carrier of divisors there are several layer-readings that diverge outside the cube: the full multiplicity $\Omega_N(d) = \sum b_i$, the number of active coordinates $\omega_N(d) = |\{i : b_i>0\}|$, the coordinate support $\mathrm{supp}_N(d)$. In the squarefree case they coincide; under multiplicities they diverge. Each reading carries recovery data — what is needed to return a state from its image.

## §2.2. Faithfulness of a reading and squarefreeness

The support reading is faithful (recovers the divisor uniquely) if and only if $N$ is squarefree (proved):

$$
\boxed{
\mathrm{supp}_N \text{ is faithful on } D(N) \quad\Longleftrightarrow\quad N \text{ is squarefree.}
}
$$

Under multiplicities $p_i$ and $p_i^2$ have the same support but are distinct — the support ceases to be a point of the carrier and becomes a coarse reading. Faithful recovery in the general case yields only the full exponent vector.

## §2.3. Realizations and projections

This refines the atlas of readings (Volume 6). A reading is either a realization — an isomorphism, the recovery is faithful, nothing is lost (the divisor carrier of a squarefree number, as well as the Boolean algebra and the color cube) — or a lossy projection, where the recovery is a fiber, not a point (the support under multiplicities, the spectrum, the semantics). The recovery discipline is the exact criterion by which a reading belongs to one kind or the other: a realization carries an inverse map, a projection carries a fiber.

---

# Section 3. The residue bridge

## §3.1. The second carrier

Besides the carrier of divisors $D(N)$ there is a second finite carrier — the residue classes $\mathbb Z/N\mathbb Z$. They are connected by the greatest common divisor:

$$
q_{\gcd} : \mathbb Z/N\mathbb Z \to D(N), \qquad q_{\gcd}([a]) = \gcd(a, N).
$$

This is a reading of a residue through a divisor — a projection of the larger carrier (residues) onto the smaller (divisors).

## §3.2. The fiber theorem

The fiber over a divisor $d$ is the group of invertible classes of the smaller modulus (proved):

$$
\boxed{
|q_{\gcd}^{-1}(d)| = \varphi(N/d), \qquad q_{\gcd}^{-1}(d) \cong (\mathbb Z/(N/d)\mathbb Z)^\times.
}
$$

The fibers partition the entire carrier of residues, which yields the classical identity

$$
\sum_{d \mid N} \varphi(N/d) = N.
$$

This is a lossy reading: the divisor is recovered faithfully, the original residue class only up to an invertible factor in the fiber. The CRT decomposition fixes the zero-pattern of the fiber (proved), and the zero-product relation on residues is determined by the gcd states — the projection of the zero divisors.

## §3.3. Status

The residue bridge is rigorous as finite arithmetic (the fiber $\varphi(N/d)$, CRT, the zero divisors — proved). Its place in the theory is a bridge: the residues are a second carrier casting a shadow onto the carrier of divisors through the gcd. This is not a realization of the scene but a connection of two arithmetic carriers, held by the reading $q_{\gcd}$ with its fibers.

---

# Section 4. The horizontal algebra sl₃

## §4.1. Six points as 3 and the conjugate 3

The rank-3 scene $D^\circ(30) = \{2,3,5,6,10,15\}$ is split by the relation $K_3\sqcup K_3$ into two three-point layers:

$$
S_1 = \{2,3,5\}, \qquad S_2 = \{6,10,15\},
$$

and the complement $\delta_{30}$ gives a duality between them ($2\leftrightarrow15$, $3\leftrightarrow10$, $5\leftrightarrow6$). This yields a reading of the six points as the triplet and antitriplet of the algebra $\mathfrak{sl}_3/\mathfrak{su}(3)$:

$$
\boxed{
\{2,3,5\} \leftrightarrow \mathbf 3, \qquad \{6,10,15\} \leftrightarrow \bar{\mathbf 3}.
}
$$

The prime coordinates are the three weights of the fundamental layer, the complementary divisors are the dual layer; $K_3\sqcup K_3$ gives the two components, $\delta_{30}$ gives the duality.

## §4.2. Horizontal versus vertical

This algebra is complementary to the structure of the observer (Volume 7). There the vertical is $\mathfrak{sl}_2$ — boundary, coboundary, the grading by layers. Here the horizontal is $\mathfrak{sl}_3$ — the six points of a single layer as $\mathbf 3 \oplus \bar{\mathbf 3}$. The vertical $\mathfrak{sl}_2$ moves between layers; the horizontal $\mathfrak{sl}_3$ reads the six points as the fundamental representation with its conjugate.

$$
\boxed{
\text{vertical: } \mathfrak{sl}_2 \text{ (layers, Volume 7)}; \qquad \text{horizontal: } \mathfrak{sl}_3 \text{ (six points as } \mathbf 3 \oplus \bar{\mathbf 3}).
}
$$

This is a rich parallel, not an identity: two different algebras on two slices of the scene.

## §4.3. Status and adjacent readings

The $\mathfrak{sl}_3$ reading is a bridge: rigorously built are the carrier $D^\circ(30)$, the layers, the relation $K_3\sqcup K_3$ and the involution $\delta_{30}$; the Lie-algebraic names are a reading of these finite data, not a new algebra within the carrier. The complement $\delta_{30}$ is also read as the arithmetic image of the half-return $T^3 = \kappa$ (Volume 4) — a connection with the axial blocks of rank 3. Further images — the Hopf fibration, the Möbius function as a reading of the boundary between the squarefree and the multiple — are separate bridge and horizon lines; the Hopf line is disputable and is not developed here.

---

# §5. Summary of Volume 9

The arithmetic realization carries structure that the abstract carrier does not have.

The multiplicative monoid $(D(N), \odot_N, 1)$ — a partial operation with a capacity condition (proved); the complement pairs are the maximal products $d\odot N/d = N$; multiplication leaks into the upper pole, giving a multiplicative cause for the poles as the boundary of closure.

The recovery discipline: the support reading is faithful if and only if the number is squarefree (proved). This refines the atlas of readings (Volume 6): a reading is a realization (an isomorphism, an inverse map) or a projection (a fiber), and the criterion of faithfulness separates them.

The residue bridge: a second carrier — the residues $\mathbb Z/N\mathbb Z$ — connected to the divisors through $q_{\gcd}([a]) = \gcd(a,N)$, with the fiber $\varphi(N/d)$ (proved) and the identity $\sum_{d\mid N}\varphi(N/d) = N$. A connection of two arithmetic carriers with the status of a bridge.

The horizontal algebra: the six points $D^\circ(30)$ as $\mathbf 3 \oplus \bar{\mathbf 3}$ of the algebra $\mathfrak{sl}_3$ — a parallel to the vertical $\mathfrak{sl}_2$ of the observer (Volume 7); the vertical moves between layers, the horizontal reads a single layer. The status of a bridge.

$$
\boxed{
\text{the carrier of divisors carries multiplication, the recovery discipline and the residue bridge; the rank-3 scene carries the horizontal } \mathfrak{sl}_3 \text{ alongside the vertical } \mathfrak{sl}_2.
}
$$
