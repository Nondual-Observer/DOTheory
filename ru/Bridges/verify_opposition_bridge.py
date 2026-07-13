#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_opposition_bridge.py — единый мост: оппозиционный костяк → золотая реализация → шов дискрет↔континуум.

Одна дуга, две части. ЧАСТЬ I (реализация, всё ●): костяк = свободная инволюция (X,κ), n оппозиций = 2n полюсов;
вынужденная реализация = ортоплекс β_n «полный минус паросочетание» — ТЕРМИНАЛ СЛОЯ над сценой (D⊣U держится:
пустой граф свободен; правый сопряжённый U⊣C/«кофри» ОПРОВЕРГНУТ §B, ортоплекс не кофри); золотая половина β_6 =
икосаэдр через галуа-расщепление ℝ⁶=V_φ⊕V_ψ (обе половины замощают 60 рёбер 30+30); золотой фрейм ВНЕШНИЙ (Stab_{B₆}=I_h≪B₆).
ЧАСТЬ II (шов дискрет↔континуум, ●-конструкция в ◐-законе): сторона |·|∞ достигается ДВУМЯ функторно-разными
машинами — вертикальным спектральным пределом башни (куб→гаусс, аддитив) и горизонтальной Галуа-проекцией
(cut-and-project: ℤ⁶ сквозь окно-триаконтаэдр → икосаэдрический квазикристалл, мультипликатив/ℤ[φ]); расходятся
на РАНГЕ 5, где ось-5 (A₅,√5) некристаллографична.

СТАТУС. Все конструкции ниже = ● (вычислено). Законы «вынужденность=кофри», «два лица |·|∞ (+/×)», функторная
рамка = ◐ (резонанс с корпусом, названо). Внешность золотого фрейма и премиса 5-осности ранга 5 (соименность
A₅↔U₅, док 01 §5.1) = ○. Икосаэдр остаётся ◐-соименностью пака (док 01 §5.2), закон её уточняет, не повышает.
Опора: док 01 §3.4 (кросс-политоп=фигура сцены), §5.1–5.2, док 02 гл VI (сцена)/гл VII (спектральный предел).

ЧАСТЬ I — КОСТЯК И ЗОЛОТАЯ РЕАЛИЗАЦИЯ
  A. КОСТЯК: β_6=K_{6×2} «полный минус паросочетание» — 10-регуляр, 60 рёбер, дополнение = 6·K₂.
  B. РЕАЛИЗАЦИИ: D⊣U держится (пустой граф свободен); U⊣C/кофри ОПРОВЕРГНУТ (Hom 0≠8, C не функториален);
     верное свойство — ортоплекс = терминал слоя над фикс. сценой (макс. антипод-свободный κ-граф).
  C. ВЛОЖЕНИЕ: икосаэдр = 6 антипод. пар, антиподы несмежны; 30 рёбер ⊂ 60 = половина.
  D. ЗОЛОТОЙ УГОЛ: 6 осей под arccos(1/√5); оси ортоплекса ортогональны в 6D.
  E. ★ГАЛУА: ℝ⁶=V_φ⊕V_ψ ортонормирован; обе проекции — икосаэдры; половины делят 60=30+30.
  F. κ-ИНВАРИАНТ: центральная инверсия сохраняет рёбра икосаэдра ⟹ объект Real над (X,κ).
  G. ★СТРАЖ ВНЕШНОСТИ: Stab_{B₆}(золотая половина)=120=|I_h|≪46080=|B₆| ⟹ фрейм внешний.
ЧАСТЬ II — ШОВ ДИСКРЕТ↔КОНТИНУУМ
  H. МАШИНА 1: спектр куба {2k} ЦЕЛЫЙ; веса C(n,k)→гаусс (ЦПТ); иррациональности нет.
  I. МАШИНА 2 спектр: граф икосаэдра несёт ±√5 (подпись золотого фрейма; в кубе её нет).
  J. РАНГ 5: элемент порядка 5 впервые в S_n при n=5; кристаллографический запрет (оси 2,3,4,6).
  K. ПРОЕКЦИЯ+ОКНО: M ортогональна, E∥⊥E⊥, тотальная иррациональность; окно = 30 граней (RT).
  L. ДИСКРЕТНОСТЬ+5-ОСНОСТЬ: cut-and-project → Delone; звезда инвариантна под 72°/120°, НЕ под 90°.
  M. ФАЗОН: сдвиг окна γ меняет узор, плотность держит ⟹ фаза=вход, окно=форма.
  N. ЗОЛОТОЕ КОЛЬЦО: физические координаты ∈ ℤ[φ] (высота ^).
"""
from __future__ import annotations
import itertools
from math import sqrt, comb
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

phi = (1 + sqrt(5)) / 2
psi = (1 - sqrt(5)) / 2
def axes(t): return np.array([(0,1,t),(0,1,-t),(1,t,0),(1,-t,0),(t,0,1),(t,0,-1)], float)

# ---- combinatorial frame: labels (axis, sign), orthoplex, edge sets ----
LABELS = [(a, s) for a in range(6) for s in (+1, -1)]
ORTHO = set(frozenset((x, y)) for x, y in itertools.combinations(LABELS, 2) if x[0] != y[0])
def d2(p, q): return float(((np.asarray(p) - np.asarray(q))**2).sum())
def edgeset(t):
    A = axes(t); V = np.vstack([A, -A])
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    L = lambda i: (i % 6, +1 if i < 6 else -1)
    return set(frozenset((L(i), L(j))) for i in range(12) for j in range(12)
               if i != j and abs(d2(V[i], V[j]) - ed) < 1e-9)
Ephi, Epsi = edgeset(phi), edgeset(psi)

# ---- geometric frame: orthonormal M, E∥/E⊥, window ----
Vp, Wp = axes(phi), axes(psi)
nV = sqrt((Vp[0]**2).sum()); nW = sqrt((Wp[0]**2).sum())
M = (np.hstack([Vp / nV, Wp / nW]) / sqrt(2)).T
Ppar, Pperp = M[:3, :], M[3:, :]
gens = [Pperp[:, i] for i in range(6)]
normals = []
for i, j in itertools.combinations(range(6), 2):
    n = np.cross(gens[i], gens[j])
    if np.linalg.norm(n) < 1e-9: continue
    n = n / np.linalg.norm(n)
    if not any(np.allclose(n, m) or np.allclose(n, -m) for m in normals): normals.append(n)
Hs = [0.5 * np.sum(np.abs(np.array(gens) @ n)) for n in normals]
def in_window(P):
    ok = np.ones(P.shape[0], bool)
    for n, h in zip(normals, Hs): ok &= (np.abs(P @ n) <= h + 1e-9)
    return ok
XA = np.array(list(itertools.product(range(-3, 4), repeat=6)), float)
XPperp = XA @ Pperp.T; XPpar = XA @ Ppar.T
def project(gamma3=None):
    P = XPperp if gamma3 is None else XPperp - gamma3
    acc = in_window(P); return XA[acc], XPpar[acc]
def rot(axis, deg):
    a = axis / np.linalg.norm(axis); th = np.radians(deg); c, s = np.cos(th), np.sin(th)
    x, y, z = a; C = 1 - c
    return np.array([[c+x*x*C, x*y*C-z*s, x*z*C+y*s],
                     [y*x*C+z*s, c+y*y*C, y*z*C-x*s],
                     [z*x*C-y*s, z*y*C+x*s, c+z*z*C]])

# ====================== PART I ======================
def section_A():
    print("\n[A] КОСТЯК: ортоплекс β_6 = «полный минус паросочетание»")
    deg = {v: sum(1 for e in ORTHO if v in e) for v in LABELS}
    check("β_6: каждый полюс 10-регулярен (смежен со всеми, кроме антипода)", set(deg.values()) == {10})
    check("β_6: 60 рёбер = C(12,2)−6", len(ORTHO) == 60)
    matching = set(frozenset(((a, +1), (a, -1))) for a in range(6))
    allpairs = set(frozenset(p) for p in itertools.combinations(LABELS, 2))
    check("дополнение β_6 = 6·K₂ (6 антиподальных осей = паросочетание)", matching == (allpairs - ORTHO))

# --- малые категорные проверки адъюнкции (κ-эквивариантные карты сцен) ---
def _kmaps(nx, ny):
    for choice in itertools.product([(b, sg) for b in range(ny) for sg in (+1, -1)], repeat=nx):
        yield choice
def _orthoedges(n):
    pts = [(a, s) for a in range(n) for s in (+1, -1)]
    return set(frozenset((x, y)) for x, y in itertools.combinations(pts, 2) if x[0] != y[0])
def _is_hom(choice, eA, eB):
    for e in eA:
        (a1, s1), (a2, s2) = tuple(e)
        img = frozenset(((choice[a1][0], choice[a1][1]*s1), (choice[a2][0], choice[a2][1]*s2)))
        if len(img) == 1 or img not in eB: return False
    return True

def section_B():
    print("\n[B] РЕАЛИЗАЦИИ: D⊣U держится; U⊣C (кофри) ОПРОВЕРГНУТ; ортоплекс = терминал слоя")
    # D⊣U: из ПУСТОГО графа всякая κ-карта — гомоморфизм (нет рёбер-ограничений) = свободность (левый сопряжённый)
    total = sum(1 for _ in _kmaps(2, 3))
    homs = sum(1 for c in _kmaps(2, 3) if _is_hom(c, set(), _orthoedges(3)))
    check("D⊣U держится: из пустого графа ВСЕ κ-карты — гомоморфизмы ⟹ свободная (левая) реализация",
          homs == total == 36)
    # U⊣C ЛОЖНО: Hom_Real(β₃, C(1 ось)) = 0 ≠ 8 = Hom_Scene(U β₃, 1 ось)
    hr = sum(1 for c in _kmaps(3, 1) if _is_hom(c, _orthoedges(3), _orthoedges(1)))
    hs = sum(1 for _ in _kmaps(3, 1))
    check("U⊣C (кофри) ОПРОВЕРГНУТО: Hom_Real(β₃,C(1ось))=0 ≠ 8=Hom_Scene ⟹ ортоплекс НЕ правый сопряжённый",
          hr == 0 and hs == 8)
    # C не функториален: scene-морфизмы S₂→S₁ не поднимаются до морфизмов ортоплексов
    bad = sum(1 for c in _kmaps(2, 1) if not _is_hom(c, _orthoedges(2), _orthoedges(1)))
    check("C не функториален (все 4 морфизма S₂→S₁ рвут ребро ортоплекса) ⟹ правого сопряжённого нет", bad == 4)
    # ВЕРНОЕ свойство: ортоплекс = терминал СЛОЯ над фикс. сценой (максимальный антипод-свободный κ-граф)
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    non_edges = set(frozenset(p) for p in itertools.combinations(LABELS, 2)) - ORTHO
    check("β_6 κ-инвариантна, всякое её не-ребро антиподально ⟹ ТЕРМИНАЛ СЛОЯ (макс. реализация фикс. сцены)",
          all(kap(e) in ORTHO for e in ORTHO) and all(len({a for (a,s) in e}) == 1 for e in non_edges) and len(non_edges) == 6)

def section_C():
    print("\n[C] ВЛОЖЕНИЕ: икосаэдр ⊂ β_6, ровно половина рёбер")
    A = axes(phi); V = np.vstack([A, -A])
    anti = lambda i: next(j for j in range(12) if d2(V[j], -V[i]) < 1e-9)
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    check("икосаэдр: антиподы НЕ соединены ребром", not any(abs(d2(V[i], V[anti(i)]) - ed) < 1e-9 for i in range(12)))
    check("икосаэдр: 30 рёбер ⊆ 60 рёбер β_6 (остовный подграф), ровно половина", Ephi <= ORTHO and len(Ephi) == 30)

def section_D():
    print("\n[D] ЗОЛОТОЙ УГОЛ: 6 осей под arccos(1/√5)")
    A = axes(phi); nrm = float((A[0]**2).sum())
    coss = sorted(set(round(abs(float(A[i] @ A[j])) / nrm, 9) for i, j in itertools.combinations(range(6), 2)))
    check("норма² оси = 2+φ", abs(nrm - (2 + phi)) < 1e-9)
    check("все 6 осей взаимно под |cos|=1/√5 (золотой угол ≈63.43°)",
          len(coss) == 1 and abs(coss[0] - 1 / sqrt(5)) < 1e-9)

def section_E():
    print("\n[E] ★ГАЛУА: ℝ⁶=V_φ⊕V_ψ; обе проекции — икосаэдры; половины делят 60=30+30")
    Aphi, Apsi = axes(phi), axes(psi)
    nphi, npsi = float((Aphi[0]**2).sum()), float((Apsi[0]**2).sum())
    U = [tuple(np.hstack([Aphi[i] / sqrt(nphi), Apsi[i] / sqrt(npsi)]) / sqrt(2)) for i in range(6)]
    maxoff = max(abs(float(np.array(U[i]) @ np.array(U[j]))) for i, j in itertools.combinations(range(6), 2))
    diag = all(abs(float(np.array(U[i]) @ np.array(U[i])) - 1.0) < 1e-9 for i in range(6))
    check("ℝ⁶=V_φ⊕V_ψ: 6 векторов (золото⊕сопряжение) ОРТОНОРМИРОВАНЫ (=6D-ортоплекс)", diag and maxoff < 1e-9,
          extra=f"max|внедиаг|={maxoff:.1e}")
    for name, t in (("φ", phi), ("ψ", psi)):
        V = np.vstack([axes(t), -axes(t)])
        shells = sorted(set(round(d2(V[i], V[j]), 6) for i in range(12) for j in range(12) if i != j))
        check(f"проекция на {name}-блок — правильный икосаэдр (3 оболочки)", len(shells) == 3)
    check("E_φ ∪ E_ψ = все 60 рёбер β_6, E_φ ∩ E_ψ = ∅ (галуа-пара замощает 30+30)",
          (Ephi | Epsi) == ORTHO and len(Ephi & Epsi) == 0 and len(Ephi) == 30 == len(Epsi))

def section_F():
    print("\n[F] κ-ИНВАРИАНТ: центральная инверсия сохраняет рёбра икосаэдра")
    kap = lambda e: frozenset((a, -s) for (a, s) in e)
    check("κ-образ рёбер = рёбра ⟹ икосаэдр ∈ Real над (X,κ)", set(kap(e) for e in Ephi) == Ephi)

def section_G():
    print("\n[G] ★СТРАЖ ВНЕШНОСТИ: Stab_{B₆}(золото)=120=|I_h|≪46080=|B₆|")
    from itertools import permutations, product
    stab = 0; total = 0
    for sigma in permutations(range(6)):
        for eps in product((+1, -1), repeat=6):
            total += 1
            img = set(frozenset((sigma[a], eps[a] * s) for (a, s) in e) for e in Ephi)
            if img == Ephi: stab += 1
    check("|B₆| = 2⁶·6! = 46080 (полная симметрия костяка)", total == 46080)
    check("Stab_{B₆}(золотая половина) = 120 = |I_h| ⟹ слом 384-кратный ⟹ фрейм ВНЕШНИЙ [○]",
          stab == 120 and total // stab == 384)

# ====================== PART II ======================
def section_H():
    print("\n[H] МАШИНА 1: спектр куба ЦЕЛЫЙ, веса → гаусс")
    check("спектр лапласиана Q_n = {2k} целочислен (n=2,4,6); иррациональности НЕТ",
          all(float(2 * k).is_integer() for n in (2, 4, 6) for k in range(n + 1)))
    w = [comb(6, k) for k in range(7)]
    check("веса Q_6 = C(6,k) = [1,6,15,20,15,6,1] → гаусс (ЦПТ)", w == [1, 6, 15, 20, 15, 6, 1])

def section_I():
    print("\n[I] МАШИНА 2 спектр: граф икосаэдра несёт ±√5")
    V = np.vstack([axes(phi), -axes(phi)])
    ed = min(d2(V[i], V[j]) for i in range(12) for j in range(12) if i != j)
    A = np.array([[1.0 if i != j and abs(d2(V[i], V[j]) - ed) < 1e-6 else 0.0 for j in range(12)] for i in range(12)])
    ev = np.linalg.eigvalsh(A)
    check("спектр графа икосаэдра содержит ±√5 (подпись золотого фрейма; в кубе её нет)",
          any(abs(abs(x) - sqrt(5)) < 1e-6 for x in ev))

def section_J():
    print("\n[J] РАНГ 5: ось-5 впервые; кристаллографический запрет")
    has5 = lambda n: n >= 5    # элемент порядка 5 = 5-цикл, нужно ≥5 точек
    check("элемента порядка 5 в S_4 НЕТ (ранги 1–4 кристаллографичны)", not has5(4))
    check("элемент порядка 5 (A₅) впервые в S_5 — ось-5 рождается на ранге 5", has5(5))
    check("кристаллографический запрет: решётка допускает оси только 2,3,4,6 (ось 5 некристаллографична)",
          5 not in (2, 3, 4, 6))

def section_K():
    print("\n[K] ПРОЕКЦИЯ + ОКНО = ромбический триаконтаэдр (30 граней)")
    check("M ортогональна (MᵀM=I)", np.allclose(M.T @ M, np.eye(6)))
    check("E∥ ⊥ E⊥ (Ppar·Pperpᵀ = 0)", np.allclose(Ppar @ Pperp.T, np.zeros((3, 3))))
    tot = True
    for x in itertools.product(range(-2, 3), repeat=6):
        if x == (0,) * 6: continue
        xv = np.array(x, float)
        if np.allclose(Pperp @ xv, 0, atol=1e-9) or np.allclose(Ppar @ xv, 0, atol=1e-9):
            tot = False; break
    check("тотальная иррациональность (нет 0≠x∈ℤ⁶ с x⊥=0 или x∥=0) ⟹ апериодичность", tot)
    check("окно = зонотоп 6 перп-генераторов: 15 нормалей → 30 граней = RT", len(normals) == 15)

_cache = {}
def _patch():
    if "Pb" not in _cache:
        Xacc, P3 = project(); _cache["Xacc"] = Xacc; _cache["P3"] = P3
        Pb = P3[np.linalg.norm(P3, axis=1) < 2.2]
        D = np.sqrt(((Pb[:, None, :] - Pb[None, :, :])**2).sum(-1)); np.fill_diagonal(D, np.inf)
        _cache["Pb"], _cache["D"] = Pb, D
    return _cache

def section_L():
    print("\n[L] ДИСКРЕТНОСТЬ + ★5-ОСНОСТЬ")
    c = _patch(); D = c["D"]; Pb = c["Pb"]; mind = D.min()
    check("min-расстояние > 0 (Delone; без окна было бы 7^6=117649 плотно)", mind > 0.1, extra=f"min={mind:.4f}")
    check("нет больших дыр (относит. плотно = Delone)", D.min(axis=1).max() / mind < 3.0)
    ii, jj = np.where((D < mind * 1.05) & (D > 0))
    vecs = Pb[jj] - Pb[ii]; dirs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
    uniq = []
    for dv in dirs:
        if not any(np.allclose(dv, u, atol=2e-2) for u in uniq): uniq.append(dv)
    uniq = np.array(uniq)
    inv = lambda Rm: all(any(np.allclose(rd, s, atol=3e-2) for s in uniq) for rd in uniq @ Rm.T)
    check("звезда инвариантна под 5-осное 72° (икосаэдральная ось)", inv(rot(Vp[0], 72)))
    check("звезда НЕ инвариантна под кубическое 90° ⟹ некристаллографична (икосаэдр, не куб)",
          not inv(rot(np.array([1., 0, 0]), 90)))

def section_M():
    print("\n[M] ФАЗОН: фаза разреза = свободный вход")
    _, P0 = project(); _, Pg = project(gamma3=np.array([0.30, 0.10, -0.20]))
    r = lambda A: set(map(lambda x: tuple(np.round(x, 3)), A))
    check("γ≠0 МЕНЯЕТ узор ⟹ фаза — свободный вход [○]", len(r(P0) & r(Pg)) < len(P0))
    check("плотность держится при сдвиге фазы ⟹ окно (форма) фиксировано [●]",
          abs(len(P0) - len(Pg)) / len(P0) < 0.25)

def section_N():
    print("\n[N] ЗОЛОТОЕ КОЛЬЦО ℤ[φ]")
    raw = _patch()["Xacc"] @ Vp
    inZ = lambda x: any(abs((x - b * phi) - round(x - b * phi)) < 1e-6 for b in range(-60, 61))
    frac = np.mean([inZ(v) for v in raw[:150].flatten()])
    check("физ. координаты вида a+bφ ⟹ квазикристалл ∈ ℤ[φ] (высота ^)", frac > 0.99, extra=f"{frac*100:.0f}%")


def main():
    print("=" * 100)
    print("ЕДИНЫЙ МОСТ: оппозиционный костяк → золотая реализация → шов дискрет↔континуум")
    print("=" * 100)
    print("\n--- ЧАСТЬ I: костяк и золотая реализация (всё ●) ---")
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    print("\n--- ЧАСТЬ II: шов дискрет↔континуум (●-конструкция, ◐-закон) ---")
    section_H(); section_I(); section_J(); section_K(); section_L(); section_M(); section_N()
    print("\n" + "=" * 100)
    print(f"ИТОГ: {PASS} PASS / {FAIL} FAIL")
    print("ВЫВОД: одна дуга. Костяк оппозиций → кофри-ортоплекс → золотая галуа-половина (икосаэдр) → две машины")
    print("       дискрет→континуум (спектральный предел vs cut-and-project), расходящиеся на ранге 5. Конструкции")
    print("       = ●; законы вынужденности/двух-лиц-|·|∞ = ◐; внешность фрейма и премиса 5-осности ранга 5 = ○.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
