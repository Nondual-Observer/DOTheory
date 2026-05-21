# DOT: Distinction Observable Theory

# Volume 3. Boundary Operators and Scene Reductions

Volumes 0-2 built the active carriers, the first complete scene, higher
rank shells, complementarity, and the projective factor

\[
U_n/\kappa\cong PG(n-2,2).
\]

They also give the inter-rank axial law

\[
Q_{n-1}^*\cong U_n/\kappa_n.
\]

Volume 3 adds the internal boundary grammar. Up to this point the
relations \(R_d\) compared positions inside one carrier, and \(\kappa\)
paired a position with its limiting complement. This volume introduces
operators that move between adjacent layers:

\[
\boxed{
\partial,\qquad \delta.
}
\]

The central formula is

\[
\boxed{
\kappa\partial=\delta\kappa.
}
\]

It says that limiting complementarity sends boundary to coboundary.

The mathematical content is the standard simplicial chain and cochain
grammar over \(\mathbb F_2\). The DOT-specific content is the connection
between this grammar, active scenes, holding conditions, reductions,
inter-rank lifting, and the observer as a boundary invariant.

---

# How to Read This Volume

This volume answers the question:

\[
\text{how does boundary act inside an active carrier?}
\]

Reading order:

1. three meanings of boundary;
2. the full boundary carrier \(Q_J\);
3. boundary and coboundary incidence;
4. chain operators \(\partial,\delta\);
5. the laws \(\partial^2=0,\delta^2=0\);
6. compatibility with complementarity;
7. examples in ranks \(3,4,5\);
8. reductions \(\rho_D,\rho_F,\rho_C\) as scene boundaries;
9. observer as common boundary invariant.

---

# Basic Notation

Let \(J\) be a finite set.

\[
Q_J=\mathcal P(J)
\]

is the full Boolean carrier.

\[
U_J=\mathcal P(J)\setminus\{\varnothing,J\}
\]

is the active carrier.

For \(A\subseteq J\),

\[
\kappa(A)=J\setminus A.
\]

The boundary of a nonempty subset is

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

The coboundary is

\[
\delta(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

All chain sums are read over \(\mathbb F_2\) unless another coefficient
system is explicitly stated.

---

# 1. What Volume 3 Adds

Volume 1 gave horizontal relations on \(U_3\):

\[
R_1,\ R_2,\ R_3.
\]

Volume 2 gave shells:

\[
S_k^{(n)}.
\]

Volume 3 adds vertical movement between shells:

\[
S_k^{(n)}\longrightarrow S_{k-1}^{(n)},
\]

and

\[
S_k^{(n)}\longrightarrow S_{k+1}^{(n)}.
\]

This movement is encoded by the boundary and coboundary operators.

---

# 2. Three Meanings of Boundary

## 2.1. Topological Boundary

In the simplicial reading,

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

Here the active carrier is the face carrier of the boundary of a simplex.

## 2.2. Boundary Incidence

If

\[
B\subset A,\qquad |B|=|A|-1,
\]

then \(B\) is an immediate face of \(A\).

This is boundary incidence.

## 2.3. Chain Boundary Operator

The chain operator sends a face to the sum of its immediate faces:

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

It satisfies

\[
\partial^2=0.
\]

## 2.4. Scene Boundary

A scene also has boundary directions as a scene. These are reductions:

\[
\rho_D,\qquad \rho_F,\qquad \rho_C.
\]

They do not act like \(\partial\) on a single face. They describe
transitions from one scene configuration to another.

---

# 3. Full Boundary Carrier and Active Scene

The full carrier is

\[
Q_J=\mathcal P(J).
\]

It contains:

\[
\varnothing,\qquad J,
\]

as two limits.

The active scene is

\[
U_J=\mathcal P(J)\setminus\{\varnothing,J\}.
\]

The boundary operator is most naturally defined on the full face carrier,
because faces can have boundaries that touch the lower limit:

\[
\partial(\{a\})=\varnothing.
\]

The active carrier is obtained after the two limits are set apart from
the active grammar.

---

# 4. Boundary and Coboundary Incidence

Boundary incidence:

\[
B\prec A
\]

means

\[
B\subset A,\qquad |B|=|A|-1.
\]

Coboundary incidence:

\[
A\prec C
\]

means

\[
A\subset C,\qquad |C|=|A|+1.
\]

Boundary moves downward in shell degree:

\[
S_k\to S_{k-1}.
\]

Coboundary moves upward:

\[
S_k\to S_{k+1}.
\]

---

# 5. Boundary Operator \(\partial\)

For \(A\subseteq J\),

\[
\boxed{
\partial(A)=\sum_{a\in A}(A\setminus\{a\}).
}
\]

Examples:

\[
\partial(\{a,b\})=\{a\}+\{b\},
\]

\[
\partial(\{a,b,c\})=\{a,b\}+\{a,c\}+\{b,c\}.
\]

The operator decreases size by one:

\[
\partial:S_k\to S_{k-1}.
\]

---

# 6. Law \(\partial^2=0\)

Every codimension-two face appears twice in the double boundary.

Over \(\mathbb F_2\), twice means zero. Therefore

\[
\boxed{
\partial^2=0.
}
\]

This is the standard chain-complex law.

In DOT, it means that the boundary grammar does not continue indefinitely
as a new edge of the edge. The edge of an edge cancels.

---

# 7. Coboundary Operator \(\delta\)

For \(A\subseteq J\),

\[
\boxed{
\delta(A)=\sum_{b\notin A}(A\cup\{b\}).
}
\]

Examples:

\[
\delta(\{a\})=\sum_{b\in J\setminus\{a\}}\{a,b\}.
\]

The operator increases size by one:

\[
\delta:S_k\to S_{k+1}.
\]

It also satisfies

\[
\boxed{
\delta^2=0.
}
\]

The proof is dual to the proof for \(\partial\).

---

# 8. Compatibility of \(\kappa,\partial,\delta\)

Complementarity reverses inclusion:

\[
B\subset A
\quad\Longleftrightarrow\quad
\kappa(A)\subset\kappa(B).
\]

Therefore boundary becomes coboundary under complementarity:

\[
\boxed{
\kappa\partial=\delta\kappa.
}
\]

Equivalently,

\[
\partial\kappa=\kappa\delta.
\]

This is the main operator law of Volume 3.

---

# 9. Two Grammars: Return and Vanishing Boundary

The polar grammar is governed by

\[
\kappa^2=\operatorname{id}.
\]

Applying complementarity twice returns to the same face.

The boundary grammar is governed by

\[
\partial^2=0.
\]

Applying boundary twice gives zero.

Thus DOT uses two different algebraic laws:

\[
\text{return: }\kappa^2=\operatorname{id},
\]

\[
\text{edge cancellation: }\partial^2=0.
\]

Their compatibility is

\[
\kappa\partial=\delta\kappa.
\]

---

# 10. Rank \(3\) Example

At rank \(3\),

\[
U_3=S_1^{(3)}\sqcup S_2^{(3)}.
\]

Boundary sends two-element faces to one-element faces:

\[
\partial:S_2^{(3)}\to S_1^{(3)}.
\]

For example:

\[
\partial(\{1,2\})=\{1\}+\{2\}.
\]

Coboundary sends one-element faces to two-element faces:

\[
\delta:S_1^{(3)}\to S_2^{(3)}.
\]

For example:

\[
\delta(\{1\})=\{1,2\}+\{1,3\}.
\]

Complementarity sends vertex to opposite edge:

\[
\{1\}\leftrightarrow \{2,3\}.
\]

The law

\[
\kappa\partial=\delta\kappa
\]

holds on this vertex-edge carrier.

---

# 11. Rank \(4\) Example

At rank \(4\),

\[
U_4=S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}.
\]

The boundary chain is

\[
S_3^{(4)}\xrightarrow{\partial}S_2^{(4)}
\xrightarrow{\partial}S_1^{(4)}.
\]

In the tetrahedral reading:

- \(S_1^{(4)}\) are vertices;
- \(S_2^{(4)}\) are edges;
- \(S_3^{(4)}\) are faces.

Complementarity pairs:

\[
S_1^{(4)}\leftrightarrow S_3^{(4)},
\]

and preserves the middle layer by size:

\[
S_2^{(4)}\leftrightarrow S_2^{(4)}.
\]

This is where vertex-face polarity and opposite-edge polarity coexist.

---

# 12. Rank \(5\) Example

At rank \(5\),

\[
U_5=S_1^{(5)}\sqcup S_2^{(5)}\sqcup S_3^{(5)}\sqcup S_4^{(5)}.
\]

The boundary chain is

\[
S_4\to S_3\to S_2\to S_1.
\]

Complementarity pairs:

\[
S_1^{(5)}\leftrightarrow S_4^{(5)},
\]

\[
S_2^{(5)}\leftrightarrow S_3^{(5)}.
\]

Thus rank \(5\) has two paired shell levels rather than one
self-dual middle shell.

---

# 13. Functoriality Under Relabeling

Let

\[
\sigma:J\to J'
\]

be a bijection. It induces a map on faces:

\[
A\mapsto\sigma(A).
\]

Boundary commutes with relabeling:

\[
\partial(\sigma A)=\sigma(\partial A).
\]

The same holds for \(\delta\) and \(\kappa\).

Thus the boundary grammar depends only on the finite incidence structure,
not on names of vertices.

---

# 14. Scene with Boundary Grammar

A scene with boundary grammar has the form

\[
S=(U,\mathcal A_S,\operatorname{Inv}(S)),
\]

where \(\mathcal A_S\) includes:

- horizontal relations \(R_d\);
- complementarity \(\kappa\);
- boundary \(\partial\);
- coboundary \(\delta\);
- cyclic transport \(T\), when a cycle is fixed.

The boundary grammar adds vertical transitions between shells to the
horizontal relation grammar.

---

# 15. Holding Conditions and Boundary Carriers

The first complete scene \(U_3\) gives the first complete carriers of the
three holding conditions:

\[
\mathcal H_D\rightsquigarrow R_3=3K_2,
\]

\[
\mathcal H_F\rightsquigarrow R_2=K_3\sqcup K_3,
\]

\[
\mathcal H_C\rightsquigarrow R_1=C_6.
\]

The boundary operator adds another view: holding requires recoverable
trace across the layers of the scene.

Thus \(\mathcal H_F\) is best read as recoverability of trace, not as the
claim that \(\partial\) vanishes or does not vanish.

---

# 16. Reductions as Scene Boundaries

Reductions are boundary directions of the scene as a scene:

\[
\rho_D,\qquad \rho_F,\qquad \rho_C.
\]

The operator \(\partial\) acts inside an already held scene. Reductions
describe transitions out of the current scene configuration.

## 16.1. Reduction \(\rho_D\)

\(\rho_D\) collapses polar distinction:

\[
x\sim\kappa x.
\]

In a rich scene this appears as the quotient

\[
U_n/\kappa.
\]

In the inter-rank reading, this axial quotient is the nonempty carrier of
the previous rank:

\[
U_n/\kappa_n\cong Q_{n-1}^*.
\]

Thus \(\rho_D\) has two coordinated meanings: it sends positions to
complement axes, and it returns the current scene to the axial grammar of
the previous rank. On \(U_3\), this gives three axes:

\[
U_3/\kappa_3\cong Q_2^*=\{01,10,11\}.
\]

## 16.2. Reduction \(\rho_F\)

\(\rho_F\) is loss of recoverable trace.

The boundary operator itself remains a formal operation. What fails is
the reading:

\[
q\circ\partial
\]

ceases to determine a recoverable trace.

On \(U_3\), this touches the chamber distinction between \(S_1^{(3)}\)
and \(S_2^{(3)}\).

## 16.3. Reduction \(\rho_C\)

\(\rho_C\) opens cyclic closure.

For a cycle,

\[
T^m=\operatorname{id}
\]

is the internal closure law. Reduction \(\rho_C\) breaks this autonomy and
requires an external continuation, apex, orientation, or carrier.

---

# 17. Reductions on Rank \(3\)

## 17.1. \(\rho_D\) on \(U_3\)

The quotient by complementarity is

\[
U_3/\kappa=\{D,F,C\}.
\]

This is the three-axis factor:

\[
PG(1,2).
\]

## 17.2. \(\rho_F\) on \(U_3\)

The chamber pair is

\[
S_1^{(3)}\sqcup S_2^{(3)}.
\]

A coarse trace-forgetting collapse reads this as a two-state chamber
factor. A finer trace weakening keeps the six vertices but loses recovery
of the shell transition.

The strict distinction is:

- quotient of carriers;
- loss of recoverability of a reading.

These should not be conflated.

## 17.3. \(\rho_C\) on \(U_3\)

The cycle

\[
C_6
\]

has internal closure through

\[
T^6=\operatorname{id}.
\]

Opening this cycle gives a path or requires an external point of
completion.

This is the first finite form of externalization of cyclic closure.

---

# 18. Reductions on Rank \(4\)

## 18.1. \(\rho_D\): Axial Factor

At rank \(4\),

\[
U_4/\kappa\cong PG(2,2).
\]

Thus polar reduction produces the Fano plane:

\[
U_4/\kappa_4\cong Q_3^*.
\]

## 18.2. \(\rho_F\): Boundary Chain

The boundary chain is

\[
S_3^{(4)}\to S_2^{(4)}\to S_1^{(4)}.
\]

Trace recovery now has a genuine three-layer carrier.

## 18.3. \(\rho_C\): Rank-4 Cycles

Rank \(4\) has several cycle avatars rather than a single canonical
six-cycle. Cyclic reduction therefore becomes an atlas-level question:
which cycle is selected, and which closure is being held.

---

# 19. Reductions on Rank \(5\)

## 19.1. \(\rho_D\): \(PG(3,2)\)

At rank \(5\),

\[
U_5/\kappa\cong PG(3,2).
\]

The axial quotient becomes a projective three-space.

## 19.2. \(\rho_F\): Central Boundary Bundle

Rank \(5\) has paired middle shells:

\[
S_2^{(5)}\leftrightarrow S_3^{(5)}.
\]

The boundary grammar links

\[
S_3^{(5)}\to S_2^{(5)}
\]

and

\[
S_2^{(5)}\to S_1^{(5)}.
\]

The trace structure becomes a bundle of middle-layer incidences.

## 19.3. \(\rho_C\): Active and Projective Cycles

Rank \(5\) separates:

- active boundary carrier \(U_5\), with \(30\) states;
- nonzero projective carrier \(Q_5^*\), with \(31\) states.

The \(C_{31}\) Singer cycle belongs to the second carrier. The active
boundary and the projective cycle are related but not identical.

---

# 20. Rank Principle in Boundary Form

The boundary form of rank growth is:

\[
\boxed{
\text{higher rank internalizes boundary directions of lower rank.}
}
\]

What appears as a collapse or reduction at a lower rank can become a
structured carrier at a higher rank.

Examples:

- the three axes of \(U_3/\kappa\) match \(Q_2^*\);
- \(Q_3^*\) becomes the Fano factor \(U_4/\kappa_4\);
- the octahedral six-state form becomes the middle layer \(S_2^{(4)}\);
- the boundary chain becomes longer and more articulated in ranks \(4\)
  and \(5\).

The same statement is written compactly as:

\[
Q_{n-1}^*\cong U_n/\kappa_n.
\]

---

# 21. Observer as Boundary Invariant

The observer of a scene is the common invariant of its grammars:

\[
O_S\in\operatorname{Inv}(S).
\]

For a scene with horizontal, polar, boundary, and cyclic grammars, one can
write schematically:

\[
O_S=\bigcap_{A\in\mathcal A_S}\operatorname{Inv}(A).
\]

On the first complete scene this includes:

\[
R_1,\ R_2,\ R_3,\ \kappa,\ \partial,\ \delta,\ T
\]

where the relevant structures are defined.

The observer is therefore not an additional vertex of the carrier. It is
the invariant side of the scene's grammar.

---

# 22. What Volume 3 Establishes

Volume 3 establishes:

- the boundary operator \(\partial\);
- the coboundary operator \(\delta\);
- the laws \(\partial^2=0,\delta^2=0\);
- the compatibility \(\kappa\partial=\delta\kappa\);
- rank examples \(3,4,5\);
- reductions as scene-boundary directions;
- the inter-rank reading of \(\rho_D\):
  \[
  \rho_D:U_n\to U_n/\kappa_n\cong Q_{n-1}^*;
  \]
- the boundary-invariant reading of the observer.

---

# Appendix A. Main Theorem of Volume 3

For every finite \(J\), with \(Q_J=\mathcal P(J)\), complementarity
\(\kappa(A)=J\setminus A\), boundary \(\partial\), and coboundary
\(\delta\), one has:

\[
\boxed{
\partial^2=0,\qquad \delta^2=0,\qquad
\kappa\partial=\delta\kappa.
}
\]

These laws are natural under relabeling of \(J\).

---

# Appendix B. Operator Table

\[
\begin{array}{c|c|c}
\text{operator} & \text{direction} & \text{law}\\
\hline
\kappa & S_k\leftrightarrow S_{n-k} & \kappa^2=\operatorname{id}\\
\partial & S_k\to S_{k-1} & \partial^2=0\\
\delta & S_k\to S_{k+1} & \delta^2=0\\
T & \text{cycle step} & T^m=\operatorname{id}
\end{array}
\]

Compatibility:

\[
\kappa\partial=\delta\kappa.
\]

---

# Summary of Volume 3

Boundary in DOT has several levels. The active carrier itself is a
boundary carrier:

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

Inside it, the chain boundary and coboundary are:

\[
\partial,\qquad \delta.
\]

They satisfy:

\[
\partial^2=0,\qquad \delta^2=0.
\]

Complementarity turns boundary into coboundary:

\[
\kappa\partial=\delta\kappa.
\]

Reductions

\[
\rho_D,\rho_F,\rho_C
\]

are boundary directions of the scene as a scene. This gives the boundary
form of the rank principle: higher ranks internalize reductions of lower
ranks.

For \(\rho_D\), the rank-to-rank form is:

\[
\rho_D:U_n\to U_n/\kappa_n\cong Q_{n-1}^*.
\]
