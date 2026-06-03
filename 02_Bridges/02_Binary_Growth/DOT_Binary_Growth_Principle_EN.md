# Binary Structure as the Rank-Growth Principle of DOT

Status: internal bridge / conceptual explanation.

This document explains how binary structure functions inside DOT as the growth mechanism of the tower of finite ranks. It is paired with the technical note:

```text
DOT_Binary_Coordinate_Note_EN.md
```

The technical note fixes the notation. This document explains the conceptual mechanism: one binary coordinate defines a minimal distinction; adding a new coordinate creates the next rank; already constructed states acquire new roles inside the higher carrier.

The document has explanatory status. All carriers, maps, relations, and shell formulas rely on the main manuscript.

---

## 1. Minimal Distinction

A minimal structural distinction has two positions. In rank $1$, it is written as the polar carrier:

$$
P=\{a,-a\}.
$$

Reading:

$$
\pi:P\to\{I\},
\qquad
\pi(a)=\pi(-a)=I.
$$

Recovery:

$$
\mathrm{rec}(I)=(P,R_P).
$$

Thus one invariant position $I$ has two polar manifestations. In binary notation, the same minimal form is:

$$
0,\quad 1.
$$

Here $0$ and $1$ denote two positions of one coordinate. The arithmetic meaning appears later, once the carrier receives algebraic operations. In the initial role, $0/1$ fixes the two sides of one distinction.

The rank-$1$ formula:

$$
Q_1=\mathbb{F}_2=\{0,1\}.
$$

---

## 2. Coordinate as the Place of a Distinction

In DOT, a coordinate is one place where a distinction takes one of two values.

For rank $n$:

$$
Q_n=\mathbb{F}_2^n.
$$

A state:

$$
x=(x_n,\ldots,x_1),
\qquad
x_i\in\{0,1\}.
$$

Each coordinate $x_i$ fixes one minimal distinction. The whole state $x$ fixes the simultaneous manifestation of $n$ distinctions.

Conceptual formula:

$$
\text{rank }n
\quad
=
\quad
n\text{ binary distinctions}.
$$

---

## 3. New Rank as a New Highest Bit

The transition $n\to n+1$ is given by rank-lift:

$$
\Lambda_n:\mathbb{F}_2\times Q_n\to Q_{n+1},
\qquad
\Lambda_n(\varepsilon,x)=\varepsilon\,|\,x.
$$

Here:

$$
\varepsilon\,|\,x=(\varepsilon,x_n,\ldots,x_1).
$$

The new coordinate is attached on the left as a new highest bit.

Each old state $x\in Q_n$ receives two positions in rank $n+1$:

$$
x
\quad
\longmapsto
\quad
0\,|\,x,
\qquad
1\,|\,x.
$$

This is the two-context form of the old state relative to the new distinction. The first context has new bit $0$, the second context has new bit $1$.

The full carrier:

$$
Q_{n+1}=(0\,|\,Q_n)\sqcup(1\,|\,Q_n).
$$

For the nonzero layer:

$$
Q_{n+1}^*
=
(0\,|\,Q_n^*)
\sqcup
\{1\,|\,0^n\}
\sqcup
(1\,|\,Q_n^*).
$$

This is the order of emergence. The shell-order is computed after the full carrier has been assembled.

---

## 4. Rereading Old States

Rank-lift preserves the bit pattern of old states inside the face $0\,|\,Q_n$. At the same time, the status of relations between old states is recomputed relative to the new carrier.

Example $3\to4$.

Embedding:

$$
\iota_{3\to4}(x)=0\,|\,x.
$$

The saturation point of rank $3$:

$$
111
$$

passes to:

$$
0\,|\,111=0111.
$$

In rank $3$, this is the total pole $1^3$. In rank $4$, it is a state of weight $3$, i.e. an element of:

$$
S_3^{(4)}.
$$

The saturation point of rank $4$:

$$
1111.
$$

The same old bit pattern receives a new role: $0111$ is the image of the old saturation point, while rank-$4$ saturation is given by the state $1111$.

Another example: complement pairs.

In rank $3$:

$$
001\leftrightarrow110
$$

because:

$$
001+111=110.
$$

After embedding:

$$
001\mapsto0001,
\qquad
110\mapsto0110.
$$

Rank-$4$ complement acts through $1111$:

$$
0001+1111=1110,
$$

$$
0110+1111=1001.
$$

Therefore the embedded pair:

$$
\{0001,0110\}
$$

has the status of the image of an old relation transported along the embedding. The proper complement relation of rank $4$ is already defined by $\kappa_4$.

Rereading means that the old carrier can be embedded into the new one, but old relations and the native relations of the new rank have different statuses.

---

## 5. The Middle Layer of Rank $4$ as a Growth Example

Rank $4$ shows how old layers are redistributed.

Middle layer:

$$
S_2^{(4)}
=
\{x\in Q_4:|x|=2\}.
$$

Through rank-lift:

$$
S_2^{(4)}
=
(0\,|\,S_2^{(3)})
\sqcup
(1\,|\,S_1^{(3)}).
$$

Thus the middle layer of rank $4$ consists of two sources:

$$
0\,|\,S_2^{(3)}
$$

and

$$
1\,|\,S_1^{(3)}.
$$

Expanded:

$$
0\,|\,S_2^{(3)}
=
\{0011,0101,0110\},
$$

$$
1\,|\,S_1^{(3)}
=
\{1001,1010,1100\}.
$$

On this six-state carrier, rank $4$ constructs graph-readings:

$$
(S_2^{(4)},\mathsf H_2^{(4)}|_{S_2^{(4)}})\cong K_{2,2,2},
$$

$$
(S_2^{(4)},\mathsf H_4^{(4)}|_{S_2^{(4)}})\cong 3K_2.
$$

Thus the octahedral pattern of rank $3$ appears in rank $4$ as a middle layer. It is a new assembly from two sources of rank-lift:

$$
0\,|\,S_2^{(3)}
\quad
\text{and}
\quad
1\,|\,S_1^{(3)}.
$$

---

## 6. The Shell Scale Inside a Rank

Hamming weight:

$$
|x|=\#\{i:x_i=1\}.
$$

Shell:

$$
S_k^{(n)}=\{x\in Q_n:|x|=k\}.
$$

Number of states in a shell:

$$
|S_k^{(n)}|=\binom nk.
$$

Full shell decomposition:

$$
Q_n=\bigsqcup_{k=0}^nS_k^{(n)}.
$$

Therefore:

$$
2^n=\sum_{k=0}^n\binom nk.
$$

The first ranks:

$$
2=1+1,
$$

$$
4=1+2+1,
$$

$$
8=1+3+3+1,
$$

$$
16=1+4+6+4+1,
$$

$$
32=1+5+10+10+5+1.
$$

In DOT, this binomial structure receives a role-reading: the shell $S_k^{(n)}$ contains the states in which exactly $k$ coordinates are manifested.

---

## 7. Lifting Shells

If:

$$
x\in S_k^{(n)},
$$

then:

$$
0\,|\,x\in S_k^{(n+1)},
$$

$$
1\,|\,x\in S_{k+1}^{(n+1)}.
$$

A new zero bit preserves Hamming weight. A new one bit increases Hamming weight by $1$.

Shell-lift:

$$
S_k^{(n)}
\hookrightarrow
S_k^{(n+1)}\sqcup S_{k+1}^{(n+1)}.
$$

The sizes agree with Pascal's identity:

$$
\binom{n+1}{k}
=
\binom nk+\binom n{k-1}.
$$

In DOT, this identity reads rank-growth: the shell $S_k^{(n+1)}$ is assembled from states in $S_k^{(n)}$ through $0|\cdot$ and states in $S_{k-1}^{(n)}$ through $1|\cdot$.

---

## 8. Complement as Full Inversion

Complement map:

$$
\kappa_n:Q_n\to Q_n,
\qquad
\kappa_n(x)=x+1^n.
$$

It changes the value of every coordinate.

Property:

$$
\kappa_n^2=\mathrm{id}_{Q_n}.
$$

On the full $Q_n$, for $n\geq1$, the map $\kappa_n$ is fixed-point-free. Therefore it decomposes $Q_n$ into:

$$
2^{n-1}
$$

unordered complement pairs.

On the nonzero layer:

$$
Q_n^*=Q_n\setminus\{0^n\}
$$

the state $1^n$ has complement $0^n$, which lies outside the layer. Hence $1^n$ remains unpaired inside $Q_n^*$.

On the full nontrivial layer:

$$
U_n=Q_n\setminus\{0^n,1^n\}
$$

the number of complement pairs is:

$$
2^{n-1}-1.
$$

Action on shells:

$$
\kappa_n:S_k^{(n)}\xrightarrow{\cong}S_{n-k}^{(n)}.
$$

For odd rank $n=2m+1$:

$$
S_m^{(n)}
\leftrightarrow
S_{m+1}^{(n)}.
$$

For even rank $n=2m$:

$$
S_m^{(n)}
\leftrightarrow
S_m^{(n)}.
$$

Thus binary complement gives duality of the middle shells in odd ranks and self-duality of the middle shell in even ranks.

---

## 9. Axial Invariants from Complement

Outer shell:

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}.
$$

Complement maps:

$$
S_1^{(n)}
\leftrightarrow
S_{n-1}^{(n)}.
$$

For each coordinate:

$$
H_i^{(n)}=\{e_i,1^n-e_i\}.
$$

These $n$ pairs decompose $V_n$:

$$
V_n=\bigsqcup_{i=1}^nH_i^{(n)}.
$$

Carrier of axial invariants:

$$
I_n=\{I_1^{(n)},\ldots,I_n^{(n)}\}.
$$

Sign carrier:

$$
\Sigma=\{-,+\}.
$$

Axial factorization:

$$
V_n\cong I_n\times\Sigma.
$$

Conceptual meaning: each coordinate gives one axis, and the complement pair gives two polar manifestations of that axis.

Rank $3$ is unique among $n\geq3$:

$$
U_3=V_3.
$$

Therefore the entire active carrier of rank $3$ is already the outer shell:

$$
X_{\mathrm{adm}}=S_1^{(3)}\sqcup S_2^{(3)}.
$$

Starting with rank $4$, the middle shells separate from the outer shell.

---

## 10. Why the Binary Structure Is Primary

A binary coordinate has two properties used by the whole finite-rank architecture.

The first property is minimal polarity:

$$
\{0,1\}.
$$

One coordinate defines exactly one pair of positions.

The second property is canonical complement:

$$
x\mapsto x+1^n.
$$

This operation:

$$
\kappa_n^2=\mathrm{id},
$$

maps shells $S_k\leftrightarrow S_{n-k}$, defines complement pairs, and is compatible with rank-lift:

$$
\kappa_{n+1}(\varepsilon\,|\,x)
=
(1+\varepsilon)\,|\,\kappa_n(x).
$$

Ternary or $q$-valued carriers may be constructed as future extensions once their own relations, readings, and recovery data have been specified. The current strict finite core uses binary carriers: minimal polarity, complement involution, shell duality, and rank-lift work in one algebraic form over $\mathbb{F}_2$.

---

## 11. What the Binary Bridge Explains

The binary growth principle connects four levels.

Rank $1$:

$$
Q_1=\{0,1\}.
$$

Rank growth:

$$
Q_{n+1}=(0\,|\,Q_n)\sqcup(1\,|\,Q_n).
$$

Shell growth:

$$
S_k^{(n)}
\hookrightarrow
S_k^{(n+1)}\sqcup S_{k+1}^{(n+1)}.
$$

Complement growth:

$$
\kappa_{n+1}(\varepsilon\,|\,x)
=
(1+\varepsilon)\,|\,\kappa_n(x).
$$

Outer-shell growth:

$$
V_n\cong I_n\times\Sigma.
$$

Thus binary structure connects the polar pair of rank $1$, the tower of shells, complement duality, axial factorization, and the universal outer graph:

$$
(V_n,\Omega_n)\cong K_{\underbrace{2,\ldots,2}_{n}}.
$$

---

## 12. Necessary Figures

### Figure A2.1. Rank-Lift

Show:

$$
Q_{n+1}=(0\,|\,Q_n)\sqcup(1\,|\,Q_n).
$$

Purpose: show the two copies of the old carrier as two contexts of the new distinction.

### Figure A2.2. Shell-Lift

Show:

$$
S_k^{(n)}
\to
S_k^{(n+1)}
$$

and

$$
S_k^{(n)}
\to
S_{k+1}^{(n+1)}.
$$

Purpose: visualise Pascal's identity as rank-growth.

### Figure A2.3. Complement Pairs

Show for $Q_3$:

$$
000\leftrightarrow111,
\quad
001\leftrightarrow110,
\quad
010\leftrightarrow101,
\quad
100\leftrightarrow011.
$$

Purpose: show full inversion.

### Figure A2.4. Rereading $3\to4$

Show:

$$
S_2^{(4)}
=
(0\,|\,S_2^{(3)})
\sqcup
(1\,|\,S_1^{(3)}).
$$

Purpose: show that the middle layer of rank $4$ is assembled from two shell sources of rank $3$.

### Figure A2.5. Outer Axial Factorization

Show:

$$
V_n=S_1^{(n)}\sqcup S_{n-1}^{(n)}
\cong
I_n\times\{-,+\}.
$$

Purpose: show how complement pairs become axial invariants.

---

## 13. Document Status

This document has the status of an internal bridge. The native carriers, relations, and proofs remain in the strict core.

Native data remain in the main manuscript:

$$
Q_n,\quad
\Lambda_n,\quad
S_k^{(n)},\quad
\kappa_n,\quad
V_n,\quad
I_n.
$$

The task of this document is to connect these formulas into one conceptual reading: binary structure gives the mechanism by which a minimal distinction unfolds into a tower of finite ranks.
