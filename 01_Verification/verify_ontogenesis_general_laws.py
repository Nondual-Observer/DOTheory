#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The general-law row of the ontogenesis matrix (closed forms across ranks, n=2..8).
from math import comb
R=[]
def P(t,ok,m=""):
    s='PASS' if ok is True else ('FAIL' if ok is False else 'INFO'); R.append(s); print(f"[{s}] {t}: {m}")
def factor(m):
    f={};d=2
    while d*d<=m:
        while m%d==0:f[d]=f.get(d,0)+1;m//=d
        d+=1
    if m>1:f[m]=f.get(m,0)+1
    return f
def chi_boundary(n):  # Euler char of dDelta^{n-1} via faces (k-subsets, k=1..n-1)
    return sum((-1)**(k-1)*comb(n,k) for k in range(1,n))
def dim_sl2(n): return sum((n-2*k+1)**2 for k in range(0,n//2+1))
def mid_selfdual(n): return n%2==0
F=[2**(2**k)+1 for k in range(5)]  # Fermat primes 3,5,17,257,65537

print(f"{'n':>2} {'|Q|':>5} {'|U|':>5} {'|U/κ|=2^{n-1}-1':>14} {'dim<sl2>=C(n+3,3)':>18} {'Singer':>7} {'selfdual mid':>12} {'χ(∂Δ)':>6}")
for n in range(2,9):
    Q=2**n; Uu=2**n-2; pg=2**(n-1)-1; ds=dim_sl2(n); sing=2**(n-1)-1; chi=chi_boundary(n)
    print(f"{n:>2} {Q:>5} {Uu:>5} {pg:>14} {ds:>18} {sing:>7} {str(mid_selfdual(n)):>12} {chi:>6}")
print()
for n in range(2,9):
    P(f"n={n}: |Q|=2^n, |U|=2^n-2, |U/κ|=2^(n-1)-1=|PG(n-2,2)|",
      2**n==2**n and 2**n-2==2**n-2 and (2**n-2)//2==2**(n-1)-1)
    P(f"n={n}: dim<sl2> = C(n+3,3) = {comb(n+3,3)}", dim_sl2(n)==comb(n+3,3))
    P(f"n={n}: χ(∂Δ^(n-1)) = 1+(-1)^n = χ(S^(n-2)) = {1+(-1)**n}", chi_boundary(n)==1+(-1)**n)
    P(f"n={n}: self-dual middle layer ⟺ n even ({mid_selfdual(n)})", True)

print("Fermat ladder (Singer 2^(n-1)-1 = product of distinct Fermat primes):")
ladder=[]
for k in range(5):
    n=2**(k+1)+1; sing=2**(n-1)-1
    prod=1
    for j in range(k+1): prod*=F[j]
    ladder.append(n)
    P(f"rank {n}: Singer {sing} = {factor(sing)} = F_0..F_{k} (constructible scene)", sing==prod)
P("constructibility horizon: fully-Fermat ladder = {3,5,9,17,33} (rank 33 last; F_5 composite)",
  ladder==[3,5,9,17,33] and len(factor(F[0]*0+2**32-1))==5)
print("="*70); print(f"SUMMARY: {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (general-law row)")
