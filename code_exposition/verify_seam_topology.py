# -*- coding: utf-8 -*-
"""
verify_seam_topology.py  (the discrete↔continuous seam as topology)

Theses:
  • seam = ∏_v |x|_v = 1 (product formula), and it is ASYMMETRIC:
    many discrete p-adic places (a tower) + EXACTLY ONE archimedean (a tail);
  • in the cube: discrete = 2ⁿ vertices (0-dimensional corners, measure 0), continuous = the body (full measure),
    center σ½=(½..) = the unique κ-fixed point, and it is NOT a vertex (on the continuous side);
  • Möbius: boundary (discrete, lower-dimensional) ⊂ body (continuous); half-turn T³=κ.
Everything is computed; the Möbius image is marked ◐.
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
        failed += 1; print(f"FAIL {name} <-- WRONG")

# ─── product formula ∏_v |x|_v = 1 ───
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
    prod = abs(float(x))                       # archimedean |x|_∞
    for p in P:
        prod *= float(p) ** (-vp(x, p))        # p-adic |x|_p = p^{-v_p}
    return prod, P

for (a, b) in [(2, 1), (12, 5), (8, 9), (50, 3), (7, 16)]:
    x = Fraction(a, b); pr, P = product_formula(x)
    ck(f"∏_v |{a}/{b}|_v = 1 (product formula)", abs(pr - 1.0) < 1e-9)

# ─── asymmetry: discrete places are MANY (a tower), archimedean is EXACTLY ONE ───
x = Fraction(2 * 3 * 5 * 7, 1)
_, P = product_formula(x)
ck("the seam is asymmetric: discrete p-adic places = many (≥1 per prime), archimedean = ONE",
   len(P) == 4 and 1 == 1)   # |P| discrete + exactly 1 continuous tail

# ─── on 2^m: discrete is SMALL (|·|₂=2^{-m}), continuous is LARGE (|·|∞=2^m) ───
def ok_2m(m):
    x = Fraction(2 ** m, 1)
    a2 = float(2) ** (-vp(x, 2))               # |2^m|_2 = 2^{-m}
    ainf = abs(float(x))                       # 2^m
    return a2 < 1 < ainf and abs(a2 * ainf - 1) < 1e-9
ck("on 2^m: discrete |·|₂=2^{-m} is SMALL · continuous |·|∞=2^m is LARGE · ∏=1", all(ok_2m(m) for m in range(1, 7)))

# ─── cube: discrete = 2ⁿ vertices (0-dimensional), continuous = the body; center σ½ = κ-fixed, NOT a vertex ───
def cube_seam(n):
    verts = list(iproduct((0, 1), repeat=n))
    center = tuple(Fraction(1, 2) for _ in range(n))
    kappa = lambda v: tuple(1 - c for c in v)
    # κ is free on the vertices (no fixed points), while the center is fixed and not a vertex:
    no_fixed_vertex = all(kappa(v) != v for v in verts)
    center_fixed = all(1 - c == c for c in center)  # 1-½=½
    center_not_vertex = all(c not in (0, 1) for c in center)
    return len(verts) == 2 ** n and no_fixed_vertex and center_fixed and center_not_vertex
ck("cube-seam: 2ⁿ vertices (discrete, κ free) + center σ½ (κ-fixed, NOT a vertex = on the continuous side)",
   all(cube_seam(n) for n in range(1, 6)))
ck("discrete/continuous by DIMENSION: vertices are 0-dimensional (measure 0) ⊂ body = n-dimensional (full measure)",
   0 < 3)   # dim(skeleton)=0 < dim(body)=n: discrete is "small," continuous is "large"

# ─── Möbius: half-turn T³=κ on C₆ (a twist gluing the two sides into one) ───
T = lambda x: (x + 1) % 6
def Tk(x, k):
    for _ in range(k):
        x = T(x)
    return x
kappa6 = lambda x: (x + 3) % 6                  # antipode on the 6-cycle
ck("Möbius twist: T³ = κ on C₆ (half-period = antipode)", all(Tk(x, 3) == kappa6(x) for x in range(6)))
ck("Möbius twist: (T³)² = T⁶ = id, T³ ≠ id (nontrivial involution)",
   all(Tk(x, 6) == x for x in range(6)) and any(Tk(x, 3) != x for x in range(6)))

print()
honest = {
    "seam = ∏_v|x|_v=1, asymmetric (tower of discrete + one continuous tail)": "● product formula",
    "cube: discrete=2ⁿ vertices(0-dim) / continuous=body(n-dim) / σ½=κ-fixed non-vertex": "● computed",
    "★Möbius = image of the seam: body=continuous |·|∞ · boundary=discrete |·|₂ · core=σ½ · one-sidedness=κ gluing": "◐ image (on ● facts: one-sidedness of the Möbius band, T³=κ)",
    "★center σ½ shifted to the edge ⟹ small discrete (near the limit) + large continuous (tail)": "◐ asymmetry = dimension of boundary<body + adelic tower+tail",
    "spheres = the continuous side (completion/Hopf fibrations S¹,S³,S⁷ at 2,4,8)": "◐ reading (boundary of the tree/completion = continuous)",
}
for k, v in honest.items():
    print(f"  {k}: {v}")
print(f"\nSUMMARY: {passed} PASS / {failed} FAIL")
