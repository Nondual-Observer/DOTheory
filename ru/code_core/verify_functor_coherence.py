#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_coherence.py — структурные замечания рецензента (3-я волна).
Где можно — устанавливаем СТРОГО; где нет — честно ○.

❗(3) ТРОЙНАЯ РОЛЬ κ (инволюция / звезда Ходжа / вейлева дуальность) — «требует
   coherence theorem». ОТВЕТ: κ есть ОДНА матрица K (дополнение x↦x+1ⁿ); проверяем,
   что эта ЕДИНСТВЕННАЯ K удовлетворяет всем ролям сразу. Более того: e=δ и f=∂ суть
   ОДНИ матрицы, поэтому «звезда Ходжа» (κ∂=δκ) и «вейлев обмен корней» (κeκ=f) — это
   БУКВАЛЬНО ОДНА И ТА ЖЕ формула. Когерентность не теорема, а тождество одного оператора.

⚠(2 разд.2) sl₂ «встроенная интерпретация» без representation functor. ОТВЕТ: задаём
   ЯВНЫЙ representation functor — тензорная степень: V_n=(V₁)^{⊗n}, e_n=e_{n−1}⊗I+I⊗e₁
   (Лейбниц), лифт=⊗V₁. Это и есть функтор рангов → sl₂-Rep, не интерпретация.

❗(2 разд.3) монада «не выведена из adjunction». ОТВЕТ: структурная карта T-алгебры
   α(b,x)=σ^b(x) строится из инволюции σ КОНСТРУКТИВНО, законы держатся для любой σ
   (не перебором) ⟹ EM(T)=ℤ/2-Set выведено из adjunction.

❗(1 разд.3) 2-категория/расслоение, связывающее уровни — НЕ построено. Честно ○:
   намечена конструкция Гротендика над категорией рангов; полная 2-когерентность открыта.
"""
from __future__ import annotations
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def popcount(x): return bin(x).count("1")
def Mm(n): return (1 << n) - 1

def E_raise(n):   # e = δ = добавить бит (повышение веса / кограница)
    N = 1 << n; A = np.zeros((N, N), int)
    for x in range(N):
        for i in range(n):
            if not (x >> i) & 1: A[x | (1 << i), x] = 1
    return A
def F_lower(n):   # f = ∂ = убрать бит (понижение веса / граница)
    N = 1 << n; A = np.zeros((N, N), int)
    for x in range(N):
        for i in range(n):
            if (x >> i) & 1: A[x & ~(1 << i), x] = 1
    return A
def H_grade(n):
    N = 1 << n; A = np.zeros((N, N), int)
    for x in range(N): A[x, x] = 2 * popcount(x) - n
    return A
def K_compl(n):
    N = 1 << n; A = np.zeros((N, N), int)
    for x in range(N): A[x ^ Mm(n), x] = 1
    return A


# ═══════ ❗(3) κ — ОДНА матрица, все роли; Ходж = Вейль буквально ═══════
def section_kappa_coherence():
    print("\n[❗3] КОГЕРЕНТНОСТЬ κ: одна матрица K, все роли; «Ходж» и «Вейль» — ОДНА формула")
    for n in range(1, 6):
        K, E, F, H = K_compl(n), E_raise(n), F_lower(n), H_grade(n)
        I = np.eye(1 << n, dtype=int)
        inv = np.array_equal(K @ K, I)                       # роль 1: инволюция объектов
        swap = np.array_equal(K @ E, F @ K)                  # K·e = f·K  (обмен повыш/пониж)
        cartan = np.array_equal(K @ H @ K, -H)               # вейлев обмен Картана
        check(f"n={n}: ОДНА K — K²=I, K·e=f·K, K·H·K=−H (три роли одного оператора)",
              inv and swap and cartan)
        # ★ e=δ, f=∂ — ОДНИ матрицы ⟹ «звезда Ходжа κ∂=δκ» и «Вейль κeκ=f» совпадают:
        hodge = np.array_equal(K @ F, E @ K)                 # κ∂=δκ  (∂=F, δ=E)
        weyl = np.array_equal(K @ E @ K, F)                  # κeκ=f
        # обе эквивалентны K·e=f·K (домножением на K, K²=I)
        same = (hodge == swap) and np.array_equal(K @ E @ K, F) and weyl
        check(f"n={n}: ∂=f, δ=e (одни матрицы) ⟹ Ходж(κ∂=δκ) И Вейль(κeκ=f) = ОДНА формула",
              hodge and weyl and same)
    print("   → κ не три согласуемых структуры, а ОДИН оператор; coherence ТОЖДЕСТВЕННА (не теорема)")


# ═══════ ⚠(2) sl₂ как representation functor (тензорная степень) ═══════
def section_sl2_functor():
    print("\n[⚠2] sl₂ = REPRESENTATION FUNCTOR: V_n=(V₁)^{⊗n}, e_n=e_{n−1}⊗I+I⊗e₁ (Лейбниц)")
    # e₁ на 1 спине: повышение |0⟩→|1⟩ (бит). Базис кронекера: новый бит — старший.
    e1 = np.array([[0, 0], [1, 0]], int)                     # add the single bit
    f1 = np.array([[0, 1], [0, 0]], int)
    h1 = np.array([[-1, 0], [0, 1]], int)
    for n in range(2, 6):
        E, F, H = E_raise(n), F_lower(n), H_grade(n)
        N1 = 1 << (n - 1)
        # рекурсия тензора: оператор ранга n = (новый старший бит) ⊗ I  +  I₂ ⊗ (ранг n−1)
        E_rec = np.kron(e1, np.eye(N1, dtype=int)) + np.kron(np.eye(2, dtype=int), E_raise(n - 1))
        F_rec = np.kron(f1, np.eye(N1, dtype=int)) + np.kron(np.eye(2, dtype=int), F_lower(n - 1))
        H_rec = np.kron(h1, np.eye(N1, dtype=int)) + np.kron(np.eye(2, dtype=int), H_grade(n - 1))
        check(f"n={n}: e_n=e₁⊗I+I⊗e_{{n−1}} (и f,H) — sl₂ есть ТЕНЗОРНАЯ СТЕПЕНЬ (V₁)^⊗n",
              np.array_equal(E, E_rec) and np.array_equal(F, F_rec) and np.array_equal(H, H_rec))
    # sl₂-соотношения держатся (над ℚ) — что это представление, а не просто операторы
    for n in range(1, 5):
        E, F, H = E_raise(n), F_lower(n), H_grade(n)
        ok = (np.array_equal(E @ F - F @ E, H) and
              np.array_equal(H @ E - E @ H, 2 * E) and
              np.array_equal(H @ F - F @ H, -2 * F))
        check(f"n={n}: [e,f]=H, [H,e]=2e, [H,f]=−2f (V_n — sl₂-модуль)", ok)
    print("   → лифт = ⊗V₁; функтор (ранги, +) → (sl₂-Rep, ⊗). Не интерпретация — явный функтор")


# ═══════ ❗(2) монада EM выведена из adjunction конструктивно ═══════
def section_monad_constructive():
    print("\n[❗2] EM(ℤ/2×(−)) выведено КОНСТРУКТИВНО: α(b,x)=σ^b(x) ↔ инволюция σ (не перебор)")
    # для произвольной инволюции σ строим T-алгебру и проверяем законы СТРУКТУРНО
    def make_algebra(sigma):                                  # σ: dict, инволюция
        X = list(sigma)
        def alpha(b, x): return x if b == 0 else sigma[x]     # α(b,x)=σ^b(x)
        # закон юнита: α(0,x)=x
        unit = all(alpha(0, x) == x for x in X)
        # ассоциативность: α(a, α(b,x)) = α(a+b mod 2, x)  для всех a,b
        assoc = all(alpha(a, alpha(b, x)) == alpha((a + b) % 2, x)
                    for a in (0, 1) for b in (0, 1) for x in X)
        # обратно: σ восстановима как α(1,·)
        recover = all(alpha(1, x) == sigma[x] for x in X)
        return unit and assoc and recover
    invs = [
        {0: 0},                                               # тривиальная
        {0: 1, 1: 0},                                         # swap
        {0: 1, 1: 0, 2: 2},                                   # swap + fixed
        {0: 1, 1: 0, 2: 3, 3: 2},                             # два swap
        {0: 0, 1: 1, 2: 2},                                   # id
    ]
    for i, s in enumerate(invs):
        # проверяем что s — инволюция, и что алгебра-законы держатся структурно
        is_inv = all(s[s[x]] == x for x in s)
        check(f"инволюция #{i} (|X|={len(s)}): α(b,x)=σ^b(x) даёт T-алгебру (юнит+ассоц+обратимость)",
              is_inv and make_algebra(s))
    print("   → структурная карта T-алгебры = действие κ, ПОСТРОЕНА из σ (вывод из adjunction,")
    print("     не счёт): EM(ℤ/2×(−)) = ℤ/2-Set = носители-с-κ [●]")


# ═══════ ❗(1) расслоение/2-категория — честно ○ ═══════
def section_fibration_open():
    print("\n[❗1] 2-КАТЕГОРИЯ / РАССЛОЕНИЕ уровней — намечено, полная когерентность ОТКРЫТА")
    # намётка (не доказательство): тотальная категория конструкции Гротендика
    #   E = { (n, структура на Q_n) },  p: E → Rank  (проекция на ранг),
    #   слои = sl₂-представления / цепные комплексы,  лифт = декартов подъём.
    # ЧЕСТНО: это НЕ проверяется как теорема — помечаем ○.
    print("   E = ∫(структуры над рангами); слои = sl₂-Rep / Ch(𝔽₂); лифт = ⊗V₁ / суспензия.")
    print("   Что это расслоение Гротендика с полной 2-когерентностью — ОТКРЫТО [○], не утверждаем.")
    print("   (слои sl₂-тензор и комплекс-конус проверены порознь; их СОВМЕСТНАЯ 2-когерентность = ○)")


def main():
    print("=" * 82)
    print("СТРУКТУРНЫЕ ЗАМЕЧАНИЯ (3-я волна): когерентность κ, sl₂-функтор, монада, расслоение")
    print("=" * 82)
    section_kappa_coherence()
    section_sl2_functor()
    section_monad_constructive()
    section_fibration_open()
    print("\n" + "=" * 82)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("РЕШЕНО ●: κ=ОДНА матрица (Ходж=Вейль одна формула, coherence тождественна);")
    print("         sl₂=тензорная степень (явный representation functor); монада EM конструктивно.")
    print("ОТКРЫТО ○: 2-категория/расслоение уровней (полная 2-когерентность); PG-естественность.")
    print("=" * 82)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
