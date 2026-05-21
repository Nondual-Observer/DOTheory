# DOT: Distinction Observable Theory

# Volume 4. Operator Tower

Volumes 0-3 built active carriers, the strict rank-3 scene, higher-rank
projective architecture, and boundary operators.

Volume 4 moves to the next level:

\[
\boxed{
\text{positions}\longrightarrow\text{operators as positions}.
}
\]

The central construction is

\[
\boxed{
\mathcal B=\mathcal Q\circ\mathcal Q.
}
\]

Here

\[
\mathcal Q(J)=\mathcal P(J)
\]

is the power-set functor, and

\[
\mathcal B(J)=\mathcal P(\mathcal P(J))
\]

is the operator carrier.

The mathematical content is standard finite set functoriality, Boolean
functions, affine functions over \(\mathbb F_2\), involutions, and the
Klein four-group. The DOT-specific content is the reappearance of the
octahedral law inside operator levels and the operator form of the
inter-rank principle:

\[
\boxed{\text{the content of a level becomes the grammar of the next level}.}
\]

---

# How to Read This Volume

Reading order:

1. minimal operator example on a polar pair;
2. power-set functor \(\mathcal Q\);
3. functorial rank growth;
4. operator carrier \(\mathcal B=\mathcal Q\circ\mathcal Q\);
5. low floors of the operator tower;
6. rank \(4\) in operator reading;
7. two operator involutions;
8. Klein four-group;
9. fixed layers and self-dual functions;
10. rank \(8\), balanced layer, and cross-polytope;
11. three appearances of the octahedron.

---

# Basic Notation

\[
\mathcal Q(J)=\mathcal P(J).
\]

\[
\mathcal B(J)=\mathcal P(\mathcal P(J)).
\]

For a finite set \(J\), an element of \(\mathcal B(J)\) can be read as a
Boolean function on \(\mathcal P(J)\), or as a selected subset of the
power-set carrier.

When \(|J|=m\),

\[
|\mathcal Q(J)|=2^m,
\]

and

\[
|\mathcal B(J)|=2^{2^m}.
\]

---

# 1. What Volume 4 Adds

The earlier volumes studied finite carriers and relations on them.

Volume 4 studies the space of possible readings of a carrier. A subset of
\(\mathcal P(J)\) can be interpreted as a Boolean predicate on faces of
\(J\). Therefore the set

\[
\mathcal P(\mathcal P(J))
\]

is the carrier of Boolean operators on the power-set scene.

This is the first step of the operator tower.

---

# 2. Minimal Operator Example

Take the polar pair

\[
P=\{0,1\}.
\]

The power set is

\[
\mathcal P(P)=\{\varnothing,\{0\},\{1\},P\}.
\]

An operator reading is a subset of this four-element set. Therefore the
operator carrier has

\[
2^4=16
\]

states.

This is already a rank-4 binary carrier. Thus the operator carrier over a
one-bit base jumps to a four-bit layer.

---

# 3. Power-Set Functor \(\mathcal Q\)

The functor

\[
\mathcal Q:\mathbf{FinSet}\to\mathbf{FinSet}
\]

is defined by

\[
\mathcal Q(J)=\mathcal P(J).
\]

For a map

\[
f:J\to K,
\]

there are two natural directions:

- direct image \(A\mapsto f(A)\);
- inverse image \(B\mapsto f^{-1}(B)\).

In the strict finite layer of DOT, the main rank carrier uses the
power-set object \(\mathcal P(J)\). Functoriality records that relabeling
of the base set induces relabeling of the carrier.

---

# 4. Functorial Rank Growth

If

\[
|J|=n,
\]

then

\[
\mathcal Q(J)\cong Q_n.
\]

Adding one base element sends \(J_n\) to \(J_{n+1}\), and the carrier
grows from

\[
Q_n
\]

to

\[
Q_{n+1}.
\]

This is the functorial form of binary rank growth.

It is compatible with the axial inter-rank law from Volume 2:

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}.
\]

At the state level, configurations become axes of the next scene. At the
operator level, readings of a carrier become positions in a new carrier.

---

# 5. Operator Carrier \(\mathcal B\)

The operator carrier is

\[
\boxed{
\mathcal B(J)=\mathcal P(\mathcal P(J)).
}
\]

It is the power set of the rank carrier.

Equivalently, \(\mathcal B(J)\) is the set of Boolean predicates on
\(\mathcal P(J)\):

\[
\mathcal B(J)\cong\{0,1\}^{\mathcal P(J)}.
\]

If \(|J|=m\), then

\[
|\mathcal B(J)|=2^{2^m}.
\]

Thus \(\mathcal B(J)\) has the size of a binary carrier of rank \(2^m\).

---

# 6. Floors of the Operator Tower

The first floors are:

\[
|J|=1:\quad |\mathcal B(J)|=2^2=4,
\]

\[
|J|=2:\quad |\mathcal B(J)|=2^4=16,
\]

\[
|J|=3:\quad |\mathcal B(J)|=2^8=256.
\]

The ranks are:

\[
2,\quad4,\quad8.
\]

Thus the operator tower doubles rank exponentials:

\[
1\mapsto2,\quad2\mapsto4,\quad3\mapsto8.
\]

The tower follows powers of two.

---

# 7. Rank \(4\) in Operator Reading

For a two-element base \(J_2\),

\[
\mathcal P(J_2)
\]

has four elements.

Therefore

\[
\mathcal B(J_2)
\]

has \(16\) elements and can be read as a rank-4 binary carrier.

This is the first substantial operator carrier. It contains the Boolean
functions on a two-bit input.

---

# 8. Middle Layer of Binary Operators

A Boolean function on two variables has a truth table of length \(4\).

The balanced functions are those with two zeros and two ones. There are

\[
\binom42=6
\]

such functions.

This six-state middle layer has an octahedral form, matching the
six-state carrier \(U_3\).

Thus the octahedron appears again, now as a layer of operators.

---

# 9. Two Operator Involutions

## 9.1. Output Negation

For a Boolean function \(f\), define

\[
C_{\mathrm{out}}(f)=1+f.
\]

This flips the output.

It satisfies

\[
C_{\mathrm{out}}^2=\operatorname{id}.
\]

## 9.2. Input Complement

For a two-bit input \(x\), define

\[
C_{\mathrm{in}}(f)(x)=f(1+x).
\]

This complements the input before applying \(f\).

It satisfies

\[
C_{\mathrm{in}}^2=\operatorname{id}.
\]

## 9.3. Commutativity

Output negation and input complement commute:

\[
C_{\mathrm{out}}C_{\mathrm{in}}
=C_{\mathrm{in}}C_{\mathrm{out}}.
\]

Together they generate a Klein four-group.

---

# 10. Klein Four-Group

The group generated by the two involutions is

\[
G_B=\langle C_{\mathrm{out}},C_{\mathrm{in}}\rangle.
\]

It has four elements:

\[
\operatorname{id},\quad
C_{\mathrm{out}},\quad
C_{\mathrm{in}},\quad
C_{\mathrm{out}}C_{\mathrm{in}}.
\]

Hence

\[
\boxed{
G_B\cong V_4.
}
\]

This group organizes the basic symmetries of the operator carrier.

---

# 11. Fixed Layers of the Klein Four-Group

## 11.1. Input-Invariant Functions

A function is input-invariant when

\[
f(x)=f(1+x).
\]

Such functions are fixed by \(C_{\mathrm{in}}\).

## 11.2. Self-Dual Functions

A function is self-dual when

\[
f(1+x)=1+f(x).
\]

Equivalently,

\[
C_{\mathrm{out}}C_{\mathrm{in}}(f)=f.
\]

The self-dual functions form a six-state layer in the two-variable case.

## 11.3. Output-Negation Fixed Points

No Boolean function over \(\mathbb F_2\) is fixed by output negation alone:

\[
f=1+f
\]

has no solution.

This distinguishes the three nontrivial involutions of the Klein group.

## 11.4. Summary Table

\[
\begin{array}{c|c|c}
\text{operation} & \text{condition} & \text{reading}\\
\hline
C_{\mathrm{in}} & f(x)=f(1+x) & \text{input-invariant}\\
C_{\mathrm{out}} & f=1+f & \text{no fixed functions}\\
C_{\mathrm{out}}C_{\mathrm{in}} & f(1+x)=1+f(x) & \text{self-dual}
\end{array}
\]

---

# 12. Self-Duality and Balancedness

For two variables, every self-dual function is balanced: it has two zeros
and two ones.

Therefore the self-dual layer sits inside the six-state balanced layer.

This six-state layer is the operator-level analogue of the rank-3 active
carrier.

It carries an octahedral organization.

---

# 13. Affine Subcarrier of Rank \(8\)

For a three-element base \(J_3\), the operator carrier has rank \(8\):

\[
\mathcal B(J_3)\cong Q_8.
\]

Inside the Boolean functions on \(Q_3\), the affine functions have the
form

\[
f(x)=a_0+a_1x_1+a_2x_2+a_3x_3.
\]

There are

\[
2^4=16
\]

affine functions.

This affine subcarrier is a structured subset of the rank-8 operator
carrier.

---

# 14. Central Layer of Rank \(8\)

The rank-8 carrier has a central balanced layer of size

\[
\binom84=70.
\]

The affine subcarrier intersects this balanced layer in a special finite
configuration.

After restriction to the right operator-invariant subset, another
octahedral-like structure appears here.

---

# 15. Third Octahedron

DOT records three appearances of the octahedral law:

1. rank \(3\): the state carrier \(U_3\);
2. rank \(4\): the balanced/self-dual operator layer on two variables;
3. rank \(8\): the affine operator layer on three variables.

The third appearance is not a new axiom. It is a repeated operator-level
manifestation of the same six-state law.

---

# 16. Bijection with Rank-3 Axes

The operator involutions and their fixed structures can be related to the
three axial directions of \(U_3\).

The precise bijection depends on the chosen presentation of the operator
carrier. The invariant content is:

- there are three nontrivial involutive directions in the Klein group;
- there are three axes in the rank-3 active carrier;
- the operator tower repeats the three-axis form at a higher level.

---

# 17. Three Appearances of the Octahedron

## 17.1. First Appearance

The first appearance is

\[
U_3=Q_3\setminus\{000,111\}.
\]

It is the six-state active carrier of the first complete scene.

## 17.2. Second Appearance

The second appearance is the six-state balanced/self-dual layer in the
rank-4 operator carrier over a two-element base.

## 17.3. Third Appearance

The third appearance is in the rank-8 operator carrier, inside the affine
operator structure.

## 17.4. General Law

The general law is:

\[
\boxed{
\text{the octahedral carrier reappears when operator layers acquire a
three-axis involutive structure.}
}
\]

---

# 18. Status of the Operator Tower

The operator tower is strict where it uses:

- finite sets;
- power sets;
- Boolean functions;
- involutions;
- fixed-point conditions;
- finite counts.

Its interpretation as repeated DOT architecture is a structural reading
supported by the explicit finite correspondences.

---

# 19. Relation to Previous Volumes

Volume 1:

\[
U_3
\]

as the first state-level octahedron.

Volume 2:

\[
U_n/\kappa\cong PG(n-2,2)
\]

as projective axial factor, together with

\[
Q_n^*\cong U_{n+1}/\kappa_{n+1}
\]

as inter-rank axial lift.

Volume 3:

\[
\kappa\partial=\delta\kappa
\]

as compatibility of polar and boundary grammars.

Volume 4:

\[
\mathcal B=\mathcal Q\circ\mathcal Q
\]

as the operator-level carrier.

---

# 20. What Volume 4 Establishes

Volume 4 establishes:

- the power-set functor \(\mathcal Q\);
- the operator carrier \(\mathcal B\);
- the first floors of the operator tower;
- output negation and input complement;
- the Klein four-group;
- self-dual and balanced functions;
- the operator form of the inter-rank growth principle;
- the recurrence of the octahedral law at operator levels.

---

# Appendix A. Main Theorem of Volume 4

For every finite set \(J\), the double power-set construction

\[
\mathcal B(J)=\mathcal P(\mathcal P(J))
\]

is the finite carrier of Boolean predicates on \(\mathcal P(J)\).

For \(|J|=2\), the balanced/self-dual layer contains a six-state structure
with the same octahedral law as \(U_3\).

---

# Appendix B. Operator Tower Table

\[
\begin{array}{c|c|c|c}
|J| & |\mathcal Q(J)| & |\mathcal B(J)| & \text{operator rank}\\
\hline
1 & 2 & 4 & 2\\
2 & 4 & 16 & 4\\
3 & 8 & 256 & 8
\end{array}
\]

---

# Appendix C. Three Octahedra

\[
\begin{array}{c|c|c}
\text{appearance} & \text{carrier} & \text{role}\\
\hline
1 & U_3 & \text{state-level first complete scene}\\
2 & \text{rank-4 operator layer} & \text{Boolean operator symmetry}\\
3 & \text{rank-8 affine layer} & \text{higher operator recurrence}
\end{array}
\]

---

# Summary of Volume 4

Volume 4 turns operators into positions. The double power-set construction

\[
\mathcal B=\mathcal Q\circ\mathcal Q
\]

builds the operator carrier. On this carrier, output negation and input
complement generate a Klein four-group. Self-dual and balanced functions
produce six-state layers in which the octahedral law reappears.

The result is an operator tower in which the first complete scene of DOT
is not isolated; it repeats at higher operator levels.

Together with the inter-rank lift, Volume 4 gives two coordinated growth
forms:

\[
\begin{array}{c|c}
\text{inter-rank lift} & \text{configurations become axes}\\
\text{operator tower} & \text{readings become positions}
\end{array}
\]
