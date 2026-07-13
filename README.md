# DOT: Distinction Observable Theory
 
[Русская версия](ru/README_RU.md)
 
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20257220.svg)](https://doi.org/10.5281/zenodo.20257220)

## About the theory

Distinction Observable Theory is a mathematically rigorous conceptual apparatus oriented toward the study of the fundamental nature of stable boundaries and distinctions. The apparatus distances itself from classical ontological questions ("what exists in the world?") and from the traditional epistemological problems of the cognitive sciences ("how does an agent perceive reality?"). Instead, the theory focuses on a maximally compressed structural question, cleansed of empirical noise: **"How exactly is a stable distinction structured?"**

If in some medium, physical or conceptual, a boundary is drawn between two states, and this boundary is successfully held, preventing the collapse of the system into an indistinguishable unity, then DOT investigates the minimal structural configuration that is generated with mathematical inevitability by the very fact of this holding. In other words, the theory studies not what is distinguished, but the anatomy of the act of distinction itself.

Traditional academic mathematics and theoretical physics gravitate toward an analytic approach: some object is posited — a set, a topological space, an algebraic group, a physical field — from which invariants, symmetries, and conservation laws are then analytically extracted. DOT proposes a methodological shift to a generative stance. Here the object is not the starting point. The entire apparatus of the theory unfolds from a single primary primitive — an act that returns to itself in one step:

```
ι² = id
```

(an involution: the identity transformation under twofold application). From this singular origin, the theory — step by step, obeying a strict internal logic — generates forced structures. In this paradigm the object — a geometric figure, an algebraic law, a numerical regularity — becomes not an initial given but the inevitable mathematical output of the generative process.

## The principle of forcedness and the statuses of assertions

The theory is governed by a rigid methodological principle of **forcedness**. At every stage of the system's unfolding, arbitrary construction is not permitted: each subsequent step is strictly forced — given the stated requirement, only one structure can arise, mathematically without alternative.

This is reflected in explicit statuses of assertions, marking the entire corpus across three levels:

- **Forced `[●]`** — conclusions that are mathematically inevitable: proven, confirmed by a verifier, or classical facts.
- **Reading `[◐]`** — a conceptual lens through which known mathematical objects fold into a single connected figure; the premise of each such recognition is named explicitly.
- **Open `[○]`** — the zone of unsolved conjectures and open questions, where the theory encounters the limits of its current apparatus.

## The second side of distinction

To distinguish means to draw a boundary, to indicate that one state is not identical to another. In classical mathematics, two sides are present in practically all fundamental operations. The first is **what** is distinguished: objects, points of space, elements of sets. The second is **relative to what** the distinction is drawn.

Classical science concentrates its attention on the first side: the given object is classified, measured, and observable quantities are extracted from it. The second side is almost always invisible, taken to be a trivial given. Yet any equivalence class exists precisely insofar as there exists a feature that remains unchanged along that class; a quotient set is well-defined only because the gluing procedure is consistent with this feature. "That relative to which one distinguishes" is the **invariant of the relating operation** — the structural anchor of consistency. Classical disciplines leave this invariant in the shadows; DOT makes the minimal structure of this anchor its direct and sole subject.

This invariant the theory calls the **observer** — and it uses the word strictly in a structural sense, with no psychological load: the observer is the center of symmetry relative to which states are related — a relation, not an element. It is not among the distinguished states themselves; below this is seen literally.

## From act to space

Space in the theory grows out of distinctions themselves. One distinction has two outcomes — "this" side of the boundary and "that" one. Adding a second distinction, independent of the first, doubles the set of possibilities: four combinations of outcomes — a square. Adding a third — eight combinations — a cube. Each independent distinction adds an autonomous **axis**; a **state** is one combination of the outcomes of all the distinctions drawn, a vertex of the cube; the totality of all states is the **carrier** of distinction, the Boolean cube `Q_n = 𝔽₂ⁿ` of `2ⁿ` vertices. The carrier grows out of the acts of distinction as their cumulative trace. The number of distinctions drawn — the number of axes of the cube — is called the **rank**.

The relating operation on the carrier is uniquely determined: the sole transformation that relates each side to its opposite and preserves the equal standing of all axes is the bitwise **complement** `κ(x) = x + 1ⁿ`, the flip of all outcomes at once. Two states stand apart here: `0ⁿ` and `1ⁿ` — the points where all distinctions are taken or none at all; these are the **poles**. Their removal leaves the states with mixed content — the **active scene** `U_n`: the field of distinction proper.

Growth is embedded in the subject itself: distinctions are added — the carrier grows. The addition of one axis, the transition `Q_n → Q_{n+1}`, is called a **lift**; the sequence of carriers connected by lifts forms the **tower of ranks**. Growth has an exact law: configurations distinguishable at rank `n` become the axes of the scene of rank `n+1` — the content of one floor turns into the directions of the next. Formally, the quotient of the active scene by the complement is the projective space over `𝔽₂`:

```
U_n / κ ≅ PG(n−2, 2)      [●]
```

— the scene of rank 3 gives the projective line, of rank 4 the Fano plane, of rank 5 `PG(3,2)`. The categorical form of this law (the lift as an adjoint triple of functors, the observer as the terminal object) is proven in document 02.

In these three paragraphs the generative thesis of the theory is at work, and that is their point. From the single act `ι² = id` there are successively determined the space (carrier), the operation (complement), the center (observer), and growth (lift) — without a single additional postulate: each object appeared because the previous one left it no alternative. And the law of growth closes the process upon itself: what is distinguished on one floor becomes the axes of the next — the structure generates its own directions of further distinction. The tower of ranks is precisely the main object of the theory: a self-generating space of distinction, each floor of which is forced by the previous one.

## Minimal example: rank 3

The smallest substantive case of the theory is surveyable in full — and it also shows what all this is for.

Take three distinctions: eight states `𝔽₂³`. The poles `000` and `111` are removed; there remains the active scene `U₃` of six states. The complement `κ(x) = x + 111` splits the six into three pairs of opposites: `{001,110}, {010,101}, {100,011}`.

The distance between states (the number of differing bits) gives exactly three relations, and each is a known graph: `R₁` (one bit) — the hexagonal cycle `C₆`; `R₂` (two bits) — two triangles `K₃ ⊔ K₃`; `R₃` (all three) — three pairs `3K₂`, the axes of opposition. Together `R₁ ∪ R₂ ∪ R₃` give the **octahedron** `K_{2,2,2}`: six vertices, three axes through a common center.

<p align="center">
  <a href="assets/figures/555.png">
    <img src="assets/figures/555.png" width="600" alt="Rank-3 scene: the octahedron K_{2,2,2} — bits, color wheel, and the divisors of the number 30 on the same vertices">
  </a>
</p>

The figure shows one and the same scene, read on three different materials.

**Bits.** Six three-bit states around a circle; the edges of the hexagon are `R₁` (one step), the diagonals through the center are `R₃ = κ`. The observer is literally visible: the center of the octahedron — the point relative to which all three axes are symmetric — **is absent among the six vertices**. The invariant of relation exists, but is not a state.

**Numbers.** The proper divisors of the number `30 = 2·3·5` — `{2,3,5,6,10,15}` — are the same six points (in the figure, the numbers beside the vertices); the complement `d ↦ 30/d` gives the same three axial pairs (`2↔15, 3↔10, 5↔6`); the fixed point of the complement `√30 ≈ 5.48` is not a divisor — the observer is again outside the carrier. `[●]` — for squarefree `N` the divisor lattice is isomorphic to the Boolean cube.

**Color.** Three channels `{R, G, B}` are three axes; six vertices — the color wheel (in the figure, the coloring of the vertices). A step around the circle is the change of one channel (`C₆`, the wheel of hues); the complementary color is the flip of all channels (`R↔C, G↔M, B↔Y` — the same `κ`); the gray point is the center, not belonging to the circle. By the same framework the auditory scene is read as well — the status of both readings is `[◐]`: the recognition of structure in perceptual material, its premises and measure are analyzed in document 01 (chapter III); an expanded document on color and sound is being prepared for addition to the package.

**Conclusion of the example.** Bits, divisors, and colors here are **one object**, and the figure is its portrait. What the three realizations share is the type of connection itself: six elements joined by the same three relations (a step — the change of one component, the triadic partition, opposition — the flip of all components), with one common absent center. Between any two realizations there exists a one-to-one correspondence preserving all three relations — an isomorphism; isomorphic structures are regarded by mathematics as one structure on different material. One source — the act of distinction, taken three times — and three of its independent projections. The same framework is found beyond these three examples as well: in the note organization of music, in the motivic structure of Sanskrit — documents on these realizations are being prepared for addition to the package. Rank 3 is the first place where distinction holds in three irreducible ways at once (opposition, triadic partition, cycle) while remaining one connected figure; therefore the example is minimal and therefore the corpus begins with it.

## Composition of the package

Four documents. Each is self-contained; the terminology and status discipline are unified.

### [01 · Exposition: the theory in full, by ranks](01_Exposition.md)

The main entry into the corpus and the most complete document of the package. The genre is a **demonstrative narrative**: prose leads, the mathematics appears at the moment of necessity, each load-bearing step is marked with a status `[●]/[◐]/[○]`; concepts are introduced where they first come into play, no preparation required. The exposition proceeds by ranks, and on each the same cycle: carrier → operation and scene → structure → observer → realizations. Inside: the forcing of the minimal operation of distinction and its invariant (chapter 0); the first distinction, the two sides of the carrier `|·|₂/|·|∞` and the imaginary unit `i = √κ` (chapters I–II); the rank-3 octahedron with realizations in logic and color (chapter III); the rank-4 break — the inner layer, the body, the atom (chapter IV); the higher ranks and the closure of growth at rank 8 — the exhaustion of division algebras, `E₈` (chapters V–VI); the reverse side — the continuous side and its splitting (chapter VII); the functor of growth (chapter VIII); the inversion — the whole scene as the unfolding of the observer (chapter IX); the boundary — the two registers of the wall: the forced form and the free values (chapter X).

Verifiers: [`code_exposition/`](code_exposition/).

### [02 · Categorical core: construction and proofs](02_Categorical_Core.md)

The demonstrative layer of the package — for the mathematician reader. The genre is a **compressed mathematical text**: each step is a theorem, an identity, or a reference to a verifier; the categorical language is introduced at the point of use. The result is one: the tower of carriers is a categorical construction. Inside: the carrier — the free object of the operation (chapter I); the lift — the adjoint triple `Λ_L ⊣ π ⊣ Λ_R`, monoidality (chapter II); the law of growth — the isomorphism of projective spaces (chapter III); `κ` — one operator in three roles: a natural transformation, De Morgan duality, the Hodge star (chapter IV); the observer — the terminal object, the seed — the initial one, and between them the monad and the Möbius function (chapter V); the `sl₂` grading and the chain complex by the same matrices (chapter VI); the continuous side — the spectral limit: the Gaussian measure, the Connes metric (chapter VII); time — a traversal, the arrow — a comonad (chapter VIII); the boundary — a single proven equality `[κ,Δ]=0`: the form is derived, the values are input (chapter IX).

Verifiers: [`code_core/`](code_core/) — 18 scripts, 385 checks, all passing.

### [03 · Number model: the same construction on divisors](03_Number_Model.md)

The second, independent realization of the construction — on numbers. The order of presentation is the reverse of the core's — **observation → recognition → naming → proof**: the object is first constructed and shown (graph, color), then recognized in known structures, and only after that proven. Inside: the series and the atom — the prime number as an axis (chapter I); the divisor cube — autonomous pure mathematics, read separately from the whole theory (chapter II); the body `L²` — the unique Hilbert space of the scene (chapter III); the octahedron of the number 30 and the Fano explosion (chapter IV); the entry of the imaginary unit `i = √κ` into the continuum (chapter V); the reverse side — the p-adic valuations, the product formula `∏|x|ᵥ = 1`, the gamma function and Möbius inversion (chapter VI); the functorial layer — the two axes of growth from the operations `+/×/^` with the bridge `exp` (chapter VII); the two lenses, graph and color, and the wall of values, explained by metamerism (chapter VIII). The role of this document in the package is an independent check: what holds in both models belongs to the construction; what holds in only one belongs to the material.

Verifiers: [`code_number_model/`](code_number_model/).

### [04 · Projection: definition and criteria](04_Projection.md)

The methodological layer of the package — the formalization of the status `[◐]`. The genre is a **definition with a run-through**: the projection of the core onto material is specified by five conditions (carrier, intertwining with `κ`, preservation of relations, center outside the image, poles outside the scene), and each instrument of evaluation is given an explicit form. Inside: the two kinds of material and the ceiling of status — mathematical up to `[●]`, empirical up to `[◐]` with a named premise (chapter I); the definition and its run-through on the dictionary bits ↔ divisors of 30 (chapter II); invariants and rigidity — the canonicity of the dictionary `12/720` (chapter III); the tuning fork — the criterion for the equivalence of realizations and for the attribution of properties to the core or the material (chapter IV); the three criteria of rejection — structural, the record guard, the fitting guard — with computable negative controls: the diatonic scale and the consecutive hexad are rejected, the whole-tone hexad passes (chapter V); the degrees of rigor — the scene projection versus the tower projection, a summary table of the package's projections (chapter VI); the boundaries: the category of materials, dynamic materials, the impenetrability of the empirical ceiling `[○]` (chapter VII). The role of the document is to turn bridges from on-the-spot interpretations into a verifiable procedure with both outcomes.

Verifiers: [`code_projection/`](code_projection/) — 19 checks, including negative controls.

### [Bridges](Bridges/)

The fourth layer of the package — **bridges**: documents connecting the core with adjacent structures without incorporating them into the forced tower. Two bridges in the layer.

[The oppositional skeleton → the golden realization → the seam discrete↔continuum](Bridges/opposition_bridge.md): the orthoplex as the terminal realization of the scene, the icosahedron as the Galois half of the six-orthoplex (`ℝ⁶ = V_φ ⊕ V_ψ`), and two transitions into the continuum — the spectral (Gaussian measure) and the projectional (icosahedral quasicrystal), diverging at rank 5. The boundaries of the bridge (the external golden frame, the missing morphism `Q₅ → A₅`) are named explicitly. Verifier: [`Bridges/verify_opposition_bridge.py`](Bridges/verify_opposition_bridge.py) — 35 checks.

[The radial layer → metric and measure around the seam](Bridges/radial_bridge.md): the metric and measure-theoretic anatomy of the radial coordinate missing from document 01 (chapter VII) — the forced norm (`L²`), the decomposition into weight and transverse, the concentration of measure, the conical metric of the zero point, the discrete pair realization as an address tree, dilation as the canonical radial flow, the angular excess at the apex of the cone with the theorem separating the two curvatures (the apical one is forced and incommensurable with `π`; the ray axis `(2,3,p)` of document 01 §7.5 is input). Verifier: [`Bridges/verify_radial_bridge.py`](Bridges/verify_radial_bridge.py) — 45 checks.

The status discipline in both bridges is the same as in the core.

**How to read.** The general entry is document 01. For the mathematician who needs proofs — document 02. For the reader coming from number theory — document 03, beginning with chapter II. For the methodologist — the question "what a projection is and when it is rejected" — document 04.

## Checks

The computable part of the corpus is accompanied by verifiers (Python 3, dependency — NumPy):

```bash
python3 -m pip install -r requirements.txt

# examples: any script can be run separately
python3 code_core/verify_functor_core.py
python3 code_core/verify_continuum_limit.py
python3 code_number_model/verify_divisor_cube_strict.py
python3 code_exposition/verify_carrier_from_operation.py
python3 code_projection/verify_projection_criteria.py
```

Each reference to a verifier in the text of the documents leads to a concrete script; the check confirms the construction and is capable of refuting it, while the proofs remain with the text.

## Support

The project develops as an **independent open research program**, without institutional funding.

Donations are voluntary.

| Currency | Network | Address |
|--------|------|-------|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |

## Licenses

The texts, theory, and documentation are under the [CC BY-NC-SA 4.0](LICENSE-THEORY.md) license, unless otherwise specified in a particular file. The executable code (`code_core/`, `code_exposition/`, `code_number_model/`) is under the [Apache License 2.0](LICENSE).

## Citation

```bibtex
@software{zhuk_2026_dot,
  author    = {Zhuk, Igor M.},
  title     = {DOT: Distinction Observable Theory},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.20257220},
  url       = {https://github.com/Nondual-Observer/DOTheory}
}
```

---

© 2026 Igor M. Zhuk. The theory and documentation are distributed under the licenses specified above.
