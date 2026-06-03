#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rigorous rank-4 cell of the ontogenesis matrix (operator-identity grade, 3 statuses).
# CORE facts: |Q4|,|U4|,|U4/kappa|; U4/kappa = Fano PG(2,2) = 2-(7,3,1); middle layer S2 = octahedron;
# kappa swaps S1<->S3, fixes S2 (zero weight at even rank); sl2 multiplicities [1,3,2], dim=35=C(7,3);
# coordinate S4 orbits on Fano points = {4,3}; avatar: dD^3 ~ S^2 (Euler char 2).
from itertools import combinations, permutations
from math import comb
R=[]
def P(t,ok,m=""):
    s='PASS' if ok is True else ('FAIL' if ok is False else 'INFO'); R.append(s); print(f"[{s}] {t}: {m}")
N=4; FULL=(1<<N)-1                      # 1111 = 15
Q=list(range(16)); U=[x for x in Q if 0<bin(x).count("1")<4]
kap=lambda x: x^FULL
print("CORE — carrier, active scene, axis quotient")
P("|Q_4|=16, |U_4|=14", len(Q)==16 and len(U)==14)
# axes = kappa-classes
rep=lambda x: min(x,kap(x)); axes=sorted(set(rep(x) for x in U))
P("|U_4/kappa| = 7 axes", len(axes)==7)

print("RIGOROUS READING — finite projective geometry: U_4/kappa = Fano PG(2,2) = 2-(7,3,1)")
idx={a:i for i,a in enumerate(axes)}
# line: triple of distinct classes whose rep-XOR is in {0, FULL} (class-invariant)
lines=[]
for a,b,c in combinations(axes,3):
    if (a^b^c) in (0,FULL): lines.append(frozenset([idx[a],idx[b],idx[c]]))
lines=set(lines)
P("7 lines, each with 3 points", len(lines)==7 and all(len(l)==3 for l in lines))
pair_cov={}
for l in lines:
    for p in combinations(sorted(l),2): pair_cov[p]=pair_cov.get(p,0)+1
P("2-(7,3,1): every pair of points on exactly one line", all(pair_cov.get(p,0)==1 for p in combinations(range(7),2)))
P("each point on exactly 3 lines (Fano)", all(sum(1 for l in lines if i in l)==3 for i in range(7)))

print("RIGOROUS READING — the break (Tom 2): middle layer S_2 = octahedron K_{2,2,2} = J(4,2)")
S=lambda k:[x for x in U if bin(x).count("1")==k]
S1,S2,S3=S(1),S(2),S(3)
P("weight layers |S1|,|S2|,|S3| = 4,6,4 (sum 14)", (len(S1),len(S2),len(S3))==(4,6,4))
# Johnson J(4,2): 2-subsets adjacent iff share one element
adj={v:set() for v in S2}
for a,b in combinations(S2,2):
    if bin(a&b).count("1")==1: adj[a].add(b); adj[b].add(a)
deg=[len(adj[v]) for v in S2]
nonedges=[(a,b) for a,b in combinations(S2,2) if b not in adj[a]]
P("S_2 is 4-regular on 6 vertices (octahedron degree)", all(d==4 for d in deg))
P("3 non-edges = 3 antipodal (disjoint) pairs -> K_{2,2,2}=octahedron (=complement 3K_2)",
  len(nonedges)==3 and all(bin(a&b).count("1")==0 for a,b in nonedges))

print("CORE — kappa on layers: swaps S1<->S3, FIXES S2 (zero weight, even rank, Tom 7 §3.3)")
P("kappa: S1<->S3 (each weight-1 axis pairs a weight-3), S2 self-dual middle",
  all(kap(x) in S3 for x in S1) and all(kap(x) in S2 for x in S2))

print("RIGOROUS READING — sl2 weight decomposition: multiplicities [1,3,2], dim = C(7,3) = 35")
def mult(n,k): return comb(n,k)-(comb(n,k-1) if k>=1 else 0)
mm=[mult(4,k) for k in range(3)]
P("sl2 multiplicities (spins 2,1,0) = [1,3,2]", mm==[1,3,2])
P("dim<sl2>_4 = sum(2j+1)^2 = 35 = C(7,3) (tetrahedral, Tom7 §7.5)",
  sum((4-2*k+1)**2 for k in range(3))==35==comb(7,3))

print("RIGOROUS READING — finite groups: coordinate S_4 on the 7 Fano points has orbits {4,3}")
def perm_axis(p):  # permutation of coordinates induces map on axes
    def act(x): 
        return sum(((x>>k)&1)<<p[k] for k in range(4))
    return {idx[a]: idx[rep(act(a))] for a in axes}
orbits=set()
# orbit sizes under all of S_4
elem_imgs=[perm_axis(p) for p in permutations(range(4))]
seen=set(); orb_sizes=[]
for start in range(7):
    if start in seen: continue
    orb={start}
    changed=True
    while changed:
        changed=False
        for g in elem_imgs:
            for o in list(orb):
                if g[o] not in orb: orb.add(g[o]); changed=True
    seen|=orb; orb_sizes.append(len(orb))
P("coordinate-S_4 orbits on 7 Fano points = {3,4} (L_inf line + 4 vertex-axes)",
  sorted(orb_sizes)==[3,4], f"orbits={sorted(orb_sizes)}; |GL(3,2)|=168=7*24 (full Fano aut, classical)")

print("AVATAR — boundary of tetrahedron dD^3 ~ S^2 (Euler characteristic 2)")
V,E,F=len(S1),len(S2),len(S3)   # vertices, edges, triangles of dD^3
P("chi(dD^3) = V-E+F = 4-6+4 = 2 = chi(S^2)  (active scene U_4 = face poset of S^2)", V-E+F==2)

print("="*66); print(f"SUMMARY: {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (rank-4 ontogenesis cell)")
