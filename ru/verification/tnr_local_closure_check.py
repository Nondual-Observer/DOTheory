"""Finite exact checks for the DOT v19 local closure."""
from itertools import combinations
from math import gcd, lcm

def defect(a,b):
    return a*b-a-b

def check_unit_defect_unique():
    sols=[]
    for a in range(2,100):
        for b in range(a,100):
            if defect(a,b)==1:
                sols.append((a,b))
    assert sols==[(2,3)]

def check_edge_defects_137():
    T=(2,3,5)
    edges=list(combinations(T,2))
    ds=[defect(a,b) for a,b in edges]
    assert ds==[1,3,7]

def check_operational_matrix():
    T=(2,3,5)
    rows=[]
    for a,b in combinations(T,2):
        s=a+b
        p=a*b
        d=defect(a,b)
        assert s+d==p
        rows.append((s,p,d))
    assert rows==[(5,6,1),(7,10,3),(8,15,7)]

def check_divisor_gluing_30():
    patches=(6,10,15)
    assert gcd(6,10)==2
    assert gcd(6,15)==3
    assert gcd(10,15)==5
    assert lcm(*patches)==30

def check_general_coprime_gluing():
    triples=[(2,3,5),(2,5,7),(3,4,5),(5,7,11),(4,9,25)]
    for a,b,c in triples:
        assert gcd(a,b)==gcd(a,c)==gcd(b,c)==1
        ab,ac,bc=a*b,a*c,b*c
        assert gcd(ab,ac)==a
        assert gcd(ab,bc)==b
        assert gcd(ac,bc)==c
        assert lcm(ab,ac,bc)==a*b*c

def check_internal_overlap_network():
    assert 2+3==5
    assert defect(2,5)==3
    assert defect(3,5)==2+5==7

def check_divisor_cube():
    divs=[d for d in range(1,31) if 30%d==0]
    assert divs==[1,2,3,5,6,10,15,30]
    layers=[
        [1],
        [2,3,5],
        [6,10,15],
        [30]
    ]
    assert [len(x) for x in layers]==[1,3,3,1]

def check_nine_slots():
    T=(2,3,5)
    rows=[]
    for a,b in combinations(T,2):
        rows.extend([a+b,a*b,defect(a,b)])
    assert len(rows)==9
    assert len(set(rows))==8 # one value 7 occurs twice
    closure_values=set(T)|set(rows)
    assert closure_values=={1,2,3,5,6,7,8,10,15}
    assert len(closure_values)==9

def run():
    tests=[
        check_unit_defect_unique,
        check_edge_defects_137,
        check_operational_matrix,
        check_divisor_gluing_30,
        check_general_coprime_gluing,
        check_internal_overlap_network,
        check_divisor_cube,
        check_nine_slots,
    ]
    for fn in tests:
        fn()
        print("PASS",fn.__name__)
    print(f"{len(tests)}/{len(tests)} PASS")

if __name__=="__main__":
    run()
