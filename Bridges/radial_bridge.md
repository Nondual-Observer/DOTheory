# Bridge: the radial layer — metric and measure around the seam

> A bridge between the reverse side (document 01, chapter VII), the categorical core (document 02, chapters V and VII), and the numerical model (document 03, chapters III and VI). Chapter VII gives the radial coordinate a partial form on the Archimedean side of the seam: the sphere theorem for the cube and octahedron of rank 3 (§7.2), the splitting into an axial and a radial part at the break of `κ` (§7.3), the curvature axis `(2,3,p)` with Bruhat–Tits trees on the p-adic side (§7.5). The present bridge investigates another stratum of the same coordinate — the metric and measure-theoretic anatomy of the radius (norm, decomposition, concentration of measure, metric of the zero point) and its discrete paired realization, separate from the p-adic trees of §7.5 — and generalizes the sphere theorem to an arbitrary rank. The bridge touches the ray curvature axis `(2,3,p)` with a single statement — the separation theorem (§8). Everything computable — `verify_radial_bridge.py` (**45 PASS**). Register: constructions `[●]`, laws `[◐]`, external inputs and fronts `[○]`.

## Statuses

- `[●]` — all constructions: the budget `r²=w²+t²` on the skeleton of any rank, the forcedness of the `L²` norm (parallelogram equality), the forcedness of the cone metric, the thin-shell law and the inaccessibility of `σ½` by measure, the dilation flow `δ_λ`, the ultrametricity of the address radius, the product formula as radial balance, the numerical realization `r(d)`, the angular excess at the apex of the cone, and the separation theorem of the two curvatures (Dehn, Niven) — verifier.
- `[◐]` — laws: the two radii as a realization of the two ends of the category (seed/terminal); numbers and bits as the polar decomposition of the tuning fork (radius/angle).
- `[○]` — the position of a state on the radius (value, not form); the link of the apex excess with the ray axis `(2,3,p)` beyond the proven separation.

---

## 1. The budget: weight and the transverse

At the vertices of the carrier `Q_n`, embedded in `[0,1]ⁿ`, the radial coordinate is constant: `r²=n/4` for any state. At `n=3` this is exactly the cube radius `√¾` from 01 §7.2; here the fact is established for an arbitrary rank `[●]` (`verify §A`, `n=2…8`).

The radius decomposes exactly. Let `w` be the projection of the deviation from the center onto the diagonal `(1,…,1)` (the weight axis), `t` the remaining, transverse part. At the vertices

$$ r^2 = w^2 + t^2, \qquad t^2 = \frac{n}{4} - \frac{(H-n/2)^2}{n} , $$

where `H` is the number of ones in the state. The poles are purely axial (`t=0`); the maximum of the transverse falls on the middle layer — the Sperner slice, the "now" of document 02 (chapter VIII). The spectral limit of the core (Gaussian measure, document 02 chapter VII) covers the axial component `w`; the transverse `t` is not covered by it. This decomposition along the weight diagonal is distinct from the splitting of 01 §7.3: there the axis is set by the break of `κ` (the direction along which the symmetry is broken), here it is a fixed diagonal, present independently of any break.

## 2. The norm of the radius is forced

The distance from `σ½`, before it can be measured, requires a choice of norm. Among the `ℓ^p` exponents the parallelogram equality

$$ \|x+y\|^2+\|x-y\|^2 = 2\|x\|^2+2\|y\|^2 $$

holds uniquely at `p=2` (Jordan–von Neumann; document 03 §3.5 — the self-duality of the norm-body under Hölder conjugation). The radius is defined as the Euclidean distance `r(x) = ‖x−σ½‖₂` — by a theorem of the core, not by convention (`verify §B`).

## 3. The cone metric is forced

The requirement of chapter VII "at `r=0` — only `σ½`" is incompatible with the product metric `d² = d_angle² + Δr²`: at `r₁=r₂=0` it leaves distinguishable points with different angular coordinates. The consistent form is the cone metric,

$$ d^2 = r_1^2+r_2^2-2r_1r_2\cos\theta , $$

gluing the zero radius into a single point; over the round sphere it recovers flat space exactly (the law of cosines, `verify §C`). The observer is the apex of this cone.

## 4. Measure: the thin shell

The measure of the body is forced by monoidality (`Q_{m+n} = Q_m □ Q_n` gives a product of measures). Hence `E[r²]=n/12`, and the body concentrates in a shell of radius `√(n/12)` — the sphere of vertices lies exactly `√3` times farther (`(n/4)/(n/12)=3`). The neighborhood of the center is empty by measure: at `n=24` the fraction of volume closer than half the typical radius is indistinguishable from zero (`verify §D`). The observer is measurably inaccessible from within the body.

## 5. The radial flow

The dilation `δ_λ(y)=λy` from `σ½` commutes with `κ` and has, for `λ≠1`, a unique fixed point — `σ½`; on numbers it contracts toward `√N` and commutes with `d↦N/d` (`verify §E`). Terminality acquires a metric face: the canonical flow contracts everything toward the observer without additional operators.

## 6. The numerical realization

In the numerical model the radius of a divisor

$$ r(d) = \left|\ln\frac{d}{\sqrt N}\right| $$

is mirror-symmetric with respect to `κ` (`r(d)=r(N/d)`) and non-degenerate: for `N=30` the radii are distinct across the pairs — `{0.091, 0.602, 1.007}` (`verify §F`). The bit model keeps all states on a single sphere; the numerical one distributes distinct radii to them. The statement `Σ_p r(p)=ln√N` holds for three prime factors (`N=30`) and does not hold for two (`N=6`) or four (`N=210`) — a coincidence of rank 3, not a law (`verify §F`).

## 7. Two radii

The sides of the seam carry radial coordinates of different types. The discrete side: `|·|₂` on the addresses of states is an ultrametric (`verify §G`), its geometry is a tree growing from the initial object (the seed); the radius here is the depth of the first distinction, quantized by floors. This tree is distinct from the p-adic Bruhat–Tits trees of 01 §7.5, which are indexed by primes `p` and pertain to the places of `ℚ`, not to the bit addresses `Q_n`. The continuous side: `|·|∞` is not an ultrametric; its geometry is the cone of §3, contracted to `σ½`, the terminal.

The two ends of the category of document 02 (chapter V) — the initial object `∅` and the terminal `•` — are realized as two radial coordinates: the depth from the seed and the proximity to the observer `[◐]`. The product formula, read radially,

$$ \sum_v \ln|x|_v = 0 , $$

gives their balance: the outward radius of a number equals the sum of its depths inward across all p-adic trees (`verify §G`). The same formula in document 03 (§6.3) reads as the conservation law of the seam (what grew outward is compensated by what entered inward); the radial reading is the same form in the radial language.

## 8. Two curvatures

At the apex of the cone of §3 the angles between the directions from `σ½` carry a forced magnitude. Any two states adjacent in Hamming distance are seen from the center at a single angle `arccos((n−2)/n)` — a consequence of the sphere of §1 and the constant edge length (`verify §H`). A closed traversal of all states by Hamming-1 steps (a Gray cycle; every such cycle has `2ⁿ` edges, and its length does not depend on the choice of cycle) has from `σ½` an angular length

$$ L(n) = 2^n \arccos\frac{n-2}{n} . $$

At `n=1,2` the length equals `2π` — the states lay out flatly around the center. At `n≥3` the length exceeds `2π` and grows with rank: the cone over the scene carries at its apex an angular excess `[●]` (`verify §H`).

The apex magnitude is separated from the ray curvature of 01 §7.5 by commensurability. The angle `arccos((n−2)/n)` is a rational multiple of `π` exactly at `n∈{1,2,4}` (Niven's theorem: a rational cosine gives an angle commensurable with `π` only for the values `0, ±1/2, ±1`); at `n=3` the incommensurability is established by Dehn's lemma — `cos(kθ)=a_k/3^k` with a numerator not divisible by three (the same dihedral angle of the regular tetrahedron as in the solution of Hilbert's third problem). The angles of the ray axis `(2,3,p)` — `π/2, π/3, π/p` — are rational fractions of `π` for any `p`. The apex excess, forced by the skeleton, is not expressible rationally through the angles of the ray axis `[●]` (`verify §H`). The reverse side carries two layers of curvature: at the apex of the cone — a forced one `[●]`, along the ray — a free input `[○]` (01 §7.5).

## 9. The boundary

The form of the radial layer is forced entirely: the norm (§2), the metric of the zero point (§3), the shell law (§4), the dilation flow (§5), the dichotomy of tree and cone (§7), the apex excess (§8). The position of a state on the radius is an input `[○]`, of the same nature as the weights at the spin-functor of document 02 (chapter IX): the form of the spectrum is forced, the values are free. The wall of values specializes to the radial coordinate without remainder.

---

Verifier: `verify_radial_bridge.py` — 45 PASS, standard library.
