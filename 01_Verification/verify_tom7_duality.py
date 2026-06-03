#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier for the Volume 7 observer-duality content (native corpus operators only).

Covers the two reframed sections of Volume 7:

  §5.3  weight  perp  orientation  (rank 3):
        - (d+delta)|U3 is the adjacency of the 6-cycle C_6
        - Sym(T) = 1/2 (d+delta)|U3 ,  [T, d+delta] = 0   (shared horizontal)
        - [T, d-delta] != 0                                (divergence on weight)
        - T = rho . kappa   (axis 3-cycle composed with complement)
        => T and sl2 form ONE structure: shared horizontal d+delta, split on weight.

  §7.5  development law (all ranks):
        - weight-multiplet branching  m_J(n+1) = m_{J-1/2}(n) + m_{J+1/2}(n)  (the lift)
        - dim<sl2>_n = sum of squares of multiplet sizes = C(n+3,3) (tetrahedral)

Everything here uses only the corpus operators d (boundary), delta (coboundary),
H (grading), kappa (complement), T (rotation). No external machinery.
"""
import numpy as np
from itertools import product, permutations
from math import comb

R = []
def check(tag, ok, msg=""):
    s = 'PASS' if ok is True else ('FAIL' if ok is False else 'INFO')
    R.append(s); print(f"[{s}] {tag}: {msg}")

# ---- rank-3 operators on the active scene U_3 (six states of weight 1,2) ----
def rank3_ops():
    X = list(product([0, 1], repeat=3)); ix = {x: i for i, x in enumerate(X)}
    U = np.zeros((8, 8)); D = np.zeros((8, 8))
    for i, x in enumerate(X):
        for k in range(3):
            if x[k] == 0:
                y = list(x); y[k] = 1; U[ix[tuple(y)], i] += 1          # delta (up)
            else:
                y = list(x); y[k] = 0; D[ix[tuple(y)], i] += 1          # d (down)
    keep = [i for i in range(8) if 0 < sum(X[i]) < 3]
    Xu = [X[i] for i in keep]; ixu = {x: i for i, x in enumerate(Xu)}
    U = U[np.ix_(keep, keep)]; D = D[np.ix_(keep, keep)]
    H = np.diag([3 - 2 * sum(x) for x in Xu])
    # complement on U_3
    K = np.zeros((6, 6))
    for i, x in enumerate(Xu): K[ixu[tuple(1 - b for b in x)], i] = 1
    # canonical hexagon walk T
    cyc = [(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1)]
    T = np.zeros((6, 6))
    for j in range(6): T[ixu[cyc[(j+1) % 6]], ixu[cyc[j]]] = 1
    def perm_op(p):
        M = np.zeros((6, 6))
        for i, x in enumerate(Xu):
            M[ixu[tuple(x[p[k]] for k in range(3))], i] = 1
        return M
    return U, D, H, T, K, perm_op

print("=" * 70)
print("Volume 7 §5.3 — weight perp orientation (rank 3)")
print("=" * 70)
U, D, H, T, K, perm_op = rank3_ops()
A = U + D            # d+delta
Rsl = D - U          # d-delta (weight direction; sign immaterial)
# (d+delta)|U3 is C_6, checked basis-invariantly: symmetric, 2-regular, connected on 6 vertices.
reach = np.linalg.matrix_power(np.eye(6) + A, 5) > 0
is_C6 = bool(np.allclose(A, A.T) and np.allclose(A.sum(0), 2) and reach.all())
check("(d+delta)|U3 = adjacency of C_6 (symmetric, 2-regular, connected)", is_C6)
check("Sym(T) = 1/2 (d+delta)|U3", np.allclose((T + T.T) / 2, A / 2))
check("[T, d+delta] = 0  (shared horizontal)", np.allclose(T @ A - A @ T, 0))
check("[T, d-delta] != 0  (divergence on weight)", not np.allclose(T @ Rsl - Rsl @ T, 0))
check("T = rho . kappa  (axis 3-cycle composed with complement)",
      any(np.allclose(perm_op(p) @ K, T) for p in permutations(range(3))))
print("  => one structure: T and sl2 share d+delta and split on the weight d-delta.")

print("=" * 70)
print("Volume 7 §7.5 — development law (all ranks)")
print("=" * 70)
def mult(n, k):  # multiplicity of the spin-(n/2-k) weight-multiplet = C(n,k)-C(n,k-1)
    return comb(n, k) - (comb(n, k - 1) if k >= 1 else 0)
branch_ok = all(
    mult(n + 1, k) == mult(n, k) + (mult(n, k - 1) if k >= 1 else 0)
    for n in range(2, 9) for k in range(0, (n + 1) // 2 + 1)
)
check("weight-multiplet branching m_J(n+1)=m_{J-1/2}(n)+m_{J+1/2}(n) (the lift)", branch_ok)
def dim_sl2(n):  # sum of squares of multiplet sizes (2J+1) over distinct J
    return sum((n - 2 * k + 1) ** 2 for k in range(0, n // 2 + 1))
tetra_ok = all(dim_sl2(n) == comb(n + 3, 3) for n in range(1, 12))
check("dim<sl2>_n = sum (multiplet size)^2 = C(n+3,3) (tetrahedral)", tetra_ok,
      f"n=3..8: {[comb(n + 3, 3) for n in range(3, 9)]}")

print("=" * 70)
print(f"SUMMARY: {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (ref: Volume 7 §5.3, §7.5)")
print("Extended bridges (Wedderburn, field, quantum information): see")
print("02_Bridges/10_Observer_Duality_Readings and _TNR_Research/00_MASTER_MAP_RU.md")
