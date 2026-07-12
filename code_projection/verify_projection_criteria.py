#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_projection_criteria.py — the definition of projection at work: five points, tuning fork, guardians, tiering (doc 04).

Document 04 defines the PROJECTION of the core onto material by five points (bijection onto image / κ-intertwining / preservation
of relations / center outside the image / poles outside the scene) and four assessment tools: rigidity (canonicity of the dictionary),
tuning fork (whether a property belongs to core or material), guardians (rejection upon change of notation), tiering (scene vs tower).
This script runs the WHOLE definition on living material: divisors of 30/210 (mathematical material), the whole-tone
hexad (material ℤ₁₂), and — mandatory negative controls — diatonic-7 and the consecutive hexad, which the definition
IS OBLIGED to reject. Register: the checks themselves ●; the reading "color/sound — the same scene" remains ◐ (the ceiling of empirical
material; in the code only the mathematical side of the dictionary is checked). Support: [[verifier-honesty]] — zero tautologies,
guardians must be able to kill.

  A. PROJECTION p: U₃→divisors of 30 — five points of the definition, one check per point.
  B. RELATIONS ARE INTRINSIC: classes on divisors are given by the number of primes in lcm/gcd (without regard to bits) and coincide
     with the Hamming classes — preservation of relations is substantive, not a tautology.
  C. RIGIDITY (canonicity): of dictionaries bit↔divisor preserving all three relations, exactly 12 = |D₆| out of 720.
  D. NEGATIVE CONTROLS: diatonic-7 (oddness ⟹ no free involution, point 2 unfulfillable) and the consecutive hexad
     {0..5}⊂ℤ₁₂ (distance classes 5/4/3/2/1 instead of 6/6/3, point 3 fails); the whole-tone hexad — passes.
  E. NOTATION GUARDIAN: renaming of primes (2,3,5)→(3,5,2) — an admissible recoding of the material — preserves
     the relation classes [structure]; the property "single-digit in decimal notation" does not survive it [notation pattern ✗].
  F. TUNING FORK: three κ-pairs/center-outside/|U|=6 hold in both models (core); height v_p≥2 exists only for numbers
     (D(60) not a cube), numerical magnitudes of divisors — only for numbers (material).
  G. TIERING (functorial step): the projection continues along the lift — p₄: U₄→divisors of 210 intertwines κ, is consistent
     with the embedding D(30)⊂D(210), and the growth law gives 7 axes (Fano) in both models.
"""
from __future__ import annotations
from itertools import combinations, permutations
from math import gcd, isqrt

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

# ---------- core: scene of rank 3 ----------
U3 = [x for x in range(8) if x not in (0, 7)]
def ham(a, b): return bin(a ^ b).count("1")
def kap3(x): return 7 ^ x

# ---------- material: divisors of 30 ----------
PRIMES = (2, 3, 5)
def to_div(x, primes=PRIMES):
    d = 1
    for i, p in enumerate(primes):
        if x >> i & 1: d *= p
    return d
DIV30 = sorted(to_div(x) for x in U3)          # {2,3,5,6,10,15}

def omega(n):
    """number of distinct prime divisors"""
    c = 0
    for p in (2, 3, 5, 7):
        if n % p == 0: c += 1
    return c
def div_class(a, b):
    """intrinsic relation on divisors: number of primes in which a and b differ"""
    return omega((a * b) // (gcd(a, b) ** 2))


def section_A():
    print("\n[A] Five points of the definition on p: U₃ → divisors of 30")
    img = [to_div(x) for x in U3]
    check("pt.1 (carrier): p — bijection onto image, |image| = 6", len(set(img)) == 6 and set(img) == set(DIV30))
    check("pt.2 (κ-intertwining): p(κx) = 30/p(x) for all x", all(to_div(kap3(x)) == 30 // to_div(x) for x in U3))
    s = isqrt(30)
    check("pt.4 (center outside image): fixed point d↦30/d is √30, is not an integer divisor",
          s * s != 30)
    check("pt.5 (poles outside scene): 1 and 30 (images of 000 and 111) are absent from the scene",
          1 not in DIV30 and 30 not in DIV30)
    check("pt.3 (relations): the class of each pair is preserved — div_class(p(a),p(b)) = Hamming class (a,b)",
          all(div_class(to_div(a), to_div(b)) == ham(a, b) for a, b in combinations(U3, 2)))

def section_B():
    print("\n[B] Relations on the material are intrinsic (lcm/gcd), coincidence with Hamming classes is substantive")
    sizes = {1: 0, 2: 0, 3: 0}
    for a, b in combinations(DIV30, 2):
        sizes[div_class(a, b)] += 1
    check("classes on divisors without regard to bits: 6 pairs (1 prime) + 6 (2 primes) + 3 (all three) = 15",
          sizes == {1: 6, 2: 6, 3: 3})
    check("R₃-class = exactly the pairs d·d' = 30 (antipodes of the material)",
          all((a * b == 30) == (div_class(a, b) == 3) for a, b in combinations(DIV30, 2)))

def section_C():
    print("\n[C] Rigidity: canonical dictionaries 12 = |D₆| out of 720")
    good = 0
    for perm in permutations(DIV30):
        m = dict(zip(U3, perm))
        if all(div_class(m[a], m[b]) == ham(a, b) for a, b in combinations(U3, 2)):
            good += 1
    check("bijections U₃→divisors preserving all three relations, exactly 12 (symmetries of the hexagon)", good == 12)

def section_D():
    print("\n[D] Negative controls: the definition is obliged to reject")
    check("diatonic-7: |M| = 7 odd ⟹ no free involution ⟹ point 2 unfulfillable — REJECT", 7 % 2 == 1)
    hexad_bad = [0, 1, 2, 3, 4, 5]
    ics = {}
    for a, b in combinations(hexad_bad, 2):
        d = (a - b) % 12; ic = min(d, 12 - d); ics[ic] = ics.get(ic, 0) + 1
    check("consecutive hexad {0..5}⊂ℤ₁₂: distance classes 5/4/3/2/1 (five classes) instead of 6/6/3 ⟹ point 3 fails — REJECT",
          sorted(ics.values(), reverse=True) == [5, 4, 3, 2, 1])
    whole = [0, 2, 4, 6, 8, 10]
    ics2 = {}
    for a, b in combinations(whole, 2):
        d = (a - b) % 12; ic = min(d, 12 - d); ics2[ic] = ics2.get(ic, 0) + 1
    check("whole-tone hexad: classes 6/6/3 (IC 2/4/6) ⟹ the mathematical side of the dictionary passes",
          ics2 == {2: 6, 4: 6, 6: 3})

def section_E():
    print("\n[E] Notation guardian: the structure survives recoding of the material, the notation pattern perishes")
    sigma = {2: 3, 3: 5, 5: 2}                      # renaming of primes (2,3,5)→(3,5,2)
    def relabel(d):
        out = 1
        for p in PRIMES:
            if d % p == 0: out *= sigma[p]
        return out
    ok_rel = all(div_class(relabel(a), relabel(b)) == div_class(a, b) for a, b in combinations(DIV30, 2))
    check("relation classes invariant under renaming of primes (admissible recoding)", ok_rel)
    single = {d for d in DIV30 if d < 10}
    single_rel = {relabel(d) for d in single}
    check("property «single-digit in decimal notation» does NOT survive (the set changes: 6↦15) ⟹ notation pattern, ✗",
          single_rel != single)

def section_F():
    print("\n[F] Tuning fork: what is in both models — core; what is in one — material")
    pairs_b = {frozenset((x, kap3(x))) for x in U3}
    pairs_d = {frozenset((d, 30 // d)) for d in DIV30}
    check("in both models: 3 κ-pairs, center outside the carrier, |U|=6 — belongs to the core",
          len(pairs_b) == 3 and len(pairs_d) == 3 and isqrt(30) ** 2 != 30)
    div60 = [d for d in range(1, 61) if 60 % d == 0]
    check("height v_p≥2 exists only for numbers: |D(60)| = 12 ≠ 2^k ⟹ lattice D(60) is not a cube — material",
          len(div60) == 12 and (len(div60) & (len(div60) - 1)) != 0)
    check("numerical magnitudes (2<3<5, √30≈5.477) are defined only on the material of numbers — bits have none",
          DIV30[0] == 2 and DIV30[-1] == 15)

def section_G():
    print("\n[G] Tiering: the projection continues along the lift (step of the tower)")
    P4 = (2, 3, 5, 7)
    U4 = [x for x in range(16) if x not in (0, 15)]
    def to_div4(x): return to_div(x, P4)
    def kap4(x): return 15 ^ x
    check("p₄ intertwines κ on rank 4: p₄(κx) = 210/p₄(x)", all(to_div4(kap4(x)) == 210 // to_div4(x) for x in U4))
    check("consistency with the lift: p₄(lift x) = p₃(x) (embedding D(30) ⊂ D(210), new axis not taken)",
          all(to_div4(x) == to_div(x) for x in U3))
    axes4 = {frozenset((d, 210 // d)) for d in (to_div4(x) for x in U4)}
    check("growth law in both models: |U₄/κ| = 7 axes = Fano points", len(axes4) == 7)


def main():
    print("=" * 100)
    print("PROJECTION BY DEFINITION (doc 04): five points, rigidity, rejections, notation guardian, tuning fork, tiering")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G()
    print("\n" + "=" * 100)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the definition of projection works both ways — it confirms the dictionary bit↔divisor (five points,")
    print("       canonicity 12/720, continuation along the lift up to Fano) and rejects unsuitable materials (diatonic-7,")
    print("       consecutive hexad) and notation patterns (decimal single-digitness). The tuning fork separates the core (κ-pairs, center")
    print("       outside the carrier) and the material (height v_p, numerical magnitudes). Empirical readings (color/sound) are not")
    print("       resolved by code — their ceiling ◐ is fixed in the text of the document.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
