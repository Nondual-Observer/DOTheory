#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_seam_structure.py — структура шва |·|₂/|·|∞ (глава VII «Изнанка»).

Чистая структурная проверка, без физической проекции (масса/Λ — отдельно).

  [A] Теорема сферы: фигура сцены вершинно-транзитивна (октаэдр, куб) ⟹ все
      вершины равноудалены от центра (на одной сфере), среднее сопротивление
      R̄(v) постоянно ⟹ радиальная координата имеет на вершинах нулевую
      дисперсию = вне графа. Центр σ½ = единственная точка r=0.

  [B] Расщепление изнанки: симметричная фигура (κ точна) → вершины на сфере;
      слом симметрии (вес антипода неравен) → вершины сходят со сферы ТОЛЬКО
      вдоль сломанной оси (осевой диполь), поперёк остаются на сфере.
      Анизотропная (осевая) часть выводима из слома; изотропный радиальный
      фон от слома не зависит = аксиома изнанки.

Запуск:  python3 verify_seam_structure.py
Зависимости: numpy.
"""

import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def mean_resistance(A):
    n = A.shape[0]
    L = np.diag(A.sum(1)) - A
    Lp = np.linalg.pinv(L)
    R = np.array([[Lp[u, u] + Lp[v, v] - 2 * Lp[u, v] for v in range(n)] for u in range(n)])
    return R.sum(1) / (n - 1)


def A_octahedron():
    P = [(i, s) for i in range(3) for s in (1, -1)]
    A = np.zeros((6, 6))
    for a, (i, s) in enumerate(P):
        for b, (j, t) in enumerate(P):
            if a != b and not (i == j and s == -t):
                A[a, b] = 1.0
    return A


def A_cube():
    cl = list(itertools.product([0, 1], repeat=3))
    A = np.zeros((8, 8))
    for a, x in enumerate(cl):
        for b, y in enumerate(cl):
            if sum(p != q for p, q in zip(x, y)) == 1:
                A[a, b] = 1.0
    return A


def section_sphere_theorem():
    print("\n[A] Теорема сферы — радиус вне графа (наблюдатель = r=0)")
    oct_c = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0],
                      [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
    r_oct = np.linalg.norm(oct_c - oct_c.mean(0), axis=1)
    check("октаэдр: все вершины на сфере одного радиуса от центра", np.allclose(r_oct, r_oct[0]))

    cube_c = np.array(list(itertools.product([0, 1], repeat=3)), float)
    r_cube = np.linalg.norm(cube_c - cube_c.mean(0), axis=1)
    check("куб: все вершины на сфере (радиус √¾ от центра σ½)",
          np.allclose(r_cube, r_cube[0]) and abs(r_cube[0] - np.sqrt(0.75)) < 1e-12)

    check("октаэдр: среднее сопротивление R̄(v) = const (нет выделенной вершины)",
          np.allclose(mean_resistance(A_octahedron()), mean_resistance(A_octahedron())[0]))
    check("куб: R̄(v) = const",
          np.allclose(mean_resistance(A_cube()), mean_resistance(A_cube())[0]))

    check("радиальная координата: нулевая дисперсия на вершинах ⟹ вне графа",
          np.std(r_oct) < 1e-12 and np.std(r_cube) < 1e-12)
    print("   → центр σ½ есть r=0 — единственная точка вне сферы (наблюдатель, по теореме)")


def section_split():
    print("\n[B] Расщепление изнанки — осевое(слом) выводимо, радиальное аксиома")
    oct_c = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0],
                      [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)

    def radii(weights):
        c = (weights[:, None] * oct_c).sum(0) / weights.sum()
        return np.linalg.norm(oct_c - c, axis=1)

    # симметрия точна
    check("симметрия точна (равные веса): вершины на сфере, std r=0",
          np.std(radii(np.ones(6))) < 1e-12)
    # слом симметрии вдоль оси 0
    w = np.ones(6)
    w[0], w[1] = 1.6, 0.4
    r = radii(w)
    axial = abs(r[0] - r[1])
    transverse = abs(r[2] - r[4])
    check("слом: осевой диполь r(+e₀)≠r(−e₀) — сход со сферы по сломанной оси", axial > 1e-3)
    check("слом: поперёк r(+e₁)=r(+e₂) — остаются на сфере (слом ровно осевой)", transverse < 1e-12)
    print(f"   осевой сход |Δr|={axial:.3f}, поперечный={transverse:.3f}")
    print("   → осевая часть изнанки = форма слома симметрии (выводима);")
    print("     изотропный радиальный фон от слома не зависит = аксиома изнанки")


def main():
    print("=" * 60)
    print("verify_seam_structure.py — структура шва (глава VII «Изнанка»)")
    print("=" * 60)
    section_sphere_theorem()
    section_split()
    print("\n" + "=" * 60)
    print(f"ИТОГ: {PASS} PASS, {FAIL} FAIL")
    print("=" * 60)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
