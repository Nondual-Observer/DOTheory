"""Exact checks for the DOT v21 factorization lattice calculus."""
from math import gcd, lcm
from itertools import combinations

def factor(n):
    f={}
    p=2
    x=n
    while p*p<=x:
        while x%p==0:
            f[p]=f.get(p,0)+1
            x//=p
        p+=1
    if x>1:
        f[x]=f.get(x,0)+1
    return f

def divisors(n):
    ds=[1]
    for p,a in factor(n).items():
        ds=[d*p**e for d in ds for e in range(a+1)]
    return sorted(ds)

def valuation_vector(n,d):
    out=[]
    for p,a in factor(n).items():
        b=0
        x=d
        while x%p==0:
            b+=1
            x//=p
        out.append(b)
    return tuple(out)

def sat(n,d):
    r=1
    for p,a in factor(n).items():
        if d%p==0:
            r*=p**a
    return r

def check_divisor_lattice():
    for n in range(2,121):
        ds=divisors(n)
        for d,e in combinations(ds,2):
            vd=valuation_vector(n,d)
            ve=valuation_vector(n,e)
            vg=valuation_vector(n,gcd(d,e))
            vl=valuation_vector(n,lcm(d,e))
            assert vg==tuple(min(a,b) for a,b in zip(vd,ve))
            assert vl==tuple(max(a,b) for a,b in zip(vd,ve))

def check_squarefree_boolean():
    for n in (6,30,42,70,105):
        fs=factor(n)
        assert all(a==1 for a in fs.values())
        assert len(divisors(n))==2**len(fs)

def check_sat_closure():
    for n in range(2,121):
        ds=divisors(n)
        for d in ds:
            s=sat(n,d)
            assert s%d==0
            assert sat(n,s)==s
        for d in ds:
            for e in ds:
                if e%d==0:
                    assert sat(n,e)%sat(n,d)==0

def check_iterated_saturation():
    for n in range(2,121):
        for d in divisors(n):
            x=d
            for _ in range(20):
                y=gcd(n,x*x)
                if y==x:
                    break
                x=y
            assert x==sat(n,d)

def check_fixed_boolean_blocks():
    for n in range(2,121):
        fs=factor(n)
        fixed=[d for d in divisors(n) if sat(n,d)==d]
        assert len(fixed)==2**len(fs)
        for d in fixed:
            c=n//d
            assert sat(n,c)==c
            assert gcd(d,c)==1

def check_30_cube():
    n=30
    lower={2,3,5}
    upper={6,10,15}
    assert {gcd(a,b) for a,b in combinations(upper,2)}==lower
    assert lcm(*upper)==30
    assert {(d,n//d) for d in lower}=={(2,15),(3,10),(5,6)}

def check_raw_vs_support():
    n=45 # 3^2 * 5
    assert sat(n,3)==9
    assert sat(n,9)==9
    assert sat(n,15)==45
    assert gcd(9,5)==1

def check_certificate_meet():
    examples=[
        (105,64-1,21),
        (105,16-1,15),
        (45,3,3),
        (45,9,9),
    ]
    for n,z,want in examples:
        assert gcd(z,n)==want

def run():
    tests=[
        check_divisor_lattice,
        check_squarefree_boolean,
        check_sat_closure,
        check_iterated_saturation,
        check_fixed_boolean_blocks,
        check_30_cube,
        check_raw_vs_support,
        check_certificate_meet,
    ]
    for fn in tests:
        fn()
        print("PASS",fn.__name__)
    print(f"{len(tests)}/{len(tests)} PASS")

if __name__=="__main__":
    run()
