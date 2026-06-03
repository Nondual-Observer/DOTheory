# Distinction Observable Theory

# Volume 3. The Vertical

The subject of this volume is the vertical movement of distinction. Until now the vertical has appeared in two forms: the lift, which increases the rank, and the boundary, which moves between layers within a rank. Here a boundary complex on a single rank is constructed, it is established that the lift and the coboundary are one and the same increment at different scopes, and the adjoint descent is introduced.

The functorial reading, noted in Volume 0 as a separate track, becomes here the working language: the adjoint pair and the chain complex are what the categorical language expresses exactly. The combinatorial meaning remains leading, the categorical one runs in parallel.

---

# Section 0. Starting Point

The relations $R_d$ compare states within a single layer by distance; the complement $\kappa$ links a state with its limit complement; the lift $\Lambda$ increases the rank. Between layers of different weight within a single rank there has so far been no movement. The boundary between weights is the third vertical movement, and its construction closes the vertical.

---

# Section 1. The Boundary within a Rank

## §1.1. Support and Poles

To a state $x \in Q_n$ is assigned a support — the set of its unit coordinates $A \subseteq J$, where $J = \{1, \dots, n\}$. This is a bijection between $Q_n$ and the subsets of $J$. The weight of a state is the cardinality of its support.

The two limits correspond to the two extreme supports:

$$
\boxed{
0^n \leftrightarrow \varnothing, \qquad 1^n \leftrightarrow J.
}
$$

The lower pole is the empty support, the upper the full one. The active scene $U_n$ consists of the nonempty proper subsets of $J$ — the supports strictly between the poles. The layer $S_k$ consists of the subsets of cardinality $k$.

The vertical within a rank is the movement by the cardinality of the support — from $\varnothing$ to $J$ and back, between the two poles.

## §1.2. The Boundary Operator

The boundary descends one cardinality level, removing one element at a time:

$$
\boxed{
\partial(A) = \sum_{a \in A} (A \setminus \{a\}),
}
$$

a sum modulo 2. The boundary carries the layer $S_k$ into the layer $S_{k-1}$ — movement downward, toward the lower pole. For example,

$$
\partial(\{1,2,3\}) = \{1,2\} + \{1,3\} + \{2,3\}, \qquad \partial(\{1\}) = \varnothing.
$$

The boundary of a vertex is the empty support — the lower pole. This accords with the fact that $\varnothing$ is a full-fledged element of the complex (the support of the lower pole), and not the absence of an element.

## §1.3. The Coboundary Operator

The coboundary rises one cardinality level, adding one missing element at a time:

$$
\boxed{
\delta(A) = \sum_{b \notin A} (A \cup \{b\}),
}
$$

a sum modulo 2. The coboundary carries the layer $S_k$ into the layer $S_{k+1}$ — movement upward, toward the upper pole. For example,

$$
\delta(\{1\}) = \{1,2\} + \{1,3\}, \qquad \delta(J \setminus \{a\}) = J.
$$

The coboundary of a state lacking a single coordinate is the upper pole.

## §1.4. The Laws of the Complex

The double boundary vanishes:

$$
\boxed{
\partial^2 = 0, \qquad \delta^2 = 0.
}
$$

For the boundary: in $\partial^2(A)$ each subset $A \setminus \{a, b\}$ arises twice — by removing $a$, then $b$, and by removing $b$, then $a$ — and cancels modulo 2. The same for the coboundary. The layers with the operators $\partial, \delta$ form a chain complex — the vertical structure of a single rank, running from pole to pole.

## §1.5. The Complement and the Direction of the Vertical

The complement of a support is the passage to the complementary set, $A \mapsto J \setminus A$. It exchanges the poles ($\varnothing \leftrightarrow J$) and reverses the vertical: removing an element from $A$ is adding an element to $J \setminus A$. Hence

$$
\boxed{
\kappa \partial = \delta \kappa.
}
$$

The limit complement carries the boundary into the coboundary. The descent to the lower pole is, after the complement, the ascent to the upper. The vertical is symmetric with respect to $\kappa$: the two directions, descent and ascent, are one movement read from different poles.

---

# Section 2. Two Verticals

## §2.1. The Vertical within a Rank

The boundary and coboundary move between the layers of a fixed rank: $\partial : S_k \to S_{k-1}$, $\delta : S_k \to S_{k+1}$. This is the vertical within a rank — movement by the cardinality of the support on a fixed ground set $J$.

## §2.2. The Vertical between Ranks

The lift moves between ranks: $\Lambda$ carries rank $n$ into rank $n+1$, adding a coordinate. In terms of supports the ground set expands: $J_n = \{1, \dots, n\}$ passes into $J_{n+1} = \{1, \dots, n+1\}$. A subset $A \subseteq J_n$ gives two subsets of $J_{n+1}$: $A$ itself (without the new element) and $A \cup \{n+1\}$ (with the new element).

## §2.3. The Coboundary and the Lift — One Increment

The coboundary and the lift are one operation — the addition of an element to the support — at different scopes.

The coboundary adds to the support any missing element within the fixed ground set $J$. The lift expands the ground set itself by one element and adds precisely this new element: the upper half of $Q_{n+1}$ — the states containing $n+1$ — is the image of rank $n$ under the map $A \mapsto A \cup \{n+1\}$.

$$
\boxed{
\text{the coboundary adds any missing element; the lift adds the new element of the ground set.}
}
$$

Both are an increment of the support. The difference is in scope: the coboundary works within a given $J$, the lift expands $J$. The vertical within a rank and the vertical between ranks are one movement of increment at different levels.

---

# Section 3. The Lift as a Cone

The addition of a new element to the support is a cone operation, linking the boundaries of neighboring ranks.

## §3.1. The Cone Formula

For a subset $A \subseteq J_n$ and a new element $* = n+1$ the boundary of the extended subset is computed directly:

$$
\partial(A \cup \{*\}) = \sum_{x \in A \cup \{*\}} (A \cup \{*\}) \setminus \{x\}.
$$

Removing $*$ gives $A$; removing each $a \in A$ gives $(A \setminus \{a\}) \cup \{*\}$. Hence

$$
\boxed{
\partial(A \cup \{*\}) = A + (\partial A) \cup \{*\},
}
$$

where $(\partial A) \cup \{*\}$ means the addition of $*$ to each summand of $\partial A$. This is the cone formula: the addition of a new element cones the complex over the new vertex. The support $\varnothing$ as the lower limit is essential here — the boundary of a vertex is $\varnothing$, and the addition of $*$ carries it into $\{*\}$, closing the formula.

## §3.2. The Ladder as a Tower of Complexes

The cone formula links the boundary of rank $n+1$ with the boundary of rank $n$. Since the cone preserves the chain complex, the law $\partial^2 = 0$ holds at each rank, and the lift carries the complex of rank $n$ into the complex of rank $n+1$.

$$
\boxed{
\text{the ladder of ranks is a tower of chain complexes linked by the cone.}
}
$$

Each rank bears a chain complex from pole to pole; the addition of a coordinate cones it into the complex of the next rank.

## §3.3. The Law of the Ladder

The law $\partial^2 = 0$ is not only an identity on a single rank but a law of the entire ladder: the vertical within each rank is a chain complex, and these complexes are linked by the vertical between ranks through the cone. The two vertical movements — within-rank and between-rank — are one vertical structure: a tower of complexes in which the boundary and the lift are one increment, read at two levels.

---

# Section 4. The Adjoint Descent

To each ascent corresponds a descent. The vertical within a rank has the descent $\partial$; the vertical between ranks has its own descent.

## §4.1. The Descent between Ranks

The lift builds rank $n+1$ as two copies of rank $n$ — with the new bit $0$ and with the new bit $1$. The descent forgets the new coordinate:

$$
\boxed{
\pi(\varepsilon \,|\, x) = x, \qquad \pi : Q_{n+1} \to Q_n.
}
$$

The descent $\pi$ inverts the lift: for each of the two embeddings $\iota_\varepsilon : Q_n \to Q_{n+1}$ (appending the new bit $\varepsilon$) one has

$$
\pi \circ \iota_\varepsilon = \operatorname{id}_{Q_n}.
$$

The descent is a retraction of the lift: having gone up and then down, a state returns to itself.

## §4.2. Two Descents

The vertical has two descents, corresponding to the two ascents. The boundary $\partial$ is the descent within a rank — to the lower pole by the cardinality of the support. The projection $\pi$ is the descent between ranks — to the lower rank by the number of coordinates. Descent and ascent are aligned at each level: within a rank $\partial$ and $\delta$, between ranks $\pi$ and $\Lambda$.

## §4.3. Reductions as the Descent of the Scene

The old corpus introduced the reductions $\rho_D, \rho_F, \rho_C$ as boundaries of the scene as a scene — in contrast to $\partial$, the boundary within the scene. These reductions are the descent at the level of the scene: each removes one direction of distinction, carrying the scene into a poorer one. The removal of a direction is the forgetting of a coordinate — the same as the projection $\pi$, but carried out along a chosen direction.

$$
\boxed{
\text{the reductions } \rho \text{ are the descent of the scene — realizations of the projection } \pi \text{ along chosen directions.}
}
$$

Thus the reductions, which in the old corpus stood apart, are recognized as the reverse side of growth: the descent adjoint to the lift.

## §4.4. The Adjoint Pair

The lift and the descent form an adjoint pair. The lift freely adjoins a new coordinate; the descent forgets a coordinate. This is the "free adjunction — forgetting" pair, the standard form of adjointness:

$$
\boxed{
\Lambda \dashv \pi.
}
$$

At the level of sets the kernel of this is the retraction $\pi \circ \iota_\varepsilon = \operatorname{id}$ (§4.1). The full adjointness as a statement about morphisms of scenes belongs to the functorial reading (Section 5): the lift is the left adjoint to the descent, and the reductions are the descent in this pair. Growth and reduction cease to be separate operations — they are the two directions of one adjoint pair.

---

# Section 5. The Functorial Reading of the Vertical

The chain complex and the adjoint pair are what the categorical language expresses exactly; the vertical is the place where the fifth projection of the theory bears weight.

## §5.1. The Lift as a Functor

The ranks are the objects, the lift the passage between them. The lift is consistent with the entire structure of a rank: it carries the complement into the complement, the poles into the poles, the chain complex into the chain complex. In the functorial reading the lift is a functor between ranks, and the growth vector

$$
Q_n^{*} \cong U_{n+1}/\kappa
$$

is a natural correspondence: the content of a rank is naturally identified with the axes of the next. Naturality means the consistency of this identification with the lift at all ranks.

## §5.2. Complex and Cone

The vertical within a rank is a chain complex $(C_\bullet, \partial)$ with $\partial^2 = 0$. The vertical between ranks is a cone: the addition of a new coordinate cones the complex of rank $n$ into the complex of rank $n+1$ (Section 3). In the functorial reading the cone is a functor between complexes, carrying a complex into a complex and preserving $\partial^2 = 0$. The tower of complexes linked by the cone is the functorial form of the ladder of ranks.

## §5.3. Adjointness

The lift $\Lambda$ is the left adjoint to the descent $\pi$: the free adjunction of a coordinate is adjoint to the forgetting of a coordinate. The reductions $\rho$ are the descent in this pair — realizations of $\pi$ along chosen directions. The adjoint pair $\Lambda \dashv \pi$ is the categorical form of the fact that growth and reduction are the two directions of one vertical. This is the formalization of the statement of Section 4; its rigorous unfolding as a statement about categories of scenes belongs to the functorial layer, developed in a separate track.

---

# §6. Summary of Volume 3

The support of a state is the set of its unit coordinates; the poles are the extreme supports $\varnothing \leftrightarrow 0^n$ and $J \leftrightarrow 1^n$; the active scene consists of the supports strictly between the poles. The vertical within a rank is the movement by the cardinality of the support.

The boundary and coboundary move between the layers:

$$
\partial(A) = \sum_{a \in A}(A \setminus \{a\}), \qquad \delta(A) = \sum_{b \notin A}(A \cup \{b\}),
$$

descent to the lower pole and ascent to the upper. They form a chain complex:

$$
\partial^2 = 0, \qquad \delta^2 = 0, \qquad \kappa\partial = \delta\kappa.
$$

The complement exchanges the poles and reverses the vertical: descent and ascent are one movement from different poles.

The coboundary and the lift are one increment of the support at different scopes: the coboundary adds any missing element within $J$, the lift expands $J$ and adds the new element. The addition of a new coordinate is a cone,

$$
\partial(A \cup \{*\}) = A + (\partial A) \cup \{*\},
$$

linking the boundaries of neighboring ranks. The ladder of ranks is a tower of chain complexes linked by the cone; $\partial^2 = 0$ is the law of the entire ladder.

To each ascent corresponds a descent. The descent between ranks is the projection $\pi(\varepsilon|x) = x$, a retraction of the lift ($\pi \circ \iota_\varepsilon = \operatorname{id}$). The reductions $\rho_D, \rho_F, \rho_C$ are the descent of the scene — realizations of $\pi$ along chosen directions. The lift and the descent form an adjoint pair $\Lambda \dashv \pi$: growth and reduction are the two directions of one vertical.

In the functorial reading the lift is a functor between ranks, the cone a functor between complexes, the growth vector a natural correspondence, and $\Lambda \dashv \pi$ an adjoint pair. This is the fifth projection of the theory, and the vertical is the place where it bears weight.

$$
\boxed{
\text{the vertical is one: the boundary and the lift are one increment; growth and reduction are an adjoint pair; the ladder is a tower of complexes.}
}
$$

The next layer of reorganization is the helicoid: what happens to the cycle under the lift, and how the within-scene rotation combines with the between-rank ascent.
