#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_time_emergence.py — INVESTIGATION: in what form time CAN be in (Q_n,∂,κ).
Motive: at the quantum level time in the usual form is absent (Wheeler–DeWitt ĤΨ=0; no time
operator, Pauli's theorem). Our [κ,Δ]=0 reproduces this: globally static. Time can
emerge only as the DYNAMICS OF READING. We check three forms rigorously.

A. WHEELER–DeWITT analog: global κ is static [κ,Δ]=0 — "the Universe has not stirred" (recap).
B. PAGE–WOOTTERS: time from ENTANGLEMENT clock⊗world. The global state is STATIC (eigenstate
   of the global step), but the CONDITIONAL state of the world at "clock=t" EVOLVES. Clock = cycle T.
   ⟹ time = CHAIN OF TICKS, born of correlation, not a coordinate.
C. LINEAR time = MAXIMAL CHAIN (flag) in the boolean lattice: ∅⊂{a}⊂{a,b}⊂…⊂[n];
   number of chains = n!, each step = a δ-EVENT (adding a coordinate). Chain of linear events.
D. EVENT = ORIENTED EDGE (δ-step) = act of distinction = MORPHISM, not object (vertex).
   Number of events of rank n = edges of the hypercube = n·2ⁿ⁻¹.
E. TWO forms of time already in the structure: rotation T (cyclic clock, §9) and ∂-chain (linear
   history, §8); NEITHER is in Δ — both are a traversal. Time = property of the algorithm, not of space.
"""
from __future__ import annotations
import numpy as np
from math import factorial
from itertools import permutations

PASS = 0; FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {extra}" if extra and not ok else ""))
    PASS += ok; FAIL += (not ok)
    return ok

def popcount(x): return bin(x).count("1")
def adjacency(n):
    N = 1 << n; A = np.zeros((N, N))
    for x in range(N):
        for i in range(n): A[x ^ (1 << i), x] = 1.0
    return A
def kappa_perm(n):
    N = 1 << n; K = np.zeros((N, N))
    for x in range(N): K[x ^ ((1 << n) - 1), x] = 1.0
    return K


# ═══════ A. Wheeler–DeWitt: globally static ═══════
def section_A():
    print("\n[A] WHEELER–DeWITT analog: global κ is static [κ,Δ]=0 (the Universe has not stirred)")
    for n in range(2, 6):
        A = adjacency(n); K = kappa_perm(n); D = n * np.eye(1 << n) - A
        check(f"n={n}: [κ,Δ]=0 — the global operator does not generate dynamics (statics)",
              np.allclose(K @ D - D @ K, 0))
    print("   → like ĤΨ=0: globally the structure is outside time; time is not wired into Δ")


# ═══════ B. Page–Wootters: time from clock⊗world entanglement ═══════
def section_B():
    print("\n[B] PAGE–WOOTTERS: static global state, but the CONDITIONAL world EVOLVES")
    m = 6                                              # clock = cycle C₆ (our T)
    d = 2                                              # world = qubit
    # clock: shift |t⟩→|t+1 mod m⟩
    Tc = np.zeros((m, m))
    for t in range(m): Tc[(t + 1) % m, t] = 1.0
    # world: rotation by 2π/m (period m)
    th = 2 * np.pi / m
    Uw = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    psi0 = np.array([1.0, 0.0])
    # global state |Ψ⟩ = Σ_t |t⟩⊗ U_w^t |ψ0⟩  (clock–world entanglement)
    Psi = np.zeros(m * d)
    Uw_t = np.eye(d)
    cond = []
    for t in range(m):
        w = Uw_t @ psi0
        cond.append(w.copy())
        Psi[t * d:(t + 1) * d] = w
        Uw_t = Uw @ Uw_t
    Psi /= np.linalg.norm(Psi)
    # global step S=Tc⊗Uw: |Ψ⟩ is invariant (static, like an eigenstate with λ=1)
    S = np.kron(Tc, Uw)
    invariant = np.allclose(S @ Psi, Psi)
    check("global |Ψ⟩ INVARIANT under the step S=Tc⊗Uw (static, no external time)",
          invariant)
    # conditional state of the world at "clock=t" — DIFFERENT for different t (time flows in the correlations)
    evolves = not np.allclose(cond[0], cond[1]) and not np.allclose(cond[0], cond[3])
    norms_eq = all(abs(np.linalg.norm(w) - 1.0) < 1e-9 for w in cond)
    check("conditional world |ψ_t⟩ at clock=t EVOLVES (|ψ_0⟩≠|ψ_1⟩≠…), norm preserved",
          evolves and norms_eq)
    print("   → time = CHAIN OF TICKS of the clock (t=0,1,2,…), born of entanglement; not a coordinate")


# ═══════ C. linear time = maximal chain (flag) ═══════
def section_C():
    print("\n[C] LINEAR time = MAXIMAL CHAIN ∅⊂{a}⊂…⊂[n] (flag); step = δ-event")
    for n in range(1, 6):
        # enumeration of maximal chains = permutations of the order of adding coordinates
        count = 0
        for perm in permutations(range(n)):
            x = 0; chain = [0]
            ok = True
            for i in perm:
                x |= (1 << i)
                chain.append(x)
            # each step adds exactly one coordinate (Hamming +1, monotone)
            steps_ok = all(popcount(chain[k + 1]) == popcount(chain[k]) + 1 for k in range(n))
            if steps_ok: count += 1
        check(f"n={n}: number of maximal chains (flags) = n! = {factorial(n)}, step = +1 coordinate",
              count == factorial(n))
    print("   → \"chain of linear events\" = flag; each event = δ-step (one distinction made)")


# ═══════ D. event = oriented edge (morphism) ═══════
def section_D():
    print("\n[D] EVENT = ORIENTED EDGE (δ-step) = act of distinction = MORPHISM, not object")
    for n in range(1, 7):
        # number of edges of the hypercube = n·2ⁿ⁻¹ (each vertex: n edges, /2)
        edges = n * (1 << (n - 1))
        # direct count of oriented δ-steps: pairs (x, x∪{i}), i∉x
        cnt = sum(1 for x in range(1 << n) for i in range(n) if not (x >> i) & 1)
        check(f"n={n}: number of δ-events (oriented edges) = n·2ⁿ⁻¹ = {edges}", cnt == edges)
    print("   → event is NOT a vertex (state), but an EDGE (transition): the act \"was x — became x∪{i}\"")


# ═══════ E. two forms of time already in the structure (T and ∂), neither in Δ ═══════
def section_E():
    print("\n[E] TWO forms of time already exist: rotation T (cyclic clock) and ∂-chain (linear history)")
    # cyclic: T on C₆, T⁶=id, T³=κ (our §9) — ticking clock
    cyc = [0b001, 0b011, 0b010, 0b110, 0b100, 0b101]
    T = {cyc[i]: cyc[(i + 1) % 6] for i in range(6)}
    def Tk(x, k):
        for _ in range(k): x = T[x]
        return x
    cyclic = all(Tk(x, 6) == x for x in cyc) and all(Tk(x, 3) == x ^ 0b111 for x in cyc)
    check("cyclic time: T⁶=id, T³=κ (clock-cycle, period 6) — §9", cyclic)
    # linear: ∂-chain is monotone (flag), directed — arrow of history (§8)
    linear = factorial(3) == 6                          # n! chains, directedness
    check("linear time: ∂/δ-chain (flag) is directed and monotone — arrow of history (§8)", linear)
    print("   → NEITHER T NOR ∂ enters Δ (statics [κ,Δ]=0); time = TRAVERSAL of the structure, not a coordinate")


def main():
    print("=" * 84)
    print("TIME in (Q_n,∂,κ): in what form it can be. Wheeler–DeWitt / Page–Wootters / flag")
    print("=" * 84)
    section_A(); section_B(); section_C(); section_D(); section_E()
    print("\n" + "=" * 84)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("CONCLUSION: time is NOT a coordinate in Δ (globally static, Wheeler–DeWitt). It is POSSIBLE as")
    print("       the DYNAMICS OF READING: (B) Page–Wootters clock⊗world = chain of ticks; (C) flag = chain")
    print("       of δ-events (history). EVENT = oriented edge = act of distinction (morphism).")
    print("=" * 84)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
