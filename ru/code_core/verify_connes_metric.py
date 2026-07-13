#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_connes_metric.py — проверка КОНКРЕТНЫХ правок собеседника: (1) Connes-метрика на
каузете, (2) κ-разбиение спектра для лоренцевой сигнатуры. Берём что работает, отклоняем
что нет — строго.

A. ★РАБОТАЕТ: Connes/липшицева спектральная метрика на гиперкубе = ХЭММИНГОВО расстояние
   (d(x,y)=sup{|f(x)−f(y)|: Lip(f)≤1}). Метрика ВЫВОДИТСЯ (не постулат) — реальное усиление,
   закрывает «метрики нет». Но она ЕВКЛИДОВА (положительна), не лоренцева.
B. предел масштаба: Хэмминг/√n → гауссовы флуктуации (ЦПТ); предел = бесконечномерное
   гауссово/OU, НЕ плоский ℝ^d конечной размерности (согласуется с continuum_limit).
C. ★НЕ РАБОТАЕТ (решающее): κ-разбиение H=H₊⊕H₋ СБАЛАНСИРОВАНО — dim H₊=dim H₋=2ⁿ⁻¹,
   потому что κ симметричен (свободная инволюция). Это НЕЙТРАЛЬНАЯ сигнатура (k,k), а НЕ
   лоренцева (1,n−1). κ не может дать ОДНО время и много пространства.
D. конструкт H=Δ−λ[κ,∂]²: число отрицательных мод ≠ 1 ⟹ не (1,…)-лоренцева.
E. вывод: метрика Connes=Хэмминг ● (берём, евклидова); κ-Lorentz ✗ (κ симметричен ⟹
   сбалансированная сигнатура); лоренцева сигнатура остаётся ВХОДОМ.
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
def hamming(x, y): return popcount(x ^ y)


# ═══════ A. Connes/липшицева метрика = Хэмминг ═══════
def section_A():
    print("\n[A] ★Connes-метрика на гиперкубе = ХЭММИНГОВО расстояние (метрика ВЫВОДИТСЯ, не постулат)")
    for n in range(2, 6):
        N = 1 << n
        ok = True
        for x in range(N):
            # оптимальная f(z)=Hamming(z,x): липшицева с константой 1 (соседи отличаются на 1)
            f = [hamming(z, x) for z in range(N)]
            lip = max(abs(f[z] - f[z ^ (1 << i)]) for z in range(N) for i in range(n))
            # достигает |f(x)−f(y)| = Hamming(x,y); и это верхняя граница (путь по рёбрам)
            for y in range(N):
                achieves = abs(f[x] - f[y]) == hamming(x, y)
                if not (lip == 1 and achieves): ok = False
        check(f"n={n}: d_Connes(x,y)=sup{{|f(x)−f(y)|:Lip≤1}}=Hamming(x,y) (метрика выведена)", ok)
    print("   → метрика = геодезическая графа = Хэмминг; спектральная, не постулированная [●], но ЕВКЛИДОВА")


# ═══════ B. масштабный предел: гауссово, не плоский ℝ^d ═══════
def section_B():
    print("\n[B] масштаб x↦(x−n/2)/√n: Хэмминг → гауссовы флуктуации (ЦПТ); предел ∞-мерн., не ℝ^d")
    # распределение нормированного веса (k−n/2)/√(n/4) → N(0,1): KS-расстояние убывает (ЦПТ)
    from math import comb, erf, sqrt
    prev = 1.0
    for n in (16, 64, 256):
        mu, sd = n / 2, sqrt(n / 4)
        tot = 2.0 ** n
        cum = 0.0; ks = 0.0
        for k in range(n + 1):
            cum += comb(n, k) / tot
            z = (k - mu) / sd
            Phi = 0.5 * (1 + erf(z / sqrt(2)))
            ks = max(ks, abs(cum - Phi))
        check(f"n={n}: KS(нормир.вес, N(0,1))={ks:.4f} убывает (ЦПТ → гауссово)", ks < prev)
        prev = ks
    print("   → предел = бесконечномерное гауссово (Wiener/OU), НЕ плоский ℝ^d конечной размерности")


# ═══════ C. ★κ-разбиение СБАЛАНСИРОВАНО, не лоренцево ═══════
def section_C():
    print("\n[C] ★РЕШАЮЩЕЕ: κ-разбиение H=H₊⊕H₋ СБАЛАНСИРОВАНО (dim=2ⁿ⁻¹ каждое) — НЕ лоренцево (1,n−1)")
    for n in range(2, 7):
        N = 1 << n
        K = np.zeros((N, N))
        for x in range(N): K[x ^ (N - 1), x] = 1.0       # κ = дополнение
        ev = np.round(np.linalg.eigvalsh(K)).astype(int)
        dim_plus = int(np.sum(ev == 1))                   # κ=+1 (симметричное = «пространство»)
        dim_minus = int(np.sum(ev == -1))                 # κ=−1 (антисимметричное = «время»)
        check(f"n={n}: dim H₊={dim_plus}, dim H₋={dim_minus} = 2ⁿ⁻¹={1<<(n-1)} — РАВНЫ (сигнатура (k,k))",
              dim_plus == dim_minus == (1 << (n - 1)))
    print("   → κ-«время» = 2ⁿ⁻¹ измерений, не ОДНО; нейтральная сигнатура (k,k), не лоренцева (1,n−1)")


# ═══════ D. конструкт H=Δ−λ[κ,∂]²: не (1,…) ═══════
def section_D():
    print("\n[D] конструкт H=Δ−λ[κ,∂]²: число отрицательных мод ≠ 1 ⟹ не (1,…)-лоренцева")
    def boundary_signed(n):
        N = 1 << n; B = np.zeros((N, N))
        for S in range(N):
            elems = [i for i in range(n) if (S >> i) & 1]
            for j, i in enumerate(elems): B[S ^ (1 << i), S] += (-1) ** j
        return B
    n = 4; N = 1 << n
    B = boundary_signed(n); Bt = B.T
    K = np.zeros((N, N))
    for x in range(N): K[x ^ (N - 1), x] = 1.0
    D = B @ Bt + Bt @ B                                    # лапласиан
    comm = K @ B - B @ K                                   # [κ,∂]
    for lam in (0.5, 1.0, 2.0):
        H = D - lam * (comm @ comm)
        ev = np.linalg.eigvalsh((H + H.T) / 2)
        neg = int(np.sum(ev < -1e-9))
        print(f"   λ={lam}: отрицательных мод H = {neg}  (лоренцева хотела бы 1)")
    H1 = D - 1.0 * (comm @ comm)
    neg1 = int(np.sum(np.linalg.eigvalsh((H1 + H1.T) / 2) < -1e-9))
    check(f"H=Δ−[κ,∂]²: отрицательных мод = {neg1} ≠ 1 ⟹ НЕ лоренцева (1,n−1)", neg1 != 1)


# ═══════ E. честный вывод ═══════
def section_E():
    print("\n[E] ЧЕСТНЫЙ ВЫВОД по правкам собеседника")
    print("   ● БЕРЁМ: Connes-метрика = Хэмминг — метрика ВЫВОДИТСЯ (закрывает «метрики нет»),")
    print("     но она ЕВКЛИДОВА (положительна), предел = гауссово, не лоренцева геометрия;")
    print("   ✗ ОТКЛОНЯЕМ κ-Lorentz: κ симметричен (свободная инволюция) ⟹ разбиение СБАЛАНСИРОВАНО")
    print("     (2ⁿ⁻¹+2ⁿ⁻¹), нейтральная сигнатура (k,k), НЕ лоренцева (1,n−1); «одно время» не выходит;")
    print("   ○ лоренцева сигнатура требует АСИММЕТРИИ, которой у κ нет — остаётся ВХОДОМ;")
    print("   ⟹ собеседник прав в диагностике (метрики не было — теперь есть, Хэмминг); но κ-Lorentz");
    print("     не срабатывает. Дыры §13 (гладкость, динамика, уникальность) собеседник сам признаёт.")


def main():
    print("=" * 86)
    print("ПРАВКИ: Connes-метрика (берём, ●) + κ-разбиение для Lorentz (отклоняем, ✗)")
    print("=" * 86)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 86)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: метрика ВЫВЕДЕНА (Connes=Хэмминг, евклидова) ● — реальное усиление; но κ-Lorentz")
    print("       ✗ (κ симметричен ⟹ сбалансированная сигнатура (k,k), не (1,n−1)). Lorentz=вход.")
    print("=" * 86)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
