# Appendix. Ontogenesis atlas of mathematical languages: a functorial derivation

## Introduction

In Volumes 0–9 the theory proceeds by rank: one primitive of distinction generates the
carrier $Q_n$, the active scene $U_n$, the complement $\kappa$, and over them the vertical
$\mathfrak{sl}_2$, the rotation, the projective quotient. At each rank **known mathematical
structures** show through: the Boolean lattice, finite projective geometry, Johnson and
Kneser graphs, finite groups, chain complexes. A natural question arises: is this a set of
separate coincidences — or **one structure unfolding by one law**?

This appendix shows the second, and shows it **rigorously**. The claim proved below:

> The rank ladder is the **orbit of one generating endofunctor** (the lift) on a category
> of finite carriers; each "mathematical language" at rank $n$ is the value of a **standard
> functor** evaluated at the $n$-th member of the orbit; and the uniformity of the closed
> forms (and hence the existence of a generator computing any cell) is the **expression of
> functoriality**.

This is **not** a claim that DOT derives all of mathematics, and **not** a new result of
category theory. The functors and adjunctions used are classical; the contribution of the
appendix is to **define them explicitly** on the DOT carriers and to **derive** that the
atlas is their joint orbit. Thus "the automation of standard formulas" gets its reason: the
formulas are uniform because the objects are values of functors natural in the rank.

Each statement is marked: **[Def.]** definition, **[Claim]/[Pf.]** statement with proof,
**[comp.]** checked computationally (`_TNR_Research/verify_categorical_backbone.py`,
`ontogenesis_generator.py`). Scope: everything is finite; the continuous enters as an avatar
(§8). The horizon is rank 33 (§9).

---

## 1. The base category and the carrier functor

**[Def. 1.1] The category `FI`.** Objects — finite sets $[n]=\{1,\dots,n\}$; morphisms —
**injections**. Then $\operatorname{Aut}([n])=S_n$ (the coordinate symmetry), and the
inclusions $\iota_n:[n]\hookrightarrow[n+1]$ give the rank lift. (`FI` is the standard
Church–Ellenberg–Farb category.)

**[Def. 1.2] The carrier functor $Q$.** On objects
$$Q([n])\;=\;\mathcal P([n])\;\cong\;\mathbb F_2^{\,n}\;=\;Q_n.$$
On morphisms: an injection $f:[m]\hookrightarrow[n]$ is sent to the push-forward of subsets
$$Q(f):Q_m\to Q_n,\qquad A\mapsto f(A).$$

**[Claim 1.3] $Q$ is a functor.** *Pf.* $Q(\mathrm{id})=\mathrm{id}$ trivially; for
$f:[m]\!\hookrightarrow\![k]$, $g:[k]\!\hookrightarrow\![n]$ the push-forward satisfies
$g(f(A))=(g\circ f)(A)$, hence $Q(g)\circ Q(f)=Q(g\circ f)$. ∎ Linearly $Q(f)$ is the
coordinate inclusion $\mathbb F_2^m\hookrightarrow\mathbb F_2^n$.

**[Def. 1.4] Complement, active scene.** $\kappa_n:Q_n\to Q_n$, $\kappa_n(A)=[n]\setminus A$
($\kappa^2=\mathrm{id}$); poles $\{\varnothing,[n]\}$; active scene
$U_n=Q_n\setminus\{\varnothing,[n]\}$, $|U_n|=2^n-2$. Axis quotient $U_n/\kappa$.

---

## 2. The lift as an endofunctor and the adjunction $\Lambda\dashv\pi$

**[Def. 2.1] The successor endofunctor $L$.** $L([n])=[n]\sqcup\{*\}=[n+1]$; on injections —
the extension fixing $*$. The orbit of the base object $\{L^n([0])\}=\{[n]\}$ is the rank
ladder.

**[Def. 2.2] Lift $\Lambda$ and projection $\pi$ (at the lattice level).**
$$\Lambda_n=Q(\iota_n):\;Q_n\hookrightarrow Q_{n+1}\quad(A\subseteq[n]\ \text{regarded as}\ \subseteq[n+1]);$$
$$\pi_n:\;Q_{n+1}\to Q_n,\qquad B\mapsto B\cap[n].$$

**[Claim 2.3 — adjunction] $\Lambda\dashv\pi$.** Viewing the lattices $Q_n,Q_{n+1}$ as
poset-categories,
$$\boxed{\;\Lambda_n(A)\subseteq B\quad\Longleftrightarrow\quad A\subseteq\pi_n(B)\;}\qquad(A\in Q_n,\;B\in Q_{n+1}).$$
*Pf.* $\Lambda_n(A)=A\subseteq[n]$. If $A\subseteq B$ then $A=A\cap[n]\subseteq B\cap[n]=\pi_n(B)$.
Conversely $A\subseteq\pi_n(B)=B\cap[n]\subseteq B$. ∎ This is a Galois connection (the
hom-order isomorphism $\mathrm{Hom}(\Lambda A,B)\cong\mathrm{Hom}(A,\pi B)$): **the lift is
left adjoint to the projection**. It is exactly the "multiplication$\dashv$division" pair of
Volume 3.

---

## 3. The inter-rank law as the lift's object action

**[Claim 3.1] $Q_n^{*}\cong U_{n+1}/\kappa$** (the nontrivial configurations of rank $n$ =
the axes of rank $n+1$). *Pf.* Define
$$\varphi:\;Q_n\setminus\{\varnothing\}\;\longrightarrow\;U_{n+1}/\kappa,\qquad A\mapsto\{\,A,\ \kappa_{n+1}(A)\,\},$$
where $A\subseteq[n]\subseteq[n+1]$ (the lift inclusion). Well-defined: $A\neq\varnothing$ and
$*\notin A$, so $A\neq\varnothing,[n+1]$, i.e. $A\in U_{n+1}$. Injective: $\{A,\kappa A\}=\{A',\kappa A'\}$
with $*\notin A,A'$ forces $A=A'$ (the case $A'=\kappa A\ni *$ is excluded). Count:
$|Q_n^{*}|=2^n-1$ equals the number of axes $|U_{n+1}/\kappa|=(2^{n+1}-2)/2=2^n-1$, so $\varphi$
is a bijection. ∎ [comp., $n=2..5$]. Thus $\Lambda$ carries configurations to the axes of the
next rank — the object action of the lift on the ladder.

**[Cor. 3.2]** $U_n/\kappa\cong PG(n-2,2)$: the quotient $\mathbb F_2^n/\langle 1^n\rangle\cong\mathbb F_2^{\,n-1}$,
its nonzero classes ($2^{n-1}-1$ of them) are the points of $PG(n-2,2)$; lines are the images
of 2-dimensional subspaces. [projectivization defined in §4.]

---

## 4. Languages as functors along the orbit

Each "language" is the value of a standard functor on $L^n([0])$; its naturality in $n$
(commutation with the lift) yields the closed form.

**[Def. 4.1] Projectivization and Grassmannian.** $\mathbb P(V)=(V\setminus0)/\mathbb F_2^{*}=V\setminus0$;
the functor $\mathrm{Gr}_k(V)=\{k\text{-dimensional subspaces of }V\}$. On the carrier:
$\mathbb P(\mathbb F_2^n/\langle1^n\rangle)=PG(n-2,2)$.

**[Claim 4.2 — subspace count] $|\mathrm{Gr}_k(\mathbb F_2^m)|=\binom{m}{k}_2$** (Gaussian
binomial), with the recursion
$$\boxed{\;\binom{m}{k}_q=q^{k}\binom{m-1}{k}_q+\binom{m-1}{k-1}_q\;}$$
*Pf.* The number of $k$-dimensional subspaces of $\mathbb F_q^m$ is
$\binom mk_q=\prod_{i=0}^{k-1}\frac{q^{m-i}-1}{q^{i+1}-1}$ (ordered independent tuples divided
by the number of bases of a subspace) — classical; the q-recursion (A) is a direct
consequence, **verified** [comp., $q=2,3$]. ∎ Points of $PG(n-2,2)$: $\binom{n-1}{1}_2=2^{n-1}-1$;
lines: $\binom{n-1}{2}_2$; etc. (values of the functor $\mathrm{Gr}_k$).

**[Def. 4.3] Chain complex.** The carrier $Q_n$ is the face lattice of the simplex $\Delta^{n-1}$;
the active $U_n$ is the faces of $\partial\Delta^{n-1}$. The boundary $\partial$ and coboundary
$\delta$ are the differentials ($\partial^2=0$, Volumes 3/7). The Euler characteristic is the
functor $\chi=\sum(-1)^{k-1}|S_k|$.

**[Claim 4.4] $\chi(\partial\Delta^{n-1})=1+(-1)^n=\chi(S^{n-2})$.** *Pf.*
$\sum_{k=0}^{n}(-1)^k\binom nk=0\Rightarrow\sum_{k=1}^{n-1}(-1)^{k-1}\binom nk=\binom n0+(-1)^n\binom nn=1+(-1)^n$. ∎
(The active scene is the face structure of the sphere $S^{n-2}$.)

**[Def. 4.5] Vertical (Schur–Weyl).** $Q_n=(\mathbb C^2)^{\otimes n}$ under $SU(2)\times S_n$;
$\mathfrak{sl}_2=\{\partial,\delta,H\}$ is the collective spin. Decomposition
$Q_n=\bigoplus_J V_J\otimes M_J$ (Volume 7).

**[Claim 4.6] $\dim\langle\mathfrak{sl}_2\rangle_n=\sum_J(\dim V_J)^2=\binom{n+3}{3}$.**
*Pf.* The image of the enveloping algebra $U(\mathfrak{sl}_2)$ is $\bigoplus_J\mathrm{End}(V_J)$
(over the distinct spins $J=\frac n2-k$, $k=0..\lfloor n/2\rfloor$), of dimension $\sum(2J+1)^2$.
This is a sum of squares of numbers of one parity $n+1,n-1,\dots$; by the sum-of-squares formula
(odd: $m(2m{-}1)(2m{+}1)/3$, even: $2m(m{+}1)(2m{+}1)/3$) it equals $\binom{n+3}{3}$. ∎
[comp., $n=2..8$: $20,35,56,84,120,165$].

**Naturality.** $\mathrm{Gr}_k,\ \chi,\ \mathrm{Aut},\ \bigoplus_J$ are functors; their
commutation with $\Lambda$ (§5) yields the recursions — which is why the formulas above are
uniform in $n$.

---

## 5. The development law = induction $\dashv$ restriction adjunction (Bratteli diagram)

**[Def. 5.1] The lift as a tensor functor.** The lift on the vertical is $-\otimes V_{1/2}$
(add a qubit); its adjoint is restriction $\mathrm{Res}$ (Frobenius reciprocity
$\mathrm{Ind}\dashv\mathrm{Res}$ of the tower $S_n\subset S_{n+1}$).

**[Claim 5.2 — branching] $V_J\otimes V_{1/2}=V_{J+1/2}\oplus V_{J-1/2}$** (Clebsch–Gordan).
*Pf.* the standard decomposition of a tensor with spin $\tfrac12$. ∎

**[Def. 5.3] Bratteli diagram.** Vertices $(n,J)$, edges $(n,J)\!\to\!(n{+}1,J\pm\tfrac12)$
(from 5.2). The multiplicity $m_J(n)=\dim M_J$ = **number of paths** from $(0,0)$ to $(n,J)$.

**[Claim 5.4] $m_J(n)=\binom{n}{k}-\binom{n}{k-1}=d_k$, $k=\tfrac n2-J$** (ballot number).
*Pf.* Paths of $\pm\tfrac12$ steps not going below zero; the reflection principle gives
$\binom nk-\binom n{k-1}$. ∎ [comp., $n=2..8$]. Thus the "branching of weight multiplets"
(Volume 7 §7.5) **is** the inductive structure of the tower, and $d_k$ are the dimensions of
the protected subsystems (DFS, see `10_Observer_Duality_Readings`).

---

## 6. The q-analog: one functor, two values

**[Def. 6.1] q-deformed count.** $\binom nk_q$ counts $k$-subsets (at $q=1$) and
$k$-subspaces of $\mathbb F_q^n$ (at $q$ a prime power), with the single recursion 4.2.

**[Claim 6.2] Simplex and projective are two values of one functor.**
$$U_n\ (\text{faces of }\partial\Delta^{n-1},\ \text{count }\tbinom nk=\tbinom nk_1)\quad\text{and}\quad U_n/\kappa=PG(n-2,2)\ (\text{subspaces},\ \tbinom{n-1}{k}_2)$$
are the values $q=1$ and $q=2$. *Pf.* the $q\to1$ limit of recursion 4.2 gives the ordinary
Pascal $\binom nk=\binom{n-1}k+\binom{n-1}{k-1}$, i.e. $\binom nk_1=\binom nk$. ∎ [comp.] The
atlas carries **both** combinatorics — set (simplex) and linear (projective) — as $q=1,2$ of
one q-functor (the "field with one element" motif).

---

## 7. The power-set functor tower

**[Claim 7.1] $B_m\cong Q_{2^m}$.** $Q=\mathcal P$ (the states functor), $B=Q\circ Q$;
Boolean functions of $m$ inputs are tables of length $2^m$, i.e. states of rank $2^m$:
$|B_m|=2^{2^m}=|Q_{2^m}|$ (Volume 7 §7). ∎ Self-application of the same functor gives the
operator floor.

---

## 8. The atlas as a function: the generator as functor evaluation

The closed forms of §1–§7 are values of the functors defined above. Hence **any cell is
computable from $n$**: `ontogenesis_generator.py` calls Gaussian binomials (4.2), Johnson/Kneser
(middle layer), quadric point counts, the orders $S_n,GL(n-1,2)$, the orbits $\{C(n,k)\}$, the
Euler $\chi$ (4.4), the Fermat test of the Singer order. **Validation:** the generator
reproduces the four independently hand-proved cells (ranks 3,4,5,6) — 7/7 — so its values at
ranks 7…33 are trustworthy consequences of the functors, not guesses.

**Continuous avatar.** $\partial\Delta^{n-1}\sim S^{n-2}$ (4.4) is the only native exit into
the continuous; smooth realizations (a circle from $C_n$, spheres) are avatars, not core.

---

## 9. Constructibility horizon — rank 33

The Singer order at the ladder ranks $n=2^{k+1}+1$ is $\prod_{j\le k}F_j=2^{2^{k+1}}-1$ (a
product of distinct Fermat primes); five of them are known ⇒ rank 33 is the last fully
constructible one ($F_5$ composite). This is the horizon of **constructibility of the
projective scene** (Gauss–Wantzel), not a boundary of mathematics. [comp.]

---

## 10. Honest scope and value

- **Derived here:** the functor $Q$ (1.3), the adjunction $\Lambda\dashv\pi$ (2.3), the
  inter-rank law (3.1), the subspace count (4.2), $\chi$ (4.4),
  $\dim\langle\mathfrak{sl}_2\rangle$ (4.6), branching = Bratteli paths (5.4), the q-analog
  (6.2), the inter-rank bijection [comp.].
- **Classical (used, not rediscovered):** `FI`, Schur–Weyl, Clebsch–Gordan, Gaussian
  binomials, the Bratteli diagram, $GL(d,2)$, $A_8$, $Sp(4,2)\!\cong\!S_6$, quadrics, codes.
- **What it is NOT:** not a derivation of the theorems of coding/group/geometry theory; **not
  a new result of category theory.** The categorical backbone is a **form of organization**
  (why the law is uniform and pre-computable), assembled from standard constructions; the
  contribution is their explicit definition on the DOT carriers and the derivation that the
  atlas is their joint orbit.
- **Value:** one generating structure (the lift endofunctor + natural functors) from which
  the ladder of finite mathematical languages unfolds pre-computably. Understanding,
  unification, pedagogy — not new frontier mathematics.

---

*Checks (in `01_Verification/`): `verify_categorical_backbone.py` (18: lift bijection,
Bratteli=$d_k$, q-Pascal, tower), `verify_ontogenesis_general_laws.py` (34),
`verify_rank4/5/6_ontogenesis.py` (13/14/12), `ontogenesis_generator.py` (7 cross-validation),
`verify_tom7_duality.py` (7) — 105 PASS, 0 FAIL. Detailed sample cells and the navigation
index — working folder `_TNR_Research/`.*
