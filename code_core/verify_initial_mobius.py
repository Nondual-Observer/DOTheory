#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_initial_mobius.py — two gaps in the functorial machine (chapter VIII), closed after assembling
number theory.

Chapter VIII §8.5 names the TERMINAL object (observer σ½), but not its dual — the INITIAL one.
And §8.6/IX gives the reduced acyclicity Σ(−1)^k C(n,k)=0, but does not identify it with the MÖBIUS
FUNCTION of the lattice = INVERSION (which in number theory became 1/ζ=Σμ/nˢ). Here both facts are
verified rigorously (●).

Every check is FALSIFIABLE (a distinguishing control alongside), no tautologies.

  A. INITIAL ⊣ TERMINAL (category of sets-with-involution κ, equivariant morphisms):
     terminal {∗} (κ=id): |Hom(X,{∗})|=1 ∀X (§8.5, observer); initial ∅: |Hom(∅,X)|=1 ∀X (seed).
     Both OUTSIDE the tower Q_n (κ on Q_n is free). Distinguishing control: Q_n itself is NOT terminal
     (|End(Q_n)|>1) and NOT initial; from the terminal into Q_n there are NO morphisms (no κ-fixed
     point) — it sits at the upper end.
  B. MÖBIUS FUNCTION = INVERSION = reduced acyclicity: μ(∅,S)=(−1)^|S|; Σ_k(−1)^k C(n,k)=0 (n≥1),
     =1 (n=0); inversion μ*ζ=δ (Σ_{T⊆S}μ(∅,T)=[S=∅]). Distinguishing control: ζ without signs
     (Σ_{T⊆S}1=2^|S|) does NOT invert — signs are necessary. The Euler characteristic of the reduced
     complex = Σμ over the cube.
"""
from __future__ import annotations
from itertools import product
from math import comb

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


# object = (carrier as tuple, involution κ as dict); morphism f is equivariant: f(κx)=κ' f(x)
def Qn(n):
    N = 1 << n
    full = N - 1
    return (tuple(range(N)), {x: x ^ full for x in range(N)})       # κ = bitwise complement

TERM = ((0,), {0: 0})                                                # {∗}, κ=id (fixed point)
INIT = ((), {})                                                      # ∅

def equivariant_homs(X, Y):
    (xs, kx), (ys, ky) = X, Y
    if not xs:
        return 1                                                     # from ∅ exactly one (the empty map)
    count = 0
    for assign in product(ys, repeat=len(xs)):
        f = dict(zip(xs, assign))
        if all(f[kx[x]] == ky[f[x]] for x in xs):                    # f(κx)=κ'f(x)
            count += 1
    return count


# ═══════ A. initial ⊣ terminal ═══════
def section_A():
    print("\n[A] INITIAL ∅ ⊣ TERMINAL {∗}: 8.5 gives only the terminal; the initial (seed) is its dual")
    objs = [INIT, Qn(1), Qn(2), Qn(3)]
    # terminal {∗}: from ANY object exactly one equivariant morphism
    term_ok = all(equivariant_homs(X, TERM) == 1 for X in objs)
    # initial ∅: into ANY object exactly one (the empty map)
    init_ok = all(equivariant_homs(INIT, X) == 1 for X in objs + [TERM])
    check("terminal {∗} (κ=id): |Hom(X,{∗})|=1 for all X (§8.5 — observer σ½)", term_ok)
    check("★initial ∅: |Hom(∅,X)|=1 for all X — the DUAL object (seed/background), omitted in 8.5", init_ok)
    # distinguishing control: Q_n itself is NOT terminal — it has >1 endomorphisms (id and κ), and |Q_n|>1
    not_term = all(equivariant_homs(Qn(n), Qn(n)) > 1 for n in (1, 2, 3))
    check("distinguishing control: Q_n is NOT terminal — |End(Q_n)|>1 (there are id and κ), |Q_n|=2ⁿ>1 ⟹ the "
          "terminal lies OUTSIDE the tower",
          not_term)
    # terminal at the UPPER end: from {∗} into Q_n there are no morphisms (needs a κ-fixed point, but κ is free)
    no_down = all(equivariant_homs(TERM, Qn(n)) == 0 for n in (1, 2, 3))
    check("from the terminal {∗} into Q_n there are NO morphisms (no κ-fixed point) ⟹ {∗}=upper end (σ½ outside the scene)",
          no_down)
    print("   → the tower: initial ∅ (seed, no distinctions) →…→ Q_n →…→ terminal {∗} (observer σ½);")
    print("     κ-duality of arrows swaps initial↔terminal (like 0↔∞ under inversion in the numbers)")


# ═══════ B. Möbius function = inversion = acyclicity ═══════
def section_B():
    print("\n[B] the MÖBIUS FUNCTION of the lattice = INVERSION (μ*ζ=δ) = reduced acyclicity Σ(−1)^k C(n,k)=0")
    mu = lambda S: (-1) ** bin(S).count("1")                         # μ(∅,S)=(−1)^|S| on the Boolean lattice
    # reduced acyclicity = Euler characteristic: Σ_k (−1)^k C(n,k) = (1−1)^n = 0 (n≥1), 1 (n=0)
    euler = {n: sum((-1) ** k * comb(n, k) for k in range(n + 1)) for n in range(7)}
    check("Σ_k(−1)^k C(n,k)=0 for n≥1 and =1 for n=0 (reduced acyclicity of the complex = Σμ over the cube)",
          all(euler[n] == 0 for n in range(1, 7)) and euler[0] == 1)
    # Möbius inversion μ*ζ=δ: Σ_{T⊆S} μ(∅,T) = [S=∅] (μ is the inverse of ζ=the constant 1 in the incidence algebra)
    inv = all(sum(mu(T) for T in range(1 << n) if (T & S) == T) == (1 if S == 0 else 0)
              for n in (1, 2, 3, 4) for S in range(1 << n))
    check("inversion μ*ζ=δ: Σ_{T⊆S}μ(∅,T)=[S=∅] ⟹ μ INVERTS summation over the lattice (in numbers = 1/ζ=Σμ/nˢ)",
          inv)
    # distinguishing control: ζ without signs does NOT invert — Σ_{T⊆S} 1 = 2^|S| ≠ δ (alternating signs are necessary)
    zeta_no_inv = all(sum(1 for T in range(1 << n) if (T & S) == T) == (1 << bin(S).count("1"))
                      for n in (1, 2, 3) for S in range(1 << n))
    check("distinguishing control: ζ without signs Σ_{T⊆S}1=2^|S| (NOT δ) ⟹ the signs of μ are necessary — inversion, not summation",
          zeta_no_inv)
    # connection to κ: μ(S)=(−1)^|S|, and μ(κS)=μ(∁S)=(−1)^{n−|S|}=(−1)^n·μ(S) — κ multiplies the Möbius value by (−1)^n
    n = 4
    kappa_mu = all((-1) ** bin(((1 << n) - 1) ^ S).count("1") == (-1) ** n * mu(S) for S in range(1 << n))
    check("μ(κS)=(−1)ⁿ·μ(S): the complement κ maps the alternating side into itself with factor (−1)ⁿ", kappa_mu)
    print("   → acyclicity (8.6/IX) = the Möbius function of the lattice = INVERSION; the alternating side of the machine,")
    print("     dual to summation by ranks; in numbers = the Möbius μ, 1/ζ=∏(1−p⁻ˢ)")


def main():
    print("=" * 96)
    print("TWO GAPS IN THE FUNCTORIAL MACHINE (ch. VIII), closed by assembling number theory: initial object + Möbius")
    print("=" * 96)
    section_A(); section_B()
    print("\n" + "=" * 96)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION (●): (A) the machine has an INITIAL object ∅ (seed/background, |Hom(∅,X)|=1), dual to the terminal")
    print("       {∗}=σ½ (observer); 8.5 named only the terminal — the asymmetry is closed. (B) the reduced")
    print("       acyclicity Σ(−1)^k=0 = the Möbius FUNCTION of the lattice = inversion μ*ζ=δ (the alternating side,")
    print("       dual to summation); in numbers = μ, 1/ζ=Σμ/nˢ. Both are closures of gaps, not new entities.")
    print("=" * 96)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
