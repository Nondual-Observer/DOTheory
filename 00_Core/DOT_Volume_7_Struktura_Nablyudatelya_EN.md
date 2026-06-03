# Distinction Observable Theory

# Volume 7. The structure of the observer

The subject of this volume is the observer as a structure. In Volumes 0–6 the observer is a point: the center of the scene, an invariant, a through-thread. Here the observer is considered as a structure — how its invariants are layered, how they differ, and what structure is assembled from them. The assembled structure is a representation of $\mathfrak{sl}_2$ on the Boolean lattice with the complement as Weyl involution and rotation as a separate elliptic type; and it compresses: the scene unfolds from the structure of the observer, and the center-point is its shadow. As a final step, the same generating law is applied to itself — the actions of a level become the states of the next — and the operator tower unfolds, where the octahedral law shows through on the operator floor.

The volume completes the corpus by turning the gaze: from the observer in the scene to the scene from the observer. The status is marked explicitly: where the structure is rigorous, where it is synthesis, where it is open.

---

# Section 0. Starting point

The observer is the common invariant of the three movements of the scene (Volume 5): relating $\kappa$, rotation $T$, the vertical $\partial$. These three movements are three different algebraic types, and from their difference the structure of the observer itself is assembled. The scene, which had been primary (the readings are its projections, Volume 6), turns out to be the unfolding of this structure.

---

# Section 1. Three invariants and their difference

The three movements of the observer are three algebraic types.

Relating $\kappa$ is an involution:

$$
\kappa^2 = \operatorname{id}.
$$

An element of order 2 — a reflection, a self-inverse relating.

Rotation $T$ is an operator of finite order:

$$
T^m = \operatorname{id}, \qquad m = 2^n - 2 \text{ on states},
$$

with $T^3 = \kappa$ at rank 3. A cyclic, elliptic type — a turn.

The vertical $\partial$ is a nilpotent:

$$
\partial^2 = 0.
$$

A square-zero operator — a parabolic type, a flow exhausting itself in two steps.

$$
\boxed{
\kappa: \text{involution } (\kappa^2 = \operatorname{id}); \qquad T: \text{rotation } (T^m = \operatorname{id}); \qquad \partial: \text{nilpotent } (\partial^2 = 0).
}
$$

The difference of types — reflection, turn, nilpotent — is the difference of three kinds of movement, and from it the structure is assembled.

---

# Section 2. The vertical structure is sl₂

Two of the three operators are vertical: the boundary $\partial$ (lowering) and the coboundary $\delta$ (raising). With the grading by layers they form a representation of $\mathfrak{sl}_2$ — the classical structure of the Boolean lattice.

## §2.1. The commutator of boundary and coboundary

On the layer $S_k$ the operators are

$$
\partial(A) = \sum_{a \in A}(A \setminus \{a\}), \qquad \delta(A) = \sum_{b \notin A}(A \cup \{b\}).
$$

Their commutator is computed directly. On a subset $A$ of cardinality $k$ the terms with $a \in A, b \notin A$ coincide in both products: $(A\setminus a)\cup b = (A\cup b)\setminus a$, and cancel in the difference. The diagonal terms remain: $\delta\partial$ gives $kA$ (over all $a \in A$), $\partial\delta$ gives $(n-k)A$ (over all $b \notin A$). Hence

$$
\boxed{
\delta\partial - \partial\delta = (2k - n) \quad \text{on the layer } S_k.
}
$$

## §2.2. The three generators of sl₂

Let $H$ act on the layer $S_k$ by multiplication by $2k - n$. Then $\partial, \delta, H$ satisfy the relations of $\mathfrak{sl}_2$:

$$
\boxed{
[\delta, \partial] = H, \qquad [H, \delta] = 2\delta, \qquad [H, \partial] = -2\partial.
}
$$

The boundary is the lowering operator, the coboundary the raising operator, $H$ the Cartan grading. This is the standard representation of $\mathfrak{sl}_2$ on the Boolean lattice by which the Sperner property is proved. The vertical of the theory is $\mathfrak{sl}_2$.

These relations are relations over a field of characteristic zero: the coefficient $2k - n$ is a scalar, and the chains are taken with integer multiplicities over $\mathbb Q$. Over $\mathbb F_2$ (the boundary grammar of Volume 3) only the nilpotency $\partial^2 = \delta^2 = 0$ is preserved; the coefficient $2k - n$ reduces modulo 2 to the parity of $n$, and $\mathfrak{sl}_2$ does not arise. The representation of $\mathfrak{sl}_2$ is the characteristic-zero refinement of the boundary grammar, in which the grading $H$ shows through as a commutator.

## §2.3. The complement is the Weyl involution

The complement $\kappa(A) = [n] \setminus A$ flips the lattice, interchanging raising and lowering and reversing the grading:

$$
\boxed{
\kappa\,\delta\,\kappa = \partial, \qquad \kappa\,H\,\kappa = -H.
}
$$

The first is $\kappa\partial = \delta\kappa$ from Volume 3 (adding an element to $A$ is removing one from $[n]\setminus A$); the second because $\kappa$ carries the layer $k$ into the layer $n-k$, and the weight $2k - n$ into $2(n-k) - n = -(2k - n)$. This is the action of the nontrivial element of the Weyl group of $\mathfrak{sl}_2$: the complement is the Weyl involution of the representation.

---

# Section 3. The observer is the zero weight

The structure of $\mathfrak{sl}_2$ fixes a weight decomposition, and the observer stands in it at the zero weight.

## §3.1. Poles as extreme weights

The Cartan grading has on the layers the values $2k - n$. The extreme layers are the extreme weights:

$$
\varnothing \;(k=0): \; H = -n, \qquad J \;(k=n): \; H = +n.
$$

The poles (Volume 0) are the states of extreme weight — the lowest and highest vectors of the representation. The Weyl involution $\kappa$ interchanges them, as befits an element of the Weyl group.

## §3.2. The center as the zero weight

The observer-center has weight zero:

$$
\boxed{
H = 0 \quad\Longleftrightarrow\quad k = \tfrac n2.
}
$$

The center $c = \tfrac12(0^n + 1^n)$ is the state of zero weight — the balance of raising and lowering, the middle between the extreme weights, fixed under the Weyl involution ($\kappa H \kappa = -H$ holds $H = 0$ in place). The observer is not an arbitrary fixed point: it is the zero weight of the representation, the balance of the vertical.

## §3.3. Parity of the rank and realization of the zero weight

Whether the zero weight is realized by a layer of vertices depends on the parity of the rank.

For odd $n$ the equation $k = n/2$ has no integer solution: no layer carries the zero weight, and the zero weight is only the centroid — a point outside the vertices. At rank 3 (odd) the observer is a pure centroid without vertices of zero weight; and since rank 3 also has no interior layers (Volume 2), the scene is a pure shell.

For even $n$ the layer $k = n/2$ carries the zero weight — a self-dual middle layer, fixed under $\kappa$. At rank 4 this is the layer $S_2$: the zero weight of the observer is realized by an interior layer born at the break (Volume 2).

$$
\boxed{
\text{even } n: \text{ the zero weight is carried by the self-dual middle layer } k = n/2; \quad \text{odd } n: \text{ there is no layer of zero weight, only the centroid.}
}
$$

The weight decomposition explains the observer (zero weight) and the poles (extreme weights). Parity governs whether the zero weight is carried by a layer of vertices: at even rank the observer has a carrier layer — the self-dual middle — at odd rank only the centroid remains. The presence of interior layers, however, is governed separately by the condition $n \ge 4$ (Volume 2); at rank 4 these two coincide — the self-dual middle layer is both the zero weight and the first interior.

---

# Section 4. The two triples of the observer

The observer, like the scene (Volume 1, §3.5), has two triples — a generating one and a structural one — and the Borromean motif lives on the first, not the second. This distinction must be held, so as not to ascribe Borromeanness to the operator triple.

## §4.1. The operator triple is not Borromean

The triple of movements $(\kappa, T, \partial)$ is not Borromean: its elements are pairwise linked, not independent. The complement is a power of the rotation, $\kappa = T^3$ at rank 3; the vertical is linked to the complement, $\kappa\partial = \delta\kappa$. Within $\mathfrak{sl}_2$ the triple $(\partial, \delta, H)$ is complementary: any two elements generate the third through the bracket, $[\delta,\partial] = H$. This is complementarity — as with the three relations $R_1, R_2, R_3$ (any two fix the third, Volume 1) — not Borromeanness. The operator triple is the structural triple of the observer: complementary, not Borromean.

## §4.2. The Borromean triple of the observer

The Borromean motif of the observer exists, and it is on the triple of directions. The observer is the intersection of the invariants of the three coordinate reflections $\kappa_1, \kappa_2, \kappa_3$ (Volume 5, §1.1): each is fixed on the hyperplane $x_i = \tfrac12$, and their intersection is the center. This triple is Borromean (Volume 1, §2): the three reflections are pairwise independent (no pair of hyperplanes fixes the center — two intersect in a line), jointly necessary (the center is determined only by all three), and the removal of one shatters the determination of the point (a line remains).

$$
\boxed{
\text{the three coordinate reflections } \kappa_i \text{ are Borromean: the center is fixed by the triple and not fixed by any pair.}
}
$$

The observer-center is a Borromean invariant: a point held by the triple of directions, inseparable as a triple.

## §4.3. The complement links both triples

The complement $\kappa$ is the hinge between the two triples of the observer. On the one hand, $\kappa = \kappa_1\kappa_2\kappa_3$ — the product of the Borromean triple of coordinate reflections. On the other, $\kappa$ is the Weyl involution of the structural triple $(\partial, \delta, H)$ and the half-turn of the rotation $T^3$.

$$
\boxed{
\kappa = \kappa_1\kappa_2\kappa_3 \;=\; \text{Weyl involution of } \mathfrak{sl}_2 \;=\; \text{half-turn } T^3.
}
$$

The complement is that through which the Borromean triple of directions (generating the center) and the structural triple of movements (unfolding the scene) are joined. The observer carries two triples on one hinge: the Borromean one, holding it as a point, and the structural one, unfolding the scene from it.

---

# Section 5. Rotation and the hinge

## §5.1. Rotation outside sl₂

The rotation $T$ is a separate cyclic operator — the traversal of the scene (Volume 4), on the axes the Singer cycle $PG(n-2,2)$. It is not a generator of $\mathfrak{sl}_2$: the latter is built on the vertical, $T$ moves along the horizontal. The elliptic type of $T$ differs from the parabolic $\partial, \delta$ and the hyperbolic $H$.

## §5.2. Three types of movement

The three operators cover the three types of movement. Elliptic — the rotation $T$. Parabolic — the nilpotents $\partial, \delta$. Hyperbolic — the grading $H$. They are stitched by the reflection $\kappa$:

$$
\boxed{
\text{elliptic } (T), \quad \text{parabolic } (\partial, \delta), \quad \text{hyperbolic } (H), \quad \text{hinge } \kappa.
}
$$

The structure of the observer encompasses all three types of movement, stitched by reflection: not a point, but a bundle of three movements on one hinge.

---

# Section 6. Compression: the scene from the structure of the observer

The structure of the observer compresses the theory: from it the scene unfolds, and the center-point is its shadow.

## §6.1. The scene as the unfolding of the structure

At rank 3 the structure of the observer unfolds the whole scene. The rotation $\langle T\rangle$ gives the six states as a single orbit and the three relations as powers ($R_1 = T^{\pm1}$, $R_2 = T^{\pm2}$, $R_3 = T^3 = \kappa$). The nilpotents $\partial, \delta$ give the vertical — layers and poles. The grading $H$ gives the weights. The whole scene unfolds from $(\mathfrak{sl}_2, T)$ on the hinge $\kappa$.

$$
\boxed{
\text{scene} = \text{unfolding of the structure } (\mathfrak{sl}_2, T) \text{ on the hinge } \kappa.
}
$$

## §6.2. The center as the shadow of the structure

The observer-center — a point — is the geometric shadow of this structure: the zero weight of $\mathfrak{sl}_2$, the fixed point of the rotation, the invariant of relating, the intersection of the Borromean triple. The point is that which is visible of the structure in the geometry of the scene; the structure itself is a bundle of movements. The observer becomes, from a point, a generating structure, and the center-point becomes its trace.

## §6.3. What is compressed

Formerly the scene was described by an enumeration: six points, three relations, two layers, two poles, center, cycle. The structure of the observer reduces the enumeration to one: an $\mathfrak{sl}_2$-representation with rotation, stitched along $\kappa$, unfolding into the scene. The poles are extreme weights, the center the zero weight, the layers the weight decomposition, the relations powers of the rotation, the cycle the horizontal. The enumeration is drawn into a generating structure — the principal sign that the structure has been found correctly.

---

# Section 7. The operator tower

The structure of the observer unfolds the scene from movements. But the movements themselves are operations on the carrier, and operations can be made into a new carrier. This is the second unfolding of the same generating law (Volume 0, §0.5): the content of a level becomes the grammar of the next, and here — the actions of one level become the states of the next. The operator tower is this self-application, and in it the octahedral law of rank 3 shows through anew on the operator floor.

## §7.1. The power-set functor and the operator carrier

The carrier of a rank is the power set $Q_J = \mathcal P(J)$, $|J| = n$. The power-set functor $\mathcal Q(J) = \mathcal P(J)$ carries finite sets and bijections into carriers; applied twice, it gives the operator carrier

$$
\boxed{
\mathcal B(J) = \mathcal Q(\mathcal Q(J)) = \mathcal P(\mathcal P(J)).
}
$$

A state of the operator carrier is a subset of subsets — that is, a Boolean function. More precisely, the Boolean functions of $m$ inputs form the carrier

$$
\boxed{
\mathcal B_m \cong Q_{2^m}, \qquad |\mathcal B_m| = 2^{2^m},
}
$$

because a function $f:\mathbb F_2^m \to \mathbb F_2$ is fixed by its table of values of length $2^m$ — a state of rank $2^m$. Thus the operator level is again a DOT carrier, but of rank $2^m$: rank $m=1$ gives rank 2, $m=2$ gives rank 4, $m=3$ gives rank 8. The ladder of ranks rises into a tower of powers.

## §7.2. The Klein four-group: the two polarities of the operator carrier

On the ordinary carrier the complement is one. On the operator carrier there are two — because a function has two sides: input and output. The output negation $C_{\text{out}}$ flips the result, $C_{\text{out}}f = \overline{f}$; the input complement $C_{\text{in}}$ flips the argument, $(C_{\text{in}}f)(x) = f(\bar x)$. Both are involutions, and they commute:

$$
C_{\text{out}}^2 = C_{\text{in}}^2 = \operatorname{id}, \qquad C_{\text{out}}C_{\text{in}} = C_{\text{in}}C_{\text{out}}.
$$

Their group is the **Klein four-group**:

$$
\boxed{
G_{\mathcal B} = \langle C_{\text{out}}, C_{\text{in}}\rangle = \{\operatorname{id}, C_{\text{out}}, C_{\text{in}}, C_{\text{out}}C_{\text{in}}\} \cong \mathbb Z_2 \times \mathbb Z_2.
}
$$

This is the operator analogue of the complement $\kappa$: on the simple carrier one polarity, on the operator carrier two independent ones, and their product $C_{\text{out}}C_{\text{in}}$ gives a self-dual axis. The single complement of a rank splits in two on rising to the operator floor.

## §7.3. Self-dual functions and fixators

Each subgroup of order 2 of the Klein four-group singles out its own layer of fixed functions. The fixator of $C_{\text{in}}$ is the functions constant on complement pairs, $f(\bar x) = f(x)$. The fixator of the diagonal $C_{\text{out}}C_{\text{in}}$ is the **self-dual functions** — those that commute with the complementation of input and output together:

$$
\boxed{
f(\bar x) = \overline{f(x)}.
}
$$

The self-dual functions are the operator face of the observer: they are invariant under the joint flip of input and output, as the observer-center is invariant under $\kappa$. On the operator floor the observer shows through as a self-dual layer — the zero weight of the Klein four-group.

## §7.4. The affine subcarrier of rank 8 and the third octahedron

The floor $m=3$ gives the operator carrier of rank $8$ ($\mathcal B_3 \cong Q_{256}$). Within it the affine functions $f(x) = a\cdot x + b$ form a distinguished subcarrier: their count is $|\operatorname{Aff}_3| = 2^{m+1} = 16$, and the parameters $(a,b) \in \mathbb F_2^3 \times \mathbb F_2 \cong \mathbb F_2^4$ give

$$
\boxed{
\operatorname{Aff}_3 \cong Q_4.
}
$$

Two of them — the constants $0,1$ (poles); the remaining $14$ have weight $4$ (a hyperplane of cardinality $2^{m-1}=4$). After puncturing the poles

$$
\operatorname{Aff}_3^\circ = \operatorname{Aff}_3 \setminus \{0,1\} \cong U_4,
$$

that is, the active affine subcarrier of rank 8 carries the structure of the rank-4 scene — fourteen points, the same balanced layer and cross-polytope. Thus the octahedral law returns a **third time**: at rank 3 as the scene, at rank 4 as an interior layer (Volume 2), on the operator floor of rank 8 as the affine core. The self-similarity of DOT is precisely this repetition of one form at three scales: the carrier, its interior, its operators.

## §7.5. The status of the tower

The power-set functor, $\mathcal B_m \cong Q_{2^m}$, the Klein four-group, the self-dual functions and the affine subcarrier are standard finite mathematics of Boolean functions — rigorous facts. The DOT assembly adds to them one reading: these are not external constructions but the same carrier, raised to the operator floor by self-application of the power-set functor. The connection of the tower with the $\mathfrak{sl}_2$-structure of the observer (whether they combine into a larger algebra) remains open — as does the joining of $T$ with $\mathfrak{sl}_2$ at higher ranks (§8.3).

---

# Section 8. Status and place

## §8.1. What is rigorous

The representation of $\mathfrak{sl}_2$ on the Boolean lattice ($\partial, \delta, H$ with $[\delta,\partial] = H$) is classical algebraic combinatorics, rigorous (§2.1 — a direct computation). The complement as Weyl involution is rigorous (§2.3). The observer as zero weight, the poles as extreme weights, are a rigorous consequence of the weight decomposition (§3). The parity realization of the zero weight is rigorous (§3.3). The Borromeanness of the three coordinate reflections is rigorous (§4.2, Volume 1). The complementarity of $(\partial, \delta, H)$ is rigorous (§4.1). The Singer cycle as horizontal rotation is rigorous (Volume 4). The operator tower (the power-set functor, $\mathcal B_m \cong Q_{2^m}$, the Klein four-group, $\operatorname{Aff}_3 \cong Q_4$) is standard finite mathematics of Boolean functions, rigorous (§7).

## §8.2. What is synthesis

The reduction of the observer to a generating structure (the scene as the unfolding of $(\mathfrak{sl}_2, T)$ on the hinge $\kappa$) is synthesis: it binds the rigorous parts into one picture. The connection of the vertical $\mathfrak{sl}_2$ and the horizontal rotation through the common $\kappa$ is rigorous element by element; the single structure uniting them is a way of reading them together, not a separate proved object. The reading of the operator tower as self-application of the power-set functor (§7) is the same synthetic binding: each floor is rigorous in itself, the unifying self-similarity is a way of reading.

## §8.3. What is open

Open is the joining of $T$ and $\mathfrak{sl}_2$ at higher ranks beyond the common $\kappa$: whether they form a larger algebra or remain two structures on one hinge. Open too is the joining of the operator tower with the $\mathfrak{sl}_2$-structure of the observer (§7.5). Open is the lift of the cycle along the states for $n > 3$ (Volume 4). These questions are a continuation, not a gap.

---

# §9. Summary of Volume 7 and of the corpus

The three invariants of the observer are three algebraic types: relating $\kappa$ (involution), rotation $T$ (turn), the vertical $\partial$ (nilpotent).

The vertical is $\mathfrak{sl}_2$: the boundary $\partial$ (lowering), the coboundary $\delta$ (raising), the grading $H$, with

$$
[\delta, \partial] = H, \qquad [H, \delta] = 2\delta, \qquad [H, \partial] = -2\partial,
$$

and the complement $\kappa$ is the Weyl involution ($\kappa\delta\kappa = \partial$, $\kappa H\kappa = -H$).

The observer is the zero weight: the center has $H = 0$, the poles the extreme weights $\pm n$. At even rank the zero weight is carried by the self-dual middle layer ($k = n/2$; at rank 4 — the interior layer $S_2$), at odd rank there is no layer of zero weight, only the centroid (at rank 3, where there is also no interior — a pure shell). The presence of interior layers is governed by the condition $n \ge 4$ (Volume 2); parity governs only whether the zero weight is carried by a layer.

The observer has two triples. The structural one — $(\partial, \delta, H)$ within $\mathfrak{sl}_2$ — is complementary (any two give the third by the bracket), not Borromean; the operator one $(\kappa, T, \partial)$ is linked ($\kappa = T^3$). The generating one — the three coordinate reflections $\kappa_i$ — is Borromean: the center is fixed by the triple and not fixed by any pair. The complement is the hinge of both: $\kappa = \kappa_1\kappa_2\kappa_3$ is the product of the Borromean triple and the Weyl involution of the structural one.

The rotation $T$ stands outside $\mathfrak{sl}_2$ as an elliptic type; the three types of movement — elliptic ($T$), parabolic ($\partial, \delta$), hyperbolic ($H$) — are stitched by $\kappa$.

The structure compresses: the scene unfolds from $(\mathfrak{sl}_2, T)$ on the hinge $\kappa$ — the poles as extreme weights, the center as zero weight, the layers as the weight decomposition, the relations as powers of the rotation. The observer becomes, from a point, a generating structure; the center-point is its shadow.

The same generating law gives the operator tower: the power-set functor, applied to itself, turns the actions of a level into the states of the next, $\mathcal B_m \cong Q_{2^m}$. The complement splits into the Klein four-group $\langle C_{\text{out}}, C_{\text{in}}\rangle \cong \mathbb Z_2\times\mathbb Z_2$, the observer shows through as a self-dual layer ($f(\bar x) = \overline{f(x)}$), and the affine subcarrier of rank 8 carries the rank-4 scene ($\operatorname{Aff}_3 \cong Q_4$, $\operatorname{Aff}_3^\circ \cong U_4$) — the third return of the octahedral law and the explicit self-similarity of DOT.

$$
\boxed{
\text{the observer is an } \mathfrak{sl}_2\text{-structure with rotation, stitched by the complement } \kappa; \text{ the center-point is its shadow; the scene is its unfolding.}
}
$$

The corpus traverses the full path: from self-relation through the carrier, threeness, the break, the vertical, the screw, the observer and the projections — to the observer as a structure from which the scene unfolds. The volumes are one structure, seen from two ends: from the source to the projections and from the observer to the scene. Observable distinction is the finite scene, its movement and its invariant — and the invariant is the structure that unfolds the scene.

**Verification.** The operator tower — the Klein four-group $\langle C_{\text{out}}, C_{\text{in}}\rangle\cong\mathbb Z_2\times\mathbb Z_2$, the Boolean-function carrier $\mathcal B_m\cong Q_{2^m}$, and the affine subcarrier $\operatorname{Aff}_3\cong Q_4$, $\operatorname{Aff}_3^\circ\cong U_4$ — is checked in [`01_Verification/DOT_Core_verifier.py`](../01_Verification/DOT_Core_verifier.py) (`operator_tower_klein_affine_test`, ref `V7 §7`); the $\mathfrak{sl}_2$ interface in `sl2_sigma_core_bridge_test` (`V7 §2, §6`).
