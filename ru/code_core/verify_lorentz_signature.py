#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_lorentz_signature.py — ЧЕСТНАЯ проверка предложения о возникновении лоренцевой
сигнатуры из κ-нецентральности. РЕШАЮЩИЙ вопрос: предложение требует [κ,Δ]≠0
(«time emergence condition»). Коммутирует ли НАШ κ с лапласианом?

A. лапласиан Δ ≥ 0 всегда (Riemannian по умолчанию) — да.
B. ★РЕШАЮЩЕЕ: наш κ (дополнение) есть ГРАФ-АВТОМОРФИЗМ гиперкуба и ЗВЕЗДА ХОДЖА ⟹
   [κ,Δ]=0. Условие предложения [κ,Δ]≠0 НЕ выполняется для нашего κ.
C. конфликт условий предложения: κ НЕцентрален в ⟨∂,δ⟩ (κ∂≠∂κ) — это у нас есть; НО
   предложению нужно вдобавок [κ,Δ]≠0 — а у нас [κ,Δ]=0. Два условия несовместны для κ.
D. конструкт предложения H=Δ−λK², K=κ∂−∂κ: считаем сигнатуру — даёт ли «1+3»?
E. вывод: механизм требует оператора, НЕ коммутирующего с Δ; наш κ коммутирует ⟹
   Euclidean, не Lorentz. Сигнатура/время = ВХОД (иной оператор), не из нашей структуры.
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

def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A

def kappa_perm(n):
    N = 1 << n; K = np.zeros((N, N))
    for x in range(N): K[x ^ ((1 << n) - 1), x] = 1.0
    return K

def boundary_signed(n):
    """знаковая симплициальная граница над ℝ: ∂S=Σ(−1)^j (S∖ j-й элемент). ∂²=0 над ℝ."""
    N = 1 << n; B = np.zeros((N, N))
    for S in range(N):
        elems = [i for i in range(n) if (S >> i) & 1]
        for j, i in enumerate(elems):
            B[S ^ (1 << i), S] += (-1) ** j
    return B


# ═══════ A. лапласиан ≥ 0 (Riemannian default) ═══════
def section_A():
    print("\n[A] лапласиан Δ ≥ 0 всегда ⟹ Riemannian по умолчанию (как и говорит предложение)")
    for n in range(2, 7):
        Dg = n * np.eye(1 << n) - adjacency(n)               # граф-лапласиан
        ev = np.linalg.eigvalsh(Dg)
        check(f"n={n}: spec(Δ_граф) ≥ 0 (min={ev.min():.3f}) — положительно полуопределён", ev.min() > -1e-9)
    for n in range(2, 6):
        B = boundary_signed(n); D = B @ B.T + B.T @ B        # Ходж-лапласиан над ℝ
        ev = np.linalg.eigvalsh(D)
        check(f"n={n}: spec(Δ_Ходж=∂δ+δ∂) ≥ 0 (min={ev.min():.3f})", ev.min() > -1e-9)


# ═══════ B. РЕШАЮЩЕЕ: [κ,Δ]=0 для нашего κ ═══════
def section_B():
    print("\n[B] ★РЕШАЮЩЕЕ: наш κ КОММУТИРУЕТ с Δ ([κ,Δ]=0) — условие предложения НЕ выполнено")
    for n in range(2, 7):
        A = adjacency(n); K = kappa_perm(n); Dg = n * np.eye(1 << n) - A
        # κ — граф-автоморфизм гиперкуба: κAκ⁻¹=A (дополнение сохраняет смежность Хэмминга)
        autom = np.allclose(K @ A @ K, A)
        commute = np.allclose(K @ Dg - Dg @ K, 0)
        check(f"n={n}: κ — граф-автоморфизм (κAκ=A) ⟹ [κ,Δ_граф]=0", autom and commute)
    for n in range(2, 6):
        B = boundary_signed(n); K = kappa_perm(n); D = B @ B.T + B.T @ B
        commute = np.allclose(K @ D - D @ K, 0)
        check(f"n={n}: κ=звезда Ходжа ⟹ [κ,Δ_Ходж]=0 (Ходж-звезда коммутирует с лапласианом)",
              commute)
    print("   → предложение требует [κ,Δ]≠0 («time emergence»); наш κ даёт [κ,Δ]=0 ⟹ механизм НЕ срабатывает")


# ═══════ C. два условия предложения несовместны для нашего κ ═══════
def section_C():
    print("\n[C] κ НЕцентрален в ⟨∂,δ⟩ (κ∂≠∂κ), НО [κ,Δ]=0 — два условия предложения несовместны")
    for n in range(2, 6):
        B = boundary_signed(n); K = kappa_perm(n)
        Bt = B.T
        non_central = not np.allclose(K @ B, B @ K)          # κ∂≠∂κ (κ меняет ∂↔δ)
        commute_lap = np.allclose(K @ (B @ Bt + Bt @ B), (B @ Bt + Bt @ B) @ K)
        # предложению нужно: НЕцентрален И [κ,Δ]≠0. У нас: НЕцентрален И [κ,Δ]=0.
        check(f"n={n}: κ∂≠∂κ (нецентрален) ✓ НО [κ,Δ]=0 — нужного предложению [κ,Δ]≠0 НЕТ",
              non_central and commute_lap)
    print("   → «нецентральность в алгебре» ≠ «[κ,Δ]≠0»; предложение их смешивает")


# ═══════ D. конструкт H=Δ−λK² — даёт ли «1+3»? ═══════
def section_D():
    print("\n[D] конструкт предложения H=Δ−λK², K=κ∂−∂κ: считаем сигнатуру (число отриц. мод)")
    n = 4
    B = boundary_signed(n); K = kappa_perm(n)
    Bt = B.T
    D = B @ Bt + Bt @ B
    Kop = K @ B - B @ K                                       # K=κ∂−∂κ
    for lam in (0.0, 0.5, 1.0, 2.0):
        H = D - lam * (Kop @ Kop)
        ev = np.linalg.eigvalsh((H + H.T) / 2)
        neg = int(np.sum(ev < -1e-9))
        pos = int(np.sum(ev > 1e-9))
        zero = int(np.sum(np.abs(ev) <= 1e-9))
        print(f"   λ={lam}: отриц.мод={neg}, нуль={zero}, полож.={pos}  (Lorentz хотел бы 1 отриц.)")
    # вывод: число отрицательных мод НЕ равно 1 (нет чистой (−,+,+,+)); зависит от λ произвольно
    H1 = D - 1.0 * (Kop @ Kop)
    ev1 = np.sort(np.linalg.eigvalsh((H1 + H1.T) / 2))
    neg1 = int(np.sum(ev1 < -1e-9))
    check(f"H=Δ−K² при λ=1: число отриц. мод = {neg1} ≠ 1 ⟹ НЕ чистая лоренцева (−,+,+,+)",
          neg1 != 1)
    print("   → H индефинитен лишь тривиально (вычли λ·положительное); структурного «1+3» нет")


# ═══════ E. честный вывод ═══════
def section_E():
    print("\n[E] ЧЕСТНЫЙ ВЫВОД по предложению о лоренцевой сигнатуре")
    print("   ● верно: Δ≥0 (Riemannian default); Lorentz нужен оператор, ломающий позитивность;")
    print("   ★ НО наш κ КОММУТИРУЕТ с Δ (граф-автоморфизм / звезда Ходжа) ⟹ [κ,Δ]=0;")
    print("   ● предложение требует [κ,Δ]≠0 — для нашего κ НЕ выполнено ⟹ механизм даёт Euclidean;")
    print("   ○ Lorentz требовал бы ДРУГОГО оператора, не коммутирующего с Δ — его в структуре НЕТ;")
    print("   ○ κ-спектр СИММЕТРИЧЕН (±λ, доказано) — даёт ±, не (−,+,+,+); сигнатура не выводится;")
    print("   ⟹ сигнатура/время = ВХОД (внешний оператор), не из (Q_n,∂,κ). Та же стена.")


def main():
    print("=" * 84)
    print("ЛОРЕНЦЕВА СИГНАТУРА из κ? Решающее: коммутирует ли наш κ с лапласианом")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: предложение требует [κ,Δ]≠0; наш κ (дополнение=граф-автоморфизм=звезда Ходжа)")
    print("       КОММУТИРУЕТ с Δ ⟹ механизм НЕ срабатывает, геометрия Euclidean. Lorentz =")
    print("       внешний оператор = ВХОД. Время из нашего κ не возникает. Стена та же.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
