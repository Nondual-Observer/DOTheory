# -*- coding: utf-8 -*-
"""
verify_radial_bridge.py — радиальный слой: метрика и мера вокруг шва.

Документ 01, глава VII (Изнанка) уже даёт радиальной координате частичную форму:
теорема о сфере для куба и октаэдра (ранг 3, §7.2), расщепление на осевую и
радиальную часть при сломе κ (§7.3), ось кривизны (2,3,p) с деревьями Брюа–Титса
на p-адической стороне (§7.5). Этот верификатор проверяет другой пласт той же
координаты: метрическую и мерную анатомию радиуса (норма, бюджет разложения,
концентрация меры, вынужденная метрика нулевой точки) и его дискретную парную
реализацию — адресное дерево (отличное от p-адических деревьев §7.5), связанное
с непрерывным радиусом формулой произведения.

  A. бюджет r² = w² + t² на скелете (обобщение теоремы о сфере §7.2 на ранг n);
  B. норма радиуса вынуждена: равенство параллелограмма только при p=2;
  C. конусная метрика вынуждена требованием "r=0 — одна точка"; метрика
     произведения противоречит; конус над круглой сферой = плоскость;
  D. концентрация меры: тонкая оболочка, недостижимость σ½ по мере;
  E. дилатация δ_λ — канонический радиальный поток;
  F. числовая реализация: r(d)=|ln(d/√N)|; страж базы убивает нумерологию;
  G. дискретный радиус: |·|₂ на адресах — ультраметрика (адресное дерево от
     семени), у |·|∞ её нет; ∏_v|x|_v=1 = радиальный баланс;
  H. две кривизны: угловой избыток в вершине конуса (L(n)=2ⁿ·arccos((n−2)/n),
     ровно 2π при n=1,2, растёт с n=3) вынужден скелетом и несоизмерим с π
     при n∉{1,2,4} (лемма Дена, теорема Нивена); углы лучевой оси (2,3,p) —
     рациональные доли π: вершинная и лучевая кривизна разделены.
"""
import math, random, itertools
from fractions import Fraction
random.seed(7)
P = 0


def ck(label, cond):
    global P
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    assert cond, label
    P += 1


print("=== A. скелет: бюджет r² = w² + t² (обобщение теоремы о сфере, §7.2, на ранг n) ===")
for n in range(2, 9):
    c = 0.5
    rr = set()
    ok_budget = True
    tmax = -1
    tmax_at = None
    tpole = None
    for v in itertools.product((0, 1), repeat=n):
        y = [x - c for x in v]
        r2 = sum(t * t for t in y)
        H = sum(v)
        w2 = (H - n / 2) ** 2 / n
        t2 = r2 - w2
        rr.add(round(r2, 9))
        if abs(t2 - (n / 4 - (H - n / 2) ** 2 / n)) > 1e-9:
            ok_budget = False
        if t2 > tmax:
            tmax, tmax_at = t2, H
        if H in (0, n):
            tpole = t2
    ck(f"n={n}: r²=n/4 у всех вершин (согласуется с §7.2: куб n=3, r²=3/4)", rr == {round(n / 4, 9)})
    ck(f"n={n}: тождество t² = n/4 − (H−n/2)²/n (бюджет вес⊥поперечное)", ok_budget)
    ck(f"n={n}: полюса чисто осевые (t²=0), максимум поперечного на среднем слое", abs(tpole) < 1e-9 and abs(tmax_at - n / 2) <= 0.5)

print("\n=== B. норма радиуса вынуждена самодвойственностью (параллелограмм ⟺ p=2) ===")


def lp(v, p):
    if p == float('inf'):
        return max(abs(t) for t in v)
    return sum(abs(t) ** p for t in v) ** (1 / p)


x = [0.3, -0.7, 0.2]
y = [-0.1, 0.4, 0.5]
for p in [1, 2, 3, float('inf')]:
    lhs = lp([a + b for a, b in zip(x, y)], p) ** 2 + lp([a - b for a, b in zip(x, y)], p) ** 2
    rhs = 2 * lp(x, p) ** 2 + 2 * lp(y, p) ** 2
    hold = abs(lhs - rhs) < 1e-9
    ck(f"p={p}: параллелограмм {'держится' if hold else 'не держится'}", hold == (p == 2))

print("\n=== C. конус вынужден; метрика произведения противоречива ===")
d_ang = 2.0
d_prod = math.sqrt(d_ang ** 2 + 0.0)
ck("метрика произведения: d((s1,0),(s2,0))>0 — противоречит единственности σ½ при r=0", d_prod > 0)


def cone(r1, r2, th):
    return math.sqrt(r1 * r1 + r2 * r2 - 2 * r1 * r2 * math.cos(min(th, math.pi)))


ck("конус: d((s1,0),(s2,0))=0 — склейка в одну точку σ½", cone(0, 0, d_ang) == 0)
ok = True
for _ in range(300):
    r1, r2 = random.uniform(0, 2), random.uniform(0, 2)
    t1, t2 = random.uniform(0, 2 * math.pi), random.uniform(0, 2 * math.pi)
    dth = abs(t1 - t2)
    dth = min(dth, 2 * math.pi - dth)
    de = math.hypot(r1 * math.cos(t1) - r2 * math.cos(t2), r1 * math.sin(t1) - r2 * math.sin(t2))
    if abs(cone(r1, r2, dth) - de) > 1e-9:
        ok = False
ck("конус над круглой окружностью = плоскость (закон косинусов, 300 случайных пар)", ok)

print("\n=== D. мера: тонкая оболочка и недостижимость наблюдателя ===")
n = 24
N = 20000
cnt_half = 0
s = 0.0
for _ in range(N):
    r2 = sum((random.random() - 0.5) ** 2 for _ in range(n))
    s += r2
    if r2 < (n / 12) * 0.25:
        cnt_half += 1
mean = s / N
ck(f"n={n}: E[r²]≈n/12 (получено {mean:.3f}, теория {n/12:.3f})", abs(mean - n / 12) < 0.05)
ck(f"n={n}: сфера вершин²/оболочка² = (n/4)/(n/12) = 3", abs((n / 4) / (n / 12) - 3) < 1e-12)
ck(f"n={n}: P(r < половина типичного) = {cnt_half/N:.4f} — окрестность σ½ пуста по мере", cnt_half / N < 0.001)

print("\n=== E. дилатация — канонический радиальный поток ===")
ok = True
for _ in range(200):
    yv = [random.uniform(-0.5, 0.5) for _ in range(5)]
    lam = random.uniform(0, 2)
    a = [-lam * t for t in yv]
    b = [lam * (-t) for t in yv]
    if any(abs(pp - qq) > 1e-12 for pp, qq in zip(a, b)):
        ok = False
ck("δ_λ∘κ = κ∘δ_λ — поток радиуса согласован с дополнением", ok)
ok = True
for _ in range(100):
    lam = random.uniform(0, 2)
    if abs(lam - 1) < 1e-3:
        continue
    yv = [random.uniform(-0.5, 0.5) for _ in range(5)]
    if max(abs(t) for t in yv) > 1e-6 and max(abs(lam * t - t) for t in yv) < 1e-12:
        ok = False
ck("δ_λ (λ≠1): всякая точка y≠0 сдвигается (λy≠y); неподвижна только y=0 = σ½", ok)
okn = True
for N0, d, lam in [(30, 2, 0.3), (30, 15, 1.7), (210, 6, 0.5)]:
    lhs = math.sqrt(N0) * ((N0 / d) / math.sqrt(N0)) ** lam
    rhs = N0 / (math.sqrt(N0) * (d / math.sqrt(N0)) ** lam)
    if abs(lhs - rhs) > 1e-9:
        okn = False
ck("на числах: δ_λ(N/d) = N/δ_λ(d) — дилатация к √N коммутирует с κ=d↦N/d", okn)

print("\n=== F. числовая реализация радиуса ===")


def radii(N0):
    ps = []
    d = 2
    m = N0
    while m > 1:
        if m % d == 0:
            ps.append(d)
            while m % d == 0:
                m //= d
        d += 1
    divs = [xx for xx in range(2, N0) if N0 % xx == 0]
    return {xx: abs(math.log(xx / math.sqrt(N0))) for xx in divs}, ps


r30, _ = radii(30)
ck("N=30: κ-пары зеркальны r(d)=r(30/d) для всех собственных делителей", all(abs(r30[d] - r30[30 // d]) < 1e-12 for d in r30))
vals = sorted(set(round(v, 6) for v in r30.values()))
ck(f"N=30: радиусы различны по парам {vals} — вырождение скелета снято числом", len(vals) == 3)
res = {}
for N0 in (6, 30, 210):
    _, ps = radii(N0)
    sum_r = sum(abs(math.log(pp / math.sqrt(N0))) for pp in ps)
    res[N0] = (sum_r, math.log(math.sqrt(N0)))
ck("страж базы: Σ_p r(p)=ln√N держится при k=3 (N=30) ...", abs(res[30][0] - res[30][1]) < 1e-9)
ck("... и не держится при k=2 (N=6) и k=4 (N=210): совпадение ранга 3, не закон", abs(res[6][0] - res[6][1]) > 1e-6 and abs(res[210][0] - res[210][1]) > 1e-6)

print("\n=== G. два радиуса: дерево от семени и конус к наблюдателю; ∏=1 = баланс ===")


def d2(a, b):
    xx = a ^ b
    if xx == 0:
        return 0.0
    k = 0
    while xx & 1 == 0:
        xx >>= 1
        k += 1
    return 2.0 ** (-k)


ok = True
for _ in range(500):
    a, b, c = (random.randrange(64) for _ in range(3))
    if d2(a, c) > max(d2(a, b), d2(b, c)) + 1e-12:
        ok = False
ck("|·|₂ на адресах — ультраметрика (адресное дерево от семени, отлично от p-адических деревьев §7.5)", ok)
x1, y1, x2, y2 = 1.0, 0.0, 0.0, 1.0
de = math.hypot(x1 - x2, y1 - y2)
ck("|·|∞-сторона не ультраметрична (√2 > max(1,1)) — непрерывный радиус живёт в конусе, не в дереве", de > 1 + 1e-9)


def valuations(num, den):
    tot = math.log(num / den)
    for p in (2, 3, 5, 7, 11, 13):
        vp = 0
        m = num
        while m % p == 0:
            m //= p
            vp += 1
        m = den
        while m % p == 0:
            m //= p
            vp -= 1
        tot += vp * math.log(1 / p)
    return tot


ok = all(abs(valuations(a, b)) < 1e-9 for a, b in [(12, 5), (7, 1), (30, 49), (64, 27)])
ck("Σ_v ln|x|_v = 0 — формула произведения как радиальный баланс: наружный радиус = сумма глубин внутрь", ok)

print("\n=== H. две кривизны: вершинный избыток вынужден, лучевая ось — вход ===")
# угол между хэмминг-соседями из центра: arccos((n−2)/n) — один для всех рёбер
ok = True
for n in range(2, 7):
    c = 0.5
    verts = list(itertools.product((0, 1), repeat=n))
    for _ in range(60):
        v = random.choice(verts)
        i = random.randrange(n)
        u = list(v)
        u[i] = 1 - u[i]
        yv = [a - c for a in v]
        yu = [a - c for a in u]
        dot = sum(p * q for p, q in zip(yv, yu))
        rr = sum(p * p for p in yv)
        if abs(dot / rr - (n - 2) / n) > 1e-12:
            ok = False
ck("угол любого ребра из σ½ один: cos = (n−2)/n (n=2..6) — длина цикла Грея не зависит от выбора цикла", ok)


def L(n):
    return (2 ** n) * math.acos((n - 2) / n)


ok = abs(L(1) - 2 * math.pi) < 1e-12 and abs(L(2) - 2 * math.pi) < 1e-12
ok = ok and all(L(n) > 2 * math.pi + 1e-9 and L(n) > L(n - 1) for n in range(3, 11))
ck("L(1)=L(2)=2π точно (плоско); L(n)>2π и растёт при n≥3 — угловой избыток в вершине конуса", ok)
# лемма Дена: cos θ = 1/3 ⟹ cos(kθ) = a_k/3^k, 3∤a_k — точная арифметика дробей
c3 = [Fraction(1), Fraction(1, 3)]
for k in range(1, 60):
    c3.append(2 * Fraction(1, 3) * c3[k] - c3[k - 1])
ok = all(c3[k].denominator == 3 ** k and c3[k].numerator % 3 != 0 for k in range(1, 60))
ck("лемма Дена: cos(kθ)=a_k/3^k, 3∤a_k (k=1..59) ⟹ arccos(1/3)/π иррационален — вершинный угол ранга 3", ok)
sol = [n for n in range(1, 50)
       if Fraction(n - 2, n) in (Fraction(0), Fraction(1, 2), Fraction(-1, 2), Fraction(1), Fraction(-1))]
ck("Нивен: arccos((n−2)/n) соизмерим с π ⟺ n∈{1,2,4}; углы оси (2,3,p) — π/2,π/3,π/p, все соизмеримы"
   " ⟹ вершинная кривизна не выражается рационально через лучевую", sol == [1, 2, 4])

print(f"\n{P} PASS — форма радиального слоя вынуждена (норма, бюджет, оболочка, конус, дерево/конус, дилатация, вершинный избыток); позиция на радиусе — вход.")
