# DOT: the Fano projection and the tetrahedral-barycentric reading of rank 4

Status: bridge Russian draft for the corpus.

This document fixes the connection between three objects:

1. the projective Fano reading on \(7\) points;
2. the tetrahedral reading of the Boolean carrier \(Q_4=\mathcal P(J_4)\);
3. the octahedron \(S_2^{(4)}\) as the layer of edge midpoints of the tetrahedron.

The main idea:

\[
\text{Fano}
\quad\text{may be read as a projective shadow of a deeper tetrahedral layer }Q_4.
\]

Here the strict core remains the Boolean lattice of faces of the tetrahedron, and the Fano image is a projective reading of this lattice.

---

# 1. The initial carrier

Let

\[
J_4=\{1,2,3,4\}.
\]

Then the power-set carrier of rank \(4\):

\[
Q_4=\mathcal P(J_4).
\]

Its layers:

\[
S_k^{(4)}=\{A\subseteq J_4: |A|=k\}.
\]

Cardinalities:

\[
|S_0|=1,\quad |S_1|=4,\quad |S_2|=6,\quad |S_3|=4,\quad |S_4|=1.
\]

That is:

\[
16=1+4+6+4+1.
\]

The punctured active carrier of DOT:

\[
X_4=Q_4\setminus\{\varnothing,J_4\}.
\]

Its size:

\[
|X_4|=14.
\]

In expanded form:

\[
X_4=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}.
\]

If one needs to keep the center of the tetrahedron, then instead of the active \(X_4\) one uses the closed nonempty reading:

\[
Q_4^\*=Q_4\setminus\{\varnothing\}
=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}\sqcup S_4^{(4)}.
\]

Here \(S_4^{(4)}=\{J_4\}\) is the center of the full tetrahedral closure, but not an active vertex of \(X_4\).

---

# 2. The barycentric map

Take a regular tetrahedron with vertices

\[
v_1,v_2,v_3,v_4\in\mathbb R^3
\]

and the normalization

\[
v_1+v_2+v_3+v_4=0.
\]

For a nonempty subset \(A\subseteq J_4\) define the barycenter:

\[
b(A)=\frac1{|A|}\sum_{i\in A}v_i.
\]

Then each nonempty element of \(Q_4^\*\) receives a geometric position:

\[
A\subseteq J_4,\ A\neq\varnothing
\quad\longmapsto\quad
b(A).
\]

The layers receive the usual geometric reading:

\[
S_1^{(4)}:\quad \text{vertices of the tetrahedron},
\]

\[
S_2^{(4)}:\quad \text{edge midpoints of the tetrahedron},
\]

\[
S_3^{(4)}:\quad \text{face centers of the tetrahedron},
\]

\[
S_4^{(4)}:\quad \text{center of the tetrahedron}.
\]

For a regular tetrahedron the face centers are simultaneously the points of tangency of the inscribed sphere with the faces. Therefore the layer \(S_3^{(4)}\) can be read as the layer of the four tangency points of the inscribed sphere.

---

# 3. The main chain

The barycentric reading gives the chain:

\[
\text{tetrahedron}
\longrightarrow
\text{octahedron of edge midpoints}
\longrightarrow
\text{dual tetrahedron of tangency points}
\longrightarrow
\text{center}.
\]

In terms of layers:

\[
S_1^{(4)}
\longrightarrow
S_2^{(4)}
\longrightarrow
S_3^{(4)}
\longrightarrow
S_4^{(4)}.
\]

This is not a temporal process, but a stratification by the cardinality of the subset:

\[
|A|=1,2,3,4.
\]

In the DOT reading this can be understood as a deepening by one Hamming step:

- single distinctions;
- pairwise links;
- triple face closures;
- the full center.

---

# 4. The complement involution as the polarity of the tetrahedron

On \(Q_4\) the complement involution acts:

\[
\kappa_4(A)=J_4\setminus A.
\]

It sends the layers:

\[
\kappa_4:S_k^{(4)}\to S_{4-k}^{(4)}.
\]

That is:

\[
S_0\leftrightarrow S_4,
\qquad
S_1\leftrightarrow S_3,
\qquad
S_2\leftrightarrow S_2.
\]

Geometrically this is the polarity of the tetrahedron:

- a vertex passes to the opposite face;
- a face passes to the opposite vertex;
- an edge passes to the opposite edge;
- the empty pole passes to the full center.

For barycenters the formula holds:

\[
b(J_4\setminus A)
=
-\frac{|A|}{4-|A|}\,b(A),
\qquad
A\neq\varnothing,\ A\neq J_4.
\]

Hence:

for a vertex \(\{i\}\):

\[
b(J_4\setminus\{i\})=-\frac13 b(\{i\});
\]

for an edge \(\{i,j\}\):

\[
b(J_4\setminus\{i,j\})=-b(\{i,j\}).
\]

That is, on the middle layer \(S_2^{(4)}\) the complement becomes ordinary central opposition.

---

# 5. The octahedron as the layer of edge midpoints

The middle layer:

\[
S_2^{(4)}
=
\{\{1,2\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}\}.
\]

These are the six edge midpoints of the tetrahedron.

The complement gives three opposite pairs:

\[
\{1,2\}\leftrightarrow\{3,4\},
\]

\[
\{1,3\}\leftrightarrow\{2,4\},
\]

\[
\{1,4\}\leftrightarrow\{2,3\}.
\]

If one joins all pairs of edge midpoints except the opposite ones, one obtains the octahedron graph:

\[
(S_2^{(4)},R_2)\cong K_{2,2,2}.
\]

Equivalently:

\[
S_2^{(4)}
\cong
L(K_4),
\]

where \(L(K_4)\) is the graph of edges of the tetrahedron adjacent at a common vertex.

In the Hamming language on \(S_2^{(4)}\):

\[
A\,R_2\,B
\quad\Longleftrightarrow\quad
|A\triangle B|=2.
\]

And opposition:

\[
B=\kappa_4(A)
\quad\Longleftrightarrow\quad
|A\triangle B|=4.
\]

Thus the layer \(S_2^{(4)}\) is a self-dual octahedron inside rank \(4\).

---

# 6. The outer layer \(V_4\)

The outer layer of rank \(4\):

\[
V_4=S_1^{(4)}\sqcup S_3^{(4)}.
\]

It contains:

- the \(4\) vertices of the tetrahedron;
- the \(4\) centers of the opposite faces.

In total:

\[
|V_4|=8.
\]

The complement involution defines four axes:

\[
\{1\}\leftrightarrow\{2,3,4\},
\]

\[
\{2\}\leftrightarrow\{1,3,4\},
\]

\[
\{3\}\leftrightarrow\{1,2,4\},
\]

\[
\{4\}\leftrightarrow\{1,2,3\}.
\]

If one excludes these four opposite pairs and joins all remaining pairs, one obtains the graph:

\[
(V_4,\Omega_4)\cong K_{2,2,2,2}.
\]

This is the graph of the \(4\)-dimensional cross-polytope.

Important: in the three-dimensional geometric picture \(V_4\) looks like a pair of dual tetrahedra. Graph-theoretically it has the structure \(K_{2,2,2,2}\). Therefore the formula

\[
(V_4,\Omega_4)\cong K_{2,2,2,2}
\]

means a graph invariant, and not the assertion that this figure is a regular four-dimensional solid in \(\mathbb R^3\).

---

# 7. The inscribed sphere and the layer \(S_3^{(4)}\)

A sphere is inscribed in the regular tetrahedron. It touches the four faces at four points.

These points have DOT names:

\[
\{1,2,3\},
\quad
\{1,2,4\},
\quad
\{1,3,4\},
\quad
\{2,3,4\}.
\]

That is:

\[
\text{tangency points of the inscribed sphere}
\quad=\quad
S_3^{(4)}.
\]

The center of the sphere:

\[
b(J_4)
\]

has the DOT name:

\[
J_4=\{1,2,3,4\}=1111.
\]

Therefore the full spherical closure is read as:

\[
S_3^{(4)}\sqcup S_4^{(4)}
=
\text{four tangency points}+\text{center}.
\]

This explains the observation:

\[
\text{three inner hidden points and one manifest one}
\]

depends on the chosen projection. If one looks from the side of one face, the tangency point of that face may manifest as the center of the visible circle, while the three other tangency points recede to the lateral faces and become hidden. But strictly all four tangency points belong to one layer:

\[
S_3^{(4)}.
\]

The center of the sphere is not one of the tangency points. It belongs to the next layer:

\[
S_4^{(4)}.
\]

This distinction is important for the corpus:

\[
\text{face center}\neq \text{center of the tetrahedron}.
\]

---

# 8. Fano as a projection of the three-dimensional tetrahedral layer

The classical Fano scene at rank \(3\) is obtained as:

\[
Q_3^\*=\mathcal P(J_3)\setminus\{\varnothing\}.
\]

If \(J_3=\{1,2,3\}\), then:

\[
Q_3^\*
=
\{1,2,3,12,13,23,123\}.
\]

Here:

- \(1,2,3\) — the three single points;
- \(12,13,23\) — the three pair points;
- \(123\) — the central triple point.

The Fano lines are given by the rule:

\[
\{A,B,A\triangle B\}.
\]

In expanded form:

\[
\{1,2,12\},
\quad
\{1,3,13\},
\quad
\{2,3,23\},
\]

\[
\{1,23,123\},
\quad
\{2,13,123\},
\quad
\{3,12,123\},
\]

\[
\{12,13,23\}.
\]

This is the standard Fano reading:

\[
7=3+3+1.
\]

---

# 9. The lifted Fano projection inside \(Q_4\)

Now embed this into the tetrahedron \(J_4=\{1,2,3,4\}\).

Choose a base face:

\[
B=\{1,2,3\}.
\]

Then the inner Fano scene of this face:

\[
F_B^{\mathrm{int}}
=
\mathcal P(B)\setminus\{\varnothing\}
=
\{1,2,3,12,13,23,123\}.
\]

It lies in \(Q_4\) as a subcarrier:

\[
F_B^{\mathrm{int}}\subset Q_4^\*.
\]

But in the lifted geometric projection the central point \(123\) may be replaced by its polar image:

\[
\kappa_4(123)=4.
\]

That is, instead of the inner face center \(123\), the apex \(4\) appears in the picture.

Define the projection:

\[
\pi_4(A)=A
\quad\text{for}\quad
\varnothing\neq A\subsetneq B,
\]

\[
\pi_4(B)=J_4\setminus B=\{4\}.
\]

Then the lifted Fano scene:

\[
F_4^{\mathrm{lift}}
=
\pi_4(F_B^{\mathrm{int}})
=
\{1,2,3,12,13,23,4\}.
\]

This is exactly the structure:

\[
\text{three base vertices}
+\text{three points on the base edges}
+\text{apex}.
\]

The Fano combinatorics is preserved not as the literal operation \(\triangle\) inside \(Q_4\), but as a projection of the Fano lines through \(\pi_4\).

For example:

\[
\{1,23,123\}
\quad\mapsto\quad
\{1,23,4\}.
\]

This gives a line:

\[
\text{base vertex}
\longrightarrow
\text{apex}
\longrightarrow
\text{opposite point on a base edge}.
\]

This is exactly what is seen in the lifted Fano picture: the central Fano point is lifted to the apex through the rank-\(4\) complement.

---

# 10. Why this is not simply the flat Fano

The flat Fano:

\[
Q_3^\*=\{1,2,3,12,13,23,123\}.
\]

The lifted Fano:

\[
F_4^{\mathrm{lift}}=\{1,2,3,12,13,23,4\}.
\]

They are isomorphic as Fano carriers if \(4\) is read as the projective name of the point \(123\):

\[
4\sim 123
\quad\text{through}\quad
\kappa_4.
\]

But in the full \(Q_4\) these are different points:

\[
4\neq 123.
\]

Their difference is precisely the new content of rank \(4\):

\[
\text{face center}
\quad\longleftrightarrow\quad
\text{opposite vertex}.
\]

What at rank \(3\) was a single Fano point \(123\) splits at rank \(4\) into a pair:

\[
123\leftrightarrow4.
\]

This is an example of a rank rereading:

the old center becomes an inner point of a face, while the new rank adds its polar apex.

---

# 11. Four Fano projections in one tetrahedron

The tetrahedron has four faces. For each face one can construct such a Fano projection.

For \(i\in J_4\) set:

\[
B_i=J_4\setminus\{i\}.
\]

Then:

\[
F_{B_i}^{\mathrm{int}}
=
\mathcal P(B_i)\setminus\{\varnothing\}
\]

is the inner Fano scene of the face \(B_i\), and the lifted version:

\[
F_i^{\mathrm{lift}}
=
\left(\mathcal P(B_i)\setminus\{\varnothing,B_i\}\right)
\sqcup
\{\{i\}\}.
\]

There are four such lifted Fano projections in total:

\[
F_1^{\mathrm{lift}},
\quad
F_2^{\mathrm{lift}},
\quad
F_3^{\mathrm{lift}},
\quad
F_4^{\mathrm{lift}}.
\]

This corresponds to the four possible choices of the apex.

In this sense the phrase "rotate the Fano" has a rigorous meaning:

\[
\text{rotation}
=
\text{change of the chosen face and its opposite vertex}.
\]

Moreover, all four readings live inside one carrier:

\[
Q_4=\mathcal P(J_4).
\]

---

# 12. The three appearances of the octahedron

In the already constructed logico-operator bridge, three appearances of the octahedron were singled out:

\[
X_3,
\qquad
S_2^{(4)},
\qquad
\operatorname{Inv}_3\cap S_4^{(8)}.
\]

The present document refines the second appearance:

\[
S_2^{(4)}
\]

is not merely a six-point graph \(K_{2,2,2}\), but has a concrete tetrahedral meaning:

\[
S_2^{(4)}
=
\text{edge midpoints of the tetrahedron}.
\]

Thereby the octahedron \(X_3\) passes into rank \(4\) as an inner layer of the tetrahedron:

\[
X_3
\longrightarrow
S_2^{(4)}.
\]

This is not a literal equality of carriers, but the preservation of the graph and relational type:

\[
(X_3,R_1\cup R_2)
\cong
(S_2^{(4)},R_2).
\]

At rank \(3\) the octahedron is the entire active scene.

At rank \(4\) it becomes an inner middle layer.

This is precisely the phase transition:

\[
\text{full scene}
\quad\longrightarrow\quad
\text{inner layer of a higher rank}.
\]

---

# 13. Relation to the Fano document

The Fano document fixes the projective reading of rank \(3\):

\[
Q_3\setminus\{0\}
\quad\leadsto\quad
\mathrm{PG}(2,2).
\]

The present document adds the next layer:

\[
\mathrm{PG}(2,2)
\quad\leadsto\quad
\text{projection of the tetrahedral }Q_4.
\]

Otherwise:

\[
\text{Fano as }Q_3^\*
\]

is the inner projective reading.

\[
\text{Fano as a lifted tetrahedral figure}
\]

is the rank reading through the complement \(S_1\leftrightarrow S_3\) in \(Q_4\).

Therefore these documents do not duplicate each other:

- the Fano document answers the question: why does \(7\) arise at rank \(3\)?
- the present document answers the question: how does the Fano projection unfold at rank \(4\)?

---

# 14. Relation to the projective-radial-conic package

In the old line of notes this theme was fixed as:

\[
\text{projective-radial-conic package}.
\]

It consisted of five elements:

1. \(RP^1\) as the space of directions;
2. the pencil of lines through the center;
3. the conic as a boundary object / absolute;
4. the polarity with respect to the conic;
5. the Möbius transport as the law of traversal with a flip.

The present document refines where this package sits in the rank structure.

## 14.1. The conic as a continuous avatar of the boundary

In the Fano reading the boundary is given discretely:

\[
Q_3^\*
=
Q_3\setminus\{000\}.
\]

One pole is switched off, and the remaining \(7\) points receive a projective closure through XOR triples.

In the conic reading the boundary is given continuously: the conic acts as an absolute relative to which the polarity is defined. Therefore the correspondence is as follows:

\[
\text{Fano}
\quad\leftrightarrow\quad
\text{discrete incidence skeleton},
\]

\[
\text{conic}
\quad\leftrightarrow\quad
\text{continuous boundary carrier}.
\]

These two objects are not identified. They form a coupling:

\[
\text{discrete incidence}
+
\text{continuous boundary}.
\]

This is exactly why the lifted Fano picture must be read not as a literal realization of the Fano plane in Euclidean geometry, but as a coupled discrete-continuous mechanism.

## 14.2. Polarity and the layer \(S_1\leftrightarrow S_3\)

In projective geometry the conic defines a polarity:

\[
\text{point}\longleftrightarrow\text{line}.
\]

In the tetrahedral \(Q_4\) reading the same type of passage appears as the complement:

\[
\kappa_4:S_1^{(4)}\to S_3^{(4)}.
\]

That is:

\[
\text{vertex}
\longleftrightarrow
\text{opposite face}.
\]

In barycentric geometry this is written as:

\[
\{i\}
\longleftrightarrow
J_4\setminus\{i\}.
\]

Therefore the old motif

\[
\text{vertex}\leftrightarrow\text{edge/face}
\]

receives a rigorous rank form:

\[
S_1^{(4)}\leftrightarrow S_3^{(4)}.
\]

This is not an ordinary symmetry of a single type, but a type-changing duality: a point passes not into a point, but into the opposite face object.

## 14.3. The inscribed conic and the tangency points

In the old note two readings were distinguished:

- a conic tangent to the sides;
- a conic passing through the vertices.

In the new \(Q_4\) reading this receives a layer interpretation.

The tangential reading:

\[
\text{face tangency points}
\quad=\quad
S_3^{(4)}.
\]

The vertex reading:

\[
\text{vertices of the tetrahedron}
\quad=\quad
S_1^{(4)}.
\]

The complement connects them:

\[
S_1^{(4)}
\leftrightarrow
S_3^{(4)}.
\]

Therefore the old distinction

\[
\text{conic through the vertices}
\quad/\quad
\text{conic tangent to the sides}
\]

can be read as two polar modes of a single tetrahedral law.

## 14.4. The pencil through the center and the color axes

The old document singled out the pencil of lines through a common center as the radial framework.

In the \(Q_3\) color reading this pencil manifests through the three complement axes:

\[
R\leftrightarrow C,
\qquad
G\leftrightarrow M,
\qquad
B\leftrightarrow Y.
\]

In bit notation:

\[
100\leftrightarrow011,
\qquad
010\leftrightarrow101,
\qquad
001\leftrightarrow110.
\]

This is the layer:

\[
R_3\cong 3K_2.
\]

In the \(Q_4\) tetrahedral reading the analogue becomes the set of axes:

\[
\{i\}\leftrightarrow J_4\setminus\{i\}.
\]

That is, the radial pencil is not a separate addition to the Fano. It is a way of reading the polar axes arising from the complement.

## 14.5. The Möbius transport

The conic defines a static law of duality:

\[
\text{point}\leftrightarrow\text{line}.
\]

The Möbius transport defines a dynamic law of traversal:

\[
\text{traversal of a direction}
\quad\leadsto\quad
\text{return with a flip of side}.
\]

At rank \(3\) the dynamic image is seen on the cycle:

\[
R_1\cong C_6.
\]

The color reading:

\[
R\to Y\to G\to C\to B\to M\to R.
\]

This is not the Möbius band itself, but a discrete transport trace: during the traversal both the coordinate axis and the polarity of the reading change.

Therefore the old package splits into two sides:

\[
\text{conic/polarity}
\quad=\quad
\text{static law of duality},
\]

\[
\text{Möbius transport}
\quad=\quad
\text{dynamic law of traversal}.
\]

Both readings are needed. One explains why a vertex passes into the opposite face; the other explains how the traversal between polar roles occurs.

## 14.6. The resulting correspondence

The old projective-radial-conic package can now be rewritten through \(Q_4\):

| Old motif | New \(Q_4\) reading |
|---|---|
| Fano incidence | \(Q_3^\*\subset Q_4\) as a face projection |
| apex | opposite vertex \(\{i\}\) |
| inscribed conic | layer of tangency points \(S_3^{(4)}\) |
| pencil through the center | complement axes \(\{i\}\leftrightarrow J_4\setminus\{i\}\) |
| polarity | \(\kappa_4:S_1\leftrightarrow S_3\) |
| transport | cycle \(C_6\) on \(X_3\) |
| octahedral layer | \(S_2^{(4)}\), edge midpoints |

The main correction to the old version:

\[
\text{Fano + conic + apex}
\]

is not a single object. It is a package of projective readings of one deeper structure:

\[
Q_4=\mathcal P(J_4).
\]

---

# 15. The chamber-color projection: \(\operatorname{Cham}(O_3)\cong Q_3\)

Now the color bridge can be developed more precisely.

In the already existing color reading of rank \(3\) it is fixed that:

\[
X_3=Q_3\setminus\{000,111\}
=
\{R,G,B,C,M,Y\}.
\]

This is the six-point chromatic shell:

\[
RGB\sqcup CMY.
\]

Geometrically it sits on the vertices of the octahedron:

\[
O_3\cong K_{2,2,2}.
\]

But the octahedron has not only vertices. It has \(8\) triangular chambers, that is, faces. It is precisely these chambers that give the full cube:

\[
\operatorname{Cham}(O_3)\cong Q_3.
\]

## 15.1. The octahedron as three axes

Let the vertices of the octahedron be written as three pairs:

\[
\{b_1^0,b_1^1\},
\qquad
\{b_2^0,b_2^1\},
\qquad
\{b_3^0,b_3^1\}.
\]

Each chamber of the octahedron chooses one vertex from each axis:

\[
\{b_1^{\varepsilon_1},b_2^{\varepsilon_2},b_3^{\varepsilon_3}\},
\qquad
\varepsilon_i\in\{0,1\}.
\]

The number of such choices:

\[
2^3=8.
\]

Therefore the set of chambers has a canonical bit notation:

\[
\operatorname{Cham}(O_3)
=
\{000,001,010,011,100,101,110,111\}
\cong Q_3.
\]

This is the precise meaning of the formula:

\[
\operatorname{Cham}(O_3)\cong Q_3.
\]

## 15.2. The chamber centers as vertices of the dual cube

Take the standard octahedron:

\[
O_3=\operatorname{conv}(\pm e_1,\pm e_2,\pm e_3).
\]

Its face is given by a choice of signs:

\[
\sigma_1x_1+\sigma_2x_2+\sigma_3x_3=1,
\qquad
\sigma_i\in\{\pm1\}.
\]

The center of this face:

\[
c_\sigma=\frac13(\sigma_1e_1+\sigma_2e_2+\sigma_3e_3).
\]

Multiplying by \(3\), we obtain:

\[
3c_\sigma=(\sigma_1,\sigma_2,\sigma_3).
\]

This is a vertex of the cube:

\[
\{\pm1\}^3.
\]

After the usual passage from signs to bits:

\[
-1\leftrightarrow0,
\qquad
+1\leftrightarrow1,
\]

we obtain:

\[
\{\pm1\}^3\cong\{0,1\}^3=Q_3.
\]

So the face centers of the octahedron, which are also the points of tangency of the inscribed sphere with the faces, indeed give the vertices of the dual RGB cube.

Rigorously:

\[
\text{face centers of }O_3
\quad\leftrightarrow\quad
\text{vertices of }O_3^\vee,
\]

and the polytope dual to the octahedron is the cube:

\[
O_3^\vee=Q_3.
\]

This is exactly what is seen in the chamber picture.

## 15.3. Vertex color and chamber color

Now one must distinguish two color layers.

**Vertex color layer:**

\[
X_3
=
\{R,G,B,C,M,Y\}
\]

sits on the vertices of the octahedron.

**Chamber color layer:**

\[
\operatorname{Cham}(O_3)
\cong Q_3
\]

sits on the faces of the octahedron and gives the entire RGB cube:

\[
\{000,100,010,001,110,101,011,111\}.
\]

In color names:

\[
000=K\quad\text{black},
\]

\[
100=R,\quad010=G,\quad001=B,
\]

\[
110=Y,\quad101=M,\quad011=C,
\]

\[
111=W\quad\text{white}.
\]

That is, the sextet \(RGB\sqcup CMY\) appears twice, but in different statuses:

1. as the vertices of the octahedron \(X_3\);
2. as the six non-extreme chambers of the cubic layer \(\operatorname{Cham}(O_3)\), between \(000\) and \(111\).

The first layer is responsible for the axes and polarities.

The second layer is responsible for the chamber states and the full color cube.

## 15.4. The black and white chambers

The chamber

\[
000
\]

chooses the lower poles of all three axes:

\[
\{b_1^0,b_2^0,b_3^0\}.
\]

In the color projection this is the black pole \(K\).

The chambers adjacent to it differ in one bit:

\[
100,\quad010,\quad001.
\]

These are the three additive primary colors:

\[
R,G,B.
\]

The chamber

\[
111
\]

chooses the upper poles of all three axes:

\[
\{b_1^1,b_2^1,b_3^1\}.
\]

In the color projection this is the white pole \(W\).

The chambers adjacent to it:

\[
110,\quad101,\quad011.
\]

These are the three subtractive secondary colors:

\[
Y,M,C.
\]

Therefore the additive and subtractive readings arise as two polar neighborhoods of chambers:

\[
000\ \text{with the neighborhood }RGB,
\]

\[
111\ \text{with the neighborhood }CMY.
\]

This refines the previous formula:

\[
X_3=Q_3\setminus\{000,111\}.
\]

Now it is clear that \(X_3\) is not merely the removal of two poles. It is the removal of two extreme chambers of the full chamber cube, after which the sextet of active color chambers remains.

## 15.5. The remaining chambers and the color order

If one looks not only at the outer visible faces, but at all eight chambers, then the color cube is fully recovered.

The adjacency of chambers is given by a common edge of the octahedron. Two chambers are adjacent if and only if their bit names differ in one digit:

\[
d_H(\varepsilon,\eta)=1.
\]

Therefore the adjacency graph of the chambers:

\[
\Gamma(\operatorname{Cham}(O_3))
\]

is the cube:

\[
\Gamma(\operatorname{Cham}(O_3))\cong Q_3.
\]

This is stronger than just "the octahedron has eight faces." Here the full law of color adjacency is fixed.

The chamber layer gives:

\[
000
\leftrightarrow
RGB
\leftrightarrow
CMY
\leftrightarrow
111.
\]

And the vertex layer gives:

\[
RGB\sqcup CMY
\]

as the six polar vertices of the octahedron.

In other words:

\[
\text{vertices of the octahedron}
=
\text{color axes},
\]

\[
\text{chambers of the octahedron}
=
\text{color states}.
\]

## 15.6. Relation to the conic and the inscribed sphere

In the previous section the conic was read as a continuous boundary.

Now this is refined for the octahedron:

- the inscribed sphere touches each of the \(8\) faces of the octahedron;
- the tangency points coincide with the centers of these faces;
- these \(8\) tangency points are the vertices of the dual cube.

That is, the continuous object, the sphere, does not add arbitrary geometry. It realizes the same law of duality:

\[
\text{face of the octahedron}
\leftrightarrow
\text{vertex of the cube}.
\]

This is precisely why the tangency points of the spherical layer can be read as vertices of the RGB cube:

\[
\text{tangency points}
\quad\cong\quad
Q_3.
\]

This is the passage from the discrete to the continuous in this color projection:

a discrete chamber of the octahedron receives a continuous tangency point on the inscribed sphere, and this tangency point is a vertex of the dual cube.

## 15.7. Summary of the chamber law

The chamber law can be written as:

\[
\boxed{
\operatorname{Cham}(O_3)\cong Q_3
}
\]

where:

\[
O_3=K_{2,2,2}
\]

is the octahedral shell of \(X_3\), and

\[
Q_3
\]

is the full color cube.

Thereby the color structure has two conjugate readings:

\[
X_3
\quad=\quad
\text{vertex octahedron of colors},
\]

\[
\operatorname{Cham}(O_3)
\quad=\quad
\text{chamber cube of colors}.
\]

This explains why the RGB cube appears not from outside, but as the dual chamber reading of the octahedron itself.

---

# 16. What is rigorous and what is DOT reading

The rigorous part:

1. \(Q_4=\mathcal P(J_4)\).
2. The layer decomposition:

\[
Q_4=S_0\sqcup S_1\sqcup S_2\sqcup S_3\sqcup S_4.
\]

3. The barycentric map:

\[
b(A)=\frac1{|A|}\sum_{i\in A}v_i.
\]

4. \(S_1\) — the vertices of the tetrahedron.
5. \(S_2\) — the edge midpoints.
6. \(S_3\) — the face centers and the tangency points of the inscribed sphere.
7. \(S_4\) — the center of the tetrahedron.
8. \((S_2^{(4)},R_2)\cong K_{2,2,2}\).
9. \(V_4=S_1\sqcup S_3\) has four complement axes and graph type \(K_{2,2,2,2}\).
10. For any face \(B_i\) the subcarrier \(\mathcal P(B_i)\setminus\{\varnothing\}\) is isomorphic to the Fano carrier \(Q_3^\*\).
11. For the standard octahedron \(O_3=\operatorname{conv}(\pm e_1,\pm e_2,\pm e_3)\) the set of chambers has a natural bit notation:

\[
\operatorname{Cham}(O_3)\cong Q_3.
\]

12. The face centers of \(O_3\), which are also the tangency points of the inscribed sphere with the faces, after rescaling are the vertices of the dual cube.
13. The adjacency graph of the chambers of the octahedron is isomorphic to the cube \(Q_3\).

The DOT reading:

1. \(S_1\to S_2\to S_3\to S_4\) is read as a deepening of distinction.
2. \(S_2^{(4)}\) is read as the rank-\(3\) octahedron immersed into rank \(4\).
3. The lifted Fano is obtained by replacing the face center \(B_i\) with the opposite apex \(\{i\}\) through \(\kappa_4\).
4. The inscribed sphere reads the layer \(S_3\) as the hidden layer of tangencies.
5. The center \(S_4\) is not an active vertex of \(X_4\), but the point of full closure.
6. The color \(X_3=RGB\sqcup CMY\) is read as the vertex octahedron of colors.
7. The full RGB cube \(Q_3\) is read as the chamber layer of the octahedron:

\[
Q_3\cong\operatorname{Cham}(O_3).
\]

Hypotheses for the next investigation:

1. A double Fano scene with a common apex point.
2. A possible \(13\)-point closure.
3. A connection with \(STS(13)\) or with the projective plane of order \(3\).

These three items are not proved here.

---

# 17. The boundary with \(STS(13)\) and \(PG(2,3)\)

It is important not to confuse three objects:

\[
\text{Fano}=PG(2,2)=STS(7),
\]

\[
PG(2,3),
\]

\[
STS(13).
\]

For \(PG(2,3)\):

- \(13\) points;
- \(13\) lines;
- each line contains \(4\) points.

For \(STS(13)\):

- \(13\) points;
- \(26\) triples;
- each pair of points lies in exactly one triple.

A double Fano glued along one point gives:

\[
7+7-1=13
\]

points, but inherits only:

\[
7+7=14
\]

Fano triples.

Here an important numerical resonance arises:

\[
13\cdot 2=26,
\]

and simultaneously

\[
2(7+7)-2=28-2=26.
\]

That is, the number of triples of the full \(STS(13)\) indeed coincides with the number obtained from doubling two Fano sets with subtraction of two central excesses. This cannot be ignored: it shows the possible form of the next closure.

But a simple gluing of two Fanos along a common point is not yet \(STS(13)\). The reason is not only the number of triples, but the covering of pairs.

In the full \(STS(13)\) one needs:

\[
\frac{13\cdot12}{6}=26
\]

triples.

If one takes two Fano planes \(F^+\) and \(F^-\), glued along one point \(o\), then their \(14\) inherited triples cover all pairs inside \(F^+\) and all pairs inside \(F^-\). What remains uncovered are exactly the transverse pairs between the six non-central points of the first Fano and the six non-central points of the second:

\[
6\cdot6=36
\]

transverse pairs.

To complete to \(STS(13)\), one must add \(12\) triples, because:

\[
12\cdot3=36.
\]

But each new triple must cover only the not-yet-covered pairs. This is impossible to do with a triple on the two parts \(6+6\): any triple contains either two points from one part or two points from the other part, and such an inner pair is already covered by one of the Fano planes.

Consequently, the ordinary bi-Fano gluing does not complete to \(STS(13)\) while preserving both Fanos as full subsystems.

The correct conclusion:

1. the simple gluing \(F^+\cup_o F^-\) has \(13\) points and \(14\) Fano triples;
2. the full \(STS(13)\) has \(13\) points and \(26\) triples;
3. the numerical formula

\[
2(7+7)-2=26
\]

points not to a simple gluing, but to a possible operator of doubling/rewiring of triples;
4. if such a construction exists in the DOT reading, it must replace part of the Fano triples or generate new triples not as an addition to two ready Fanos, but as a new \(13\)-point closure.

Therefore a double Fano scene must not automatically be called \(STS(13)\). The correct status of the simple gluing:

\[
\text{partial triple system on 13 points}
\]

or

\[
\text{bi-Fano scene with a common point}.
\]

The further question:

\[
\text{can one derive from the bi-Fano motif a rewiring operator yielding }STS(13)?
\]

This is a separate problem.

---

# 18. A higher-rank hypothesis: Fano, bi-Fano, and \(STS(13)\)

A suspicion to keep for the next investigation:

\[
\text{Fano}
\quad\longrightarrow\quad
\text{bi-Fano}
\quad\longrightarrow\quad
STS(13)
\]

may be not a flat construction within one rank, but a shadow of a higher rank.

Here it is important not to confuse two scales. This is not about the passage to the operator carrier \(Q_{2^3}=Q_8\), but about the passages of the ordinary binary tower:

\[
2^3
\quad\longrightarrow\quad
2^4
\quad\longrightarrow\quad
2^5.
\]

Otherwise:

\[
Q_3^\*
\quad\leadsto\quad
Q_4
\quad\leadsto\quad
Q_5.
\]

The Fano has \(7=2^3-1\) points. The next full tetrahedral level has \(16=2^4\) positions. The next, five-dimensional binary level after it, has \(32=2^5\) positions.

The first rigorous lift of the Fano has the form:

\[
Q_4^\*=\mathcal P(J_4)\setminus\{\varnothing\}.
\]

Its size:

\[
|Q_4^\*|=15.
\]

On \(Q_4^\*\) there are natural XOR triples:

\[
\{A,B,A\triangle B\},
\qquad
A,B\neq\varnothing,\quad A\neq B.
\]

They form a projective space:

\[
PG(3,2),
\]

and as a triple system this is:

\[
STS(15).
\]

The number of triples:

\[
\frac{15\cdot14}{6}=35.
\]

Therefore the rigorous rank lift of the Fano gives not \(STS(13)\), but \(STS(15)\):

\[
STS(7)
\quad\leadsto\quad
STS(15).
\]

This agrees well with the binary growth:

\[
2^3-1=7,
\qquad
2^4-1=15.
\]

But it is precisely here that one sees why \(Q_4^\*\) is not yet the natural place for the bi-Fano with one common point. In \(PG(3,2)\) two distinct Fano planes intersect in a projective line, that is, in three points, and not in one.

Therefore the bi-Fano of the form

\[
7+7-1=13
\]

is naturally sought at the next level:

\[
Q_5^\*=\mathcal P(J_5)\setminus\{\varnothing\}.
\]

Its size:

\[
|Q_5^\*|=31.
\]

The XOR triples on \(Q_5^\*\):

\[
\{A,B,A\triangle B\}
\]

form:

\[
PG(4,2),
\]

and as a triple system:

\[
STS(31).
\]

The number of triples:

\[
\frac{31\cdot30}{6}=155.
\]

In \(PG(4,2)\) the Fano planes correspond to the three-dimensional linear subspaces of \(\mathbb F_2^5\). Their number:

\[
\binom{5}{3}_2
=155.
\]

And now two Fano planes can intersect in exactly one projective point. Then their union has:

\[
7+7-1=13
\]

points.

This gives a more precise scheme:

\[
Q_3^\*
\quad\longrightarrow\quad
Q_4^\*
\quad\longrightarrow\quad
Q_5^\*
\]

or in terms of objects:

\[
Fano
\quad\longrightarrow\quad
PG(3,2)
\quad\longrightarrow\quad
PG(4,2).
\]

At the level of \(Q_5^\*\) the bi-Fano with a common point already arises naturally as a subconfiguration.

Then \(13\) occupies an intermediate position within rank \(5\), and not within the full projective reading of rank \(4\). It cannot be obtained as a full projective carrier, but it can be obtained as the union of two Fano planes with a one-point intersection:

\[
31
\quad\supset\quad
13.
\]

Moreover, such a \(13\)-point bi-Fano carrier is still not \(STS(13)\) if one preserves both Fano planes as full subsystems. The reason is the same: the full \(STS(13)\) cannot contain a Fano subsystem on \(7\) points, because for an external point at least \(7\) external points would be required, and outside the Fano there are only \(6\).

Consequently, at rank \(5\) the correct carrier of the bi-Fano appears:

\[
\text{two Fano planes in }PG(4,2)\text{ with a common point}.
\]

And \(STS(13)\), if it arises from this motif, must arise not as an inheritance of XOR triples from \(PG(4,2)\), but as a new rewiring of triples on the same \(13\)-point carrier.

The resulting hypothesis:

\[
\text{bi-Fano}_{13}
\subset
PG(4,2)
\quad\leadsto\quad
STS(13)
\]

not as a substructure, but as a change of the closure law on the same number of points.

So, if \(STS(13)\) indeed arises from the Fano motif a rank higher, then the scheme must be as follows:

\[
Q_3^\*
\quad\longrightarrow\quad
Q_4
\quad\longrightarrow\quad
Q_5^\*
\quad\longrightarrow\quad
\text{bi-Fano motif on }13
\quad\longrightarrow\quad
\text{rewiring of triples}
\quad\longrightarrow\quad
STS(13).
\]

In this scheme the bi-Fano is not a final system. It is a generating template that fixes:

- the common center;
- the two seven-element Fano projections;
- the \(13=7+7-1\) points;
- the numerical resonance \(13\cdot2=26\).

And \(STS(13)\) appears only after a new operation that does not add Fano to Fano, but changes the very law of triples.

Such a status agrees well with DOT:

\[
\text{first the carrier},
\quad
\text{then the double projective reading},
\quad
\text{then a new type of closure of relations}.
\]

Open problem:

\[
\text{find the explicit operator rewiring the bi-Fano motif into }STS(13).
\]

---

# 19. Corpus formulation

For the corpus the following compressed formulation can be used.

**Candidate theorem.**  
Let \(J_4\) be a four-element set. The nonempty subsets \(Q_4^\*=\mathcal P(J_4)\setminus\{\varnothing\}\) have a natural barycentric reading on a regular tetrahedron: \(S_1^{(4)}\) is the set of vertices, \(S_2^{(4)}\) is the set of edge midpoints, \(S_3^{(4)}\) is the set of face centers and tangency points of the inscribed sphere, \(S_4^{(4)}\) is the center of the tetrahedron.

The complement involution \(\kappa_4(A)=J_4\setminus A\) realizes the tetrahedral polarity:

\[
S_1^{(4)}\leftrightarrow S_3^{(4)},
\qquad
S_2^{(4)}\leftrightarrow S_2^{(4)},
\qquad
S_0^{(4)}\leftrightarrow S_4^{(4)}.
\]

The middle layer \(S_2^{(4)}\) with the relation \(|A\triangle B|=2\) is isomorphic to the octahedral graph:

\[
(S_2^{(4)},R_2)\cong K_{2,2,2}.
\]

For each face \(B_i=J_4\setminus\{i\}\) the carrier \(\mathcal P(B_i)\setminus\{\varnothing\}\) is the Fano carrier \(Q_3^\*\). The lifted Fano projection is obtained by replacing the central point \(B_i\) with the opposite apex \(\{i\}\) through the complement \(\kappa_4\). Therefore the Fano can be read as a projective shadow of the tetrahedral rank \(4\), and the rank-\(3\) octahedron as the middle layer \(S_2^{(4)}\) of the same tetrahedral structure.

---

# 20. Summary

The main structure of the document:

\[
Q_4=\mathcal P(J_4)
\]

has the tetrahedral barycentric reading:

\[
S_1
\to
S_2
\to
S_3
\to
S_4.
\]

In this reading:

\[
S_1=\text{vertices of the tetrahedron},
\]

\[
S_2=\text{edge midpoints}=\text{octahedron},
\]

\[
S_3=\text{face centers}=\text{tangency points of the inscribed sphere},
\]

\[
S_4=\text{center}.
\]

The complement involution:

\[
\kappa_4:S_k\to S_{4-k}
\]

becomes a geometric polarity:

\[
\text{vertex}\leftrightarrow\text{opposite face},
\qquad
\text{edge}\leftrightarrow\text{opposite edge}.
\]

The Fano arises as a \(Q_3^\*\)-subcarrier on each face, and the lifted Fano is obtained when the face center is replaced by the opposite apex through \(\kappa_4\).

Therefore the picture

\[
\text{tetrahedron}
\longrightarrow
\text{octahedron of edge midpoints}
\longrightarrow
\text{dual tetrahedron of tangency points}
\longrightarrow
\text{center}
\]

is not decorative geometry, but the precise geometrization of the Boolean lattice of rank \(4\).
