#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_seam_structure.py — structure of the seam |·|₂/|·|∞ (chapter VII "The Underside").

A pure structural check, without the physical projection (mass/Λ — separate).

  [A] Sphere theorem: a vertex-transitive scene figure (octahedron, cube) ⟹ all
      vertices are equidistant from the center (on one sphere), the mean resistance
      R̄(v) is constant ⟹ the radial coordinate has zero variance on the vertices,
      i.e. it lies outside the graph. Center σ½ = the unique point r=0.

  [B] Split of the underside: a symmetric figure (κ exact) → vertices on the sphere;
      a broken symmetry (antipode weight unequal) → vertices leave the sphere ONLY
      along the broken axis (axial dipole), across it they remain on the sphere.
      The anisotropic (axial) part is derivable from the break; the isotropic radial
      background does not depend on the break = the axiom of the underside.

Run:  python3 verify_seam_structure.py
Dependencies: numpy.
"""

import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    ok = bool(cond)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def mean_resistance(A):
    n = A.shape[0]
    L = np.diag(A.sum(1)) - A
    Lp = np.linalg.pinv(L)
    R = np.array([[Lp[u, u] + Lp[v, v] - 2 * Lp[u, v] for v in range(n)] for u in range(n)])
    return R.sum(1) / (n - 1)


def A_octahedron():
    P = [(i, s) for i in range(3) for s in (1, -1)]
    A = np.zeros((6, 6))
    for a, (i, s) in enumerate(P):
        for b, (j, t) in enumerate(P):
            if a != b and not (i == j and s == -t):
                A[a, b] = 1.0
    return A


def A_cube():
    cl = list(itertools.product([0, 1], repeat=3))
    A = np.zeros((8, 8))
    for a, x in enumerate(cl):
        for b, y in enumerate(cl):
            if sum(p != q for p, q in zip(x, y)) == 1:
                A[a, b] = 1.0
    return A


def section_sphere_theorem():
    print("\n[A] Sphere theorem — radius lies outside the graph (observer = r=0)")
    oct_c = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0],
                      [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)
    r_oct = np.linalg.norm(oct_c - oct_c.mean(0), axis=1)
    check("octahedron: all vertices on a sphere of one radius from the center", np.allclose(r_oct, r_oct[0]))

    cube_c = np.array(list(itertools.product([0, 1], repeat=3)), float)
    r_cube = np.linalg.norm(cube_c - cube_c.mean(0), axis=1)
    check("cube: all vertices on a sphere (radius √¾ from the center σ½)",
          np.allclose(r_cube, r_cube[0]) and abs(r_cube[0] - np.sqrt(0.75)) < 1e-12)

    check("octahedron: mean resistance R̄(v) = const (no distinguished vertex)",
          np.allclose(mean_resistance(A_octahedron()), mean_resistance(A_octahedron())[0]))
    check("cube: R̄(v) = const",
          np.allclose(mean_resistance(A_cube()), mean_resistance(A_cube())[0]))

    check("radial coordinate: zero variance on the vertices ⟹ lies outside the graph",
          np.std(r_oct) < 1e-12 and np.std(r_cube) < 1e-12)
    print("   → the center σ½ is r=0 — the unique point outside the sphere (the observer, by the theorem)")


def section_split():
    print("\n[B] Split of the underside — the axial (break) part is derivable, the radial part is an axiom")
    oct_c = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0],
                      [0, -1, 0], [0, 0, 1], [0, 0, -1]], float)

    def radii(weights):
        c = (weights[:, None] * oct_c).sum(0) / weights.sum()
        return np.linalg.norm(oct_c - c, axis=1)

    # symmetry exact
    check("symmetry exact (equal weights): vertices on the sphere, std r=0",
          np.std(radii(np.ones(6))) < 1e-12)
    # symmetry break along axis 0
    w = np.ones(6)
    w[0], w[1] = 1.6, 0.4
    r = radii(w)
    axial = abs(r[0] - r[1])
    transverse = abs(r[2] - r[4])
    check("break: axial dipole r(+e₀)≠r(−e₀) — leaves the sphere along the broken axis", axial > 1e-3)
    check("break: across it r(+e₁)=r(+e₂) — remain on the sphere (the break is exactly axial)", transverse < 1e-12)
    print(f"   axial deviation |Δr|={axial:.3f}, transverse={transverse:.3f}")
    print("   → the axial part of the underside = the shape of the symmetry break (derivable);")
    print("     the isotropic radial background does not depend on the break = the axiom of the underside")


def main():
    print("=" * 60)
    print("verify_seam_structure.py — structure of the seam (chapter VII \"The Underside\")")
    print("=" * 60)
    section_sphere_theorem()
    section_split()
    print("\n" + "=" * 60)
    print(f"SUMMARY: {PASS} PASS, {FAIL} FAIL")
    print("=" * 60)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
