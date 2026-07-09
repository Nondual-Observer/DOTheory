# DOT: Distinction Observable Theory

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20257220.svg)](https://doi.org/10.5281/zenodo.20257220)

## About the theory

Distinction Observable Theory is a mathematically rigorous conceptual apparatus oriented toward the study of the fundamental nature of stable boundaries and distinctions. The apparatus distances itself from classical ontological questions ("what exists in the world?") and from the traditional epistemological problems of cognitive science ("how does an agent perceive reality?"). Instead, the theory focuses on a maximally compressed structural question, stripped of empirical noise: **"How exactly is a stable distinction built?"**

If, in some setting — physical or conceptual — a boundary is drawn between two states, and that boundary is successfully held, preventing the system from collapsing into indistinguishable unity — DOT investigates the minimal structural configuration that is generated with mathematical inevitability by the sheer fact of that holding. In other words, the theory studies not what is distinguished, but the anatomy of the act of distinction itself.

Traditional academic mathematics and theoretical physics gravitate toward an analytic approach: an object is posited — a set, a topological space, an algebraic group, a physical field — from which invariants, symmetries, and conservation laws are then analytically extracted. DOT proposes a methodological shift to a generative stance. Here the starting point is not an object. The entire apparatus of the theory unfolds from a single primary primitive — an act that returns to itself in one step:

```
ι² = id
```

(an involution: the identity transformation under two-fold application). From this singular origin the theory, step by step, obeying strict internal logic, generates forced structures. In this paradigm an object — a geometric figure, an algebraic law, a numerical regularity — becomes not a starting given, but an inevitable mathematical output of the generative process.

## The principle of forcedness and the status of statements

The theory is governed by a strict methodological principle of **forcedness**. At every stage of the system's unfolding, arbitrary construction is not permitted: each subsequent step is strictly forced — given the requirement in play, only one structure can arise, with no mathematical alternative.

This is reflected in explicit statement statuses that mark the entire corpus at three levels:

- **Forced `[●]`** — conclusions that are mathematically inevitable: proved, confirmed by a verifier, or classical facts.
- **Reading `[◐]`** — a conceptual lens through which known mathematical objects fold into a single coherent figure; the premise of each such reading is stated explicitly.
- **Open `[○]`** — the zone of unresolved conjectures and open questions, where the theory meets the limits of its current apparatus.

## The second side of distinction

To distinguish means to draw a boundary, to indicate that one state is not identical to another. In classical mathematics, virtually every fundamental operation has two sides. The first is **what** is distinguished: objects, points of a space, elements of sets. The second is **relative to what** the distinction is drawn.

Classical science concentrates attention on the first side: the given object is classified, measured, observables are extracted from it. The second side is almost always invisible, taken as a trivial given. Yet any equivalence class exists precisely insofar as there exists a feature that remains invariant along that class; a quotient set is well defined only because the gluing procedure is consistent with that feature. "That relative to which one distinguishes" is the **invariant of the relating operation** — the structural anchor of consistency. Classical disciplines leave this invariant in the shadows; DOT makes the minimal structure of this anchor its direct and sole subject.

The theory calls this invariant the **observer** — using the word strictly in a structural sense, without psychological weight: the observer is the center of symmetry relative to which states are related — a relation, not an element. Among the distinguished states themselves it is absent; below this is seen literally.

## From the act to the space

Space, in the theory, grows out of the distinctions themselves. One distinction has two outcomes — "this" side of the boundary and "that" one. Adding a second distinction, independent of the first, doubles the set of possibilities: four combinations of outcomes — a square. Adding a third — eight combinations — a cube. Each independent distinction adds an autonomous **axis**; a **state** is one combination of outcomes of all distinctions made, a vertex of the cube; the totality of all states is the **carrier** of the distinction, the Boolean cube `Q_n = 𝔽₂ⁿ` of `2ⁿ` vertices. The carrier grows out of acts of distinction as their cumulative trace. The number of distinctions made — the number of axes of the cube — is called the **rank**.

The relating operation on the carrier is uniquely defined: the only transformation that relates each side to its opposite while preserving the equal standing of all axes is the bitwise **complement** `κ(x) = x + 1ⁿ`, a flip of all outcomes at once. Two states stand apart here: `0ⁿ` and `1ⁿ` — the points where either all distinctions or none have been made; these are the **poles**. Removing them leaves the states of mixed content — the **active scene** `U_n`: the field of distinction proper.

Growth is built into the subject itself: distinctions are added — the carrier grows. Adding one axis, the transition `Q_n → Q_{n+1}`, is called a **lift**; the sequence of carriers connected by lifts forms the **tower of ranks**. Growth has an exact law: configurations distinguishable at rank `n` become the axes of the scene of rank `n+1` — the content of one floor turns into the directions of the next. Formally, the quotient of the active scene by the complement is a projective space over `𝔽₂`:

```
U_n / κ ≅ PG(n−2, 2)      [●]
```

— the scene of rank 3 gives a projective line, rank 4 the Fano plane, rank 5 `PG(3,2)`. The categorical form of this law (the lift as an adjoint triple of functors, the observer as a terminal object) is proved in document 02.

In these three paragraphs is the generative thesis of the theory in action, and this is their point. From a single act `ι² = id` are successively defined a space (the carrier), an operation (the complement), a center (the observer), and growth (the lift) — without a single additional postulate: each object appeared because the previous one left it no alternative. And the growth law closes the process onto itself: what is distinguished on one floor becomes the axes of the next — structure generates its own directions of further distinction. The tower of ranks is the theory's central object: a self-generating space of distinction, each floor of which is forced by the one before.

## Minimal example: rank 3

The theory's smallest substantive case can be surveyed in full — and it is also the one that shows what all of this is for.

Take three distinctions: eight states `𝔽₂³`. The poles `000` and `111` are removed; what remains is the active scene `U₃` of six states. The complement `κ(x) = x + 111` splits the six into three pairs of opposites: `{001,110}, {010,101}, {100,011}`.

The distance between states (the number of differing bits) gives exactly three relations, and each is a known graph: `R₁` (one bit) is the hexagonal cycle `C₆`; `R₂` (two bits) is two triangles `K₃ ⊔ K₃`; `R₃` (all three) is three pairs `3K₂`, the axes of opposition. Together `R₁ ∪ R₂ ∪ R₃` give the **octahedron** `K_{2,2,2}`: six vertices, three axes through a common center.

<p align="center">
  <a href="assets/figures/555.png">
    <img src="assets/figures/555.png" width="600" alt="Scene of rank 3: the octahedron K_{2,2,2} — bits, the color wheel, and the divisors of 30 on the same vertices">
  </a>
</p>

The figure shows one and the same scene read on three different materials.

**Bits.** Six three-bit states arranged in a circle; the hexagon's edges are `R₁` (one step), the diagonals through the center are `R₃ = κ`. The observer is seen literally: the center of the octahedron — the point relative to which all three axes are symmetric — **is absent among the six vertices**. The invariant of relation exists, but is not a state.

**Numbers.** The proper divisors of the number `30 = 2·3·5` — `{2,3,5,6,10,15}` — are the same six points (numbers at the vertices in the figure); the complement `d ↦ 30/d` gives the same three axial pairs (`2↔15, 3↔10, 5↔6`); the fixed point of the complement, `√30 ≈ 5.48`, is not a divisor — the observer is again outside the carrier. `[●]` — for squarefree `N` the divisor lattice is isomorphic to the Boolean cube.

**Color.** The three channels `{R, G, B}` are three axes; the six vertices form the color wheel (vertex coloring in the figure). A step around the circle is a change of one channel (`C₆`, the hue circle); the complementary color is a flip of all channels (`R↔C, G↔M, B↔Y` — the same `κ`); the gray point is the center, not belonging to the circle. The same framework reads the auditory scene as well — the status of both readings is `[◐]`: the recognition of the structure in perceptual material, its premises and its measure, is worked out in document 01 (chapter III); an expanded document on color and sound is in preparation for addition to the package.

**Conclusion of the example.** Bits, divisors, and colors here are **one object**, and the figure is its portrait. What is common to the three realizations is the type of connection itself: six elements joined by the same three relations (a step is a change of one component, a triadic partition, opposition is a flip of all components), with one common absent center. Between any two realizations there exists a one-to-one correspondence preserving all three relations — an isomorphism; mathematics regards isomorphic structures as one structure on different material. One source — the act of distinction, taken three times — and its three independent projections. The same framework is found beyond these three examples as well: in the notational organization of music, in the motivic structure of Sanskrit — documents on these realizations are in preparation for addition to the package. Rank 3 is the first place where a distinction is held in three irreducible ways at once (opposition, triadic partition, cycle), while remaining one connected figure; that is why the example is minimal and why the corpus begins with it.

## Package contents

Three documents. Each is self-contained; terminology and status discipline are uniform across them.

### [01 · Exposition: the theory in full, by rank](01_Exposition.md)

The main entry point into the corpus and the fullest document in the package. The genre is **proof-carrying narrative**: prose leads, mathematics appears the moment it is needed, every load-bearing step is marked with a status `[●]/[◐]/[○]`; concepts are introduced where they first work, no prior preparation is required. The exposition proceeds by rank, with the same cycle at each: carrier → operation and scene → structure → observer → realizations. Inside: the forcing of the minimal operation of distinction and its invariant (chapter 0); the first distinction, the two sides of the carrier `|·|₂/|·|∞`, and the imaginary unit `i = √κ` (chapters I–II); the octahedron of rank 3 with realizations in logic and color (chapter III); the break at rank 4 — the inner layer, the body, the atom (chapter IV); higher ranks and the closure of growth at rank 8 — the exhaustion of division algebras, `E₈` (chapters V–VI); the underside — the continuous side and its splitting (chapter VII); the growth functor (chapter VIII); inversion — the whole scene as an unfolding of the observer (chapter IX); the boundary — two registers of the wall: the forced form and the free values (chapter X).

Verifiers: [`code_exposition/`](code_exposition/).

### [02 · Categorical Core: construction and proofs](02_Categorical_Core.md)

The proof layer of the package — for the mathematically trained reader. The genre is **compressed mathematical text**: every step is a theorem, an identity, or a reference to a verifier; categorical language is introduced the moment it is put to work. There is a single result: the tower of carriers is a categorical construction. Inside: the carrier as the free object of the operation (chapter I); the lift as an adjoint triple `Λ_L ⊣ π ⊣ Λ_R`, monoidality (chapter II); the growth law as an isomorphism of projective spaces (chapter III); `κ` as one operator in three roles: natural transformation, De Morgan duality, Hodge star (chapter IV); the observer as terminal object, the seed as initial object, a monad and the Möbius function between them (chapter V); `sl₂` grading and the chain complex from the same matrices (chapter VI); the continuous side — the spectral limit: Gaussian measure, the Connes metric (chapter VII); time as traversal, the arrow as a comonad (chapter VIII); the boundary — a single proved identity `[κ,Δ]=0`: the form is derived, the values are input (chapter IX).

Verifiers: [`code_core/`](code_core/) — 18 scripts, 385 checks, all passing.

### [03 · Number Model: the same construction on divisors](03_Number_Model.md)

A second, independent realization of the construction — on numbers. The order of presentation is the reverse of the core — **observation → recognition → naming → proof**: the object is first built and shown (graph, color), then recognized in known structures, and only afterward proved. Inside: the series and the atom — a prime number as an axis (chapter I); the divisor cube — self-contained pure mathematics, readable independently of the whole theory (chapter II); the body `L²` — the scene's unique Hilbert space (chapter III); the octahedron of the number 30 and the Fano explosion (chapter IV); the entry of the imaginary unit `i = √κ` into the continuum (chapter V); the underside — p-adic valuations, the product formula `∏|x|ᵥ = 1`, the Gamma function, and Möbius inversion (chapter VI); the functorial layer — two axes of growth from the operations `+/×/^` with the bridge `exp` (chapter VII); two lenses, graph and color, and the wall of values explained by metamerism (chapter VIII). The document's role in the package is independent verification: what holds in both models belongs to the construction; what holds in only one belongs to the material.

Verifiers: [`code_number_model/`](code_number_model/).

### [Bridges](Bridges/)

A fourth layer of the package — **bridges**: documents that connect the core to adjacent structures without folding them into the forced tower. Two bridges are in the layer.

[The opposition skeleton → golden realization → the discrete↔continuum seam](Bridges/opposition_bridge.md): the orthoplex as the terminal realization of the scene, the icosahedron as the golden Galois half of the six-orthoplex (`ℝ⁶ = V_φ ⊕ V_ψ`), and two transitions into the continuum — spectral (a Gaussian measure) and projective (an icosahedral quasicrystal) — diverging at rank 5. The boundaries of the bridge (the external golden frame, the missing morphism `Q₅ → A₅`) are named explicitly. Verifier: [`Bridges/verify_opposition_bridge.py`](Bridges/verify_opposition_bridge.py) — 35 checks.

[The radial layer → metric and measure around the seam](Bridges/radial_bridge.md): the metric and measure-theoretic anatomy of the radial coordinate missing from document 01 (chapter VII) — a forced norm (`L²`), a decomposition into weight and transverse, concentration of measure, the cone metric of the zero point, a discrete paired realization as an address tree, dilation as the canonical radial flow, the angular excess at the apex of the cone with a separation theorem for the two curvatures (the apex one is forced and incommensurable with `π`; the ray axis `(2,3,p)` of document 01 §7.5 is input). Verifier: [`Bridges/verify_radial_bridge.py`](Bridges/verify_radial_bridge.py) — 45 checks.

Status discipline in both bridges is the same as in the core.

**How to read.** The general entry point is document 01. For the mathematician who needs proofs — document 02. For the reader coming from number theory — document 03, starting from chapter II.

## Verification

The computable part of the corpus is accompanied by verifiers (Python 3, dependency — NumPy):

```bash
python3 -m pip install -r requirements.txt

# examples: each script runs independently
python3 code_core/verify_functor_core.py
python3 code_core/verify_continuum_limit.py
python3 code_number_model/verify_divisor_cube_strict.py
python3 code_exposition/verify_carrier_from_operation.py
```

Every reference to a verifier in the text of the documents points to a specific script; the check confirms the construction and is capable of refuting it — the proofs remain the responsibility of the text.

## Support

The project develops as an **independent, open research program**, without institutional funding.

Donations are voluntary.

| Currency | Network | Address |
|--------|------|-------|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |

## Licenses

Texts, the theory, and documentation are under the [CC BY-NC-SA 4.0](LICENSE-THEORY.md) license unless otherwise noted in a specific file. Executable code (`code_core/`, `code_exposition/`, `code_number_model/`) is under the [Apache License 2.0](LICENSE).

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

© 2026 Igor M. Zhuk. The theory and documentation are distributed under the licenses indicated above.
