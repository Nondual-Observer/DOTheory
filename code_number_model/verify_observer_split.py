#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_observer_split.py — split of the observer (witness σ½ / agent "+1") = projection of κ-symmetry.

The act splits into ACTION
(outward, kartṛ/parasmaipada) and PRESENCE (inward, sākṣin/ātmanepada), witness=σ½. ★Mathematical core:
the "observer" is NOT the point σ½, but κ-INVARIANCE, manifesting in TWO ways: on the carrier U_n it is SPLIT
(κ-pairs {d,N/d} = agent↔witness, σ½ absent), in the quotient U_n/κ it is LIFTED (unified axes). And by the
GROWTH LAW the axes of rank n (split) = objects of rank n−1 (unified) — a bijection ⟹ the split = the SHADOW
of the unity of the neighboring rank. Register ●◐○: mathematics (σ½ outside the carrier, κ-pairs, lift bijection)=●;
agent/witness=Sanskrit=◐; numerical bridges of Sanskrit (6 kārakas=octahedron, 7=Fano)=✗ NOT taken. Support:
the growth law (D(M)\\{1}=axes of D(M·p)).

  A. σ½=√N OUTSIDE the carrier D(N) (κ without fixed points) = the absent center-WITNESS.
  B. κ-pairs {d,N/d} IN the carrier = agent (d<√N, outward) ↔ witness (N/d>√N, inward), 2 faces of one axis.
  C. ★LIFT BIJECTION: axes of rank n (split) = nontrivial divisors of rank n−1 (unified) — EXACTLY, for n=2..5.
  D. TWO KINDS of κ: on the carrier split (κ-pairs), in the quotient U_n/κ lifted (axes) — the counts agree.
  E. GUARD: 6 kārakas=octahedron / 7=Fano — coincidences of count, NOT structure (a base change kills them).
"""
from __future__ import annotations
import math
from itertools import combinations

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def squarefree(primes):
    N = 1
    for p in primes:
        N *= p
    return N

def divisors(N):
    return [d for d in range(1, N + 1) if N % d == 0]

PRIMES = [2, 3, 5, 7, 11, 13]


# ═══════════════ A. σ½ outside the carrier = the absent witness ═══════════════
def section_A():
    print("\n[A] σ½=√N OUTSIDE the carrier D(N) (κ without fixed points) = the absent center-WITNESS (sākṣin)")
    ok_all = True
    for k in (2, 3, 4):
        N = squarefree(PRIMES[:k])
        root = math.isqrt(N)
        is_perfect_square = root * root == N
        in_divisors = N % root == 0 and is_perfect_square
        # for a squarefree product of DISTINCT primes N is not a perfect square ⟹ √N is not a divisor
        ok = (not is_perfect_square) and (math.sqrt(N) not in divisors(N))
        ok_all = ok_all and ok
        print(f"   rank {k}: N={N}, √N={math.sqrt(N):.3f} — a divisor? {not ok and 'yes' or 'NO'} (σ½ outside the scene)")
    check("σ½=√N does NOT belong to D(N) for squarefree N (rank 2,3,4) ⟹ the witness=the absent center, "
          "the fixed point of κ is OUTSIDE the carrier (κ on U_n has no fixed point)", ok_all)


# ═══════════════ B. κ-pairs = agent↔witness (two faces of one axis) ═══════════════
def section_B():
    print("\n[B] κ-pairs {d,N/d} IN the carrier = agent (d<√N, outward) ↔ witness (N/d>√N, inward)")
    N = 30
    U = [d for d in divisors(N) if d not in (1, N)]
    root = math.sqrt(N)
    pairs = sorted(set(tuple(sorted((d, N // d))) for d in U))
    # each pair: the smaller<√N (agent/outward), the larger>√N (witness/inward)
    split_ok = all(lo < root < hi for lo, hi in pairs)
    check(f"N={N}: κ-pairs {pairs}; in each the smaller<√N<the larger (agent outward ↔ witness inward): {split_ok} "
          f"⟹ each axis is SPLIT into two faces around the absent center σ½", split_ok)


# ═══════════════ C. ★lift bijection: axes of rank n (split) = objects of rank n−1 (unified) ═══════════════
def section_C():
    print("\n[C] ★LIFT BIJECTION: axes of rank n (SPLIT, κ-pairs) = nontrivial divisors of rank n−1 (UNIFIED)")
    ok_all = True
    for k in range(2, 6):
        M = squarefree(PRIMES[:k - 1])            # rank n−1
        N = M * PRIMES[k - 1]                      # rank n = M·p
        # axes of N = κ-pairs among U_N
        U = [d for d in divisors(N) if d not in (1, N)]
        axes = set(frozenset((d, N // d)) for d in U)
        # the representative of each axis, NOT divisible by the new prime p, = a divisor of M (≠1)
        p = PRIMES[k - 1]
        reps = set()
        for ax in axes:
            d = min(ax)
            rep = d if d % p != 0 else (N // d)
            reps.add(rep)
        nontrivM = set(d for d in divisors(M) if d != 1)
        bij = (reps == nontrivM) and (len(axes) == len(nontrivM))
        ok_all = ok_all and bij
        print(f"   rank {k-1}→{k}: M={M}, N={N}: axes of N={len(axes)} (split) ↔ nontrivial divisors of M={len(nontrivM)} "
              f"(unified); representatives = D(M)\\{{1}}: {bij}")
    check("axes of rank n (κ-pairs, agent↔witness SPLIT) = nontrivial divisors of rank n−1 (UNIFIED) — a BIJECTION "
          "for n=2..5 ⟹ the split of the observer = the SHADOW of the unity of the neighboring rank", ok_all)


# ═══════════════ D. two kinds of κ: split on the carrier / lifted in the quotient ═══════════════
def section_D():
    print("\n[D] TWO KINDS of κ: on the carrier U_n it is SPLIT (κ-pairs), in the quotient U_n/κ it is LIFTED (unified axes)")
    ok_all = True
    for k in range(2, 6):
        N = squarefree(PRIMES[:k])
        U = [d for d in divisors(N) if d not in (1, N)]
        carrier = len(U)                          # |U_n| = split points
        quotient = len(set(frozenset((d, N // d)) for d in U))   # |U_n/κ| = lifted axes
        ok = (carrier == 2 ** k - 2) and (quotient == 2 ** (k - 1) - 1) and (carrier == 2 * quotient)
        ok_all = ok_all and ok
        print(f"   rank {k}: carrier |U|={carrier}=2^{k}−2 (split); quotient |U/κ|={quotient}=2^{{{k-1}}}−1 "
              f"(lifted); carrier=2×quotient: {carrier == 2 * quotient}")
    check("at every rank |U_n|=2^n−2 (split) = 2·|U_n/κ| (quotient, lifted) ⟹ κ-symmetry appears in TWO ways: "
          "as a split on the carrier and as unity in the quotient — the observer=κ, not a point", ok_all)


# ═══════════════ E. guard: the numerical bridges of Sanskrit are killed ═══════════════
def section_E():
    print("\n[E] GUARD: '6 kārakas=octahedron', '7=Fano' — coincidences of count, NOT structure (a base change kills them)")
    # the kārakas are always 6 (a fixed grammatical category); the vertices |U_n|=2^n−2 (grows)
    karaka = 6
    coincide_only_at_3 = (2 ** 3 - 2 == karaka) and all(2 ** k - 2 != karaka for k in (4, 5, 6))
    check(f"kārakas always=6; |U_n|=2^n−2 grows; the coincidence |U_n|=6 holds ONLY at n=3 (rank 4→14≠6): "
          f"{coincide_only_at_3} ⟹ '6 kārakas=octahedron' = a coincidence of the number 6 (like 4=2², 8=gluons), ✗ NOT taken; "
          f"we take only the VOICE (parasmaipada↔ātmanepada = κ-pair outward/inward, ● grammar)", coincide_only_at_3)


def main():
    print("=" * 100)
    print("SPLIT OF THE OBSERVER (witness σ½ / agent \"+1\") = projection of κ-symmetry; unity via the lift")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: 'the observer' = NOT the point σ½, but κ-INVARIANCE. σ½=√N=the absent center-WITNESS (outside")
    print("       the carrier); the agent \"+1\"=the active face (unfolds the axis outward); κ stitches (a change of voice).")
    print("       κ appears in TWO ways: on the carrier SPLIT (κ-pairs agent↔witness), in the quotient U_n/κ LIFTED")
    print("       (unified axes). ★By the growth law the axes of rank n (split) = objects of rank n−1 (unified) —")
    print("       a BIJECTION ⟹ the split = the SHADOW of the unity of the neighboring rank; the symmetry 'of the more general rank' = κ")
    print("       itself. ● mathematics; ◐ agent/witness=Sanskrit; ✗ numerical bridges (6=octahedron,7=Fano).")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
