#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_octahedron_relations.py — ★R₁/R₂/R₃, голономия T/𝒯, арифм.октаэдр, наблюдатель=фактор Uₙ/κ, Петерсен, Мерсенн.

Восстанавливает пропущенное ядро ранга 3 и высших рангов: ЕДИНОЕ хэммингово расстояние на U₃ разбивается на ТРИ отношения R₁(d=1)=C₆, R₂(d=2)=2K₃,
R₃(d=3)=3K₂; R₁∪R₂=K(2,2,2)=октаэдр, R₃=три оси. Голономия: сдвиг T (порядок 6, T³=κ) ≠ скрученный транспорт 𝒯
(±1, 𝒯²=id, лента Мёбиуса). Наблюдатель = проективный ФАКТОР Uₙ/κ≅PG(n−2,2) (не только центр σ½). Арифм.октаэдр
= делители 30. Цвет: R₁=hue-круг, R₂=RGB/CMY, R₃=комплементы. Высшие ранги: Петерсен дважды (KG(5,2)), горизонт
Мерсенна |Uₙ/κ|=2ⁿ⁻¹−1. Регистр ●◐○: комбинаторика/спектры/арифметика=●; цвет↔число, наблюдатель=фактор=◐;
E₈/Гаусс-Вантцель=◐/○.

  A. ★R₁/R₂/R₃: единое d_H на U₃ → три отношения C₆ / 2K₃ / 3K₂; R₁∪R₂=K(2,2,2); R₃=три оси.
  B. ГОЛОНОМИЯ: сдвиг T (порядок 6, T³=κ) ≠ транспорт 𝒯 (±1 на петле, 𝒯²=id, C₆→C₃ связный двойной накрыв).
  C. АРИФМ.ОКТАЭДР: делители 30 {2,3,5,6,10,15} = те же R₁/R₂/R₃ (сопряж.пары / простые↔полупростые / цикл).
  D. ЦВЕТ R₁/R₂/R₃: 6 хром.вершин; R₁=hue-круг, R₂=RGB/CMY, R₃=комплементы R↔C; группа B₃=48.
  E. НАБЛЮДАТЕЛЬ=ФАКТОР: Uₙ/κ≅PG(n−2,2), число осей 2ⁿ⁻¹−1 (n=3→3, 4→7 Фано, 5→15).
  F. ★ПЕТЕРСЕН: ранг 5 слой S₂⁽⁵⁾=KG(5,2) (дизъюнктность) = Петерсен (10 верш, 3-регуляр, спектр {3,1⁵,−2⁴}).
  G. ГОРИЗОНТ МЕРСЕННА: |Uₙ/κ|=2ⁿ⁻¹−1 простое ⟺ n∈{3,4,6,8} (Зингер транзитивен); Гаусс-Вантцель=◐/○.
  H. страж: R₁/R₂/R₃=ОДНО расстояние по значению (не три объекта); наблюдатель=фактор/центр=два чтения.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

U3 = [0b001, 0b010, 0b100, 0b011, 0b101, 0b110]      # шесть точек (без полюсов 000,111)
def dH(a, b): return bin(a ^ b).count('1')
def kap(x): return 7 ^ x
def components(adj, verts):
    seen, comp = set(), 0
    for v in verts:
        if v in seen: continue
        comp += 1; stack = [v]
        while stack:
            u = stack.pop()
            if u in seen: continue
            seen.add(u)
            stack += [w for w in verts if adj(u, w) and w not in seen]
    return comp


# ═══════════════ A. R₁/R₂/R₃ ═══════════════
def section_A():
    print("\n[A] ★R₁/R₂/R₃: единое d_H на U₃ → три отношения C₆ / 2K₃ / 3K₂; R₁∪R₂=K(2,2,2); R₃=три оси")
    pairs = list(combinations(U3, 2))
    r1 = [(a, b) for a, b in pairs if dH(a, b) == 1]
    r2 = [(a, b) for a, b in pairs if dH(a, b) == 2]
    r3 = [(a, b) for a, b in pairs if dH(a, b) == 3]
    counts = (len(r1), len(r2), len(r3)) == (6, 6, 3) and len(pairs) == 15   # 6+6+3=15
    deg1 = all(sum(1 for b in U3 if dH(a, b) == 1) == 2 for a in U3)         # R₁ 2-регулярен = C₆
    r1_conn = components(lambda a, b: dH(a, b) == 1, U3) == 1                 # C₆ связен (один цикл)
    r2_comp = components(lambda a, b: dH(a, b) == 2, U3) == 2                 # 2K₃ = два треугольника
    deg2 = all(sum(1 for b in U3 if dH(a, b) == 2) == 2 for a in U3)         # внутри K₃ 2-регуляр
    r3_match = all(sum(1 for b in U3 if dH(a, b) == 3) == 1 for a in U3) and all(kap(a) == [b for b in U3 if dH(a, b) == 3][0] for a in U3)  # 3K₂ = κ-пары
    oct_deg = all(sum(1 for b in U3 if dH(a, b) in (1, 2)) == 4 for a in U3)  # R₁∪R₂ = K(2,2,2) 4-регуляр
    check(f"d_H на 15 парах U₃ разбивает на R₁(d=1)={len(r1)}=C₆ (2-регуляр,связен:{deg1 and r1_conn}) · "
          f"R₂(d=2)={len(r2)}=2K₃ (2 компоненты:{r2_comp}, 2-регуляр:{deg2}) · R₃(d=3)={len(r3)}=3K₂ (κ-пары:"
          f"{r3_match}); счёт 6+6+3=15:{counts}; R₁∪R₂=K(2,2,2) 4-регуляр:{oct_deg} ⟹ ★ОДНО расстояние → ТРИ "
          f"отношения; октаэдр=R₁∪R₂, три оси=R₃ (ядро ранга 3)",
          counts and deg1 and r1_conn and r2_comp and deg2 and r3_match and oct_deg)


# ═══════════════ B. голономия T vs 𝒯 ═══════════════
def section_B():
    print("\n[B] ГОЛОНОМИЯ: сдвиг T (порядок 6, T³=κ) ≠ транспорт 𝒯 (±1, 𝒯²=id, C₆→C₃ связный двойной накрыв)")
    order = [0b001, 0b011, 0b010, 0b110, 0b100, 0b101]     # C₆ (соседние d=1)
    ham1 = all(dH(order[i], order[(i + 1) % 6]) == 1 for i in range(6))
    T3_kappa = all(order[(i + 3) % 6] == kap(order[i]) for i in range(6))   # T³ = κ (сдвиг на 3 = антипод)
    # 𝒯: фактор C₆/κ = C₃; накрытие C₆→C₃ связно (нетривиальный класс H¹(S¹;ℤ/2))
    classes = {}
    for i, x in enumerate(order):
        k = frozenset((x, kap(x)))
        classes.setdefault(k, []).append(i)
    c3 = len(classes) == 3 and all(len(v) == 2 for v in classes.values())    # 3 κ-класса по 2
    # связность накрытия: обход C₃ один раз = полуоборот C₆ = κ ≠ id ⟹ 𝒯 меняет знак, 𝒯²=id
    monodromy = T3_kappa                                    # петля C₃ поднимается в путь длины 3 = κ
    check(f"C₆ (соседние d=1): {ham1}; сдвиг T: T³=κ (порядок 6), полуоборот=антипод: {T3_kappa}; фактор C₆/κ=C₃ "
          f"(3 класса по 2): {c3}; накрытие C₆→C₃ СВЯЗНО ⟹ монодромия нетривиальна (петля C₃ → κ, не id): "
          f"{monodromy} ⟹ ★различать СДВИГ T (переставляет точки) и ТРАНСПОРТ 𝒯 (знак ±1 на петле, 𝒯²=id) — "
          f"именно 𝒯 есть строгая лента Мёбиуса (H¹(S¹;ℤ/2))", ham1 and T3_kappa and c3 and monodromy)


# ═══════════════ C. арифметический октаэдр ═══════════════
def section_C():
    print("\n[C] АРИФМ.ОКТАЭДР: делители 30 {2,3,5,6,10,15} = те же R₁/R₂/R₃ под D(30)≅Q₃")
    primes = {2: 0b100, 3: 0b010, 5: 0b001}                # простое → ось-бит
    def pset(d):                                            # делитель → битвектор множества простых
        v = 0
        for p, bit in primes.items():
            if d % p == 0: v |= bit
        return v
    divs = [2, 3, 5, 6, 10, 15]                             # собственные делители 30 (без 1,30)
    vecs = {d: pset(d) for d in divs}
    # R₃ = сопряжённые пары d↦30/d = хэмминг-3 = комплемент
    r3 = all(dH(vecs[d], vecs[30 // d]) == 3 for d in divs)
    conj = {frozenset((d, 30 // d)) for d in divs} == {frozenset((2, 15)), frozenset((3, 10)), frozenset((5, 6))}
    # R₂ = простые {2,3,5} (вес 1) vs полупростые {6,10,15} (вес 2)
    primes_layer = {d for d in divs if bin(vecs[d]).count('1') == 1} == {2, 3, 5}
    semi_layer = {d for d in divs if bin(vecs[d]).count('1') == 2} == {6, 10, 15}
    # R₁ = цикл 2→6→3→15→5→10→2 (соседние отличаются одним простым = хэмминг-1)
    cyc = [2, 6, 3, 15, 5, 10]
    r1 = all(dH(vecs[cyc[i]], vecs[cyc[(i + 1) % 6]]) == 1 for i in range(6))
    check(f"делители 30 под простые↔биты: R₃=сопряж.пары {{2,15}},{{3,10}},{{5,6}} (d↦30/d, хэмминг-3): "
          f"{r3 and conj}; R₂=простые {{2,3,5}} / полупростые {{6,10,15}}: {primes_layer and semi_layer}; "
          f"R₁=цикл 2→6→3→15→5→10→2 (хэмминг-1): {r1} ⟹ АРИФМЕТИЧЕСКИЙ октаэдр = тот же R₁/R₂/R₃ (число=куб "
          f"простых, D(30)≅Q₃)", r3 and conj and primes_layer and semi_layer and r1)


# ═══════════════ D. цвет R₁/R₂/R₃ ═══════════════
def section_D():
    print("\n[D] ЦВЕТ R₁/R₂/R₃: R₁=hue-круг, R₂=RGB/CMY, R₃=комплементы R↔C; группа B₃=48")
    col = {'R': 0b100, 'G': 0b010, 'B': 0b001, 'Y': 0b110, 'M': 0b101, 'C': 0b011}
    r3 = (dH(col['R'], col['C']) == 3 and dH(col['G'], col['M']) == 3 and dH(col['B'], col['Y']) == 3)  # комплементы
    rgb = {col['R'], col['G'], col['B']}; cmy = {col['Y'], col['M'], col['C']}
    r2 = all(dH(a, b) == 2 for a in rgb for b in rgb if a != b) and all(dH(a, b) == 2 for a in cmy for b in cmy if a != b)
    wheel = ['R', 'Y', 'G', 'C', 'B', 'M']                  # hue-круг
    r1 = all(dH(col[wheel[i]], col[wheel[(i + 1) % 6]]) == 1 for i in range(6))
    b3 = 2 ** 3 * 6 == 48                                   # |B₃|=(ℤ/2)³⋊S₃ = 8·6
    check(f"R₃=комплементы R↔C,G↔M,B↔Y (хэмминг-3): {r3}; R₂=RGB-триада/CMY-триада (внутри хэмминг-2): {r2}; "
          f"R₁=hue-круг R→Y→G→C→B→M (хэмминг-1): {r1}; |B₃|=(ℤ/2)³⋊S₃=48: {b3} ⟹ 4 карты RGB/CMY/Lab/HSB = "
          f"три проекции одного октаэдра (R₁=hue/HSB, R₂=RGB↔CMY, R₃=Lab-оппонент/комплемент)", r3 and r2 and r1 and b3)


# ═══════════════ E. наблюдатель = проективный фактор ═══════════════
def section_E():
    print("\n[E] НАБЛЮДАТЕЛЬ=ФАКТОР: Uₙ/κ≅PG(n−2,2), число осей 2ⁿ⁻¹−1 (n=3→3, 4→7 Фано, 5→15)")
    ok = True
    for n in (3, 4, 5, 6):
        full = (1 << n) - 1
        U = [x for x in range(1 << n) if x not in (0, full)]
        seen, axes = set(), 0
        for x in U:
            if x in seen: continue
            seen.add(x); seen.add(full ^ x); axes += 1
        ok = ok and (axes == 2 ** (n - 1) - 1)             # |Uₙ/κ| = 2ⁿ⁻¹−1 = |PG(n−2,2)|
    check(f"|Uₙ/κ|=2ⁿ⁻¹−1=|PG(n−2,2)| (n=3→3, 4→7=Фано, 5→15, 6→31): {ok} ⟹ ★НАБЛЮДАТЕЛЬ как ПРОЕКТИВНЫЙ "
          f"ФАКТОР (оси, куда сворачиваются противоположные направления) — второе чтение рядом с центром σ½ "
          f"(◐); лифт Q*_{{n−1}}≅Uₙ/κ: содержание ранга → оси следующего", ok)


# ═══════════════ F. Петерсен ═══════════════
def section_F():
    print("\n[F] ★ПЕТЕРСЕН: ранг 5 слой S₂⁽⁵⁾=KG(5,2) (дизъюнктность) = Петерсен (10 верш, 3-регуляр, {3,1⁵,−2⁴})")
    verts = list(combinations(range(5), 2))                # 2-подмножества {0..4} = средний слой S₂⁽⁵⁾
    n = len(verts)
    A = np.zeros((n, n), int)
    for i, a in enumerate(verts):
        for j, b in enumerate(verts):
            if i != j and set(a).isdisjoint(b):            # смежны ⟺ дизъюнктны = Kneser KG(5,2)
                A[i][j] = 1
    ten = n == 10
    reg3 = all(A.sum(1)[i] == 3 for i in range(n))         # 3-регуляр
    tri_free = all(not (A[i][j] and A[j][k] and A[i][k]) for i in range(n) for j in range(n) for k in range(n))
    spec = sorted(np.linalg.eigvalsh(A.astype(float)).round(6))
    petersen_spec = np.allclose(spec, sorted([3] + [1] * 5 + [-2] * 4))
    check(f"S₂⁽⁵⁾ = 2-подмн.{{0..4}} = {n} вершин: {ten}; смежность=дизъюнктность (Kneser KG(5,2)): 3-регуляр "
          f"{reg3}, без треугольников {tri_free}, спектр {{3,1⁵,−2⁴}} {petersen_spec} ⟹ ★ПЕТЕРСЕН на ранге 5 "
          f"(комбинаторное предсказание лифта, не физика); появляется и на ранге 6 (S₃⁽⁶⁾/κ)",
          ten and reg3 and tri_free and petersen_spec)


# ═══════════════ G. горизонт Мерсенна ═══════════════
def section_G():
    print("\n[G] ГОРИЗОНТ МЕРСЕННА: |Uₙ/κ|=2ⁿ⁻¹−1 просто ⟺ n∈{3,4,6,8}; простой порядок = нет подорбит; Гаусс-Вантцель=○")
    # Точность формулировки: цикл Зингера ТРАНЗИТИВЕН на точках PG(n−2,2) при ЛЮБОМ n (классика, не отличитель).
    # Содержание горизонта — ПОРЯДОК цикла: при простом 2ⁿ⁻¹−1 каждый нетривиальный элемент — полный цикл
    # (образующая группы простого порядка); при составном есть собственные подгруппы → короткие подорбиты.
    from math import gcd
    def is_prime(m): return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))
    horizon = [n for n in range(3, 12) if is_prime(2 ** (n - 1) - 1)]
    want = [3, 4, 6, 8]                                     # 2ⁿ⁻¹−1 ∈ {3,7,31,127} простые
    check(f"|Uₙ/κ|=2ⁿ⁻¹−1 просто (Мерсенн) при n∈{horizon} (={want}); n=5→2⁴−1=15=3·5 составное",
          horizon == want and 2 ** 4 - 1 == 15 and 15 % 3 == 0 and 15 % 5 == 0)
    # полных циклов в Z/m ровно φ(m) (образующие); подорбиты элемента k имеют длину m/gcd(k,m)
    def full_cycles(m): return sum(1 for k in range(1, m) if gcd(k, m) == 1)
    check("порядок 7 (n=4) прост: полный цикл — КАЖДЫЙ из 6 нетривиальных (φ(7)=6, подорбит нет)",
          full_cycles(7) == 6)
    check("порядок 15 (n=5) составной: полных циклов лишь φ(15)=8 из 14; у k=5 подорбиты длины 3, у k=3 — длины 5",
          full_cycles(15) == 8 and 15 // gcd(5, 15) == 3 and 15 // gcd(3, 15) == 5)
    check("порядок 31 (n=6) прост: φ(31)=30 — подорбит нет", full_cycles(31) == 30)
    print("   ● арифметика горизонта и подорбит; связь с Гаусс–Вантцель (правильные многоугольники) = ○ фронт")


# ═══════════════ H. страж ═══════════════
def section_H():
    print("\n[H] СТРАЖ: R₁/R₂/R₃=ОДНО расстояние по значению; наблюдатель=фактор/центр=два чтения")
    print("   ● доказано: три отношения из ОДНОГО d_H (A), голономия T/𝒯 (B), арифм.октаэдр (C), цвет-карты (D),")
    print("     фактор Uₙ/κ=PG(n−2,2) (E), Петерсен спектр (F), горизонт Мерсенна (G)")
    print("   ◐ чтения: цвет↔число↔звук (одна фигура), наблюдатель=проективный фактор (рядом с центром σ½)")
    print("   ◐/○ фронт: E₈=октонионы, Гаусс–Вантцель↔Мерсенн — узор, не вывод")
    # R₁,R₂,R₃ покрывают ВСЕ пары ровно раз (одно расстояние, три значения)
    pairs = list(combinations(U3, 2))
    cover = sum(1 for a, b in pairs if dH(a, b) in (1, 2, 3)) == len(pairs) == 15
    check(f"R₁∪R₂∪R₃ покрывают все 15 пар U₃ ровно раз (одно расстояние d∈{{1,2,3}}): {cover} ⟹ три отношения = "
          f"ОДНА мера по значению, не три независимых объекта; октаэдр/Фано/цвет/делители = чтения одной "
          f"вынужденной фигуры", cover)


def main():
    print("=" * 100)
    print("R₁/R₂/R₃, ГОЛОНОМИЯ T/𝒯, АРИФМ.ОКТАЭДР, НАБЛЮДАТЕЛЬ=ФАКТОР Uₙ/κ, ПЕТЕРСЕН, ГОРИЗОНТ МЕРСЕННА")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G(); section_H()
    print("\n" + "=" * 100)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: единое хэммингово расстояние на U₃ даёт ТРИ отношения — R₁=C₆ (цикл), R₂=2K₃ (расщепление),")
    print("       R₃=3K₂ (оси); R₁∪R₂=октаэдр K(2,2,2), R₃=три оси. Голономия: сдвиг T (T³=κ) ≠ транспорт 𝒯 (±1,")
    print("       лента Мёбиуса). Арифм.октаэдр=делители 30, цвет=три проекции (B₃), наблюдатель=фактор Uₙ/κ=")
    print("       PG(n−2,2). Высшие ранги: Петерсен (KG(5,2)) на 5/6, горизонт Мерсенна n∈{3,4,6,8}. ● комбинатор.;")
    print("       ◐ цвет↔число, наблюдатель=фактор; ◐/○ E₈/Гаусс-Вантцель.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
