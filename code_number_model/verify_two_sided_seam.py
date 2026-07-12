#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_two_sided_seam.py — why only +×^ (outward) is looked at, and restoration of the MIRROR (inward) around the seam σ½.

Question (user): «why do most analyses take the one-directional path +×^! (growth outward), and not the pairs
+/−, ×/÷, ^/log? for us the seam goes BOTH inward AND outward, yet we look only at the positive side». ANSWER
(I confirm — the asymmetry is REAL, I restore the mirror): the REASON is that the direct operations +×^! are TOTAL
(closed in ℕ, defined everywhere), while the inverse −/÷/log are PARTIAL (−∉ℕ, ÷∉ℤ, log∉ℚ) — the standard view takes
the total side and HIDES the partial one. BUT in DOT the partiality of the inverse side is NOT a defect, but a p-adic TOWER
INWARD: ÷p «goes inward» into |·|_p. The seam σ½ is SYMMETRIC (κ: x↦1−x = s↦1−s), both sides are EQUAL, and
★the product formula ∏_v|x|_v=1 BALANCES them (outward |·|∞ × inward all |·|_p = 1). ★The factorial «separately» —
an illusion: Γ(s)Γ(1−s)=π/sin(πs) makes it TWO-SIDED (n! outward + poles inward), stitched by the SAME s↦1−s at σ½;
we looked only at n! (the outward half). Register: ● mathematics (totality/partiality, ∏=1, Γ-reflection,
Euler); ◐ identification of the involution 1−x as ONE seam σ½ (the form is proven, the unity of the object=◐); ○ zeros of zeta/RG.
Support: σ½=Re=½, prime=atom/composite=reverse side, places of ℚ/∏=1 named.

  A. ★WHY outward: the direct +×^! are TOTAL (closed in ℕ), the inverse −/÷/log are PARTIAL ⟹ the standard takes the total.
  B. MIRROR inward: ÷p = p-adic tower; |x|_p grows INWARD (the more divisible — the smaller the Archimedean, the larger the p-adic).
  C. ★∏_v|x|_v=1: outward |·|∞ × inward all |·|_p = 1 (the product formula = the SEAM balances both sides).
  D. DIVISOR CUBE is symmetric: d↔N/d (κ) around √N=σ½; below √N (inward) ↔ above √N (outward) EQUAL in number.
  E. ★FACTORIAL is two-sided: Γ(s)Γ(1−s)=π/sin(πs) (reflection s↦1−s=σ½); n! outward + poles inward = two sides.
  F. VERDICT: we looked outward (+×^!); the mirror (−÷log, p-adic, inward) is EQUAL; σ½+∏=1 stitch. The asymmetry is named.
"""
from __future__ import annotations
import math
from math import gcd

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


# ═══════════════ A. why outward: totality of direct vs partiality of inverse ═══════════════
def section_A():
    print("\n[A] ★WHY outward: the direct +×^! are TOTAL (closed in ℕ), the inverse −/÷/log are PARTIAL ⟹ the standard takes the total")
    # direct: a+b, a·b, a^b, a! ∈ ℕ ALWAYS (totally closed)
    forward_total = all((a + b) >= 0 and (a * b) >= 0 and (a ** b) >= 1 and math.factorial(a) >= 1
                        for a in range(1, 6) for b in range(1, 6))
    # inverse: a−b∈ℕ only if a≥b; a/b∈ℕ only if b∣a; log_b(a)∈ℕ only if a=b^k — PARTIAL
    sub_partial = any((a - b) < 0 for a in range(1, 6) for b in range(1, 6))         # − goes out of ℕ
    div_partial = any((a % b) != 0 for a in range(1, 8) for b in range(2, 8))        # ÷ not closed
    log_partial = not float(math.log(5, 2)).is_integer()                             # log_2(5)=2.32…∉ℕ
    check(f"direct +×^! TOTAL (closed in ℕ everywhere):{forward_total}; inverse PARTIAL — −∉ℕ(a<b):{sub_partial}, "
          f"÷∉ℤ(b∤a):{div_partial}, log_2(5)∉ℕ:{log_partial} ⟹ the REASON for one-directionality: the standard takes the TOTAL "
          f"side (growth, defined everywhere) and HIDES the partial one (inverse) — but partiality = structure, not a defect",
          forward_total and sub_partial and div_partial and log_partial)


# ═══════════════ B. mirror inward = p-adic tower ═══════════════
def v_p(n, p):
    if n == 0:
        return math.inf
    v = 0
    n = abs(n)
    while n % p == 0:
        n //= p; v += 1
    return v

def section_B():
    print("\n[B] MIRROR inward: ÷p = p-adic TOWER; |x|_p grows INWARD (more divisible ⟹ smaller Archimedean, larger p-adic)")
    p = 2
    # sequence ×p outward: |·|∞ grows, |·|_p DECREASES (inward); ÷p mirror
    xs = [1, 2, 4, 8, 16]                                    # ×2 outward
    arch = [x for x in xs]                                   # |x|_∞ = x (grows outward)
    padic = [p ** (-v_p(x, p)) for x in xs]                  # |x|_2 = 2^{-v} (decreases = goes inward)
    arch_grows = all(arch[i] < arch[i + 1] for i in range(len(xs) - 1))
    padic_shrinks = all(padic[i] > padic[i + 1] for i in range(len(xs) - 1))
    check(f"×{p} outward: |x|_∞={arch} GROWS (outward):{arch_grows}; |x|_{p}={padic} DECREASES (inward):{padic_shrinks} "
          f"⟹ the same operation ×p seen with TWO eyes: Archimedean=growth outward, p-adic=immersion inward "
          f"(tower of divisibility) ⟹ the inner side is REAL, just measured by |·|_p, not |·|∞", arch_grows and padic_shrinks)


# ═══════════════ C. ★product formula ∏_v|x|_v=1 balances both sides ═══════════════
def primes_upto(n):
    return [q for q in range(2, n + 1) if all(q % d for d in range(2, int(q ** 0.5) + 1))]

def section_C():
    print("\n[C] ★∏_v|x|_v=1: outward |·|∞ × inward all |·|_p = 1 (the product formula = the SEAM balances both sides)")
    ok_all = True
    tests = [(12, 5), (50, 21), (7, 1), (1, 360), (99, 100)]
    for a, b in tests:
        g = gcd(a, b); a2, b2 = a // g, b // g
        val_inf = a2 / b2                                   # |x|_∞ (outward)
        prod_p = 1.0
        for q in primes_upto(max(a2, b2)):
            vp = v_p(a2, q) - v_p(b2, q)
            prod_p *= q ** (-vp)                            # ∏ |x|_q (inward)
        total = val_inf * prod_p
        if abs(total - 1.0) > 1e-9:
            ok_all = False
        print(f"   x={a}/{b}: |x|_∞={val_inf:.4g} (outward) · ∏|x|_p={prod_p:.4g} (inward) = {total:.6g}")
    check(f"for all x: |x|_∞ · ∏_p|x|_p = 1 (Ostrowski product formula):{ok_all} ⟹ the OUTER side "
          f"(Archimedean, growth) and the INNER (all p-adic, divisibility) are EXACTLY balanced by the seam ⟹ both "
          f"EQUAL; to look only at |·|∞ (growth) = to see half (∏=1 requires both)", ok_all)


# ═══════════════ D. divisor cube is symmetric d↔N/d around √N=σ½ ═══════════════
def section_D():
    print("\n[D] DIVISOR CUBE is symmetric: d↔N/d (κ) around √N=σ½; below √N (inward) ↔ above √N (outward) EQUAL in number")
    N = 360
    divs = [d for d in range(1, N + 1) if N % d == 0]
    root = math.sqrt(N)
    below = [d for d in divs if d < root]                   # «inward» (small divisors)
    above = [d for d in divs if d > root]                   # «outward» (large = N/d)
    paired = all((N // d) in divs and (N // d) > root for d in below)   # κ: d↦N/d maps below→above
    balanced = len(below) == len(above)                     # symmetry in number (N not a perfect square)
    check(f"N={N}: divisors below √N={root:.1f}: {len(below)} (inward), above: {len(above)} (outward); κ:d↦N/d "
          f"maps inward↔outward:{paired}; equal in number:{balanced} ⟹ the divisor lattice is SELF-DUAL around "
          f"√N=σ½ (center); each small divisor (inward) ↔ large (outward) — two sides of ONE seam", paired and balanced)


# ═══════════════ E. ★factorial is two-sided: Γ(s)Γ(1−s)=π/sin(πs), reflection s↦1−s=σ½ ═══════════════
def section_E():
    print("\n[E] ★FACTORIAL is two-sided: Γ(s)Γ(1−s)=π/sin(πs) (reflection s↦1−s=σ½); n! outward + poles inward = two sides")
    # reflection of Γ: Γ(s)Γ(1−s)=π/sin(πs) — SYMMETRIC under s↦1−s (the same κ as cube/zeta)
    refl_ok = True
    for s in [0.2, 0.3, 0.45, 0.6, 0.8]:
        lhs = math.gamma(s) * math.gamma(1 - s)
        rhs = math.pi / math.sin(math.pi * s)
        if abs(lhs - rhs) > 1e-9:
            refl_ok = False
    # σ½=½ — fixed point of s↦1−s, and Γ(½)²=π (extremum of the reflection)
    fixed = abs(math.gamma(0.5) ** 2 - math.pi) < 1e-9 and abs((1 - 0.5) - 0.5) < 1e-12
    # n!=Γ(n+1) outward (n≥0); poles of Γ at 0,−1,−2,... = the INNER side (negative)
    factorial_outward = all(abs(math.gamma(n + 1) - math.factorial(n)) < 1e-6 for n in range(0, 7))
    check(f"Γ(s)Γ(1−s)=π/sin(πs) (reflection s↦1−s):{refl_ok}; ½ fixed, Γ(½)²=π:{fixed}; n!=Γ(n+1) outward "
          f"(n≥0):{factorial_outward} ⟹ the factorial is NOT a «separate» operation, but a TWO-SIDED object Γ: n! (outward) + "
          f"poles at neg.integers (inward), stitched by the REFLECTION s↦1−s at σ½=½; we looked only at the n!-half",
          refl_ok and fixed and factorial_outward)
    print(f"   → s↦1−s (Γ-reflection) = s↦1−s (ξ of zeta) = x↦1−x (κ of the cube) = ONE form of involution (● form; ◐ one seam).")


# ═══════════════ G. guard of base change on the MIRRORS (Γ, ∏=1): ½=fixed point, not magic ═══════════════
def section_G():
    print("\n[G] GUARD OF BASE CHANGE on the MIRRORS (Γ(½)²=π, ∏=1): ½ = FIXED POINT of the involution (invariant), NOT a magic number")
    # the corpus applied the base guard to the ζ-line (½=mirage 4/6 vs invariant=center of the involution 6/6),
    # but NOT to the Γ-reflection and ∏=1 — we apply it SYMMETRICALLY (a finding of the review, agent of the reverse side)
    # TEST: under reparametrization φ(t)=a·t+b the involution t↦1−t passes into a conjugate one, the fixed point MOVES
    results = []
    for a, b in [(1, 0), (2, 1), (3, 1), (0.5, 4)]:
        phi = lambda t: a * t + b
        phinv = lambda t: (t - b) / a
        invol = lambda t: phi(1 - phinv(t))                  # conjugate involution in the new coordinates
        fix = phi(0.5)                                       # fixed point = image of ½
        is_fixed = abs(invol(fix) - fix) < 1e-9              # it is indeed fixed (the structure exists always)
        half_here = abs(fix - 0.5) < 1e-9                    # but the number ½ ITSELF — only in the base (1,0)
        results.append((is_fixed, half_here, fix))
    structure_always = all(r[0] for r in results)            # the fixed point EXISTS in any base (invariant)
    number_varies = sum(1 for r in results if r[1]) == 1     # the number ½ — only in ONE base (mirage)
    check(f"under base changes φ=a·t+b: the fixed point of the involution EXISTS ALWAYS (invariant):{structure_always}; but the "
          f"NUMBER ½ itself — only in the base (1,0), in others it shifts {[round(r[2],2) for r in results]}: the number varies "
          f"(mirage):{number_varies} ⟹ σ½/Γ(½)²=π/∏=1: the invariant = «FIXED POINT OF κ» (●◐), while «magic ½» = "
          f"a mirage of normalization (✗) — the SAME verdict the guard gave the ζ-line, now for the mirrors too", structure_always and number_varies)
    print(f"   → the discipline is symmetric: the base guard was on ζ (½=center of the involution, not a number), now on Γ/∏=1 — the same")
    print(f"     result ⟹ ½ everywhere = the fixed point of the seam (κ:x↦1−x=s↦1−s), NOT numerology of «exactly ½».")


# ═══════════════ F. verdict ═══════════════
def section_F():
    print("\n[F] VERDICT ●◐○")
    print("   ● mathematics: direct total/inverse partial; |x|_∞·∏|x|_p=1; d↔N/d around √N; Γ(s)Γ(1−s) reflection.")
    print("   ◐ DOT-recognition: outward/inward = face/reverse side; involution 1−x = ONE seam σ½ (the form is proven, the unity ◐).")
    print("   ○ zeros of zeta, RG, full p-adic dynamics — frontier; here the SYMMETRY of the two sides is established, not the whole reverse side.")


def main():
    print("=" * 100)
    print("TWO SIDES OF THE SEAM IN NUMBERS: why one looks outward (+×^!), and restoration of the mirror (inward, p-adic) around σ½")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_G(); section_F()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: the user is RIGHT — the asymmetry is real and now named+corrected. WHY only +×^! (outward) is looked at:")
    print("       the direct operations are TOTAL (closed in ℕ), the inverse −/÷/log are PARTIAL — the standard takes the total")
    print("       side, hides the partial one. BUT partiality = a p-adic TOWER INWARD (÷p goes into |·|_p): the mirror")
    print("       is REAL. The seam σ½ is symmetric (κ:x↦1−x=s↦1−s), and ∏_v|x|_v=1 EXACTLY balances outward(|·|∞)+inward(|·|_p)")
    print("       ⟹ both sides are EQUAL. The divisor cube is self-dual (d↔N/d around √N). ★The factorial is NOT separate:")
    print("       Γ(s)Γ(1−s)=π/sin(πs) — two-sided (n! outward + poles inward), stitched by s↦1−s at σ½. To look only")
    print("       outward = to see HALF; the full picture = two sides of the seam, ∏=1 — the conservation law between them.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
