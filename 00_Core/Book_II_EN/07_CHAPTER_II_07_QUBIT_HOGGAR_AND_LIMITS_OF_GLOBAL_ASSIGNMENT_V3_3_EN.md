# Chapter II.7. Qubit, Hoggar, and Limits of Global Assignment: The `SIC` Tetrahedron, the Peres–Mermin Square, and Parity Charge $\kappa$

Fill a $3 \times 3$ table with the numbers $\pm 1$ so that the product along every row is $+1$ and the product along every column is also $+1$, except for the last column, where the product must be $-1$. Try it—and you will quickly see that it is impossible: the product of all nine numbers computed row by row equals $+1$, whereas computed column by column it equals $-1$. This chapter shows that operators on $\mathbb{C}^2 \otimes \mathbb{C}^2$ admit such a table, and explains why this represents a limit of *global assignment* of values by the observer rather than a paradox.

In `Chapter II.6`, we constructed the quantum operational contract of the observer $\Gamma$ in a finite-dimensional Hilbert space $\mathcal{H} = \mathbb{C}^d$ and proved (`Theorem II.6.1`) that the Walsh–Bloch map carries the $16$ Boolean tables of the four-point scene $S_4 = \mathbb{F}_2^2$ into Hermitian qubit operators with two critical thresholds: $\lambda = 1$ (where the $6$ two-point slices of the octahedron $O_6$ survive, yielding the three Pauli bases) and $\lambda = 1/\sqrt{3}$ (where the four single-point questions of the scene $S_4$ reach the boundary of the effect cone as rank-$1$ operators).

The present chapter takes the next step and ties together the **geometry of optimal quantum measurements** (`MUB` and `SIC-POVM` in dimensions $d = 2, 3, 8$) and the **cohomological theory of quantum contextuality**, bringing both backbone invariants of Book I—the four-point scene $S_4$ and the triple parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$—back to center stage:
1. we prove that at the threshold $\lambda = 1/\sqrt{3}$, the four single-point indicators $\delta_s$ ($s \in S_4$) form the regular `SIC-POVM` tetrahedron of a qubit, while the six two-point slices of the octahedron $O_6$ at the threshold $\lambda = 1$ form a complete family of $d+1 = 3$ mutually unbiased bases (`MUB`) of a qubit; we also explain precisely why the Klein four-group $V_4$ alone is insufficient to single out the regular tetrahedron and why a $3$-cycle permuting the coordinate axes is needed, generating the proper $\kappa$-preserving tetrahedral rotation group $A_4 = W(B_3)^+ \cap W(D_3)$;
2. next, we pass to dimensions $d = 3$ (the Hesse configuration of $9$ rays) and $d = 8$—the celebrated $64$ Hoggar lines (S. G. Hoggar, 1982, 1998) on three qubits $(\mathbb{C}^2)^{\otimes 3}$, constructed by the action of the Heisenberg–Weyl group on the three-bit Fano space $\mathbb{F}_2^3 \times \mathbb{F}_2^3$ from `Chapter II.5`, and compute in exact rational arithmetic their frame potentials $\Phi_2 = 1/36$ (a complex projective $2$-design) and $\Phi_3 = 11/648 > 1/120$;
3. we then compare **two parity obstructions to global assignment**: the prohibition against a global table of pre-existing answers in the Peres–Mermin square ($9$ two-qubit observables across $6$ contexts) and the non-triviality of the parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ of Book I (`Theorem I.9.3a`). Both prohibitions turn out to be **odd classes in a one-dimensional cokernel over $\mathbb{F}_2$** (the Abramsky–Mansfield–Barbosa *All-vs-Nothing* cohomological obstruction): every observable enters into exactly one row and one column (the analogue of $\partial_1 \partial_2 = 0$ from `Chapter II.3`), so the sum of local equations over all $6$ contexts vanishes identically modulo $2$, whereas the right-hand side yields an odd charge $1 \pmod 2$ (without claiming a direct identification of the classes $[\beta_{\mathrm{PM}}]$ and $[\kappa]$ in the absence of explicit chain maps between the complexes);
4. finally, on the partially ordered set (poset) of measurement contexts, we erect the strict Abramsky–Brandenburger sheaf-theoretic hierarchy (probabilistic $\subsetneq$ logical $\subsetneq$ strong contextuality), separating the Bell–`CHSH` model ($2\sqrt{2} > 2$), Hardy's model, and the Peres–Mermin square.

---

## §II.7.1. The Upper Bound $k \le d + 1$ for Mutually Unbiased Bases and the Qubit `SIC` Tetrahedron as the Four Points of the Scene $S_4$

Two orthonormal bases $\mathcal{B}^{(a)} = \{|e^{(a)}_i\rangle\}_{i=1}^d$ and $\mathcal{B}^{(b)} = \{|e^{(b)}_j\rangle\}_{j=1}^d$ of the space $\mathbb{C}^d$ are called *mutually unbiased* (`MUB`) if for all $i, j \in \{1, \dots, d\}$ the squared modulus of their inner product is constant:
$$
\bigl|\langle e^{(a)}_i | e^{(b)}_j \rangle\bigr|^2 = \mathrm{tr}\bigl(P^{(a)}_i P^{(b)}_j\bigr) = \frac{1}{d} \qquad (a \ne b).
$$
From the observer's standpoint, this expresses maximal mutual uninformativeness of two questions: if a state is prepared as an eigenvector of the basis $\mathcal{B}^{(a)}$, then reading in the basis $\mathcal{B}^{(b)}$ outputs the uniform distribution $(1/d, \dots, 1/d)$.

> **Proposition II.7.1 (Dimensional bound $k \le d + 1$ for `MUB` and explicit complete families at $d = 2, 3$).**  
> *Classical foundation.* The bound $k \le d + 1$ and complete families of mutually unbiased bases in prime-power dimensions are classical results of Ivanović (1981) and Wootters–Fields (1989). *Contribution of this book:* Formulation of explicit families at $d = 2, 3$ as sets of mutually complementary observer questions.
> 1. In the space $\mathbb{C}^d$ ($d \ge 2$), every family of pairwise mutually unbiased orthonormal bases contains at most $k \le d + 1$ bases.
> 2. At $d = 2$, the bound $k = 3$ is attained by the eigenbases of the three Pauli matrices $\sigma_x, \sigma_y, \sigma_z$, that is, precisely by the six projectors $E_1(q)$ of the two-point slices of the octahedron $O_6$ ($X_0, X_1, C_0, C_1, B_0, B_1$) at the threshold $\lambda = 1$ from `Theorem II.6.1`.
> 3. At $d = 3$, the bound $k = 4$ is attained by the computational basis $\{|0\rangle, |1\rangle, |2\rangle\}$ together with the three Gaussian bases $\mathcal{B}^{(m)}$ ($m \in \{0, 1, 2\} = \mathbb{F}_3$) with vectors
>    $$
>    |\psi^{(m)}_n\rangle = \frac{1}{\sqrt{3}} \sum_{q=0}^2 \omega^{m q^2 + n q}\,|q\rangle, \qquad \omega = e^{2\pi i / 3}, \quad n \in \{0, 1, 2\}.
>    $$

**Proof.**  
1. In each orthonormal basis $\mathcal{B}^{(a)}$, the traceless Hermitian matrices $\widetilde{P}^{(a)}_i = P^{(a)}_i - \frac{1}{d} I_d$ ($i = 1, \dots, d$) satisfy $\sum_{i=1}^d \widetilde{P}^{(a)}_i = 0$ and span a $(d-1)$-dimensional real subspace $V^{(a)}$ inside the $(d^2 - 1)$-dimensional space of traceless Hermitian matrices $\mathrm{Herm}_d^0(\mathbb{C})$. For $a \ne b$, the condition $\mathrm{tr}(P^{(a)}_i P^{(b)}_j) = \frac{1}{d}$ is equivalent to Hilbert–Schmidt orthogonality:
$$
\mathrm{tr}\bigl(\widetilde{P}^{(a)}_i \widetilde{P}^{(b)}_j\bigr) = \mathrm{tr}\bigl(P^{(a)}_i P^{(b)}_j\bigr) - \frac{1}{d} = 0.
$$
Therefore, $k$ pairwise orthogonal $(d-1)$-dimensional subspaces $V^{(1)} \perp \cdots \perp V^{(k)}$ fit inside a $(d^2 - 1)$-dimensional space only when $k(d - 1) \le d^2 - 1 = (d-1)(d+1)$, whence $k \le d + 1$.
2–3. At $d = 2$, the three Pauli axes are pairwise orthogonal in $\mathbb{R}^3$. At $d = 3$, the inner product of $|\psi^{(m)}_n\rangle$ and $|\psi^{(m')}_{n'}\rangle$ equals $\frac{1}{3}\sum_{q=0}^2 \omega^{(m'-m)q^2 + (n'-n)q}$: when $m' = m$, the linear sum of roots of unity equals $\delta_{n, n'}$, while when $m' \ne m$, the modulus of the quadratic Gauss sum modulo $3$ equals $\sqrt{3}$, yielding $|\langle \psi^{(m)}_n | \psi^{(m')}_{n'} \rangle|^2 = (\sqrt{3}/3)^2 = 1/3$. $\blacksquare$

Let us now see what happens in a qubit ($d = 2$) at the first threshold of `Theorem II.6.1`—$\lambda = 1/\sqrt{3}$, where the **four single-point questions** $\delta_s : S_4 \to \{0,1\}$ ($\delta_s(x) = 1 \iff x = s$) of our four-point scene $S_4 = \{00, 01, 10, 11\}$ reach the boundary of the effect cone.

> **Theorem II.7.1 (The qubit `SIC` tetrahedron as the four single-point questions of the scene $S_4$ and the role of the $3$-cycle in the group $A_4 = W(B_3)^+ \cap W(D_3)$).**  
> *Classical foundation.* The tetrahedron of four equiangular complex lines and symmetric informationally complete families have been studied previously (Zauner, 1999; Renes et al., 2004). *Contribution of this book:* Coincidence of the qubit `SIC` tetrahedron with the boundary points $2E_{1/\sqrt{3}}(\delta_s)$ of the four-state scene $S_4$.
> 1. At the critical threshold $\lambda = 1/\sqrt{3}$, the images of the four single-point indicators $\delta_s$ ($s \in S_4 = \{00, 01, 10, 11\}$) under the Walsh–Bloch map of `Theorem II.6.1`, multiplied by $2$, are rank-$1$ orthogonal projectors
>    $$
>    \Pi_s = 2\,E_{1/\sqrt{3}}(\delta_s) = \frac{1}{2}\bigl(I_2 + \mathbf{u}_s \cdot \boldsymbol{\sigma}\bigr), \qquad s \in S_4,
>    $$
>    whose unit Bloch vectors $\mathbf{u}_s \in S^2 \subset \mathbb{R}^3$ coincide with the four even vertices of the cube (the four filled faces $\kappa = 0$ of the octahedron $O_6$ from `Theorem II.4.1`):
>    $$
>    \begin{aligned}
>    \mathbf{u}_{00} &= \frac{1}{\sqrt{3}}(+1, +1, +1), \qquad & \mathbf{u}_{01} &= \frac{1}{\sqrt{3}}(+1, -1, -1), \\
>    \mathbf{u}_{10} &= \frac{1}{\sqrt{3}}(-1, +1, -1), \qquad & \mathbf{u}_{11} &= \frac{1}{\sqrt{3}}(-1, -1, +1).
>    \end{aligned}
>    $$
> 2. For any two distinct points $s \ne s'$ of the scene $S_4$, the inner product of the Bloch vectors equals $\langle \mathbf{u}_s, \mathbf{u}_{s'} \rangle = -\frac{1}{3}$, and the trace of the product of projectors is constant:
>    $$
>    \mathrm{tr}(\Pi_s \Pi_{s'}) = \frac{1}{2}\bigl(1 + \langle \mathbf{u}_s, \mathbf{u}_{s'} \rangle\bigr) = \frac{1}{2}\left(1 - \frac{1}{3}\right) = \frac{1}{3} = \frac{1}{d + 1} \qquad (s \ne s').
>    $$
>    Consequently, the quadruple of effects $M_s = \frac{1}{2}\Pi_s = E_{1/\sqrt{3}}(\delta_s)$ ($\sum_{s \in S_4} M_s = I_2$) forms the canonical symmetric informationally complete measurement (`SIC-POVM`) of a qubit—a regular tetrahedron on the Bloch sphere.
> 3. **(Why the Klein four-group $V_4$ is insufficient and a $3$-cycle is required).** The Klein four-group $V_4 = \{\mathrm{diag}(1,1,1),\, \mathrm{diag}(1,-1,-1),\, \mathrm{diag}(-1,1,-1),\, \mathrm{diag}(-1,-1,1)\} \subset \mathrm{SO}_3(\mathbb{R})$ maps any vector $(a, b, c) \in S^2$ to a quadruple of vectors $(a,b,c), (a,-b,-c), (-a,b,-c), (-a,-b,c)$ summing to zero ($\sum \mathbf{v}_s = 0$), yet **does not force** this quadruple to be a regular tetrahedron: for example, at $(a,b,c) = (3/5, 4/5, 0)$, the $V_4$-orbit forms a planar rectangle in the plane $z = 0$ with two distinct inner products $-7/25$ and $-1$. Equality of all six pairwise cosines $\langle \mathbf{u}_s, \mathbf{u}_{s'} \rangle = -1/3$ ($|a| = |b| = |c| = 1/\sqrt{3}$) is enforced precisely when one adjoins to the group $V_4$ the **$3$-cycle permuting the coordinate axes** ($x \mapsto y \mapsto z \mapsto x$), generating the proper $\kappa$-preserving tetrahedral group $A_4 = V_4 \rtimes C_3 = W(B_3)^+ \cap W(D_3)$.

**Proof.**  
By the Walsh character table (§II.6.2), for the single-point indicator $\delta_s$ we have $c_0(\delta_s) = 1/4$ and $c_j(\delta_s) = \frac{1}{4}\chi_j(s) = \pm \frac{1}{4}$, where the product of signs equals $\chi_1(s)\chi_2(s)\chi_3(s) = +1$. Multiplying by $2$ at $\lambda = 1/\sqrt{3}$ gives $\Pi_s = \frac{1}{2}(I_2 + \mathbf{u}_s \cdot \boldsymbol{\sigma})$ with $\mathbf{u}_s = \frac{1}{\sqrt{3}}(\chi_1(s), \chi_2(s), \chi_3(s))$ and $\|\mathbf{u}_s\|_2^2 = 3/3 = 1$. Since for $s \ne s'$ exactly two of the three characters change sign while one remains unchanged, the inner product equals $\frac{1}{3}(+1 - 1 - 1) = -\frac{1}{3}$. Finally, for an arbitrary $V_4$-orbit of a vector $(a,b,c) \in S^2$ ($a^2+b^2+c^2=1$), the three inner products with the non-trivial shifts in $V_4 \setminus \{I\}$ are $a^2 - b^2 - c^2 = 2a^2 - 1$, $2b^2 - 1$, and $2c^2 - 1$; they coincide with one another if and only if $a^2 = b^2 = c^2 = 1/3$, which is enforced by invariance under the $3$-cycle $(a,b,c) \mapsto (b,c,a)$. $\blacksquare$

---

## §II.7.2. The Hesse Configuration ($d = 3$) and the $64$ Hoggar Lines ($d = 8$) over the Fano Space $\mathbb{F}_2^3 \times \mathbb{F}_2^3$

In arbitrary dimension $d$, a family of $d^2$ rank-$1$ projectors $\{P_k = |\psi_k\rangle\langle\psi_k|\}_{k=1}^{d^2}$ in $\mathbb{C}^d$ is called *symmetric informationally complete* (`SIC-POVM`) if all pairwise overlaps between distinct rays are constant and equal to
$$
\mathrm{tr}(P_j P_k) = |\langle \psi_j | \psi_k \rangle|^2 = \frac{1}{d + 1} \qquad (j \ne k),
$$
which guarantees $\sum_{k=1}^{d^2} \frac{1}{d} P_k = I_d$ and the linear independence of all $d^2$ operators in $\mathrm{Herm}_d(\mathbb{C})$.

Alongside the qubit tetrahedron ($d = 2$, $d^2 = 4$), two exceptional analytic constructions occupy a central place in the geometry of finite groups:
1. **The Hesse configuration in dimension $d = 3$ ($d^2 = 9$ rays).** Let the Heisenberg–Weyl shift and phase operators $X|q\rangle = |q+1 \bmod 3\rangle$, $Z|q\rangle = \omega^q |q\rangle$ ($\omega = e^{2\pi i/3}$) act on $\mathbb{C}^3$. The orbit of the two-component fiducial vector
   $$
   |\psi_0\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \in \mathbb{C}^3
   $$
   under the $9$ operators $D_{a,b} = X^a Z^b$ ($a, b \in \mathbb{F}_3$) yields $9$ unit vectors $|\psi_{a,b}\rangle = D_{a,b}|\psi_0\rangle$ satisfying $|\langle \psi_0 | \psi_{a,b}\rangle|^2 = \frac{1}{4} = \frac{1}{d+1}$ for all $(a,b) \ne (0,0)$ (if $a = 0, b \ne 0$, then $|\frac{1}{2}(\omega^b + \omega^{2b})|^2 = |-1/2|^2 = 1/4$; if $a \ne 0$, exactly one term of modulus $1/2$ survives in the inner product). These $9$ rays form the inflection points of a cubic curve in the projective plane $\mathbb{C}P^2$—the classical *Hesse configuration* (O. Hesse, 1844).
2. **The $64$ Hoggar lines in dimension $d = 8$ ($d^2 = 64$ rays on three qubits, S. G. Hoggar, 1982, 1998).** In the $8$-dimensional space of three qubits $\mathcal{H} = (\mathbb{C}^2)^{\otimes 3} \cong \mathbb{C}^8$, whose computational basis states $|x\rangle$ ($x \in \mathbb{F}_2^3$) are indexed by the vertices of the three-bit Fano cube from `Chapter II.5`, the $64$-element group of $3$-qubit Pauli operators acts via
   $$
   D_{a,b} = (\sigma_x^{a_1}\sigma_z^{b_1}) \otimes (\sigma_x^{a_2}\sigma_z^{b_2}) \otimes (\sigma_x^{a_3}\sigma_z^{b_3}), \qquad (a, b) \in \mathbb{F}_2^3 \times \mathbb{F}_2^3,
   $$
   mapping a basis vector $|x\rangle$ to $(-1)^{\langle b, x\rangle} |x \oplus a\rangle$ (precisely the $6$-dimensional symplectic space $V_6 \cong \mathbb{F}_2^6$ from `Theorem II.5.2`).

> **Theorem II.7.2 (The Hoggar lines in $\mathbb{C}^8$, the Gram matrix algebra, and the frame potentials $\Phi_2 = 1/36$, $\Phi_3 = 11/648$).**  
> *Classical foundation.* Hoggar's sixty-four equiangular lines (1982) and frame potentials (Welch, 1974; Benedetto–Fickus, 2003) are classical constructions. *Contribution of this book:* Exact matrix calculation in $\mathbb{Q}(i)$ and verification of the third frame-potential gap $\Phi_3 - \Phi_3^{\mathrm{Welch}} = 7/810 > 0$.
> In $\mathbb{C}^8$, choose the Gaussian integer Hoggar fiducial vector (with squared norm $\|\tilde{\varphi}\|^2 = 5 + 7 \cdot 1 = 12$)
> $$
> |\varphi_0\rangle = \frac{1}{\sqrt{12}}\,\tilde{\varphi}, \qquad \tilde{\varphi} = (-1 + 2i,\, 1,\, 1,\, 1,\, 1,\, 1,\, 1,\, 1)^{\mathsf{T}} \in \mathbb{Z}[i]^8,
> $$
> and set $|\varphi_{a,b}\rangle = D_{a,b}|\varphi_0\rangle$, $P_{a,b} = |\varphi_{a,b}\rangle\langle\varphi_{a,b}|$ for all $64$ pairs $(a, b) \in \mathbb{F}_2^3 \times \mathbb{F}_2^3$.
> 1. For all $63$ non-zero pairs $(a,b) \ne (0,0)$, the squared modulus of the Gaussian inner product $|\langle \tilde{\varphi} | D_{a,b} \tilde{\varphi} \rangle|^2$ is identically equal to $16$ ($|\pm 4|^2 = 16$ or $|\pm 4i|^2 = 16$), whence for the normalized rays
>    $$
>    \mathrm{tr}(P_{a,b} P_{a',b'}) = |\langle \varphi_{a,b} | \varphi_{a',b'} \rangle|^2 = \frac{16}{12^2} = \frac{16}{144} = \frac{1}{9} = \frac{1}{d + 1} \qquad \bigl((a,b) \ne (a',b')\bigr).
>    $$
> 2. The sum of all $64$ projectors is a scalar multiple of the identity matrix: $F = \sum_{a,b} P_{a,b} = 8 I_8$ ($\mathrm{tr}\,F = 64$, $\mathrm{tr}(F^2) = 512$). Let $G_{\mathrm{frame}} = (\langle \varphi_\alpha | \varphi_\beta \rangle)_{1 \le \alpha,\beta \le 64} \in \mathbb{Q}(i)^{64 \times 64}$ be the complex Gram matrix of inner products of the rays. Then $G_{\mathrm{frame}}^2 = 8 G_{\mathrm{frame}}$ and $\operatorname{rank} G_{\mathrm{frame}} = 8$. The Hermitian phase matrix $S = 3(G_{\mathrm{frame}} - I_{64})$ has zero diagonal and off-diagonal entries of modulus $1$ in $\mathbb{Q}(i)$, and satisfies the quadratic equation over $\mathbb{Q}(i)$:
>    $$
>    S^2 = 63 I_{64} + 18 S.
>    $$
>    By contrast, the matrix of squared moduli $H_{\alpha\beta} = \mathrm{tr}(P_\alpha P_\beta) = |\langle \varphi_\alpha | \varphi_\beta \rangle|^2 = \frac{8}{9}\delta_{\alpha\beta} + \frac{1}{9}$ has full rank $64$ and does not satisfy this equation.
> 3. **(Projective design threshold: $2$-design, but not $3$-design).** The normalized frame potential of order $t$ of the Hoggar family, $\Phi_t = \frac{1}{64^2} \sum_{\alpha,\beta} |\langle \varphi_\alpha | \varphi_\beta \rangle|^{2t}$, compares with the Welch lower bound $\Phi_t^{\mathrm{Welch}} = \binom{d+t-1}{t}^{-1}$ as follows:
>    - at $t = 2$:
>      $$
>      \Phi_2 = \frac{1}{64}\left(1 + 63 \cdot \frac{1}{9^2}\right) = \frac{1}{64}\left(1 + \frac{7}{9}\right) = \frac{16}{64 \cdot 9} = \frac{1}{36} = \binom{8+2-1}{2}^{-1} = \Phi_2^{\mathrm{Welch}},
>      $$
>      so the $64$ Hoggar lines form an exact complex projective $2$-design;
>    - at $t = 3$:
>      $$
>      \Phi_3 = \frac{1}{64}\left(1 + 63 \cdot \frac{1}{9^3}\right) = \frac{1}{64}\left(1 + \frac{7}{81}\right) = \frac{88}{64 \cdot 81} = \frac{11}{648} > \frac{1}{120} = \binom{8+3-1}{3}^{-1} = \Phi_3^{\mathrm{Welch}},
>      $$
>      so at third order a strictly positive gap $\Phi_3 - \Phi_3^{\mathrm{Welch}} = \frac{11}{648} - \frac{1}{120} = \frac{28}{3240} = \frac{7}{810} > 0$ appears, and the Hoggar lines (like any `SIC-POVM`) do not form a projective $3$-design.

**Proof.**  
1. Let $(a,b) \ne (0,0)$. If $a = 0$ and $b \ne 0$, the character $(-1)^{\langle b, x\rangle}$ equals $+1$ at $x = 000$ and takes the value $+1$ three times and $-1$ four times on the $7$ non-zero points of $\mathbb{F}_2^3 \setminus \{0\}$, so $\langle \tilde{\varphi} | D_{0,b} \tilde{\varphi} \rangle = |{-1+2i}|^2 + (3 - 4)\cdot 1^2 = 5 - 1 = 4$, and $|4|^2 = 16$. If $a \ne 0$, then in the sum $\langle \tilde{\varphi} | D_{a,b} \tilde{\varphi} \rangle = \sum_{x \in \mathbb{F}_2^3} \overline{\tilde{\varphi}_{x \oplus a}}\,(-1)^{\langle b,x\rangle}\tilde{\varphi}_x$, the pair of points $\{0, a\}$ contributes $(-1+2i) + (-1)^{\langle b,a\rangle}(-1-2i)$ (which equals $-2$ when $\langle b,a\rangle = 0$ and $4i$ when $\langle b,a\rangle = 1$), while the remaining $6$ points $x \notin \{0, a\}$ contribute the character sum $\sum_{x \notin \{0,a\}} (-1)^{\langle b,x\rangle}$, which equals $6$ when $b = 0$, $-2$ when $b \ne 0, \langle b,a\rangle = 0$, and $0$ when $b \ne 0, \langle b,a\rangle = 1$. In all three cases, the inner product $\langle \tilde{\varphi} | D_{a,b} \tilde{\varphi} \rangle \in \{4, -4, 4i\}$ has squared modulus $16$ (which is also verified across all $63$ pairs in gate `GATE-II07-02`). Dividing by $12^2 = 144$ gives $|\langle \varphi_{a,b} | \varphi_{a',b'} \rangle|^2 = 16/144 = 1/9$.
2–3. The frame identity $F = \sum_{\alpha=1}^{64} |\varphi_\alpha\rangle\langle\varphi_\alpha| = 8 I_8$ means that the matrix $V \in \mathbb{C}^{8 \times 64}$ with columns $|\varphi_\alpha\rangle$ satisfies $V V^\dagger = 8 I_8$. Therefore, the complex Gram matrix $G_{\mathrm{frame}} = V^\dagger V \in \mathbb{Q}(i)^{64 \times 64}$ with entries $\langle \varphi_\alpha | \varphi_\beta \rangle$ has rank $\operatorname{rank} G_{\mathrm{frame}} = \operatorname{rank} V = 8$ and satisfies $G_{\mathrm{frame}}^2 = V^\dagger (V V^\dagger) V = 8 G_{\mathrm{frame}}$. Substituting $G_{\mathrm{frame}} = I_{64} + \frac{1}{3} S$ into the identity $G_{\mathrm{frame}}^2 = 8 G_{\mathrm{frame}}$ yields over $\mathbb{Q}(i)$:
$$
\left(I_{64} + \frac{1}{3} S\right)^2 = 8\left(I_{64} + \frac{1}{3} S\right) \Longleftrightarrow \frac{1}{9} S^2 = 7 I_{64} + 2 S \Longleftrightarrow S^2 = 63 I_{64} + 18 S.
$$
Meanwhile, the real matrix of squared moduli $H = \frac{8}{9}I_{64} + \frac{1}{9}J_{64}$ has eigenvalues $\frac{8}{9} + \frac{64}{9} = 8$ (with multiplicity $1$) and $\frac{8}{9}$ (with multiplicity $63$), so $\operatorname{rank} H = 64$ and $H^2 \ne 8H$. Finally, since for each of the $64$ rays the sum of the $2t$-th powers of the moduli of inner products with all $64$ rays equals $1 + 63 \cdot 9^{-t}$, the normalized frame potential equals $\Phi_t = (1 + 63 \cdot 9^{-t}) / 64$, which at $t = 2, 3$ gives $\Phi_2 = 1/36 = \Phi_2^{\mathrm{Welch}}$ and $\Phi_3 = 11/648$, with $\Phi_3 - \Phi_3^{\mathrm{Welch}} = 11/648 - 1/120 = 28/3240 = 7/810 > 0$. $\blacksquare$

---

## §II.7.3. The Peres–Mermin Square and the Parity Charge $\kappa$ of Book I: Odd Classes in a One-Dimensional Cokernel over $\mathbb{F}_2$

Let us turn to the second main theme of the chapter—the prohibition against the existence of a single pre-existing table of answers for families of pairwise compatible quantum questions (the Kochen–Specker theorem in the form of the Peres–Mermin square). We will show that both this quantum prohibition and the non-triviality of the torsor presheaf $\mathcal{S}_w$ with parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ from `Chapter I.9` and `Chapter II.3` are **odd classes in a one-dimensional cokernel over $\mathbb{F}_2$**, arising from the twofold cancellation of every local variable upon summing over all contexts.

Consider in the $4$-dimensional space of two qubits $\mathcal{H} = \mathbb{C}^2 \otimes \mathbb{C}^2$ the $3 \times 3$ table of nine Hermitian unitary observables $A_{ij}$ with spectrum $\{\pm 1\}$ (**the Peres–Mermin magic square**, A. Peres, 1990; N. D. Mermin, 1990):

| Context | Column $C_1$ | Column $C_2$ | Column $C_3$ | Row product |
| :--- | :---: | :---: | :---: | :---: |
| **Row $R_1$** | $A_{11} = \sigma_z \otimes I_2$ | $A_{12} = I_2 \otimes \sigma_z$ | $A_{13} = \sigma_z \otimes \sigma_z$ | $A_{11} A_{12} A_{13} = +I_4$ |
| **Row $R_2$** | $A_{21} = I_2 \otimes \sigma_x$ | $A_{22} = \sigma_x \otimes I_2$ | $A_{23} = \sigma_x \otimes \sigma_x$ | $A_{21} A_{22} A_{23} = +I_4$ |
| **Row $R_3$** | $A_{31} = \sigma_z \otimes \sigma_x$ | $A_{32} = \sigma_x \otimes \sigma_z$ | $A_{33} = \sigma_y \otimes \sigma_y$ | $A_{31} A_{32} A_{33} = +I_4$ |
| **Column product** | $A_{11} A_{21} A_{31} = +I_4$ | $A_{12} A_{22} A_{32} = +I_4$ | $A_{13} A_{23} A_{33} = \mathbf{-I_4}$ | **Odd charge $\kappa = 1$.** |

Let us check the operator products in this table:
1. Within each of the three rows $R_1, R_2, R_3$ and within each of the three columns $C_1, C_2, C_3$, all three operators **commute pairwise** (since they either act on different tensor factors or anticommute simultaneously on both factors: $(\sigma_z \otimes \sigma_x)(\sigma_x \otimes \sigma_z) = (i\sigma_y)\otimes(-i\sigma_y) = \sigma_y \otimes \sigma_y = (\sigma_x \otimes \sigma_z)(\sigma_z \otimes \sigma_x)$). Therefore, each row $R_i$ and each column $C_j$ forms an admissible **jointly measurable context** for the observer.
2. Across all three rows $R_1, R_2, R_3$ and the first two columns $C_1, C_2$, the product of the three operators of the context equals $+I_4$.
3. In the third column $C_3$, however, the product of the operators equals:
   $$
   A_{13} A_{23} A_{33} = (\sigma_z \otimes \sigma_z)(\sigma_x \otimes \sigma_x)(\sigma_y \otimes \sigma_y) = (\sigma_z \sigma_x \sigma_y) \otimes (\sigma_z \sigma_x \sigma_y) = (i I_2) \otimes (i I_2) = i^2 I_4 = -I_4!
   $$

Let us now translate the multiplicative outcomes $\{\pm 1\}$ into additive bits $b_{ij} \in \mathbb{F}_2 = \{0,1\}$ via the rule $(-1)^{b_{ij}} \in \{\pm 1\}$. Then in any quantum state $|\Psi\rangle \in \mathbb{C}^4$, joint measurement of any of the six contexts must yield a bit triple satisfying an even equation in five contexts and an odd equation in the sixth:
$$
\begin{aligned}
(R_1):\quad b_{11} \oplus b_{12} \oplus b_{13} &= 0, \qquad & (C_1):\quad b_{11} \oplus b_{21} \oplus b_{31} &= 0, \\
(R_2):\quad b_{21} \oplus b_{22} \oplus b_{23} &= 0, \qquad & (C_2):\quad b_{12} \oplus b_{22} \oplus b_{32} &= 0, \\
(R_3):\quad b_{31} \oplus b_{32} \oplus b_{33} &= 0, \qquad & (C_3):\quad b_{13} \oplus b_{23} \oplus b_{33} &= \mathbf{1}.
\end{aligned}
$$

> **Theorem II.7.3 (Parity obstruction in the Peres–Mermin square and its comparison with the charge $\kappa$ of Book I).**  
> *Classical foundation.* The Peres–Mermin square (1990) and the Abramsky–Brandenburger sheaf-theoretic description of contextuality (2011) are published classical results. *Contribution of this book:* Exact comparison with the parity obstruction $\kappa$ in the one-dimensional cokernel over $\mathbb{F}_2$ and the three-level hierarchy of global sections $|\mathcal{S}_e(X)| = 16 \supsetneq 5 \supsetneq 0$.
> Let $\mathcal{K}_{\mathrm{PM}}$ be the bipartite incidence complex of the Peres–Mermin square ($9$ variables $b_{ij}$ as "edges," each entering into exactly two of the $6$ contexts—one row $R_i$ and one column $C_j$—and the $6$ contexts as "faces" of the coboundary operator $\delta : \mathbb{F}_2^9 \to \mathbb{F}_2^6$).
> 1. Since each of the $9$ variables $b_{ij}$ enters into exactly one row $R_i$ and into exactly one column $C_j$, the sum of all six equations on the left-hand side vanishes identically in $\mathbb{F}_2$ for **every** global assignment table $b \in \mathbb{F}_2^9$ (the cancellation law of a twice-traversed boundary $\partial_1 \partial_2 = 0$ from `Chapter II.3`):
>    $$
>    \sum_{i=1}^3 (\delta b)(R_i) \;\oplus\; \sum_{j=1}^3 (\delta b)(C_j) = 2 \sum_{i,j=1}^3 b_{ij} \equiv 0 \pmod 2.
>    $$
> 2. Meanwhile, the right-hand side of the quantum operator identities $\beta = (0, 0, 0,\, 0, 0, 1)^{\mathsf{T}} \in \mathbb{F}_2^6$ has total parity charge
>    $$
>    \kappa_{\mathrm{PM}} = 0 \oplus 0 \oplus 0 \oplus 0 \oplus 0 \oplus 1 = 1 \ne 0 \pmod 2.
>    $$
>    Consequently, the vector $\beta$ does not lie in the image of the coboundary operator $\operatorname{Im}\delta$ (it defines the non-zero cohomology class $[\beta] \ne 0$ in $\operatorname{Coker}\delta = \mathbb{F}_2^6 / \operatorname{Im}\delta \cong \mathbb{F}_2$, $\operatorname{rank}\delta = 5$; see S. Abramsky, R. Mansfield, and R. S. Barbosa, 2012), and the presheaf of locally admissible quantum outcomes $\mathcal{S}_{\mathrm{PM}}$ is a locally non-empty $\mathbb{F}_2^2$-torsor possessing no global section whatsoever:
>    $$
>    \mathcal{S}_{\mathrm{PM}}(X) = \varnothing \qquad \text{(regardless of the quantum state } \rho \in \mathcal{S}(\mathbb{C}^4)\text{!)}.
>    $$
> 3. Both prohibitions—the quantum Peres–Mermin prohibition and the combinatorial prohibition on the nerve of six slices $O_6$ from `Theorem I.9.3a` and `Theorem II.3.1`—are odd classes in a one-dimensional cokernel over $\mathbb{F}_2$: the local equations are consistent, whereas the sum over all contexts equals $1 \pmod 2$ owing to the twofold cancellation of every local variable ($b \oplus b = 0$). Direct identification of the class $[\beta_{\mathrm{PM}}]$ with the class $[\kappa]$ on the nerve $\mathcal{N}(O_6)$ is not claimed unless explicit chain maps between the complexes are specified.

**Proof.**  
Adding modulo $2$ the three row equations $\bigoplus_{j=1}^3 b_{ij} = 0$ and the three column equations $\bigoplus_{i=1}^3 b_{ij} = \delta_{j,3}$ for any putative global table $b \in \mathbb{F}_2^9$ yields $\bigoplus_{i,j=1}^3 (b_{ij} \oplus b_{ij}) = 0$ on the left-hand side and $0 \oplus 0 \oplus 0 \oplus 0 \oplus 0 \oplus 1 = 1$ on the right-hand side, a contradiction $0 = 1$. $\blacksquare$

---

## §II.7.4. The Sheaf-Theoretic Hierarchy of Contextuality on the Context Poset and Tsirelson's Bound $2\sqrt{2}$

To classify all intermediate regimes between complete classical gluing and the rigid logical prohibition of Peres–Mermin, consider the partially ordered set (poset) of measurement contexts $\mathcal{M}$ and the distribution presheaf $\mathcal{D}(\mathcal{E}) : \mathcal{M}^{\mathrm{op}} \to \mathbf{Set}$ (S. Abramsky and A. Brandenburger, *New J. Phys.* 13, 113036, 2011).

Let $e = \{e_C\}_{C \in \mathcal{M}}$ be an empirical model—a family of local probability distributions satisfying the **no-signaling (pairwise marginal compatibility) condition**: for any two contexts $C, C' \in \mathcal{M}$, the marginal distributions on their intersection $C \cap C'$ agree ($e_C|_{C \cap C'} = e_{C'}|_{C \cap C'}$). Define the support of the model on a context $C$ as the subset of outcomes with positive probability: $S_e(C) = \{ s \in \mathcal{E}(C) : e_C(s) > 0 \}$.

A strict three-tier sheaf-theoretic hierarchy of obstructions to global gluing arises:
1. **Probabilistic contextuality (violation of Bell inequalities):** there exists no single global probability distribution $d \in \mathcal{D}(\mathcal{E}(X))$ whose marginals on all contexts $C \in \mathcal{M}$ equal $e_C$.
2. **Logical (possibilistic) contextuality (Hardy's model):** in some context $C_0$, there exists a possible local outcome $s_0 \in S_e(C_0)$ ($e_{C_0}(s_0) > 0$) that cannot be extended to any global section of the support presheaf $S_e(X)$ (compatible with all $S_e(C)$).
3. **Strong contextuality (the Peres–Mermin square and the Popescu–Rohrlich box):** the set of global sections of the support presheaf is empty altogether:
   $$
   S_e(X) = \varnothing,
   $$
   meaning that **not a single** locally possible outcome extends to a global table of answers compatible with the supports of all contexts.

Each successive property is strictly stronger than the preceding one:
$$
\text{Strong contextuality} \;\Longrightarrow\; \text{Logical contextuality} \;\Longrightarrow\; \text{Probabilistic contextuality},
$$
and the converse implications **do not hold**, as confirmed by the classical Bell–`CHSH` inequality for four correlators of two parties $(A_0, A_1)$ and $(B_0, B_1)$ with values $\pm 1$:
$$
S_{\mathrm{CHSH}} = \langle A_0 B_0 \rangle + \langle A_0 B_1 \rangle + \langle A_1 B_0 \rangle - \langle A_1 B_1 \rangle.
$$
- For any global classical table $(a_0, a_1, b_0, b_1) \in \{\pm 1\}^4$, the quantity $a_0(b_0 + b_1) + a_1(b_0 - b_1)$ equals $\pm 2$ (since one of the parentheses $b_0 \pm b_1$ equals $0$ and the other equals $\pm 2$), whence the classical bound is $|S_{\mathrm{CHSH}}| \le 2$.
- In the Hilbert space model, for the operator $\widehat{S} = A_0 \otimes (B_0 + B_1) + A_1 \otimes (B_0 - B_1)$, the Landau–Tsirelson identity
  $$
  \widehat{S}^2 = 4 I_4 - [A_0, A_1] \otimes [B_0, B_1]
  $$
  together with the commutator norm bound $\|[A_0, A_1]\| \le 2$ yields the exact quantum Tsirelson bound $\|\widehat{S}\| \le \sqrt{4 + 4} = 2\sqrt{2} \approx 2.8284$, which is attained on the singlet state for the Pauli angle choices $A_0 = \sigma_z$, $A_1 = \sigma_x$, $B_0 = \frac{\sigma_z + \sigma_x}{\sqrt{2}}$, $B_1 = \frac{\sigma_z - \sigma_x}{\sqrt{2}}$ (where all four signed correlators equal $\frac{1}{\sqrt{2}}$ and their sum equals $4 \cdot \frac{1}{\sqrt{2}} = 2\sqrt{2} > 2$).
- At the same time, in the optimal quantum Tsirelson model, all $4$ local outcomes $(\pm 1, \pm 1)$ in each of the $4$ contexts have strictly positive probability $\frac{2 \pm \sqrt{2}}{8} > 0$, so the local support $S_e(C) = \{\pm 1\}^2$ is full. Therefore, the optimal Tsirelson model is **probabilistically contextual** ($2\sqrt{2} > 2$) yet **not logically contextual** ($|S_e(X)| = 16$).
- Conversely, on the unnormalized integer two-qubit Hardy state $|\tilde{\Psi}_{\mathrm{H}}\rangle = |01\rangle + |10\rangle + |11\rangle \in \mathbb{Z}^4$ ($\|\tilde{\Psi}_{\mathrm{H}}\|^2 = 3$) with Pauli observables $A_0 = B_0 = \sigma_z$ and $A_1 = B_1 = \sigma_x$, all context probabilities are exact rationals: $e_{A_0 B_0}(+1,+1) = 0$, $e_{A_0 B_1}(-1,-1) = 0$, and $e_{A_1 B_0}(-1,-1) = 0$, whereas in the fourth context the outcome $(-1,-1)$ has positive probability $e_{A_1 B_1}(-1,-1) = \frac{1}{12} > 0$. This outcome cannot be extended to any global assignment $(a_0, a_1, b_0, b_1) \in \{\pm 1\}^4$ (since $a_1 = b_1 = -1$ forces $a_0 = +1$ via $e_{A_0 B_1}(-1,-1) = 0$ and $b_0 = +1$ via $e_{A_1 B_0}(-1,-1) = 0$, contradicting $e_{A_0 B_0}(+1,+1) = 0$), while exactly $|S_e(X)| = 5 > 0$ global assignments survive: Hardy's model is **logically contextual yet not strongly contextual**, whereas the Peres–Mermin square is **strongly contextual** ($|S_e(X)| = 0$).

---

## §II.7.5. Historical-Philosophical Parallel: Discriminative Insight *Viveka-khyāti* (`YS 2.26`, `SK 64`) and Context-Dependence of Answers

In the second chapter of the *Yoga Sūtras* (`YS 2.26`) and in the concluding portion of the *Sāṃkhyakārikā* (`SK 64`), the central instrument of liberation from illusory conflation is called *viveka-khyāti*—unwavering discriminative recognition (*viveka-khyātir aviplavā hānopāyaḥ*), which maintains the boundary between the pure witness and the intertwined regimes of instrumental experience.

In the methodology of the present chapter (outside the premises of the quantum theorems), this motif warns against naive classical realism, which demands that the answer $b_{ij} \in \{0,1\}$ to the question $A_{ij}$ "already lie inside the box on its own" prior to specifying in which context—along row $R_i$ or along column $C_j$—this question is asked together with its compatible neighbors. Theorem II.7.3 shows that relinquishing a pre-existing global table entails neither arbitrariness nor the collapse of logic: within each individual context, the laws of Boolean logic hold strictly, while the impossibility of merging them into a single global sheet is measured by the exact cohomological invariant $\kappa_{\mathrm{PM}} = 1 \in \operatorname{Coker}\delta \cong \mathbb{F}_2$.

---

## §II.7.6. Chapter Summary and Bridge to Chapter II.8

The table below summarizes the results of `Chapter II.7` on quantum states and measurement contexts.

#### Table II.7.1. Geometry of Question Packings and Cohomology of Contextuality in Chapter II.7

| Construction and dimension | Connection to the backbone of Book I ($S_4, O_6, \kappa$) | Proved mathematical result |
| :--- | :--- | :--- |
| `MUB` at $d = 2, 3$ (`Prop. II.7.1`) | The six slices of the octahedron $O_6$ at $\lambda = 1$ yield the $3$ Pauli bases of a qubit | Bound $k \le d + 1$ and attainability $k=3$ ($d=2$), $k=4$ ($d=3$, Gauss sums) |
| Qubit `SIC` tetrahedron at $d = 2$ (`Theorem II.7.1`) | The four single-point questions $\delta_s$ ($s \in S_4$) at $\lambda = 1/\sqrt{3}$ | Bloch vectors $\mathbf{u}_s$ form the even tetrahedron $\kappa = 0$ with $\langle \mathbf{u}_s, \mathbf{u}_{s'}\rangle = -1/3$; role of the $3$-cycle in $A_4 = W(B_3)^+ \cap W(D_3)$ |
| Hesse configuration ($d=3$) and $64$ Hoggar lines ($d=8$, `Theorem II.7.2`) | Heisenberg–Weyl group on $V_6 = \mathbb{F}_2^3 \times \mathbb{F}_2^3$ from `Chapter II.5` | Overlaps $1/9$, $G_{\mathrm{frame}}^2 = 8 G_{\mathrm{frame}} \implies S^2 = 63I + 18S$; $2$-design ($\Phi_2 = 1/36$), but not $3$-design ($\Phi_3 = 11/648 > 1/120$) |
| Peres–Mermin square (`Theorem II.7.3`) | Comparison of odd obstructions in a one-dimensional cokernel with the charge $\kappa = x_0 \oplus c_0 \oplus b_0$ | Every variable enters twice ($\sum \delta b \equiv 0 \pmod 2$, $\operatorname{rank}\delta = 5$), while the right-hand side has odd charge $\kappa_{\mathrm{PM}} = 1 \implies \mathcal{S}_{\mathrm{PM}}(X) = \varnothing$ |
| Sheaf-theoretic hierarchy of contextuality (`§II.7.4`) | Gradation of gluing obstructions on the context poset $\mathcal{M}$ | Strict chain $|S_e(X)| = 16$ (Tsirelson, $2\sqrt{2} > 2$) $\supsetneq$ $|S_e(X)| = 5$ (Hardy, $1/12 > 0$) $\supsetneq$ $|S_e(X)| = 0$ (Peres–Mermin) |

From finite families of incompatible quantum contexts we pass in **Chapter `II.8`** to the fourth enrichment from `Table I.9.3`: how the observer transitions from discrete graphs and simplicial nerves (such as the octahedron $O_6$) to refined cellular meshes, semi-discrete gradient flows with spontaneous two-level value splitting, and exact rational `SOS` certificates of polynomial non-negativity on the $21$-dimensional flag space of the Fano plane.

---

## Summary Passport of Chapter II.7 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Proposition II.7.1` and `Theorem II.7.1` | Verification of `MUB` at $d=2,3$, coincidence of the qubit `SIC` tetrahedron with $2 E_{1/\sqrt{3}}(\delta_s)$ ($s \in S_4$), the planar $V_4$-orbit counterexample $(3/5, 4/5, 0)$, and the Hesse configuration at $d=3$ | `GATE-II07-01` |
| `Theorem II.7.2` | Complete computation of the $64$ Hoggar lines in exact Gaussian arithmetic $\mathbb{Q}(i)$: all $63$ overlaps equal $16/144 = 1/9$, $F = 8I_8$, $S^2 = 63I_{64} + 18S$, $\Phi_2 = 1/36$, and $\Phi_3 = 11/648 > 1/120$ | `GATE-II07-02` |
| `Theorem II.7.3` | Verification of commutativity and products $\pm I_4$ in the Peres–Mermin square, vanishing of the sum of rows of the matrix $\delta \bmod 2$, and absence of a solution $\delta b = \beta$ among all $2^9 = 512$ tables $b \in \mathbb{F}_2^9$ | `GATE-II07-03` |
| `§II.7.4` | Exact verification over $\mathbb{Q}(\sqrt{2})$ and $\mathbb{Q}$: Tsirelson's bound $S_{\mathrm{CHSH}} = 2\sqrt{2} > 2$ ($|S_e(X)| = 16$), rational Hardy model ($e_{A_1 B_1}(-1,-1) = 1/12 > 0$, $|S_e(X)| = 5$), and strong contextuality ($|S_e(X)| = 0$) | `GATE-II07-04` |
