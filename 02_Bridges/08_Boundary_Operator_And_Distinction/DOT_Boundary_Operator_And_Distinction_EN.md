# DOT: the boundary operator, polarity, and distinction as the singling-out of an edge

Status: research bridge draft.

This document introduces a new layer of relations for the DOT corpus. Until now the main work was conducted with relations between already given positions of a single carrier:

\[
R_d(A,B)\iff |A\triangle B|=d,
\]

and with the complement involution:

\[
\kappa(A)=J\setminus A.
\]

Now another type of structure is added:

\[
\partial.
\]

It describes not the difference of one position from another, but the passage from an object to its boundary.

The main formula:

\[
\kappa^2=\operatorname{id},
\qquad
\partial^2=0.
\]

These are two different grammars:

- \(\kappa^2=\operatorname{id}\) — the polar grammar of return;
- \(\partial^2=0\) — the boundary grammar of the disappearance of the edge of an edge.

It is precisely this pair that links the old line `ID|NOT`, the seam, Möbius, the conic as boundary, and the new formalization of distinction as the singling-out of an edge.

---

# 1. Motif: distinction as the singling-out of a boundary

In the early notes the phrase was already fixed:

> DOT begins not with an entity, but with the boundary of an admissible position of distinction.

This is important to strengthen.

Distinction can be understood in two ways.

The first way is positional:

\[
x\neq y.
\]

Then points and a relation between them are needed.

The second way is by boundary:

\[
\text{to distinguish an object}
\quad=\quad
\text{to single out its edge}.
\]

Then not only a graph of points is needed, but also an operator that sends an object to its boundary:

\[
\partial(\text{object})=\text{boundary of the object}.
\]

This does not replace \(R_d\) and \(\kappa\). It adds a vertical dimension to them.

---

# 2. The three levels of the word "boundary"

One must immediately separate three different meanings.

## 2.1. The topological boundary

In topology the boundary of a region \(A\) is written as:

\[
\operatorname{bd}(A)
\quad\text{or}\quad
\partial A.
\]

It separates \(A\) from the external complement:

\[
A
\quad/\quad
X\setminus A.
\]

Such a boundary is conveniently read as a seam: it simultaneously separates and links the two sides.

## 2.2. Boundary incidence

In finite combinatorics one can say:

\[
B\subset A,\qquad |B|=|A|-1.
\]

Then \(B\) is a face of \(A\), or the immediate boundary of \(A\).

This is a relation between layers:

\[
S_k\to S_{k-1}.
\]

But this is not yet the operator \(\partial\) with the law \(\partial^2=0\). This is only an incidence relation.

## 2.3. The chain boundary operator

To obtain the law

\[
\partial^2=0,
\]

one must pass to formal sums of faces, that is, to chains.

Over \(\mathbb F_2\) the boundary of a simplex \(A\) is defined as:

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

Here the sum is taken modulo \(2\).

Then each second-order face appears twice, and therefore disappears:

\[
\partial^2(A)=0.
\]

This is the key technical caution:

\[
\text{the relation "to be a face" is not nilpotent},
\]

but

\[
\text{the chain boundary operator is nilpotent}.
\]

---

# 3. The power-set carrier and the layers

Let \(J\) be a finite set of cardinality \(n\).

The power-set carrier:

\[
Q_J=\mathcal P(J).
\]

The layers:

\[
S_k(J)=\{A\subseteq J: |A|=k\}.
\]

The decomposition:

\[
Q_J=\bigsqcup_{k=0}^n S_k(J).
\]

In coordinate notation:

\[
Q_J\cong Q_n=\{0,1\}^n.
\]

This is the same carrier already used in the logico-operator, Fano-tetrahedral, and color bridges.

## 3.1. Why the full \(Q_J\) is needed here

In the ordinary active scene of DOT the punctured carrier is often used:

\[
X_J=\mathcal P(J)\setminus\{\varnothing,J\}.
\]

But the boundary grammar naturally lives on the full carrier \(Q_J\).

The reason is simple:

\[
\partial(\{a\})=\varnothing,
\]

while

\[
\delta(J\setminus\{a\})=J.
\]

That is, the lower and upper poles are needed as the terminal edges of the boundary ladder. If one removes them in advance, the operators \(\partial\) and \(\delta\) cease to be closed on the carrier.

Therefore for the new block one must distinguish two modes:

\[
Q_J
\quad
\text{the full boundary carrier},
\]

\[
X_J
\quad
\text{the punctured active scene}.
\]

The puncture remains important for the scene of distinction, but the boundary operator shows that the removed poles do not vanish without a trace. They remain as the limits of the ladder:

\[
S_0
\leftrightarrow
S_1
\leftrightarrow
\cdots
\leftrightarrow
S_n.
\]

This gives a useful refinement for the corpus:

\[
\text{active scene}
\neq
\text{full boundary shell}.
\]

The active scene works after the puncture. The boundary shell explains where this puncture gets its lower and upper limits from.

---

# 4. Horizontal relations: \(R_d\)

The Hamming relations:

\[
R_d(A,B)\iff |A\triangle B|=d.
\]

They compare two positions as elements of one common carrier.

If \(A,B\in S_k\), then \(d\) is always even:

\[
|A\triangle B|=2(k-|A\cap B|).
\]

For example, on the middle layer \(S_2^{(4)}\):

\[
R_2
\]

gives the octahedral graph:

\[
(S_2^{(4)},R_2)\cong K_{2,2,2}.
\]

That is, \(R_d\) is the horizontal language of distinction:

\[
\text{position}\leftrightarrow\text{position}.
\]

---

# 5. The polar involution: \(\kappa\)

The complement involution:

\[
\kappa(A)=J\setminus A.
\]

It sends the layers:

\[
\kappa:S_k\to S_{n-k}.
\]

And satisfies:

\[
\kappa^2=\operatorname{id}.
\]

This is the rigorous form of `NOT*NOT = ID`.

In bit notation:

\[
\kappa(x)=x\oplus 1^n.
\]

In the geometric reading of rank \(4\):

\[
S_1^{(4)}\leftrightarrow S_3^{(4)}
\]

becomes a polarity:

\[
\text{vertex}\leftrightarrow\text{opposite face}.
\]

On the middle layer:

\[
S_2^{(4)}\leftrightarrow S_2^{(4)}
\]

becomes the opposition of edges of the tetrahedron.

---

# 6. The boundary relation

Now we introduce the new layer.

For \(A\in S_k(J)\) the immediate faces:

\[
\operatorname{bd}_1(A)=
\{A\setminus\{a\}:a\in A\}.
\]

The boundary relation:

\[
B_k^-(A,B)
\iff
B=A\setminus\{a\}
\quad\text{for some }a\in A.
\]

Here:

\[
A\in S_k,
\qquad
B\in S_{k-1}.
\]

That is:

\[
B_k^-\subseteq S_k\times S_{k-1}.
\]

This is not a symmetric relation and not an ordinary distance. It is directed downward through the layers.

Similarity to \(R_1\):

\[
|A\triangle B|=1.
\]

But the single condition \(d_H(A,B)=1\) is not sufficient. A direction is also needed:

\[
B\subset A.
\]

Therefore the boundary relation is the directed and typed part of \(R_1\).

---

# 7. The coboundary relation

The dual relation goes upward:

\[
\operatorname{cobd}_1(A)=
\{A\cup\{b\}:b\in J\setminus A\}.
\]

The coboundary relation:

\[
B_k^+(A,C)
\iff
C=A\cup\{b\}
\quad\text{for some }b\notin A.
\]

Here:

\[
A\in S_k,
\qquad
C\in S_{k+1}.
\]

That is:

\[
B_k^+\subseteq S_k\times S_{k+1}.
\]

The boundary and coboundary relations together give a vertical ladder:

\[
S_0
\leftrightarrow
S_1
\leftrightarrow
S_2
\leftrightarrow
\cdots
\leftrightarrow
S_n.
\]

This is a new structure relative to the previous focus on \(R_d\) and \(\kappa\).

---

# 8. The chain groups and the operator \(\partial\)

To obtain the law \(\partial^2=0\), we introduce the chain spaces over \(\mathbb F_2\):

\[
C_k(J)=\mathbb F_2[S_k(J)].
\]

This is the vector space whose basis is the elements of the layer \(S_k\).

The boundary operator:

\[
\partial_k:C_k(J)\to C_{k-1}(J),
\]

\[
\partial_k(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

Then:

\[
\partial_{k-1}\partial_k=0.
\]

Proof:

let \(A\in S_k\). After two applications of the boundary one obtains the sum of all subsets of the form:

\[
A\setminus\{a,b\},
\qquad
a\neq b.
\]

Each such subset appears twice:

1. first remove \(a\), then \(b\);
2. first remove \(b\), then \(a\).

Over \(\mathbb F_2\):

\[
1+1=0.
\]

Therefore:

\[
\partial^2(A)=0.
\]

This is the rigorous source of the formula:

\[
\partial^2=0.
\]

---

# 9. The coboundary operator \(\delta\)

Analogously we define the upward operator:

\[
\delta_k:C_k(J)\to C_{k+1}(J),
\]

\[
\delta_k(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

Then:

\[
\delta_{k+1}\delta_k=0.
\]

The reason is the same: each addition of two new elements can occur in two orders.

Over \(\mathbb F_2\) these two orders cancel each other:

\[
1+1=0.
\]

Thus a second vertical nilpotency appears:

\[
\delta^2=0.
\]

---

# 10. Compatibility of \(\kappa\), \(\partial\), and \(\delta\)

The complement sends the boundary to the coboundary.

If:

\[
B=A\setminus\{a\},
\]

then:

\[
\kappa(B)=J\setminus(A\setminus\{a\})
=(J\setminus A)\cup\{a\}.
\]

That is:

\[
\kappa(B)
\]

is a coface of \(\kappa(A)\).

In operator form:

\[
\kappa_{k-1}\partial_k
=
\delta_{n-k}\kappa_k.
\]

Or briefly:

\[
\kappa\partial=\delta\kappa.
\]

Dually:

\[
\kappa\delta=\partial\kappa.
\]

This is a very important formula for DOT.

It says:

\[
\text{polarity sends the singling-out of a boundary to the singling-out of a coboundary}.
\]

Otherwise:

\[
\text{to pass to the opposite pole}
\]

means to change the direction of the boundary ladder.

## 10.1. Functorial canonicity

This structure does not depend on the names of the elements of \(J\).

Let:

\[
f:J\to J'
\]

be a bijection of finite sets. Then it induces a map:

\[
Q_f:\mathcal P(J)\to\mathcal P(J'),
\qquad
Q_f(A)=f[A].
\]

It preserves the layers:

\[
Q_f(S_k(J))=S_k(J'),
\]

and the Hamming relations:

\[
A\,R_d\,B
\quad\Longleftrightarrow\quad
Q_f(A)\,R_d\,Q_f(B).
\]

It also commutes with the complement:

\[
Q_f\kappa_J=\kappa_{J'}Q_f.
\]

And with the boundary operator:

\[
Q_f\partial_J=\partial_{J'}Q_f.
\]

Indeed:

\[
Q_f\partial(A)
=
\sum_{a\in A}f[A\setminus\{a\}]
=
\sum_{a\in A}(f[A]\setminus\{f(a)\})
=
\partial(f[A]).
\]

Analogously:

\[
Q_f\delta_J=\delta_{J'}Q_f.
\]

Consequently, the construction:

\[
J\mapsto
(Q_J,\{R_d\},\kappa,\partial,\delta)
\]

is canonical with respect to renamings of the carrier. In the rigorous language this is a functor from the groupoid of finite sets and bijections to the category of boundary DOT scenes.

Important: for arbitrary embeddings \(J\hookrightarrow J'\) the compatibility with \(\kappa\) and \(\delta\) is no longer automatic, because the external complement changes. Therefore at this stage the correct rigorous status is functoriality under bijections. The relative version for embeddings must be built separately.

---

# 11. Two grammars: \(\kappa^2=\operatorname{id}\) and \(\partial^2=0\)

Now one can rigorously compare:

\[
\kappa^2=\operatorname{id},
\qquad
\partial^2=0.
\]

## 11.1. The polar grammar

\[
\kappa^2=\operatorname{id}.
\]

Meaning:

double negation returns the original position.

In logical language:

\[
\operatorname{NOT}\operatorname{NOT}=\operatorname{ID}.
\]

In DOT:

\[
\text{the opposite of the opposite}
=
\text{the original}.
\]

This is the grammar of reversibility.

## 11.2. The boundary grammar

\[
\partial^2=0.
\]

Meaning:

the boundary of the boundary disappears.

This is neither a return nor a negation. This is the law of the trace:

\[
\text{object}
\to
\text{boundary}
\to
\text{zero second edge}.
\]

This is the grammar of completion.

## 11.3. The distinction

\[
\kappa
\]

preserves the amount of structural content, but changes the pole.

\[
\partial
\]

lowers the dimension and sends an object to its edge.

Therefore:

\[
\kappa
\quad\text{is responsible for polarity},
\]

\[
\partial
\quad\text{is responsible for boundariness}.
\]

Together they give a new form of the scene of distinction:

\[
S=(Q_J,\{R_d\},\kappa,\partial,\delta).
\]

---

# 12. Example of rank \(3\)

Let:

\[
J_3=\{1,2,3\}.
\]

Then:

\[
Q_3=\mathcal P(J_3).
\]

The upper point:

\[
123.
\]

Its boundary:

\[
\partial(123)=12+13+23.
\]

Further:

\[
\partial(12)=1+2,
\]

\[
\partial(13)=1+3,
\]

\[
\partial(23)=2+3.
\]

Therefore:

\[
\partial^2(123)
=(1+2)+(1+3)+(2+3).
\]

Each vertex appears twice:

\[
1+1=0,\quad 2+2=0,\quad 3+3=0.
\]

And:

\[
\partial^2(123)=0.
\]

In this reading:

\[
123
\to
\{12,13,23\}
\to
\{1,2,3\}
\to
0.
\]

This is a boundary ladder, distinct from the Fano lines.

A Fano line is given by:

\[
\{A,B,A\triangle B\}.
\]

The boundary is given by:

\[
A\mapsto \{A\setminus\{a\}:a\in A\}.
\]

Both mechanisms live on \(Q_3\), but these are different laws.

---

# 13. Example of rank \(4\)

Let:

\[
J_4=\{1,2,3,4\}.
\]

The full point:

\[
1234.
\]

The boundary:

\[
\partial(1234)=123+124+134+234.
\]

These are the four faces of the tetrahedron.

Further:

\[
\partial(123)=12+13+23,
\]

and analogously for the other three faces.

The entire ladder:

\[
S_4
\xrightarrow{\partial}
S_3
\xrightarrow{\partial}
S_2
\xrightarrow{\partial}
S_1
\xrightarrow{\partial}
S_0.
\]

Geometrically:

\[
\text{tetrahedron}
\to
\text{faces}
\to
\text{edges}
\to
\text{vertices}
\to
\text{empty base}.
\]

And the complement acts simultaneously:

\[
S_0\leftrightarrow S_4,
\qquad
S_1\leftrightarrow S_3,
\qquad
S_2\leftrightarrow S_2.
\]

The result is a two-dimensional grammar:

\[
\partial:\ S_k\to S_{k-1},
\]

\[
\kappa:\ S_k\to S_{n-k}.
\]

This is exactly the structure that was missing in the previous reading of the tetrahedral rank \(4\).

---

# 14. Relation to the octahedron

The middle layer of rank \(4\):

\[
S_2^{(4)}
\]

consists of the \(6\) edges of the tetrahedron.

As the adjacency graph of edges:

\[
(S_2^{(4)},R_2)\cong K_{2,2,2}.
\]

That is, the octahedron appears as the middle layer.

Now the boundary reading is added:

\[
\partial(S_3^{(4)})\subset S_2^{(4)}.
\]

Each face of the tetrahedron has three edges. So each point of \(S_3\) defines a triangular chamber in \(S_2\).

Thus a new relation arises:

\[
\text{face of the tetrahedron}
\to
\text{triangular chamber of the octahedral layer}.
\]

This explains the connection between:

- the tetrahedron;
- the octahedron of edge midpoints;
- the chambers of the octahedron;
- the color cube.

The boundary \(S_3\to S_2\) shows which three edges form one face.

And the chamber reading of the octahedron shows how the choice of one vertex from each axis gives a point of \(Q_3\).

---

# 15. The discrete and the continuous

Now one can carefully formulate the passage between the discrete and the continuous.

The discrete layer:

\[
Q_J,\quad S_k,\quad R_d,\quad \kappa,\quad \partial.
\]

It is finite and combinatorial.

The continuous reading appears through the geometric realization:

\[
|Q_J|
\]

as a simplicial complex.

For example:

- \(S_0\) — the empty base;
- \(S_1\) — vertices;
- \(S_2\) — edges;
- \(S_3\) — triangular faces;
- \(S_4\) — the tetrahedral chamber.

The combinatorial boundary \(\partial\) becomes the algebraic trace of the geometric boundary.

That is:

\[
\text{the continuous}
\]

is not introduced as an external substance. It appears as the geometric realization of the discrete boundary grammar.

In this sense the conic and the sphere are not new foundations, but continuous carriers of the already given boundary law.

---

# 16. The conic, the sphere, and the tangency points

In the Fano-tetrahedral document it is already fixed that:

\[
S_3^{(4)}
\]

is read as the face centers of the tetrahedron and as the tangency points of the inscribed sphere with the faces.

This is the continuous reading of the boundary layer:

\[
S_3^{(4)}
=
\text{tangency points of the boundaries}.
\]

In the octahedron:

- there are \(8\) chambers;
- the inscribed sphere touches each chamber;
- the tangency points are the vertices of the dual cube.

That is:

\[
\operatorname{Cham}(O_3)\cong Q_3.
\]

Here the boundary works as the place of translation:

\[
\text{discrete chamber}
\to
\text{tangency point}
\to
\text{vertex of the dual cube}.
\]

This is not a random mixing of the discrete and the continuous, but a typical scheme:

\[
\text{discrete incidence}
+
\text{continuous boundary}
+
\text{dual carrier}.
\]

---

# 17. The Möbius transport

The Möbius layer is responsible not for the boundary itself, but for the transport along it.

Locally there are two sides:

\[
+,\quad -.
\]

Globally, upon traversal, a flip may occur:

\[
+\mapsto -.
\]

At rank \(3\) the discrete trace of this is seen on the cycle:

\[
R_1\cong C_6.
\]

The color reading:

\[
R\to Y\to G\to C\to B\to M\to R.
\]

If one places a local polar pair on this cycle, one can obtain the Möbius law of monodromy:

\[
\text{after a full traversal the polarity changes}.
\]

Thus three things are separated:

1. \(\partial\) — singles out the boundary;
2. \(\kappa\) — flips the pole;
3. the Möbius transport — carries the polarity along a closed traversal.

---

# 18. New relations for the corpus

The following relations and operators can be added to the rigorous part.

## 18.1. The boundary relation

\[
B_k^-(A,B)
\iff
B=A\setminus\{a\}
\quad(a\in A).
\]

Type:

\[
B_k^-\subseteq S_k\times S_{k-1}.
\]

## 18.2. The coboundary relation

\[
B_k^+(A,C)
\iff
C=A\cup\{b\}
\quad(b\notin A).
\]

Type:

\[
B_k^+\subseteq S_k\times S_{k+1}.
\]

## 18.3. The chain boundary operator

\[
\partial_k(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

Law:

\[
\partial_{k-1}\partial_k=0.
\]

## 18.4. The chain coboundary operator

\[
\delta_k(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

Law:

\[
\delta_{k+1}\delta_k=0.
\]

## 18.5. Compatibility with the complement

\[
\kappa\partial=\delta\kappa,
\]

\[
\kappa\delta=\partial\kappa.
\]

This is a new rigorous block for the corpus.

## 18.6. Functoriality under renamings

For each bijection \(f:J\to J'\) the induced map:

\[
Q_f(A)=f[A]
\]

preserves:

\[
R_d,\quad \kappa,\quad \partial,\quad \delta.
\]

That is, the boundary DOT scene does not depend on the concrete names of the coordinates, but is determined only by the cardinality of the carrier and the structure of the power-set lattice.

---

# 19. The scene of distinction with a boundary

The previous working form of the scene:

\[
S=(X,\Theta).
\]

For the power-set carrier:

\[
S_J=(Q_J,\{R_d\},\kappa).
\]

Now one can strengthen it:

\[
S_J^\partial
=
(Q_J,\{R_d\},\kappa,\partial,\delta).
\]

Here:

- \(R_d\) — horizontal distinction;
- \(\kappa\) — polar distinction;
- \(\partial\) — boundary distinction;
- \(\delta\) — coboundary unfolding.

Then distinction acquires three modes:

\[
\text{to distinguish}
\quad
\text{to oppose}
\quad
\text{to single out a boundary}.
\]

This is an important extension of DOT.

---

# 20. The observer as an invariant of the boundary

If the observer is read as an invariant of the scene:

\[
O_S\notin X,
\qquad
O_S\in\operatorname{Inv}(S),
\]

then after adding \(\partial\) one must refine:

\[
O_S\in
\operatorname{Inv}(Q_J,\{R_d\},\kappa,\partial,\delta).
\]

That is, the observer must preserve not only:

- the Hamming relations;
- polarity;
- the layers;

but also:

- the boundary ladder;
- the nilpotency \(\partial^2=0\);
- the compatibility \(\kappa\partial=\delta\kappa\).

This gives a stronger formalization of the observer:

\[
\text{observer}
=
\text{an invariant not only of positions, but also of the law of singling-out an edge}.
\]

---

# 21. Theorem form

**Candidate theorem.**  
Let \(J\) be a finite set of cardinality \(n\), \(Q_J=\mathcal P(J)\), \(S_k(J)=\{A\subseteq J:|A|=k\}\). On the chain spaces

\[
C_k(J)=\mathbb F_2[S_k(J)]
\]

define:

\[
\partial_k(A)=\sum_{a\in A}(A\setminus\{a\}),
\]

\[
\delta_k(A)=\sum_{b\notin A}(A\cup\{b\}),
\]

\[
\kappa_k(A)=J\setminus A.
\]

Then:

\[
\partial_{k-1}\partial_k=0,
\]

\[
\delta_{k+1}\delta_k=0,
\]

\[
\kappa_{k-1}\partial_k
=
\delta_{n-k}\kappa_k,
\]

\[
\kappa_{k+1}\delta_k
=
\partial_{n-k}\kappa_k.
\]

Consequently, the power-set carrier \(Q_J\) carries not only the Hamming and polar structure, but also a canonical boundary-coboundary structure.

In the DOT reading this means that distinction can be formalized not only as a relation between positions, but also as the operation of singling out a boundary.

---

# 22. Open questions

1. How to include \(\partial\) in the main definition of the scene of distinction: as an operator, as a relation, or as additional structure?
2. Is it necessary to distinguish the topological boundary and the chain boundary in the corpus by separate names?
3. How to connect \(\partial^2=0\) with the prohibition of coincidence \(\mathcal Z_D\): is nilpotency a boundary form of the prohibition of collapse?
4. How does \(\partial\) interact with the Fano triples \(\{A,B,A\triangle B\}\)?
5. Can one obtain the Möbius transport as the joint structure \((C_6,\kappa,\partial)\), and not only as a topological image?
6. How to write the color chamber projection through \(\partial(S_3)\to S_2\) and the dual cube of chambers?
7. Does \(Q_4\) have a universal property as the first carrier where \(\kappa\), \(\partial\), the tetrahedron, the octahedron, and the chamber cube are simultaneously visible?

---

# 23. Summary

The new material gives DOT one more fundamental layer.

Before:

\[
R_d
\quad
\text{and}
\quad
\kappa
\]

described distinction through distance and polarity.

Now:

\[
\partial
\]

describes distinction through the singling-out of a boundary.

The resulting triple:

\[
R_d:
\text{difference},
\]

\[
\kappa:
\text{opposition},
\]

\[
\partial:
\text{boundary}.
\]

Together they give a more complete formula for the scene:

\[
S_J^\partial
=
(Q_J,\{R_d\},\kappa,\partial,\delta).
\]

The main new thought:

\[
\operatorname{NOT}^2=\operatorname{id}
\]

and

\[
\partial^2=0
\]

do not compete. These are two different forms of the holding of distinction:

- the first returns the pole;
- the second completes the edge.

It is precisely between them that the language of the seam, the boundary, the conic, spherical tangency, and the Möbius transport arises.
