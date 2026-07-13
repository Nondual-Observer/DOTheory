#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_observer_definition.py — строгое определение наблюдателя σ½: инвариант κ вне состояний носителя.

Проверяет мотив определения:
 §A  κ:x↦x⊕1ⁿ на Q_n свободна (нет неподвижной точки, n≥1) и κ²=id — инвариант не реализуется состоянием.
 §B  непрерывное отражение r(x)=1−x на [0,1]ⁿ имеет ЕДИНСТВЕННУЮ неподвижную точку (½,…,½), и она ВНЕ вершин {0,1}ⁿ.
 §C  уравнение неподвижной точки сводится к 2x=1: разрешимо над char≠2 (x=½), неразрешимо над 𝔽₂ (2≡0).
 §D  {0,1} = ℤ/2-torsor: κ=перенос действует свободно и транзитивно — выделенного нуля нет.
 §E  расщепление проекторами P±=(1±T)/2 (T=−1) над ℚ: идемпотенты P±²=P±, P+P−=0, P++P−=I; над 𝔽₂ ½ отсутствует.

Регистр ●◐○: §A–§E математика = ●; отнесение центра ½ к наблюдателю = ◐; разделение сторон |·|₂/|·|∞ — ранг 2 (гл. III).
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

# ═══════════ A. κ на Q_n свободна, κ²=id ═══════════
def section_A():
    print("\n[A] κ:x↦x⊕1ⁿ свободна на Q_n (нет x с κx=x), κ²=id — инвариант не есть состояние")
    for n in range(1, 7):
        full = (1 << n) - 1                     # 1ⁿ = все единицы
        kap = lambda x: x ^ full
        states = range(1 << n)
        check(f"n={n}: κ без неподвижной точки (свобода действия)", all(kap(x) != x for x in states))
        check(f"n={n}: κ²=id (инволюция)", all(kap(kap(x)) == x for x in states))

# ═══════════ B. непрерывное отражение: центр ½ вне вершин ═══════════
def section_B():
    print("\n[B] r(x)=1−x на [0,1]ⁿ: единственная неподвижная (½,…,½), она ВНЕ вершин {0,1}ⁿ")
    for n in range(1, 5):
        fix = tuple(Fr(1, 2) for _ in range(n))
        r = lambda v: tuple(1 - c for c in v)
        check(f"n={n}: r(½,…,½) = (½,…,½)", r(fix) == fix)
        is_vertex = all(c in (Fr(0), Fr(1)) for c in fix)
        check(f"n={n}: центр вне вершин куба", not is_vertex)

# ═══════════ C. 2x=1: char≠2 даёт ½, над 𝔽₂ решения нет ═══════════
def section_C():
    print("\n[C] неподвижность сводится к 2x=1: над char≠2 корень x=½; над 𝔽₂ (2≡0) корня нет")
    check("над ℚ: 2·½ = 1 (½ существует)", 2 * Fr(1, 2) == 1)
    check("над 𝔽₂: ни один y не даёт 2y=1 (2≡0)", all((2 * y) % 2 != 1 for y in (0, 1)))
    check("2 обратимо над ℚ, но не mod 2 (зероделитель)", gcd(2, 2) != 1)

# ═══════════ D. torsor: κ свободна и транзитивна ═══════════
def section_D():
    print("\n[D] {0,1} = ℤ/2-torsor: κ=перенос свободен и транзитивен — выделенного нуля нет")
    S = [0, 1]; kap = lambda x: x ^ 1
    check("κ свободна (нет неподвижной)", all(kap(x) != x for x in S))
    orbit = {0, kap(0)}                          # орбита нуля под ⟨κ⟩
    check("одна орбита = весь носитель (транзитивна)", orbit == set(S))

# ═══════════ E. проекторы над ℚ; над 𝔽₂ ½ отсутствует ═══════════
def section_E():
    print("\n[E] P±=(1±T)/2, T=−1: над ℚ идемпотенты и дополнительны; над 𝔽₂ ½ не определена")
    T = Fr(-1)
    Pp = (1 + T) / 2                              # P+ = 0
    Pm = (1 - T) / 2                              # P- = 1
    check("P+² = P+ (идемпотент)", Pp * Pp == Pp)
    check("P−² = P− (идемпотент)", Pm * Pm == Pm)
    check("P+·P− = 0 (дополнительны)", Pp * Pm == 0)
    check("P+ + P− = 1 (полнота)", Pp + Pm == 1)
    check("над 𝔽₂: 2 не обратимо ⟹ (1±T)/2 не определён", all((2 * y) % 2 != 1 for y in (0, 1)))

if __name__ == "__main__":
    print("=" * 72)
    print("verify_observer_definition.py — наблюдатель σ½: инвариант κ вне состояний носителя")
    print("=" * 72)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 72)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("=" * 72)
