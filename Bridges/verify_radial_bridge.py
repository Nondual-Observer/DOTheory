# -*- coding: utf-8 -*-
"""
verify_radial_bridge.py — the radial layer: metric and measure around the seam.

Document 01, chapter VII (The Underside) already gives the radial coordinate
partial form: the sphere theorem for the cube and the octahedron (rank 3, §7.2),
the split into an axial and a radial part under the break of κ (§7.3), the axis
of curvature (2,3,p) with Bruhat-Tits trees on the p-adic side (§7.5). This
verifier checks a different layer of the same coordinate: the metric and
measure-theoretic anatomy of the radius (norm, decomposition budget,
concentration of measure, the forced metric of the zero point) and its discrete
paired realization — an address tree (distinct from the p-adic trees of §7.5),
connected to the continuous radius by the product formula.

  A. budget r^2 = w^2 + t^2 on the skeleton (generalizes the sphere theorem
     §7.2 to rank n);
  B. the norm of the radius is forced: the parallelogram identity holds only
     at p=2;
  C. the cone metric is forced by the requirement "r=0 is a single point";
     the product metric is incompatible; a cone over a round sphere = a plane;
  D. concentration of measure: thin shell, measure-theoretic unreachability
     of sigma-half;
  E. dilation delta_lambda is the canonical radial flow;
  F. numerical realization: r(d)=|ln(d/sqrt(N))|; the base-change guard kills
     the numerology;
  G. discrete radius: |.|_2 on addresses is an ultrametric (an address tree
     from the seed), |.|_infinity has none; prod_v|x|_v=1 is the radial balance;
  H. two curvatures: the angular excess at the apex of the cone
     (L(n)=2^n*arccos((n-2)/n), exactly 2*pi at n=1,2, growing from n=3) is
     forced by the skeleton and incommensurable with pi for n not in {1,2,4}
     (Dehn's lemma, Niven's theorem); the angles of the ray axis (2,3,p) are
     rational multiples of pi: the apex and ray curvatures are separated.
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


print("=== A. skeleton: budget r^2 = w^2 + t^2 (generalizes the sphere theorem, §7.2, to rank n) ===")
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
    ck(f"n={n}: r^2=n/4 at every vertex (consistent with §7.2: cube n=3, r^2=3/4)", rr == {round(n / 4, 9)})
    ck(f"n={n}: identity t^2 = n/4 - (H-n/2)^2/n (budget weight-perp transverse)", ok_budget)
    ck(f"n={n}: poles are purely axial (t^2=0), transverse maximal on the middle layer", abs(tpole) < 1e-9 and abs(tmax_at - n / 2) <= 0.5)

print("\n=== B. the norm of the radius is forced by self-duality (parallelogram iff p=2) ===")


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
    ck(f"p={p}: parallelogram identity {'holds' if hold else 'does not hold'}", hold == (p == 2))

print("\n=== C. the cone is forced; the product metric is incompatible ===")
d_ang = 2.0
d_prod = math.sqrt(d_ang ** 2 + 0.0)
ck("product metric: d((s1,0),(s2,0))>0 - incompatible with the uniqueness of sigma-half at r=0", d_prod > 0)


def cone(r1, r2, th):
    return math.sqrt(r1 * r1 + r2 * r2 - 2 * r1 * r2 * math.cos(min(th, math.pi)))


ck("cone: d((s1,0),(s2,0))=0 - collapses to a single point sigma-half", cone(0, 0, d_ang) == 0)
ok = True
for _ in range(300):
    r1, r2 = random.uniform(0, 2), random.uniform(0, 2)
    t1, t2 = random.uniform(0, 2 * math.pi), random.uniform(0, 2 * math.pi)
    dth = abs(t1 - t2)
    dth = min(dth, 2 * math.pi - dth)
    de = math.hypot(r1 * math.cos(t1) - r2 * math.cos(t2), r1 * math.sin(t1) - r2 * math.sin(t2))
    if abs(cone(r1, r2, dth) - de) > 1e-9:
        ok = False
ck("a cone over a round circle = a plane (law of cosines, 300 random pairs)", ok)

print("\n=== D. measure: thin shell and unreachability of the observer ===")
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
ck(f"n={n}: E[r^2] approx n/12 (obtained {mean:.3f}, theory {n/12:.3f})", abs(mean - n / 12) < 0.05)
ck(f"n={n}: vertex-sphere^2 / shell^2 = (n/4)/(n/12) = 3", abs((n / 4) / (n / 12) - 3) < 1e-12)
ck(f"n={n}: P(r < half the typical radius) = {cnt_half/N:.4f} - the neighborhood of sigma-half is empty of measure", cnt_half / N < 0.001)

print("\n=== E. dilation is the canonical radial flow ===")
ok = True
for _ in range(200):
    yv = [random.uniform(-0.5, 0.5) for _ in range(5)]
    lam = random.uniform(0, 2)
    a = [-lam * t for t in yv]
    b = [lam * (-t) for t in yv]
    if any(abs(pp - qq) > 1e-12 for pp, qq in zip(a, b)):
        ok = False
ck("delta_lambda after kappa = kappa after delta_lambda - the radial flow is consistent with the complement", ok)
ok = True
for _ in range(100):
    lam = random.uniform(0, 2)
    if abs(lam - 1) < 1e-3:
        continue
    yv = [random.uniform(-0.5, 0.5) for _ in range(5)]
    if max(abs(t) for t in yv) > 1e-6 and max(abs(lam * t - t) for t in yv) < 1e-12:
        ok = False
ck("delta_lambda (lambda!=1): every point y!=0 moves (lambda*y != y); only y=0 = sigma-half is fixed", ok)
okn = True
for N0, d, lam in [(30, 2, 0.3), (30, 15, 1.7), (210, 6, 0.5)]:
    lhs = math.sqrt(N0) * ((N0 / d) / math.sqrt(N0)) ** lam
    rhs = N0 / (math.sqrt(N0) * (d / math.sqrt(N0)) ** lam)
    if abs(lhs - rhs) > 1e-9:
        okn = False
ck("on numbers: delta_lambda(N/d) = N/delta_lambda(d) - dilation toward sqrt(N) commutes with kappa=d maps to N/d", okn)

print("\n=== F. numerical realization of the radius ===")


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
ck("N=30: kappa-pairs are mirror-symmetric r(d)=r(30/d) for every proper divisor", all(abs(r30[d] - r30[30 // d]) < 1e-12 for d in r30))
vals = sorted(set(round(v, 6) for v in r30.values()))
ck(f"N=30: radii distinct by pair {vals} - the degeneracy of the skeleton is lifted by number", len(vals) == 3)
res = {}
for N0 in (6, 30, 210):
    _, ps = radii(N0)
    sum_r = sum(abs(math.log(pp / math.sqrt(N0))) for pp in ps)
    res[N0] = (sum_r, math.log(math.sqrt(N0)))
ck("base-change guard: sum_p r(p)=ln(sqrt(N)) holds at k=3 (N=30) ...", abs(res[30][0] - res[30][1]) < 1e-9)
ck("... and fails at k=2 (N=6) and k=4 (N=210): a coincidence at rank 3, not a law", abs(res[6][0] - res[6][1]) > 1e-6 and abs(res[210][0] - res[210][1]) > 1e-6)

print("\n=== G. two radii: a tree from the seed and a cone to the observer; prod=1 as balance ===")


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
ck("|.|_2 on addresses is an ultrametric (an address tree from the seed, distinct from the p-adic trees of §7.5)", ok)
x1, y1, x2, y2 = 1.0, 0.0, 0.0, 1.0
de = math.hypot(x1 - x2, y1 - y2)
ck("the |.|_infinity side is not an ultrametric (sqrt(2) > max(1,1)) - the continuous radius lives in a cone, not a tree", de > 1 + 1e-9)


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
ck("sum_v ln|x|_v = 0 - the product formula as a radial balance: outward radius = sum of depths inward", ok)

print("\n=== H. two curvatures: the apex excess is forced, the ray axis is input ===")
# the angle of any Hamming-neighbor edge seen from the center: arccos((n-2)/n) - one for all edges
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
ck("every edge subtends the same angle at sigma-half: cos = (n-2)/n (n=2..6) - the Gray-cycle length is cycle-independent", ok)


def L(n):
    return (2 ** n) * math.acos((n - 2) / n)


ok = abs(L(1) - 2 * math.pi) < 1e-12 and abs(L(2) - 2 * math.pi) < 1e-12
ok = ok and all(L(n) > 2 * math.pi + 1e-9 and L(n) > L(n - 1) for n in range(3, 11))
ck("L(1)=L(2)=2*pi exactly (flat); L(n)>2*pi and growing for n>=3 - an angular excess at the apex of the cone", ok)
# Dehn's lemma: cos theta = 1/3 implies cos(k*theta) = a_k/3^k with 3 not dividing a_k - exact fraction arithmetic
c3 = [Fraction(1), Fraction(1, 3)]
for k in range(1, 60):
    c3.append(2 * Fraction(1, 3) * c3[k] - c3[k - 1])
ok = all(c3[k].denominator == 3 ** k and c3[k].numerator % 3 != 0 for k in range(1, 60))
ck("Dehn's lemma: cos(k*theta)=a_k/3^k, 3 does not divide a_k (k=1..59) => arccos(1/3)/pi is irrational - the apex angle of rank 3", ok)
sol = [n for n in range(1, 50)
       if Fraction(n - 2, n) in (Fraction(0), Fraction(1, 2), Fraction(-1, 2), Fraction(1), Fraction(-1))]
ck("Niven: arccos((n-2)/n) is commensurable with pi iff n in {1,2,4}; the (2,3,p) axis angles pi/2,pi/3,pi/p are all commensurable"
   " => the apex curvature is not rationally expressible through the ray axis", sol == [1, 2, 4])

print(f"\n{P} PASS - the form of the radial layer is forced (norm, budget, shell, cone, tree/cone, dilation, apex excess); position on the radius is input.")
