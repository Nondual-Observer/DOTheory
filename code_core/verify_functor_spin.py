#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_spin.py — EXPLICIT FUNCTOR F: 𝒟(cube Q_n, lift Λ, κ) → 𝒫(spin system).
Answer to the reviewer's objection "there is no morphism between levels": we build ONE explicit
functor and check it ON SEVERAL OPERATIONS (lift, κ, composition), not at a single point of agreement.

SOURCE 𝒟 (our combinatorics):
  objects   — hypercubes Q_n = graph on 𝔽₂ⁿ (vertices=bitstrings, edges=Hamming-1);
  morphisms — lift Λ: Q_n ↪ Q_{n+1}=Q_n □ K₂ (add an axis); κ: x↦x+1ⁿ (complement).

TARGET 𝒫 (physics):
  objects   — n spins-½, Hamiltonian A_n=∑σ_x^(i) (transverse field / hopping on the cube);
  morphisms — add a spin; global flip X=∏σ_x.

FUNCTOR F: Q_n ↦ (ℂ²)^⊗n with A_n=∑σ_x; Λ ↦ ⊗(add a spin); κ ↦ X=σ_x^⊗n.
KEY: A(Q_n) (the hypercube adjacency matrix) is IDENTICALLY EQUAL to ∑σ_x^(i) — this is not a
coincidence of value but an equality of OPERATORS, from which the WHOLE structure transfers
(spectrum, multiplicities, κ-symmetry, lift). We check functoriality: F(Λ∘Λ)=F(Λ)∘F(Λ), F(κ²)=id, etc.

HONEST BOUNDARY (answer to "a bridge at a single point"): the image of the functor = FREE spins (∑σ_x).
Mass/interaction/curvature require WEIGHTS on the edges (an input, as so(4) from 1/r) — the bare
Q_n has none of these. The functor is reliable up to the free system; beyond that lies an open
front [○].
"""
from __future__ import annotations
import numpy as np
from math import comb

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], float)
SZ = np.array([[1, 0], [0, -1]], float)

def kron_list(mats):
    out = np.array([[1.0]])
    for m in mats:
        out = np.kron(out, m)
    return out

def single(op, i, n):
    """operator op on spin i out of n (the rest — identity)."""
    return kron_list([op if j == i else I2 for j in range(n)])

def A_cube(n):
    """hypercube adjacency matrix Q_n = ∑ σ_x^(i) (bit-flip i = a Hamming edge)."""
    return sum(single(SX, i, n) for i in range(n))

def hypercube_adjacency_combinatorial(n):
    """A(Q_n) built PURELY combinatorially (from 𝔽₂ⁿ), independent of spins — for cross-check."""
    N = 1 << n
    A = np.zeros((N, N))
    for x in range(N):
        for i in range(n):
            A[x, x ^ (1 << i)] = 1.0
    return A


# ───────────────────────── A. spectral correspondence ─────────────────────────
def section_A():
    print("\n[A] spectrum of cube Q_n = spectrum of free spins ∑σ_x: {n−2k, multiplicity C(n,k)}")
    for n in range(1, 7):
        A = A_cube(n)
        Acomb = hypercube_adjacency_combinatorial(n)
        # (1) the spin operator is IDENTICALLY EQUAL to the combinatorial cube adjacency matrix
        same_operator = np.allclose(A, Acomb)
        # (2) spectrum = {n−2k} with multiplicities C(n,k) — the WHOLE structure, not one number
        ev = np.round(np.linalg.eigvalsh(A)).astype(int)
        from collections import Counter
        got = Counter(ev.tolist())
        want = Counter({n - 2 * k: comb(n, k) for k in range(n + 1)})
        check(f"n={n}: A(Q_n) ≡ ∑σ_x (equality of OPERATORS) and spectrum={{n−2k, C(n,k)}}",
              same_operator and got == want,
              extra=f"got={dict(got)} want={dict(want)}")


# ───────────────────────── B. functoriality of the lift ─────────────────────────
def section_B():
    print("\n[B] lift Λ: Q_n→Q_{n+1}=Q_n□K₂  ↦  add a spin (A_{n+1}=A_n⊗I+I⊗σ_x)")
    for n in range(1, 6):
        An = A_cube(n)
        An1_direct = A_cube(n + 1)
        An1_lift = np.kron(An, I2) + np.kron(np.eye(1 << n), SX)
        check(f"n={n}→{n+1}: F(Λ) = add a spin (equality of operators)",
              np.allclose(An1_direct, An1_lift))
        # spectrum lifts λ → λ±1 (each eigenvalue splits)
        sp_n = np.round(np.linalg.eigvalsh(An)).astype(int)
        sp_n1 = sorted(np.round(np.linalg.eigvalsh(An1_direct)).astype(int).tolist())
        want = sorted([v + s for v in sp_n for s in (+1, -1)])
        check(f"n={n}→{n+1}: spectrum lifts λ↦λ±1 (structure, not a point)", sp_n1 == want)

def section_B_composition():
    print("\n[B′] COMPOSITION of the functor: F(Λ∘Λ) = F(Λ)∘F(Λ) (two lifts = two spins)")
    for n in range(1, 5):
        An = A_cube(n)
        # two lifts in a row
        step1 = np.kron(An, I2) + np.kron(np.eye(1 << n), SX)
        step2 = np.kron(step1, I2) + np.kron(np.eye(1 << (n + 1)), SX)
        direct = A_cube(n + 2)
        check(f"n={n}: F(Λ²)=F(Λ)∘F(Λ) — functoriality of composition", np.allclose(step2, direct))


# ───────────────────────── C. κ-complement = global flip ─────────────────────────
def section_C():
    print("\n[C] κ: x↦x+1ⁿ (complement)  ↦  X=σ_x^⊗n (global flip);  κ²=id, [A,κ]=0")
    for n in range(1, 6):
        A = A_cube(n)
        X = kron_list([SX] * n)
        # κ realizes the antipode x↦x+1ⁿ: check the basis permutation
        N = 1 << n
        perm_ok = all(abs(X[(x ^ (N - 1)), x] - 1.0) < 1e-12 for x in range(N))
        check(f"n={n}: F(κ)=X realizes the antipode x↦x+1ⁿ", perm_ok)
        check(f"n={n}: F(κ²)=F(id)=I (involution)", np.allclose(X @ X, np.eye(N)))
        check(f"n={n}: [A,κ]=0 — the complement commutes (preserves levels)",
              np.allclose(A @ X, X @ A))


# ───────────────────────── D. chiral κ = particle/hole ─────────────────────────
def section_D():
    print("\n[D] chiral involution Z=σ_z^⊗n (weight parity): {A,Z}=0 ⟹ spectrum λ↔−λ")
    for n in range(1, 6):
        A = A_cube(n)
        Z = kron_list([SZ] * n)
        anti = np.allclose(A @ Z + Z @ A, 0)
        ev = sorted(np.round(np.linalg.eigvalsh(A)).astype(int).tolist())
        symm = ev == sorted([-v for v in ev])
        check(f"n={n}: {{A,Z}}=0 (bipartiteness=particle/hole) ⟹ spectrum ±λ", anti and symm)


# ───────────────────────── E. σ½ as the spectral center ─────────────────────────
def section_E():
    print("\n[E] σ½ = the middle stratum k=n/2: max. degeneracy C(n,n/2), massless center")
    for n in (2, 4, 6):
        A = A_cube(n)
        ev = np.round(np.linalg.eigvalsh(A)).astype(int)
        from collections import Counter
        c = Counter(ev.tolist())
        mid_deg = c[0]                     # eigenvalue 0 = the middle k=n/2
        check(f"n={n}: the middle λ=0 has MAX multiplicity C(n,n/2)={comb(n, n//2)}",
              mid_deg == comb(n, n // 2) and mid_deg == max(c.values()))
    print("   → the spectral center (λ=0, k=n/2) = σ½ = κ-fix of the middle layer = massless middle")


# ───────────────────────── F. honest boundary of the functor ─────────────────────────
def section_F():
    print("\n[F] BOUNDARY: bare Q_n → FREE spins; mass requires a WEIGHT (input), not from the cube")
    n = 4
    A = A_cube(n)
    ev = np.round(np.linalg.eigvalsh(A)).astype(int)
    # the bare cube is vertex-transitive ⟹ the middle is degenerate ⟹ NO mass gap
    gap_bare = sorted(set(ev.tolist()))
    has_zero = 0 in gap_bare
    check("bare Q_n: the middle λ=0 is present (massless, no gap) — a free system",
          has_zero)
    # INTRODUCE a weight imbalance on one axis (κ-break, doc 88): the gap opens, but weight g is an INPUT
    g = 0.7
    A_weighted = sum((1.0 if i > 0 else 1.0 + g) * single(SX, i, n) for i in range(n))
    ev_w = np.linalg.eigvalsh(A_weighted)
    # check that the imbalance SHIFTS the structure (weight — a free parameter, not from Q_n)
    moved = not np.allclose(sorted(ev.tolist()), sorted(np.round(ev_w).astype(int).tolist()))
    check("WEIGHTED cube (κ-break, weight g=INPUT): the structure shifts — mass requires an input",
          moved)
    print("   → the functor is RELIABLE up to free spins (∑σ_x); mass/interaction/curvature")
    print("     = weights on edges = INPUT (as so(4) from 1/r) ⟹ the bridge is built AT ONE POINT [○]")


def main():
    print("=" * 74)
    print("EXPLICIT FUNCTOR F: 𝒟(Q_n, Λ, κ) → 𝒫(spin system ∑σ_x)")
    print("checking functoriality on OPERATIONS (lift/κ/composition), not at a point")
    print("=" * 74)
    section_A(); section_B(); section_B_composition()
    section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 74)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the morphism EXISTS explicitly (Q_n ↦ free spins), functorial on 4 operations;")
    print("       BUT the image = a free system; rich physics = weights-as-input = an open front [○].")
    print("=" * 74)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
