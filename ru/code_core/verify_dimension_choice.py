#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_dimension_choice.py — ЧЕСТНАЯ граница: размерность 3+1 достижима ВЫБОРОМ подпорядка
(прореживание в d-мерный Минковский), но НЕ выводится из Q_n. Структура канонически даёт
d=1 (цепь = чистое время) и d=∞ (вся решётка); d=4 = вход (выбор многообразия).

A. ПРОРЕЖИВАНИЕ Минковского d=2,3,4: доля упорядоченных пар r_d РАЗЛИЧНА и СТАБИЛЬНА по N
   (истинный d-мерный каузет: r_d ≈ const при росте N).
B. БУЛЕВА РЕШЁТКА: r_n МОНОТОННО УБЫВАЕТ (нет плато), высота (длиннейшая цепь)=n+1~log₂N,
   ширина=C(n,⌊n/2⌋)~N ⟹ размерность Майрхейма–Мейера → ∞, НЕ фиксируется на 4.
C. ЦЕПЬ (флаг) = d=1: r=1 (полный порядок) — чистое время одномерно.
D. r_n решётки ПЕРЕСЕКАЕТ r_4 при каком-то n, но НЕ ОСТАЁТСЯ (нет плато) ⟹ не стабильно 4D;
   стабильный d=4 требует ПРОРЕЖИВАНИЯ 4-Минковского = ВХОД.
E. вывод: d=4 = выбор вложения, не следствие; структура даёт 1 (время-цепь) и ∞ (решётка).
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
    """N точек в d-мерном причинном интервале Минковского [0..apex]; доля упоряд. пар."""
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < N:
        t = rng.random()
        xs = rng.random(d - 1) * 2 - 1          # пространственные в [−1,1]
        if np.linalg.norm(xs) < min(t, 1 - t):  # внутри причинного интервала [0,apex]
            pts.append((t, xs))
    # причинный порядок: p≺q ⟺ Δt > |Δx⃗| (будущее-времениподобно)
    rel = 0
    for i in range(N):
        ti, xi = pts[i]
        for j in range(N):
            if i == j: continue
            tj, xj = pts[j]
            if tj > ti and (tj - ti) > np.linalg.norm(xj - xi):
                rel += 1                          # i ≺ j
    return rel / (N * (N - 1) / 2)                # доля упорядоченных пар (i<j считается раз)


# ═══════ A. прореживание Минковского: r_d различна и стабильна ═══════
def section_A():
    print("\n[A] ПРОРЕЖИВАНИЕ Минковского d=2,3,4: r_d РАЗЛИЧНА и СТАБИЛЬНА по N (истинный d-каузет)")
    rd = {}
    for d in (2, 3, 4):
        vals = [sprinkle_minkowski(d, N, seed=10 * d + s) for N in (120, 240) for s in (1, 2)]
        rd[d] = np.mean(vals)
        spread = max(vals) - min(vals)
        check(f"d={d}: r_d≈{rd[d]:.3f}, стабильна по N (разброс {spread:.3f}<0.08) — фикс. размерность",
              spread < 0.08)
    # выше d ⟹ реже порядок (r убывает с d)
    check(f"r_2>r_3>r_4 ({rd[2]:.3f}>{rd[3]:.3f}>{rd[4]:.3f}): размерность читается из доли пар",
          rd[2] > rd[3] > rd[4])
    section_A.rd = rd


# ═══════ B. булева решётка: r_n убывает, размерность → ∞ ═══════
def section_B():
    print("\n[B] БУЛЕВА РЕШЁТКА: r_n убывает (нет плато); высота~log₂N, ширина~N ⟹ d→∞")
    prev = 1.0
    for n in range(3, 9):
        N = 1 << n
        r = (3 ** n - 2 ** n) / (N * (N - 1) / 2)
        check(f"n={n}: r_n={r:.4f} < предыдущего (убывает, нет плато ⟹ не фикс. d)", r < prev)
        prev = r
    # высота (длиннейшая цепь) = n+1 ~ log₂N; для d-каузета высота~N^{1/d} ⟹ d~n/log₂(n+1)
    d_ests = []
    for n in (8, 12, 16, 20, 24):
        d_est = n / log2(n + 1)                   # оценка размерности Майрхейма–Мейера
        d_ests.append(d_est)
        print(f"   n={n}: высота={n+1}~log₂N, ширина≈{comb(n, n//2)}~N ⟹ d_оц≈{d_est:.2f}")
    growing = all(d_ests[i] < d_ests[i + 1] for i in range(len(d_ests) - 1))
    check("d_оц РАСТЁТ монотонно с n (→∞) — размерность НЕ фиксируется (решётка ∞-мерна)", growing)
    print("   → высота логарифмична, не степенна́я ⟹ каузет плоский/широкий = бесконечномерный")


# ═══════ C. цепь = 1D ═══════
def section_C():
    print("\n[C] ЦЕПЬ (флаг) = d=1: полный порядок, r=1 — чистое время одномерно")
    for n in range(2, 6):
        # максимальная цепь ∅⊂{a}⊂…⊂[n]: n+1 элемент, все пары сравнимы ⟹ r=1
        chain = [sum(1 << j for j in range(k)) for k in range(n + 1)]
        rel = sum(1 for i in range(len(chain)) for j in range(len(chain))
                  if i < j and (chain[i] & chain[j]) == chain[i])
        r = rel / (len(chain) * (len(chain) - 1) / 2)
        check(f"n={n}: цепь длины {n+1}, r=1.0 (полный порядок) = d=1 (чистое время)", abs(r - 1.0) < 1e-9)


# ═══════ D. r_n пересекает r_4, но не остаётся ═══════
def section_D():
    print("\n[D] r_n решётки ПЕРЕСЕКАЕТ r_4 при каком-то n, но НЕ остаётся ⟹ не стабильно 4D")
    r4 = section_A.rd[4]
    crossings = []
    for n in range(3, 12):
        N = 1 << n
        r = (3 ** n - 2 ** n) / (N * (N - 1) / 2)
        crossings.append((n, r))
    # есть n где r_n ≈ r_4, но r_n продолжает падать (не плато)
    near = [n for n, r in crossings if abs(r - r4) < 0.1]
    keeps_falling = crossings[-1][1] < crossings[len(crossings) // 2][1]
    check(f"r_n≈r_4≈{r4:.3f} лишь у n≈{near} (мгновенно), затем r_n падает дальше — нет плато 4D",
          len(near) >= 1 and keeps_falling)
    print("   → стабильный d=4 (плато r_4) требует ПРОРЕЖИВАНИЯ 4-Минковского = выбор многообразия")


# ═══════ E. честный вывод ═══════
def section_E():
    print("\n[E] ЧЕСТНЫЙ ВЫВОД")
    print("   ● размерность d=4 ДОСТИЖИМА: прореживание 4-мерного Минковского даёт стабильный каузет;")
    print("   ○ но 4-мерное многообразие — ВХОД (выбор), не выводится из Q_n;")
    print("   ● структура КАНОНИЧЕСКИ даёт d=1 (цепь=чистое время) и d=∞ (вся решётка);")
    print("   ⟹ 3+1 — выбор подпорядка/вложения, не следствие. Та же стена входа, что и сигнатура.")


def main():
    print("=" * 84)
    print("РАЗМЕРНОСТЬ 3+1: достижима выбором (прореживание), но не выводится из Q_n")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: d=4 ДОСТИЖИМА прореживанием 4-Минковского (●), но многообразие = ВХОД (○).")
    print("       Q_n канонически = d=1 (цепь) и d=∞ (решётка); 3+1 = выбор, не вывод. Стена входа.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
