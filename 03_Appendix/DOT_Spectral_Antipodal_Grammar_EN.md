# DOT: Spectral Antipodal Grammar

## Status

This appendix fixes the spectral layer that clarifies the place of Euler's
formula, cycles, Walsh-Hadamard harmonics, and antipodal complementarity in
DOT.

The main correction is:

\[
\boxed{
\text{finite combinatorics gives the sign } -1,\text{ not } e^{i\pi}
\text{ by itself.}
}
\]

The notation

\[
-1=e^{i\pi}
\]

appears only after choosing the complex Fourier representation. Thus this
is not a derivation of Euler's identity from combinatorics. It is a
spectral fact:

\[
\boxed{
\text{finite complementarity carries a spectral } \mathbb Z_2\text{-grading.}
}
\]

Euler's formula is the continuous harmonic notation of that grading on a
fundamental complex mode.

---

# 1. Rank 3 as the Distance Association Scheme of \(C_6\)

At rank \(3\), DOT has the full octahedral scene:

\[
\boxed{
S_3=(U_3;R_1,R_2,R_3).
}
\]

The relations are:

\[
R_1=C_6,
\qquad
R_2=K_3\sqcup K_3,
\qquad
R_3=3K_2.
\]

With the diagonal relation:

\[
A_0=I,
\qquad
A_1=R_1,
\qquad
A_2=R_2,
\qquad
A_3=R_3.
\]

Then:

\[
\boxed{
\mathbf J=A_0+A_1+A_2+A_3.
}
\]

Here \(\mathbf J\) is the all-ones matrix on the six-state carrier, not the
locus \(J_n\) used in the main DOT corpus.

Without the diagonal:

\[
\boxed{
K_6=R_1\sqcup R_2\sqcup R_3.
}
\]

This is the distance association scheme of \(C_6\):

\[
\boxed{
\text{the full rank-3 octahedral scene realizes the distance association
scheme of }C_6.
}
\]

In this reading:

- \(A_1\) is distance \(1\), the cycle \(C_6\);
- \(A_2\) is distance \(2\), the two-triangle layer \(K_3\sqcup K_3\);
- \(A_3\) is distance \(3\), the antipodal layer \(3K_2\).

The octahedral shell is:

\[
\boxed{
R_1\cup R_2\cong K_{2,2,2}.
}
\]

The internal axial layer is:

\[
\boxed{
R_3=3K_2.
}
\]

---

# 2. The \(P\)-Matrix of the \(C_6\) Scheme

For the distance scheme of \(C_6\), the first eigenmatrix \(P\) can be
written as:

\[
\boxed{
P=
\begin{pmatrix}
1 & 2 & 2 & 1 \\
1 & 1 & -1 & -1 \\
1 & -1 & -1 & 1 \\
1 & -2 & 2 & -1
\end{pmatrix}.
}
\]

Rows correspond to spectral blocks \(E_0,E_1,E_2,E_3\), while columns
correspond to relations \(A_0,A_1,A_2,A_3\).

The antipodal column is:

\[
\boxed{
A_3:\quad
\begin{pmatrix}
1\\
-1\\
1\\
-1
\end{pmatrix}.
}
\]

This is the spectral trace of the antipodal involution.

The nontrivial row sums vanish:

\[
1+1-1-1=0,
\]

\[
1-1-1+1=0,
\]

\[
1-2+2-1=0.
\]

Thus the vanishing of \(1+\kappa\) on odd modes is only one fragment of the
larger fact:

\[
\boxed{
\mathbf J \text{ kills all nontrivial spectral blocks.}
}
\]

---

# 3. Antipodal Involution and Fourier Reading

Let \(C_{2m}\) have shift operator \(T\). The half-turn is:

\[
\boxed{
\kappa=T^m.
}
\]

Then:

\[
\kappa^2=1.
\]

The characters of the cyclic group are:

\[
\chi_k(j)=e^{2\pi i k j/(2m)}.
\]

The shift \(T\) acts on the \(k\)-th mode as:

\[
T\mapsto e^{2\pi i k/(2m)}.
\]

The antipodal involution acts as:

\[
\boxed{
\kappa=T^m\mapsto e^{i\pi k}=(-1)^k.
}
\]

For odd \(k\):

\[
\kappa\mapsto -1.
\]

For even \(k\):

\[
\kappa\mapsto +1.
\]

Therefore:

\[
\boxed{
\frac{1+\kappa}{2}
\text{ projects onto } \kappa\text{-even modes,}
}
\]

\[
\boxed{
\frac{1-\kappa}{2}
\text{ projects onto } \kappa\text{-odd modes.}
}
\]

These projectors belong to the spectral linear representation over a field
of characteristic not \(2\), for example over \(\mathbb R\) or
\(\mathbb C\). They are not operations inside the original
\(\mathbb F_2\)-combinatorial carrier, where division by \(2\) is not
available.

Euler's formula enters only as the notation of an odd complex mode:

\[
\boxed{
\kappa\mapsto -1=e^{i\pi}.
}
\]

Hence:

\[
\boxed{
1+\kappa\mapsto 1+e^{i\pi}=0.
}
\]

The correct statement is:

\[
\boxed{
e^{i\pi}+1=0
\text{ is the Fourier-language rendering of the eigenvalue }-1
\text{ of antipodal complementarity.}
}
\]

---

# 4. Two Different \(\mathbb Z_2\)-Involutions

Two different operations must not be identified.

## 4.1. Antipodal Involution \(\kappa\)

\[
\boxed{
\kappa=T^m.
}
\]

It commutes with the cyclic shift:

\[
\kappa T=T\kappa.
\]

It preserves the Fourier mode:

\[
\kappa\chi_k=(-1)^k\chi_k.
\]

This is complementarity / antipodality.

## 4.2. The Bipartite Operator \(\beta\)

On functions on \(C_{2m}\):

\[
\boxed{
(\beta f)(j)=(-1)^j f(j).
}
\]

It anticommutes with the shift:

\[
\boxed{
T\beta=-\beta T.
}
\]

In Fourier language it shifts modes:

\[
\boxed{
\beta:\chi_k\mapsto\chi_{k+m}.
}
\]

This is not antipodality. It is the bipartite sign structure responsible
for the spectral symmetry:

\[
\lambda\leftrightarrow-\lambda.
\]

Thus:

\[
\boxed{
\kappa \text{ gives an antipodal sign within a mode;}
}
\]

\[
\boxed{
\beta \text{ gives a bipartite transfer between modes.}
}
\]

DOT must keep these two kinds of minus signs separate.

---

# 5. Hypercube Generalization

For DOT, the full Boolean carrier is more native than \(C_{2m}\):

\[
Q_n=\mathbb F_2^n.
\]

Antipodal complementarity is:

\[
\boxed{
\kappa(x)=x+\mathbf 1,
}
\]

where

\[
\mathbf 1=(1,\ldots,1).
\]

The Walsh-Hadamard characters are:

\[
\boxed{
\chi_a(x)=(-1)^{a\cdot x}.
}
\]

Then:

\[
\chi_a(\kappa x)
=
\chi_a(x+\mathbf 1)
=
(-1)^{a\cdot \mathbf 1}\chi_a(x).
\]

But:

\[
a\cdot \mathbf 1=|a|\pmod 2.
\]

Hence:

\[
\boxed{
\chi_a(\kappa x)=(-1)^{|a|}\chi_a(x).
}
\]

Equivalently:

\[
\boxed{
\kappa\chi_a=(-1)^{|a|}\chi_a.
}
\]

This is the central spectral law for higher ranks:

\[
\boxed{
\text{complementarity splits the Boolean spectrum by parity of Walsh weight.}
}
\]

Even Walsh weight:

\[
|a|\equiv0\pmod2
\quad\Rightarrow\quad
\kappa\chi_a=+\chi_a.
\]

Odd Walsh weight:

\[
|a|\equiv1\pmod2
\quad\Rightarrow\quad
\kappa\chi_a=-\chi_a.
\]

Thus the \(C_6\) observation becomes part of the general DOT grammar:

\[
\boxed{
C_6 \text{ gives the cyclic example,}
\qquad
Q_n \text{ gives the native Boolean form of the law.}
}
\]

---

# 6. Quotient and Twisted Sections

Let there be an antipodal cover:

\[
\pi:X\to X/\kappa.
\]

Functions on \(X\) split into two parts:

\[
f(\kappa x)=f(x)
\]

and

\[
f(\kappa x)=-f(x).
\]

The first kind descends to the quotient \(X/\kappa\). The second kind does
not descend as an ordinary function; it is a twisted section with respect
to the nontrivial sign character of \(\mathbb Z_2\).

In operator form:

\[
\boxed{
\mathcal F(X)=\mathcal F^+_\kappa\oplus\mathcal F^-_\kappa,
}
\]

\[
\mathcal F^+_\kappa=\ker(\kappa-I),
\qquad
\mathcal F^-_\kappa=\ker(\kappa+I).
\]

The projectors are:

\[
\boxed{
\Pi_+=\frac{I+\kappa}{2},
\qquad
\Pi_-=\frac{I-\kappa}{2}.
}
\]

Again, these are projectors in the spectral representation over
\(\mathbb R\) or \(\mathbb C\), not operations inside the original
\(\mathbb F_2\)-carrier.

In DOT terms:

\[
\boxed{
\mathcal F^+_\kappa
\text{ is the quotient reading of axes;}
}
\]

\[
\boxed{
\mathcal F^-_\kappa
\text{ is the twisted reading of the polar lift.}
}
\]

This refines the inter-rank law:

\[
Q_n^*\cong U_{n+1}/\kappa.
\]

Axes of the next rank live in the quotient, while cyclic traversals and
sign traces may live in the twisted anti-invariant layer.

---

# 7. Dihedral Reading

For \(C_{2m}\), the cyclic group \(\mathbb Z_{2m}\) sits inside the
dihedral symmetry group of the cycle.

The element:

\[
\kappa=T^m
\]

is central in the cyclic part and appears as the central half-turn in the
dihedral symmetry.

In irreducible representations, a central element acts by a scalar. In the
standard two-dimensional representation, the half-turn acts as:

\[
\boxed{
\kappa\mapsto -I.
}
\]

This is the representation-theoretic version of the same fact:

\[
\boxed{
\text{antipodality}
\to
\text{central half-turn}
\to
\text{sign central character}.
}
\]

This layer is not required for the DOT core, but it is useful as a bridge
to representation theory.

---

# 8. What This Changes in DOT

## 8.1. Rank 3

Rank \(3\) now has three coordinated readings:

1. graph reading:

\[
K_6=R_1\sqcup R_2\sqcup R_3;
\]

2. association-scheme reading:

\[
\mathbf J=A_0+A_1+A_2+A_3;
\]

3. spectral reading:

\[
A_3=\kappa
\quad\leadsto\quad
\kappa|_{E_k}=(-1)^k.
\]

## 8.2. Euler Formula

One must not say:

\[
\text{DOT derives } e^{i\pi}+1=0.
\]

The correct statement is:

\[
\boxed{
\text{DOT fixes the finite source of the sign }-1,
\text{ while Fourier language writes it as }e^{i\pi}.
}
\]

## 8.3. Higher Ranks

For \(Q_n\):

\[
\boxed{
\kappa\chi_a=(-1)^{|a|}\chi_a.
}
\]

This connects:

- complementarity;
- parity;
- Walsh-Hadamard harmonics;
- the quotient \(U_n/\kappa\);
- the twisted polar lift.

## 8.4. Main Spectral Law

\[
\boxed{
\text{antipodal complementarity defines a spectral } \mathbb Z_2\text{-grading.}
}
\]

This is stronger and more general than the particular \(C_6\) reading via
Euler's formula.

---

# 9. Open Directions

1. How the anti-invariant layer \(\mathcal F^-_\kappa\) lifts under
\(n\to n+1\).

2. How the spectral \(\mathbb Z_2\)-grading relates to the three holding
conditions \(\mathcal H_D,\mathcal H_F,\mathcal H_C\).

3. How to separate the cyclic \(C_6\) reading from the Walsh-Hadamard
reading of the full cube \(Q_n\).

4. Whether the operator \(T\) can be described as a choice of cyclic line
inside the spectral scheme rather than as a primitive operator.

5. How to use the projectors

\[
\Pi_\pm=\frac{I\pm\kappa}{2}
\]

for a formal account of quotient and twisted readings of a scene.

---

# 10. Summary

Spectral antipodal grammar adds a strict layer to DOT:

\[
\boxed{
\text{complementarity}
\to
\text{antipodal involution}
\to
\mathbb Z_2\text{-grading of the spectrum}
\to
\text{quotient/twisted reading}.
}
\]

Euler's formula has a modest but precise place in this layer:

\[
\boxed{
e^{i\pi}+1=0
\text{ is the complex-Fourier notation of the vanishing of an anti-invariant pair.}
}
\]

In the finite core, the sign remains:

\[
\boxed{
\kappa=-1 \text{ on odd modes.}
}
\]

In the continuous avatar, this sign is written as a phase:

\[
\boxed{
-1=e^{i\pi}.
}
\]
