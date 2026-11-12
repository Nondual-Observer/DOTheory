# Chapter II.5. The Nonassociative Step: The Fano Plane, Octonions over $\mathbb{F}_2$, the Paige Loop, and the Cayley–Dickson Tower

In `Chapter II.4`, we traversed the stage of non-commutative groups ($ab \ne ba$), where the composition of three successive actions still obeyed the associative law $(ab)c = a(bc)$. Now the next stage from `Table I.9.3` of Book I opens before us: **what happens to the observer's contract when the composition rule itself depends on parenthesization—that is, on which two of three steps are glued together first?**

At first glance, abandoning associativity might seem to take us far away from the finite core of Book I. In reality, the exact opposite is true: the nonassociative geometry of the octonions grows directly out of the **three-bit space of parity charges** $\mathbb{F}_2^3 = \{(x_0, c_0, b_0)\}$ of our checkerboard octahedron $O_6$ (`Chapter I.9`) and the **projective Fano plane** $\mathrm{PG}(2, \mathbb{F}_2)$ from `Chapter I.6`.

Indeed, the cube $\mathbb{F}_2^3$ has exactly $8$ vertices. The zero vector $(0,0,0)$ corresponds to the trivial unit direction $e_0 = 1$, while the remaining **seven non-zero vectors** $v_1, \dots, v_7 \in \mathbb{F}_2^3 \setminus \{(0,0,0)\}$ (on which the triple parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ lived in Book I) form the $7$ points of the projective Fano plane $\mathrm{PG}(2, \mathbb{F}_2)$. Each of the $7$ lines of the Fano plane consists of three non-zero vectors $\{u, v, u \oplus v\}$ whose sum modulo $2$ vanishes: $u \oplus v \oplus w = 0$.

A natural question arises connecting `Chapter I.5` (sign) with `Chapter I.6` (Fano):

> **How does a "sign-blind observer," who sees on the Fano plane only unordered triples of points $\{i, j, k\}$ ($e_i \star e_j = e_k$), differ from a "signed observer," who orients each of the seven Fano lines with a cyclic sign $\varepsilon_{ijk} \in \{\pm 1\}$ ($e_i e_j = \varepsilon_{ijk} e_k$), and where does the exact algebraic boundary lie beyond which further doubling of dimension produces zero divisors?**

The present chapter provides a rigorous and exhaustive answer to this question:
1. we prove (`Theorem II.5.1`) that the **unsigned multiplication table along the Fano lines** on $\mathbb{F}_2 \oplus \mathbb{F}_2^7$ is isomorphic to the group algebra $\mathbb{F}_2[\mathbb{F}_2^3]$, and is therefore **commutative and fully associative** ($0$ associativity violations out of all $512$ basis triples): a sign-blind observer cannot distinguish the orientation of Fano lines and remains inside the associative world of bitwise addition $\oplus$;
2. as soon as a coherent cyclic orientation with sign $\varepsilon_{ijk} = \pm 1$ over a ring of characteristic $\ne 2$ (or a twisted code cocycle over $\mathbb{F}_2$) is introduced on the seven Fano lines, commutativity and associativity give way to **alternativity** ($x(xy) = x^2 y$, $(yx)x = y x^2$) and the Moufang identities: the $8$-dimensional Cayley–Graves octonion algebra is born;
3. in the modular algebra of split octonions $\mathrm{Oct}(\mathbb{F}_2)$ of $256$ elements, we find exactly $120$ elements of norm $1$, which split into $36$ elements with isotropic off-diagonal projection and $84$ elements with non-isotropic off-diagonal projection; taking the quotient by the center $\{\pm I\} = \{I\}$ carves out the famous simple Moufang loop—the **Paige loop** (Paige, 1956) with automorphism group $G_2(2)$ of order $12\,096$ and canonical $6$-dimensional symplectic space $V_6 = I^\perp / \langle I \rangle$;
4. finally, at the fourth step of the Cayley–Dickson doubling tower ($1 \to 2 \to 4 \to 8 \to 16$, sedenions $\mathbb{S}$), we prove why the loss of alternativity destroys the identity $\bar{x}(xy) = N(x)y$ and opens up the $84$-quartet family of normalized zero divisors, exhibiting explicit integer witnesses $(e_1 + e_{10})(e_4 - e_{15}) = 0$ and $(e_3 + e_{10})(e_6 - e_{15}) = 0$, and we compare this barrier with the $8$-fold Bott periodicity of real Clifford algebras $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$.

---

## §II.5.1. Seven Fano Lines on the Three-Bit Charge Space $\mathbb{F}_2^3 \setminus \{0\}$: Why the Unsigned Table Is Associative and the Signed Table Is Alternative

Let us fix the standard binary numbering of the seven points of the Fano plane $\mathrm{PG}(2, \mathbb{F}_2)$ by the non-zero three-bit vectors $v_i \in \mathbb{F}_2^3 \setminus \{(0,0,0)\}$ ($i = 1, \dots, 7$), in which the index $i \in \{1, \dots, 7\}$ coincides with the binary representation of the vector $v_i = (b_2, b_1, b_0)_2$:
$$
\begin{aligned}
v_1 &= (0,0,1), \quad v_2 = (0,1,0), \quad v_3 = (0,1,1), \quad v_4 = (1,0,0), \\
v_5 &= (1,0,1), \quad v_6 = (1,1,0), \quad v_7 = (1,1,1).
\end{aligned}
$$
Under this numbering, three distinct points $i, j, k \in \{1, \dots, 7\}$ lie on a single Fano line if and only if their bitwise sum (XOR) vanishes:
$$
v_i \oplus v_j = v_k \Longleftrightarrow i \oplus j = k.
$$
In particular, the seventh point $v_7 = (1,1,1)$ is the sum vector of all three coordinates, corresponding to the triple parity character $w_{111}$ and the charge $\kappa = x_0 \oplus c_0 \oplus b_0$ from Book I (`Chapter I.9`) and `Chapter II.1` (`Proposition II.1.1`). The seven Fano lines with the cyclic Graves–Cayley orientation take the form:
$$
\mathcal{L}_{\mathrm{Fano}} = \bigl\{ (1,2,3),\; (1,4,5),\; (1,7,6),\; (2,4,6),\; (2,5,7),\; (3,4,7),\; (3,6,5) \bigr\}.
$$

Let us now compare two algebras on the $8$-dimensional space with basis $\{e_0, e_1, \dots, e_7\}$:
1. **The unsigned Fano algebra**, in which the observer records only the collinearity of triples $\{i, j, k\} \in \mathcal{L}_{\mathrm{Fano}}$ without orientation sign:
   $$
   e_0 \star e_i = e_i \star e_0 = e_i, \qquad e_i \star e_i = e_0, \qquad e_i \star e_j = e_{i \oplus j} \quad (i \ne j).
   $$
2. **The signed Cayley–Graves octonion algebra** $\mathbb{O}$ over a field (or commutative ring) $K$ of characteristic $\operatorname{char} K \ne 2$, in which the unit $e_0 = 1$ is neutral, and the imaginary units anticommute and square to $-e_0$:
   $$
   e_i^2 = -e_0, \qquad e_i e_j = -e_j e_i = \varepsilon_{ijk}\, e_k \qquad \bigl((i,j,k) \text{ a cyclic permutation of a line in } \mathcal{L}_{\mathrm{Fano}}\bigr).
   $$

> **Theorem II.5.1 (Associativity of the unsigned Fano table $\mathbb{F}_2[\mathbb{F}_2^3]$ and the birth of alternativity from a signed $2$-cochain).**  
> *Classical foundation.* Associativity of the group algebra $K[\mathbb{F}_2^3]$ and representation of the octonions as the twisted group algebra $\mathbb{R}_\sigma[\mathbb{F}_2^3]$ with a sign $2$-cocycle and its $3$-coboundary on the Fano plane (Albuquerque and Majid, 1999). *Contribution of this book:* Direct passage from the unsigned commutative-associative Fano table of Book I to the alternative octonion algebra by choosing a sign $2$-cocycle $\sigma$, verified exhaustively across all $512$ basis triples.
> 1. **(The unsigned Fano table is associative).** Over any field $K$ (and in particular over $K = \mathbb{F}_2$), the unsigned Fano algebra $(K^8, \star)$ with the rule $e_r \star e_s = e_{r \oplus s}$ ($0 \le r, s \le 7$, where $v_0 = (0,0,0)$) is canonically isomorphic to the group algebra of the elementary abelian $2$-group $K[\mathbb{F}_2^3]$ under the map $e_r \mapsto [v_r]$. By virtue of the associativity and commutativity of bitwise addition $\oplus$ on $\mathbb{F}_2^3$, the operation $\star$ is **commutative and strictly associative** on all $8^3 = 512$ basis triples:
>    $$
>    (e_r \star e_s) \star e_t = e_{(r \oplus s) \oplus t} = e_{r \oplus (s \oplus t)} = e_r \star (e_s \star e_t) \qquad (\forall r, s, t \in \{0, \dots, 7\}),
>    $$
>    and a fortiori alternative. Thus, a sign-blind observer (`Chapter I.5`) who does not distinguish the traversal direction of Fano lines remains inside the associative group algebra $K[\mathbb{F}_2^3]$.
> 2. **(The signed octonion table is nonassociative, yet alternative).** Conversely, in the signed octonion algebra $\mathbb{O}$ over a ring $K$ ($\operatorname{char} K \ne 2$), out of the $512$ basis triples $(e_r, e_s, e_t)$ exactly $168$ triples (all ordered triples of non-collinear imaginary units—the $7 \times 6 \times 4 = 168$ Fano frames) are anti-associative:
>    $$
>    (e_i e_j) e_k = -\, e_i (e_j e_k) \ne e_i (e_j e_k) \qquad (\text{when } \det(v_i, v_j, v_k) = 1 \text{ over } \mathbb{F}_2),
>    $$
>    whereas all collinear triples and all triples with repeated elements are associative. Consequently, in the octonion algebra $\mathbb{O}$ the following identities hold identically:
>    - **left and right alternativity**: $x(xy) = (xx)y$ and $(yx)x = y(xx)$ for all $x, y \in \mathbb{O}$;
>    - **the Moufang identities**: $(zx)(yz) = z(xy)z$, $z(x(zy)) = (zxz)y$, $((xz)y)z = x(zyz)$;
>    - **multiplicativity of the quadratic norm** $N(x) = x \bar{x} = \sum_{r=0}^7 x_r^2$:
>      $$
>      N(xy) = N(x)\,N(y), \qquad \bar{x}(xy) = N(x)\,y, \qquad (yx)\bar{x} = N(x)\,y.
>      $$

**Proof.**  
1. Since the map $r \mapsto v_r \in \mathbb{F}_2^3$ ($0 \le r \le 7$) converts the bitwise operation $r \oplus s$ into vector addition $v_r + v_s \pmod 2$ in the abelian group $(\mathbb{F}_2^3, +)$, the basis elements $e_r$ form a group isomorphic to $\mathbb{F}_2^3$. The associativity of the group law $(v_r + v_s) + v_t = v_r + (v_s + v_t)$ extends by linearity to the entire group algebra $K[\mathbb{F}_2^3]$.

2. In the signed octonion table $e_r e_s = (-1)^{\phi(r,s)} e_{r \oplus s}$, the sign is given by a $2$-cochain $\phi : \mathbb{F}_2^3 \times \mathbb{F}_2^3 \to \mathbb{F}_2$ whose coboundary $\delta_2 \phi(u, v, w) = \phi(v, w) \oplus \phi(u+v, w) \oplus \phi(u, v+w) \oplus \phi(u, v)$ equals the trilinear determinant $\det(u, v, w) \in \mathbb{F}_2$:
$$
(e_u e_v) e_w = (-1)^{\det(u, v, w)}\, e_u (e_v e_w).
$$
The determinant $\det(u, v, w)$ over $\mathbb{F}_2$ equals $1$ if and only if the vectors $u, v, w \in \mathbb{F}_2^3$ are linearly independent (do not lie on a single Fano line and do not contain zero—there are exactly $7 \cdot 6 \cdot 4 = 168$ such ordered triples in $\mathbb{F}_2^3$), and equals $0$ whenever $u, v, w$ are linearly dependent over $\mathbb{F}_2$ (in particular, whenever two of the three vectors coincide: $u = v$ or $v = w$). From the vanishing $\det(u, u, w) = \det(u, v, u) = 0$, bilinearity of the associator $[x, y, z] = (xy)z - x(yz)$ immediately yields $[x, x, y] = [y, x, x] = 0$, i.e., alternativity. Finally, for the conjugate $\bar{x} = x_0 e_0 - \sum_{i=1}^7 x_i e_i$, we have $x + \bar{x} = 2 x_0 e_0 \in K e_0$, so $[\bar{x}, x, y] = - [x, x, y] = 0$, whence $\bar{x}(xy) = (\bar{x}x)y = N(x)y$. $\blacksquare$

> **Methodological Note (Sign as the Sole Source of Nonassociativity on the Fano Plane).**  
> Without signed orientation (`Chapter I.5`), collinearity of point triples on the Fano plane defines the commutative and strictly associative group algebra $\mathbb{F}_2[\mathbb{F}_2^3]$; the nonassociativity and alternativity of the octonions arise exclusively from the non-trivial trilinear coboundary $\det(u, v, w) \in \mathbb{F}_2$ of the signed $2$-cochain $\phi$.

---

## §II.5.2. Modular Octonions $\mathrm{Oct}(\mathbb{F}_2)$, the Paige Loop of Order $120$, the Symplectic Core $V_6$, and the Group $G_2(2)$

In characteristic $2$ ($\mathbb{F}_2$), where $+1 = -1$, the sign factor $(-1)^{\phi(r,s)}$ becomes trivial if one remains in the diagonal basis of Fano lines. However, the octonion algebra is defined over the ring of integers $\mathbb{Z}$ as the lattice of split octonions (Zorn vector-matrices), which reduces modulo $2$ to an $8$-dimensional nonassociative alternative algebra $\mathrm{Oct}(\mathbb{F}_2)$ of $2^8 = 256$ elements.

Recall the explicit construction of the Zorn algebra $\mathrm{Oct}(\mathbb{F}_2)$. Every element $x \in \mathrm{Oct}(\mathbb{F}_2)$ is written as a vector-matrix
$$
x = \begin{pmatrix} a & u \\ v & b \end{pmatrix}, \qquad a, b \in \mathbb{F}_2, \quad u, v \in \mathbb{F}_2^3,
$$
with Zorn multiplication (where $u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3 \pmod 2$ is the dot product and $u \times v = (u_2 v_3 + u_3 v_2,\, u_3 v_1 + u_1 v_3,\, u_1 v_2 + u_2 v_1) \pmod 2$ is the cross product in $\mathbb{F}_2^3$):
$$
\begin{pmatrix} a_1 & u_1 \\ v_1 & b_1 \end{pmatrix}
\begin{pmatrix} a_2 & u_2 \\ v_2 & b_2 \end{pmatrix}
=
\begin{pmatrix}
a_1 a_2 + u_1 \cdot v_2 & a_1 u_2 + b_2 u_1 + v_1 \times v_2 \\
a_2 v_1 + b_1 v_2 + u_1 \times u_2 & b_1 b_2 + v_1 \cdot u_2
\end{pmatrix} \pmod 2.
$$
The identity element of the algebra is $I = \bigl(\begin{smallmatrix} 1 & 0 \\ 0 & 1 \end{smallmatrix}\bigr)$, conjugation takes the form $\bar{x} = \bigl(\begin{smallmatrix} b & u \\ v & a \end{smallmatrix}\bigr)$, the linear trace is $\mathrm{tr}(x) = x + \bar{x} = (a + b) I \in \mathbb{F}_2$, and the quadratic norm is
$$
N(x) = x \bar{x} = (ab + u \cdot v) I \in \mathbb{F}_2,
$$
with polar bilinear symplectic form
$$
\omega(x, y) = N(x + y) + N(x) + N(y) = a_1 b_2 + b_1 a_2 + u_1 \cdot v_2 + v_1 \cdot u_2 \in \mathbb{F}_2.
$$

> **Theorem II.5.2 (Structure of $\mathrm{Oct}(\mathbb{F}_2)$, the simple Paige loop of order $120$, the symplectic space $V_6 = I^\perp/\langle I\rangle$, and the group $G_2(2)$).**  
> *Classical foundation.* Zorn's vector-matrix model of split octonions and Paige's simple Moufang loops (1956) are classical constructions. *Contribution of this book:* Separation of the trace split $64 + 56 = 120$ from the quadratic split $36 + 84 = 120$ with an exhaustive check of all $120^3$ Moufang triples.
> In the $256$-element modular octonion algebra $\mathrm{Oct}(\mathbb{F}_2)$:
> 1. **(Canonical $6$-dimensional symplectic core $V_6$).** For every $x \in \mathrm{Oct}(\mathbb{F}_2)$, pairing with the identity $I$ under the bilinear form $\omega$ coincides with the linear trace:
>    $$
>    \omega(x, I) = a \cdot 1 + b \cdot 1 + u \cdot 0 + v \cdot 0 = a + b = \mathrm{tr}(x) \in \mathbb{F}_2.
>    $$
>    Consequently, the $7$-dimensional trace-zero hyperplane $T_0 = \{x \in \mathrm{Oct}(\mathbb{F}_2) : \mathrm{tr}(x) = 0\}$ ($|T_0| = 128$) coincides identically with the orthogonal complement of the identity $I^\perp = \{x : \omega(x, I) = 0\}$. Since in characteristic $2$ the identity element $I = \bigl(\begin{smallmatrix} 1 & 0 \\ 0 & 1 \end{smallmatrix}\bigr)$ itself has trace zero, $\omega(I, I) = 1 + 1 = 0$, the one-dimensional line $\langle I \rangle = \{0, I\}$ is the radical of the restriction of $\omega$ to $I^\perp$, and the $6$-dimensional quotient space
>    $$
>    V_6 = I^\perp / \langle I \rangle \cong \mathbb{F}_2^6 \qquad (|V_6| = 64)
>    $$
>    carries a canonical non-degenerate symplectic form $\bar{\omega}([u,v], [u',v']) = u \cdot v' + v \cdot u'$.
> 2. **(The Paige loop of order $120$ and the partition $120 = 36 + 84$).** The set of invertible norm-$1$ elements
>    $$
>    M_{120} = \{ x \in \mathrm{Oct}(\mathbb{F}_2) : N(x) = ab + u \cdot v = 1 \}
>    $$
>    contains exactly $120$ elements ($|M_{120}| = 120$) and forms under Zorn multiplication a **simple nonassociative Moufang loop of order $120$—the Paige loop** (L. J. Paige, 1956; since in characteristic $2$ the center $\{\pm I\} = \{I\}$ is trivial, $M_{120}/\{I\} = M_{120}$). According to the value of the linear trace $\mathrm{tr}(x) = \omega(x, I) \in \{0, 1\}$, the Paige loop $M_{120}$ splits into $64$ trace-zero elements ($a=b$) and $56$ trace-$1$ elements ($a+b=1$), while according to the value of the off-diagonal quadratic form $q_0(u,v) = u \cdot v \in \{0,1\}$ it splits into two canonical classes:
>    - **$36$ elements with $u \cdot v = 0$** (where $a = b = 1$ and $ab + u \cdot v = 1$; all non-trivial elements in this class satisfy $x^2 = I$, i.e., are involutions in $M_{120}$);
>    - **$84$ elements with $u \cdot v = 1$** ($28$ trace-zero elements with $a=b=0$ and $56$ trace-$1$ elements with $a + b = 1$, the latter satisfying the quadratic equation $x^2 + x + I = 0$, i.e., having order $3$ in $M_{120}$).
> 3. **(Idempotents, hyperbolic quadratic forms, and the group $G_2(2)$).** The set of non-trivial idempotents $E_{72} = \{ e \in \mathrm{Oct}(\mathbb{F}_2) \setminus \{0, I\} : e^2 = e \}$ consists of all elements with trace $\mathrm{tr}(e) = 1$ and norm $N(e) = 0$. Let us verify the exact counts for $M_{120}$ and $E_{72}$ in integer arithmetic.

Let us carry out the exact enumeration for $M_{120}$ and $E_{72}$ in integer arithmetic:
- in $\mathbb{F}_2^3 \times \mathbb{F}_2^3$ ($64$ pairs $(u,v)$), the dot product $u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$ is a non-degenerate hyperbolic quadratic form of rank $6$ and Arf invariant $0$: it takes the value $1$ on exactly $2^{3-1}(2^3 - 1) = 4 \cdot 7 = \mathbf{28}$ pairs $(u,v)$ and the value $0$ on exactly $2^{3-1}(2^3 + 1) = 4 \cdot 9 = \mathbf{36}$ pairs $(u,v)$.
- **At trace $\mathrm{tr}(x) = a + b = 0$**, we have $a = b \in \{0, 1\}$:
  * if $a = b = 0$, then $N(x) = u \cdot v = 1$ gives **$28$ elements**;
  * if $a = b = 1$, then $N(x) = 1 + u \cdot v = 1 \iff u \cdot v = 0$, giving **$36$ elements**.
  In total at trace $0$ we obtain $28 + 36 = \mathbf{64}$ elements of norm $1$. Meanwhile, at trace $\mathrm{tr}(x) = a + b = 1$, we have $(a,b) \in \{(1,0), (0,1)\}$, whence $ab = 0$ and:
  * the condition $N(x) = u \cdot v = 1$ gives $2 \times 28 = \mathbf{56}$ elements of norm $1$ and trace $1$ ($x^2 + x + I = 0$);
  * the condition $N(x) = u \cdot v = 0$ gives $2 \times 36 = \mathbf{72}$ **non-trivial idempotents** ($e^2 = e$, since $e^2 + \mathrm{tr}(e)e + N(e)I = e^2 + e = 0$).
  And the total number of norm-$1$ elements in $\mathrm{Oct}(\mathbb{F}_2)$ is $(28 + 36) + 56 = 64 + 56 = \mathbf{120}$.
- Observe now how the Paige loop $M_{120}$ itself partitions according to the value of the canonical hyperbolic quadratic form $q_0(u,v) = u \cdot v$ of its off-diagonal projection $w = (u,v) \in V_6$:
  * exactly **$36$ elements** of the Paige loop have $q_0(u,v) = u \cdot v = 0$ (and diagonal $a = b = 1$), and their off-diagonal projections $w = (u,v) \in V_6$ are **the exact same $36$ isotropic vectors** that are doubly covered ($2\text{-to-}1$: pairs $\{e, I \oplus e\}$ with $(a,b) \in \{(1,0), (0,1)\}$) by the set $E_{72}$ of $72$ non-trivial idempotents;
  * the remaining **$28 + 56 = 84$ elements** of the Paige loop have $q_0(u,v) = u \cdot v = 1$ ($28$ elements with $a = b = 0$ and $56$ elements with trace $a \oplus b = 1$), yielding the canonical partition
    $$
    |M_{120}| = 36 + 84 = 120.
    $$
- Furthermore, for each vector $w = (u,v) \in V_6$, the shifted quadratic form $q_w(z) = q_0(z) \oplus \bar{\omega}(w, z) = q_0(z \oplus w) \oplus q_0(w)$ on $V_6$ (polarizing the same symplectic form $\bar{\omega}$) belongs:
  * when $q_0(w) = 0$ (i.e., for all $36$ projections $w(e)$ of idempotents $e \in E_{72}$)—to the family of **$36$ quadratic forms of plus type** ($\mathrm{O}^+_6(\mathbb{F}_2)$, $2^{3-1}(2^3 + 1) = 36$), each of which takes the value $0$ on $V_6$ exactly $36$ times and the value $1$ exactly $28$ times;
  * when $q_0(w) = 1$—to the family of **$28$ quadratic forms of minus type** ($\mathrm{O}^-_6(\mathbb{F}_2)$, $2^{3-1}(2^3 - 1) = 28$), each of which takes the value $0$ on $V_6$ exactly $28$ times and the value $1$ exactly $36$ times.

Let us record this exact combinatorial anatomy in a summary table:

#### Table II.5.1. Exact Combinatorial Anatomy of the Modular Octonions $\mathrm{Oct}(\mathbb{F}_2)$ and the Symplectic Core $V_6 = I^\perp/\langle I\rangle$

| Invariant in $\mathrm{Oct}(\mathbb{F}_2)$ ($256$ elements) | Exact count | Algebraic characterization |
| :--- | :---: | :--- |
| Dimension of the symplectic core $V_6 = I^\perp / \langle I \rangle$ | $\dim_{\mathbb{F}_2} V_6 = 6$ ($64$ vectors) | $\omega(x, I) = \mathrm{tr}(x)$, $T_0 = I^\perp$ ($128$ elements), $I \in I^\perp$ |
| Paige loop $M_{120} = \{x : N(x) = 1\}$ (simple Moufang loop) | $120$ | $64$ elements in $M_{120} \cap I^\perp$ ($28 + 36$) and $56$ elements of trace $1$ ($x^2+x+I=0$) |
| Partition $120 = 36 + 84$ by $q_0(u,v) \in \{0,1\}$ and plus-forms on $V_6$ | $36 + 84 = 120$ | $36$ elements with $u \cdot v = 0$ ($a=b=1$) and $28 + 56 = 84$ elements with $u \cdot v = 1$; $36 = 2^{3-1}(2^3+1)$ plus-forms of $\mathrm{O}^+_6(\mathbb{F}_2)$ |
| Non-trivial idempotents $E_{72} = \{e \ne 0, I : e^2 = e\}$ | $72$ | $\mathrm{tr}(e) = 1, N(e) = u \cdot v = 0$ ($2 \times 36 = 72$); for each $e \in E_{72}$ the form $q_{w(e)}(z) = q_0(z) \oplus \bar{\omega}(w(e), z)$ has $36$ zeros and $28$ ones on $V_6$ |
| Order of the automorphism group $G_2(2) = \mathrm{Aut}(\mathrm{Oct}(\mathbb{F}_2))$ | $12\,096$ | $|G_2(2)| = 2^6 (2^6 - 1)(2^2 - 1) = 64 \cdot 63 \cdot 3 = 12\,096$; $[G_2(2) : \mathrm{PSU}_3(3)] = 2$ |

Let us also define explicitly the coboundary operator $\delta_4$ connecting the $36$ quadratic plus-forms on $V_6$ with the space of homogeneous cubic Boolean forms: if a quadratic form $q : V_6 \to \mathbb{F}_2$ has associated bilinear form $\bar{\omega}(x, y) = q(x+y) + q(x) + q(y)$, then the **fourth polarization difference**
$$
(\delta_4 q)(x, y, z) = q(x+y+z) + q(x+y) + q(x+z) + q(y+z) + q(x) + q(y) + q(z) + q(0)
$$
vanishes identically ($\delta_4 q = 0$) for all quadratic forms $q$, while shifting the base plus-form $q_0$ by linear functionals $\ell \in V_6^*$ ($\ell(x) = \bar{\omega}(a, x)$) parameterizes the $36$ plus-forms and $28$ minus-forms (totaling $36 + 28 = 64 = |V_6^*|$) inside a single affine torsor over $V_6^*$.

---

## §II.5.3. The Cayley–Dickson Tower $1 \to 2 \to 4 \to 8 \to 16$: Why the Sedenions $\mathbb{S}$ Lose Alternativity and Acquire Zero Divisors

In the classical Cayley–Dickson doubling tower over the field of real numbers $\mathbb{R}$, each successive algebra $A_{n+1} = A_n \oplus A_n e_{2^n}$ is constructed from the preceding one by the rule
$$
(a, b)(c, d) = (ac - \bar{d}b,\; da + b\bar{c}), \qquad \overline{(a, b)} = (\bar{a}, -b).
$$
At each doubling of dimension, exactly one structural symmetry is lost:
- $\mathbb{R}$ ($\dim = 1$): ordered, commutative, associative field;
- $\mathbb{C}$ ($\dim = 2$, `Chapter I.5`): loses linear ordering and self-conjugacy ($\bar{z} \ne z$), but retains commutativity and associativity;
- $\mathbb{H}$ ($\dim = 4$, the quaternions of `Chapter II.4`): loses commutativity ($ij = -ji$), but retains associativity;
- $\mathbb{O}$ ($\dim = 8$, the octonions): loses associativity, but retains **alternativity** and norm multiplicativity $N(xy) = N(x)N(y)$, owing to which $\mathbb{O}$ has no zero divisors:
  $$
  xy = 0 \implies N(x)y = \bar{x}(xy) = 0 \implies N(x) = 0 \text{ or } y = 0.
  $$

What happens at the next step $8 \to 16$, when we form the $16$-dimensional algebra of **sedenions** $\mathbb{S} = \mathbb{O} \oplus \mathbb{O} e_8$ with basis $e_0, e_1, \dots, e_{15}$?

> **Proposition II.5.1 (Breakdown of alternativity in the sedenions $\mathbb{S}$ and explicit zero-divisor witnesses).**  
> *Classical foundation.* Cayley–Dickson doubling and the appearance of zero divisors in sedenions belong to classical nonassociative algebra. *Contribution of this book:* Explicit integer zero-divisor witnesses and exhaustive enumeration of all $84$ elementary quartets.
> In the $16$-dimensional sedenion algebra $\mathbb{S}$ with basis $\{e_0, e_1, \dots, e_{15}\}$ obtained by Cayley–Dickson doubling of the octonions $\mathbb{O}$ ($e_{8+i} = (0, e_i)$):
> 1. The property of alternativity and the identity $\bar{x}(xy) = N(x)y$ fail: there exist non-zero elements $x, y \in \mathbb{S}$ with non-zero Euclidean norms $N(x) = 2 \ne 0$ and $N(y) = 2 \ne 0$ whose product vanishes ($xy = 0$).
> 2. In particular, for the pair of two-component vectors $x = e_1 + e_{10}$ and $y = e_4 - e_{15}$, the Cayley–Dickson multiplication table gives the four pairwise products:
>    $$
>    e_1 e_4 = +e_5, \qquad e_{10} e_{15} = +e_5, \qquad e_{10} e_4 = -e_{14}, \qquad e_1 e_{15} = -e_{14}.
>    $$
>    Expanding the product $(e_1 + e_{10})(e_4 - e_{15})$ by bilinearity yields an exact zero:
>    $$
>    (e_1 + e_{10})(e_4 - e_{15}) = e_1 e_4 - e_1 e_{15} + e_{10} e_4 - e_{10} e_{15} = e_5 - (-e_{14}) + (-e_{14}) - e_5 = e_5 + e_{14} - e_{14} - e_5 = 0.
>    $$
>    A second independent integer witness is given by the pair $(e_3 + e_{10})(e_6 - e_{15}) = 0$. In total, among basis binomials of the form $(e_i \pm e_j)(e_k \pm e_l) = 0$ ($1 \le i < 8 < j \le 15$), there are exactly $84$ elementary zero-divisor quartets, generating inside $\mathbb{S}$ a compact manifold of normalized zero-divisor pairs homeomorphic to the exceptional Lie group $G_2$ of dimension $14$.

**Proof.**  
In the notation of Cayley–Dickson pairs $(a, b) = a + b e_8$ ($a, b \in \mathbb{O}$), we have $e_1 = (e_1, 0)$, $e_4 = (e_4, 0)$, $e_{10} = (0, e_2)$ ($10 = 8 + 2$), and $e_{15} = (0, e_7)$ ($15 = 8 + 7$). Using the formula $(a, b)(c, d) = (ac - \bar{d}b,\, da + b\bar{c})$ together with $\bar{e}_i = -e_i$ for $i \in \{1,\dots,7\}$ and the cyclic orientations of the Fano lines in $\mathcal{L}_{\mathrm{Fano}}$—$(1,4,5) \implies e_1 e_4 = +e_5$, $(2,5,7) \implies (7,2,5) \implies e_7 e_2 = +e_5$, $(2,4,6) \implies e_2 e_4 = +e_6$, and $(1,7,6) \implies (7,1,6)$ with reversed traversal $e_7 e_1 = -e_6$—we obtain directly without any change of sign convention:
$$
\begin{aligned}
(e_1 + e_{10})(e_4 - e_{15}) &= (e_1, e_2)(e_4, -e_7) = \bigl(e_1 e_4 - \overline{(-e_7)} e_2,\; (-e_7) e_1 + e_2 \bar{e}_4\bigr) \\
&= \bigl(e_1 e_4 - e_7 e_2,\; -e_7 e_1 - e_2 e_4\bigr) = \bigl(e_5 - e_5,\; -(-e_6) - e_6\bigr) = (0, 0).
\end{aligned}
$$
Similarly, for the second witness $(e_3 + e_{10})(e_6 - e_{15}) = (e_3, e_2)(e_6, -e_7)$, using the lines $(3,6,5) \implies e_3 e_6 = +e_5$, $(2,5,7) \implies e_7 e_2 = +e_5$, $(3,4,7) \implies e_7 e_3 = +e_4$, and $(2,4,6) \implies e_2 e_6 = -e_4$, we obtain $(e_3 e_6 - e_7 e_2,\, -e_7 e_3 - e_2 e_6) = (e_5 - e_5,\, -e_4 + e_4) = (0, 0)$. $\blacksquare$

---

## §II.5.4. $8$-Fold Bott Periodicity of Real Clifford Algebras $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$

Whereas in the Cayley–Dickson tower the step $8 \to 16$ destroys division without zero divisors owing to the loss of associativity, in the **associative** world of Clifford algebras generated by orthogonal anticommuting reflections $\gamma_1, \dots, \gamma_n$ ($\gamma_i^2 = -1$, $\gamma_i \gamma_j = -\gamma_j \gamma_i$ for $i \ne j$), dimension $8$ plays the role of an exact return period.

> **Proposition II.5.2 (Eightfold periodicity of real Clifford algebras and the isomorphism $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$).**  
> *Classical foundation.* Eightfold periodicity of real Clifford algebras $\mathrm{Cl}_{0,n+8} \cong \mathrm{Cl}_{0,n} \otimes \mathrm{Mat}_{16}(\mathbb{R})$ (Cartan, 1908; Bott, 1959; Atiyah–Bott–Shapiro, 1964) and Morita equivalence. *Contribution of this book:* Explicit integer realization of eight anticommuting skew-symmetric generators $\Gamma_1,\dots,\Gamma_8 \in \mathrm{Mat}_{16}(\mathbb{Z})$ built from left multiplication by octonion basis units.
> Over the field of real numbers $A = \mathbb{R}$, the associative Clifford algebras $\mathrm{Cl}_{0,n}$ of the negative-definite quadratic form $-x_1^2 - \cdots - x_n^2$ for $n = 0, 1, \dots, 8$ form the eight-periodic Morita–Bott sequence:
>
> | Number of generators $n$ | Dimension $2^n$ | Isomorphic matrix algebra $\mathrm{Cl}_{0,n}$ | Center of the algebra |
> | :---: | :---: | :---: | :---: |
> | $0$ | $1$ | $\mathbb{R}$ | $\mathbb{R}$ |
> | $1$ | $2$ | $\mathbb{C}$ | $\mathbb{C}$ |
> | $2$ | $4$ | $\mathbb{H}$ | $\mathbb{R}$ |
> | $3$ | $8$ | $\mathbb{H} \oplus \mathbb{H}$ | $\mathbb{R} \oplus \mathbb{R}$ |
> | $4$ | $16$ | $\mathrm{Mat}_2(\mathbb{H})$ | $\mathbb{R}$ |
> | $5$ | $32$ | $\mathrm{Mat}_4(\mathbb{C})$ | $\mathbb{C}$ |
> | $6$ | $64$ | $\mathrm{Mat}_8(\mathbb{R})$ | $\mathbb{R}$ |
> | $7$ | $128$ | $\mathrm{Mat}_8(\mathbb{R}) \oplus \mathrm{Mat}_8(\mathbb{R})$ | $\mathbb{R} \oplus \mathbb{R}$ |
> | $8$ | $256$ | $\mathrm{Mat}_{16}(\mathbb{R})$ | $\mathbb{R}$ |
>
> At $n = 8$, the algebra $\mathrm{Cl}_{0,8}$ of dimension $2^8 = 256$ is canonically isomorphic to the full matrix algebra $\mathrm{Mat}_{16}(\mathbb{R})$ (acting by left multiplications of imaginary octonions on the spinor space $\mathbb{O} \oplus \mathbb{O} \cong \mathbb{R}^{16}$), and further growth in the number of generators obeys the periodicity $\mathrm{Cl}_{0, n+8} \cong \mathrm{Cl}_{0,n} \otimes_{\mathbb{R}} \mathrm{Mat}_{16}(\mathbb{R})$. Moreover, over the base field $A = \mathbb{R}$, the $256$-dimensional algebra $\mathrm{Mat}_{16}(\mathbb{R})$ itself is equivalent to $\mathbb{R}$ only in the sense of **Morita equivalence** of module categories ($\mathbf{Mod}(\mathrm{Mat}_{16}(\mathbb{R})) \simeq \mathbf{Mod}(\mathbb{R})$), whereas the vector-space dimensions of the algebras themselves are distinct: $\dim_{\mathbb{R}} \mathrm{Cl}_{0,8} = 256 \ne 1 = \dim_{\mathbb{R}} \mathbb{R}$.

**Proof.**  
The seven operators $L_i : \mathbb{O} \to \mathbb{O}$ of left multiplication by the imaginary basis units of the octonions ($i = 1, \dots, 7$) are skew-symmetric and, by virtue of the alternativity $e_i(e_i x) = -x$, satisfy the relations $L_i^2 = -I_8$, $L_i L_j + L_j L_i = 0$ ($i \ne j$). The block $16 \times 16$ matrices
$$
\Gamma_i = \begin{pmatrix} 0 & L_i \\ L_i & 0 \end{pmatrix} \quad (1 \le i \le 7), \qquad
\Gamma_8 = \begin{pmatrix} 0 & -I_8 \\ I_8 & 0 \end{pmatrix}
$$
anticommute pairwise and satisfy $\Gamma_\alpha^2 = -I_{16}$ ($\alpha = 1, \dots, 8$), defining a representation of the simple algebra $\mathrm{Cl}_{0,8}$ inside $\mathrm{Mat}_{16}(\mathbb{R})$. Since $\dim_{\mathbb{R}} \mathrm{Cl}_{0,8} = 2^8 = 256 = 16^2 = \dim_{\mathbb{R}} \mathrm{Mat}_{16}(\mathbb{R})$, this homomorphism is an algebra isomorphism. $\blacksquare$

---

## §II.5.5. Chapter Summary and Bridge to Chapter II.6

The table below summarizes the results of `Chapter II.5` on algebras and signs.

#### Table II.5.2. From the Unsigned Fano Table to Octonions, the Paige Loop, and the Sedenion Barrier

| Stage and question of the observer | Mathematical object in `Chapter II.5` | Proved property |
| :--- | :--- | :--- |
| $7$ non-zero vectors of the charge space $\mathbb{F}_2^3 \setminus \{0\}$ without sign | Unsigned Fano table $e_i \star e_j = e_{i\oplus j}$ | Isomorphic to $\mathbb{F}_2[\mathbb{F}_2^3]$: **commutative and associative** (`Theorem II.5.1(1)`) |
| Orientation of the $7$ Fano lines with sign $\varepsilon_{ijk} = \pm 1$ | Cayley–Graves octonion algebra $\mathbb{O}$ | $168$ anti-associative Fano frames; alternativity and $N(xy)=N(x)N(y)$ (`Theorem II.5.1(2)`) |
| Modular reduction modulo $2$ | Zorn algebra $\mathrm{Oct}(\mathbb{F}_2)$ ($256$ elements) and core $V_6 = I^\perp/\langle I\rangle$ | Simple Moufang loop (Paige loop) of order $120 = 36 + 84$, $72$ idempotents, $\mathrm{Aut} = G_2(2)$ (`Theorem II.5.2`) |
| Fourth Cayley–Dickson step ($8 \to 16$) | Sedenions $\mathbb{S}$ | Loss of alternativity and zero divisors $(e_1+e_{10})(e_4-e_{15}) = 0$ (`Prop. II.5.1`) |
| Eight anticommuting reflections | Real Clifford algebra $\mathrm{Cl}_{0,8}$ | Isomorphism $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$ and Morita equivalence with $\mathbb{R}$ (`Prop. II.5.2`) |

In `Chapter II.5`, we saw how division algebras and matrix spinor representations grow out of finite Fano geometry and signed cocycles. The next step from `Table I.9.3` transfers the observer's operational contract $\Gamma$ into a finite-dimensional complex Hilbert space $\mathcal{H} = \mathbb{C}^d$: how do the four points of our base scene $S_4 = \mathbb{F}_2^2$ and the $16$ Boolean questions on it map into Hermitian qubit effects, and how does the Nerode theorem operate for quantum measurement branches? This is the subject of **Chapter `II.6`**.

---

## Summary Passport of Chapter II.5 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Theorem II.5.1` | Exhaustive enumeration of $512$ triples: $0$ associativity violations for the unsigned Fano table ($\cong \mathbb{F}_2[\mathbb{F}_2^3]$), $168$ anti-associative triples, and $0$ violations of alternativity and Moufang identities for the signed table $\mathbb{O}$ | `GATE-II05-01` |
| `Theorem II.5.2` (part 1) | Exhaustive enumeration of $\mathrm{Oct}(\mathbb{F}_2)$ ($256$ elements): $\omega(x,I) = \mathrm{tr}(x)$, $\dim V_6 = 6$, Paige loop $|M_{120}| = 120$, and partitions $64 + 56 = 36 + 84 = 120$ | `GATE-II05-02` |
| `Theorem II.5.2` (part 2) | $72$ non-trivial idempotents in $\mathrm{Oct}(\mathbb{F}_2)$, Moufang identity across all $120^3 = 1\,728\,000$ triples of $M_{120}$, hyperbolicity of the forms $q_e$ ($36$ zeros / $28$ ones on $V_6$), $\delta_4 q = 0$, and order $|G_2(2)| = 12\,096$ | `GATE-II05-03` |
| `Propositions II.5.1` and `II.5.2` | Exhaustive enumeration of all $84$ elementary zero-divisor quartets in $\mathbb{S}$ (including $(e_1+e_{10})(e_4-e_{15}) = 0$ and $(e_3+e_{10})(e_6-e_{15}) = 0$) and relations $\Gamma_\alpha \Gamma_\beta + \Gamma_\beta \Gamma_\alpha = -2\delta_{\alpha\beta}I_{16}$ in $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$ | `GATE-II05-04` |
