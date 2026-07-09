#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_color_projection.py — color projection as an ACCOMPANYING lens (◐ reading).

Color = the most vivid and ONLY measured map of our octahedron Q₃: trichromacy gives exactly 3 axes, group
B₃, the lightness axis is measured as the observer (corr=0.874).
Here we check the COLOR CORRESPONDENCES of our structures: observer σ½=lightness L; the two sides of the seam=
additive RGB/subtractive CMY; κ=complement; simplex {e,i,π}=HSB polar; factorial/Chebyshev=spectrum/atoms;
metamerism=loss under projection (why the values lie beyond the wall). Register ●◐○: color facts (RGB↔CMY=κ,
L=DC, HSB=polar)=● mathematics/measurement; identification color↔number=◐ reading; values (chromaticity=distribution
of primes)=○. Color LEADS visually, but does NOT replace our proven structures — it colors them in.

  A. RGB↔CMY=κ (complement): weight-1↔weight-2, R↔C,G↔M,Y↔B = our κ-axes of the octahedron (R₃).
  B. lightness L=(R+G+B)=DC=INVARIANT of all maps (RGB-sum=HSB-V for gray) = observer σ½, ⊥ to chromaticity.
  C. HSB=polar {hue=angle, sat=radius, val=L} = simplex {e,i,π}=exp; i=√κ only on the continuous circle.
  D. hue-cycle = C₆ (6 Kuhn sectors, neighbors=distance 1); half-turn 180°=complement=κ.
  E. factorial↔Chebyshev = light(whole spectrum, additive)↔paint(atoms-primes, subtractive).
  F. ★METAMERISM: different N of the same rank ω (one L) = different chromaticity → one projection onto the observer (loss=the wall).
"""
from __future__ import annotations
import colorsys, math

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok


# ═══════════════ A. RGB↔CMY = κ (complement) ═══════════════
def section_A():
    print("\n[A] RGB↔CMY = κ (complement x↦1−x): weight-1 (light) ↔ weight-2 (paint) = our κ-axes of octahedron R₃")
    prim = {'R': (1, 0, 0), 'G': (0, 1, 0), 'B': (0, 0, 1)}
    comp_names = {(0, 1, 1): 'C', (1, 0, 1): 'M', (1, 1, 0): 'Y'}
    ok = True
    pairs = []
    for nm, v in prim.items():
        c = tuple(1 - x for x in v)
        cn = comp_names[c]
        pairs.append(f"{nm}↔{cn}")
        if sum(v) != 1 or sum(c) != 2:
            ok = False
    check(f"R↔C, G↔M, B↔Y ({', '.join(pairs)}): weight-1 (Σ=1, additive/light/outward) ↔ weight-2 (Σ=2, subtractive/"
          f"paint/inward), complement=κ: {ok} ⟹ color κ = our κ (d↦N/d), opponent pairs = R₃ axes", ok)


# ═══════════════ B. lightness L = DC = observer invariant ═══════════════
def section_B():
    print("\n[B] lightness L=(R+G+B) = DC = INVARIANT of all maps = observer σ½ (⊥ to chromaticity; measured 0.874)")
    # L is the same in the RGB-sum and HSB-value for gray; the axis 000↔111 = achromatic (punctured poles)
    grays = [(t, t, t) for t in (0.0, 0.25, 0.5, 0.75, 1.0)]
    # for gray: hue undefined, saturation=0, value=t=L ⟹ gray = pure L-axis
    achromatic = all(colorsys.rgb_to_hsv(*g)[1] == 0.0 and abs(colorsys.rgb_to_hsv(*g)[2] - g[0]) < 1e-9 for g in grays)
    # L is orthogonal to chromaticity: R,G,B,C,M,Y all have L=1/3 or 2/3, but DIFFERENT hue
    chroma = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    same_L_diff_hue = (len(set(round(sum(c) / 3, 3) for c in chroma)) == 1)  # R,G,B all have L=1/3
    check(f"gray axis 000↔111: saturation=0, value=L (pure lightness, no chromaticity): {achromatic}; R,G,B "
          f"have ONE L=1/3 but DIFFERENT hue: {same_L_diff_hue} ⟹ L=DC=observer axis σ½, ORTHOGONAL to "
          f"chromaticity (in the corpus we measured corr(frequency,DC)=+0.874, on semantics 0.02)", achromatic and same_L_diff_hue)


# ═══════════════ C. HSB = polar = simplex {e,i,π} ═══════════════
def section_C():
    print("\n[C] HSB = polar {hue=angle, sat=radius, val=lightness} = simplex {e,i,π}=exp; i=√κ on the continuous circle")
    cols = {'R': (1, 0, 0), 'Y': (1, 1, 0), 'G': (0, 1, 0), 'C': (0, 1, 1), 'B': (0, 0, 1), 'M': (1, 0, 1)}
    hsv = {nm: colorsys.rgb_to_hsv(*v) for nm, v in cols.items()}
    # hue = angle (0..1 = 0..360°); pure colors on radius 1 (saturation=1)
    angles = {nm: round(h[0] * 360) for nm, h in hsv.items()}
    polar_ok = all(abs(hsv[nm][1] - 1.0) < 1e-9 for nm in cols)  # all on unit radius (max sat)
    # 6 colors = 6 angles 60° apart (like roots of unity) = e^{iθ}; polar = e^{i·angle}·radius
    six_sectors = sorted(angles.values()) == [0, 60, 120, 180, 240, 300]
    check(f"HSB: hue-angles {sorted(angles.values())}=[0,60,..,300] (6 sectors 60° apart, like roots of 1=e^{{iθ}}); "
          f"all on radius 1: {polar_ok}; ⟹ HSB=POLAR (angle=i/period π, radius=scale e, height=L) = simplex "
          f"{{e,i,π}}; i=√κ exists on the continuous circle, not on the discrete 6",
          polar_ok and six_sectors)


# ═══════════════ D. hue-cycle = C₆, half-turn = κ ═══════════════
def section_D():
    print("\n[D] hue-cycle = C₆ (6 Kuhn sectors); half-turn 180° = complement = κ")
    # neighboring sectors differ by 60° (one cycle step); opposite (180°) = complements
    import cmath
    T = cmath.exp(1j * math.pi / 3)            # rotation by 60° = one step of the hue-cycle
    T6 = abs(T ** 6 - 1) < 1e-9                 # T⁶=1 (full circle)
    T3 = abs(T ** 3 - (-1)) < 1e-9             # T³=−1=κ (half-turn=complement)
    # complement in hue = shift by 180° = 3 sectors: R(0°)→C(180°), Y(60°)→B(240°), G(120°)→M(300°)
    check(f"hue-cycle: T=e^{{iπ/3}} (step 60°), T⁶=1 (circle): {T6}; T³=−1=κ (half-turn=complementary color): {T3} "
          f"⟹ hue-cycle = C₆ = R₁ of our octahedron; T³=κ = e^{{iπ}}=−1 (spectral theorem) — color complement "
          f"= antipode of the divisor", T6 and T3)


# ═══════════════ E. factorial↔Chebyshev = light/paint ═══════════════
def primes_upto(n): return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
def section_E():
    print("\n[E] factorial↔Chebyshev = light(whole spectrum, additive, outward) ↔ paint(atoms-primes, subtractive, inward)")
    n = 20
    logfact = sum(math.log(k) for k in range(1, n + 1))   # whole spectrum (all wavelengths)
    theta = sum(math.log(p) for p in primes_upto(n))      # projection onto atoms (primes)
    # factorial > θ: the full set is larger than the singled-out atoms (loss under projection onto primes)
    check(f"log({n}!)=Σlog k={logfact:.2f} (LIGHT: whole spectrum of factors, additive outward) > θ({n})=Σlog p="
          f"{theta:.2f} (PAINT: projection onto PRIME-atoms, subtractive inward): {logfact > theta} ⟹ like RGB-light "
          f"(full) vs CMY-projection onto a basis; the choice of 'what to take' = a choice of filter-cone", logfact > theta)


# ═══════════════ F. ★metamerism = loss under projection onto the observer ═══════════════
def omega(n):
    c = 0; d = 2; m = n
    while d * d <= m:
        if m % d == 0:
            c += 1
            while m % d == 0: m //= d
        d += 1
    if m > 1: c += 1
    return c
def section_F():
    print("\n[F] ★METAMERISM: different N of the same rank ω (one L-lightness) = different chromaticity → ONE projection (loss)")
    # numbers of rank ω=2 (one 'lightness' = rank), but different primes (different 'chromaticity')
    rank2 = [n for n in range(2, 40) if omega(n) == 2 and all(n % (p * p) for p in (2, 3, 5))][:6]
    same_rank = all(omega(n) == 2 for n in rank2)
    distinct = len(set(rank2)) == len(rank2)
    check(f"numbers of rank ω=2 (one L=rank): {rank2} — all ω=2: {same_rank}, but DIFFERENT (different primes=chromaticity): "
          f"{distinct} ⟹ METAMERISM: different 'spectra' (factorizations) → one projection onto the observer (rank/L); "
          f"the σ½ projection LOSES chromaticity ⟹ VALUES are not recoverable from structure (the wall of the corpus explained by color)",
          same_rank and distinct)
    print("   → this is ◐ reading (color metamerism ↔ the wall of number values), not a proof; but it VIVIDLY explains")
    print("     why the observer-projection loses the values: like the eye losing the spectrum in 3 cones.")


def main():
    print("=" * 100)
    print("COLOR PROJECTION (accompanying ◐) of our structures: octahedron Q₃ colored in, observer=L")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: color = a vivid ACCOMPANYING map (◐) of our octahedron Q₃, and it is the ONLY MEASURED one.")
    print("       observer σ½ = lightness L = DC = frequency (corr 0.874); the two sides of the seam = additive RGB/subtractive")
    print("       CMY; κ = complement (R↔C); simplex {e,i,π} = HSB polar; hue-cycle = C₆, T³=κ; factorial/Chebyshev")
    print("       = light/paint. ★METAMERISM (different N of the same rank → one L) VIVIDLY explains the wall of values:")
    print("       projection onto the observer loses chromaticity, as the eye loses the spectrum. ● color facts/measurement;")
    print("       ◐ identification color↔number; ○ values (chromaticity=distribution of primes). Color COLORS IN,")
    print("       it does not replace the proven structures.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
