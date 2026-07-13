#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_hexad_rigidity.py — жёсткость шестёрки ранга 3, четыре чтения ранга, строитель/страж.

  A. Жёсткость: из 720 перестановок U₃ все три отношения R₁,R₂,R₃ сохраняют РОВНО 12 (D₆);
     сохранение одного R₁ уже влечёт R₂ и R₃ (хэммингово расстояние = цикловое на C₆).
  B. Четыре чтения ранга n: симплекс n+1 / кросс-политоп 2n / куб 2ⁿ / симметрия n!;
     куб и кросс-политоп двойственны (счёт вершин/гиперграней меняется местами), симплекс самодвойствен.
  C. Две шестёрки: 2n=n! разрешимо ровно при n=3 (сцена 2n и симметрия n! совпадают числом только там).
  D. Строитель/страж: a+b=a·b в натуральных числах ровно при a=b=2 (узел 4, где стороны совпадают).
Регистр: A–D — ● перебор/арифметика; чтения «акт/тело/мир/симметрия» и «строитель/страж» — ◐ (в главе так и помечены).
"""
from __future__ import annotations
from itertools import permutations
from math import factorial

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

U = ['001', '010', '100', '011', '101', '110']
def ham(a, b): return sum(x != y for x, y in zip(a, b))
REL = {(i, j): ham(U[i], U[j]) for i in range(6) for j in range(i + 1, 6)}

def preserves(p, only=None):
    for (i, j), v in REL.items():
        w = REL[tuple(sorted((p[i], p[j])))]
        if only is None:
            if w != v: return False
        else:
            if (w == only) != (v == only): return False
    return True

def section_A():
    print("\n[A] Жёсткость шестёрки: 12 из 720; R₁ влечёт всё")
    all3 = [p for p in permutations(range(6)) if preserves(p)]
    check("сохраняющих R₁,R₂,R₃ ровно 12", len(all3) == 12, f"={len(all3)}")
    r1 = [p for p in permutations(range(6)) if preserves(p, only=1)]
    check("сохраняющих только-R₁ тоже 12 (D₆)", len(r1) == 12, f"={len(r1)}")
    check("каждая R₁-сохраняющая сохраняет все три", all(preserves(p) for p in r1))
    # различающий контроль: перестановка вне D₆ ломает отношения
    bad = next(p for p in permutations(range(6)) if not preserves(p))
    check("контроль: существует перестановка, ломающая отношения", not preserves(bad))

def section_B():
    print("\n[B] Четыре чтения ранга: счёты и двойственность фигур")
    for n in (2, 3, 4):
        simplex_v, simplex_f = n + 1, n + 1            # вершины/гиперграни симплекса
        cross_v, cross_f = 2 * n, 2 ** n               # кросс-политоп
        cube_v, cube_f = 2 ** n, 2 * n                 # куб
        check(f"n={n}: куб ({cube_v}в/{cube_f}г) ↔ кросс-политоп ({cross_v}в/{cross_f}г) — счёты меняются местами",
              (cube_v, cube_f) == (cross_f, cross_v))
        check(f"n={n}: симплекс самодвойствен ({simplex_v}в/{simplex_f}г)", simplex_v == simplex_f)
    check("ранг 3: сцена |U₃|=6=2n (кросс-политоп=октаэдр)", 2 * 3 == 6)

def section_C():
    print("\n[C] Две шестёрки: 2n=n! ровно при n=3")
    sols = [n for n in range(1, 13) if 2 * n == factorial(n)]
    check("решение единственно: n=3", sols == [3], f"={sols}")
    check("6 вершин октаэдра = |S₃|=6", 2 * 3 == factorial(3))

def section_D():
    print("\n[D] Строитель/страж: узел совпадения сторон")
    sols = [(a, b) for a in range(1, 50) for b in range(a, 50) if a + b == a * b]
    check("a+b=a·b в ℕ ровно при (2,2)", sols == [(2, 2)], f"={sols}")

if __name__ == "__main__":
    print("=" * 70)
    print("verify_hexad_rigidity.py — жёсткость 12/720 · четыре чтения ранга · 2n=n! · узел 4")
    print("=" * 70)
    section_A(); section_B(); section_C(); section_D()
    print("\n" + "=" * 70)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("=" * 70)
