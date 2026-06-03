# Note A. Binary Coordinates in DOT

Status: explanatory note for the strict finite core.

This note has the status of an internal explanatory note. It fixes the binary coordinate convention used inside the finite-rank construction.

---

## A.1. Coordinate Carrier

For rank $n$:

$$
Q_n=\mathbb{F}_2^n.
$$

An element

$$
x=(x_n,\ldots,x_1)
$$

is a binary state with $n$ coordinates.

The zero state:

$$
0^n=(0,\ldots,0).
$$

The full state:

$$
1^n=(1,\ldots,1).
$$

The nonzero layer:

$$
Q_n^*=Q_n\setminus\{0^n\}.
$$

The full nontrivial layer:

$$
U_n=Q_n\setminus\{0^n,1^n\}.
$$

---

## A.2. Hamming Weight and Shells

Hamming weight:

$$
|x|=\#\{i:x_i=1\}.
$$

Shell:

$$
S_k^{(n)}=\{x\in Q_n:|x|=k\}.
$$

Then:

$$
Q_n=\bigsqcup_{k=0}^n S_k^{(n)}.
$$

For the nonzero carrier:

$$
Q_n^*=\bigsqcup_{k=1}^n S_k^{(n)}.
$$

For the full nontrivial carrier:

$$
U_n=\bigsqcup_{k=1}^{n-1}S_k^{(n)}.
$$

---

## A.3. Hamming Relations

For $X\subseteq Q_n$:

$$
\mathsf H_k^{(n)}|_X
=
\{(x,y)\in X\times X:x\neq y,\ d_H(x,y)=k\}.
$$

Here:

$$
d_H(x,y)=|\{i:x_i\neq y_i\}|.
$$

In rank $3$, on the carrier

$$
X_{\mathrm{adm}}=Q_3\setminus\{000,111\},
$$

these relation-layers are:

$$
R_1,\quad R_2,\quad R_3.
$$

They give:

$$
R_1\cong C_6,
\qquad
R_2\cong K_3\sqcup K_3,
\qquad
R_3\cong 3K_2.
$$

---

## A.4. Complement

Complement map:

$$
\kappa_n(x)=x+1^n.
$$

It satisfies:

$$
\kappa_n^2=\mathrm{id}_{Q_n}.
$$

Shell action:

$$
\kappa_n:S_k^{(n)}\to S_{n-k}^{(n)}.
$$

For odd $n=2m+1$:

$$
S_m^{(n)}
\leftrightarrow
S_{m+1}^{(n)}.
$$

For even $n=2m$:

$$
S_m^{(n)}
\leftrightarrow
S_m^{(n)}.
$$

---

## A.5. Rank Growth

The rank-lift from $n$ to $n+1$ appends a new highest bit on the left:

$$
\varepsilon\,|\,x=(\varepsilon,x_n,\ldots,x_1).
$$

Binary rank-lift:

$$
\Lambda_n:\mathbb{F}_2\times Q_n\to Q_{n+1},
\qquad
\Lambda_n(\varepsilon,x)=\varepsilon\,|\,x.
$$

Hence:

$$
Q_{n+1}
=
(0\,|\,Q_n)\sqcup(1\,|\,Q_n).
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

This is the emergence-order.

The shell-order is computed after the full carrier has been assembled.

---

## A.6. Status

The binary coordinate system belongs to the strict finite construction.

It defines:

$$
Q_n,
\qquad
S_k^{(n)},
\qquad
d_H,
\qquad
\kappa_n,
\qquad
\Lambda_n.
$$

A bridge-layer maps finite structures into another realised domain, for example into RGB/Kuhn colour geometry. This note fixes the internal coordinate language of the strict core.

---

## A.7. Useful Figures

### Figure A1. $Q_1,Q_2,Q_3$

$$
Q_1=\{0,1\},
$$

$$
Q_2=\{00,01,10,11\},
$$

$$
Q_3=\{000,001,010,011,100,101,110,111\}.
$$

### Figure A2. Shell Decomposition of $Q_3$

$$
S_0=\{000\},
$$

$$
S_1=\{001,010,100\},
$$

$$
S_2=\{011,101,110\},
$$

$$
S_3=\{111\}.
$$

### Figure A3. Complement-Pairs in $Q_3$

$$
000\leftrightarrow111,
$$

$$
001\leftrightarrow110,
$$

$$
010\leftrightarrow101,
$$

$$
100\leftrightarrow011.
$$

### Figure A4. Rank-Lift $Q_3^*\to Q_4^*$

$$
Q_4^*
=
(0\,|\,Q_3^*)
\sqcup
\{1000\}
\sqcup
(1\,|\,Q_3^*).
$$

Purpose: distinguish emergence-order from shell-order.
