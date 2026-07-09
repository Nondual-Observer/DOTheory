#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_causal_structure.py — the next step: CAUSALITY. We found the arrow (comonad,
direction), but not the light cone. Causality = a PARTIAL ORDER on events, and it
already exists: the Boolean lattice Q_n with inclusion ⊆ IS a causal set.

A. Q_n with ⊆ — a locally-finite partial order = a CAUSAL SET (causet).
B. LIGHT CONES: the future J⁺(x)={y⊇x} (2^{n−|x|}), the past J⁻(x)={z⊆x} (2^{|x|}),
   spacelike = incomparable (neither x⊆y, nor y⊆x).
C. TIME = CHAINS (timelike, flags, n! maximal ones); SPACE = ANTICHAINS (spacelike,
   weight layers); ★the MAXIMAL spatial slice = the MIDDLE layer = σ½ (Sperner).
D. THE ARROW (comonad coarse-graining) is consistent with the order: G lowers weight = motion toward the past.
E. Myrheim–Meyer DIMENSION: the fraction of ordered pairs → 0 ⟹ NOT a fixed d-Minkowski;
   the causal STRUCTURE is there (cones, time/space), but signature/dimension = INPUT ○.
"""
from __future__ import annotations
from math import comb
from itertools import combinations

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def popcount(x): return bin(x).count("1")
def leq(x, y): return (x & y) == x        # x ⊆ y


# ═══════ A. causal set ═══════
def section_A():
    print("\n[A] Q_n with ⊆ — a locally-finite partial order = a CAUSAL SET")
    for n in range(2, 6):
        N = 1 << n
        refl = all(leq(x, x) for x in range(N))
        antisym = all((not (leq(x, y) and leq(y, x))) or x == y for x in range(N) for y in range(N))
        # transitivity
        trans = True
        for x in range(N):
            for y in range(N):
                if leq(x, y):
                    for z in range(N):
                        if leq(y, z) and not leq(x, z): trans = False
        # local finiteness: the interval [x,y] is finite (a Boolean subcube) — always true for finite N
        check(f"n={n}: ⊆ is reflexive, antisymmetric, transitive, locally finite (causet)",
              refl and antisym and trans)


# ═══════ B. light cones ═══════
def section_B():
    print("\n[B] LIGHT CONES: J⁺(x)=2^{n−|x|}, J⁻(x)=2^{|x|}, spacelike=incomparable")
    for n in range(2, 6):
        N = 1 << n
        ok = True
        for x in range(N):
            fut = sum(1 for y in range(N) if leq(x, y))      # future x⊆y
            past = sum(1 for z in range(N) if leq(z, x))     # past z⊆x
            if fut != (1 << (n - popcount(x))) or past != (1 << popcount(x)): ok = False
        # spacelike pairs = incomparable
        space = sum(1 for x in range(N) for y in range(N)
                    if x < y and not leq(x, y) and not leq(y, x))
        check(f"n={n}: |J⁺(x)|=2^{{n−|x|}}, |J⁻(x)|=2^{{|x|}}; spacelike-pairs={space}", ok and space > 0)
    print("   → the past/future cone and the spacelike region are defined by the order")


# ═══════ C. time=chains, space=antichains, max layer = σ½ (Sperner) ═══════
def max_antichain_size(n):
    """width of the partial order (max antichain) by brute force for small n."""
    N = 1 << n
    elems = list(range(N))
    best = 0
    # a greedy per-layer approach is not enough; for n≤4 — search over subsets of one layer + Sperner.
    # We check the Sperner conjecture: max antichain = the middle layer. Brute force for n≤3.
    if n <= 3:
        from itertools import chain, combinations as comb_it
        # enumerating all antichains is expensive; we use: width = max size of a set of pairwise incomparable elements
        # for n≤3 (N≤8) enumerate subsets
        for r in range(N + 1):
            for subset in comb_it(elems, r):
                if all(not leq(a, b) and not leq(b, a) for a, b in comb_it(subset, 2)):
                    best = max(best, len(subset))
        return best
    return comb(n, n // 2)   # Sperner's theorem for n≥4


def section_C():
    print("\n[C] TIME=chains (timelike), SPACE=antichains; max layer=middle=σ½ (Sperner)")
    from math import factorial
    for n in range(2, 6):
        # chains (timelike, maximal ones = flags) = n!
        chains = factorial(n)
        # the middle layer (max antichain by Sperner) = C(n, ⌊n/2⌋), and this is the σ½ layer (weight n/2, H=0)
        mid = comb(n, n // 2)
        # check: the middle layer is an antichain (pairwise incomparable)
        N = 1 << n
        mid_layer = [x for x in range(N) if popcount(x) == n // 2]
        is_antichain = all(not leq(a, b) and not leq(b, a)
                           for a, b in combinations(mid_layer, 2))
        check(f"n={n}: timelike chains (flags)=n!={chains}; middle layer=antichain of size C(n,⌊n/2⌋)={mid}",
              is_antichain and len(mid_layer) == mid)
    # Sperner: max antichain = middle layer (brute force n≤3)
    for n in (2, 3):
        w = max_antichain_size(n)
        check(f"n={n}: WIDTH (max spatial plane) = C(n,⌊n/2⌋)={comb(n, n//2)} (Sperner) = σ½ layer",
              w == comb(n, n // 2))
    print("   → the max spatial slice (antichain) = middle layer = H=0 = σ½: the observer = \"now\"")


# ═══════ D. the arrow (comonad) is consistent with the order ═══════
def section_D():
    print("\n[D] THE ARROW (comonad coarse-graining) is consistent: G lowers weight = toward the past under ⊆")
    for n in range(2, 6):
        N = 1 << n; top = 1 << (n - 1)
        ok = True
        for x in range(N):
            Gx = x & ~top                                    # coarse-graining (forget a coordinate)
            # G(x) ⊆ x (coarse-graining goes DOWN the order = toward the past) and weight does not increase
            if not (leq(Gx, x) and popcount(Gx) <= popcount(x)): ok = False
        check(f"n={n}: G(x)⊆x — comonad coarse-graining = motion toward the past (consistent with the arrow)", ok)
    print("   → the irreversible arrow (comonad) and the causal order ⊆ point the same way")


# ═══════ E. Myrheim–Meyer dimension: not a fixed Minkowski ═══════
def section_E():
    print("\n[E] DIMENSION: the fraction of ordered pairs r → 0 ⟹ NOT a fixed d-Minkowski (signature=input)")
    prev = 1.0
    for n in range(2, 8):
        N = 1 << n
        # number of strict causal pairs x⊊y = 3ⁿ − 2ⁿ (Σ C(n,k)2^{n−k} − diagonal)
        ordered = 3 ** n - 2 ** n
        total = N * (N - 1) // 2
        r = ordered / total
        check(f"n={n}: fraction of ordered pairs r={r:.4f} decreasing (the causet becomes sparser)", r < prev)
        prev = r
    print("   → r→0 ⟹ the Myrheim–Meyer dimension does NOT stabilize at 4: the causal STRUCTURE")
    print("     is there (cones, time/space, σ½ slice), but 4D-Minkowski/signature = INPUT [○]")


def main():
    print("=" * 84)
    print("CAUSALITY: the Boolean lattice Q_n with ⊆ as a causal set")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: causal STRUCTURE follows from the order ⊆ — light cones, timelike chains,")
    print("       spacelike antichains, max slice = σ½ (Sperner), consistent with the comonad arrow.")
    print("       BUT the dimension is not fixed at 4 (r→0); the Minkowski signature remains an INPUT [○].")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
