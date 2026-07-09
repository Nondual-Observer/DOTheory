# Categorical Core: Construction and Proofs

This section presents the functorial part of the theory: the carrier as a free object, the lift as an adjoint triple, the growth law as an isomorphism of projective spaces, the observer as a terminal object. Every stage is proved in the text or confirmed by a verifier from the `code_core/` folder — 18 scripts, 385 checks, all passing. The introduction, nine chapters, and epilogue follow as a single document.

---

## Introduction: the functoriality of the theory

### Subject and method

The question of the theory's functoriality has two forms, and they must be kept separate. The **external** form: does a structure-preserving map exist from the discrete construction to physical models? Such a map runs into input values — weights and constants absent from the bare structure; its exact boundary is worked out in chapter IX. The **internal** form: is the categorical construction itself the mathematical core — the growth of ranks? Here there are no input values, and the answer is established rigorously.

This series establishes the internal form: **the tower of carriers `Q_n=𝔽₂ⁿ` is a categorical construction.** The carrier is the free object of an operation; growth is an adjoint and monoidal triple; the growth law is an isomorphism of projective spaces; the complement is one operator in coherent roles; the tower is stretched between an initial object and a terminal; the scene carries a grading and a complex via the same matrices; the continuous side is derived as a spectral limit; time is a traversal, the arrow is a comonad; the boundary of the construction reduces to one identity `[κ,Δ]=0`.

The mode of exposition is proof-driven narrative: prose leads, and every mathematical step is either proved on the spot or referred to a verifier (`code_core/verify_*.py`).

### Statement statuses

The status marking is uniform across all sections of the package and is defined in the introduction of the "Exposition" section (document 01). Briefly: `[●]` — proved (a theorem, an identity, a verified construction; thus, the terminal object and the uniqueness of morphisms into it is a theorem); `[◐]` — reading (a name or a recognition layered on a theorem; thus, "observer" is the name of the terminal by the theory's definition); `[○]` — input or open (what the construction receives from outside, or what remains unproved; thus, Lorentzian signature is an input).

### Outline

Chapter order: **the carrier from the operation** (I) → **the lift: an adjoint triple** (II) → **the growth law** (III) → **the complement** (IV) → **the observer: terminal and monad** (V) → **the scene: grading, complex, motion, balance** (VI) → **the continuum limit** (VII) → **time as traversal** (VIII) → **the boundary: input and the external bridge** (IX) → epilogue: the construction as a whole and its two models.

The series is self-contained: notions of category theory are introduced at the point of use, with direct meaning. Parallel expositions are the "Exposition" section (document 01; its chapter VIII gives the same construction in overview, within the general series of ranks) and the number model (document 03; its chapter VII is the functorial layer of the second model). Beyond them, this document unfolds the full proof layers: the triple of adjoints on all pairs, the strict status of the growth law, the coherence of `κ` as a single matrix, the two ends of the tower with the Möbius band, the conservation law of the construction, the spectral derivation of the continuous side, the arc of time, and the exact boundary `[κ,Δ]=0`.

---

## Chapter I. The carrier from the operation: a free object

The functorial exposition begins at the same place as the whole theory — the operation of distinction. The difference is in **what** is claimed here: the carrier **is derived** from the operation as its free orbit, without postulating a ready-made set on which the operation then acts. Below this derivation is carried out rigorously; this closes the front "the carrier as a colimit before the carrier," which had remained open (document 01, chapter I).

### 1.1. The operation is primary

The initial object is a **fixed-point-free involution** `κ`, `κ²=id`: the minimal act of distinction, sending each side to its opposite. On a rank-`n` carrier it is realized by the complement `κ(x)=x+1ⁿ` over `𝔽₂`.

> **Statement 1 (freeness of the action).** The equation `κ(x)=x` is unsolvable in every `Q_n=𝔽₂ⁿ`: it would imply `1ⁿ=0`. The action of `ℤ/2=⟨κ⟩` on `Q_n` is free, and the carrier splits into exactly `2ⁿ⁻¹` orbit-pairs `{x,κx}` `[●]` (`code_core/verify_functor_core.py §E`, `n=1…6`).

Each orbit is a copy of the regular representation of `ℤ/2`. Thus `Q_n` is `2ⁿ⁻¹` copies of the simplest free action.

### 1.2. The universal property

The word "free" carries two related meanings here, and both are exact. The action is free: `κ` fixes no point, and so no pair degenerates — there are no forced identifications. The object is free: the carrier is generated by the operation with no relation beyond `κ²=id` — it contains nothing except what the operation itself forces. The second meaning is the universal property:

> **Statement 2 (free object).** For any set with involution `Y`, an equivariant map `Q_n → Y` is determined by a free choice of image on one representative per orbit; the image of the second element of the pair is forced by equivariance. The number of morphisms
> $$\bigl|\mathrm{Hom}_{ℤ/2}(Q_n,\,Y)\bigr| \;=\; |Y|^{\,2^{n-1}} \;=\; |Y|^{\#\text{orbits}}. \qquad [●]$$
> (`code_core/verify_functor_fronts.py`, front 3.)

This is the definition of a free object, witnessed by exhaustive check: `Q_n` is a free `ℤ/2`-set on `2ⁿ⁻¹` generators. The rank-one carrier is the free object on a single point: the regular orbit `{0,1}`.

### 1.3. "The carrier before itself" — front closed

The meaning of the construction: **the operation is primary, the carrier derivative**. `Q_n` arises as an orbit-colimit of the involution — the universal object among all `κ`-sets. The promise "the carrier as a colimit of the operation" is fulfilled by pure combinatorics, with no physics and no wall of values: the front is **closed** `[●]`.

### Summary

The operation of distinction `κ` (a fixed-point-free involution) generates the carrier: `Q_n` is a free `ℤ/2`-object on `2ⁿ⁻¹` orbits, with the universal property `|\mathrm{Hom}(Q_n,Y)|=|Y|^{2^{n-1}}` `[●]`. The front "the carrier before itself" is closed: the operation is primary, the carrier is derived.


---

## Chapter II. The lift: an adjoint triple and monoidality

Growth of rank — the lift `Q_n → Q_{n+1}` — is the central operation of the tower. This chapter establishes its categorical form: the lift is an **adjoint functor** — indeed a triple at once — and it is **monoidal**: composite ranks are built tensorially. Adjacent ranks are linked by adjunction, i.e. by a universal property, and all arbitrariness is excluded from the linkage of ranks.

### 2.1. Three maps

The objects are Boolean lattices `Q_n=𝔽₂ⁿ` with the inclusion order on masks `x≤y ⟺ x⊆y`. Between adjacent ranks three monotone maps act:

- **projection** `π: Q_{n+1}→Q_n` — forget the top coordinate;
- **left lift** `Λ_L(x)=(x,0)` — embed, new coordinate `0`;
- **right lift** `Λ_R(x)=(x,1)` — embed, new coordinate `1`.

### 2.2. The adjoint triple

> **Theorem (the triple).** On Boolean lattices both Hom-isomorphisms hold:
> $$\Lambda_L \dashv \pi \dashv \Lambda_R,$$
> that is, `Λ_L(x) ≤ y ⟺ x ≤ π(y)` and `π(y) ≤ x ⟺ y ≤ Λ_R(x)` for all `x∈Q_n`, `y∈Q_{n+1}` `[●]` (`code_core/verify_functor_core.py §A`, all pairs, `n=1…4`).

Both Hom-isomorphisms reduce to coordinatewise comparison: `(x,0)≤(y',b) ⟺ x≤y'` — the left adjunction; `(y',b)≤(x,1) ⟺ y'≤x` — the right one. The classical model for the construction is `∃ ⊣ substitution ⊣ ∀` in predicate logic — the lift stands to the projection as a quantifier stands to substitution.

The unit of the adjunction is the identity `π∘Λ_L = π∘Λ_R = id` `[●]` (`§B`): the projection reverses the lift. Composition of lifts is correct (`Q_n→Q_{n+2}`) `[●]`. The tower is the iteration of a single adjoint functor.

### 2.3. Monoidality

The lift is also consistent with the product of ranks.

> **Statement (monoidality).** `Q_{m+n} = Q_m □ Q_n` (the Cartesian product of graphs) with coordinatewise complement `κ_{m+n} = κ_m ⊗ κ_n`; the lift is multiplication by an edge, `(−) □ K₂` `[●]` (`code_core/verify_functor_layers.py`).

Repeated lifting builds ranks tensorially: `Q_n = K₂^{□n}`. The first composite rank `4=2×2` gives `Q₄=Q₂□Q₂` — the place where the system of directions first splits in two (in the terms of document 01 — the break, its chapter IV; here the monoidal formula alone suffices).

### Summary

The lift is an adjoint triple `Λ_L⊣π⊣Λ_R` on Boolean lattices (Hom-isomorphisms on all pairs, unit `π∘Λ=id`) and a monoidal functor (`Q_{m+n}=Q_m□Q_n`, lift `=□K₂`) `[●]`. Growth of the tower is the iteration of an adjoint and monoidal functor.


---

## Chapter III. The growth law: the content of a rank becomes the axes of the next

The heart of the tower is the growth law: what was the content of a rank becomes, at the next rank, the axes. This chapter establishes its precise status — an **isomorphism of projective spaces**, given by a linear embedding — and separates what is established from what, beyond the isomorphism, is not yet claimed.

### 3.1. Statement

The active scene of rank `n+1` — the carrier without its two poles, `U_{n+1}=Q_{n+1}∖\{0,1^{n+1}\}` — splits under `κ` into axes (`κ`-pairs `{x,κx}`). The set of axes is the projective space of the previous rank:

$$\mathrm{PG}(n{-}1,2) \;\cong\; U_{n+1}/\kappa, \qquad |\cdot| = 2^{n}-1.$$

The count is immediate (`(2^{n+1}-2)/2 = 2^n-1`); the content of the statement lies in the structure of the correspondence.

### 3.2. Explicit bijection and its linearity

> **Theorem (isomorphism of projective structures).** The map `φ(a)=2a` (coordinate shift) realizes the correspondence: each `κ`-pair in `U_{n+1}` contains exactly one even element, and `φ` is a bijection of the nonzero vectors of `𝔽₂ⁿ` onto the system of even representatives. Moreover `φ` is **linear** (`φ(a⊕b)=φ(a)⊕φ(b)`), and hence preserves incidence: lines `{a,b,a⊕b}` map to collinear triples. The correspondence is an isomorphism of projective spaces, with line structure (stronger than a bijection of points) `[●]` (`code_core/verify_functor_core.py §C`; `code_core/verify_functor_strict.py §3`, `n=2…5`).

Behind the bijection lies linear algebra: `κ`-orbits are the cosets of the line `⟨1^{n+1}⟩`, the quotient `𝔽₂^{n+1}/⟨1^{n+1}⟩≅𝔽₂ⁿ` is a vector space, its nonzero classes are the points of `PG(n−1,2)`; `φ` is a section of the quotient. Over `𝔽₂` projective points coincide with nonzero vectors, and the whole projective structure is canonical.

Thus at the third rank the three axes of the scene are `PG(1,2)`; at the fourth, seven axes fold into the Fano plane `PG(2,2)`, each of whose lines is a copy of this triple; at the fifth, `PG(3,2)` with fifteen points.

### 3.3. The boundary of the statement: isomorphism and naturality

What is established: a **rank-by-rank isomorphism of structures** — points and lines, for each `n`. What is not established (and not assumed): that the family of these isomorphisms is **natural with respect to the lift** — that the square formed by `φ_n`, `φ_{n+1}` and the growth maps commutes. This is a separate statement, an open front `[◐]` (`code_core/verify_functor_strict.py`, conclusion §3).

The isomorphism gives the growth law a rigorous mathematical status at each floor; naturality would link the floors into a single diagram. The first is proved, the second is open.

### Summary

The growth law is established as an isomorphism of projective spaces `PG(n−1,2)≅U_{n+1}/κ`: an explicit linear bijection `φ(a)=2a`, incidence preserved `[●]`. The content of a rank — its projective space — becomes the axes of the `κ`-scene of the next rank. The naturality of the family of isomorphisms with respect to the lift is a separate open question `[◐]`.


---

## Chapter IV. The complement: one matrix in three roles

The complement `κ` enters the exposition three times: as naturality with respect to the lift, as lattice duality, and — ahead, in chapter VI — as the Hodge star, coinciding with the Weyl involution. Here the first two roles are established, along with the main coherence fact: all roles are carried by **one operator**, one matrix, and the agreement of roles is an identity, with no separate coherence theorem needed.

### 4.1. Naturality with respect to the lift

> **Theorem (naturality).** For all ranks
> $$\kappa_{n+1}\circ\Lambda_L \;=\; \Lambda_R\circ\kappa_n \qquad [●]$$
> (`code_core/verify_functor_core.py §D`, `n=1…5`).

The check is a single line: `κ_{n+1}(x,0) = (κ_n x, 1) = Λ_R(κ_n x)`. To lift and then complement is the same as to complement and then lift into the other embedding. The complement swaps the two adjoint lifts; this is the exact sense in which `κ` "lifts unchanged" through the whole tower.

**Categorical packaging — with a qualification.** The family `(κ_n)` forms a natural isomorphism `Λ_L ⇒ Λ_R` **in the category of sets**: the components are bijections, the squares commute. In the category of lattices with monotone maps, however, `κ_n` is not a morphism — it **reverses** order; there its place is the second role (§4.2), the contravariant one. One family, two categorical roles, and both exact.

### 4.2. Lattice duality

Read on the Boolean lattice `(∧,∨,≤)`, `κ` is a **duality** — a contravariant involutive endofunctor, reversing order by De Morgan's law:

$$\kappa(a\wedge b)=\kappa(a)\vee\kappa(b),\qquad a\le b \iff \kappa(a)\ge\kappa(b),\qquad \kappa^2=\mathrm{id}. \qquad [●]$$

(`code_core/verify_functor_layers.py`.) The complement is the lattice's self-duality with respect to the dualizing pair `{0,1}`: the same operator that swaps the poles and the axes also inverts the whole order.

### 4.3. Coherence: one matrix

The triple role of `κ` — involution, Hodge star, Weyl duality — might seem to demand a coherence theorem: a proof that the three structures agree. The situation is stronger than a theorem.

> **Fact (one operator).** `κ` is one matrix `K` — the complement `x↦x+1ⁿ`. The raising operator `e` and the coboundary `δ` are one 0/1-matrix; the lowering operator `f` and the boundary `∂` are one. Hence "the Hodge star" `κ∂=δκ` and "the Weyl swap of roots" `κeκ=f` are literally **one and the same formula**, written in two dictionaries `[●]` (`code_core/verify_functor_coherence.py §3`).

Coherence of the roles is the identity of a single operator. (A qualification about the fields over which these matrices are read is given in chapter VI, where both structures are unfolded.)

### Summary

The complement `κ` carries its roles with one operator: a natural isomorphism `Λ_L⇒Λ_R` in sets (`κ∘Λ_L=Λ_R∘κ`) `[●]`; a contravariant lattice duality (De Morgan) `[●]`; and — one matrix — the Hodge star and the Weyl involution (chapter VI), coinciding as formulas `[●]`.


---

## Chapter V. The observer: terminal, monad, and the two ends of the tower of ranks

The complement has no fixed point in any carrier (ch. I). This chapter gives the invariant a precise categorical place — the **terminal object** — and builds the apparatus by which the tower closes onto it: the monad of the free–forgetful adjunction. Symmetry is then completed from below: the tower also has an **initial object**, and its trace in the construction is the Möbius function. The observer and the seed turn out to be two ends of one construction.

### 5.1. A monad from adjunction

The free functor `F` (chapter I: free `ℤ/2`-object) and the forgetful functor `U` form an adjunction `F⊣U`, and it generates a **monad** `T = ℤ/2×(−)` on sets: unit `η(s)=(0,s)`, multiplication `μ(a,b,s)=(a+b,s)`. All three monad laws are checked `[●]` (`code_core/verify_functor_fronts.py`, front 1).

> **Theorem (algebras of the monad).** The category of Eilenberg–Moore algebras `EM(T)` is exactly the category of sets with involution — carriers-with-`κ`. The structure map of an algebra is built constructively from the involution: `α(b,x)=σ^b(x)`, and the algebra laws hold for any involution `σ` — by derivation, uniformly `[●]` (`code_core/verify_functor_strict.py §2`; `code_core/verify_functor_coherence.py §2.3`).

The structure closes on itself: the operation (the monad) and its carriers (the algebras) generate each other. This is the categorical skeleton of what the theory calls the ouroboros.

### 5.2. The observer — a terminal object

> **Theorem (terminal).** In the category of sets with involution, the terminal object is a single point with `κ=id`: the unique algebra whose action has a fixed point. From every carrier there is a unique morphism `Q_n → •` into it; the terminal itself does not lie among the free carriers, where the action is free `[●]` (`code_core/verify_functor_fronts.py`; `code_core/verify_functor_strict.py §1`).

There are no morphisms in the reverse direction: `\mathrm{Hom}(•,\,Q_n)=∅` — an equivariant point would have to map to a fixed point, which does not exist in `Q_n`. The terminal is not embeddable in the scene; everything converges to it, nothing among the free carriers issues from it. This is the exact categorical form of the recurring thesis "the observer is outside every scene, yet is that to which the scene converges."

> **Theorem (constitutivity of non-inclusion).** In the full subcategory of free involutions (scenes) there is no terminal object at all: for the pair `P=({a,b}, swap)`, an equivariant map into `T` is determined by a free choice of the image of `a`, whence `|\mathrm{Hom}(P,T)|=|T|`; terminality would require `|T|=1`, and a one-point action is not free. Symmetrically, adjoining a fixed point to a carrier destroys freeness: a scene that includes its own invariant ceases to be a scene. The observer's non-inclusion is constitutive — its presence among the states is incompatible with what it holds `[●]`.

> **Fact (two-sided forcedness).** On the body `[0,1]ⁿ` every continuous extension of `κ` has a fixed point (Brouwer); no free extension exists at all (Smith: a finite group does not act freely on a contractible finite-dimensional complex); and the canonical affine extension `κ̄(x)=1ⁿ−x` has exactly one — the center `σ½` `[●]` (classical; the affine case is a direct computation). The observer is discretely forbidden and continuously forced: this is the categorical–topological side of the seam.

(The full unfolded version of the theorem — with its satellites, its lineage from Lawvere and Hilbert to Spencer-Brown, and a survey of paths — lies beyond the scope of this package.)

Terminal = invariant of `κ` — `[●]`, a theorem. "Observer" is the name of this invariant by the theory's definition; all the additional load ("unfolds the scene," ouroboros dynamics) is interpretation on top of terminality `[◐]`. The geometric identification of the terminal with the point `½` of the continuous side is the same `◐` as from the first rank on (the point `½` lies on `|·|∞`); the categorical skeleton of the ouroboros is built, its geometric-dynamic flesh remains a front `[◐/○]`.

A related analogy from set theory: expelling a self-complementary invariant from the carrier is the same move used to deal with self-membership. The observer relates to the tower as Russell's class relates to the universe of sets: a self-referential complement that has no place among the elements, yet which the construction is forced to name `[◐]` (`code_core/verify_zfc_in_dot.py`).

### 5.3. The initial object and Möbius: the second end

The terminal is the upper end; the category has a lower one too.

> **Statement (initial object).** The empty set `∅` with the empty involution is an initial object: from it a unique (empty) morphism leads into every carrier `[●]` (`code_core/verify_initial_mobius.py`).

The seed (`∅`, the beginning from which everything issues) and the observer (`•`, the terminal, to which everything converges) are the two ends of one category, and the tower is stretched between them. The trace of this duality in the arithmetic of the construction is the **Möbius function**: the reduced acyclicity of the complex (ch. VI) is the alternating-sign identity `Σ_{S}(−1)^{|S|}=[n=0]`, i.e. the inversion `μ*ζ=δ` on the lattice — in numbers, `1/ζ(s)=Σμ(n)n^{-s}` `[●]` (`code_core/verify_initial_mobius.py`; the assembly with number theory — document 03). The seed-`∅` gives the unit of convolution, and Möbius is the operator of return to it.

The duality of ends also carries the theory's **method**. Each step of the generative construction takes the minimal object of the class specified by that step's conditions — in strict form, initial (free): unique up to a unique isomorphism, given by a formula, and requiring no axiom of choice (the finite minimum is a ZF theorem; the minimum everywhere is well-ordering, equivalent to AC by Zermelo). The principle "the theory's primitive = its initial object" is a classical line: Dedekind (recursion from the minimality of a chain, 1888), Birkhoff (free algebras, 1935), Gödel (the minimal inner model `L`, 1938), Lawvere (the natural-numbers object, 1963), Lambek (the initial algebra of a functor as its fixed point, 1968), the initial semantics of the Goguen–ADJ school (syntax as the initial algebra of a signature, 1977). The theory's method lives at the initial end of the category, the subject of its main theorem at the terminal end: the generative construction and the non-includable observer are a dual pair `[●]`; reading arrow-reversal as yet another face of `κ` is `[◐]`.

### Summary

The tower is stretched between two ends: the initial object `∅` (the seed) and the terminal `•` (the invariant of `κ`, the observer), with the monad `T=ℤ/2×(−)` of the free–forgetful adjunction, whose algebras are precisely the carriers `[●]`. From every carrier there is a unique morphism to the terminal; in the reverse direction there are none (`\mathrm{Hom}(•,Q_n)=∅`) `[●]`. Non-inclusion is constitutive: in the subcategory of scenes there is no terminal, and adjoining a fixed point destroys the scene `[●]`; on the continuous body, by contrast, a fixed point is forced (Brouwer/Smith) and unique — `σ½` `[●]`. Method is dual to subject: the primitive is the initial, the observer is the terminal `[●]`. Möbius is the arithmetic trace of the beginning (`μ*ζ=δ`) `[●]`. The name "observer" and the full ouroboros load are interpretation on top of the theorem `[◐]`; ouroboros dynamics is a front `[○]`, with a hypothesis in checkable form: self-closure is yet another form of the wall (document 01, chapter IX §9.3). A second front of the same kind `[○]` is **the distinction of distinguishers**: the terminal is one, yet perspectives are many; how the many points of view arise from and agree with a single terminal (sections of the quotient?) is open (document 01, chapter X §10.6).


---

## Chapter VI. The scene: grading, complex, motion, and balance

The scene of each rank carries two structures — the `sl₂` weight grading and the chain complex with its Hodge star — and both are drawn into one center by one operator `κ`. Below, both structures are built, their literal coincidence at the level of matrices, the scene's own motion (holonomy and the Singer screw), and its own conservation law — the discrete form of `∏=1`.

### 6.1. The `sl₂` weight grading

On each `Q_n` a triple of Stanley operators acts: `H` (weight `2k−n`, where `k` is the number of ones), `e` (raising: add a coordinate), `f` (lowering: remove one). The relations

$$[e,f]=H,\qquad [H,e]=2e,\qquad [H,f]=-2f$$

hold **identically at every rank** `n=1…5` `[●]` (`code_core/verify_functor_fronts.py`, front 2; `code_core/verify_functor_layers.py`). Uniformity, which had remained open in document 01 for `n>3`, is established: the base `sl₂`-triple is a single one for the whole tower. Weights are distributed unimodally with multiplicities `C(n,k)` and peak at the middle `H=0` — the stratum of the observer.

The representation is given by an **explicit functor**: `V_n=(V_1)^{⊗n}` — the tensor power of the two-dimensional representation, action by the Leibniz rule `e_n=e_1⊗I+I⊗e_{n-1}`, lift = tensor multiplication by `V_1` `[●]` (`code_core/verify_functor_coherence.py §2`). The grading of the scene is the image of the functor of ranks in representations of `sl₂`. The complement here is the Weyl involution: `κeκ=f`, `κHκ=−H` `[●]`.

What remains open is: whether the specific "octahedral algebra of rank 3," if it is richer than the base `sl₂`, is a separate question `[○]` (document 01, chapter III).

> **Remark (the scene as the terminal of the fiber of realizations).** The edge rule of the active scene — "all poles are adjacent except the antipode" — is forced by terminality in the fiber: among the `κ`-invariant antipode-free graphs on `2n` poles, the orthoplex `K_{n×2}` is maximal — the **terminal realization of the fixed scene**, into which every other embeds (every non-edge of it is an antipodal pair) `[●]`. The forgetful functor `U:\mathrm{Real}→\mathrm{Scene}` (forgetting edges) has a left adjoint `D⊣U` (the empty graph — the free realization); it has no right adjoint (cofree object) — the orthoplex does not serve as a cofree object, the Hom-bijection breaks `[●]`. This is the categorical form of "the figure of the scene is forced as minimal" (document 03, §4.3). The full law, the Galois realization of the icosahedron, and the verifier: the note `Bridges/opposition_bridge.md`.

### 6.2. The chain complex and the Hodge star

The same lattice carries a second structure — a chain complex over `𝔽₂`: layers by weight `C_k` of dimension `C(n,k)`, boundary `∂` (remove a coordinate), coboundary `δ` (add one):

$$\partial^2=0,\qquad \delta^2=0 \qquad [●]$$

— every pair of coordinates is removed via two paths, which over `𝔽₂` is zero (`code_core/verify_functor_layers.py`). The complex is reduced-acyclic: `Σ_k(−1)^k C(n,k)=0`. The complement in this dictionary is the **Hodge star**, `κ∂=δκ`: it sends weight `k` to `n−k` and exchanges boundary with coboundary, making the figure self-dual. The lift is a **suspension**: `∂_{n+1}` is the cone over `∂_n` `[●]`.

### 6.3. One operator, two fields

The coincidence of the structures is literal, with one qualification that must be stated. The raising operator `e` and the coboundary `δ` are **one integer 0/1-matrix**; the lowering operator `f` and the boundary `∂` are one; `κ` is one permutation matrix `[●]` (`code_core/verify_functor_coherence.py §3`). Hence the Weyl swap `κeκ=f` and the Hodge star `κ∂=δκ` are one formula in two dictionaries, and the coherence of the three roles of `κ` is an identity.

The qualification is the **field of reading**: the `sl₂` relations (`[e,f]=H`, eigenvalues `2k−n`) are read over `ℚ` — over `𝔽₂` they degenerate (`2e=0`); the identities of the complex (`∂²=0`), by contrast, are read over `𝔽₂` — over `ℤ` without signs `∂²=2(\cdot)≠0`. The matrices are the same, the fields differ: the grading is characteristic zero, the complex is characteristic two. This is the exact form of the fact that one discrete figure carries two algebras.

### 6.4. Motion: holonomy and the screw

The scene carries its own rotation. At the third rank the active scene is a six-cycle `C₆`; its shift `T` has order six, and the half-turn coincides with the complement: `T³=κ` `[●]`. The quotient `C₆/κ` is a triangle, and the covering `C₆→C₃` is connected — a nontrivial class in `H¹(S¹;ℤ/2)`, the discrete one-sidedness of a Möbius band `[●]` (`code_core/verify_functor_layers.py`).

On the axes, rotation is canonical for every rank — the Singer cycle on `PG(n−2,2)` of order `2^{n-1}−1`; the orders of adjacent ranks are coprime (`2^n−1=2(2^{n-1}−1)+1`), and hence adding the rotation to the lift produces a **screw**, non-closing at any floor `[●]`.

### 6.5. The conservation law of the construction: the discrete `∏=1`

The pieces above combine into the construction's own conservation law — without importing anything from outside.

> **Statement (balance).** The construction carries two `κ`-mirror flows: `δ` (coboundary, growth outward) and `∂` (boundary, descent inward), conjugate via the Hodge star `κ∂=δκ`. Their balance is the reduced Euler characteristic
> $$\sum_k (-1)^k \binom{n}{k} = 0$$
> — the additive form of `∏=1`: what grows outward is exactly compensated by what comes in; two-sided about `σ½` (the spectrum is symmetric under `k↔n−k`) `[●]` (`code_core/verify_machine_conservation.py`).

Identifying this additive balance with the multiplicative product formula `∏_v|x|_v=1` over the places of `ℚ` is a recognition of one shape, "the full set → neutral" `[◐]`; this part of the construction itself is assembled from what is already proved, without a new input. Thus "the seam = `∏=1`" holds as a property of the construction itself, independently of any import from number theory (the full stitching of the sides — document 03).

### Summary

The scene carries the `sl₂` grading (uniform across ranks, given by the functor `V_1^{⊗n}`, over `ℚ`) and the chain complex (`∂²=0`, Hodge `κ∂=δκ`, suspension, over `𝔽₂`) via **the same matrices**, read over two fields; `κ` unites the Weyl involution and the Hodge star in one identity `[●]`. The scene moves (holonomy `T³=κ` with the Möbius band; the Singer screw without closure) and balances (`Σ(−1)^kC(n,k)=0` — the discrete `∏=1`) `[●]`.


---

## Chapter VII. The continuum side as a spectral limit

The continuous side — where the invariant-observer `½` lies — enters the construction by derivation: as a **limit of the spectrum**. Here are established the limit itself (a Gaussian measure), the derived metric (the Connes distance = Hamming), and the exact boundary of the derivation — a single equation `[κ,Δ]=0`. The chapter closes with a look from the side of set theory: the discrete tower is `V_ω`, and the Axiom of Infinity is the seam itself.

### 7.1. The Laplacian and its spectrum

On the chain complex (ch. VI) a Laplacian is defined, `Δ_n=∂δ+δ∂`; on the scalar layer it equals the hypercube Laplacian `Δ_n=nI−A` (`A` — adjacency) with spectrum `{2k: k=0…n}` and multiplicities `C(n,k)`; the heat trace factorizes:

$$\mathrm{Tr}\,e^{-t\Delta_n}=(1+e^{-2t})^n. \qquad [●]$$

(`code_core/verify_continuum_limit.py`.)

### 7.2. The limit — a Gaussian measure

> **Theorem (the limit).** The centered and normalized spectrum (weight `k` with weights `C(n,k)/2^n`) converges as `n→∞` to a **Gaussian measure** on the line — by the central limit theorem `[●]` (`code_core/verify_continuum_limit.py`).

The complement `κ` sends the weight layer `k` to `n−k`, i.e. it acts in the centered variable as the involution `λ↦−λ` — the Hodge star of the limit measure; its fixed point is the center, the very `σ½`-invariant. The continuous side **is derived** as a spectral limit measure; this is the exact form of "the continuous completion" of the carrier.

What the limit gives: a measure. What it does not give: Riemannian geometry `(M,g)` — the spectral dimension of the hypercube does not stabilize, the limit is a measure on the line, not a manifold `[●]`. Metric, dimension, signature are a structure of a different kind (see §7.4 and ch. IX).

### 7.3. The metric is derived: the Connes distance

The discrete side does have a metric, and it is not postulated.

> **Statement (Connes = Hamming).** The Connes spectral distance `d(x,y)=\sup\{|f(x)−f(y)|:\ \mathrm{Lip}(f)\le 1\}` on the carrier coincides with the geodesic — Hamming — distance `[●]` (`code_core/verify_connes_metric.py`).

The metric is derived from the same spectral triple — and it is **Euclidean** (positive).

### 7.4. The boundary in a single equation: `[κ,Δ]=0`

> **Fact (decisive).** The complement commutes with the Laplacian: `[κ,Δ]=0` — because `κ` is a graph automorphism of the carrier and the Hodge star of the complex `[●]` (`code_core/verify_lorentz_signature.py`).

From this one fact — three boundaries at once (`code_core/verify_dynamics_spectral.py`, `code_core/verify_lorentz_signature.py`):

- **signature:** the `κ`-splitting of the spectrum into `±1`-subspaces gives equal dimensions `\dim H_+=\dim H_-=2^{n-1}` — a neutral signature `(k,k)`, with no asymmetry of "a single time"; a Lorentzian `(1,n−1)` signature does not come out of `κ`;
- **dynamics:** all `κ`-`Δ`-constructs vanish — `κΔκ−Δ=0`, `[κ,Δ]=0`, the curvature term `\mathrm{Tr}(κΔ)=0`; the action reduces to `\mathrm{Tr}(Δ)` with no curvature term;
- **evolution:** an operator generating dynamics would have to fail to preserve the Laplacian; none among the combinatorics of `κ` does.

Energy (`Δ`), causal order (`⊆`, ch. VIII), the arrow (comonad, ch. VIII), and a Euclidean metric are present in the construction; Lorentzian signature, curvature, and dynamical evolution are **input**. The boundary is named by one proved equality.

### 7.5. Set theory: `V_ω` and the Infinity-seam

The same boundary is visible from the side of foundations. The entire discrete carrier `⋃Q_n`, read under the Ackermann encoding (`a∈b ⟺` bit `a` of the number `b`), is exactly the hereditarily finite sets `V_ω`: all axioms of ZF except Infinity hold, and choice on the finite is a theorem `[●]` (`code_core/verify_zfc_in_dot.py`). The Axiom of Infinity — the completed union as a single object — is precisely the passage to the continuous side; as shown above, it yields a **measure**, not a cumulative hierarchy `V_{ω+}` `[◐]` — a seam.

### Summary

The continuous side is derived: the spectral limit of the Laplacian is a Gaussian measure with Hodge star `λ↦−λ` and observer-center `[●]`; the metric — the Connes distance — coincides with the Hamming distance and is Euclidean `[●]`. The boundary of the derivation is one equality `[κ,Δ]=0`: the signature is balanced `(k,k)`, `κ`-curvature and `κ`-dynamics vanish — Lorentzian structure and evolution are input `[●]`. The discrete tower is `V_ω`; Infinity is a seam to the measure `[◐]`.


---

## Chapter VIII. Time as traversal, not coordinate

The construction is static: the complement commutes with the Laplacian, and no operator of it generates evolution — as in the constraint equation `ĤΨ=0`, where the whole does not evolve. Time appears in it as a **traversal**: the order of reading the structure. Time is resolved into three layers — linear (a flag), cyclic (a clock), and an arrow (comonad) — together with the causal order, in which the observer turns out to be "now."

### 8.1. Statics of the whole

The global state of the tower is static: `[κ,Δ]=0` (ch. VII), there is no evolving operator in the combinatorics of the complement `[●]` (`code_core/verify_time_emergence.py`). This is the discrete analogue of the Wheeler–DeWitt situation: the whole does not move. Time, if it is to exist, is a property of reading.

### 8.2. Linear time: a flag

Linear time is a **maximal chain** of the lattice: a flag `∅⊂\{a\}⊂\{a,b\}⊂…⊂[n]`. There are `n!` such chains, each step is one `δ`-event, the addition of a coordinate `[●]`. History is a sequence of distinctions made.

An event here is a **transition**: the directed edge `x→x∪\{i\}`, a single act of distinction. States (vertices) are fixed; the event is the morphism.

### 8.3. Cyclic time: a clock

Cyclic time is the rotation `T` of the scene (ch. VI: `T³=κ` at the third rank). On splitting the carrier into a **clock** and a **world** (the Page–Wootters mechanism), the conditional state of the world evolves with the reading of the clock, while the whole remains static `[●]` (`code_core/verify_time_emergence.py`). Neither the flag nor the rotation enters the Laplacian: both are traversals.

### 8.4. The arrow: the comonad of observation

The complement — reversible (`κ²=id`) and static (`[κ,Δ]=0`) — cannot be a source of irreversibility; irreversibility comes from the **comonad of observation**:

$$G=\Lambda_L\circ\pi \qquad (\text{forget a coordinate and re-embed it}).$$

> **Statement (the arrow).** `G` is idempotent (`G²=G`: coarsening cannot be undone — information is lost) and does not commute with the Laplacian (`[G,Δ]\neq 0`) `[●]` (`code_core/verify_time_emergence.py`; `code_core/verify_growth_directions.py`).

This is exactly the operator that the boundary of chapter VII demanded: one that **does not preserve** the Laplacian, irreversible — giving a direction. And it is internal: `G` is part of the adjoint triple already at hand (`Λ_L∘π` is the comonad of the adjunction `Λ_L⊣π`). Of the three candidates for the source of direction (sheaves, braiding, comonad), the first two are program and input `[○]`, the comonad is established `[●]` (`code_core/verify_growth_directions.py`).

### 8.5. Causal order: cones and "now"

Causality is already given by the inclusion `⊆`: the carrier is a causal set, where the future and past cones of an event are `\{y⊇x\}` and `\{z⊆x\}`, time is chains (timelike), space is antichains (spacelike) `[●]` (`code_core/verify_causal_structure.py`).

> **Fact (Sperner).** The largest antichain of the lattice is the middle layer: the observer `σ½` is the **maximal slice of simultaneity**, "now" `[●]`.

The arrow-comonad is consistent with the order (coarsening moves downward along `⊆`). What the order does not give is a fixed dimension: as a causal set, the lattice canonically carries `d=1` (a chain — pure time) and `d=∞` (the whole lattice); `3+1` is reachable by choosing a four-dimensional thinning, but this is a choice of embedding, an input `[●` reachability / `○` not derived`]` (`code_core/verify_dimension_choice.py`).

### Summary

Time in the construction is a traversal: linear — a flag of `n!` chains of `δ`-events; cyclic — a clock-rotation (Page–Wootters, the whole static); the arrow — the comonad of observation `G=Λ_L∘π` (`G²=G`, `[G,Δ]≠0`) — an irreversible operator from the adjoint triple itself `[●]`. Causal order is the inclusion `⊆` (cones; "now" = the middle layer by Sperner = `σ½`) `[●]`; dimension and signature are input `[○]`.


---

## Chapter IX. The boundary: input and the external bridge

The categorical construction is complete in itself — and precisely for that reason it must name where it ends. This chapter gathers the boundary in full: what the construction hands to **input** (and why — in a single equation), what its sole **external bridge** looks like (a functor into free spins), and what happens at the first step beyond the bridge (mass: the form is forced, the value is free). This is the wall of the series — named exactly, with its mechanism.

### 9.1. Input, reduced to one equality

Everything separating the geometry of spacetime from mere order reduces to the fact `[κ,Δ]=0` (ch. VII):

| required | what the construction gives | status |
|---|---|---|
| Lorentzian signature `(1,n−1)` | `κ`-splitting is balanced `(k,k)` | input `[○]` |
| curvature / action term | `\mathrm{Tr}(κΔ)=0`, action = `\mathrm{Tr}(Δ)` | input `[○]` |
| dynamical evolution | all `κ`-`Δ`-constructs `=0`; an operator not preserving `Δ` is needed | input `[○]` (internal candidate for the arrow — the comonad, ch. VIII) |
| dimension `3+1` | canonically `d=1` and `d=∞`; `3+1` is a choice of thinning | input `[○]` |
| manifold `(M,g)` | the limit is a measure, not a manifold | input `[○]` |

The construction has: energy (`Δ`), causal order (`⊆`), the arrow (`G`), a Euclidean metric (Connes = Hamming), balance (`Σ(−1)^kC(n,k)=0`). The boundary is a consequence of one proved equality `[●]`.

### 9.2. The external bridge: a functor into free spins

The one verified bridge outward is the functor `F: Q_n →` spin systems:

$$A(Q_n) \;\equiv\; \sum_i \sigma_x^{(i)} \qquad (\text{a literal equality of operators}),$$

lift ↦ add a spin, `κ` ↦ global flip, `σ½` ↦ the massless center; functoriality is checked on four operations `[●]` (`code_core/verify_functor_spin.py`, 45 checks). But the image is a **free** system: there is no interaction within the cube itself. The bridge is built at one point; beyond it lies a front `[◐→○]`.

### 9.3. The first step beyond the bridge: mass — the form is forced, the value is free

What happens if the bridge is given a minimal input — weights `w_i`? Investigated without fitting (`code_core/verify_mass_gap_input.py`):

- **the cube without weights is massless** `[●]`: spectrum `{n−2k}`, the center `λ=0` is degenerate (`C(n,n/2)`), no gap — vertex-transitivity;
- **weights open a gap but not its value** `[●]`: incommensurate `w_i` open a gap `Δ_{\text{gap}}=\min|\sum\pm w_i|>0`, yet `Δ(2w)=2Δ(w)` — the scale is stretchable, the value of the mass is not forced;
- **there is no distinguished set of weights** `[●]`: the `S_n`-symmetry of the cube makes all permutations of `w` equivalent — the value is free, an input;
- **the form is forced** `[●]`: for any `w`, the spectrum is symmetric `±λ` (particle–hole symmetry from `\{A_w,Z\}=0`), and an actual gap requires **interaction** (a `σ_z σ_z`-term), which the cube does not have.

The upshot of this step: structure forces the **form** of the spectrum (its symmetry, who can interact with whom), but not the **values** (weights, strengths). This is the same wall of values found throughout the corpus — seen here from the functorial branch, by its own means.

### 9.4. Locating the question of the morphism

The objection "there is no morphism between the discrete side and physics — only coincidences of values" receives, after this series, a precise location:

- **the core** — the growth of ranks — is functorial and proved (ch. I–VI): the adjoint triple, the isomorphism of the growth law, the naturality of `κ`, the monad with its two ends, the functor of representations; with no excursion into physics and no wall of values;
- the **external bridge** is real, but at one point only (free spins), and runs into weights-as-input `[◐→○]`;
- the objection, accordingly, pertains to **application**; the construction remains outside its reach: the internal coherence of the theory is established independently of whether it reaches all the way to physics.

### Summary

The boundary of the construction is named with its mechanism: Lorentzian signature, curvature, evolution, `3+1`, `(M,g)` are input, and all of these are consequences of one equality `[κ,Δ]=0` `[●]`. The external bridge — a functor into free spins — is exact at one point `[●]`, beyond it lies a front `[◐→○]`; the first step past it shows the wall of values in pure form: the form is forced, the value is free `[●]`.


---

## Epilogue. The construction as a whole and its two models

The series has passed through the construction layer by layer; what remains is to see it in one glance and return it to its place among the models.

### The construction in one paragraph

The operation of distinction — a fixed-point-free involution — generates the carrier as a **free object** (ch. I). Growth is an **adjoint triple** `Λ_L⊣π⊣Λ_R`, monoidal (`Q_{m+n}=Q_m□Q_n`, ch. II). The growth law is an **isomorphism of projective spaces** `PG(n−1,2)≅U_{n+1}/κ`: the content of a rank becomes the axes of the next (ch. III). The complement is **one operator** in three roles: a natural isomorphism `Λ_L⇒Λ_R` (in sets), De Morgan duality, and — one matrix — the Hodge star = the Weyl involution (ch. IV, VI). The tower is stretched between the **beginning** `∅` (the seed; its arithmetic trace is Möbius `μ*ζ=δ`) and the **terminal** `•` (the invariant of `κ`; from every carrier a unique morphism into it, and none in reverse: `\mathrm{Hom}(•,Q_n)=∅`); the carriers are algebras of the monad `ℤ/2×(−)` (ch. V). The scene carries the `sl₂` grading (functor `V_1^{⊗n}`, over `ℚ`) and the complex (`∂²=0`, over `𝔽₂`) via the same matrices; it moves by the holonomy `T³=κ` and the Singer screw; it balances by the discrete `∏=1` (ch. VI). The continuous side is a **spectral limit**: a Gaussian measure, the Connes metric = Hamming (ch. VII). Time is a **traversal**: flag, clock, the arrow-comonad `G` (`[G,Δ]≠0`), the causal order `⊆` with "now" = `σ½` by Sperner (ch. VIII). The boundary is one equality `[κ,Δ]=0`: signature, curvature, evolution, dimension, `(M,g)` are input; the external bridge is free spins, at one point; mass — the form is forced, the value is free (ch. IX).

The metric realization of these two ends — the seed as the source of an address tree, the observer as the apex of a cone — is the bridge note `Bridges/radial_bridge.md`.

### Two models, one functor

This series is defined on **bits** `Q_n=𝔽₂ⁿ` — the side of structure. The second, independent model is **numbers** `D(N)` (document 03): there the same morphisms (`κ`=complement `d↦N/d`, `H`=number of primes, lift=multiplication by a prime, `π`=remove a factor) coincide under the functor `Λ:S↦∏p`, and beyond that it contains something invisible to bits — height `^` (multiplicity `v_p`) and the grading of the arrow `P`. Numbers are the **tuning fork** (an independent model against which membership of a property in the construction is checked): what holds in both models belongs to the functor of the construction; what holds in only one is a shell above it. The corresponding expositions are document 01 (chapter VIII: the same construction in overview, within the general series) and document 03 (chapter VII: the functorial layer of numbers).

### A closing register

- `[●]` — the free carrier (`|\mathrm{Hom}|=|Y|^{2^{n-1}}`); the triple `Λ_L⊣π⊣Λ_R`; monoidality `□`; the isomorphism `PG(n−1,2)≅U_{n+1}/κ` (linear, with lines); `κ∘Λ_L=Λ_R∘κ`; De Morgan; one matrix (Hodge=Weyl); the monad `ℤ/2×(−)`, `EM`=carriers, terminal and initial object, `\mathrm{Hom}(•,Q_n)=∅`; Möbius `μ*ζ=δ`; `sl₂` uniform (functor `V_1^{⊗n}`); `∂²=0`, suspension; `T³=κ`, Möbius covering, Singer screw; `Σ(−1)^kC(n,k)=0`; spectral limit=Gaussian; Connes=Hamming; `[κ,Δ]=0` and its consequences; `V_ω`=discrete, finite choice=theorem; flag/clock/arrow-comonad; Sperner-"now"; spin bridge (one point); mass: form.
- `[◐]` — the name "observer" and the ouroboros load beyond terminality; the geometric `½` on the underside; the naturality of the `PG`-isomorphisms with respect to the lift; additive balance = multiplicative `∏=1` (one shape); Infinity=seam to the measure; Russell's class.
- `[○]` — a 2-category / Grothendieck construction over ranks; ouroboros dynamics (hypothesis: self-closure is yet another form of the wall); the distinction of distinguishers (the multiplicity of perspectives under a single terminal); the specific rank-3 algebra; Lorentzian signature, curvature, evolution, `3+1`, `(M,g)` — input; the values of weights/masses.

The construction is built, its boundary named with its mechanism: what is proved is proved enumerably, the inputs are named. The functorial coherence of the theory is internal, and it is established; external bridges are separate work with their own wall. The question of the morphism is located: it pertains to the bridge, the core stands.
