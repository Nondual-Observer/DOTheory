#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_connes_metric.py — check of the interlocutor's CONCRETE edits: (1) Connes metric on
the causet, (2) κ-split of the spectrum for a Lorentzian signature. We take what works, reject
what does not — rigorously.

A. ★WORKS: Connes/Lipschitz spectral metric on the hypercube = HAMMING distance
   (d(x,y)=sup{|f(x)−f(y)|: Lip(f)≤1}). The metric is DERIVED (not a postulate) — a real gain,
   closes "there is no metric". But it is EUCLIDEAN (positive), not Lorentzian.
B. scaling limit: Hamming/√n → Gaussian fluctuations (CLT); limit = infinite-dimensional
   Gaussian/OU, NOT flat ℝ^d of finite dimension (consistent with continuum_limit).
C. ★DOES NOT WORK (decisive): κ-split H=H₊⊕H₋ is BALANCED — dim H₊=dim H₋=2ⁿ⁻¹,
   because κ is symmetric (free involution). This is a NEUTRAL signature (k,k), NOT
   Lorentzian (1,n−1). κ cannot give ONE time and many spaces.
D. construct H=Δ−λ[κ,∂]²: number of negative modes ≠ 1 ⟹ not (1,…)-Lorentzian.
E. conclusion: Connes metric=Hamming ● (taken, Euclidean); κ-Lorentz ✗ (κ symmetric ⟹
   balanced signature); Lorentzian signature remains an INPUT.
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
def hamming(x, y): return popcount(x ^ y)


# ═══════ A. Connes/Lipschitz metric = Hamming ═══════
def section_A():
    print("\n[A] ★Connes metric on the hypercube = HAMMING distance (metric DERIVED, not a postulate)")
    for n in range(2, 6):
        N = 1 << n
        ok = True
        for x in range(N):
            # optimal f(z)=Hamming(z,x): Lipschitz with constant 1 (neighbors differ by 1)
            f = [hamming(z, x) for z in range(N)]
            lip = max(abs(f[z] - f[z ^ (1 << i)]) for z in range(N) for i in range(n))
            # attains |f(x)−f(y)| = Hamming(x,y); and this is the upper bound (path along edges)
            for y in range(N):
                achieves = abs(f[x] - f[y]) == hamming(x, y)
                if not (lip == 1 and achieves): ok = False
        check(f"n={n}: d_Connes(x,y)=sup{{|f(x)−f(y)|:Lip≤1}}=Hamming(x,y) (metric derived)", ok)
    print("   → metric = graph geodesic = Hamming; spectral, not postulated [●], but EUCLIDEAN")


# ═══════ B. scaling limit: Gaussian, not flat ℝ^d ═══════
def section_B():
    print("\n[B] scaling x↦(x−n/2)/√n: Hamming → Gaussian fluctuations (CLT); limit ∞-dim, not ℝ^d")
    # distribution of normalized weight (k−n/2)/√(n/4) → N(0,1): KS-distance decreases (CLT)
    from math import comb, erf, sqrt
    prev = 1.0
    for n in (16, 64, 256):
        mu, sd = n / 2, sqrt(n / 4)
        tot = 2.0 ** n
        cum = 0.0; ks = 0.0
        for k in range(n + 1):
            cum += comb(n, k) / tot
            z = (k - mu) / sd
            Phi = 0.5 * (1 + erf(z / sqrt(2)))
            ks = max(ks, abs(cum - Phi))
        check(f"n={n}: KS(norm.weight, N(0,1))={ks:.4f} decreases (CLT → Gaussian)", ks < prev)
        prev = ks
    print("   → limit = infinite-dimensional Gaussian (Wiener/OU), NOT flat ℝ^d of finite dimension")


# ═══════ C. ★κ-split is BALANCED, not Lorentzian ═══════
def section_C():
    print("\n[C] ★DECISIVE: κ-split H=H₊⊕H₋ is BALANCED (dim=2ⁿ⁻¹ each) — NOT Lorentzian (1,n−1)")
    for n in range(2, 7):
        N = 1 << n
        K = np.zeros((N, N))
        for x in range(N): K[x ^ (N - 1), x] = 1.0       # κ = complement
        ev = np.round(np.linalg.eigvalsh(K)).astype(int)
        dim_plus = int(np.sum(ev == 1))                   # κ=+1 (symmetric = "space")
        dim_minus = int(np.sum(ev == -1))                 # κ=−1 (antisymmetric = "time")
        check(f"n={n}: dim H₊={dim_plus}, dim H₋={dim_minus} = 2ⁿ⁻¹={1<<(n-1)} — EQUAL (signature (k,k))",
              dim_plus == dim_minus == (1 << (n - 1)))
    print("   → κ-\"time\" = 2ⁿ⁻¹ dimensions, not ONE; neutral signature (k,k), not Lorentzian (1,n−1)")


# ═══════ D. construct H=Δ−λ[κ,∂]²: not (1,…) ═══════
def section_D():
    print("\n[D] construct H=Δ−λ[κ,∂]²: number of negative modes ≠ 1 ⟹ not (1,…)-Lorentzian")
    def boundary_signed(n):
        N = 1 << n; B = np.zeros((N, N))
        for S in range(N):
            elems = [i for i in range(n) if (S >> i) & 1]
            for j, i in enumerate(elems): B[S ^ (1 << i), S] += (-1) ** j
        return B
    n = 4; N = 1 << n
    B = boundary_signed(n); Bt = B.T
    K = np.zeros((N, N))
    for x in range(N): K[x ^ (N - 1), x] = 1.0
    D = B @ Bt + Bt @ B                                    # Laplacian
    comm = K @ B - B @ K                                   # [κ,∂]
    for lam in (0.5, 1.0, 2.0):
        H = D - lam * (comm @ comm)
        ev = np.linalg.eigvalsh((H + H.T) / 2)
        neg = int(np.sum(ev < -1e-9))
        print(f"   λ={lam}: negative modes of H = {neg}  (Lorentzian would want 1)")
    H1 = D - 1.0 * (comm @ comm)
    neg1 = int(np.sum(np.linalg.eigvalsh((H1 + H1.T) / 2) < -1e-9))
    check(f"H=Δ−[κ,∂]²: negative modes = {neg1} ≠ 1 ⟹ NOT Lorentzian (1,n−1)", neg1 != 1)


# ═══════ E. honest conclusion ═══════
def section_E():
    print("\n[E] HONEST CONCLUSION on the interlocutor's edits")
    print("   ● TAKE: Connes metric = Hamming — the metric is DERIVED (closes \"there is no metric\"),")
    print("     but it is EUCLIDEAN (positive), limit = Gaussian, not Lorentzian geometry;")
    print("   ✗ REJECT κ-Lorentz: κ is symmetric (free involution) ⟹ the split is BALANCED")
    print("     (2ⁿ⁻¹+2ⁿ⁻¹), neutral signature (k,k), NOT Lorentzian (1,n−1); \"one time\" does not emerge;")
    print("   ○ Lorentzian signature requires an ASYMMETRY that κ lacks — remains an INPUT;")
    print("   ⟹ the interlocutor is right in the diagnosis (there was no metric — now there is, Hamming); but κ-Lorentz");
    print("     does not fire. The §13 gaps (smoothness, dynamics, uniqueness) the interlocutor admits himself.")


def main():
    print("=" * 86)
    print("EDITS: Connes metric (take, ●) + κ-split for Lorentz (reject, ✗)")
    print("=" * 86)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 86)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: metric DERIVED (Connes=Hamming, Euclidean) ● — a real gain; but κ-Lorentz")
    print("       ✗ (κ symmetric ⟹ balanced signature (k,k), not (1,n−1)). Lorentz=input.")
    print("=" * 86)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
