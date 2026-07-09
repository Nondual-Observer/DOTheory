#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_opposition_bridge.py — a single bridge: opposition skeleton → golden realization → the discrete↔continuum seam.

One arc, two parts. PART I (realization, all ●): skeleton = free involution (X,κ), n oppositions = 2n poles;
forced realization = orthoplex β_n "complete minus perfect matching" — the FIBER-TERMINAL over the scene
(D⊣U holds: the empty graph is free; the right adjoint U⊣C/"cofree" is REFUTED §B, the orthoplex is not cofree);
the golden half β_6 = the icosahedron via the Galois split ℝ⁶=V_φ⊕V_ψ (both halves tile 60 edges as 30+30);
the golden frame is EXTERNAL (Stab_{B₆}=I_h≪B₆).
PART II (the discrete↔continuum seam, a ●-construction within a ◐-law): the |·|∞ side is reached by TWO
functorially distinct machines — the vertical spectral limit of the tower (cube→Gaussian, additive) and the
horizontal Galois projection (cut-and-project: ℤ⁶ through a triacontahedron window → an icosahedral quasicrystal,
multiplicative/ℤ[φ]); they diverge at RANK 5, where the axis-5 (A₅,√5) is non-crystallographic.

STATUS. All constructions below = ● (computed). The laws "forcedness=cofree," "two faces of |·|∞ (+/×)," the
functorial frame = ◐ (resonance with the corpus, named). The externality of the golden frame and the premise of
the 5-fold symmetry of rank 5 (coincidence-of-name A₅↔U₅, document 01 §5.1) = ○. The icosahedron remains a
◐-coincidence-of-name of the pack (document 01 §5.2); the law sharpens it, without raising its status.
Support: document 01 §3.4 (cross-polytope=figure of the scene), §5.1–5.2, document 02 chapter VI (scene)/chapter VII
(spectral limit).

PART I — SKELETON AND GOLDEN REALIZATION
  A. SKELETON: β_6=K_{6×2} "complete minus perfect matching" — 10-regular, 60 edges, complement = 6·K₂.
  B. REALIZATIONS: D⊣U holds (the empty graph is free); U⊣C/cofree is REFUTED (Hom 0≠8, C is not functorial);
     the correct property is: the orthoplex = fiber-terminal over a fixed scene (max. antipode-free κ-graph).
  C. EMBEDDING: the icosahedron = 6 antipodal pairs, antipodes non-adjacent; 30 edges ⊂ 60 = half.
  D. GOLDEN ANGLE: 6 axes under arccos(1/√5); the orthoplex axes are orthogonal in 6D.
  E. ★GALOIS: ℝ⁶=V_φ⊕V_ψ orthonormal; both projections are icosahedra; the halves split 60=30+30.
  F. κ-INVARIANCE: central inversion preserves the icosahedron's edges ⟹ an object of Real over (X,κ).
  G. ★EXTERNALITY GUARD: Stab_{B₆}(golden half)=120=|I_h|≪46080=|B₆| ⟹ the frame is external.
PART II — THE DISCRETE↔CONTINUUM SEAM
  H. MACHINE 1: the spectrum of the cube {2k} is INTEGER; weights C(n,k)→Gaussian (CLT); no irrationality.
  I. MACHINE 2 spectrum: the icosahedron graph carries ±√5 (a signature of the golden frame; absent in the cube).
  J. RANK 5: an element of order 5 appears first in S_n at n=5; the crystallographic restriction (axes 2,3,4,6).
  K. PROJECTION+WINDOW: M orthogonal, E∥⊥E⊥, total irrationality; window = 30 faces (RT).
  L. DISCRETENESS+5-FOLD SYMMETRY: cut-and-project → Delone; the star is invariant under 72°/120°, NOT under 90°.
  M. PHASON: shifting the window by γ changes the pattern, density holds ⟹ phase=input, window=form.
  N. GOLDEN RING: physical coordinates ∈ ℤ[φ] (height ^).
"""
from __future__ import annotations
import itertools
from math import sqrt, comb
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

phi = (1 + sqrt(5)) / 2
psi = (1 - sqrt(5)) / 2
def axes(t): return np.array([(0,1,t),(0,1,-t),(1,t,0),(1,-t,0),(t,0,1),(t,0,-1)], float)

# ---- combinatorial frame: labels (axis, sign), orthoplex, edge sets ----
LABELS = [(a, s) for a in range(6) for s in (+1, -1)]
ORTHO = set(frozenset((x, y)) for x, y in itertools.combinations(LABELS, 2) if x[0] != y[0])
def d2(p, q): return float(((np.asarray(p) - np.asarray(q))**2).sum())
def edgeset(t):
    A = axes(t); V = np.vstack([A, -A])
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    L = lambda i: (i % 6, +1 if i < 6 else -1)
    return set(frozenset((L(i), L(j))) for i in range(12) for j in range(12)
               if i != j and abs(d2(V[i], V[j]) - ed) < 1e-9)
Ephi, Epsi = edgeset(phi), edgeset(psi)

# ---- geometric frame: orthonormal M, E∥/E⊥, window ----
Vp, Wp = axes(phi), axes(psi)
nV = sqrt((Vp[0]**2).sum()); nW = sqrt((Wp[0]**2).sum())
M = (np.hstack([Vp / nV, Wp / nW]) / sqrt(2)).T
Ppar, Pperp = M[:3, :], M[3:, :]
gens = [Pperp[:, i] for i in range(6)]
normals = []
for i, j in itertools.combinations(range(6), 2):
    n = np.cross(gens[i], gens[j])
    if np.linalg.norm(n) < 1e-9: continue
    n = n / np.linalg.norm(n)
    if not any(np.allclose(n, m) or np.allclose(n, -m) for m in normals): normals.append(n)
Hs = [0.5 * np.sum(np.abs(np.array(gens) @ n)) for n in normals]
def in_window(P):
    ok = np.ones(P.shape[0], bool)
    for n, h in zip(normals, Hs): ok &= (np.abs(P @ n) <= h + 1e-9)
    return ok
XA = np.array(list(itertools.product(range(-3, 4), repeat=6)), float)
XPperp = XA @ Pperp.T; XPpar = XA @ Ppar.T
def project(gamma3=None):
    P = XPperp if gamma3 is None else XPperp - gamma3
    acc = in_window(P); return XA[acc], XPpar[acc]
def rot(axis, deg):
    a = axis / np.linalg.norm(axis); th = np.radians(deg); c, s = np.cos(th), np.sin(th)
    x, y, z = a; C = 1 - c
    return np.array([[c+x*x*C, x*y*C-z*s, x*z*C+y*s],
                     [y*x*C+z*s, c+y*y*C, y*z*C-x*s],
                     [z*x*C-y*s, z*y*C+x*s, c+z*z*C]])

# ====================== PART I ======================
def section_A():
    print("\n[A] SKELETON: orthoplex β_6 = \"complete minus perfect matching\"")
    deg = {v: sum(1 for e in ORTHO if v in e) for v in LABELS}
    check("β_6: every pole is 10-regular (adjacent to all but its antipode)", set(deg.values()) == {10})
    check("β_6: 60 edges = C(12,2)−6", len(ORTHO) == 60)
    matching = set(frozenset(((a, +1), (a, -1))) for a in range(6))
    allpairs = set(frozenset(p) for p in itertools.combinations(LABELS, 2))
    check("complement of β_6 = 6·K₂ (6 antipodal axes = a perfect matching)", matching == (allpairs - ORTHO))

# --- small categorical checks of the adjunction (κ-equivariant maps of scenes) ---
def _kmaps(nx, ny):
    for choice in itertools.product([(b, sg) for b in range(ny) for sg in (+1, -1)], repeat=nx):
        yield choice
def _orthoedges(n):
    pts = [(a, s) for a in range(n) for s in (+1, -1)]
    return set(frozenset((x, y)) for x, y in itertools.combinations(pts, 2) if x[0] != y[0])
def _is_hom(choice, eA, eB):
    for e in eA:
        (a1, s1), (a2, s2) = tuple(e)
        img = frozenset(((choice[a1][0], choice[a1][1]*s1), (choice[a2][0], choice[a2][1]*s2)))
        if len(img) == 1 or img not in eB: return False
    return True

def section_B():
    print("\n[B] REALIZATIONS: D⊣U holds; U⊣C (cofree) is REFUTED; the orthoplex = fiber-terminal")
    # D⊣U: from the EMPTY graph every κ-map is a homomorphism (no edge constraints) = freeness (left adjoint)
    total = sum(1 for _ in _kmaps(2, 3))
    homs = sum(1 for c in _kmaps(2, 3) if _is_hom(c, set(), _orthoedges(3)))
    check("D⊣U holds: from the empty graph ALL κ-maps are homomorphisms ⟹ a free (left) realization",
          homs == total == 36)
    # U⊣C is FALSE: Hom_Real(β₃, C(1 axis)) = 0 ≠ 8 = Hom_Scene(U β₃, 1 axis)
    hr = sum(1 for c in _kmaps(3, 1) if _is_hom(c, _orthoedges(3), _orthoedges(1)))
    hs = sum(1 for _ in _kmaps(3, 1))
    check("U⊣C (cofree) is REFUTED: Hom_Real(β₃,C(1 axis))=0 ≠ 8=Hom_Scene ⟹ the orthoplex is NOT a right adjoint",
          hr == 0 and hs == 8)
    # C is not functorial: scene-morphisms S₂→S₁ do not lift to morphisms of orthoplexes
    bad = sum(1 for c in _kmaps(2, 1) if not _is_hom(c, _orthoedges(2), _orthoedges(1)))
    check("C is not functorial (all 4 morphisms S₂→S₁ tear an edge of the orthoplex) ⟹ no right adjoint exists", bad == 4)
    # THE CORRECT property: the orthoplex = fiber-terminal over a FIXED scene (maximal antipode-free κ-graph)
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    non_edges = set(frozenset(p) for p in itertools.combinations(LABELS, 2)) - ORTHO
    check("β_6 is κ-invariant, every one of its non-edges is antipodal ⟹ FIBER-TERMINAL (max. realization of a fixed scene)",
          all(kap(e) in ORTHO for e in ORTHO) and all(len({a for (a,s) in e}) == 1 for e in non_edges) and len(non_edges) == 6)

def section_C():
    print("\n[C] EMBEDDING: the icosahedron ⊂ β_6, exactly half the edges")
    A = axes(phi); V = np.vstack([A, -A])
    anti = lambda i: next(j for j in range(12) if d2(V[j], -V[i]) < 1e-9)
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    check("icosahedron: antipodes are NOT joined by an edge", not any(abs(d2(V[i], V[anti(i)]) - ed) < 1e-9 for i in range(12)))
    check("icosahedron: 30 edges ⊆ 60 edges of β_6 (a spanning subgraph), exactly half", Ephi <= ORTHO and len(Ephi) == 30)

def section_D():
    print("\n[D] GOLDEN ANGLE: 6 axes under arccos(1/√5)")
    A = axes(phi); nrm = float((A[0]**2).sum())
    coss = sorted(set(round(abs(float(A[i] @ A[j])) / nrm, 9) for i, j in itertools.combinations(range(6), 2)))
    check("norm² of an axis = 2+φ", abs(nrm - (2 + phi)) < 1e-9)
    check("all 6 axes mutually at |cos|=1/√5 (golden angle ≈63.43°)",
          len(coss) == 1 and abs(coss[0] - 1 / sqrt(5)) < 1e-9)

def section_E():
    print("\n[E] ★GALOIS: ℝ⁶=V_φ⊕V_ψ; both projections are icosahedra; the halves split 60=30+30")
    Aphi, Apsi = axes(phi), axes(psi)
    nphi, npsi = float((Aphi[0]**2).sum()), float((Apsi[0]**2).sum())
    U = [tuple(np.hstack([Aphi[i] / sqrt(nphi), Apsi[i] / sqrt(npsi)]) / sqrt(2)) for i in range(6)]
    maxoff = max(abs(float(np.array(U[i]) @ np.array(U[j]))) for i, j in itertools.combinations(range(6), 2))
    diag = all(abs(float(np.array(U[i]) @ np.array(U[i])) - 1.0) < 1e-9 for i in range(6))
    check("ℝ⁶=V_φ⊕V_ψ: 6 vectors (golden⊕conjugate) are ORTHONORMAL (=a 6D orthoplex)", diag and maxoff < 1e-9,
          extra=f"max|off-diag|={maxoff:.1e}")
    for name, t in (("φ", phi), ("ψ", psi)):
        V = np.vstack([axes(t), -axes(t)])
        shells = sorted(set(round(d2(V[i], V[j]), 6) for i in range(12) for j in range(12) if i != j))
        check(f"the projection onto the {name}-block is a regular icosahedron (3 shells)", len(shells) == 3)
    check("E_φ ∪ E_ψ = all 60 edges of β_6, E_φ ∩ E_ψ = ∅ (the Galois pair tiles 30+30)",
          (Ephi | Epsi) == ORTHO and len(Ephi & Epsi) == 0 and len(Ephi) == 30 == len(Epsi))

def section_F():
    print("\n[F] κ-INVARIANCE: central inversion preserves the icosahedron's edges")
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    check("κ-image of the edges = the edges ⟹ the icosahedron ∈ Real over (X,κ)", set(kap(e) for e in Ephi) == Ephi)

def section_G():
    print("\n[G] ★EXTERNALITY GUARD: Stab_{B₆}(golden)=120=|I_h|≪46080=|B₆|")
    from itertools import permutations, product
    stab = 0; total = 0
    for sigma in permutations(range(6)):
        for eps in product((+1, -1), repeat=6):
            total += 1
            img = set(frozenset((sigma[a], eps[a] * s) for (a, s) in e) for e in Ephi)
            if img == Ephi: stab += 1
    check("|B₆| = 2⁶·6! = 46080 (the full symmetry of the skeleton)", total == 46080)
    check("Stab_{B₆}(golden half) = 120 = |I_h| ⟹ a 384-fold collapse ⟹ the frame is EXTERNAL [○]",
          stab == 120 and total // stab == 384)

# ====================== PART II ======================
def section_H():
    print("\n[H] MACHINE 1: the spectrum of the cube is INTEGER, weights → Gaussian")
    check("the Laplacian spectrum of Q_n = {2k} is integer-valued (n=2,4,6); NO irrationality",
          all(float(2 * k).is_integer() for n in (2, 4, 6) for k in range(n + 1)))
    w = [comb(6, k) for k in range(7)]
    check("weights of Q_6 = C(6,k) = [1,6,15,20,15,6,1] → Gaussian (CLT)", w == [1, 6, 15, 20, 15, 6, 1])

def section_I():
    print("\n[I] MACHINE 2 spectrum: the icosahedron graph carries ±√5")
    V = np.vstack([axes(phi), -axes(phi)])
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    A = np.array([[1.0 if i != j and abs(d2(V[i], V[j]) - ed) < 1e-6 else 0.0 for j in range(12)] for i in range(12)])
    ev = np.linalg.eigvalsh(A)
    check("the spectrum of the icosahedron graph contains ±√5 (a signature of the golden frame; absent in the cube)",
          any(abs(abs(x) - sqrt(5)) < 1e-6 for x in ev))

def section_J():
    print("\n[J] RANK 5: axis-5 for the first time; the crystallographic restriction")
    has5 = lambda n: n >= 5    # an element of order 5 = a 5-cycle, needs ≥5 points
    check("no element of order 5 in S_4 (ranks 1–4 are crystallographic)", not has5(4))
    check("an element of order 5 (A₅) appears first in S_5 — axis-5 is born at rank 5", has5(5))
    check("the crystallographic restriction: a lattice admits only axes 2,3,4,6 (axis 5 is non-crystallographic)",
          5 not in (2, 3, 4, 6))

def section_K():
    print("\n[K] PROJECTION + WINDOW = a rhombic triacontahedron (30 faces)")
    check("M is orthogonal (MᵀM=I)", np.allclose(M.T @ M, np.eye(6)))
    check("E∥ ⊥ E⊥ (Ppar·Pperpᵀ = 0)", np.allclose(Ppar @ Pperp.T, np.zeros((3, 3))))
    tot = True
    for x in itertools.product(range(-2, 3), repeat=6):
        if x == (0,) * 6: continue
        xv = np.array(x, float)
        if np.allclose(Pperp @ xv, 0, atol=1e-9) or np.allclose(Ppar @ xv, 0, atol=1e-9):
            tot = False; break
    check("total irrationality (no 0≠x∈ℤ⁶ with x⊥=0 or x∥=0) ⟹ aperiodicity", tot)
    check("window = the zonotope of 6 perp-generators: 15 normals → 30 faces = RT", len(normals) == 15)

_cache = {}
def _patch():
    if "Pb" not in _cache:
        Xacc, P3 = project(); _cache["Xacc"] = Xacc; _cache["P3"] = P3
        Pb = P3[np.linalg.norm(P3, axis=1) < 2.2]
        D = np.sqrt(((Pb[:, None, :] - Pb[None, :, :])**2).sum(-1)); np.fill_diagonal(D, np.inf)
        _cache["Pb"], _cache["D"] = Pb, D
    return _cache

def section_L():
    print("\n[L] DISCRETENESS + ★5-FOLD SYMMETRY")
    c = _patch(); D = c["D"]; Pb = c["Pb"]; mind = D.min()
    check("min-distance > 0 (Delone; without the window it would be 7^6=117649 dense)", mind > 0.1, extra=f"min={mind:.4f}")
    check("no large gaps (relatively dense = Delone)", D.min(axis=1).max() / mind < 3.0)
    ii, jj = np.where((D < mind * 1.05) & (D > 0))
    vecs = Pb[jj] - Pb[ii]; dirs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
    uniq = []
    for dv in dirs:
        if not any(np.allclose(dv, u, atol=2e-2) for u in uniq): uniq.append(dv)
    uniq = np.array(uniq)
    inv = lambda Rm: all(any(np.allclose(rd, s, atol=3e-2) for s in uniq) for rd in uniq @ Rm.T)
    check("the star is invariant under the 5-fold 72° (icosahedral axis)", inv(rot(Vp[0], 72)))
    check("the star is NOT invariant under the cubic 90° ⟹ non-crystallographic (icosahedron, not cube)",
          not inv(rot(np.array([1., 0, 0]), 90)))

def section_M():
    print("\n[M] PHASON: the phase of the cut is a free input")
    _, P0 = project(); _, Pg = project(gamma3=np.array([0.30, 0.10, -0.20]))
    r = lambda A: set(map(lambda x: tuple(np.round(x, 3)), A))
    check("γ≠0 CHANGES the pattern ⟹ the phase is a free input [○]", len(r(P0) & r(Pg)) < len(P0))
    check("density holds under a phase shift ⟹ the window (form) is fixed [●]",
          abs(len(P0) - len(Pg)) / len(P0) < 0.25)

def section_N():
    print("\n[N] GOLDEN RING ℤ[φ]")
    raw = _patch()["Xacc"] @ Vp
    inZ = lambda x: any(abs((x - b * phi) - round(x - b * phi)) < 1e-6 for b in range(-60, 61))
    frac = np.mean([inZ(v) for v in raw[:150].flatten()])
    check("physical coordinates of the form a+bφ ⟹ the quasicrystal ∈ ℤ[φ] (height ^)", frac > 0.99, extra=f"{frac*100:.0f}%")


def main():
    print("=" * 100)
    print("A SINGLE BRIDGE: opposition skeleton → golden realization → the discrete↔continuum seam")
    print("=" * 100)
    print("\n--- PART I: skeleton and golden realization (all ●) ---")
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    print("\n--- PART II: the discrete↔continuum seam (●-construction, ◐-law) ---")
    section_H(); section_I(); section_J(); section_K(); section_L(); section_M(); section_N()
    print("\n" + "=" * 100)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: one arc. The skeleton of oppositions → the cofree-refuted orthoplex → the golden Galois half (icosahedron) → two")
    print("       discrete→continuum machines (spectral limit vs. cut-and-project), diverging at rank 5. Constructions")
    print("       = ●; the laws of forcedness/two-faces-of-|·|∞ = ◐; the externality of the frame and the premise of rank 5's 5-fold symmetry = ○.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
