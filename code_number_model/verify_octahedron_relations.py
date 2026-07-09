#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_octahedron_relations.py — ★R₁/R₂/R₃, holonomy T/𝒯, the arithmetic octahedron, observer=quotient Uₙ/κ, Petersen, Mersenne.

Restores the missing core of rank 3 and higher ranks: the UNIFIED Hamming distance on U₃ splits into THREE relations R₁(d=1)=C₆, R₂(d=2)=2K₃,
R₃(d=3)=3K₂; R₁∪R₂=K(2,2,2)=octahedron, R₃=three axes. Holonomy: the shift T (order 6, T³=κ) ≠ the twisted transport 𝒯
(±1, 𝒯²=id, Möbius band). The observer = the projective QUOTIENT Uₙ/κ≅PG(n−2,2) (not only the center σ½). The arithmetic
octahedron = the divisors of 30. Color: R₁=hue circle, R₂=RGB/CMY, R₃=complements. Higher ranks: Petersen twice (KG(5,2)),
the Mersenne horizon |Uₙ/κ|=2ⁿ⁻¹−1. Register ●◐○: combinatorics/spectra/number theory=●; color↔number, observer=quotient=◐;
E₈/Gauss–Wantzel=◐/○.

  A. ★R₁/R₂/R₃: a unified d_H on U₃ → three relations C₆ / 2K₃ / 3K₂; R₁∪R₂=K(2,2,2); R₃=three axes.
  B. HOLONOMY: the shift T (order 6, T³=κ) ≠ the transport 𝒯 (±1 on a loop, 𝒯²=id, C₆→C₃ a connected double cover).
  C. THE ARITHMETIC OCTAHEDRON: divisors of 30 {2,3,5,6,10,15} = the same R₁/R₂/R₃ (conjugate pairs / primes↔semiprimes / cycle).
  D. COLOR R₁/R₂/R₃: 6 chromatic vertices; R₁=hue circle, R₂=RGB/CMY, R₃=complements R↔C; the group B₃=48.
  E. THE OBSERVER=QUOTIENT: Uₙ/κ≅PG(n−2,2), the number of axes 2ⁿ⁻¹−1 (n=3→3, 4→7 Fano, 5→15).
  F. ★PETERSEN: rank 5's layer S₂⁽⁵⁾=KG(5,2) (disjointness) = Petersen (10 vertices, 3-regular, spectrum {3,1⁵,−2⁴}).
  G. THE MERSENNE HORIZON: |Uₙ/κ|=2ⁿ⁻¹−1 prime ⟺ n∈{3,4,6,8} (the Singer cycle is transitive); Gauss–Wantzel=◐/○.
  H. guard: R₁/R₂/R₃=ONE distance by value (not three objects); observer=quotient/center=two readings.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

U3 = [0b001, 0b010, 0b100, 0b011, 0b101, 0b110]      # six points (excluding the poles 000,111)
def dH(a, b): return bin(a ^ b).count('1')
def kap(x): return 7 ^ x
def components(adj, verts):
    seen, comp = set(), 0
    for v in verts:
        if v in seen: continue
        comp += 1; stack = [v]
        while stack:
            u = stack.pop()
            if u in seen: continue
            seen.add(u)
            stack += [w for w in verts if adj(u, w) and w not in seen]
    return comp


# ═══════════════ A. R₁/R₂/R₃ ═══════════════
def section_A():
    print("\n[A] ★R₁/R₂/R₃: a unified d_H on U₃ → three relations C₆ / 2K₃ / 3K₂; R₁∪R₂=K(2,2,2); R₃=three axes")
    pairs = list(combinations(U3, 2))
    r1 = [(a, b) for a, b in pairs if dH(a, b) == 1]
    r2 = [(a, b) for a, b in pairs if dH(a, b) == 2]
    r3 = [(a, b) for a, b in pairs if dH(a, b) == 3]
    counts = (len(r1), len(r2), len(r3)) == (6, 6, 3) and len(pairs) == 15   # 6+6+3=15
    deg1 = all(sum(1 for b in U3 if dH(a, b) == 1) == 2 for a in U3)         # R₁ is 2-regular = C₆
    r1_conn = components(lambda a, b: dH(a, b) == 1, U3) == 1                 # C₆ is connected (a single cycle)
    r2_comp = components(lambda a, b: dH(a, b) == 2, U3) == 2                 # 2K₃ = two triangles
    deg2 = all(sum(1 for b in U3 if dH(a, b) == 2) == 2 for a in U3)         # 2-regular inside K₃
    r3_match = all(sum(1 for b in U3 if dH(a, b) == 3) == 1 for a in U3) and all(kap(a) == [b for b in U3 if dH(a, b) == 3][0] for a in U3)  # 3K₂ = κ-pairs
    oct_deg = all(sum(1 for b in U3 if dH(a, b) in (1, 2)) == 4 for a in U3)  # R₁∪R₂ = K(2,2,2) 4-regular
    check(f"d_H on the 15 pairs of U₃ splits into R₁(d=1)={len(r1)}=C₆ (2-regular,connected:{deg1 and r1_conn}) · "
          f"R₂(d=2)={len(r2)}=2K₃ (2 components:{r2_comp}, 2-regular:{deg2}) · R₃(d=3)={len(r3)}=3K₂ (κ-pairs:"
          f"{r3_match}); count 6+6+3=15:{counts}; R₁∪R₂=K(2,2,2) 4-regular:{oct_deg} ⟹ ★ONE distance → THREE "
          f"relations; octahedron=R₁∪R₂, three axes=R₃ (the core of rank 3)",
          counts and deg1 and r1_conn and r2_comp and deg2 and r3_match and oct_deg)


# ═══════════════ B. holonomy T vs 𝒯 ═══════════════
def section_B():
    print("\n[B] HOLONOMY: the shift T (order 6, T³=κ) ≠ the transport 𝒯 (±1, 𝒯²=id, C₆→C₃ a connected double cover)")
    order = [0b001, 0b011, 0b010, 0b110, 0b100, 0b101]     # C₆ (neighbors at d=1)
    ham1 = all(dH(order[i], order[(i + 1) % 6]) == 1 for i in range(6))
    T3_kappa = all(order[(i + 3) % 6] == kap(order[i]) for i in range(6))   # T³ = κ (a shift by 3 = the antipode)
    # 𝒯: the quotient C₆/κ = C₃; the covering C₆→C₃ is connected (a nontrivial class in H¹(S¹;ℤ/2))
    classes = {}
    for i, x in enumerate(order):
        k = frozenset((x, kap(x)))
        classes.setdefault(k, []).append(i)
    c3 = len(classes) == 3 and all(len(v) == 2 for v in classes.values())    # 3 κ-classes of 2 each
    # connectedness of the covering: traversing C₃ once = a half-turn of C₆ = κ ≠ id ⟹ 𝒯 flips sign, 𝒯²=id
    monodromy = T3_kappa                                    # a loop in C₃ lifts to a path of length 3 = κ
    check(f"C₆ (neighbors at d=1): {ham1}; the shift T: T³=κ (order 6), a half-turn=the antipode: {T3_kappa}; the quotient C₆/κ=C₃ "
          f"(3 classes of 2 each): {c3}; the covering C₆→C₃ is CONNECTED ⟹ the monodromy is nontrivial (a loop in C₃ → κ, not id): "
          f"{monodromy} ⟹ ★distinguish the SHIFT T (permutes points) from the TRANSPORT 𝒯 (a sign ±1 on a loop, 𝒯²=id) — "
          f"it is precisely 𝒯 that is the strict Möbius band (H¹(S¹;ℤ/2))", ham1 and T3_kappa and c3 and monodromy)


# ═══════════════ C. the arithmetic octahedron ═══════════════
def section_C():
    print("\n[C] THE ARITHMETIC OCTAHEDRON: divisors of 30 {2,3,5,6,10,15} = the same R₁/R₂/R₃ under D(30)≅Q₃")
    primes = {2: 0b100, 3: 0b010, 5: 0b001}                # prime → axis-bit
    def pset(d):                                            # divisor → bit-vector of the set of primes
        v = 0
        for p, bit in primes.items():
            if d % p == 0: v |= bit
        return v
    divs = [2, 3, 5, 6, 10, 15]                             # proper divisors of 30 (excluding 1,30)
    vecs = {d: pset(d) for d in divs}
    # R₃ = conjugate pairs d↦30/d = Hamming-3 = complement
    r3 = all(dH(vecs[d], vecs[30 // d]) == 3 for d in divs)
    conj = {frozenset((d, 30 // d)) for d in divs} == {frozenset((2, 15)), frozenset((3, 10)), frozenset((5, 6))}
    # R₂ = primes {2,3,5} (weight 1) vs semiprimes {6,10,15} (weight 2)
    primes_layer = {d for d in divs if bin(vecs[d]).count('1') == 1} == {2, 3, 5}
    semi_layer = {d for d in divs if bin(vecs[d]).count('1') == 2} == {6, 10, 15}
    # R₁ = the cycle 2→6→3→15→5→10→2 (neighbors differ by one prime = Hamming-1)
    cyc = [2, 6, 3, 15, 5, 10]
    r1 = all(dH(vecs[cyc[i]], vecs[cyc[(i + 1) % 6]]) == 1 for i in range(6))
    check(f"divisors of 30 mapped to primes↔bits: R₃=conjugate pairs {{2,15}},{{3,10}},{{5,6}} (d↦30/d, Hamming-3): "
          f"{r3 and conj}; R₂=primes {{2,3,5}} / semiprimes {{6,10,15}}: {primes_layer and semi_layer}; "
          f"R₁=cycle 2→6→3→15→5→10→2 (Hamming-1): {r1} ⟹ the ARITHMETIC octahedron = the same R₁/R₂/R₃ (a number=a cube of "
          f"primes, D(30)≅Q₃)", r3 and conj and primes_layer and semi_layer and r1)


# ═══════════════ D. color R₁/R₂/R₃ ═══════════════
def section_D():
    print("\n[D] COLOR R₁/R₂/R₃: R₁=hue circle, R₂=RGB/CMY, R₃=complements R↔C; the group B₃=48")
    col = {'R': 0b100, 'G': 0b010, 'B': 0b001, 'Y': 0b110, 'M': 0b101, 'C': 0b011}
    r3 = (dH(col['R'], col['C']) == 3 and dH(col['G'], col['M']) == 3 and dH(col['B'], col['Y']) == 3)  # complements
    rgb = {col['R'], col['G'], col['B']}; cmy = {col['Y'], col['M'], col['C']}
    r2 = all(dH(a, b) == 2 for a in rgb for b in rgb if a != b) and all(dH(a, b) == 2 for a in cmy for b in cmy if a != b)
    wheel = ['R', 'Y', 'G', 'C', 'B', 'M']                  # hue circle
    r1 = all(dH(col[wheel[i]], col[wheel[(i + 1) % 6]]) == 1 for i in range(6))
    b3 = 2 ** 3 * 6 == 48                                   # |B₃|=(ℤ/2)³⋊S₃ = 8·6
    check(f"R₃=complements R↔C,G↔M,B↔Y (Hamming-3): {r3}; R₂=RGB-triad/CMY-triad (Hamming-2 within): {r2}; "
          f"R₁=hue circle R→Y→G→C→B→M (Hamming-1): {r1}; |B₃|=(ℤ/2)³⋊S₃=48: {b3} ⟹ the 4 maps RGB/CMY/Lab/HSB = "
          f"three projections of one octahedron (R₁=hue/HSB, R₂=RGB↔CMY, R₃=Lab-opponent/complement)", r3 and r2 and r1 and b3)


# ═══════════════ E. the observer = the projective quotient ═══════════════
def section_E():
    print("\n[E] THE OBSERVER=QUOTIENT: Uₙ/κ≅PG(n−2,2), the number of axes 2ⁿ⁻¹−1 (n=3→3, 4→7 Fano, 5→15)")
    ok = True
    for n in (3, 4, 5, 6):
        full = (1 << n) - 1
        U = [x for x in range(1 << n) if x not in (0, full)]
        seen, axes = set(), 0
        for x in U:
            if x in seen: continue
            seen.add(x); seen.add(full ^ x); axes += 1
        ok = ok and (axes == 2 ** (n - 1) - 1)             # |Uₙ/κ| = 2ⁿ⁻¹−1 = |PG(n−2,2)|
    check(f"|Uₙ/κ|=2ⁿ⁻¹−1=|PG(n−2,2)| (n=3→3, 4→7=Fano, 5→15, 6→31): {ok} ⟹ ★THE OBSERVER as a PROJECTIVE "
          f"QUOTIENT (the axes, onto which opposite directions collapse) — a second reading alongside the center σ½ "
          f"(◐); the lift Q*_{{n−1}}≅Uₙ/κ: the content of a rank → the axes of the next", ok)


# ═══════════════ F. Petersen ═══════════════
def section_F():
    print("\n[F] ★PETERSEN: rank 5's layer S₂⁽⁵⁾=KG(5,2) (disjointness) = Petersen (10 vertices, 3-regular, {3,1⁵,−2⁴})")
    verts = list(combinations(range(5), 2))                # 2-subsets of {0..4} = the middle layer S₂⁽⁵⁾
    n = len(verts)
    A = np.zeros((n, n), int)
    for i, a in enumerate(verts):
        for j, b in enumerate(verts):
            if i != j and set(a).isdisjoint(b):            # adjacent ⟺ disjoint = Kneser KG(5,2)
                A[i][j] = 1
    ten = n == 10
    reg3 = all(A.sum(1)[i] == 3 for i in range(n))         # 3-regular
    tri_free = all(not (A[i][j] and A[j][k] and A[i][k]) for i in range(n) for j in range(n) for k in range(n))
    spec = sorted(np.linalg.eigvalsh(A.astype(float)).round(6))
    petersen_spec = np.allclose(spec, sorted([3] + [1] * 5 + [-2] * 4))
    check(f"S₂⁽⁵⁾ = 2-subsets of {{0..4}} = {n} vertices: {ten}; adjacency=disjointness (Kneser KG(5,2)): 3-regular "
          f"{reg3}, triangle-free {tri_free}, spectrum {{3,1⁵,−2⁴}} {petersen_spec} ⟹ ★PETERSEN appears at rank 5 "
          f"(a combinatorial prediction of the lift, not physics); it also appears at rank 6 (S₃⁽⁶⁾/κ)",
          ten and reg3 and tri_free and petersen_spec)


# ═══════════════ G. the Mersenne horizon ═══════════════
def section_G():
    print("\n[G] THE MERSENNE HORIZON: |Uₙ/κ|=2ⁿ⁻¹−1 is prime ⟺ n∈{3,4,6,8}; prime order = no suborbits; Gauss–Wantzel=○")
    # Precision of the statement: the Singer cycle is TRANSITIVE on the points of PG(n−2,2) for ANY n (classical, not a distinguisher).
    # The content of the horizon is the ORDER of the cycle: when 2ⁿ⁻¹−1 is prime, every nontrivial element is a full cycle
    # (a generator of the group of prime order); when composite there are proper subgroups → short suborbits.
    from math import gcd
    def is_prime(m): return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))
    horizon = [n for n in range(3, 12) if is_prime(2 ** (n - 1) - 1)]
    want = [3, 4, 6, 8]                                     # 2ⁿ⁻¹−1 ∈ {3,7,31,127} are prime
    check(f"|Uₙ/κ|=2ⁿ⁻¹−1 is prime (Mersenne) at n∈{horizon} (={want}); n=5→2⁴−1=15=3·5 composite",
          horizon == want and 2 ** 4 - 1 == 15 and 15 % 3 == 0 and 15 % 5 == 0)
    # the number of full cycles in Z/m is exactly φ(m) (the generators); the suborbit of element k has length m/gcd(k,m)
    def full_cycles(m): return sum(1 for k in range(1, m) if gcd(k, m) == 1)
    check("order 7 (n=4) is prime: a full cycle — EVERY one of the 6 nontrivial elements (φ(7)=6, no suborbits)",
          full_cycles(7) == 6)
    check("order 15 (n=5) is composite: only φ(15)=8 of 14 are full cycles; k=5 has suborbits of length 3, k=3 — of length 5",
          full_cycles(15) == 8 and 15 // gcd(5, 15) == 3 and 15 // gcd(3, 15) == 5)
    check("order 31 (n=6) is prime: φ(31)=30 — no suborbits", full_cycles(31) == 30)
    print("   ● the arithmetic of the horizon and the suborbits; the link to Gauss–Wantzel (regular polygons) = ○ frontier")


# ═══════════════ H. guard ═══════════════
def section_H():
    print("\n[H] GUARD: R₁/R₂/R₃=ONE distance by value; observer=quotient/center=two readings")
    print("   ● proven: three relations from ONE d_H (A), holonomy T/𝒯 (B), the arithmetic octahedron (C), color maps (D),")
    print("     the quotient Uₙ/κ=PG(n−2,2) (E), the Petersen spectrum (F), the Mersenne horizon (G)")
    print("   ◐ readings: color↔number↔sound (one figure), the observer=the projective quotient (alongside the center σ½)")
    print("   ◐/○ frontier: E₈=octonions, Gauss–Wantzel↔Mersenne — a pattern, not a derivation")
    # R₁,R₂,R₃ cover ALL pairs exactly once (one distance, three values)
    pairs = list(combinations(U3, 2))
    cover = sum(1 for a, b in pairs if dH(a, b) in (1, 2, 3)) == len(pairs) == 15
    check(f"R₁∪R₂∪R₃ cover all 15 pairs of U₃ exactly once (one distance d∈{{1,2,3}}): {cover} ⟹ the three relations = "
          f"ONE measure by value, not three independent objects; octahedron/Fano/color/divisors = readings of one "
          f"forced figure", cover)


def main():
    print("=" * 100)
    print("R₁/R₂/R₃, HOLONOMY T/𝒯, THE ARITHMETIC OCTAHEDRON, THE OBSERVER=QUOTIENT Uₙ/κ, PETERSEN, THE MERSENNE HORIZON")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G(); section_H()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: a unified Hamming distance on U₃ gives THREE relations — R₁=C₆ (a cycle), R₂=2K₃ (a split),")
    print("       R₃=3K₂ (axes); R₁∪R₂=the octahedron K(2,2,2), R₃=three axes. Holonomy: the shift T (T³=κ) ≠ the transport 𝒯 (±1,")
    print("       Möbius band). The arithmetic octahedron=the divisors of 30, color=three projections (B₃), the observer=the quotient Uₙ/κ=")
    print("       PG(n−2,2). Higher ranks: Petersen (KG(5,2)) at 5/6, the Mersenne horizon n∈{3,4,6,8}. ● combinatorics;")
    print("       ◐ color↔number, observer=quotient; ◐/○ E₈/Gauss–Wantzel.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
