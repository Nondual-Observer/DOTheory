"""DOT v22: descent/gluing, closure composition, and minimal memory."""

from itertools import combinations, product
from math import gcd, lcm

# ---------- helpers ----------
def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def block_product(blocks, idxset):
    z = 1
    for i in idxset:
        z *= blocks[i]
    return z

# ---------- I. divisor descent / gluing ----------
def check_divisor_descent():
    # Pairwise coprime prime-power blocks; not necessarily squarefree.
    blocks = (4, 9, 5)  # 2^2, 3^2, 5
    N = 4*9*5
    patches = (frozenset((0,1)), frozenset((0,2)), frozenset((1,2)))
    patch_moduli = [block_product(blocks, S) for S in patches]
    patch_divs = [divisors(m) for m in patch_moduli]

    compatible_count = 0
    for local in product(*patch_divs):
        ok = True
        for i,j in combinations(range(len(patches)),2):
            inter = patches[i] & patches[j]
            m_inter = block_product(blocks, inter)
            if gcd(local[i], m_inter) != gcd(local[j], m_inter):
                ok = False
                break
        if not ok:
            continue
        compatible_count += 1
        glued = lcm(*local)
        assert glued in divisors(N)
        for val, mod in zip(local, patch_moduli):
            assert gcd(glued, mod) == val

        # Uniqueness by brute force.
        pre = [
            d for d in divisors(N)
            if all(gcd(d, mod) == val for val, mod in zip(local, patch_moduli))
        ]
        assert pre == [glued]

    # Every global divisor gives one compatible family, so number equals |Div(N)|.
    assert compatible_count == len(divisors(N))

def check_relation_pairwise_not_global():
    # Each binary relation projects surjectively to each one-bit overlap,
    # yet the three relations have no joint global state.
    Rxy = {(x,y) for x,y in product((0,1), repeat=2) if x^y == 0}
    Ryz = {(y,z) for y,z in product((0,1), repeat=2) if y^z == 0}
    Rzx = {(z,x) for z,x in product((0,1), repeat=2) if z^x == 1}
    assert {x for x,_ in Rxy} == {0,1}
    assert {y for _,y in Rxy} == {0,1}
    assert {y for y,_ in Ryz} == {0,1}
    assert {z for _,z in Ryz} == {0,1}
    assert {z for z,_ in Rzx} == {0,1}
    assert {x for _,x in Rzx} == {0,1}
    global_states = [
        (x,y,z) for x,y,z in product((0,1), repeat=3)
        if (x,y) in Rxy and (y,z) in Ryz and (z,x) in Rzx
    ]
    assert global_states == []

# ---------- II. closure composition ----------
def rule_closure(rules, universe):
    universe = frozenset(universe)
    def C(seed):
        s = set(seed)
        changed = True
        while changed:
            changed = False
            for prem, concl in rules:
                if prem <= s and concl not in s:
                    s.add(concl); changed = True
        return frozenset(s)
    return C

def check_noncommuting_one_pass():
    U = ("a","b","c")
    C1 = rule_closure([(frozenset(("a",)), "b")], U)
    C2 = rule_closure([(frozenset(("b",)), "c")], U)
    x = frozenset(("a",))
    # C1 after C2: first C2 sees no b, then C1 adds b.
    one = C1(C2(x))
    two = C1(C2(one))
    assert one == frozenset(("a","b"))
    assert two == frozenset(("a","b","c"))
    assert C1(C2(x)) != C2(C1(x))

def all_closure_operators_3():
    U = frozenset(range(3))
    subs = [frozenset(s) for r in range(4) for s in combinations(U,r)]
    families = []
    # Moore families: contain U and closed under arbitrary finite intersections;
    # on a finite ground set pairwise intersection is enough.
    for mask in range(1 << len(subs)):
        fam = {subs[i] for i in range(len(subs)) if mask >> i & 1}
        if U not in fam:
            continue
        if all((A & B) in fam for A in fam for B in fam):
            families.append(frozenset(fam))
    ops = []
    for fam in families:
        def make_op(fam):
            def C(A):
                supers = [F for F in fam if A <= F]
                z = set(U)
                for F in supers:
                    z &= set(F)
                return frozenset(z)
            return C
        ops.append(make_op(fam))
    return U, subs, ops

def check_closure_join_iteration():
    U, subs, ops = all_closure_operators_3()
    # Test every ordered pair of closure operators on P(3).
    for C,D in product(ops, repeat=2):
        for x in subs:
            seq = x
            for _ in range(16):
                nxt = D(C(seq))
                if nxt == seq:
                    break
                seq = nxt
            Jx = seq
            assert C(Jx) == Jx
            assert D(Jx) == Jx

            # Least common fixed point above x.
            common = [
                y for y in subs
                if x <= y and C(y) == y and D(y) == y
            ]
            assert common
            least = set(U)
            for y in common:
                least &= set(y)
            assert Jx == frozenset(least)

            # If the operators commute pointwise, one pass is enough.
            commute = all(C(D(z)) == D(C(z)) for z in subs)
            if commute:
                assert D(C(x)) == Jx

# ---------- III. minimal memory ----------
FACTS = [
    "a","b","c",
    "s_ab","p_ab","d_ab",
    "s_ac","p_ac","d_ac",
    "s_bc","p_bc","d_bc",
    "N",
]
RULES = []
for x,y,pair in [("a","b","ab"),("a","c","ac"),("b","c","bc")]:
    RULES.append((frozenset([x,y]), f"s_{pair}"))
    RULES.append((frozenset([x,y]), f"p_{pair}"))
for pair in ["ab","ac","bc"]:
    s,p,d = f"s_{pair}",f"p_{pair}",f"d_{pair}"
    RULES += [
        (frozenset([s,p]), d),
        (frozenset([s,d]), p),
        (frozenset([p,d]), s),
    ]
RULES += [
    (frozenset(["p_ab","p_ac"]), "a"),
    (frozenset(["p_ab","p_bc"]), "b"),
    (frozenset(["p_ac","p_bc"]), "c"),
    (frozenset(["p_ab","p_ac","p_bc"]), "N"),
]

def fact_closure(seed):
    s = set(seed)
    changed = True
    while changed:
        changed = False
        for prem, concl in RULES:
            if prem <= s and concl not in s:
                s.add(concl); changed = True
    return frozenset(s)

def check_13_fact_closure_and_generators():
    U = frozenset(FACTS)
    subsets = [
        frozenset(c)
        for r in range(len(FACTS)+1)
        for c in combinations(FACTS,r)
    ]
    closed = [S for S in subsets if fact_closure(S) == S]
    assert len(closed) == 847

    generating = [S for S in subsets if fact_closure(S) == U]
    minimal = [
        G for G in generating
        if not any(H < G for H in generating)
    ]
    dist = {}
    for G in minimal:
        dist[len(G)] = dist.get(len(G),0)+1
    assert dist == {3:2,4:6,5:9,6:4}

    min_size = min(map(len, generating))
    minimum = {G for G in generating if len(G)==min_size}
    assert min_size == 3
    assert minimum == {
        frozenset(("a","b","c")),
        frozenset(("p_ab","p_ac","p_bc")),
    }

    # N alone is not a generator.
    assert fact_closure(("N",)) == frozenset(("N",))

def run():
    tests = [
        check_divisor_descent,
        check_relation_pairwise_not_global,
        check_noncommuting_one_pass,
        check_closure_join_iteration,
        check_13_fact_closure_and_generators,
    ]
    for fn in tests:
        fn()
        print("PASS", fn.__name__)
    print(f"{len(tests)}/{len(tests)} PASS")

if __name__ == "__main__":
    run()
