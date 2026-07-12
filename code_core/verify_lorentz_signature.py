#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_lorentz_signature.py — HONEST check of the proposal on the emergence of the Lorentzian
signature from κ-noncentrality. The DECISIVE question: the proposal requires [κ,Δ]≠0
("time emergence condition"). Does OUR κ commute with the Laplacian?

A. Laplacian Δ ≥ 0 always (Riemannian by default) — yes.
B. ★DECISIVE: our κ (complement) is a GRAPH AUTOMORPHISM of the hypercube and the HODGE STAR ⟹
   [κ,Δ]=0. The proposal's condition [κ,Δ]≠0 is NOT satisfied for our κ.
C. conflict of the proposal's conditions: κ is NONcentral in ⟨∂,δ⟩ (κ∂≠∂κ) — this we have; BUT
   the proposal additionally needs [κ,Δ]≠0 — and we have [κ,Δ]=0. The two conditions are incompatible for κ.
D. the proposal's construct H=Δ−λK², K=κ∂−∂κ: we compute the signature — does it give "1+3"?
E. conclusion: the mechanism requires an operator NOT commuting with Δ; our κ commutes ⟹
   Euclidean, not Lorentz. Signature/time = INPUT (a different operator), not from our structure.
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

def popcount(x): return bin(x).count("1")

def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A

def kappa_perm(n):
    N = 1 << n; K = np.zeros((N, N))
    for x in range(N): K[x ^ ((1 << n) - 1), x] = 1.0
    return K

def boundary_signed(n):
    """signed simplicial boundary over ℝ: ∂S=Σ(−1)^j (S minus the j-th element). ∂²=0 over ℝ."""
    N = 1 << n; B = np.zeros((N, N))
    for S in range(N):
        elems = [i for i in range(n) if (S >> i) & 1]
        for j, i in enumerate(elems):
            B[S ^ (1 << i), S] += (-1) ** j
    return B


# ═══════ A. Laplacian ≥ 0 (Riemannian default) ═══════
def section_A():
    print("\n[A] Laplacian Δ ≥ 0 always ⟹ Riemannian by default (as the proposal states)")
    for n in range(2, 7):
        Dg = n * np.eye(1 << n) - adjacency(n)               # graph Laplacian
        ev = np.linalg.eigvalsh(Dg)
        check(f"n={n}: spec(Δ_graph) ≥ 0 (min={ev.min():.3f}) — positive semidefinite", ev.min() > -1e-9)
    for n in range(2, 6):
        B = boundary_signed(n); D = B @ B.T + B.T @ B        # Hodge Laplacian over ℝ
        ev = np.linalg.eigvalsh(D)
        check(f"n={n}: spec(Δ_Hodge=∂δ+δ∂) ≥ 0 (min={ev.min():.3f})", ev.min() > -1e-9)


# ═══════ B. DECISIVE: [κ,Δ]=0 for our κ ═══════
def section_B():
    print("\n[B] ★DECISIVE: our κ COMMUTES with Δ ([κ,Δ]=0) — the proposal's condition is NOT satisfied")
    for n in range(2, 7):
        A = adjacency(n); K = kappa_perm(n); Dg = n * np.eye(1 << n) - A
        # κ — graph automorphism of the hypercube: κAκ⁻¹=A (complement preserves Hamming adjacency)
        autom = np.allclose(K @ A @ K, A)
        commute = np.allclose(K @ Dg - Dg @ K, 0)
        check(f"n={n}: κ — graph automorphism (κAκ=A) ⟹ [κ,Δ_graph]=0", autom and commute)
    for n in range(2, 6):
        B = boundary_signed(n); K = kappa_perm(n); D = B @ B.T + B.T @ B
        commute = np.allclose(K @ D - D @ K, 0)
        check(f"n={n}: κ=Hodge star ⟹ [κ,Δ_Hodge]=0 (Hodge star commutes with the Laplacian)",
              commute)
    print("   → the proposal requires [κ,Δ]≠0 (\"time emergence\"); our κ gives [κ,Δ]=0 ⟹ the mechanism does NOT trigger")


# ═══════ C. the proposal's two conditions are incompatible for our κ ═══════
def section_C():
    print("\n[C] κ NONcentral in ⟨∂,δ⟩ (κ∂≠∂κ), BUT [κ,Δ]=0 — the proposal's two conditions are incompatible")
    for n in range(2, 6):
        B = boundary_signed(n); K = kappa_perm(n)
        Bt = B.T
        non_central = not np.allclose(K @ B, B @ K)          # κ∂≠∂κ (κ swaps ∂↔δ)
        commute_lap = np.allclose(K @ (B @ Bt + Bt @ B), (B @ Bt + Bt @ B) @ K)
        # the proposal needs: NONcentral AND [κ,Δ]≠0. We have: NONcentral AND [κ,Δ]=0.
        check(f"n={n}: κ∂≠∂κ (noncentral) ✓ BUT [κ,Δ]=0 — the [κ,Δ]≠0 the proposal needs is ABSENT",
              non_central and commute_lap)
    print("   → \"noncentrality in the algebra\" ≠ \"[κ,Δ]≠0\"; the proposal conflates them")


# ═══════ D. construct H=Δ−λK² — does it give "1+3"? ═══════
def section_D():
    print("\n[D] the proposal's construct H=Δ−λK², K=κ∂−∂κ: compute the signature (number of neg. modes)")
    n = 4
    B = boundary_signed(n); K = kappa_perm(n)
    Bt = B.T
    D = B @ Bt + Bt @ B
    Kop = K @ B - B @ K                                       # K=κ∂−∂κ
    for lam in (0.0, 0.5, 1.0, 2.0):
        H = D - lam * (Kop @ Kop)
        ev = np.linalg.eigvalsh((H + H.T) / 2)
        neg = int(np.sum(ev < -1e-9))
        pos = int(np.sum(ev > 1e-9))
        zero = int(np.sum(np.abs(ev) <= 1e-9))
        print(f"   λ={lam}: neg.modes={neg}, zero={zero}, pos.={pos}  (Lorentz would want 1 neg.)")
    # conclusion: the number of negative modes is NOT 1 (no pure (−,+,+,+)); depends on λ arbitrarily
    H1 = D - 1.0 * (Kop @ Kop)
    ev1 = np.sort(np.linalg.eigvalsh((H1 + H1.T) / 2))
    neg1 = int(np.sum(ev1 < -1e-9))
    check(f"H=Δ−K² at λ=1: number of neg. modes = {neg1} ≠ 1 ⟹ NOT pure Lorentzian (−,+,+,+)",
          neg1 != 1)
    print("   → H is indefinite only trivially (we subtracted λ·positive); no structural \"1+3\"")


# ═══════ E. honest conclusion ═══════
def section_E():
    print("\n[E] HONEST CONCLUSION on the proposal about the Lorentzian signature")
    print("   ● true: Δ≥0 (Riemannian default); Lorentz needs an operator breaking positivity;")
    print("   ★ BUT our κ COMMUTES with Δ (graph automorphism / Hodge star) ⟹ [κ,Δ]=0;")
    print("   ● the proposal requires [κ,Δ]≠0 — NOT satisfied for our κ ⟹ the mechanism gives Euclidean;")
    print("   ○ Lorentz would require a DIFFERENT operator, not commuting with Δ — it is ABSENT from the structure;")
    print("   ○ κ-spectrum is SYMMETRIC (±λ, proven) — gives ±, not (−,+,+,+); the signature is not derivable;")
    print("   ⟹ signature/time = INPUT (external operator), not from (Q_n,∂,κ). The same wall.")


def main():
    print("=" * 84)
    print("LORENTZIAN SIGNATURE from κ? The decisive point: does our κ commute with the Laplacian")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the proposal requires [κ,Δ]≠0; our κ (complement=graph automorphism=Hodge star)")
    print("       COMMUTES with Δ ⟹ the mechanism does NOT trigger, geometry Euclidean. Lorentz =")
    print("       external operator = INPUT. Time does not emerge from our κ. The same wall.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
