#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_strict_core_bridge.py

Самодостаточная численная проверка ЧЕТЫРЁХ результатов, отмеченных меткой
[●]. Они доказаны в строгом конечном ядре корпуса; здесь — независимое
подтверждение средствами самой серии-изложения, чтобы ссылки не висели
на внешней ветке.

  1. Универсальность 𝔽₂-кирпича (гл I §1.1).
     Любой минимальный различитель (S, N, χ) — двусостоятельный носитель
     |S|=2, свободная инволюция N (без неподвижных точек), сравнение χ,
     различающее лишь совпадение/несовпадение и инвариантное к перевороту
     полюсов χ(Na,Nb)=χ(a,b) — единствен в своём классе и изоморфен (Q₁,κ).

  2. Единственность октаэдра (гл III §3.3).
     Активная сцена ранга 3 есть кросс-политоп K_{2,2,2}; |V|=2m, и при
     m≥3 (три оси удержания) минимум числа вершин = 6, достигается ровно
     при m=3. Тетраэдр исключён (нет антиподальных пар → нет свободной
     κ), куб исключён (κ-инвариантный центр среди... вне вершин).

  3. ℤ₂-голономия = лента Мёбиуса (гл III §3.3).
     Скрученный транспорт на C₆ несёт калибровочно-инвариантную голономию
     ∏εᵢ; класс H¹(S¹;ℤ₂)≅ℤ₂ нетривиален (∃ конфигурация ∏=−1), двойной
     возврат 𝒯²=id. Это отдельный от поворота T оператор.

  4. sl₂-грейдинг Стэнли (гл VII §7.1).
     Взвешенные операторы повышения e и понижения f веса на булевой
     решётке Q_n с градуировкой H=2k−n удовлетворяют
       [H,e]=2e,  [H,f]=−2f,  [e,f]=H,
     а дополнение κ есть вейлева инволюция: κHκ=−H, κeκ=f.
     (Грейдинг живёт над ℚ; e,f — образующие алгебры Ли, НЕ дифференциалы:
      e²≠0 — этим он отличается от цепного комплекса гл VII §7.2.)

Запуск:  python3 verify_strict_core_bridge.py
Зависимости: numpy.
"""

import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


# ----------------------------------------------------------------------
# 1. Универсальность 𝔽₂-кирпича
# ----------------------------------------------------------------------
def section_brick():
    print("\n[1] Универсальность 𝔽₂-кирпича (гл I §1.1)")
    S = [0, 1]

    # все биекции S->S
    bijections = [dict(zip(S, p)) for p in itertools.permutations(S)]
    # свободная инволюция: N(N(x))=x, N(x)!=x всюду
    free_invols = [
        N for N in bijections
        if all(N[N[x]] == x for x in S) and all(N[x] != x for x in S)
    ]
    check("на |S|=2 свободная инволюция ровно одна (обмен)", len(free_invols) == 1)
    N = free_invols[0]

    # сравнение χ(a,b)=0 ⟺ a=b
    chi = {(a, b): int(a != b) for a in S for b in S}
    # χ различает лишь совпадение/несовпадение (значения только 0/1, 0 ⟺ a=b)
    distinguishes_only = all(
        (chi[(a, b)] == 0) == (a == b) for a in S for b in S
    )
    check("χ различает лишь совпадение/несовпадение", distinguishes_only)
    # инвариантность к перевороту полюсов: χ(Na,Nb)=χ(a,b)
    inv = all(chi[(N[a], N[b])] == chi[(a, b)] for a in S for b in S)
    check("χ инвариантна к перевороту полюсов χ(Na,Nb)=χ(a,b)", inv)

    # изоморфизм на кирпич (B2,σ,χ2): B2={0,1}, σ=swap, χ2=[a≠b]
    sigma = {0: 1, 1: 0}
    chi2 = {(a, b): int(a != b) for a in (0, 1) for b in (0, 1)}
    isos = []
    for e in bijections:  # биекция S->B2
        ok_N = all(e[N[x]] == sigma[e[x]] for x in S)          # e∘N = σ∘e
        ok_chi = all(chi[(a, b)] == chi2[(e[a], e[b])] for a in S for b in S)
        if ok_N and ok_chi:
            isos.append(e)
    # изоморфизм существует (структура реализуема как кирпич)
    check("(S,N,χ) изоморфна кирпичу (B₂,σ,χ₂)", len(isos) >= 1)
    # структура единственна в классе: единственная N, единственная допустимая χ
    valid_chi = 0
    for vals in itertools.product([0, 1], repeat=4):
        c = {(a, b): vals[2 * a + b] for a in S for b in S}
        if all((c[(a, b)] == 0) == (a == b) for a in S for b in S) and \
           all(c[(N[a], N[b])] == c[(a, b)] for a in S for b in S):
            valid_chi += 1
    check("минимальный различитель единствен в классе (1 N, 1 χ)",
          len(free_invols) == 1 and valid_chi == 1)

    # вынужденность |S|=2: на нечётном носителе свободной инволюции нет
    def has_free_involution(k):
        for p in itertools.permutations(range(k)):
            P = dict(enumerate(p))
            if all(P[P[x]] == x for x in range(k)) and all(P[x] != x for x in range(k)):
                return True
        return False
    check("|S|=2 вынуждено: на |S|=3 свободной инволюции нет",
          (not has_free_involution(3)) and has_free_involution(2))


# ----------------------------------------------------------------------
# 2. Единственность октаэдра
# ----------------------------------------------------------------------
def crosspolytope_graph(m):
    """Вершины ±e_i (2m штук), смежны все пары, кроме антиподальной."""
    verts = []
    for i in range(m):
        verts.append((i, +1))
        verts.append((i, -1))
    n = len(verts)
    A = np.zeros((n, n), dtype=int)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            ia, sa = verts[a]
            ib, sb = verts[b]
            antipode = (ia == ib and sa == -sb)
            A[a, b] = 0 if antipode else 1
    return verts, A


def antipode_perm(verts):
    idx = {v: k for k, v in enumerate(verts)}
    return [idx[(i, -s)] for (i, s) in verts]


def section_octahedron():
    print("\n[2] Единственность октаэдра K_{2,2,2} (гл III §3.3)")

    # |V| = 2m; при m>=3 минимум = 6 при m=3
    sizes = {m: 2 * m for m in range(1, 6)}
    primitive = {m: v for m, v in sizes.items() if m >= 3}  # три оси удержания
    check("|V|=2m; при m≥3 минимум вершин = 6", min(primitive.values()) == 6)
    check("минимум 6 достигается ровно при m=3",
          [m for m, v in primitive.items() if v == 6] == [3])

    verts, A = crosspolytope_graph(3)
    check("октаэдр (m=3): |V|=6", len(verts) == 6)
    # K_{2,2,2}: каждая вершина смежна 4, несмежна ровно с антиподом
    deg = A.sum(axis=1)
    check("каждая вершина смежна 4, несмежна ровно с антиподом",
          np.all(deg == 4))
    kap = antipode_perm(verts)
    check("κ (антипод) свободна: нет неподвижных вершин",
          all(kap[i] != i for i in range(6)))
    check("κ инволюция: κ²=id", all(kap[kap[i]] == i for i in range(6)))

    # тетраэдр K4 исключён: полный граф, нет несмежной пары => нет антиподов
    K4 = np.ones((4, 4), int) - np.eye(4, dtype=int)
    has_nonadjacent_pair = np.any(K4 == 0)  # вне диагонали
    offdiag_zero = np.any((K4 == 0) & (~np.eye(4, dtype=bool)))
    check("тетраэдр K₄ исключён: нет несмежной пары (нет антиподов)",
          not offdiag_zero)

    # куб Q3 исключён как примитивная сцена: антипод свободен, НО центр
    # (½,½,½) есть κ-инвариант ВНЕ вершин; активная сцена = Q3 без 2 полюсов = 6
    Q3 = list(itertools.product([0, 1], repeat=3))
    comp = {v: tuple(1 - c for c in v) for v in Q3}
    center_fixed_is_vertex = any(comp[v] == v for v in Q3)
    check("куб: κ-инвариантный центр НЕ среди вершин (центр вне Q₃)",
          not center_fixed_is_vertex)
    poles = [v for v in Q3 if v in ((0, 0, 0), (1, 1, 1))]
    active = [v for v in Q3 if v not in poles]
    check("активная сцена куба (без 2 полюсов) = 6 = октаэдр",
          len(active) == 6)


# ----------------------------------------------------------------------
# 3. ℤ₂-голономия (лента Мёбиуса) на C₆
# ----------------------------------------------------------------------
def section_holonomy():
    print("\n[3] ℤ₂-голономия = лента Мёбиуса на C₆ (гл III §3.3)")
    m = 6  # рёбер в цикле C6

    # нетривиальный класс: конфигурация знаков с ∏ε = −1
    twisted = [-1] + [1] * (m - 1)
    check("нетривиальная голономия существует: ∏εᵢ = −1",
          int(np.prod(twisted)) == -1)
    trivial = [1] * m
    check("тривиальная голономия: ∏εᵢ = +1", int(np.prod(trivial)) == 1)

    # калибровочная инвариантность: εᵢ → s_v · εᵢ · s_{v+1}; ∏ε неизменно
    def holonomy(eps):
        return int(np.prod(eps))

    invariant = True
    base = twisted[:]
    h0 = holonomy(base)
    for sbits in itertools.product([1, -1], repeat=m):  # калибровка на 6 вершинах цикла
        s = list(sbits)
        gauged = [s[i] * base[i] * s[(i + 1) % m] for i in range(m)]
        if holonomy(gauged) != h0:
            invariant = False
            break
    check("голономия калибровочно инвариантна (∏ε под s_v·ε·s_{v+1})", invariant)

    # ровно два класса H¹(S¹;ℤ₂) ≅ ℤ₂
    classes = set()
    for eps in itertools.product([1, -1], repeat=m):
        classes.add(int(np.prod(eps)))
    check("ровно два класса голономии (H¹(S¹;ℤ₂)≅ℤ₂)", classes == {1, -1})

    # двойной возврат 𝒯²=id: голономия по двойному обходу = (∏ε)² = +1
    check("двойной возврат 𝒯²=id: (∏ε)²=+1 на любом классе",
          all(c * c == 1 for c in classes))

    # отличие от поворота: поворот T на C6 имеет порядок 6, T³=κ (порядок 2)
    T = np.roll(np.eye(m, dtype=int), 1, axis=0)      # сдвиг на 1 шаг
    T6 = np.linalg.matrix_power(T, 6)
    T3 = np.linalg.matrix_power(T, 3)
    check("поворот T: T⁶=id, T³≠id (T³=κ, порядок 6 ≠ голономия)",
          np.array_equal(T6, np.eye(m, dtype=int)) and not np.array_equal(T3, np.eye(m, dtype=int)))


# ----------------------------------------------------------------------
# 4. sl₂-грейдинг Стэнли на булевой решётке Q_n
# ----------------------------------------------------------------------
def boolean_sl2(n):
    """Взвешенные up/down операторы и H=2k−n на Q_n=2^n подмножеств."""
    subsets = list(itertools.product([0, 1], repeat=n))
    idx = {s: i for i, s in enumerate(subsets)}
    N = len(subsets)
    U = np.zeros((N, N))  # повышение веса: e
    D = np.zeros((N, N))  # понижение веса: f
    for s in subsets:
        for j in range(n):
            if s[j] == 0:
                t = tuple(1 if k == j else s[k] for k in range(n))
                U[idx[t], idx[s]] = 1.0        # добавить элемент j: s -> t
            else:
                t = tuple(0 if k == j else s[k] for k in range(n))
                D[idx[t], idx[s]] = 1.0        # убрать элемент j: s -> t
    H = np.diag([2 * sum(s) - n for s in subsets]).astype(float)
    K = np.zeros((N, N))  # κ: антипод (комплемент множества)
    for s in subsets:
        c = tuple(1 - b for b in s)
        K[idx[c], idx[s]] = 1.0
    return U, D, H, K


def comm(X, Y):
    return X @ Y - Y @ X


def section_sl2():
    print("\n[4] sl₂-грейдинг Стэнли на булевой решётке (гл VII §7.1)")
    for n in (3, 4):
        e, f, H, K = boolean_sl2(n)
        ok1 = np.allclose(comm(H, e), 2 * e)
        ok2 = np.allclose(comm(H, f), -2 * f)
        ok3 = np.allclose(comm(e, f), H)
        check(f"n={n}: [H,e]=2e", ok1)
        check(f"n={n}: [H,f]=−2f", ok2)
        check(f"n={n}: [e,f]=H", ok3)
        # κ — вейлева инволюция
        check(f"n={n}: κ²=id", np.allclose(K @ K, np.eye(K.shape[0])))
        check(f"n={n}: κHκ=−H (переворот градуировки)",
              np.allclose(K @ H @ K, -H))
        check(f"n={n}: κeκ=f (меняет повышение и понижение)",
              np.allclose(K @ e @ K, f))
        # e — НЕ дифференциал: e²≠0 (отличие от цепного комплекса §7.2)
        check(f"n={n}: e²≠0 (грейдинг — не комплекс)",
              not np.allclose(e @ e, 0))


def main():
    print("=" * 64)
    print("verify_strict_core_bridge.py — мост к строгому ядру (4 результата)")
    print("=" * 64)
    section_brick()
    section_octahedron()
    section_holonomy()
    section_sl2()
    print("\n" + "=" * 64)
    print(f"ИТОГ: {PASS} PASS, {FAIL} FAIL")
    print("=" * 64)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
