# DOT: Inter-Rank Lift of Relations and Operators

This note records the current English form of the inter-rank mechanism used
in the main corpus. The full Russian research note is longer; this version
keeps the statements that are needed for Volumes 2-6.

The central law is:

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}.
\]

The content of one rank becomes the axial grammar of the next rank.

# 1. Full Polar Lift

Let

\[
L_{n+1}=J_n\sqcup\{\ast\}.
\]

Then

\[
Q_{n+1}=\mathcal P(L_{n+1}).
\]

For each \(A\subseteq J_n\), define its polar lift by

\[
\Phi_n(A)=\{A,\ L_{n+1}\setminus A\}.
\]

The two elements of this pair are complements in \(Q_{n+1}\). Therefore
\(\Phi_n(A)\) is a \(\kappa_{n+1}\)-axis.

This gives a bijection:

\[
\Phi_n:Q_n\longrightarrow Q_{n+1}/\kappa_{n+1}.
\]

Hence

\[
Q_n\cong Q_{n+1}/\kappa_{n+1}.
\]

This is the full inter-rank invariant.

# 2. Active Polar Lift

The active carrier of rank \(n+1\) is

\[
U_{n+1}=Q_{n+1}\setminus\{\varnothing,L_{n+1}\}.
\]

The empty configuration of \(Q_n\) lifts to the limiting axis

\[
\varnothing\mapsto \{\varnothing,L_{n+1}\}.
\]

This axis is removed from \(U_{n+1}\). Therefore the active lift starts
from the nonempty part

\[
Q_n^*=Q_n\setminus\{\varnothing\}.
\]

Thus:

\[
\Phi_n:Q_n^*\longrightarrow U_{n+1}/\kappa_{n+1},
\]

and

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}.
\]

The upper configuration \(J_n\) is included. It lifts to the axis

\[
J_n\mapsto \{J_n,\{\ast\}\},
\]

which is a legitimate internal axis of \(U_{n+1}\).

# 3. Examples

## 3.1. Step \(1\to2\)

\[
Q_1^*=\{1\}.
\]

The active lift gives one axis in \(U_2\):

\[
1\mapsto \{01,10\}.
\]

This is the active pair of rank \(2\).

## 3.2. Step \(2\to3\)

\[
Q_2^*=\{01,10,11\}.
\]

These three configurations become the three axes of \(U_3\):

\[
01\mapsto\{001,110\},
\]

\[
10\mapsto\{010,101\},
\]

\[
11\mapsto\{011,100\}.
\]

Therefore

\[
Q_2^*\cong U_3/\kappa_3.
\]

The three axes of the rank-3 octahedral scene are the lifted nonempty
configurations of rank \(2\).

## 3.3. Step \(3\to4\)

\[
Q_3^*=\{001,010,011,100,101,110,111\}.
\]

These seven configurations become the seven axes of \(U_4\):

\[
001\mapsto\{0001,1110\},
\]

\[
010\mapsto\{0010,1101\},
\]

\[
011\mapsto\{0011,1100\},
\]

\[
100\mapsto\{0100,1011\},
\]

\[
101\mapsto\{0101,1010\},
\]

\[
110\mapsto\{0110,1001\},
\]

\[
111\mapsto\{0111,1000\}.
\]

Thus

\[
Q_3^*\cong U_4/\kappa_4.
\]

The quotient is the Fano plane:

\[
U_4/\kappa_4\cong PG(2,2).
\]

In this reading, the seven Fano points are lifted rank-3 configurations.

# 4. Lift of Relations

Let \(R_d\) be the Hamming-distance relation on \(Q_n\):

\[
R_d(A,B)\quad\Longleftrightarrow\quad |A\triangle B|=d.
\]

The polar lift sends points \(A,B\in Q_n\) to axes

\[
\Phi_n(A),\qquad \Phi_n(B)
\]

inside \(Q_{n+1}/\kappa_{n+1}\).

Define the lifted relation by

\[
\widehat R_d(\Phi_n(A),\Phi_n(B))
\quad\Longleftrightarrow\quad
R_d(A,B).
\]

Then the quotient carrier

\[
Q_{n+1}/\kappa_{n+1}
\]

inherits the Hamming scheme of \(Q_n\).

In active form the same statement applies to

\[
U_{n+1}/\kappa_{n+1}
\]

with the limiting axis removed.

# 5. Boundary Operators

On the subset language, the boundary operator is

\[
\partial(A)=\sum_{a\in A}(A\setminus\{a\}),
\]

and the coboundary is

\[
\delta(A)=\sum_{b\notin A}(A\cup\{b\}).
\]

They satisfy

\[
\partial^2=0,\qquad \delta^2=0,
\]

and complementarity exchanges them:

\[
\kappa\partial=\delta\kappa.
\]

Under the polar lift, an axis contains both sides:

\[
\Phi_n(A)=\{A,L_{n+1}\setminus A\}.
\]

The boundary of one side corresponds to the coboundary of the complementary
side. Thus the boundary lift is naturally two-sided: the lifted axis keeps
the \(\partial/\delta\) duality as part of its internal grammar.

# 6. Cycles and Cyclic Avatars

Strict cycles are cycles inside the graph \(R_1(U_n)\). Their edges are
ordinary Hamming-distance-1 edges of the active carrier.

A cyclic avatar is different. Start with a cycle of axes in
\[
U_{n+1}/\kappa_{n+1}.
\]

Choose a lift of that cycle to \(U_{n+1}\). If the lifted traversal switches
side each time it moves to the next axis, then a cycle of \(m\) axes becomes
a \(2m\)-step cycle on the lifted carrier.

The resulting transport \(T\) satisfies

\[
T^{2m}=\operatorname{id},\qquad T^m=\kappa.
\]

For rank \(3\), the three-axis cycle lifts to the six-cycle

\[
C_6.
\]

This gives the familiar law:

\[
T^6=\operatorname{id},\qquad T^3=\kappa.
\]

On higher ranks, strict \(R_1\)-cycles and cyclic avatars should be kept
separate. A strict cycle belongs to the Hamming graph. A cyclic avatar
belongs to the lifted axial grammar.

# 7. Reductions

The reduction \(\rho_D\) collapses complementary sides into axes:

\[
\rho_D:U_n\to U_n/\kappa_n.
\]

By the active lift,

\[
U_n/\kappa_n\cong Q_{n-1}^*.
\]

Therefore \(\rho_D\) has a rank-to-rank reading:

\[
\rho_D:U_n\to Q_{n-1}^*.
\]

It sends the current scene to the nonempty configuration grammar of the
previous rank.

The other reductions \(\rho_F\) and \(\rho_C\) should be read together
with the traces and closures they preserve or collapse. Their exact
inter-rank form depends on the relation or operator being lifted.

# 8. Summary

The main formulas are:

\[
Q_n\cong Q_{n+1}/\kappa_{n+1},
\]

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1},
\]

\[
\widehat R_d(\Phi_n(A),\Phi_n(B))
\Longleftrightarrow
R_d(A,B),
\]

\[
\kappa\partial=\delta\kappa,
\]

\[
T^{2m}=\operatorname{id},\qquad T^m=\kappa.
\]

The conceptual form is:

\[
\boxed{\text{the content of one rank becomes the grammar of the next rank}.}
\]

