# DOT: AMR After the Inter-Rank Lift

## Status

This document fixes the current place of AMR in the new DOT corpus after
the inter-rank law

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}
\]

has been made explicit.

AMR is not the entry point into Volumes 0-6. It is an arithmetic bridge:
it shows how rank carriers, axes, complementarity, boundary, and
recoverability can be read on standard arithmetic material.

Inside AMR two branches must be kept separate:

1. **AMR-DC**: the divisor carrier. This is a strict arithmetic avatar of
   the Boolean carrier of DOT.
2. **AMR-SR**: scale and residue on pairs of positive integers. This is a
   frontier-diagnostic branch with partial bridge arrows.

The two branches should not be mixed: they have different carriers,
different readings, and different recovery data.

---

# 1. AMR-DC: The Divisor Carrier as an Arithmetic Avatar of \(Q_n\)

Let

\[
N=p_1^{a_1}\cdots p_r^{a_r}.
\]

The divisor carrier is

\[
D(N)=\{d\in\mathbb N:d\mid N\}.
\]

In exponent coordinates,

\[
D(N)\cong \prod_{i=1}^r\{0,1,\ldots,a_i\}.
\]

This is the standard finite divisor lattice. The DOT reading begins when
this lattice is used as a carrier of a scene of distinction.

If \(N\) is square-free,

\[
N_n=p_1p_2\cdots p_n,
\]

then each divisor is determined by a subset of prime factors:

\[
D(N_n)\cong Q_n.
\]

The proper divisor carrier

\[
D^\circ(N_n)=D(N_n)\setminus\{1,N_n\}
\]

corresponds to the active domain:

\[
D^\circ(N_n)\cong U_n.
\]

Thus AMR-DC is a strict arithmetic bridge for the rank carrier of DOT in
the square-free case.

---

# 2. Divisor Complementarity

On \(D(N)\) there is divisor conjugation:

\[
\kappa_N(d)=\frac Nd.
\]

In older AMR notes this operation was sometimes denoted \(\delta_N\). In
the current corpus it is better to write \(\kappa_N\), because \(\delta\)
is already reserved for the coboundary operator in DOT.

The operation \(\kappa_N\) is an involution:

\[
\kappa_N^2=\operatorname{id}.
\]

For square-free \(N_n\), it is exactly complement of the subset of prime
factors:

\[
\kappa_N(d)\quad\leftrightarrow\quad J_n\setminus A.
\]

Therefore:

\[
\boxed{
\kappa_N \text{ is the arithmetic reading of limiting complementarity.}
}
\]

---

# 3. The Inter-Rank Law in the Divisor Reading

Let

\[
N_n=p_1\cdots p_n,
\qquad
N_{n+1}=N_n p_{n+1}.
\]

The general DOT law

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}
\]

has the following arithmetic form:

\[
\boxed{
D(N_n)\setminus\{1\}
\cong
D^\circ(N_{n+1})/\kappa_{N_{n+1}}.
}
\]

Meaning:

\[
\boxed{
\text{non-unit divisors of the current square-free product become}
}
\]

\[
\boxed{
\text{complementary axes of the proper divisor carrier of the next product.}
}
\]

The map is explicit:

\[
d\longmapsto \{d,N_{n+1}/d\}.
\]

The divisor \(1\) is not part of the active law because it lifts to the
limiting pair of the next rank:

\[
1\longmapsto \{1,N_{n+1}\}.
\]

This axis is removed when passing to \(D^\circ(N_{n+1})\).

## 3.1. The Step \(2\to3\)

\[
N_2=6,\qquad N_3=30.
\]

The non-unit divisors of \(6\) are

\[
2,\quad 3,\quad 6.
\]

They become three axes in \(D^\circ(30)\):

\[
2\mapsto\{2,15\},
\]

\[
3\mapsto\{3,10\},
\]

\[
6\mapsto\{6,5\}.
\]

This is the arithmetic reading of the three axes of the first complete
rank-3 scene.

## 3.2. The Step \(3\to4\)

\[
N_3=30,\qquad N_4=210.
\]

The non-unit divisors of \(30\) are

\[
2,3,5,6,10,15,30.
\]

They become seven axes in \(D^\circ(210)\):

\[
2\mapsto\{2,105\},
\]

\[
3\mapsto\{3,70\},
\]

\[
5\mapsto\{5,42\},
\]

\[
6\mapsto\{6,35\},
\]

\[
10\mapsto\{10,21\},
\]

\[
15\mapsto\{15,14\},
\]

\[
30\mapsto\{30,7\}.
\]

On the axial quotient this gives the same structure as Volume 5:

\[
D^\circ(210)/\kappa_{210}\cong PG(2,2).
\]

Thus the Fano plane in the arithmetic reading appears as the quotient of
the proper divisors of \(210\) by divisor conjugation.

---

# 4. Relations and Operators on \(D(N_n)\)

For square-free \(N_n\), a divisor \(d\) corresponds to a subset of prime
factors. Hence the standard DOT operators receive arithmetic readings.

## 4.1. Hamming Relations

If \(d_A,d_B\in D(N_n)\) correspond to subsets \(A,B\subseteq J_n\), then

\[
R_m(d_A,d_B)
\quad\Longleftrightarrow\quad
|A\triangle B|=m.
\]

Arithmetic meaning: two divisors differ in exactly \(m\) prime
coordinates.

## 4.2. Boundary and Coboundary

On the square-free carrier, the boundary removes one prime factor:

\[
\partial(d)=\sum_{p\mid d}\frac d p.
\]

The coboundary adds one missing prime factor:

\[
\delta(d)=\sum_{p\mid N,\;p\nmid d}dp.
\]

The sums are taken in the chain group over \(\mathbb F_2\), as in Volume
3.

The laws are preserved:

\[
\partial^2=0,\qquad \delta^2=0.
\]

Complementarity exchanges boundary and coboundary:

\[
\kappa_N\partial=\delta\kappa_N.
\]

So AMR-DC gives not only an arithmetic carrier, but also an arithmetic
avatar of the boundary grammar.

---

# 5. Recoverability as Part of AMR

A strong part of AMR-DC is its discipline of readings:

\[
\Pi=(X,R,q,\mathrm{rec}).
\]

Here \(X\) is the carrier, \(R\) is the relation, \(q\) is the reading, and
\(\mathrm{rec}\) is the recovery data.

Different readings preserve different data:

- exponent coordinates recover the divisor exactly;
- support of prime factors is exact only for square-free numbers;
- the pair reading \(\{d,N/d\}\) preserves the axis but forgets the side;
- the gcd reading of residue classes preserves the divisor state but
  forgets the unit data inside the fiber.

This agrees with the current DOT presentation: the observer is the
invariant structure coordinating a reading, and a trace must come with a
specified recovery status.

---

# 6. AMR-SR: Scale and Residue

AMR-SR has a different carrier:

\[
\mathcal R=\mathbb N_{>0}^2.
\]

Each pair decomposes as

\[
(a,b)=g(p,q),
\qquad
g=\gcd(a,b),
\qquad
\gcd(p,q)=1.
\]

The AMR-SR residue is

\[
\mathrm{Res}_{\mathrm{sr}}=(g-1)|p-q|.
\]

This branch studies scale, primitive direction, difference layer, and
residue. It is not the divisor carrier and is not identical with the rank
carrier of DOT.

The old partial bridge keeps its status:

\[
k=3\to (R_1,R_2),
\]

\[
k=4\to R_3.
\]

These arrows are bridge signatures. They are not a theorem of the form
\(k\mapsto R_k\), not an inter-rank lift, and not a functor
AMR-SR \(\to\) AMR-DC.

After the threshold, AMR-SR contains pair and axial towers, a synchronous
diagonal, and frontier plateaus. In the current corpus these should be
read as external diagnostics of scale-residue behavior, not as part of the
strict DOT core.

---

# 7. Integration Summary

The new DOT corpus changes the status of AMR as follows:

\[
\begin{array}{c|c|c}
\text{branch} & \text{carrier} & \text{status in current DOT}\\
\hline
\text{AMR-DC} & D(N) & \text{strict arithmetic bridge}\\
\text{AMR-SR} & \mathbb N_{>0}^2 & \text{frontier diagnostics}\\
\text{chain extension} & \prod_i\{0,\ldots,a_i\} & \text{extension beyond the Boolean case}\\
\end{array}
\]

Main strict AMR-DC formula:

\[
\boxed{
D(N_n)\setminus\{1\}
\cong
D^\circ(N_{n+1})/\kappa_{N_{n+1}}.
}
\]

Main methodological boundary:

\[
\boxed{
\mathrm{Res}_{\mathrm{sr}}\ne R_{\mathrm{oct}}.
}
\]

The AMR-SR residue is a scalar function on pairs of positive integers.
The octahedral relations of DOT are relations on a finite active carrier.
Any connection between them must be built as a separate bridge with an
explicit carrier, relation, reading, and recovery status.
