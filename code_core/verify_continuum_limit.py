#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_continuum_limit.py — an HONEST check of the proposal "continuity = the spectral
limit of Q_n," rather than passing off a scheme as a construction.

Proposal: Q_n → Laplacian Δ_n → spectrum → scale limit → (M,g) → σ½=KMS fixed point.
The method is sound (spectral geometry is a real discrete→continuum mechanism; κ→Hodge star
has ALREADY been proved on our side). Question: what does the limit give ON THE HYPERCUBE
— a manifold or a measure?

WE CHECK:
A. the scalar hypercube Laplacian L=D−A=nI−A; spectrum {2k, multiplicity C(n,k)} (over ℝ, canonical).
B. the heat trace Z(t)=Tr e^{−tL}=(1+e^{−2t})ⁿ — an exact formula.
C. the SPECTRAL DIMENSION d_s(t)=−2 dlnZ/dlnt is NOT constant (no plateau) ⟹ the limit is NOT
   a d-manifold: the hypercube is not spectrally geometric in the sense of (M,g).
D. the eigenvalue distribution → GAUSSIAN (CLT) ⟹ the limit = a MEASURE (our underside-weight),
   not a metric. This is consistent with the corpus (the continuum side = a measure), but does not give (M,g).
E. honest conclusion: κ→Hodge is really [◐]; the limit=measure [●]; (M,g)/dimension/signature=INPUT [○].

⚠ Over 𝔽₂ ∂²=0, but there is NO SPECTRUM; over ℝ the scalar L=D−A is canonical (no signs needed),
   but the full Hodge complex over ℝ requires ORIENTATIONS (signs) — extra structure (a soft input).
"""
from __future__ import annotations
import numpy as np
from math import comb, exp, log

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


# ═══════ A. spectrum of the scalar hypercube Laplacian ═══════
def section_A():
    print("\n[A] the hypercube Laplacian L=nI−A: spectrum {2k, multiplicity C(n,k)} (canonical over ℝ)")
    from collections import Counter
    for n in range(1, 8):
        A = adjacency(n)
        L = n * np.eye(1 << n) - A
        ev = np.round(np.linalg.eigvalsh(L)).astype(int)
        got = Counter(ev.tolist())
        want = Counter({2 * k: comb(n, k) for k in range(n + 1)})
        check(f"n={n}: spec(L) = {{2k : k=0..{n}}} with multiplicities C(n,k)", got == want)


# ═══════ B. heat trace Z(t)=(1+e^{−2t})ⁿ ═══════
def section_B():
    print("\n[B] heat trace Z(t)=Tr e^{−tL} = (1+e^{−2t})ⁿ (exact)")
    for n in (3, 5, 7):
        for t in (0.05, 0.2, 0.5, 1.0):
            Z_direct = sum(comb(n, k) * exp(-2 * t * k) for k in range(n + 1))
            Z_formula = (1 + exp(-2 * t)) ** n
            check(f"n={n}, t={t}: Z(t)=(1+e^{{−2t}})ⁿ", abs(Z_direct - Z_formula) < 1e-9)


# ═══════ C. spectral dimension is NOT constant (no manifold) ═══════
def section_C():
    print("\n[C] spectral dimension d_s(t)=−2 dlnZ/dlnt — NO PLATEAU ⟹ the limit is NOT a d-manifold")
    # d_s(t) = 4 n t e^{−2t} / (1+e^{−2t})   (analytically from Z=(1+e^{−2t})ⁿ)
    def d_s(n, t):
        return 4 * n * t * exp(-2 * t) / (1 + exp(-2 * t))
    for n in (10, 20, 50):
        # for a d-manifold d_s(t)≈const on a window of small t; for the hypercube it changes by orders of magnitude
        window = [0.005, 0.01, 0.02, 0.05, 0.1]
        vals = [d_s(n, t) for t in window]
        ratio = max(vals) / max(min(vals), 1e-9)
        check(f"n={n}: d_s(t) changes by {ratio:.0f}× on the window of small t (no plateau ⟹ not a manifold)",
              ratio > 5)
        # as t→0 d_s→0 (point-like/measure-like), not a fixed dimension
        check(f"n={n}: d_s(t→0)→0 (the limit is measure-like, not d-dimensional): d_s(0.001)={d_s(n,0.001):.3f}",
              d_s(n, 0.001) < 0.5)


# ═══════ D. eigenvalue distribution → Gaussian (the limit = a MEASURE) ═══════
def section_D():
    print("\n[D] the spectrum distribution → GAUSSIAN (CLT) ⟹ the limit = a MEASURE (underside-weight), not a metric")
    # eigenvalues 2k, k~Binomial(n,1/2); (k−n/2)/√(n/4) → N(0,1)
    def ks_to_normal(n):
        # empirical CDF of the normalized levels vs the standard normal
        from math import erf, sqrt
        ks = sorted(range(n + 1))
        weights = [comb(n, k) for k in ks]
        tot = sum(weights)
        mu, sd = n / 2, sqrt(n / 4)
        cum = 0.0; D = 0.0
        for k, w in zip(ks, weights):
            cum += w / tot
            z = (k - mu) / sd
            Phi = 0.5 * (1 + erf(z / sqrt(2)))
            D = max(D, abs(cum - Phi))
        return D
    prev = 1.0
    for n in (10, 50, 200, 800):
        D = ks_to_normal(n)
        check(f"n={n}: KS distance of the spectrum to N(0,1) = {D:.4f} (↓ ⟹ the limit=a Gaussian measure)",
              D < prev)
        prev = D
    print("   → the scale limit of the spectrum = a Gaussian measure on ℝ¹ (= the corpus's weight/underside), NOT (M,g)")


# ═══════ E. honest summary ═══════
def section_E():
    print("\n[E] HONEST SUMMARY on the proposal")
    print("   ● the method is sound: continuity as a SPECTRAL LIMIT (not an identification) — better;")
    print("   ● κ→Hodge star is ALREADY proved discretely (one operator: κ∂=δκ);")
    print("   ● on the hypercube the limit = a GAUSSIAN MEASURE (underside-weight), the spectral dimension is unstable;")
    print("   ○ (M,g): the Riemannian metric/dimension are NOT derived — a different discretization is needed (a triangulation")
    print("     of a manifold) or a measure/scale = INPUT; on the bare Q_n they are absent;")
    print("   ○ Lorentzian (+,−,−,−): the κ-spectrum is SYMMETRIC (±λ), the signature is not derived; Wick=input;")
    print("   ○ convergence to (M,g) and the connection to GR dynamics — not proved (the author of the proposal admits this).")
    print("   ⟹ the proposal gives the WALL a spectral form (limit=measure=underside), it does NOT break through it.")


def main():
    print("=" * 84)
    print("EVALUATION OF THE PROPOSAL \"continuity = the spectral limit of Q_n\" — what it REALLY gives")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the method is sound (spectral limit), κ=Hodge is already ours; BUT the hypercube limit = a GAUSSIAN")
    print("       MEASURE (underside), NOT (M,g). Metric/dimension/signature = INPUT [○]. The wall is the same,")
    print("       now spectral: the proposal gives it a form, it does not break through.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
