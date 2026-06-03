# Internal Evolution of the Active Carrier

Status: research note to the DOT corpus.

The aim of this document is to describe not the numerical cardinality of the
active carrier, but the change in its internal structure under transitions
between ranks. We are interested in how, inside \(U_n\), the layers, relations,
cycles, middle shells, octahedral modules and projective axes are transformed.

Main formula:

\[
\boxed{
\text{a rank transition develops the internal scene through copying,
stitching and a change in the role of the boundary.}
}
\]

---

# 1. Initial carrier

The full rank-\(n\) carrier:

\[
Q_n=\mathbb F_2^n.
\]

The active carrier:

\[
U_n=Q_n\setminus\{0^n,1^n\}.
\]

In the language of subsets:

\[
U_n\cong\mathcal P(J_n)\setminus\{\varnothing,J_n\}.
\]

In simplicial language:

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

Here \(U_n\) is the carrier of the nonempty proper faces of the
\((n-1)\)-simplex.

---

# 2. The transition \(n\to n+1\)

The full carrier splits into two copies of the previous rank:

\[
Q_{n+1}=0Q_n\sqcup 1Q_n.
\]

The active carrier receives two copies of the old active carrier and two
new active points:

\[
\boxed{
U_{n+1}
=
0U_n
\sqcup
1U_n
\sqcup
\{0\,1^n,\;1\,0^n\}.
}
\]

The two points \(0\,1^n\) and \(1\,0^n\) come from the limit pair of the old
rank. The old limits enter into the interior of the new active carrier.

This yields an important principle:

\[
\boxed{
\text{the limit pair of one rank becomes the active pair of the next.}
}
\]

---

# 3. The law of layers

The weight-\(k\) layer:

\[
S_k^{(n)}=\{x\in Q_n:|x|=k\}.
\]

Under the transition \(n\to n+1\):

\[
\boxed{
S_k^{(n+1)}
=
0S_k^{(n)}
\sqcup
1S_{k-1}^{(n)}.
}
\]

This is Pascal's law in structural form. The new layer is assembled from two
adjacent old layers.

Examples:

\[
S_2^{(4)}
=
0S_2^{(3)}
\sqcup
1S_1^{(3)}.
\]

The middle layer of rank \(4\) is assembled from two chambers of rank \(3\).

\[
S_2^{(5)}
=
0S_2^{(4)}
\sqcup
1S_1^{(4)}.
\]

\[
S_3^{(5)}
=
0S_3^{(4)}
\sqcup
1S_2^{(4)}.
\]

The middle layer of rank \(4\) enters into both middle shells of rank \(5\).

---

# 4. The law of relations

Let \(R_d^{(n)}\) be the Hamming-distance-\(d\) relation on the
active carrier of rank \(n\):

\[
xR_d^{(n)}y
\quad\Longleftrightarrow\quad
d_H(x,y)=d.
\]

In the full binary carrier, under raising of the rank:

\[
\boxed{
R_d^{(n+1)}
=
0R_d^{(n)}
\sqcup
1R_d^{(n)}
\sqcup
(0/1)R_{d-1}^{(n)}.
}
\]

Meaning:

1. inside the lower copy the old \(R_d\) remains \(R_d\);
2. inside the upper copy the old \(R_d\) remains \(R_d\);
3. between the copies the old \(R_{d-1}\) becomes the new \(R_d\).

In this way the old relation raises its Hamming layer under the
inter-copy stitching.

For rank \(3\to4\):

\[
R_1^{(3)}\leadsto R_1^{(4)}\text{ inside the copies and }R_2^{(4)}
\text{ between the copies}.
\]

\[
R_2^{(3)}\leadsto R_2^{(4)}\text{ inside the copies and }R_3^{(4)}
\text{ between the copies}.
\]

\[
R_3^{(3)}\leadsto R_3^{(4)}\text{ inside the copies and }R_4^{(4)}
\text{ between the copies}.
\]

---

# 4A. The layer-development functor

The previous section says how relations are transferred between ranks.
A stronger formulation: adjacent interior layers of one rank can
unfold into a graph of the next rank.

Consider a pair of adjacent layers:

\[
S_k^{(n)},\qquad S_{k+1}^{(n)}.
\]

Between them there is a boundary incidence:

\[
A\subset B,
\qquad
A\in S_k^{(n)},\quad B\in S_{k+1}^{(n)}.
\]

Under the transition to rank \(n+1\) the layer \(S_{k+1}^{(n+1)}\) splits:

\[
\boxed{
S_{k+1}^{(n+1)}
=
0S_{k+1}^{(n)}
\sqcup
1S_k^{(n)}.
}
\]

Now on this new layer we take the interior relation \(R_2\). We obtain the
Johnson graph:

\[
\boxed{
R_2|_{S_{k+1}^{(n+1)}}=J(n+1,k+1).
}
\]

Its structure splits into three parts:

\[
\boxed{
J(n+1,k+1)
=
J(n,k+1)
\;\cup\;
J(n,k)
\;\cup\;
\operatorname{Inc}(S_k^{(n)},S_{k+1}^{(n)}).
}
\]

Here:

1. \(J(n,k+1)\) lives inside the copy \(0S_{k+1}^{(n)}\);
2. \(J(n,k)\) lives inside the copy \(1S_k^{(n)}\);
3. \(\operatorname{Inc}(S_k^{(n)},S_{k+1}^{(n)})\) is the boundary incidence
   \(A\subset B\), having become inter-copy edges.

This is precisely what may be called the layer-development functor:

\[
\boxed{
\mathcal D_{n,k}:
\big(S_k^{(n)},S_{k+1}^{(n)},\partial\big)
\longmapsto
\big(S_{k+1}^{(n+1)},J(n+1,k+1)\big).
}
\]

Meaning:

\[
\boxed{
\text{a boundary incidence of rank }n\text{ becomes graph connectivity
of rank }n+1.
}
\]

This place no longer reduces to enumerating known layers. The DOT reading
here consists in the fact that an interior layer together with its boundary
unfolds into the next graph level.

## 4A.1. First example: two triads give the octahedron

Take \(n=3,\ k=1\):

\[
S_1^{(3)},\qquad S_2^{(3)}.
\]

Each layer has three points:

\[
3+3.
\]

On them:

\[
J(3,1)=K_3,
\qquad
J(3,2)=K_3.
\]

The boundary incidence \(S_1^{(3)}\leftrightarrow S_2^{(3)}\) connects the
vertices of the triangle with its edges.

After development:

\[
S_2^{(4)}
=
0S_2^{(3)}
\sqcup
1S_1^{(3)}.
\]

On the new layer:

\[
\boxed{
J(4,2)\cong K_{2,2,2}.
}
\]

That is:

\[
\boxed{
K_3\sqcup K_3
\;+\;
\text{vertex--edge incidence}
\quad\longmapsto\quad
\text{octahedron}.
}
\]

This is an exact operation: two chamber triads of rank \(3\) unfold into the
middle octahedron of rank \(4\).

## 4A.2. Second example: octahedron and tetrahedron give \(J(5,2)\)

Take \(n=4,\ k=1\):

\[
S_1^{(4)},\qquad S_2^{(4)}.
\]

Here:

\[
J(4,1)=K_4,
\]

\[
J(4,2)\cong K_{2,2,2}.
\]

The boundary incidence connects the vertices of the tetrahedron with its
edges.

After development:

\[
S_2^{(5)}
=
0S_2^{(4)}
\sqcup
1S_1^{(4)}.
\]

On the new layer:

\[
\boxed{
J(5,2)=L(K_5).
}
\]

That is, the line graph of \(K_5\) arises as the development of the pair:

\[
\boxed{
\text{tetrahedral vertices}
\;+\;
\text{octahedral layer of edges}
\;+\;
\text{incidence}
\quad\longmapsto\quad
J(5,2).
}
\]

## 4A.3. The middle line as iteration of the functor

The functor \(\mathcal D_{n,k}\) gives a new formulation of the middle line:

\[
3+3\longmapsto6,
\]

\[
6+4\longmapsto10,
\]

\[
10+10\longmapsto20,
\]

\[
20+15\longmapsto35,
\]

\[
35+35\longmapsto70.
\]

Here each number denotes a layer, and the arrow denotes the construction of a
new Johnson graph from two old layers and their boundary incidence.

In this form the rank transition becomes a graph operation:

\[
\boxed{
\text{layer + adjacent layer + boundary}
\quad\longmapsto\quad
\text{graph of the next rank}.
}
\]

This is a stronger candidate for an independent finding than the simple
observation about middle layers.

---

# 5. Rank \(3\): the first complete scene

The active carrier:

\[
U_3=S_1^{(3)}\sqcup S_2^{(3)}.
\]

Sizes:

\[
3+3.
\]

Three relations:

\[
(U_3,R_1)\cong C_6,
\]

\[
(U_3,R_2)\cong K_3\sqcup K_3,
\]

\[
(U_3,R_3)\cong 3K_2.
\]

The octahedral skeleton:

\[
\boxed{
(U_3,R_1\cup R_2)\cong K_{2,2,2}.
}
\]

At rank \(3\) the octahedron is the entire active scene.

---

# 6. The transition \(3\to4\)

The active carrier of rank \(4\):

\[
U_4=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}.
\]

Sizes:

\[
4+6+4.
\]

The middle layer:

\[
S_2^{(4)}=6.
\]

It is assembled from two old chambers:

\[
S_2^{(4)}
=
0S_2^{(3)}
\sqcup
1S_1^{(3)}.
\]

On this layer:

\[
\boxed{
R_2|_{S_2^{(4)}}\cong K_{2,2,2}.
}
\]

Consequently:

\[
\boxed{
\text{the octahedral shell of rank }3\text{ becomes the middle layer of rank }4.
}
\]

In doing so, the role of the relation changes. At rank \(3\) the octahedral
shell was given by \(R_1\cup R_2\). In the middle layer of rank \(4\) the
octahedral connectivity is manifested inside \(R_2\).

---

# 7. The cycle \(C_6\) and the graph \(R_1\)

At rank \(3\):

\[
(U_3,R_1)\cong C_6.
\]

After the transition \(3\to4\) this cycle does not become a single cycle on
\(14\) vertices. It turns into two copies of the old cycle, an inter-copy
stitching, and two new active limit points.

At rank \(4\):

\[
|U_4|=14,\qquad |E(R_1)|=24.
\]

The cyclomatic number of the graph \(R_1(U_4)\):

\[
\beta_1=24-14+1=11.
\]

General formula:

\[
\boxed{
|E(R_1(U_n))|=n(2^{n-1}-2).
}
\]

\[
\boxed{
\beta_1(R_1(U_n))=(n-2)2^{n-1}-2n+3.
}
\]

First values:

| rank | \(|U_n|\) | \(|E(R_1)|\) | \(\beta_1(R_1)\) |
|---:|---:|---:|---:|
| 3 | 6 | 6 | 1 |
| 4 | 14 | 24 | 11 |
| 5 | 30 | 70 | 41 |
| 6 | 62 | 180 | 119 |
| 7 | 126 | 434 | 309 |
| 8 | 254 | 1008 | 755 |
| 9 | 510 | 2286 | 1777 |
| 10 | 1022 | 5100 | 4079 |
| 12 | 4094 | 24552 | 20459 |
| 16 | 65534 | 524256 | 458723 |
| 20 | 1048574 | 10485720 | 9437147 |
| 24 | 16777214 | 201326544 | 184549331 |

The \(R_1\) line develops as follows:

\[
\boxed{
C_6\longrightarrow\text{a growing network of cycles of the binary boundary.}
}
\]

---

# 8. The outer cycle

There is an outer layer:

\[
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
\]

Its size:

\[
|V_n|=2n.
\]

On it arises the cross-polytope graph:

\[
K_{2,2,\ldots,2}.
\]

In this graph one can choose a Hamiltonian cycle:

\[
C_{2n}.
\]

This yields an outer cyclic line:

\[
C_6,\quad C_8,\quad C_{10},\quad C_{12},\quad C_{14},\ldots
\]

At rank \(3\):

\[
V_3=U_3,
\]

so the outer cycle coincides with the cycle of the entire active scene.

Starting from rank \(4\), the outer cycle is the skeleton of the outer shell,
not of the entire scene.

---

# 9. The middle line

The interior middle of the active carrier alternates.

Odd ranks give a pair of middle layers:

\[
S_{(n-1)/2}^{(n)}
\leftrightarrow
S_{(n+1)/2}^{(n)}.
\]

Even ranks give a single self-dual middle layer:

\[
S_{n/2}^{(n)}.
\]

Table up to rank \(24\):

| rank | \(|U_n|\) | middle structure |
|---:|---:|---|
| 3 | 6 | \(3+3\) |
| 4 | 14 | \(6\) |
| 5 | 30 | \(10+10\) |
| 6 | 62 | \(20\) |
| 7 | 126 | \(35+35\) |
| 8 | 254 | \(70\) |
| 9 | 510 | \(126+126\) |
| 10 | 1022 | \(252\) |
| 11 | 2046 | \(462+462\) |
| 12 | 4094 | \(924\) |
| 13 | 8190 | \(1716+1716\) |
| 14 | 16382 | \(3432\) |
| 15 | 32766 | \(6435+6435\) |
| 16 | 65534 | \(12870\) |
| 17 | 131070 | \(24310+24310\) |
| 18 | 262142 | \(48620\) |
| 19 | 524286 | \(92378+92378\) |
| 20 | 1048574 | \(184756\) |
| 21 | 2097150 | \(352716+352716\) |
| 22 | 4194302 | \(705432\) |
| 23 | 8388606 | \(1352078+1352078\) |
| 24 | 16777214 | \(2704156\) |

The main law:

\[
\boxed{
\text{an odd rank develops the middle pair, an even rank assembles it
into a self-dual middle.}
}
\]

---

# 10. Johnson and Kneser layers

Inside the layer \(S_k^{(n)}\) the relation \(R_2\) gives the Johnson graph:

\[
\boxed{
R_2|_{S_k^{(n)}}=J(n,k).
}
\]

On the same layer the relation of maximal disjointness gives the Kneser
graph:

\[
KG(n,k).
\]

Examples:

\[
J(3,1)=K_3,\qquad J(3,2)=K_3.
\]

These are the two triads of rank \(3\).

\[
J(4,2)\cong K_{2,2,2}.
\]

This is the middle octahedron of rank \(4\).

\[
J(5,2)=L(K_5).
\]

And

\[
KG(5,2)
\]

is the Petersen graph.

After rank \(5\) the internal geometry of the active carrier develops
through the family of Johnson and Kneser graphs on the middle layers.

---

# 11. Projective axes

The polar involution:

\[
\kappa(x)=1^n-x.
\]

The axes are the \(\kappa\)-pairs:

\[
\{x,\kappa x\}.
\]

The number of axes:

\[
|U_n/\kappa|=2^{n-1}-1.
\]

The projective quotient:

\[
\boxed{
U_n/\kappa\cong PG(n-2,2).
}
\]

The types of axes are given by the sizes of the sides:

\[
(k,n-k).
\]

Up to rank \(24\) the number of types grows as \(\lfloor n/2\rfloor\).

Special cases:

| rank | axis types |
|---:|---|
| 3 | \((1,2)\) |
| 4 | \((1,3),(2,2)\) |
| 5 | \((1,4),(2,3)\) |
| 6 | \((1,5),(2,4),(3,3)\) |
| 7 | \((1,6),(2,5),(3,4)\) |
| 8 | \((1,7),(2,6),(3,5),(4,4)\) |

The self-dual type \((k,k)\) appears only in even ranks.

---

# 12. Four lines of evolution

The internal evolution of \(U_n\) is conveniently traced along four lines.

## 12.1. Outer shell

\[
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
\]

It gives:

\[
K_{2,2,\ldots,2},
\qquad
C_{2n}.
\]

This is the line of the outer skeleton.

## 12.2. Middle shell

\[
3+3,\quad 6,\quad 10+10,\quad 20,\quad 35+35,\quad 70,\ldots
\]

This is the line of the internal geometry.

## 12.3. Layer graphs

\[
J(n,k),\qquad KG(n,k).
\]

This is the line of the internal combinatorics of the shells.

## 12.4. Relations \(R_d\)

\[
R_d^{(n+1)}
=
0R_d^{(n)}
\sqcup
1R_d^{(n)}
\sqcup
(0/1)R_{d-1}^{(n)}.
\]

This is the line of the transfer of the grammar of distinctions between ranks.

---

# 13. The role of the octahedron

The octahedron has several stages.

1. Rank \(3\): the entire active scene.

\[
(U_3,R_1\cup R_2)\cong K_{2,2,2}.
\]

2. Rank \(4\): the middle layer.

\[
S_2^{(4)},\qquad R_2|_{S_2^{(4)}}\cong K_{2,2,2}.
\]

3. Rank \(5\): a local module inside \(S_2^{(5)}\) and \(S_3^{(5)}\).

4. Higher ranks: a recurring local configuration in the Johnson graphs.

Summary:

\[
\boxed{
\text{the octahedron does not vanish; it changes status: scene, layer,
module, local pattern.}
}
\]

---

# 14. Connection with the three reductions

The three reductions give three rules of internal evolution.

\[
\rho_D\leadsto\kappa.
\]

This is the line of limit axes and projective quotients:

\[
U_n/\kappa\cong PG(n-2,2).
\]

\[
\rho_F\leadsto\partial,\delta.
\]

This is the line of layers, traces and transitions between shells:

\[
S_k^{(n)}\to S_{k-1}^{(n)}.
\]

\[
\rho_C\leadsto T.
\]

This is the line of cycles and closures:

\[
C_6,\quad C_{2n},\quad R_1\text{-cycles},\quad C_{|U_n|}.
\]

At rank \(3\) all three lines coincide on one small scene. At higher
ranks they diverge and form different atlases of one active carrier.

---

# 15. Conclusion

The internal development of the active carrier is given not by a single
formula, but by the coordination of four recursions:

\[
\boxed{
U_{n+1}
=
0U_n
\sqcup
1U_n
\sqcup
\{0\,1^n,\;1\,0^n\};
}
\]

\[
\boxed{
S_k^{(n+1)}
=
0S_k^{(n)}
\sqcup
1S_{k-1}^{(n)};
}
\]

\[
\boxed{
R_d^{(n+1)}
=
0R_d^{(n)}
\sqcup
1R_d^{(n)}
\sqcup
(0/1)R_{d-1}^{(n)};
}
\]

\[
\boxed{
U_n/\kappa\cong PG(n-2,2).
}
\]

Rank \(3\) is the first complete scene of this system. Rank \(4\)
carries the octahedron over into the middle layer. Rank \(5\) carries the
middle layer over into two middle shells and introduces the Petersen graph.
Beyond that, the family of hypersimplicial middle layers, Johnson graphs,
Kneser graphs and projective axes develops.

The main formula of the research:

\[
\boxed{
\text{the active carrier grows as the boundary of a simplex, while its internal
grammar grows as a system of transferable relations.}
}
\]

---

# 16. A possible external presentation

For external discussion it is better not to begin with DOT as a whole
theory. A single visible configuration works more strongly.

## 16.1. A configuration for discrete mathematics

Topic:

> Remove the two opposite vertices from the \(n\)-cube and look at the
> induced Hamming-distance structure. At \(n=3\) the active carrier is an
> octahedron; at \(n=4\) the same octahedron reappears as the middle layer
> of the tetrahedral boundary; afterward it becomes a recurring Johnson
> graph module.

Content:

1. \(U_n=Q_n\setminus\{0^n,1^n\}\).
2. \(U_3\) gives an octahedron.
3. \(S_2^{(4)}\) again gives an octahedron.
4. The middle line:

\[
3+3\to6\to10+10\to20\to35+35\to70.
\]

5. Inside the layers \(J(n,k)\) and \(KG(n,k)\) appear.

This is sufficiently obvious, verifiable, and does not require accepting DOT.

## 16.2. A configuration for philosophy of mathematics

Topic:

> A finite distinction can be studied through what remains after removing
> the two total poles of a binary carrier. The first complete active
> boundary is not a line or a triangle, but a six-state octahedral scene
> carrying three different relation types at once: a cycle, two triads,
> and three opposite pairs.

Content:

1. distinction as a held non-coincidence;
2. two limits \(0^n,1^n\);
3. the active boundary between the limits;
4. the first complete scene \(U_3\);
5. three regimes of relations:

\[
C_6,\qquad K_3\sqcup K_3,\qquad 3K_2.
\]

This is better for discussing the meaning of "objects as stable forms
of distinction".

## 16.3. What should not be brought into the first post

The first external post should not include:

1. the entire DOT vocabulary;
2. the reductions \(\rho_D,\rho_F,\rho_C\);
3. the observer;
4. Fermat primes;
5. topological avatars;
6. large philosophical claims.

The first post should be a verifiable combinatorial picture.

## 16.4. The best first hook

The strongest first hook:

\[
\boxed{
3+3\to6\to10+10\to20\to35+35\to70
}
\]

and alongside it:

\[
\boxed{
\text{octahedron as whole scene}
\to
\text{octahedron as middle layer}
\to
\text{octahedron as local module}.
}
\]

This is short, visible, verifiable by ordinary combinatorics, and leaves room
for further conversation.
