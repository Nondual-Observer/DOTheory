#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cryptographic Spectral Block — Unified Verification Suite
=========================================================

This script is the single minimal verifier for the connected theorem-package
stored in the earlier bridge document:

  DOT_Cryptographic_Spectral_Block.md

It checks, in one place, the full chain:

  1. block-graph construction O_n + Q_n + B
  2. complete analytic spectrum
  3. CI spectral stratification
  4. weight-0 coupled sector
  5. balancedness criterion
  6. resilience criterion

The script is intentionally self-contained.

References to the proof document:

  §4  — Lemma 1, Lemma 2, Lemma 3
  §5  — Theorem A (complete spectrum)
  §7  — Theorem B (correlation immunity)
  §9  — Theorem C (balancedness)
  §10 — Theorem D (resilience)

Honest scope:

  - this verifies the theorem-package on the full block composite
      G_block^(n) = O_n ∪ Q_n ∪ B
  - this is not a verifier for any restricted subgraph obtained by deleting boundary vertices
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from itertools import product

import numpy as np


# ============================================================================
# §1. Core graph objects
# ============================================================================

def build_composite_graph(n: int):
    """
    Build the composite graph G_block^(n) = O_n ∪ Q_n ∪ B.

    Returns:
      L     : full block Laplacian
      B     : incidence matrix between poles and cube vertices
      verts : all cube vertices as tuples in {0,1}^n
      m     : number of octahedral vertices (= 2n)
      N     : number of cube vertices (= 2^n)
    """
    m = 2 * n
    N = 2 ** n
    verts = list(product([0, 1], repeat=n))

    # O_n = K_{2,...,2}: complete n-partite graph on pairs ±e_i
    A_oct = np.ones((m, m)) - np.eye(m)
    for i in range(n):
        A_oct[2 * i, 2 * i + 1] = 0
        A_oct[2 * i + 1, 2 * i] = 0

    # Q_n: standard hypercube adjacency
    A_cube = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            if sum(a != b for a, b in zip(verts[i], verts[j])) == 1:
                A_cube[i, j] = 1
                A_cube[j, i] = 1

    # B[v, s] = 1 iff the bit at the pole axis matches the pole sign
    B = np.zeros((m, N))
    for v in range(m):
        axis = v // 2
        sign = v % 2
        for s in range(N):
            if verts[s][axis] == sign:
                B[v, s] = 1

    total = m + N
    A = np.zeros((total, total))
    A[:m, :m] = A_oct
    A[m:, m:] = A_cube
    A[:m, m:] = B
    A[m:, :m] = B.T

    L = np.diag(A.sum(axis=1)) - A
    return L, B, verts, m, N


def analytic_spectrum(n: int) -> dict[float, int]:
    """
    Theorem A: exact spectrum of L_block.
    Stored as a rounded dictionary {eigenvalue: multiplicity}.
    """
    p = 2 ** (n - 1)
    T = 3 * n + p
    Delta = (n - 4 + p) ** 2 + 2 ** (n + 1)
    sqrt_delta = math.sqrt(Delta)

    spec: dict[float, int] = {}

    def add(lam: float, mult: int):
        key = round(float(lam), 8)
        spec[key] = spec.get(key, 0) + mult

    # weight-0 coupled sector
    add(0.0, 1)
    add(n + p, 1)

    # weight-1 coupled sector
    add((T - sqrt_delta) / 2, n)
    add((T + sqrt_delta) / 2, n)

    # decoupled weight-k sectors, k >= 2
    for k in range(2, n + 1):
        add(2 * k + n, math.comb(n, k))

    # pure octahedral sector
    add(2 * n + p, n - 1)
    return spec


def expected_bbt_spectrum(n: int) -> dict[float, int]:
    """
    Corollary 3.1:
      Spec(B B^T) = { n 2^(n-1) (mult 1), 2^(n-1) (mult n), 0 (mult n-1) }.
    """
    p = 2 ** (n - 1)
    return {
        round(float(0.0), 8): n - 1,
        round(float(p), 8): n,
        round(float(n * p), 8): 1,
    }


# ============================================================================
# §2. Walsh tools and Boolean-function helpers
# ============================================================================

def walsh_character(u, verts, N: int) -> np.ndarray:
    """Return χ_u on the cube vertices."""
    chi = np.zeros(N)
    for s_idx in range(N):
        dot = sum(a * b for a, b in zip(u, verts[s_idx])) % 2
        chi[s_idx] = (-1) ** dot
    return chi


def compute_walsh_spectrum(f_bits, verts, N: int) -> np.ndarray:
    """Compute the full Walsh spectrum W_f(u)."""
    W = np.zeros(N)
    for u_idx in range(N):
        total = 0
        for x_idx in range(N):
            dot = sum(a * b for a, b in zip(verts[u_idx], verts[x_idx])) % 2
            total += (-1) ** (f_bits[x_idx] ^ dot)
        W[u_idx] = total
    return W


def compute_ci(f_bits, verts, N: int, n: int) -> int:
    """
    Largest t such that W_f(u)=0 for all 1 <= wt(u) <= t.
    """
    W = compute_walsh_spectrum(f_bits, verts, N)
    ci = 0
    for t in range(1, n + 1):
        good = all(
            abs(W[u_idx]) < 0.5
            for u_idx in range(N)
            if 0 < sum(verts[u_idx]) <= t
        )
        if good:
            ci = t
        else:
            break
    return ci


def compute_resilience(f_bits, verts, N: int, n: int) -> int:
    """
    Largest t such that:
      - f is balanced
      - W_f(u)=0 for all wt(u) in [1..t]
    Returns -1 for unbalanced functions.
    """
    f_pm = np.array([2 * b - 1 for b in f_bits], dtype=float)
    balanced = abs(np.sum(f_pm)) < 1e-9
    if not balanced:
        return -1
    return compute_ci(f_bits, verts, N, n)


# ============================================================================
# §3. Spectral-sector helpers
# ============================================================================

def normalized(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def orth_projector_from_columns(cols: list[np.ndarray]) -> np.ndarray:
    Q, _ = np.linalg.qr(np.column_stack([normalized(c) for c in cols]))
    return Q @ Q.T


def projection_energy(v: np.ndarray, basis: list[np.ndarray]) -> float:
    if not basis:
        return 0.0
    P = orth_projector_from_columns(basis)
    pv = P @ v
    return float(np.dot(pv, pv))


def eigenspace_basis(evals: np.ndarray, evecs: np.ndarray, lam: float, tol=1e-8):
    idx = [i for i, ev in enumerate(evals) if abs(ev - lam) < tol]
    return [evecs[:, i] for i in idx]


def exact_rank_from_integer_rows(rows: list[list[int]]) -> int:
    """
    Exact Gaussian elimination over Q for small integer matrices.
    Used for collision-sector sanity checks at n=3,4.
    """
    if not rows:
        return 0
    mat = [[Fraction(x) for x in row] for row in rows]
    nrows = len(mat)
    ncols = len(mat[0])
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = None
        for r in range(rank, nrows):
            if mat[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        pv = mat[rank][col]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(nrows):
            if r == rank or mat[r][col] == 0:
                continue
            factor = mat[r][col]
            mat[r] = [a - factor * b for a, b in zip(mat[r], mat[rank])]
        rank += 1
        col += 1
    return rank


def weight0_lines(n: int, m: int, N: int):
    """
    §8 of the proof:
      C0^- = span((1_m, 1_N))
      C0^+ = span((2^(n-1) 1_m, -n 1_N))
    """
    p = 2 ** (n - 1)
    c0_minus = np.concatenate([np.ones(m), np.ones(N)])
    c0_plus = np.concatenate([p * np.ones(m), -n * np.ones(N)])
    return c0_minus, c0_plus


def decoupled_weight_basis(n: int, m: int, N: int, verts, k: int):
    """
    §4 / §7 / §10:
    D_k = span{ (0, χ_u) : wt(u)=k }.
    """
    basis = []
    for u in verts:
        if sum(u) == k:
            v = np.zeros(m + N)
            v[m:] = walsh_character(u, verts, N)
            basis.append(v)
    return basis


# ============================================================================
# §4. Verification logic
# ============================================================================

def verify_dimension(n: int, full_enumeration: bool) -> bool:
    print(f"\n{'═' * 74}")
    print(f"  DIMENSION n = {n}")
    print(f"{'═' * 74}")

    ok = True
    L, B, verts, m, N = build_composite_graph(n)
    evals, evecs = np.linalg.eigh(L)
    numeric_spec = {}
    for ev in evals:
        key = round(float(ev), 8)
        numeric_spec[key] = numeric_spec.get(key, 0) + 1
    exact_spec = analytic_spectrum(n)

    # [C1] Lemma 1
    c1 = True
    for u in verts:
        chi = walsh_character(u, verts, N)
        in_kernel = np.max(np.abs(B @ chi)) < 1e-10
        expected = (sum(u) >= 2)
        if in_kernel != expected:
            c1 = False
            break
    print(f"[C1] Lemma 1: ker(B) = high-weight Walsh          : {'PASS' if c1 else 'FAIL'}")
    ok &= c1

    # [C1a] Corollary 3.1
    c1a = True
    rank_B = int(np.linalg.matrix_rank(B))
    if rank_B != n + 1:
        c1a = False
    else:
        bbt = B @ B.T
        bbt_eigs = np.linalg.eigvalsh(bbt)
        num_bbt = {}
        for ev in bbt_eigs:
            key = round(float(ev), 8)
            num_bbt[key] = num_bbt.get(key, 0) + 1
        if num_bbt != expected_bbt_spectrum(n):
            c1a = False
    print(f"[C1a] Cor. 3.1: rank(B) and Spec(BB^T)          : {'PASS' if c1a else 'FAIL'}")
    ok &= c1a

    # [C2] Lemma 2
    c2 = True
    total = m + N
    for u in verts:
        wt = sum(u)
        if wt < 2:
            continue
        v = np.zeros(total)
        v[m:] = walsh_character(u, verts, N)
        if np.max(np.abs(L @ v - (2 * wt + n) * v)) > 1e-8:
            c2 = False
            break
    print(f"[C2] Lemma 2: decoupled weight-k eigenvectors    : {'PASS' if c2 else 'FAIL'}")
    ok &= c2

    # [C3] Lemma 3
    c3 = True
    for i in range(n):
        phi = np.zeros(m)
        phi[2 * i] = 1
        phi[2 * i + 1] = -1
        rhs1 = walsh_character(tuple(1 if j == i else 0 for j in range(n)), verts, N)
        lhs1 = B.T @ phi
        lhs2 = B @ rhs1
        rhs2 = (2 ** (n - 1)) * phi
        if np.max(np.abs(lhs1 - rhs1)) > 1e-10 or np.max(np.abs(lhs2 - rhs2)) > 1e-10:
            c3 = False
            break
    print(f"[C3] Lemma 3: exact axis–character coupling      : {'PASS' if c3 else 'FAIL'}")
    ok &= c3

    # [C4] Theorem A: spectrum
    c4 = (numeric_spec == exact_spec)
    print(f"[C4] Theorem A: full analytic spectrum           : {'PASS' if c4 else 'FAIL'}")
    ok &= c4

    p = 2 ** (n - 1)
    Delta = (n - 4 + p) ** 2 + 2 ** (n + 1)
    lam_w0_plus = n + p
    lam_w1_minus = (3 * n + p - math.sqrt(Delta)) / 2

    c0_minus, c0_plus = weight0_lines(n, m, N)

    # [C5] Theorem C: weight-0 lines
    c5a = np.max(np.abs(L @ c0_minus)) < 1e-10
    c5b = np.max(np.abs(L @ c0_plus - lam_w0_plus * c0_plus)) < 1e-10
    print(f"[C5] Theorem C: weight-0 coupled lines            : {'PASS' if (c5a and c5b) else 'FAIL'}")
    ok &= c5a and c5b

    # [C6] Spanning property for weight-1 coupled sector
    w1_basis = eigenspace_basis(evals, evecs, lam_w1_minus, tol=1e-6)
    cube_proj = np.column_stack([v[m:] for v in w1_basis])
    c6 = np.linalg.matrix_rank(cube_proj, tol=1e-8) == n
    print(f"[C6] Theorem B: weight-1 spanning property        : {'PASS' if c6 else 'FAIL'}")
    ok &= c6

    # [C6b] Exact collision-sector separation for n=3,4
    if n in (3, 4):
        collision_k = 2 if n == 3 else 4
        d_basis = decoupled_weight_basis(n, m, N, verts, collision_k)
        integer_rows = [list(map(int, np.rint(v))) for v in d_basis]
        integer_rows.append(list(map(int, np.rint(c0_plus))))
        exact_direct_sum = exact_rank_from_integer_rows(integer_rows) == len(d_basis) + 1
        zero_octa = all(np.all(np.rint(v[:m]).astype(int) == 0) for v in d_basis)
        nonzero_octa = np.any(np.rint(c0_plus[:m]).astype(int) != 0)
        c6b = exact_direct_sum and zero_octa and nonzero_octa
        print(f"[C6b] Collision case n={n}: exact C0^+ ⊕ D_k check  : {'PASS' if c6b else 'FAIL'}")
        ok &= c6b

    if full_enumeration:
        # Exhaustive checks for n=3,4
        c0_minus_n = normalized(c0_minus)
        c0_plus_n = normalized(c0_plus)
        d_bases = {k: decoupled_weight_basis(n, m, N, verts, k) for k in range(2, n + 1)}

        c7 = True  # CI theorem
        c8 = True  # balancedness theorem
        c9 = True  # resilience theorem
        count = 0

        for bits in product([0, 1], repeat=N):
            if sum(bits) in (0, N):
                continue
            count += 1

            f_pm = np.array([2 * b - 1 for b in bits], dtype=float)
            f_block = np.zeros(m + N)
            f_block[m:] = f_pm

            # Balancedness data
            balanced = abs(np.sum(f_pm)) < 1e-9
            proj_c0m_zero = abs(np.dot(f_block, c0_minus_n)) < 1e-10
            proj_c0p_zero = abs(np.dot(f_block, c0_plus_n)) < 1e-10
            if balanced != proj_c0m_zero or balanced != proj_c0p_zero:
                c8 = False
                break

            # CI theorem
            ci = compute_ci(bits, verts, N, n)
            for t in range(1, n + 1):
                cond = projection_energy(f_block, w1_basis) < 1e-10
                if cond and t >= 2:
                    for k in range(2, t + 1):
                        if projection_energy(f_block, d_bases[k]) >= 1e-10:
                            cond = False
                            break
                if (ci >= t) != cond:
                    c7 = False
                    break
            if not c7:
                break

            # Resilience theorem
            res = compute_resilience(bits, verts, N, n)
            for t in range(0, n + 1):
                cond = proj_c0p_zero
                if t >= 1:
                    cond = cond and (projection_energy(f_block, w1_basis) < 1e-10)
                if cond and t >= 2:
                    for k in range(2, t + 1):
                        if projection_energy(f_block, d_bases[k]) >= 1e-10:
                            cond = False
                            break
                if (res >= t) != cond:
                    c9 = False
                    break
            if not c9:
                break

        print(f"[C7] Theorem B: CI criterion exhaustive         : {'PASS' if c7 else 'FAIL'}  ({count} functions)")
        print(f"[C8] Theorem C: balancedness exhaustive         : {'PASS' if c8 else 'FAIL'}  ({count} functions)")
        print(f"[C9] Theorem D: resilience exhaustive          : {'PASS' if c9 else 'FAIL'}  ({count} functions)")
        ok &= c7 and c8 and c9
    else:
        # Structural checks for n>=5
        # weight-0 separated line
        w0_basis = eigenspace_basis(evals, evecs, lam_w0_plus, tol=1e-8)
        c7 = len(w0_basis) == 1 and projection_energy(normalized(c0_plus), w0_basis) > 1 - 1e-8
        print(f"[C7] n>=5: C0^+ = E_(n+2^(n-1))               : {'PASS' if c7 else 'FAIL'}")
        ok &= c7

        c8 = True
        for k in range(2, n + 1):
            d_basis = decoupled_weight_basis(n, m, N, verts, k)
            eig_basis = eigenspace_basis(evals, evecs, 2 * k + n, tol=1e-8)
            if len(d_basis) != len(eig_basis):
                c8 = False
                break
            Pd = orth_projector_from_columns(d_basis)
            Pe = orth_projector_from_columns(eig_basis)
            if np.max(np.abs(Pd - Pe)) > 1e-8:
                c8 = False
                break
        print(f"[C8] n>=5: D_k = E_(2k+n) for all k>=2       : {'PASS' if c8 else 'FAIL'}")
        ok &= c8

    print(f"\n{'PASS' if ok else 'FAIL'}")
    return ok


def main() -> int:
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║   CRYPTOGRAPHIC SPECTRAL BLOCK — UNIFIED VERIFICATION SUITE        ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")

    all_ok = True
    all_ok &= verify_dimension(3, full_enumeration=True)
    all_ok &= verify_dimension(4, full_enumeration=True)
    for n in range(5, 9):
        all_ok &= verify_dimension(n, full_enumeration=False)

    print(f"\n{'═' * 74}")
    if all_ok:
        print("  ██████  ALL CRYPTOGRAPHIC SPECTRAL BLOCK CHECKS PASSED.  ██████")
    else:
        print("  ██████  SOME CRYPTOGRAPHIC SPECTRAL BLOCK CHECKS FAILED. ██████")
    print(f"{'═' * 74}\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
