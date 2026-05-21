# DOT: Distinction Observable Theory

# Volume 2. Higher Ranks and Projective Architecture

Volume 0 introduced the foundation of DOT. Volume 1 unfolded the first
complete scene:

\[
\boxed{
S_3=(U_3;R_1,R_2,R_3).
}
\]

This volume builds the next strict layer: higher active carriers, shell
decomposition, limiting complementarity, axes, projective factors, and the
rank-to-rank lift by which configurations of one rank become axes of the
next rank.

The main line is

\[
\boxed{
U_n=Q_n\setminus\{0^n,1^n\}
}
\]

as the active carrier,

\[
\boxed{
U_n=\mathcal F(\partial\Delta^{n-1})
}
\]

as the carrier of nonempty proper faces of a simplex,

\[
\boxed{
\kappa:S_k^{(n)}\leftrightarrow S_{n-k}^{(n)}
}
\]

as limiting complementarity, and

\[
\boxed{
U_n/\kappa\cong PG(n-2,2)
}
\]

as the projective axial factor, and

\[
\boxed{
Q_{n-1}^*\cong U_n/\kappa_n
}
\]

as the inter-rank axial lift.

The constructions in this volume are standard finite combinatorics:
Boolean cubes, subsets, simplex faces, shell layers, complementarity,
Johnson and Kneser graphs, and binary projective spaces. The DOT-specific
content is the way these constructions describe rank growth of active
scenes.

---

# How to Read This Volume

Volume 2 shows how the rank-3 scene becomes the first case of a general
rank architecture.

Reading order:

1. general active carrier \(U_n\);
2. shells \(S_k^{(n)}\);
3. limiting complementarity \(\kappa\);
4. axes and axis types \((k,n-k)\);
5. projective factor \(U_n/\kappa\);
6. inter-rank lift \(Q_{n-1}^*\cong U_n/\kappa_n\);
7. rank \(4\): tetrahedral boundary and Fano plane;
8. rank \(5\): four-simplex boundary and \(PG(3,2)\);
9. the general rank principle.

---

# Basic Notation

\[
Q_n=\mathbb F_2^n
\]

is the full binary carrier of rank \(n\).

\[
U_n=Q_n\setminus\{0^n,1^n\}
\]

is the active carrier.

\[
S_k^{(n)}=\{x\in Q_n:\ |x|=k\}
\]

is the shell of weight \(k\).

\[
\kappa(x)=1^n+x
\]

is limiting complementarity.

Using a finite set \(J_n=\{1,\ldots,n\}\), one also has

\[
Q_n\cong\mathcal P(J_n),
\]

and

\[
U_n=\mathcal P(J_n)\setminus\{\varnothing,J_n\}.
\]

---

# 1. What Continues After Rank \(3\)

Rank \(3\) is the first complete active scene. It has:

\[
U_3=S_1^{(3)}\sqcup S_2^{(3)},
\]

\[
R_1=C_6,\qquad R_2=K_3\sqcup K_3,\qquad R_3=3K_2.
\]

Higher ranks preserve the same basic carrier principle and add new shell
types. The central change is that the axes stop being homogeneous.

At rank \(3\), every complement-pair has type

\[
(1,2).
\]

At rank \(4\), two types appear:

\[
(1,3),\qquad (2,2).
\]

At rank \(5\), the types are

\[
(1,4),\qquad (2,3).
\]

Thus higher ranks add more states together with new kinds of cuts.

---

# 2. General Active Carrier \(U_n\)

For any \(n\ge 1\),

\[
Q_n=\mathbb F_2^n.
\]

The two limiting states are

\[
0^n,\qquad 1^n.
\]

The active carrier is

\[
\boxed{
U_n=Q_n\setminus\{0^n,1^n\}.
}
\]

Its cardinality is

\[
|U_n|=2^n-2.
\]

In the subset language,

\[
Q_n\cong\mathcal P(J_n),
\]

and the limits are

\[
\varnothing,\qquad J_n.
\]

Therefore

\[
U_n=\mathcal P(J_n)\setminus\{\varnothing,J_n\}.
\]

This is the finite carrier between the lower and upper limits.

---

# 3. Shells and Layers

The shell of weight \(k\) is

\[
S_k^{(n)}=\{x\in Q_n:\ |x|=k\}.
\]

Its size is

\[
|S_k^{(n)}|=\binom nk.
\]

The full carrier decomposes as

\[
Q_n=\bigsqcup_{k=0}^{n}S_k^{(n)}.
\]

The active carrier removes the two limiting shells:

\[
U_n=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
\]

In the simplicial reading, \(S_k^{(n)}\) is the set of \((k-1)\)-faces of
\(\Delta^{n-1}\).

Thus the active carrier is the face carrier of the boundary:

\[
\boxed{
U_n=\mathcal F(\partial\Delta^{n-1}).
}
\]

---

# 4. Limiting Complementarity and Axes

Limiting complementarity is

\[
\kappa(A)=J_n\setminus A
\]

in the subset language, or

\[
\kappa(x)=1^n+x
\]

in the binary language.

It satisfies

\[
\boxed{
\kappa^2=\operatorname{id}.
}
\]

It sends the shell \(S_k^{(n)}\) to the shell \(S_{n-k}^{(n)}\):

\[
\boxed{
\kappa:S_k^{(n)}\leftrightarrow S_{n-k}^{(n)}.
}
\]

An axis is a complement-pair:

\[
H_A=\{A,J_n\setminus A\}.
\]

The type of the axis is

\[
(k,n-k),
\qquad k=|A|.
\]

Usually the smaller side is used to classify the axis:

\[
k\le n-k.
\]

At even rank, axes of type

\[
(n/2,n/2)
\]

are self-dual by size. Rank \(4\) is the first place where this occurs.

---

# 5. Projective Factor

The complement quotient is

\[
U_n/\kappa.
\]

Since every orbit has two elements,

\[
|U_n/\kappa|=\frac{2^n-2}{2}=2^{n-1}-1.
\]

The quotient can be identified with the nonzero vectors of
\(\mathbb F_2^{n-1}\), hence with the points of binary projective space:

\[
\boxed{
U_n/\kappa\cong PG(n-2,2).
}
\]

This is a strict finite theorem of the carrier architecture.

Examples:

\[
U_3/\kappa\cong PG(1,2),
\]

\[
U_4/\kappa\cong PG(2,2),
\]

\[
U_5/\kappa\cong PG(3,2).
\]

Thus the axial factor of the active scene is projective.

---

# 6. Inter-Rank Reading of the Projective Factor

The complement quotient also has a rank-to-rank meaning.

For the full carrier:

\[
Q_{n-1}\cong Q_n/\kappa_n.
\]

For the active carrier:

\[
\boxed{
Q_{n-1}^*\cong U_n/\kappa_n.
}
\]

Here \(Q_{n-1}^*=Q_{n-1}\setminus\{\varnothing\}\).

The empty configuration of \(Q_{n-1}\) lifts to the limiting axis
\(\{\varnothing,J_n\}\), which is absent from \(U_n\). The upper
configuration \(J_{n-1}\) remains as an internal axis of \(U_n\).

Thus the previous rank is preserved as the axial grammar of the next
rank. This is the inter-rank invariant of development used later for
reductions, operator towers, Fano readings, and cyclic avatars.

---

# 7. Rank \(4\): Active Boundary of the Tetrahedron

At rank \(4\),

\[
Q_4=\mathbb F_2^4,
\]

\[
|Q_4|=16.
\]

The active carrier is

\[
U_4=Q_4\setminus\{0000,1111\},
\]

so

\[
|U_4|=14.
\]

The shell decomposition is

\[
U_4=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)},
\]

with sizes

\[
4+6+4.
\]

In the simplicial reading, \(Q_4\cong\mathcal P(J_4)\). The simplex is the
tetrahedron \(\Delta^3\). The active carrier is the set of nonempty proper
faces of its boundary.

Thus rank \(4\) is the active boundary of a tetrahedron.

---

# 8. Middle Layer of Rank \(4\)

The middle shell is

\[
S_2^{(4)}.
\]

It has

\[
\binom42=6
\]

elements.

These elements are the edges of the tetrahedron.

On \(S_2^{(4)}\), complementarity pairs opposite edges:

\[
A\leftrightarrow J_4\setminus A.
\]

There are three such opposite-edge pairs.

With the natural incidence relations, this middle layer has the form of
an octahedral six-state carrier. It is the first place where the rank-3
octahedral form becomes an internal layer of a higher scene.

---

# 9. Rank \(4\) and the Fano Plane

The complement quotient of \(U_4\) has

\[
|U_4/\kappa|=2^{3}-1=7
\]

points.

By the general theorem,

\[
\boxed{
U_4/\kappa\cong PG(2,2).
}
\]

This is the Fano plane.

Thus the Fano plane appears as the projective axial factor of the active
rank-4 boundary.

The seven points of the factor correspond to the seven complement-pairs
in \(U_4\). These pairs include:

- four vertex-face pairs of type \((1,3)\);
- three edge-edge pairs of type \((2,2)\).

The Fano structure is not added from outside. It is the quotient of the
active tetrahedral boundary by complementarity.

---

# 10. Outer Shell and Cycles of Rank \(4\)

The outer shell of rank \(4\) is

\[
V_4=S_1^{(4)}\sqcup S_3^{(4)}.
\]

It has

\[
4+4=8
\]

vertices.

Complementarity pairs vertices and opposite faces:

\[
S_1^{(4)}\leftrightarrow S_3^{(4)}.
\]

The middle layer \(S_2^{(4)}\) is self-dual by shell degree.

Rank \(4\) therefore has two visible regimes:

- an outer vertex-face polarity;
- a middle opposite-edge polarity.

This is the first rank with more than one type of axis.

---

# 11. Rank \(5\): Active Boundary of the Four-Simplex

At rank \(5\),

\[
Q_5=\mathbb F_2^5,
\]

\[
|Q_5|=32.
\]

The active carrier is

\[
U_5=Q_5\setminus\{00000,11111\},
\]

and

\[
|U_5|=30.
\]

The shell decomposition is

\[
U_5=S_1^{(5)}\sqcup S_2^{(5)}\sqcup S_3^{(5)}\sqcup S_4^{(5)},
\]

with sizes

\[
5+10+10+5.
\]

In the simplicial reading, this is the active boundary of the
four-simplex \(\Delta^4\).

---

# 12. Middle Layers of Rank \(5\)

The two middle shells are

\[
S_2^{(5)},\qquad S_3^{(5)}.
\]

They have equal size:

\[
|S_2^{(5)}|=|S_3^{(5)}|=10.
\]

Complementarity exchanges them:

\[
\kappa:S_2^{(5)}\leftrightarrow S_3^{(5)}.
\]

On \(S_2^{(5)}\), the elements are the edges of the complete graph
\(K_5\).

The graph joining two edges when they share a vertex is the line graph:

\[
J(5,2)=L(K_5).
\]

The graph joining disjoint two-subsets is the Kneser graph:

\[
KG(5,2),
\]

which is the Petersen graph.

Thus rank \(5\) contains the Petersen graph as a strict middle-layer
structure.

---

# 13. Rank \(5\) and \(PG(3,2)\)

The complement quotient has

\[
|U_5/\kappa|=2^4-1=15
\]

points.

By the general theorem,

\[
\boxed{
U_5/\kappa\cong PG(3,2).
}
\]

Rank \(5\) is therefore the first rank whose projective factor is a
three-dimensional binary projective space.

The axis types are:

\[
(1,4),\qquad (2,3).
\]

The first type gives five vertex-hyperface pairs. The second gives ten
edge-triangle pairs.

---

# 14. Nonzero Carrier \(Q_5^*\) and Cycle \(C_{31}\)

Another useful carrier is

\[
Q_5^*=Q_5\setminus\{00000\}.
\]

It has

\[
31
\]

points.

This carrier is different from \(U_5\), which has \(30\) points:

\[
|U_5|=30,\qquad |Q_5^*|=31.
\]

The projective/Singer reading lives on \(Q_5^*\), not on \(U_5\).

This distinction is important:

- \(U_5\) is the active boundary carrier;
- \(Q_5^*\) is the nonzero projective carrier.

In the Singer reading, one obtains a cyclic structure of length \(31\).

---

# 15. General Rank Law

For every \(n\ge 2\):

\[
U_n=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
\]

The shell sizes are binomial:

\[
|S_k^{(n)}|=\binom nk.
\]

Complementarity exchanges shells:

\[
\kappa:S_k^{(n)}\leftrightarrow S_{n-k}^{(n)}.
\]

Axes are complement-pairs:

\[
H_A=\{A,J_n\setminus A\}.
\]

The quotient is projective:

\[
U_n/\kappa\cong PG(n-2,2).
\]

This is the basic projective-rank law of DOT.

The same factor is the axial lift of the previous rank:

\[
Q_{n-1}^*\cong U_n/\kappa_n.
\]

---

# 16. Reductions and Higher Ranks

The higher-rank principle can be stated as:

\[
\boxed{
\text{a higher rank gives internal carriers to reductions of a lower rank.}
}
\]

At rank \(3\), complement-pairs are axes of the first complete scene.

At rank \(4\), the axis quotient becomes the Fano plane, and the rank-3
octahedral form appears as the middle layer \(S_2^{(4)}\).

At rank \(5\), the projective factor becomes \(PG(3,2)\), and the middle
layers contain \(J(5,2)\) and the Petersen graph.

Thus rank growth is structural unfolding, not cardinal growth alone.

---

# 17. Boundary of This Volume

Volume 2 fixes:

- general active carriers \(U_n\);
- shell decomposition;
- complementarity;
- axes and axis types;
- projective factors;
- inter-rank lift \(Q_{n-1}^*\cong U_n/\kappa_n\);
- ranks \(4\) and \(5\) as first higher examples.

It does not yet develop:

- chain boundary operators \(\partial,\delta\);
- scene reductions \(\rho_D,\rho_F,\rho_C\);
- operator towers;
- Fano-tetrahedral details;
- topological avatars.

Those are handled in Volumes 3-6.

---

# Appendix A. Ranks \(2\)–\(5\)

\[
\begin{array}{c|c|c|c}
n & |Q_n| & |U_n| & \text{shell sizes of }U_n\\
\hline
2 & 4 & 2 & 2\\
3 & 8 & 6 & 3+3\\
4 & 16 & 14 & 4+6+4\\
5 & 32 & 30 & 5+10+10+5
\end{array}
\]

---

# Appendix B. Axis Types

\[
\begin{array}{c|c|c}
n & \text{axis types} & |U_n/\kappa|\\
\hline
3 & (1,2) & 3\\
4 & (1,3),(2,2) & 7\\
5 & (1,4),(2,3) & 15\\
6 & (1,5),(2,4),(3,3) & 31
\end{array}
\]

---

# Summary of Volume 2

The active carrier of rank \(n\) is

\[
U_n=Q_n\setminus\{0^n,1^n\}.
\]

It is the set of nonempty proper faces of the simplex:

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

Complementarity pairs every face with its opposite face:

\[
A\leftrightarrow J_n\setminus A.
\]

The quotient by this pairing is projective:

\[
U_n/\kappa\cong PG(n-2,2).
\]

The same quotient is the lifted nonempty carrier of the previous rank:

\[
Q_{n-1}^*\cong U_n/\kappa_n.
\]

Rank \(4\) gives the tetrahedral boundary and the Fano plane. Rank \(5\)
gives the four-simplex boundary, the Petersen graph in the middle layer,
and \(PG(3,2)\).
