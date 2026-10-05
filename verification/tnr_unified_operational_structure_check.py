"""Exact checks for the DOT v20 unified operational structure."""
from itertools import combinations
from fractions import Fraction
from math import gcd, lcm
from sympy import primerange

B=(1,2,4)
T=(2,3,5)
P=30
D30={1,2,3,5,6,10,15,30}

def defect(a,b):
    return a*b-a-b

def check_unit_shift():
    assert tuple(x+1 for x in B)==T

def check_flag_defect_bridge():
    flags=(B[0],B[0]+B[1],sum(B))
    defs=tuple(defect(a,b) for a,b in combinations(T,2))
    assert flags==(1,3,7)
    assert defs==flags
    for (a,b),d in zip(combinations(T,2),defs):
        assert d==(a-1)*(b-1)-1

def check_edge_to_axis():
    expected=[
        ((2,3),5,6),
        ((2,5),3,10),
        ((3,5),2,15),
    ]
    for (a,b),c,m in expected:
        assert a*b==m
        assert P//m==c
        assert c*m==P

def check_axis_passports():
    axes=[(5,6),(3,10),(2,15)]
    assert [Fraction(c,m) for c,m in axes]==[Fraction(5,6),Fraction(3,10),Fraction(2,15)]
    assert [c+m for c,m in axes]==[11,13,17]
    assert [m-c for c,m in axes]==[1,7,13]

def check_local_rows():
    rows=[]
    for a,b in combinations(T,2):
        s=a+b;m=a*b;d=defect(a,b)
        assert s+d==m
        rows.append((s,m,d))
    assert rows==[(5,6,1),(7,10,3),(8,15,7)]

def check_internal_counts():
    counts=[]
    promos=[]
    for a,b in combinations(T,2):
        vals=(a+b,a*b,defect(a,b))
        k=sum(v in D30 for v in vals)
        counts.append(k)
        promos.append(3-k)
    assert counts==[3,2,1]
    assert promos==[0,1,2]

def check_divisor_cube():
    assert [1,2,3,5,6,10,15,30]==sorted(D30)
    assert gcd(6,10)==2
    assert gcd(6,15)==3
    assert gcd(10,15)==5
    assert lcm(6,10,15)==30

def check_prime_triple_finite_audit():
    # Among prime triples below 100, (2,3,5) is the unique one with
    # local-output-in-D(P) counts 3,2,1 in natural edge order.
    ps=list(primerange(2,100))
    hits=[]
    for a,b,c in combinations(ps,3):
        P0=a*b*c
        D={1,a,b,c,a*b,a*c,b*c,P0}
        counts=[]
        for x,y in combinations((a,b,c),2):
            vals=(x+y,x*y,x*y-x-y)
            counts.append(sum(v in D for v in vals))
        if counts==[3,2,1]:
            hits.append((a,b,c))
    assert hits==[(2,3,5)]

def run():
    tests=[
        check_unit_shift,
        check_flag_defect_bridge,
        check_edge_to_axis,
        check_axis_passports,
        check_local_rows,
        check_internal_counts,
        check_divisor_cube,
        check_prime_triple_finite_audit,
    ]
    for fn in tests:
        fn()
        print("PASS",fn.__name__)
    print(f"{len(tests)}/{len(tests)} PASS")

if __name__=="__main__":
    run()
