# Bridge: oppositional skeleton → golden realization → discrete↔continuum seam

> A bridge-note between the categorical core (documents 01–03) and the golden closure of the corpus. One arc in two parts. **Part I**: the skeleton of `n` oppositions (`2n` poles) carries a forced realization — the orthoplex `β_n` (the terminal object of the layer over the scene) — and its golden Galois half at `n=6` is the icosahedron (`ℝ⁶=V_φ⊕V_ψ`). **Part II**: the same golden frame yields a second discrete→continuum transition — cut-and-project (`ℤ⁶` through a continuous window → icosahedral quasicrystal), which diverges from the first (spectral) transition exactly at rank 5. Everything is verified — `verify_opposition_bridge.py` (**35 PASS**). Register: **constructions `[●]`, laws `[◐]`, external inputs and fronts `[○]`**.

## What this is: a bridge, not a segment of the ladder

This is a **supplementary section** — a bridge on top of the forced tower. The pack (documents 01–03) is laid out over the binary cube `Q_n=𝔽₂ⁿ`; the present document resides in `Bridges/`, the pack references it from two points (doc 01 §5.2 — the golden anchoring of the icosahedron; doc 02 §6.1 — the characterization of the scene as the terminal of the layer), but it is not part of the ladder itself. The pack already carries both ends of the arc: the cross-polytope as the "figure of the scene" (doc 01 §3.4) and the icosahedron/gold at rank 5 as a `[◐]`-namesake correspondence (doc 01 §5.1–5.2). The bridge stitches them together and continues onto the continuum side. By the corpus discipline the golden is an external 5-closure, and the statuses below hold this.

## Statuses

- `[●]` — all constructions: the skeleton `β_n`, `D⊣U` (free realization), orthoplex = terminal of the layer, refutation of the cofree (`U⊣C` does not hold), the Galois splitting `ℝ⁶=V_φ⊕V_ψ`, the `30+30` tiling, the guard of externality, the spectra of the cube/icosahedron, the 5-axis at rank 5, window=triacontahedron, discreteness, 5-axiality, phason, `ℤ[φ]` (verifier).
- `[◐]` — laws: "two machines — the additive and multiplicative faces of `|·|∞` (`+/×`)", the functorial frame (colimit of the tower vs Galois decomposition). Resonance with the corpus, named.
- `[○]` — the golden frame is external (the skeleton's symmetry does not single it out); the missing morphism `Q₅→A₅` (the namesake correspondence `A₅↔U₅`, doc 01 §5.1); the unity of the two machines and the general case `(n,d)` are not shown.

---

# Part I. The skeleton and the golden realization

## Layer 0. The skeleton: `n` oppositions = `2n` poles

The base is the category **Scene** of free involutions `(X, κ)`, `κ²=id` without fixed points (the same observer's Scene, doc 01 ch I; doc 02 ch V). An object with `n` orbits is `n` oppositions, `2n` poles; the growth of the skeleton is the addition of an opposition, `+2` poles. This is the cross-polytope side, dual to the cube: `Q_n` carries `2ⁿ` corners (coordinates), `β_n` carries `2n` poles (axes); the figures are a `κ`-pair (doc 01 §3.4).

## Layer 1. Realizations: `D ⊣ U` holds, the orthoplex is the terminal of the layer

Above the skeleton is the category **Real** of `κ`-invariant antipode-free graphs. The edge-forgetting functor `U:\mathrm{Real}→\mathrm{Scene}` has a **left** adjoint `D ⊣ U`: `D` is the empty graph (free realization), from which every `κ`-map is a homomorphism; the bijection `Hom_{\mathrm{Real}}(DS,A)\cong Hom_{\mathrm{Scene}}(S,UA)` is verified `[●]` (§B). `U` has no **right** adjoint (cofree): the orthoplex does not serve as a cofree object — the `Hom`-bijection breaks (`Hom_{\mathrm{Real}}(β_3, C(\text{one axis}))=0 \ne 8=Hom_{\mathrm{Scene}}`), and the assignment `C:\mathrm{Scene}→\mathrm{Real}` is not functorial (all four morphisms `S_2→S_1` tear an edge) `[●]` (§B). The correct universal property is weaker and more precise: the orthoplex `β_n=K_{n×2}` (all non-antipodal pairs) is the **terminal object of the layer** `\mathrm{Real}` over a fixed scene — the maximal `κ`-invariant antipode-free graph into which every other realization of the same skeleton embeds (every non-edge of it is an antipodal pair) `[●]` (§A–B). This is precisely the categorical form of "the figure of the scene is forced as minimal" (doc 03 §4.3): the forcedness of the edge rule "all are adjacent except the antipode" = terminality in the layer.

## Layer 2. The golden half: `ℝ⁶ = V_φ ⊕ V_ψ`

The symmetric `3`-dimensional realization `β_6` is the orthogonal splitting of the ambient `ℝ⁶` into the irreducibles of the residual group:

$$\mathbb{R}^6 = V_\varphi \oplus V_\psi, \qquad \varphi \leftrightarrow \psi \ \text{ under } \ \mathrm{Gal}(\mathbb{Q}(\sqrt5)/\mathbb{Q}).$$

Two three-dimensional irreducibles `H₃=A₅×Z₂`, Galois-conjugate (`√5→−√5`). Verified `[●]` (§C–E): six axes at the golden angle `arccos(1/√5)`, six vectors `gold⊕conjugate` are orthonormal (they form a `6D`-orthoplex); the projection onto either block is a regular icosahedron; the two Galois halves **tile** the `60` edges as `30+30`. The icosahedron is a spanning subgraph of `β_6` (half the edges), central inversion preserves its edges (an object of `Real`, §F).

**The guard of externality `[●]` (§G).** The full symmetry of the skeleton is `B₆` of order `46080`; only `I_h` of order `120` holds the golden half (a `384`-fold break). The skeleton's symmetry does **not** single out the gold: the golden frame is an external input `[○]`. The icosahedron remains a `[◐]`-namesake correspondence of the pack (doc 01 §5.2); this layer refines it (a verified realization instead of a coincidence of number), without raising its status.

---

# Part II. The discrete↔continuum seam

The golden frame of Part I yields a **second** machine of transition into the continuum, distinct from the spectral limit of the pack (doc 02 ch VII).

## Two machines: the functorial difference

| | **Machine 1** — the spectral limit | **Machine 2** — cut-and-project |
|---|---|---|
| operation | `colim_{n→∞} Q_n` — vertical limit of the tower | `ℝ⁶=V_φ⊕V_ψ` — horizontal Galois decomposition |
| algebra | abelian `(ℤ/2)ⁿ`, CLT | non-abelian `A₅`, `√5` |
| source | intrinsic: the spectrum of the cube | external frame of Part I |
| spectral signature | `{2k}` integer, without irrationality | icosahedron: `{5,±√5,−1}` — carries `√5` |
| continuum object | measure (Gaussian) along the weight axis | window (triacontahedron) across physical space |
| what it completes | the additive side `+` | the multiplicative `×/^` (`φ`-inflation, `ℤ[φ]`) |

The difference is visible in the spectrum `[●]` (§H–I): the Laplacian of the cube is integer-valued (`{2k}`, weights → Gaussian), whereas the graph of the icosahedron carries `±√5`. In functors: a limit over a diagram (tower, the vertical) versus a decomposition under a group action (`⊕` under `Gal(ℚ√5)`, the horizontal).

## Divergence: rank 5

Ranks 1–4 are crystallographic (axes 2, 3, 4, 6) — the transition is single, spectral. At **rank 5** the 5-axis first appears (`A₅`, `√5`, Abel–Ruffini) `[●]` (§J); by the crystallographic restriction it does not tile periodically, and the spectral limit does not accommodate it — this forces a second, transverse machine. The discrete→continuum bridge **bifurcates at rank 5**, is realized at rank 6. The fork coincides with the corpus exceptionality of rank 5.

## Cut-and-project: the construction is carried through

The step shell→lattice is closed `[●]` (§K–N): the full lattice `ℤ⁶`, the ambient split by the golden frame into `E∥⊕E⊥` (orthogonally, totally irrationally ⟹ aperiodically). The acceptance window in the shadow `E⊥` is the zonotope of six perp-generators, `15` normals → **30 faces = rhombic triacontahedron**. A point of `ℤ⁶` generates an atom in `E∥` if its shadow is in the window:

- **discreteness** — a Delone set (min-distance `> 0`, without large holes);
- **5-axiality** — the star of shortest directions is invariant under `72°` and `120°`, **not** under `90°`: non-crystallographic icosahedral order;
- **phason** — a shift of the window `γ` changes the pattern, keeps the density: **the window (form) is fixed `[●]`, the phase of the cut is a free input `[○]`**;
- **the golden ring** — coordinates `∈ ℤ[φ]` (height `^`).

This is our seam "the form is forced / the value is free", read on the Galois shadow: the form is given by the fixed golden window, the freedom by the phase of the cut. The seed (`β_6`) and the lattice (`ℤ⁶`) are linked: `β_6` is the minimal shell of `ℤ⁶`.

## Open fronts `[○]`

- **The unity of the two machines (a research program).** The Gaussian (spectrum) and the window (cut-and-project) are two different machines. The hypothesis worth working toward: both are **the left and right factorizations of a single more general functor** discrete→continuum; then the `+`-limit and the `×`-inflation are its two adjoint ends. For now this is a question, not a conclusion.
- **The missing functor `Q₅→A₅`.** The forcing of Machine 2 rests on the `[◐]`-namesake correspondence `A₅↔U₅` (doc 01 §5.1). The exact form of the gap is the **missing morphism** `Q₅ → A₅`: in the chain `Q₅→A₅→H₃→` icosahedron, the first link is empty. To construct it is the central open problem of the whole arc.
- **Example versus theorem: the general case `(n,d)`.** The construction is verified for `(6,3)` — this is an example. The value is decided by the passage to `(n,d)`: `(6,3)` gives a beautiful solid, `(n,d)` would give a framework. The candidate is `H₄`/the 600-cell; the forcedness of `H₃` is not proven.

---

## Summary

One arc: the skeleton of oppositions (`Scene`, `+2`) → the terminal-in-layer orthoplex `β_n` (`D⊣U` holds, the cofree `U⊣C` is refuted; the dual of the cube) → the golden Galois half `β_6` (icosahedron, `ℝ⁶=V_φ⊕V_ψ`, `30+30` tiling, the frame external) → two machines discrete→continuum (vertical spectral limit vs horizontal Galois projection), diverging at rank 5, where the 5-axis is non-crystallographic. Cut-and-project is carried through from `ℤ⁶` to a 5-axial quasicrystal in `ℤ[φ]` with the phase as input. The constructions (including `D⊣U`, the terminal of the layer, and the refutation of the cofree) are `[●]`, **35 PASS**; the law of the "two faces of `|·|∞`" and the functorial frame are `[◐]`; the externality of the frame and the missing functor `Q₅→A₅` are `[○]`. The arc links the coordinate side of the cube `Q_n` with the golden and continuum sides, remaining a bridge, not a segment of the ladder. The skeleton is `verify_opposition_bridge.py`.
