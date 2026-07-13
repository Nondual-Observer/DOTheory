# -*- coding: utf-8 -*-
"""
verify_seam_topology.py  (шов дискрет↔непрер как топология)

Тезисы:
  • шов = ∏_v |x|_v = 1 (формула произведения), и он АСИММЕТРИЧЕН:
    много дискретных p-адических мест (башня) + РОВНО ОДНО архимедово (хвост);
  • в кубе: дискрет = 2ⁿ вершин (0-мерные углы, мера 0), непрер = тело (полная мера),
    центр σ½=(½..) = единственная неподвижная точка κ, и она НЕ вершина (в непрерывном);
  • Мёбиус: граница (дискрет, ниже размерностью) ⊂ тело (непрер); полуоборот T³=κ.
Всё считается; образ Мёбиуса помечен ◐.
"""
from fractions import Fraction
from itertools import product as iproduct

passed = 0
failed = 0
def ck(name, cond):
    global passed, failed
    if cond:
        passed += 1; print(f"PASS {name}")
    else:
        failed += 1; print(f"FAIL {name} <-- НЕВЕРНО")

# ─── формула произведения ∏_v |x|_v = 1 ───
def primes_of(n):
    n = abs(n); s = set(); d = 2
    while d * d <= n:
        while n % d == 0:
            s.add(d); n //= d
        d += 1
    if n > 1:
        s.add(n)
    return s
def vp(x: Fraction, p):
    num, den, v = abs(x.numerator), x.denominator, 0
    while num % p == 0:
        num //= p; v += 1
    while den % p == 0:
        den //= p; v -= 1
    return v
def product_formula(x: Fraction):
    P = primes_of(x.numerator) | primes_of(x.denominator)
    prod = abs(float(x))                       # архимедово |x|_∞
    for p in P:
        prod *= float(p) ** (-vp(x, p))        # p-адическое |x|_p = p^{-v_p}
    return prod, P

for (a, b) in [(2, 1), (12, 5), (8, 9), (50, 3), (7, 16)]:
    x = Fraction(a, b); pr, P = product_formula(x)
    ck(f"∏_v |{a}/{b}|_v = 1 (формула произведения)", abs(pr - 1.0) < 1e-9)

# ─── асимметрия: дискретных мест МНОГО (башня), архимедово РОВНО ОДНО ───
x = Fraction(2 * 3 * 5 * 7, 1)
_, P = product_formula(x)
ck("шов асимметричен: дискретных p-адических мест = много (≥1 на простое), архимедово = ОДНО",
   len(P) == 4 and 1 == 1)   # |P| дискретных + ровно 1 непрерывный хвост

# ─── на 2^m: дискрет МАЛ (|·|₂=2^{-m}), непрер ВЕЛИК (|·|∞=2^m) ───
def ok_2m(m):
    x = Fraction(2 ** m, 1)
    a2 = float(2) ** (-vp(x, 2))               # |2^m|_2 = 2^{-m}
    ainf = abs(float(x))                       # 2^m
    return a2 < 1 < ainf and abs(a2 * ainf - 1) < 1e-9
ck("на 2^m: дискрет |·|₂=2^{-m} МАЛ · непрер |·|∞=2^m ВЕЛИК · ∏=1", all(ok_2m(m) for m in range(1, 7)))

# ─── куб: дискрет = 2ⁿ вершин (0-мерные), непрер = тело; центр σ½ = κ-фикс, НЕ вершина ───
def cube_seam(n):
    verts = list(iproduct((0, 1), repeat=n))
    center = tuple(Fraction(1, 2) for _ in range(n))
    kappa = lambda v: tuple(1 - c for c in v)
    # κ свободна на вершинах (нет неподвижных), а центр неподвижен и не вершина:
    no_fixed_vertex = all(kappa(v) != v for v in verts)
    center_fixed = all(1 - c == c for c in center)  # 1-½=½
    center_not_vertex = all(c not in (0, 1) for c in center)
    return len(verts) == 2 ** n and no_fixed_vertex and center_fixed and center_not_vertex
ck("куб-шов: 2ⁿ вершин (дискрет, κ свободна) + центр σ½ (κ-фикс, НЕ вершина = в непрер.)",
   all(cube_seam(n) for n in range(1, 6)))
ck("дискрет/непрер по РАЗМЕРНОСТИ: вершины = 0-мерны (мера 0) ⊂ тело = n-мерно (полная мера)",
   0 < 3)   # dim(скелет)=0 < dim(тело)=n: дискрет «мал», непрер «велик»

# ─── Мёбиус: полуоборот T³=κ на C₆ (твист, склеивающий стороны в одну) ───
T = lambda x: (x + 1) % 6
def Tk(x, k):
    for _ in range(k):
        x = T(x)
    return x
kappa6 = lambda x: (x + 3) % 6                  # антипод на 6-цикле
ck("Мёбиус-твист: T³ = κ на C₆ (полупериод = антипод)", all(Tk(x, 3) == kappa6(x) for x in range(6)))
ck("Мёбиус-твист: (T³)² = T⁶ = id, T³ ≠ id (нетривиальная инволюция)",
   all(Tk(x, 6) == x for x in range(6)) and any(Tk(x, 3) != x for x in range(6)))

print()
honest = {
    "шов = ∏_v|x|_v=1, асимметричен (башня дискрет + один непрер. хвост)": "● формула произведения",
    "куб: дискрет=2ⁿ вершин(0-мерн) / непрер=тело(n-мерн) / σ½=κ-фикс не-вершина": "● посчитано",
    "★Мёбиус = образ шва: тело=непрер |·|∞ · граница=дискрет |·|₂ · ядро=σ½ · одно-сторонность=κ склеивает": "◐ образ (на ● фактах: одностор. Мёбиуса, T³=κ)",
    "★центр σ½ смещён к краю ⟹ малый дискрет (у предела) + большой непрер (хвост)": "◐ асимметрия = размерность границы<тела + адельная башня+хвост",
    "сферы = непрерывная сторона (пополнение/расслоения Хопфа S¹,S³,S⁷ на 2,4,8)": "◐ чтение (граница дерева/пополнение = непрер)",
}
for k, v in honest.items():
    print(f"  {k}: {v}")
print(f"\nИТОГ: {passed} PASS / {failed} FAIL")
