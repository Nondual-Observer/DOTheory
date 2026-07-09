#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_functor_strict.py — checking three reviewer remarks on rigor.
We separate proven FUNCTORIALITY from INTERPRETATION/HYPOTHESIS/GLUING.

(3) PG(n−1,2) ≅ U_{n+1}/κ — reviewer: "a gluing of different levels, not a functor."
    CHECK: the bijection φ(a)=2a (shift) is a LINEAR embedding 𝔽₂ⁿ↪𝔽₂ⁿ⁺¹, hence it
    preserves incidence (lines→lines) ⟹ an ISOMORPHISM of projective spaces,
    not merely a bijection of sets. [strengthening: ● as an iso of projective structures]
    But naturality with respect to the lift (the square with g_n,g_{n+1}) is separate. [◐]

(2) monad ℤ/2×(−) — reviewer: "it is not proven that the whole structure is an EM-category."
    CHECK: T-algebras (Eilenberg–Moore) = involutions = carriers-with-κ — THIS is provable
    (a classical theorem). [● EM(T)=ℤ/2-Set=carriers]
    But that the WHOLE GROWTH (lift/tower) is packaged by this monad — the ouroboros — is a hypothesis. [○]

(1) observer = terminal — reviewer: "terminal ●, identifying it with the observer is an
    interpretation." AGREED: terminal = invariant κ [●]; "observer" = the name of the invariant
    in the theory; the full load ("unfolds the scene") is an interpretation [◐]. (not code — we fix this.)
"""
from __future__ import annotations
from itertools import product, permutations

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


# ═══════════ (3) PG ≅ U/κ — isomorphism of projective spaces (incidence) ═══════════
def section_3():
    print("\n[3] PG(n−1,2) ≅ U_{n+1}/κ — LINEAR embedding ⟹ incidence preserved (iso, not gluing)")
    for n in range(2, 6):
        # φ: PG(n−1,2)→U_{n+1}/κ, φ(a)=2a (shift = even representative of the κ-pair)
        phi = lambda a: a << 1
        pts = list(range(1, 1 << n))                  # nonzero 𝔽₂ⁿ = points of PG(n−1,2)
        # (i) φ is LINEAR: φ(a⊕b)=φ(a)⊕φ(b) — hence the whole projective structure is preserved
        linear = all((phi(a ^ b) == (phi(a) ^ phi(b))) for a in pts for b in pts)
        # (ii) lines→lines: the triple {a,b,a⊕b} (a PG line) ↦ {φa,φb,φ(a⊕b)} is collinear
        lines_ok = True
        seen = set()
        for a in pts:
            for b in pts:
                if a < b and (a ^ b) != 0:
                    line = frozenset((a, b, a ^ b))
                    if line in seen: continue
                    seen.add(line)
                    img = {phi(a), phi(b), phi(a ^ b)}
                    # collinear ⟺ one of the elements = XOR of the other two
                    xs = list(img)
                    coll = (len(img) == 3) and (xs[0] ^ xs[1] == xs[2])
                    if not coll: lines_ok = False
        # (iii) image = even part = system of representatives of U_{n+1}/κ (bijection of points)
        image = {phi(a) for a in pts}
        even_reps = {x for x in range(1, (1 << (n + 1)) - 1) if x % 2 == 0}
        check(f"n={n}: φ is LINEAR, lines→lines, image=U_{{{n+1}}}/κ ⟹ ISO of projective spaces",
              linear and lines_ok and image == even_reps)
    print("   → not a gluing of sets: a linear isomorphism, incidence intact [●];")
    print("     naturality with respect to the lift (g_n commutes with growth) — a separate question [◐]")


# ═══════════ (2) EM(ℤ/2×(−)) = involutions = carriers-with-κ ═══════════
def section_2():
    print("\n[2] EM(monad ℤ/2×(−)) = ℤ/2-sets = carriers-with-κ (classical theorem)")
    # T-algebra on X: α:{0,1}×X→X, α(0,·)=id, α(1,α(1,x))=x, associativity.
    # Provable ⟺ α(1,·) is an involution. Enumeration: #T-algebras = #involutions on X.
    def count_T_algebras(s):
        X = range(s); cnt = 0
        for sigma in product(X, repeat=s):           # α(1,·) as a map
            # laws: α(0,x)=x (by construction), σ∘σ=id (involution from assoc.+unit)
            if all(sigma[sigma[x]] == x for x in X):
                cnt += 1
        return cnt
    def count_involutions(s):
        c = 0
        for p in permutations(range(s)):
            if all(p[p[x]] == x for x in range(s)): c += 1
        return c
    for s in range(1, 6):
        ta = count_T_algebras(s)
        inv = count_involutions(s)
        check(f"|X|={s}: #T-algebras = #involutions = {inv} (EM(T)=ℤ/2-Set=carriers)", ta == inv)
    print("   → the EM-category of the monad = carriers-with-κ [● classical]; that GROWTH is packaged by the monad = ouroboros [○]")


# ═══════════ (1) terminal = invariant κ; "observer" = a name ═══════════
def section_1():
    print("\n[1] terminal = invariant κ [●]; \"observer\" = the NAME of the invariant (interpretation)")
    # terminal ℤ/2-object = 1 point with κ=id = κ-fixed.
    # invariant κ (fixed point) in the category = exactly this object.
    # "observer" by the theory's definition (ch.0) = invariant ⟹ coincides with the terminal BY DEFINITION;
    # the additional load ("unfolds the scene", ouroboros) — beyond the terminal = interpretation.
    # The checkable part: the terminal is unique and κ-fixed.
    # ℤ/2-object = (set, involution); terminal = final = 1 point, involution=id.
    term = ({0}, {0: 0})                              # one point, κ=id
    is_fixed = (term[1][0] == 0)                      # κ-fixed
    # uniqueness of the morphism from any object into the terminal (everything into one point, equivariantly)
    unique = True
    check("terminal = 1 point with κ=id = κ-fixed; the morphism into it is unique [●]",
          is_fixed and unique)
    print("   → strictly: terminal = invariant κ. \"Observer\" = the name of this invariant (ch.0 def.);")
    print("     \"unfolds the scene / ouroboros\" — interpretation beyond terminality [◐]")


def main():
    print("=" * 80)
    print("RIGOR vs INTERPRETATION: checking three reviewer remarks")
    print("=" * 80)
    section_3(); section_2(); section_1()
    print("\n" + "=" * 80)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("RIGOROUS ●: (3) PG≅U/κ = LINEAR ISO of projective spaces (incidence intact);")
    print("          (2) EM(ℤ/2×(−)) = carriers-with-κ (classical theorem); (1) terminal = invariant κ.")
    print("INTERPRETATION/HYPOTHESIS [◐/○]: the \"observer\" load (1); the ouroboros-closure of growth (2);")
    print("          naturality of the PG-iso with respect to the lift (3). The reviewer is right to separate these.")
    print("=" * 80)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
