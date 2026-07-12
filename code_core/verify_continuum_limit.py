#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_continuum_limit.py — an HONEST check of the proposal "continuity = spectral
limit of Q_n", rather than passing a scheme off as a construction.

Proposal: Q_n → Laplacian Δ_n → spectrum → scaling limit → (M,g) → σ½=KMS-fixed point.
Method is correct (spectral geometry is a real discrete→continuum mechanism; κ→Hodge star
is ALREADY proven for us). Question: what does the limit give ON THE HYPERCUBE — a manifold or a measure?

WE CHECK:
A. scalar Laplacian of the hypercube L=D−A=nI−A; spectrum {2k, multiplicity C(n,k)} (over ℝ, canonical).
B. heat trace Z(t)=Tr e^{−tL}=(1+e^{−2t})ⁿ — exact formula.
C. SPECTRAL DIMENSION d_s(t)=−2 dlnZ/dlnt NOT constant (no plateau) ⟹ limit is NOT
   a d-manifold: the hypercube is spectrally non-geometric in the (M,g) sense.
D. distribution of eigenvalues → GAUSSIAN (CLT) ⟹ limit = MEASURE (our reverse-side weight),
   not a metric. This is consistent with the corpus (continuous side = measure), but does not give (M,g).
E. honest conclusion: κ→Hodge is real [◐]; limit=measure [●]; (M,g)/dimension/signature=INPUT [○].

⚠ Over 𝔽₂ ∂²=0, but there is NO SPECTRUM; over ℝ the scalar L=D−A is canonical (no signs needed), but the full
   Hodge complex over ℝ requires ORIENTATIONS (signs) — extra structure (a soft input).
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
    print("\n[A] hypercube Laplacian L=nI−A: spectrum {2k, multiplicity C(n,k)} (canonical over ℝ)")
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
    print("\n[B] heat trace Z(t)=Tr e^{−tL} = (1+e^{−2t})ⁿ (exactly)")
    for n in (3, 5, 7):
        for t in (0.05, 0.2, 0.5, 1.0):
            Z_direct = sum(comb(n, k) * exp(-2 * t * k) for k in range(n + 1))
            Z_formula = (1 + exp(-2 * t)) ** n
            check(f"n={n}, t={t}: Z(t)=(1+e^{{−2t}})ⁿ", abs(Z_direct - Z_formula) < 1e-9)


# ═══════ C. spectral dimension NOT constant (no manifold) ═══════
def section_C():
    print("\n[C] spectral dimension d_s(t)=−2 dlnZ/dlnt — NO PLATEAU ⟹ limit is NOT a d-manifold")
    # d_s(t) = 4 n t e^{−2t} / (1+e^{−2t})   (analytically from Z=(1+e^{−2t})ⁿ)
    def d_s(n, t):
        return 4 * n * t * exp(-2 * t) / (1 + exp(-2 * t))
    for n in (10, 20, 50):
        # for a d-manifold d_s(t)≈const on a window of small t; for the hypercube — it changes severalfold
        window = [0.005, 0.01, 0.02, 0.05, 0.1]
        vals = [d_s(n, t) for t in window]
        ratio = max(vals) / max(min(vals), 1e-9)
        check(f"n={n}: d_s(t) changes {ratio:.0f}× over a window of small t (no plateau ⟹ not a manifold)",
              ratio > 5)
        # as t→0 d_s→0 (point-like/measure-like), not a fixed dimension
        check(f"n={n}: d_s(t→0)→0 (limit measure-like, not d-dimensional): d_s(0.001)={d_s(n,0.001):.3f}",
              d_s(n, 0.001) < 0.5)


# ═══════ D. eigenvalue distribution → Gaussian (limit = MEASURE) ═══════
def section_D():
    print("\n[D] spectrum distribution → GAUSSIAN (CLT) ⟹ limit = MEASURE (reverse-side weight), not a metric")
    # eigenvalues 2k, k~Binomial(n,1/2); (k−n/2)/√(n/4) → N(0,1)
    def ks_to_normal(n):
        # empirical CDF of normalized levels vs standard normal
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
        check(f"n={n}: KS-distance of spectrum to N(0,1) = {D:.4f} (↓ ⟹ limit=Gaussian measure)",
              D < prev)
        prev = D
    print("   → scaling limit of the spectrum = Gaussian measure on ℝ¹ (= weight/reverse-side of the corpus), NOT (M,g)")


# ═══════ E. honest summary ═══════
def section_E():
    print("\n[E] HONEST SUMMARY on the proposal")
    print("   ● method is correct: continuity as a SPECTRAL LIMIT (not identification) — better;")
    print("   ● κ→Hodge star is ALREADY proven discretely (one operator: κ∂=δκ);")
    print("   ● on the hypercube the limit = GAUSSIAN MEASURE (reverse-side weight), spectral dimension unstable;")
    print("   ○ (M,g): Riemannian metric/dimension are NOT derived — need a different discretization (triangulation")
    print("     of a manifold) or a measure/scale = INPUT; on the bare Q_n they are absent;")
    print("   ○ Lorentzian (+,−,−,−): κ-spectrum is SYMMETRIC (±λ), signature is not derived; Wick=input;")
    print("   ○ convergence to (M,g) and the link to GR dynamics — not proven (the proposal's author admits it).")
    print("   ⟹ the proposal gives the WALL a spectral form (limit=measure=reverse-side), does NOT break it.")


def main():
    print("=" * 84)
    print("EVALUATION OF THE PROPOSAL 'continuity = spectral limit of Q_n' — what it REALLY gives")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: method is correct (spectral limit), κ=Hodge is already ours; BUT the hypercube limit = GAUSSIAN")
    print("       MEASURE (reverse-side), NOT (M,g). Metric/dimension/signature = INPUT [○]. Same wall,")
    print("       now spectral: the proposal gives it a form, does not break it.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
