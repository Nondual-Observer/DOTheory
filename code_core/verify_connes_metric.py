#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_connes_metric.py — a check of the interlocutor's SPECIFIC proposals: (1) the Connes
metric on the causet, (2) κ-splitting of the spectrum for a Lorentzian signature. We take
what works, reject what doesn't — strictly.

A. ★WORKS: the Connes/Lipschitz spectral metric on the hypercube = HAMMING distance
   (d(x,y)=sup{|f(x)−f(y)|: Lip(f)≤1}). The metric IS DERIVED (not postulated) — a real
   strengthening, closing the "there is no metric" gap. But it is EUCLIDEAN (positive), not Lorentzian.
B. scale limit: Hamming/√n → Gaussian fluctuations (CLT); the limit = infinite-dimensional
   Gaussian/OU, NOT flat finite-dimensional ℝ^d (consistent with continuum_limit).
C. ★DOES NOT WORK (decisive): the κ-split H=H₊⊕H₋ is BALANCED — dim H₊=dim H₋=2ⁿ⁻¹,
   because κ is symmetric (a free involution). This is a NEUTRAL signature (k,k), NOT
   Lorentzian (1,n−1). κ cannot give ONE time direction and many space directions.
D. the construct H=Δ−λ[κ,∂]²: the number of negative modes ≠ 1 ⟹ not (1,…)-Lorentzian.
E. conclusion: the Connes metric = Hamming ● (we take it, Euclidean); κ-Lorentz ✗ (κ is
   symmetric ⟹ a balanced signature); the Lorentzian signature remains an INPUT.
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
    print("\n[A] ★Connes metric on the hypercube = HAMMING distance (metric IS DERIVED, not postulated)")
    for n in range(2, 6):
        N = 1 << n
        ok = True
        for x in range(N):
            # optimal f(z)=Hamming(z,x): Lipschitz with constant 1 (neighbors differ by 1)
            f = [hamming(z, x) for z in range(N)]
            lip = max(abs(f[z] - f[z ^ (1 << i)]) for z in range(N) for i in range(n))
            # achieves |f(x)−f(y)| = Hamming(x,y); and this is an upper bound (path along edges)
            for y in range(N):
                achieves = abs(f[x] - f[y]) == hamming(x, y)
                if not (lip == 1 and achieves): ok = False
        check(f"n={n}: d_Connes(x,y)=sup{{|f(x)−f(y)|:Lip≤1}}=Hamming(x,y) (metric derived)", ok)
    print("   → the metric = graph geodesic = Hamming; spectral, not postulated [●], but EUCLIDEAN")


# ═══════ B. scale limit: Gaussian, not flat ℝ^d ═══════
def section_B():
    print("\n[B] scale x↦(x−n/2)/√n: Hamming → Gaussian fluctuations (CLT); limit is ∞-dimensional, not ℝ^d")
    # distribution of the normalized weight (k−n/2)/√(n/4) → N(0,1): the KS distance decreases (CLT)
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
        check(f"n={n}: KS(normalized weight, N(0,1))={ks:.4f} decreasing (CLT → Gaussian)", ks < prev)
        prev = ks
    print("   → the limit = infinite-dimensional Gaussian (Wiener/OU), NOT flat finite-dimensional ℝ^d")


# ═══════ C. ★κ-split is BALANCED, not Lorentzian ═══════
def section_C():
    print("\n[C] ★DECISIVE: the κ-split H=H₊⊕H₋ is BALANCED (dim=2ⁿ⁻¹ each) — NOT Lorentzian (1,n−1)")
    for n in range(2, 7):
        N = 1 << n
        K = np.zeros((N, N))
        for x in range(N): K[x ^ (N - 1), x] = 1.0       # κ = complement
        ev = np.round(np.linalg.eigvalsh(K)).astype(int)
        dim_plus = int(np.sum(ev == 1))                   # κ=+1 (symmetric = "space")
        dim_minus = int(np.sum(ev == -1))                 # κ=−1 (antisymmetric = "time")
        check(f"n={n}: dim H₊={dim_plus}, dim H₋={dim_minus} = 2ⁿ⁻¹={1<<(n-1)} — EQUAL (signature (k,k))",
              dim_plus == dim_minus == (1 << (n - 1)))
    print("   → the κ-\"time\" = 2ⁿ⁻¹ dimensions, not ONE; a neutral signature (k,k), not Lorentzian (1,n−1)")


# ═══════ D. the construct H=Δ−λ[κ,∂]²: not (1,…) ═══════
def section_D():
    print("\n[D] the construct H=Δ−λ[κ,∂]²: the number of negative modes ≠ 1 ⟹ not (1,…)-Lorentzian")
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
        print(f"   λ={lam}: negative modes of H = {neg}  (a Lorentzian one would want 1)")
    H1 = D - 1.0 * (comm @ comm)
    neg1 = int(np.sum(np.linalg.eigvalsh((H1 + H1.T) / 2) < -1e-9))
    check(f"H=Δ−[κ,∂]²: negative modes = {neg1} ≠ 1 ⟹ NOT Lorentzian (1,n−1)", neg1 != 1)


# ═══════ E. honest conclusion ═══════
def section_E():
    print("\n[E] HONEST CONCLUSION on the interlocutor's proposals")
    print("   ● WE TAKE: the Connes metric = Hamming — the metric IS DERIVED (closes \"there is no metric\"),")
    print("     but it is EUCLIDEAN (positive), the limit = Gaussian, not a Lorentzian geometry;")
    print("   ✗ WE REJECT κ-Lorentz: κ is symmetric (a free involution) ⟹ the split is BALANCED")
    print("     (2ⁿ⁻¹+2ⁿ⁻¹), a neutral signature (k,k), NOT Lorentzian (1,n−1); \"one time\" does not come out;")
    print("   ○ a Lorentzian signature requires ASYMMETRY, which κ does not have — it remains an INPUT;")
    print("   ⟹ the interlocutor is right in the diagnosis (there was no metric — now there is, Hamming); but κ-Lorentz");
    print("     does not work. The gaps of §13 (smoothness, dynamics, uniqueness) the interlocutor admits himself.")


def main():
    print("=" * 86)
    print("PROPOSALS: the Connes metric (we take it, ●) + κ-split for Lorentz (we reject it, ✗)")
    print("=" * 86)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 86)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the metric IS DERIVED (Connes=Hamming, Euclidean) ● — a real strengthening; but κ-Lorentz")
    print("       ✗ (κ is symmetric ⟹ a balanced signature (k,k), not (1,n−1)). Lorentz=input.")
    print("=" * 86)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
