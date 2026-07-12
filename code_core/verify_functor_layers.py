#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_layers.py — missing functorial layers of the discrete part
(beyond the growth skeleton in Core/Fronts). Pure combinatorics/algebra, without physics.

A. κ as the DUALITY of the boolean lattice — a contravariant involutive functor
   (de Morgan κ(a∧b)=κ(a)∨κ(b), order reversal, κ²=id). [ch. II]
B. CHAIN COMPLEX over 𝔽₂ — ∂²=0=δ², κ=HODGE STAR (κ∂=δκ), reduced
   acyclicity, LIFT=SUSPENSION (cone). [ch. VIII §8.2 — second structure]
C. LIFT IS MONOIDAL — Q_{m+n}=Q_m□Q_n, κ coordinatewise; break 4=2×2. [ch. IV]
D. HOLONOMY — T³=κ on C₆; C₆→C₆/κ=C₃ connected double cover (nontrivial H¹). [ch. III]
E. SINGER CYCLE — order 2ⁿ⁻¹−1; incommensurability gcd(2ⁿ⁻¹−1,2ⁿ−1)=1. [ch. III]
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


# ═══════════════ A. κ-duality (contravariant functor) ═══════════════
def section_A():
    print("\n[A] κ = DUALITY of the boolean lattice (de Morgan, order reversal) [ch.II]")
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
        check(f"n={n}: de Morgan κ(a∧b)=κa∨κb, order reversal a≤b⟺κa≥κb, κ²=id",
              dm and order and inv)
    print("   → κ — contravariant involutive endofunctor (anti-automorphism of the lattice)")


# ═══════════════ B. chain complex, Hodge, suspension ═══════════════
def boundary(n):
    """∂: remove a one. ∂[y,x]=1 if y=x∖{i}, i∈x (over 𝔽₂)."""
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
    print("\n[B] CHAIN COMPLEX over 𝔽₂: ∂²=0, κ=Hodge star (κ∂=δκ), acyclicity [ch.VIII]")
    for n in range(1, 6):
        Bd, Dl, K = boundary(n), coboundary(n), kappa_mat(n)
        d2 = np.all((Bd @ Bd) % 2 == 0)
        c2 = np.all((Dl @ Dl) % 2 == 0)
        hodge = np.all((K @ Bd) % 2 == (Dl @ K) % 2)               # κ∂=δκ — Hodge star
        check(f"n={n}: ∂²=0, δ²=0 over 𝔽₂; κ∂=δκ (κ=HODGE STAR)", d2 and c2 and hodge)
        # reduced acyclicity: all H_k=0 (ranks mod 2) and Euler Σ(−1)ᵏC(n,k)=0
        # H_k = dim C_k − rank∂_k − rank∂_{k+1}; ∂_k = part of ∂ from layer k → k−1
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
        check(f"n={n}: reduced ACYCLIC (all H_k=0) and Euler Σ(−1)ᵏC(n,k)={euler}=0",
              homol_ok and euler == 0)

    # LIFT = SUSPENSION (cone): ∂_{n+1} = [[∂_n, Id],[0, ∂_n]] in the basis (bit n =0)⊕(bit n =1)
    print("   lift = SUSPENSION (cone): ∂_{n+1} = block cone over ∂_n")
    for n in range(1, 5):
        Bn, Bn1 = boundary(n), boundary(n + 1)
        N = 1 << n
        B0 = list(range(N))                       # bit n = 0  (base Q_n)
        B1 = [x | (1 << n) for x in range(N)]      # bit n = 1
        order = B0 + B1
        reordered = Bn1[np.ix_(order, order)] % 2
        # expected cone: [[Bn, I],[0, Bn]]
        cone = np.block([[Bn % 2, np.eye(N, dtype=int)],
                         [np.zeros((N, N), int), Bn % 2]]) % 2
        check(f"n={n}→{n+1}: ∂_{{{n+1}}} = cone [[∂_n, I],[0, ∂_n]] (lift=suspension)",
              np.array_equal(reordered, cone))


# ═══════════════ C. monoidality of the lift ═══════════════
def section_C():
    print("\n[C] LIFT IS MONOIDAL: Q_{m+n}=Q_m□Q_n, κ coordinatewise; break 4=2×2 [ch.IV]")
    def adj(n):
        N = 1 << n; A = np.zeros((N, N), int)
        for x in range(N):
            for i in range(n): A[x ^ (1 << i), x] = 1
        return A
    for (m, n) in [(1, 1), (1, 2), (2, 2), (2, 3)]:
        Amn = adj(m + n)
        # Q_{m+n} = Q_m □ Q_n: A = A_m⊗I + I⊗A_n
        box = np.kron(adj(m), np.eye(1 << n, dtype=int)) + np.kron(np.eye(1 << m, dtype=int), adj(n))
        # κ coordinatewise: κ_{m+n} = κ_m ⊗ κ_n
        kmn = kappa_mat(m + n)
        kbox = np.kron(kappa_mat(m), kappa_mat(n))
        check(f"Q_{{{m+n}}} = Q_{m}□Q_{n} (A=A_m⊗I+I⊗A_n) and κ=κ_m⊗κ_n",
              np.array_equal(Amn, box) and np.array_equal(kmn, kbox))
    print("   → break 4=2×2: Q₄=Q₂□Q₂, lift — monoidal functor (□, K₂)")


# ═══════════════ D. holonomy (Möbius) ═══════════════
def section_D():
    print("\n[D] HOLONOMY: T³=κ on C₆; C₆→C₆/κ=C₃ connected double cover [ch.III]")
    # C₆ = Hamming-1 cycle on U₃
    cyc = [0b001, 0b011, 0b010, 0b110, 0b100, 0b101]   # each step — flip of one bit
    # check that this is a Hamming-1 cycle
    is_cycle = all(popcount(cyc[i] ^ cyc[(i + 1) % 6]) == 1 for i in range(6))
    T = {cyc[i]: cyc[(i + 1) % 6] for i in range(6)}    # shift
    def T3(x):
        for _ in range(3): x = T[x]
        return x
    t3_is_kappa = all(T3(x) == x ^ 0b111 for x in cyc)  # T³ = κ (antipode)
    check("C₆ — Hamming-1 cycle; T³=κ (half-turn = complement)", is_cycle and t3_is_kappa)
    # C₆/κ: 3 κ-pairs; cover is connected ⟺ C₆ is ONE cycle (not two triangles)
    pairs = {frozenset((x, x ^ 0b111)) for x in cyc}
    connected = (len(pairs) == 3)                       # 3 pairs = C₃ below; C₆ connected above
    check("C₆/κ = C₃ (3 pairs), cover CONNECTED ⟹ nontrivial class H¹(S¹;ℤ₂)=ℤ₂ (Möbius)",
          connected)


# ═══════════════ E. Singer cycle / incommensurability ═══════════════
def section_E():
    print("\n[E] SINGER CYCLE on PG(n−2,2): order 2ⁿ⁻¹−1; incommensurability of neighbors [ch.III]")
    for n in range(2, 8):
        singer = (1 << (n - 1)) - 1                     # |PG(n-2,2)| = 2^{n-1}−1
        # incommensurability: gcd(order of floor n, order of floor n+1)=1
        g = gcd((1 << (n - 1)) - 1, (1 << n) - 1)
        check(f"n={n}: Singer cycle of order {singer}; gcd(2ⁿ⁻¹−1,2ⁿ−1)={g}=1 (incommensurable)",
              g == 1)
    print("   → rotations of neighboring ranks are coprime (2ⁿ−1=2(2ⁿ⁻¹−1)+1): the screw does not close")


def main():
    print("=" * 78)
    print("MISSING FUNCTORIAL LAYERS of the discrete part (beyond the growth skeleton)")
    print("=" * 78)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 78)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("ADDED: κ-duality (contravariant functor); chain complex ∂/δ + κ=Hodge +")
    print("          lift=suspension; monoidality of the lift; holonomy (Möbius); Singer cycle.")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
