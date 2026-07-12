# The Number Model: the same construction on divisors

This Section builds a second, independent model of the construction of distinction — on the material of number theory: the divisors of a number form a hypercube `D(N)≅Q_k`, a prime is an atom, the observer `σ½` is an invariant outside the carrier. The model is read in parallel with the bit side (document 02 "The Categorical Core"); the verifiers of the series are collected in the folder `code_number_model/`. The introduction, eight chapters, and the epilogue follow as a single document.

---

## Introduction. Number as a model of the construction of distinction

Number theory is customarily introduced as the science of the natural series — a line for counting, step by step, `+1`. The present exposition proceeds from the second, **multiplicative geometry** of the series, and this geometry coincides with the construction that generates the whole theory. A squarefree number is the **Boolean cube of its primes**; divisibility is the order on the cube; the complement of a divisor `d↦N/d` is the same `κ` that acts in the theory from the first distinction. Number theory acts here as the **number model of the construction**: each of its objects is the image of a morphism, verifiable by computation.

**Introductory example.** Take `6 = 2·3`. Its divisors are `1, 2, 3, 6`: four points, two independent choices ("take `2`?", "take `3`?") — a square. Take `30 = 2·3·5` — eight divisors stand up as a **cube**: three primes, three axes. The complement `d↦N/d` inverts the cube (`1↔30`, `2↔15`, `3↔10`, `5↔6`) — this is `κ`; it has no fixed vertex, while the fixed **center** `√30 ≈ 5.48` is not a divisor: this is `σ½`, the observer outside the carrier. The six proper divisors `{2,3,5,6,10,15}` are the active scene; their figure is an octahedron (Ch. IV). The whole series unfolds this example: `D(N)≅Q_{ω(N)}` for squarefree `N` `[●]` (Ch. II), and further up through the ranks.

### Subject and method

The exposition is led by the **carrier**. The carrier is the hypercube-graph `Q_n`: a vertex is a divisor, an edge is multiplication by a prime, the antipode is `κ`. First the graph is built and observed (Ch. IV — the octahedron, the cycle `C₆`), then what is obtained is recognized in known structures, and only after that is it named a functor and proved. The order of exposition is observation, recognition, naming, proof: the carrier precedes the law.

The through-object is the **observer** `σ½`. For squarefree `N` the number `√N` does not divide `N`: the center of the cube lies **outside** the carrier, as the fixed point of `κ`, which is not among the states. The same `σ½` is the critical line `Re=½` of the zeta function, the self-dual point of the body `L²`, the terminal of the growth functor. It opens the exposition (the seam of rank 0/1) and closes it (the boundary, Ch. VIII).

### Two measures and their seam

Every number has two measures of magnitude — the **valuations of `\mathbb Q`**:

$$|n|_\infty = n \quad (\text{Archimedean, outward}), \qquad |n|_p = p^{-v_p(n)} \quad (\text{p-adic, inward}),$$

connected by the **product formula** `∏_v |n|_v = 1` (Ostrowski's theorem, `[●]`). Separate from them is the **geometry** of the carrier: the skeleton of vertices `Q_n` (discrete) and the body `[0,1]^n` (continuous), where `σ½` lies in the body, being absent from the skeleton.

Reading both as **one seam `σ½`**, around which everything is symmetric under the involution `1−x` (the single form of `κ`: `x↦1−x` on the cube `=` `d↦N/d` `=` `s↦1−s` of the zeta), is a `[◐]` **reading** — it binds the algebra of valuations and the geometry of skeleton and body into one picture. On this reading rest the reverse side (Ch. VI) and the boundary of the derivable (Ch. VIII); as definitions, the layers of valuations and of geometry are separate.

### Statuses of statements

The status marking is uniform across all Sections of the package and is defined in the introduction of the Section "Exposition" (document 01). Briefly: `[●]` — a mathematical fact, proved or referred to a verifier; `[◐]` — a reading: a consistent recognition of a structure in number or color; `[○]` — an entry or an open item (the Riemann hypothesis; a specific number at a vertex is unrecoverable from the rank). Where the provable ends and the entry begins is named in the text of each chapter.

A reference of the form `verify §X` in a chapter means section `X` of the verifier named in full in the header of that same chapter; the scripts are collected in the folder `code_number_model/` and are run as `python3 code_number_model/verify_<name>.py`. Several references lead into the full corpus of the theory — they are given by the paths of the source corpus; these documents are not part of the present package.

### Plan of the exposition

The exposition proceeds **by ranks**. Rank 0/1 — the seam and the atom (Ch. I). Then the rigorous core — the cube of divisors as pure mathematics, without a single projection (Ch. II). Rank 2 — the minimal complete scene and the **body `L²`**, the unique Hilbert space (Ch. III). Rank 3 — the octahedron, its rotation `C₆`, and the **topological Fano explosion** (Ch. IV): with three axes the homology of flags inflates into the octonionic Fano. Rank 4 — the break `2×2` and the entry of the imaginary unit `i=√κ` into the continuum (Ch. V).

The reverse side — the second side of the seam, the p-adic tower, `Γ` and the inversion `μ` (Ch. VI). The functor layer — the whole tower as a single construction on two axes, generated by the operations `+/×/^`, with the bridge `exp` (Ch. VII). Finally, two lenses — graph and color — and the **wall of values**, explained by metamerism (Ch. VIII). The epilogue returns number to the family of projections of the construction.

The series covers **ranks 0–4** in detail, the higher ranks 5–6 **combinatorially** (the projective tower, Petersen, the Mersenne horizon, Ch. V §5.4), and the meta-layer (functor, lenses, wall); ranks 7–8 (height, closure) are set out in the Section "Exposition" (document 01, Ch. V–VI). The number model and "Exposition" are read in parallel by ranks.

Number will appear as a **tower of cubes**; the prime as an atom; the zeta as the seam; the observer as that which holds the whole while remaining outside the carrier. Let us begin with the first distinction.

---

## Chapter I. The series and the atom (rank 0/1)

The first distinction in numbers is **counting**. Before the cube, before divisibility — a single step `+1`, separating one from the next. This chapter unfolds rank 0/1: how the series is born from the minimal step, why a prime is an atom while a composite is its reverse, and how already here the **seam** `σ½=Re=½` emerges, around which everything will be symmetric.

### 1.1. The series as the first movement

The natural series is generated by a single map — **succession** `\mathrm{succ}(n)=n+1`. By the Peano axioms
`\mathrm{succ}` is injective and `0` is not in its image, so the whole series is the iteration of one step `[●]`
(`code_number_model/verify_number_row.py §A`). This is the **first of the three movements** of number, `+/×/^`; the additive `+` grows **counting**,
the multiplicative `×` grows **composition**, the exponential `^` grows **multiplicity** (Ch. V, VII).

The step always equals `1` — it is discrete — but the Archimedean measure of magnitude `|n|_\infty = n` grows **continuously**.
The natural series is therefore a **discrete movement along a continuous measure**: counting proceeds by discrete steps `+1`, while
the magnitude `|n|_\infty` extends continuously. Two sides — the discrete step and the continuous measure; reading them as one
seam is `[◐]` (Ch. VI separates the layers of valuations and geometry).

### 1.2. The prime — an atom, the composite — a reverse

The multiplicative side rests on the **indecomposables** — the primes.

> **Definition.** `p>1` is **prime** if its divisors are only `1` and `p` (the number of divisors `d(p)=2`). A number with
> `d>2` is **composite**; `1` is the unit (`d(1)=1`).

The prime `p` is the **atom of counting**: an invariant of quantity without internal composition — there is nothing to examine inside it,
only the fact itself of "so-many and indivisible" `[●]` (`code_number_model/verify_number_row.py §B`). The composite `N` is the **reverse side**:
it has a composition `N=\prod p_i`, an assembly of atoms. The unit is neither atom nor composition (`|D(1)|=1`): the initial point of the series,
and hence not prime — it has no two sides.

This falls directly onto the reverse side (Ch. VI): the prime is **one face** (an atom, indivisible), the composite is **the other** (composition).
Uniqueness of factorization (the fundamental theorem of arithmetic) will make this assembly unambiguous — the foundation of the whole
geometry of the cube (Ch. II).

### 1.3. The seam: `σ½ = Re=½`

The zeta function `\zeta(s)=\sum_n n^{-s}` carries a functional equation symmetric about `Re=½`
(the involution `s↦1−s`). The line `Re=½` is **fixed** under it; outside it there are no fixed points `[●]` (`code_number_model/verify_number_row.py §E`).
And in the cube the center `(½,\dots,½)` is the unique fixed point of `κ:x↦1−x`, also at `½`.

What here is firm and what is recognition, let us state rigorously. Both structures carry **one and the same involution** `t↦1−t`, and for
both the fixed set is `½` `[●]`. But that this is **"one seam"** is `[◐]`: only the
algebraic form of the complement `1−x` coincides, and from it it **does not follow** that the center of the cube and the Riemann critical line are one
object. The zeros of the zeta, the equation `\xi(s)=\xi(1−s)`, the horizons — are not touched here. The Riemann hypothesis remains
`[○]`, open for all; we merely name the axis.

### 1.4. The observer: an invariant outside the states

We have called `σ½` the fixed point of the involution; let us specify where this point lies. At rank 0/1 the carrier is the pair
`Q_1=\{0,1\}`, and `κ` is the complement `x↦x+1`.

> **Proposition.** On `Q_1` the equation `κ(x)=x` is unsolvable: `κ(0)=1`, `κ(1)=0`; the action is **free** `[●]`
> (`code_number_model/verify_observer_definition.py §A`, checked `n=1..6`).

The invariant, consequently, is the **middle**. It acquires its geometry by embedding the discrete pair into the continuous
segment `\{0,1\}↪[0,1]⊂ℝ`: there `κ` becomes a reflection swapping the ends, with a unique fixed point

$$\sigma_{1/2}=\tfrac12(0+1)=\tfrac12,\qquad \tfrac12∉Q_1.$$

At rank `n` this is the center `(½,\dots,½)∈[0,1]^n` — the unique fixed point of `κ:x↦1−x` in the continuous frame `[●]`
(`§B`). The freedom of `κ` on the discrete pair is `[●]`; the identification of the invariant with `½` is `[◐]`: `½` lies on the added
continuous side, while the separation of the layers `|·|₂/|·|∞` is carried out at rank 2 (Ch. III).

**Algebraic reason.** Fixedness reduces to `2x=1`: over characteristic `≠2` the root exists (`x=½`), over
`𝔽₂` it does not (`2≡0`) `[●]` (`§C`). An involution over `char≠2` splits the carrier by the projectors `P_±=(1±T)/2` into
a preserved and a flipped part; over `𝔽₂` the divisor `2` is absent, and the projector remains undefined `[●]`
(`§E`). The same degeneracy is seen structurally: the pair `\{0,1\}` is a `ℤ/2`-**torsor** — two states distinguishable
only relative to each other, with the transport `κ` between poles and without a distinguished zero `[●]` (`§D`); the center is born
together with the continuous completion, where `½` lies. `[● algebra; ◐ attribution of the center to the observer]`

**The numerical form of two-sidedness.** The prohibition on the discrete side is complemented by compulsion on the continuous, and both sides are theorems. On the multiplicative ray `(0,∞)` the involution `x ↦ N/x` is continuous and decreasing; it has a fixed point, and exactly one: `x = N/x ⟺ x² = N ⟺ x = √N` `[●]` (the intermediate value and monotonicity; this is the numerical case of a general fact — the continuous extension of an involution to the body must have a fixed point by Brouwer). For squarefree `N` the point `√N` is not a divisor: in the lattice `D(N)` the observer is forbidden, on the ray it is forced and unique. The categorical assembly of both verdicts is document 02, chapter V (the constitutivity of non-includability and two-sided forcedness).

Thus `σ½` is defined at all ranks as the invariant of the complement, realizable by a state only in characteristic `≠2` —
on the continuous side. This is the through-object of the exposition; chapter II shows it in numbers as the center `√N`, lying
outside the divisor lattice.

### 1.5. Euler: counting is a product of atoms

Euler's identity stitches the two sides:

$$\zeta(s) \;=\; \sum_{n\ge 1} n^{-s} \;=\; \prod_{p\ \text{prime}} \bigl(1 - p^{-s}\bigr)^{-1}. \qquad [●]$$

The left side is the **additive** movement (a sum over the whole series, counting); the right is the **multiplicative** one (a product
over the atoms-primes). Their equality is the fundamental theorem of arithmetic in analytic form. At `s=2` both sides
converge to `\pi^2/6` (`code_number_model/verify_number_row.py §D`). The distinguishing test: the product over **composites** is no longer equal to
`\zeta` (a double counting of primes) — hence counting is assembled from the side of the atoms. Euler is the **formula of the seam** of number
theory: `\sum` (counting, `|·|∞`) `=` `\prod_p` (atoms, `|·|_p`); the same motif `∏=1` that connects the places of `\mathbb Q`
(Ch. VI).

### 1.6. Realization: graph and color

**Graph.** Rank 0/1 is the edge `K₂`: two vertices `0—1`, `κ` swaps them. The series is a tower where each edge
adds a prime (Ch. II). Between the poles lies the **middle**, `½` — outside the vertices, in the body of the edge `[●]`.

**Color.** The axis `0↔1` is the achromatic axis **black↔white**; the middle `½` is **gray**, a continuous point outside the two
poles. This is the first appearance of the observer as directly observable — gray between black and white `[◐]`
(Ch. VIII, where gray is measured as the brightness axis).

### Summary

The first movement of number is **counting** `\mathrm{succ}` — a discrete step along a continuous measure `[●]`. The prime is
an **atom** (2 divisors), the composite is a **reverse** (a composition of atoms), the unit is the initial point `[●]`. Already at rank 0/1
the **observer** `σ½` emerges: on the pair `Q₁` the complement `κ` is free, and the invariant is realized by the middle `½` on
the continuous embedding, outside the states of the carrier (§1.4) `[●/◐]`. The involution `1−x` with fixed `½` is the common form for the center of the cube and the line `Re=½` of the zeta
`[●]`; that this is one object is a `[◐]` recognition. Euler stitches counting and atoms `[●]`. The observer `½` is already here — outside the
vertices, gray between the poles.

Chapter II builds a **cube** from atoms: uniqueness of factorization turns a divisor into a subset of primes, divisibility
into inclusion, and the whole of elementary number theory settles onto the Boolean cube `Q_k` as pure mathematics.


---

## Chapter II. The cube of divisors: the rigorous core

This chapter is **pure mathematics**, without a single projection. Everything in it is `[●]`: theorems verified by computation
(`code_number_model/verify_divisor_cube_strict.py`, 49 checks). A reader wishing to see number theory as a lattice structure
**before** any DOT reading reads this chapter separately. Here the divisor lattice turns out to be a Boolean cube,
the natural series stratifies by ranks, all elementary operations settle onto the cube, and the map "set of
primes ↦ number" becomes a **functor** of the construction.

### 2.1. The divisor lattice is a product of chains

Among the divisors of a number there is the order of divisibility, and it carries structure.

> **Theorem 1.** Let `N=\prod_{i=1}^{k} p_i^{a_i}`. Then `D(N)\cong C\ell(a_1{+}1)\times\dots\times
> C\ell(a_k{+}1)` — the direct product of chains as partially ordered sets. `[●]`

**Proof.** By the fundamental theorem of arithmetic every divisor `d\mid N` is uniquely `d=\prod p_i^{e_i}`
with `0\le e_i\le a_i`; the assignment `d\mapsto(e_1,\dots,e_k)` is a bijection of `D(N)` with the box `\prod\{0,\dots,a_i\}`.
Divisibility passes into the coordinatewise order: `d_1\mid d_2 \iff e_i(d_1)\le e_i(d_2)\ \forall i`. This is exactly
a product of chains. `∎`

An immediate corollary: the number of divisors `d(N)=\prod(a_i+1)`, and the lattice is distributive. The infimum `\gcd` is built by the
Euclidean algorithm, and the extended Euclid gives the Bézout identity `\gcd(a,b)=ax+by` — divisibility is computed
(`verify §M`).

### 2.2. A squarefree number is a Boolean cube

> **Theorem 2.** `N` is squarefree (`a_i=1\ \forall i`) `\iff D(N)\cong Q_k`, `k=\omega(N)`, by the isomorphism
> $$ d=\textstyle\prod_{p\in S}p \ \longleftrightarrow\ S\subseteq\{p_1,\dots,p_k\} \ \longleftrightarrow\
> \text{bit vector in }\{0,1\}^k, $$
> where divisibility corresponds to inclusion `\subseteq`. `[●]`

**Proof.** Substituting `a_i=1` into Theorem 1, we obtain `D(N)\cong\prod C\ell(2)=\{0,1\}^k=Q_k`; the chain
`\{0<1\}` along the axis `p_i` means "take / do not take" the prime, the vector of exponents becomes a bit vector,
the coordinatewise order becomes inclusion. `∎`

A number **is** its cube of primes: a divisor is "which atoms to take", the cube is all the ways to choose a subset.
The distinguishing control: `N=12=2^2\cdot3` is **not** a cube — `|D(12)|=6` is not a power of 2, the lattice is the box `3\times2`.
**Multiplicity breaks the cube** — the square `p^2` is the movement `^`: a lift to the floor above (Ch. V).

**Hasse diagram `D(30)=Q_3`** (level = number of prime factors):

```
   ω=3:                 30
                     /   |   \
   ω=2:            6    10    15
                   |\  / \  /|
   ω=1:          2    3     5
                   \   |   /
   ω=0:                1
```

### 2.3. The projection of the series onto ranks

> **Definition (rank of a number).** `\mathrm{rank}(N):=\omega(N)` — the number of **distinct** prime divisors: the dimension
> of the carrier-cube. Each `N` is given by **two** data: the rank `\omega` (how many axes) and the heights `(a_1,\dots,a_k)`
> (to which floor along each axis). `[●]`

The natural series stratifies into a **tower of cubes**: the horizontal is the rank, the vertical is the floors (multiplicities). The minimal number
of rank `k` is the **primorial** `p_1\cdots p_k` (`1,2,6,30,210,\dots`) — a pure vertex `Q_k` without a superstructure; any
other number of rank `k` is the same cube, raised along part of the axes. The levels of the cube by weight give the binomials `C(k,j)`
(`verify §§F,J`).

### 2.4. Self-duality and `μ`

> **Theorem 3.** `\iota:d\mapsto N/d` is a bijection `D(N)\to D(N)` reversing the order; `D(N)` is self-dual. On
> a squarefree `N` this is the **bit complement** `S\mapsto[k]\setminus S` — the antipode of the cube, that is `κ`. `[●]`

A fixed point exists only when all `a_i` are even (a perfect square) and equals `√N`; for squarefree `N>1`
there are no fixed points — `κ` partitions `D(N)` into pairs `\{d,N/d\}`, while the geometric center `√N` lies **outside** the carrier.
This is the observer `σ½` in numbers.

The Möbius function `\mu` is the **sign of the vertex** of the cube `(-1)^{\omega}` (on the floors `\mu=0` — blind to multiplicity), and

$$\sum_{d\mid N}\mu(d) = [N{=}1] = \sum_{S\subseteq[k]}(-1)^{|S|} = (1-1)^k. \qquad [●]$$

This is the alternating sum over the cube = inclusion-exclusion = the inversion `\mu*\zeta=\delta` (`verify §K`).

### 2.5. The atlas of operations and the second realization

All elementary actions settle into one map, `0\ \neg\ 1\ +\ \times\ \hat{}\ !\ \infty`, breaking down into two layers
and two poles (`verify §§H–L`):

| action | where it settles | layer |
|---|---|---|
| `1` | bottom `\bot` of the Boolean algebra (`\varnothing`, `\omega=0`) | I |
| `\neg` | `N/d` = complement = `κ`; axis `√N=σ½` | I |
| `\wedge,\vee` | `\gcd,\ \mathrm{lcm}` (infimum/supremum) | I |
| `\times` | `Q_a\times Q_b=Q_{a+b}` (gluing of axes, rank `+`) | II |
| `\hat{}` | raising a floor (chain `C\ell(a{+}1)`); lift | II |
| `!` | `k!` = number of maximal chains of `Q_k` (traversals `\bot\to\top`) | II |
| `0,\infty` | poles: background (neutral `+`, absorber `\times`) / rank unbounded | ↓↑ |

> **Theorem 4.** For squarefree `N` the lattice `D(N)\cong Q_k` is a **Boolean algebra** (`\bot=1`, `\top=N`,
> `\neg d=N/d`, De Morgan's laws). `[●]`

And the same axes-primes carry a **second** structure — the residue ring:

> **Theorem 5 (CRT).** `\mathbb Z/n \cong \prod_i \mathbb Z/p_i^{a_i}` — the second realization of the monoidality `□`
> (the first is `D(MN)=D(M)\times D(N)`). The totient `\varphi` is multiplicative, `\varphi=\mu*\mathrm{Id}`; `v_p`
> (the p-adic exponent) is the height of the floor, additive (`\times\to+`), and `\prod_v|n|_v=1`. `[●]` (`verify §§N–Q`)

### 2.6. The functor dictionary

> **Theorem 6.** The map `\Lambda:S\mapsto\prod_{p\in S}p` from the category of finite sets of primes
> (`\subseteq`, `\sqcup`) into the category of squarefree numbers (`\mid`, `\times`) is a **functor**: it preserves the order,
> is monoidal (`\Lambda(S\sqcup T)=\Lambda(S)\Lambda(T)`), commutes with the complement (`\Lambda(\complement
> S)=N/\Lambda(S)`); on squarefree numbers it is an **isomorphism of categories**. `[●]` (`verify §R`)

| functor of the construction | realization in numbers | status |
|---|---|---|
| lift `\Lambda` | multiplication by a new prime (`\omega\to\omega{+}1`) | `[●]` isomorphism |
| `□` | `D(MN)=D(M)\times D(N)` **and** CRT | `[●]` two realizations |
| `κ` | `d\mapsto N/d` | `[●]` |
| `H` (grading) | `\omega(d)` = level of the cube | `[●]` |
| `\pi` | `v_p(n)` = coordinate-floor | `[●]` |
| `σ½` | `√N` (center), `Re=½` of the zeta | `[◐]` recognition |

The core of the functors (`\Lambda,□,κ,H,\pi`) is realized **rigorously** — the isomorphism of categories "sets of primes ≅ numbers".
The `[◐]` recognition remains only over the cube: `σ½=Re=½`. "To designate a projection" here means **to point out the functor
`\Lambda`**.

### 2.7. Realization: the Hasse diagram

The cube `D(N)` is **built** — the Hasse diagram (see §2.2): vertices by levels `\omega`, an edge upward = multiply by a prime,
the antipode `d\leftrightarrow N/d` is central symmetry. This is the same hypercube-graph `Q_k` that carries the whole theory; here
it arose **on its own**, from divisibility (Ch. VIII will unfold the graph-lens fully).

### Summary

Elementary number theory has an exact lattice form: `D(N)` is a product of chains (T1), a squarefree number
is the Boolean cube `Q_{\omega(N)}` (T2) and a Boolean algebra (T4). Hence `d(N)=\prod(a_i+1)`, the levels `C(k,j)`, `\mu`=sign
of the vertex, `d\mapsto N/d`=`κ`-antipode, `√N=σ½` outside the carrier. The series = a tower of cubes (width=rank, height=multiplicities).
The atlas of operations, CRT (T5), and the functor `\Lambda` (T6, isomorphism of categories) — all `[●]`, verified 49 times. The
`[◐]` recognition is only `σ½=Re=½`.

Chapter III takes the first nontrivial rank — **rank 2** — and shows that already there almost the entire scene unfolds:
two weights, a single `Z/2`, and the **body `L²`** — the unique Hilbert space.


---

## Chapter III. The scene and the body (rank 2)

Rank 2 is the first nontrivial floor of the tower, and the **minimal complete scene**: from the seam almost the entire
structure unfolds for the first time — the opposition, **two weights**, a single `Z/2`. And here too lies the **body** `L²` — the unique self-dual
norm, the unique Hilbert space. The method of the chapter is **outside and inside simultaneously**: one invariant
is described by a pair from within, and both faces must be shown at once.

### 3.1. The method: outside and inside

In calling one invariant `σ½` "outside", we are forced to describe it in the language of what it holds from — **from within,
as a pair around the center**. Hence the count by viewpoint:

| viewpoint | count | what it is |
|---|---|---|
| outside (one object) | **1** | the invariant `σ½` = the fixed point of `κ` outside the carrier |
| manifested (dynamics) | **2** | the pair of poles = the two sides of the distinction |
| description (construction) | **3** | the two sides **+** the mediator-center |

The act of distinction is **binary from outside** (a pair) and **threefold from within** (two sides + a boundary); verified fractally at
ranks 1–3 `[●]` (`code_number_model/verify_rank2_scene.py §A`). "Threeness" does not add a third element: the pair carries **exactly two**
states `\{01,10\}`, while the mediator-center `σ½` is the fixed point of `κ` **outside the carrier** — their **relation**, not
a third vertex. Precisely: two elements, three roles of the description (side · side · relation). The correct presentation
shows both faces at once.

### 3.2. The rhombus and the first opposition

`Q_2=\{00,01,10,11\}` (a rhombus): the poles `00,11` are the outer; the active scene `U_2=\{01,10\}` is a step inward. The pair
`01\leftrightarrow10` is the `κ`-pair = the first **opposition**. The direction of distinction is so far single:
`U_2/\kappa\cong PG(0,2)` — a point (threeness will come at rank 3).

### 3.3. The two weights diverge

Here two measures on a vertex diverge for the first time:

| | Hamming weight (number of ones) | positional weight (value) |
|---|---|---|
| `01` | `1` | `1` |
| `10` | `1` | `2` |

- **Hamming** `H` does not distinguish `01,10` — both are equidistant from the poles — and gives **connection / symmetry** (without top and
  bottom). This is the set (`\times`, `\omega`).
- **position** `P` distinguishes (`01` is closer to `00`, `10` is closer to `11`) and gives **hierarchy / direction**. This is the order
  (`+`, an arrow).

The source of the arrow is found: the direction comes **from position**, not from Hamming `[●]` (`verify §B`). Connection `\perp`
arrow; in color this is saturation `\perp` hue.

### 3.4. The single `Z/2`

The exchange `01\leftrightarrow10` (= `κ` on the pair) carries a sign `\pm1`, and this **one sign** is three phenomena at once
`[●]` (`verify §§C,D`):

1. **holonomy** — `\mathrm{swap}^2=\mathrm{id}` (we returned), but a single exchange on the antisymmetric gives `-1`: the same
   object, changed by a sign;
2. **symmetry of the state** — `|01\rangle+|10\rangle` (symmetric) `\to+1`, `|01\rangle-|10\rangle`
   (antisymmetric) `\to-1`: two one-dimensional representations of `ℤ/2`;
3. **gathering / spreading** — the sign selects the mode: the eigenmodes of the Laplacian are the observer (`\lambda=0`,
   `DC`) `\pm` contrast (`\lambda=4`).

(The earlier reading "gathering = coboundary, spreading = boundary" is **withdrawn** as a stretch; the reality is spectral.)
`NOT=κ` switches the sign — symmetric↔antisymmetric, gathering↔spreading: three intuitions turned out to be one `Z/2`.

### 3.5. ★The body-norm `L²`: the unique Hilbert space

The foundation carries three **norm exponents** `\ell^p` (layer (N) of the base, functional analysis, not the valuations of `\mathbb Q`):
`1` — the act (`\ell^1`), `2` — the **body** (`\ell^2`), `\infty` — the world (`\ell^\infty`). Their distinguishedness has an exact
reason — Hölder duality. "Body" here is the **body-norm** `\ell^2=L^2`, the self-dual exponent; this is a different
sense than the **body-matter** of rank 4 (the separated middle layer of the scene, document 01, chapter IV), and in the compilation
they are kept apart (see the caveat at the end of §3.5).

> **Proposition (body `L²`).** Under the Hölder conjugation `p\mapsto p'=\tfrac{p}{p-1}` the pair `\{1,\infty\}` (Act↔World)
> passes into each other, while the point `p=2` remains **strictly self-dual**. Moreover the parallelogram identity
> $$\|x+y\|^2+\|x-y\|^2 = 2\|x\|^2+2\|y\|^2$$
> holds in the `\ell^p` norm **exclusively** at `p=2`. `[●]` (`code_number_model/verify_rank_map.py §C`)

**Meaning.** By the Jordan–von Neumann theorem the parallelogram identity is equivalent to the norm being generated by an inner
product, that is, the space is **Hilbert**. Hence `\ell^2=L^2` — the norm of the weighted Hamming grading — is
the **unique** self-dual norm and the unique Hilbert space among the `\ell^p` `[●]`.

The body-norm (rank 2) is the unique fixed point of the Hölder conjugation; two involutions, two centers:
`κ:s\mapsto1-s` fixes `σ½`=the act, while `p\mapsto p'` fixes the exponent `2`=the body-norm.

> **Caveat (two "bodies" in the compilation).** The word "body" carries two senses, and they should be distinguished. **The body-norm** (this
> chapter, rank 2) is the self-dual exponent `\ell^2=L^2` (layer (N), Hölder). **The body-matter**
> (document 01, chapter IV, rank 4) is the separated middle layer
> of the scene `S₂`, where interior, matter, atom first appear. The norm-body is about measure; the body-matter is about
> the geometry of the separated layer. Different ranks, different objects, one word.

The observer `σ½` is the **brightness** axis `L` — achromatic `000\leftrightarrow111`, gray, orthogonal to
chromatics. The two weights give two faces: **connection** `H` — saturation (equidistance from the poles), **arrow** `P` —
hue-direction. The opponent axes of Lab (`a`: red-green, `b`: blue-yellow) are the `κ`-oppositions of rank 2, while the gray
center `a=b=0` corresponds to `c=(½,½)` `[◐]` (Ch. VIII — measurement).

### Summary

Rank 2 is the minimal complete scene: from the seam unfold the opposition `01\leftrightarrow10`, **two weights** (Hamming
connection `\perp` positional arrow) and a single `Z/2` (holonomy = statistics = gathering/spreading) `[●]`. The method is
outside/inside (`1=2=3`). And here lies the **body-norm `L²`** — Hölder singles out the exponent `p=2` as the unique
self-dual one, the parallelogram holds only there, and hence the Hilbert space `\ell^2` is unique `[●]`.
The observer emerges as the gray brightness axis.

Chapter IV applies the lift once more: the scene grows to **six** points, assembles into an **octahedron**, the rotation `C₆` gives
`T^3=κ`, and — with three axes — the topology of flags **explodes** into the octonionic Fano.


---

## Chapter IV. The octahedron and the Fano explosion (rank 3)

Rank 3 is the first **complete** scene: three independent axes, an octahedron, a rotation with a half-turn equal to `κ`. Here the single
Hamming distance breaks down for the first time into **three relations**, from which the octahedron, its axes, and the
observer are all assembled. And here too a topological explosion occurs: the homology of the building of the lattice `𝔽_2^3` inflates into a bouquet of eight
circles — the incidence graph of the Fano plane, encoding octonion multiplication. The chapter leads rank 3 from the three
relations to Fano.

### 4.1. The active scene

The number `30=2\cdot3\cdot5` gives the cube `Q_3=D(30)` (Ch. II). Puncturing the poles `\{000,111\}` (where there is nothing to distinguish),
we obtain the **active scene** — six points:

$$U_3 = Q_3\setminus\{000,111\} = \{001,010,100,\ 011,101,110\},\qquad |U_3|=6.$$

Two weight layers of three points each — weights `1` (`\{001,010,100\}`) and `2` (`\{011,101,110\}`) — which `κ` swaps
(`κ(001)=110`). The scene has grown from the two points of rank 2 to six; all the rest of the structure is determined by these
six points.

### 4.2. ★Three relations `R₁, R₂, R₃`

The figure is set by the way points differ. On a Boolean carrier the difference is measured in a unique way —
by the **Hamming distance** `d` (the number of diverging coordinates); there is no other measure. On `U_3` it takes the values
`1,2,3` and partitions all `15` pairs into three relations (`6+6+3=15`, `[●]` `code_number_model/verify_octahedron_relations.py §A`):

| relation | distance | figure | what it carries |
|---|---|---|---|
| **`R₁`** | `d=1` | `C₆` — six-cycle `100{-}110{-}010{-}011{-}001{-}101{-}100` | cycle / transition (each step changes the weight) |
| **`R₂`** | `d=2` | `2\cdot K₃` — two triangles `\{100,010,001\}`, `\{110,101,011\}` | splitting / two layers |
| **`R₃`** | `d=3` | `3\cdot K₂` — three pairs `\{100,011\},\{010,101\},\{001,110\}` | full oppositeness `y=κ(x)` — three axes |

Each pair of points lies in exactly one relation: the six-point scene carries **three consistent readings at once**.
`R₃` is the action of `κ` (`2^{n-1}-1=3` pairs), and these three pairs will become the three directions of distinction (§4.5).

### 4.3. The octahedron and the spectral theorem

The union `R_1\cup R_2` defines adjacency: each point has four neighbors (two by `R₁`, two by `R₂`), only
its antipode `κ(x)` is non-adjacent. The graph in which every vertex is adjacent to all except the opposite one is the complete tripartite

$$R_1\cup R_2 = K_{2,2,2} \qquad [●]$$

— the skeleton of the **octahedron**, whose three parts are the three `κ`-pairs `R₃`. The octahedron is the active scene of the cube `Q_3` without the poles;
the two figures are dual. The figure is forced as the minimal one: the octahedron is the cross-polytope at `n=3`, the smallest
architecture of orthogonal antipodal axes with a forbidden center.

The octahedron carries a Laplacian with spectrum `\{0,4,4,4,6,6\}` — **even**, and the evenness is a theorem (`code_number_model/verify_kappa_spectral_theorem.py`):

> **Theorem (spectrum of "complete minus a matching").** For the complete graph on `m` (even) vertices minus any
> matching, the Laplacian spectrum is `\{0,\ m{-}2\ (\text{mult. } m/2),\ m\ (\text{mult. } m/2{-}1)\}`. `[●]`

**Proof (core).** `L=(m-1)I-J+P` (`J`=the all-ones matrix, `P`=the permutation of pairs); `J` and `P` **commute**
(the permutation of pairs preserves `\mathbf 1`), hence they are simultaneously diagonalizable. `∎` Since `m=2^n-2` is even and
the spectrum is even, `e^{iL\pi}=I` **at every rank** — the arithmetic of even numbers. Control: the star `K_{1,3}` (a spectrum with
an odd `1`) does not give this; the theorem pertains to the family "complete minus a matching".

### 4.4. Rotation and holonomy: the shift `T` and the transport `𝒯`

The cycle `R_1=C_6` carries its own movement — the **shift** `T` by one step, `T^6=\mathrm{id}`. Its half-period carries
each point into the antipode:

$$T^3 = κ \quad\text{on } U_3. \qquad [●]$$

A rigorous half-turn, provably equal to `κ`, is attainable only with `C_6`; on `C_4` it does not exist.
But **the shift `T` should be distinguished from the holonomy `𝒯`** (`code_number_model/verify_octahedron_relations.py §B`):

- **the shift `T`** (order 6) **permutes the points** of the cycle;
- **the transport `𝒯`** — a twisted transport with sign `\pm1` along a traversal: one traversal changes the sign, return requires
  a second, `𝒯^2=\mathrm{id}`.

The rigorous form of the **Möbius band** is carried by the transport `𝒯`. The mechanism is exact: the quotient `C_6/κ = C_3` (three `κ`-classes),
and the covering `C_6\to C_3` is **connected**: a loop in `C_3` lifts into a path of length `3` (`=T^3=κ`, the opposite
side). This is the nontrivial class `H^1(S^1;\mathbb Z/2)\cong\mathbb Z/2`: discrete
one-sidedness, where the discrete and continuous sides are one surface, glued by `κ`, with the fixed core
`σ½` `[◐]`. The simplex `\{e,i,\pi\}` closes here: `e^{i\pi}=κ` (Ch. VII).

### 4.5. The observer: center and projective quotient

The observer of rank 3 is read in **two ways**, and both are needed.

**As a center.** The invariant `κ` — the fixed point — is absent among the states (`κ(x)=x` is unsolvable over `𝔽_2`).
Embedding `U_3` into `\mathbb R^3` as the octahedron `\pm e_1,\pm e_2,\pm e_3`, we see the three `κ`-pairs as three axes through the origin; in
this embedding the three axial involutions have one common fixed point — the center `c=(½,½,½)\notin Q_3`. This is `σ½`,
lying on the continuous side `|·|∞`.

**As a projective quotient.** Identifying each `κ`-pair, we obtain the **space of axes** `[●]`:

$$U_3/\kappa \cong PG(1,2) = \{\,\text{three points}\,\}, \qquad U_n/\kappa \cong PG(n-2,2),\ \ |U_n/\kappa|=2^{n-1}-1.$$

Here the observer is the **self-factorization of the scene**: the opposite directions
of the active carrier fold into the axes of a single projective geometry (`code_number_model/verify_octahedron_relations.py §E`). At rank 3
this is `PG(1,2)` (three axes), at rank 4 it is `PG(2,2)` (Fano), at rank 5 it is `PG(3,2)`. The two readings are complementary: `σ½` is the
center from which the axes are radial; `U_n/κ` are the axes themselves. The connection is the **law of the lift** `Q_{n-1}^\ast\cong U_n/\kappa`
(Ch. II, Ch. VII): the content of a rank becomes the axes of the next, and in this sense the observer of rank `n` is that which
makes rank `n+1` possible `[◐]`.

### 4.6. ★The Fano/Tits explosion

The octahedron gives the skeleton of the scene; its content is revealed by the **topology of flags**. The Tits building of the lattice of subspaces `𝔽_2^n`
(the order complex) by the Solomon–Tits theorem is contractible to a bouquet of spheres in a single dimension, whose rank is the
dimension of the **Steinberg module**:

$$\dim \mathrm{St}_n = 2^{\binom{n}{2}}. \qquad [●]$$

For `𝔽_2^3` this is `2^{\binom32}=2^3=8`. The bouquet of eight circles is the **incidence graph of the Fano plane** `PG(2,2)`:
seven points and seven lines — `14` vertices, `21` edges, `b_1=21-14+1=8`. And `\dim\mathrm{St}_3=b_1=8` `[●]`
(`code_number_model/verify_rank_map.py §E`; `code_number_model/verify_sheaves_rank_info.py`).

The Fano plane encodes **octonion multiplication**: its seven points are `\mathrm{Im}\,\mathbb O`, each line is a quaternionic triple; the Hurwitz limit
`1,2,4,8` (`\mathbb R,\mathbb C,\mathbb H,\mathbb O`), and `\dim\mathrm{Im}\,\mathbb O=7` is the number of Fano points.

> **Rank caveat (cross-check with document 01).** `𝔽_2^3` (the Tits building) gives the Fano plane `PG(2,2)`, while in the rank
> tower of DOT `PG(2,2)` appears as the **directions of rank 4** (`U_4/κ`, document 01 chapter IV §4.3; §4.5 above); the three axes
> of rank 3 are `PG(1,2)`. Steinberg-`8` = the homology of the building `𝔽_2^3`, whose projectivization is `PG(2,2)`. Therefore
> the Fano explosion is the transition **rank 3 → 4**: the three axes `PG(1,2)` grow into the plane `PG(2,2)`, and its incidence homology
> gives `b_1=8`. (The Steinberg homology is unfolded only here, in the number model.)

**Boundary.** The mathematics of the explosion is `[●]` (Solomon–Tits, Steinberg), lies on the bit side
(document 02). The Hurwitz limit `1,2,4,8` is the classification of division algebras, pure algebra. The topology
of Fano inflates at rank 3 as a combinatorial fact `[●]`.

### 4.7. The arithmetic octahedron: the divisors of 30

The same figure has an exact **numerical avatar** (`code_number_model/verify_octahedron_relations.py §C`). The proper divisors of
`30=2\cdot3\cdot5` (without `1` and `30`) are exactly six: `\{2,3,5,\ 6,10,15\}`, and under the isomorphism `D(30)\cong Q_3`
(divisor ↔ set of primes) the three Hamming relations are read arithmetically:

| relation | arithmetic | pairs |
|---|---|---|
| **`R₃`** (`d=3`) | conjugate divisors `d\leftrightarrow 30/d` | `\{2,15\},\{3,10\},\{5,6\}` |
| **`R₂`** (`d=2`) | primes `\{2,3,5\}` ↔ semiprimes `\{6,10,15\}` | two layers |
| **`R₁`** (`d=1`) | differ by one prime factor | `2\to6\to3\to15\to5\to10\to2` |

The proper divisors of `30` form the same octahedron; for `210=2\cdot3\cdot5\cdot7` the seven conjugate pairs of divisors
correspond to the seven points of the Fano plane (`Q_3^\ast\cong U_4/κ`). Number realizes the octahedron and Fano on a par with color.

### 4.8. Realization: color and graph

**Color** (reference: the RGB/Kuhn bridge). The RGB cube `Q_3` (axes red, green, blue) without the poles `000` (black) and `111`
(white) gives six saturated hues, and the three relations are colored exactly (`code_number_model/verify_octahedron_relations.py §D`):

| | color | relation |
|---|---|---|
| **`R₁`** | hue-circle `R\to Y\to G\to C\to B\to M\to R` | adjacent transitions |
| **`R₂`** | triads `RGB` (weight 1) / `CMY` (weight 2) | light/paint splitting |
| **`R₃`** | complements `R\leftrightarrow C,\ G\leftrightarrow M,\ B\leftrightarrow Y` | opponent axes (`κ`) |

`RGB/CMY/Lab/HSB` are **four maps** of one 3-dimensional octahedron, organized by the group
`B_3=(\mathbb Z/2)^3\rtimes S_3` (`|B_3|=48`); these are **three projections**: `HSB` linearizes the cycle `R₁` (hue=angle on `C_6`,
the half-turn `180°`=`T^3=κ`=complement), `RGB/CMY` — the splitting `R₂`, `Lab` — the opposition `R₃` (axes `a,b`), while brightness
`L` — the observer (measured `L`=DC=frequency, `0.874`, Ch. VIII). The continuous body `[0,1]^3` breaks down into six
Kuhn sectors (six orders of `S_3`), where the `HSV` formulas give local coordinates `[◐]`.

**Graph.** The octahedron `K(2,2,2)`, the cycle `C_6`, and the three relations `R₁/R₂/R₃` are graph-facts, computed on matrices; the graph
lens (Ch. VIII) shows them directly, and the spectral theorem pertains to the same graph `[●]`.

### Summary

At rank 3 the single relation of difference — the Hamming distance — split into **three**: `R₁=C_6` (cycle),
`R₂=2K_3` (splitting), `R₃=3K_2` (three axes); `R_1\cup R_2=K_{2,2,2}` — the octahedron `[●]`. Its own movement
gave the rigorous half-turn `T^3=κ`, and the transport `𝒯` (`𝒯^2=\mathrm{id}`) gave the Möbius band `[●]`. The observer is read
in two ways — the center `σ½` and the projective quotient `U_3/κ=PG(1,2)` `[●]/[◐]`. The event of the rank is the **Fano/Tits explosion**: Steinberg
`2^{\binom32}=8` = the incidence graph of Fano = `\mathrm{Im}\,\mathbb O` `[●]`. The octahedron
is realized in three avatars: numerical (the divisors of `30`), color (`RGB/CMY`, three projections of `B_3`), and graph.

Chapter V crosses a **threshold**: the composite rank `4=2\times2` gives the first break `Q_2\square Q_2`, the middle layer
separates, and `i=√κ` enters the continuum; there too the lift continues to predict the higher figures — Fano and Petersen.


---

## Chapter V. Break and continuum (rank 4)

Rank 4 is the first **composite** rank: `4=2\times2`. Here the tower breaks in two for the first time, the middle layer
separates from the poles, and — what is more essential for number — the **imaginary unit** `i=√κ` enters the structure, and with it
the transition to the continuous side. Rank 4 is the boundary beyond which the discrete root descends from the finite cycle onto the
circle.

### 5.1. The break `Q₄=Q₂□Q₂`

The composite rank is the **product** of carriers: `Q_4=Q_2\square Q_2`, the Cartesian product of graphs, with the
coordinatewise `κ=κ_2\otimes κ_2`. The ranks **add** — `Q_a\square Q_b=Q_{a+b}` — and this is the monoidality of the lift
(Ch. VII). In numbers this is the `\times` of coprimes: `D(6)\times D(35)=D(210)`, `Q_2\square Q_2=Q_4` `[●]`
(`code_number_model/verify_functor_operations.py §C`).

The first composite rank is the one where **the system of axes breaks in two for the first time**: `4=2\times2` is that very break,
at which, in the general theory, `\mathfrak{so}(4)=\mathfrak{su}(2)^2` decouples, and the middle weight layer is separated
as an inner layer standing apart from the poles (unlike ranks 2–3). Number sees this break as a **tensor** doubling
of the cube.

### 5.2. `i=√κ`: the boundary of the discrete and the continuous

At rank 2 the sign of the self-relation was `\pm1` (reflection, `T^2=κ` on `C_4`); at rank 3 it was the half-turn `T^3=κ` on `C_6`.
Let us ask about the **quarter-turn** — the root of `κ`:

$$i^2 = -1 = κ, \qquad i = √κ.$$

Does `i` exist discretely? On the cycle `C_n` a quarter-turn exists only when `4\mid n`. On `C_6` (rank 3) it does **not**
(`i^6=-1\ne1`): `√κ` is discretely absent. It appears where the period is divisible by 4 — on `C_4`, `C_8` `[●]`
(`code_number_model/verify_operator_ladder.py §D`, `code_number_model/verify_rank_map.py §F`).

> **Meaning.** `i=√κ` is the **first root requiring continuity**. The discrete side takes the finite roots `C_{2^k}`;
> a quarter-turn on six sectors is impossible, on the circle it is possible. Rank 4 (`4\mid4`) is the first place where `i`
> exists discretely; but its true home is the circle. `i` is the marker of the **transition into the continuum**, where reflection
> `(\pm1)` is replaced by rotation `(\pm i)`.

Hence the simplex `\{e,i,\pi\}` — three invariants of `\exp:(\mathbb C,+)\to(\mathbb C^\ast,\times)`, and this is a **forced hierarchy of roles** along the base/exponent axis: `e` — the carrier (base; the unique natural one, `d/dx\,e^x=e^x`; base only), `i` — the operator (angle; `√κ`, order 4), `\pi` — the measure (period; half-period).

The asymmetry is forced by type and is the **projection of `\iota^2=\mathrm{id}`**: `e^{i\pi}=κ` — the involution itself, `(e^{i\pi})^2=e^{i2\pi}=\mathrm{id}` — its order 2 `[●/◐]` (`code_number_model/verify_simplex_center.py §F`).

At rank 3 spin is realized as **real** `\mathfrak{so}(3)`
(the structure constants `\varepsilon_{ijk}` are real, `i` is not needed); complexification is a separate step into the
continuum, and it comes here `[●/◐]`.

### 5.3. What is further up the tower

Rank 4 in the number branch is **thin**: the break of the system of axes and the **body-matter** (the separated middle layer `S₂`)
are unfolded in document 01 (chapter IV) `[●]` by reference.
To number corresponds the **entry of `i`** into the continuum — this is its share of rank 4. The modular layer `4/5` (`SL(2,\mathbb Z)`,
the `j`-invariant, Hecke operators) is classical `[●]`, but the connection with the rank `\omega(N)` is still open (`SL(2,\mathbb Z)\ne`
the divisor lattice): we take it as a **pointer** `[○]` — an open front into which the reverse side grows.

### 5.4. Higher up the tower: Fano, Petersen, the Mersenne horizon

The lift `Q_{n-1}^\ast\cong U_n/\kappa` (Ch. IV §4.5) continues to predict the figures of discrete geometry, and this is the
**combinatorics of number**. The space of axes grows as a projective tower:

$$U_n/\kappa \cong PG(n-2,2):\quad PG(1,2)\,(3,\text{rank }3)\ \to\ PG(2,2)\,(7,\text{Fano, rank }4)\ \to\
PG(3,2)\,(15,\text{rank }5)\ \to\ \dots$$

★**The Petersen graph appears twice** (`code_number_model/verify_octahedron_relations.py §F`). At rank 5 the middle layer `S_2^{(5)}` —
the ten two-element subsets `\{i,j\}\subset\{1,\dots,5\}`; the disjointness relation (`d=4`) is the Kneser
graph `KG(5,2)` — the **Petersen graph** (10 vertices, 3-regular, spectrum `\{3,1^5,(-2)^4\}`, triangle-free).
At rank 6 the quotient `S_3^{(6)}/\kappa` (ten axes) gives Petersen a second time, through complements in a five-element
set. One figure, two appearances by different mechanisms — the combinatorial self-similarity of the construction `[●]`.

★**The Mersenne horizon** (`code_number_model/verify_octahedron_relations.py §G`). The number of axes `|U_n/\kappa|=2^{n-1}-1`. The Singer cycle
acts on the points of `PG(n-2,2)` transitively for every `n` — this is classical, it does not serve as a distinguisher; the content
of the horizon is the **order** of the cycle. When `2^{n-1}-1` is a **Mersenne prime**, the Singer group has prime order:
each of its nontrivial elements is a full cycle on all axes, there are no proper suborbits `[●]`. This singles out the ranks

$$n=3,4,6,8,14,\dots\qquad(n-1=\text{Mersenne exponent}).$$

At rank 5 the order is composite (`2^4-1=15=3\cdot5`): the cycle has proper subgroups of orders 3 and 5, and the rotation
of axes breaks into short suborbits. The connection of this series with the Gauss–Wantzel theorem on constructible
polygons is a `[○]` front: a pattern, not a derivation.

> **Clarification of the shares by ranks.** Ranks 5–6 carry a rich **discrete geometry** (Petersen, `PG(3,2)`, `PG(4,2)`)
> — the numerical/combinatorial side; ranks 7–8 (height, closure — document 01, chapters V–VI) lie outside the number series.
> The number series covers the higher ranks combinatorially as well.

### 5.5. Realization: the quarter-turn

**Graph/color.** On the hue-circle (rank 3, six sectors) there is no quarter-turn — six is not divisible by four; it appears
only on the continuous circle, between the discrete colors. `i` is a rotation by `90°` in the body, which cannot be reached on six vertices
`[◐]`. Thus the discrete/continuum boundary is seen directly: `κ` (`180°`) is attainable on the cycle, `√κ` (`90°`) — only on the
circle.

### Summary

Rank 4 is the first composite one: `Q_4=Q_2\square Q_2`, a tensor doubling of the cube, the first break of the system of axes `[●]`. And
the boundary of the continuum: `i=√κ` is discretely absent on `C_6` (rank 3) and appears where `4\mid n` — the **first root
requiring continuity** `[●]`; reflection `(\pm1)` is replaced by rotation `(\pm i)`, the simplex
`\{e,i,\pi\}` closes. The modular layer `4/5` is a pointer `[○]`, an open front. To number rank 4 gives the entry of `i`.
Higher up the tower the lift predicts Fano and Petersen **combinatorially** (§5.4) — the numerical side of the higher ranks `[●]`.

Chapter VI turns the gaze to the **reverse side**: if `+\times\hat{}\,!` grow outward, then `-\div\log` go inward —
the p-adic tower, `\Gamma` with poles, the inversion `\mu`; and `\prod_v|x|_v=1` balances both sides of the seam.


---

## Chapter VI. The reverse side: two sides of the seam

Everything set out so far has looked **outward**: the growth of the series, the cube, the octahedron, the lift — the operations `+\ \times\ \hat{}\ !`,
total, growing. But from the seam `σ½` there goes both outward **and inward**. The direct operations are closed within `\mathbb N`;
the inverse ones — `-\ \div\ \log` — are partial, and the standard view takes the total side, hiding the partial one. This chapter
restores the **mirror**: the partiality of the inverse operations is a **p-adic tower inward**, and the seam
is symmetric — both sides are equal in standing, and `\prod_v|x|_v=1` balances them exactly.

### 6.1. Why one looks outward

The tower of hyperoperators is built forward: `\mathrm{succ}\to+\to\times\to\hat{}\to\dots`, and all of them are **total** —
`a+b`, `a\cdot b`, `a^b`, `a!` are always defined. The inverse ones are partial: `a-b\in\mathbb N` only when `a\ge b`;
`a/b\in\mathbb Z` only when `b\mid a`; `\log_b a\in\mathbb N` only when `a=b^k`. Such is the reason for the one-directionality:
mathematics takes the total side. But partiality is the **structure of the inner side**: there, where the inverse operation
is "not defined in `\mathbb N`", it **goes inward**.

### 6.2. The mirror: the same operation, the second eye

Take `\times p`. The Archimedean magnitude `|x|_\infty` **grows**: `1,2,4,8`. But the p-adic `|x|_p=p^{-v_p(x)}`
**decreases**: `1,\tfrac12,\tfrac14,\dots` — the same action **submerges inward**, into the tower of divisibility. One operation,
**two eyes**: the Archimedean (growth outward) and the p-adic (submersion inward). The inner side is real — it is measured
by `|·|_p` `[●]` (`code_number_model/verify_two_sided_seam.py §B`). Thus `\div p` (partial outward) is a descent down the tower
(total inward): the "partiality" of the inverse ones in `\mathbb N` is a **projection** of the two-sided picture onto one side.

The height of the floor `v_p` (Ch. II, Ch. V) is this inner count: the movement `\hat{}` (multiplicity) grows the cube
**into the depth**, whereas `\times` grows it **into the breadth** (new axes). `\hat{}\perp\times`: the floor against the axis; `\mu` is blind
to the floors — the cube does not see the reverse side, the reverse side is measured by `|·|_p`.

### 6.3. The product formula `∏_v|x|_v=1` and its reading

By Ostrowski's theorem all valuations of `\mathbb Q` are the single Archimedean `|·|_\infty` and the tower of p-adic `|·|_p`,
connected by the exact equality:

$$|x|_\infty\cdot\prod_{p}|x|_p = 1. \qquad [●]$$

This is a **standard fact of valuations** (layer (V) of the base of definitions; `7\to 7\cdot\tfrac17=1`,
`\tfrac{12}5\to 2.4\cdot0.4167=1`, `code_number_model/verify_two_sided_seam.py §C`). The formula is an algebraic identity, not an image:
`∏_p|x|_p=1/|x|_\infty` follows from the canonical decomposition.

Reading the equality as a **"conservation law of the seam"** — what grew outward `|·|_\infty` has submerged inward
`|·|_p` exactly — is a `[◐]` **reading**: it binds the identity with the picture of two sides around `σ½`. To look only at
`|·|_\infty` means to see half; but "two-sidedness" as a single seam is a recognition, not a theorem. The same form
"full set → neutral" is seen in Euler (Ch. I, `\sum=\prod_p`) and in the discrete `\sum_k(-1)^k C(n,k)=0`.

The radial reading of the same equality — the outer radius of a number as the sum of its inward depths along the p-adic trees — is the bridge note `Bridges/radial_bridge.md`.

### 6.4. The factorial is two-sided: `Γ`

The factorial seems to stand apart from `+\times\hat{}`. This is the illusion of one side. Its continuation is the `\Gamma`-
function, and it has a **reflection**:

$$\Gamma(s)\,\Gamma(1-s) = \frac{\pi}{\sin(\pi s)}. \qquad [●]$$

Symmetric under `s\mapsto1-s` — the same `κ` as `x\mapsto1-x` (cube) and `s\mapsto1-s` (zeta) `[●]`
(`code_number_model/verify_two_sided_seam.py §E`). Here `n!=\Gamma(n+1)` is the outer half (growth), while the **poles** of `\Gamma` at
`0,-1,-2,\dots` are the inner one (the negative integers); the fixed point of `s\mapsto1-s` is `½=σ½`, and `\Gamma(½)^2=\pi`
— the reflection is extremal at the seam. The factorial is a **canonically two-sided** object, stitched by `s\mapsto1-s` at `σ½`.
The same holds for the zeta: `\xi(s)=\xi(1-s)` — the sum `\sum` (outward) `=` the Euler product `\prod_p` (inward), stitched at `σ½`.

### 6.5. Inversion: `μ` as the alternating side

Every direct operation has an inner mirror, and for summation it has a name. **Möbius** `\mu` is the **inversion**
of the zeta: `\mu*\zeta=\delta`, that is `\sum_{d\mid N}\mu(d)=[N{=}1]`, and analytically

$$\frac1{\zeta(s)} = \sum_{n\ge1}\mu(n)\,n^{-s} = \prod_p\bigl(1-p^{-s}\bigr). \qquad [●]$$

And `\mu(N)=(-1)^{\omega(N)}` is the **sign of the vertex** of the cube — the same `Z/2` sign as the singlet/triplet of holonomy (Ch. III).
Thus the `Z/2`-holonomy in the number model **is the Möbius function**: one object, two roles — inversion (the reverse side of `\zeta`)
and the sign of statistics. The totient `\varphi=\mu*\mathrm{Id}` — also through inversion (`code_number_model/verify_functor_operations.py §F`).

### 6.6. The base guard

So that two-sidedness does not reduce to the mysticism of `½`, let us apply the base-change guard.
Under the base changes `\varphi=a\cdot t+b` the fixed point of the involution **always** exists (an invariant `[●/◐]`), while the number
`½` itself **shifts** (a mirage of normalization `[✗]`). The same verdict everywhere: `σ½` is the "fixed point of `κ`", **not**
the numerology "exactly `½`". And: `\log` is base-independent (`\log_b=\log/\log b` — only a scale), `!=k!` is the number of
maximal chains of the cube (structurally, not "the magic of the factorial") `[●]` (`code_number_model/verify_functor_operations.py §H`).

### 6.7. Realization: additive and subtractive

The two sides of the seam are **two streams of color**. `RGB` is the additive system (light): start `000` (black),
**we add** → `111`; a stream outward from emptiness. `CMY` is the subtractive one (paint): start `111` (white),
**we subtract** → `000`; a stream inward from fullness. The complement `R\leftrightarrow C` is `κ`, the opponent pairs are the axes
of the octahedron. Two inverse streams around one brightness axis `[◐]`. The factorial is **light** (the whole spectrum of factors);
the choice of primes is a **projection onto atom-filters** (Ch. VIII).

### Summary

From the seam there goes **inward too**: the direct operations `+\times\hat{}\,!` are total (outward, `|·|_\infty`), the inverse ones
`-\div\log` are partial — this is the p-adic tower inward (`|·|_p`) `[●]`. `\prod_v|x|_v=1` is the conservation law of the seam
(outward = inward) `[●]`. The factorial/`\Gamma` and the zeta are two-sided objects, stitched by `s\mapsto1-s` at `σ½` `[●]`.
`\mu` is the inversion of `\zeta` and the sign of the `Z/2`-holonomy `[●]`. The base guard keeps `σ½` an invariant, `½` a mirage `[✗]`.
Color shows the two sides as additive/subtractive. The full picture of number is **two sides of the seam**.

Chapter VII gathers everything into **one construction**: `\iota^2=\mathrm{id}` unfolds along two axes, the operations `+/\times/\hat{}`
generate them, `\exp` is the bridge, and the morphisms are uniform across ranks and across the two models — bits and numbers.


---

## Chapter VII. The functor layer: the tower of ranks as a single construction

So far we have gone by steps — rank after rank. This chapter looks at the very **construction** of growth: at the fact that all
morphisms are uniform across ranks, that the two axes of growth are generated by the operations `+/\times/\hat{}`, while `\exp` stitches them, and that
one and the same construction is realized **in two models** — on bits and on numbers. Number ceases to be "similar" to the
structure and turns out to be its second rigorous realization. At the end the chapter names what from the deep functor core
is **posited** here.

### 7.1. The root: `ι²=id`

The functor is not built anew at each rank. **One root** — the zeroth invariant `\iota^2=\mathrm{id}`, the minimal
nontrivial involution, the self-identity of distinction "this / not-this". From it come the carrier (orbits of `\iota` → bits →
`Q_n=\iota^{\,n}`), the complement `κ` (`\iota` on all coordinates), the observer `σ½` (the fixed point of `\iota`, outside the
carrier), holonomy (the sign of `\iota`, `\pm1`). `κ^2=\mathrm{id}` holds in **both** models — in bits (`x\mapsto1-x`)
and in numbers (`d\mapsto N/d`) `[●]` (`code_number_model/verify_functor_layer_general.py §A`; `code_number_model/verify_functor_synthesis.py §A`).

### 7.2. The two axes

From the root — two independent unfoldings:

$$
\underbrace{Q_n=\iota^{\,n},\ \ \Lambda_L\dashv\pi\dashv\Lambda_R}_{\text{DIMENSION axis (discrete)}}
\qquad\Big|\qquad
\underbrace{\mathrm{id}\to κ\to i\to\dots}_{\text{ANGLE axis (continuous)}}
$$

The **dimension axis** grows the number of axes (ranks, lift). The **angle axis** divides the period: roots of the identity `\mathrm{id}\to
κ=\sqrt{\mathrm{id}}\to i=\sqrt{κ}\to\dots`, periods `1,2,4,8`; the discrete takes the finite `C_{2^k}`, the continuous — the whole
circle. `i=\sqrt{κ}` is the first root requiring continuity (Ch. V). Ranks grow dimension, roots divide the
angle — the axes are orthogonal `[●]` (`code_number_model/verify_functor_layer_general.py §E`).

### 7.3. The morphisms are uniform — and `κ` permutes the lifts

Each morphism is given by **one formula at all ranks** and is consistent with the lift (checked `n=1..4`): `κ` (`κ^2=id`),
the lift `\Lambda_L\dashv\pi\dashv\Lambda_R` (`\pi\circ\Lambda=\mathrm{id}`), the projection (`\pi\circ κ=κ\circ\pi`), two
gradings. The node — **`κ` swaps the two lifts**:

$$κ\circ\Lambda_L = \Lambda_R\circ κ. \qquad [●]$$

`κ` **permutes the left and right** lifts: to lift and complement = to complement and lift into the other
branch. This is a **natural transformation** and the **structural source of left/right** — two adjoint
lifts, `κ` swaps them `[●]` (`code_number_model/verify_functor_layer_general.py §B`).

### 7.4. Two gradings and holonomy

The scene carries **two** gradings (the support of rank 2, Ch. III):

- `H` (Hamming) — the number of active axes `\omega`; `H\circ κ=n-H`, symmetric around `σ½` (connection, set);
- `P` (position) — the value; `P\circ κ=(2^n-1)-P`, carries the **arrow** (order).

The source of direction is `P` `[●]`. And the `Z/2`-holonomy is uniform: at rank `n` the cycle `C_{2n}`,
`T=e^{i\pi/n}`, `T^n=κ`, `T^{2n}=\mathrm{id}` — `Z/2=\langle κ\rangle\hookrightarrow C_{2n}` at **every** rank
(rank 2: `C_4`, `T^2=κ`; rank 3: `C_6`, `T^3=κ`) `[●]` (`code_number_model/verify_functor_layer_general.py §§C,D`).

### 7.5. The operations generate the axes; `exp` is the bridge

The two axes are **grown by the operations** `+/\times/\hat{}` (the tower of hyperoperators: `\times`=iteration of `+`,
`\hat{}`=iteration of `\times`, Ch. VI). Each generates its own face `[●]` (`code_number_model/verify_functor_operations.py`):

- **`\times`** generates the **dimension** axis: `Q_a\square Q_b=Q_{a+b}` (rank adds), two realizations —
  `D(MN)=D(M)\times D(N)` and CRT `\mathbb Z/n`;
- **`\exp`** generates the **angle** axis: the monoid isomorphism `(\mathbb R,+)\to(\mathbb R_+,\times)`, and the roots of the angle axis
  lie on its image — `e^{i\pi}=κ`, `e^{i\pi/2}=i`. `\exp` carries `+\to\times` **and** discrete→continuum at once:
  it is the **bridge between the two axes**;
- **`\hat{}`** generates the **reverse side**: the height `v_p`, breaks the cube, `|·|_p` inward (Ch. VI).

> **Meaning.** The angle axis is the `\exp` of the additive tower: the discrete half-periods `\pi/2^k` under `\exp` become points
> of the circle. The boundary `i=\sqrt{κ}` (`4\mid n`) is the place where the discrete root descends from the finite cycle onto the circle, and
> `\exp` is the operator of this descent. `e^{i\pi}=κ` itself is the root `\iota^2=\mathrm{id}` (§7.1), projected into the
> continuum: a forced hierarchy of roles `e` (carrier) / `i` (operator) / `\pi` (measure), Ch. V §5.2. `[●/◐]`

### 7.6. Two models: number as a tuning fork

The morphisms are uniform across ranks **and across models**. The functor `\Lambda:S\mapsto\prod p` (Ch. II, T6) is on
squarefree numbers the isomorphism of categories "sets of primes ≅ numbers", and one morphism **coincides in both
models** under `\Lambda`: `κ` (complement ↔ `N/d`), `H` (Hamming ↔ `\omega`), the lift (`+`axis ↔ `\times`prime), `\pi`
(forget an axis ↔ remove a factor) `[●]` (`code_number_model/verify_functor_synthesis.py §B`). Number is the **second independent model** and
thereby the **tuning fork of functoriality**: what holds in both models is a functor of the construction; what holds only in one is a shell over
it. And `\mu` in numbers is the inversion `\zeta^{-1}` **and** the sign of the `Z/2`-holonomy at once (Ch. VI).

### 7.7. The boundary of the layer: the derived and the posited

The deepest theorems of the functor core are proved on the **bit** side (document 02, 385 checks;
in survey prose — document 01, chapter VIII); the frame of `\iota^2=\mathrm{id}`
**places** them, and here an exact caveat is needed:

- **the monad and the terminal** (`\mathbb Z/2\times(-)`, `σ½`=the terminal object) **are derived** from the root: the carrier is
  the free `\mathbb Z/2`-object (`|\mathrm{Hom}(Q_n,Y)|=|Y|^{2^{n-1}}`) → monad → terminal `[●]`
  (`code_number_model/verify_functor_synthesis.py §C`);
- **the law of growth** `PG(n-1,2)\cong U_{n+1}/κ` (the content of a rank → the axes of the next) — is **posited**:
  the count `2^n-1` comes from `\iota^2=\mathrm{id}` (orbits), but `PG\cong U/κ` as an **isomorphism of projective spaces**
  (lines→lines) requires a **linear** input (the shift `a\mapsto2a`), beyond a single involution. It lies `[●]` in
  the functorization; the frame places it on the dimension axis `[○]` (`code_number_model/verify_functor_synthesis.py §D`).

The full picture of the seam of the two models is the synthesis section of the full corpus (not part of the package): the bits carry the **structure** (`|·|_2`), the numbers carry the **height
and the reverse side** (`|·|_\infty`: `\hat{}`, `P`), invisible to the bits; `\exp` is the bridge of the sides; `\prod=1` in two forms (discrete
`\sum(-1)^k C(n,k)=0` = p-adic `\prod_v|x|_v=1`) is the seam itself in the law.

### Summary

The tower is **one construction**: from the root `\iota^2=\mathrm{id}` come two axes (dimension `\times`/lift, angle
`\exp`/roots), the morphisms are uniform across ranks `[●]`; `κ` permutes `\Lambda_L\leftrightarrow\Lambda_R` —
a natural transformation, the source of left/right `[●]`; two gradings `H\perp P` and `Z/2`-holonomy `[●]`; the operations
`+/\times/\hat{}` generate the axes, `\exp`=the bridge, `\hat{}`=the reverse side `[●]`; number is the second tuning-fork model, `\mu`=inversion
=the sign of `Z/2` `[●]`. The monad/terminal are derived from the root; `PG\cong U/κ` is posited (a linear input `[○]`), and lies on the
bit side. What is derived from the root is derived; what is posited is named as an input.

Chapter VIII makes the accompaniment explicit: **two lenses** — the graph (the carrier made visible) and color (a projection) — and the **wall of
values**, explained by metamerism.


---

## Chapter VIII. Two lenses and the wall of values

The construction has been built and named. What remains is to make explicit what has guided the exposition all along as an **accompaniment** —
the two lenses of the carrier, graph and color — and to name the **boundary**: what the construction does not generate. Both lenses make visible
one and the same thing, each with its own eye; and both, having reached their limit, show the **wall of values** — why the specific
number at the apex is not extracted from the structure. This is the finale: the structure reaches the observer and stops.

### 8.1. The graph — the carrier made visible

The graph **is the carrier itself**: `Q_n` is the hypercube-graph, and every morphism is an operation on it `[●]`
(`code_number_model/verify_graph_projection.py`, 8 checks):

| morphism | operation on the graph |
|---|---|
| `κ` | the antipodal automorphism (`κAκ=A`, no fixed vertex, the antipode at distance `n`) |
| the lift `\Lambda` | the graph product `\square K_2` (double + join the copies) |
| `H` | the layers of Hamming distance (distance-regular, the scheme `H(n,2)`) |
| holonomy | the cycle `C_6`, the half-turn `T^3=κ` |
| `\mu` | the sign of a vertex `(-1)^{\text{weight}}`; `\sum` = the reduced Euler characteristic `=0` |
| `U_3` | the octahedron `K(2,2,2)` (complete minus a matching), spectrum `\{0,4,4,4,6,6\}` |
| axes | the folded cube `Q_n/κ` (`2^{n-1}` vertices) |

We **draw** the tower of graphs (edge → square → cube → octahedron → cycle), and the functor only names what has been drawn.
This returns the exposition to its first step — **I see** — before **I name**.

### 8.2. Color — a projection of the carrier

Color is an **accompaniment**, but a measured one. The octahedron `Q_3` is colored by four charts (`RGB/CMY/Lab/HSB`, Ch. IV),
the group `B_3`. And here is the single **measured** appearance of the observer: the brightness axis `L` (the DC component,
frequency) — an invariant orthogonal to chromaticity; in the full corpus it is measured as `\mathrm{corr}(\text{frequency},DC)=+0.874` `[●]`,
on semantics only `0.02`. The observer is an extractable and removable axis: the separation is whitening by brightness `[◐]`.

### 8.3. Two lenses together

The graph and color are **parallel lenses** of one carrier, like `|·|_2` and `|·|_\infty`:

| structure | **graph** (the carrier, drawn) | **color** (a projection, colored) |
|---|---|---|
| `κ` | the antipodal automorphism | the complement `R\leftrightarrow C` |
| `σ½` | the center, no fixed vertex | brightness `L` (measured) |
| holonomy | the cycle `C_6`, half-turn=antipode | the hue circle, `180°`=complement |
| `H` | the layers of Hamming distance | slices of brightness/saturation |

The graph **leads** (what actually is), color **recognizes** (how it looks to the eye). Both are `[◐]` as lenses, `[●]` in
their own facts (graph spectra / color measurements).

### 8.4. ★The wall of values: metamerism

And here is the boundary that both lenses show alike. The exact **value** — which specific number stands at the apex —
is **not recoverable** from the structure. The reason is visible in color as **metamerism**: different spectra
give one color, because the three cone types lose information.

In numbers: numbers of **one rank** `\omega` — `\{6,10,14,15,21,22\}` (all with `\omega=2`) — have one projection onto
the observer (rank / brightness `L`), but different "chromaticity" (different primes). The projection `σ½` **loses chromaticity** —
which is why the values are not extracted from the structure, **just as the eye loses the spectrum in three cone types** `[◐]`
(`code_number_model/verify_color_projection.py §F`). In the graph it is the same: the folded cube `Q_n/κ` loses the distinction of vertices within a `κ`-class.

Color **vividly explains the nature** of the wall: the observer sees the projection, and the spectrum is lost. This is the
same limit that closes off the numerical values (the study of factorization; full corpus: there is no
acceleration of factorization).

### 8.5. The boundary, named precisely

Let us gather the wall into a single list — where the construction ends `[○]`:

- **values** — which specific number stands at the apex is not recoverable from the rank; it is lost in the projection onto `σ½`
  (metamerism);
- the **Riemann hypothesis** (all zeros on `σ½`) — remains open; the Mertens sum `M(x)=O(x^{1/2+\varepsilon})`
  is equivalent to it;
- the **law of growth `PG\cong U/κ`, the monad** — on the bit side (document 02 and the synthesis section of the full corpus), referenced here.

The general form of the wall is **form against interaction**: the discrete forces the **structure of relations** (topology — order,
`κ`, the minimum `⊥`, the center `σ½`, the hierarchy of roles), but not the **interaction** — force, content, value, lying on
`|·|_\infty`. The same limit is visible in the simplex `\{e,i,\pi\}`: it **has no** forced center-observer —
the metric center (orthocenter/barycenter) is frame-dependent, because it symmetrizes a forced hierarchy of roles (Ch. V §5.2);
the forced anchor is on the discrete side (the minimum `⊥` + the `κ`-center `σ½`), while the metric reaches for `|·|_\infty`-content,
which the structure does not give `[○]` (`code_number_model/verify_simplex_center.py`).

The wall is **in one place**: the values on the continuous reverse side `|·|_\infty`.
The construction reaches the observer `σ½` and **ends**; what lies beyond the projection is an input.

### Summary

The two lenses make the carrier visible: the **graph** (`Q_n` is the hypercube-graph, every morphism is an operation on it, `[●]`) and
**color** (the octahedron is colored, the observer is measured at `0.874`, `[●/◐]`). They are parallel, like `|·|_2`/`|·|_\infty`: the graph
leads, color recognizes. And both show the **wall of values** — metamerism: the projection onto `σ½` loses chromaticity, the values are not
derived `[◐]`. The boundary is named precisely and in one place.

The epilogue returns number to the family of projections of the construction — one of the facets, where the observer `σ½` is the common seam.


---

## Epilogue. Projections: number among the facets of the construction

We have traversed number by ranks — from the first distinction of counting to the functor layer and the wall of values. What remains is to return it
to its place: **number theory is one projection of the construction of distinction** — the realization of the construction on counting. The common core is
the observer `σ½`.

### What turned out to be number

Number turns out to be a **tower of cubes**. A squarefree number is the Boolean cube of its primes (`D(N)\cong Q_k`); a prime is
an atom; a composite is the reverse side; multiplicity is a floor above the cube. Divisibility is the order on the cube, the complement `d\mapsto N/d`
is `κ`, the center `√N` is the observer `σ½` outside the carrier. Zeta stitches together counting (`\sum`) and atoms (`\prod_p`), and
`\prod_v|x|_v=1` balances the outward and the inward. All of this is images of morphisms of one construction, realized on counting
`[●]`.

### Number as a second model of the construction

Number is a **second independent model** of the construction, alongside the bits `Q_n`: an isomorphism of categories "finite sets
of primes ≅ squarefree numbers under divisibility" (Ch. II). This is why it is a **tuning fork**: what holds in both the bits and
the numbers is the functor of the construction; what lies in only one model is a shell above it.

The common core of both models is the observer `σ½`. In numbers it is `√N` (the center of the self-dual lattice of divisors)
and the line `Re=½` of zeta; both carry one involution `1-x` with the fixed point `½` `[◐]` (the general form is proved, Ch. I) —
a recognition, not a theorem about the unity of the object.

### Two lenses, one carrier

Number is shown by **two lenses**: the graph (the carrier made visible — `Q_n` is the hypercube, the morphisms are operations on the graph) and
color (a projection — the octahedron is colored, the observer is measured). They are parallel, like the two sides of the seam `|·|_2/|·|_\infty`;
and both, having reached their limit, show one **wall**: the projection onto `σ½` loses the spectrum (metamerism), the values are not
derived.

### The register, in closing

- `[●]` — all the ranked mathematics: `D(N)\cong Q_k`, the product of chains, `\mu`, the Atlas, CRT, the functor `\Lambda`; the two
  weights `H\perp P`, the **body `L^2`** (Hölder `p=2`); the octahedron, `T^3=κ`, `e^{iL\pi}=I`, **Steinberg's `8`=Fano=Im`\mathbb
  O`**; the break `Q_2\square Q_2`, `i=\sqrt{κ}`; `\prod_v|x|_v=1`; the functor layer.
- `[◐]` — projections: `σ½=Re=½` (one seam), the color/graph lenses.
- `[○]` — input/wall: the Riemann hypothesis, values (metamerism); the center of the simplex `{e,i,π}` is frame-dependent (interaction=`|·|∞`); `PG\cong U/κ`/the monad — on the bit side.

The observer `σ½` is the **first word** (gray between black and white, rank 0/1) and the **last** (that beyond which the wall stands).
It holds the tower of cubes while remaining outside it: the absent middle, the invariant `κ`, the critical line. Number is presented
structurally and fully; the proved is separated from the projected, the wall is named precisely. The construction is one — number is one of its
facets, seen from its own angle.

