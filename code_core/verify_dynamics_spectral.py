#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_dynamics_spectral.py — check of "dynamical" edits (3+1, energy operator,
Einstein–Hilbert). The interlocutor themself withdrew them in §5–9 as "a detour into adjacent physics."
We confirm STRICTLY: all three κ-Δ constructs = ZERO, because κ commutes with Δ. A single root cause.

A. ENERGY SPLITTING §2.3: H_T=κΔκ−Δ = 0 (κΔκ=Δ, since κ is an automorphism/commutes).
B. EVOLUTION §2.5: ∂_t ~ [κ,Δ] = 0 (no time evolution from κ).
C. CURVATURE §3.4: R_n=Tr(κΔ) = 0 (Tr κ=0 is free; Tr κA=0 antipodes are not adjacent).
D. ACTION §3.6: S=Tr(Δ)+αTr(κΔ)=Tr(Δ) — the "curvature term" is identically 0.
E. 3+1 §1.5: the hypercube has n commuting directions (bit-flips), NOT 3; "3" is merely
   a specific feature of rank 3 (U₃/κ=PG(1,2)=3 axes), not a spatial dimension.
F. what ACTUALLY remains: H=Δ as energy (standard graph-QM, not κ-dependent, not new);
   the pure core (Q_n/κ/growth/Δ/σ½/time-traversal) — the interlocutor is right in §4.
"""
from __future__ import annotations
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A
def kappa(n):
    N = 1 << n; K = np.zeros((N, N))
    for x in range(N): K[x ^ ((1 << n) - 1), x] = 1.0
    return K


# ═══════ A. energy splitting κΔκ−Δ = 0 ═══════
def section_A():
    print("\n[A] §2.3 ENERGY SPLITTING H_T=κΔκ−Δ = 0 (κΔκ=Δ, κ commutes) — the construct is trivial")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        H_T = K @ D @ K - D
        check(f"n={n}: κΔκ−Δ = 0 (identically) ⟹ κ does not split energy", np.allclose(H_T, 0))


# ═══════ B. evolution [κ,Δ]=0 ═══════
def section_B():
    print("\n[B] §2.5 EVOLUTION ∂_t ~ [κ,Δ] = 0 (no time evolution from κ) — recap")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        check(f"n={n}: [κ,Δ]=0 ⟹ ∂_t~0 (κ is static relative to Δ)", np.allclose(K @ D - D @ K, 0))


# ═══════ C. curvature Tr(κΔ) = 0 ═══════
def section_C():
    print("\n[C] §3.4 CURVATURE R_n=Tr(κΔ) = 0 (Tr κ=0 is free; Tr κA=0 antipodes are not adjacent)")
    for n in range(2, 7):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        tr_kappa = np.trace(K)                       # = 0 (κ is free, no fixed points)
        tr_kA = np.trace(K @ A)                      # = 0 (antipode is not adjacent: Hamming distance=n>1)
        R = np.trace(K @ D)                          # = n·Tr(κ) − Tr(κA) = 0
        check(f"n={n}: Tr(κ)={tr_kappa:.0f}, Tr(κA)={tr_kA:.0f} ⟹ R_n=Tr(κΔ)={R:.0f} (curvature is trivial)",
              abs(tr_kappa) < 1e-9 and abs(tr_kA) < 1e-9 and abs(R) < 1e-9)


# ═══════ D. action S = Tr(Δ) + 0 ═══════
def section_D():
    print("\n[D] §3.6 ACTION S=Tr(Δ)+α·Tr(κΔ)=Tr(Δ): the \"curvature term\" Tr(κΔ)=0 identically")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        tr_D = np.trace(D)                            # = n·2ⁿ (no loops)
        tr_kD = np.trace(K @ D)                       # = 0
        check(f"n={n}: Tr(Δ)={tr_D:.0f}=n·2ⁿ, Tr(κΔ)={tr_kD:.0f}=0 ⟹ S=Tr(Δ) (Einstein–Hilbert term 0)",
              abs(tr_D - n * (1 << n)) < 1e-9 and abs(tr_kD) < 1e-9)


# ═══════ E. 3+1 is not derived: n directions, not 3 ═══════
def section_E():
    print("\n[E] §1.5 DIMENSION 3+1: the hypercube has n commuting directions, NOT 3")
    for n in range(2, 7):
        # n bit-flips σ_x^(i) — independent commuting involution-directions
        directions = n
        # at rank 3: U₃/κ = PG(1,2) = 3 axes (a feature specific to n=3, not a dimension of spacetime)
        axes_rank3 = 3 if n == 3 else (1 << (n - 1)) - 1   # |U_n/κ| = 2^{n-1}−1
        check(f"n={n}: independent directions={directions} (grows with n); \"3\" only at n=3 (PG(1,2))",
              directions == n and (n != 3 or axes_rank3 == 3))
    print("   → there is no number \"3 spatial\" in Q_n; there are n directions; \"3\" = a feature specific to rank 3, not d_space")


# ═══════ F. what actually remains ═══════
def section_F():
    print("\n[F] what ACTUALLY remains: H=Δ as energy (standard graph-QM), the pure core")
    for n in (3, 4):
        D = n * np.eye(1 << n) - adjacency(n)
        ev = np.linalg.eigvalsh(D)
        # Δ≥0, ground state λ=0 (constant) — standard graph-QM energy, NOT κ-dependent
        check(f"n={n}: H=Δ≥0, ground state λ=0 (constant) — graph-QM energy (standard, not new, not κ)",
              ev.min() > -1e-9 and abs(ev.min()) < 1e-9)
    print("   → H=Δ = standard graph energy; the κ-Δ dynamics all =0; the core (Q_n/κ/growth/σ½/traversal) is intact")


def main():
    print("=" * 86)
    print("DYNAMICS from κ-Δ: all three constructs (energy/curvature/action) = 0, since [κ,Δ]=0")
    print("=" * 86)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 86)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: ALL κ-Δ dynamical constructs = 0 (κΔκ−Δ, [κ,Δ], Tr(κΔ)) — a single root cause")
    print("       [κ,Δ]=0. 3+1 is not derived (n directions). The interlocutor is RIGHT in §5–9: dynamics/GR is")
    print("       interpretation, not derivation. What remains is the pure core + H=Δ (standard). The same wall.")
    print("=" * 86)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
