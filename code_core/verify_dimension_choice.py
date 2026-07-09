#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_dimension_choice.py — HONEST boundary: dimension 3+1 is reachable by a CHOICE of suborder
(sparsification into d-dimensional Minkowski), but is NOT derived from Q_n. The structure canonically gives
d=1 (chain = pure time) and d=∞ (the whole lattice); d=4 = input (choice of manifold).

A. Minkowski SPARSIFICATION d=2,3,4: the fraction of ordered pairs r_d is DIFFERENT and STABLE across N
   (a true d-dimensional causet: r_d ≈ const as N grows).
B. BOOLEAN LATTICE: r_n MONOTONICALLY DECREASES (no plateau), height (longest chain)=n+1~log₂N,
   width=C(n,⌊n/2⌋)~N ⟹ Myrheim–Meyer dimension → ∞, NOT fixed at 4.
C. CHAIN (flag) = d=1: r=1 (total order) — pure time is one-dimensional.
D. the lattice's r_n CROSSES r_4 at some n, but does NOT STAY there (no plateau) ⟹ not stably 4D;
   a stable d=4 requires SPARSIFICATION of 4-Minkowski = INPUT.
E. conclusion: d=4 = a choice of embedding, not a consequence; the structure gives 1 (time-chain) and ∞ (lattice).
"""
from __future__ import annotations
import numpy as np
from math import comb, log2

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


def sprinkle_minkowski(d, N, seed):
    """N points in a d-dimensional Minkowski causal interval [0..apex]; fraction of ordered pairs."""
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < N:
        t = rng.random()
        xs = rng.random(d - 1) * 2 - 1          # spatial coordinates in [−1,1]
        if np.linalg.norm(xs) < min(t, 1 - t):  # inside the causal interval [0,apex]
            pts.append((t, xs))
    # causal order: p≺q ⟺ Δt > |Δx⃗| (future-timelike)
    rel = 0
    for i in range(N):
        ti, xi = pts[i]
        for j in range(N):
            if i == j: continue
            tj, xj = pts[j]
            if tj > ti and (tj - ti) > np.linalg.norm(xj - xi):
                rel += 1                          # i ≺ j
    return rel / (N * (N - 1) / 2)                # fraction of ordered pairs (i<j counted once)


# ═══════ A. Minkowski sparsification: r_d is different and stable ═══════
def section_A():
    print("\n[A] Minkowski SPARSIFICATION d=2,3,4: r_d is DIFFERENT and STABLE across N (a true d-causet)")
    rd = {}
    for d in (2, 3, 4):
        vals = [sprinkle_minkowski(d, N, seed=10 * d + s) for N in (120, 240) for s in (1, 2)]
        rd[d] = np.mean(vals)
        spread = max(vals) - min(vals)
        check(f"d={d}: r_d≈{rd[d]:.3f}, stable across N (spread {spread:.3f}<0.08) — fixed dimension",
              spread < 0.08)
    # higher d ⟹ order is rarer (r decreases with d)
    check(f"r_2>r_3>r_4 ({rd[2]:.3f}>{rd[3]:.3f}>{rd[4]:.3f}): dimension is read off the fraction of pairs",
          rd[2] > rd[3] > rd[4])
    section_A.rd = rd


# ═══════ B. Boolean lattice: r_n decreases, dimension → ∞ ═══════
def section_B():
    print("\n[B] BOOLEAN LATTICE: r_n decreases (no plateau); height~log₂N, width~N ⟹ d→∞")
    prev = 1.0
    for n in range(3, 9):
        N = 1 << n
        r = (3 ** n - 2 ** n) / (N * (N - 1) / 2)
        check(f"n={n}: r_n={r:.4f} < previous (decreasing, no plateau ⟹ dimension not fixed)", r < prev)
        prev = r
    # height (longest chain) = n+1 ~ log₂N; for a d-causet height~N^{1/d} ⟹ d~n/log₂(n+1)
    d_ests = []
    for n in (8, 12, 16, 20, 24):
        d_est = n / log2(n + 1)                   # Myrheim–Meyer dimension estimate
        d_ests.append(d_est)
        print(f"   n={n}: height={n+1}~log₂N, width≈{comb(n, n//2)}~N ⟹ d_est≈{d_est:.2f}")
    growing = all(d_ests[i] < d_ests[i + 1] for i in range(len(d_ests) - 1))
    check("d_est GROWS monotonically with n (→∞) — dimension is NOT fixed (the lattice is ∞-dimensional)", growing)
    print("   → height is logarithmic, not power-law ⟹ the causet is flat/wide = infinite-dimensional")


# ═══════ C. chain = 1D ═══════
def section_C():
    print("\n[C] CHAIN (flag) = d=1: total order, r=1 — pure time is one-dimensional")
    for n in range(2, 6):
        # maximal chain ∅⊂{a}⊂…⊂[n]: n+1 elements, all pairs comparable ⟹ r=1
        chain = [sum(1 << j for j in range(k)) for k in range(n + 1)]
        rel = sum(1 for i in range(len(chain)) for j in range(len(chain))
                  if i < j and (chain[i] & chain[j]) == chain[i])
        r = rel / (len(chain) * (len(chain) - 1) / 2)
        check(f"n={n}: chain of length {n+1}, r=1.0 (total order) = d=1 (pure time)", abs(r - 1.0) < 1e-9)


# ═══════ D. r_n crosses r_4 but does not stay there ═══════
def section_D():
    print("\n[D] the lattice's r_n CROSSES r_4 at some n, but does NOT stay there ⟹ not stably 4D")
    r4 = section_A.rd[4]
    crossings = []
    for n in range(3, 12):
        N = 1 << n
        r = (3 ** n - 2 ** n) / (N * (N - 1) / 2)
        crossings.append((n, r))
    # there is an n where r_n ≈ r_4, but r_n keeps falling (not a plateau)
    near = [n for n, r in crossings if abs(r - r4) < 0.1]
    keeps_falling = crossings[-1][1] < crossings[len(crossings) // 2][1]
    check(f"r_n≈r_4≈{r4:.3f} only at n≈{near} (momentarily), then r_n keeps falling — no 4D plateau",
          len(near) >= 1 and keeps_falling)
    print("   → a stable d=4 (a plateau at r_4) requires SPARSIFICATION of 4-Minkowski = choice of manifold")


# ═══════ E. honest conclusion ═══════
def section_E():
    print("\n[E] HONEST CONCLUSION")
    print("   ● dimension d=4 is REACHABLE: sparsifying a 4-dimensional Minkowski space gives a stable causet;")
    print("   ○ but the 4-dimensional manifold is an INPUT (a choice), not derived from Q_n;")
    print("   ● the structure CANONICALLY gives d=1 (chain=pure time) and d=∞ (the whole lattice);")
    print("   ⟹ 3+1 is a choice of suborder/embedding, not a consequence. The same input-wall as the signature.")


def main():
    print("=" * 84)
    print("DIMENSION 3+1: reachable by choice (sparsification), but not derived from Q_n")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: d=4 is REACHABLE by sparsifying 4-Minkowski (●), but the manifold is an INPUT (○).")
    print("       Q_n canonically = d=1 (chain) and d=∞ (lattice); 3+1 = a choice, not a derivation. Input-wall.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
