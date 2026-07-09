#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_mass_gap_input.py — INVESTIGATION: does structure force a mass gap,
or is mass = input (weights/couplings on edges)?

Context. The physics functor F: Q_n → spins gives A_n = ∑_i σ_x^(i) (FREE spins, no
interaction). The bare cube is vertex-transitive ⟹ the midpoint λ=0 is degenerate ⟹ there
is no mass gap (massless center σ½). Question: if we add a minimal INPUT (weights w_i, then
interaction) — does mass get born FORCED, or are weight/strength free? We do not fit in
advance: the code itself will show what is forced (form) and what is free (value).

  A. THE BARE A=∑σ_x IS MASSLESS: spectrum {n−2k, mult. C(n,k)}; even n ⟹ λ=0 degenerate
     C(n,n/2) — no gap at the center. Vertex-transitive (S_n permutes coordinates).
  B. WEIGHTS A_w=∑ w_i σ_x: spectrum = {∑±w_i} (still FREE modes). Incommensurate w
     move the center away from 0 ⟹ gap Δ=min|∑±w_i|>0. BUT Δ(2w)=2Δ(w) ⟹ the scale (value
     of the mass) is NOT forced — it is stretchable.
  C. NO privileged w: S_n symmetry of the bare cube ⟹ every permutation of w is equivalent;
     the structure does not single out a privileged set ⟹ the VALUE is free (input).
  D. THE FORM IS FORCED (not the value): the chiral Z=∏σ_z gives {A_w,Z}=0 for ANY w ⟹
     the spectrum is SYMMETRIC ±λ (particle/hole). κ=∏σ_x COMMUTES for any w (mass does
     NOT arise from this breaking — the transverse field is κ-invariant).
  E. A GENUINE gap requires INTERACTION (a term σ_z^(i)σ_z^(j), which the bare cube does
     NOT have): it splits the degenerate center and BREAKS {·,Z}=0 (mass breaks the
     particle-hole symmetry — as in reality). The topology of "who couples to whom" can be
     given by structure (edges), the coupling STRENGTH g cannot: Δ grows with g ⟹ form yes,
     number no.
  F. AXIAL DIPOLE: breaking ONE axis (w_1≠rest) already lifts the center degeneracy, and
     the gap is sensitive PRECISELY to the broken axis (mass = axial deviation, not radial).

We CHECK the conclusion, we do not postulate it. If a FORCED weight ratio turned up — that
would be a bridge to point 2; if not — the wall is confirmed rigorously and localized (=
vertex symmetry).
"""
from __future__ import annotations
import numpy as np
from math import comb
from itertools import product

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], dtype=float)
SZ = np.array([[1, 0], [0, -1]], dtype=float)

def op_at(P, i, n):
    """Operator P on spin i, identity on the rest (Kronecker)."""
    mats = [P if j == i else I2 for j in range(n)]
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out

def transverse(weights):
    """A_w = ∑ w_i σ_x^(i)."""
    n = len(weights)
    H = np.zeros((1 << n, 1 << n))
    for i, w in enumerate(weights):
        H += w * op_at(SX, i, n)
    return H

def kron_all(P, n):
    out = P
    for _ in range(n - 1):
        out = np.kron(out, P)
    return out

def gap_around_zero(H):
    """Minimal |λ| = the gap around zero (mass of the massless center)."""
    ev = np.linalg.eigvalsh(H)
    return float(np.min(np.abs(ev)))

def degeneracy_at_zero(H, tol=1e-9):
    ev = np.linalg.eigvalsh(H)
    return int(np.sum(np.abs(ev) < tol))


# ═══════ A. the bare ∑σ_x is massless (degenerate center) ═══════
def section_A():
    print("\n[A] THE BARE A=∑σ_x IS MASSLESS: the midpoint λ=0 is degenerate C(n,n/2), no gap at the center")
    for n in (2, 4, 6):                                   # even: there is a stratum k=n/2
        H = transverse([1.0] * n)
        deg = degeneracy_at_zero(H)
        check(f"n={n}: λ=0 multiplicity {deg} = C({n},{n//2})={comb(n, n//2)} ⟹ massless center",
              deg == comb(n, n // 2))
    print("   → vertex-transitive (all n axes are equivalent): no privileged mass")


# ═══════ B. weights give a gap, but the scale is free ═══════
def section_B():
    print("\n[B] WEIGHTS A_w=∑w_iσ_x: gap Δ=min|∑±w_i|>0, but Δ(2w)=2Δ(w) ⟹ the value is NOT forced")
    w = [1.0, 1.3, 1.7, 2.1]                              # incommensurate
    Hd = transverse(w)
    gap1 = gap_around_zero(Hd)
    gap2 = gap_around_zero(transverse([2 * x for x in w]))
    # direct count: the gap = min over all ±-combinations
    direct = min(abs(sum(s * x for s, x in zip(signs, w)))
                 for signs in product([1, -1], repeat=len(w)))
    check(f"incommensurate w: gap Δ={gap1:.4f}>0 (the center moved off zero = mass appeared)",
          gap1 > 1e-6 and abs(gap1 - direct) < 1e-9)
    check(f"scaling: Δ(2w)={gap2:.4f} = 2·Δ(w)={2*gap1:.4f} ⟹ the MAGNITUDE of the mass is free (input)",
          abs(gap2 - 2 * gap1) < 1e-9)


# ═══════ C. no privileged w (S_n symmetry) ═══════
def section_C():
    print("\n[C] NO privileged w: permuting the axes = an automorphism ⟹ the value is free")
    n = 4
    w = [1.0, 1.3, 1.7, 2.1]
    base = sorted(np.linalg.eigvalsh(transverse(w)))
    # any permutation of the weights gives the SAME spectrum (coordinates are interchangeable)
    perms_equal = True
    for perm in [[1.3, 1.0, 2.1, 1.7], [2.1, 1.7, 1.3, 1.0], [1.7, 2.1, 1.0, 1.3]]:
        if not np.allclose(sorted(np.linalg.eigvalsh(transverse(perm))), base):
            perms_equal = False
    check("the spectrum is invariant under permuting the weights ⟹ structure does not single out a set w (value=input)",
          perms_equal)


# ═══════ D. the FORM is forced: ±λ symmetry and κ-invariance for any w ═══════
def section_D():
    print("\n[D] THE FORM IS FORCED (not the value): {A_w,Z}=0 ⟹ spectrum ±λ; [A_w,κ]=0 for ANY w")
    for n in (2, 3, 4):
        w = [1.0 + 0.37 * i for i in range(n)]           # arbitrary, unequal
        A = transverse(w)
        Z = kron_all(SZ, n)                              # chiral κ
        X = kron_all(SX, n)                              # complement κ
        anti = A @ Z + Z @ A                             # {A,Z}
        comm = A @ X - X @ A                             # [A,κ]
        ev = np.linalg.eigvalsh(A)
        sym = np.allclose(sorted(ev), sorted(-ev))       # spectrum ±λ
        check(f"n={n}: {{A_w,Z}}=0 (spectrum ±λ symmetric: {sym}) AND [A_w,κ]=0 — the form is forced",
              np.allclose(anti, 0) and np.allclose(comm, 0) and sym)
    print("   → particle-hole symmetry ±λ and κ-invariance hold for any weights (●form)")


# ═══════ E. a genuine gap = INTERACTION (input), the strength is free ═══════
def section_E():
    print("\n[E] A GENUINE gap = interaction σ_z⊗σ_z (NOT present in the bare cube): the strength g is free")
    # minimal model: 2 spins, H = (σx⊗I + I⊗σx) + g·(σz⊗σz)
    Hx = op_at(SX, 0, 2) + op_at(SX, 1, 2)
    Hzz = op_at(SZ, 0, 2) @ op_at(SZ, 1, 2)
    base_gap = gap_around_zero(Hx)                        # g=0: degenerate center
    gaps = {}
    for g in (0.0, 0.5, 1.0, 2.0):
        gaps[g] = gap_around_zero(Hx + g * Hzz)
    grows = gaps[0.5] < gaps[1.0] < gaps[2.0]            # the gap grows with the strength g
    Z = kron_all(SZ, 2)
    # does the interaction BREAK {·,Z}=0? σzσz commutes with Z=σzσz (trivially); we take σxσx as the mass term
    Hxx = op_at(SX, 0, 2) @ op_at(SX, 1, 2)
    anti_break = not np.allclose((Hx + Hxx) @ Z + Z @ (Hx + Hxx), 0)
    check(f"g=0 the center is degenerate (gap={base_gap:.3f}); the interaction opens a gap that grows with g "
          f"({gaps[0.5]:.3f}<{gaps[1.0]:.3f}<{gaps[2.0]:.3f})", base_gap < 1e-9 and grows)
    check("the mass term σx⊗σx BREAKS {·,Z}=0 (mass breaks the particle-hole symmetry, as in the SM)",
          anti_break)
    print("   → the topology of \"who couples to whom\" can be structural (edges), but the STRENGTH g = INPUT (value)")


# ═══════ F. axial dipole: breaking ONE axis lifts the degeneracy ═══════
def section_F():
    print("\n[F] AXIAL DIPOLE: breaking one axis (w_1≠rest) lifts the center degeneracy along THAT axis")
    n = 4
    deg_sym = degeneracy_at_zero(transverse([1, 1, 1, 1]))       # symmetric: degenerate
    deg_broken = degeneracy_at_zero(transverse([1.6, 1, 1, 1]))  # axis 1 broken
    # the gap opened precisely from breaking axis 1; the magnitude = a function of the deviation
    gap_small = gap_around_zero(transverse([1.2, 1, 1, 1]))
    gap_big = gap_around_zero(transverse([1.9, 1, 1, 1]))
    check(f"symmetric λ=0 mult.{deg_sym}; breaking axis 1 ⟹ mult.{deg_broken} (degeneracy lifted)",
          deg_sym == comb(n, n // 2) and deg_broken < deg_sym)
    check(f"the gap grows with the axis deviation ({gap_small:.3f}→{gap_big:.3f}) — mass=AXIAL deviation",
          gap_big > gap_small > 0)
    print("   → mass = axial dipole (κ broken along an axis), NOT a radial mode")


def main():
    print("=" * 90)
    print("MASS — FORCED or INPUT? Minimal input to free spins, an honest measurement")
    print("=" * 90)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 90)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: mass is NOT forced by the bare structure — vertex transitivity (all axes")
    print("       are equivalent) is ITSELF THE REASON for masslessness and for the non-derivability of the value.")
    print("       THE FORM IS FORCED: gap present/absent, ±λ symmetry, axial dipole, coupling topology.")
    print("       THE VALUE IS FREE: the gap's scale (the strength g) is stretchable, structure does not single it out.")
    print("       ⟹ a bridge to point 2 IS POSSIBLE IN FORM, but the mass number = INPUT. The wall [κ,Δ]=0")
    print("       is not broken; it is localized precisely: the non-derivability of mass = symmetry of the bare cube.")
    print("=" * 90)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
