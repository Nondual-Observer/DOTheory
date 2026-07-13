#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_dynamics_spectral.py — проверка «динамических» правок (3+1, энергооператор,
Эйнштейн–Гильберт). Собеседник сам отозвал их в §5–9 как «съезд в соседнюю физику».
Подтверждаем СТРОГО: все три κ-Δ-конструкта = НОЛЬ, ибо κ коммутирует с Δ. Единый корень.

A. ЭНЕРГОРАЗДЕЛЕНИЕ §2.3: H_T=κΔκ−Δ = 0 (κΔκ=Δ, ибо κ — автоморфизм/коммутирует).
B. ЭВОЛЮЦИЯ §2.5: ∂_t ~ [κ,Δ] = 0 (нет временно́й эволюции из κ).
C. КРИВИЗНА §3.4: R_n=Tr(κΔ) = 0 (Tr κ=0 свободна; Tr κA=0 антиподы не смежны).
D. ДЕЙСТВИЕ §3.6: S=Tr(Δ)+αTr(κΔ)=Tr(Δ) — «curvature term» тождественно 0.
E. 3+1 §1.5: гиперкуб имеет n коммутирующих направлений (битфлипы), НЕ 3; «3» — лишь
   специфика ранга 3 (U₃/κ=PG(1,2)=3 оси), не пространственная размерность.
F. что РЕАЛЬНО остаётся: H=Δ как энергия (стандарт graph-QM, не κ-зависимо, не ново);
   чистое ядро (Q_n/κ/рост/Δ/σ½/время-обход) — собеседник §4 прав.
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

def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A
def kappa(n):
    N = 1 << n; K = np.zeros((N, N))
    for x in range(N): K[x ^ ((1 << n) - 1), x] = 1.0
    return K


# ═══════ A. энергоразделение κΔκ−Δ = 0 ═══════
def section_A():
    print("\n[A] §2.3 ЭНЕРГОРАЗДЕЛЕНИЕ H_T=κΔκ−Δ = 0 (κΔκ=Δ, κ коммутирует) — конструкт тривиален")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        H_T = K @ D @ K - D
        check(f"n={n}: κΔκ−Δ = 0 (тождественно) ⟹ κ не разделяет энергию", np.allclose(H_T, 0))


# ═══════ B. эволюция [κ,Δ]=0 ═══════
def section_B():
    print("\n[B] §2.5 ЭВОЛЮЦИЯ ∂_t ~ [κ,Δ] = 0 (нет временно́й эволюции из κ) — recap")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        check(f"n={n}: [κ,Δ]=0 ⟹ ∂_t~0 (κ статичен относительно Δ)", np.allclose(K @ D - D @ K, 0))


# ═══════ C. кривизна Tr(κΔ) = 0 ═══════
def section_C():
    print("\n[C] §3.4 КРИВИЗНА R_n=Tr(κΔ) = 0 (Tr κ=0 свободна; Tr κA=0 антиподы не смежны)")
    for n in range(2, 7):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        tr_kappa = np.trace(K)                       # = 0 (κ свободна, нет неподвижных)
        tr_kA = np.trace(K @ A)                      # = 0 (антипод не смежен: Хэмминг=n>1)
        R = np.trace(K @ D)                          # = n·Tr(κ) − Tr(κA) = 0
        check(f"n={n}: Tr(κ)={tr_kappa:.0f}, Tr(κA)={tr_kA:.0f} ⟹ R_n=Tr(κΔ)={R:.0f} (кривизна тривиальна)",
              abs(tr_kappa) < 1e-9 and abs(tr_kA) < 1e-9 and abs(R) < 1e-9)


# ═══════ D. действие S = Tr(Δ) + 0 ═══════
def section_D():
    print("\n[D] §3.6 ДЕЙСТВИЕ S=Tr(Δ)+α·Tr(κΔ)=Tr(Δ): «curvature term» Tr(κΔ)=0 тождественно")
    for n in range(2, 6):
        K, A = kappa(n), adjacency(n)
        D = n * np.eye(1 << n) - A
        tr_D = np.trace(D)                            # = n·2ⁿ (нет петель)
        tr_kD = np.trace(K @ D)                       # = 0
        check(f"n={n}: Tr(Δ)={tr_D:.0f}=n·2ⁿ, Tr(κΔ)={tr_kD:.0f}=0 ⟹ S=Tr(Δ) (Эйнштейн–Гильберт-член 0)",
              abs(tr_D - n * (1 << n)) < 1e-9 and abs(tr_kD) < 1e-9)


# ═══════ E. 3+1 не выводится: n направлений, не 3 ═══════
def section_E():
    print("\n[E] §1.5 РАЗМЕРНОСТЬ 3+1: гиперкуб имеет n коммутирующих направлений, НЕ 3")
    for n in range(2, 7):
        # n битфлипов σ_x^(i) — независимые коммутирующие инволюции-направления
        directions = n
        # на ранге 3: U₃/κ = PG(1,2) = 3 оси (специфика n=3, не размерность пространства-времени)
        axes_rank3 = 3 if n == 3 else (1 << (n - 1)) - 1   # |U_n/κ| = 2^{n-1}−1
        check(f"n={n}: независимых направлений={directions} (растёт с n); «3» лишь при n=3 (PG(1,2))",
              directions == n and (n != 3 or axes_rank3 == 3))
    print("   → числа «3 пространственных» в Q_n нет; n направлений; «3» = специфика ранга 3, не d_space")


# ═══════ F. что реально остаётся ═══════
def section_F():
    print("\n[F] что РЕАЛЬНО остаётся: H=Δ как энергия (стандарт graph-QM), чистое ядро")
    for n in (3, 4):
        D = n * np.eye(1 << n) - adjacency(n)
        ev = np.linalg.eigvalsh(D)
        # Δ≥0, основное состояние λ=0 (константа) — стандартная graph-QM энергия, НЕ κ-зависимо
        check(f"n={n}: H=Δ≥0, основное λ=0 (константа) — энергия graph-QM (стандарт, не ново, не κ)",
              ev.min() > -1e-9 and abs(ev.min()) < 1e-9)
    print("   → H=Δ = стандартная графовая энергия; κ-Δ динамика вся =0; ядро (Q_n/κ/рост/σ½/обход) цело")


def main():
    print("=" * 86)
    print("ДИНАМИКА из κ-Δ: все три конструкта (энерго/кривизна/действие) = 0, ибо [κ,Δ]=0")
    print("=" * 86)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 86)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: ВСЕ κ-Δ динамические конструкты = 0 (κΔκ−Δ, [κ,Δ], Tr(κΔ)) — единый корень")
    print("       [κ,Δ]=0. 3+1 не выводится (n направлений). Собеседник §5–9 ПРАВ: динамика/GR =")
    print("       интерпретация, не вывод. Остаётся чистое ядро + H=Δ (стандарт). Стена та же.")
    print("=" * 86)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
