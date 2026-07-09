# Bridge: opposition skeleton → golden realization → the discrete↔continuum seam

> A bridge note between the categorical core (documents 01–03) and the golden closure of the corpus. One arc in two parts. **Part I**: a skeleton of `n` oppositions (`2n` poles) carries a forced realization — the orthoplex `β_n` (terminal object of the fiber over the scene) — and its golden Galois half at `n=6` is the icosahedron (`ℝ⁶=V_φ⊕V_ψ`). **Part II**: the same golden frame yields a second discrete→continuum transition — cut-and-project (`ℤ⁶` through a continuous window → an icosahedral quasicrystal) — which diverges from the first (spectral) transition exactly at rank 5. Everything is checked — `verify_opposition_bridge.py` (**35 PASS**). Register: **constructions `[●]`, laws `[◐]`, external inputs and fronts `[○]`**.

## What this is: a bridge, not a rung of the ladder

This is a **supplementary section** — a bridge laid over the forced tower. The pack (documents 01–03) is set out on the binary cube `Q_n=𝔽₂ⁿ`; this document lives in `Bridges/`, and the pack references it from two points (document 01 §5.2 — the golden tie-in of the icosahedron; document 02 §6.1 — the characterization of the scene as fiber-terminal), but it does not itself belong to the ladder. The pack already carries both ends of the arc: the cross-polytope as the "figure of the scene" (document 01 §3.4) and the icosahedron/golden ratio at rank 5 as a `[◐]`-coincidence-of-name (document 01 §5.1–5.2). The bridge stitches them together and continues onto the continuum side. By corpus discipline, the golden ratio is an external 5-closure, and the statuses below preserve that.

## Statuses

- `[●]` — all constructions: the skeleton `β_n`, `D⊣U` (free realization), orthoplex = fiber-terminal, the refutation of the cofree object (`U⊣C` does not hold), the Galois split `ℝ⁶=V_φ⊕V_ψ`, the `30+30` tiling, the externality guard, the cube/icosahedron spectra, axis-5 at rank 5, window=triacontahedron, discreteness, 5-fold symmetry, phason, `ℤ[φ]` (verifier).
- `[◐]` — laws: "two machines — additive and multiplicative faces of `|·|∞` (`+/×`)," the functorial frame (colimit of the tower vs. Galois decomposition). Resonates with the corpus, named.
- `[○]` — the golden frame is external (the skeleton's symmetry does not select it); the missing morphism `Q₅→A₅` (coincidence-of-name `A₅↔U₅`, document 01 §5.1); the unity of the two machines and the general case `(n,d)` are not shown.

---

# Part I. Skeleton and golden realization

## Layer 0. Skeleton: `n` oppositions = `2n` poles

The base is the category **Scene** of free involutions `(X, κ)`, `κ²=id` with no fixed points (the same Scene of the observer, document 01 chapter I; document 02 chapter V). An object with `n` orbits — `n` oppositions, `2n` poles; growth of the skeleton is the addition of an opposition, `+2` poles. This is the cross-polytope side, dual to the cube: `Q_n` carries `2ⁿ` corners (coordinates), `β_n` carries `2n` poles (axes); the two figures form a `κ`-pair (document 01 §3.4).

## Layer 1. Realizations: `D ⊣ U` holds, the orthoplex is the fiber-terminal

Over the skeleton lies the category **Real** of `κ`-invariant, antipode-free graphs. The edge-forgetting functor `U:\mathrm{Real}→\mathrm{Scene}` has a **left** adjoint `D ⊣ U`: `D` is the empty graph (the free realization), from which every `κ`-map is a homomorphism; the bijection `Hom_{\mathrm{Real}}(DS,A)\cong Hom_{\mathrm{Scene}}(S,UA)` is checked `[●]` (§B). `U` has **no right** adjoint (cofree object): the orthoplex does not serve as a cofree object — the `Hom`-bijection breaks (`Hom_{\mathrm{Real}}(β_3, C(\text{one axis}))=0 \ne 8=Hom_{\mathrm{Scene}}`), and the assignment `C:\mathrm{Scene}→\mathrm{Real}` is not functorial (all four morphisms `S_2→S_1` tear an edge) `[●]` (§B). The correct universal property is weaker and sharper: the orthoplex `β_n=K_{n×2}` (all non-antipodal pairs) is the **terminal object of the fiber** `\mathrm{Real}` over a fixed scene — the maximal `κ`-invariant antipode-free graph into which every other realization of the same skeleton embeds (every non-edge of it is an antipodal pair) `[●]` (§A–B). This is the categorical form of "the figure of the scene is forced as minimal" (document 03 §4.3): the forcedness of the edge rule "all pairs adjacent except the antipode" = terminality in the fiber.

## Layer 2. The golden half: `ℝ⁶ = V_φ ⊕ V_ψ`

The symmetric `3`-dimensional realization of `β_6` is an orthogonal splitting of the ambient `ℝ⁶` into the irreducibles of the residual group:

$$\mathbb{R}^6 = V_\varphi \oplus V_\psi, \qquad \varphi \leftrightarrow \psi \ \text{ under } \ \mathrm{Gal}(\mathbb{Q}(\sqrt5)/\mathbb{Q}).$$

Two three-dimensional irreducibles of `H₃=A₅×Z₂`, Galois-conjugate (`√5→−√5`). Checked `[●]` (§C–E): six axes under the golden angle `arccos(1/√5)`, six vectors `golden⊕conjugate` are orthonormal (forming a `6D`-orthoplex); the projection onto either block is a regular icosahedron; the two Galois halves **tile** the `60` edges as `30+30`. The icosahedron is a spanning subgraph of `β_6` (half the edges); central inversion preserves its edges (an object of `Real`, §F).

**Externality guard `[●]` (§G).** The full symmetry of the skeleton is `B₆` of order `46080`; the golden half is held only by `I_h` of order `120` (a `384`-fold collapse). The skeleton's symmetry **does not select** the golden ratio: the golden frame is an external input `[○]`. The icosahedron remains a `[◐]`-coincidence-of-name in the pack (document 01 §5.2); this layer sharpens it (a checked realization in place of a numerical coincidence) without raising its status.

---

# Part II. The discrete↔continuum seam

The golden frame of Part I yields a **second** machine for the transition into the continuum, distinct from the pack's spectral limit (document 02 chapter VII).

## Two machines: the functorial difference

| | **Machine 1** — spectral limit | **Machine 2** — cut-and-project |
|---|---|---|
| operation | `colim_{n→∞} Q_n` — vertical limit of the tower | `ℝ⁶=V_φ⊕V_ψ` — horizontal Galois decomposition |
| algebra | abelian `(ℤ/2)ⁿ`, CLT | non-abelian `A₅`, `√5` |
| source | intrinsic: spectrum of the cube | external frame from Part I |
| spectral signature | `{2k}` integer, no irrationality | icosahedron: `{5,±√5,−1}` — carries `√5` |
| continuum object | measure (Gaussian) along the weight axis | window (triacontahedron) across physical space |
| what it completes | the additive side `+` | the multiplicative side `×/^` (`φ`-inflation, `ℤ[φ]`) |

The difference is visible in the spectrum `[●]` (§H–I): the Laplacian of the cube is integer-valued (`{2k}`, weights → Gaussian), while the icosahedron graph carries `±√5`. In functorial terms: a limit over a diagram (the tower, vertical) versus a decomposition under a group action (`⊕` under `Gal(ℚ√5)`, horizontal).

## The divergence: rank 5

Ranks 1–4 are crystallographic (axes 2, 3, 4, 6) — there is one transition, the spectral one. At **rank 5**, an axis-5 appears for the first time (`A₅`, `√5`, Abel–Ruffini) `[●]` (§J); by the crystallographic restriction it cannot tile periodically, and the spectral limit does not accommodate it — this forces the second, transverse machine. The discrete→continuum bridge **bifurcates at rank 5**, and is realized at rank 6. The fork coincides with the corpus's exceptional treatment of rank 5.

## Cut-and-project: the construction carried through

The step shell→lattice is closed `[●]` (§K–N): the full lattice `ℤ⁶`, with the ambient space split by the golden frame into `E∥⊕E⊥` (orthogonal, totally irrational ⟹ aperiodic). The acceptance window in the shadow `E⊥` is the zonotope of the six perp-generators, `15` normals → **30 faces = a rhombic triacontahedron**. A point of `ℤ⁶` produces an atom in `E∥` if its shadow lies in the window:

- **discreteness** — a Delone set (min-distance `> 0`, no large gaps);
- **5-fold symmetry** — the star of shortest directions is invariant under `72°` and `120°`, **not** under `90°`: non-crystallographic icosahedral order;
- **phason** — shifting the window by `γ` changes the pattern while the density holds: **the window (shape) is fixed `[●]`, the phase of the cut is a free input `[○]`**;
- **golden ring** — coordinates `∈ ℤ[φ]` (height `^`).

This is our seam "the form is forced / the value is free," read on the Galois shadow: the fixed golden window gives the form, the phase of the cut gives the freedom. The seed (`β_6`) and the lattice (`ℤ⁶`) are linked: `β_6` is the minimal shell of `ℤ⁶`.

## Open fronts `[○]`

- **Unity of the two machines (a research program).** The Gaussian (spectrum) and the window (cut-and-project) are two different machines. A hypothesis worth pursuing: both are the **left and right factorizations of one more general functor** discrete→continuum; then the `+`-limit and the `×`-inflation would be its two adjoint ends. For now this is a question, not a conclusion.
- **The missing functor `Q₅→A₅`.** The forcing of Machine 2 rests on the `[◐]`-coincidence-of-name `A₅↔U₅` (document 01 §5.1). The precise shape of the gap is a **missing morphism** `Q₅ → A₅`: in the chain `Q₅→A₅→H₃→` the icosahedron, the first link is empty. Constructing it is the central open problem of the whole arc.
- **An example versus a theorem: the general case `(n,d)`.** The construction is checked for `(6,3)` — this is an example. The value hinges on the passage to `(n,d)`: `(6,3)` gives a beautiful solid, `(n,d)` would give a framework. A candidate is `H₄`/the 600-cell; the forcedness of `H₃` is not proved.

---

## Summary

One arc: the skeleton of oppositions (`Scene`, `+2`) → the fiber-terminal orthoplex `β_n` (`D⊣U` holds, the cofree object `U⊣C` is refuted; the dual of the cube) → the golden Galois half `β_6` (the icosahedron, `ℝ⁶=V_φ⊕V_ψ`, the `30+30` tiling, an external frame) → two discrete→continuum machines (the vertical spectral limit vs. the horizontal Galois projection), diverging at rank 5, where the axis-5 is non-crystallographic. Cut-and-project is carried through from `ℤ⁶` to a 5-fold quasicrystal in `ℤ[φ]` with a phase input. The constructions (including `D⊣U`, the fiber-terminal, and the refutation of the cofree object) are `[●]`, **35 PASS**; the law of "the two faces of `|·|∞`" and the functorial frame are `[◐]`; the externality of the frame and the missing functor `Q₅→A₅` are `[○]`. The arc links the coordinate side of the cube `Q_n` to the golden and continuum sides, remaining a bridge, not a rung of the ladder. The skeleton is `verify_opposition_bridge.py`.
