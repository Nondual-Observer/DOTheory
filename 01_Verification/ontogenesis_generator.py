#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# THE ATLAS AS A FUNCTION: gen(n) pre-computes the whole ontogenesis cell from rank n alone.
# Hand-verified cells (n=3,4,5,6) become VALIDATION points; if gen reproduces them, its
# outputs for n=7..33 are trustworthy PREDICTIONS. All formulas are standard finite math
# (Gaussian binomials, Johnson/Kneser, quadric counts, group orders) — rigorous reading, computed.
from math import comb
def gauss(m,r,q=2):                       # Gaussian binomial [m,r]_q = # of (r-1)-flats... use for subspace counts
    if r<0 or r>m: return 0
    num=den=1
    for i in range(r): num*=(q**(m-i)-1); den*=(q**(i+1)-1)
    return num//den
def glorder(m,q=2):                        # |GL(m,q)|
    o=1
    for i in range(m): o*=(q**m-q**i)
    return o
def factor(x):
    f={};d=2
    while d*d<=x:
        while x%d==0:f[d]=f.get(d,0)+1;x//=d
        d+=1
    if x>1:f[x]=f.get(x,0)+1
    return f
FERMAT={3,5,17,257,65537}
def is_fermat_product(x):                  # x = product of DISTINCT Fermat primes?
    f=factor(x)
    return all(p in FERMAT and e==1 for p,e in f.items()) and x>1

def gen(n):
    d=n-2                                   # projective dimension of U_n/kappa = PG(d,2)
    pts=2**(n-1)-1
    flats={k: gauss(d+1,k+1) for k in range(0,d+1)}   # k-flats of PG(d,2): points(k0),lines(k1),...
    layers=[comb(n,k) for k in range(1,n)]
    self_dual_mid = (n%2==0)
    mid_k=n//2
    middle = None
    if n>=3:
        k=n//2
        middle={'k':k,'verts':comb(n,k),'johnson_deg':k*(n-k),'kneser_deg':comb(n-k,k)}
    sl2_mult=[comb(n,j)-(comb(n,j-1) if j>=1 else 0) for j in range(0,n//2+1)]
    sl2_dim=comb(n+3,3)
    singer=2**(n-1)-1
    # S_n orbits on the axes (kappa-pairs)
    orbits=[comb(n,k) for k in range(1,(n-1)//2+1)]
    if n%2==0: orbits.append(comb(n,n//2)//2)
    # quadrics in PG(d,2)
    if d>=1:
        if d%2==0:                          # parabolic Q(d,2)
            quad={'type':'parabolic','pts':(2**d-1)}
        else:                               # hyperbolic Q+ and elliptic Q-
            m=(d-1)//2
            quad={'type':'hyperbolic/elliptic','Qplus':(2**m+1)*(2**(m+1)-1),'Qminus':(2**m-1)*(2**(m+1)+1)}
    else: quad=None
    return dict(n=n, pg_dim=d, pts=pts, lines=flats.get(1,0), planes=flats.get(2,0),
                layers=layers, self_dual_mid=self_dual_mid, middle=middle,
                sl2_mult=sl2_mult, sl2_dim=sl2_dim, singer=singer,
                singer_factor=factor(singer) if singer>1 else {}, constructible=is_fermat_product(singer),
                Sn=comb(n,n)*1, Sn_order=__import__('math').factorial(n), GL=glorder(max(n-1,1)),
                orbits=sorted(orbits), quad=quad, chi=1+(-1)**n)

# ---- cross-validate against hand-verified cells (ranks 3,4,5,6) ----
HAND={
 3:dict(pts=3,layers=[3,3],sl2_mult=[1,2],sl2_dim=20,orbits=[3],singer=3,constructible=True),
 4:dict(pts=7,layers=[4,6,4],sl2_mult=[1,3,2],sl2_dim=35,orbits=[3,4],singer=7,constructible=False,
        quadpar=3),
 5:dict(pts=15,layers=[5,10,10,5],sl2_mult=[1,4,5],sl2_dim=56,orbits=[5,10],singer=15,constructible=True,
        Qplus=9,Qminus=5),
 6:dict(pts=31,layers=[6,15,20,15,6],sl2_mult=[1,5,9,5],sl2_dim=84,orbits=[6,10,15],singer=31,
        constructible=False,quadpar=15),
}
R=[]
def P(t,ok): s='PASS' if ok else 'FAIL'; R.append(s); print(f"[{s}] {t}")
print("CROSS-VALIDATION: gen(n) reproduces hand-verified cells n=3,4,5,6")
for n,h in HAND.items():
    g=gen(n)
    P(f"n={n} pts/layers/sl2/dim/orbits/singer/constructible",
      g['pts']==h['pts'] and g['layers']==h['layers'] and g['sl2_mult']==h['sl2_mult']
      and g['sl2_dim']==h['sl2_dim'] and g['orbits']==h['orbits'] and g['singer']==h['singer']
      and g['constructible']==h['constructible'])
    if 'Qplus' in h: P(f"n={n} quadrics Q+={h['Qplus']},Q-={h['Qminus']}",
                       g['quad']['Qplus']==h['Qplus'] and g['quad']['Qminus']==h['Qminus'])
    if 'quadpar' in h: P(f"n={n} parabolic quadric={h['quadpar']}", g['quad']['pts']==h['quadpar'])
print(f"  -> {R.count('PASS')} PASS, {R.count('FAIL')} FAIL  (generator validated on hand cells)")

print("\nPREDICTED ATLAS (generated, n=2..16):")
print(f"{'n':>2}{'PG':>4}{'pts':>7}{'sl2dim':>8}{'Singer':>9}{'constr':>7}{'selfdual':>9}  orbits / quadric")
for n in range(2,17):
    g=gen(n)
    q=g['quad']; qs = (f"par={q['pts']}" if q and q['type']=='parabolic' else (f"Q+={q['Qplus']},Q-={q['Qminus']}" if q else "-"))
    print(f"{n:>2}{g['pg_dim']:>4}{g['pts']:>7}{g['sl2_dim']:>8}{g['singer']:>9}{str(g['constructible']):>7}{str(g['self_dual_mid']):>9}  {g['orbits']}  {qs}")

print("\nFERMAT LADDER / constructible ranks up to 33 (Singer = product of distinct Fermat primes):")
for n in range(2,34):
    if gen(n)['constructible']:
        print(f"  rank {n:>2}: Singer {gen(n)['singer']} = {gen(n)['singer_factor']}")
