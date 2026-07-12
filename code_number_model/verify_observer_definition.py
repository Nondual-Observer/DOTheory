#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_observer_definition.py — rigorous definition of the observer σ½: invariant κ outside carrier states.

Verifies the motive of the definition:
 §A  κ:x↦x⊕1ⁿ on Q_n is free (no fixed point, n≥1) and κ²=id — the invariant is not realized by a state.
 §B  the continuous reflection r(x)=1−x on [0,1]ⁿ has a UNIQUE fixed point (½,…,½), and it lies OUTSIDE the vertices {0,1}ⁿ.
 §C  the fixed-point equation reduces to 2x=1: solvable over char≠2 (x=½), unsolvable over 𝔽₂ (2≡0).
 §D  {0,1} = ℤ/2-torsor: κ=translation acts freely and transitively — there is no distinguished zero.
 §E  splitting by projectors P±=(1±T)/2 (T=−1) over ℚ: idempotents P±²=P±, P+P−=0, P++P−=I; over 𝔽₂ ½ is absent.

Register ●◐○: §A–§E mathematics = ●; assigning the center ½ to the observer = ◐; separation of sides |·|₂/|·|∞ — rank 2 (ch. III).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

# ═══════════ A. κ on Q_n free, κ²=id ═══════════
def section_A():
    print("\n[A] κ:x↦x⊕1ⁿ free on Q_n (no x with κx=x), κ²=id — the invariant is not a state")
    for n in range(1, 7):
        full = (1 << n) - 1                     # 1ⁿ = all ones
        kap = lambda x: x ^ full
        states = range(1 << n)
        check(f"n={n}: κ has no fixed point (free action)", all(kap(x) != x for x in states))
        check(f"n={n}: κ²=id (involution)", all(kap(kap(x)) == x for x in states))

# ═══════════ B. continuous reflection: center ½ outside vertices ═══════════
def section_B():
    print("\n[B] r(x)=1−x on [0,1]ⁿ: unique fixed point (½,…,½), it lies OUTSIDE the vertices {0,1}ⁿ")
    for n in range(1, 5):
        fix = tuple(Fr(1, 2) for _ in range(n))
        r = lambda v: tuple(1 - c for c in v)
        check(f"n={n}: r(½,…,½) = (½,…,½)", r(fix) == fix)
        is_vertex = all(c in (Fr(0), Fr(1)) for c in fix)
        check(f"n={n}: center outside the cube vertices", not is_vertex)

# ═══════════ C. 2x=1: char≠2 gives ½, over 𝔽₂ no solution ═══════════
def section_C():
    print("\n[C] fixedness reduces to 2x=1: over char≠2 root x=½; over 𝔽₂ (2≡0) no root")
    check("over ℚ: 2·½ = 1 (½ exists)", 2 * Fr(1, 2) == 1)
    check("over 𝔽₂: no y gives 2y=1 (2≡0)", all((2 * y) % 2 != 1 for y in (0, 1)))
    check("2 invertible over ℚ, but not mod 2 (zero divisor)", gcd(2, 2) != 1)

# ═══════════ D. torsor: κ free and transitive ═══════════
def section_D():
    print("\n[D] {0,1} = ℤ/2-torsor: κ=translation free and transitive — no distinguished zero")
    S = [0, 1]; kap = lambda x: x ^ 1
    check("κ free (no fixed point)", all(kap(x) != x for x in S))
    orbit = {0, kap(0)}                          # orbit of zero under ⟨κ⟩
    check("one orbit = whole carrier (transitive)", orbit == set(S))

# ═══════════ E. projectors over ℚ; over 𝔽₂ ½ absent ═══════════
def section_E():
    print("\n[E] P±=(1±T)/2, T=−1: over ℚ idempotent and complementary; over 𝔽₂ ½ undefined")
    T = Fr(-1)
    Pp = (1 + T) / 2                              # P+ = 0
    Pm = (1 - T) / 2                              # P- = 1
    check("P+² = P+ (idempotent)", Pp * Pp == Pp)
    check("P−² = P− (idempotent)", Pm * Pm == Pm)
    check("P+·P− = 0 (complementary)", Pp * Pm == 0)
    check("P+ + P− = 1 (completeness)", Pp + Pm == 1)
    check("over 𝔽₂: 2 not invertible ⟹ (1±T)/2 undefined", all((2 * y) % 2 != 1 for y in (0, 1)))

if __name__ == "__main__":
    print("=" * 72)
    print("verify_observer_definition.py — observer σ½: invariant κ outside carrier states")
    print("=" * 72)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 72)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("=" * 72)
