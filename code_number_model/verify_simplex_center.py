#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_simplex_center.py — control: the simplex {e,i,π} has NO forced observer-center.

Checks THREE things at once:
  (1) Concurrence of triangle altitudes — ALWAYS (Euclid, any triangle) ⟹ trivial, not evidence (§A).
  (2) The «center» is NOT unique and is frame-dependent: orthocenter H ≠ centroid G ≠ circumcenter O for asymmetric
      realizations {e,i,π}; they coincide only under IMPOSED equilaterality, which erases the constants themselves (§B–§D).
  (3) The forced anchor — on the DISCRETE cube, not in the metric: a unique minimum ⊥ of the lattice (minimality
      of order, without metric) + κ without fixed points (the center √N outside the vertices). The structure is forced, the metric is not (§E).
  (4) The vertices {e,i,π} are NOT symmetric: a forced hierarchy of roles (carrier/operator/measure) = projection of ι²=id;
      i of order 4 (i²=κ), κ of order 2, (e^{iπ})²=id, e — the natural base (§F).

Register ●◐○: §A–§F mathematics = ●; identification of roles with ι²=id = ◐; «living interaction» (|·|∞) not forced = ○.
Support: e^{iπ}=−1 forced from κ²=id.
"""
from __future__ import annotations
import math

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

# ─────────── triangle geometry ───────────
def _solve2(a,b,c,d,e,f):
    det = a*d - b*c
    return ((e*d - b*f)/det, (a*f - e*c)/det)

def centroid(A,B,C):
    return ((A[0]+B[0]+C[0])/3.0, (A[1]+B[1]+C[1])/3.0)

def orthocenter(A,B,C):
    bc=(C[0]-B[0], C[1]-B[1]); ac=(C[0]-A[0], C[1]-A[1])
    e = bc[0]*A[0]+bc[1]*A[1]; f = ac[0]*B[0]+ac[1]*B[1]
    return _solve2(bc[0],bc[1], ac[0],ac[1], e, f)

def circumcenter(A,B,C):
    ab=(B[0]-A[0],B[1]-A[1]); ac=(C[0]-A[0],C[1]-A[1])
    e = ab[0]*(A[0]+B[0])/2 + ab[1]*(A[1]+B[1])/2
    f = ac[0]*(A[0]+C[0])/2 + ac[1]*(A[1]+C[1])/2
    return _solve2(ab[0],ab[1], ac[0],ac[1], e, f)

def dist(P,Q): return math.hypot(P[0]-Q[0],P[1]-Q[1])

def altitude_residual(A,B,C):
    # the altitude from C passes through the orthocenter ⟺ (H-C)·(B-A)=0
    H = orthocenter(A,B,C); ba=(B[0]-A[0],B[1]-A[1])
    return H, (H[0]-C[0])*ba[0]+(H[1]-C[1])*ba[1]

REAL = {
 "R1 literal (e,0),(π,0),(0,1)": ((math.e,0.0),(math.pi,0.0),(0.0,1.0)),
 "R2 Euler   1, i, -1":          ((1.0,0.0),(0.0,1.0),(-1.0,0.0)),
 "R3 equilateral":               ((1.0,0.0),(-0.5,math.sqrt(3)/2),(-0.5,-math.sqrt(3)/2)),
 "R4 log     (1,0),(ln π,0),(0,1)": ((1.0,0.0),(math.log(math.pi),0.0),(0.0,1.0)),
}

# ═══════════ A. altitudes concur — always (trivial) ═══════════
def section_A():
    print("\n[A] Altitudes concur ALWAYS (Euclid) — trivially, not specific to {e,i,π}")
    for name,(A,B,C) in REAL.items():
        _,res = altitude_residual(A,B,C)
        check(f"concurrence of altitudes: {name}", abs(res) < 1e-9, f"residual={res:.1e}")

# ═══════════ B. center is NOT unique (asymmetric realizations) ═══════════
def section_B():
    print("\n[B] H≠G≠O in asymmetric realizations — the «center» is not uniquely defined")
    for key in ("R1 literal (e,0),(π,0),(0,1)", "R2 Euler   1, i, -1", "R4 log     (1,0),(ln π,0),(0,1)"):
        A,B,C = REAL[key]
        G=centroid(A,B,C); H,_=altitude_residual(A,B,C); O=circumcenter(A,B,C)
        spread = max(dist(H,G), dist(G,O), dist(H,O))
        check(f"three centers diverge: {key}", spread > 1e-3, f"spread={spread:.3f}")

# ═══════════ C. coincide ONLY under imposed equilaterality ═══════════
def section_C():
    print("\n[C] H=G=O only under equilaterality — but it erases the distinction e,i,π")
    A,B,C = REAL["R3 equilateral"]
    G=centroid(A,B,C); H,_=altitude_residual(A,B,C); O=circumcenter(A,B,C)
    check("equilateral: three centers coincided", max(dist(H,G),dist(G,O)) < 1e-9)
    # substantively: for the centers to coincide, equilaterality is needed — and the real e,i,π do NOT give it.
    # the literal R1 (true values) is NOT equilateral and the centers there do not coincide (see §B):
    a,b,c = REAL["R1 literal (e,0),(π,0),(0,1)"]
    sides = sorted([dist(a,b), dist(b,c), dist(a,c)])
    check("real {e,i,π} (R1) NOT equilateral ⟹ the coincidence is bought by changing the shape",
          (sides[2]-sides[0]) > 0.1, f"sides={[round(s,3) for s in sides]}")

# ═══════════ D. Euler realization: the orthocenter SITS on vertex i ═══════════
def section_D():
    print("\n[D] Realization {1,i,-1}: orthocenter = vertex i (the center collapses into the agent)")
    A,B,C = REAL["R2 Euler   1, i, -1"]   # B = (0,1) = i
    H,_ = altitude_residual(A,B,C)
    check("orthocenter == vertex i", dist(H,(0.0,1.0)) < 1e-9, f"H={H}")
    G = centroid(A,B,C)
    check("centroid ≠ i (the center is not unique even here)", dist(G,(0.0,1.0)) > 1e-3)

# ═══════════ E. the forced anchor — on the discrete cube, without metric ═══════════
def section_E():
    print("\n[E] What is FORCED: minimum of the lattice (order) + κ without fixed points (involution) — no metric needed")
    # Q_2 = Boolean lattice of divisors of p*q ; vertices = bit vectors; order = inclusion
    verts = [(0,0),(1,0),(0,1),(1,1)]
    leq = lambda a,b: a[0]<=b[0] and a[1]<=b[1]
    mins = [v for v in verts if all((not leq(u,v)) or u==v for u in verts)]
    check("unique minimum ⊥ of the lattice (forced by order, without metric)", mins == [(0,0)])
    # κ = complement x↦1-x coordinatewise; no fixed vertices ⟹ the center is outside the carrier
    kappa = lambda x: (1-x[0], 1-x[1])
    fixed = [v for v in verts if kappa(v)==v]
    check("κ without fixed points on the vertices (the center √N is absent, not chosen)", fixed == [])
    check("κ²=id (involution)", all(kappa(kappa(v))==v for v in verts))

# ═══════════ F. vertices NOT symmetric: hierarchy of roles = projection of ι²=id ═══════════
def section_F():
    print("\n[F] {e,i,π} — a forced hierarchy of roles (carrier/operator/measure), projection of ι²=id")
    i = 1j
    check("i² = κ = -1  (i NOT an involution; i²=id false)", abs(i*i - (-1)) < 1e-12)
    check("i⁴ = id  (order of i = 4, operator-root √κ)", abs(i**4 - 1) < 1e-12)
    check("κ² = id  (order of κ = 2 — this is the true ι²=id)", ((-1)**2) == 1)
    check("e^{iπ} = κ = -1  (result = inversion)", abs(cmath_exp(i*math.pi) - (-1)) < 1e-12)
    check("(e^{iπ})² = e^{i2π} = id  (‹²› realized by doubling π→2π)", abs(cmath_exp(i*2*math.pi) - 1) < 1e-9)
    # e — the natural base: (e^h - 1)/h → 1 (the exponential is its own derivative); π^h does not do so
    d_e  = (math.e**1e-6 - 1)/1e-6
    d_pi = (math.pi**1e-6 - 1)/1e-6
    check("e — the unique natural base: d/dx e^x|₀ = 1 (carrier of the bridge +→×)", abs(d_e - 1) < 1e-3, f"={d_e:.4f}")
    check("π does NOT behave so: d/dx π^x|₀ = ln π ≠ 1 (π — a measure, not a carrier)", abs(d_pi - math.log(math.pi)) < 1e-3)

def cmath_exp(z):
    import cmath; return cmath.exp(z)

if __name__ == "__main__":
    print("="*70)
    print("verify_simplex_center.py — the center of the simplex {e,i,π}: a hinge, not an observer")
    print("="*70)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "="*70)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("="*70)
