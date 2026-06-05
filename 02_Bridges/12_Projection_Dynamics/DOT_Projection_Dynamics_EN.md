# Reading dynamics: projection as an act (the language of projection)

**What this is.** Volume 6 gives readings as a **static catalogue of projections** — which readings exist. This bridge
adds the **verb**: how a projection is PERFORMED (the act), how it CHANGES, and how a TRANSITION between projections
happens. Read through external languages: measurement theory (evolution + measurement), change of basis, a category with
idempotents, the hyperoctahedral group.

Like the other bridges, this is a **translation, not a foundation**: the corpus is self-contained. Full computations are
in the reading branch (elementary linear algebra; the laws below are one-line checkable).

---

## 1. The primitives of the language

- **State** \(x\) — a point/superposition on the scene (the cube or its continuous extension).
- **Frame** \(F\) — a choice of distinctions (codebook/basis): vertices (**point**), Walsh (**spectrum**), rank-bands
  (**grading**).
- **Projection** \(\pi_F(x)\) — snap to the nearest distinction of \(F\) = the **act**: lossy, idempotent
  \(\pi^2=\pi\), irreversible.
- **Frame-change** \(g\in\{\partial,T,H,W,\kappa\}\) — a reversible transform of the frame.
- **Transition** — a path of frame-changes, possibly with acts \(\pi\) along the way.

## 2. Two sorts of operation (evolution ⟂ measurement)

| sort | operation | property |
|---|---|---|
| **EVOLUTION** | frame-change \(g\) | reversible (orthogonal); a group |
| **MEASUREMENT** | projection \(\pi_F\) | irreversible, \(\pi^2=\pi\), lossy |

Formally a **category** (objects = frames, morphisms = reversible changes ⊔ idempotent projections), not a groupoid. The
same split as in Volume 7: reversible evolution (the observer-\(i\), the Weyl/Cartan side) ⟂ the irreversible act.

## 3. The key law: \([\pi,g]\ne0\) — changing the frame CHANGES the reading

$$\pi_F(g\cdot x)\;\ne\;g\cdot\pi_F(x).$$

Since \(\pi\) is lossy, **order matters**: rotate-then-decide ≠ decide-then-rotate. The commutator \([\pi,g]\) is the
**content of "changing the projection"**: without the lossiness of \(\pi\) the change would be empty (just other
coordinates); it is the loss that makes the change meaningful.

## 4. The algebra of transitions: free vs contentful

Reversible changes split into two classes:

- **FREE** (\([\pi,g]=0\) covariantly): \(g\) is a **frame-automorphism** (it permutes the atom set). For the
  cross-polytope \(\{\pm e_i\}\) this is the **hyperoctahedral group** \(B_n=(\mathbb Z_2)^n\rtimes S_n\) — **the very
  forcing group** (Volume 0 §2.5: \(B_n\)-neutrality forces \(\kappa\)). Free changes only **relabel** distinctions,
  with no loss — the **"invariants of attention"**.
- **CONTENTFUL**: generic rotations, the Walsh \(W\) — they **mix** atoms, the reading changes.

So the symmetries that do not change the reading = \(B_n\) = the group that **defines** the structure. The split
"relabel ↔ mix" is the algebra of transitions.

## 5. The observer is NOT a strict fixed point (an honest correction)

The naive "the observer is fixed by all reversible changes" is **false**:

- Walsh \(W\) **swaps** the observer's two faces — the **DC mode** (spectral face) and the **point-mass** \(\delta_0\)
  (point face): \(W(\mathrm{DC})=\delta_0,\ W(\delta_0)=\mathrm{DC}\);
- translation moves \(\delta_0\to\delta_w\).

The invariant is **not a single vector but the observer's cross-frame identity**: the pair-orbit
\(\{\mathrm{DC},\delta_0\}\) (on which \(W^2=\mathrm{id}\)). DC is fixed by the spatial symmetries
(translations+permutations), \(\delta_0\) by the linear ones (permutations + \(\kappa\)); **\(W\) carries the observer
between its faces**. This is the operational form of the discrete/continuous boundary: \(W\) is its swap.

## 6. Reading dynamics

The language yields a **generative cycle** the static Volume 6 lacked:
$$\textbf{observe}\ (\pi:\ \text{collapse, breaking }\kappa\text{-symmetry})\ \to\ \textbf{change frame}\ (g)\ \to\ \textbf{observe}.$$
Growth is forced by **capacity** (scene overflow → lift \(H\), a larger frame); the **arrow** comes from the
irreversibility of \(\pi\); the chosen vertex is the **seed of the lift** (Volume 5), the new axis entering through the
centre.

## 7. Status and scope

A layer of **connections/dynamics over Volume 6**: the static readings gain a verb (act, change, transition). The native
content (the observer, readings-as-projections) is in Volumes 5–7; here is an external reading of their **dynamics**.

**Honestly:** the "evolution + measurement" structure, a category with idempotents, change of basis, hyperoctahedral
stabilizers, the Fourier swap DC↔point-mass — **standard mathematics**; there is no new theorem. **The contribution is
the language**: projection/change/transition as operations and their laws (free = \(B_n\); \([\pi,g]\ne0\); the observer
is \(W\)-covariant, not fixed). The laws are elementary and one-line checkable by linear algebra.
