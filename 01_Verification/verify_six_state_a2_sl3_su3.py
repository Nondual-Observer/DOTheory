#!/usr/bin/env python3
"""Verifier for the standalone six-state A2/sl3/su3 note.

This script is intentionally self-contained and uses only the Python standard library.

It checks:
1. Chevalley-Serre relations for type A2.
2. Generation of the full Lie algebra sl3(C).
3. The block action on the six-state module 3 ⊕ 3̄.
4. The standard compact anti-Hermitian basis of su(3).

Run:
    python3 verify_six_state_a2_sl3_su3.py
"""

from __future__ import annotations


Matrix = list[list[complex]]


def zero(n: int) -> Matrix:
    return [[0j for _ in range(n)] for _ in range(n)]


def e_ij(n: int, i: int, j: int) -> Matrix:
    out = zero(n)
    out[i][j] = 1
    return out


def diag(*vals: complex) -> Matrix:
    out = zero(len(vals))
    for i, v in enumerate(vals):
        out[i][i] = v
    return out


def add(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]


def scale(c: complex, a: Matrix) -> Matrix:
    n = len(a)
    return [[c * a[i][j] for j in range(n)] for i in range(n)]


def mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = zero(n)
    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue
            for j in range(n):
                out[i][j] += a[i][k] * b[k][j]
    return out


def comm(a: Matrix, b: Matrix) -> Matrix:
    return sub(mul(a, b), mul(b, a))


def transpose(a: Matrix) -> Matrix:
    n = len(a)
    return [[a[j][i] for j in range(n)] for i in range(n)]


def conj_transpose(a: Matrix) -> Matrix:
    n = len(a)
    return [[a[j][i].conjugate() for j in range(n)] for i in range(n)]


def block_diag(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    m = len(b)
    out = zero(n + m)
    for i in range(n):
        for j in range(n):
            out[i][j] = a[i][j]
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = b[i][j]
    return out


def mat_equal(a: Matrix, b: Matrix, tol: float = 1e-12) -> bool:
    n = len(a)
    for i in range(n):
        for j in range(n):
            if abs(a[i][j] - b[i][j]) > tol:
                return False
    return True


def flatten_real(a: Matrix) -> list[float]:
    out: list[float] = []
    for row in a:
        for z in row:
            out.append(float(z.real))
            out.append(float(z.imag))
    return out


def real_rank(rows: list[list[float]], tol: float = 1e-12) -> int:
    a = [row[:] for row in rows]
    m = len(a)
    n = len(a[0]) if a else 0
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = None
        for r in range(rank, m):
            if abs(a[r][col]) > tol:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        piv = a[rank][col]
        a[rank] = [x / piv for x in a[rank]]
        for r in range(m):
            if r == rank:
                continue
            factor = a[r][col]
            if abs(factor) > tol:
                a[r] = [x - factor * y for x, y in zip(a[r], a[rank])]
        rank += 1
        col += 1
    return rank


def vec_action(a: Matrix, basis_index: int) -> list[complex]:
    n = len(a)
    col = [0j] * n
    col[basis_index] = 1
    out = [0j] * n
    for i in range(n):
        for j in range(n):
            out[i] += a[i][j] * col[j]
    return out


def ad_power(x: Matrix, y: Matrix, k: int) -> Matrix:
    out = y
    for _ in range(k):
        out = comm(x, out)
    return out


def rho(x: Matrix) -> Matrix:
    return block_diag(x, scale(-1, transpose(x)))


def check_chevalley_serre() -> None:
    e1 = e_ij(3, 0, 1)
    e2 = e_ij(3, 1, 2)
    f1 = e_ij(3, 1, 0)
    f2 = e_ij(3, 2, 1)
    h1 = diag(1, -1, 0)
    h2 = diag(0, 1, -1)
    z = zero(3)
    A = ((2, -1), (-1, 2))
    es = (e1, e2)
    fs = (f1, f2)
    hs = (h1, h2)

    assert mat_equal(comm(h1, h2), z)
    for i in range(2):
        for j in range(2):
            assert mat_equal(comm(hs[i], es[j]), scale(A[i][j], es[j]))
            assert mat_equal(comm(hs[i], fs[j]), scale(-A[i][j], fs[j]))
            assert mat_equal(comm(es[i], fs[j]), hs[i] if i == j else z)
    assert mat_equal(ad_power(e1, e2, 2), z)
    assert mat_equal(ad_power(e2, e1, 2), z)
    assert mat_equal(ad_power(f1, f2, 2), z)
    assert mat_equal(ad_power(f2, f1, 2), z)


def check_generated_algebra() -> None:
    e1 = e_ij(3, 0, 1)
    e2 = e_ij(3, 1, 2)
    f1 = e_ij(3, 1, 0)
    f2 = e_ij(3, 2, 1)
    e3 = comm(e1, e2)
    f3 = comm(f2, f1)
    h1 = comm(e1, f1)
    h2 = comm(e2, f2)
    family = [e1, e2, e3, f1, f2, f3, h1, h2]
    assert real_rank([flatten_real(m) for m in family]) == 8


def check_block_module() -> None:
    labels = ["100", "010", "001", "011", "101", "110"]
    ops = {
        "e1": rho(e_ij(3, 0, 1)),
        "e2": rho(e_ij(3, 1, 2)),
        "e3": rho(e_ij(3, 0, 2)),
        "f1": rho(e_ij(3, 1, 0)),
        "f2": rho(e_ij(3, 2, 1)),
        "f3": rho(e_ij(3, 2, 0)),
    }
    expected = {
        "e1": {"010": "100", "011": "-101"},
        "e2": {"001": "010", "101": "-110"},
        "e3": {"001": "100", "011": "-110"},
        "f1": {"100": "010", "101": "-011"},
        "f2": {"010": "001", "110": "-101"},
        "f3": {"100": "001", "110": "-011"},
    }
    for name, op in ops.items():
        seen: dict[str, str] = {}
        for idx, src in enumerate(labels):
            img = vec_action(op, idx)
            nz = [(k, c) for k, c in enumerate(img) if abs(c) > 1e-12]
            if not nz:
                continue
            assert len(nz) == 1
            k, coeff = nz[0]
            sign = "-" if abs(coeff + 1) < 1e-12 else ""
            seen[src] = f"{sign}{labels[k]}"
        assert seen == expected[name], (name, seen)


def check_compact_real_form() -> None:
    h1 = diag(1, -1, 0)
    h2 = diag(0, 1, -1)
    basis = [
        scale(1j, h1),
        scale(1j, h2),
        sub(e_ij(3, 0, 1), e_ij(3, 1, 0)),
        scale(1j, add(e_ij(3, 0, 1), e_ij(3, 1, 0))),
        sub(e_ij(3, 1, 2), e_ij(3, 2, 1)),
        scale(1j, add(e_ij(3, 1, 2), e_ij(3, 2, 1))),
        sub(e_ij(3, 0, 2), e_ij(3, 2, 0)),
        scale(1j, add(e_ij(3, 0, 2), e_ij(3, 2, 0))),
    ]
    for m in basis:
        assert mat_equal(conj_transpose(m), scale(-1, m))
        assert abs(sum(m[i][i] for i in range(3))) < 1e-12
    assert real_rank([flatten_real(m) for m in basis]) == 8


def main() -> None:
    check_chevalley_serre()
    check_generated_algebra()
    check_block_module()
    check_compact_real_form()
    print("PASS: six-state A2/sl3(C)/su3 standalone checks")


if __name__ == "__main__":
    main()
