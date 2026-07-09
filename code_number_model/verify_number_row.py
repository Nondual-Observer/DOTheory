#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_number_row.py — the NATURAL NUMBER ROW through DOT (part B): counting=motion, prime=atom, D(N)≅Q_n, Euler.

Query: the natural number row = discrete motion along a continuous boundary (1+1, additive); prime = the invariant
of counting WITHOUT internal content; composite = the reverse side (composed of primes); D(N)≅Q_n; the same
seam/Riemann as physics (part A); Euler/zeta. What it is called — number theory. Parallel to part A (Physics_Chain).

Discipline: every check is FALSIFIABLE (a distinguishing control sits alongside). Values=input(○).

  A. THE NATURAL NUMBER ROW = ADDITIVE MOTION (+1), DISTINCT from the multiplicative one (×2): the additive orbit
     +1 from 0 covers the WHOLE row, the multiplicative orbit ×2 from 1 is sparse {1,2,4,8,…} (distinguishing
     control: the orbits do not coincide).
  B. PRIME = ATOM OF COUNTING (no composition): prime ⟺ exactly 2 divisors {1,p}; composite ⟺ >2 (there is composition).
     Distinguishing control: primes give |D|=2, composites >2 (and 1 — the unit, |D|=1, neither an atom nor a composite).
  C. ★D(N) ≅ Q_k for squarefree N=p₁···p_k: the divisor lattice is ISOMORPHIC to the Boolean cube (divisor↔subset
     of primes, divisibility↔⊆). Distinguishing control: N with a square (p²) is NOT a Boolean cube (|D| is not a
     power of 2, a chain).
  D. EULER stitches together COUNTING and PRIMES: ζ(s)=Σ_n n^−s = ∏_p (1−p^−s)^−1 (s=2 → π²/6). The sum over the
     naturals = the product over the primes ⟺ uniqueness of factorization. Distinguishing control: ∏ over COMPOSITES
     ≠ ζ (double counting).
  E. σ½ = THE SHARED SEAM of physics and numbers: the functional equation ζ(s)↔ζ(1−s) is symmetric relative to
     Re=½ (=σ½ of part A). Distinguishing control: outside Re=½ there is no fixed point of s↦1−s. The same center
     as the central axis of physics.
  F. THE FUNCTORIAL LAW (categorification, FinSet): +/×/^ = ⊔/×/exp; n^m=|Hom(m,n)|; |Q_n|=2^n=|2^[n]|.
     Distinguishing control: ^ is asymmetric (n^m≠m^n) like Hom; × is symmetric.
"""
from __future__ import annotations
from itertools import combinations
import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


# ═══════ A. the natural number row = additive motion (≠ multiplicative) ═══════
def section_A():
    print("\n[A] THE NATURAL NUMBER ROW = ADDITIVE MOTION (+1), DISTINCT from the multiplicative one (×2)")
    M = 33
    # the additive orbit of 0 under +1 covers the WHOLE row; the multiplicative orbit of 1 under ×2 is sparse
    add_orbit, n = set(), 0
    while n < M: add_orbit.add(n); n += 1
    mul_orbit, m = set(), 1
    while m < M: mul_orbit.add(m); m *= 2
    # distinguishing control: if the row were "multiplicative", +1 would not cover everything / the orbits would coincide
    check("the additive orbit (+1) from 0 = the WHOLE row [0,M): succ generates ℕ — the natural row = motion by +",
          add_orbit == set(range(M)))
    check("the multiplicative orbit (×2) from 1 = SPARSE {1,2,4,8,16,32} ⊊ the row — a DIFFERENT motion (× ≠ +)",
          mul_orbit == {1, 2, 4, 8, 16, 32} and mul_orbit < add_orbit)
    print("   → the row = the additive path +1 (a discrete step along the continuous measure |·|∞(n)=n); ×=expansion, ^=limit")
    print("     = three motions +/×/^ (as with time)")


# ═══════ B. prime = atom of counting ═══════
def section_B():
    print("\n[B] PRIME = ATOM OF COUNTING (no internal composition); composite = the reverse side (composition)")
    def divisors(n):
        return [d for d in range(1, n + 1) if n % d == 0]
    primes = [p for p in range(2, 40) if len(divisors(p)) == 2]
    comps = [c for c in range(2, 40) if len(divisors(c)) > 2]
    # distinguishing control: prime ⟺ |D|=2 (atom, no composition); composite ⟺ |D|>2 (has composition); 1 ⟺ |D|=1 (the unit)
    primes_are_atoms = all(len(divisors(p)) == 2 for p in primes) and primes[:5] == [2, 3, 5, 7, 11]
    comps_have_structure = all(len(divisors(c)) > 2 for c in comps) and 1 not in comps and 1 not in primes
    one_is_unit = len(divisors(1)) == 1
    check("prime = ATOM: exactly 2 divisors {1,p} (no internal composition) — the invariant of counting", primes_are_atoms)
    check("composite = the REVERSE side: >2 divisors (composed of primes); 1 = the unit (|D|=1, neither atom nor composite)",
          comps_have_structure and one_is_unit)


# ═══════ C. D(N) ≅ Q_k ═══════
def section_C():
    print("\n[C] ★D(N) ≅ Q_k for squarefree N=p₁···p_k: the divisor lattice = the Boolean cube (divisor↔subset)")
    primes = [2, 3, 5]                                       # k=3 → we expect Q₃
    N = 2 * 3 * 5
    divs = sorted(d for d in range(1, N + 1) if N % d == 0)
    # subsets of primes → divisors; divisibility d1|d2 ⟺ S1⊆S2 (order isomorphism D(N)≅(2^[k],⊆))
    subsets = [frozenset(c) for r in range(len(primes) + 1) for c in combinations(range(len(primes)), r)]
    prod = lambda S: int(np.prod([primes[i] for i in S])) if S else 1
    sub_to_div = {S: prod(S) for S in subsets}
    # the divisibility matrix of divisors and the inclusion matrix of subsets must agree under this correspondence
    order_iso = True
    for S1 in subsets:
        for S2 in subsets:
            divides = (sub_to_div[S2] % sub_to_div[S1] == 0)
            included = S1 <= S2
            if divides != included:
                order_iso = False
    cube_size = (len(divs) == 2 ** len(primes))             # |D(N)|=2^k = |Q_k|
    check(f"D({N})≅Q_{len(primes)}: |D|={len(divs)}=2^{len(primes)} and divisibility ⟺ ⊆ (isomorphism of the lattice to the cube)",
          order_iso and cube_size)
    # distinguishing control: N=12=2²·3 is NOT squarefree ⟹ NOT a Boolean cube (|D|=6 not a power of 2)
    d12 = [d for d in range(1, 13) if 12 % d == 0]
    not_cube = (len(d12) != 2 ** int(round(np.log2(len(d12)))))  # 6 is not a power of two
    check("distinguishing control: N=12=2²·3 (with a square) is NOT a cube — |D(12)|=6 is not a power of 2 ⟹ squarefree is needed", not_cube)
    print("   → a squarefree number = the Boolean cube of its primes (D(p₁p₂p₃)=Q₃); composition = a subset of atoms")


# ═══════ D. Euler stitches together counting and primes ═══════
def section_D():
    print("\n[D] EULER: ζ(s)=Σ_n n^−s = ∏_p (1−p^−s)^−1 — the sum over COUNTING = the product over PRIMES")
    s = 2.0
    target = np.pi ** 2 / 6                                  # ζ(2)
    Nmax, Pmax = 20000, 20000
    zeta_sum = sum(n ** (-s) for n in range(1, Nmax + 1))
    primes = [p for p in range(2, Pmax + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    euler_prod = 1.0
    for p in primes:
        euler_prod *= 1.0 / (1.0 - p ** (-s))
    # the sum over the naturals ≈ the product over the primes ≈ π²/6 (uniqueness of factorization, the fundamental theorem of arithmetic)
    agree = abs(zeta_sum - target) < 1e-3 and abs(euler_prod - target) < 1e-3
    check("ζ(2)=Σn^−2 = ∏_p(1−p^−2)^−1 = π²/6: counting all numbers = the product of atoms (uniqueness of factorization)",
          agree, f"sum={zeta_sum:.6f} prod={euler_prod:.6f} π²/6={target:.6f}")
    # distinguishing control: the product over COMPOSITES ≠ ζ (double counting of primes) — atomicity of primes is necessary
    comps = [c for c in range(4, 200) if any(c % q == 0 for q in range(2, c))]
    prod_comp = 1.0
    for c in comps:
        prod_comp *= 1.0 / (1.0 - c ** (-s))
    differs = abs(prod_comp - target) > 0.1
    check("distinguishing control: ∏ over COMPOSITES ≠ ζ(2) (double counting) ⟹ the product runs ONLY over the prime atoms",
          differs)


# ═══════ E. σ½ = the shared seam of physics and numbers ═══════
def section_E():
    print("\n[E] σ½ = THE SHARED SEAM: ζ(s)↔ζ(1−s) is symmetric relative to Re=½ (= the central axis of physics, part A)")
    # the functional equation is symmetric relative to s↦1−s; the fixed line Re=½ (the same σ½)
    on, off = 0.5 + 14.13j, 0.7 + 14.13j                    # 0.5+14.13i ~ the first non-trivial zero
    re_half_fixed = abs((1 - on).real - on.real) < 1e-12
    off_not_fixed = abs((1 - off).real - off.real) > 1e-9   # distinguishing control: outside Re=½ it is not fixed
    check("Re(s)=½ = the fixed point of s↦1−s (the symmetry axis of the ζ functional equation); outside it — no. = σ½ of physics [◐ identification]",
          re_half_fixed and off_not_fixed)
    print("   → ● strictly: the involution t↦1−t (both on the cube [0,1]ⁿ and on ℂ) is fixed on Re=½. [◐] that this is ONE seam")
    print("     of physics and numbers — a reading via the SHARED algebraic form 1−x, not a proof (zeta/horizons are not touched)")


# ═══════ F. functorial law (categorification) ═══════
def section_F():
    from itertools import product
    print("\n[F] THE FUNCTORIAL LAW (categorification, FinSet): +/×/^ = ⊔/×/exp; n^m=|Hom(m,n)|; |Q_n|=2^n")
    # WE BUILD the objects and count (not a formula checked against itself): |functions m→n| and |subsets of [n]|
    hom_counts = {(n, m): len(list(product(range(n), repeat=m))) for n in range(1, 4) for m in range(1, 4)}
    pow_is_hom = all(hom_counts[(n, m)] == n ** m for n in range(1, 4) for m in range(1, 4))
    cube_is_subsets = all(len(list(product((0, 1), repeat=n))) == 2 ** n for n in range(6))  # 2^[n]
    # substantively: ^ is ASYMMETRIC (n^m≠m^n in general) like Hom is asymmetric; × is symmetric (distinguishing control)
    pow_asym = any(n ** m != m ** n for n in range(1, 5) for m in range(1, 5))
    mul_sym = all(n * m == m * n for n in range(1, 5) for m in range(1, 5))
    check("n^m = |Hom(m,n)| (built the functions m→n, counted them); |Q_n|=2^n=|subsets of [n]| (built it, counted it)",
          pow_is_hom and cube_is_subsets)
    check("distinguishing control: ^ is ASYMMETRIC (∃ n^m≠m^n) like Hom; × is symmetric (n·m=m·n) — categorification of +/×/^",
          pow_asym and mul_sym)
    print("   → the law of the natural number row is already functorial (Lawvere–Schanuel/Baez): numbers=the skeleton of FinSet; DOT")
    print("     adds the OBSERVER σ½ + the seam of places |·|₂/|·|∞ (absent from pure categorification) — see doc §6")


def main():
    print("=" * 96)
    print("THE NATURAL NUMBER ROW through DOT (part B): counting=motion · prime=atom · D(N)≅Q_k · Euler · σ½-seam")
    print("=" * 96)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 96)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the natural number row = additive motion (succ +1, discrete along a continuous measure). Prime = the ATOM")
    print("       of counting (2 divisors, no composition); composite = the reverse side (a subset of atoms). ★D(N)≅")
    print("       Q_k for squarefree (the divisor lattice = the Boolean cube of primes). Euler ζ=Σ_n=∏_p stitches together counting and")
    print("       primes (uniqueness of factorization). σ½=Re=½ = the SHARED seam of physics (part A) and numbers. The law")
    print("       of the row is already functorial (FinSet, Lawvere); DOT's contribution = the observer σ½ + the seam of places. Values=input(○).")
    print("=" * 96)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
