#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_layers.py — недостающие функториальные слои дискретной части
(сверх костяка роста в Core/Fronts). Чистая комбинаторика/алгебра, без физики.

A. κ как ДВОЙСТВЕННОСТЬ булевой решётки — контравариантный инволютивный функтор
   (де Морган κ(a∧b)=κ(a)∨κ(b), обращение порядка, κ²=id). [гл. II]
B. ЦЕПНОЙ КОМПЛЕКС над 𝔽₂ — ∂²=0=δ², κ=ЗВЕЗДА ХОДЖА (κ∂=δκ), приведённая
   ацикличность, ЛИФТ=СУСПЕНЗИЯ (конус). [гл. VIII §8.2 — вторая структура]
C. ЛИФТ МОНОИДАЛЕН — Q_{m+n}=Q_m□Q_n, κ покоординатно; разрыв 4=2×2. [гл. IV]
D. ГОЛОНОМИЯ — T³=κ на C₆; C₆→C₆/κ=C₃ связный двойной накрыватель (нетрив. H¹). [гл. III]
E. ЦИКЛ ЗИНГЕРА — порядок 2ⁿ⁻¹−1; несоизмеримость gcd(2ⁿ⁻¹−1,2ⁿ−1)=1. [гл. III]
"""
from __future__ import annotations
import numpy as np
from math import comb, gcd

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def popcount(x): return bin(x).count("1")
def M(n): return (1 << n) - 1

def rank_gf2(A):
    A = (np.array(A) % 2).astype(int).copy()
    rows, cols = A.shape; r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        for i in range(rows):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
        if r == rows: break
    return r


# ═══════════════ A. κ-двойственность (контравариантный функтор) ═══════════════
def section_A():
    print("\n[A] κ = ДВОЙСТВЕННОСТЬ булевой решётки (де Морган, обращение порядка) [гл.II]")
    for n in range(1, 6):
        m = M(n)
        dm = order = inv = True
        for a in range(1 << n):
            if (a ^ m) ^ m != a: inv = False                       # κ²=id
            for b in range(1 << n):
                if ((a & b) ^ m) != ((a ^ m) | (b ^ m)): dm = False  # κ(a∧b)=κa∨κb
                le = (a & b) == a                                   # a≤b
                ge = ((a ^ m) & (b ^ m)) == (b ^ m)                 # κa≥κb
                if le != ge: order = False
        check(f"n={n}: де Морган κ(a∧b)=κa∨κb, обращение порядка a≤b⟺κa≥κb, κ²=id",
              dm and order and inv)
    print("   → κ — контравариантный инволютивный эндофунктор (антиавтоморфизм решётки)")


# ═══════════════ B. цепной комплекс, Ходж, суспензия ═══════════════
def boundary(n):
    """∂: убрать единицу. ∂[y,x]=1 если y=x∖{i}, i∈x (над 𝔽₂)."""
    N = 1 << n; B = np.zeros((N, N), int)
    for x in range(N):
        for i in range(n):
            if (x >> i) & 1:
                B[x ^ (1 << i), x] = 1
    return B

def coboundary(n):
    N = 1 << n; D = np.zeros((N, N), int)
    for x in range(N):
        for i in range(n):
            if not (x >> i) & 1:
                D[x | (1 << i), x] = 1
    return D

def kappa_mat(n):
    N = 1 << n; K = np.zeros((N, N), int)
    for x in range(N): K[x ^ M(n), x] = 1
    return K

def section_B():
    print("\n[B] ЦЕПНОЙ КОМПЛЕКС над 𝔽₂: ∂²=0, κ=звезда Ходжа (κ∂=δκ), ацикличность [гл.VIII]")
    for n in range(1, 6):
        Bd, Dl, K = boundary(n), coboundary(n), kappa_mat(n)
        d2 = np.all((Bd @ Bd) % 2 == 0)
        c2 = np.all((Dl @ Dl) % 2 == 0)
        hodge = np.all((K @ Bd) % 2 == (Dl @ K) % 2)               # κ∂=δκ — звезда Ходжа
        check(f"n={n}: ∂²=0, δ²=0 над 𝔽₂; κ∂=δκ (κ=ЗВЕЗДА ХОДЖА)", d2 and c2 and hodge)
        # приведённая ацикличность: все H_k=0 (ранги mod 2) и Эйлер Σ(−1)ᵏC(n,k)=0
        # H_k = dim C_k − rank∂_k − rank∂_{k+1}; ∂_k = часть ∂ со слоя k → k−1
        N = 1 << n
        lvl = [[x for x in range(N) if popcount(x) == k] for k in range(n + 1)]
        homol_ok = True
        for k in range(n + 1):
            # ∂_k: C_k→C_{k-1}; rank
            if k == 0:
                rk = 0
            else:
                sub = Bd[np.ix_(lvl[k - 1], lvl[k])] if lvl[k - 1] and lvl[k] else np.zeros((1, 1), int)
                rk = rank_gf2(sub)
            if k == n:
                rk1 = 0
            else:
                sub1 = Bd[np.ix_(lvl[k], lvl[k + 1])] if lvl[k] and lvl[k + 1] else np.zeros((1, 1), int)
                rk1 = rank_gf2(sub1)
            Hk = len(lvl[k]) - rk - rk1
            if Hk != 0: homol_ok = False
        euler = sum((-1) ** k * comb(n, k) for k in range(n + 1))
        check(f"n={n}: приведённо АЦИКЛИЧЕН (все H_k=0) и Эйлер Σ(−1)ᵏC(n,k)={euler}=0",
              homol_ok and euler == 0)

    # ЛИФТ = СУСПЕНЗИЯ (конус): ∂_{n+1} = [[∂_n, Id],[0, ∂_n]] в базисе (бит n =0)⊕(бит n =1)
    print("   лифт = СУСПЕНЗИЯ (конус): ∂_{n+1} = блочный конус над ∂_n")
    for n in range(1, 5):
        Bn, Bn1 = boundary(n), boundary(n + 1)
        N = 1 << n
        B0 = list(range(N))                       # бит n = 0  (база Q_n)
        B1 = [x | (1 << n) for x in range(N)]      # бит n = 1
        order = B0 + B1
        reordered = Bn1[np.ix_(order, order)] % 2
        # ожидаемый конус: [[Bn, I],[0, Bn]]
        cone = np.block([[Bn % 2, np.eye(N, dtype=int)],
                         [np.zeros((N, N), int), Bn % 2]]) % 2
        check(f"n={n}→{n+1}: ∂_{{{n+1}}} = конус [[∂_n, I],[0, ∂_n]] (лифт=суспензия)",
              np.array_equal(reordered, cone))


# ═══════════════ C. моноидальность лифта ═══════════════
def section_C():
    print("\n[C] ЛИФТ МОНОИДАЛЕН: Q_{m+n}=Q_m□Q_n, κ покоординатно; разрыв 4=2×2 [гл.IV]")
    def adj(n):
        N = 1 << n; A = np.zeros((N, N), int)
        for x in range(N):
            for i in range(n): A[x ^ (1 << i), x] = 1
        return A
    for (m, n) in [(1, 1), (1, 2), (2, 2), (2, 3)]:
        Amn = adj(m + n)
        # Q_{m+n} = Q_m □ Q_n: A = A_m⊗I + I⊗A_n
        box = np.kron(adj(m), np.eye(1 << n, dtype=int)) + np.kron(np.eye(1 << m, dtype=int), adj(n))
        # κ покоординатно: κ_{m+n} = κ_m ⊗ κ_n
        kmn = kappa_mat(m + n)
        kbox = np.kron(kappa_mat(m), kappa_mat(n))
        check(f"Q_{{{m+n}}} = Q_{m}□Q_{n} (A=A_m⊗I+I⊗A_n) и κ=κ_m⊗κ_n",
              np.array_equal(Amn, box) and np.array_equal(kmn, kbox))
    print("   → разрыв 4=2×2: Q₄=Q₂□Q₂, лифт — моноидальный функтор (□, K₂)")


# ═══════════════ D. голономия (Мёбиус) ═══════════════
def section_D():
    print("\n[D] ГОЛОНОМИЯ: T³=κ на C₆; C₆→C₆/κ=C₃ связный двойной накрыватель [гл.III]")
    # C₆ = хэмминг-1 цикл на U₃
    cyc = [0b001, 0b011, 0b010, 0b110, 0b100, 0b101]   # каждый шаг — флип одного бита
    # проверка что это цикл по Хэммингу-1
    is_cycle = all(popcount(cyc[i] ^ cyc[(i + 1) % 6]) == 1 for i in range(6))
    T = {cyc[i]: cyc[(i + 1) % 6] for i in range(6)}    # сдвиг
    def T3(x):
        for _ in range(3): x = T[x]
        return x
    t3_is_kappa = all(T3(x) == x ^ 0b111 for x in cyc)  # T³ = κ (антипод)
    check("C₆ — хэмминг-1 цикл; T³=κ (полуоборот = дополнение)", is_cycle and t3_is_kappa)
    # C₆/κ: 3 κ-пары; накрыватель связен ⟺ C₆ — ОДИН цикл (не два треугольника)
    pairs = {frozenset((x, x ^ 0b111)) for x in cyc}
    connected = (len(pairs) == 3)                       # 3 пары = C₃ внизу; C₆ связен сверху
    check("C₆/κ = C₃ (3 пары), накрыватель СВЯЗЕН ⟹ нетрив. класс H¹(S¹;ℤ₂)=ℤ₂ (Мёбиус)",
          connected)


# ═══════════════ E. цикл Зингера / несоизмеримость ═══════════════
def section_E():
    print("\n[E] ЦИКЛ ЗИНГЕРА на PG(n−2,2): порядок 2ⁿ⁻¹−1; несоизмеримость соседей [гл.III]")
    for n in range(2, 8):
        singer = (1 << (n - 1)) - 1                     # |PG(n-2,2)| = 2^{n-1}−1
        # несоизмеримость: gcd(порядок этажа n, порядок этажа n+1)=1
        g = gcd((1 << (n - 1)) - 1, (1 << n) - 1)
        check(f"n={n}: цикл Зингера порядка {singer}; gcd(2ⁿ⁻¹−1,2ⁿ−1)={g}=1 (несоизмеримы)",
              g == 1)
    print("   → вращения соседних рангов взаимно просты (2ⁿ−1=2(2ⁿ⁻¹−1)+1): винт не замыкается")


def main():
    print("=" * 78)
    print("НЕДОСТАЮЩИЕ ФУНКТОРИАЛЬНЫЕ СЛОИ дискретной части (сверх костяка роста)")
    print("=" * 78)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 78)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ДОБАВЛЕНО: κ-двойственность (контравар.функтор); цепной комплекс ∂/δ + κ=Ходж +")
    print("          лифт=суспензия; моноидальность лифта; голономия (Мёбиус); цикл Зингера.")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
