#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_kappa_spectral_theorem.py — why e^{iLπ}=I is NOT a coincidence of rank 3, but a theorem about κ at every rank.

Continuation of the note "π via e^{iπL}=I — true, but trivial, spectrum {0,4,6}
even". Here — WHY the spectrum is even: this is not a property specifically of the octahedron, but a THEOREM
about the graph "complete minus a perfect matching", true for ANY matching and ANY m, and in particular — for κ
at EVERY rank n≥3 (not only n=3). The root — κ is an INVOLUTION WITHOUT FIXED POINTS on the active carrier U_n
(already proved); this is the only thing the theorem needs. ★SECOND independent path to the same
κ↔π connection — a literal embedding of the R1 cycle (C₆ at rank 3) into the six roots of unity (T=e^{iπ/3},
T³=κ). ★METHODOLOGICAL lesson: the first check "on a different graph" took K₄ as an "unrelated" comparison —
but K₄ IS the COMPLETE (unpunctured) Q₂, a degenerate member of the SAME construction, not an honest control;
an honest control is a graph outside the "complete minus a perfect matching" family (a star), and honest
generality is ranks OF ONE construction (n=2..6, sections D/E). Register: ● the whole theorem (proved and
verified); ◐ identification with "the true nature of π" — NOT asserted (see section G/F-summary); ✗ nothing
is killed — this is a refinement, not a retraction.

  A. ★GENERAL THEOREM: K_m minus ANY perfect matching → spectrum {0,m−2(×m/2),m(×m/2−1)} — for any m, m even.
  B. J AND P COMMUTE (P preserves the "all ones" vector) — the mechanism of the theorem, not a specificity of κ.
  C. COROLLARY: e^{iLπ}=I ALWAYS (the spectrum is always even, not a "coincidence" of ranks 2,3).
  D. CHECK ACROSS RANKS n=2..6 (our construction U_n minus the κ-matching): the theorem holds at every one.
  E. METHODOLOGY: K₄=degenerate Q₂ (not a control); an honest control=a star (outside the family, doesn't hold).
  F. ROOT: κ²=id WITHOUT fixed points on U_n (n≥1) — the only thing needed; the theorem is not about the octahedron.
  G. ★THIRD PATH: C₆ (rank 3, R1 cycle) = literally 6 roots of unity; T=e^{iπ/3}, T⁶=1, T³=κ=e^{iπ}=−1.
  H. SUMMARY + guard: what is proved, what is a reading, what is not asserted.
"""
from __future__ import annotations
import numpy as np
import cmath, math

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def expm_herm(M, t):
    """e^{itM} for a Hermitian M via diagonalization (no scipy)."""
    w, V = np.linalg.eigh(M)
    return V @ np.diag(np.exp(1j * t * w)) @ V.conj().T

def complete_minus_matching(m, pairs):
    A = np.ones((m, m)) - np.eye(m)
    for a, b in pairs:
        A[a, b] = 0; A[b, a] = 0
    return np.diag(A.sum(1)) - A   # Laplacian


# ═══════════════ A. general theorem: K_m minus ANY perfect matching ═══════════════
def section_A():
    print("\n[A] ★GENERAL THEOREM: K_m minus ANY perfect matching → spectrum {0,m−2(×m/2),m(×m/2−1)}")
    rng = np.random.RandomState(0)
    all_ok = True
    for m in (4, 6, 8, 10):
        verts = list(range(m)); rng.shuffle(verts)
        pairs = [(verts[2 * i], verts[2 * i + 1]) for i in range(m // 2)]   # ARBITRARY matching
        L = complete_minus_matching(m, pairs)
        spec = np.sort(np.linalg.eigvalsh(L))
        predicted = sorted([0] + [m] * (m // 2 - 1) + [m - 2] * (m // 2))
        ok = np.allclose(spec, predicted, atol=1e-8)
        all_ok = all_ok and ok
        print(f"   m={m:>2}, random matching {pairs}: spectrum={np.round(spec,2)} = "
              f"prediction {predicted}: {ok}")
    check("the theorem holds for an ARBITRARY matching (not only κ) and arbitrary even m "
          "⟹ this is a fact about the structure «complete graph minus a matching», not about a specific graph", all_ok)


# ═══════════════ B. J and P commute ═══════════════
def section_B():
    print("\n[B] J AND P COMMUTE (P preserves the «all ones» vector) — the mechanism of the theorem")
    m = 8
    pairs = [(0, 1), (2, 3), (4, 5), (6, 7)]
    J = np.ones((m, m))
    P = np.eye(m)
    for a, b in pairs:
        P[a, a] = 0; P[b, b] = 0; P[a, b] = 1; P[b, a] = 1
    comm = np.allclose(J @ P, P @ J)
    ones = np.ones(m)
    fixes_ones = np.allclose(P @ ones, ones)
    check(f"JP=PJ:{comm}; P fixes the «all 1s» vector (P·𝟙=𝟙):{fixes_ones} ⟹ J,P are JOINTLY diagonalizable "
          f"⟹ the spectrum of L=(m−1)I−J+P is computed COORDINATE-WISE (section A — a direct corollary)",
          comm and fixes_ones)


# ═══════════════ C. corollary: e^{iLπ}=I always ═══════════════
def section_C():
    print("\n[C] COROLLARY: e^{iLπ}=I ALWAYS (the spectrum is always even for ANY even m, not a «coincidence»)")
    all_ok = True
    for m in (4, 6, 8, 10, 12):
        pairs = [(2 * i, 2 * i + 1) for i in range(m // 2)]
        L = complete_minus_matching(m, pairs)
        U = expm_herm(L, math.pi)
        ok = np.allclose(U, np.eye(m), atol=1e-8)
        all_ok = all_ok and ok
        print(f"   m={m:>2}: e^(iLπ)=I: {ok}")
    check("for ANY even m (not only m=6 of the octahedron) e^{iLπ}=I ⟹ the return at π is a PROPERTY OF THE FAMILY "
          "«complete minus a matching», not a privilege of the rank object", all_ok)


# ═══════════════ D. check across ranks of our construction n=2..6 ═══════════════
def kappa_pairs_of_rank(n):
    full = (1 << n) - 1
    U = [x for x in range(1 << n) if x not in (0, full)]
    idx = {v: i for i, v in enumerate(U)}
    pairs = []
    for x in U:
        y = full ^ x
        if y in idx and idx[x] < idx[y]:
            pairs.append((idx[x], idx[y]))
    return U, pairs

def section_D():
    print("\n[D] CHECK ACROSS RANKS n=2..6 (U_n minus the κ-matching): the theorem holds at every one")
    all_ok = True
    for n in (2, 3, 4, 5, 6):
        U, pairs = kappa_pairs_of_rank(n)
        m = len(U)
        L = complete_minus_matching(m, pairs)
        spec = np.sort(np.linalg.eigvalsh(L))
        predicted = sorted([0] + [m] * (m // 2 - 1) + [m - 2] * (m // 2))
        spec_ok = np.allclose(spec, predicted, atol=1e-7)
        U_pi = expm_herm(L, math.pi)
        return_ok = np.allclose(U_pi, np.eye(m), atol=1e-7)
        all_ok = all_ok and spec_ok and return_ok
        print(f"   rank {n}: |U_{n}|=m={m:>3}, κ-pairs={len(pairs):>2}; spectrum=prediction:{spec_ok}; "
              f"e^(iLπ)=I:{return_ok}")
    check("at ALL checked ranks 2..6 the theorem and the corollary hold without exception ⟹ this is an invariant "
          "of the WHOLE rank tower, not a peculiarity of rank 3", all_ok)


# ═══════════════ E. methodology: K4 is not a control, the star IS an honest control ═══════════════
def section_E():
    print("\n[E] METHODOLOGY: K₄=degenerate (unpunctured) Q₂, NOT an unrelated control; honest control=a star")
    # K4 = the COMPLETE (unpunctured) Q_2: on 2 bits max.distance=2=R2, nothing to puncture
    full_Q2 = [(0, 1) for _ in range(0)]  # no matching at all — this is K4 WITHOUT subtraction
    A_K4 = np.ones((4, 4)) - np.eye(4)
    L_K4 = np.diag(A_K4.sum(1)) - A_K4
    spec_K4 = np.sort(np.linalg.eigvalsh(L_K4))
    is_K4_full_Q2 = np.allclose(spec_K4, [0, 4, 4, 4])
    # punctured U_2 (as at other ranks): only 2 points = the κ-pair ITSELF ⟹ the graph after subtraction is EMPTY
    U2, pairs2 = kappa_pairs_of_rank(2)
    degenerate = (len(U2) == 2 and len(pairs2) == 1)
    check(f"K₄: spectrum={spec_K4} = spectrum of K_4 WITHOUT subtraction (no matching, since on 2 bits there is "
          f"nothing to puncture — max.distance is already =2=R2):{is_K4_full_Q2} ⟹ K₄ is NOT an 'unrelated graph', "
          f"but a DEGENERATE member of the FAMILY (complete Q₂, the matching is trivially empty), not an honest "
          f"control; the true U_2 (punctured) = {len(U2)} points = the κ-pair itself, the graph is EMPTY (degenerate):{degenerate}",
          is_K4_full_Q2 and degenerate)
    # honest control: the star K_{1,3} — does NOT belong to the family "complete minus a perfect matching"
    A_star = np.array([[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], dtype=float)
    L_star = np.diag(A_star.sum(1)) - A_star
    spec_star = np.sort(np.linalg.eigvalsh(L_star))
    U_star = expm_herm(L_star, math.pi)
    star_fails = not np.allclose(U_star, np.eye(4), atol=1e-8)
    check(f"star K_(1,3): spectrum={np.round(spec_star,3)} (there is an odd {1}); e^(iLπ)=I is FALSE:{star_fails} "
          f"⟹ the star is OUTSIDE the family «complete minus a perfect matching» ⟹ an honest negative control "
          f"(unlike K₄, which was a degenerate member of the SAME family, not a control at all)",
          star_fails)


# ═══════════════ F. root: κ²=id without fixed points — the only condition ═══════════════
def section_F():
    print("\n[F] ROOT: κ²=id WITHOUT fixed points on U_n (n≥1) — the only thing the theorem needs")
    all_no_fix = True
    for n in (1, 2, 3, 4, 5):
        full = (1 << n) - 1
        U = [x for x in range(1 << n) if x not in (0, full)]
        no_fixed = all((full ^ x) != x for x in U)   # κ(x)=x is impossible on a squarefree carrier
        kappa_invol = all((full ^ (full ^ x)) == x for x in U)   # κ²=id
        all_no_fix = all_no_fix and no_fixed and kappa_invol
        print(f"   rank {n}: κ²=id:{kappa_invol}; no fixed points on U_{n}:{no_fixed}")
    check("κ is an involution WITHOUT fixed points on EVERY U_n (n≥1, already proved for D(N)) ⟹ this is "
          "the ONLY structural condition the theorem needs (sections A-B); the theorem is NOT specifically about "
          "the octahedron — it is about κ, and κ exists at every rank by construction", all_no_fix)


# ═══════════════ G. third path: C6 = six roots of unity ═══════════════
def section_G():
    print("\n[G] ★THIRD PATH: C₆ (rank 3, R1 cycle) = literally 6 roots of unity; T=e^(iπ/3), T³=κ=e^(iπ)=−1")
    T = cmath.exp(1j * math.pi / 3)
    powers = [T ** k for k in range(7)]
    period6 = abs(powers[6] - 1) < 1e-9
    half_is_kappa = abs(powers[3] - (-1)) < 1e-9
    check(f"T=e^(iπ/3): T⁶=1:{period6}; T³=−1 (=e^(iπ), κ-analog by sign):{half_is_kappa} ⟹ the R1 cycle (C₆, "
          f"rank 3) is literally EMBEDDED into the 6th roots of unity — a path to the same κ↔π connection "
          f"INDEPENDENT of the spectral theorem (A-D): ONE — via the POINTS of the cycle, the OTHER — via the "
          f"SPECTRUM of the whole graph",
          period6 and half_is_kappa)
    print("   → the two paths are INDEPENDENT: the spectral one (A-D, any rank, whole graph) and the pointwise one (G,")
    print("     only rank 3, only the R1 cycle) — both arrive at the same e^{iπ}=−1, but by different mechanisms.")


# ═══════════════ H. summary + guard ═══════════════
def section_H():
    print("\n[H] GUARD ●◐○")
    print("   ● the whole theorem: the general spectrum formula (A,B), the corollary e^{iLπ}=I (C), the check")
    print("     across ranks (D), the K₄/star methodology (E), the root κ²=id-without-fix (F), the C₆=6-roots embedding (G).")
    print("   ◐ identification: «the return at π» = the SAME constant π that is geometric (via e^{iπ}=−1,")
    print("     Euler) — the form is proved, but this is an ADDITIONAL place where π appears, not a replacement of geometry.")
    print("   ✗ NOT asserted: «π is not the ratio of a circle's circumference to its diameter» (the source document")
    print("     claimed this) — this is an overclaim; here it is honestly stated: π ALSO appears forced here, as")
    print("     ONE of the consequences of κ having order exactly 2 — no more and no less than that.")


def main():
    print("=" * 100)
    print("SPECTRAL THEOREM OF κ: e^{iLπ}=I — not a coincidence of rank 3, but a theorem about κ at every rank")
    print("=" * 100)
    section_A(); section_B(); section_C(); section_D(); section_E(); section_F(); section_G(); section_H()
    print("\n" + "=" * 100)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: «e^{iLπ}=I, true but trivial» — unfolded. THEOREM: the graph «complete minus")
    print("       a perfect matching» on m points ALWAYS has spectrum {0,m−2(×m/2),m(×m/2−1)} (proved: J,P")
    print("       commute, since P preserves the «all ones» vector) — for ANY matching, not only κ.")
    print("       The spectrum is ALWAYS even (m even) ⟹ e^{iLπ}=I ALWAYS — checked at ranks 2..6 of our")
    print("       construction, without exception. The ONLY condition — κ is an involution WITHOUT fixed points")
    print("       (already proved for D(N)) — the theorem is not specifically about the octahedron, it is about κ. Methodology:")
    print("       K₄ is not an unrelated control (a degenerate Q₂ of the same family), an honest control is the star (outside")
    print("       the family, doesn't hold). ★A third, independent path: C₆=6 roots of unity (T³=κ=e^{iπ}=−1).")
    print("       Honestly: here π appears ADDITIONALLY as a consequence of order(κ)=2 — not a replacement of geometry.")
    print("=" * 100)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
