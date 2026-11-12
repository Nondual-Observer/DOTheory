# Appendices to Volume III (`Appendices PM, GR, VP, AD`, Edition `v3.3`)

This file unites four reference and documentation appendices to the third volume of the monograph ("Book III: Domain Bridges, Verifications, and Program for the Next Step"):
1. **`Appendix PM` (`Summary Passports and Technical Tables of the Domain Bridges of Book III`)** — a unified reference table of all domain bridges `DB-01..DB-05` with model parameters, benchmark constructions, and falsification conditions.
2. **`Appendix GR` (`Registry of Verification Gates of Book III with Classification by Verification Type`)** — a complete description of all `16` gates of the single-threaded verifier `07_verify_full_book_III_v3_3.jl` with a clear separation into analytical/exhaustive proofs and integrity/lint checks.
3. **`Appendix VP` (`How to Verify the Book Independently`)** — the command to launch the verifier, passing criteria, analytical supplement to Chapters `III.1` and `III.3`, and the certification registry of all `15` statements of the volume.
4. **`Appendix AD` (`Concordance of Notation and Cross-Volume Structural Invariants of Book III`)** — a reference table of the main symbols of Volume III and their correspondence with the constructions of Books I and II.

---

## Appendix PM. Summary Passports and Technical Tables of the Domain Bridges of Book III

### Table PM.1. Unified Technical Summary of the Domain Bridges of `Chapters III.2–III.4` (`DB-01..DB-05`)

| Code and Chapter | Object / Canonical Source | Key Verified Invariants and Exact Numbers | Status |
| :--- | :--- | :--- | :---: |
| **`DB-01` (`Chapter III.2`)** | Directed weighted graphs; synthetic registry on $40$ vertices and two-triad graph on $6$ vertices (`Table III.2.1`) | `Lemma III.2.1(1–3)` (signs $\sigma$, retentions $\alpha$, permutation of unequal weights); roles $11 + 7 + 9 + 6 + 10 = 43$, five bifunctional vertices, $43 - 5 = 38$ labelled and $38 + 2 = 40$ records; sides $21 : 19$ across all records versus $19 : 19$ across labelled vertices (change of $\mathrm{Dom}(q)$); threshold $w < 2$: mass $32 \to 30$ and breakup into $2$ components; random-walk resolvent `Proposition III.2.1`: `0` loss of weight mass and $\min \widetilde{P}_1 = 5/1833 > 0$. | Proved |
| **`DB-02, DB-03` (`Chapter III.3`)** | Role graphs of *Sāṃkhya*, *Advaita*, and Pāṇini's $6$ *kārakas* | Self-dual mirror code $C = C^\perp \subset \mathbb{F}_2^6$ ($|C|=8$); $Q_3 \setminus \{000,111\} \cong O_6$; Möbius–Petersen intertwining $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$, $\mathcal{F}^{\mathsf{T}}\mathcal{F} = I_5$; gluing $O_6(\Lambda_4) \cap O_6(\Lambda_4') = \triangle(ME,MB,EB)$; roots of involutions $0$ in $\mathfrak{S}_6$ versus $12$ in $\mathfrak{S}_8$; $C_6(1,2) \cong O_6 = C_6 \sqcup 2C_3$; pair of $6$-cycles generates $9/9$ in $\mathrm{End}(V_-)$. | Core proved; dictionary is hypothesis (`L4`) |
| **`DB-04, DB-05` (`Chapter III.4`)** | Oracle-free cofactor merging and gauge symmetry of hidden Markov models | `Lemma III.4.1` ($\Pi_6 \to O_6$: $-3/+6$ edges, $+6$ triangles, $\dim_{\mathbb{F}_2}\ker p = 4$); `Theorem III.4.1` ($\gcd(X\pm Y, N)$ on $S_4 = \{\pm 1\}^2$, $r_{\mathrm{cyc}} = |E|-|V|+c$, oracle-free splitting of $N = 2537 = 43 \times 59$); `Theorem III.4.2` ($\mathfrak{S}_m$-invariance of HMM probability law over $\mathbb{Q}$ at $m = 2, 3$ and rational witness $41/200, 59/200$). | Proved |

---

## Appendix GR. Registry of Verification Gates of Book III with Classification by Verification Type

All `16` gates of the unified single-threaded verifier `07_verify_full_book_III_v3_3.jl` operate exclusively in exact integer, rational (`Rational{Int128}` / `Rational{BigInt}`), quadratic ($\mathbb{Q}(\sqrt{5})$), and finite-field ($\mathbb{F}_2$) arithmetic with zero floating-point types, and are divided into two classes:
- **`[PROOF / EXHAUSTIVE]`** — complete analytical, matrix, or exhaustive-enumeration proof of a mathematical statement in exact arithmetic;
- **`[INTEGRITY / LINT]`** — file integrity reconciliation, source self-audit confirming zero `Float64`, and strict text lint of the clean edition.

### Table GR.1. Complete Registry of Gates of the Verifier `07_verify_full_book_III_v3_3.jl`

| Gate Code | Chapter | Verified Statement | Gate Type |
| :--- | :---: | :--- | :---: |
| **`GATE-III01-01`** | `III.1` | `Proposition III.1.1`: continuation family $Q(x)=x(x-1)$ versus $P(x)=0$ on nodes $\{0,1\}$ diverging at $x_* = 1/2$ (`-1/4`) and $x_* = 2$ (`2`), together with rank-$2$ orthogonal projectors $P_1, P_2$ in $K^4$ satisfying $\mathrm{rk}(P_1 A P_1) = \mathrm{rk}(P_2 A P_2) = 1 < 2 = \mathrm{rk}(A)$ over $\mathbb{Q}$ and $\mathbb{F}_2$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III01-02`** | `III.1, III.3` | Triangulation of the Möbius strip $M_5$, characteristic polynomial of $K = B^{\mathsf{T}}B$, identity $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$ over $\mathbb{Q}$ and in $\mathbb{Q}(\sqrt{5})$, isometry $\mathcal{F}^{\mathsf{T}}\mathcal{F} = I_5$ across all orientations, and intertwining with $D_{10}$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III01-03`** | `III.1` | Rejected bridge $P_7 \not\cong \mathrm{PG}(2,2)$: absence of a nondegenerate projective morphism from the seven-vertex linear path $P_7$ (and $P_6 \sqcup \{v_7\}$) into the Fano plane $\mathrm{PG}(2,2)$ ($|\mathrm{GL}_3(\mathbb{F}_2)| = 168$ versus $|\mathrm{Aut}(P_7)| = 2$). | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III02-01`** | `III.2` | `Lemma III.2.1(1–3)`: opposite responses under sign flip $\sigma = \pm 1$, non-commutativity $[P_\pi, D_\alpha + W_\sigma] \ne 0$ when $\alpha(2) \ne \alpha(3)$, and counterexample of permuting unequal weights $w_1 \ne w_2$ on $\{1 \to 2, 1 \to 3\}$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III02-02`** | `III.2` | Synthetic registry of `Table III.2.1` on $40$ vertices ($43 - 5 = 38$, $38 + 2 = 40$, sides $(21, 19)$ versus $(19, 19)$) and exact rational inversion $\widetilde{P}_1 = \frac{1}{2}(I_6 - \frac{1}{2}P)^{-1}$ on the $6$-vertex graph (first column $(344/611,\dots)$, $\min \widetilde{P}_1 = 5/1833 > 0$, mass $32$ versus $30$). | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III02-03`** | `III.2` | `Proposition III.2.1`: conservativity of the resolvent $\widetilde{P}_\tau = (1-\alpha_\tau)(I - \alpha_\tau P)^{-1}$ over $\mathbb{Q}$ across multiple rational $\tau > 0$ ($\mathbf{1}^{\mathsf{T}}\widetilde{P}_\tau = \mathbf{1}^{\mathsf{T}}$ and `0` loss of weight mass). | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III03-01`** | `III.3` | `Proposition III.3.1` and `Lemma III.3.1`: self-dual mirror code $C = C^\perp \subset \mathbb{F}_2^6$ ($|C|=8$), isomorphism $Q_3 \setminus \{000,111\} \cong O_6$ and two $\mathbb{Z}_3$-orbits of weights $1$ and $2$, plus exhaustive check of all $512$ Boolean $3 \times 3$ tables. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III03-02`** | `III.3` | `Theorem III.3.1(1,3)` and `Lemma III.3.2`: duality of $\mathrm{KG}(5,2)$ and $J(5,2)=L(K_5)$ on $\Lambda_5$ (multiplicities $1, 5, 4$), gluing $O_6(\Lambda_4) \cap O_6(\Lambda_4') = \triangle(ME,MB,EB)$, and failure of the role folding $q(D)=q(N)=C$ across all surjections of $\Lambda_5$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III03-03`** | `III.3` | `Theorem III.3.2`: exhaustive search of $\mathfrak{S}_6$ ($720$ elements, $0$ roots of $r^2 = c_6$) and $\mathfrak{S}_8$ ($40{,}320$ elements, exactly $12$ products of two disjoint $4$-cycles with $r^2 = c_8 = (1\;2)(3\;4)(5\;6)(7\;8)$), together with the intersection $11 + 3 - 1 = 13$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III03-04`** | `III.3` | `Proposition III.3.2` and `Lemma III.3.3`: $C_6(1,2) \cong O_6 = C_6 \sqcup 2C_3$, distinction of the three index-$2$ subgroups in $W(B_3)$ ($W(B_3)^+ \cong \mathfrak{S}_4$, $T_h = A_4 \times C_2$, $W(D_3) \cong \mathfrak{S}_4$), and span rank of a single $6$-cycle ($3/9$) versus a pair of $6$-cycles ($9/9$) over $\mathbb{Q}$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III04-01`** | `III.4` | `Lemma III.4.1`: rebuilding the prism $\Pi_6$ ($9$ edges, $2$ triangles) into the octahedron $O_6$ ($12$ edges, $8$ triangles) and parity kernel $\dim_{\mathbb{F}_2}\ker p = 4$ in $\mathbb{F}_2^5$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III04-02`** | `III.4` | `Theorem III.4.1` and `DB-04`: oracle-free splitting of $N = 2537 = 43 \times 59$ via cycles of the $1\mathrm{LP}$/$2\mathrm{LP}$ cofactor multigraph ($r_{\mathrm{cyc}} = 2$, trivial cycle $C_1$ and splitting cycles $C_2, C_3$) and check on $N = 105$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III04-03`** | `III.4` | `Theorem III.4.2` and `DB-05`: exact $\mathfrak{S}_m$-invariance of the HMM probability distribution over $\mathbb{Q}$ at $m=2,3$ on all strings $y_{1:T}$ (including the rational witness $41/200, 59/200$). | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III05-01`** | `III.5` | `Theorem III.5.1` and `Lemma III.5.1`: acceptance of a valid morphism $\phi$, rejection of all corrupted certificates, counterexample to the necessity of a morphism without minimality of $M$, traversal of $X \times M$, and exact rational Grönwall bound for $L < 1, L = 1, L > 1$. | `[PROOF / EXHAUSTIVE]` |
| **`GATE-III-LINT`** | `Entire volume` | Text lint across all `7` files of Book III (`00_PASSPORT`, `01..05`, `06_APPENDICES`): absence of laboratory ciphers, local file paths, service stamps, and any non-mathematical domain references outside the declared bridges; chapter word count $\ge 11{,}000$ words. | `[INTEGRITY / LINT]` |
| **`GATE-III-SYS-FLOAT`** | `Verifier` | Source self-audit of `07_verify_full_book_III_v3_3.jl`: strictly `0` floating-point types or operations (`Float64`, `Float32`, `sqrt`, `cos`, `sin`, `exp`, `log`, `svd`, `eigen`). | `[INTEGRITY / LINT]` |

---

## Appendix VP. How to Verify the Book Independently

### VP.1. Running the Verifier

All numerical, matrix, and enumerative statements of Book III are verified by a single script `07_verify_full_book_III_v3_3.jl` located in the volume folder. Only the Julia language (version `1.10` or newer) with the standard libraries `LinearAlgebra`, `Printf`, `Dates`, and `SHA` is required; no external packages or network access are needed. Run from the volume folder:

```
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 07_verify_full_book_III_v3_3.jl
```

The verifier `07_verify_full_book_III_v3_3.jl` is written entirely in exact integer, rational (`Rational{Int128}` / `Rational{BigInt}`), quadratic ($\mathbb{Q}(\sqrt{5})$), and finite-field ($\mathbb{F}_2$) arithmetic (`0` floating-point operations, audited by `GATE-III-SYS-FLOAT`); single-threaded execution guarantees deterministic traversal order and a reproducible log.

### VP.2. What Counts as Passing

1. Each output line begins with `[PASS]` or `[FAIL]`, followed by the gate code, chapter, verification type (`Table GR.1`), and a concise summary of the verified quantities.
2. Upon the very first `[FAIL]`, the verifier halts with an error message.
3. Upon complete passage, the summary `16 / 16 ALL_PASS` is printed (`14` mathematical gates across Chapters `III.1–III.5`, the text-lint gate `GATE-III-LINT`, and the exact-arithmetic self-audit `GATE-III-SYS-FLOAT`), and the certificate `08_book_III_v3_3_master_certificate.json` is written with the Julia version, execution timestamp, `SHA-256` hash, and breakdown of every gate.
4. The gate `GATE-III-LINT` verifies all `7` markdown files of the volume: absence of laboratory tags and editorial stamps, and a total word count across the five chapters of at least `11,000` words.

### VP.3. Reading the Verification Alongside the Text

For every statement of the book referenced in Row 7 of a chapter passport, `Table GR.1` lists the corresponding gate. Open the chapter alongside the matching `let … end` block of the verifier: that block explicitly writes out the matrices, sets, and enumerations on which the statement is tested. The synthetic benchmarks of `Chapter III.2` (the $40$-vertex registry and the two-triad graph of mass $32$) and the cofactor multigraph of `Chapter III.4` are defined directly in code and can be varied to observe which hypothesis of a statement fails when altered.

### VP.4. Analytical Supplement to Chapters `III.1` and `III.3`

**Polynomial link between the Hodge Laplacian $K = B^{\mathsf{T}}B$ on the Möbius strip $M_5$ and the Petersen projector $\Pi_G$:**  
For the minimal triangulation $M_5$ on the $5$ vertices $\{0,1,2,3,4\}$ with $5$ faces $f_1=\{0,1,2\},\; f_2=\{0,1,3\},\; f_3=\{0,2,4\},\; f_4=\{1,3,4\},\; f_5=\{2,3,4\}$, each face contains exactly $3$ edges of the complete graph $K_5$ ($K_{ii} = 3$), and any two distinct faces share either one interior edge with oppositely matched orientation along the Möbius cycle ($K_{ij} = \pm 1$) or only a single vertex ($K_{ij} = 0$). By circulant $D_{10}$-symmetry, $K$ and $B^{\mathsf{T}} A_{\mathrm{KG}} B$ are simultaneously diagonalized in the Fourier basis of modes $m \in \{0, \pm 1, \pm 2\} \pmod 5$. On mode $m = 0$ we have $\lambda_0(K) = 5$ and $\lambda_0(H_o) = \frac{1}{6}(25 - 35 + 13) = \frac{3}{6} = \frac{1}{2}$; on modes $m = \pm 1, \pm 2$ we have $\lambda(K) = \frac{5 \pm \sqrt{5}}{2}$, $\lambda(K)^2 - 5\lambda(K) + 5 = 0$, whence
$$
\lambda(H_o) = \frac{1}{6}\bigl(\lambda(K)^2 - 7\lambda(K) + 13\bigr) = \frac{1}{6}\bigl(8 - 2\lambda(K)\bigr) = \frac{3 \mp \sqrt{5}}{6} > 0.
$$

### VP.5. Summary Certification Registry of the 15 Statements of Book III Across the Five Epistemic Statuses

In the table below, for each of the `15` headings of theorems, lemmas, and propositions of Volume III, we specify its epistemic status, classical foundation, contribution of this book, and verification gate in `07_verify_full_book_III_v3_3.jl`.

| No. | Statement | Epistemic Status | Classical Foundation | Contribution of This Book | `Julia` Gate |
| :-: | :--- | :--- | :--- | :--- | :--- |
| `1` | **Proposition III.1.1** | Proved prohibition / counterexample | Quotient of the polynomial ring $K[x]$ by the ideal of Lagrange interpolation nodes and rank properties of block matrix slices under orthogonal projections. | Combining the polynomial continuation torsor $P_c(x)$ and the rank-$1$ slice counterexample $P_i A P_i$ over $\mathbb{Q}$ and $\mathbb{F}_2$ into a unified algebraic falsification test for domain bridges. | `GATE-III01-01, GATE-III01-02` |
| `2` | **Lemma III.2.1** | Proved prohibition / counterexample | Signed graphs (F. Harary, 1953) and commutation conditions for permutation matrices with diagonal and weighted operators. | Proving the insufficiency of an unsigned weight matrix $W$ without transmission signs $\sigma$, retention coefficients $\alpha$, and fixed output-channel bindings. | `GATE-III02-01` |
| `3` | **Proposition III.2.1** | Extension of a classical theorem within contract $\Gamma$ | Neumann series and the random-walk resolvent on a directed graph (L. Katz index, 1953; PageRank core, 1998). | Contrasting the conservative resolvent $\widetilde{P}_\tau$ (`0` mass loss and preserved strong connectivity) against threshold edge truncation as a carrier substitution. | `GATE-III02-02, GATE-III02-03` |
| `4` | **Proposition III.3.1** | Extension of a classical theorem within contract $\Gamma$ | Binary self-dual code with generator matrix $[I_n \mid I_n]$ and exchange-involution projectors $\frac{1}{2}(I \pm \sigma)$. | Operational reading of $C = \ker\Delta = C^\perp \subset \mathbb{F}_2^{2n}$ as the error-free mirror code linking an external pattern to its internal trace. | `GATE-III03-01` |
| `5` | **Lemma III.3.1** | Original proved result of this book | Geometry of the three-dimensional Boolean cube $Q_3$, the complete tripartite graph $K_{2,2,2} \cong O_6$, and cyclic coordinate shifts. | Identifying the equatorial hexagon $C_6$ and the two filled triangular $\mathbb{Z}_3$-orbits of weights $1$ and $2$ on $Q_3 \setminus \{000,111\}$. | `GATE-III03-01` |
| `6` | **Theorem III.3.1** | Two-arrow structural correspondence (bridge) | Kneser graph $\mathrm{KG}(5,2)$ (L. Lovász, 1978), Johnson graph $J(5,2) = L(K_5)$, and minimal triangulation of the Möbius strip $M_5$. | Proving the polynomial identity $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$, the $D_{10}$-equivariant isometry $\mathcal{F} : C_2(M_5) \to \ker(A_{\mathrm{KG}}-I_{10})$, and the gluing of two octahedra along $\triangle(ME,MB,EB)$. | `GATE-III01-02, GATE-III03-02` |
| `7` | **Lemma III.3.2** | Proved prohibition / counterexample | Proper colorings of the Petersen graph ($\chi = 3$) and induced maps on pair graphs. | Proving that the role folding $q(D)=q(N)=C$ destroys edges of $\mathrm{KG}(5,2)$ and that no proper $3$-coloring of $\mathrm{KG}(5,2)$ is induced by any folding of the base alphabet $\Lambda_5$. | `GATE-III03-02` |
| `8` | **Theorem III.3.2** | Original proved result of this book | Classical criterion for square roots of permutations via even-length cycle counts. | Contrasting the impossibility of $r^2 = c_6$ in $\mathfrak{S}_6$ ($0$ solutions) against the $12$ solutions of $r^2 = c_8$ in $\mathfrak{S}_8$, each pairing antipodes with zero invariant pairs. | `GATE-III03-03` |
| `9` | **Proposition III.3.2** | Original proved result of this book | Circulant graph $C_6(1,2)$ on $\mathbb{Z}_6$ and step-length partition of octahedral edges. | Decomposing $E(O_6) = E(C_6) \sqcup E(C_3^{\mathrm{even}}) \sqcup E(C_3^{\mathrm{odd}})$ ($12 = 6 + 3 + 3$) across the three axes of case-role pairs in Pāṇini's scheme. | `GATE-III03-04` |
| `10` | **Lemma III.3.3** | Original proved result of this book | Representations of the hyperoctahedral group $W(B_3)$ and Burnside's theorem for absolutely irreducible representations (with trivial commutant $\mathbb{R}\cdot I_3$). | Separating the three index-$2$ subgroups of $W(B_3)$ and contrasting the algebra span of a single equatorial $6$-cycle ($3/9$) against a non-collinear pair ($9/9$) in $\mathrm{End}(V_-)$. | `GATE-III03-04` |
| `11` | **Lemma III.4.1** | Original proved result of this book | Edge deletion and addition on the $6$-vertex prism $K_3 \square K_2$ and the even-weight linear code in $\mathbb{F}_2^5$. | Exact edge and triangle balance when rebuilding the prism $\Pi_6$ into the octahedron $O_6$ ($\Delta|E| = -3 + 6 = +3$, $\Delta N_\triangle = +6$) and the $4$-dimensional even kernel. | `GATE-III04-01` |
| `12` | **Theorem III.4.1** | Extension of a classical theorem within contract $\Gamma$ | Congruence of squares of Kraitchik (1926) and Dixon (1981), Kirchhoff's cyclomatic rank (1847), and the two-large-prime cofactor graph of Lenstra and Manasse (1994). | Formulating the oracle-free relation-merging contract with zero access to $(p,q)$ and working through trivial versus splitting cycles on $N = 2537$. | `GATE-III04-02` |
| `13` | **Theorem III.4.2** | Two-arrow structural correspondence (bridge) | Invariance of hidden Markov model likelihood under state permutations $\mathfrak{S}_m$ (T. Petrie, 1969). | Formulating the relabelling gauge torsor $|\mathcal{R}| = m!$ as an exact obstruction to inferring external semantics from monolingual string statistics without a bilingual anchor. | `GATE-III04-03` |
| `14` | **Theorem III.5.1** | Extension of a classical theorem within contract $\Gamma$ | Equivalence testing and minimization of finite deterministic automata (E. F. Moore, 1956; J. E. Hopcroft and R. M. Karp, 1971). | Contrasting $O(|X|\cdot|\Sigma|)$ verification of an exhibited certificate $\phi : X \to M$, a counterexample to necessity without minimality of $M$, and $X \times M$ traversal. | `GATE-III05-01` |
| `15` | **Lemma III.5.1** | Classical result in operational notation | Discrete Grönwall lemma for the linear recurrent inequality $e_{t+1} \le L e_t + \varepsilon$. | Explicit trajectory-divergence budget and logarithmic prediction horizon for approximate dynamical bridges across all three regimes ($L < 1, L = 1, L > 1$). | `GATE-III05-01` |

---

## Appendix AD. Concordance of Notation and Cross-Volume Structural Invariants of Book III

| Symbol | Definition in Book III | Connection with Books I and II | Chapters in Book III |
| :--- | :--- | :--- | :---: |
| **$\Gamma = (X, \mathcal{Q}, \mathcal{A}, \mathrm{Dom}, Y, m_{\mathrm{acc}})$** | Operational contract of the observer with external typing condition $\mathcal{O} \notin X$ | Introduced in the `Introduction` and `Chapter I.1`; internal reflection via the Cantor–Lawvere diagonal proved in `Chapter II.9` | `III.1–III.5` |
| **$(\iota, \mathcal{O}_\pi)$** | Two-arrow domain bridge: $\iota$ embeds the core model object, $\mathcal{O}_\pi$ specifies procedural readout of data | Extends the separation of internal register $M$ and external carrier $X$ from `Chapters I.2–I.4` | `III.1–III.5` |
| **`L1, L2, L3, L4`** | Four epistemic levels: mathematical core (`L1`), primary source/table (`L2`), passported bridge (`L3`), dictionary of interpretations (`L4`) | Refine the five epistemic statuses of the mathematical core of Books I–II for external models | `III.1, III.3, III.5` |
| **`DB-01..DB-05`** | Five passported domain bridges of Volume III (unified numbering across `Chapter III.1` and `Table III.4.1`) | Built on $S_4$, $O_6$, $M_{\min}$, $(Z_D, Z_C, Z_F)$, and cohomology $\kappa \in H^1$ from Books I–II | `III.1–III.4` |
| **$\widetilde{P}_\tau = (I + \tau L)^{-1}$** | Conservative random-walk resolvent on the full weighted digraph ($\alpha_\tau = \frac{\tau}{1+\tau}$, mass conservation $\mathbf{1}^{\mathsf{T}}\widetilde{W}_\tau\mathbf{1} = M$) | Preserves the carrier $X$ with zero edge deletion, contrasting with window truncation in `Chapter II.1` | `III.2` |
| **$\mathrm{KG}(5,2),\, J(5,2),\, M_5$** | Petersen graph ($e \cap f = \varnothing$), Johnson graph ($|e \cap f| = 1$) on $10$ role pairs $\binom{\Lambda_5}{2}$, and $5$-face Möbius strip | Generalize the octahedron $O_6 \cong J(4,2)$ (`Chapter I.6`) and odd cocycle holonomy $\kappa$ (`Chapter I.9`, `Chapter II.3`) | `III.1, III.3` |
| **$\mathcal{F} = F_0 H_o^{-1/2}$** | Orthogonal $D_{10}$-equivariant Whitney–Hodge isometry $C_2(M_5) \to \ker(A_{\mathrm{KG}} - I_{10})$, $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$ | Connects cellular chains and the Hodge Laplacian (`Chapter II.3`) with the orientation sign character $\chi : D_{10} \to \{\pm 1\}$ | `III.1, III.3` |
| **$\mathcal{G}_{\mathrm{LP}},\; r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}})$** | Large-prime cofactor multigraph and Kirchhoff's cyclomatic rank $|E_{\mathrm{LP}}| - |V_{\mathrm{LP}}| + c = \dim_{\mathbb{F}_2} H_1(\mathcal{G}_{\mathrm{LP}};\mathbb{F}_2)$ | Realizes the oracle-free protocol of `Chapter I.8` and $1$-cycle homology over $\mathbb{F}_2$ (`Chapter I.9`) | `III.4` |
| **$\theta^\sigma = (P_\sigma^{\mathsf{T}}\pi_0, P_\sigma^{\mathsf{T}} A P_\sigma, P_\sigma^{\mathsf{T}} B)$** | Gauge $\mathfrak{S}_m$-orbit of HMM parameters generating the identical string distribution $\mathbb{P}(y_{1:T} \mid \theta^\sigma) = \mathbb{P}(y_{1:T} \mid \theta)$ | Canonical witness of the regime $|\mathcal{R}| = m! > 1$ (internal relabelling torsor without an external anchor, cf. `Chapter II.1`) | `III.4` |
| **$\mathcal{R} \subseteq X \times M,\; e_t \le L^t e_0 + \varepsilon\frac{L^t-1}{L-1}$** | Reachable core of the synchronous product of transition systems and discrete Grönwall divergence bound | Close the minimal Moore–Nerode realization theorem (`Chapter I.3`) and stability budget (`Chapter II.8`) | `III.5` |

---

## Classical Mathematical and Historical-Linguistic Sources of the Volume

Similarity of mathematical structures does not imply identity of historical concepts, and citing a classical source records the provenance of a theorem or primary text without transferring its authority to the applied interpretations of this book.

1. E. F. Codd, *A Relational Model of Data for Large Shared Data Banks*, Communications of the ACM **13**(6), 377–387 (1970): https://doi.org/10.1145/362384.362685.
2. E. F. Moore, *Gedanken-Experiments on Sequential Machines*, in: *Automata Studies*, Annals of Mathematics Studies **34**, Princeton University Press, 129–153 (1956): https://www.cs.cmu.edu/~cdm/resources/Moore1956-gedanken-experiments.pdf.
3. L. Lovász, *Kneser's Conjecture, Chromatic Number, and Homotopy*, Journal of Combinatorial Theory, Series A **25**(3), 319–324 (1978): https://doi.org/10.1016/0097-3165%2878%2990022-5.
4. L. Page, S. Brin, R. Motwani, and T. Winograd, *The PageRank Citation Ranking: Bringing Order to the Web*, Stanford InfoLab Technical Report (1998): https://cs.brown.edu/courses/csci2531/papers/pagerank.pdf.
5. T. Petrie, *Probabilistic Functions of Finite State Markov Chains*, Annals of Mathematical Statistics **40**(1), 97–115 (1969): https://www.jstor.org/stable/2239201; M. Stephens, *Dealing with Label Switching in Mixture Models*, Journal of the Royal Statistical Society B **62**(4), 795–809 (2000).
6. Īśvarakṛṣṇa, *Sāṃkhya-kārikā*; Patañjali, *Yoga-sūtras*; Gauḍapāda, *Māṇḍūkya-kārikā*; Śaṅkara, *Brahma-sūtra-bhāṣya*; Pāṇini, *Aṣṭādhyāyī*; Bhartṛhari, *Vākyapadīya* (exact citations by sūtra and kārikā are compiled in `Table III.3.2`).
7. M. Kraitchik, *Théorie des nombres*, Tome II, Gauthier-Villars, Paris (1926); J. D. Dixon, *Asymptotically Fast Factorization of Integers*, Mathematics of Computation **36**(153), 255–260 (1981); A. K. Lenstra and M. S. Manasse, *Factoring With Two Large Primes*, Mathematics of Computation **63**(208), 785–798 (1994).
8. G. Kirchhoff, *Ueber die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Ströme geführt wird*, Annalen der Physik und Chemie **148**(12), 497–508 (1847).
9. F. Harary, *On the Notion of Balance of a Signed Graph*, Michigan Mathematical Journal **2**(2), 143–146 (1953–1954): https://doi.org/10.1307/mmj/1028989917.
10. L. Katz, *A New Status Index Derived from Sociometric Analysis*, Psychometrika **18**(1), 39–43 (1953): https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Katz-1953-status.pdf.
11. J. E. Hopcroft and R. M. Karp, *A Linear Algorithm for Testing Equivalence of Finite Automata*, Cornell University Technical Report TR 71-114 (1971): https://hdl.handle.net/1813/5958.

This list records the classical mathematical and historical-linguistic primary sources upon which the definitions, classical theorems, and domain bridge passports of Volume III rest.
