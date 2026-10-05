"""Finite checks for the DOT v17 action algebra."""
from itertools import combinations, product

def complement_pairs():
    Omega = frozenset(("W","A","I"))
    proper = [frozenset(s) for r in (1,2) for s in combinations(Omega,r)]
    pairs = set()
    for s in proper:
        t = Omega - s
        pairs.add(tuple(sorted((tuple(sorted(s)),tuple(sorted(t))))))
    assert len(proper)==6
    assert len(pairs)==3

def active_graphs():
    # binary addresses 1..6, complement xor 7
    V = list(range(1,7))
    comp = {v:v^7 for v in V}
    assert sorted((min(v,comp[v]),max(v,comp[v])) for v in V if v<comp[v]) == [(1,6),(2,5),(3,4)]
    def hd(a,b): return (a^b).bit_count()
    e1 = {tuple(sorted((a,b))) for a,b in combinations(V,2) if hd(a,b)==1}
    assert len(e1)==6
    deg1={v:0 for v in V}
    for a,b in e1: deg1[a]+=1; deg1[b]+=1
    assert all(d==2 for d in deg1.values())  # C6
    eo = {tuple(sorted((a,b))) for a,b in combinations(V,2) if b != comp[a]}
    assert len(eo)==12
    dego={v:0 for v in V}
    for a,b in eo: dego[a]+=1; dego[b]+=1
    assert all(d==4 for d in dego.values())  # octahedron graph

def arithmetic_fibres():
    add3={(a,b) for a in range(4) for b in range(4) if a+b==3}
    assert add3=={(0,3),(1,2),(2,1),(3,0)}
    mul12={(a,b) for a in range(1,13) for b in range(1,13) if a*b==12}
    assert mul12=={(1,12),(2,6),(3,4),(4,3),(6,2),(12,1)}

def pullback_composition():
    X=range(5)
    f=lambda x:x+1
    g=lambda y:2*y
    q=lambda z:z%3
    lhs=[q(g(f(x))) for x in X]
    # f^*(g^*q)
    rhs=[(lambda xx: (lambda yy:q(g(yy)))(f(xx)))(x) for x in X]
    assert lhs==rhs

def equality_closure():
    assert 2+1==3
    # same result can have multiple descriptions
    reps=[("2+1",2+1),("1+2",1+2),("4-1",4-1)]
    assert len({v for _,v in reps})==1
    assert len(reps)==3

def joint_interaction_not_inverse():
    # World and observer both update forward; map deliberately non-invertible.
    def Phi(w,o):
        return (w ^ o, w)  # for bits this one happens to be invertible; use lossy below
    def Lossy(w,o):
        return (w|o, w&o)
    outputs={Lossy(w,o) for w,o in product((0,1),repeat=2)}
    assert len(outputs)<4  # no global inverse
    # Yet a question always pulls back by composition.
    q=lambda state: state[0]^state[1]
    vals={(w,o):q(Lossy(w,o)) for w,o in product((0,1),repeat=2)}
    assert len(vals)==4

def run():
    tests=[complement_pairs,active_graphs,arithmetic_fibres,pullback_composition,equality_closure,joint_interaction_not_inverse]
    lines=[]
    for fn in tests:
        fn()
        line=f"PASS {fn.__name__}"
        print(line); lines.append(line)
    print(f"{len(tests)}/{len(tests)} PASS")
    return lines

if __name__=="__main__":
    run()
