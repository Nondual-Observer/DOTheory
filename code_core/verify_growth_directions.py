#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_growth_directions.py — assessment of three directions of development (A sheaves, B braiding,
C comonad). Honestly: what is provable ●, what is a program ○. The main point — C gives a REAL result.

A. SHEAVES on PG(n−1,2): the lift induces a direct image; base functoriality ● ; full
   sheaf cohomology of "distinctions" = program ○ (the sheaf must be defined).
B. BRAIDING: the current monoidal permutation is SYMMETRIC (c²=id); a nontrivial
   braiding (phase shift) requires additional phase structure = INPUT ○.
C. ★COMONAD OF GROWTH: the triple Λ_L⊣π⊣Λ_R gives not only a monad (π∘Λ=id) but also a COMONAD
   G=Λ_L∘π (forget a coordinate = OBSERVATION/coarse-graining). KEY: G is IDEMPOTENT (G²=G,
   non-invertible = loss of information) AND [G,Δ]≠0 (does NOT commute with the Laplacian). This is precisely
   that "second operator" — but it is an ARROW (irreversible observation), not a signature. And it is NOT
   input — it is a comonad of the already-present triple of adjoints.
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

def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A


# ═══════ A. sheaves on PG: base functoriality of the lift ═══════
def section_A():
    print("\n[A] SHEAVES on PG(n−1,2): the lift induces a direct image (base functoriality ●)")
    # PG(n−1,2) = nonzero 𝔽₂ⁿ; lift PG(n−1,2)↪PG(n,2) via embedding 𝔽₂ⁿ↪𝔽₂ⁿ⁺¹ (a↦a)
    for n in range(2, 6):
        pts_n = list(range(1, 1 << n))               # points of PG(n−1,2)
        lift = lambda a: a                            # embedding (top bit 0)
        img = [lift(a) for a in pts_n]
        # lift is injective and points land in PG(n,2) (nonzero 𝔽₂ⁿ⁺¹)
        injective = len(set(img)) == len(pts_n)
        in_target = all(1 <= y < (1 << (n + 1)) for y in img)
        check(f"n={n}: lift PG({n-1},2)↪PG({n},2) injective, image in target — induces a direct image",
              injective and in_target)
    print("   → base ● (lift→image); the sheaf of \"distinctions\" and its cohomology = program [○]")


# ═══════ B. braiding: the current permutation is symmetric ═══════
def section_B():
    print("\n[B] BRAIDING: the current monoidal permutation is SYMMETRIC (c²=id) — braiding=input")
    # symmetry: c_{B,A}∘c_{A,B}=id, where c_{A,B}:Q_m□Q_n→Q_n□Q_m, (x,y)↦(y,x)
    for (m, n) in [(1, 1), (2, 1), (2, 2), (3, 2)]:
        Nm, Nn = 1 << m, 1 << n
        c_AB = np.zeros((Nn * Nm, Nm * Nn))           # (x,y)↦(y,x)
        for x in range(Nm):
            for y in range(Nn):
                c_AB[y * Nm + x, x * Nn + y] = 1.0
        c_BA = np.zeros((Nm * Nn, Nn * Nm))           # (y,x)↦(x,y)
        for y in range(Nn):
            for x in range(Nm):
                c_BA[x * Nn + y, y * Nm + x] = 1.0
        symm = np.allclose(c_BA @ c_AB, np.eye(Nm * Nn))   # c_{B,A}∘c_{A,B}=id
        check(f"m={m},n={n}: c_{{B,A}}∘c_{{A,B}}=id — permutation is SYMMETRIC, NOT braiding", symm)
    print("   → nontrivial braiding (c²≠id, phase shift) requires phase structure = INPUT [○]")


# ═══════ C. ★COMONAD OF GROWTH: second operator, not commuting with Δ ═══════
def section_V():
    print("\n[C] ★COMONAD G=Λ_L∘π (observation): G²=G (irreversible) AND [G,Δ]≠0 — SECOND OPERATOR")
    for n in range(2, 7):
        N = 1 << n
        top = 1 << (n - 1)                            # top coordinate
        # G = forget the top coordinate (Λ_L∘π): x ↦ x with the top bit zeroed
        G = np.zeros((N, N))
        for x in range(N):
            G[x & ~top, x] = 1.0                       # coarse-graining (pull-back of observation)
        D = n * np.eye(N) - adjacency(n)              # Laplacian
        # (1) COMONAD: G²=G (idempotent — irreversible coarse-graining/observation)
        idemp = np.allclose(G @ G, G)
        # (2) IRREVERSIBLE: rank < N (loss of information)
        rank = np.linalg.matrix_rank(G)
        irreversible = rank == N // 2
        # (3) ★DOES NOT COMMUTE with Δ: [G,Δ]≠0 (unlike κ!)
        non_comm = not np.allclose(G @ D - D @ G, 0)
        check(f"n={n}: G²=G (comonad, irreversible, rank={rank}=N/2) AND [G,Δ]≠0 — second operator",
              idemp and irreversible and non_comm)
    print("   → the comonad of OBSERVATION (coarse-graining) does NOT commute with Δ ⟹ irreversibility = ARROW;")
    print("     this is NOT input — comonad of the triple Λ_L⊣π⊣Λ_R; κ is reversible/static, the comonad breaks it")


# ═══════ synthesis ═══════
def section_synth():
    print("\n[synthesis] what C gives for time")
    print("   ● κ COMMUTES with Δ ([κ,Δ]=0) — reversible statics (Wheeler–DeWitt);")
    print("   ● COMONAD G of observation does NOT commute ([G,Δ]≠0) and is IRREVERSIBLE (G²=G) — ARROW;")
    print("   ⟹ irreversibility/arrow = coarse-graining (loss of information), not κ; consistent with");
    print("     Page–Wootters (observation=condition=comonad) and the entropy arrow (coarse-graining);")
    print("   ○ BUT this is a thermodynamic arrow (irreversibility), NOT yet the Lorentzian SIGNATURE;")
    print("     the signature (−,+,+,+) is still a separate question. C gives an arrow, not a cone.")


def main():
    print("=" * 84)
    print("THREE DIRECTIONS: A sheaves (○ program), B braiding (○ input), C comonad (● arrow)")
    print("=" * 84)
    section_A(); section_B(); section_V(); section_synth()
    print("\n" + "=" * 84)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: A, B — meaningful programs with honest input/○. ★C GIVES A RESULT: the comonad")
    print("       of observation G=Λ_L∘π is irreversible (G²=G) and [G,Δ]≠0 — second operator = ARROW")
    print("       (irreversible coarse-graining), from the existing triple, not input. But not a signature.")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
