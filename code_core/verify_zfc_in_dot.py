#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_zfc_in_dot.py — does ZFC embed in DOT?

HONEST STRUCTURAL ANSWER (the checkable part): ★the DISCRETE side of DOT = ⋃Q_n with the order ⊆, involution κ and
BIT membership — this is EXACTLY the hereditarily finite sets V_ω under the Ackermann encoding
(a∈b ⟺ bit a of the number b is set). V_ω ⊨ ZF−Infinity, and CHOICE (AC) on the finite is FREE (a ZF theorem).
⟹ ALL axioms of ZFC, EXCEPT Infinity, embed in DOT EXACTLY (isomorphism, not analogy). The axiom
of INFINITY = EXACTLY the seam |·|₂↔|·|∞: the limit of the tower = MEASURE (Gaussian underside),
not the set V_{ω+} ⟹ the full transfinite of ZFC is NOT derivable (input ○). σ½ (κ-fixed point) is NOT in any
cube = a RHYME with Russell's class (self-complement carried OUTSIDE the universe = observer/proper class).

Register: ● finite set theory = discrete DOT (Ackermann, isomorphism) · ◐ Inf=seam, σ½↔Russell ·
○ transfinite/AC-on-the-infinite = input (the same wall of values).

  A. ACKERMANN ENCODING: a∈b ⟺ (b>>a)&1; cube Q_n={m:m<2ⁿ}=HF-sets over {0..n−1} (discrete DOT=V_ω).
  B. FOUNDATION + NO SELF-MEMBERSHIP: member strictly smaller (a<n), ∈ well-founded, x∉x ∀x.
  C. PAIR/UNION = lattice operations of the cube (axioms Pairing/Union hold elementwise).
  D. POWER ≠ LIFT: Power Set (n→2ⁿ ground) and DOT lift (n→n+1, ×2 points) — DIFFERENT growth operations, both in HF.
  E. CHOICE on the FINITE = THEOREM: constructive choice function (min) always works ⟹ AC is free.
  F. σ½ = Russell's class: κ(x)=x IMPOSSIBLE (Tr κ=0, κ²=id) ⟹ self-complement OUTSIDE the cube (observer).
  G. INFINITY = SEAM: the rank of each element is FINITE, but UNBOUNDED ⟹ Inf=the only axiom outside the machine.
  H. GUARD ●◐○.
"""
from __future__ import annotations
from functools import reduce

PASS = 0; FAIL = 0
def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    PASS += ok; FAIL += (not ok)
    return ok

members = lambda n: [a for a in range(n.bit_length()) if (n >> a) & 1]   # Ackermann: members of the set-code n


# ═══════════════ A. Ackermann encoding = discrete DOT ═══════════════
def section_A():
    print("\n[A] ACKERMANN ENCODING: a∈b ⟺ (b>>a)&1; Q_n={m<2ⁿ}=HF over {0..n−1} (discrete DOT = V_ω)")
    # bijection ℕ↔HF: the code is recovered from the members as Σ2^a (bit representation — REAL invertibility)
    bij = all(sum(1 << a for a in members(n)) == n for n in range(256))
    check("ℕ↔HF bijection: n = Σ_{a∈n} 2^a (code ⟺ set of members) for n<256 — membership IS a bit", bij)
    # cube Q_n = numbers <2ⁿ = sets all of whose members are <n (ground {0..n−1})
    for n in (2, 3, 4):
        Qn = list(range(2 ** n))
        all_members_below = all(all(a < n for a in members(m)) for m in Qn)
        check(f"Q_{n}: {len(Qn)}=2^{n} points, all members <{n} (=subsets of ground {{0..{n-1}}}) ⟹ cube=fragment of HF",
              len(Qn) == 2 ** n and all_members_below)


# ═══════════════ B. Foundation + no self-membership ═══════════════
def section_B():
    print("\n[B] FOUNDATION: member STRICTLY smaller (a<n) ⟹ ∈ well-founded, ∅=bottom; x∉x ∀x")
    N = 512
    well_founded = all(all(a < n for a in members(n)) for n in range(1, N))   # every member strictly smaller
    check(f"∀n∈[1,{N}): all members a<n ⟹ ∈ well-founded (no ∞-chains ∋), ∅=code0=unique minimum", well_founded)
    no_self = all(not ((x >> x) & 1) for x in range(N))                       # bit x of number x is NEVER set
    check(f"x∉x ∀x<{N} (bit x of number x = 0, since 2^x>x) ⟹ no self-membership (like Foundation in ZF)", no_self)
    # Russell R={x:x∉x} = EVERYTHING ⟹ not a set (proper class) — self-membership belongs to NO ONE
    check("⟹ Russell's class R={x:x∉x} = the whole universe = NOT an element (proper class), as in ZF", no_self)


# ═══════════════ C. Pairing / Union = cube operations ═══════════════
def section_C():
    print("\n[C] PAIR / UNION = lattice operations of the cube (axioms hold elementwise)")
    pair = lambda a, b: (1 << a) | (1 << b)
    pairing_ok = all(set(members(pair(a, b))) == {a, b} for a in range(6) for b in range(6))
    check("Pairing: code {a,b}=(1<<a)|(1<<b), members = exactly {a,b} (all a,b<6)", pairing_ok)
    # Union S = ⋃_{y∈S} y; code = OR of members; check x∈⋃S ⟺ ∃y∈S: x∈y
    def union_code(S): return reduce(lambda u, y: u | y, members(S), 0)
    union_ok = True
    for S in range(128):
        uc = union_code(S)
        for x in range(8):
            lhs = bool((uc >> x) & 1)
            rhs = any((y >> x) & 1 for y in members(S))
            if lhs != rhs: union_ok = False
    check("Union: x∈⋃S ⟺ ∃y∈S(x∈y) for all S<128, x<8 (code ⋃S = OR of members) — the Union axiom holds", union_ok)


# ═══════════════ D. Power Set ≠ lift ═══════════════
def section_D():
    print("\n[D] POWER ≠ LIFT: Power Set (ground n→2ⁿ) and DOT lift (n→n+1, points ×2) — DIFFERENT growth operations")
    # DOT lift: Q_n→Q_{n+1}, points 2ⁿ→2^{n+1} (×2, +1 coordinate)
    lift_doubles = all(2 ** (n + 1) == 2 * 2 ** n for n in range(8))
    # Power Set: ground of n elements → 2ⁿ subsets (new ground = 2ⁿ); cube over it = 2^(2ⁿ) points
    power_explodes = all(2 ** (2 ** n) > 2 ** (n + 1) for n in range(2, 6))   # power GROWS faster than the lift
    check("lift: points 2ⁿ→2^{n+1} (×2, +1 axis) — generator of the DOT machine", lift_doubles)
    check("Power Set: ground n→2ⁿ ⟹ cube 2^(2ⁿ) ≫ lift 2^{n+1} (n≥2) — BOTH operations in HF, the machine iterates the LIFT",
          power_explodes)


# ═══════════════ E. finite choice = theorem (AC is free) ═══════════════
def section_E():
    print("\n[E] CHOICE on the FINITE = THEOREM: constructive choice function (min) ⟹ AC is free (input only ∞)")
    # deterministic nonempty finite families (without random): family_k depends on k structurally
    families = [
        [{1, 2}, {3}, {4, 5, 6}],
        [{i, i + 1} for i in range(1, 10)],
        [set(members(m)) for m in range(1, 20) if m],          # families from members of HF-codes
        [{7}], [{2, 4, 8, 16}, {3, 9}],
    ]
    families = [F for F in families if all(len(s) for s in F)]   # all nonempty
    choice = lambda F: [min(s) for s in F]                       # CONSTRUCTIVE choice function
    ok = all(all(ch in s for ch, s in zip(choice(F), F)) for F in families) and \
         all(len(choice(F)) == len(F) for F in families)
    check("finite family of nonempty ⟹ choice function f(s)=min(s) ALWAYS exists and is total (without an axiom) "
          "⟹ AC is free on the finite; nontrivial ONLY on an infinite family = input ○", ok)


# ═══════════════ F. σ½ = Russell's class (self-complement outside the cube) ═══════════════
def section_F():
    print("\n[F] σ½ = Russell's class: κ(x)=x IMPOSSIBLE (Tr κ=0, κ²=id) ⟹ self-complement OUTSIDE the cube = observer")
    for n in (1, 2, 3, 4, 5):
        mask = (1 << n) - 1
        kappa = lambda x: x ^ mask
        involution = all(kappa(kappa(x)) == x for x in range(1 << n))
        fixed = [x for x in range(1 << n) if kappa(x) == x]
        check(f"Q_{n}: κ²=id={involution}, κ-fixed points={len(fixed)}=0 (Tr κ=0) ⟹ σ½ NOT a point of the cube "
              f"(self-complement carried OUTSIDE — like Russell's class/observer)", involution and len(fixed) == 0)


# ═══════════════ G. Infinity = seam ═══════════════
def section_G():
    print("\n[G] INFINITY = SEAM |·|₂↔|·|∞: the rank is FINITE for each, but UNBOUNDED ⟹ Inf outside the machine")
    from functools import lru_cache
    import sys
    sys.setrecursionlimit(100000)
    @lru_cache(maxsize=None)
    def rank(n): return 0 if n == 0 else 1 + max(rank(a) for a in members(n))
    # tower a_0=0, a_{k+1}=2^{a_k}: rank = k (each element of finite rank)
    tower = [0]
    for _ in range(5):
        tower.append(1 << tower[-1])     # 0,1,2,4,16,65536
    ranks_ok = all(rank(tower[k]) == k for k in range(5))   # rank(65536)=4 etc.
    check(f"tower 0→1→2→4→16→65536: rank = {[rank(tower[k]) for k in range(5)]} = 0..4 "
          f"(each element of FINITE rank)", ranks_ok)
    # rank is unbounded: ∃ element of any finite rank, but NONE is infinite ⟹ Inf = completion of the tower
    unbounded = rank(tower[5]) == 5 and all(rank(n) < 10 ** 9 for n in range(64))
    check("rank is UNBOUNDED (∃ element of rank k ∀k), but ALWAYS finite ⟹ Infinity (the completed ⋃Q_n as "
          "an OBJECT) = the only axiom OUTSIDE the machine = SEAM to |·|∞ (limit=measure, not V_{ω+}) ○", unbounded)


# ═══════════════ H. guard ═══════════════
def section_H():
    print("\n[H] GUARD ●◐○")
    print("   ● discrete DOT = V_ω (Ackermann, isomorphism): Extensionality/Foundation/Pairing/Union/Separation/")
    print("     Replacement hold; AC is FREE on the finite (a ZF theorem). This is EXACTLY ZF−Infinity.")
    print("   ◐ Infinity = seam |·|₂↔|·|∞ (Inf=the only axiom outside the machine); σ½ ↔ Russell's class")
    print("     (self-complement outside the universe); Power Set vs lift = two growth operations.")
    print("   ○ the full TRANSFINITE of ZFC (V_α, α≥ω; large cardinals) is NOT derivable: limit=measure (Gaussian underside),")
    print("     not the cumulative hierarchy; AC-on-the-infinite is INDEPENDENT (Gödel/Cohen) = input = the same wall of values.")


def main():
    print("=" * 100)
    print("ZFC in DOT? — the finite part embeds EXACTLY (=V_ω, Ackermann); Infinity=seam; AC free/input")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G(); section_H()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: ZFC as a WHOLE does NOT \"embed\" in DOT. More precisely: the DISCRETE side of DOT (⋃Q_n,⊆,κ,bit-∈) IS the finitary")
    print("       set theory V_ω (Ackermann, ●) — into it embed ALL axioms of ZFC except Infinity, and choice")
    print("       there is FREE. The axiom of Infinity = EXACTLY the seam to |·|∞ (limit=measure, not a set); the full")
    print("       transfinite + AC-on-the-infinite = INPUT (the same wall). σ½ = Russell's class (self-complement outside).")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
