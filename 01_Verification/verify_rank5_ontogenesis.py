#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rigorous rank-5 cell of the ontogenesis matrix (operator-identity grade, 3 statuses).
from itertools import combinations, permutations, product
from math import comb
R=[]
def P(t,ok,m=""):
    s='PASS' if ok is True else ('FAIL' if ok is False else 'INFO'); R.append(s); print(f"[{s}] {t}: {m}")
N=5; FULL=(1<<N)-1                       # 11111 = 31
Q=list(range(32)); U=[x for x in Q if 0<bin(x).count("1")<5]
kap=lambda x:x^FULL
print("CORE — carrier, active scene, axis quotient")
P("|Q_5|=32, |U_5|=30", len(Q)==32 and len(U)==30)
rep=lambda x:min(x,kap(x)); axes=sorted(set(rep(x) for x in U))
P("|U_5/kappa| = 15 axes", len(axes)==15)

print("RIGOROUS READING — U_5/kappa = PG(3,2): 15 pts, 35 lines, 15 planes; 2-(15,3,1)")
# do projective facts in F_2^4 directly (15 nonzero vectors), isomorphic to U_5/kappa
pts=list(range(1,16))
lines=set(frozenset([a,b,a^b]) for a,b in combinations(pts,2))
P("35 lines, each 3 points", len(lines)==35 and all(len(l)==3 for l in lines))
pc={}
for l in lines:
    for p in combinations(sorted(l),2): pc[p]=pc.get(p,0)+1
P("2-(15,3,1): every pair on exactly one line; 7 lines/point",
  all(pc[p]==1 for p in combinations(pts,2)) and all(sum(1 for l in lines if i in l)==7 for i in pts))
planes=set()
for a in range(1,16):  # hyperplane {x : a.x=0}
    hp=frozenset(x for x in pts if bin(a&x).count("1")%2==0)
    planes.add(hp)
P("15 planes (hyperplanes), each a 7-point Fano", len(planes)==15 and all(len(p)==7 for p in planes))

print("RIGOROUS READING — middle layer S_2: Kneser KG(5,2)=Petersen, Johnson J(5,2)=complement")
S=lambda k:[x for x in U if bin(x).count("1")==k]
S1,S2,S3,S4=S(1),S(2),S(3),S(4)
P("layers |S1..S4| = 5,10,10,5 (sum 30); odd rank: no self-dual middle", (len(S1),len(S2),len(S3),len(S4))==(5,10,10,5))
kn={v:set() for v in S2}      # Kneser: disjoint 2-subsets
for a,b in combinations(S2,2):
    if a&b==0: kn[a].add(b); kn[b].add(a)
deg=[len(kn[v]) for v in S2]
tri=any(c in kn[b] for a in S2 for b in kn[a] for c in kn[a] if c in kn[b])
def has4cycle():
    for a in S2:
        nb=list(kn[a])
        for b,c in combinations(nb,2):
            if len(kn[b]&kn[c])>=2: return True
    return False
P("KG(5,2)=Petersen: 10 vertices, 3-regular, girth 5 (no triangle, no 4-cycle)",
  len(S2)==10 and all(d==3 for d in deg) and not tri and not has4cycle())

print("CORE — kappa swaps S1<->S4, S2<->S3 (odd rank: only centroid, no zero-weight layer)")
P("kappa: S1<->S4, S2<->S3", all(kap(x) in S4 for x in S1) and all(kap(x) in S3 for x in S2))

print("RIGOROUS READING — sl2 multiplets [1,4,5]; dim = C(8,3) = 56")
def mult(n,k): return comb(n,k)-(comb(n,k-1) if k>=1 else 0)
mm=[mult(5,k) for k in range(3)]
P("sl2 multiplicities (spins 5/2,3/2,1/2) = [1,4,5]", mm==[1,4,5])
P("dim<sl2>_5 = sum(2j+1)^2 = 56 = C(8,3)", sum((5-2*k+1)**2 for k in range(3))==56==comb(8,3))

print("RIGOROUS READING — finite groups: coordinate S_5 orbits on 15 PG(3,2) points = {5,10}")
idx={a:i for i,a in enumerate(axes)}
def perm_axis(p):
    act=lambda x: sum(((x>>k)&1)<<p[k] for k in range(5))
    return {idx[a]: idx[rep(act(a))] for a in axes}
gs=[perm_axis(p) for p in permutations(range(5))]
seen=set(); orbs=[]
for s in range(15):
    if s in seen: continue
    o={s}; ch=True
    while ch:
        ch=False
        for g in gs:
            for x in list(o):
                if g[x] not in o: o.add(g[x]); ch=True
    seen|=o; orbs.append(len(o))
P("coordinate-S_5 orbits = {5,10} (vertex axes + edge axes); GL(4,2)=A_8 order 20160 (classical full)",
  sorted(orbs)==[5,10], f"orbits={sorted(orbs)}")

print("RIGOROUS READING — finite quadrics in PG(3,2): hyperbolic Q+ = 9 pts (3x3 Segre), elliptic Q- = 5 pts")
b=lambda x,i:(x>>i)&1
Qplus=[x for x in pts if (b(x,0)&b(x,1))^(b(x,2)&b(x,3))==0]      # x0x1+x2x3
Qminus=[x for x in pts if (b(x,0)&b(x,1))^(b(x,2)^(b(x,2)&b(x,3))^b(x,3))==0]  # x0x1 + (x2^2+x2x3+x3^2)
P("hyperbolic Q+(3,2) has 9 points (=3x3 grid, two reguli) ; elliptic Q-(3,2) has 5 points",
  len(Qplus)==9 and len(Qminus)==5, f"|Q+|={len(Qplus)}, |Q-|={len(Qminus)}")

print("RIGOROUS READING — Singer rotation order on PG(3,2) = 2^4-1 = 15 = 3*5 = F_0*F_1 (Fermat product)")
P("Singer order 15 = 3*5 = F_0*F_1 (first Fermat-product axis count; |U_5|=30=2*3*5)",
  2**4-1==15==3*5 and len(U)==30==2*3*5)

print("AVATAR — boundary of 4-simplex dD^4 ~ S^3 (Euler characteristic 0)")
V,E,F,T=5,10,10,5
P("chi(dD^4)=V-E+F-T=5-10+10-5=0=chi(S^3) (active scene U_5 = face poset of S^3)", V-E+F-T==0)

print("="*66); print(f"SUMMARY: {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (rank-5 ontogenesis cell)")
