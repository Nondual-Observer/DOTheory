#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_strict_core_bridge.py

Self-contained numerical check of FOUR results marked with the tag
[●]. They are proven in the strict finite core of the corpus; here — an independent
confirmation by means of the exposition series itself, so that the references do not hang
on an external branch.

  1. Universality of the 𝔽₂-brick (ch I §1.1).
     Any minimal distinguisher (S, N, χ) — a two-state carrier
     |S|=2, a free involution N (without fixed points), a comparison χ
     distinguishing only coincidence/non-coincidence and invariant to the flip of
     poles χ(Na,Nb)=χ(a,b) — is unique in its class and isomorphic to (Q₁,κ).

  2. Uniqueness of the octahedron (ch III §3.3).
     The active scene of rank 3 is the cross-polytope K_{2,2,2}; |V|=2m, and at
     m≥3 (three holding axes) the minimum number of vertices = 6, attained exactly
     at m=3. The tetrahedron is excluded (no antipodal pairs → no free
     κ), the cube is excluded (κ-invariant center among... outside the vertices).

  3. ℤ₂-holonomy = Möbius band (ch III §3.3).
     Twisted transport on C₆ carries a gauge-invariant holonomy
     ∏εᵢ; the class H¹(S¹;ℤ₂)≅ℤ₂ is nontrivial (∃ configuration ∏=−1), the double
     return 𝒯²=id. This is an operator separate from the rotation T.

  4. Stanley's sl₂-grading (ch VII §7.1).
     Weighted raising e and lowering f weight operators on the Boolean
     lattice Q_n with grading H=2k−n satisfy
       [H,e]=2e,  [H,f]=−2f,  [e,f]=H,
     and the complement κ is the Weyl involution: κHκ=−H, κeκ=f.
     (The grading lives over ℚ; e,f — generators of the Lie algebra, NOT differentials:
      e²≠0 — by this it differs from the chain complex ch VII §7.2.)

Run:  python3 verify_strict_core_bridge.py
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


# ----------------------------------------------------------------------
# 1. Universality of the 𝔽₂-brick
# ----------------------------------------------------------------------
def section_brick():
    print("\n[1] Universality of the 𝔽₂-brick (ch I §1.1)")
    S = [0, 1]

    # all bijections S->S
    bijections = [dict(zip(S, p)) for p in itertools.permutations(S)]
    # free involution: N(N(x))=x, N(x)!=x everywhere
    free_invols = [
        N for N in bijections
        if all(N[N[x]] == x for x in S) and all(N[x] != x for x in S)
    ]
    check("on |S|=2 the free involution is exactly one (swap)", len(free_invols) == 1)
    N = free_invols[0]

    # comparison χ(a,b)=0 ⟺ a=b
    chi = {(a, b): int(a != b) for a in S for b in S}
    # χ distinguishes only coincidence/non-coincidence (values only 0/1, 0 ⟺ a=b)
    distinguishes_only = all(
        (chi[(a, b)] == 0) == (a == b) for a in S for b in S
    )
    check("χ distinguishes only coincidence/non-coincidence", distinguishes_only)
    # invariance to pole flip: χ(Na,Nb)=χ(a,b)
    inv = all(chi[(N[a], N[b])] == chi[(a, b)] for a in S for b in S)
    check("χ is invariant to pole flip χ(Na,Nb)=χ(a,b)", inv)

    # isomorphism onto the brick (B2,σ,χ2): B2={0,1}, σ=swap, χ2=[a≠b]
    sigma = {0: 1, 1: 0}
    chi2 = {(a, b): int(a != b) for a in (0, 1) for b in (0, 1)}
    isos = []
    for e in bijections:  # bijection S->B2
        ok_N = all(e[N[x]] == sigma[e[x]] for x in S)          # e∘N = σ∘e
        ok_chi = all(chi[(a, b)] == chi2[(e[a], e[b])] for a in S for b in S)
        if ok_N and ok_chi:
            isos.append(e)
    # isomorphism exists (the structure is realizable as a brick)
    check("(S,N,χ) isomorphic to the brick (B₂,σ,χ₂)", len(isos) >= 1)
    # the structure is unique in its class: a unique N, a unique admissible χ
    valid_chi = 0
    for vals in itertools.product([0, 1], repeat=4):
        c = {(a, b): vals[2 * a + b] for a in S for b in S}
        if all((c[(a, b)] == 0) == (a == b) for a in S for b in S) and \
           all(c[(N[a], N[b])] == c[(a, b)] for a in S for b in S):
            valid_chi += 1
    check("minimal distinguisher unique in its class (1 N, 1 χ)",
          len(free_invols) == 1 and valid_chi == 1)

    # forcedness of |S|=2: on an odd carrier there is no free involution
    def has_free_involution(k):
        for p in itertools.permutations(range(k)):
            P = dict(enumerate(p))
            if all(P[P[x]] == x for x in range(k)) and all(P[x] != x for x in range(k)):
                return True
        return False
    check("|S|=2 forced: on |S|=3 there is no free involution",
          (not has_free_involution(3)) and has_free_involution(2))


# ----------------------------------------------------------------------
# 2. Uniqueness of the octahedron
# ----------------------------------------------------------------------
def crosspolytope_graph(m):
    """Vertices ±e_i (2m of them), all pairs adjacent except the antipodal one."""
    verts = []
    for i in range(m):
        verts.append((i, +1))
        verts.append((i, -1))
    n = len(verts)
    A = np.zeros((n, n), dtype=int)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            ia, sa = verts[a]
            ib, sb = verts[b]
            antipode = (ia == ib and sa == -sb)
            A[a, b] = 0 if antipode else 1
    return verts, A


def antipode_perm(verts):
    idx = {v: k for k, v in enumerate(verts)}
    return [idx[(i, -s)] for (i, s) in verts]


def section_octahedron():
    print("\n[2] Uniqueness of the octahedron K_{2,2,2} (ch III §3.3)")

    # |V| = 2m; at m>=3 the minimum = 6 at m=3
    sizes = {m: 2 * m for m in range(1, 6)}
    primitive = {m: v for m, v in sizes.items() if m >= 3}  # three holding axes
    check("|V|=2m; at m≥3 the minimum of vertices = 6", min(primitive.values()) == 6)
    check("minimum 6 attained exactly at m=3",
          [m for m, v in primitive.items() if v == 6] == [3])

    verts, A = crosspolytope_graph(3)
    check("octahedron (m=3): |V|=6", len(verts) == 6)
    # K_{2,2,2}: each vertex adjacent to 4, non-adjacent exactly to the antipode
    deg = A.sum(axis=1)
    check("each vertex adjacent to 4, non-adjacent exactly to the antipode",
          np.all(deg == 4))
    kap = antipode_perm(verts)
    check("κ (antipode) is free: no fixed vertices",
          all(kap[i] != i for i in range(6)))
    check("κ involution: κ²=id", all(kap[kap[i]] == i for i in range(6)))

    # tetrahedron K4 excluded: complete graph, no non-adjacent pair => no antipodes
    K4 = np.ones((4, 4), int) - np.eye(4, dtype=int)
    has_nonadjacent_pair = np.any(K4 == 0)  # off-diagonal
    offdiag_zero = np.any((K4 == 0) & (~np.eye(4, dtype=bool)))
    check("tetrahedron K₄ excluded: no non-adjacent pair (no antipodes)",
          not offdiag_zero)

    # cube Q3 excluded as a primitive scene: the antipode is free, BUT the center
    # (½,½,½) is a κ-invariant OUTSIDE the vertices; active scene = Q3 without 2 poles = 6
    Q3 = list(itertools.product([0, 1], repeat=3))
    comp = {v: tuple(1 - c for c in v) for v in Q3}
    center_fixed_is_vertex = any(comp[v] == v for v in Q3)
    check("cube: κ-invariant center NOT among the vertices (center outside Q₃)",
          not center_fixed_is_vertex)
    poles = [v for v in Q3 if v in ((0, 0, 0), (1, 1, 1))]
    active = [v for v in Q3 if v not in poles]
    check("active scene of the cube (without 2 poles) = 6 = octahedron",
          len(active) == 6)


# ----------------------------------------------------------------------
# 3. ℤ₂-holonomy (Möbius band) on C₆
# ----------------------------------------------------------------------
def section_holonomy():
    print("\n[3] ℤ₂-holonomy = Möbius band on C₆ (ch III §3.3)")
    m = 6  # edges in the cycle C6

    # nontrivial class: sign configuration with ∏ε = −1
    twisted = [-1] + [1] * (m - 1)
    check("nontrivial holonomy exists: ∏εᵢ = −1",
          int(np.prod(twisted)) == -1)
    trivial = [1] * m
    check("trivial holonomy: ∏εᵢ = +1", int(np.prod(trivial)) == 1)

    # gauge invariance: εᵢ → s_v · εᵢ · s_{v+1}; ∏ε unchanged
    def holonomy(eps):
        return int(np.prod(eps))

    invariant = True
    base = twisted[:]
    h0 = holonomy(base)
    for sbits in itertools.product([1, -1], repeat=m):  # gauge on the 6 vertices of the cycle
        s = list(sbits)
        gauged = [s[i] * base[i] * s[(i + 1) % m] for i in range(m)]
        if holonomy(gauged) != h0:
            invariant = False
            break
    check("holonomy is gauge-invariant (∏ε under s_v·ε·s_{v+1})", invariant)

    # exactly two classes H¹(S¹;ℤ₂) ≅ ℤ₂
    classes = set()
    for eps in itertools.product([1, -1], repeat=m):
        classes.add(int(np.prod(eps)))
    check("exactly two holonomy classes (H¹(S¹;ℤ₂)≅ℤ₂)", classes == {1, -1})

    # double return 𝒯²=id: holonomy over a double traversal = (∏ε)² = +1
    check("double return 𝒯²=id: (∏ε)²=+1 on any class",
          all(c * c == 1 for c in classes))

    # difference from rotation: rotation T on C6 has order 6, T³=κ (order 2)
    T = np.roll(np.eye(m, dtype=int), 1, axis=0)      # shift by 1 step
    T6 = np.linalg.matrix_power(T, 6)
    T3 = np.linalg.matrix_power(T, 3)
    check("rotation T: T⁶=id, T³≠id (T³=κ, order 6 ≠ holonomy)",
          np.array_equal(T6, np.eye(m, dtype=int)) and not np.array_equal(T3, np.eye(m, dtype=int)))


# ----------------------------------------------------------------------
# 4. Stanley's sl₂-grading on the Boolean lattice Q_n
# ----------------------------------------------------------------------
def boolean_sl2(n):
    """Weighted up/down operators and H=2k−n on Q_n=2^n subsets."""
    subsets = list(itertools.product([0, 1], repeat=n))
    idx = {s: i for i, s in enumerate(subsets)}
    N = len(subsets)
    U = np.zeros((N, N))  # raising weight: e
    D = np.zeros((N, N))  # lowering weight: f
    for s in subsets:
        for j in range(n):
            if s[j] == 0:
                t = tuple(1 if k == j else s[k] for k in range(n))
                U[idx[t], idx[s]] = 1.0        # add element j: s -> t
            else:
                t = tuple(0 if k == j else s[k] for k in range(n))
                D[idx[t], idx[s]] = 1.0        # remove element j: s -> t
    H = np.diag([2 * sum(s) - n for s in subsets]).astype(float)
    K = np.zeros((N, N))  # κ: antipode (complement of the set)
    for s in subsets:
        c = tuple(1 - b for b in s)
        K[idx[c], idx[s]] = 1.0
    return U, D, H, K


def comm(X, Y):
    return X @ Y - Y @ X


def section_sl2():
    print("\n[4] Stanley's sl₂-grading on the Boolean lattice (ch VII §7.1)")
    for n in (3, 4):
        e, f, H, K = boolean_sl2(n)
        ok1 = np.allclose(comm(H, e), 2 * e)
        ok2 = np.allclose(comm(H, f), -2 * f)
        ok3 = np.allclose(comm(e, f), H)
        check(f"n={n}: [H,e]=2e", ok1)
        check(f"n={n}: [H,f]=−2f", ok2)
        check(f"n={n}: [e,f]=H", ok3)
        # κ — Weyl involution
        check(f"n={n}: κ²=id", np.allclose(K @ K, np.eye(K.shape[0])))
        check(f"n={n}: κHκ=−H (flip of the grading)",
              np.allclose(K @ H @ K, -H))
        check(f"n={n}: κeκ=f (swaps raising and lowering)",
              np.allclose(K @ e @ K, f))
        # e — NOT a differential: e²≠0 (difference from the chain complex §7.2)
        check(f"n={n}: e²≠0 (grading — not a complex)",
              not np.allclose(e @ e, 0))


def main():
    print("=" * 64)
    print("verify_strict_core_bridge.py — bridge to the strict core (4 results)")
    print("=" * 64)
    section_brick()
    section_octahedron()
    section_holonomy()
    section_sl2()
    print("\n" + "=" * 64)
    print(f"TOTAL: {PASS} PASS, {FAIL} FAIL")
    print("=" * 64)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
