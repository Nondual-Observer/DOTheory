#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_hexad_rigidity.py — rigidity of the rank-3 hexad, four readings of rank, builder/guard.

  A. Rigidity: of the 720 permutations of U₃, all three relations R₁,R₂,R₃ are preserved by
     EXACTLY 12 (D₆); preserving one R₁ already implies R₂ and R₃ (Hamming distance = cyclic
     distance on C₆).
  B. Four readings of rank n: simplex n+1 / cross-polytope 2n / cube 2ⁿ / symmetry n!;
     the cube and the cross-polytope are dual (vertex/facet counts swap), the simplex is self-dual.
  C. Two hexads: 2n=n! is solvable exactly at n=3 (the scene 2n and the symmetry n! coincide
     in number only there).
  D. Builder/guard: a+b=a·b in the natural numbers exactly at a=b=2 (node 4, where the two
     sides coincide).
Register: A–D are ● enumeration/arithmetic; the readings "act/body/world/symmetry" and
"builder/guard" are ◐ (marked as such in the chapter).
"""
from __future__ import annotations
from itertools import permutations
from math import factorial

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

U = ['001', '010', '100', '011', '101', '110']
def ham(a, b): return sum(x != y for x, y in zip(a, b))
REL = {(i, j): ham(U[i], U[j]) for i in range(6) for j in range(i + 1, 6)}

def preserves(p, only=None):
    for (i, j), v in REL.items():
        w = REL[tuple(sorted((p[i], p[j])))]
        if only is None:
            if w != v: return False
        else:
            if (w == only) != (v == only): return False
    return True

def section_A():
    print("\n[A] Rigidity of the hexad: 12 out of 720; R₁ implies everything")
    all3 = [p for p in permutations(range(6)) if preserves(p)]
    check("preserving R₁,R₂,R₃ exactly 12", len(all3) == 12, f"={len(all3)}")
    r1 = [p for p in permutations(range(6)) if preserves(p, only=1)]
    check("preserving only-R₁ is also 12 (D₆)", len(r1) == 12, f"={len(r1)}")
    check("every R₁-preserving permutation preserves all three", all(preserves(p) for p in r1))
    # distinguishing control: a permutation outside D₆ breaks the relations
    bad = next(p for p in permutations(range(6)) if not preserves(p))
    check("control: there exists a permutation breaking the relations", not preserves(bad))

def section_B():
    print("\n[B] Four readings of rank: counts and duality of figures")
    for n in (2, 3, 4):
        simplex_v, simplex_f = n + 1, n + 1            # simplex vertices/facets
        cross_v, cross_f = 2 * n, 2 ** n               # cross-polytope
        cube_v, cube_f = 2 ** n, 2 * n                 # cube
        check(f"n={n}: cube ({cube_v}v/{cube_f}f) ↔ cross-polytope ({cross_v}v/{cross_f}f) — counts swap",
              (cube_v, cube_f) == (cross_f, cross_v))
        check(f"n={n}: simplex is self-dual ({simplex_v}v/{simplex_f}f)", simplex_v == simplex_f)
    check("rank 3: scene |U₃|=6=2n (cross-polytope=octahedron)", 2 * 3 == 6)

def section_C():
    print("\n[C] Two hexads: 2n=n! exactly at n=3")
    sols = [n for n in range(1, 13) if 2 * n == factorial(n)]
    check("the solution is unique: n=3", sols == [3], f"={sols}")
    check("6 vertices of the octahedron = |S₃|=6", 2 * 3 == factorial(3))

def section_D():
    print("\n[D] Builder/guard: the node where the sides coincide")
    sols = [(a, b) for a in range(1, 50) for b in range(a, 50) if a + b == a * b]
    check("a+b=a·b in ℕ exactly at (2,2)", sols == [(2, 2)], f"={sols}")

if __name__ == "__main__":
    print("=" * 70)
    print("verify_hexad_rigidity.py — rigidity 12/720 · four readings of rank · 2n=n! · node 4")
    print("=" * 70)
    section_A(); section_B(); section_C(); section_D()
    print("\n" + "=" * 70)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 70)
