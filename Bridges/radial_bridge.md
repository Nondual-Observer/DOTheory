# Bridge: the radial layer — metric and measure around the seam

> A bridge between the underside (document 01, chapter VII), the categorical core (document 02, chapters V and VII), and the number model (document 03, chapters III and VI). Chapter VII already gives the radial coordinate partial form on the archimedean side of the seam: the sphere theorem for the cube and the octahedron at rank 3 (§7.2), the split into an axial and a radial part under the break of `κ` (§7.3), the axis of curvature `(2,3,p)` with Bruhat–Tits trees on the p-adic side (§7.5). This bridge examines a different layer of the same coordinate — the metric and measure-theoretic anatomy of the radius (norm, decomposition, concentration of measure, the metric of the zero point) and its discrete paired realization, separate from the p-adic trees of §7.5 — and generalizes the sphere theorem to arbitrary rank. The ray axis of curvature `(2,3,p)` is touched by a single statement — the separation theorem (§8). Everything computable is `verify_radial_bridge.py` (**45 PASS**). Register: constructions `[●]`, laws `[◐]`, external inputs and fronts `[○]`.

## Statuses

- `[●]` — all constructions: the budget `r²=w²+t²` on the skeleton of any rank, the forcedness of the `L²` norm (the parallelogram identity), the forcedness of the cone metric, the law of the thin shell and the measure-theoretic unreachability of `σ½`, the dilation flow `δ_λ`, the ultrametricity of the address radius, the product formula as a radial balance, the numerical realization `r(d)`, the angular excess at the apex of the cone and the separation theorem for the two curvatures (Dehn, Niven) — verifier.
- `[◐]` — laws: the two radii as a realization of the two ends of the category (seed/terminal); numbers and bits as the polar decomposition of the tuning fork (radius/angle).
- `[○]` — the position of a state on the radius (a value, not a form); any connection of the apex excess to the ray axis `(2,3,p)` beyond the proved separation.

---

## 1. Budget: weight and transverse

On the vertices of the carrier `Q_n`, embedded in `[0,1]ⁿ`, the radial coordinate is constant: `r²=n/4` for every state. At `n=3` this is exactly the cube's radius `√¾` from 01 §7.2; here the fact is established for arbitrary rank `[●]` (`verify §A`, `n=2…8`).

The radius decomposes exactly. Let `w` be the projection of the deviation from the center onto the diagonal `(1,…,1)` (the weight axis), and let `t` be the remaining, transverse part. On the vertices,

$$ r^2 = w^2 + t^2, \qquad t^2 = \frac{n}{4} - \frac{(H-n/2)^2}{n} , $$

where `H` is the number of ones in the state. Poles are purely axial (`t=0`); the transverse part is maximal on the middle layer — the Sperner slice, the "now" of document 02 (chapter VIII). The spectral limit of the core (the Gaussian measure, document 02 chapter VII) covers the axial component `w`; the transverse `t` is not covered by it. This decomposition along the weight diagonal is distinct from the split of 01 §7.3: there the axis is set by the break of `κ` (the direction along which symmetry is broken), while here it is a fixed diagonal, present independently of any break.

## 2. The norm of the radius is forced

Distance from `σ½`, before it can be measured, requires a choice of norm. Among the `ℓ^p` exponents, the parallelogram identity

$$ \|x+y\|^2+\|x-y\|^2 = 2\|x\|^2+2\|y\|^2 $$

holds uniquely at `p=2` (Jordan–von Neumann; document 03 §3.5 — the self-duality of the norm-body under Hölder conjugation). The radius is defined as the Euclidean distance `r(x) = ‖x−σ½‖₂` — a theorem of the core, not a convention (`verify §B`).

## 3. The cone metric is forced

Chapter VII's requirement that "at `r=0` there is only `σ½`" is incompatible with the product metric `d² = d_angle² + Δr²`: at `r₁=r₂=0` it leaves points with different angular coordinates distinguishable. The consistent form is the cone metric,

$$ d^2 = r_1^2+r_2^2-2r_1r_2\cos\theta , $$

which collapses zero radius to a single point; over a round sphere it recovers flat space exactly (the law of cosines, `verify §C`). The observer is the apex of this cone.

## 4. Measure: the thin shell

The measure of the body is forced by monoidality (`Q_{m+n} = Q_m □ Q_n` gives a product of measures). From this, `E[r²]=n/12`, and the body concentrates in a shell of radius `√(n/12)` — the sphere of vertices lies exactly `√3` times farther out (`(n/4)/(n/12)=3`). The neighborhood of the center is empty of measure: at `n=24` the fraction of volume closer than half the typical radius is indistinguishable from zero (`verify §D`). The observer is measure-theoretically unreachable from inside the body.

## 5. The radial flow

The dilation `δ_λ(y)=λy` from `σ½` commutes with `κ` and has, for `λ≠1`, a unique fixed point — `σ½`; on numbers it contracts toward `√N` and commutes with `d↦N/d` (`verify §E`). Terminality acquires a metric face: a single canonical flow contracts everything toward the observer, with no additional operators required.

## 6. Numerical realization

In the number model, the radius of a divisor,

$$ r(d) = \left|\ln\frac{d}{\sqrt N}\right| , $$

is mirror-symmetric under `κ` (`r(d)=r(N/d)`) and non-degenerate: for `N=30` the radii are distinct by pair — `{0.091, 0.602, 1.007}` (`verify §F`). The bit model holds all states on a single sphere; the number model assigns them distinct radii. The statement `Σ_p r(p)=ln√N` holds for three prime factors (`N=30`) and fails for two (`N=6`) or four (`N=210`) — a coincidence at rank 3, not a law (`verify §F`).

## 7. Two radii

The sides of the seam carry radial coordinates of different type. The discrete side: `|·|₂` on the addresses of states is an ultrametric (`verify §G`), whose geometry is a tree growing from the initial object, the seed; the radius here is the depth of first distinction, quantized by floor. This tree is distinct from the p-adic Bruhat–Tits trees of 01 §7.5, which are indexed by primes `p` and pertain to the places of `ℚ`, not to the bit addresses of `Q_n`. The continuous side: `|·|∞` is not an ultrametric; its geometry is the cone of §3, contracted toward `σ½`, the terminal.

The two ends of the category of document 02 (chapter V) — the initial object `∅` and the terminal `•` — are realized as two radial coordinates: depth from the seed and proximity to the observer `[◐]`. The product formula, read radially,

$$ \sum_v \ln|x|_v = 0 , $$

gives their balance: the outward radius of a number equals the sum of its depths inward across all p-adic trees (`verify §G`). The same formula in document 03 (§6.3) reads as the law of conservation of the seam (what grew outward is exactly compensated by what plunged inward); the radial reading is the same form in radial language.

## 8. Two curvatures

At the apex of the cone of §3, the angles between directions out of `σ½` carry a forced quantity. Any two Hamming-adjacent states are seen from the center under the same angle `arccos((n−2)/n)` — a consequence of the sphere of §1 and the constant edge length (`verify §H`). A closed tour of all states by Hamming-1 steps (a Gray cycle; every such cycle has `2ⁿ` edges, and its length does not depend on the choice of cycle) has, from `σ½`, the angular length

$$ L(n) = 2^n \arccos\frac{n-2}{n} . $$

At `n=1,2` the length equals `2π` — the states fit flatly around the center. At `n≥3` the length exceeds `2π` and grows with rank: the cone over the scene carries an angular excess at its apex `[●]` (`verify §H`).

The apex quantity is separated from the ray curvature of 01 §7.5 by commensurability. The angle `arccos((n−2)/n)` is a rational multiple of `π` exactly for `n∈{1,2,4}` (Niven's theorem: a rational cosine yields an angle commensurable with `π` only for the values `0, ±1/2, ±1`); at `n=3` the incommensurability is established by Dehn's lemma — `cos(kθ)=a_k/3^k` with numerator not divisible by three (the same dihedral angle of the regular tetrahedron as in the solution of Hilbert's third problem). The angles of the ray axis `(2,3,p)` — `π/2, π/3, π/p` — are rational multiples of `π` for every `p`. The apex excess, forced by the skeleton, is not rationally expressible through the angles of the ray axis `[●]` (`verify §H`). The underside carries two layers of curvature: at the apex of the cone — forced `[●]`; along the ray — free input `[○]` (01 §7.5).

## 9. Boundary

The form of the radial layer is forced throughout: the norm (§2), the metric of the zero point (§3), the shell law (§4), the dilation flow (§5), the dichotomy of tree and cone (§7), the apex excess (§8). The position of a state on the radius is input `[○]`, of the same nature as the weights of the spin functor of document 02 (chapter IX): the form of the spectrum is forced, the values are free. The wall of values specializes to the radial coordinate without remainder.

---

Verifier: `verify_radial_bridge.py` — 45 PASS, standard library.
