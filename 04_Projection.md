# Projection: definition and criteria

Documents 01–03 built the core and realized it twice — on bits and on numbers; the status `[◐]` everywhere marked the places where a known structure is **recognized** in the construction. This document turns the marker into an object: it gives a definition of projection, a list of preserved invariants, a criterion of equivalence of realizations, rejection criteria, and a measure of rigor. After it, the question "is this one figure?" ceases to be decided by eye — it acquires a procedure with both outcomes: to confirm and to reject. The document's verifier — `code_projection/verify_projection_criteria.py` (19 checks) — runs the definition on live material, including mandatory negative controls.

## Introduction: from marker to object

The package has already shown one scene on three materials: six bit states, six divisors of the number 30, six colors of the circle (document 01, chapter III; README). The assertion "this is one object" rested on isomorphism — a one-to-one correspondence preserving all three relations. But isomorphism is a notion about two already given structures; it is silent about **what exactly** must be preserved when the core is applied to new material, when two realizations are to be counted as one, and what could show that the presented correspondence is unsuitable. As long as these three questions are decided ad hoc, each bridge carries an interpretive residue. The document answers them with a general definition; everything in it is assembled from tools already working in the corpus — no new entities are introduced, their explicit form is introduced.

**Statuses.** The definition itself and its runs on mathematical material are `[●]` (verifier). Readings on empirical material (color, sound, physics) are not raised by the definition: they have a ceiling, named in chapter I. The open places are collected in chapter VII.

## Chapter I. Core and material

**The core** — that which is built in document 02 and does not depend on the material: the scene `(U_n, κ)` with relation classes `R_1, …, R_n` (Hamming distance), poles outside the scene, center `σ½` outside the carrier, and the lift `Λ_L ⊣ π ⊣ Λ_R`, linking the storeys into a tower.

**The material** — a set `M` with its own, independently defined structure: a candidate for involution `κ_M` and a family of relations. The requirement of independence is essential: the material's relations must be given by its own means (for divisors — by the arithmetic of `lcm/gcd`, for tones — by interval classes `ℤ₁₂`), without regard to the bits; otherwise "preservation of relations" is tautological. The verifier enforces this literally (§B).

Materials divide into two kinds, and the difference sets the **status ceiling**:

- **mathematical material** (divisors, graphs, groups, lattices): its relations are theorems, and the projection onto it can be proved in full — ceiling `[●]`;
- **empirical material** (color, sound, physical fields): its structure is partly given by measurement or perception, and at least one premise of the correspondence lies outside mathematics (opponency of channels, octave equivalence, identification of operators with fields). The projection onto such material is provable only in its mathematical part; in full, its status does not exceed `[◐]`, and the premise is named explicitly.

The separation removes the ambiguity of the word "realization": the divisors of 30 are a realization in the strict sense (a provable isomorphism); the color circle is a reading with a named perceptual premise. Both are projections by the definition below; the difference is in the ceiling.

## Chapter II. Definition

> **Definition (projection of a scene).** Let `(U_n, κ)` be the scene of the core, `M` a material with candidate involution `κ_M` and its own relations. A **projection** is a map `p: U_n → M` satisfying five conditions:
>
> 1. **carrier**: `p` is a bijection onto its image (distinguished states are distinguishable in the material);
> 2. **intertwining**: `p ∘ κ = κ_M ∘ p` — the complement of the core passes into the opposite of the material;
> 3. **relations**: the class of each pair is preserved — `x R_d y ⟺ p(x) R'_d p(y)`, where `R'_d` are the relations given by the material's own means;
> 4. **center**: the fixed point of `κ_M` (if it exists in the material) does not belong to the image `p(U_n)` — the observer remains outside the carrier;
> 5. **poles**: the images of `0ⁿ` and `1ⁿ` lie outside the scene of the material.

Each condition is substantive — there exist materials that fall exactly on it (chapter V). The run of the definition on the dictionary bit ↔ divisors of 30 is five checks, one per condition `[●]` (§A): a bijection onto `{2,3,5,6,10,15}`; `p(κx) = 30/p(x)`; the classes of pairs by the number of primes in `lcm/gcd` coincide with the Hamming ones; the fixed point of `d ↦ 30/d` is `√30`, which is not a divisor; the poles `1` and `30` are outside the scene.

## Chapter III. Invariants and canonicity

A list of what the projection preserves by definition: the cardinality of the scene `2ⁿ−2`; the structure of `κ`-pairs (`2^{n−1}−1` axes); the partition of all pairs of states into `n` relation classes with their graph types (at rank 3 — `C₆ / K₃⊔K₃ / 3K₂`); the externality of the center and the poles. Derived invariants — the spectrum, the weight grading, the quotient `U_n/κ ≅ PG(n−2,2)` — are preserved as consequences.

Beyond preservation, the projection has a **measure of canonicity — rigidity**: the number of dictionaries satisfying the definition. For rank 3 there are exactly `12 = |D₆|` out of `720` possible bijections `[●]` (§C) — the correspondence is canonical up to the figure's own symmetry. Rigidity distinguishes a forced dictionary from a fitted one: if the number of admissible dictionaries is close to the number of all bijections, the correspondence carries no information; if they are a single symmetry orbit, the dictionary is essentially unique. Rigidity must be stated for every claimed projection.

## Chapter IV. Equivalence: the tuning fork

> **Definition (equivalence of realizations).** Two projections `p₁: U_n → M₁`, `p₂: U_n → M₂` are equivalent if `p₂ ∘ p₁^{-1}` is an isomorphism of images preserving relations. **A property belongs to the core** if it holds in all equivalent realizations; **a property belongs to the material** if it is present in at least one and absent in another.

This is a formalization of the tuning fork principle (document 02, epilogue: two models, one functor). The run `[●]` (§F): three `κ`-pairs, the external center, `|U₃| = 6` — hold on bits and on numbers, belong to the core. The height `v_p ≥ 2` is only in the numbers (`D(60)` is a lattice of 12 elements, which is not a cube); the numerical magnitudes of the divisors (`2 < 3 < 5`, `√30 ≈ 5.477`) are only in the numbers. Both properties belong to the material, and no conclusion of the core is entitled to rest on them. The tuning fork is a working instrument of attribution: every assertion of the corpus about the "construction" must survive a change of realization.

## Chapter V. Rejection: guards and negative controls

The definition must be able to reject — otherwise it asserts nothing. Three rejection criteria, each with a precedent:

**Structural rejection** — violation of any of the five conditions. Negative controls `[●]` (§D): the **diatonic** (7 notes) — odd cardinality, no free involution exists, condition 2 is unsatisfiable; the **consecutive hexad** `{0,…,5} ⊂ ℤ₁₂` — six points are present, but the distance classes give the partition `5/4/3/2/1` instead of `6/6/3`, condition 3 falls. The whole-tone hexad, by comparison, passes (classes `6/6/3` on intervals `2/4/6`). The definition separates suitable six-element material from unsuitable, and does so computably.

**Notation guard** — the claimed structure must survive every admissible recoding of the material: renaming of generators, change of numeral base, change of normalization. The run `[●]` (§E): the relation classes on divisors are invariant under the renaming of primes `(2,3,5) → (3,5,2)`; whereas the property "a divisor is unique in decimal notation" does not survive this substitution — a pattern of notation, rejected. Precedents of the package: the base guard — the geometric `½` is shifted by a change of normalization, a mirage `[✗]` under invariant `σ½` (document 03, chapter VI); the "theory of prime-horizons" — magnitudes of notation, perishing under a change of base `[✗]` (document 01, chapter VI).

**Fitting guard** — a correspondence that uses free parameters tuned to the answer is not a projection; each tuned parameter must be declared an input `[○]` or a fit `[◐]`. Precedent of the package — the mass labeling (document 01, chapter V): the quark masses are named a fit `[◐]`, the phase `δ = 2/9` a recognition with an explicit "not derived", `sin²θ_W = 2/9` refuted `[✗]`.

## Chapter VI. Measure of rigor: grades of projection

Projections are ranked along three independent axes.

**Storeyedness.** A *scenic* projection satisfies the definition at one rank. A *tower* one continues along the lift: there exists `p_{n+1}` with `p_{n+1} ∘ Λ = Λ_M ∘ p_n`, and the law of growth holds in the material. The run `[●]` (§G): the divisor dictionary is a tower one (intertwining of `κ` at rank 4 via `d ↦ 210/d`, consistency with the embedding `D(30) ⊂ D(210)`, seven Fano axes in both models). The tower grade is precisely what the corpus's functorial audit calls "functorized"; the scenic one without continuation — "recognition".

**Material ceiling** (chapter I): mathematical — up to `[●]`; empirical — up to `[◐]` with a named premise.

**Rigidity** (chapter III): the number of admissible dictionaries relative to the number of all bijections.

A summary of the package's projections:

| projection | storeyedness | ceiling | rigidity | status |
|---|---|---|---|---|
| bits ↔ divisors (doc 03) | tower (§G) | mathematical | `12/720` | `[●]` |
| bits ↔ color (doc 01, ch III) | scenic (lift in the material undefined) | empirical (premise: opponency) | `12/720` | `[◐]` |
| bits ↔ whole-tone hexad | scenic | empirical (premise: octave equivalence) | `12/720` | `[◐]` |
| cube → free spins (doc 02, ch IX) | tower, at one point | empirical (identification of operators) | — | `[◐]` |

The table shows the definition at work: four correspondences, previously marked with a single `[◐]`/`[●]` ad hoc, are now distinguishable along three axes, and for each it is visible exactly what it lacks to reach the next grade.

## Chapter VII. Boundaries `[○]`

- **The category of materials is not built.** The definition specifies a projection one at a time; a unified category in which projections would be morphisms and the tuning fork a universal property remains a program.
- **Dynamic materials.** The definition covers static structures (sets with relations); material with its own dynamics (flows, evolution) requires an extension — preservation not only of relations but also of motion. This is the very place where the question of a morphism into physics is localized (document 02, chapter IX, §9.4): the bridge into free spins is the only point where intertwining with dynamics is checked.
- **The empirical ceiling is not pierceable from within.** No accumulation of mathematical checks raises a `[◐]`-reading to `[●]`: the premise (opponency, octave, identification of operators) lies outside the apparatus. The definition records this as a property of the material's kind; the honest form of growth here is refinement of the premise, its empirical test, or rejection.

## Summary

The marker `[◐]` has received a definition. A projection is a map of the scene into the material with five preserved conditions (carrier, intertwining, relations, center, poles); the material must carry its structure independently, and its kind sets the status ceiling (mathematical — `[●]`, empirical — `[◐]` with a named premise). Canonicity is measured by rigidity (`12/720` at rank 3); the equivalence of realizations and the attribution of properties to the core or the material are decided by the tuning fork; rejection is secured by three guards — structural, notation, fitting — and the definition computably rejects unsuitable materials (the diatonic, the consecutive hexad) and patterns of notation (decimal uniqueness). Rigor is graded: a scenic projection versus a tower one (continuation along the lift — the divisors pass up to Fano). The entire definition is run by the verifier: `code_projection/verify_projection_criteria.py`, 19 checks, including negative controls. Named as open are the category of materials, dynamic materials, and the impenetrability of the empirical ceiling from within `[○]`. Thereby the bridges of the corpus cease to be ad hoc interpretations: each correspondence has a checking procedure, a measure of rigor, and a named point where it could fall.
