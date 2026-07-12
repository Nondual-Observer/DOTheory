# Categorical Core: construction and proofs

The section sets out the functorial part of the theory: the carrier as a free object, the lift as an adjoint triple, the growth law as an isomorphism of projective spaces, the observer as a terminal object. Each step is proved in the text or confirmed by a verifier from the `code_core/` folder — 18 scripts, 385 checks, all passing. The introduction, nine chapters, and the epilogue follow as a single document.

---

## Introduction: functoriality of the theory

### Subject and method

The question of the theory's functoriality has two forms, and they should be separated. The **external** form — whether a structure-preserving map exists from the discrete construction into physical models. Such a map runs up against input values — weights and constants absent from the bare structure; its exact boundaries are examined in chapter IX. The **internal** form — whether the mathematical core itself is a categorical construction: the growth of ranks. Here there are no input values, and the answer is established rigorously.

The series establishes the internal form: **the tower of carriers `Q_n=𝔽₂ⁿ` is a categorical construction.** The carrier is the free object of the operation; growth is an adjoint and monoidal triple; the growth law is an isomorphism of projective spaces; the complement is one operator in coordinated roles; the tower is stretched between an initial object and a terminal; the scene bears the grading and the complex by the same matrices; the continuous side is derived by a spectral limit; time is a traversal, the arrow is a comonad; the boundary of the construction is reduced to a single equality `[κ,Δ]=0`.

The mode of exposition is a demonstrative narrative: prose leads, each mathematical step is proved on the spot or referred to a verifier (`code_core/verify_*.py`).

### Statuses of statements

The status marking is uniform across all sections of the package and is defined in the introduction of the "Exposition" section (document 01). Briefly: `[●]` — proved (theorem, identity, verified construction; thus the terminal object and the uniqueness of morphisms into it — a theorem); `[◐]` — reading (a name or recognition on top of a theorem; thus "observer" is the name of the terminal by the theory's definition); `[○]` — input or open (what the construction receives from outside or what remains unproved; thus the Lorentzian signature — input).

### Plan of exposition

The order of chapters: **the carrier from the operation** (I) → **the lift: adjoint triple** (II) → **the growth law** (III) → **the complement** (IV) → **the observer: terminal and monad** (V) → **the scene: grading, complex, motion, balance** (VI) → **the continuous limit** (VII) → **time as traversal** (VIII) → **the boundary: input and external bridge** (IX) → epilogue: the whole construction and its two models.

The series is self-contained: notions of category theory are introduced at the moment of use, with their direct meaning. Parallel expositions are the "Exposition" section (document 01; its chapter VIII gives the same construction in overview, within the general series of ranks) and the numerical model (document 03; its chapter VII is the functorial layer of the second model). Beyond them, the full demonstrative layers are unfolded here: the triple of adjoints on all pairs, the rigorous status of the growth law, the coherence of `κ` by one matrix, the two ends of the tower with Möbius, the conservation law of the construction, the spectral derivation of the continuous side, the arc of time, and the exact boundary `[κ,Δ]=0`.

---

## Chapter I. The carrier from the operation: the free object

The functorial exposition begins from the same place as the whole theory — from the operation of distinction. The difference is in **what** is asserted here: the carrier is **derived** from the operation as its free orbit, without postulating a ready-made set on which the operation then acts. Below this derivation is carried out rigorously; thereby the front "the carrier as a colimit before the carrier", which had remained open, is closed (document 01, chapter I).

### 1.1. The operation is primary

The starting object is an **involution without fixed points** `κ`, `κ²=id`: the minimal act of distinction, sending each side into its opposite. On the rank-`n` carrier it is realized by the complement `κ(x)=x+1ⁿ` over `𝔽₂`.

> **Statement 1 (freeness of the action).** The equation `κ(x)=x` is unsolvable in every `Q_n=𝔽₂ⁿ`: it entails `1ⁿ=0`. The action of `ℤ/2=⟨κ⟩` on `Q_n` is free, and the carrier splits into exactly `2ⁿ⁻¹` orbit-pairs `{x,κx}` `[●]` (`code_core/verify_functor_core.py §E`, `n=1…6`).

Each orbit is a copy of the regular representation of `ℤ/2`. Thereby `Q_n` is `2ⁿ⁻¹` copies of the simplest free action.

### 1.2. The universal property

The word "freeness" carries here two connected meanings, and both are exact. The action is free: `κ` leaves no point in place, and therefore no pair degenerates — there are no forced identifications. The object is free: the carrier is generated by the operation without a single relation beyond `κ²=id` — there is nothing in it except what the operation itself forces. The second meaning is the universal property:

> **Statement 2 (free object).** For any set with involution `Y` an equivariant map `Q_n → Y` is given by a free choice of image on one representative per orbit; the image of the second element of the pair is forced by equivariance. The number of morphisms
> $$\bigl|\mathrm{Hom}_{ℤ/2}(Q_n,\,Y)\bigr| \;=\; |Y|^{\,2^{n-1}} \;=\; |Y|^{\#\text{orbits}}. \qquad [●]$$
> (`code_core/verify_functor_fronts.py`, front 3.)

This is the definition of a free object, witnessed by enumeration: `Q_n` is a free `ℤ/2`-set on `2ⁿ⁻¹` generators. The first-rank carrier is the free object on one point: the regular orbit `{0,1}`.

### 1.3. "The carrier before itself" — the front is closed

The meaning of the construction: **the operation is primary, the carrier is derivative**. `Q_n` arises as the orbit-colimit of the involution — the universal object among all `κ`-sets. The promise "the carrier as a colimit of the operation" is fulfilled by pure combinatorics, without physics and without the wall of values: the front is **closed** `[●]`.

### Summary

The operation of distinction `κ` (involution without fixed points) generates the carrier: `Q_n` is a free `ℤ/2`-object on `2ⁿ⁻¹` orbits, with the universal property `|\mathrm{Hom}(Q_n,Y)|=|Y|^{2^{n-1}}` `[●]`. The front "the carrier before itself" is closed: the operation is primary, the carrier is derived.


---

## Chapter II. The lift: adjoint triple and monoidality

The growth of rank — the lift `Q_n → Q_{n+1}` — is the central operation of the tower. This chapter establishes its categorical form: the lift is an **adjoint functor** — and at once a triple; and it is **monoidal** — composite ranks are built tensorially. Neighboring ranks are connected by an adjunction, that is, by a universal property, and every arbitrariness is excluded from the linking of ranks.

### 2.1. Three maps

The objects are the Boolean lattices `Q_n=𝔽₂ⁿ` with the mask-inclusion order `x≤y ⟺ x⊆y`. Between neighboring ranks three monotone maps act:

- the **projection** `π: Q_{n+1}→Q_n` — forget the highest coordinate;
- the **left lift** `Λ_L(x)=(x,0)` — embed, new coordinate `0`;
- the **right lift** `Λ_R(x)=(x,1)` — embed, new coordinate `1`.

### 2.2. The adjoint triple

> **Theorem (triple).** On the Boolean lattices both Hom-isomorphisms hold:
> $$\Lambda_L \dashv \pi \dashv \Lambda_R,$$
> that is, `Λ_L(x) ≤ y ⟺ x ≤ π(y)` and `π(y) ≤ x ⟺ y ≤ Λ_R(x)` for all `x∈Q_n`, `y∈Q_{n+1}` `[●]` (`code_core/verify_functor_core.py §A`, all pairs, `n=1…4`).

Both Hom-isomorphisms reduce to coordinatewise comparison: `(x,0)≤(y',b) ⟺ x≤y'` — the left adjunction; `(y',b)≤(x,1) ⟺ y'≤x` — the right. The pattern of the construction is classical: `∃ ⊣ substitution ⊣ ∀` in predicate logic — the lift stands to the projection as the quantifier to substitution.

The unit of the adjunction — the identity `π∘Λ_L = π∘Λ_R = id` `[●]` (`§B`): the projection inverts the lift. The composition of lifts is well-defined (`Q_n→Q_{n+2}`) `[●]`. The tower is the iteration of a single adjoint functor.

### 2.3. Monoidality

The lift is compatible also with the product of ranks.

> **Statement (monoidality).** `Q_{m+n} = Q_m □ Q_n` (Cartesian product of graphs) with coordinatewise complement `κ_{m+n} = κ_m ⊗ κ_n`; the lift is multiplication by an edge `(−) □ K₂` `[●]` (`code_core/verify_functor_layers.py`).

The repeated lift builds ranks tensorially: `Q_n = K₂^{□n}`. The first composite rank `4=2×2` gives `Q₄=Q₂□Q₂` — the place where the system of directions first splits in two (in the terms of document 01 — the break, its chapter IV; here the monoidal formula itself suffices).

### Summary

The lift is an adjoint triple `Λ_L⊣π⊣Λ_R` on the Boolean lattices (Hom-isomorphisms on all pairs, unit `π∘Λ=id`) and a monoidal functor (`Q_{m+n}=Q_m□Q_n`, lift `=□K₂`) `[●]`. The growth of the tower is the iteration of an adjoint and monoidal functor.


---

## Chapter III. The growth law: the content of a rank is the axes of the next

The heart of the tower is the growth law: what was the content of a rank becomes, at the next rank, the axes. This chapter establishes its exact status: an **isomorphism of projective spaces**, given by a linear embedding — and separates what is established from what, beyond the isomorphism, is not yet asserted.

### 3.1. The statement

The active scene of rank `n+1` — the carrier without the two poles, `U_{n+1}=Q_{n+1}∖\{0,1^{n+1}\}` — splits under the action of `κ` into axes (`κ`-pairs `{x,κx}`). The set of axes is the projective space of the previous rank:

$$\mathrm{PG}(n{-}1,2) \;\cong\; U_{n+1}/\kappa, \qquad |\cdot| = 2^{n}-1.$$

The count is obvious (`(2^{n+1}-2)/2 = 2^n-1`); the content of the statement is in the structure of the correspondence.

### 3.2. The explicit bijection and its linearity

> **Theorem (isomorphism of projective structures).** The map `φ(a)=2a` (coordinate shift) realizes the correspondence: each `κ`-pair in `U_{n+1}` contains exactly one even element, and `φ` is a bijection of the nonzero vectors of `𝔽₂ⁿ` onto the system of even representatives. Moreover `φ` is **linear** (`φ(a⊕b)=φ(a)⊕φ(b)`), and therefore preserves incidence: the lines `{a,b,a⊕b}` pass into collinear triples. The correspondence is an isomorphism of projective spaces, with the structure of lines (stronger than a bijection of points) `[●]` (`code_core/verify_functor_core.py §C`; `code_core/verify_functor_strict.py §3`, `n=2…5`).

Behind the bijection stands linear algebra: the orbits of `κ` are the cosets of the line `⟨1^{n+1}⟩`, the quotient `𝔽₂^{n+1}/⟨1^{n+1}⟩≅𝔽₂ⁿ` is a vector space, its nonzero classes are the points of `PG(n−1,2)`; `φ` is a section of the quotient. Over `𝔽₂` the projective points coincide with the nonzero vectors, and the whole projective structure is canonical.

Thus at the third rank the three axes of the scene are `PG(1,2)`; at the fourth the seven axes assemble into the Fano plane `PG(2,2)`, each line of which is a copy of this triple; at the fifth — `PG(3,2)` with fifteen points.

### 3.3. The boundary of the statement: isomorphism and naturality

Established: a **rank-by-rank isomorphism of structures** — points and lines, for each `n`. Not established (and not assumed): that the family of these isomorphisms is **natural with respect to the lift** — that the square of `φ_n`, `φ_{n+1}` and the growth maps commutes. This is a separate statement, an open front `[◐]` (`code_core/verify_functor_strict.py`, conclusion §3).

The isomorphism gives the growth law a rigorous mathematical status on each floor; naturality would bind the floors into a single diagram. The first is proved, the second is open.

### Summary

The growth law is established as an isomorphism of projective spaces `PG(n−1,2)≅U_{n+1}/κ`: an explicit linear bijection `φ(a)=2a`, incidence preserved `[●]`. The content of a rank — its projective space — becomes the axes of the `κ`-scene of the next rank. The naturality of the family of isomorphisms with respect to the lift is a separate open question `[◐]`.


---

## Chapter IV. The complement: one matrix in three roles

The complement `κ` enters the exposition three times: as naturality with respect to the lift, as duality of the lattice, and — ahead, in chapter VI — as the Hodge star coinciding with the Weyl involution. Here the first two roles are established, together with the main fact of coherence: all roles are borne by **one operator**, one matrix, and the coordination of roles is an identity, without a separate theorem of compatibility.

### 4.1. Naturality with respect to the lift

> **Theorem (naturality).** For all ranks
> $$\kappa_{n+1}\circ\Lambda_L \;=\; \Lambda_R\circ\kappa_n \qquad [●]$$
> (`code_core/verify_functor_core.py §D`, `n=1…5`).

The check is one line: `κ_{n+1}(x,0) = (κ_n x, 1) = Λ_R(κ_n x)`. To lift and complement is the same as to complement and lift into the other embedding. The complement swaps the two adjoint lifts; in this lies the exact meaning of `κ` "lifting unchanged" through the whole tower.

**The categorical packaging — with precision.** The family `(κ_n)` forms a natural isomorphism `Λ_L ⇒ Λ_R` **in the category of sets**: the components are bijections, the squares commute. In the category of lattices with monotone maps, however, `κ_n` is not a morphism — it **reverses** the order; there its place is the second role (§4.2), contravariant. One family, two categorical roles, and both exact.

### 4.2. Duality of the lattice

Read on the Boolean lattice `(∧,∨,≤)`, `κ` is a **duality** — a contravariant involutive endofunctor reversing the order by de Morgan's law:

$$\kappa(a\wedge b)=\kappa(a)\vee\kappa(b),\qquad a\le b \iff \kappa(a)\ge\kappa(b),\qquad \kappa^2=\mathrm{id}. \qquad [●]$$

(`code_core/verify_functor_layers.py`.) The complement is the self-duality of the lattice with respect to the dualizing pair `{0,1}`: the same operator that swaps the poles and axes also inverts the whole order.

### 4.3. Coherence: one matrix

The triple role of `κ` — involution, Hodge star, Weyl duality — could require a coherence theorem: a proof that the three structures are consistent. The situation is stronger than a theorem.

> **Fact (one operator).** `κ` is one matrix `K` — the complement `x↦x+1ⁿ`. The raising `e` and coboundary `δ` are one 0/1-matrix; the lowering `f` and boundary `∂` are one. Therefore the "Hodge star" `κ∂=δκ` and the "Weyl exchange of roots" `κeκ=f` are literally **one and the same formula**, written in two vocabularies `[●]` (`code_core/verify_functor_coherence.py §3`).

The coherence of roles is an identity of a single operator. (The caveat about the fields in which these matrices are read — in chapter VI, where both structures are unfolded.)

### Summary

The complement `κ` bears its roles by a single operator: a natural isomorphism `Λ_L⇒Λ_R` in sets (`κ∘Λ_L=Λ_R∘κ`) `[●]`; a contravariant duality of the lattice (de Morgan) `[●]`; and — by one matrix — the Hodge star and the Weyl involution (chapter VI), coinciding as formulas `[●]`.


---

## Chapter V. The observer: terminal, monad, and the two ends of the tower of ranks

The fixed point of the complement is absent in every carrier (ch. I). This chapter gives the invariant its exact categorical place — a **terminal object** — and builds the apparatus by which the tower closes onto it: the monad of the free–forgetful adjunction. Then the symmetry is completed from below: the tower also has an **initial object**, and its trace in the construction — the Möbius function. The observer and the seed turn out to be the two ends of a single construction.

### 5.1. The monad from the adjunction

The free functor `F` (chapter I: the free `ℤ/2`-object) and the forgetful `U` form the adjunction `F⊣U`, and it generates the **monad** `T = ℤ/2×(−)` on sets: unit `η(s)=(0,s)`, multiplication `μ(a,b,s)=(a+b,s)`. All three monad laws are verified `[●]` (`code_core/verify_functor_fronts.py`, front 1).

> **Theorem (algebras of the monad).** The category of Eilenberg–Moore algebras `EM(T)` is exactly the category of sets with involution — carriers-with-`κ`. The structure map of an algebra is built from the involution constructively: `α(b,x)=σ^b(x)`, and the algebra laws hold for any involution `σ` — by derivation, uniformly `[●]` (`code_core/verify_functor_strict.py §2`; `code_core/verify_functor_coherence.py §2.3`).

The structure closes onto itself: the operation (the monad) and its carriers (the algebras) generate each other. This is the categorical skeleton of what the theory calls the ouroboros.

### 5.2. The observer — the terminal object

> **Theorem (terminal).** In the category of sets with involution the terminal object is one point with `κ=id`: the unique algebra whose action has a fixed point. From every carrier a unique morphism leads into it `Q_n → •`; the terminal itself does not lie among the free carriers, where the action is free `[●]` (`code_core/verify_functor_fronts.py`; `code_core/verify_functor_strict.py §1`).

There are no morphisms in the reverse direction: `\mathrm{Hom}(•,\,Q_n)=∅` — an equivariant point must pass into a fixed point, which does not exist in `Q_n`. The terminal is unembeddable into the scene; everything converges to it, nothing issues from it among the free carriers. This is the exact categorical form of the running thesis "the observer is outside every scene, yet is that to which the scene converges".

> **Theorem (constitutivity of non-inclusion).** In the full subcategory of free involutions (scenes) there is no terminal object at all: for the pair `P=({a,b}, swap)` an equivariant map into `T` is determined by a free choice of the image of `a`, whence `|\mathrm{Hom}(P,T)|=|T|`; terminality requires `|T|=1`, while the one-point action is not free. Symmetrically, adding a fixed point to a carrier destroys freeness: a scene that has included its invariant ceases to be a scene. The non-inclusion of the observer is constitutive — its presence among the states is incompatible with what it holds `[●]`.

> **Fact (two-sided forcedness).** On the body `[0,1]ⁿ` every continuous extension of `κ` has a fixed point (Brouwer), a free extension does not exist at all (Smith: a finite group does not act freely on a contractible finite-dimensional complex), while the canonical affine extension `κ̄(x)=1ⁿ−x` has exactly one — the center `σ½` `[●]` (classical; the affine case is a direct computation). The observer is discretely forbidden and continuously forced: this is the categorical-topological side of the seam.

(The full unfolded version of the theorem — with its satellites, a lineage from Lawvere and Hilbert to Spencer-Brown, and a reconnaissance of paths — is outside the present package.)

The terminal = the invariant `κ` — `[●]`, a theorem. "Observer" is the name of this invariant by the theory's definition; the whole additional load ("unfolds the scene", the dynamics of the ouroboros) is interpretation beyond terminality `[◐]`. The geometric identification of the terminal with the point `½` of the continuous side is the same `◐` as from the first rank (the point `½` lies on `|·|∞`); the categorical skeleton of the ouroboros is built, its geometric-dynamical flesh remains a front `[◐/○]`.

A kindred analogy from set theory: the removal of the self-complementary invariant beyond the carrier is the same move by which self-membership is handled. The observer relates to the tower as Russell's class to the universe of sets: a self-referential complement that has no place among the elements, yet which the construction is forced to name `[◐]` (`code_core/verify_zfc_in_dot.py`).

### 5.3. The initial object and Möbius: the second end

The terminal is the upper end; the category also has a lower one.

> **Statement (initial object).** The empty set `∅` with the empty involution is the initial object: from it a unique (empty) morphism leads into every carrier `[●]` (`code_core/verify_initial_mobius.py`).

The seed (`∅`, the beginning from which everything issues) and the observer (`•`, the terminal to which everything converges) are the two ends of a single category, and the tower is stretched between them. The trace of this duality in the arithmetic of the construction is the **Möbius function**: the reduced acyclicity of the complex (ch. VI) is the alternating-sign identity `Σ_{S}(−1)^{|S|}=[n=0]`, that is, the inversion `μ*ζ=δ` on the lattice — in numbers `1/ζ(s)=Σμ(n)n^{-s}` `[●]` (`code_core/verify_initial_mobius.py`; the assembly with number theory — document 03). The beginning-`∅` gives the unit of convolution, and Möbius is the operator of return to it.

The duality of the ends carries also the **method** of the theory. Each step of the generating construction takes the minimal object of the class specified by the conditions of the step — in rigorous form the initial (free) one: unique up to unique isomorphism, indicable by a formula and not invoking the axiom of choice (the finite minimum is a ZF theorem; the minimum everywhere is a well-ordering, equivalent to AC after Zermelo). The principle "the primitive of a theory = its initial object" is a classical line: Dedekind (recursion from the minimality of the chain, 1888), Birkhoff (free algebras, 1935), Gödel (the minimal inner model `L`, 1938), Lawvere (the natural-numbers object, 1963), Lambek (the initial algebra of a functor as its fixed point, 1968), the initial semantics of the Goguen–ADJ school (syntax is the initial algebra of a signature, 1977). The method of the theory lives on the initial end of the category, the subject of its main theorem on the terminal one: the generating construction and the non-includable observer are a dual pair `[●]`; the reading of the reversal of arrows as one more face of `κ` — `[◐]`.

### Summary

The tower is stretched between two ends: the initial object `∅` (the seed) and the terminal `•` (the invariant `κ`, the observer), with the monad `T=ℤ/2×(−)` of the free–forgetful adjunction, whose algebras are the carriers themselves `[●]`. From every carrier into the terminal — a unique morphism; in the reverse direction there are no morphisms (`\mathrm{Hom}(•,Q_n)=∅`) `[●]`. The non-inclusion is constitutive: in the subcategory of scenes there is no terminal, and adding a fixed point destroys the scene `[●]`; on the continuous body the fixed point, on the contrary, is forced (Brouwer/Smith) and unique — `σ½` `[●]`. The method is dual to the subject: the primitive is the initial, the observer is the terminal `[●]`. Möbius is the arithmetic trace of the beginning (`μ*ζ=δ`) `[●]`. The name "observer" and the full load of the ouroboros are interpretation over the theorem `[◐]`; the dynamics of the ouroboros is a front `[○]`, with a hypothesis in verifiable form: self-closure is one more form of the wall (document 01, chapter IX §9.3). A second front of the same kind `[○]` is the **distinction of the distinguishers**: the terminal is one, while the perspectives are many; how from a single terminal many points of view arise and are reconciled (sections of the quotient?) is open (document 01, chapter X §10.6).


---

## Chapter VI. The scene: grading, complex, motion, and balance

The scene of each rank bears two structures — the weight grading `sl₂` and the chain complex with the Hodge star — and both contract into one center by one operator `κ`. Below both structures are built, their literal coincidence at the level of matrices, the scene's own motion (holonomy and the Singer screw), and the construction's own conservation law — the discrete form of `∏=1`.

### 6.1. The weight grading `sl₂`

On each `Q_n` the Stanley triple of operators acts: `H` (weight `2k−n`, where `k` is the number of ones), `e` (raising: add a coordinate), `f` (lowering: remove). The relations

$$[e,f]=H,\qquad [H,e]=2e,\qquad [H,f]=-2f$$

hold **identically on all ranks** `n=1…5` `[●]` (`code_core/verify_functor_fronts.py`, front 2; `code_core/verify_functor_layers.py`). The uniformity, which had remained open in document 01 for `n>3`, is established: the base `sl₂`-triple is one for the whole tower. The weights are distributed unimodally with multiplicities `C(n,k)` and a peak at the middle `H=0` — the stratum of the observer.

The representation is given by an **explicit functor**: `V_n=(V_1)^{⊗n}` — the tensor power of the two-dimensional representation, the action by Leibniz `e_n=e_1⊗I+I⊗e_{n-1}`, lift = tensor multiplication by `V_1` `[●]` (`code_core/verify_functor_coherence.py §2`). The grading of the scene is the image of the functor of ranks into representations of `sl₂`. The complement here is the Weyl involution: `κeκ=f`, `κHκ=−H` `[●]`.

Open remains: the specific "octahedral algebra of rank 3", if it is richer than the base `sl₂`, is a separate question `[○]` (document 01, chapter III).

> **Remark (the scene as the terminal of the layer of realizations).** The edge rule of the active scene — "all poles are adjacent except the antipode" — is forced by terminality in the layer: among the `κ`-invariant antipode-free graphs on `2n` poles the orthoplex `K_{n×2}` is maximal — the **terminal realization of the fixed scene**, into which every other embeds (every non-edge of it is an antipodal pair) `[●]`. The forgetting of edges `U:\mathrm{Real}→\mathrm{Scene}` has a left adjoint `D⊣U` (the empty graph is the free realization); a right adjoint (cofree) it does not have — the orthoplex does not serve as a cofree object, the `Hom`-bijection breaks `[●]`. This is the categorical form of "the figure of the scene is forced as minimal" (document 03, §4.3). The full law, the Galois realization of the icosahedron, and the verifier — the note `Bridges/opposition_bridge.md`.

### 6.2. The chain complex and the Hodge star

The same lattice bears a second structure — a chain complex over `𝔽₂`: the weight layers `C_k` of dimension `C(n,k)`, boundary `∂` (remove a coordinate), coboundary `δ` (add):

$$\partial^2=0,\qquad \delta^2=0 \qquad [●]$$

— every pair of coordinates is removed by two paths, which over `𝔽₂` is zero (`code_core/verify_functor_layers.py`). The complex is reduced-acyclic: `Σ_k(−1)^k C(n,k)=0`. The complement in this vocabulary is the **Hodge star**, `κ∂=δκ`: it sends weight `k` into `n−k` and exchanges boundary with coboundary, making the figure self-dual. The lift is a **suspension**: `∂_{n+1}` is a cone over `∂_n` `[●]`.

### 6.3. One operator, two fields

The coincidence of the structures is literal, with one caveat that ought to be spoken. The raising `e` and the coboundary `δ` are **one integer 0/1-matrix**; the lowering `f` and the boundary `∂` are one; `κ` is one permutation matrix `[●]` (`code_core/verify_functor_coherence.py §3`). Therefore the Weyl exchange `κeκ=f` and the Hodge star `κ∂=δκ` are one formula in two vocabularies, and the coherence of the three roles of `κ` is an identity.

The caveat is the **field of reading**: the `sl₂` relations (`[e,f]=H`, eigenvalues `2k−n`) are read over `ℚ` — over `𝔽₂` they degenerate (`2e=0`); the identities of the complex (`∂²=0`), by contrast, are read over `𝔽₂` — over `ℤ` without signs `∂²=2(\cdot)≠0`. The matrices are one, the fields different: the grading is characteristic zero, the complex characteristic two. In this lies the exact form of the fact that one discrete figure bears two algebras.

### 6.4. Motion: holonomy and the screw

The scene bears its own rotation. At the third rank the active scene is the six-cycle `C₆`; its shift `T` has order six, and the half-turn coincides with the complement: `T³=κ` `[●]`. The quotient `C₆/κ` is a triangle, the covering `C₆→C₃` is connected — a nontrivial class in `H¹(S¹;ℤ/2)`, the discrete one-sidedness of the Möbius band `[●]` (`code_core/verify_functor_layers.py`).

On the axes the rotation is canonical for every rank — the Singer cycle on `PG(n−2,2)` of order `2^{n-1}−1`; the orders of neighboring ranks are coprime (`2^n−1=2(2^{n-1}−1)+1`), and therefore the addition of the rotation to the lift is a **screw**, not closing on any floor `[●]`.

### 6.5. The conservation law of the construction: discrete `∏=1`

The bricks above assemble into an own conservation law — without import from outside.

> **Statement (balance).** The construction bears two `κ`-mirror flows: `δ` (coboundary, growth outward) and `∂` (boundary, descent inward), conjugate by the Hodge star `κ∂=δκ`. Their balance is the reduced Euler characteristic
> $$\sum_k (-1)^k \binom{n}{k} = 0$$
> — the additive form of `∏=1`: what grew outward is exactly compensated by what came inward; two-sided around `σ½` (the spectrum is symmetric `k↔n−k`) `[●]` (`code_core/verify_machine_conservation.py`).

The identification of this additive balance with the multiplicative product formula `∏_v|x|_v=1` of the places of `ℚ` is a recognition of one form "full set → neutral" `[◐]`; this part of the construction itself is assembled from what is proved, without new input. Thereby "the seam = `∏=1`" holds as a property of the construction itself, independently of the import from number theory (the full stitching of the sides — document 03).

### Summary

The scene bears the grading `sl₂` (uniform across ranks, given by the functor `V_1^{⊗n}`, over `ℚ`) and the chain complex (`∂²=0`, Hodge `κ∂=δκ`, suspension, over `𝔽₂`) — by **the same matrices** under two fields of reading; `κ` combines the Weyl involution and the Hodge star by one identity `[●]`. The scene moves (holonomy `T³=κ` with Möbius; the Singer screw without closure) and balances (`Σ(−1)^kC(n,k)=0` — discrete `∏=1`) `[●]`.


---

## Chapter VII. The continuous side as a spectral limit

The continuous side — where the invariant-observer `½` lies — appears in the construction by derivation: as a **limit of the spectrum**. Here the limit itself is established (the Gaussian measure), the derivable metric (Connes distance = Hamming), and the exact boundary of the derivation — by one equation `[κ,Δ]=0`. The chapter is closed by a view from the side of set theory: the discrete tower is `V_ω`, and the axiom of Infinity is the seam itself.

### 7.1. The Laplacian and its spectrum

On the chain complex (ch. VI) the Laplacian `Δ_n=∂δ+δ∂` is defined; on the scalar layer it equals the Laplacian of the hypercube `Δ_n=nI−A` (`A` is the adjacency) with spectrum `{2k: k=0…n}` and multiplicities `C(n,k)`; the heat trace factorizes:

$$\mathrm{Tr}\,e^{-t\Delta_n}=(1+e^{-2t})^n. \qquad [●]$$

(`code_core/verify_continuum_limit.py`.)

### 7.2. The limit — the Gaussian measure

> **Theorem (limit).** The centered and normalized spectrum (weight `k` with weights `C(n,k)/2^n`) converges as `n→∞` to the **Gaussian measure** on the line — by the central limit theorem `[●]` (`code_core/verify_continuum_limit.py`).

The complement `κ` sends the weight layer `k` into `n−k`, that is, in the centered variable acts by the involution `λ↦−λ` — the Hodge star of the limit measure; its fixed point is the center, that very `σ½`-invariant. The continuous side is **derived** as a spectral limit-measure; in this lies the exact form of the "continuous completion" of the carrier.

What the limit gives is a measure. What it does not give is Riemannian geometry `(M,g)`: the spectral dimension of the hypercube does not stabilize, the limit is a measure on the line, not a manifold `[●]`. Metric, dimension, signature are a structure of another kind (see §7.4 and ch. IX).

### 7.3. The metric is derived: Connes distance

The discrete side, meanwhile, does have a metric, and it is not postulated.

> **Statement (Connes = Hamming).** The spectral Connes distance `d(x,y)=\sup\{|f(x)−f(y)|:\ \mathrm{Lip}(f)\le 1\}` on the carrier coincides with the geodesic — Hamming — one `[●]` (`code_core/verify_connes_metric.py`).

The metric is derived from the same spectral triple — and it is **Euclidean** (positive).

### 7.4. The boundary by one equation: `[κ,Δ]=0`

> **Fact (decisive).** The complement commutes with the Laplacian: `[κ,Δ]=0` — for `κ` is a graph automorphism of the carrier and the Hodge star of the complex `[●]` (`code_core/verify_lorentz_signature.py`).

From this one fact — three boundaries at once (`code_core/verify_dynamics_spectral.py`, `code_core/verify_lorentz_signature.py`):

- **signature:** the `κ`-splitting of the spectrum into `±1`-subspaces gives equal dimensions `\dim H_+=\dim H_-=2^{n-1}` — the neutral signature `(k,k)`, without the asymmetry of a "single time"; the Lorentzian `(1,n−1)` does not issue from `κ`;
- **dynamics:** all `κ`-`Δ`-constructs vanish — `κΔκ−Δ=0`, `[κ,Δ]=0`, the `\mathrm{Tr}(κΔ)`-curvature `=0`; the action reduces to `\mathrm{Tr}(Δ)` without a curvature term;
- **evolution:** an operator generating dynamics must **not** preserve the Laplacian — there are none such among the combinatorics of `κ`.

Energy (`Δ`), the causal order (`⊆`, ch. VIII), the arrow (the comonad, ch. VIII), and the Euclidean metric the construction does have; the Lorentzian signature, curvature, and dynamical evolution are **input**. The boundary is named by one proved equality.

### 7.5. Set theory: `V_ω` and the Infinity-seam

The same boundary is visible from the side of foundations. The whole discrete carrier `⋃Q_n`, read by the Ackermann encoding (`a∈b ⟺` bit `a` of the number `b`), is exactly the hereditarily-finite sets `V_ω`: all axioms of ZF except Infinity hold, and choice on the finite is a theorem `[●]` (`code_core/verify_zfc_in_dot.py`). The axiom of Infinity — the completed union as a single object — is precisely the passage to the continuous side; as shown above, it gives a **measure**, not the cumulative hierarchy `V_{ω+}` `[◐]` — the seam.

### Summary

The continuous side is derived: the spectral limit of the Laplacian is the Gaussian measure with the Hodge star `λ↦−λ` and the observer-center `[●]`; the metric — Connes distance — coincides with the Hamming one and is Euclidean `[●]`. The boundary of the derivation is the single equality `[κ,Δ]=0`: the signature is balanced `(k,k)`, the `κ`-curvature and `κ`-dynamics are zero — the Lorentzian structure and evolution are input `[●]`. The discrete tower is `V_ω`; Infinity is the seam to the measure `[◐]`.


---

## Chapter VIII. Time as a traversal, not a coordinate

The construction is static: the complement commutes with the Laplacian, and none of its operators generates evolution — as in the constraint equation `ĤΨ=0`, where the whole does not evolve. Time appears in it by a **traversal**: by the order of reading the structure. Time is decomposed into three layers — linear (the flag), cyclic (the clock), and the arrow (the comonad) — together with the causal order, in which the observer turns out to be the "now".

### 8.1. The statics of the whole

The global state of the tower is static: `[κ,Δ]=0` (ch. VII), there is no evolving operator in the combinatorics of the complement `[●]` (`code_core/verify_time_emergence.py`). This is the discrete analogue of the Wheeler–DeWitt situation: the whole does not move. Time, if it is to be, is a property of the reading.

### 8.2. Linear time: the flag

Linear time is a **maximal chain** of the lattice: the flag `∅⊂\{a\}⊂\{a,b\}⊂…⊂[n]`. There are `n!` such chains, each step is one `δ`-event, the addition of a coordinate `[●]`. History is the sequence of accomplished distinctions.

An event, meanwhile, is a **transition**: an oriented edge `x→x∪\{i\}`, one act of distinction. The states (vertices) are fixed; an event is a morphism.

### 8.3. Cyclic time: the clock

Cyclic time is the rotation `T` of the scene (ch. VI: `T³=κ` at the third rank). Under the division of the carrier into a **clock** and a **world** (the Page–Wootters mechanism) the conditional state of the world evolves with the reading of the clock, whereas the whole remains static `[●]` (`code_core/verify_time_emergence.py`). Neither the flag nor the rotation enters the Laplacian: both are traversals.

### 8.4. The arrow: the comonad of observation

The complement — invertible (`κ²=id`) and static (`[κ,Δ]=0`) — cannot be a source of irreversibility; it comes from the **comonad of observation**:

$$G=\Lambda_L\circ\pi \qquad (\text{forget the coordinate and embed back}).$$

> **Statement (arrow).** `G` is idempotent (`G²=G`: a coarsening cannot be undone — information is lost) and does not commute with the Laplacian (`[G,Δ]\neq 0`) `[●]` (`code_core/verify_time_emergence.py`; `code_core/verify_growth_directions.py`).

This is exactly the operator that the boundary of chapter VII required: **not preserving the Laplacian**, irreversible — setting a direction. And it is internal: `G` is part of the already-present adjoint triple (`Λ_L∘π` is the comonad of the adjunction `Λ_L⊣π`). Of the three candidates for the source of direction (sheaves, braiding, comonad) the first two are a program and input `[○]`, the comonad is established `[●]` (`code_core/verify_growth_directions.py`).

### 8.5. The causal order: cones and the "now"

Causality is already given by inclusion `⊆`: the carrier is a causal set, where the future and past cones of an event are `\{y⊇x\}` and `\{z⊆x\}`, time is the chains (timelike), space the antichains (spacelike) `[●]` (`code_core/verify_causal_structure.py`).

> **Fact (Sperner).** The largest antichain of the lattice is the middle layer: the observer `σ½` is the **maximal slice of simultaneity**, the "now" `[●]`.

The arrow-comonad is consistent with the order (coarsening leads downward along `⊆`). What the order does not give is a fixed dimension: as a causal set the lattice canonically bears `d=1` (a chain — pure time) and `d=∞` (the whole lattice); `3+1` is attainable by a choice of a four-dimensional thinning, but this is a choice of embedding, input `[●` attainability / `○` not a derivation`]` (`code_core/verify_dimension_choice.py`).

### Summary

Time in the construction is a traversal: linear — the flag of `n!` chains of `δ`-events; cyclic — the clock-rotation (Page–Wootters, the whole static); the arrow — the comonad of observation `G=Λ_L∘π` (`G²=G`, `[G,Δ]≠0`) — an irreversible operator from the adjoint triple itself `[●]`. The causal order — inclusion `⊆` (cones; the "now" = the middle layer by Sperner = `σ½`) `[●]`; dimension and signature — input `[○]`.


---

## Chapter IX. The boundary: input and external bridge

The categorical construction is complete in itself — and precisely therefore is obliged to name where it ends. This chapter gathers the boundary in full: what the construction cedes to **input** (and why — by one equation), how its single **external bridge** looks (the functor into free spins), and what happens on the first step past the bridge (mass: the form is forced, the value is free). This is the wall of the series — named exactly, with the mechanism.

### 9.1. Input, reduced to one equality

All that separates the geometry of spacetime from the order reduces to the fact `[κ,Δ]=0` (ch. VII):

| required | what the construction gives | status |
|---|---|---|
| Lorentzian signature `(1,n−1)` | the `κ`-splitting is balanced `(k,k)` | input `[○]` |
| curvature / action term | `\mathrm{Tr}(κΔ)=0`, action = `\mathrm{Tr}(Δ)` | input `[○]` |
| dynamical evolution | all `κ`-`Δ`-constructs `=0`; an operator not preserving `Δ` is needed | input `[○]` (the internal candidate for the arrow — the comonad, ch. VIII) |
| dimension `3+1` | canonically `d=1` and `d=∞`; `3+1` — a choice of thinning | input `[○]` |
| manifold `(M,g)` | the limit is a measure, not a manifold | input `[○]` |

The construction does have: energy (`Δ`), the causal order (`⊆`), the arrow (`G`), the Euclidean metric (Connes=Hamming), the balance (`Σ(−1)^kC(n,k)=0`). The boundary is a consequence of one proved equality `[●]`.

### 9.2. The external bridge: the functor into free spins

The single verified bridge outward is the functor `F: Q_n →` spin systems:

$$A(Q_n) \;\equiv\; \sum_i \sigma_x^{(i)} \qquad (\text{literal equality of operators}),$$

lift ↦ add a spin, `κ` ↦ global flip, `σ½` ↦ massless center; functoriality is verified on four operations `[●]` (`code_core/verify_functor_spin.py`, 45 checks). But the image is a **free** system: there is no interaction in the cube itself. The bridge is built at one point; beyond that — a front `[◐→○]`.

### 9.3. The first step past the bridge: mass — the form is forced, the value is free

What happens if the bridge is given a minimal input — the weights `w_i`? Investigated without fitting (`code_core/verify_mass_gap_input.py`):

- **the cube without weights is massless** `[●]`: spectrum `{n−2k}`, the center `λ=0` is degenerate (`C(n,n/2)`), there is no gap — vertex-transitivity;
- **the weights give a gap, but not a value** `[●]`: incommensurable `w_i` open `Δ_{\text{gap}}=\min|\sum\pm w_i|>0`, however `Δ(2w)=2Δ(w)` — the scale is stretchable, the value of the mass is not forced;
- **there is no distinguished set of weights** `[●]`: the `S_n`-symmetry of the cube makes all permutations of `w` equivalent — the value is free, input;
- **the form is forced** `[●]`: for any `w` the spectrum is symmetric `±λ` (particle-hole symmetry from `\{A_w,Z\}=0`), while a genuine gap requires an **interaction** (a `σ_z σ_z`-term), which is not in the cube.

The summary of the step: the structure forces the **form** of the spectrum (the symmetry, who can interact with whom), but not the **values** (the weights, the strengths). This is the same wall of values as in the whole corpus — seen from the functorial branch by its own means.

### 9.4. Localization of the question of the morphism

The objection "between the discrete and physics there is no morphism — there are coincidences of values" receives, after this series, an exact localization:

- the **core** — the growth of ranks — is functorial and proved (ch. I–VI): the adjoint triple, the isomorphism of the growth law, the naturality of `κ`, the monad with two ends, the functor of representations; without an exit into physics and without the wall of values;
- the **external bridge** is real, but at one point (free spins), and runs up against the weights-input `[◐→○]`;
- the objection, therefore, pertains to the **application**; the construction remains outside it: the internal coherence of the theory is established independently of whether it reaches physics.

### Summary

The boundary of the construction is named with the mechanism: the Lorentzian signature, curvature, evolution, `3+1`, `(M,g)` — input, and all this is consequences of one equality `[κ,Δ]=0` `[●]`. The external bridge — the functor into free spins, exact at one point `[●]`, beyond that a front `[◐→○]`; the first step past it shows the wall of values in pure form: the form is forced, the value is free `[●]`.


---

## Epilogue. The whole construction and its two models

The series has gone through the construction layer by layer; it remains to see it in a single glance and return it to its place among the models.

### The construction in one paragraph

The operation of distinction — an involution without fixed points — generates the carrier as a **free object** (ch. I). Growth is an **adjoint triple** `Λ_L⊣π⊣Λ_R`, monoidal (`Q_{m+n}=Q_m□Q_n`, ch. II). The growth law is an **isomorphism of projective spaces** `PG(n−1,2)≅U_{n+1}/κ`: the content of a rank becomes the axes of the next (ch. III). The complement is **one operator** in three roles: a natural isomorphism `Λ_L⇒Λ_R` (in sets), de Morgan duality, and — by one matrix — the Hodge star = the Weyl involution (ch. IV, VI). The tower is stretched between the **beginning** `∅` (the seed; its arithmetic trace — Möbius `μ*ζ=δ`) and the **terminal** `•` (the invariant `κ`; from every carrier — a unique morphism into it, back — not one: `\mathrm{Hom}(•,Q_n)=∅`); the carriers are algebras of the monad `ℤ/2×(−)` (ch. V). The scene bears the grading `sl₂` (the functor `V_1^{⊗n}`, over `ℚ`) and the complex (`∂²=0`, over `𝔽₂`) by the same matrices; moves by holonomy `T³=κ` and the Singer screw; balances by the discrete `∏=1` (ch. VI). The continuous side is a **spectral limit**: the Gaussian measure, the Connes = Hamming metric (ch. VII). Time is a **traversal**: the flag, the clock, the arrow-comonad `G` (`[G,Δ]≠0`), the causal order `⊆` with the "now" = `σ½` by Sperner (ch. VIII). The boundary is one equality `[κ,Δ]=0`: signature, curvature, evolution, dimension, `(M,g)` — input; the external bridge — free spins, one point; mass — the form is forced, the value is free (ch. IX).

The metric realization of these two ends — the seed as the source of the address tree, the observer as the apex of the cone — the bridge note `Bridges/radial_bridge.md`.

### Two models, one functor

This series is defined on **bits** `Q_n=𝔽₂ⁿ` — the side of structure. The second, independent model is **numbers** `D(N)` (document 03): there the same morphisms (`κ`=complement `d↦N/d`, `H`=number of primes, lift=multiplication, `π`=remove a factor) coincide under the functor `Λ:S↦∏p`, and beyond that contains what is invisible to the bits — the height `^` (multiplicity `v_p`) and the grading of the arrow `P`. The numbers are a **tuning fork** (an independent model against which the belonging of a property to the construction is checked): what holds in both models is the functor of the construction; what is in one — a shell over it. The coordinated expositions are document 01 (chapter VIII: the same construction in overview, in the general series) and document 03 (chapter VII: the functorial layer of numbers).

### The register in closing

- `[●]` — the free carrier (`|\mathrm{Hom}|=|Y|^{2^{n-1}}`); the triple `Λ_L⊣π⊣Λ_R`; monoidality `□`; the isomorphism `PG(n−1,2)≅U_{n+1}/κ` (linear, with lines); `κ∘Λ_L=Λ_R∘κ`; de Morgan; one matrix (Hodge=Weyl); the monad `ℤ/2×(−)`, `EM`=carriers, terminal and initial object, `\mathrm{Hom}(•,Q_n)=∅`; Möbius `μ*ζ=δ`; `sl₂` is uniform (the functor `V_1^{⊗n}`); `∂²=0`, suspension; `T³=κ`, Möbius-covering, the Singer screw; `Σ(−1)^kC(n,k)=0`; spectral limit=Gaussian; Connes=Hamming; `[κ,Δ]=0` and its consequences; `V_ω`=discrete, finite choice=theorem; flag/clock/comonad-arrow; Sperner-"now"; spin-bridge (one point); mass: form.
- `[◐]` — the name "observer" and the load of the ouroboros beyond terminality; the geometric `½` on the reverse side; the naturality of the `PG`-isomorphisms to the lift; the additive balance = the multiplicative `∏=1` (one form); Infinity=the seam to the measure; Russell's class.
- `[○]` — the 2-category / Grothendieck construction over the ranks; the dynamics of the ouroboros (hypothesis: self-closure is one more form of the wall); the distinction of the distinguishers (the multiplicity of perspectives under a single terminal); the specific algebra of rank 3; the Lorentzian signature, curvature, evolution, `3+1`, `(M,g)` — input; the values of the weights/masses.

The construction is built, its boundary named with the mechanism: the proved is proved enumerably, the inputs are named. The functorial coherence of the theory is internal, and it is established; the external bridges are a separate work with their own wall. The question of the morphism is localized: it pertains to the bridge, the core stands.
