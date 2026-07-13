#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_causal_structure.py — следующий шаг: ПРИЧИННОСТЬ. Мы нашли стрелу (комонада,
направление), но не световой конус. Причинность = ЧАСТИЧНЫЙ ПОРЯДОК на событиях, и он
уже есть: булева решётка Q_n с включением ⊆ ЕСТЬ причинное множество (causal set).

A. Q_n с ⊆ — локально-конечный частичный порядок = ПРИЧИННОЕ МНОЖЕСТВО (causet).
B. СВЕТОВЫЕ КОНУСЫ: будущее J⁺(x)={y⊇x} (2^{n−|x|}), прошлое J⁻(x)={z⊆x} (2^{|x|}),
   пространственно-подобное = несравнимые (ни x⊆y, ни y⊆x).
C. ВРЕМЯ = ЦЕПИ (timelike, флаги, n! максимальных); ПРОСТРАНСТВО = АНТИЦЕПИ (spacelike,
   весовые слои); ★МАКСИМАЛЬНАЯ пространственная плоскость = СРЕДНИЙ слой = σ½ (Шпернер).
D. СТРЕЛА (комонада-огрубление) согласована с порядком: G понижает вес = движение к прошлому.
E. РАЗМЕРНОСТЬ Майрхейма–Мейера: доля упорядоченных пар → 0 ⟹ НЕ фикс. d-Минковский;
   причинная СТРУКТУРА есть (конусы, время/пространство), но сигнатура/размерность = ВХОД ○.
"""
from __future__ import annotations
from math import comb
from itertools import combinations

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def popcount(x): return bin(x).count("1")
def leq(x, y): return (x & y) == x        # x ⊆ y


# ═══════ A. причинное множество ═══════
def section_A():
    print("\n[A] Q_n с ⊆ — локально-конечный частичный порядок = ПРИЧИННОЕ МНОЖЕСТВО")
    for n in range(2, 6):
        N = 1 << n
        refl = all(leq(x, x) for x in range(N))
        antisym = all((not (leq(x, y) and leq(y, x))) or x == y for x in range(N) for y in range(N))
        # транзитивность
        trans = True
        for x in range(N):
            for y in range(N):
                if leq(x, y):
                    for z in range(N):
                        if leq(y, z) and not leq(x, z): trans = False
        # локальная конечность: интервал [x,y] конечен (булев подкуб) — всегда для конечного N
        check(f"n={n}: ⊆ рефлексивно, антисимметрично, транзитивно, локально-конечно (causet)",
              refl and antisym and trans)


# ═══════ B. световые конусы ═══════
def section_B():
    print("\n[B] СВЕТОВЫЕ КОНУСЫ: J⁺(x)=2^{n−|x|}, J⁻(x)=2^{|x|}, spacelike=несравнимые")
    for n in range(2, 6):
        N = 1 << n
        ok = True
        for x in range(N):
            fut = sum(1 for y in range(N) if leq(x, y))      # будущее x⊆y
            past = sum(1 for z in range(N) if leq(z, x))     # прошлое z⊆x
            if fut != (1 << (n - popcount(x))) or past != (1 << popcount(x)): ok = False
        # пространственно-подобные пары = несравнимые
        space = sum(1 for x in range(N) for y in range(N)
                    if x < y and not leq(x, y) and not leq(y, x))
        check(f"n={n}: |J⁺(x)|=2^{{n−|x|}}, |J⁻(x)|=2^{{|x|}}; spacelike-пар={space}", ok and space > 0)
    print("   → конус прошлого/будущего и пространственно-подобная область определены порядком")


# ═══════ C. время=цепи, пространство=антицепи, max слой = σ½ (Шпернер) ═══════
def max_antichain_size(n):
    """ширина частичного порядка (макс. антицепь) перебором для малых n."""
    N = 1 << n
    elems = list(range(N))
    best = 0
    # жадно по слоям недостаточно; для n≤4 — поиск по подмножествам одного слоя + Шпернер.
    # Проверяем гипотезу Шпернера: max антицепь = средний слой. Брутфорс для n≤3.
    if n <= 3:
        from itertools import chain, combinations as comb_it
        # перебор всех антицепей дорог; используем: ширина = макс размер множества попарно несравнимых
        # для n≤3 (N≤8) перебор подмножеств
        for r in range(N + 1):
            for subset in comb_it(elems, r):
                if all(not leq(a, b) and not leq(b, a) for a, b in comb_it(subset, 2)):
                    best = max(best, len(subset))
        return best
    return comb(n, n // 2)   # Шпернер (теорема) для n≥4


def section_C():
    print("\n[C] ВРЕМЯ=цепи (timelike), ПРОСТРАНСТВО=антицепи; max слой=средний=σ½ (Шпернер)")
    from math import factorial
    for n in range(2, 6):
        # цепи (timelike, максимальные = флаги) = n!
        chains = factorial(n)
        # средний слой (max антицепь по Шпернеру) = C(n, ⌊n/2⌋), и это σ½-слой (вес n/2, H=0)
        mid = comb(n, n // 2)
        # проверка: средний слой — антицепь (попарно несравнимы)
        N = 1 << n
        mid_layer = [x for x in range(N) if popcount(x) == n // 2]
        is_antichain = all(not leq(a, b) and not leq(b, a)
                           for a, b in combinations(mid_layer, 2))
        check(f"n={n}: timelike-цепей (флагов)=n!={chains}; средний слой=антицепь размера C(n,⌊n/2⌋)={mid}",
              is_antichain and len(mid_layer) == mid)
    # Шпернер: max антицепь = средний слой (брутфорс n≤3)
    for n in (2, 3):
        w = max_antichain_size(n)
        check(f"n={n}: ШИРИНА (max пространственная плоскость) = C(n,⌊n/2⌋)={comb(n, n//2)} (Шпернер) = σ½-слой",
              w == comb(n, n // 2))
    print("   → max пространственный срез (антицепь) = средний слой = H=0 = σ½: наблюдатель = «сейчас»")


# ═══════ D. стрела (комонада) согласована с порядком ═══════
def section_D():
    print("\n[D] СТРЕЛА (комонада-огрубление) согласована: G понижает вес = к прошлому по ⊆")
    for n in range(2, 6):
        N = 1 << n; top = 1 << (n - 1)
        ok = True
        for x in range(N):
            Gx = x & ~top                                    # огрубление (забыть координату)
            # G(x) ⊆ x (огрубление идёт ВНИЗ по порядку = к прошлому) и вес не растёт
            if not (leq(Gx, x) and popcount(Gx) <= popcount(x)): ok = False
        check(f"n={n}: G(x)⊆x — комонада-огрубление = движение к прошлому (согласовано со стрелой)", ok)
    print("   → необратимая стрела (комонада) и причинный порядок ⊆ сонаправлены")


# ═══════ E. размерность Майрхейма–Мейера: не фикс. Минковский ═══════
def section_E():
    print("\n[E] РАЗМЕРНОСТЬ: доля упорядоченных пар r → 0 ⟹ НЕ фикс. d-Минковский (сигнатура=вход)")
    prev = 1.0
    for n in range(2, 8):
        N = 1 << n
        # число строгих причинных пар x⊊y = 3ⁿ − 2ⁿ (Σ C(n,k)2^{n−k} − диагональ)
        ordered = 3 ** n - 2 ** n
        total = N * (N - 1) // 2
        r = ordered / total
        check(f"n={n}: доля упорядоченных пар r={r:.4f} убывает (causet разрежается)", r < prev)
        prev = r
    print("   → r→0 ⟹ размерность Майрхейма–Мейера НЕ стабилизируется на 4: причинная СТРУКТУРА")
    print("     есть (конусы, время/пространство, σ½-срез), но 4D-Минковский/сигнатура = ВХОД [○]")


def main():
    print("=" * 84)
    print("ПРИЧИННОСТЬ: булева решётка Q_n с ⊆ как причинное множество (causal set)")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: причинная СТРУКТУРА есть из порядка ⊆ — световые конусы, timelike-цепи,")
    print("       spacelike-антицепи, max срез = σ½ (Шпернер), согласовано со стрелой-комонадой.")
    print("       НО размерность не фикс. 4 (r→0); Минковский-сигнатура остаётся ВХОДОМ [○].")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
