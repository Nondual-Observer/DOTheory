# DOT: logico-operator reading of the operator tower

In this bridge the power-set carrier \(Q_n\) is read as a Boolean algebra
\[
Q_J=\mathcal P(J),
\]
and the operator tower arises as iterated application of the power-set carrier:
\[
\mathcal B_J=\mathcal P(\mathcal P(J)).
\]

Rank \(3\) yields the punctured Boolean carrier \(X_3\). Rank \(4\) yields the space of binary Boolean operators. Rank \(8\) yields the space of ternary Boolean operators and the central layer \(S_4^{(8)}\). These levels are linked by a single group of natural involutions.

## Main organizing principle

The Klein four-group of involutions
\[
G_{\mathrm{B}}=\langle C_{\mathrm{out}},C_{\mathrm{in}}\rangle\cong\mathbb Z_2\times\mathbb Z_2
\]
acts on the operator tower $\mathcal B_m$. Its three nontrivial elements yield three series of natural subcarriers. Through this action the three appearances of the octahedron at rank 3, rank 4, and rank 8 become three realizations of a single functorial law.

## Route

\[
\mathbb D
\;\to\;
Q_J=\mathcal P(J)
\;\to\;
\mathcal B_J=\mathcal P(\mathcal P(J))
\;\to\;
G_{\mathrm{B}}\text{-stratification}.
\]

---

# §1. The coordinate carrier $\mathbb D$ and the involution $\nu$

## §1.1. Coordinate reading of the polar layer

The strict core in §1 constructs the polar layer $(P,R_P)$, $P=\{a,-a\}$. In §3 the polarity $a$ receives the coordinate name $0$, and the polarity $-a$ the name $1$. The rank-1 coordinate carrier is
\[
\mathbb D=\{0,1\}.
\]

Connection with the core: $\mathbb D$ is the coordinate reading of the polar layer $(P,R_P)$ from the strict core §3.

## §1.2. The involution $\nu$

On $\mathbb D$ there is exactly one nontrivial bijection:
\[
\nu:\mathbb D\to\mathbb D,
\qquad
\nu(0)=1,
\qquad
\nu(1)=0.
\]

This is the coordinate reading of the canonical permutation $\tau$ from the strict core §2.

In logical language $\nu$ is called `NOT`.

## §1.3. Coordinate reading and operator status

`NOT` appears here as exactly one coordinate involution on $\mathbb D$. It is the first element of the future operator tower.

In the rank-1 strict core neither `AND` nor `OR` is yet defined: they require a second coordinate digit. Therefore this section fixes exactly the coordinate involution, without any claim to functional completeness of the Boolean algebra.

In this bridge `NOT` is the logical name for $\tau$ from the strict core §2.

---

# §2. The power-set carrier $Q_J$ and the Hamming relation

## §2.1. The power-set carrier

For a finite set $J$:
\[
Q_J=\mathcal P(J).
\]

A coordinate bijection $J\xrightarrow{\sim}\{1,\ldots,n\}$ gives the canonical identification
\[
Q_J\cong\{0,1\}^n=Q_n.
\]

Connection with the core: $Q_n$ as the $n$-bit coordinate carrier is constructed in the strict core §3 (rank 1), §4 (rank 2), §5 (rank 3).

## §2.2. The weight-$k$ layer

\[
S_k(J)=\{A\subseteq J:|A|=k\}.
\]

Connection with the core: the layer decomposition of the strict core §5.6 gives the same stratification for $J=J_3$.

Cardinality:
\[
|S_k(J)|=\binom{n}{k}.
\]

## §2.3. The Hamming relation on $Q_J$

\[
R_d^J(A,B)
\quad\Longleftrightarrow\quad
|A\triangle B|=d.
\]

Connection with the core: for $J=J_3$ and $d\in\{1,2,3\}$ this coincides with the relation grammar of the strict core §6. Here $R_d^J$ is generalized functorially.

## §2.4. Agreement with bitwise sum

Under the coordinate identification $Q_J\cong\mathbb F_2^n$:
\[
A\triangle B=A\oplus B,
\]
where $\oplus$ is bitwise addition in $\mathbb F_2^n$.

In logical language $\oplus$ is called `XOR`. At the $\mathbb F_2$ level this is the same operation: $0\oplus0=0,\ 0\oplus1=1,\ 1\oplus0=1,\ 1\oplus1=0$.

## §2.5. The complement involution

\[
\kappa_J(A)=J\setminus A.
\]

Properties:
\[
\kappa_J^2=\operatorname{id}_{\mathcal P(J)},
\qquad
\kappa_J(S_k(J))=S_{n-k}(J).
\]

Connection with the core: for $J=J_3$ this is the complement involution of the strict core §5.8.

---

# §3. The punctured Boolean carrier of rank 3

## §3.1. Rank-3 coordinates and neutral names

Let $J_3=\{e_1,e_2,e_3\}$ be a three-element set with neutral coordinate labels. The names $e_i$ are chosen deliberately so as not to collide with the reserved names of the axial invariants of the semantic layer (the names $D/F/C$ appear in the strict core but are not used in this bridge).

## §3.2. The power-set carrier of rank 3

\[
Q_3=\mathcal P(J_3),
\qquad
|Q_3|=8.
\]

The eight elements:
\[
\varnothing,
\quad
\{e_1\},\{e_2\},\{e_3\},
\quad
\{e_2,e_3\},\{e_1,e_3\},\{e_1,e_2\},
\quad
J_3.
\]

In coordinate notation:
\[
000,
\quad
100,010,001,
\quad
011,101,110,
\quad
111.
\]

## §3.3. The punctured carrier $X_3$

\[
X_3
=Q_3\setminus\{\varnothing,J_3\}
\cong
Q_3\setminus\{000,111\}.
\]

Connection with the core: \(X_3\) is exactly \(X_{\mathrm{adm}}\) from the strict core §5.5. This is one set in two readings: in the core it is the admissible carrier of rank \(3\), and in this bridge it is the punctured Boolean carrier.

Cardinality:
\[
|X_3|=6.
\]

Decomposition into layers:
\[
X_3=S_1^{(3)}\sqcup S_2^{(3)},
\]
\[
S_1^{(3)}=\{\{e_1\},\{e_2\},\{e_3\}\},
\qquad
S_2^{(3)}=\{\{e_2,e_3\},\{e_1,e_3\},\{e_1,e_2\}\}.
\]

## §3.4. Complement pairs on \(X_3\)

The complement $\kappa_3=\kappa_{J_3}$ swaps $S_1^{(3)}$ and $S_2^{(3)}$:
\[
\{e_1\}\leftrightarrow\{e_2,e_3\},
\qquad
\{e_2\}\leftrightarrow\{e_1,e_3\},
\qquad
\{e_3\}\leftrightarrow\{e_1,e_2\}.
\]

Connection with the core: these three complement pairs coincide with \(\beta_1,\beta_2,\beta_3\), which define the inner axial layer of the full octahedral scene in the strict core §7.

## §3.5. The relation grammar on \(X_3\) in the Boolean reading

By §2.3:
\[
R_1^{(3)}:\ |A\triangle B|=1,
\]
\[
R_2^{(3)}:\ |A\triangle B|=2,
\]
\[
R_3^{(3)}:\ |A\triangle B|=3.
\]

Connection with the core: this is exactly $R_1,R_2,R_3$ from the strict core §6 with $J=J_3$, restricted to $X_3$.

In the bridge notation:
\[
R_3^{(3)}=3K_2
\]
is the three complement pairs.

## §3.6. Boolean operations as reading

On the full $Q_3$ the standard operations are defined:
\[
A\wedge B=A\cap B,
\]
\[
A\vee B=A\cup B,
\]
\[
\neg A=\kappa_3(A)=J_3\setminus A,
\]
\[
A\oplus B=A\triangle B.
\]

On $X_3$ these operations are not closed: $\{e_1\}\cap\{e_2\}=\varnothing\notin X_3$, $\{e_1\}\cup\{e_2,e_3\}=J_3\notin X_3$.

The Boolean operations exist on $Q_3$ as structure; on $X_3$ they serve as a `reading`, from which the proper relations $R_1,R_2,R_3$ are recovered.

## §3.7. Proper and bridge reading on $X_3$

Proper on $X_3$ (from the strict core):
- $X_{\mathrm{adm}}$ as a relational carrier §5;
- $R_1,R_2,R_3$ §6;
- the octahedral graph reading $R_{12}\cong K_{2,2,2}$ §7;
- the chamber layer §8;
- the incidence package §9;
- cyclic transport §10, the periodization package §11.

Bridge readings added here:
- $X_3\cong X_{\mathrm{adm}}$ as a punctured Boolean carrier;
- the Boolean operations $\cap,\cup,\neg,\oplus$ as a reading on the full $Q_3$;
- the complement pairs $\beta_i$ as Boolean complement.

---

# §4. The layer-mirror law

## §4.1. The involution $\kappa_n$ on layers

For $Q_n=\mathcal P(J_n)$:
\[
\kappa_n:S_k^{(n)}\to S_{n-k}^{(n)}.
\]

This notation means reflection of the index line $0,1,\ldots,n$ about the center $n/2$.

## §4.2. The active carrier and paired layers

The active carrier:
\[
U_n=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
\]

Paired layers:
\[
a=1,\ldots,\left\lfloor(n-1)/2\right\rfloor,
\qquad
b=n-a,
\qquad
S_a^{(n)}\leftrightarrow S_b^{(n)}.
\]

The central layer for even $n$:
\[
S_{n/2}^{(n)}\leftrightarrow S_{n/2}^{(n)}.
\]

The central pair for odd $n$:
\[
S_{(n-1)/2}^{(n)}\leftrightarrow S_{(n+1)/2}^{(n)}.
\]

## §4.3. Table of small ranks

\[
n=3:\quad S_1\leftrightarrow S_2,
\]
\[
n=4:\quad S_1\leftrightarrow S_3,\quad S_2\leftrightarrow S_2,
\]
\[
n=5:\quad S_1\leftrightarrow S_4,\quad S_2\leftrightarrow S_3,
\]
\[
n=6:\quad S_1\leftrightarrow S_5,\quad S_2\leftrightarrow S_4,\quad S_3\leftrightarrow S_3,
\]
\[
n=8:\quad S_1\leftrightarrow S_7,\ S_2\leftrightarrow S_6,\ S_3\leftrightarrow S_5,\ S_4\leftrightarrow S_4.
\]

## §4.4. Two-sided and one-sided flip

**Proposition 4.1.** Under simultaneous complementation of both sides:
\[
|\kappa_n(A)\triangle\kappa_n(B)|=|A\triangle B|.
\]

**Verification.** $\kappa_n(A)\triangle\kappa_n(B)=(J\setminus A)\triangle(J\setminus B)=A\triangle B$. $\square$

**Proposition 4.2.** Under one-sided complementation:
\[
|\kappa_n(A)\triangle B|=n-|A\triangle B|.
\]

**Verification.** $\kappa_n(A)\triangle B=(J\setminus A)\triangle B=J\triangle A\triangle B$. Since $A\triangle B\subseteq J$, $J\triangle(A\triangle B)=J\setminus(A\triangle B)$. The cardinality equals $n-|A\triangle B|$. $\square$

## §4.5. Two modes of the coordinate involution

The two-sided flip preserves the difference level \(d\). The one-sided flip sends the level \(d\) to the complementary level \(n-d\).

In particular, on $X_3$:
\[
R_1\leftrightarrow R_2
\]
by the one-sided $\kappa_3$, and
\[
R_3\leftrightarrow R_0
\]
by the one-sided $\kappa_3$. But $R_0$ is the identity, so $\kappa_3$ sends the complement pairs $R_3$ to identity pairs — this is consistent with the fact that $\kappa_3$ swaps vertices within the complement pairs $\beta_i$.

---

# §5. The power-set functor

## §5.1. The base category

\[
\mathbf{FinBij}:
\]
objects are finite sets, morphisms are bijections.

Bijections are chosen because they preserve:
- the cardinality of a subset;
- complement;
- symmetric difference;
- intersection and union.

For arbitrary maps these properties are not preserved.

## §5.2. The functor $\mathcal Q$

\[
\mathcal Q:\mathbf{FinBij}\to\mathbf{Set},
\qquad
\mathcal Q(J)=\mathcal P(J),
\]
\[
\mathcal Q(\sigma)(A)=\sigma[A].
\]

**Proposition 5.1.** $\mathcal Q$ is a functor.

**Verification.**
\[
\mathcal Q(\mathrm{id}_J)(A)=\mathrm{id}_J[A]=A,
\]
\[
\mathcal Q(\tau\circ\sigma)(A)=(\tau\circ\sigma)[A]=\tau[\sigma[A]]=\mathcal Q(\tau)(\mathcal Q(\sigma)(A)). \;\square
\]

## §5.3. Naturality of the operations

**Proposition 5.2.** For a bijection $\sigma:J\to K$:
\[
\sigma[A\cap B]=\sigma[A]\cap\sigma[B],
\]
\[
\sigma[A\cup B]=\sigma[A]\cup\sigma[B],
\]
\[
\sigma[A\triangle B]=\sigma[A]\triangle\sigma[B],
\]
\[
\sigma[J\setminus A]=K\setminus\sigma[A].
\]

**Verification.** All four formulas follow from the injectivity and surjectivity of $\sigma$. For example, for $\cap$: $\sigma[A\cap B]\subseteq\sigma[A]\cap\sigma[B]$ — the image of the intersection. The reverse inclusion: if $k\in\sigma[A]\cap\sigma[B]$, then $k=\sigma(a)=\sigma(b)$ for $a\in A,b\in B$, and injectivity gives $a=b\in A\cap B$. $\square$

## §5.4. Naturality of $\kappa$

**Proposition 5.3.** The family $\kappa_J:\mathcal P(J)\to\mathcal P(J)$ is a natural transformation $\kappa:\mathcal Q\Rightarrow\mathcal Q$:
\[
\mathcal Q(\sigma)\circ\kappa_J=\kappa_K\circ\mathcal Q(\sigma).
\]

**Verification.** Left-hand side: $\sigma[J\setminus A]=K\setminus\sigma[A]$ by 5.2. Right-hand side: $\kappa_K(\sigma[A])=K\setminus\sigma[A]$. Equality. $\square$

## §5.5. Naturality of layers and of the relation grammar

**Proposition 5.4.** Under $\mathcal Q(\sigma)$:
\[
|\sigma[A]|=|A|,
\]
\[
\mathcal Q(\sigma)(S_k(J))=S_k(K),
\]
\[
(A,B)\in R_d^J
\quad\Longleftrightarrow\quad
(\sigma[A],\sigma[B])\in R_d^K.
\]

**Verification.** The first is bijectivity. The second is a consequence of the first. The third is a consequence of 5.2 for $\triangle$ and of the first for cardinality. $\square$

## §5.6. Functorial summary of §5

All proper objects of the strict core (\(Q_n\), \(X_{\mathrm{adm}}\), \(R_d\), the complement pairs, the octahedral shell, and the full octahedral scene) do not depend on the names of the coordinates. They are natural subcarriers of \(\mathcal Q\).

---

# §6. The functorial law of rank growth

## §6.1. Coordinate extension

For a finite $J$ choose an element $\ast\notin J$:
\[
E(J)=J\sqcup\{\ast\}.
\]

For a bijection $\sigma:J\to K$:
\[
E(\sigma)=\sigma\sqcup\mathrm{id}_{\{\ast\}}:E(J)\to E(K).
\]

Connection with the core: this corresponds to the rank lift in the strict core §3 (\(P\to Q_2\)) and to its generalization in §5 (\(Q_n\to Q_{n+1}\)).

## §6.2. The splitting bijection

\[
\Lambda_J:\{0,1\}\times\mathcal P(J)\xrightarrow{\cong}\mathcal P(E(J)),
\]
\[
\Lambda_J(0,A)=A,
\qquad
\Lambda_J(1,A)=A\cup\{\ast\}.
\]

## §6.3. Naturality of $\Lambda$

**Proposition 6.1.**
\[
\mathcal Q(E(\sigma))\circ\Lambda_J=\Lambda_K\circ(\mathrm{id}_{\{0,1\}}\times\mathcal Q(\sigma)).
\]

**Verification.** For $(0,A)$: left-hand side $\mathcal Q(E(\sigma))(A)=E(\sigma)[A]=\sigma[A]=\Lambda_K(0,\sigma[A])$. For $(1,A)$: $\mathcal Q(E(\sigma))(A\cup\{\ast\})=\sigma[A]\cup\{\ast\}=\Lambda_K(1,\sigma[A])$. $\square$

## §6.4. The lift of layers

\[
\Lambda_J(0,S_k(J))\subset S_k(E(J)),
\]
\[
\Lambda_J(1,S_k(J))\subset S_{k+1}(E(J)).
\]

## §6.5. The lift of complement

**Proposition 6.2.**
\[
\kappa_{E(J)}(\Lambda_J(\varepsilon,A))=\Lambda_J(1-\varepsilon,\kappa_J(A)).
\]

**Verification.** For $\varepsilon=0$: $\kappa_{E(J)}(A)=E(J)\setminus A=(J\setminus A)\cup\{\ast\}=\Lambda_J(1,\kappa_J(A))$. For $\varepsilon=1$: $\kappa_{E(J)}(A\cup\{\ast\})=J\setminus A=\Lambda_J(0,\kappa_J(A))$. $\square$

## §6.6. The functorial form of growth

The bijection $\Lambda_J$ gives a splitting of each rank-$(n+1)$ layer into the image from rank $n$:
\[
S_k^{(n+1)}\cong S_k^{(n)}\sqcup S_{k-1}^{(n)}.
\]

This law reflects the binomial identity $\binom{n+1}{k}=\binom{n}{k}+\binom{n}{k-1}$.

---

# §7. The operator functor $\mathcal B=\mathcal Q\circ\mathcal Q$

## §7.1. The operator carrier

For $J\in\mathbf{FinBij}$:
\[
\mathcal B_J=\{0,1\}^{Q_J}.
\]

Each $f:Q_J\to\{0,1\}$ is determined by its truth support:
\[
\operatorname{supp}(f)=\{A\in Q_J:f(A)=1\}.
\]

This bijection gives the canonical identification:
\[
\mathcal B_J\cong\mathcal P(Q_J)=\mathcal P(\mathcal P(J)).
\]

## §7.2. $\mathcal B$ as a functor

\[
\mathcal B=\mathcal Q\circ\mathcal Q:\mathbf{FinBij}\to\mathbf{Set}.
\]

On objects: $\mathcal B(J)=\mathcal P(\mathcal P(J))$. On morphisms: $\mathcal B(\sigma)(U)=\mathcal Q(\sigma)[U]=\{\sigma[A]:A\in U\}$ for $U\subseteq\mathcal P(J)$.

The functoriality of $\mathcal B$ follows from the functoriality of $\mathcal Q$.

## §7.3. The functional form of $\mathcal B(\sigma)$

If $f:\mathcal P(J)\to\{0,1\}$ has $\operatorname{supp}(f)=U$, then $\mathcal B(\sigma)f$ has $\operatorname{supp}=\mathcal Q(\sigma)[U]$. Equivalently:
\[
(\mathcal B(\sigma)f)(B)=f(\mathcal Q(\sigma)^{-1}(B)),
\qquad
B\in\mathcal P(K).
\]

**Verification of equivalence.** $(\mathcal B(\sigma)f)(B)=1\iff B\in\mathcal Q(\sigma)[U]\iff\mathcal Q(\sigma)^{-1}(B)\in U\iff f(\mathcal Q(\sigma)^{-1}(B))=1$. $\square$

## §7.4. The size of the operator carrier

\[
|\mathcal B_J|=2^{|Q_J|}=2^{2^{|J|}}.
\]

For $|J|=m$:
\[
\mathcal B_m\cong Q_{2^m}.
\]

## §7.5. The operator tower

Applying $\mathcal Q$ twice gives the sequence:
\[
J
\;\xrightarrow{\mathcal Q}\;
\mathcal P(J)
\;\xrightarrow{\mathcal Q}\;
\mathcal P(\mathcal P(J)).
\]

This is the **operator tower**. Its ranks:
\[
\mathcal B_0\cong Q_1,
\qquad
\mathcal B_1\cong Q_2,
\qquad
\mathcal B_2\cong Q_4,
\qquad
\mathcal B_3\cong Q_8,
\qquad
\mathcal B_4\cong Q_{16},\ldots
\]

The subsequence of DOT ranks on which the operator reading lives:
\[
1,\ 2,\ 4,\ 8,\ 16,\ldots
\]

## §7.6. Not every rank is an operator rank

Ranks \(3,5,6,7\) do not have the form \(\mathcal B_m\) for an integer \(m\). They are proper state carriers of DOT with their own relation grammar and are not identified with operator carriers of standard arity.

In particular, rank 3 is $\mathcal P(J_3)$ as the state carrier of three coordinates, but not the space of Boolean operators of any standard arity.

---

# §8. The low ranks of the operator tower

## §8.1. Rank 0: constants

\[
\mathcal B_0=\{0,1\}^{Q_0},
\qquad
Q_0=\{\ast\}.
\]

It has 2 elements: the identically zero and the identically one functions. In the operator tower these are the poles — the two constants.

\[
\mathcal B_0\cong Q_1=\mathbb D.
\]

## §8.2. Rank 1: unary operators

\[
\mathcal B_1=\{0,1\}^{\mathbb D},
\qquad
|\mathcal B_1|=4.
\]

The four unary operators:
\[
0,\quad x,\quad \neg x,\quad 1.
\]

In the coordinate reading:
\[
\mathcal B_1\cong Q_2=\{00,01,10,11\}.
\]

The correspondence:
\[
0\leftrightarrow00,
\qquad
x\leftrightarrow01,
\qquad
\neg x\leftrightarrow10,
\qquad
1\leftrightarrow11.
\]

Here the coordinates $(f(0),f(1))$ are written as a pair of bits.

Layer decomposition:
\[
\mathcal B_1=S_0^{(2)}\sqcup S_1^{(2)}\sqcup S_2^{(2)},
\qquad
1+2+1.
\]

Connection with the core: $Q_2$ is constructed in the strict core §4. Here its operator reading as the space of unary Boolean operators is added.

## §8.3. The punctured operator carrier of rank 1

\[
\mathcal B_1^\circ=\mathcal B_1\setminus\{0,1\}=\{x,\neg x\}\cong Q_2\setminus\{00,11\}.
\]

These are the two nontrivial unary operators. On $\mathcal B_1^\circ$ the map $\nu\mapsto\nu\cdot\nu$ acts: the composition $x\leftrightarrow\neg x$ by output negation (see §10).

---

# §9. Rank 4 in the operator reading

## §9.1. The carrier $\mathcal B_2$

\[
\mathcal B_2=\{0,1\}^{Q_2}\cong\mathcal P(Q_2)\cong Q_4,
\]
\[
|\mathcal B_2|=16.
\]

Each binary operator $f:Q_2\to\{0,1\}$ is determined by its truth table on 4 inputs. Via $\operatorname{supp}$ this is identified with a subset of $Q_2$.

## §9.2. Decomposition into layers

\[
\mathcal B_2=S_0^{(4)}\sqcup S_1^{(4)}\sqcup S_2^{(4)}\sqcup S_3^{(4)}\sqcup S_4^{(4)},
\]
\[
1+4+6+4+1.
\]

## §9.3. The punctured operator carrier of rank 2

\[
\mathcal B_2^\circ=\mathcal B_2\setminus\{0_{\mathcal B},1_{\mathcal B}\}\cong Q_4\setminus\{0000,1111\}.
\]

\[
|\mathcal B_2^\circ|=14.
\]

## §9.4. The distinction between the two "rank 4"s

In the strict core "rank 4" is the **methodological carrier** $Q_4^*=\mathbb F_2^4\setminus\{0000\}$, 15 elements indexed by the principles $P_1,\ldots,P_{15}$ (`TNR_Stratification_Protocol`, §3.5).

In the operator reading "rank 4" is the **operator carrier** $\mathcal B_2^\circ=Q_4\setminus\{0000,1111\}$, 14 elements: 14 nontrivial binary Boolean operators (the two constants removed as the poles of the operator tower).

The structural distinction:
\[
Q_4^*=Q_4\setminus\{0000\}:\ 15\text{ elements},
\]
\[
\mathcal B_2^\circ=Q_4\setminus\{0000,1111\}:\ 14\text{ elements}.
\]

The methodological carrier removes one pole. The operator carrier removes both poles. They occupy different subsets of the same $Q_4$.

In this document "rank 4" in the operator reading means $\mathcal B_2^\circ$; "rank 4" in the methodological reading of the strict core means $Q_4^*$. These two scenes have one ambient \(Q_4\), but different subcarriers.

## §9.5. The middle layer $S_2^{(4)}$

\[
|S_2^{(4)}|=6.
\]

The six balanced binary operators (weight 2 in the truth table):
\[
x,\quad \neg x,\quad y,\quad \neg y,\quad x\oplus y,\quad \neg(x\oplus y).
\]

The tables (inputs $00,01,10,11$):
\[
\begin{array}{lccccc}
x:&0&0&1&1\\
\neg x:&1&1&0&0\\
y:&0&1&0&1\\
\neg y:&1&0&1&0\\
x\oplus y:&0&1&1&0\\
\neg(x\oplus y):&1&0&0&1
\end{array}
\]

## §9.6. Complement pairs on \(S_2^{(4)}\)

The triple of complement pairs by output negation:
\[
\{x,\neg x\},
\qquad
\{y,\neg y\},
\qquad
\{x\oplus y,\neg(x\oplus y)\}.
\]

In the coordinate tables these pairs have Hamming distance $4$ (full antipodality).

## §9.7. The graph $(S_2^{(4)},R_2)$

**Proposition 9.1.**
\[
(S_2^{(4)},R_2)\cong K_{2,2,2}.
\]

**Verification.** Hamming distances between all pairs of the six operators:
- complement pairs: distance 4 (not in $R_2$);
- all other pairs: distance 2 (in $R_2$).

For example: $d(x,y)=d(0011,0101)=2$, $d(x,\neg y)=d(0011,1010)=2$, $d(x,x\oplus y)=d(0011,0110)=2$, $d(x,\neg(x\oplus y))=d(0011,1001)=2$. The same is checked for $\neg x$ and $y$.

$R_2$ is the complete graph $K_6$ minus the 3 edges of the complement pairs. This is exactly $K_{2,2,2}$. $\square$

## §9.8. Agreement with rank 3

Connection with the core: $K_{2,2,2}$ arose in the strict core §7 as the octahedral shell on $X_{\mathrm{adm}}$. Here the same graph arose on $S_2^{(4)}\subset\mathcal B_2$. These are two different carriers with one and the same graph structure:
\[
X_{\mathrm{adm}}\subset Q_3:\ 6\text{ admissible coordinates},
\]
\[
S_2^{(4)}\subset\mathcal B_2:\ 6\text{ balanced binary operators}.
\]

Both carry $K_{2,2,2}$, but these are different proper scenes: the first is the rank-3 state carrier; the second is the middle layer of the rank-4 operator carrier.

---

# §10. The Klein four-group of involutions

## §10.1. Output negation $C_{\mathrm{out}}$

For $f\in\mathcal B_J$:
\[
C_{\mathrm{out}}(f)=\neg f,
\]
that is, $(C_{\mathrm{out}}f)(B)=1-f(B)$.

In terms of supp: $C_{\mathrm{out}}(U)=\mathcal P(J)\setminus U=\kappa_{\mathcal P(J)}(U)$.

That is, $C_{\mathrm{out}}=\kappa$ at the second level $\mathcal P(\mathcal P(J))$.

## §10.2. The action of $C_{\mathrm{out}}$ on layers

\[
C_{\mathrm{out}}:S_k^{(2^m)}\to S_{2^m-k}^{(2^m)}.
\]

For $m=3$ ($\mathcal B_3\cong Q_8$):
\[
S_k^{(8)}\leftrightarrow S_{8-k}^{(8)}.
\]

## §10.3. Input complement $C_{\mathrm{in}}$

For $f\in\mathcal B_J$:
\[
(C_{\mathrm{in}}f)(B)=f(\kappa_J(B)).
\]

In terms of supp: $C_{\mathrm{in}}(U)=\kappa_J[U]=\{\kappa_J(A):A\in U\}$.

That is, $C_{\mathrm{in}}$ is the induced action of $\kappa_J$ on $\mathcal B_J$ via $\mathcal Q(\kappa_J)$.

## §10.4. The action of $C_{\mathrm{in}}$ on layers

**Proposition 10.1.** $C_{\mathrm{in}}$ preserves weight:
\[
C_{\mathrm{in}}:S_k^{(2^m)}\to S_k^{(2^m)}.
\]

**Verification.** $\kappa_J$ is a bijection $\mathcal P(J)\to\mathcal P(J)$. Therefore $|\kappa_J[U]|=|U|$. $\square$

## §10.5. Commutativity

**Proposition 10.2.**
\[
C_{\mathrm{out}}\circ C_{\mathrm{in}}=C_{\mathrm{in}}\circ C_{\mathrm{out}}.
\]

**Verification.**
\[
(C_{\mathrm{out}}(C_{\mathrm{in}}f))(B)=1-f(\kappa_J(B)),
\]
\[
(C_{\mathrm{in}}(C_{\mathrm{out}}f))(B)=(C_{\mathrm{out}}f)(\kappa_J(B))=1-f(\kappa_J(B)).
\]
Equality. $\square$

## §10.6. The Klein four-group

**Definition 10.3.** The group $G_{\mathrm{B}}=\langle C_{\mathrm{out}},C_{\mathrm{in}}\rangle$ has 4 elements:
\[
\mathrm{id},
\quad
C_{\mathrm{out}},
\quad
C_{\mathrm{in}},
\quad
C_{\mathrm{out}}\circ C_{\mathrm{in}}.
\]

**Proposition 10.4.**
\[
G_{\mathrm{B}}\cong\mathbb Z_2\times\mathbb Z_2.
\]

**Verification.** $C_{\mathrm{out}}^2=C_{\mathrm{in}}^2=\mathrm{id}$. Commutativity by 10.2. The four elements are distinct: $C_{\mathrm{out}}\neq C_{\mathrm{in}}$ (the first changes the layer, the second does not). $\square$

## §10.7. Naturality of $C_{\mathrm{out}}, C_{\mathrm{in}}$

**Proposition 10.5.** The families $C_{\mathrm{out}}^J, C_{\mathrm{in}}^J$ are natural transformations $\mathcal B\Rightarrow\mathcal B$:
\[
\mathcal B(\sigma)\circ C_{\mathrm{out}}^J=C_{\mathrm{out}}^K\circ\mathcal B(\sigma),
\]
\[
\mathcal B(\sigma)\circ C_{\mathrm{in}}^J=C_{\mathrm{in}}^K\circ\mathcal B(\sigma).
\]

**Verification for $C_{\mathrm{out}}$.** $C_{\mathrm{out}}^J(U)=\kappa_{\mathcal P(J)}(U)$. The naturality of $\kappa$ by 5.4 at the level of $\mathcal P(J)$ gives $\mathcal Q(\mathcal Q(\sigma))(\kappa_{\mathcal P(J)}(U))=\kappa_{\mathcal P(K)}(\mathcal Q(\mathcal Q(\sigma))(U))$, that is, $\mathcal B(\sigma)(C_{\mathrm{out}}^J U)=C_{\mathrm{out}}^K(\mathcal B(\sigma)U)$. $\square$

**Verification for $C_{\mathrm{in}}$.** $C_{\mathrm{in}}^J(U)=\kappa_J[U]$. For $\sigma:J\to K$:
\[
\mathcal B(\sigma)(C_{\mathrm{in}}^J U)=\mathcal Q(\sigma)[\kappa_J[U]]=(\sigma\circ\kappa_J)[U],
\]
\[
C_{\mathrm{in}}^K(\mathcal B(\sigma)U)=\kappa_K[\mathcal Q(\sigma)[U]]=(\kappa_K\circ\sigma)[U].
\]
By the naturality of $\kappa$: $\sigma\circ\kappa_J=\kappa_K\circ\sigma$. Equality. $\square$

Therefore the entire Klein four-group $G_{\mathrm{B}}$ is the group of natural automorphisms of the functor $\mathcal B$.

---

# §11. The subgroups of $G_{\mathrm{B}}$ and their fixed sets

## §11.1. The three proper subgroups of order 2

\[
H_{\mathrm{out}}=\langle C_{\mathrm{out}}\rangle,
\qquad
H_{\mathrm{in}}=\langle C_{\mathrm{in}}\rangle,
\qquad
H_{\mathrm{diag}}=\langle C_{\mathrm{out}}\circ C_{\mathrm{in}}\rangle.
\]

## §11.2. Fixed sets of $H_{\mathrm{in}}$: input-invariant functions

\[
\operatorname{Inv}_m=\{f\in\mathcal B_m:C_{\mathrm{in}}f=f\}=\{f:f(\bar x)=f(x)\}.
\]

Such an $f$ is constant on input-complement pairs. The number of input pairs is $2^{m-1}$. Therefore
\[
|\operatorname{Inv}_m|=2^{2^{m-1}}.
\]

For $m=3$: $|\operatorname{Inv}_3|=2^4=16$.

## §11.3. Fixed sets of $H_{\mathrm{diag}}$: self-dual functions

\[
\operatorname{SD}_m=\{f\in\mathcal B_m:C_{\mathrm{out}}C_{\mathrm{in}}f=f\}=\{f:f(\bar x)=\neg f(x)\}.
\]

Such an $f$ takes opposite values on input-complement pairs. On each pair exactly one value in $\{0,1\}$ is chosen. The number of pairs is $2^{m-1}$. Therefore
\[
|\operatorname{SD}_m|=2^{2^{m-1}}.
\]

For $m=3$: $|\operatorname{SD}_3|=2^4=16$.

## §11.4. Fixed sets of $H_{\mathrm{out}}$: empty on nontrivial functions

\[
\{f:C_{\mathrm{out}}f=f\}=\{f:\neg f=f\}=\varnothing.
\]

Since $\neg f=f$ means $f(B)=\neg f(B)$ for every $B$, which is impossible. Therefore the subgroup $H_{\mathrm{out}}$ has no fixed points on $\mathcal B_m$.

## §11.5. Summary table of fixed sets

| Subgroup | Condition | Proper series |
|---|---|---|
| $H_{\mathrm{in}}$ | $f(\bar x)=f(x)$ | $\operatorname{Inv}_m$ |
| $H_{\mathrm{diag}}$ | $f(\bar x)=\neg f(x)$ | $\operatorname{SD}_m$ |
| $H_{\mathrm{out}}$ | $f=\neg f$ | $\varnothing$ |

## §11.6. Naturality of the subcarriers

**Proposition 11.1.** $\operatorname{Inv}_m$ and $\operatorname{SD}_m$ are natural subfunctors of $\mathcal B$.

**Verification.** By 10.7 the action of $G_{\mathrm{B}}$ is natural. A natural action commutes with $\mathcal B(\sigma)$. Therefore the fixed sets of each subgroup map to the fixed sets of the same subgroup. $\square$

## §11.7. Self-duality and balance

**Proposition 11.2.** $\operatorname{SD}_m\subset S_{2^{m-1}}^{(2^m)}$.

**Verification.** For $f\in\operatorname{SD}_m$, on each pair $\{x,\bar x\}\subset Q_m$ one of the values equals 1 and the other 0. Therefore there are exactly $2^{m-1}$ ones in the truth table, that is, weight $2^{m-1}$. $\square$

Therefore for $m=3$:
\[
\operatorname{SD}_3\subset S_4^{(8)}.
\]

---

# §12. The affine subcarrier of rank 8

## §12.1. Affine Boolean functions

For $f:\mathbb F_2^m\to\mathbb F_2$:
\[
f\text{ is affine}
\quad\Longleftrightarrow\quad
f(x)=a\cdot x+b,
\quad
a\in\mathbb F_2^m,
\quad
b\in\mathbb F_2.
\]

Here $a\cdot x=a_1x_1+\cdots+a_mx_m$ in $\mathbb F_2$.

The parameters: $|\mathbb F_2^m|\cdot|\mathbb F_2|=2^{m+1}$. Therefore
\[
|\operatorname{Aff}_m|=2^{m+1}.
\]

For $m=3$: $|\operatorname{Aff}_3|=16$.

## §12.2. The layer distribution of affine functions

**Proposition 12.1.** For $m\geq 1$:
- $a=0,b=0$: $f\equiv 0$, weight 0;
- $a=0,b=1$: $f\equiv 1$, weight $2^m$;
- $a\neq 0$: $\{x:a\cdot x=0\}$ is a hyperplane of dimension $m-1$, of cardinality $2^{m-1}$; therefore the weight of $f$ equals either $2^{m-1}$ (for $b=0$) or $2^{m-1}$ (for $b=1$ — the complement is taken).

**Verification.** For $a\neq 0$ the form $x\mapsto a\cdot x$ is a nontrivial linear functional on $\mathbb F_2^m$, its kernel has codimension 1. The values $0$ and $1$ are taken on sets of equal cardinality $2^{m-1}$. $\square$

For $m=3$: 2 constants (weight 0 and 8), the remaining 14 have weight 4. Therefore
\[
\operatorname{Aff}_3^\circ:=\operatorname{Aff}_3\setminus\{0,1\}\subset S_4^{(8)},
\]
\[
|\operatorname{Aff}_3^\circ|=14.
\]

## §12.3. Structural coincidence with operator rank 4

The parameters of an affine function form $\mathbb F_2^{m+1}$. Therefore
\[
\operatorname{Aff}_m\cong\mathbb F_2^{m+1}\cong Q_{m+1}.
\]

For $m=3$:
\[
\operatorname{Aff}_3\cong Q_4,
\qquad
\operatorname{Aff}_3^\circ\cong Q_4\setminus\{0000,1111\}=\mathcal B_2^\circ.
\]

That is, the affine subcarrier of rank 8 as a set coincides structurally with the operator carrier of rank 4 (without the poles).

This is a concrete realization of one and the same 14-element $\mathcal B_2^\circ$ inside two different carriers:
\[
\mathcal B_2^\circ\subset\mathcal B_2\cong Q_4,
\]
\[
\operatorname{Aff}_3^\circ\subset\mathcal B_3\cong Q_8.
\]

## §12.4. Affinity and the choice of coordinates

\(\operatorname{Aff}_m\) is a proper subcarrier of \(\mathcal B_m\), singled out by the structure of \(\mathbb F_2\)-affinity on \(\mathcal P(J_m)=\mathbb F_2^m\). It is not a subfunctor of \(\mathcal B\) under all bijections, because a bijection \(\sigma\) need not be \(\mathbb F_2\)-linear. After a coordinate linear structure is chosen, \(\operatorname{Aff}_m\) is well defined.

---

# §13. The balanced layer of rank 8 and the central cross-polytope

## §13.1. The carrier $\mathcal B_3$

\[
\mathcal B_3=\{0,1\}^{Q_3}\cong Q_8,
\qquad
|\mathcal B_3|=256.
\]

After puncturing:
\[
\mathcal B_3^\circ=\mathcal B_3\setminus\{0,1\},
\qquad
|\mathcal B_3^\circ|=254.
\]

## §13.2. Layers

\[
\mathcal B_3=\bigsqcup_{k=0}^{8}S_k^{(8)},
\]
\[
1+8+28+56+70+56+28+8+1=256.
\]

All numbers are the binomials $\binom{8}{k}$.

## §13.3. The central layer

\[
|S_4^{(8)}|=\binom{8}{4}=70.
\]

This is the layer of balanced ternary functions.

## §13.4. The $C_{\mathrm{out}}$ pairs in $S_4^{(8)}$

$C_{\mathrm{out}}$ swaps $S_k^{(8)}$ and $S_{8-k}^{(8)}$. On $S_4^{(8)}$ it stabilizes the layer and acts as the complement involution. There are no fixed points of $C_{\mathrm{out}}$ in $S_4^{(8)}$ (by 11.4).

Therefore $C_{\mathrm{out}}$ partitions $S_4^{(8)}$ into 35 complement pairs:
\[
\text{number of pairs}=\frac{70}{2}=35.
\]

The Hamming distance within a pair: $|f\triangle\neg f|=8$ (full antipodality).

## §13.5. The graph $S_4^{(8)}$ minus the complement pairs

Consider the graph $H_{35}$ on the 70 vertices $S_4^{(8)}$: an edge between $f$ and $g$ if $f\neq g$ and $g\neq\neg f$.

Then $H_{35}$ is $K_{70}$ minus a perfect matching of 35 edges. This is the **cocktail-party graph** on 70 vertices:
\[
H_{35}\cong K_{35\times 2}.
\]

## §13.6. The cross-polytope

$K_{35\times 2}$ is the 1-skeleton of the 35-dimensional cross-polytope. This is the **central cross-polytope of rank 8**.

Connection with the core: for $m=2$ the analogous graph on $S_2^{(4)}$ (6 vertices minus 3 complement pairs) is the octahedral $K_{2,2,2}=K_{3\times 2}$ — the 1-skeleton of the 3-dimensional cross-polytope.

The generalization law:
\[
\text{for }m\geq 2:\quad
(S_{2^{m-1}}^{(2^m)}\setminus\text{complement pairs})\cong K_{(2^{m-1}\binom{2^m}{2^{m-1}}/2^{m})\times 2}
\]
— the $1$-skeleton of the $(|S_{2^{m-1}}^{(2^m)}|/2)$-dimensional cross-polytope.

For small $m$:
\[
m=2:\ |S_2^{(4)}|/2=3,\quad K_{3\times 2}=K_{2,2,2},
\]
\[
m=3:\ |S_4^{(8)}|/2=35,\quad K_{35\times 2}.
\]

---

# §14. The third octahedron and its bijection with the rank-3 axes

## §14.1. The input-complement pairs in \(Q_3\)

The orbits of $\kappa_3$ on $Q_3$ are the 4 pairs:
\[
p_0=\{000,111\},
\quad
p_1=\{001,110\},
\quad
p_2=\{010,101\},
\quad
p_3=\{011,100\}.
\]

Connection with the core: \(p_1,p_2,p_3\) coincide with the complement pairs \(\beta_1,\beta_2,\beta_3\) from the strict core §7. The pair \(p_0\) is the removed pole pair of totality \(\{000,111\}\), absent from \(X_{\mathrm{adm}}\).

## §14.2. Balanced input-invariant functions

By 11.2: $\operatorname{Inv}_3=\{f:f(\bar x)=f(x)\}$, $|\operatorname{Inv}_3|=16$.

The balanced elements (in $S_4^{(8)}$): a function $f\in\operatorname{Inv}_3$ chooses a value $f|_{p_i}\in\{0,1\}$ for each $i\in\{0,1,2,3\}$. Since $f$ is balanced (weight 4), and each $p_i$ contributes 2 to the weight, exactly 2 of the 4 orbits must be set to 1.

**Proposition 14.1.**
\[
|\operatorname{Inv}_3\cap S_4^{(8)}|=\binom{4}{2}=6.
\]

**Verification.** A balanced input-invariant function is determined by a choice of 2 of the 4 orbits. $\square$

## §14.3. The graph of these 6 functions

Let $f_S$ be the function that chose the orbits from a subset $S\subset\{p_0,p_1,p_2,p_3\}$, $|S|=2$.

**Proposition 14.2.** The Hamming distance:
\[
|f_S\triangle f_T|=4\cdot|S\triangle T|.
\]

**Verification.** Each orbit $p_i$ has 2 inputs. On an orbit where $f_S$ and $f_T$ agree, the contribution to $f_S\triangle f_T$ equals 0. On an orbit where they differ, the contribution equals 2.

The orbits differ on $p_i\in S\triangle T$. Therefore $|f_S\triangle f_T|=2\cdot|S\triangle T|$. 

Correction: $|S\triangle T|\in\{0,2,4\}$ for $|S|=|T|=2$. For $|S\triangle T|=0$: $f_S=f_T$. For $|S\triangle T|=2$: $|f_S\triangle f_T|=4$. For $|S\triangle T|=4$: $|f_S\triangle f_T|=8$ (complement). $\square$

## §14.4. The graph $K_{2,2,2}$ on the 6 functions

**Proposition 14.3.**
\[
(\operatorname{Inv}_3\cap S_4^{(8)},\ \text{edge at distance }4)\cong K_{2,2,2}.
\]

**Verification.** Six vertices = the 6 two-element subsets of \(\{p_0,p_1,p_2,p_3\}\). The complement pairs (distance \(8\)) are the partitions of \(4\) into \(2+2\), of which there are \(3\):
\[
\{p_0,p_1\}\mid\{p_2,p_3\},
\qquad
\{p_0,p_2\}\mid\{p_1,p_3\},
\qquad
\{p_0,p_3\}\mid\{p_1,p_2\}.
\]

The remaining 12 pairs have distance 4 and form the edges. This is $K_6$ minus the 3 edges of the matching, that is, $K_{2,2,2}$. $\square$

## §14.5. The bijection with the rank-3 axes

**Proposition 14.4.** Each of the 3 partitions of $\{p_0,p_1,p_2,p_3\}$ into 2+2 includes $p_0$ in one of the two pairs. The bijection:
\[
\beta_i\;\longleftrightarrow\;
\text{the partition in which }p_0\text{ is paired with }p_i.
\]

Explicitly:
\[
\beta_1\;\longleftrightarrow\;\{p_0,p_1\}\mid\{p_2,p_3\},
\]
\[
\beta_2\;\longleftrightarrow\;\{p_0,p_2\}\mid\{p_1,p_3\},
\]
\[
\beta_3\;\longleftrightarrow\;\{p_0,p_3\}\mid\{p_1,p_2\}.
\]

**Verification of correctness.** $\beta_i=p_i$ for $i=1,2,3$ by §14.1. Each partition is determined by which $p_i$ is grouped with $p_0$. This gives a bijection $\{p_1,p_2,p_3\}\to\{\text{partitions}\}$, that is, $\{\beta_1,\beta_2,\beta_3\}\to\{\text{partitions}\}$. $\square$

## §14.6. The substantive meaning of the bijection

The third octahedral shell in $\operatorname{Inv}_3\cap S_4^{(8)}$ structurally repeats the octahedral shell $X_{\mathrm{adm}}$:
- the three axis-partitions of the third octahedron correspond to the three complement pairs $\beta_i$ of rank 3 through the choice of a "partner" for $p_0=\{000,111\}$;
- the pole pair $\{000,111\}$, removed in the strict core, returns upon lifting into the operator tower as a structuring element of the third octahedron.

Therefore the octahedral law of rank 3 does not disappear upon lifting the arity to 3, but becomes an inner subcarrier of the balanced layer of rank 8.

---

# §15. The three appearances of the octahedron as realizations of a single law

## §15.1. The general octahedral law

**Law (general form).** Let $V$ be a carrier with an involution $\iota:V\to V$ of order 2, having exactly 3 fixed orbits of size 2 and no fixed points. Then the graph $(V,\text{edge when }\iota(v)\neq w)$ is isomorphic to $K_{2,2,2}$.

This is the abstract description of the octahedral shell.

## §15.2. The three realizations

**Realization I — strict core, rank 3.**
\[
V=X_{\mathrm{adm}},
\qquad
\iota=\kappa_3|_{X_{\mathrm{adm}}}.
\]
Three orbits: $\beta_1,\beta_2,\beta_3$. The graph $R_{12}=R_1\cup R_2\cong K_{2,2,2}$. Proper in the strict core §7.

**Realization II — operator rank 4.**
\[
V=S_2^{(4)},
\qquad
\iota=C_{\mathrm{out}}|_{S_2^{(4)}}.
\]
Three orbits: $\{x,\neg x\},\{y,\neg y\},\{x\oplus y,\neg(x\oplus y)\}$. The graph $R_2\cong K_{2,2,2}$. Bridge §9.7.

**Realization III — operator rank 8.**
\[
V=\operatorname{Inv}_3\cap S_4^{(8)},
\qquad
\iota=C_{\mathrm{out}}|_V.
\]
Three orbits are determined by the partitions of $\{p_0,p_1,p_2,p_3\}$ into 2+2. The graph $\cong K_{2,2,2}$. Bridge §14.

## §15.3. Summary table

| Realization | Carrier | Involution | Size | Source |
|---|---|---|---|---|
| I | $X_{\mathrm{adm}}\subset Q_3$ | $\kappa_3$ | 6 | strict core, §7 |
| II | $S_2^{(4)}\subset\mathcal B_2$ | $C_{\mathrm{out}}$ | 6 | this bridge, §9 |
| III | $\operatorname{Inv}_3\cap S_4^{(8)}\subset\mathcal B_3$ | $C_{\mathrm{out}}$ | 6 | this bridge, §14 |

All three carry one octahedral graph isomorphism. The substantive distinctness is preserved: the first is the admissible state carrier; the second is the middle layer of the rank-4 operator carrier; the third is the intersection of the fixed set of $H_{\mathrm{in}}$ with the middle layer of $\mathcal B_3$.

---

# §16. The structural ladder

## §16.1. The full ladder of the operator tower

\[
\mathbb D=\mathbb F_2
\]
\[
\downarrow\quad \nu=\text{coordinate reading of }\tau
\]
\[
\mathcal B_0\cong Q_1\quad\text{(constants)}
\]
\[
\downarrow\quad \text{unary lift}
\]
\[
\mathcal B_1\cong Q_2\quad\text{(unary operators)}
\]
\[
\downarrow\quad \text{binary lift}
\]
\[
\mathcal B_2\cong Q_4\quad\text{(binary operators)}
\]
\[
\downarrow\quad \text{ternary lift}
\]
\[
\mathcal B_3\cong Q_8\quad\text{(ternary operators)}.
\]

## §16.2. Operator ranks and state ranks

The state ranks of DOT (`TNR_Stratification_Protocol`): $1,2,3,4,5,\ldots$ Each receives its own proper carrier $Q_n^*$ and its own relation grammar.

The operator ranks (this bridge): $1,2,4,8,16,\ldots=2^m$. The operator carrier $\mathcal B_m\cong Q_{2^m}$ arises on those state ranks that are powers of two.

Ranks 3, 5, 6, 7 have only the state reading, without an operator superstructure of standard arity.

## §16.3. The double layer of rank 4

At rank 4 two scenes coexist in one \(Q_4\):
- the methodological carrier of the strict core: \(Q_4^*\), 15 elements \(P_1,\ldots,P_{15}\);
- the operator carrier of this bridge: \(\mathcal B_2^\circ\), 14 elements as binary Boolean operators without constants.

These two subsets of \(Q_4\) have the common part \(Q_4\setminus\{0000,1111\}\) of \(14\) elements and differ by the inclusion of the point \(1111\), which in the strict core falls into \(P_{15}\) (saturation), and in this bridge drops out as the second pole.

## §16.4. The octahedral law and the tower

The octahedral law manifests at three ranks of the tower:
\[
\text{rank 3 (states, strict core)},
\qquad
\text{rank 4 (operator reading)},
\qquad
\text{rank 8 (inner subcarrier)}.
\]

Each appearance is associated with an involution of order 2 and three fixed complement pairs.

---

# §17. Boundaries of the reading

In this document the names \(e_1,e_2,e_3\) are used as neutral coordinate labels. The names \(D,F,C\) are not used for coordinates, so as not to mix the operator tower with the axial semantic layer.

The words "octahedron" and "cross-polytope" in this bridge mean a finite graph type. No topological or metric embeddings of these objects are introduced here.

The three appearances of the graph \(K_{2,2,2}\) are not identified as sets:

\[
X_{\mathrm{adm}},
\qquad
S_2^{(4)}\subset\mathcal B_2,
\qquad
\operatorname{Inv}_3\cap S_4^{(8)}\subset\mathcal B_3.
\]

They have one graph form, but different roles: the rank-\(3\) state carrier, the middle layer of binary operators, and the inner subcarrier of the central layer of ternary operators.

Likewise \(\operatorname{Aff}_3^\circ\) and \(\mathcal B_2^\circ\) are not identified. Both carriers have \(14\) elements and are coordinate-isomorphic to \(Q_4\setminus\{0000,1111\}\), but the first is an affine subcarrier inside \(\mathcal B_3\), and the second is the operator carrier of the binary level.

---

# §18. Summary

In this bridge three levels of the operator reading over the strict core of DOT are fixed.

**First level.** The power-set carrier \(Q_J=\mathcal P(J)\) with the Hamming relation \(R_d^J(A,B)\iff|A\triangle B|=d\) functorially generalizes the relation grammar of the strict core §6 to an arbitrary finite \(J\). At rank \(3\) this functor gives the punctured Boolean carrier \(X_3\cong X_{\mathrm{adm}}\), and the Boolean operations \(\cap,\cup,\neg,\oplus\) arise as a reading from which the proper relations \(R_1,R_2,R_3\) are recovered.

**Second level.** The operator functor $\mathcal B=\mathcal Q\circ\mathcal Q$ gives the ladder
\[
\mathcal B_0\cong Q_1,\quad
\mathcal B_1\cong Q_2,\quad
\mathcal B_2\cong Q_4,\quad
\mathcal B_3\cong Q_8,\ldots
\]
The Klein four-group $G_{\mathrm{B}}=\langle C_{\mathrm{out}},C_{\mathrm{in}}\rangle$ acts on each floor as the group of natural automorphisms. Its three proper subgroups of order 2 yield three series of natural subcarriers: $\operatorname{Inv}_m$ (the fixed set of $C_{\mathrm{in}}$), $\operatorname{SD}_m$ (the fixed set of $C_{\mathrm{out}}C_{\mathrm{in}}$), and the empty fixed set of $C_{\mathrm{out}}$. The subgroup $H_{\mathrm{out}}$ is free — it generates the complement pairs on each layer.

**Third level.** At rank 8 the central layer $S_4^{(8)}$ has 70 balanced functions, 35 complement pairs, and the cocktail-party graph $K_{35\times 2}$ as the 1-skeleton of the 35-dimensional cross-polytope. Inside $S_4^{(8)}$ are located $\operatorname{Aff}_3^\circ\cong\mathcal B_2^\circ\cong Q_4\setminus\{0,1\}$ (the affine subcarrier, 14 elements), $\operatorname{SD}_3$ (the self-dual functions, 16 elements), $\operatorname{Inv}_3$ (the input-invariant functions, 16 elements), and the intersection $\operatorname{Inv}_3\cap S_4^{(8)}$ of 6 functions forming $K_{2,2,2}$.

**The octahedral law.** \(K_{2,2,2}\) arises as the graph "\(V\) with an involution of order \(2\) having \(3\) fixed pairs" whenever such a structure is given. The three realizations:
\[
X_{\mathrm{adm}}\ \text{with}\ \kappa_3,
\qquad
S_2^{(4)}\ \text{with}\ C_{\mathrm{out}},
\qquad
\operatorname{Inv}_3\cap S_4^{(8)}\ \text{with}\ C_{\mathrm{out}}
\]
are three manifestations of a single functorial law. The bijection between the third octahedron and the rank-\(3\) axes is written out via the partitions of the four input-complement orbits \(\{p_0,p_1,p_2,p_3\}\) into \(2+2\) with the partner for \(p_0=\{000,111\}\) fixed.
