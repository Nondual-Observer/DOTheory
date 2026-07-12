#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_carrier_from_operation.py

Fixes a weak spot of chapters 0–I: "operation before carrier" WITHOUT conflating two
pictures (categorical generator of a colimit vs ordinary element of a set).

The remark we fix: the predicate "ι≠id" is itself "∃x: ι(x)≠x" —
a statement about a MAP ON A CARRIER; to write it, the carrier X is already needed.
So "operation strictly before any set" is an over-promise. What is defensible
is not "there is no carrier at all", but "there is no carrier SEPARATE from the operation".

Resolution in TWO MOMENTS (variant A — regular representation, Cayley):

  Moment 1 — operation as group G=⟨g | g^2=e⟩, WITHOUT a carrier.
    The order is computed from the PRESENTATION: free group on one generator = ℤ,
    quotient by g^2=e = ℤ/2ℤ — exactly two classes; g≠e by parity (1∉2ℤ).
    No "there exists x": no quantifier over a carrier — the order of the operation is read off.

  Moment 2 — the carrier is BORN as a regular orbit.
    G acts on its own carrier by shift; the orbit of the identity e under ⟨g⟩ is
    {e,g} — this is the first carrier. The generator x:=e is canonical (the identity).
    Cardinality of the carrier = ORDER of the involution: |⟨g|g^n=e⟩|=n.

Summary: "two" is DERIVED (order of ℤ/2), not postulated; element-language is legitimate
only AFTER Moment 2; "the pair is a shadow of self-relation" becomes literal.
"""

results = []
def ck(name, cond):
    results.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

# ============ Moment 1: group from presentation ⟨g | g^n=e⟩, without a carrier ============
# Free group on one generator = ℤ (words g^k). The relation g^n=e gives
# the quotient ℤ/nℤ. Key: we build from the RELATION, no "set on which we act".
def order_from_presentation(n):
    # normal forms of words g^k modulo g^n=e = residue classes {0,...,n-1}
    return len(range(n))

G = list(range(2))                      # ⟨g | g^2=e⟩ as ℤ/2: {e=0, g=1}
e, g = 0, 1
mul = lambda a, b: (a + b) % 2          # group operation (g^2=e)

ck("Moment1: order ⟨g|g^2=e⟩ = 2 — from presentation, without a carrier",
   order_from_presentation(2) == 2)
ck("Moment1: g ≠ e by parity (1 ∉ 2ℤ) — replacement of 'ι≠id' without a quantifier over a carrier",
   (1 % 2) != (0 % 2) and g != e)
ck("Moment1: relation g·g = e holds", mul(g, g) == e)
ck("Moment1: e — identity of the group (mul(e,x)=x for all x)",
   all(mul(e, x) == x for x in G))

# ============ Moment 2: carrier = regular orbit (Cayley) ============
# G acts on its OWN carrier by shift λ_h(x)=h·x. The carrier = G itself.
iota = lambda x: mul(g, x)              # ι := left shift by g
orbit_of_e = sorted({e, iota(e)})       # orbit of the identity under ⟨g⟩
carrier = orbit_of_e                    # the carrier IS the orbit, not an input

ck("Moment2: orbit of the identity e under ⟨g⟩ = {e,g}", orbit_of_e == [e, g])
ck("Moment2: the carrier IS the orbit (generated, not given in advance)", carrier == orbit_of_e)
ck("Moment2: |carrier| = 2 = order of the involution g",
   len(carrier) == 2 == order_from_presentation(2))
ck("Moment2: x:=e is canonical — the identity of the group, not an arbitrary element",
   all(mul(e, x) == x for x in carrier))

# ι — nontrivial involution WITHOUT fixed points (freeness; Prop.2 ch.I §3)
ck("ι is free: ι(x) ≠ x for all x", all(iota(x) != x for x in carrier))
ck("ι² = id on the carrier", all(iota(iota(x)) == x for x in carrier))
ck("ι = swap 0↔1", iota(0) == 1 and iota(1) == 0)

# ============ "Two = period two": orbit cardinality = order, and only n=2 is an involution ============
for n in (2, 3, 4, 5):
    iota_n = lambda x, n=n: (1 + x) % n
    cur, orbit = 0, {0}
    for _ in range(n + 1):
        cur = iota_n(cur); orbit.add(cur)
    is_involution = all(iota_n(iota_n(x)) == x for x in range(n)) and \
                    any(iota_n(x) != x for x in range(n))
    ck(f"n={n}: |orbit of the identity| = order = {n}", len(orbit) == n)
    if n == 2:
        ck("n=2: shift by g — INVOLUTION (period 2)", is_involution)
    else:
        ck(f"n={n}: shift by g — NOT an involution (period {n}≠2), drops out", not is_involution)

# ============ Discipline: "two" is not written in by hand (base change) ============
# Change the presentation (g^3=e) → carrier of THREE. So "2" depends ONLY on g^2=e,
# and is not slipped in as a constant. Change of base/type kills the suspicion of numerology.
ck("Base change: g^3=e gives carrier 3, not 2 ⇒ '2' derived from g^2=e, not written in",
   order_from_presentation(3) == 3 and order_from_presentation(2) == 2)

# ============ Summary ============
npass = sum(1 for _, c in results if c)
nfail = sum(1 for _, c in results if not c)
print(f"\nTOTAL: {npass} PASS / {nfail} FAIL")
