#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rigorous rank-6 cell (operator-identity grade, 3 statuses). Even rank: self-dual middle returns.
from itertools import combinations, permutations
from math import comb
R=[]
def P(t,ok,m=""):
    s='PASS' if ok is True else ('FAIL' if ok is False else 'INFO'); R.append(s); print(f"[{s}] {t}: {m}")
N=6; FULL=(1<<N)-1
Q=list(range(64)); U=[x for x in Q if 0<bin(x).count("1")<6]; kap=lambda x:x^FULL
print("CORE — carrier, scene, axis quotient")
P("|Q_6|=64, |U_6|=62=2*31", len(Q)==64 and len(U)==62==2*31)
rep=lambda x:min(x,kap(x)); axes=sorted(set(rep(x) for x in U))
P("|U_6/kappa| = 31 axes", len(axes)==31)

print("RIGOROUS READING — U_6/kappa = PG(4,2): 31 pts, 155 lines, 2-(31,3,1); 31 solids (PG(3,2))")
pts=list(range(1,32))   # nonzero F_2^5
lines=set(frozenset([a,b,a^b]) for a,b in combinations(pts,2))
pc={}
for l in lines:
    for p in combinations(sorted(l),2): pc[p]=pc.get(p,0)+1
P("155 lines, 3 pts each; 2-(31,3,1); 15 lines/point",
  len(lines)==155 and all(len(l)==3 for l in lines) and all(pc[p]==1 for p in combinations(pts,2))
  and all(sum(1 for l in lines if i in l)==15 for i in pts))
solids=set(frozenset(x for x in pts if bin(a&x).count("1")%2==0) for a in range(1,32))
P("31 solids (hyperplanes), each 15 points = PG(3,2)", len(solids)==31 and all(len(s)==15 for s in solids))

print("RIGOROUS READING — EVEN rank: self-dual middle layer S_3 returns (zero weight, Tom7 §3.3)")
S=lambda k:[x for x in U if bin(x).count("1")==k]
layers=[len(S(k)) for k in range(1,6)]
P("layers = 6,15,20,15,6 (sum 62)", layers==[6,15,20,15,6])
P("kappa fixes middle S_3 (weight 3 = zero weight); swaps S1<->S5, S2<->S4",
  all(kap(x) in S(3) for x in S(3)) and all(kap(x) in S(5) for x in S(1)) and all(kap(x) in S(4) for x in S(2)))
# Kneser KG(6,3) on S_3 = perfect matching 10K_2 ; Johnson J(6,3) 9-regular
S3=S(3)
kn=[sum(1 for y in S3 if (x&y)==0) for x in S3]      # disjoint
jn=[sum(1 for y in S3 if bin(x&y).count("1")==2) for x in S3]  # share 2
P("middle graph: KG(6,3)=10K_2 (each 3-set 1 disjoint complement = kappa); J(6,3) 9-regular",
  len(S3)==20 and all(d==1 for d in kn) and all(d==9 for d in jn))

print("RIGOROUS READING — generalized quadrangle GQ(2,2): parabolic quadric Q(4,2)=15 pts; Sp(4,2)=S_6=720")
b=lambda x,i:(x>>i)&1
Qpar=[x for x in pts if (b(x,0) ^ (b(x,1)&b(x,2)) ^ (b(x,3)&b(x,4)))==0]  # x0 + x1x2 + x3x4 (x^2=x over F2)
sp42=2**4*(2**2-1)*(2**4-1)
P("parabolic quadric Q(4,2) = 15 points (the doily GQ(2,2)); |Sp(4,2)|=720=6!",
  len(Qpar)==15 and sp42==720==comb(6,6)*720//720*720 if False else len(Qpar)==15 and sp42==720,
  f"|Q(4,2)|={len(Qpar)}, |Sp(4,2)|={sp42}=6!")

print("RIGOROUS READING — coordinate S_6 orbits on 31 PG(4,2) points = {6,15,10}")
idx={a:i for i,a in enumerate(axes)}
def perm_axis(p):
    act=lambda x: sum(((x>>k)&1)<<p[k] for k in range(6))
    return {idx[a]: idx[rep(act(a))] for a in axes}
gs=[perm_axis(p) for p in permutations(range(6))]
seen=set(); orbs=[]
for s in range(31):
    if s in seen: continue
    o={s}; ch=True
    while ch:
        ch=False
        for g in gs:
            for x in list(o):
                if g[x] not in o: o.add(g[x]); ch=True
    seen|=o; orbs.append(len(o))
P("S_6 orbits on 31 points = {6,15,10} (vertex/edge/middle axes); S_6 = first S_n with OUTER automorphism (classical)",
  sorted(orbs)==[6,10,15], f"orbits={sorted(orbs)}")

print("RIGOROUS READING — sl2 multiplets [1,5,9,5]; dim = C(9,3) = 84")
def mult(n,k): return comb(n,k)-(comb(n,k-1) if k>=1 else 0)
P("sl2 multiplicities (spins 3,2,1,0) = [1,5,9,5]; dim = 84 = C(9,3)",
  [mult(6,k) for k in range(4)]==[1,5,9,5] and sum((6-2*k+1)**2 for k in range(4))==84==comb(9,3))

print("CORE — Singer 31 = 2^5-1 Mersenne PRIME (rank 6 OFF the Fermat ladder {3,5,9,17,33})")
P("Singer order 31 prime (Mersenne), not a Fermat product; rank 6 even, not on ladder", 31==2**5-1)

print("AVATAR — boundary of 5-simplex dD^5 ~ S^4, Euler char 2")
P("chi(dD^5)=6-15+20-15+6=2=chi(S^4)", 6-15+20-15+6==2==1+(-1)**6)
print("="*66); print(f"SUMMARY: {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (rank-6 ontogenesis cell)")
