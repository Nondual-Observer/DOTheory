#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_spin.py — ЯВНЫЙ ФУНКТОР F: 𝒟(куб Q_n, лифт Λ, κ) → 𝒫(спиновая система).
Ответ на удар рецензента «отсутствует морфизм между уровнями»: строим ОДИН явный функтор
и проверяем его НА НЕСКОЛЬКИХ ОПЕРАЦИЯХ (лифт, κ, композиция), не в одной точке совпадения.

ИСТОЧНИК 𝒟 (наша комбинаторика):
  объекты   — гиперкубы Q_n = граф на 𝔽₂ⁿ (вершины=битстроки, рёбра=Хэмминг-1);
  морфизмы  — лифт Λ: Q_n ↪ Q_{n+1}=Q_n □ K₂ (добавить ось); κ: x↦x+1ⁿ (дополнение).

ЦЕЛЬ 𝒫 (физика):
  объекты   — n спинов-½, гамильтониан A_n=∑σ_x^(i) (поперечное поле / прыжки на кубе);
  морфизмы  — добавить спин; глобальный flip X=∏σ_x.

ФУНКТОР F: Q_n ↦ (ℂ²)^⊗n с A_n=∑σ_x; Λ ↦ ⊗(добавить спин); κ ↦ X=σ_x^⊗n.
КЛЮЧ: A(Q_n) (матрица смежности гиперкуба) ТОЖДЕСТВЕННО РАВНА ∑σ_x^(i) — это не совпадение
значения, а равенство ОПЕРАТОРОВ, откуда переносится ВСЯ структура (спектр, кратности,
κ-симметрия, лифт). Проверяем функториальность: F(Λ∘Λ)=F(Λ)∘F(Λ), F(κ²)=id и т.д.

ЧЕСТНАЯ ГРАНИЦА (ответ «мост в одной точке»): образ функтора = СВОБОДНЫЕ спины (∑σ_x).
Масса/взаимодействие/кривизна требуют ВЕСОВ на рёбрах (вход, как so(4) из 1/r) — их в голом
Q_n нет. Функтор достоверен до свободной системы; дальше — открытый фронт [○].
"""
from __future__ import annotations
import numpy as np
from math import comb

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], float)
SZ = np.array([[1, 0], [0, -1]], float)

def kron_list(mats):
    out = np.array([[1.0]])
    for m in mats:
        out = np.kron(out, m)
    return out

def single(op, i, n):
    """оператор op на спине i из n (остальные — единица)."""
    return kron_list([op if j == i else I2 for j in range(n)])

def A_cube(n):
    """матрица смежности гиперкуба Q_n = ∑ σ_x^(i) (бит-флип i = ребро Хэмминга)."""
    return sum(single(SX, i, n) for i in range(n))

def hypercube_adjacency_combinatorial(n):
    """A(Q_n) построенная ЧИСТО комбинаторно (из 𝔽₂ⁿ), независимо от спинов — для сверки."""
    N = 1 << n
    A = np.zeros((N, N))
    for x in range(N):
        for i in range(n):
            A[x, x ^ (1 << i)] = 1.0
    return A


# ───────────────────────── A. спектральное соответствие ─────────────────────────
def section_A():
    print("\n[A] спектр куба Q_n = спектр свободных спинов ∑σ_x: {n−2k, кратность C(n,k)}")
    for n in range(1, 7):
        A = A_cube(n)
        Acomb = hypercube_adjacency_combinatorial(n)
        # (1) спиновый оператор ТОЖДЕСТВЕННО = комбинаторная матрица смежности куба
        same_operator = np.allclose(A, Acomb)
        # (2) спектр = {n−2k} с кратностями C(n,k) — ВСЯ структура, не одно число
        ev = np.round(np.linalg.eigvalsh(A)).astype(int)
        from collections import Counter
        got = Counter(ev.tolist())
        want = Counter({n - 2 * k: comb(n, k) for k in range(n + 1)})
        check(f"n={n}: A(Q_n) ≡ ∑σ_x (равенство ОПЕРАТОРОВ) и спектр={{n−2k, C(n,k)}}",
              same_operator and got == want,
              extra=f"got={dict(got)} want={dict(want)}")


# ───────────────────────── B. функториальность лифта ─────────────────────────
def section_B():
    print("\n[B] лифт Λ: Q_n→Q_{n+1}=Q_n□K₂  ↦  добавить спин (A_{n+1}=A_n⊗I+I⊗σ_x)")
    for n in range(1, 6):
        An = A_cube(n)
        An1_direct = A_cube(n + 1)
        An1_lift = np.kron(An, I2) + np.kron(np.eye(1 << n), SX)
        check(f"n={n}→{n+1}: F(Λ) = добавить спин (тождество операторов)",
              np.allclose(An1_direct, An1_lift))
        # спектр лифтится λ → λ±1 (каждое собств. значение расщепляется)
        sp_n = np.round(np.linalg.eigvalsh(An)).astype(int)
        sp_n1 = sorted(np.round(np.linalg.eigvalsh(An1_direct)).astype(int).tolist())
        want = sorted([v + s for v in sp_n for s in (+1, -1)])
        check(f"n={n}→{n+1}: спектр лифтится λ↦λ±1 (структура, не точка)", sp_n1 == want)

def section_B_composition():
    print("\n[B′] КОМПОЗИЦИЯ функтора: F(Λ∘Λ) = F(Λ)∘F(Λ) (два лифта = два спина)")
    for n in range(1, 5):
        An = A_cube(n)
        # два лифта подряд
        step1 = np.kron(An, I2) + np.kron(np.eye(1 << n), SX)
        step2 = np.kron(step1, I2) + np.kron(np.eye(1 << (n + 1)), SX)
        direct = A_cube(n + 2)
        check(f"n={n}: F(Λ²)=F(Λ)∘F(Λ) — функториальность композиции", np.allclose(step2, direct))


# ───────────────────────── C. κ-дополнение = глобальный flip ─────────────────────────
def section_C():
    print("\n[C] κ: x↦x+1ⁿ (дополнение)  ↦  X=σ_x^⊗n (глобальный flip);  κ²=id, [A,κ]=0")
    for n in range(1, 6):
        A = A_cube(n)
        X = kron_list([SX] * n)
        # κ реализует антипод x↦x+1ⁿ: проверяем перестановку базиса
        N = 1 << n
        perm_ok = all(abs(X[(x ^ (N - 1)), x] - 1.0) < 1e-12 for x in range(N))
        check(f"n={n}: F(κ)=X реализует антипод x↦x+1ⁿ", perm_ok)
        check(f"n={n}: F(κ²)=F(id)=I (инволюция)", np.allclose(X @ X, np.eye(N)))
        check(f"n={n}: [A,κ]=0 — дополнение коммутирует (сохраняет уровни)",
              np.allclose(A @ X, X @ A))


# ───────────────────────── D. киральная κ = частица/дырка ─────────────────────────
def section_D():
    print("\n[D] киральная инволюция Z=σ_z^⊗n (чётность веса): {A,Z}=0 ⟹ спектр λ↔−λ")
    for n in range(1, 6):
        A = A_cube(n)
        Z = kron_list([SZ] * n)
        anti = np.allclose(A @ Z + Z @ A, 0)
        ev = sorted(np.round(np.linalg.eigvalsh(A)).astype(int).tolist())
        symm = ev == sorted([-v for v in ev])
        check(f"n={n}: {{A,Z}}=0 (двудольность=частица/дырка) ⟹ спектр ±λ", anti and symm)


# ───────────────────────── E. σ½ как спектральный центр ─────────────────────────
def section_E():
    print("\n[E] σ½ = серединный страт k=n/2: макс. вырождение C(n,n/2), безмассовый центр")
    for n in (2, 4, 6):
        A = A_cube(n)
        ev = np.round(np.linalg.eigvalsh(A)).astype(int)
        from collections import Counter
        c = Counter(ev.tolist())
        mid_deg = c[0]                     # eigenvalue 0 = середина k=n/2
        check(f"n={n}: середина λ=0 имеет МАКС кратность C(n,n/2)={comb(n, n//2)}",
              mid_deg == comb(n, n // 2) and mid_deg == max(c.values()))
    print("   → центр спектра (λ=0, k=n/2) = σ½ = κ-фикс среднего слоя = безмассовая середина")


# ───────────────────────── F. честная граница функтора ─────────────────────────
def section_F():
    print("\n[F] ГРАНИЦА: голый Q_n → СВОБОДНЫЕ спины; масса требует ВЕСА (вход), не из куба")
    n = 4
    A = A_cube(n)
    ev = np.round(np.linalg.eigvalsh(A)).astype(int)
    # голый куб вершинно-транзитивен ⟹ середина вырождена ⟹ НЕТ массовой щели
    gap_bare = sorted(set(ev.tolist()))
    has_zero = 0 in gap_bare
    check("голый Q_n: середина λ=0 присутствует (безмассовый, нет щели) — свободная система",
          has_zero)
    # ВВЕДЁМ вес-разбаланс на одной оси (κ-слом, док 88): щель открывается, но вес g — ВХОД
    g = 0.7
    A_weighted = sum((1.0 if i > 0 else 1.0 + g) * single(SX, i, n) for i in range(n))
    ev_w = np.linalg.eigvalsh(A_weighted)
    # проверяем, что разбаланс СДВИГАЕТ структуру (вес — свободный параметр, не из Q_n)
    moved = not np.allclose(sorted(ev.tolist()), sorted(np.round(ev_w).astype(int).tolist()))
    check("ВЗВЕШЕННЫЙ куб (κ-слом, вес g=ВХОД): структура сдвигается — масса требует входа",
          moved)
    print("   → функтор ДОСТОВЕРЕН до свободных спинов (∑σ_x); масса/взаимодействие/кривизна")
    print("     = веса на рёбрах = ВХОД (как so(4) из 1/r) ⟹ мост построен В ОДНОЙ ТОЧКЕ [○]")


def main():
    print("=" * 74)
    print("ЯВНЫЙ ФУНКТОР F: 𝒟(Q_n, Λ, κ) → 𝒫(спиновая система ∑σ_x)")
    print("проверка функториальности на ОПЕРАЦИЯХ (лифт/κ/композиция), не в точке")
    print("=" * 74)
    section_A(); section_B(); section_B_composition()
    section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 74)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: морфизм СУЩЕСТВУЕТ явно (Q_n ↦ свободные спины), функториален на 4 операциях;")
    print("       НО образ = свободная система; богатая физика = веса-вход = открытый фронт [○].")
    print("=" * 74)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
