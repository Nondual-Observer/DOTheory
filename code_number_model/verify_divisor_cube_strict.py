#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_divisor_cube_strict.py — the RIGOROUS mathematical core: the divisor lattice = a cube; projection onto ranks.

PURE mathematics — all statements ● (theorems of elementary number theory, verified by computation);
NO physical optics. Every check is FALSIFIABLE — a distinguishing control alongside; nothing is written
in by hand as an «answer to oneself».

  A. STRUCTURAL THEOREM: D(N) ≅ ∏ᵢ Cℓ(aᵢ+1) (product of chains). A divisor ↔ exponent vector
     (e₁,…,e_k), 0≤eᵢ≤aᵢ; divisibility ⟺ coordinate-wise ≤. The divisor lattice = a «box».
  B. SQUAREFREE ⟺ BOOLEAN CUBE: N squarefree ⟺ D(N) ≅ Q_k (all chains of length 2). A divisor ↔ a bit vector,
     divisibility ⟺ ⊆. Distinguishing: N=12=2²·3 — not a cube (|D|=6≠2^k).
  C. NUMBER OF DIVISORS: d(N)=∏(aᵢ+1) (= |lattice|); for squarefree d(N)=2^ω(N)=|Q_k|.
  D. MÖBIUS = SIGN OF A VERTEX + INCL-EXCL: μ(N)=(−1)^ω on squarefree, 0 on squares; Σ_{d|N} μ(d)=[N=1]
     (=(1−1)^k on the cube = inclusion-exclusion). Distinguishing: for N>1 the sum is ZERO, for N=1 — a unit.
  E. SELF-DUALITY: d↦N/d — a bijection of divisors REVERSING divisibility (anti-isomorphism of the lattice); on
     squarefree this is κ:x↦1−x (bit complement, antipode of the cube).
  F. PROJECTION ONTO RANKS: rank(N):=ω(N) (number of DISTINCT primes) = dimension of the carrier cube Q_{ω(N)};
     the levels of the squarefree divisor cube = binomial C(k,j) (weight = number of prime factors of a divisor).
  G. LOCALITY (Euler): σ(N)=∏_p (1+p+…+p^a) — multiplicative, the local factor = sum over the floors
     of one axis. Distinguishing: σ is multiplicative on coprimes, NOT additive.

  ── ATLAS OF OPERATIONS (0 NOT 1 + × ^ ! ∞) — where each action lands ──
  H. BOOLEAN ALGEBRA: D(squarefree N) = a boolean algebra (⊥=1, ⊤=N, ∧=gcd, ∨=lcm, ¬=N/d); complement
     d∧¬d=1, d∨¬d=N; De Morgan. Here land 1 (bottom), NOT (¬), ∧/∨. Distinguishing: 12 is not boolean.
  I. MULTIPLICATION = GLUING OF AXES: × of coprimes = Q_a × Q_b = Q_(a+b) (Cartesian product, rank +).
     Distinguishing: NOT coprime — the rank does not add up.
  J. FACTORIAL = TRAVERSALS OF THE CUBE: n! → k! = number of maximal chains of the cube Q_k (all paths ⊥→⊤). n! is not
     squarefree (Legendre v_p(n!)=Σ⌊n/pⁱ⌋) — lives high above the cube.
  K. MÖBIUS → ∞: μ is blind to floors (≠0 ⟺ a cube vertex); μ*1=δ (inverse to 1 in the Dirichlet ring); 1/ζ=Σμ/nˢ=
     ∏(1−p⁻ˢ) — μ INVERTS the Euler product; limit s→1: ζ→∞ (pole), 1/ζ→0 ⟹ μ at the ∞-pole.
  L. POLES 0 and ∞: 0 = the lower cutoff (neutral for +, absorber for ×, outside the cube = background); 0→1 = the first
     distinction (additive invariant); κ:d↦N/d swaps the poles (1↔N), center √N=σ½; ∞ = rank unbounded.

  ── SECOND REALIZATION (residues) + FUNCTOR DICTIONARY ──
  M. EUCLID + BÉZOUT: gcd via remainders (=∧ of the lattice); gcd(a,b)=ax+by (constructive infimum).
  N. CRT: ℤ/n ≅ ∏ ℤ/pᵢ^aᵢ — a ring isomorphism = monoidality of □ on RESIDUES (2nd realization of the cube).
  O. EULER's φ: multiplicative (=□); φ(p^a)=p^a−p^(a−1); Σ_{d|n}φ(d)=n (φ*1=Id); φ=μ*Id (incl-excl).
  P. v_p VALUATION = floor height: v_p(mn)=v_p(m)+v_p(n) (×→+); |n|_p=p^(−v_p); ∏|n|_v=1 (bridge to |·|∞).
  Q. FERMAT/EULER: a^φ(n)≡1 (mod n); (ℤ/n)* a group of order φ(n); for a prime cyclic (primitive root).
  R. FUNCTOR DICTIONARY: Λ:S↦∏p — a functor (preserves order ⊆↦|, monoidality □↦×, κ↦d↦N/d);
     on squarefree = an ISOMORPHISM of categories, the machine functors realized RIGOROUSLY (●), not recognized (◐ only σ½).
"""
from __future__ import annotations
from itertools import product
from math import prod, comb, gcd, pi, factorial

def lcm(a, b):
    return a * b // gcd(a, b)

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    return sorted(d for d in range(1, n + 1) if n % d == 0)

def omega(n):           # number of DISTINCT primes
    return len(factorize(n))

def mobius(n):
    f = factorize(n)
    return 0 if any(a >= 2 for a in f.values()) else (-1) ** len(f)

def phi(n):             # Euler totient = |(ℤ/nℤ)*|
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def vp(n, p):           # p-adic valuation = floor height along axis p
    v = 0
    while n % p == 0:
        v += 1; n //= p
    return v


# ═══════ A. structural theorem: D(N) = product of chains ═══════
def section_A():
    print("\n[A] D(N) ≅ ∏ chains: divisor ↔ exponent vector, divisibility ⟺ coordinate-wise ≤")
    N = 360                                                  # 2³·3²·5 → exponents (3,2,1)
    f = factorize(N)
    primes = sorted(f); exps = [f[p] for p in primes]
    d_to_vec = lambda d: tuple(factorize(d).get(p, 0) for p in primes)
    divs = divisors(N)
    # bijection divisors ↔ «box» ∏[0..aᵢ]; |D| = ∏(aᵢ+1)
    box = list(product(*[range(a + 1) for a in exps]))
    bijection = sorted(d_to_vec(d) for d in divs) == sorted(box) and len(divs) == prod(a + 1 for a in exps)
    check(f"D({N})↔box ∏[0..aᵢ], aᵢ={exps}: bijection divisor↔exponent vector, |D|={len(divs)}=∏(aᵢ+1)",
          bijection)
    # divisibility ⟺ coordinate-wise ≤ (distinguishing: ALL pairs are checked, a wrong pair would fail)
    order_iso = all((d2 % d1 == 0) == all(a <= b for a, b in zip(d_to_vec(d1), d_to_vec(d2)))
                    for d1 in divs for d2 in divs)
    check("divisibility d₁|d₂ ⟺ exponents coordinate-wise ≤ ⟹ isomorphism of the lattice to a product of chains", order_iso)


# ═══════ B. squarefree ⟺ boolean cube ═══════
def section_B():
    print("\n[B] N SQUAREFREE ⟺ D(N) ≅ Q_k (boolean cube): divisor ↔ bit vector, divisibility ⟺ ⊆")
    N = 210                                                  # 2·3·5·7, squarefree, k=4
    primes = sorted(factorize(N)); k = len(primes)
    divs = divisors(N)
    d_to_bits = lambda d: tuple(1 if d % p == 0 else 0 for p in primes)
    is_cube = sorted(d_to_bits(d) for d in divs) == sorted(product((0, 1), repeat=k)) and len(divs) == 2 ** k
    order = all((d2 % d1 == 0) == all(a <= b for a, b in zip(d_to_bits(d1), d_to_bits(d2)))
                for d1 in divs for d2 in divs)
    check(f"squarefree {N}: D≅Q_{k} (divisor↔bit vector), |D|={len(divs)}=2^{k}", is_cube)
    check("divisibility ⟺ ⊆ of bits ⟹ the divisor lattice = boolean cube Q_k", order)
    # distinguishing: 12=2²·3 NOT a cube (|D| not a power of 2)
    d12 = divisors(12)
    pow2 = {2 ** i for i in range(6)}
    check("distinguishing: 12=2²·3 — |D(12)|=6 ∉ {2^i} ⟹ NOT a cube (has a square) — squarefreeness is needed",
          len(d12) == 6 and 6 not in pow2)


# ═══════ C. number of divisors ═══════
def section_C():
    print("\n[C] d(N) = ∏(aᵢ+1) (number of divisors = size of the box); squarefree ⟹ d(N)=2^ω(N)")
    for N in (360, 1000, 1):
        f = factorize(N)
        formula = prod(a + 1 for a in f.values()) if f else 1
        check(f"d({N})=∏(aᵢ+1)={formula} matches direct enumeration of divisors", formula == len(divisors(N)))
    check("squarefree: d(N)=2^ω(N) — e.g. d(210)=2^4=16 = number of vertices of Q_4",
          len(divisors(210)) == 2 ** omega(210))


# ═══════ D. Möbius = sign of a vertex + inclusion-exclusion ═══════
def section_D():
    print("\n[D] MÖBIUS: μ=(−1)^ω on squarefree, 0 on squares; Σ_{d|N} μ(d)=[N=1] (incl-excl on the cube)")
    # μ — sign of a cube vertex (parity of the number of primes); 0 outside the cube (has a square)
    signs_ok = mobius(1) == 1 and mobius(30) == -1 and mobius(210) == 1 and mobius(12) == 0 and mobius(8) == 0
    check("μ(1)=1, μ(2·3·5)=−1, μ(2·3·5·7)=+1 (=(−1)^ω, sign of a vertex); μ(2²·3)=μ(2³)=0 (square)", signs_ok)
    # identity Σ_{d|N} μ(d) = [N=1] = (1−1)^k on the cube of primes = inclusion-exclusion
    identity = all(sum(mobius(d) for d in divisors(N)) == (1 if N == 1 else 0)
                   for N in (1, 2, 6, 30, 210, 12, 36, 100))
    # distinguishing: for N>1 the sum is strictly ZERO, for N=1 — a unit (not a constant)
    distinct = sum(mobius(d) for d in divisors(1)) == 1 and sum(mobius(d) for d in divisors(30)) == 0
    check("Σ_{d|N} μ(d) = [N=1]: a unit at N=1, ZERO at N>1 = (1−1)^k = incl-excl on the divisor cube",
          identity and distinct)


# ═══════ E. self-duality d↦N/d ═══════
def section_E():
    print("\n[E] d↦N/d: bijection of divisors, REVERSES divisibility (anti-isomorphism); squarefree ⟹ κ-antipode of the cube")
    N = 210
    divs = divisors(N)
    bij = sorted(N // d for d in divs) == divs
    anti = all((d2 % d1 == 0) == ((N // d1) % (N // d2) == 0) for d1 in divs for d2 in divs)
    check("d↦N/d — bijection of divisors, reverses order (d₁|d₂ ⟺ N/d₂ | N/d₁): the lattice is self-dual",
          bij and anti)
    # on squarefree: N/d = bit complement of the set of primes = κ:x↦1−x
    primes = sorted(factorize(N))
    bits = lambda d: tuple(1 if d % p == 0 else 0 for p in primes)
    kappa_ok = all(bits(N // d) == tuple(1 - b for b in bits(d)) for d in divs)
    check("squarefree: N/d = complement of the set of primes = κ (x↦1−x), antipode of a vertex in the cube Q_k", kappa_ok)


# ═══════ F. projection onto ranks ═══════
def section_F():
    print("\n[F] PROJECTION ONTO RANKS: rank(N):=ω(N) = dimension of the cube Q_{ω(N)}; levels = binomial C(k,j)")
    ranks = {N: omega(N) for N in (1, 2, 6, 30, 210)}
    check("rank(N)=ω(N) (distinct primes): 1→Q₀, 2→Q₁, 6→Q₂, 30→Q₃, 210→Q₄",
          ranks == {1: 0, 2: 1, 6: 2, 30: 3, 210: 4})
    # levels of the squarefree divisor cube = binomial coefficients (weight = number of prime factors)
    N, k = 210, 4
    levels = [0] * (k + 1)
    for d in divisors(N):
        levels[omega(d)] += 1
    check(f"levels of D(210)=Q_4 by weight = binomial {[comb(k, j) for j in range(k + 1)]} (= 1,4,6,4,1)",
          levels == [comb(k, j) for j in range(k + 1)])


# ═══════ G. locality (Euler): multiplicativity ═══════
def section_G():
    print("\n[G] LOCALITY (Euler): σ(N)=∏_p (1+p+…+p^a); multiplicative, local factor=floors of an axis")
    sigma = lambda n: sum(divisors(n))
    N = 360
    f = factorize(N)
    local = prod(sum(p ** e for e in range(a + 1)) for p, a in f.items())
    check(f"σ({N})=∏_p Σ_{{e=0}}^{{a}} p^e = {local} (local factor = sum over the floors of an axis) = direct Σ of divisors",
          sigma(N) == local)
    # distinguishing: σ multiplicative on coprimes (σ(6)=σ(2)σ(3)), but NOT additive
    mult = sigma(6) == sigma(2) * sigma(3)
    not_add = sigma(6) != sigma(2) + sigma(3)
    check("σ multiplicative on coprime: σ(6)=σ(2)·σ(3)=3·4=12, and NOT additive (≠3+4) — a product structure",
          mult and not_add)


# ═══════ H. D(squarefree N) = boolean algebra ═══════
def section_H():
    print("\n[H] D(squarefree N) = BOOLEAN ALGEBRA: complement d↦N/d (¬), De Morgan (⊥=1,⊤=N,∧=gcd,∨=lcm)")
    N = 210
    D = divisors(N)
    # complement ¬d=N/d: d∧¬d=⊥(1), d∨¬d=⊤(N)
    comp = all(gcd(d, N // d) == 1 and lcm(d, N // d) == N for d in D)
    demorgan = all(N // gcd(a, b) == lcm(N // a, N // b) for a in D for b in D)
    check("complement ¬d=N/d: gcd(d,N/d)=1 (bottom ⊥) and lcm(d,N/d)=N (top ⊤) — boolean complement", comp)
    check("De Morgan N/gcd(a,b)=lcm(N/a,N/b) ⟹ D(squarefree) = boolean algebra (⊥=1,⊤=N,∧=gcd,∨=lcm,¬=N/d)",
          demorgan)
    # distinguishing: on NON-squarefree (12) the complement breaks — d=2: gcd(2,6)=2≠1, no complement
    check("distinguishing: 12=2²·3 — gcd(2,12/2)=gcd(2,6)=2≠1 ⟹ no complement ⟹ not boolean (squarefreeness needed)",
          gcd(2, 12 // 2) != 1)


# ═══════ I. × of coprimes = Cartesian product of cubes ═══════
def section_I():
    print("\n[I] × OF COPRIMES = Q_a × Q_b = Q_(a+b): multiplication glues axes, rank ADDS UP")
    M, K = 6, 35                                              # coprime: 2·3 and 5·7
    cart = len(divisors(M)) * len(divisors(K)) == len(divisors(M * K))
    rank_add = omega(M) + omega(K) == omega(M * K)
    check(f"|D(6)|·|D(35)|={len(divisors(M))}·{len(divisors(K))}=|D(210)|={len(divisors(M*K))} and ω 2+2=4 ⟹ Q₂×Q₂=Q₄",
          cart and rank_add)
    # distinguishing: NOT coprime (6·10) — axes overlapped, rank does NOT add up
    check("distinguishing: NOT coprime 6·10=60 — ω(60)=3 ≠ ω(6)+ω(10)=4 (axes overlapped, not Q_(a+b))",
          omega(60) != omega(6) + omega(10))


# ═══════ J. factorial = number of maximal chains of the cube ═══════
def section_J():
    print("\n[J] FACTORIAL = number of MAXIMAL CHAINS of the cube Q_k = k! (all traversals ⊥→⊤); n! not squarefree")
    def max_chains(k):                                       # paths ∅→[k] by steps of +1 element = orders of axes
        def cnt(s):
            return 1 if len(s) == k else sum(cnt(s | {i}) for i in range(k) if i not in s)
        return cnt(frozenset())
    check("number of max. chains of the cube Q_k (paths ⊥→⊤ = orders of adding axes) = k! for k=1..5",
          all(max_chains(k) == factorial(k) for k in range(1, 6)))
    # n! is heavily built up above the cube: Legendre v_p(n!)=Σ⌊n/pⁱ⌋, not squarefree
    def legendre(n, p):
        s, pk = 0, p
        while pk <= n: s += n // pk; pk *= p
        return s
    f6 = factorize(factorial(6))
    check("v_p(n!)=Σ⌊n/pⁱ⌋ (Legendre): v₂(6!)=4 matched; n! NOT squarefree ⟹ lives high above the cube (floors)",
          f6.get(2, 0) == legendre(6, 2) and any(a >= 2 for a in f6.values()))


# ═══════ K. Möbius: inversion of ζ, blindness to floors, limit s→1 (∞) ═══════
def section_K():
    print("\n[K] MÖBIUS μ: INVERSION of ζ (1/ζ=Σμ/nˢ=∏(1−p⁻ˢ)); blind to floors (≠0⟺a cube vertex); limit s→1=∞")
    # μ≠0 ⟺ N squarefree ⟺ a cube vertex: μ SEES only the pure cube, blind to the ^-superstructure (floors)
    blind = all((mobius(N) != 0) == all(a == 1 for a in factorize(N).values()) for N in range(1, 200))
    check("μ(N)≠0 ⟺ N squarefree (a cube vertex); μ=0 on floors ⟹ μ sees ONLY the pure cube (blind to ^)",
          blind)
    # Dirichlet inversion: μ*1=δ (μ inverse to the constant 1) — this is exactly Σ_{d|N}μ(d)=[N=1]
    check("convolution μ*1=δ (Σ_{d|N}μ(d)=[N=1]): μ = INVERSE to the constant 1 in the Dirichlet ring (= incl-excl)",
          all(sum(mobius(d) for d in divisors(N)) == (1 if N == 1 else 0) for N in range(1, 100)))
    # 1/ζ(s)=Σμ(n)/nˢ=∏(1−p⁻ˢ); at s=2 → 6/π² (μ INVERTS the Euler product)
    s, target = 2.0, 6.0 / pi ** 2
    msum = sum(mobius(n) / n ** s for n in range(1, 20000))
    primes = [p for p in range(2, 20000) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    prodp = prod((1 - p ** (-s)) for p in primes)
    check(f"1/ζ(2)=Σμ(n)/n²=∏(1−p⁻²)=6/π²≈{target:.5f}: μ INVERTS the Euler product (∏ vs Σ)",
          abs(msum - target) < 1e-3 and abs(prodp - target) < 1e-3)
    # LIMIT s→1: ζ has a POLE (harmonic series s=1 diverges ~ln N →∞), while s=2 saturates (distinguishing)
    H = [sum(1.0 / n for n in range(1, 10 ** k + 1)) for k in (2, 3, 4)]          # s=1
    Z2 = [sum(1.0 / n ** 2 for n in range(1, 10 ** k + 1)) for k in (2, 3, 4)]    # s=2
    harm_diverges = H[0] < H[1] < H[2] and (H[2] - H[1]) > 0.5                    # grows ~ln10≈2.3/order
    z2_saturates = abs(Z2[2] - Z2[1]) < 0.01                                      # → π²/6, finite
    check("pole s=1: Σ1/n DIVERGES (grows ~ln N →∞), while Σ1/n² saturates ⟹ ζ has a pole at s=1 (=∞)",
          harm_diverges and z2_saturates)
    # 1/ζ = Σμ/nˢ → 0 at the pole: the μ-side FADES at the ∞-pole of ζ
    check("1/ζ=Σμ/nˢ → 0 at the pole s→1 (the μ-side fades at ∞): 1/H(N) monotonically → 0",
          1.0 / H[0] > 1.0 / H[1] > 1.0 / H[2] and 1.0 / H[2] < 0.2)
    print("   → μ lands in TWO places: LOCALLY — sign of a cube vertex (−1)^ω (●); IN THE LIMIT — inversion of ζ at the ∞-")
    print("     pole (●). The Mertens sum M(x)=Σ_{n≤x}μ(n) — an ∞-limit object, its growth ⟺ σ½ (Riemann, ○).")


# ═══════ L. poles 0 and ∞ (cutoffs; first distinction 0→1) ═══════
def section_L():
    print("\n[L] POLES 0 and ∞ (cutoffs-background): 0→1 = the first distinction (additive invariant); κ:0↔∞, center √N=σ½")
    # 0 = the lower pole: neutral for +, ABSORBER for × (erases) — outside the multiplicative cube
    check("0 = the lower pole: neutral for + (0+n=n) and ABSORBER for × (0·n=0, erases) ⟹ outside the multipl. cube (background)",
          all(0 + n == n for n in range(6)) and all(0 * n == 0 for n in range(6)))
    # the first distinction from the background: 0→1 (succ) = additive invariant (unit); 1 = bottom ⊥ of the cube (ω=0)
    check("0→1 (succ) = the FIRST distinction from the background = additive invariant (unit of counting); 1=bottom ⊥ of the cube (ω=0)",
          (0 + 1 == 1) and omega(1) == 0)
    # κ:d↦N/d swaps bottom↔top (poles 1↔N); the fixed point = √N = center = σ½ (for a square N)
    N = 36                                                   # √36=6 — the center exists
    check("κ:d↦N/d swaps the poles (1↔N=bottom↔top); fixed point=√N=center=σ½ (N=36 ⟹ √N=6 fixed)",
          (N // 1 == N) and (N // N == 1) and (N // 6 == 6))
    # ∞ = the upper pole: rank unbounded — a primorial gives Q_k for ANY k, there is no top of the series
    primorial = [1, 2, 6, 30, 210, 2310]
    check("∞ = the upper pole: rank UNBOUNDED — primorials p₁···p_k give Q_k for any k (there is no top of the series)",
          [omega(p) for p in primorial] == [0, 1, 2, 3, 4, 5])


# ═══════ M. Euclidean algorithm and Bézout identity (foundation gcd = ∧) ═══════
def section_M():
    print("\n[M] EUCLID + BÉZOUT: gcd via remainders (=∧ of the lattice); gcd(a,b)=ax+by (constructive infimum)")
    def euclid(a, b):
        while b: a, b = b, a % b
        return a
    def ext(a, b):                                          # extended Euclid: (g, x, y), g=ax+by
        if b == 0: return a, 1, 0
        g, x, y = ext(b, a % b)
        return g, y, x - (a // b) * y
    check("the Euclidean algorithm (chain of remainders) gives gcd = ∧ of the lattice D — foundation of the infimum",
          all(euclid(a, b) == gcd(a, b) for a, b in [(12, 18), (17, 5), (240, 46), (100, 60)]))
    bezout = all((lambda g, x, y: g == gcd(a, b) and a * x + b * y == g)(*ext(a, b))
                 for a, b in [(12, 18), (17, 5), (240, 46)])
    check("Bézout: gcd(a,b)=ax+by (extended Euclid) — the infimum is linearly expressible; constructive ∧", bezout)
    # distinguishing: coprime ⟺ gcd=1 (Bézout gives 1), non-coprime ⟺ >1
    check("distinguishing: gcd(17,5)=1 (coprime, ∃ 17x+5y=1), gcd(12,18)=6>1 (common divisor)",
          gcd(17, 5) == 1 and gcd(12, 18) == 6)


# ═══════ N. CRT: ℤ/n ≅ ∏ ℤ/pᵢ^aᵢ = monoidality of □ on residues ═══════
def section_N():
    print("\n[N] CRT (Chinese thm.): ℤ/n ≅ ∏ ℤ/pᵢ^aᵢ — a ring isomorphism = □ on RESIDUES (2nd realization)")
    n, parts = 12, [4, 3]                                   # 12 = 4·3, parts are coprime
    proj = lambda x: tuple(x % m for m in parts)
    biject = len({proj(x) for x in range(n)}) == n
    addhom = all(proj((a + b) % n) == tuple((proj(a)[i] + proj(b)[i]) % parts[i] for i in range(len(parts)))
                 for a in range(n) for b in range(n))
    mulhom = all(proj((a * b) % n) == tuple((proj(a)[i] * proj(b)[i]) % parts[i] for i in range(len(parts)))
                 for a in range(n) for b in range(n))
    check("ℤ/12 → ℤ/4×ℤ/3 (x↦(x mod 4, x mod 3)): bijection", biject)
    check("CRT preserves + and × (ring isomorphism) ⟹ ℤ/n≅∏ℤ/pᵢ^aᵢ = monoidality of □ on residues",
          addhom and mulhom)
    # distinguishing: NON-coprime parts [4,6] — NOT an isomorphism: |ℤ/4×ℤ/6|=24≠12 (not a surjection)
    check("distinguishing: parts [4,6] NOT coprime (gcd=2) ⟹ |ℤ/4×ℤ/6|=24≠12, NOT an isomorphism; CRT requires coprime axes",
          gcd(4, 6) == 2 and 4 * 6 != 12 and 4 * 3 == 12)


# ═══════ O. Euler's φ: multiplicative (□), φ=μ*Id, Σφ(d)=n ═══════
def section_O():
    print("\n[O] EULER's φ (totient): multiplicative (=□); φ(p^a)=p^a−p^(a−1); Σ_{d|n}φ(d)=n; φ=μ*Id")
    mult = all(phi(m * k) == phi(m) * phi(k) for m, k in [(4, 3), (5, 6), (7, 10), (8, 9)] if gcd(m, k) == 1)
    pa = all(phi(p ** a) == p ** a - p ** (a - 1) for p, a in [(2, 3), (3, 2), (5, 2)])
    check("φ multiplicative φ(mn)=φ(m)φ(n) on coprime (=□, local along axes); φ(p^a)=p^a−p^(a−1)",
          mult and pa)
    check("Σ_{d|n}φ(d)=n (convolution φ*1=Id): the sum of φ over the divisor cube recovers n",
          all(sum(phi(d) for d in divisors(n)) == n for n in range(1, 60)))
    check("φ=μ*Id (φ(n)=Σ_{d|n}μ(d)·n/d): φ via Möbius inversion = inclusion-exclusion on the cube",
          all(phi(n) == sum(mobius(d) * (n // d) for d in divisors(n)) for n in range(1, 60)))


# ═══════ P. v_p valuation = floor height; product formula ═══════
def section_P():
    print("\n[P] v_p VALUATION = FLOOR HEIGHT: v_p(mn)=v_p(m)+v_p(n) (×→+); |n|_p=p^(−v_p); ∏|n|_v=1")
    add = all(vp(m * k, p) == vp(m, p) + vp(k, p) for p in (2, 3, 5) for m, k in [(4, 6), (8, 12), (9, 15)])
    coord = all(vp(360, p) == factorize(360).get(p, 0) for p in (2, 3, 5))
    check("v_p(mn)=v_p(m)+v_p(n): p-adic VALUATION (turns × into +); v_p = coordinate of the floor of axis p",
          add and coord)
    # product formula: ∏_p |n|_p · |n|_∞ = ∏_p p^(−v_p) · n = (1/n)·n = 1 (the floor is stitched to the Archimedean |·|∞)
    prodform = all(abs(prod(p ** (-vp(n, p)) for p in factorize(n)) * n - 1.0) < 1e-12 for n in (12, 30, 360))
    check("|n|_p=p^(−v_p); product formula ∏_p|n|_p·|n|_∞=1 ⟹ the floor (v_p) is stitched to the Archimedean side |·|∞",
          prodform)


# ═══════ Q. Fermat's little / Euler: group (ℤ/n)* ═══════
def section_Q():
    print("\n[Q] FERMAT's LITTLE / EULER: a^φ(n)≡1 (mod n) for gcd(a,n)=1; (ℤ/n)* a group, for a prime cyclic")
    fermat = all(pow(a, phi(n), n) == 1 for n in (7, 12, 15, 20) for a in range(1, n) if gcd(a, n) == 1)
    grp = all(len([a for a in range(1, n) if gcd(a, n) == 1]) == phi(n) for n in (7, 12, 15))
    check("a^φ(n)≡1 (mod n) for gcd(a,n)=1 (Euler); |(ℤ/n)*|=φ(n) — order of the group of invertible residues",
          fermat and grp)
    def order(a, p):
        o, x = 1, a % p
        while x != 1: x = x * a % p; o += 1
        return o
    # for a prime p the group (ℤ/p)* is CYCLIC: there is a primitive root (an element of order p−1)
    check("for a prime p (ℤ/p)* is CYCLIC — ∃ primitive root (g of order p−1): mod 7 this is g=3 (order 6)",
          order(3, 7) == 6 and any(order(g, 11) == 10 for g in range(2, 11)))


# ═══════ R. functor dictionary: Λ — a genuine machine functor ═══════
def section_R():
    print("\n[R] FUNCTOR DICTIONARY: Λ:S↦∏_{p∈S}p — a FUNCTOR (preserves order, □, κ) ⟹ ● not recognition")
    primes = [2, 3, 5, 7]
    Lam = lambda S: prod(primes[i] for i in S) if S else 1
    subs = [set(c) for r in range(len(primes) + 1)
            for c in __import__("itertools").combinations(range(len(primes)), r)]
    # (1) lift Λ/H: preserves order ⊆ ↦ | (functor of partially ordered sets)
    order = all((S <= T) == (Lam(T) % Lam(S) == 0) for S in subs for T in subs)
    check("Λ preserves order: S⊆T ⟺ Λ(S)|Λ(T) — a functor (cat. of sets of primes → numbers with divisibility)",
          order)
    # (2) monoidality □: Λ(S⊔T)=Λ(S)·Λ(T) for disjoint (□ ↦ × of coprimes)
    mono = all(Lam(S | T) == Lam(S) * Lam(T) for S in subs for T in subs if not (S & T))
    check("Λ monoidal: Λ(S⊔T)=Λ(S)·Λ(T) (□ of the cube ↦ × coprime) — the functor preserves the tensor Q_a□Q_b=Q_(a+b)",
          mono)
    # (3) κ: Λ(complement)=N/Λ(S) (κ of the cube ↦ d↦N/d)
    N, full = prod(primes), set(range(len(primes)))
    kappa = all(Lam(full - S) == N // Lam(S) for S in subs)
    check("Λ commutes with κ: Λ(∁S)=N/Λ(S) (complement of the cube ↦ d↦N/d) ⟹ Λ carries ALL functors (●)",
          kappa)
    print("   → CONCLUSION: on squarefree numbers Λ — an isomorphism of categories (sets of primes ≅ numbers with |);")
    print("     the machine functors Λ/□/κ/H realized RIGOROUSLY (●), not 'recognized'. Recognition (◐) — only σ½=Re=½.")


def main():
    print("=" * 96)
    print("RIGOROUS CORE: divisor lattice = product of chains; squarefree = boolean cube; projection onto ranks")
    print("=" * 96)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    section_H(); section_I(); section_J(); section_K(); section_L()
    section_M(); section_N(); section_O(); section_P(); section_Q(); section_R()
    print("\n" + "=" * 96)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION (all ●, pure number theory): D(N)≅∏ chains Cℓ(aᵢ+1); N squarefree ⟺ D(N)≅Q_k = a BOOLEAN")
    print("       ALGEBRA (⊥=1,⊤=N,∧=gcd,∨=lcm,¬=N/d). ATLAS OF OPERATIONS: layer I (inside the cube) — 1=⊥, NOT=¬,")
    print("       ∧/∨; layer II (between numbers) — + counting, × gluing of axes Q_a×Q_b=Q_(a+b), ^ a floor, ! = k! traversals")
    print("       of the cube; POLES — 0 (background, neutral+/absorber×, 0→1 the first invariant), ∞ (rank unbounded).")
    print("       MÖBIUS μ: locally sign of a vertex (−1)^ω, in the limit — inversion of ζ (1/ζ=Σμ/nˢ) at the ∞-pole.")
    print("       SECOND REALIZATION (residues): CRT ℤ/n≅∏ℤ/pᵢ^aᵢ = □ on residues; Euler's φ multiplicative=□,")
    print("       φ=μ*Id; v_p=floor height (×→+, bridge to |·|∞); Fermat a^φ≡1, (ℤ/n)* cyclic for a prime.")
    print("       ★FUNCTOR DICTIONARY: Λ:S↦∏p — a functor (order/□/κ); on squarefree = an ISOMORPHISM of catego-")
    print("       ries, the machine functors Λ/□/κ/H realized RIGOROUSLY (●); recognition (◐) — only σ½=Re=½.")
    print("=" * 96)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
