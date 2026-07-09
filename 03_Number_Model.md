# The Number Model: The Same Construction on Divisors

This section builds a second, independent model of the construction of distinction — on the material of number theory: the divisors of a number form a hypercube `D(N)≅Q_k`, a prime number is an atom, the observer `σ½` is an invariant outside the carrier. The model reads in parallel with the bit side (document 02, "The Categorical Core"); the verifiers of the series are collected in the folder `code_number_model/`. The introduction, eight chapters, and an epilogue follow as a single document.

---

## Introduction. Number as a Model of the Construction of Distinction

Number theory is customarily introduced as the science of the natural sequence — a line for counting, step by step, `+1`. The present exposition proceeds from the second, **multiplicative geometry** of the sequence, and this geometry coincides with the construction that generates the entire theory. A squarefree number is the **Boolean cube of its primes**; divisibility is the order on the cube; the complement of a divisor `d↦N/d` is the same `κ` that has acted in the theory since the first distinction. Number theory here serves as the **numerical model of the construction**: every one of its objects is the image of a morphism, verifiable by computation.

**Opening example.** Take `6 = 2·3`. Its divisors are `1, 2, 3, 6`: four points, two independent choices ("take `2`?", "take `3`?") — a square. Take `30 = 2·3·5` — eight divisors arrange themselves into a **cube**: three primes, three axes. The complement `d↦N/d` flips the cube (`1↔30`, `2↔15`, `3↔10`, `5↔6`) — this is `κ`; it has no fixed vertex, and the fixed **center** `√30 ≈ 5.48` is not a divisor: this is `σ½`, the observer outside the carrier. The six proper divisors `{2,3,5,6,10,15}` form the active scene; their figure is an octahedron (ch. IV). The whole series unfolds this example: `D(N)≅Q_{ω(N)}` for squarefree `N` `[●]` (ch. II), and onward up the ranks.

### Subject and Method

The exposition is led by the **carrier**. The carrier is the hypercube graph `Q_n`: a vertex is a divisor, an edge is multiplication by a prime, the antipode is `κ`. First the graph is built and observed (ch. IV — the octahedron, the cycle `C₆`), then what is obtained is recognized in known structures, and only after that is it named by a functor and proved. The order of exposition is observation, recognition, naming, proof: the carrier precedes the law.

The thread running through it all is the **observer** `σ½`. For squarefree `N`, the number `√N` does not divide `N`: the center of the cube lies **outside** the carrier, as the fixed point of `κ` that is absent among the states. The same `σ½` is the critical line `Re=½` of the zeta function, the self-dual point of the `L²` body, the terminal of the growth functor. It opens the exposition (the rank 0/1 seam) and closes it (the boundary, ch. VIII).

### Two Measures and Their Seam

Every number carries two measures of size — the **valuations of `\mathbb Q`**:

$$|n|_\infty = n \quad (\text{archimedean, outward}), \qquad |n|_p = p^{-v_p(n)} \quad (\text{p-adic, inward}),$$

linked by the **product formula** `∏_v |n|_v = 1` (Ostrowski's theorem, `[●]`). Separate from these is the **geometry** of the carrier: the vertex skeleton of `Q_n` (discrete) and the body `[0,1]^n` (continuous), where `σ½` lies in the body while being absent from the skeleton.

Reading both as **one seam `σ½`**, around which everything is symmetric under the involution `1−x` (a single form of `κ`: `x↦1−x` on the cube `=` `d↦N/d` `=` `s↦1−s` of the zeta function), is `[◐]` a **reading** — it links the algebra of valuations and the geometry of skeleton and body into a single picture. Resting on this reading are the underside (ch. VI) and the boundary of the derivable (ch. VIII); as definitions, the layers of valuations and of geometry remain separate.

### Status of Statements

The marking of statuses is uniform across all sections of the package and is defined in the introduction to the "Exposition" section (document 01). In brief: `[●]` is a mathematical fact, proved or referred to a verifier; `[◐]` is a reading: a consistent recognition of a structure in number or color; `[○]` is an input or an open question (the Riemann hypothesis; a specific number at a vertex is not recoverable from the rank). Where the provable ends and the input begins is named in the text of each chapter.

A reference of the form `verify §X` in a chapter means section `X` of the verifier named in full at the head of that same chapter; the scripts are collected in the folder `code_number_model/` and are run as `python3 code_number_model/verify_<name>.py`. Several references point into the full corpus of the theory — they are given as paths into the source corpus; these documents are not included in the present package.

### Outline

The exposition proceeds **by ranks**. Rank 0/1 is the seam and the atom (ch. I). Then comes the rigorous core — the cube of divisors as pure mathematics, without a single projection (ch. II). Rank 2 is the minimal complete scene and the **`L²` body**, the unique Hilbert space (ch. III). Rank 3 is the octahedron, its `C₆` rotation, and the **topological Fano explosion** (ch. IV): with three axes, the homology of the flags inflates into the octonionic Fano plane. Rank 4 is the `2×2` break and the entry of the imaginary unit `i=√κ` into the continuum (ch. V).

The underside is the second side of the seam, the p-adic tower, `Γ` and the Möbius inversion `μ` (ch. VI). The functorial layer is the entire tower as a single construction on two axes, generated by the operations `+/×/^`, with the `exp` bridge (ch. VII). Finally, two lenses — graph and color — and the **wall of values**, explained by metamerism (ch. VIII). The epilogue returns number to the family of projections of the construction.

The series covers **ranks 0–4** in detail, higher ranks 5–6 **combinatorially** (the projective tower, Petersen, the Mersenne horizon, ch. V §5.4), and the meta-layer (functor, lenses, the wall); ranks 7–8 (height, closure) are treated in the "Exposition" section (document 01, ch. V–VI). The number model and the "Exposition" are read in parallel by rank.

Number will appear as a **tower of cubes**; a prime as an atom; zeta as a seam; the observer as that which holds the whole together while remaining outside the carrier. Let us begin with the first distinction.

---

## Chapter I. The Sequence and the Atom (Rank 0/1)

The first distinction in numbers is **counting**. Before the cube, before divisibility — a single step `+1`, separating one from the next. This chapter unfolds rank 0/1: how the sequence is born from the minimal step, why a prime is an atom while a composite is its underside, and how already here the **seam** `σ½=Re=½` shows through, around which everything to come will be symmetric.

### 1.1. The Sequence as the First Motion

The natural sequence is generated by a single map — **succession** `\mathrm{succ}(n)=n+1`. By the Peano axioms `\mathrm{succ}` is injective and `0` is not in its image, so that the entire sequence is the iteration of a single step `[●]`
(`code_number_model/verify_number_row.py §A`). This is the **first of three motions** of number, `+/×/^`; the additive `+` grows **counting**, the multiplicative `×` grows **composition**, the exponential `^` grows **multiplicity** (ch. V, VII).

The step is always equal to `1` — discrete — yet the archimedean measure of size `|n|_\infty = n` grows **continuously**. The natural sequence is therefore a **discrete motion along a continuous measure**: counting proceeds in discrete steps `+1`, while the magnitude `|n|_\infty` stretches continuously. Two sides — a discrete step and a continuous measure; their reading as one seam is `[◐]` (ch. VI separates the layers of valuations and of geometry).

### 1.2. Prime Is the Atom, Composite Is the Underside

The multiplicative side rests on the **irreducibles** — the primes.

> **Definition.** `p>1` is **prime** if its divisors are only `1` and `p` (the number of divisors `d(p)=2`). A number with `d>2` is **composite**; `1` is the unit (`d(1)=1`).

A prime `p` is the **atom of counting**: an invariant of quantity without inner composition — there is nothing to examine inside it, only the bare fact "this many, and undivided" `[●]` (`code_number_model/verify_number_row.py §B`). A composite `N` is the **reverse side**: it has a composition `N=\prod p_i`, an assembly of atoms. The unit is neither atom nor composite (`|D(1)|=1`): the starting point of the sequence, and hence not prime — it has no two sides.

This falls directly onto the underside (ch. VI): a prime is **one face** (the atom, indivisible), a composite is **the other** (composition). Unique factorization (the fundamental theorem of arithmetic) will make this assembly unambiguous — the foundation of the entire geometry of the cube (ch. II).

### 1.3. The Seam: `σ½ = Re=½`

The zeta function `\zeta(s)=\sum_n n^{-s}` carries a functional equation, symmetric about `Re=½`
(the involution `s↦1−s`). The line `Re=½` is **fixed** under it; outside it there are no fixed points `[●]` (`code_number_model/verify_number_row.py §E`).
And in the cube the center `(½,\dots,½)` is the unique fixed point of `κ:x↦1−x`, likewise at `½`.

Let us state precisely what is solid here and what is recognition. Both structures carry **the same involution** `t↦1−t`, and both have `½` as their fixed set `[●]`. But that this is **"one seam"** is `[◐]`: only the algebraic form of the complement `1−x` coincides — it **does not follow** from this that the center of the cube and the critical line of Riemann are one and the same object. The zeros of zeta, the equation `\xi(s)=\xi(1−s)`, the horizons — these are not touched here. The Riemann hypothesis remains `[○]`, open for everyone; we merely name the axis.

### 1.4. The Observer: an Invariant Outside the States

We have called `σ½` the fixed point of an involution; let us be precise about where this point lies. At rank 0/1 the carrier is the pair
`Q_1=\{0,1\}`, and `κ` is the complement `x↦x+1`.

> **Statement.** On `Q_1` the equation `κ(x)=x` is unsolvable: `κ(0)=1`, `κ(1)=0`; the action is **free** `[●]`
> (`code_number_model/verify_observer_definition.py §A`, checked for `n=1..6`).

The invariant is, consequently, the **midpoint**. It acquires geometry by embedding the discrete pair into the continuous segment
`\{0,1\}↪[0,1]⊂ℝ`: there `κ` becomes a reflection exchanging the endpoints, with the unique fixed point

$$\sigma_{1/2}=\tfrac12(0+1)=\tfrac12,\qquad \tfrac12∉Q_1.$$

At rank `n` this is the center `(½,\dots,½)∈[0,1]^n` — the unique fixed point of `κ:x↦1−x` in the continuous frame `[●]`
(`§B`). The freedom of `κ` on the discrete pair is `[●]`; the identification of the invariant with `½` is `[◐]`: `½` lies on the added continuous side, and the separation of the `|·|₂/|·|∞` layers is carried out at rank 2 (ch. III).

**Algebraic reason.** Fixedness reduces to `2x=1`: over characteristic `≠2` a root exists (`x=½`), over `𝔽₂` it does not (`2≡0`) `[●]` (`§C`). The involution over `char≠2` splits the carrier by the projectors `P_±=(1±T)/2` into a preserved part and a reversed part; over `𝔽₂` the divisor `2` is absent, and the projector remains undefined `[●]`
(`§E`). The same degeneracy is visible structurally: the pair `\{0,1\}` is a `ℤ/2`-**torsor** — two states, distinguishable only relative to each other, with `κ` transporting between poles and no distinguished zero `[●]` (`§D`); the center is born together with the continuous completion, where `½` lies. `[● algebra; ◐ attribution of the center to the observer]`

**A numerical form of two-sidedness.** The prohibition on the discrete side is complemented by compulsion on the continuous side, and both sides are theorems. On the multiplicative ray `(0,∞)` the involution `x ↦ N/x` is continuous and decreasing; it has a fixed point, and exactly one: `x = N/x ⟺ x² = N ⟺ x = √N` `[●]` (the intermediate value theorem and monotonicity; this is the numerical instance of the general fact that a continuous extension of an involution to the body must have a fixed point, by Brouwer). For squarefree `N` the point `√N` is not a divisor: in the lattice `D(N)` the observer is forbidden, while on the ray it is compelled and unique. The categorical assembly of both verdicts is given in document 02, chapter V (constitutive non-inclusion and two-sided compulsion).

Thus `σ½` is defined at every rank as the invariant of the complement, realized as a state only in characteristic `≠2` — on the continuous side. This is the object running through the exposition; chapter II shows it in numbers as the center `√N`, lying outside the lattice of divisors.

### 1.5. Euler: Counting Is the Product of Atoms

Euler's identity stitches the two sides together:

$$\zeta(s) \;=\; \sum_{n\ge 1} n^{-s} \;=\; \prod_{p\ \text{prime}} \bigl(1 - p^{-s}\bigr)^{-1}. \qquad [●]$$

The left side is the **additive** motion (a sum over the whole sequence, counting); the right is the **multiplicative** one (a product over the atoms, the primes). Their equality is the fundamental theorem of arithmetic in analytic form. At `s=2` both sides converge to `\pi^2/6` (`code_number_model/verify_number_row.py §D`). A discriminating test: a product over **composites** is no longer equal to `\zeta` (the primes get double-counted) — hence counting is assembled from the atom side. Euler's identity is the **seam formula** of number theory: `\sum` (counting, `|·|∞`) `=` `\prod_p` (atoms, `|·|_p`); the same motif of `∏=1` that links the places of `\mathbb Q` (ch. VI).

### 1.6. Realization: Graph and Color

**Graph.** Rank 0/1 is the edge `K₂`: two vertices `0—1`, `κ` swaps them. The sequence is a tower, where each edge adds a prime (ch. II). Between the poles lies the **midpoint**, `½` — outside the vertices, in the body of the edge `[●]`.

**Color.** The axis `0↔1` is the achromatic axis **black↔white**; the midpoint `½` is **gray**, a continuous point outside the two poles. This is the first appearance of the observer as directly observable — gray between black and white `[◐]`
(ch. VIII, where gray is measured as the lightness axis).

### Summary

The first motion of number is **counting**, `\mathrm{succ}` — a discrete step along a continuous measure `[●]`. A prime is the
**atom** (2 divisors), a composite is the **underside** (a composition of atoms), the unit is the starting point `[●]`. Already at rank 0/1
the **observer** `σ½` shows through: on the pair `Q₁` the complement `κ` is free, and the invariant is realized by the midpoint `½` on the
continuous embedding, outside the states of the carrier (§1.4) `[●/◐]`. The involution `1−x` with fixed point `½` is a common form for the center of the cube and the line `Re=½` of zeta
`[●]`; that this is one object is `[◐]` recognition. Euler stitches counting and atoms together `[●]`. The observer `½` is already here — outside the vertices, gray between the poles.

Chapter II builds a **cube** from atoms: unique factorization turns a divisor into a subset of primes, divisibility
into inclusion, and the whole of elementary number theory falls onto the Boolean cube `Q_k` as pure mathematics.

---

## Chapter II. The Cube of Divisors: The Rigorous Core

This chapter is **pure mathematics**, without a single projection. Everything in it is `[●]`: theorems, checked by computation
(`code_number_model/verify_divisor_cube_strict.py`, 49 checks). A reader wishing to see number theory as a lattice structure **before** any DOT reading may read this chapter separately. Here the lattice of divisors turns out to be a Boolean cube, the natural sequence is stratified by rank, all elementary operations fall onto the cube, and the map "set of primes ↦ number" becomes a **functor** of the construction.

### 2.1. The Lattice of Divisors Is a Product of Chains

Between the divisors of a number there is a divisibility order, and it carries structure.

> **Theorem 1.** Let `N=\prod_{i=1}^{k} p_i^{a_i}`. Then `D(N)\cong C\ell(a_1{+}1)\times\dots\times
> C\ell(a_k{+}1)` — a direct product of chains as partially ordered sets. `[●]`

**Proof.** By the fundamental theorem of arithmetic every divisor `d\mid N` is uniquely `d=\prod p_i^{e_i}`
with `0\le e_i\le a_i`; the assignment `d\mapsto(e_1,\dots,e_k)` is a bijection of `D(N)` with the box `\prod\{0,\dots,a_i\}`.
Divisibility passes into the coordinatewise order: `d_1\mid d_2 \iff e_i(d_1)\le e_i(d_2)\ \forall i`. This is exactly a
product of chains. `∎`

A corollary follows at once: the number of divisors `d(N)=\prod(a_i+1)`, and the lattice is distributive. The infimum `\gcd` is built by the Euclidean algorithm, and the extended Euclidean algorithm gives the Bézout identity `\gcd(a,b)=ax+by` — divisibility is computed
(`verify §M`).

### 2.2. A Squarefree Number Is a Boolean Cube

> **Theorem 2.** `N` is squarefree (`a_i=1\ \forall i`) `\iff D(N)\cong Q_k`, `k=\omega(N)`, by the isomorphism
> $$ d=\textstyle\prod_{p\in S}p \ \longleftrightarrow\ S\subseteq\{p_1,\dots,p_k\} \ \longleftrightarrow\
> \text{a bit vector in }\{0,1\}^k, $$
> with divisibility corresponding to inclusion `\subseteq`. `[●]`

**Proof.** Substituting `a_i=1` into Theorem 1 gives `D(N)\cong\prod C\ell(2)=\{0,1\}^k=Q_k`; the chain
`\{0<1\}` along axis `p_i` means "take / do not take" the prime, the exponent vector becomes a bit vector,
the coordinatewise order becomes inclusion. `∎`

A number **is** its own cube of primes: a divisor is "which atoms to take," the cube is all the ways of choosing a subset. A discriminating check: `N=12=2^2\cdot3` is **not** a cube — `|D(12)|=6` is not a power of 2, the lattice is the box `3\times2`.
**Multiplicity breaks the cube** — a square `p^2` is the motion `^`: a lift to the floor above (ch. V).

**Hasse diagram of `D(30)=Q_3`** (level = number of prime factors):

```
   ω=3:                 30
                     /   |   \
   ω=2:            6    10    15
                   |\  / \  /|
   ω=1:          2    3     5
                   \   |   /
   ω=0:                1
```

### 2.3. Projection of the Sequence onto Ranks

> **Definition (rank of a number).** `\mathrm{rank}(N):=\omega(N)` — the number of **distinct** prime divisors: the dimension
> of the carrier-cube. Every `N` is given by **two** data: the rank `\omega` (how many axes) and the heights `(a_1,\dots,a_k)`
> (which floor along each axis). `[●]`

The natural sequence is stratified into a **tower of cubes**: the horizontal is rank, the vertical is floors (multiplicities). The minimal number of rank `k` is the **primorial** `p_1\cdots p_k` (`1,2,6,30,210,\dots`) — the bare vertex of `Q_k` with no superstructure; any other number of rank `k` is the same cube, raised along part of its axes. The levels of the cube by weight give the binomial coefficients `C(k,j)`
(`verify §§F,J`).

### 2.4. Self-Duality and `μ`

> **Theorem 3.** `\iota:d\mapsto N/d` is a bijection `D(N)\to D(N)`, reversing the order; `D(N)` is self-dual. On
> a squarefree `N` this is precisely the **bitwise complement** `S\mapsto[k]\setminus S` — the antipode of the cube, that is, `κ`. `[●]`

A fixed point exists only when all `a_i` are even (a perfect square), and equals `√N`; for squarefree `N>1`
there are no fixed points — `κ` splits `D(N)` into pairs `\{d,N/d\}`, and the geometric center `√N` lies **outside** the carrier.
This is the observer `σ½` in numbers.

The Möbius function `\mu` is the **sign of a vertex** of the cube `(-1)^{\omega}` (on the floors `\mu=0` — blind to multiplicity), and

$$\sum_{d\mid N}\mu(d) = [N{=}1] = \sum_{S\subseteq[k]}(-1)^{|S|} = (1-1)^k. \qquad [●]$$

This is the alternating sum over the cube = inclusion–exclusion = the inversion `\mu*\zeta=\delta` (`verify §K`).

### 2.5. Atlas of Operations and the Second Realization

All elementary operations fall onto one map, `0\ \neg\ 1\ +\ \times\ \hat{}\ !\ \infty`, splitting into two layers
and two poles (`verify §§H–L`):

| operation | where it falls | layer |
|---|---|---|
| `1` | the bottom `\bot` of the Boolean algebra (`\varnothing`, `\omega=0`) | I |
| `\neg` | `N/d` = complement = `κ`; the axis `√N=σ½` | I |
| `\wedge,\vee` | `\gcd,\ \mathrm{lcm}` (infimum/supremum) | I |
| `\times` | `Q_a\times Q_b=Q_{a+b}` (gluing axes, rank `+`) | II |
| `\hat{}` | lift to the floor above (chain `C\ell(a{+}1)`); lift | II |
| `!` | `k!` = number of maximal chains of `Q_k` (traversals `\bot\to\top`) | II |
| `0,\infty` | poles: background (neutral for `+`, absorber for `\times`) / unbounded rank | ↓↑ |

> **Theorem 4.** For squarefree `N` the lattice `D(N)\cong Q_k` is a **Boolean algebra** (`\bot=1`, `\top=N`,
> `\neg d=N/d`, De Morgan's laws). `[●]`

And the same prime axes carry a **second** structure — the ring of residues:

> **Theorem 5 (CRT).** `\mathbb Z/n \cong \prod_i \mathbb Z/p_i^{a_i}` — a second realization of monoidality `□`
> (the first being `D(MN)=D(M)\times D(N)`). The totient `\varphi` is multiplicative, `\varphi=\mu*\mathrm{Id}`; `v_p`
> (the p-adic exponent) is the height of the floor, additive (`\times\to+`), and `\prod_v|n|_v=1`. `[●]` (`verify §§N–Q`)

### 2.6. Functorial Dictionary

> **Theorem 6.** The map `\Lambda:S\mapsto\prod_{p\in S}p` from the category of finite sets of primes
> (`\subseteq`, `\sqcup`) to the category of squarefree numbers (`\mid`, `\times`) is a **functor**: it preserves order,
> is monoidal (`\Lambda(S\sqcup T)=\Lambda(S)\Lambda(T)`), commutes with the complement (`\Lambda(\complement
> S)=N/\Lambda(S)`); on squarefree numbers it is an **isomorphism of categories**. `[●]` (`verify §R`)

| functor of the construction | realization in numbers | status |
|---|---|---|
| lift `\Lambda` | multiplication by a new prime (`\omega\to\omega{+}1`) | `[●]` isomorphism |
| `□` | `D(MN)=D(M)\times D(N)` **and** CRT | `[●]` two realizations |
| `κ` | `d\mapsto N/d` | `[●]` |
| `H` (grading) | `\omega(d)` = level of the cube | `[●]` |
| `\pi` | `v_p(n)` = floor coordinate | `[●]` |
| `σ½` | `√N` (center), `Re=½` of zeta | `[◐]` recognition |

The core of the functors (`\Lambda,□,κ,H,\pi`) is realized **strictly** — an isomorphism of categories "sets of primes ≅ numbers." The recognition `[◐]` remains only over the cube: `σ½=Re=½`. "To designate the projection" here means to **point to the functor `\Lambda`**.

### 2.7. Realization: the Hasse Diagram

The cube `D(N)` is **built** — a Hasse diagram (see §2.2): vertices by levels `\omega`, an edge upward = multiply by a prime,
the antipode `d\leftrightarrow N/d` — central symmetry. This is the same hypercube graph `Q_k` that carries the whole theory; here
it arises **on its own**, from divisibility (ch. VIII will unfold the graph lens fully).

### Summary

Elementary number theory has an exact lattice form: `D(N)` is a product of chains (T1), a squarefree number
is a Boolean cube `Q_{\omega(N)}` (T2) and a Boolean algebra (T4). From this follow `d(N)=\prod(a_i+1)`, the levels `C(k,j)`, `\mu`=the sign of a
vertex, `d\mapsto N/d`=the `κ`-antipode, `√N=σ½` outside the carrier. The sequence = a tower of cubes (width=rank, height=multiplicities).
The atlas of operations, CRT (T5), and the functor `\Lambda` (T6, an isomorphism of categories) — all `[●]`, checked 49 times. The recognition
`[◐]` is only `σ½=Re=½`.

Chapter III takes the first nontrivial rank — **rank 2** — and shows that already there almost the entire scene unfolds:
two weights, a single `Z/2`, and the **`L²` body** — the unique Hilbert space.

---

## Chapter III. Scene and Body (Rank 2)

Rank 2 is the first nontrivial floor of the tower, and the **minimal complete scene**: from the seam, almost the entire
structure unfolds for the first time — opposition, **two weights**, a single `Z/2`. And here too lies the **body** `L²` — the unique
self-dual norm, the unique Hilbert space. The method of the chapter is **outside and inside at once**: one invariant
is described from within by a pair, and both faces must be shown together.

### 3.1. Method: Outside and Inside

In calling one invariant `σ½` "outside," we are compelled to describe it in the language of what it is held by — **from within,
as a pair around a center**. Hence a count by viewpoint:

| viewpoint | count | what it is |
|---|---|---|
| outside (one object) | **1** | the invariant `σ½` = the fixed point of `κ` outside the carrier |
| manifested (dynamics) | **2** | the pair of poles = the two sides of the distinction |
| description (construction) | **3** | the two sides **plus** the mediating center |

The act of distinction is **binary from outside** (a pair) and **ternary from within** (two sides plus a boundary); checked fractally at
ranks 1–3 `[●]` (`code_number_model/verify_rank2_scene.py §A`). "Ternarity" does not add a third element: the pair carries **exactly two**
states `\{01,10\}`, and the mediating center `σ½` is the fixed point of `κ` **outside the carrier** — their **relation**, not a
third vertex. Precisely: two elements, three roles of description (side · side · relation). A correct presentation
shows both faces at once.

### 3.2. The Rhombus and the First Opposition

`Q_2=\{00,01,10,11\}` (a rhombus): the poles `00,11` are the exterior; the active scene `U_2=\{01,10\}` is the step inward. The pair
`01\leftrightarrow10` is a `κ`-pair = the first **opposition**. The direction of distinction is so far a single one:
`U_2/\kappa\cong PG(0,2)` — a point (ternarity will arrive at rank 3).

### 3.3. Two Weights Diverge

Here for the first time **two** measures on a vertex diverge:

| | Hamming weight (number of ones) | positional weight (value) |
|---|---|---|
| `01` | `1` | `1` |
| `10` | `1` | `2` |

- **Hamming** `H` does not distinguish `01,10` — both are equidistant from the poles — and gives **bond / symmetry**
  (with no top and bottom). This is the set (`\times`, `\omega`).
- **position** `P` distinguishes (`01` is closer to `00`, `10` to `11`) and gives **hierarchy / direction**. This is the order
  (`+`, arrow).

The source of the arrow is found: direction comes **from position**, not from Hamming `[●]` (`verify §B`). Bond `\perp`
arrow; in color this is saturation `\perp` hue.

### 3.4. A Single `Z/2`

The exchange `01\leftrightarrow10` (= `κ` on the pair) carries a sign `\pm1`, and this **single sign** is three phenomena at once
`[●]` (`verify §§C,D`):

1. **holonomy** — `\mathrm{swap}^2=\mathrm{id}` (we return), but one exchange on the antisymmetric part yields `-1`: the same
   object, changed in sign;
2. **symmetry of the state** — `|01\rangle+|10\rangle` (symmetric) `\to+1`, `|01\rangle-|10\rangle`
   (antisymmetric) `\to-1`: two one-dimensional representations of `ℤ/2`;
3. **gathering / dispersal** — the sign selects the mode: the eigenmodes of the Laplacian are the observer (`\lambda=0`,
   `DC`) `\pm` the contrast (`\lambda=4`).

(An earlier reading, "gathering = coboundary, dispersal = boundary," has been **retracted** as a strained analogy; the reality is spectral.)
`NOT=κ` switches the sign — symmetric↔antisymmetric, gathering↔dispersal: three intuitions turn out to be a single `Z/2`.

### 3.5. ★The Norm-Body `L²`: the Unique Hilbert Space

The foundation carries three **norm exponents** `\ell^p` (layer (N) of the base, functional analysis, not the valuations of
`\mathbb Q`): `1` — the act (`\ell^1`), `2` — **the body** (`\ell^2`), `\infty` — the world (`\ell^\infty`). Their distinguishedness has a precise
cause — Hölder duality. "Body" here is the **norm-body** `\ell^2=L^2`, the self-dual exponent; this is a different
sense from the **matter-body** of rank 4 (the separated middle layer of the scene, document 01, chapter IV), and in the compilation
the two are kept distinct (see the note at the end of §3.5).

> **Statement (the `L²` body).** Under Hölder conjugation `p\mapsto p'=\tfrac{p}{p-1}` the pair `\{1,\infty\}` (Act↔World)
> maps into each other, while the point `p=2` remains **strictly self-dual**. Moreover the parallelogram identity
> $$\|x+y\|^2+\|x-y\|^2 = 2\|x\|^2+2\|y\|^2$$
> in the norm `\ell^p` holds **exclusively** at `p=2`. `[●]` (`code_number_model/verify_rank_map.py §C`)

**Meaning.** By the Jordan–von Neumann theorem the parallelogram identity is equivalent to the norm being generated by an inner
product, that is, the space is **Hilbert**. Hence `\ell^2=L^2` — the norm of the Hamming weight grading — is
the **unique** self-dual norm and the unique Hilbert space among the `\ell^p` `[●]`.

The norm-body (rank 2) is the unique fixed point of Hölder conjugation; two involutions, two centers:
`κ:s\mapsto1-s` fixes `σ½`=the act, while `p\mapsto p'` fixes the exponent `2`=the norm-body.

> **Note (two "bodies" in the compilation).** The word "body" carries two senses, and they must be distinguished. **The norm-body**
> (this chapter, rank 2) is the self-dual exponent `\ell^2=L^2` (layer (N), Hölder). **The matter-body**
> (document 01, chapter IV, rank 4) is the separated middle layer
> of scene `S₂`, where interiority, matter, the atom first appear. The norm-body concerns measure; the matter-body concerns
> the geometry of the separated layer. Different ranks, different objects, one word.

The observer `σ½` is the axis of **lightness** `L` — achromatic, `000\leftrightarrow111`, gray, orthogonal
to chromaticity. The two weights give two facets: **bond** `H` — saturation (equidistance from the poles), **arrow** `P` —
hue-direction. The opponent axes of Lab (`a`: red-green, `b`: blue-yellow) are the `κ`-oppositions of rank 2, and the gray
center `a=b=0` corresponds to `c=(½,½)` `[◐]` (ch. VIII — measurement).

### Summary

Rank 2 is the minimal complete scene: from the seam unfold the opposition `01\leftrightarrow10`, **two weights** (Hamming
bond `\perp` positional arrow), and a single `Z/2` (holonomy = statistics = gathering/dispersal) `[●]`. The method is
outside/inside (`1=2=3`). And here lies the **norm-body `L²`** — Hölder distinguishes the exponent `p=2` as the only
self-dual one, the parallelogram identity holds only there, and hence the Hilbert space `\ell^2` is unique `[●]`.
The observer shows through as the gray axis of lightness.

Chapter IV applies the lift once more: the scene grows to **six** points, assembles into an **octahedron**, the rotation `C₆` gives
`T^3=κ`, and — with three axes — the topology of the flags **explodes** into the octonionic Fano plane.

---

## Chapter IV. The Octahedron and the Fano Explosion (Rank 3)

Rank 3 is the first **complete** scene: three independent axes, an octahedron, a rotation with a half-turn equal to `κ`. Here the single
Hamming distance splits for the first time into **three relations**, out of which the octahedron, its axes, and
the observer are all assembled. And here too a topological explosion occurs: the homology of the building of the lattice `𝔽_2^3` inflates into a bouquet of eight
circles — the incidence graph of the Fano plane, encoding octonion multiplication. The chapter carries rank 3 from three
relations to Fano.

### 4.1. The Active Scene

The number `30=2\cdot3\cdot5` gives the cube `Q_3=D(30)` (ch. II). Removing the poles `\{000,111\}` (where there is nothing to distinguish),
we obtain the **active scene** — six points:

$$U_3 = Q_3\setminus\{000,111\} = \{001,010,100,\ 011,101,110\},\qquad |U_3|=6.$$

Two weight layers of three points each — weight `1` (`\{001,010,100\}`) and weight `2` (`\{011,101,110\}`) — which `κ` exchanges
(`κ(001)=110`). The scene has grown from the two points of rank 2 to six; the whole further structure is determined by these
six points.

### 4.2. ★Three Relations `R₁, R₂, R₃`

The figure is set by the way its points differ. On a Boolean carrier, difference is measured in a single way —
by **Hamming distance** `d` (the number of diverging coordinates); there is no other measure. On `U_3` it takes the values
`1,2,3` and partitions all `15` pairs into three relations (`6+6+3=15`, `[●]` `code_number_model/verify_octahedron_relations.py §A`):

| relation | distance | figure | what it carries |
|---|---|---|---|
| **`R₁`** | `d=1` | `C₆` — a six-cycle `100{-}110{-}010{-}011{-}001{-}101{-}100` | cycle / transition (each step changes weight) |
| **`R₂`** | `d=2` | `2\cdot K₃` — two triangles `\{100,010,001\}`, `\{110,101,011\}` | split / two layers |
| **`R₃`** | `d=3` | `3\cdot K₂` — three pairs `\{100,011\},\{010,101\},\{001,110\}` | full opposition `y=κ(x)` — three axes |

Each pair of points lies in exactly one relation: the six-point scene carries **three consistent readings at once**.
`R₃` is the action of `κ` (`2^{n-1}-1=3` pairs), and these three pairs become the three directions of distinction (§4.5).

### 4.3. The Octahedron and the Spectral Theorem

The union `R_1\cup R_2` sets adjacency: each point has four neighbors (two by `R₁`, two by `R₂`), and only its antipode `κ(x)` is
non-adjacent. A graph in which every vertex is adjacent to all but its opposite is the complete tripartite graph

$$R_1\cup R_2 = K_{2,2,2} \qquad [●]$$

— the skeleton of the **octahedron**, whose three parts are the three `κ`-pairs of `R₃`. The octahedron is the active scene of the cube `Q_3` with the poles removed;
the two figures are dual. The figure is forced as minimal: the octahedron is the cross-polytope at `n=3`, the smallest
architecture built from orthogonal antipodal axes with a forbidden center.

The octahedron carries a Laplacian with spectrum `\{0,4,4,4,6,6\}` — **even**, and evenness is a theorem (`code_number_model/verify_kappa_spectral_theorem.py`):

> **Theorem (spectrum "complete minus a perfect matching").** For the complete graph on `m` (even) vertices minus any
> perfect matching, the Laplacian spectrum is `\{0,\ m{-}2\ (\text{mult. } m/2),\ m\ (\text{mult. } m/2{-}1)\}`. `[●]`

**Proof (core).** `L=(m-1)I-J+P` (`J`=the all-ones matrix, `P`=the pair permutation); `J` and `P` **commute**
(a permutation of pairs preserves `\mathbf 1`), hence they are simultaneously diagonalizable. `∎` Since `m=2^n-2` is even and the
spectrum is even, `e^{iL\pi}=I` **at every rank** — arithmetic of even numbers. Control: the star `K_{1,3}` (spectrum with an
odd `1`) does not give this; the theorem pertains to the family "complete minus a perfect matching."

### 4.4. Rotation and Holonomy: the Shift `T` and the Transport `𝒯`

The cycle `R_1=C_6` carries its own motion — a **shift** `T` by one step, `T^6=\mathrm{id}`. Its half-period sends
each point to its antipode:

$$T^3 = κ \quad\text{on } U_3. \qquad [●]$$

A strict half-turn, provably equal to `κ`, is attainable only with `C_6`; on `C_4` there is none.
But **the shift `T` must be distinguished from the holonomy `𝒯`** (`code_number_model/verify_octahedron_relations.py §B`):

- the **shift `T`** (order 6) **permutes the points** of the cycle;
- the **transport `𝒯`** — a twisted carrying-over with sign `\pm1` on the traversal: one traversal changes the sign, a return
  requires a second, `𝒯^2=\mathrm{id}`.

The strict form of the **Möbius band** is carried by the transport `𝒯`. The mechanism is exact: the quotient `C_6/κ = C_3` (three `κ`-classes),
and the covering `C_6\to C_3` is **connected**: a loop in `C_3` lifts to a path of length `3` (`=T^3=κ`, the opposite
side). This is the nontrivial class `H^1(S^1;\mathbb Z/2)\cong\mathbb Z/2`: a discrete
one-sidedness, where the discrete and continuous sides are one surface, glued by `κ`, with a fixed core
`σ½` `[◐]`. The simplex `\{e,i,\pi\}` closes here: `e^{i\pi}=κ` (ch. VII).

### 4.5. The Observer: Center and Projective Quotient

The observer at rank 3 reads in **two ways**, and both are needed.

**As center.** The invariant of `κ` — the fixed point — is absent among the states (`κ(x)=x` is unsolvable over `𝔽_2`).
Embedding `U_3` into `\mathbb R^3` as the octahedron `\pm e_1,\pm e_2,\pm e_3`, we see the three `κ`-pairs as three axes through the origin; in
this embedding the three axial involutions have one common fixed point — the center `c=(½,½,½)\notin Q_3`. This is `σ½`,
lying on the continuous side `|·|∞`.

**As projective quotient.** Identifying each `κ`-pair, we obtain the **space of axes** `[●]`:

$$U_3/\kappa \cong PG(1,2) = \{\,\text{three points}\,\}, \qquad U_n/\kappa \cong PG(n-2,2),\ \ |U_n/\kappa|=2^{n-1}-1.$$

Here the observer is the **self-factorization of the scene**: opposite directions
of the active carrier collapse into the axes of one projective geometry (`code_number_model/verify_octahedron_relations.py §E`). At rank 3
this is `PG(1,2)` (three axes), at rank 4 — `PG(2,2)` (Fano), at rank 5 — `PG(3,2)`. The two readings are complementary: `σ½` is the
center, from which the axes are radial; `U_n/κ` are the axes themselves. The connection is the **growth law** `Q_{n-1}^\ast\cong U_n/\kappa`
(ch. II, ch. VII): the content of a rank becomes the axes of the next, and in this sense the observer of rank `n` is that which
makes rank `n+1` possible `[◐]`.

### 4.6. ★The Fano/Tits Explosion

The octahedron gives the skeleton of the scene; its content is revealed by the **topology of the flags**. The Tits building of the lattice of subspaces of `𝔽_2^n`
(the order complex), by the Solomon–Tits theorem, is contractible to a bouquet of spheres in a single dimension, whose rank is the
dimension of the **Steinberg module**:

$$\dim \mathrm{St}_n = 2^{\binom{n}{2}}. \qquad [●]$$

For `𝔽_2^3` this is `2^{\binom32}=2^3=8`. The bouquet of eight circles is the **incidence graph of the Fano plane** `PG(2,2)`:
seven points and seven lines — `14` vertices, `21` edges, `b_1=21-14+1=8`. And `\dim\mathrm{St}_3=b_1=8` `[●]`
(`code_number_model/verify_rank_map.py §E`; `code_number_model/verify_sheaves_rank_info.py`).

The Fano plane encodes **octonion multiplication**: its seven points are `\mathrm{Im}\,\mathbb O`, each line a quaternionic triple; the Hurwitz limit
`1,2,4,8` (`\mathbb R,\mathbb C,\mathbb H,\mathbb O`), and `\dim\mathrm{Im}\,\mathbb O=7` is the number of points of Fano.

> **Rank note (cross-check with document 01).** `𝔽_2^3` (the Tits building) gives the Fano plane `PG(2,2)`, whereas in the rank
> tower of DOT `PG(2,2)` appears as the **directions of rank 4** (`U_4/κ`, document 01 chapter IV §4.3; §4.5 above); the three axes of
> rank 3 are `PG(1,2)`. The Steinberg-`8` = the homology of the building `𝔽_2^3`, whose projectivization is `PG(2,2)`. Hence
> the Fano explosion is the transition **rank 3 → 4**: the three axes `PG(1,2)` grow into the plane `PG(2,2)`, and its incidence homology
> gives `b_1=8`. (Steinberg homology is unfolded only here, in the number model.)

**Boundary.** The mathematics of the explosion is `[●]` (Solomon–Tits, Steinberg), and lies on the bit side
(document 02). The Hurwitz limit `1,2,4,8` is the classification of division algebras, pure algebra. The topology of
Fano inflates at rank 3 as a combinatorial fact `[●]`.

### 4.7. The Arithmetic Octahedron: the Divisors of 30

The same figure has an exact **numerical avatar** (`code_number_model/verify_octahedron_relations.py §C`). The proper divisors of
`30=2\cdot3\cdot5` (excluding `1` and `30`) are exactly six: `\{2,3,5,\ 6,10,15\}`, and under the isomorphism `D(30)\cong Q_3`
(divisor ↔ set of primes) the three Hamming relations read arithmetically:

| relation | arithmetic | pairs |
|---|---|---|
| **`R₃`** (`d=3`) | conjugate divisors `d\leftrightarrow 30/d` | `\{2,15\},\{3,10\},\{5,6\}` |
| **`R₂`** (`d=2`) | primes `\{2,3,5\}` ↔ semiprimes `\{6,10,15\}` | two layers |
| **`R₁`** (`d=1`) | differing by one prime factor | `2\to6\to3\to15\to5\to10\to2` |

The proper divisors of `30` form the same octahedron; for `210=2\cdot3\cdot5\cdot7` the seven conjugate pairs of divisors
correspond to the seven points of the Fano plane (`Q_3^\ast\cong U_4/κ`). Number realizes the octahedron and Fano on a par with color.

### 4.8. Realization: Color and Graph

**Color** (reference: the RGB/Kuhn bridge). The RGB cube `Q_3` (axes red, green, blue) with the poles `000` (black) and `111`
(white) removed gives six saturated hues, and the three relations color exactly (`code_number_model/verify_octahedron_relations.py §D`):

| | color | relation |
|---|---|---|
| **`R₁`** | the hue circle `R\to Y\to G\to C\to B\to M\to R` | neighboring transitions |
| **`R₂`** | triads `RGB` (weight 1) / `CMY` (weight 2) | split light/pigment |
| **`R₃`** | complements `R\leftrightarrow C,\ G\leftrightarrow M,\ B\leftrightarrow Y` | opponent axes (`κ`) |

`RGB/CMY/Lab/HSB` are **four maps** of one 3-dimensional octahedron, organized by the group
`B_3=(\mathbb Z/2)^3\rtimes S_3` (`|B_3|=48`); these are **three projections**: `HSB` linearizes the cycle `R₁` (hue=angle on `C_6`,
half-turn `180°`=`T^3=κ`=complement), `RGB/CMY` is the split `R₂`, `Lab` is the opposition `R₃` (axes `a,b`), and lightness
`L` is the observer (measured `L`=DC=frequency, `0.874`, ch. VIII). The continuous body `[0,1]^3` splits into six
Kuhn sectors (six orderings of `S_3`), where `HSV` formulas give local coordinates `[◐]`.

**Graph.** The octahedron `K(2,2,2)`, the cycle `C_6`, and the three relations `R₁/R₂/R₃` are graph facts, computed on matrices; the
graph lens (ch. VIII) shows them directly, and the spectral theorem pertains to the same graph `[●]`.

### Summary

At rank 3 the single relation of difference — Hamming distance — splits into **three**: `R₁=C_6` (cycle),
`R₂=2K_3` (split), `R₃=3K_2` (three axes); `R_1\cup R_2=K_{2,2,2}` — the octahedron `[●]`. Its own motion
gives the strict half-turn `T^3=κ`, and the transport `𝒯` (`𝒯^2=\mathrm{id}`) gives the Möbius band `[●]`. The observer reads
two ways — the center `σ½` and the projective quotient `U_3/κ=PG(1,2)` `[●]/[◐]`. The event of the rank is the **Fano/Tits
explosion**: Steinberg `2^{\binom32}=8` = the incidence graph of Fano = `\mathrm{Im}\,\mathbb O` `[●]`. The octahedron
is realized in three avatars: numerical (the divisors of `30`), color (`RGB/CMY`, three projections of `B_3`), and graph-theoretic.

Chapter V crosses a **threshold**: the composite rank `4=2\times2` gives the first break `Q_2\square Q_2`, the middle layer
separates, and `i=√κ` enters the continuum; there too the lift continues to predict higher figures — Fano and Petersen.

---

## Chapter V. The Break and the Continuum (Rank 4)

Rank 4 is the first **composite** rank: `4=2\times2`. Here the tower splits in two for the first time, the middle layer
separates from the poles, and — more consequentially for number — the **imaginary unit** `i=√κ` enters the structure, and with it
the passage to the continuous side. Rank 4 is the boundary past which the discrete root steps off the finite cycle onto the
circle.

### 5.1. The Break `Q₄=Q₂□Q₂`

A composite rank is a **product** of carriers: `Q_4=Q_2\square Q_2`, the Cartesian product of graphs, with
coordinatewise `κ=κ_2\otimes κ_2`. Ranks **add** — `Q_a\square Q_b=Q_{a+b}` — and this is the monoidality of the lift
(ch. VII). In numbers this is the `\times` of coprimes: `D(6)\times D(35)=D(210)`, `Q_2\square Q_2=Q_4` `[●]`
(`code_number_model/verify_functor_operations.py §C`).

The first composite rank is the one where **the axis system splits in two for the first time**: `4=2\times2` is that very break,
at which in the general theory `\mathfrak{so}(4)=\mathfrak{su}(2)^2` decouples, and the middle weight layer separates as an
internal layer, standing apart from the poles (unlike ranks 2–3). Number sees this break as a **tensor** doubling of the
cube.

### 5.2. `i=√κ`: the Boundary of Discrete and Continuous

At rank 2 the sign of the self-relation was `\pm1` (a reflection, `T^2=κ` on `C_4`); at rank 3 — the half-turn `T^3=κ` on `C_6`.
Let us ask about the **quarter-turn** — the root of `κ`:

$$i^2 = -1 = κ, \qquad i = √κ.$$

Does `i` exist discretely? On the cycle `C_n` a quarter-turn exists only when `4\mid n`. On `C_6` (rank 3) it is **absent**
(`i^6=-1\ne1`): `√κ` is discretely absent. It appears where the period is divisible by 4 — on `C_4`, `C_8` `[●]`
(`code_number_model/verify_operator_ladder.py §D`, `code_number_model/verify_rank_map.py §F`).

> **Meaning.** `i=√κ` is the **first root requiring continuity**. The discrete side takes the finite roots `C_{2^k}`;
> a quarter-turn on six sectors is impossible, on a circle it is possible. Rank 4 (`4\mid4`) is the first place where `i`
> discretely exists; but its true home is the circle. `i` is a marker of the **passage into the continuum**, where reflection
> `(\pm1)` gives way to rotation `(\pm i)`.

Hence the simplex `\{e,i,\pi\}` — three invariants of `\exp:(\mathbb C,+)\to(\mathbb C^\ast,\times)`, and this is a **forced hierarchy of roles** along the base/exponent axis: `e` is the carrier (the base; the only natural one, `d/dx\,e^x=e^x`; base only), `i` is the operator (the angle; `√κ`, order 4), `\pi` is the measure (the period; the half-period).

The asymmetry is forced by type and is the **projection of `\iota^2=\mathrm{id}`**: `e^{i\pi}=κ` is the involution itself, `(e^{i\pi})^2=e^{i2\pi}=\mathrm{id}` is its order 2 `[●/◐]` (`code_number_model/verify_simplex_center.py §F`).

At rank 3 spin is realized as **real** `\mathfrak{so}(3)`
(the structure constants `\varepsilon_{ijk}` are real, `i` is not needed); complexification is a separate step into the
continuum, and it arrives here `[●/◐]`.

### 5.3. What Comes Next Up the Tower

Rank 4 in the numerical branch is **thin**: the break in the axis system and the **matter-body** (the separated middle layer `S₂`)
are unfolded in document 01 (chapter IV) `[●]` by reference.
What corresponds to number is the **entry of `i`** into the continuum — this is its share of rank 4. The modular layer `4/5`
(`SL(2,\mathbb Z)`, the `j`-invariant, Hecke operators) is classical `[●]`, but its connection to rank `\omega(N)` remains open (`SL(2,\mathbb Z)\ne`
the lattice of divisors): we take it as a **pointer** `[○]` — an open front, where the underside grows.

### 5.4. Further Up the Tower: Fano, Petersen, the Mersenne Horizon

The lift `Q_{n-1}^\ast\cong U_n/\kappa` (ch. IV §4.5) continues to predict figures of discrete geometry, and this is
**the combinatorics of number**. The space of axes grows as a projective tower:

$$U_n/\kappa \cong PG(n-2,2):\quad PG(1,2)\,(3,\text{rank }3)\ \to\ PG(2,2)\,(7,\text{Fano, rank }4)\ \to\
PG(3,2)\,(15,\text{rank }5)\ \to\ \dots$$

★**The Petersen graph appears twice** (`code_number_model/verify_octahedron_relations.py §F`). At rank 5 the middle layer `S_2^{(5)}` is
the ten two-element subsets `\{i,j\}\subset\{1,\dots,5\}`; the relation of disjointness (`d=4`) is the Kneser graph
`KG(5,2)` — the **Petersen graph** (10 vertices, 3-regular, spectrum `\{3,1^5,(-2)^4\}`, triangle-free).
At rank 6 the quotient `S_3^{(6)}/\kappa` (ten axes) gives Petersen a second time, through complements in a five-element
set. One figure, two appearances by different mechanisms — the combinatorial self-similarity of the construction `[●]`.

★**The Mersenne horizon** (`code_number_model/verify_octahedron_relations.py §G`). The number of axes `|U_n/\kappa|=2^{n-1}-1`. The Singer cycle
acts transitively on the points of `PG(n-2,2)` for every `n` — this is classical, and does not by itself discriminate; the content of the
horizon is the **order** of the cycle. When `2^{n-1}-1` is a **Mersenne prime**, the Singer group has prime order:
every one of its nontrivial elements is a full cycle on all axes, and there are no proper suborbits `[●]`. This singles out the ranks

$$n=3,4,6,8,14,\dots\qquad(n-1=\text{the Mersenne exponent}).$$

At rank 5 the order is composite (`2^4-1=15=3\cdot5`): the cycle has proper subgroups of orders 3 and 5, and the rotation of
axes splits into short suborbits. The connection of this sequence with the Gauss–Wantzel theorem on constructible
polygons is `[○]` a front: a pattern, not a derivation.

> **Refinement of the shares by rank.** Ranks 5–6 carry rich **discrete geometry** (Petersen, `PG(3,2)`, `PG(4,2)`)
> — the numerical/combinatorial side; ranks 7–8 (height, closure — document 01, chapters V–VI) lie outside the numerical series.
> The numerical series covers the higher ranks combinatorially as well.

### 5.5. Realization: the Quarter-Turn

**Graph/color.** On the hue circle (rank 3, six sectors) there is no quarter-turn — six is not divisible by four; it appears
only on the continuous circle, between the discrete colors. `i` is a rotation by `90°` in the body, unattainable on the six vertices
`[◐]`. Thus the boundary of discrete/continuum is seen directly: `κ` (`180°`) is attainable on the cycle, `√κ` (`90°`) — only on the
circle.

### Summary

Rank 4 is the first composite: `Q_4=Q_2\square Q_2`, the tensor doubling of the cube, the first break in the axis system `[●]`. And
the boundary of the continuum: `i=√κ` is discretely absent on `C_6` (rank 3) and appears where `4\mid n` — the **first root
requiring continuity** `[●]`; reflection `(\pm1)` gives way to rotation `(\pm i)`, closing the simplex
`\{e,i,\pi\}`. The modular layer `4/5` is a pointer `[○]`, an open front. To number, rank 4 gives the entry of `i`.
Further up the tower the lift predicts Fano and Petersen **combinatorially** (§5.4) — the numerical side of the higher ranks `[●]`.

Chapter VI turns its gaze to the **underside**: if `+\times\hat{}\,!` grow outward, then `-\div\log` go inward —
the p-adic tower, `\Gamma` with its poles, the inversion `\mu`; and `\prod_v|x|_v=1` balances both sides of the seam.

---

## Chapter VI. The Underside: Two Sides of the Seam

Everything set out so far has looked **outward**: the growth of the sequence, the cube, the octahedron, the lift — the operations
`+\ \times\ \hat{}\ !`, total, growing. But from the seam `σ½` there is also a way **inward**. The forward operations are closed in `\mathbb N`;
the inverse ones — `-\ \div\ \log` — are partial, and the standard view takes the total side, hiding the partial one. This chapter
restores the **mirror**: the partiality of the inverse operations is a **p-adic tower inward**, and the seam
is symmetric — both sides are equal partners, and `\prod_v|x|_v=1` balances them exactly.

### 6.1. Why the Gaze Goes Outward

The tower of hyperoperations is built forward: `\mathrm{succ}\to+\to\times\to\hat{}\to\dots`, and all of them are **total** —
`a+b`, `a\cdot b`, `a^b`, `a!` are always defined. The inverses are partial: `a-b\in\mathbb N` only when `a\ge b`;
`a/b\in\mathbb Z` only when `b\mid a`; `\log_b a\in\mathbb N` only when `a=b^k`. This is the reason for the one-directionality:
mathematics takes the total side. But partiality is **the structure of the internal side**: where an inverse operation
is "undefined in `\mathbb N`," it **goes inward**.

### 6.2. The Mirror: the Same Operation, a Second Eye

Take `\times p`. The archimedean magnitude `|x|_\infty` **grows**: `1,2,4,8`. But the p-adic `|x|_p=p^{-v_p(x)}`
**shrinks**: `1,\tfrac12,\tfrac14,\dots` — the same action **plunges inward**, into the tower of divisibility. One operation,
**two eyes**: the archimedean (growth outward) and the p-adic (submersion inward). The internal side is real — it is measured by
`|·|_p` `[●]` (`code_number_model/verify_two_sided_seam.py §B`). Thus `\div p` (partial outward) is a descent down the tower
(total inward): the "partiality" of inverses in `\mathbb N` is a **projection** of the two-sided picture onto one side.

The height of the floor `v_p` (ch. II, ch. V) is this internal count: the motion `\hat{}` (multiplicity) grows the cube
**inward**, while `\times` grows it **outward** (new axes). `\hat{}\perp\times`: floor versus axis; `\mu` is blind
to the floors — the cube does not see the underside, the underside is measured by `|·|_p`.

### 6.3. The Product Formula `∏_v|x|_v=1` and Its Reading

By Ostrowski's theorem, all valuations of `\mathbb Q` are the single archimedean `|·|_\infty` and the tower of p-adic `|·|_p`,
linked by an exact equality:

$$|x|_\infty\cdot\prod_{p}|x|_p = 1. \qquad [●]$$

This is a **standard fact about valuations** (layer (V) of the base definitions; `7\to 7\cdot\tfrac17=1`,
`\tfrac{12}5\to 2.4\cdot0.4167=1`, `code_number_model/verify_two_sided_seam.py §C`). The formula is an algebraic identity, not an image:
`∏_p|x|_p=1/|x|_\infty` follows from the canonical factorization.

Reading the equality as the **"law of conservation of the seam"** — that whatever grew outward, `|·|_\infty`, plunged inward
by exactly as much, `|·|_p` — is `[◐]` a **reading**: it links the identity to the picture of two sides around `σ½`. Looking only at
`|·|_\infty` is to see half; but "two-sidedness" as a single seam is recognition, not a theorem. The same form,
"the full set → the neutral element," is seen in Euler's identity (ch. I, `\sum=\prod_p`) and in the discrete `\sum_k(-1)^k C(n,k)=0`.

A radial reading of the same equality — the outward radius of a number as the sum of its depths inward across the p-adic trees — is the bridge note `Bridges/radial_bridge.md`.

### 6.4. The Factorial Is Two-Sided: `Γ`

The factorial seems to stand apart from `+\times\hat{}`. This is an illusion of one side. Its continuation is the `\Gamma`-
function, and it has a **reflection**:

$$\Gamma(s)\,\Gamma(1-s) = \frac{\pi}{\sin(\pi s)}. \qquad [●]$$

Symmetric under `s\mapsto1-s` — the same `κ` as `x\mapsto1-x` (the cube) and `s\mapsto1-s` (zeta) `[●]`
(`code_number_model/verify_two_sided_seam.py §E`). At the same time `n!=\Gamma(n+1)` is the outward half (growth), while the **poles** of `\Gamma` at
`0,-1,-2,\dots` are the internal half (the negative integers); the fixed point of `s\mapsto1-s` is `½=σ½`, and `\Gamma(½)^2=\pi`
— the reflection at its extremum on the seam. The factorial is a **canonically two-sided** object, stitched by `s\mapsto1-s` at `σ½`.
The same holds for zeta: `\xi(s)=\xi(1-s)` — the sum `\sum` (outward) `=` Euler's product `\prod_p` (inward), stitched at `σ½`.

### 6.5. Inversion: `μ` as the Alternating Side

Every forward operation has an internal mirror, and for summation it has a name. **Möbius** `\mu` is the **inversion**
of zeta: `\mu*\zeta=\delta`, that is, `\sum_{d\mid N}\mu(d)=[N{=}1]`, and analytically

$$\frac1{\zeta(s)} = \sum_{n\ge1}\mu(n)\,n^{-s} = \prod_p\bigl(1-p^{-s}\bigr). \qquad [●]$$

And `\mu(N)=(-1)^{\omega(N)}` is the **sign of a vertex** of the cube — the same `Z/2` sign as the singlet/triplet of the holonomy (ch. III).
Thus the `Z/2`-holonomy in the number model **is the Möbius function**: one object, two roles — inversion (the underside of `\zeta`)
and the sign of statistics. The totient `\varphi=\mu*\mathrm{Id}` is also inversion (`code_number_model/verify_functor_operations.py §F`).

### 6.6. The Base-Change Guard

So that two-sidedness does not reduce to a mysticism of `½`, we apply the base-change guard.
Under base changes `\varphi=a\cdot t+b` the fixed point of the involution **always** exists (an invariant `[●/◐]`), while the number
`½` itself **shifts** (a mirage of normalization `[✗]`). The verdict is the same throughout: `σ½` is "the fixed point of `κ`,"
**not** a numerology of "exactly `½`." And: `\log` is base-independent (`\log_b=\log/\log b` is merely a scale), `!=k!` is the number
of maximal chains of the cube (structural, not "the magic of the factorial") `[●]` (`code_number_model/verify_functor_operations.py §H`).

### 6.7. Realization: Additive and Subtractive

The two sides of the seam are **two streams of color**. `RGB` is the additive system (light): starting at `000` (black),
**adding** → `111`; a stream outward from emptiness. `CMY` is subtractive (pigment): starting at `111` (white),
**subtracting** → `000`; a stream inward from fullness. The complement `R\leftrightarrow C` is `κ`, the opponent pairs are the axes
of the octahedron. Two opposite streams around one lightness axis `[◐]`. The factorial is **light** (the whole spectrum of factors);
the choice of primes is the **projection onto atom-filters** (ch. VIII).

### Summary

From the seam a way also leads **inward**: the forward operations `+\times\hat{}\,!` are total (outward, `|·|_\infty`), the inverse
ones `-\div\log` are partial — this is the p-adic tower inward (`|·|_p`) `[●]`. `\prod_v|x|_v=1` is the law of conservation of the seam
(outward = inward) `[●]`. The factorial/`\Gamma` and zeta are two-sided objects, stitched by `s\mapsto1-s` at `σ½` `[●]`.
`\mu` is the inversion of `\zeta` and the sign of `Z/2`-holonomy `[●]`. The base-change guard holds `σ½` invariant, `½` a mirage `[✗]`.
Color shows the two sides as additive/subtractive. The complete picture of number is **the two sides of the seam**.

Chapter VII gathers everything into **one construction**: `\iota^2=\mathrm{id}` unfolds along two axes, the operations `+/\times/\hat{}`
generate them, `\exp` is the bridge, and the morphisms are uniform across ranks and across the two models — bits and numbers.

---

## Chapter VII. The Functorial Layer: the Tower of Ranks as a Single Construction

Until now we have proceeded step by step — rank by rank. This chapter looks at the **construction** of growth itself: at the fact that
all morphisms are uniform across ranks, that two axes of growth are generated by the operations `+/\times/\hat{}`, that `\exp` stitches
them together, and that one and the same construction is realized **in two models** — on bits and on numbers. Number ceases to be "similar" to
the structure and turns out to be its second rigorous realization. At the end the chapter states precisely what, out of the deep
functorial core, is **posited** here.

### 7.1. The Root: `ι²=id`

The functor is not built anew at every rank. **One root** — the zero invariant `\iota^2=\mathrm{id}`, the minimal
nontrivial involution, the self-identity of the distinction "this / not-this." From it come the carrier (orbits of `\iota` → bits →
`Q_n=\iota^{\,n}`), the complement `κ` (`\iota` on all coordinates), the observer `σ½` (the fixed point of `\iota`, outside the
carrier), the holonomy (the sign of `\iota`, `\pm1`). `κ^2=\mathrm{id}` holds in **both** models — in bits (`x\mapsto1-x`)
and in numbers (`d\mapsto N/d`) `[●]` (`code_number_model/verify_functor_layer_general.py §A`; `code_number_model/verify_functor_synthesis.py §A`).

### 7.2. Two Axes

From the root come two independent unfoldings:

$$
\underbrace{Q_n=\iota^{\,n},\ \ \Lambda_L\dashv\pi\dashv\Lambda_R}_{\text{axis of DIMENSION (discrete)}}
\qquad\Big|\qquad
\underbrace{\mathrm{id}\to κ\to i\to\dots}_{\text{axis of ANGLE (continuous)}}
$$

The **dimension axis** grows the number of axes (ranks, lift). The **angle axis** divides the period: roots of the identity `\mathrm{id}\to
κ=\sqrt{\mathrm{id}}\to i=\sqrt{κ}\to\dots`, periods `1,2,4,8`; the discrete side takes the finite `C_{2^k}`, the continuous side takes the whole
circle. `i=\sqrt{κ}` is the first root requiring continuity (ch. V). Ranks grow dimension, roots divide
angle — the axes are orthogonal `[●]` (`code_number_model/verify_functor_layer_general.py §E`).

### 7.3. The Morphisms Are Uniform — and `κ` Permutes the Lifts

Every morphism is given by **one formula at every rank** and is consistent with the lift (checked for `n=1..4`): `κ` (`κ^2=id`),
the lift `\Lambda_L\dashv\pi\dashv\Lambda_R` (`\pi\circ\Lambda=\mathrm{id}`), the projection (`\pi\circ κ=κ\circ\pi`), two
gradings. The key point is that **`κ` exchanges the two lifts**:

$$κ\circ\Lambda_L = \Lambda_R\circ κ. \qquad [●]$$

`κ` **swaps the left and right** lifts: to lift and then complement equals to complement and then lift, into the other
branch. This is a **natural transformation** and the **structural origin of left/right** — two adjoint
lifts, exchanged by `κ` `[●]` (`code_number_model/verify_functor_layer_general.py §B`).

### 7.4. Two Gradings and Holonomy

The scene carries **two** gradings (established at rank 2, ch. III):

- `H` (Hamming) — the number of active axes `\omega`; `H\circ κ=n-H`, symmetric around `σ½` (bond, set);
- `P` (position) — the value; `P\circ κ=(2^n-1)-P`, carries the **arrow** (order).

The source of direction is `P` `[●]`. And the `Z/2`-holonomy is uniform: at rank `n` the cycle `C_{2n}`,
`T=e^{i\pi/n}`, `T^n=κ`, `T^{2n}=\mathrm{id}` — `Z/2=\langle κ\rangle\hookrightarrow C_{2n}` at **every** rank
(rank 2: `C_4`, `T^2=κ`; rank 3: `C_6`, `T^3=κ`) `[●]` (`code_number_model/verify_functor_layer_general.py §§C,D`).

### 7.5. The Operations Generate the Axes; `exp` Is the Bridge

The two axes are **grown by the operations** `+/\times/\hat{}` (the tower of hyperoperations: `\times`=iteration of `+`,
`\hat{}`=iteration of `\times`, ch. VI). Each generates its own facet `[●]` (`code_number_model/verify_functor_operations.py`):

- **`\times`** generates the axis of **dimension**: `Q_a\square Q_b=Q_{a+b}` (rank adds), two realizations —
  `D(MN)=D(M)\times D(N)` and CRT for `\mathbb Z/n`;
- **`\exp`** generates the axis of **angle**: the monoid isomorphism `(\mathbb R,+)\to(\mathbb R_+,\times)`, and the roots of the angle axis
  lie on its image — `e^{i\pi}=κ`, `e^{i\pi/2}=i`. `\exp` carries `+\to\times` **and** discrete→continuum at once:
  it is the **bridge between the two axes**;
- **`\hat{}`** generates the **underside**: the height `v_p`, breaks the cube, `|·|_p` inward (ch. VI).

> **Meaning.** The angle axis is `\exp` of the additive tower: the discrete half-periods `\pi/2^k`, under `\exp`, become points of the
> circle. The boundary `i=\sqrt{κ}` (`4\mid n`) is the place where the discrete root steps off the finite cycle onto the circle, and
> `\exp` is the operator of this passage. `e^{i\pi}=κ` itself is the root `\iota^2=\mathrm{id}` (§7.1), projected into the
> continuum: the forced hierarchy of roles `e` (carrier) / `i` (operator) / `\pi` (measure), ch. V §5.2. `[●/◐]`

### 7.6. Two Models: Number as the Tuning Fork

The morphisms are uniform across ranks **and across models**. The functor `\Lambda:S\mapsto\prod p` (ch. II, T6) is,
on squarefree numbers, an isomorphism of categories "sets of primes ≅ numbers," and one morphism **coincides in both
models** under `\Lambda`: `κ` (complement ↔ `N/d`), `H` (Hamming ↔ `\omega`), the lift (`+`axis ↔ `\times`prime), `\pi`
(forget an axis ↔ remove a factor) `[●]` (`code_number_model/verify_functor_synthesis.py §B`). Number is the **second independent model** and
thereby the **tuning fork of functoriality**: what holds in both models is the functor of the construction; what holds only in one is a
shell above it. And `\mu` in numbers is at once the inversion `\zeta^{-1}` **and** the sign of `Z/2`-holonomy (ch. VI).

### 7.7. Boundary of the Layer: Derived and Posited

The deepest theorems of the functorial core are proved on the **bit** side (document 02, 385 checks;
in expository prose — document 01, chapter VIII); the frame of `\iota^2=\mathrm{id}`
**places** them, and here a precise qualification is needed:

- the **monad and terminal** (`\mathbb Z/2\times(-)`, `σ½`=the terminal object) **are derived** from the root: the carrier is the
  free `\mathbb Z/2`-object (`|\mathrm{Hom}(Q_n,Y)|=|Y|^{2^{n-1}}`) → monad → terminal `[●]`
  (`code_number_model/verify_functor_synthesis.py §C`);
- the **growth law** `PG(n-1,2)\cong U_{n+1}/κ` (the content of a rank becoming the axes of the next) **is posited**:
  the count `2^n-1` comes from `\iota^2=\mathrm{id}` (orbits), but `PG\cong U/κ` as an **isomorphism of projective spaces**
  (lines→lines) requires a **linear** input (the shift `a\mapsto2a`), beyond a single involution. It lies `[●]` within the
  functorization; the frame places it on the axis of dimension as `[○]` (`code_number_model/verify_functor_synthesis.py §D`).

The complete picture of the seam between the two models belongs to the synthesis section of the full corpus (not included in the package): bits carry **structure** (`|·|_2`), numbers carry **height
and underside** (`|·|_\infty`: `\hat{}`, `P`), invisible to bits; `\exp` is the bridge between the sides; `\prod=1` in two forms (discrete
`\sum(-1)^k C(n,k)=0` = p-adic `\prod_v|x|_v=1`) is the seam itself, in the form of a law.

### Summary

The tower is **one construction**: from the root `\iota^2=\mathrm{id}` come two axes (dimension `\times`/lift, angle
`\exp`/roots), the morphisms are uniform across ranks `[●]`; `κ` exchanges `\Lambda_L\leftrightarrow\Lambda_R` —
a natural transformation, the origin of left/right `[●]`; two gradings `H\perp P` and `Z/2`-holonomy `[●]`; the operations
`+/\times/\hat{}` generate the axes, `\exp`=the bridge, `\hat{}`=the underside `[●]`; number is the second model-tuning fork, `\mu`=inversion
=the sign of `Z/2` `[●]`. The monad/terminal are derived from the root; `PG\cong U/κ` is posited (linear input `[○]`), and lies on the
bit side. What is derived from the root is derived; what is posited is named as input.

Chapter VIII makes the accompaniment explicit: **two lenses** — graph (the carrier made visible) and color (a projection) — and the **wall
of values**, explained by metamerism.

---

## Chapter VIII. Two Lenses and the Wall of Values

The construction has been built and named. What remains is to make explicit what has led the exposition all along as an **accompaniment** —
the two lenses of the carrier, graph and color — and to name the **boundary**: what the construction does not generate. Both lenses make visible
one and the same thing, each with its own eye; and both, on reaching their limit, show the **wall of values** — why the specific
number at a vertex is not extracted from the structure. This is the finale: the construction reaches the observer and stops.

### 8.1. Graph — the Carrier Made Visible

The graph is the **carrier itself**: `Q_n` is the hypercube graph, and every morphism is an operation on it `[●]`
(`code_number_model/verify_graph_projection.py`, 8 checks):

| morphism | operation on the graph |
|---|---|
| `κ` | the antipodal automorphism (`κAκ=A`, no fixed vertex, the antipode at distance `n`) |
| lift `\Lambda` | the graph product `\square K_2` (double + connect the copies) |
| `H` | Hamming-distance layers (distance-regular, the scheme `H(n,2)`) |
| holonomy | the cycle `C_6`, the half-turn `T^3=κ` |
| `\mu` | the sign of a vertex `(-1)^{\text{weight}}`; `\sum` = the reduced Euler characteristic `=0` |
| `U_3` | the octahedron `K(2,2,2)` (complete minus a perfect matching), spectrum `\{0,4,4,4,6,6\}` |
| axes | the folded cube `Q_n/κ` (`2^{n-1}` vertices) |

We **draw** the tower of graphs (edge → square → cube → octahedron → cycle), and the functor merely names what has been drawn.
This returns to the exposition its first step — **seeing** — before **naming**.

### 8.2. Color — a Projection of the Carrier

Color is **accompanimental**, yet measured. The octahedron `Q_3` is colored by four maps (`RGB/CMY/Lab/HSB`, ch. IV),
the group `B_3`. And here lies the single **measured** manifestation of the observer: the lightness axis `L` (the constant
component, frequency) — an invariant orthogonal to chromaticity; in the corpus it is measured that `\mathrm{corr}(\text{frequency},DC)=+0.874` `[●]`,
whereas on semantics only `0.02`. The observer is an extractable and removable axis: separation is whitening by lightness `[◐]`.

### 8.3. The Two Lenses Together

Graph and color are **parallel lenses** on one carrier, like `|·|_2` and `|·|_\infty`:

| structure | **graph** (carrier, drawn) | **color** (projection, colored) |
|---|---|---|
| `κ` | the antipodal automorphism | the complement `R\leftrightarrow C` |
| `σ½` | the center, no fixed vertex | lightness `L` (measured) |
| holonomy | the cycle `C_6`, half-turn=antipode | the hue circle, `180°`=complement |
| `H` | Hamming-distance layers | slices of lightness/saturation |

The graph **leads** (what is really there), color **recognizes** (how it looks to the eye). Both are `[◐]` as lenses, `[●]` in
their own facts (graph spectra / color measurements).

### 8.4. ★The Wall of Values: Metamerism

And here is the boundary that both lenses show alike. The precise **value** — which specific number stands at a vertex —
is **not recoverable** from the structure. The reason is visible in color as **metamerism**: different spectra
give a single color, because the three cone types lose information.

In numbers: numbers of **the same rank** `\omega` — `\{6,10,14,15,21,22\}` (all with `\omega=2`) — have one and the same
projection onto the observer (rank / lightness `L`), but different "chromaticity" (different primes). The projection onto `σ½`
**loses chromaticity** — hence values are not extracted from the structure, **just as the eye loses the spectrum in three cone types**
`[◐]` (`code_number_model/verify_color_projection.py §F`). In the graph the same holds: the folded cube `Q_n/κ` loses the distinction between vertices within a `κ`-class.

Color **vividly explains the nature** of the wall: the observer sees a projection, and the spectrum is lost. This is the
same limit that closes off numerical values (the study of factorization; full corpus: there is no speedup of factorization).

### 8.5. The Boundary, Named Precisely

Let us gather the wall into a single list — where the construction ends `[○]`:

- **values** — which specific number stands at a vertex is not recoverable from the rank; it is lost in the projection onto `σ½`
  (metamerism);
- **the Riemann hypothesis** (all zeros on `σ½`) — remains open; the Mertens sum `M(x)=O(x^{1/2+\varepsilon})`
  is equivalent to it;
- **the growth law `PG\cong U/κ`, the monad** — on the bit side (document 02 and the synthesis section of the full corpus), referred there.

The general form of the wall is **form versus interaction**: the discrete side forces the **structure of relations**
(topology — order, `κ`, the minimum `⊥`, the center `σ½`, the hierarchy of roles), but not the **interaction** — the force, the content, the value, lying on
`|·|_\infty`. The same limit is seen in the simplex `\{e,i,\pi\}`: it **has no** forced observer-center —
the metric center (orthocenter/barycenter) is frame-dependent, because it symmetrizes the forced hierarchy of roles (ch. V §5.2);
the forced anchor is on the discrete side (the minimum `⊥` + the `κ`-center `σ½`), while the metric is drawn by the
`|·|_\infty`-content, which the structure does not supply `[○]` (`code_number_model/verify_simplex_center.py`).

The wall is **in one place**: values, on the continuous underside `|·|_\infty`.
The construction reaches the observer `σ½` and **ends**; what lies past the projection is input.

### Summary

Two lenses make the carrier visible: **graph** (`Q_n` is the hypercube graph, every morphism an operation on it, `[●]`) and
**color** (the octahedron colored, the observer measured at `0.874`, `[●/◐]`). They are parallel, like `|·|_2`/`|·|_\infty`: the graph
leads, color recognizes. And both show the **wall of values** — metamerism: the projection onto `σ½` loses chromaticity, values are not
derived `[◐]`. The boundary is named precisely and in one place.

The epilogue returns number to the family of projections of the construction — one of the facets where the observer `σ½` is the common seam.

---

## Epilogue. Projections: Number Among the Facets of the Construction

We have carried number through the ranks — from the first distinction of counting to the functorial layer and the wall of values. What remains is to return it
to its place: **number theory is one projection of the construction of distinction** — its realization on counting. The common
axis running through it is the observer `σ½`.

### What Turned Out to Be Number

Number turns out to be a **tower of cubes**. A squarefree number is the Boolean cube of its primes (`D(N)\cong Q_k`); a prime is
the atom; a composite is the underside; multiplicity is the floor above the cube. Divisibility is the order on the cube, the complement `d\mapsto N/d`
is `κ`, the center `√N` is the observer `σ½` outside the carrier. Zeta stitches together counting (`\sum`) and atoms (`\prod_p`), and
`\prod_v|x|_v=1` balances outward and inward. All of this is the images of morphisms of one construction, realized on counting
`[●]`.

### Number as the Second Model of the Construction

Number is the **second independent model** of the construction, alongside bits `Q_n`: an isomorphism of categories, "finite sets of
primes ≅ squarefree numbers under divisibility" (ch. II). It is therefore a **tuning fork**: what holds both in bits and in
numbers is the functor of the construction; what lies only in one model is a shell above it.

The common axis of both models is the observer `σ½`. In numbers it is `√N` (the center of the self-dual lattice of divisors)
and the line `Re=½` of zeta; both carry the one involution `1-x` with fixed point `½` `[◐]` (the common form is proved, ch. I) —
recognition, not a theorem about the unity of the object.

### Two Lenses, One Carrier

Number is shown by **two lenses**: graph (the carrier made visible — `Q_n` is the hypercube, morphisms are operations on the graph) and
color (a projection — the octahedron colored, the observer measured). They are parallel, like the two sides of the seam `|·|_2/|·|_\infty`;
and both, on reaching their limit, show one **wall**: the projection onto `σ½` loses the spectrum (metamerism), values are not
derived.

### A Final Reckoning

- `[●]` — all the rank mathematics: `D(N)\cong Q_k`, the product of chains, `\mu`, the atlas, CRT, the functor `\Lambda`; the two
  weights `H\perp P`, the **`L^2` body** (Hölder `p=2`); the octahedron, `T^3=κ`, `e^{iL\pi}=I`, **Steinberg `8`=Fano=Im`\mathbb
  O`**; the break `Q_2\square Q_2`, `i=\sqrt{κ}`; `\prod_v|x|_v=1`; the functorial layer.
- `[◐]` — projections: `σ½=Re=½` (one seam), the color/graph lenses.
- `[○]` — input/wall: the Riemann hypothesis, values (metamerism); the center of the simplex `{e,i,π}` is frame-dependent (interaction=`|·|∞`); `PG\cong U/κ`/the monad — on the bit side.

The observer `σ½` is the **first word** (gray between black and white, rank 0/1) and the **last** (that behind which the wall stands).
It holds the tower of cubes together while remaining outside it: the absent midpoint, the invariant of `κ`, the critical line. Number has been presented
structurally and completely; what is proved is separated from what is projected, the wall named precisely. The construction is one — number is one of its
facets, seen from its own angle.
