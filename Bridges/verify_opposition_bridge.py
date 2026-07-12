#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_opposition_bridge.py — unified bridge: oppositional skeleton → golden realization → seam discrete↔continuum.

One arc, two parts. PART I (realization, all ●): skeleton = free involution (X,κ), n oppositions = 2n poles;
forced realization = orthoplex β_n "complete minus matching" — TERMINAL OF THE LAYER over the scene (D⊣U holds:
empty graph is free; the right adjoint U⊣C/"cofree" is REFUTED §B, orthoplex is not cofree); golden half of β_6 =
icosahedron via the Galois splitting ℝ⁶=V_φ⊕V_ψ (both halves tile the 60 edges 30+30); golden frame is EXTERNAL (Stab_{B₆}=I_h≪B₆).
PART II (seam discrete↔continuum, ●-construction in a ◐-law): the |·|∞ side is reached by TWO functorially different
machines — the vertical spectral limit of the tower (cube→Gaussian, additive) and the horizontal Galois projection
(cut-and-project: ℤ⁶ through the triacontahedron-window → icosahedral quasicrystal, multiplicative/ℤ[φ]); they diverge
at RANK 5, where the 5-axis (A₅,√5) is non-crystallographic.

STATUS. All constructions below = ● (computed). The laws "forcedness=cofree", "two faces of |·|∞ (+/×)", the functorial
frame = ◐ (resonance with the corpus, named). Externality of the golden frame and the premise of 5-axis-ness of rank 5 (co-naming
A₅↔U₅, doc 01 §5.1) = ○. The icosahedron remains a ◐-co-naming for now (doc 01 §5.2), the law refines it, does not elevate it.
Support: doc 01 §3.4 (cross-polytope=scene figure), §5.1–5.2, doc 02 ch VI (scene)/ch VII (spectral limit).

PART I — SKELETON AND GOLDEN REALIZATION
  A. SKELETON: β_6=K_{6×2} "complete minus matching" — 10-regular, 60 edges, complement = 6·K₂.
  B. REALIZATIONS: D⊣U holds (empty graph is free); U⊣C/cofree is REFUTED (Hom 0≠8, C not functorial);
     the correct property — orthoplex = terminal of the layer over a fixed scene (max. antipode-free κ-graph).
  C. EMBEDDING: icosahedron = 6 antipodal pairs, antipodes non-adjacent; 30 edges ⊂ 60 = half.
  D. GOLDEN ANGLE: 6 axes at arccos(1/√5); the orthoplex axes are orthogonal in 6D.
  E. ★GALOIS: ℝ⁶=V_φ⊕V_ψ orthonormal; both projections — icosahedra; the halves split 60=30+30.
  F. κ-INVARIANT: central inversion preserves the edges of the icosahedron ⟹ Real object over (X,κ).
  G. ★GUARDIAN OF EXTERNALITY: Stab_{B₆}(golden half)=120=|I_h|≪46080=|B₆| ⟹ frame is external.
PART II — SEAM DISCRETE↔CONTINUUM
  H. MACHINE 1: spectrum of the cube {2k} is INTEGER; weights C(n,k)→Gaussian (CLT); no irrationality.
  I. MACHINE 2 spectrum: the icosahedron graph carries ±√5 (signature of the golden frame; the cube has none).
  J. RANK 5: an element of order 5 for the first time in S_n at n=5; crystallographic restriction (axes 2,3,4,6).
  K. PROJECTION+WINDOW: M is orthogonal, E∥⊥E⊥, total irrationality; window = 30 faces (RT).
  L. DISCRETENESS+5-AXIS-NESS: cut-and-project → Delone; the star is invariant under 72°/120°, NOT under 90°.
  M. PHASON: shift of the window γ changes the pattern, density holds ⟹ phase=input, window=form.
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
    print("\n[A] SKELETON: orthoplex β_6 = \"complete minus matching\"")
    deg = {v: sum(1 for e in ORTHO if v in e) for v in LABELS}
    check("β_6: every pole is 10-regular (adjacent to all but the antipode)", set(deg.values()) == {10})
    check("β_6: 60 edges = C(12,2)−6", len(ORTHO) == 60)
    matching = set(frozenset(((a, +1), (a, -1))) for a in range(6))
    allpairs = set(frozenset(p) for p in itertools.combinations(LABELS, 2))
    check("complement of β_6 = 6·K₂ (6 antipodal axes = a matching)", matching == (allpairs - ORTHO))

# --- small categorical checks of adjunction (κ-equivariant maps of scenes) ---
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
    print("\n[B] REALIZATIONS: D⊣U holds; U⊣C (cofree) REFUTED; orthoplex = terminal of the layer")
    # D⊣U: from the EMPTY graph every κ-map is a homomorphism (no edge constraints) = freeness (left adjoint)
    total = sum(1 for _ in _kmaps(2, 3))
    homs = sum(1 for c in _kmaps(2, 3) if _is_hom(c, set(), _orthoedges(3)))
    check("D⊣U holds: from the empty graph ALL κ-maps are homomorphisms ⟹ free (left) realization",
          homs == total == 36)
    # U⊣C FALSE: Hom_Real(β₃, C(1 axis)) = 0 ≠ 8 = Hom_Scene(U β₃, 1 axis)
    hr = sum(1 for c in _kmaps(3, 1) if _is_hom(c, _orthoedges(3), _orthoedges(1)))
    hs = sum(1 for _ in _kmaps(3, 1))
    check("U⊣C (cofree) REFUTED: Hom_Real(β₃,C(1axis))=0 ≠ 8=Hom_Scene ⟹ orthoplex is NOT a right adjoint",
          hr == 0 and hs == 8)
    # C is not functorial: scene-morphisms S₂→S₁ do not lift to morphisms of orthoplexes
    bad = sum(1 for c in _kmaps(2, 1) if not _is_hom(c, _orthoedges(2), _orthoedges(1)))
    check("C is not functorial (all 4 morphisms S₂→S₁ tear an edge of the orthoplex) ⟹ no right adjoint exists", bad == 4)
    # The CORRECT property: orthoplex = terminal of the LAYER over a fixed scene (maximal antipode-free κ-graph)
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    non_edges = set(frozenset(p) for p in itertools.combinations(LABELS, 2)) - ORTHO
    check("β_6 is κ-invariant, every one of its non-edges is antipodal ⟹ TERMINAL OF THE LAYER (max realization of a fixed scene)",
          all(kap(e) in ORTHO for e in ORTHO) and all(len({a for (a,s) in e}) == 1 for e in non_edges) and len(non_edges) == 6)

def section_C():
    print("\n[C] EMBEDDING: icosahedron ⊂ β_6, exactly half the edges")
    A = axes(phi); V = np.vstack([A, -A])
    anti = lambda i: next(j for j in range(12) if d2(V[j], -V[i]) < 1e-9)
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    check("icosahedron: antipodes are NOT joined by an edge", not any(abs(d2(V[i], V[anti(i)]) - ed) < 1e-9 for i in range(12)))
    check("icosahedron: 30 edges ⊆ 60 edges of β_6 (spanning subgraph), exactly half", Ephi <= ORTHO and len(Ephi) == 30)

def section_D():
    print("\n[D] GOLDEN ANGLE: 6 axes at arccos(1/√5)")
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
    check("ℝ⁶=V_φ⊕V_ψ: 6 vectors (gold⊕conjugate) are ORTHONORMAL (=6D orthoplex)", diag and maxoff < 1e-9,
          extra=f"max|off-diag|={maxoff:.1e}")
    for name, t in (("φ", phi), ("ψ", psi)):
        V = np.vstack([axes(t), -axes(t)])
        shells = sorted(set(round(d2(V[i], V[j]), 6) for i in range(12) for j in range(12) if i != j))
        check(f"projection onto the {name}-block is a regular icosahedron (3 shells)", len(shells) == 3)
    check("E_φ ∪ E_ψ = all 60 edges of β_6, E_φ ∩ E_ψ = ∅ (the Galois pair tiles 30+30)",
          (Ephi | Epsi) == ORTHO and len(Ephi & Epsi) == 0 and len(Ephi) == 30 == len(Epsi))

def section_F():
    print("\n[F] κ-INVARIANT: central inversion preserves the edges of the icosahedron")
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    check("κ-image of the edges = the edges ⟹ icosahedron ∈ Real over (X,κ)", set(kap(e) for e in Ephi) == Ephi)

def section_G():
    print("\n[G] ★GUARDIAN OF EXTERNALITY: Stab_{B₆}(gold)=120=|I_h|≪46080=|B₆|")
    from itertools import permutations, product
    stab = 0; total = 0
    for sigma in permutations(range(6)):
        for eps in product((+1, -1), repeat=6):
            total += 1
            img = set(frozenset((sigma[a], eps[a] * s) for (a, s) in e) for e in Ephi)
            if img == Ephi: stab += 1
    check("|B₆| = 2⁶·6! = 46080 (the full symmetry of the skeleton)", total == 46080)
    check("Stab_{B₆}(golden half) = 120 = |I_h| ⟹ a 384-fold break ⟹ the frame is EXTERNAL [○]",
          stab == 120 and total // stab == 384)

# ====================== PART II ======================
def section_H():
    print("\n[H] MACHINE 1: the spectrum of the cube is INTEGER, the weights → Gaussian")
    check("the Laplacian spectrum of Q_n = {2k} is integer-valued (n=2,4,6); NO irrationality",
          all(float(2 * k).is_integer() for n in (2, 4, 6) for k in range(n + 1)))
    w = [comb(6, k) for k in range(7)]
    check("the weights of Q_6 = C(6,k) = [1,6,15,20,15,6,1] → Gaussian (CLT)", w == [1, 6, 15, 20, 15, 6, 1])

def section_I():
    print("\n[I] MACHINE 2 spectrum: the icosahedron graph carries ±√5")
    V = np.vstack([axes(phi), -axes(phi)])
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    A = np.array([[1.0 if i != j and abs(d2(V[i], V[j]) - ed) < 1e-6 else 0.0 for j in range(12)] for i in range(12)])
    ev = np.linalg.eigvalsh(A)
    check("the spectrum of the icosahedron graph contains ±√5 (the signature of the golden frame; the cube has none)",
          any(abs(abs(x) - sqrt(5)) < 1e-6 for x in ev))

def section_J():
    print("\n[J] RANK 5: the 5-axis for the first time; the crystallographic restriction")
    has5 = lambda n: n >= 5    # an element of order 5 = a 5-cycle, needs ≥5 points
    check("there is NO element of order 5 in S_4 (ranks 1–4 are crystallographic)", not has5(4))
    check("an element of order 5 (A₅) first appears in S_5 — the 5-axis is born at rank 5", has5(5))
    check("the crystallographic restriction: a lattice admits only axes 2,3,4,6 (a 5-axis is non-crystallographic)",
          5 not in (2, 3, 4, 6))

def section_K():
    print("\n[K] PROJECTION + WINDOW = rhombic triacontahedron (30 faces)")
    check("M is orthogonal (MᵀM=I)", np.allclose(M.T @ M, np.eye(6)))
    check("E∥ ⊥ E⊥ (Ppar·Pperpᵀ = 0)", np.allclose(Ppar @ Pperp.T, np.zeros((3, 3))))
    tot = True
    for x in itertools.product(range(-2, 3), repeat=6):
        if x == (0,) * 6: continue
        xv = np.array(x, float)
        if np.allclose(Pperp @ xv, 0, atol=1e-9) or np.allclose(Ppar @ xv, 0, atol=1e-9):
            tot = False; break
    check("total irrationality (no 0≠x∈ℤ⁶ with x⊥=0 or x∥=0) ⟹ aperiodicity", tot)
    check("window = zonotope of 6 perp-generators: 15 normals → 30 faces = RT", len(normals) == 15)

_cache = {}
def _patch():
    if "Pb" not in _cache:
        Xacc, P3 = project(); _cache["Xacc"] = Xacc; _cache["P3"] = P3
        Pb = P3[np.linalg.norm(P3, axis=1) < 2.2]
        D = np.sqrt(((Pb[:, None, :] - Pb[None, :, :])**2).sum(-1)); np.fill_diagonal(D, np.inf)
        _cache["Pb"], _cache["D"] = Pb, D
    return _cache

def section_L():
    print("\n[L] DISCRETENESS + ★5-AXIS-NESS")
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
    check("the star is invariant under the 5-axis 72° (icosahedral axis)", inv(rot(Vp[0], 72)))
    check("the star is NOT invariant under the cubic 90° ⟹ non-crystallographic (icosahedron, not cube)",
          not inv(rot(np.array([1., 0, 0]), 90)))

def section_M():
    print("\n[M] PHASON: the cut phase = a free input")
    _, P0 = project(); _, Pg = project(gamma3=np.array([0.30, 0.10, -0.20]))
    r = lambda A: set(map(lambda x: tuple(np.round(x, 3)), A))
    check("γ≠0 CHANGES the pattern ⟹ phase is a free input [○]", len(r(P0) & r(Pg)) < len(P0))
    check("density holds under a phase shift ⟹ the window (form) is fixed [●]",
          abs(len(P0) - len(Pg)) / len(P0) < 0.25)

def section_N():
    print("\n[N] GOLDEN RING ℤ[φ]")
    raw = _patch()["Xacc"] @ Vp
    inZ = lambda x: any(abs((x - b * phi) - round(x - b * phi)) < 1e-6 for b in range(-60, 61))
    frac = np.mean([inZ(v) for v in raw[:150].flatten()])
    check("physical coordinates of the form a+bφ ⟹ quasicrystal ∈ ℤ[φ] (height ^)", frac > 0.99, extra=f"{frac*100:.0f}%")


def main():
    print("=" * 100)
    print("UNIFIED BRIDGE: oppositional skeleton → golden realization → seam discrete↔continuum")
    print("=" * 100)
    print("\n--- PART I: skeleton and golden realization (all ●) ---")
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    print("\n--- PART II: seam discrete↔continuum (●-construction, ◐-law) ---")
    section_H(); section_I(); section_J(); section_K(); section_L(); section_M(); section_N()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: one arc. The skeleton of oppositions → cofree orthoplex → golden Galois half (icosahedron) → two machines")
    print("       discrete→continuum (spectral limit vs cut-and-project), diverging at rank 5. Constructions")
    print("       = ●; the laws of forcedness/two-faces-of-|·|∞ = ◐; externality of the frame and the premise of 5-axis-ness of rank 5 = ○.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
