# Distinction Observable Theory

# Volume 0. Foundations

> Neti, neti — not this, not this.
>
> — Yājñavalkya, *Bṛhadāraṇyaka Upaniṣad*

This volume is the entry point into DOT. It introduces the basic language:
distinction, scene, observer, polar pair, active boundary, first complete
scene, axes, metacube reading, and the first view of higher ranks.

The aim of the volume is to show how familiar mathematical objects appear
from one structural question: how can a distinction be held as a scene?

The strict core of DOT is finite. Every construction in the core is given
on a finite carrier with explicitly stated relations and operators. The
interpretive layer is kept separate from the finite checks: graphs,
cycles, boundaries, projective factors, and topological avatars are
introduced only after the carrier and the relevant relation have been
fixed.

## How to Read This Volume

The volume should be read in order.

The first section introduces the minimal conceptual layer: distinction,
scene, holding, reduction, and observer. The second section constructs the
rank carriers and explains the active boundary. The third section builds
the first complete scene \(U_3\). The fourth section explains axes,
invariants, the metacube reading, and the readings of rank \(3\). The
final section gives a map of higher ranks and of the later volumes.

The terminology is introduced at the point where it is needed. Standard
mathematical constructions are used in their usual meaning; DOT adds a
particular reading and a particular order of assembly.

## Notation

The main finite carriers are:

\[
Q_n=\mathbb F_2^n,
\qquad
U_n=Q_n\setminus\{0^n,1^n\}.
\]

The set \(Q_n\) is the full binary carrier of rank \(n\). The set \(U_n\)
is the active carrier obtained after setting apart the two limiting
states.

The weight layer is

\[
S_k^{(n)}=\{x\in Q_n: |x|=k\}.
\]

The complement involution is

\[
\kappa(x)=x+1^n.
\]

For subsets \(A\subseteq J_n\), the same involution is written as

\[
\kappa(A)=J_n\setminus A.
\]

The Hamming-distance relation is

\[
R_d(A,B)\quad\Longleftrightarrow\quad |A\triangle B|=d.
\]

The boundary and coboundary operators are

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}),
\qquad
\delta(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

They satisfy

\[
\partial^2=0,\qquad \delta^2=0,
\qquad
\kappa\partial=\delta\kappa.
\]

The first complete scene is

\[
S_3=(U_3;R_1,R_2,R_3).
\]

On this scene:

\[
R_1\cong C_6,\qquad
R_2\cong K_3\sqcup K_3,\qquad
R_3\cong 3K_2.
\]

The octahedral skeleton is

\[
(U_3,R_1\cup R_2)\cong K_{2,2,2}.
\]

# Part I. Foundation of Scene

# §1. What DOT Studies

DOT studies held distinction.

A distinction in DOT is a structurally held non-coincidence of positions.
It requires positions, a separation between them, relations that hold this
separation, and a trace by which the distinction can be read or recovered.

The theory begins from the conditions under which distinction can be held,
presented, and recovered. The objects of the theory arise later, as stable
forms inside held scenes of distinction.

The observer is introduced in the same spirit. The observer is not a
subject placed before the scene. The observer is the invariant side of a
scene: that by which different readings still refer to the same scene.

In familiar scientific language, the observer is close to a frame of
reference, a standard, or an invariant. A frame gives a mode of
description. A standard fixes the sense of measurement. An invariant is
preserved under admissible changes of description. DOT uses the word
observer for this structural role.

The basic question of the theory is therefore:

\[
\text{what finite structures can hold a distinction as observable?}
\]

# §2. Minimal Scene: The Polar Pair

The minimal scene of distinction is a polar pair:

\[
P=\{a,-a\}.
\]

The pair has an exchange:

\[
\tau(a)=-a,\qquad \tau(-a)=a.
\]

The law of the exchange is

\[
\tau^2=\operatorname{id}.
\]

This is the minimal involution. It is the first operator of distinction:
one side is sent to its opposite, and applying the operation twice returns
the starting side.

With coordinates

\[
a\mapsto 0,\qquad -a\mapsto 1,
\]

the pair is identified with

\[
P\cong\mathbb F_2=\{0,1\},
\qquad
\tau(x)=x+1.
\]

In the logical reading, \(\tau\) is NOT. In the arithmetic reading, it is
addition of \(1\) modulo \(2\). In the geometric reading, it is the
half-turn of a one-dimensional polar projection.

The polar pair already contains distinction, exchange, and return. It is
the minimal finite scene.

# §3. Scene, Holding, Reduction, and Observer

A scene in DOT is written as

\[
S=(X,\mathcal A_S,\operatorname{Inv}(S)).
\]

Here:

- \(X\) is the carrier of positions;
- \(\mathcal A_S\) is the grammar of the scene: relations, acts, and
  operators fixed on the carrier;
- \(\operatorname{Inv}(S)\) is the invariant structure by which the scene
  is read as the same scene.

For the polar pair:

\[
X=P,\qquad \mathcal A_S=\{\tau\}.
\]

The invariant content is the fact that the two positions form one polar
pair and that the exchange is involutive.

## Holding

A scene is held when its distinctions remain nontrivial, readable, and
internally closed. DOT separates three holding conditions.

The first condition holds distinction against collapse into identity.
The second condition holds the trace of distinction against
unrecoverability. The third condition holds the closure of the scene
against dependence on an external completion.

These conditions will later receive their first complete carriers on
rank \(3\).

## Reductions

A reduction is a boundary direction of a scene. It is a way in which the
scene can pass into another configuration when one of its holding
conditions is not maintained.

There are three basic reductions:

- reduction of difference into identity;
- reduction of trace into unrecoverability;
- reduction of internal closure into external dependence.

In the older language these appeared as prohibitions. In the present
formulation they are treated as boundary directions of the scene.

## Observer

The observer of a scene is the invariant structure common to the grammar
of the scene.

In the working formula:

\[
O_S\in \operatorname{Inv}(S).
\]

For richer scenes this becomes an intersection of invariants of several
acts or operators:

\[
O_S=\bigcap_{A\in\mathcal A_S}\operatorname{Inv}(A).
\]

This formula is not a psychological definition. It is a structural one:
the observer is the stable invariant by which a scene remains readable as
the same scene.

# Part II. From Polar Pair to Active Boundary

# §4. Product of Polar Pairs

Several binary distinctions are held together by taking products of polar
pairs.

The full rank-\(n\) carrier is

\[
Q_n=P^n\cong \mathbb F_2^n.
\]

An element of \(Q_n\) is a binary word of length \(n\). Each coordinate is
one polar distinction. The full word records their joint state.

Rank \(1\):

\[
Q_1=\{0,1\}.
\]

Rank \(2\):

\[
Q_2=\{00,01,10,11\}.
\]

Rank \(3\):

\[
Q_3=\{000,001,010,011,100,101,110,111\}.
\]

The rank transition is the addition of a new binary coordinate:

\[
\Lambda_n(\varepsilon,x)=\varepsilon|x.
\]

Thus each old state receives two new positions in the next rank.

# §5. The Two Limits of the Full Carrier

The full carrier \(Q_n\) contains two limiting states:

\[
0^n,\qquad 1^n.
\]

The lower limit \(0^n\) is the state in which no coordinate is active. The
upper limit \(1^n\) is the state in which all coordinates are active.

The active carrier is obtained by setting these two limits apart:

\[
U_n=Q_n\setminus\{0^n,1^n\}.
\]

For rank \(1\):

\[
U_1=\varnothing.
\]

The full carrier \(Q_1\) is the polar pair itself; both of its points are
limits.

For rank \(2\):

\[
U_2=\{01,10\}.
\]

The active part is again a pair.

For rank \(3\):

\[
U_3=Q_3\setminus\{000,111\}.
\]

This gives six active states. Rank \(3\) is the first rank where the
active carrier can support three different forms of holding at once.

# §6. Boolean and Simplicial Reading

The binary carrier has an equivalent subset reading.

Let

\[
J_n=\{1,\ldots,n\}.
\]

A binary word in \(Q_n\) is identified with a subset of \(J_n\): the
positions of the ones.

Thus

\[
Q_n\cong\mathcal P(J_n).
\]

The lower limit is \(\varnothing\). The upper limit is \(J_n\). The active
carrier is

\[
U_n=\mathcal P(J_n)\setminus\{\varnothing,J_n\}.
\]

This is the set of all nonempty proper faces of the simplex
\(\Delta^{n-1}\). Therefore

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

The active carrier is the combinatorial carrier of the boundary of a
simplex.

Its barycentric subdivision has the usual geometric realization

\[
|\operatorname{sd}(\partial\Delta^{n-1})|\cong S^{n-2}.
\]

This gives the discrete-continuous bridge: the same finite carrier has a
Boolean reading and a simplicial boundary reading.

# §7. Limiting Complementarity

The complement involution is

\[
\kappa(A)=J_n\setminus A.
\]

It exchanges a face with its opposite complementary face. In binary
coordinates:

\[
\kappa(x)=x+1^n.
\]

The law is

\[
\kappa^2=\operatorname{id}.
\]

The involution preserves \(U_n\), because the complement of a nonempty
proper subset is again a nonempty proper subset.

Complementarity gives the first system of axes:

\[
H_A=\{A,J_n\setminus A\}.
\]

At rank \(3\), these axes are the three opposite pairs of the octahedral
scene.

# §8. Horizontal Relations

On \(U_n\), DOT uses Hamming-distance relations:

\[
R_d(A,B)\quad\Longleftrightarrow\quad |A\triangle B|=d.
\]

These are standard finite relations. DOT uses them as horizontal
grammars of distinction on the active carrier.

At rank \(3\), the three possible nonzero distances between active states
are \(1,2,3\). They become the three relation layers of the first complete
scene.

# Part III. The First Complete Scene \(U_3\)

# §9. The Carrier \(U_3\) and Its Layers

The active carrier of rank \(3\) is

\[
U_3=\{001,010,100,011,101,110\}.
\]

In subset notation:

\[
U_3=\mathcal P(\{1,2,3\})\setminus\{\varnothing,\{1,2,3\}\}.
\]

It has two weight layers:

\[
S_1^{(3)}=\{001,010,100\},
\]

\[
S_2^{(3)}=\{011,101,110\}.
\]

Complementarity exchanges these two layers:

\[
\kappa(S_1^{(3)})=S_2^{(3)}.
\]

This is the first rank where the active carrier is large enough to carry
opposite pairs, triads, and a cycle on the same six positions.

# §10. The Three Relations \(R_1,R_2,R_3\)

On \(U_3\), Hamming distance gives three relation layers.

## The relation \(R_1\)

The relation \(R_1\) connects states at distance \(1\). On \(U_3\) it is
a six-cycle:

\[
(U_3,R_1)\cong C_6.
\]

One possible traversal is

\[
100\to110\to010\to011\to001\to101\to100.
\]

## The relation \(R_2\)

The relation \(R_2\) connects states at distance \(2\). It splits into
two triangular components:

\[
(U_3,R_2)\cong K_3\sqcup K_3.
\]

These components are the two weight layers:

\[
S_1^{(3)},\qquad S_2^{(3)}.
\]

## The relation \(R_3\)

The relation \(R_3\) connects complementary states:

\[
(U_3,R_3)\cong 3K_2.
\]

The three pairs are

\[
\{001,110\},\qquad
\{010,101\},\qquad
\{100,011\}.
\]

The relation \(R_3\) is the polar layer of the full scene.

Together the three relations partition all unordered pairs of the
six-state carrier:

\[
|R_1|=6,\qquad |R_2|=6,\qquad |R_3|=3,
\]

\[
6+6+3=\binom62.
\]

# §11. Octahedral Skeleton and Full Scene

The octahedral skeleton is obtained from the first two relation layers:

\[
(U_3,R_1\cup R_2)\cong K_{2,2,2}.
\]

The third layer \(R_3\) consists of the three opposite pairs of the
octahedron. It is not a surface edge of the octahedral skeleton; it is the
polar layer of the complete scene.

Thus the full rank-3 scene is

\[
S_3=(U_3;R_1,R_2,R_3).
\]

The skeleton, chambers, cycle, and opposite pairs are different readings
of one finite carrier.

# §12. Holding Conditions on \(U_3\)

On the first complete scene, the three holding conditions receive their
first distinct carriers of manifestation:

\[
\mathcal H_D\rightsquigarrow R_3=3K_2,
\]

\[
\mathcal H_F\rightsquigarrow R_2=K_3\sqcup K_3,
\]

\[
\mathcal H_C\rightsquigarrow R_1=C_6.
\]

This does not identify a condition with a graph. The graph is the first
finite carrier on which the condition is fully visible.

The scene is complete because all three modes are present on one carrier:

- polar opposition;
- triadic splitting;
- cyclic closure.

# §13. The Cyclic Operator \(T\)

On the cycle \(C_6\), let \(T\) be the step operator:

\[
100\mapsto110\mapsto010\mapsto011\mapsto001\mapsto101\mapsto100.
\]

Then

\[
T^6=\operatorname{id}.
\]

The half-period is complementarity:

\[
T^3=\kappa.
\]

Thus cyclic traversal and polar opposition are tied on the first complete
scene.

# §14. Boundary Grammar \(\partial,\delta\)

In the simplicial reading, active states are faces of a simplex boundary.
This gives the boundary operator:

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}).
\]

The law is

\[
\partial^2=0.
\]

The coboundary operator is

\[
\delta(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

The law is

\[
\delta^2=0.
\]

Complementarity exchanges boundary and coboundary:

\[
\kappa\partial=\delta\kappa.
\]

This is a local law of the simplicial core of DOT.

It is important to separate \(R_2\) from \(\partial\). The relation \(R_2\)
is horizontal: it relates states inside the same layer. The operator
\(\partial\) is vertical: it maps a face to its immediate boundary faces.

# §15. Why \(U_3\) Is the First Complete Scene

Rank \(1\) gives the polar pair. Rank \(2\) gives a square and an active
pair. Rank \(3\) gives the first active carrier on which three modes of
holding are visible at once.

The first complete scene has:

\[
3K_2,\qquad K_3\sqcup K_3,\qquad C_6.
\]

These three structures live on the same six positions. Their compatibility
is the finite core of the first full DOT scene.

# Part IV. Axes, Invariants, and Readings

# §16. Limiting Axes

An axis of \(U_n\) is a complementary pair:

\[
H_A=\{A,J_n\setminus A\}.
\]

At rank \(3\), there are three axes:

\[
\{001,110\},\qquad
\{010,101\},\qquad
\{100,011\}.
\]

In the simplicial reading of \(\partial\Delta^2\), each axis has the form

\[
\text{vertex}\leftrightarrow\text{opposite edge}.
\]

Thus rank \(3\) already contains the simplest form of projective
direction: a pair of complementary faces read as one axis.

# §17. Projective Factor and Names of Axes

The quotient of \(U_n\) by complementarity has

\[
|U_n/\kappa|=2^{n-1}-1
\]

points and is naturally read as

\[
U_n/\kappa\cong PG(n-2,2).
\]

For rank \(3\):

\[
U_3/\kappa\cong PG(1,2).
\]

This is the three-point projective line over \(\mathbb F_2\).

The three axes are named

\[
D,\qquad F,\qquad C.
\]

At this point the names are labels of the three complementary axes. Their
interpretive content is introduced after the finite structure has been
fixed.

# §18. Axis as Invariant Manifested by a Pair

After the three axes have been named, the full rank-3 carrier receives a
metacube reading:

\[
Q_3=D\times F\times C.
\]

The active carrier \(U_3\) consists of the six mixed modes between the two
total limits \(000\) and \(111\).

At this point \(D,F,C\) are names of the three points of the projective
factor \(U_3/\kappa\), hence names of the three invariant axes of the
first complete scene.

Each axis has three levels of reading:

\[
\begin{array}{c|c}
\text{level} & \text{what is given} \\
\hline
1 & \text{one invariant of the axis} \\
2 & \text{two sides of its manifestation on } U_3 \\
3 & \text{three structural places: side, invariant, opposite side}
\end{array}
\]

For an axis \(H_A=\{A,\kappa(A)\}\):

\[
O_A\leadsto \{A,\kappa(A)\}\leadsto (A,O_A,\kappa(A)).
\]

Here \(O_A\) is the invariant of the axis. It is not added to the carrier
as a new vertex. It specifies the standpoint from which \(A\) and
\(\kappa(A)\) are read as the two sides of one axis.

Thus the number \(6\) in \(U_3\) has two compatible readings:

\[
|U_3|=3\times 2.
\]

There are three axial invariants, each manifested by two sides on the
active carrier. There is also a level reading:

\[
1\cdot 2\cdot 3.
\]

Here \(1\) is the invariant of the axis, \(2\) is its paired
manifestation, and \(3\) is the minimal triadic scheme of holding: one
side, the invariant itself, and the opposite side.

Rank \(3\) is the first rank that holds three axial invariants together.
Rank \(1\) has one full polar carrier. Rank \(2\) has an active inner pair
between the limits. Rank \(3\) has three axes, three relations
\(R_1,R_2,R_3\), three modes of holding, and one common invariant of the
complete scene.

# §19. Triadicity of the Invariant and the Two Chambers

The two-chamber structure \(R_2=K_3\sqcup K_3\) shows how the triadicity
of the invariant unfolds on the active carrier.

The first layer is

\[
S_1^{(3)}=\{100,010,001\}.
\]

It singles out one side of one of the three axes.

The second layer is

\[
S_2^{(3)}=\{110,101,011\}.
\]

It singles out the complement of one side, that is, the opposite edge in
the simplicial reading.

Complementarity exchanges the layers:

\[
\kappa(S_1^{(3)})=S_2^{(3)},\qquad
\kappa(S_2^{(3)})=S_1^{(3)}.
\]

In the logical reading this gives a De Morgan form. In the boundary
reading it exchanges boundary and coboundary. In the cyclic reading it is
the half-period \(T^3=\kappa\).

Action and boundary are two modes of the same triadic scheme:

\[
\text{action: source }|\text{ transition }|\text{ result},
\]

\[
\text{boundary: inside }|\text{ edge }|\text{ outside}.
\]

Both records have the same form: two sides and an intervening place by
which they are held as one structure. Object and action are therefore two
readings of one invariant. The object is the reading from the side of a
stable carrier; the action is the reading from the side of transition.

# §20. Four Readings of Rank \(3\)

The first complete scene has several compatible readings.

In the logical reading, complementarity is NOT, and the two chambers are
related by De Morgan duality.

In the graph reading, the three relation layers are \(C_6\),
\(K_3\sqcup K_3\), and \(3K_2\).

In the geometric reading, \(R_1\cup R_2\) is the skeleton of the
octahedron, while \(R_3\) is the system of opposite pairs.

In the cyclic and analytic reading, \(T\) is the generator of a six-step
cycle and \(T^3=\kappa\) is the half-period law.

These readings are projections of one finite scene.

# §21. Observer of the Complete Scene

At this point the construction has produced

\[
U_3,\quad R_1,R_2,R_3,\quad \kappa,\quad T,\quad \partial,\quad \delta.
\]

The observer of the first complete scene can now be written as

\[
O_3^{\mathrm{adm}}
=\bigcap_{A\in\mathcal A_{S_3}}\operatorname{Inv}(A).
\]

The notation \(O_3^{\mathrm{adm}}\) marks the admissibility invariant of
rank \(3\), not the set of axes \(I_3^{\mathrm{axes}}\).

A minimal operator reading is

\[
O_3^{\mathrm{adm}}\sim(\kappa,\partial,T).
\]

Here \(\kappa\) holds limiting complementarity, \(\partial\) holds the
recoverable boundary trace, and \(T\) holds cyclic transition. Concrete
computations of the separate invariants are carried out in the later
volumes.

# Part V. Map of Higher Unfoldings

# §22. Axis Types in Higher Ranks

For \(U_n\), an axis is a complementary cut

\[
H_A=\{A,J_n\setminus A\}.
\]

Its type is determined by the sizes of the two sides:

\[
(|A|,n-|A|).
\]

At rank \(3\), all axes have the same type \((1,2)\). At rank \(4\), two
types appear:

\[
(1,3),\qquad (2,2).
\]

The self-dual type \((2,2)\) is new. It is the middle layer of the
tetrahedral boundary and carries the octahedral slice of rank \(4\).

# §23. Ranks \(4\) and \(5\) as Pointers

Rank \(4\) has active carrier

\[
U_4=Q_4\setminus\{0000,1111\}.
\]

Its layers have sizes

\[
4+6+4.
\]

The middle layer of size \(6\) is an octahedral slice. The quotient
\(U_4/\kappa\) is the Fano plane:

\[
U_4/\kappa\cong PG(2,2).
\]

Rank \(5\) has active carrier of size \(30\), with layers

\[
5+10+10+5.
\]

Its middle layers carry graphs such as \(L(K_5)\) and the Petersen graph,
and the quotient by complementarity gives

\[
U_5/\kappa\cong PG(3,2).
\]

# §24. General Projective and Arithmetic Law

In general:

\[
|U_n|=2^n-2=2(2^{n-1}-1).
\]

The quotient by complementarity gives

\[
|U_n/\kappa|=2^{n-1}-1.
\]

The projective reading is

\[
U_n/\kappa\cong PG(n-2,2).
\]

The arithmetic line uses the factorization of \(2^{n-1}-1\). Fermat prime
thresholds appear at ranks

\[
3,5,9,17,33,\ldots
\]

These ranks form a cyclic-constructible horizon rather than the strict
core of the theory.

# §25. What the Next Volumes Unfold

Volume 1 proves the rank-3 core in strict finite form.

Volume 2 develops higher ranks, axis types, and projective architecture.

Volume 3 develops boundary operators and scene reductions.

Volume 4 develops the operator tower.

Volume 5 develops the Fano-tetrahedral reading of rank \(4\).

Volume 6 develops cycles, circle, and topological avatars.

# §26. Summary of Volume 0

The foundation of DOT can be summarized as follows.

Distinction is structurally held non-coincidence.

A scene is a finite carrier with a grammar of relations and operators and
an invariant structure of reading.

The observer is the invariant side of a scene.

Rank is the number of independent binary distinctions held together.

The active carrier is obtained by setting apart the two total limits of
the full binary carrier.

The active carrier has a simplicial boundary reading:

\[
U_n=\mathcal F(\partial\Delta^{n-1}).
\]

Rank \(3\) is the first complete scene:

\[
S_3=(U_3;R_1,R_2,R_3).
\]

On it:

\[
R_1=C_6,\qquad R_2=K_3\sqcup K_3,\qquad R_3=3K_2.
\]

The octahedral skeleton is

\[
(U_3,R_1\cup R_2)\cong K_{2,2,2}.
\]

The quotient \(U_3/\kappa\) gives three axes. Each axis is read as one
invariant manifested by a pair and held by a triadic scheme:

\[
O_A\leadsto \{A,\kappa(A)\}\leadsto (A,O_A,\kappa(A)).
\]

The observer of the first complete scene has the minimal operator reading

\[
O_3^{\mathrm{adm}}\sim(\kappa,\partial,T).
\]

The later volumes unfold the same structure through higher ranks,
boundary operators, operator towers, projective factors, cycles, and
topological avatars.
