# Chapter III.4. Rebuilding the Prism into the Octahedron, Cofactor Graphs, and Gauge Symmetry of Hidden Markov Models

In `Chapter I.7` and `Chapter I.8` we proved that any oracle-free investigation of a hidden arithmetic or symbolic object must operate across finite observation windows, Hankel matrices, and compatibility of local transfers. In this chapter we assemble the summary catalog of the five domain bridges of Volume III (**`DB-01..DB-05`**) and examine in detail two mathematical problems in which violating the oracle-free contract or conflating internal transition statistics with external semantics leads to systematic methodological errors:
1. **Oracle-free merging of partial multiplicative relations (`DB-04`)**: how fundamental cycles in the multigraph of large prime cofactors generate a congruence of squares $X^2 \equiv Y^2 \pmod N$ (`Theorem III.4.1`) under a complete prohibition against directly or indirectly accessing the secret prime factors $(p, q)$ (`Definition III.4.1`), and why on the four-state sign scene $S_4 = \{\pm 1\}^2$ some cycles degenerate into a trivial merge whereas others split $N$.
2. **Gauge $\mathfrak{S}_m$-symmetry of hidden Markov models (`DB-05`)**: why, by **Theorem `III.4.2`**, no internal transition statistics over an unlabelled symbol alphabet $\Sigma^*$ can uniquely identify an external semantic assignment of hidden states without an independent bilingual channel of joint observations.

---

## §III.4.1. Summary Catalog of Domain Bridges `DB-01..DB-05` and Rebuilding the Triangular Prism into the Octahedron

Let us bring together in a single table the five passported bridges of Volume III and prove a compact graph-and-code lemma on rebuilding the triangular prism into the octahedron and on the even linear subcode.

### Table III.4.1. Summary Registry of Domain Bridges `DB-01..DB-05`

| Bridge Code | Subject Domain and Chapter | First Arrow $\iota$ (Core Model Object) | Second Arrow $\mathcal{O}_\pi$ (Readout and Data) | Epistemic Status |
| :---: | :--- | :--- | :--- | :---: |
| **`DB-01`** | Directed weighted graphs and filtration (`Chapter III.2`) | Full weight matrix $W$, transmission signs $\sigma$, constants $\alpha$, and resolvent $\widetilde{P}_\tau$ | Synthetic $40$-vertex registry (inclusion-exclusion and $\mathrm{Dom}(q)$) and two-triad graph of mass $32$ (`0` weight loss) | Proved |
| **`DB-02`** | Role schemes of *Sāṃkhya* and *Advaita* (`Chapter III.3`) | Self-dual mirror code $C = C^\perp$, graphs $\mathrm{KG}(5,2)$, $J(5,2)$, $M_5$, and gluing of two $O_6$ | Textual enumerations in `SK, YS, MK, BSB` verified against critical editions | Graphs proved; dictionary interpretive (`L4`) |
| **`DB-03`** | Six case roles (*kāraka*) of Pāṇini's grammar (`Chapter III.3`) | Circulant $C_6(1,2) \cong O_6 = C_6 \sqcup 2C_3$ and pair of $6$-cycles in $\mathrm{End}(V_-) \cong M_3(\mathbb{R})$ | Verb valency rules in *Aṣṭādhyāyī* `1.4.23–55` | Algebra proved; role mapping model-based |
| **`DB-04`** | Oracle-free cofactor merging (`Chapter III.4`, §III.4.2) | Congruence of squares $X^2 \equiv Y^2 \pmod N$ on $S_4 = \{\pm 1\}^2$ and Kirchhoff's cyclomatic rank $r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}})$ | Residues $R(x) = x^2 - kN$, cofactor multigraph $\mathcal{G}_{\mathrm{LP}}$, and step-by-step splitting of $N = 2537 = 43 \times 59$ with zero access to $(p,q)$ | Proved |
| **`DB-05`** | Hidden Markov models and unlabelled strings (`Chapter III.4`, §III.4.3) | Gauge action of the permutation group $\mathfrak{S}_m$ on parameters $(\pi_0, A, B)$ | Probability distribution $\mathbb{P}(y_{1:T} \mid \theta)$ on $\Sigma^T$ and rational witness $41/200, 59/200$ | Proved |

### Lemma III.4.1 (Rebuilding the Triangular Prism $K_3 \square K_2$ into the Octahedron $O_6$ and the $4$-Dimensional Even Subcode in $\mathbb{F}_2^5$)

*Classical foundation.* Edge deletion and addition on the $6$-vertex prism $K_3 \square K_2$ and the even-weight linear code in $\mathbb{F}_2^5$. *Contribution of this book:* Exact edge and triangle balance when rebuilding the prism $\Pi_6$ into the octahedron $O_6$ ($\Delta|E| = -3 + 6 = +3$, $\Delta N_\triangle = +6$) and the $4$-dimensional even kernel.

1. **Rebuilding a prism into an octahedron on $6$ vertices:** *On the $6$ vertices $\{a_1, a_2, a_3, b_1, b_2, b_3\}$, let the $3$-regular graph of the triangular prism $\Pi_6 = K_3 \square K_2$ be given ($6$ vertices, $9$ edges: two parallel triangles $\triangle(a_1 a_2 a_3)$ and $\triangle(b_1 b_2 b_3)$ and three vertical rungs $a_i b_i$; the number of triangular faces is $N_\triangle(\Pi_6) = 2$). If one **deletes** the $3$ vertical rungs $\{a_1 b_1, a_2 b_2, a_3 b_3\}$ ($\Delta E_- = -3$), turning the pairs $\{a_i, b_i\}$ into three diagonals of opposition, and **adds** the $6$ skew cross-edges $\{a_i b_j : i \ne j\}$ ($\Delta E_+ = +6$), then the resulting graph coincides with the octahedron $O_6 \cong K_{2,2,2}$ having $9 - 3 + 6 = 12$ edges and $N_\triangle(O_6) = 2 + 6 = 8$ triangles ($\Delta |E| = +3$, $\Delta N_\triangle = +6$).*
2. **Even kernel in a $5$-bit feature space:** *For the linear parity functional $p(x_1, \dots, x_5) = x_1 \oplus x_2 \oplus x_3 \oplus x_4 \oplus x_5 : \mathbb{F}_2^5 \to \mathbb{F}_2$, the kernel $\ker p = \{x \in \mathbb{F}_2^5 : \mathrm{wt}(x) \equiv 0 \pmod 2\}$ has dimension $\dim_{\mathbb{F}_2} \ker p = 4$ ($|\ker p| = 16$), and the sign character $(-1)^{p(x)} \in \{+1, -1\}$ converts addition modulo $2$ into multiplicative sign multiplication.*

**Proof (analytical).** In the prism $\Pi_6$, two vertices from different triangular layers $a_i$ and $b_j$ are adjacent when $i = j$ ($3$ edges) and non-adjacent when $i \ne j$. Replacing the interlayer adjacency condition by its opposite ($i \ne j$, $6$ edges) makes each pair $\{a_i, b_i\}$ the unique non-adjacent pair inside the part $\pi_i = \{a_i, b_i\}$, which by definition of the complete tripartite graph gives $K_{2,2,2} \cong O_6$, where all $2^3 = 8$ transversals of the parts $\pi_1, \pi_2, \pi_3$ form triangles $K_3$. Item (2) follows from the rank-nullity theorem for the nonzero linear functional $p : \mathbb{F}_2^5 \twoheadrightarrow \mathbb{F}_2$: $\dim_{\mathbb{F}_2} \ker p = 5 - 1 = 4$. $\blacksquare$

---

## §III.4.2. Oracle-Free Cofactor Merging and Cyclomatic Rank of the Graph of Partial Relations (`DB-04`)

Let $N = p q$ be an odd composite integer whose factorization into primes $p, q$ ($1 < p < q < N$) is unknown to the observer. In `Chapter I.7` and `Chapter I.8` it was shown that direct addition and multiplication of residues in the ring $\mathbb{Z}/N\mathbb{Z}$ are accessible to a polynomial observer, whereas the decomposition into prime factors is hidden behind the multiplicative structure of the Chinese Remainder Theorem $\mathbb{Z}/N\mathbb{Z} \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$.

The classical Fermat–Kraitchik–Dixon method reduces finding a nontrivial divisor of $N$ to constructing a **nontrivial congruence of squares** $X^2 \equiv Y^2 \pmod N$ with $X \not\equiv \pm Y \pmod N$ out of partial multiplicative relations.

### Theorem III.4.1 (Classical Kraitchik–Dixon Congruence-of-Squares Criterion for Splitting $\gcd(X \pm Y, N)$ and Kirchhoff's Cyclomatic Rank of the Large-Prime Cofactor Graph)

*Classical foundation.* Congruence of squares of Kraitchik (1926) and Dixon (1981), Kirchhoff's cyclomatic rank (1847), and the two-large-prime cofactor graph of Lenstra and Manasse (1994). *Contribution of this book:* Formulating the oracle-free relation-merging contract with zero access to $(p,q)$ and working through trivial versus splitting cycles on $N = 2537$.

*Let $N = pq$ be the product of two distinct odd primes $p \ne q$. Then:*

1. **Criterion for a nontrivial congruence of squares on the four-state sign scene:** *Every pair of invertible residues $X, Y \in (\mathbb{Z}/N\mathbb{Z})^\times$ satisfying the congruence $X^2 \equiv Y^2 \pmod N$ determines a pair of sign ratios $(\varepsilon_p, \varepsilon_q) \in S_4 = \{\pm 1\}^2$, where $X \equiv \varepsilon_p Y \pmod p$ and $X \equiv \varepsilon_q Y \pmod q$, together with a pair of greatest common divisors $d_- = \gcd(X - Y, N)$ and $d_+ = \gcd(X + Y, N)$ satisfying $N \mid d_- d_+$. Specifically:*
   - *on the two diagonal cells $\varepsilon_p = \varepsilon_q$ ($X \equiv \pm Y \pmod N$), one has $\{d_-, d_+\} = \{1, N\}$ (a trivial merge yielding no divisor);*
   - *on the two off-diagonal cells $\varepsilon_p = -\varepsilon_q$ ($X \not\equiv \pm Y \pmod N$), one has $\{d_-, d_+\} = \{p, q\}$, which immediately yields both nontrivial prime factors of $N$.*
   *(Numerical illustration for $N = 105 = 3 \times 5 \times 7$: the congruence $29^2 = 841 \equiv 1 = 1^2 \pmod{105}$ gives $\gcd(29-1, 105) = \gcd(28, 105) = 7$ and $\gcd(29+1, 105) = \gcd(30, 105) = 15$, whereas the trivial congruence $104^2 \equiv 1^2 \pmod{105}$ gives $\gcd(104-1, 105) = 1$ and $\gcd(104+1, 105) = 105$).*
2. **Graph of large prime cofactors and cyclomatic count of combined smooth relations:** *Let $B = \{p_1, \dots, p_{|B|}\}$ be a fixed factor base of small primes (including the sign $-1$ where needed), and suppose a set of partial relations has been collected with at most two large prime cofactors $\ell, \ell' \notin B$:*
   $$
   x_k^2 \equiv \Biggl(\prod_{p_i \in B} p_i^{e_{k,i}}\Biggr) \cdot \ell_k \cdot \ell_k' \pmod N,
   $$
   *where fully $B$-smooth relations correspond to the distinguished vertex $\ell = 1$. Construct the undirected cofactor multigraph $\mathcal{G}_{\mathrm{LP}} = (V_{\mathrm{LP}}, E_{\mathrm{LP}})$ whose vertices are $1$ and the encountered large cofactors $\ell$, and in which each partial relation $k$ contributes an edge $e_k = \{\ell_k, \ell_k'\}$. Then every Eulerian subgraph ($1$-cycle over $\mathbb{F}_2$) $C \in Z_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2)$ corresponds to a product of relations in which all large prime cofactors $\ell \notin B$ enter with **even** exponent and collect into a known square $\bigl(\prod \ell^{m_\ell}\bigr)^2 \bmod N$, and the dimension of the space of all such combined $B$-smooth relations on the graph $\mathcal{G}_{\mathrm{LP}}$ with $c$ connected components equals its Kirchhoff cyclomatic rank (first Betti number):*
   $$
   r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}}) = |E_{\mathrm{LP}}| - |V_{\mathrm{LP}}| + c = \dim_{\mathbb{F}_2} H_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2).
   $$
   *As soon as $r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}}) > |B|$, the factor-base exponent-parity map $H_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2) \to \mathbb{F}_2^{|B|}$ has a nonzero kernel of dimension $\ge r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}}) - |B| \ge 1$, producing a congruence of squares $X^2 \equiv Y^2 \pmod N$.*

**Proof (analytical).**
1. From $N \mid (X^2 - Y^2) = (X - Y)(X + Y)$ and the coprimality of the distinct odd prime divisors $p \ne q$, it follows that each prime $r \in \{p, q\}$ divides exactly one of the differences $X - Y$ or $X + Y$ (otherwise $r \mid 2X$ and $r \mid 2Y$, contradicting $\gcd(X, N) = 1$). When $\varepsilon_p = -\varepsilon_q$, one of the integers $X-Y, X+Y$ is divisible by $p$ and coprime to $q$, while the other is divisible by $q$ and coprime to $p$, whence $\{\gcd(X-Y,N), \gcd(X+Y,N)\} = \{p, q\}$.
2. In the multigraph $\mathcal{G}_{\mathrm{LP}}$, the cellular boundary operator $\partial_1 : C_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2) \to C_0(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2)$ maps each edge $e_k = \{\ell_k, \ell_k'\}$ to the sum of its endpoints $\ell_k \oplus \ell_k'$ modulo $2$, which equals the exponent-oddness vector of the large prime cofactors in the product. Hence an edge subset $C \subseteq E_{\mathrm{LP}}$ belongs to $\ker \partial_1 = Z_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2)$ if and only if every vertex $\ell \in V_{\mathrm{LP}}$ is incident to an even number of edges from $C$, i.e. every cofactor $\ell \notin B$ enters the product to an even power $\ell^{2m_\ell}$. For a one-dimensional cell complex with $c$ connected components, $\mathrm{rk}_{\mathbb{F}_2}\partial_1 = |V_{\mathrm{LP}}| - c$, so $\dim_{\mathbb{F}_2} H_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2) = \dim_{\mathbb{F}_2} \ker \partial_1 = |E_{\mathrm{LP}}| - |V_{\mathrm{LP}}| + c$. When $r_{\mathrm{cyc}} > |B|$, nontriviality of the kernel of the factor-base parity map follows from rank-nullity over $\mathbb{F}_2$. $\blacksquare$

**Worked oracle-free merge of $1\mathrm{LP}$ and $2\mathrm{LP}$ cofactors for $N = 2537$.** Suppose the procedure is given only the odd composite integer $N = 2537$ ($\lfloor\sqrt{2537}\rfloor = 50$, with its prime factors hidden) and the singleton factor base $B = \{2\}$ ($|B| = 1$). Evaluating $R(x) = x^2 - 2537$ and stripping powers of $2$ by trial division yields four partial relations with large cofactors $\ell \in \{17, 37\} \notin B$:
- $e_1$ ($x_1 = 53$): $53^2 - 2537 = 272 = 2^4 \cdot 17$ — $1\mathrm{LP}$ edge $\{1, 17\}$;
- $e_2$ ($x_2 = 83$): $83^2 - 2537 = 4352 = 2^8 \cdot 17$ — second $1\mathrm{LP}$ edge $\{1, 17\}$;
- $e_3$ ($x_3 = 61$): $61^2 - 2537 = 1184 = 2^5 \cdot 37$ — $1\mathrm{LP}$ edge $\{1, 37\}$;
- $e_4$ ($x_4 = 87$): $87^2 - 2537 = 5032 = 2^3 \cdot 17 \cdot 37$ — $2\mathrm{LP}$ edge $\{17, 37\}$.

The connected cofactor multigraph $\mathcal{G}_{\mathrm{LP}}$ on $V_{\mathrm{LP}} = \{1, 17, 37\}$ ($|V_{\mathrm{LP}}| = 3$, $c = 1$, $|E_{\mathrm{LP}}| = 4$) has Kirchhoff cyclomatic rank $r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}}) = 4 - 3 + 1 = 2 > |B| = 1$. Across all three nonzero cycles in $H_1(\mathcal{G}_{\mathrm{LP}}; \mathbb{F}_2) \cong \mathbb{F}_2^2$, the summed exponent of $2$ is already even, allowing us to trace both outcomes of `Theorem III.4.1(1)` on the same modulus $N$:
1. **Triangle cycle $C_1 = \{e_1, e_3, e_4\}$ ($x = 53, 61, 87$):** multiplying gives $(53 \cdot 61 \cdot 87)^2 \equiv 2^{4+5+3}\cdot 17^2 \cdot 37^2 = (2^6 \cdot 629)^2 \pmod{2537}$, whence $X_1 = 281{,}271 \bmod 2537 = 2201$ and $Y_1 = 40{,}256 \bmod 2537 = 2201$. Here $X_1 \equiv +Y_1 \pmod{2537}$ (diagonal sign cell $\varepsilon_p = \varepsilon_q = +1$), giving $\{d_-, d_+\} = \{2537, 1\}$—a trivial merge.
2. **Triangle $2\mathrm{LP}$ cycle $C_2 = \{e_2, e_3, e_4\}$ ($x = 83, 61, 87$):** multiplying gives $(83 \cdot 61 \cdot 87)^2 \equiv 2^{8+5+3}\cdot 17^2 \cdot 37^2 = (2^8 \cdot 629)^2 \pmod{2537}$, whence $X_2 = 440{,}481 \bmod 2537 = 1580$ and $Y_2 = 161{,}024 \bmod 2537 = 1193$ ($X_2 \not\equiv \pm Y_2 \pmod{2537}$). The Euclidean algorithm splits $N$ with zero oracle access:
   $$
   \gcd(1580 - 1193,\, 2537) = \gcd(387,\, 2537) = 43, \qquad \gcd(1580 + 1193,\, 2537) = \gcd(2773,\, 2537) = 59, \qquad 43 \times 59 = 2537
   $$
   (the third cycle—the digon $C_3 = C_1 \oplus C_2 = \{e_1, e_2\}$—likewise gives $X_3 = 1862,\; Y_3 = 1088$ and the same nontrivial factorization $\{43, 59\}$, `GATE-III04-02`).

### Definition III.4.1 (Oracle-Free Cofactor Merging Contract)

To rule out the methodological error of "oracle leakage" (where diagnostic computation of residues $x \bmod p$ and $x \bmod q$ using factors known to a test author directly or indirectly influences candidate selection), every algorithm that builds and merges partial relations is audited against three mandatory conditions of the **Oracle-Free Contract**:
1. **Sole input to the protocol $\mathcal{O}_\pi$:** the procedure receives only the composite integer $N \in \mathbb{Z}_{>1}$; the prime divisors $(p, q)$ are absent from function arguments, global state, and configuration tables throughout the computation.
2. **Polynomially observable features:** while scanning arguments $x$ and factoring values $R(x) = x^2 - kN$, only functions computable in polynomial time from $(N, B, x)$ are admissible: valuations $v_{p_i}(R(x))$ at small primes $p_i \in B$, the residual cofactor $\ell(x) = |R(x)| / \prod_{p_i \in B} p_i^{v_{p_i}(R(x))}$, and cofactor collisions across edges of the multigraph $\mathcal{G}_{\mathrm{LP}}$.
3. **Disqualification rule:** any access to $(p, q)$, Euler's totient $\varphi(N)$, or Legendre symbols modulo the secret divisors prior to the final $\gcd(X \pm Y, N)$ call violates the oracle-free contract of `Chapter I.8` and invalidates the experiment regardless of the fraction of merges found.

---

## §III.4.3. Gauge $\mathfrak{S}_m$-Unidentifiability of Hidden Markov Models Without an External Anchor (`DB-05`)

We now turn to the second bridge of the chapter—applying finite stochastic automata and hidden Markov models (HMMs) to unlabelled symbol sequences $y_{1:T} \in \Sigma^T$. Low conditional transition entropy and rigid positional stratification of symbols in a corpus over a finite alphabet $\Sigma$ often create the illusion that recovering a hidden-state transition matrix is enough to establish from internal string statistics alone the external semantic meaning of each state or ending class. The following theorem proves why such an inference is mathematically impossible without an external channel of joint observations.

### Theorem III.4.2 (Classical Permutation Unidentifiability of Hidden Markov Models and Impossibility of Recovering External Semantics from Internal String Statistics Alone)

*Classical foundation.* Invariance of hidden Markov model likelihood under state permutations $\mathfrak{S}_m$ (T. Petrie, 1969). *Contribution of this book:* Formulating the relabelling gauge torsor $|\mathcal{R}| = m!$ (and transition-matrix automorphisms) as an exact obstruction to inferring external semantic labels from monolingual string statistics without a bilingual anchor.

*Suppose an observer has access solely to unlabelled symbol sequences $y_{1:T} = (y_1, \dots, y_T) \in \Sigma^T$ over a finite alphabet $\Sigma$, generated by a hidden Markov model with a finite set of hidden states $Z = \{1, \dots, m\}$, initial distribution $\pi_0 \in \Delta(Z)$, row-stochastic transition matrix $A \in \mathbb{R}^{m \times m}$ ($A_{ij} = \mathbb{P}(z_{t+1}=j \mid z_t=i)$), and symbol emission matrix $B \in \mathbb{R}^{m \times |\Sigma|}$ ($B_{i,a} = \mathbb{P}(y_t=a \mid z_t=i)$). Then:*

1. **Exact invariance of the probability distribution under the hidden-label permutation group $\mathfrak{S}_m$:** *For every permutation of hidden states $\sigma \in \mathfrak{S}_m$ with permutation matrix $P_\sigma \in \{0,1\}^{m \times m}$, the transformed parameters*
   $$
   \theta^\sigma = (\pi_0^\sigma, A^\sigma, B^\sigma) = \bigl(P_\sigma^{\mathsf{T}} \pi_0,\; P_\sigma^{\mathsf{T}} A P_\sigma,\; P_\sigma^{\mathsf{T}} B\bigr)
   $$
   *generate **identically the same** probability distribution over all symbol strings $y_{1:T} \in \Sigma^T$ of every finite length $T \ge 1$:*
   $$
   \mathbb{P}(y_{1:T} \mid \theta^\sigma) = \mathbb{P}(y_{1:T} \mid \theta) \qquad \forall\,y_{1:T} \in \Sigma^T, \;\forall\,\sigma \in \mathfrak{S}_m.
   $$
2. **Unidentifiability of external semantic binding without a bilingual anchor:** *Let $\mathcal{M}$ be an external set of domain or grammatical meanings ($|\mathcal{M}| \ge m$), and suppose two bijective semantic interpretations $s_1, s_2 : Z \to \mathcal{M}$ differ by a permutation $s_2 = s_1 \circ \sigma^{-1}$ ($\sigma \in \mathfrak{S}_m$, $\sigma \ne \mathrm{id}$). Even if the transition matrix $A$ and initial vector $\pi_0$ are fixed and invariant under $\sigma$ ($P_\sigma^{\mathsf{T}} A P_\sigma = A$, $P_\sigma^{\mathsf{T}} \pi_0 = \pi_0$), in the absence of an external channel of joint observations $\mathcal{O}_{\mathrm{ext}}$ on $\Sigma^* \times \mathcal{M}$ (a "bilingual text" or independent external labelling), no statistical estimator on the observable string space $\Sigma^T$ can distinguish the models $(\theta, s_1)$ and $(\theta^\sigma, s_2)$: both the total variation distance and the Kullback–Leibler divergence between their output measures on $\Sigma^T$ are identically zero.*

**Proof (analytical).**
For any string $y_{1:T} \in \Sigma^T$, summing over all $m^T$ hidden-state paths expresses the marginal probability $\mathbb{P}(y_{1:T} \mid \theta)$ via the diagonal emission matrices $D(a) = \mathrm{diag}(B_{1,a}, \dots, B_{m,a})$ as the matrix product
$$
\mathbb{P}(y_{1:T} \mid \theta) = \pi_0^{\mathsf{T}} D(y_1) A D(y_2) A \cdots A D(y_T) \mathbf{1}_m.
$$
Substituting $\pi_0^\sigma = P_\sigma^{\mathsf{T}} \pi_0$, $A^\sigma = P_\sigma^{\mathsf{T}} A P_\sigma$, $D^\sigma(a) = P_\sigma^{\mathsf{T}} D(a) P_\sigma$ and using the orthogonality of the permutation matrix $P_\sigma P_\sigma^{\mathsf{T}} = I_m$ together with invariance of the all-ones vector $P_\sigma \mathbf{1}_m = \mathbf{1}_m$, all interior pairs $P_\sigma P_\sigma^{\mathsf{T}}$ cancel:
$$
\mathbb{P}(y_{1:T} \mid \theta^\sigma) = \pi_0^{\mathsf{T}} P_\sigma \bigl(P_\sigma^{\mathsf{T}} D(y_1) P_\sigma\bigr)\bigl(P_\sigma^{\mathsf{T}} A P_\sigma\bigr) \cdots \bigl(P_\sigma^{\mathsf{T}} D(y_T) P_\sigma\bigr) \mathbf{1}_m = \pi_0^{\mathsf{T}} D(y_1) A \cdots D(y_T) \mathbf{1}_m = \mathbb{P}(y_{1:T} \mid \theta).
$$
Item (2) follows directly from equality of the measures $\mathbb{P}(\cdot \mid \theta^\sigma) = \mathbb{P}(\cdot \mid \theta)$ across all of $\Sigma^T$ for every $T \ge 1$: the distribution of every decision rule $f : \Sigma^T \to \{s_1, s_2\}$ is identical under both hypotheses. $\blacksquare$

**Explicit rational witness of permutation indistinguishability ($|\mathcal{R}| = m! = 2$).** Set $m = 2$, $\Sigma = \{\texttt{a}, \texttt{b}\}$, $\pi_0 = (\frac{1}{2}, \frac{1}{2})^{\mathsf{T}}$, symmetric transition matrix $A = \begin{psmallmatrix} 3/4 & 1/4 \\ 1/4 & 3/4 \end{psmallmatrix}$ ($P_\sigma^{\mathsf{T}} A P_\sigma = A$ for the transposition $\sigma = (1\;2)$), and emission matrix $B = \begin{psmallmatrix} 4/5 & 1/5 \\ 1/5 & 4/5 \end{psmallmatrix}$. Under the hidden-role swap $\sigma = (1\;2)$, the parameters $\theta^\sigma = (\pi_0, A, B^\sigma)$ with $B^\sigma = \begin{psmallmatrix} 1/5 & 4/5 \\ 4/5 & 1/5 \end{psmallmatrix} \ne B$ exchange the emission profiles of states $1$ and $2$, yet generate the exact same rational distribution on every word, in particular at $T = 2$:
$$
\mathbb{P}(\texttt{ab} \mid \theta) = \frac{12 + 16 + 1 + 12}{200} = \frac{41}{200} = \frac{12 + 1 + 16 + 12}{200} = \mathbb{P}(\texttt{ab} \mid \theta^\sigma),
$$
and similarly $\mathbb{P}(\texttt{aa}) = \mathbb{P}(\texttt{bb}) = \frac{59}{200}$, $\mathbb{P}(\texttt{ba}) = \frac{41}{200}$ ($\frac{59+41+41+59}{200} = 1$; in `GATE-III04-03` the identity is also verified over $\mathbb{Q}$ across all $|\mathfrak{S}_3| = 6$ permutations of an asymmetric three-state model on all binary words of lengths $T = 1, \dots, 4$). Internal morphostatistics can separate a low-rank positional automaton from uniform random noise, yet without an external bilingual anchor it cannot select a single point on the $\mathfrak{S}_m$-orbit of semantic interpretations.

---

## §III.4.4. Domain Bridge Passport for `Chapter III.4` (Oracle-Free Cofactor Graphs `DB-04` and Hidden Markov Models `DB-05`)

| No. | Passport Row | Content for Bridges `DB-04` and `DB-05` |
| :---: | :--- | :--- |
| **1** | **Subject and primary data** | `DB-04`: odd composite moduli $N = pq$ (worked benchmarks $N = 105$ and $N = 2537 = 43 \times 59$ with factor base $B = \{2\}$). `DB-05`: finite hidden Markov models $(\pi_0, A, B)$ over the rational field $\mathbb{Q}$ at $m = 2$ and $m = 3$ on the string space $\Sigma^T$. |
| **2** | **Quantities, scales, and procedure** | `DB-04`: quadratic residues $R(x) = x^2 - kN$, cofactors $\ell(x) \notin B$, Kirchhoff's cyclomatic rank $r_{\mathrm{cyc}}(\mathcal{G}_{\mathrm{LP}}) = |E_{\mathrm{LP}}| - |V_{\mathrm{LP}}| + c$, and $\gcd(X \pm Y, N)$. `DB-05`: exact rational string probabilities $\mathbb{P}(y_{1:T} \mid \theta^\sigma)$ along the full orbit $\sigma \in \mathfrak{S}_m$. |
| **3** | **Split prior to fitting** | `DB-04`: the factor base $B$ and edge-selection rule $\{\ell_k, \ell_k'\}$ are fixed prior to cycle search with zero access to $(p, q)$ (`Definition III.4.1`). `DB-05`: the group action of $\mathfrak{S}_m$ is defined canonically prior to evaluating any particular string $y_{1:T}$. |
| **4** | **Free choices and degrees of freedom** | In `Lemma III.4.1` and `Theorems III.4.1–III.4.2` there are **`0`** free fitting parameters. In `DB-05`, the relabelling gauge torsor has cardinality $|\mathfrak{S}_m| = m!$ (or $|\mathrm{Aut}(A,\pi_0)|$ when the hidden chain dynamics are fixed). |
| **5** | **Null and surrogate control** | `DB-04`: trivial cycle $C_1 = \{e_1, e_3, e_4\}$ ($X_1 \equiv +Y_1 \pmod{2537}$, $\gcd = 1$) versus splitting cycles $C_2, C_3$ ($X \not\equiv \pm Y$, $\{43, 59\}$). `DB-05`: permuted emission matrix $B^\sigma \ne B$ yielding zero divergence on observable string distributions ($41/200 = 41/200$). |
| **6** | **Pre-specified comparison and full cost** | Exact verification of the prism-to-octahedron balance $\Pi_6 \to O_6$ ($\Delta|E| = +3, \Delta N_\triangle = +6$), nullity $\dim_{\mathbb{F}_2}\ker p = 4$, identity $r_{\mathrm{cyc}} = 4 - 3 + 1 = 2 > 1$ on $N = 2537$, and coincidence of all probabilities $\mathbb{P}(y_{1:T} \mid \theta^\sigma)$ over $\mathbb{Q}$ at $m = 2, 3$. |
| **7** | **Falsification condition and reproducibility** | `DB-04` is disqualified upon any access to $(p, q)$ prior to the final $\gcd(X \pm Y, N)$ step; any claim of unique semantic decipherment from an internal HMM transition matrix alone is refuted by `Theorem III.4.2`. All computations are reproducible in `07_verify_full_book_III_v3_3.jl` (`GATE-III04-01..03`). |
| **8** | **Position of the Observer in the bridge ($\Gamma, \iota, \mathcal{O}_\pi$)** | In both bridges, the Observer operates in a **strictly oracle-free regime** (`Chapter I.8`): in `DB-04` the protocol $\mathcal{O}_\pi$ sees only factorizations of $x^2 - kN$ over $B$ and cycles in $\mathcal{G}_{\mathrm{LP}}$, while the hidden sign pair $(\varepsilon_p, \varepsilon_q) \in S_4 = \{\pm 1\}^2$ separates trivial merges from nontrivial splits; in `DB-05` the protocol sees only surface strings $\Sigma^T$, while the group $\mathfrak{S}_m$ forms the indistinguishability kernel of internal labels in the absence of an external anchor. |

---

### What This Chapter Transmits to the Next (`Chapter III.4` $\to$ `Chapter III.5`)

Across `Chapters III.1–III.4` we formulated the law of the two-arrow domain bridge and verified it across five independent models (`DB-01..DB-05`)—ranging from directed weighted graphs and the conservative resolvent to the role graphs of *Sāṃkhya* and *Pāṇini*, oracle-free multigraphs of large prime cofactors, and the gauge symmetry of hidden Markov models. In the concluding chapter of the monograph (`Chapter III.5`), we consolidate the acceptance rules for any new result into a formal verifiable protocol (sufficiency of an exhibited morphism and decidability of equivalence on the reachable product $X \times M$, the discrete Grönwall bound, and the level-transition matrix `L1–L4`) and close the single deductive arc across all **`24` structural parts of the three books** (`Introduction + 9 chapters of Book I + 9 chapters of Book II + 5 chapters of Book III`).
