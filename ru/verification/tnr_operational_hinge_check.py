"""Exact finite checks for the DOT v18 operational hinge."""
from fractions import Fraction
from itertools import combinations, permutations

def oct_graph(V, comp):
    V=tuple(V)
    edges=set()
    for a,b in combinations(V,2):
        if comp[a]!=b:
            edges.add(tuple(sorted((a,b))))
    return edges

def check_additive_octahedron():
    V=tuple(range(1,7))
    comp={x:7-x for x in V}
    pairs=sorted((x,comp[x]) for x in V if x<comp[x])
    assert pairs==[(1,6),(2,5),(3,4)]
    assert all(a+b==7 for a,b in pairs)
    E=oct_graph(V,comp)
    assert len(E)==12
    deg={v:0 for v in V}
    for a,b in E: deg[a]+=1;deg[b]+=1
    assert set(deg.values())=={4}

def check_multiplicative_octahedron():
    V=(2,3,5,6,10,15)
    comp={x:30//x for x in V}
    pairs=sorted((x,comp[x]) for x in V if x<comp[x])
    assert pairs==[(2,15),(3,10),(5,6)]
    assert all(a*b==30 for a,b in pairs)
    E=oct_graph(V,comp)
    assert len(E)==12
    deg={v:0 for v in V}
    for a,b in E: deg[a]+=1;deg[b]+=1
    assert set(deg.values())=={4}

def check_unique_sum_product_triple():
    sols=[]
    for a in range(1,30):
        for b in range(a,30):
            for c in range(b,30):
                if a+b+c==a*b*c:
                    sols.append((a,b,c))
    assert sols==[(1,2,3)]

def check_projection_intersections():
    triples=[((1,2,3),0,1),((2,3,5),1,3),((3,5,7),2,7)]
    for T,j,want in triples:
        S=sum(T)
        P=T[0]*T[1]*T[2]
        assert Fraction(P,S)==want
        x=T[j]
        A=Fraction(x,S)
        M=Fraction(x*x,P)
        assert A==M
    # ensure in these triples exactly one coordinate has A=M
    for T,j,_ in triples:
        S=sum(T); P=T[0]*T[1]*T[2]
        hits=[k for k,x in enumerate(T) if Fraction(x,S)==Fraction(x*x,P)]
        assert hits==[j]

def check_operational_core():
    Vp={1,2,3,4,5,6}
    Vx={2,3,5,6,10,15}
    core=Vp & Vx
    assert core=={2,3,5,6}
    assert 2+3==5
    assert 2*3==6
    cp={x:7-x for x in Vp}
    cx={x:30//x for x in Vx}
    Ep=oct_graph(Vp,cp)
    Ex=oct_graph(Vx,cx)
    core_pairs={tuple(sorted(e)) for e in combinations(sorted(core),2)}
    union={(a,b) for a,b in (Ep|Ex) if a in core and b in core}
    assert union==core_pairs # K4

def check_half_gap_and_ratio_bridge():
    h0=Fraction(3-(1*2),2)
    h1=Fraction((2+3)-(2*3),2)
    assert h0==Fraction(1,2)
    assert h1==Fraction(-1,2)
    assert Fraction(5,6)-1==Fraction(-1,6)
    assert Fraction(1,6)==- (Fraction(5,6)-1)
    assert Fraction(3,6)==Fraction(1,2)

def check_three_complement_readings():
    R7=(Fraction(1,6),Fraction(2,5),Fraction(3,4))
    Rsum=(Fraction(1,5),Fraction(2,4),Fraction(3,3))
    Rprod=(Fraction(1,6),Fraction(2,3),Fraction(3,2))
    assert Rsum[1]==Fraction(1,2)
    assert Rprod[2]-1==Fraction(1,2)
    assert R7[0]==Rprod[0]

def check_unit_defect_uniqueness():
    sols=[]
    for a in range(2,50):
        for b in range(a,50):
            if a*b-(a+b)==1:
                sols.append((a,b))
    assert sols==[(2,3)]

def run():
    checks=[
        check_additive_octahedron,
        check_multiplicative_octahedron,
        check_unique_sum_product_triple,
        check_projection_intersections,
        check_operational_core,
        check_half_gap_and_ratio_bridge,
        check_three_complement_readings,
        check_unit_defect_uniqueness,
    ]
    for fn in checks:
        fn()
        print("PASS",fn.__name__)
    print(f"{len(checks)}/{len(checks)} PASS")

if __name__=="__main__":
    run()
