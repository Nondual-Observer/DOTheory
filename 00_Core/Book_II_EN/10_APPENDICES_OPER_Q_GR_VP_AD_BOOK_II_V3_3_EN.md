# Appendices to Book II (Canonical Edition `v3.3`)

This file brings together the five canonical appendices to the Second Volume of the monograph ("Book II. Memory, Continuous Continuation, Gluing, and the Quantum Scene"):
1. **Appendix `OPER`** — operator derivations for Ho–Kalman linear memory, Cayley–Padé jets, the Smith normal form of simplicial complexes, and the symmetry group of the observer's octahedron $W(B_3) = \mathrm{Aut}(O_6)$ (for `Chapters II.1–II.4`);
2. **Appendix `Q`** — multiplication tables of octonions and sedenions, anatomy of the modular octonions $\mathrm{Oct}(\mathbb{F}_2)$ and the Paige loop, the Walsh–Bloch bridge on $S_4$, the $64$ Hoggar lines in $\mathbb{C}^8$, the cohomological calculation of the Peres–Mermin square, and the Veronese decomposition $84 + 1687 = 1771$ on Fano flags (for `Chapters II.5–II.9`);
3. **Appendix `GR-II`** — atlas of text diagrams and figures of Book II with mathematical explanations;
4. **Appendix `VP-II`** — how to verify the book independently: the launch command for the single-threaded script `11_verify_full_book_II_v3_3.jl`, the pass criterion, and the master passport of all `38` verification gates;
5. **Appendix `AD-II`** — concordance of notation, sign conventions, and units of measurement of Book II.

---

## Appendix OPER. Operator Memory, Cayley Jets, Smith Normal Form, and the Octahedral Group (for Chapters II.1–II.4)

### OPER.1. The Ho–Kalman Skeletal Algorithm and Recovery of Hidden Memory from a Hankel Window

Suppose that over a field $K$ we are given a sequence of Markov parameters $M_0, M_1, \dots, M_{2N-1} \in K^{m \times p}$ and that the block Hankel matrix $\mathcal{H}_N = (M_{i+j})_{0 \le i,j < N}$ satisfies the rank stabilization condition:
$$
\operatorname{rank}_K \mathcal{H}_N = \operatorname{rank}_K \mathcal{H}_{N+1} = r.
$$
Choose in the matrix $\mathcal{H}_N$ a basis minor of order $r \times r$ (or construct a Gaussian skeletal decomposition $\mathcal{H}_N = P Q$, where $P \in K^{mN \times r}$ has full column rank $r$ and $Q \in K^{r \times pN}$ has full row rank $r$). Then there exist rational left and right pseudoinverse matrices $P^+ \in K^{r \times mN}$ and $Q^+ \in K^{pN \times r}$ for which $P^+ P = I_r$ and $Q Q^+ = I_r$.

For the one-step shifted Hankel matrix $\sigma(\mathcal{H}_N) = (M_{i+j+1})_{0 \le i,j < N}$, the formulas of `Theorem II.1.2`
$$
A_{\min} = Q E_U \in K^{r \times p}, \qquad B_{\min} = P^+\, \sigma(\mathcal{H}_N)\, Q^+ \in K^{r \times r}, \qquad C_{\min} = E_Y^{\mathsf{T}} P \in K^{m \times r}
$$
yield a minimal linear realization of dimension $r = \operatorname{rank}_K \mathcal{H}_N$.

In particular, for the $4$-periodic Gray-code traversal $00 \to 01 \to 11 \to 10$ of the four-point scene $S_4$ when reading the first coordinate $x_1 = (0, 0, 1, 1, 0, 0, 1, 1, \dots)$ over the field $K = \mathbb{Q}$ (`§II.1.2`), the Hankel window $H_3(x_1)$ and the shifted window $\sigma(H_3(x_1))$ take the form:
$$
H_3 = \begin{pmatrix}
0 & 0 & 1 \\
0 & 1 & 1 \\
1 & 1 & 0
\end{pmatrix}, \qquad
\sigma(H_3) = \begin{pmatrix}
0 & 1 & 1 \\
1 & 1 & 0 \\
1 & 0 & 0
\end{pmatrix}, \qquad \det H_3 = -1 \ne 0.
$$
Setting $P = H_3$ and $Q = I_3$, we obtain the canonical companion shift matrix:
$$
B_{\min} = H_3^{-1} \sigma(H_3) = \begin{pmatrix}
-1 & 1 & 1 \\
1 & -1 & 0 \\
1 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
0 & 1 & 1 \\
1 & 1 & 0 \\
1 & 0 & 0
\end{pmatrix}
= \begin{pmatrix}
0 & 0 & -1 \\
1 & 0 & 1 \\
0 & 1 & 1
\end{pmatrix},
\qquad
A_{\min} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},
\qquad
C_{\min} = \begin{pmatrix} 0 & 0 & 1 \end{pmatrix},
$$
whose characteristic polynomial is $\chi_{B_{\min}}(\lambda) = \det(\lambda I_3 - B_{\min}) = \lambda^3 - \lambda^2 + \lambda - 1 = (\lambda - 1)(\lambda^2 + 1)$, and $C_{\min} B_{\min}^t A_{\min} = x_{1,t}$ for all $t \ge 0$.

---

### OPER.2. Exact Table of Euler, Cayley–Padé, and Shift-Exponential Jets in $J^4_0$

In the space of $4$-jets $J^4_0 = \mathbb{Q}[x]/(x^5)$ with basis $\{1, x, x^2, x^3, x^4\}$, the differentiation operator $J_1 = \frac{d}{dx}$ satisfies $J_1^5 = 0$. A comparison of the coefficients at powers $h^k J_1^k$ ($0 \le k \le 4$) for the three transport operators from `Theorem II.2.1` is compiled in the following table:

| Order $k$ in step $h$ | True shift $E(h) = \exp(h J_a)$ | Explicit Euler step $I + h J_a$ | Symmetric Cayley step $(I+\frac{h}{2}J_a)(I-\frac{h}{2}J_a)^{-1}$ | Difference $E(h) - T_{\mathrm{Cayley}}(h)$ |
| :---: | :---: | :---: | :---: | :---: |
| $k = 0$ ($I$) | $1$ | $1$ | $1$ | $0$ |
| $k = 1$ ($h J_a$) | $1$ | $1$ | $\frac{1}{2} + \frac{1}{2} = 1$ | $0$ |
| $k = 2$ ($h^2 J_a^2$) | $\frac{1}{2}$ | $0$ | $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$ | $0$ |
| $k = 3$ ($h^3 J_a^3$) | $\frac{1}{6}$ | $0$ | $\frac{1}{8} + \frac{1}{8} = \frac{1}{4}$ | $\frac{1}{6} - \frac{1}{4} = \mathbf{-\frac{1}{12}}$ |
| $k = 4$ ($h^4 J_a^4$) | $\frac{1}{24}$ | $0$ | $\frac{1}{16} + \frac{1}{16} = \frac{1}{8}$ | $\frac{1}{24} - \frac{1}{8} = -\frac{1}{12}$ |

---

### OPER.3. Smith Normal Form ($\mathrm{SNF}$) of the Boundary Operator $\partial_2$ for $\mathbb{R}P^2$

For the $6$-vertex triangulation $K_{\mathbb{R}P^2}$ from `Theorem II.3.2` ($f_0 = 6$ vertices, $f_1 = 15$ edges, $f_2 = 10$ triangles), the integer matrix $\partial_2 \in \mathbb{Z}^{15 \times 10}$ is reduced by elementary integer row and column operations (the Euclidean algorithm in the ring $\mathbb{Z}$) to its diagonal Smith normal form:
$$
U\,\partial_2\,V = \begin{pmatrix}
I_9 & 0 \\
0 & 2 \\
0_{5 \times 9} & 0_{5 \times 1}
\end{pmatrix} \in \mathbb{Z}^{15 \times 10}, \qquad U \in \mathrm{GL}_{15}(\mathbb{Z}), \quad V \in \mathrm{GL}_{10}(\mathbb{Z}).
$$
The sum of all $10$ oriented triangles with suitable orientation signs $\varepsilon_\tau \in \{\pm 1\}$ yields an integer $2$-chain $c_{\mathrm{fund}} = \sum_{\tau \in F} \varepsilon_\tau \tau \in C_2(K_{\mathbb{R}P^2}; \mathbb{Z})$ whose boundary equals twice the equatorial cycle:
$$
\partial_2 c_{\mathrm{fund}} = 2\,\gamma_{\mathrm{eq}} \ne 0 \quad \text{in } C_1(K_{\mathbb{R}P^2}; \mathbb{Z}), \qquad \partial_1 \gamma_{\mathrm{eq}} = 0.
$$
It is precisely this factor of $2$ that produces $H_1(\mathbb{R}P^2; \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$ and $H^2(\mathbb{R}P^2; \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$, vanishes modulo $2$ (generating the nonzero fundamental cycle $c_{\mathrm{fund}} \bmod 2 \in H_2(\mathbb{R}P^2; \mathbb{F}_2) \cong \mathbb{F}_2$), and becomes invertible over $\mathbb{Q}$ ($\gamma_{\mathrm{eq}} = \partial_2(\frac{1}{2} c_{\mathrm{fund}})$, killing the homology $H_1(\mathbb{R}P^2; \mathbb{Q}) = 0$).

---

### OPER.4. Anatomy of the Symmetry Group of the Observer's Octahedron $W(B_3) = \mathrm{Aut}(O_6)$

In `Theorem II.4.1`, the group $W(B_3) \subset \mathrm{O}_3(\mathbb{Z})$ of order $48$ acts on the $6$ vertices of the octahedron $\{\pm e_1, \pm e_2, \pm e_3\}$ and on the $8$ faces of the octahedron indexed by the octants $(i, j, k) \in \mathbb{F}_2^3$ with parity charge $\kappa(i, j, k) = i \oplus j \oplus k \in \mathbb{F}_2$. The complete classification of all $48$ elements $M \in W(B_3)$ by determinant $\det M \in \{\pm 1\}$, parity-charge shift $\Delta \kappa \in \{0, 1\}$, and element order $\mathrm{ord}(M)$ takes the form:

| Transformation Type in $W(B_3)$ | Number of Elements | Determinant $\det M$ | Action on Charge $\kappa$ | Element Order | In $W(B_3)^+ \cong \mathfrak{S}_4$? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Identity $+I_3$ | $1$ | $+1$ | Preserves ($\Delta\kappa = 0$) | $1$ | Yes |
| Half-turns about vertex axes ($2$ sign flips without permutation) | $3$ | $+1$ | Preserves ($\Delta\kappa = 0$) | $2$ | Yes (subgroup $V_4$) |
| Rotations by $\pm 120^\circ$ about face diagonals ($3$-cycles of axes with an even number of minus signs) | $8$ | $+1$ | Preserves ($\Delta\kappa = 0$) | $3$ | Yes (with $V_4$ gives $A_4$) |
| Half-turns about edge midpoints (transposition of $2$ axes with $1$ sign flip) | $6$ | $+1$ | Inverts ($\Delta\kappa = 1$) | $2$ | Yes |
| Rotations by $\pm 90^\circ$ about vertex axes (transposition of $2$ axes with $1$ sign flip) | $6$ | $+1$ | Inverts ($\Delta\kappa = 1$) | $4$ | Yes |
| Central inversion $-I_3$ (flip of all $3$ signs) | $1$ | $-1$ | Inverts ($\Delta\kappa = 1$) | $2$ | No |
| Reflections in coordinate planes ($1$ sign flip) | $3$ | $-1$ | Inverts ($\Delta\kappa = 1$) | $2$ | No |
| Rotoinversions of order $6$ ($3$-cycles with an odd number of minus signs) | $8$ | $-1$ | Inverts ($\Delta\kappa = 1$) | $6$ | No |
| Diagonal reflections in edge planes (transposition of $2$ axes with an even number of minus signs) | $6$ | $-1$ | Preserves ($\Delta\kappa = 0$) | $2$ | No |
| Rotoinversions of order $4$ (transposition of $2$ axes with an even number of minus signs) | $6$ | $-1$ | Preserves ($\Delta\kappa = 0$) | $4$ | No |

From this table one immediately reads off the number of involutions (elements of order $2$):
$$
3 + 6 + 1 + 3 + 6 = \mathbf{19} \text{ involutions in } W(B_3),
$$
which is strictly verified in `Proposition II.4.1` and gate `GATE-II04-02`. At the same time, the table separates the two distinct index-$2$ subgroups of order $24$ isomorphic to $\mathfrak{S}_4$: the charge-preserving subgroup $W(D_3) = \{M \in W(B_3) : \Delta\kappa(M) = 0\}$ (rows 1–3 and 9–10: $1 + 3 + 8 + 6 + 6 = 24$, with $W(B_3) = W(D_3) \times \{\pm I_3\}$) and the proper spatial rotation subgroup $W(B_3)^+ = \{M \in W(B_3) : \det M = +1\}$ (rows 1–5: $1 + 3 + 8 + 6 + 6 = 24$), whose intersection forms the alternating tetrahedral group $A_4 = W(B_3)^+ \cap W(D_3)$ of order $12$.

---

## Appendix Q. Octonions, Quantum Effects, Hoggar Lines, and Flag Certificates (for Chapters II.5–II.9)

### Q.1. Cayley–Graves Octonion Sign Table and Verification of Zero-Divisor Witnesses in the Sedenions $\mathbb{S}$

In the standard Cayley–Dickson basis $\{e_0, e_1, \dots, e_7\}$ of the octonion algebra $\mathbb{O}$, the seven oriented Fano lines are given by the cyclic triples
$$
(1,2,3),\quad (1,4,5),\quad (1,7,6),\quad (2,4,6),\quad (2,5,7),\quad (3,4,7),\quad (3,6,5),
$$
where for each triple $(i, j, k)$ the equalities $e_i e_j = +e_k = -e_j e_i$, $e_j e_k = +e_i$, $e_k e_i = +e_j$, and $e_i^2 = -e_0$ hold.

Upon passing to the $16$-dimensional sedenion algebra $\mathbb{S} = \mathbb{O} \oplus \mathbb{O} e_8$ ($e_{8+r} = (0, e_r)$ for $0 \le r \le 7$) via the Cayley–Dickson formula $(a, b)(c, d) = (ac - \bar{d}b,\, da + b\bar{c})$, for the four basis units $e_1 = (e_1, 0)$, $e_4 = (e_4, 0)$, $e_{10} = (0, e_2)$, $e_{15} = (0, e_7)$ we obtain:
1. $e_1 e_4 = (e_1 e_4, 0) = (+e_5, 0) = +e_5$;
2. $e_{10} e_{15} = (0, e_2)(0, e_7) = (-\bar{e}_7 e_2, 0) = (e_7 e_2, 0) = +e_5$ (since from the cycle $(2,5,7)$ it follows that $e_7 e_2 = +e_5$);
3. $e_{10} e_4 = (0, e_2)(e_4, 0) = (0, e_2 \bar{e}_4) = (0, -e_2 e_4) = (0, -e_6) = -e_{14}$ (since from the cycle $(2,4,6)$ it follows that $e_2 e_4 = +e_6$ and $8 + 6 = 14$);
4. $e_1 e_{15} = (e_1, 0)(0, e_7) = (0, e_7 e_1) = (0, -e_6) = -e_{14}$ (since from the cycle $(1,7,6)$ it follows that $e_1 e_7 = +e_6 \implies e_7 e_1 = -e_6$).

Therefore, for the integer elements $x = e_1 + e_{10}$ and $y = e_4 - e_{15}$ ($N(x) = N(y) = 2 \ne 0$), the product equals:
$$
(e_1 + e_{10})(e_4 - e_{15}) = e_1 e_4 - e_1 e_{15} + e_{10} e_4 - e_{10} e_{15} = (+e_5) - (-e_{14}) + (-e_{14}) - (+e_5) = 0.
$$
Similarly, for the second pair $x' = e_3 + e_{10}$, $y' = e_6 - e_{15}$:
- $e_3 e_6 = +e_5$ (from the cycle $(3,6,5)$);
- $e_{10} e_{15} = +e_5$ (from the cycle $(2,5,7)$);
- $e_{10} e_6 = (0, -e_2 e_6) = (0, +e_4) = +e_{12}$ (from the cycle $(2,4,6) \implies e_2 e_6 = -e_4$);
- $e_3 e_{15} = (0, e_7 e_3) = (0, +e_4) = +e_{12}$ (from the cycle $(3,4,7) \implies e_7 e_3 = +e_4$);
whence $(e_3 + e_{10})(e_6 - e_{15}) = e_5 - e_{12} + e_{12} - e_5 = 0$.

---

### Q.2. Complete Table of the $16$ Boolean Questions of Scene $S_4$ and Their Walsh–Bloch Images $E_\lambda(q)$

For the four-point scene $S_4 = \{00, 01, 10, 11\}$, all $16$ Boolean questions $q : S_4 \to \{0,1\}$ partition by Hamming weight $|q|$ into five layers with exact positivity thresholds $0 \preceq E_\lambda(q) \preceq I_2$:

| Weight Layer $|q|$ | Number of Tables | Examples of Questions on $S_4$ | Mean $c_0(q)$ | Walsh Vector $\mathbf{c}(q) = (c_1, c_2, c_3)$ | Norm $\|\mathbf{c}(q)\|_2$ | Admissibility Threshold $\|\lambda\|_{\max}$ |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| $|q| = 0$ | $1$ | Zero question $0_{S_4}$ | $0$ | $(0, 0, 0)$ | $0$ | $\infty$ |
| $|q| = 1$ | $4$ | Single-point indicators $\delta_{00}, \delta_{01}, \delta_{10}, \delta_{11}$ | $\frac{1}{4}$ | $\frac{1}{4}(\pm 1, \pm 1, \pm 1)$ ($\prod = +1$) | $\frac{\sqrt{3}}{4}$ | **$\frac{1}{\sqrt{3}}$** (`SIC` tetrahedron) |
| $|q| = 2$ | $6$ | Six two-point slices of the octahedron $O_6$: $X_0, X_1, C_0, C_1, B_0, B_1$ | $\frac{1}{2}$ | $(\pm\frac{1}{2}, 0, 0)$ and permutations | $\frac{1}{2}$ | **$1$** ($3$ Pauli `MUB` bases) |
| $|q| = 3$ | $4$ | Three-point complements $1 - \delta_s$ | $\frac{3}{4}$ | $\frac{1}{4}(\pm 1, \pm 1, \pm 1)$ ($\prod = -1$) | $\frac{\sqrt{3}}{4}$ | **$\frac{1}{\sqrt{3}}$** |
| $|q| = 4$ | $1$ | Unit question $1_{S_4}$ | $1$ | $(0, 0, 0)$ | $0$ | $\infty$ |

---

## Appendix GR-II. Atlas of Diagrams and Figures of Book II

All graphical diagrams of the Second Volume are embedded directly in the text of the respective chapters and contain no intra-laboratory stamps:
1. **Diagram of the block Hankel operator factorization** $\mathcal{H} = \mathcal{O}\mathcal{R}$ through the minimal hidden-memory space $V_{\min}$ (`Chapter II.1`, §II.1.3).
2. **Diagram of signed boundary cancellation** $\partial_1 \partial_2 = 0$ on the oriented triangle $\Delta^2 = [v_0, v_1, v_2]$ (`Chapter II.3`, §II.3.1).
3. **Map of proven functors and transitions of Books I and II** from the finite core of the contract $\Gamma$ to the four enrichments of the Second Volume (`Chapter II.9`, §II.9.4).

---

## Appendix VP-II. How to Verify the Book Independently and Master Passport of Verification Gates

**Execution.** All statements marked in the chapter passports are verified by a single single-threaded script in `Julia 1.12.6` using exclusively exact integer, rational, and cyclotomic/quadratic algebraic arithmetic. Simply navigate to the volume directory and run:

```bash
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 11_verify_full_book_II_v3_3.jl
```

**Pass Criterion.** The script prints a line-by-line report for each gate and the final summary line `38 / 38 GATES PASS` (`36` mathematical gates across chapters `II.1–II.9`, `1` strict text-and-structure lint gate `GATE-II09-05`, and `1` exact-arithmetic self-audit gate `GATE-II-SYS-FLOAT`); simultaneously, it overwrites the machine-readable certificate `12_book_II_v3_3_master_certificate.json` with the list of gates, their status, and the computed invariants. Any gate with status `FAIL` means that the corresponding statement of the book is not confirmed in its current form.

**Verification Architecture.** Below is the master table of all `38` gates of the script `11_verify_full_book_II_v3_3.jl` (`36` mathematical and `2` system gates).

Every mathematical gate of the verifier `11_verify_full_book_II_v3_3.jl` performs a direct algebraic or combinatorial computation without floating-point numbers and without constant tautologies:

| Gate Code | Chapter and Theorem | What Is Explicitly Computed and Verified in `Julia 1.12.6` | Verification Type |
| :--- | :--- | :--- | :--- |
| `GATE-II01-01` | `Ch. II.1`, Table `II.1.1` | Hankel ranks $1, 2, 3, 4$ when traversing scene $S_4$ and recovery of $(A_{\min}, B_{\min}, C_{\min})$ | Exact computation in $\mathbb{Q}$ |
| `GATE-II01-02` | `Ch. II.1`, Thm. `II.1.1` | Stabilization $\ker \mathcal{O}_d = \ker \mathcal{O}$ and joint window injectivity $(C B^{j_0},\dots,C B^{j_0+r-1})|_{W_0}$ for disturbance recovery | Exact computation in $\mathbb{Q}$ |
| `GATE-II01-03` | `Ch. II.1`, Thm. `II.1.2` | Scalar ($p=m=1$) and block MIMO ($p=m=2$) Ho–Kalman skeletal decomposition $C_{\min}B_{\min}^t A_{\min} = M_t$ for $0 \le t \le 10$ | Exact computation in $\mathbb{Q}$ |
| `GATE-II01-04` | `Ch. II.1`, Prop. `II.1.1` | Construction of the Walsh matrix on $D^n$ ($n=2,3,4$), verification of $\dim\ker\Pi_{\le 1} = 2^n-(n+1)$ and $\Pi_{\le 1}(w_{111}) = 0$ | Exhaustive enumeration and linear algebra |
| `GATE-II01-05` | `Ch. II.1`, Prop. `II.1.2` | Exhaustive enumeration of $\mathfrak{S}_n$ ($n=4,5,6$): $|\mathrm{Aut}(P_n)| = 2$ and $|\mathrm{Aut}(C_n)| = 2n$ | Exhaustive group enumeration |
| `GATE-II02-01` | `Ch. II.2`, Lemma `II.2.1` | Formal resolvent $C(I-wB)^{-1}A$ and reciprocal polynomial $\widetilde{\chi}_B(w) = w^d\chi_B(1/w)$ | Polynomial algebra over $\mathbb{Q}$ |
| `GATE-II02-02` | `Ch. II.2`, Prop. `II.2.1` | Tower $\mathbb{Z}/2^m\mathbb{Z}$, injectivity of $\Phi_m$, $|\Phi_m(x^{(+)})-\Phi_m(x^{(-)})| = 2^{-m}$, and non-additivity $\Phi_2(1)+\Phi_2(1) \not\equiv \Phi_2(2) \pmod 1$ | Exact rational arithmetic |
| `GATE-II02-03` | `Ch. II.2`, Thm. `II.2.1`, Lemma `II.2.2` | Jet computation $T_{\mathrm{Cayley}}(h) - \exp(h J_a) = \frac{1}{12}h^3 J_a^3 + O(h^4)$ and Taylor series $\widetilde{\sigma}(z)$ from power series | Exact rational arithmetic |
| `GATE-II02-04` | `Ch. II.2`, Prop. `II.2.2` | Automatic evaluation of Jacobian matrices via dual numbers $K[\varepsilon]/(\varepsilon^2)$ over $\mathbb{Q}$ and $\mathbb{F}_2$ and verification of $J_{G\circ F} = J_G J_F$ | Dual-number algebra |
| `GATE-II03-01` | `Ch. II.3`, Lemma `II.3.1`, `§II.3.2` | Verification of $\partial_1\partial_2 = 0$ and emptiness $(\mathrm{id}\circ\mathrm{id})\cap\mathrm{flip} = \varnothing$ in the Möbius triangle | Combinatorial check |
| `GATE-II03-02` | `Ch. II.3`, Thm. `II.3.1` | Cohomology of the nerve $\mathcal{N}(O_6)$ of scene $S_4$: $\operatorname{rank}\delta_0 = 5$, $\operatorname{rank}\delta_1 = 4$, $\dim H^1 = 3$, $\delta_1 w = 0$, and enumeration of all $64$ gauges $g \in \mathbb{F}_2^6$ ($\delta_0 g \ne w$) | Exhaustive enumeration over $\mathbb{F}_2$ |
| `GATE-II03-03` | `Ch. II.3`, Thm. `II.3.2` | Smith normal form algorithm $\mathrm{SNF}(\partial_2)$ for the $6$-vertex triangulation of $\mathbb{R}P^2$: invariant factors $(1,\dots,1,2)$ and ranks over $\mathbb{Z}, \mathbb{F}_2, \mathbb{Q}$ | Integer Smith normal form |
| `GATE-II03-04` | `Ch. II.3`, Table `II.3.1` | Verification of separability failure in the presheaf $\mathcal{G}$ and local contractibility of the torsor $\mathcal{S}_w$ on spanning trees of $O_6$ | Exhaustive section enumeration |
| `GATE-II04-01` | `Ch. II.4`, Thm. `II.4.1` | Exact integer enumeration of $W(B_3) = \mathrm{Aut}(O_6)$ of order $48$: $W(D_3) \cong \mathfrak{S}_4$ preserves $\kappa$ and $\mathcal{N}(O_6)$, $W(B_3)^+ \cong \mathfrak{S}_4$ permutes the $4$ cube diagonals ($A_4 = W(B_3)^+ \cap W(D_3)$ of order $12$), $-I_3$ inverts $\kappa \mapsto \kappa \oplus 1$ | Exact integer matrix-group enumeration |
| `GATE-II04-02` | `Ch. II.4`, Prop. `II.4.1` | Construction of $Q_8 \subset \mathrm{SL}_2(\mathbb{F}_3)$, free action on $S_{\mathrm{odd}}$, absence of a homomorphic section $V_4 \to Q_8$ among all $64$ maps, and involution counts $19, 13, 1$ | Exhaustive enumeration over $\mathbb{F}_3$ |
| `GATE-II04-03` | `Ch. II.4`, Thm. `II.4.2` | Computation of $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ via $\mathrm{SNF}$ of the relation matrix and verification of $f(\sigma_1\sigma_2^{-1}) = (123) \ne \mathrm{id}$ in $\mathfrak{S}_3$ | Group and integer algebra |
| `GATE-II05-01` | `Ch. II.5`, Thm. `II.5.1` | Exhaustive enumeration of $512$ triples: $0$ associativity violations for the unsigned Fano table ($\cong \mathbb{F}_2[\mathbb{F}_2^3]$), $168$ anti-associative triples, and $0$ alternativity and Moufang violations for $\mathbb{O}$ | Exhaustive enumeration of $8^3 = 512$ triples |
| `GATE-II05-02` | `Ch. II.5`, Thm. `II.5.2` (pt. 1) | Exhaustive enumeration of $\mathrm{Oct}(\mathbb{F}_2)$ ($256$ Zorn matrices): $\omega(x,I)=\mathrm{tr}(x)$, $\dim V_6 = 6$, Paige loop $|M_{120}| = 120$, trace split $64 + 56 = 120$, and quadratic split $36 + 84 = 120$ | Exhaustive enumeration of $256$ elements |
| `GATE-II05-03` | `Ch. II.5`, Thm. `II.5.2` (pt. 2) | Exhaustive check of all $120^3 = 1\,728\,000$ Moufang triples on $M_{120}$, $72$ nontrivial idempotents, hyperbolicity of $q_e$ ($36$ zeros / $28$ ones), $\delta_4 q = 0$, and $|G_2(2)| = 12\,096$ | Exhaustive enumeration over $\mathbb{F}_2$ |
| `GATE-II05-04` | `Ch. II.5`, Props. `II.5.1, II.5.2` | Sedenion signs $e_{10}e_4 = e_1 e_{15} = -e_{14}$, vanishing of $(e_1+e_{10})(e_4-e_{15}) = 0$ and $(e_3+e_{10})(e_6-e_{15}) = 0$, enumeration of all $84$ elementary zero-divisor quartets, and Clifford generators $\mathrm{Cl}_{0,8} \cong \mathrm{Mat}_{16}(\mathbb{R})$ | Exact integer algebra |
| `GATE-II06-01` | `Ch. II.6`, Thm. `II.6.1` | Exhaustive enumeration of $16$ Boolean tables on $S_4$ over $\mathbb{Q}$: $E_\lambda(\neg q) = I_2 - E_\lambda(q)$, $c_0^2 + \|\mathbf{c}(q)\|_2^2 = c_0$, and effect filtration $16 \to 8 \to 2$ at $\lambda^2 \in \{1/3, 1, 9/4\}$ | Exact rational algebra |
| `GATE-II06-02` | `Ch. II.6`, Prop. `II.6.1` | Step-by-step stabilization $W_0 \subset W_1 \subset W_2 = W_\infty$ in $\le d^2-1$ steps, completeness of $12$ `MUB` projectors in $\mathbb{Z}[\omega]$ ($\operatorname{rank}=9$) versus $16$ rational projectors ($\operatorname{rank}=6$) in $\mathrm{Herm}_3(\mathbb{C})$ | Exact cyclotomic and rational algebra |
| `GATE-II06-03` | `Ch. II.6`, Prop. `II.6.1(3)`, Thm. `II.6.2` | Unitality $\Phi^\dagger(I_d) = I_d$, reset-channel counterexample $\mathrm{tr}(\Phi_{\mathrm{reset}}^\dagger(|0\rangle\langle 0|)) = d$, and Busch valuation linearity | Exact rational algebra |
| `GATE-II06-04` | `Ch. II.6`, Thm. `II.6.2`, `§II.6.4` | Busch's symmetric trine POVM in $\mathbb{Q}(\sqrt{3})$ ($E_1+E_2+E_3=I_2$, $E_k^2=\frac{2}{3}E_k$) and nonlinear hemisphere valuation counterexample on projectors $\mathcal{P}(\mathbb{C}^2)$ at $d=2$ | Exact quadratic algebra $\mathbb{Q}(\sqrt{3})$ |
| `GATE-II07-01` | `Ch. II.7`, Prop. `II.7.1`, Thm. `II.7.1` | Verification of `MUB` at $d=2,3$, coincidence of the qubit `SIC` tetrahedron with $2E_{1/\sqrt{3}}(\delta_s)$ on $S_4$, planar $V_4$-orbit counterexample $(3/5, 4/5, 0)$, and exact verification of all $36$ overlaps $|\langle\psi_i|\psi_j\rangle|^2 = 1/4$ of the Hesse `SIC` configuration at $d=3$ in $\mathbb{Z}[\omega]$ | Exact cyclotomic and rational algebra |
| `GATE-II07-02` | `Ch. II.7`, Thm. `II.7.2` | Exhaustive enumeration of $64$ Hoggar lines in $\mathbb{Q}(i)$: all $63$ overlaps $16/144 = 1/9$, $F=8I_8$, $G_{\mathrm{frame}}^2 = 8G_{\mathrm{frame}}$ ($\operatorname{rank} G_{\mathrm{frame}} = 8$), $\operatorname{rank} H = 64$, $S^2 = 63I_{64} + 18S$, $\Phi_2 = 1/36$, $\Phi_3 - \Phi_3^{\mathrm{Welch}} = 11/648 - 1/120 = 7/810 > 0$ | Exact Gaussian and rational arithmetic |
| `GATE-II07-03` | `Ch. II.7`, Thm. `II.7.3` | Peres–Mermin square: commutativity, products $\pm I_4$, $\sum \delta b \equiv 0 \pmod 2$, and absence of a solution $\delta b = \beta$ among all $512$ tables $b \in \mathbb{F}_2^9$ | Exhaustive enumeration of $2^9 = 512$ |
| `GATE-II07-04` | `Ch. II.7`, `§II.7.4` | Tsirelson bound $S_{\mathrm{CHSH}} = 2\sqrt{2} > 2$ in $\mathbb{Q}(\sqrt{2})$ ($|\mathcal{S}_e(X)|=16$), rational Hardy model ($e_{A_1 B_1}(-1,-1)=1/12>0$, $|\mathcal{S}_e(X)|=5$), and Peres–Mermin square ($|\mathcal{S}_e(X)|=0$) | Exact quadratic and sheaf check |
| `GATE-II08-01` | `Ch. II.8`, Prop. `II.8.1` | Whitney identity $R_1 W_1 = \mathrm{id}$, defect $W_1 R_1(x\,dx) = \frac{1}{2}dx$, and subdivision chain identity $\partial'_2 s_2 = s_1 \partial_2$ | Exact rational arithmetic |
| `GATE-II08-02` | `Ch. II.8`, Thm. `II.8.1` | Semi-discrete Cahn–Hilliard flow $\dot{u} = -M L(\gamma L u + F'(u))$ on $O_6$: $\mathbf{1}^{\mathsf{T}}\dot{u} = 0$, $\frac{dE_h}{dt} = -M\mu^{\mathsf{T}}L\mu < 0$, and exact kernel multiplicities of $L_{O_6} - \lambda I_6$ ($\{0, 4^{\times 3}, 6^{\times 2}\}$) | Exact rational arithmetic |
| `GATE-II08-03` | `Ch. II.8`, `§II.8.4` | Exact integer eigenvectors for spectrum $\{3, -1, -2\}$ of indefinite Gram matrix $G_{\mathrm{bad}}$ for $(x^2+y^2)^2$ and exact decomposition $G_{\mathrm{PSD}} = L D L^{\mathsf{T}} \succeq 0$ | Linear algebra over $\mathbb{Q}$ |
| `GATE-II08-04` | `Ch. II.8`, Thm. `II.8.2` | Exhaustive enumeration of $G_{1344}$ on Fano flags $\mathbb{Q}^{21}$: $231 = 42 + 7\cdot 27$, $1771 = 189 + 7\cdot 226$, explicit projector $P_{\perp,c}$ in `Rational{BigInt}` ($P_{\perp,c}^2 = P_{\perp,c}$, $\mathrm{tr}\,P_{\perp,c} = 214$), rank $7\cdot 12 = 84$, and $1771 - 84 = 1687$ | Exact `Rational{BigInt}` arithmetic |
| `GATE-II09-01` | `Ch. II.9`, Thm. `II.9.1` | Lawvere–Cantor diagonal prohibition and analysis of the exponential $Y^A$ in $\mathbf{Set}^{C_2}$ ($|A^{C_2}| = 0$, $|Y^A| = 4$, $|(Y^A)^{C_2}| = 2$) | Combinatorial-categorical check |
| `GATE-II09-02` | `Ch. II.9`, Thm. `II.9.2` (items 1–2) | Verification of the $2$-cocycle $\beta((g,u),(h,v)) = g_1 h_2$ on the $64$-element extension $\widetilde{G}_\beta$, $\beta(t,t) = 1$, and splitting on subgroups $K$ with $\beta|_{K\times K} \sim 0$ | Exhaustive enumeration of $64^2$ pairs |
| `GATE-II09-03` | `Ch. II.9`, Thm. `II.9.2` (item 3) | Computation of $\dim H^1(\mathrm{GL}_3(\mathbb{F}_2), \mathbb{F}_2^3) = 1$ ($\dim Z^1 = 4$, $\dim B^1 = 3$), construction of the fixed-point-free $1$-cocycle, two orbits $8 + 56 = 64$ on $X_{64}$ with stabilizers $21$ and $3$, and minimality of quotient $8 = 168/21$ | Constructive cohomological and group check |
| `GATE-II09-04` | `Ch. II.9`, Table `II.9.1` | Summary cross-check of all $9$ canonical minimal-memory thresholds of Books I–II | Cross-volume invariant check |
| `GATE-II09-05` | Entire volume (`00..10_*_V3_3_EN.md`) | Strict machine lint checking clean prose, balanced display equations, and integrity of local links across all files of the volume | Strict text-and-structure lint |
| `GATE-II-SYS-FLOAT` | `11_verify_full_book_II_v3_3.jl` | Automated self-audit of the verifier source code confirming zero floating-point types, tolerances `atol/rtol`, or random number generators | Exact-arithmetic self-audit |


### VP-II.2. Master Certification Registry of the 31 Statements of Book II Across Epistemic Statuses

In the table below, for each of the `31` headers of theorems, lemmas, and propositions of the Second Volume, we record its epistemic status, classical foundation, specific contribution of this book, and gate in `11_verify_full_book_II_v3_3.jl`.

| No. | Statement | Epistemic Status | Classical Foundation | Contribution of This Book | `Julia` Gate |
| :-: | :--- | :--- | :--- | :--- | :--- |
| `1` | **Theorem II.1.1** | Extension of a classical theorem within contract $\Gamma$ | Kalman's observability criterion for finite-dimensional linear systems (Kalman, 1960) and stabilization of ascending kernel filtrations via the Cayley–Hamilton theorem. | Shifted-window observability formula $(C B^{j_0}, \dots, C B^{j_0+r-1})|_{W_0}$ under delay threshold $j_0$, separating zero single-slice response from joint injectivity over horizon $r$. | `GATE-II01-02` |
| `2` | **Theorem II.1.2** | Classical result in operational notation | The Ho–Kalman minimal linear realization theorem via block Hankel factorization (Ho and Kalman, 1966) and M. P. Schützenberger's theory of rational series (1961). | Operational reading of the minimal state dimension $\dim V_{\min} = \operatorname{rank}\mathcal{H}_f$ as linear observer memory carrying the $\mathrm{GL}_r(K)$ basis gauge torsor ($|\mathcal{R}| > 1$). | `GATE-II01-03` |
| `3` | **Proposition II.1.1** | Extension of a classical theorem within contract $\Gamma$ | Walsh–Hadamard transform and character orthogonality on the elementary abelian group $\mathbb{F}_2^n$—classical harmonic analysis on the Boolean cube. | Exact characterization of the $(2^n - n - 1)$-dimensional shadow kernel of a first-order linear projector, blind to all pure higher-order parities $k \ge 2$ (including $\beta = x \oplus c$ on $S_4$). | `GATE-II01-04` |
| `4` | **Proposition II.1.2** | Extension of a classical theorem within contract $\Gamma$ | Permutation representations of the symmetric group $\mathfrak{S}_n$ and automorphism groups of path and cycle graphs. | Symmetry reduction from full channel permutations $\mathfrak{S}_n$ to the dihedral or reflection subgroup once a nearest-neighbor quadratic step-energy functional is imposed. | `GATE-II01-05` |
| `5` | **Lemma II.2.1** | Extension of a classical theorem within contract $\Gamma$ | Formal resolvent identity $(I - wA)^{-1} = \sum_{k \ge 0} w^k A^k$ in formal power series $K[[w]]$ and the unilateral $Z$-transform of linear systems. | Unconditional algebraic alignment of the delay indeterminate $w = 1/z$ with the Hankel windows of Book I, separated explicitly from the analytic convergence disk $|z| > \rho(A)$. | `GATE-II02-01` |
| `6` | **Proposition II.2.1** | Extension of a classical theorem within contract $\Gamma$ | Binary expansions on the circle $\mathbb{R}/\mathbb{Z}$ and the compact totally disconnected ring of $2$-adic integers $\mathbb{Z}_2$. | Operational reading of the continuous surjection $\bar{\Phi} : \mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$ as gluing indistinguishable binary tails ($0.0111\ldots_2 = 0.1000\ldots_2$), together with a proof that $\bar{\Phi}$ is not an additive group homomorphism. | `GATE-II02-02` |
| `7` | **Theorem II.2.1** | Classical result in operational notation | Cayley's rational transform $(I - \frac{h}{2}J_a)^{-1}(I + \frac{h}{2}J_a)$ (Cayley, 1846) and the $[1/1]$ diagonal Padé approximant to the matrix exponential $\exp(h J_a)$. | Exact second-order jet agreement of the reversible rational step with $\exp(h J_a)$ without transcendental series, plus the exact cubic remainder coefficient $+\frac{1}{12}h^3 J_a^3$. | `GATE-II02-03` |
| `8` | **Lemma II.2.2** | Classical result in operational notation | Odd symmetry of the centered logistic function $\sigma(u) - \frac{1}{2} = \frac{1}{2}\tanh(u/2)$ and its power-series expansion around zero. | Explicit unsaturated linear readout window around the threshold contrasted with tail collapse under clipping and scale saturation. | `GATE-II02-03` |
| `9` | **Proposition II.2.2** | Classical result in operational notation | Ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$ (Clifford, 1873), algebraic first-order Taylor expansion $P(x + \varepsilon v) = P(x) + \varepsilon\, dP(x)v$, and the Jacobi chain rule. | Purely algebraic formulation of first-order jets and tangent question pushforwards over any commutative ring $K$ with zero limit passages $\Delta x \to 0$. | `GATE-II02-04` |
| `10` | **Lemma II.3.1** | Classical result in operational notation | The identities $\partial^2 = 0$ and $\delta^2 = 0$ are the classical fundamental identities of simplicial chains and cochains (Poincaré; Čech cochains; Eilenberg–Steenrod axiomatics, 1952). | Use of this identity as the consistency condition for the observer's local records on the nerve of slices. | `GATE-II03-01` |
| `11` | **Theorem II.3.1** | Original proved result of this book | Simplicial cochains and cohomology of two-dimensional cell complexes over $\mathbb{F}_2$ (Alexandroff, 1928; Čech, 1932). | Explicit matrix computation $\operatorname{rank}\delta_0 = 5$, $\operatorname{rank}\delta_1 = 4$, and $\dim_{\mathbb{F}_2} H^1(\mathcal{N}(O_6); \mathbb{F}_2) = 3$ on the checkerboard octahedron nerve of the six slices of $S_4$. | `GATE-II03-02` |
| `12` | **Theorem II.3.2** | Classical result in operational notation | Smith normal form of integer boundary matrices (H. Smith, 1861), the universal coefficient theorem, and cellular homology of the real projective plane $\mathbb{R}P^2$. | Contrast between visibility of $\mathbb{Z}/2\mathbb{Z}$ torsion over $\mathbb{Z}$ and $\mathbb{F}_2$ ($H^2(\mathbb{R}P^2;\mathbb{F}_2) \cong \mathbb{F}_2$) and complete blindness of the rational window $H^1(\mathbb{R}P^2;\mathbb{Q}) = H^2(\mathbb{R}P^2;\mathbb{Q}) = 0$. | `GATE-II03-03` |
| `13` | **Theorem II.4.1** | Original proved result of this book | The isomorphism $W(B_3) \cong \mathfrak{S}_4 \times C_2 \cong \mathrm{Aut}(O_6)$ is a classical fact about the hyperoctahedral symmetry group of the cube and octahedron; signed edge labels and their inversion belong to the language of signed graphs and gain graphs (Harary, 1953; Zaslavsky, 1982–1989). | Separation of the subgroup $W(D_3) \cong \mathfrak{S}_4$ (preserving charge $\kappa$ and the nerve $\mathcal{N}(O_6)$) from the proper rotation subgroup $W(B_3)^+ \cong \mathfrak{S}_4$ (preserving $\kappa$ on $A_4$ and inverting $\kappa$ on $12$ odd rotations). | `GATE-II04-01` |
| `14` | **Proposition II.4.1** | Extension of a classical theorem within contract $\Gamma$ | Hamilton's quaternion group $Q_8$ (1843) and the cohomological non-splitting of the central extension $1 \to C_2 \to Q_8 \to V_4 \to 1$. | Absence of a homomorphic section of quarter-turns over the Klein four-group $V_4$ ($|\mathcal{R}| = 0$) and triple spectral separation of $W(B_3)$, $\mathrm{GL}_2(\mathbb{F}_3)$, and $Q_8$ by elements of orders $2$ and $4$. | `GATE-II04-02` |
| `15` | **Theorem II.4.2** | Classical result in operational notation | Item 1 is the classical universal property of a quotient group (homomorphism theorem); the abelianization $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ is a classical fact about Artin's braid group (1925). | Reading abelianization as the loss of noncommutative memory of permutation order. | `GATE-II04-03` |
| `16` | **Theorem II.5.1** | Classical result in operational notation | Associativity of the group algebra $K[\mathbb{F}_2^3]$ and representation of the octonions as the twisted group algebra $\mathbb{R}_\sigma[\mathbb{F}_2^3]$ with a sign $2$-cocycle and its $3$-coboundary on the Fano plane (Albuquerque and Majid, 1999). | Direct passage from the unsigned commutative-associative Fano table of Book I to the alternative octonion algebra by choosing a sign $2$-cocycle $\sigma$, verified exhaustively across all $512$ basis triples. | `GATE-II05-01` |
| `17` | **Theorem II.5.2** | Extension of a classical theorem within contract $\Gamma$ | Zorn's vector-matrix model of split octonions and Paige's simple Moufang loops (1956) are classical constructions. | Separation of the trace split $64 + 56 = 120$ from the quadratic split $36 + 84 = 120$ with an exhaustive check of all $120^3$ Moufang triples. | `GATE-II05-02, GATE-II05-03` |
| `18` | **Proposition II.5.1** | Classical result in operational notation | Cayley–Dickson doubling and the appearance of zero divisors in sedenions belong to classical nonassociative algebra. | Explicit integer zero-divisor witnesses and exhaustive enumeration of all $84$ elementary quartets. | `GATE-II05-04` |
| `19` | **Proposition II.5.2** | Classical result in operational notation | Eightfold periodicity of real Clifford algebras $\mathrm{Cl}_{0,n+8} \cong \mathrm{Cl}_{0,n} \otimes \mathrm{Mat}_{16}(\mathbb{R})$ (Cartan, 1908; Bott, 1959; Atiyah–Bott–Shapiro, 1964) and Morita equivalence. | Explicit integer realization of eight anticommuting skew-symmetric generators $\Gamma_1,\dots,\Gamma_8 \in \mathrm{Mat}_{16}(\mathbb{Z})$ built from left multiplication by octonion basis units. | `GATE-II05-04` |
| `20` | **Theorem II.6.1** | Original proved result of this book | The Pauli basis and the representation of Hermitian matrices via real coefficients are known in linear algebra; the Walsh transform is based on characters. | Quantum threshold filtration of Boolean tables $16 \to 8 \to 2$ on scene $S_4$ across $|\lambda| = 1/\sqrt{3}$ and $|\lambda| = 1$. | `GATE-II06-01` |
| `21` | **Proposition II.6.1** | Extension of a classical theorem within contract $\Gamma$ | Stabilization of an ascending chain of subspaces in at most $\dim - 1$ steps is a classical linear-algebraic argument (Schützenberger, 1961; Carlyle–Paz, 1971; Tzeng, 1992). | Quantum Nerode equivalence formulated as an observer indistinguishability relation on effects. | `GATE-II06-02, GATE-II06-03` |
| `22` | **Theorem II.6.2** | Classical result in operational notation | Gleason's theorem (1957) on subspace measures for $d \ge 3$ and Busch's theorem (2003) on effect valuations for $d \ge 2$ are classical results. | Comparison of the two domains of applicability and explicit analysis of the qubit exception $d = 2$ via Busch's trine. | `GATE-II06-03, GATE-II06-04` |
| `23` | **Proposition II.7.1** | Classical result in operational notation | The bound $k \le d + 1$ and complete families of mutually unbiased bases in prime-power dimensions are classical results of Ivanović (1981) and Wootters–Fields (1989). | Formulation of explicit families at $d = 2, 3$ as sets of mutually complementary observer questions. | `GATE-II07-01` |
| `24` | **Theorem II.7.1** | Extension of a classical theorem within contract $\Gamma$ | The tetrahedron of four equiangular complex lines and symmetric informationally complete families have been studied previously (Zauner, 1999; Renes et al., 2004). | Coincidence of the qubit `SIC` tetrahedron with the boundary points $2E_{1/\sqrt{3}}(\delta_s)$ of the four-state scene $S_4$. | `GATE-II07-01` |
| `25` | **Theorem II.7.2** | Classical result in operational notation | Hoggar's sixty-four equiangular lines (1982) and frame potentials (Welch, 1974; Benedetto–Fickus, 2003) are classical constructions. | Exact matrix calculation in $\mathbb{Q}(i)$ and verification of the third frame-potential gap $\Phi_3 - \Phi_3^{\mathrm{Welch}} = 7/810 > 0$. | `GATE-II07-02` |
| `26` | **Theorem II.7.3** | Extension of a classical theorem within contract $\Gamma$ | The Peres–Mermin square (1990) and the Abramsky–Brandenburger sheaf-theoretic description of contextuality (2011) are published classical results. | Exact comparison with the parity obstruction $\kappa$ in the one-dimensional cokernel over $\mathbb{F}_2$ and the three-level hierarchy of global sections $|\mathcal{S}_e(X)| = 16 \supsetneq 5 \supsetneq 0$. | `GATE-II07-03, GATE-II07-04` |
| `27` | **Proposition II.8.1** | Classical result in operational notation | Whitney forms (1957), the de Rham map, and cohomology invariance under subdivision are classical constructions. | Explicit rational verification of the one-sided identity $R_1 W_1 = \mathrm{id}$ and the reconstruction defect inside a cell. | `GATE-II08-01` |
| `28` | **Theorem II.8.1** | Extension of a classical theorem within contract $\Gamma$ | Conservative Cahn–Hilliard gradient flows and their discrete analogues on graphs are established constructions. | Explicit free-energy dissipation law on the octahedron graph $O_6$ with spectrum $L_{O_6} = \{0, 4^{\times 3}, 6^{\times 2}\}$. | `GATE-II08-02` |
| `29` | **Theorem II.8.2** | Original proved result of this book | Isotypic character decomposition (Frobenius, Schur) and sum-of-squares representations via positive semidefinite Gram matrices (Hilbert, 1888; Choi–Lam–Reznick, 1995; Parrilo, 2000; Lasserre, 2001; Gatermann–Parrilo, 2004). | Isotypic splitting $231 = 42 + 7\cdot 27$ and $1771 = 189 + 7\cdot 226$ on the $21$ flags of the Fano plane and the explicit rational orthogonal projector $P_{\perp,c}$ of codimension $84$ ($1771 - 84 = 1687$). | `GATE-II08-04` |
| `30` | **Theorem II.9.1** | Extension of a classical theorem within contract $\Gamma$ | Lawvere's diagonal fixed-point theorem (1969) rests on the categorical form of Cantor's diagonal argument. | Separation of pointwise surjectivity from the exponential in $\mathbf{Set}^{C_2}$ ($|Y^A| = 4$, $|(Y^A)^{C_2}| = 2$) with the observer-stratification rule. | `GATE-II09-01` |
| `31` | **Theorem II.9.2** | Original proved result of this book | Cohomological classification of group extensions and the correspondence between $1$-cocycles and complements in semidirect products belong to classical group theory. | Explicit computation of the $64$-element non-split extension $\widetilde{G}_\beta$ and the two orbits $8 + 56 = 64$ of the affine action of $\mathrm{GL}_3(\mathbb{F}_2)$ on $X_{64}$. | `GATE-II09-02, GATE-II09-03` |

---

## Appendix AD-II. Concordance of Notation and Cross-Chapter Structural Invariants of Book II

| Symbol | Mathematical Object | Where Introduced and Used |
| :--- | :--- | :--- |
| $\mathcal{O}_d,\; \mathcal{R}_d,\; \mathcal{H}$ | Observability, reachability, and block Hankel operators ($\operatorname{rank}\mathcal{H} = \dim V_{\min}$) | `Chapter II.1` (`Theorems II.1.1, II.1.2`) |
| $T_{\mathrm{Cayley}}(h)$ | Cayley transform $(I - \frac{h}{2}J_a)^{-1}(I + \frac{h}{2}J_a) = \exp(h J_a) + \frac{1}{12}h^3 J_a^3 + O(h^4)$ | `Chapter II.2` (`Theorem II.2.1`) |
| $\mathcal{N}(O_6),\; \mathcal{S}_w$ | Six-slice nerve of scene $S_4$ ($\dim_{\mathbb{F}_2} H^1 = 3$) and presheaf of $\mathbb{F}_2$-torsors of local potentials | `Chapter II.3` (`Theorem II.3.1`, `§II.3.3`) |
| $W(B_3),\; W(D_3),\; W(B_3)^+$ | Full octahedral symmetry group ($48$), $\kappa$-preserving subgroup ($24$), and proper rotation subgroup ($24$); $A_4 = W(D_3) \cap W(B_3)^+$ ($12$) | `Chapter II.4` (`Theorem II.4.1`, `OPER.4`) |
| $\mathbb{R}_\sigma[\mathbb{F}_2^3],\; \mathrm{Oct}(\mathbb{F}_2),\; M_{120}$ | Twisted group algebra of octonions, $256$ Zorn matrices over $\mathbb{F}_2$, and Paige's simple Moufang loop ($120 = 64 + 56 = 36 + 84$) | `Chapter II.5` (`Theorems II.5.1, II.5.2`) |
| $E_\lambda(q),\; \mathcal{E}(\mathcal{H}),\; W_\infty$ | Contrast-$\lambda$ effect operator on $S_4$ (filtration $16 \to 8 \to 2$), effect cone, and future quantum-question subspace | `Chapter II.6` (`Theorem II.6.1`, `Prop. II.6.1`) |
| $\Phi_k,\; \mathcal{S}_e(X)$ | $k$-th frame potential ($\Phi_3^{\mathrm{Hoggar}} = 11/648 > 1/120$) and presheaf of admissible global assignments ($16 \supsetneq 5 \supsetneq 0$) | `Chapter II.7` (`Theorems II.7.2, II.7.3`, `§II.7.4`) |
| $W_k,\; R_k,\; P_{\perp,c}$ | Whitney and de Rham maps ($R_1 W_1 = \mathrm{id}$) and rational orthogonal projector off the degenerate kernel on Fano flags ($1771 - 84 = 1687$) | `Chapter II.8` (`Prop. II.8.1`, `Theorem II.8.2`) |
| $Y^A,\; \widetilde{G}_\beta,\; X_{64}$ | Exponential in $\mathbf{Set}^{C_2}$ ($|Y^A(*)| = 4$), central extension over $\mathbb{F}_2^2$, and $64$-element carrier with orbits $8 + 56$ under $\mathrm{GL}_3(\mathbb{F}_2)$ | `Chapter II.9` (`Theorems II.9.1, II.9.2`) |

---

## Classical Mathematical Sources of the Volume

For every statement, the hypotheses of the original classical theorem are strictly preserved (in particular, the dimension restriction $d \ge 3$ in Gleason's 1957 theorem on projective measures is kept distinct from Busch's 2003 theorem on valuations over the full effect cone for $d \ge 2$).

1. Ho, B. L., & Kalman, R. E. (1966). Effective construction of linear state-variable models from input/output functions. *Regelungstechnik*, 14(12), 545–548. https://doi.org/10.1524/auto.1966.14.112.545
2. Schützenberger, M. P. (1961). On the definition of a family of automata. *Information and Control*, 4(2–3), 245–270. https://doi.org/10.1016/S0019-9958(61)80020-X
3. Carlyle, J. W., & Paz, A. (1971). Realizations by stochastic finite automata. *Journal of Computer and System Sciences*, 5(1), 26–40. https://doi.org/10.1016/S0022-0000(71)80005-3
4. Tzeng, W.-G. (1992). A polynomial-time algorithm for the equivalence of probabilistic automata. *SIAM Journal on Computing*, 21(2), 216–227. https://doi.org/10.1137/0221017
5. Eilenberg, S., & Steenrod, N. (1952). *Foundations of Algebraic Topology*. Princeton University Press.
6. Zaslavsky, T. (1982). Signed graphs. *Discrete Applied Mathematics*, 4(1), 47–74. https://doi.org/10.1016/0166-218X(82)90033-6
7. Artin, E. (1925). Theorie der Zöpfe. *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*, 4, 47–72. https://doi.org/10.1007/BF02950718
8. Albuquerque, H., & Majid, S. (1999). Quasialgebra structure of the octonions. *Journal of Algebra*, 220(1), 188–224. https://doi.org/10.1006/jabr.1998.7850
9. Paige, L. J. (1956). A class of simple Moufang loops. *Proceedings of the American Mathematical Society*, 7(3), 471–482. https://doi.org/10.2307/2032757
10. Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *Journal of Mathematics and Mechanics*, 6(6), 885–893. https://doi.org/10.1512/iumj.1957.6.56050
11. Busch, P. (2003). Quantum states and generalized observables: A simple proof of Gleason's theorem. *Physical Review Letters*, 91(12), 120403. https://doi.org/10.1103/PhysRevLett.91.120403
12. Ivanović, I. D. (1981). Geometrical description of quantal state determination. *Journal of Physics A: Mathematical and General*, 14(12), 3241–3245. https://doi.org/10.1088/0305-4470/14/12/019
13. Wootters, W. K., & Fields, B. D. (1989). Optimal state-determination by mutually unbiased measurements. *Annals of Physics*, 191(2), 363–381. https://doi.org/10.1016/0003-4916(89)90322-9
14. Renes, J. M., Blume-Kohout, R., Scott, A. J., & Caves, C. M. (2004). Symmetric informationally complete quantum measurements. *Journal of Mathematical Physics*, 45(6), 2171–2180. https://doi.org/10.1063/1.1737053
15. Hoggar, S. G. (1982). Two quaternionic 4-polytopes. In *The Geometric Vein: The Coxeter Festschrift* (pp. 219–230). Springer. https://doi.org/10.1007/978-1-4612-5648-9_14
16. Welch, L. R. (1974). Lower bounds on the maximum cross correlation of signals. *IEEE Transactions on Information Theory*, 20(3), 397–399. https://doi.org/10.1109/TIT.1974.1055219
17. Peres, A. (1990). Incompatible results of quantum measurements. *Physics Letters A*, 151(3–4), 107–108. https://doi.org/10.1016/0375-9601(90)90172-K ; Mermin, N. D. (1990). Simple unified form for the major no-hidden-variables theorems. *Physical Review Letters*, 65(27), 3373–3376. https://doi.org/10.1103/PhysRevLett.65.3373
18. Hardy, L. (1993). Nonlocality for two particles without inequalities for almost all entangled states. *Physical Review Letters*, 71(11), 1665–1668. https://doi.org/10.1103/PhysRevLett.71.1665
19. Abramsky, S., & Brandenburger, A. (2011). The sheaf-theoretic structure of non-locality and contextuality. *New Journal of Physics*, 13(11), 113036. https://doi.org/10.1088/1367-2630/13/11/113036 ; Abramsky, S., Mansfield, S., & Soares Barbosa, R. (2012). The cohomology of non-locality and contextuality. *Electronic Proceedings in Theoretical Computer Science*, 95, 1–14. https://doi.org/10.4204/EPTCS.95.1
20. Whitney, H. (1957). *Geometric Integration Theory*. Princeton University Press.
21. Hilbert, D. (1888). Über die Darstellung definiter Formen als Summe von Formenquadraten. *Mathematische Annalen*, 32(3), 342–350 ; Choi, M. D., Lam, T. Y., & Reznick, B. (1995). Sums of squares of real polynomials. *Proceedings of Symposia in Pure Mathematics*, 58(2), 103–126.
22. Parrilo, P. A. (2000). *Structured Semidefinite Programs and Semialgebraic Geometry Methods in Robustness and Optimization* (PhD thesis, California Institute of Technology) ; Lasserre, J. B. (2001). Global optimization with polynomials and the problem of moments. *SIAM Journal on Optimization*, 11(3), 796–817 ; Gatermann, K., & Parrilo, P. A. (2004). Symmetry groups, semidefinite programs, and sums of squares. *Journal of Pure and Applied Algebra*, 192(1–3), 95–128. https://doi.org/10.1016/j.jpaa.2003.12.011
23. Lawvere, F. W. (1969). Diagonal arguments and cartesian closed categories. In *Category Theory, Homology Theory and their Applications II* (Lecture Notes in Mathematics, Vol. 92, pp. 134–145). Springer. Reprint in *Reprints in Theory and Applications of Categories*, 15 (2006), 1–13.

