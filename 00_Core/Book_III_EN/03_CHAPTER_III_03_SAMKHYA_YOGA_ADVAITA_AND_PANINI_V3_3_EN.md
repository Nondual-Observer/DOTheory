# Chapter III.3. Sāṃkhya, Yoga, Advaita, and Pāṇini: Role Discrimination, Pair Graphs, and the Limits of Transfer

In classical Indian philosophy and linguistics (from Īśvarakṛṣṇa's *Sāṃkhya-kārikā* and Patañjali's *Yoga-sūtras* to Gauḍapāda's and Śaṅkara's *Advaita Vedānta* and Pāṇini's grammar *Aṣṭādhyāyī*), the central subject of analysis is the **structure of the act of discrimination, naming, and action**: who is the pure witness (*sākṣin / puruṣa*), what constitutes the tripartite internal instrument of cognition (*antaḥkaraṇa*: mind-*manas*, self-reference-*ahaṃkāra*, decisive discrimination-*buddhi*), how the six case roles of action (*kāraka*) bind agent, object, and instrument in a verbal root, and why identifying the witness with the instrument (*adhyāsa*, superimposition, or *aviveka*, non-discrimination) generates a systematic distortion of the picture.

In accordance with the law of the domain bridge (`Chapter III.1, §III.1.4`), comparing the mathematical core with philosophical and grammatical canons requires special rigor. Any attempt to declare an ancient text a "proof" of a mathematical theorem or, conversely, to pass off an external coincidence of numbers as structural identity immediately destroys trust in the work (in `Chapter III.1, §III.1.5` we already examined the paradigmatic rejected bridge $P_7 \not\cong \mathrm{PG}(2,2)$). Therefore, in the present chapter we enforce a strict demarcation: all statements of the mathematical core—on the self-dual mirror-reflection code, the pair graphs $\mathrm{KG}(5,2)$, $J(5,2) = L(K_5)$, and $O_6 = J(4,2) = L(K_4)$, the isometric intertwining of the Petersen graph with the Möbius strip $M_5$, the gluing of two octahedra along a shared triangle of internal roles, odd cycles arising when folding the witness onto the object, square roots of complement involutions in $\mathfrak{S}_6$ and $\mathfrak{S}_8$, and the generation of the $9$-dimensional dipole algebra $\mathrm{End}(V_-)$ by a pair of equatorial $6$-cycles—are proved strictly within the formal definitions of this book and explicitly separated from the philological table of primary sources (`L2`) and the dictionary of interpretations `REG-INTERP` (`L4`).

---

## §III.3.1. The Observer Typing Condition, the Self-Dual Mirror Code, and Two Orbits on the Octahedron $O_6$

In the `Introduction` (Part II) and `Chapter I.1`, the position of the Observer $\mathcal{O}$ was separated from the set of distinguishable states of the carrier $X$ by the typing rule $\mathcal{O} \notin X$: the casing of an instrument or a photograph of a camera may enter the frame $X$ as one of the objects $x \in X$, but the operator position $\Gamma$ itself, which specifies the cut of questions $\mathcal{Q}$ and partial actions $\mathcal{A}$ over $X$, is a structure of higher type and is not an element of $X$. In `Chapter II.9` (`Theorem II.9.1`) this principle received an exact internal reflection in the **Cantor–Lawvere diagonal theorem**: in no cartesian closed category with an object of truth values $Y$ admitting a fixed-point-free endomorphism $\neg : Y \to Y$ does there exist a surjective internal coding $e : X \times X \to Y$ of all predicates $Y^X$ by elements of $X$ itself (even on a three-element carrier $|X| = 3$, the three rows of a $3 \times 3$ table cannot generate all $2^3 = 8$ Boolean columns, and the anti-diagonal predicate $g(x) = \neg e(x,x)$ is guaranteed to be absent among the rows).

> **Methodological demarcation (`Introduction` versus `Chapter II.9`).** The rule $\mathcal{O} \notin X$ is the initial **typing condition** of the operational contract $\Gamma$, adopted in the `Introduction` as the definition of the boundary of the model; the Cantor–Lawvere diagonal theorem (`Chapter II.9`) proves the impossibility of complete internal self-coding of predicates $Y^X$ inside $X$, but does not "derive" the external position $\mathcal{O}$ from $X$. In the classical *Sāṃkhya-kārikā* (`SK 19–20`) and in the introductory section of Śaṅkara's *Brahma-sūtra-bhāṣya* (`BSB 1.1.1`, *adhyāsa-bhāṣya*), this exact distinction is drawn: the witness (*sākṣin*, cf. `SK 19`: *tasmāc ca viparyāsāt siddhaṃ sākṣitvam asya puruṣasya*) is by type not an object from the field of *prakṛti* (*yuṣmat-pratyaya-gocara*, the domain of "thou / this"), and attributing the properties of the instrument to the witness and vice versa is a categorical superimposition (*adhyāsa*). The image of a colorless crystal appearing red next to a hibiscus flower (*kusumavac ca maṇiḥ*) goes back to the commentarial tradition on `SK 20` and to the *Sāṃkhya-sūtras* (`SS 2.35`, cf. also *Yoga-sūtras* `YS 1.41`: *abhijātasyeva maṇer*), where it illustrates the induced coloring of the instrument's response without altering the witness itself.

When, within a model, one constructs a **symmetric mirror reflection** of an external state code $x_{\mathrm{ext}} \in \mathbb{F}_2^n$ into an internal register $x_{\mathrm{int}} \in \mathbb{F}_2^n$, a canonical linear self-dual code arises:

### Proposition III.3.1 (Self-Dual Code of an Ideal Mirror in $\mathbb{F}_2^{2n}$ and Weight Balance)

*Classical foundation.* Binary self-dual code with generator matrix $[I_n \mid I_n]$ and exchange-involution projectors $\frac{1}{2}(I \pm \sigma)$. *Contribution of this book:* Operational reading of $C = \ker\Delta = C^\perp \subset \mathbb{F}_2^{2n}$ as the error-free mirror code linking an external pattern to its internal trace.

*Let the space of pairs "external pattern — internal trace" be given as $\mathbb{F}_2^{2n} = \mathbb{F}_2^n \oplus \mathbb{F}_2^n$ with the canonical symmetric bilinear form $\langle (u_1, v_1), (u_2, v_2) \rangle = u_1 \cdot u_2 + v_1 \cdot v_2 \pmod 2$ and the mismatch (reflection error) operator*
$$
\Delta : \mathbb{F}_2^{2n} \to \mathbb{F}_2^n, \qquad \Delta(x_{\mathrm{ext}}, x_{\mathrm{int}}) = x_{\mathrm{ext}} \oplus x_{\mathrm{int}}.
$$
*Then:*

1. **Self-duality of the error-free reflection code:** *The kernel of the mismatch operator $C = \ker \Delta = \{(x, x) : x \in \mathbb{F}_2^n\} \subset \mathbb{F}_2^{2n}$ has dimension $\dim_{\mathbb{F}_2} C = n$ and coincides with its orthogonal complement: $C = C^\perp$. In particular, for $n = 3$ in the $6$-dimensional Boolean cube $Q_6 = \mathbb{F}_2^6$, the ideal mirror code $C$ consists of $|C| = 2^3 = 8$ words of even weight and is a $[6, 3, 2]$ self-dual linear code.*
2. **Involution exchanging external and internal:** *The linear exchange involution $\sigma(x_{\mathrm{ext}}, x_{\mathrm{int}}) = (x_{\mathrm{int}}, x_{\mathrm{ext}})$ satisfies $\sigma^2 = I_{2n}$, with $C = \mathrm{Fix}(\sigma) = \ker(I_{2n} \oplus \sigma)$ over $\mathbb{F}_2$, while over a field of characteristic $\ne 2$ the symmetric projector $\Pi_+ = \frac{1}{2}(I_{2n} + \sigma)$ and the antisymmetric mismatch projector $\Pi_- = \frac{1}{2}(I_{2n} - \sigma)$ yield an orthogonal decomposition $\Bbbk^{2n} = V_+ \oplus V_-$ with equal weights $\frac{1}{2}$ and $\frac{1}{2}$.*

**Proof (analytical).** For any $(x, x), (y, y) \in C$ we have $\langle (x, x), (y, y) \rangle = x \cdot y + x \cdot y = 0 \pmod 2$, whence $C \subseteq C^\perp$. Since the bilinear form is nondegenerate on $\mathbb{F}_2^{2n}$, $\dim C^\perp = 2n - \dim C = 2n - n = n = \dim C$, and therefore $C = C^\perp$. Item (2) is verified by direct squaring: $\Pi_\pm^2 = \Pi_\pm$ and $\Pi_+ \Pi_- = 0$. $\blacksquare$

> **Remark III.3.1 (On the weight shift when conflating a tripartite instrument with a bipartite pair).** If the three components of the internal instrument ($M, E, B$) carry equal shares $\frac{1}{3}$ in a symmetric normalization, and upon losing one of the discrimination channels the weight is redistributed equally between the remaining two ($\frac{1}{2}$), then the elementary arithmetic shift in the share of a single channel is $\frac{1}{2} - \frac{1}{3} = \frac{1}{6}$. This arithmetic identity is convenient as a mnemonic marker for weight skew when a tripartite scheme degenerates into a bipartite one, but in itself it is a numerical consequence of normalization rather than an independent theorem.

Consider now the three-bit cube $Q_3 = \mathbb{F}_2^3$, corresponding to the three binary axes of description in `Chapter I.2` (`§I.2.4`). If we remove from $Q_3$ the two diametrically opposite monochromatic vertices—the all-zero word $000$ and the all-one word $111$, in which all three channels are indistinguishable from one another—the remaining six vertices form the octahedron $O_6$:

### Lemma III.3.1 (Induced Subgraph $Q_3 \setminus \{000, 111\} \cong O_6$ and Two $\mathbb{Z}_3$-Orbits)

*Classical foundation.* Geometry of the three-dimensional Boolean cube $Q_3$, the complete tripartite graph $K_{2,2,2} \cong O_6$, and cyclic coordinate shifts. *Contribution of this book:* Identifying the equatorial hexagon $C_6$ and the two filled triangular $\mathbb{Z}_3$-orbits of weights $1$ and $2$ on $Q_3 \setminus \{000,111\}$.

*Let $Q_3 = \mathbb{F}_2^3$ be the graph of the three-dimensional Boolean cube, in which two vertices are connected by an edge at Hamming distance $d_H(u,v) = 1$, or, equivalently, on the set $V_6 = Q_3 \setminus \{000, 111\}$ of the six non-monochromatic words let edges be drawn between all pairs $u \ne v$ with $u \ne \bar{v}$ ($\bar{v} = v \oplus 111$, Hamming distance $d_H(u,v) \in \{1, 2\}$). Then:*

1. **Isomorphism with the octahedron $O_6 = K_{2,2,2}$:** *The three pairs of componentwise opposite words*
   $$
   \pi_1 = \{100, 011\}, \qquad \pi_2 = \{010, 101\}, \qquad \pi_3 = \{001, 110\}
   $$
   *lie at distance $d_H = 3$ within each pair and at distance $d_H \in \{1, 2\}$ between any words from distinct pairs. Therefore, the graph on $V_6$ with edges $d_H(u,v) \in \{1,2\}$ is isomorphic to the complete tripartite graph $K_{2,2,2} = O_6$ ($6$ vertices, $12$ edges, degree of every vertex equal to $4$), while the induced subgraph of the cube $Q_3[V_6]$ ($d_H(u,v) = 1$) is the equatorial hexagon $C_6$: $(100) - (110) - (010) - (011) - (001) - (101) - (100)$.*
2. **Two $\mathbb{Z}_3$-orbits of cyclic axis shift:** *The group of cyclic permutations of the three coordinates $\mathbb{Z}_3 = \langle (1\;2\;3) \rangle$ acts on $Q_3$ by automorphisms, fixes both poles $000$ and $111$, and partitions $V_6$ into exactly two disjoint orbits of length $3$ by Hamming weight:*
   $$
   \mathcal{O}_{\mathrm{wt}=1} = \{100, 010, 001\}, \qquad \mathcal{O}_{\mathrm{wt}=2} = \{110, 011, 101\},
   $$
   *each of which forms in $O_6$ a filled triangle ($K_3$), corresponding to two opposite faces of the octahedron in the checkerboard splitting $8 = 4 + 4$ (`Theorem I.9.3a`).*

**Proof (analytical).** For any $u \in V_6$, the unique vertex in $Q_3$ at distance $d_H(u,v) = 3$ is its componentwise negation $\bar{u} = u \oplus 111 \in V_6$. Consequently, excluding the pairs $\{u, \bar{u}\}$ from $K_6$ removes exactly $3$ independent edges $\pi_1, \pi_2, \pi_3$ and yields $O_6 \cong K_{2,2,2}$ with $\binom{6}{2} - 3 = 12$ edges. Since cyclic coordinate shift preserves the Hamming weight $\mathrm{wt}(u) \in \{1,2\}$, and words of weight $1$ and $2$ contain no triples with all three bits equal, the action of $\mathbb{Z}_3$ is transitive on each of the two spheres $\mathrm{wt} = 1$ and $\mathrm{wt} = 2$ of size $\binom{3}{1} = \binom{3}{2} = 3$. $\blacksquare$

> **Demarcation between mathematical fact and philosophical interpretation (level `L4`).** In the classical *Māṇḍūkya Upaniṣad* (`MU 3–7`) and Gauḍapāda's *Māṇḍūkya-kārikā* (`MK 1.1–16`), the four states (*jāgrat*: waking; *svapna*: dreaming; *suṣupti*: deep dreamless sleep; and *turīya*: the fourth, timeless witnessing) describe regimes of engagement of external and internal activity. If in an illustrative Boolean scheme we assign a bit $E \in \{0,1\}$ to external support and a bit $M \in \{0,1\}$ to internal elaboration, then the cell $(E=1, M=0)$ ("external perception with the internal instrument completely switched off") is excluded **by the very definition of the model** (external sense in *Sāṃkhya* and *Vedānta* is not read without the participation of *manas*, cf. `SK 35`), leaving the three working regimes $(1,1), (0,1), (0,0)$, while *turīya* is matched to the observation frame $\Gamma$ itself. This correspondence belongs to the dictionary of interpretations `REG-INTERP` (`L4`) and must not be presented as a consequence of `Lemma III.3.1`.

---

## §III.3.2. Five-Element and Four-Element Role Alphabets, the Graphs $\mathrm{KG}(5,2)$, $J(5,2) = L(K_5)$, the Möbius–Petersen Intertwining, and the Gluing of Two Octahedra

To investigate the graphs of pairwise interactions between roles in the act of discrimination, let us first fix explicit finite alphabets of roles (to avoid any undefined letter labels):

### Definition III.3.1 (Role Alphabets $\Lambda_5$, $\Lambda_4$, and $\Lambda_4'$)

1. **The five-element alphabet of roles of the discrimination scene** $\Lambda_5 = \{A, D, P_{\mathrm{wit}}, V, N\}$ ($|\Lambda_5| = 5$) consists of five formal labels:
   - $A$ (*agent / executor*, initiating a test action);
   - $D$ (*discriminating decision / buddhi*, pronouncing the verdict on the response);
   - $P_{\mathrm{wit}}$ (*witness / sākṣin*, the invariant reference point of the protocol);
   - $V$ (*question / vṛtti*, the active query form on the carrier);
   - $N$ (*carrier / prakṛti*, the discriminated domain support).
2. **Two four-element alphabets for a pair of octahedra** $\Lambda_4 = \{S, M, E, B\}$ and $\Lambda_4' = \{C, M, E, B\}$ ($|\Lambda_4| = |\Lambda_4'| = 4$, $|\Lambda_4 \cup \Lambda_4'| = 5$) consist of the three shared internal roles of the tripartite instrument (*antaḥkaraṇa*, cf. `SK 30, 33, 35`):
   - $M$ (*manas*—coordinator of inputs and apprehension),
   - $E$ (*ahaṃkāra*—loop of self-reference and appropriation),
   - $B$ (*buddhi*—loop of decisive discrimination),
   and two external poles:
   - $S$ (*sākṣin / puruṣa*—the witness pole in $\Lambda_4$),
   - $C$ (*citta-viṣaya / external scene of the carrier*—the object pole in $\Lambda_4'$).

On the $10$-element set of unordered pairs $V_{10} = \binom{\Lambda_5}{2}$ ($|V_{10}| = \binom{5}{2} = 10$), there exist two mutually complementary canonical graphs that must never be conflated:
- **The Kneser graph $\mathrm{KG}(5,2)$ (the Petersen graph):** two pairs $e, f \in \binom{\Lambda_5}{2}$ are connected by an edge if and only if they are **disjoint** ($e \cap f = \varnothing$). This is a $3$-regular graph on $10$ vertices with $15$ edges, adjacency spectrum $\{3^{(1)}, 1^{(5)}, (-2)^{(4)}\}$, chromatic number $\chi(\mathrm{KG}(5,2)) = 3$, and girth $5$ (triangle-free).
- **The Johnson graph $J(5,2) = L(K_5)$ (the line graph of the complete graph $K_5$, the complement of the Petersen graph):** two pairs $e, f \in \binom{\Lambda_5}{2}$ are connected by an edge if and only if they **intersect in exactly one element** ($|e \cap f| = 1$). This is a $6$-regular graph on $10$ vertices with $30$ edges and adjacency spectrum $\{6^{(1)}, 1^{(4)}, (-2)^{(5)}\}$.

For any $4$-element subset (such as $\Lambda_4$ or $\Lambda_4'$), the analogous Johnson graph on $\binom{4}{2} = 6$ pairs with an edge when $|e \cap f| = 1$ is precisely the **octahedron graph** $J(4,2) = L(K_4) \cong O_6$ (`Chapter I.6, §I.6.2`), in which disjoint pairs $\{xy, zw\}$ form the three diagonals of opposition.

### Theorem III.3.1 (The Graphs $\mathrm{KG}(5,2)$, $J(5,2) = L(K_5)$, the Isometric Möbius–Petersen Intertwining, and the Gluing of Two Octahedra Along the Triangle of the Internal Instrument)

*Classical foundation.* Kneser graph $\mathrm{KG}(5,2)$ (L. Lovász, 1978), Johnson graph $J(5,2) = L(K_5)$, and minimal triangulation of the Möbius strip $M_5$. *Contribution of this book:* Proving the polynomial identity $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$, the $D_{10}$-equivariant isometry $\mathcal{F} : C_2(M_5) \to \ker(A_{\mathrm{KG}}-I_{10})$, and the gluing of two octahedra along $\triangle(ME,MB,EB)$.

1. **Kneser–Johnson duality on the $10$ pairs $\binom{\Lambda_5}{2}$:** *The adjacency matrices $A_{\mathrm{KG}}$ of the Petersen graph $\mathrm{KG}(5,2)$ and $A_{J}$ of the Johnson graph $J(5,2) = L(K_5)$ satisfy $A_{\mathrm{KG}} + A_J = J_{10} - I_{10}$, commute, and decompose $\mathbb{R}^{10} = \mathbb{R}\mathbf{1}_{10} \oplus V_5 \oplus V_4$ into a direct sum of three common eigenspaces of dimensions $1$, $5$, and $4$:*
   $$
   \ker(A_{\mathrm{KG}} - I_{10}) = \ker(A_J + 2I_{10}) = V_5 \quad (\dim V_5 = 5), \qquad \ker(A_{\mathrm{KG}} + 2I_{10}) = \ker(A_J - I_{10}) = V_4 \quad (\dim V_4 = 4).
   $$
2. **Exact isometric intertwining of the $5$-face Möbius strip $M_5$ with the eigenspace $V_5 = \ker(A_{\mathrm{KG}} - I_{10})$:** *Let the minimal triangulation of the Möbius strip consisting of $5$ triangular faces be given on the $5$ vertices $\{0,1,2,3,4\}$:*
   $$
   M_5 = \bigl\{\{0,1,2\},\; \{0,1,3\},\; \{0,2,4\},\; \{1,3,4\},\; \{2,3,4\}\bigr\}
   $$
   *($5$ boundary edges forming the cycle $0-2-3-1-4-0$ and $5$ interior edges forming the cycle $0-1-2-4-3-0$). Let $B \in \{-1,0,1\}^{10 \times 5}$ be the oriented boundary matrix $\partial_2$ of the complex $M_5$, $K = B^{\mathsf{T}} B \in \mathbb{Z}^{5 \times 5}$ the Hodge Laplacian on $2$-chains $C_2(M_5) \cong \mathbb{R}^5$ with spectrum $\bigl\{5,\; \frac{5+\sqrt{5}}{2}^{\times 2},\; \frac{5-\sqrt{5}}{2}^{\times 2}\bigr\}$ and eigenvector $v_0 = D_o \mathbf{1}_5$ ($K v_0 = 5 v_0$, where $D_o = \mathrm{diag}(1,1,-1,1,1)$), $j_{\mathrm{comp}} : C_2(M_5) \to \mathbb{R}^{10}$ the embedding of each face $f \in M_5$ into its complementary pair $\Omega \setminus f \in \binom{\Omega}{2}$, and $\Pi_G = \frac{1}{6}(A_{\mathrm{KG}} + 2I_{10})(3I_{10} - A_{\mathrm{KG}})$ the orthogonal projector of $\mathbb{R}^{10}$ onto $V_5 = \ker(A_{\mathrm{KG}} - I_{10})$. Then for the operator $F_0 = \Pi_G j_{\mathrm{comp}} D_o : C_2(M_5) \to V_5$, the Gram matrix $H_o = F_0^{\mathsf{T}} F_0$ is an exact degree-two polynomial in $K$ over $\mathbb{Q}$:*
   $$
   H_o = F_0^{\mathsf{T}} F_0 = \frac{1}{6}\bigl(K^2 - 7K + 13 I_5\bigr),
   $$
   *is positive definite (with eigenvalues $\frac{1}{2}$ and $\frac{3 \pm \sqrt{5}}{6} \approx 0.8727^{\times 2},\; 0.1273^{\times 2}$ under all $2^6 = 64$ choices of face orientations and signs), and the normalized Whitney–Hodge operator*
   $$
   \mathcal{F} = F_0 H_o^{-1/2} : C_2(M_5) \longrightarrow \ker(A_{\mathrm{KG}} - I_{10})
   $$
   *is an orthogonal isometry ($\mathcal{F}^{\mathsf{T}} \mathcal{F} = I_5$, $\mathcal{F} \mathcal{F}^{\mathsf{T}} = \Pi_G$) intertwining the action of the dihedral group $D_{10} = \mathrm{Aut}(M_5)$ up to the orientation sign character $\chi : D_{10} \to \{\pm 1\}$ ($\chi = +1$ on cyclic shifts $\mathbb{Z}_5$ and $\chi = -1$ on reflections of the Möbius strip):*
   $$
   \rho_{\mathrm{KG}}(g)\,\mathcal{F} = \chi(g)\,\mathcal{F}\,\rho_{M_5}(g) \qquad \forall\,g \in D_{10}.
   $$
3. **Gluing of two octahedra $O_6(\Lambda_4)$ and $O_6(\Lambda_4')$ along the triangle of the internal instrument inside $J(5,2)$:** *In the Johnson graph $J(\Lambda_4 \cup \Lambda_4', 2) = J(5,2)$ on the $10$ pairs from $\{S, C, M, E, B\}$, the induced subgraphs on the $6$ pairs $\binom{\Lambda_4}{2}$ and on the $6$ pairs $\binom{\Lambda_4'}{2}$ are two octahedra $O_6(\Lambda_4) \cong K_{2,2,2}$ and $O_6(\Lambda_4') \cong K_{2,2,2}$. Their intersection consists of precisely the three pairs of internal organs*
   $$
   \binom{\Lambda_4}{2} \cap \binom{\Lambda_4'}{2} = \binom{\{M, E, B\}}{2} = \{ME,\; MB,\; EB\},
   $$
   *which form in both octahedra a shared filled triangular face $\triangle(ME, MB, EB) \cong K_3$, whereas the tenth pair $SC$ ("direct short-circuiting of witness and external object bypassing the instrument $\{M,E,B\}$") belongs neither to $O_6(\Lambda_4)$ nor to $O_6(\Lambda_4')$.*

**Proof (analytical).**
1. In the complete graph $K_{10}$ on the pairs $\binom{\Lambda_5}{2}$, each pair $e$ is disjoint from $\binom{3}{2} = 3$ pairs and intersects in one element with $2 \times 3 = 6$ pairs, whence $A_{\mathrm{KG}} + A_J = J_{10} - I_{10}$. The minimal polynomial of $A_{\mathrm{KG}}$ is $(x - 3)(x - 1)(x + 2)$, where the simple eigenvalue $3$ belongs to $\mathbf{1}_{10}$. Solving the linear system for the multiplicities $m_1, m_{-2}$ of the eigenvalues $1$ and $-2$—total dimension $1 + m_1 + m_{-2} = 10$ and zero trace $\mathrm{tr}(A_{\mathrm{KG}}) = 1\cdot 3 + m_1\cdot 1 + m_{-2}\cdot(-2) = 0$—uniquely gives $m_1 = 5$ and $m_{-2} = 4$, that is, $\dim \ker(A_{\mathrm{KG}} - I_{10}) = 5$ and $\dim \ker(A_{\mathrm{KG}} + 2I_{10}) = 4$.
2. Each face $f \in M_5$ is incident to $3$ edges from $E(K_5) \cong V(\mathrm{KG}(5,2))$, which pairwise intersect at a vertex in $K_5$ and are therefore pairwise non-adjacent in $\mathrm{KG}(5,2)$. Direct substitution of the adjacency matrices $A_{\mathrm{KG}}$ and $B^{\mathsf{T}} A_{\mathrm{KG}} B$, expressed through face intersections in $M_5$, into $\Pi_G = -\frac{1}{6}(A_{\mathrm{KG}}^2 - A_{\mathrm{KG}} - 6I_{10})$ yields the identity $B^{\mathsf{T}} \Pi_G B = \frac{1}{6}(K^2 - 7K + 13I_5)$. Since for $\lambda \in \{5,\, \frac{5\pm\sqrt{5}}{2}\}$ the values $\frac{1}{6}(\lambda^2 - 7\lambda + 13)$ equal $\frac{1}{2} > 0$ and $\frac{3\mp\sqrt{5}}{6} > 0$, the matrix $H_o$ is invertible and positive definite, whence $\mathcal{F}^{\mathsf{T}} \mathcal{F} = H_o^{-1/2} F_0^{\mathsf{T}} F_0 H_o^{-1/2} = I_5$. Because $D_{10}$ preserves $M_5$ while reversing the orientation of $2$-chains under reflections ($\chi(g) = -1$) and commutes with $A_{\mathrm{KG}}$ and $\Pi_G$, we obtain the intertwining $\rho_{\mathrm{KG}}(g)\mathcal{F} = \chi(g)\mathcal{F}\rho_{M_5}(g)$.
3. Since $\Lambda_4 \cap \Lambda_4' = \{M, E, B\}$, the intersection of the sets of $2$-element subsets equals $\binom{\Lambda_4 \cap \Lambda_4'}{2} = \{ME, MB, EB\}$. Any two of these three pairs share exactly one common element ($M, E$, or $B$), so they are pairwise adjacent in $J(5,2)$ and form a triangle $K_3$ common to $O_6(\Lambda_4)$ and $O_6(\Lambda_4')$. The tenth pair $SC$ contains both external poles $S \notin \Lambda_4'$ and $C \notin \Lambda_4$, and therefore does not lie in the union $V(O_6(\Lambda_4)) \cup V(O_6(\Lambda_4'))$ ($6 + 6 - 3 = 9$ vertices). $\blacksquare$

Let us now show what happens to the Kneser graph $\mathrm{KG}(5,2)$ if the observer performs a categorical gluing of the roles $D$ and $N$ into a single indistinguishable label $C$:

### Lemma III.3.2 (Failure of the Natural Role Folding $q(D) = q(N) = C$ Versus Non-Role $3$-Coloring of $\mathrm{KG}(5,2)$)

*Classical foundation.* Proper colorings of the Petersen graph ($\chi = 3$) and induced maps on pair graphs. *Contribution of this book:* Proving that the role folding $q(D)=q(N)=C$ destroys edges of $\mathrm{KG}(5,2)$ and that no proper $3$-coloring of $\mathrm{KG}(5,2)$ is induced by any folding of the base alphabet $\Lambda_5$.

*Let $q : \Lambda_5 \to \Lambda_4' = \{A, P_{\mathrm{wit}}, V, C\}$ be the surjective role folding that identifies the discriminating decision $D$ and the carrier $N$ into a single symbol $C = q(D) = q(N)$ while leaving $A, P_{\mathrm{wit}}, V$ fixed. Then:*

1. **Collapse of the pair $DN$ into a loop and destruction of the homomorphism into $O_6(\Lambda_4')$:** *The pair $\{D, N\} \in \binom{\Lambda_5}{2}$ is mapped under $q$ to the degenerate singleton $\{C, C\} = \{C\} \notin \binom{\Lambda_4'}{2}$, while on the remaining $9$ pairs the map $q_*(\{x,y\}) = \{q(x), q(y)\}$ glues together the three pairs $\{\{A,D\},\{A,N\}\}$, $\{\{P_{\mathrm{wit}},D\},\{P_{\mathrm{wit}},N\}\}$, $\{\{V,D\},\{V,N\}\}$ and sends the disjointness edge $\{\{A,P_{\mathrm{wit}}\}, \{V,N\}\} \in E(\mathrm{KG}(5,2))$ to the opposition diagonal $\{\{A,P_{\mathrm{wit}}\}, \{V,C\}\} \notin E(O_6(\Lambda_4'))$.*
2. **Contrast with an abstract $3$-coloring of $\mathrm{KG}(5,2)$:** *Although the Petersen graph $\mathrm{KG}(5,2)$ has chromatic number $\chi(\mathrm{KG}(5,2)) = 3$ (there exists a proper coloring of its $10$ vertices into $3$ colors with color classes of sizes $4, 3, 3$), no proper $3$-coloring of $\mathrm{KG}(5,2)$ is induced by any surjective folding of the base role alphabet $\Lambda_5$.*

**Proof (analytical).** Item (1) is verified by direct substitution of $q(D) = q(N) = C$: the pair $\{D,N\}$ loses its two-element character, while the disjoint pairs $\{A,P_{\mathrm{wit}}\}$ and $\{V,C\}$ in $\Lambda_4'$ have $|e \cap f| = 0 \ne 1$ and are therefore not connected by an edge in $O_6(\Lambda_4') = J(4,2)$. For item (2): any nontrivial folding of $\Lambda_5$ identifies at least two base roles $x \ne y \in \Lambda_5$; then the three remaining roles $z, u, w$ form a triangle $\{z,u\}, \{u,w\}, \{z,w\}$ on the remaining pairs or generate an edge in $\mathrm{KG}(5,2)$ between $\{x,y\}$ and $\{z,u\}$, which fails to partition the $10$ pairs into $3$ independent sets of $\mathrm{KG}(5,2)$ via a map of the base letters. $\blacksquare$

---

## §III.3.3. Cycle Parity: Absence of a Square Root of the $6$-Element Complement Involution in $\mathfrak{S}_6$ Versus $12$ Roots of the $8$-Element Involution in $\mathfrak{S}_8$

In `Chapter I.5` and `Chapter II.4` we saw that permutation sign and cycle-length parity govern the lifting of actions to double covers. In the combinatorics of the classical enumerations of *Sāṃkhya* (`SK 3, 22, 24–27, 40`), one encounters both $6$-element cycles of equatorial states of the octahedron $O_6$ and the $8$-element core of the subtle carrier (*purīṣṭaka / aṣṭaka*: $5$ subtle elements *tanmātra* $+$ $3$ internal organs *manas, ahaṃkāra, buddhi*) as well as the $13$-element instrument (*trayodaśa-karaṇa* in `SK 32`: $10$ external indriyas $+$ $3$ internal organs, which coincides with the set-theoretic union of the $11$ indriyas $\{5\ \text{cognitive} + 5\ \text{conative} + \text{manas}\}$ and the $3$ organs $\{\text{manas, ahaṃkāra, buddhi}\}$ by virtue of the unique intersection $\mathrm{Indriya}_{11} \cap \mathrm{Antaḥkaraṇa}_3 = \{\mathrm{manas}\}$, $11 + 3 - 1 = 13$).

Let us compare the antipodal pole-exchange involution on the $6$ vertices of the octahedron $c_6 = (1\;2)(3\;4)(5\;6) \in \mathfrak{S}_6$ ($3$ disjoint transpositions of antipodes) and on the $8$ vertices of the cube $c_8 = (1\;2)(3\;4)(5\;6)(7\;8) \in \mathfrak{S}_8$ ($4$ disjoint transpositions of antipodes) with respect to the algebraic question: **does there exist a half-turn permutation $r$ whose square $r^2$ coincides with the complement involution ($r^2 = c_{2k}$)?**

### Theorem III.3.2 (Impossibility of a Square Root of the Complement Involution $c_6$ in $\mathfrak{S}_6$ and $12$ Square Roots of $c_8$ in $\mathfrak{S}_8$)

*Classical foundation.* Classical criterion for square roots of permutations via even-length cycle counts. *Contribution of this book:* Contrasting the impossibility of $r^2 = c_6$ in $\mathfrak{S}_6$ ($0$ solutions) against the $12$ solutions of $r^2 = c_8$ in $\mathfrak{S}_8$, each pairing antipodes with zero invariant pairs.

*Let $c_6 = (1\;2)(3\;4)(5\;6) \in \mathfrak{S}_6$ be the fixed-point-free involution consisting of three disjoint transpositions on $6$ elements, and let $c_8 = (1\;2)(3\;4)(5\;6)(7\;8) \in \mathfrak{S}_8$ be the fixed-point-free involution consisting of four disjoint transpositions on $8$ elements. Then:*

1. **Absence of square roots for $n = 6$ ($0$ out of $720$):** *The equation $r^2 = c_6$ has no solution $r \in \mathfrak{S}_6$ (the number of roots is $0$).*
2. **Exactly $12$ square roots for $n = 8$ ($12$ out of $40{,}320$):** *The equation $r^2 = c_8$ has in $\mathfrak{S}_8$ exactly $12$ solutions, each of which is a product of two disjoint cycles of length $4$ ($r = \sigma_1 \sigma_2$ with $\mathrm{supp}(\sigma_1) \cap \mathrm{supp}(\sigma_2) = \varnothing$), and none of these $12$ solutions leaves invariant any of the four pairs $\{2i-1, 2i\}$ of the involution $c_8$.*

**Proof (analytical).**
Decompose a candidate permutation $r \in \mathfrak{S}_{2k}$ into a product of disjoint cycles and trace all possible cycle lengths in $r$ under squaring:
- every cycle of odd length $2m+1 \ge 1$ in $r$ squares to a single cycle of the same odd length $2m+1$, which cannot appear in the decomposition of $c_{2k}$ because all cycles in $c_{2k}$ have length $2$;
- every transposition (a cycle of even length $2m$ with $m = 1$) in $r$ squares to two fixed points $(a\;b)^2 = (a)(b) = \mathrm{id}$, which is impossible since $c_{2k}$ has no fixed points;
- every cycle of even length $2m$ with $m \ne 2$ ($m \ge 3$) splits in $r^2$ into two disjoint cycles of length $m \ge 3$, which are likewise absent from $c_{2k}$;
- finally, a cycle of length $4$ ($2m$ with $m = 2$) splits upon squaring into **two** disjoint transpositions: $(a_1\;b_1\;a_2\;b_2)^2 = (a_1\;a_2)(b_1\;b_2)$.
Consequently, a solution $r \in \mathfrak{S}_{2k}$ of the equation $r^2 = c_{2k}$ must consist exclusively of disjoint $4$-cycles, and the number of transpositions $k$ in $c_{2k}$ must be even ($2 \mid k$):
1. For $n = 6$, the involution $c_6$ consists of $k = 3$ (an odd number of) transpositions (and has sign $\mathrm{sgn}(c_6) = (-1)^3 = -1$, whereas $\mathrm{sgn}(r^2) = (\mathrm{sgn}\,r)^2 = +1$). Therefore, in $\mathfrak{S}_6$ there are no solutions to $r^2 = c_6$ ($0$ out of $6! = 720$).
2. For $n = 8$, the involution $c_8$ consists of $k = 4$ transpositions $p_1=(1\;2),\; p_2=(3\;4),\; p_3=(5\;6),\; p_4=(7\;8)$. To form two $4$-cycles in $r$, the four transpositions $p_1, p_2, p_3, p_4$ must be partitioned into two pairs ($\frac{1}{2}\binom{4}{2} = 3$ ways), and within each pair of transpositions $(a_1\;a_2)$ and $(b_1\;b_2)$ there exist exactly $2$ four-cycles $(a_1\;b_1\;a_2\;b_2)$ and $(a_1\;b_2\;a_2\;b_1)$ whose square equals $(a_1\;a_2)(b_1\;b_2)$, with each such $4$-cycle mapping the elements $\{a_1, a_2\}$ into $\{b_1, b_2\}$ and back, preserving none of the original pairs. In total, the number of roots in $\mathfrak{S}_8$ is $3 \times 2 \times 2 = 12$. $\blacksquare$

---

## §III.3.4. Pāṇini's Six Case Roles (*kāraka*), the Decomposition $C_6 \sqcup 2C_3$, and Generation of the $9$-Dimensional Dipole Algebra $\mathrm{End}(V_-)$

In Pāṇini's grammar (*Aṣṭādhyāyī*, Book `1`, Chapter `4`, sūtras `1.4.23–1.4.55`, the section *kārakādhikāra* opened by the heading sūtra `1.4.23` *kārake*), every verbal action (*kriyā*) is organized around **six operational case roles** (*kāraka*), whereas the genitive case of possession (*ṣaṣṭhī*, `2.3.50` *ṣaṣṭhī śeṣe*) is deliberately excluded from the *kārakas* because it links noun to noun rather than directly to the verbal action.

### Table III.3.1. Pāṇini's Six *kārakas* (`Aṣṭādhyāyī 1.4.24–54`) and the Three Axes of the Octahedron $O_6$

| No. | Role (*kāraka*) and Pāṇini's Sūtra | Definition in the *Aṣṭādhyāyī* | Paired Role on the Same Axis of $O_6$ | Axis in the Tripartite Partition $O_6 = K_{2,2,2}$ |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Kartṛ** (agent, `1.4.54` *svatantraḥ kartā*) | Independent initiator of the action (under the causative becomes *hetu*, `1.4.55` *tatprayojako hetuś ca*) | **Karman** (direct object / target, `1.4.49` *kartur īpsitatamaṃ karma*) | **Axis I (Initiator $\leftrightarrow$ Target):** $\pi_1 = \{\mathrm{Kartṛ},\, \mathrm{Karman}\}$ |
| **2** | **Karaṇa** (instrument, `1.4.42` *sādhakatamaṃ karaṇam*) | Most effective means of accomplishing the act | **Adhikaraṇa** (locus / substrate, `1.4.45` *ādhāro 'dhikaraṇam*) | **Axis II (Means $\leftrightarrow$ Substrate):** $\pi_2 = \{\mathrm{Karaṇa},\, \mathrm{Adhikaraṇa}\}$ |
| **3** | **Apādāna** (fixed point of departure, `1.4.24` *dhruvam apāye 'pādānam*) | Stationary point from which separation occurs | **Sampradāna** (recipient of transmission, `1.4.32` *karmaṇā yam abhipraiti sa sampradānam*) | **Axis III (Departure $\leftrightarrow$ Reception):** $\pi_3 = \{\mathrm{Apādāna},\, \mathrm{Sampradāna}\}$ |

When these six roles are arranged in cyclic order around the equator $C_6$ of the octahedron $O_6$ so that the opposite poles of each of the three axes $\pi_1, \pi_2, \pi_3$ lie at distance $3$ along the $6$-cycle, the classical circulant graph $C_6(1,2)$ arises:

### Proposition III.3.2 (Isomorphism of the Circulant $C_6(1,2) \cong O_6$ and the Edge Decomposition $E(O_6) = E(C_6) \sqcup E(2C_3)$)

*Classical foundation.* Circulant graph $C_6(1,2)$ on $\mathbb{Z}_6$ and step-length partition of octahedral edges. *Contribution of this book:* Decomposing $E(O_6) = E(C_6) \sqcup E(C_3^{\mathrm{even}}) \sqcup E(C_3^{\mathrm{odd}})$ ($12 = 6 + 3 + 3$) across the three axes of case-role pairs in Pāṇini's scheme.

*On the set $V_6 = \mathbb{Z}_6 = \{0,1,2,3,4,5\}$, let the circulant graph $C_6(1,2)$ be given, in which vertex $k$ is connected to $k \pm 1 \pmod 6$ (step $1$) and to $k \pm 2 \pmod 6$ (step $2$). Then:*

1. **Isomorphism with the octahedron $O_6$:** *The only edges absent from $C_6(1,2)$ are the three diametral pairs of step $3$: $\{0,3\}, \{1,4\}, \{2,5\}$. Therefore $C_6(1,2) \cong K_{2,2,2} = O_6$.*
2. **Decomposition of the $12$ edges into an equatorial $6$-cycle and two triangles:** *The set of $12$ edges of the octahedron $O_6$ canonically decomposes into a disjoint union:*
   $$
   E(O_6) = E(C_6) \sqcup E(C_3^{\mathrm{even}}) \sqcup E(C_3^{\mathrm{odd}}), \qquad 12 = 6 + 3 + 3,
   $$
   *where $C_6 = (0-1-2-3-4-5-0)$ is the Hamiltonian equatorial cycle of step $1$ (linking adjacent roles of different axes), while $C_3^{\mathrm{even}} = \{0,2,4\}$ and $C_3^{\mathrm{odd}} = \{1,3,5\}$ are two disjoint triangles of step $2$ (corresponding to the two $\mathbb{Z}_3$-orbits from `Lemma III.3.1(2)`). Passing from the continuous $3$-torus of phases $T^3 = (S^1)^3$ of the three axes to the $6$ discrete poles $(\pm e_1, \pm e_2, \pm e_3)$ embeds the vertices of $O_6$ as the intersections of the coordinate axes with the unit sphere in $\mathbb{R}^3$.*

**Proof (analytical).** In $\mathbb{Z}_6$, the nonzero residues partition into $\{\pm 1\}$ ($6$ edges of the cycle $C_6$), $\{\pm 2\}$ ($6$ edges of the two triangles $\{0,2,4\}$ and $\{1,3,5\}$), and $\{3\}$ ($3$ diagonals $\{0,3\},\{1,4\},\{2,5\}$), which gives $C_6(1,2) = K_6 \setminus \{\{0,3\},\{1,4\},\{2,5\}\} \cong O_6$ and $12 = 6 + 3 + 3$. $\blacksquare$

Let us now verify the algebraic completeness of the equatorial $6$-cycles in the odd (dipole) sector $V_- \cong \mathbb{R}^3$ of the representation of the octahedral group $W(B_3) = \mathfrak{S}_3 \ltimes (\mathbb{Z}_2)^3$ (`Chapter II.4`):

### Lemma III.3.3 (Generation of the Full $9$-Dimensional Matrix Algebra $\mathrm{End}(V_-) \cong M_3(\mathbb{R})$ by a Pair of Equatorial $6$-Cycles and Structure of the Index-$2$ Subgroups in $W(B_3)$)

*Classical foundation.* Representations of the hyperoctahedral group $W(B_3)$ and Burnside's theorem for absolutely irreducible representations (with trivial commutant $\mathbb{R}\cdot I_3$). *Contribution of this book:* Separating the three index-$2$ subgroups of $W(B_3)$ and contrasting the algebra span of a single equatorial $6$-cycle ($3/9$) against a non-collinear pair ($9/9$) in $\mathrm{End}(V_-)$.

*Let $V_- \cong \mathbb{R}^3$ be the faithful three-dimensional signed representation of the hyperoctahedral group $W(B_3)$ ($|W(B_3)| = 48$) on the differences of opposite vertices of the octahedron $e_i = v_i^+ - v_i^-$ ($i=1,2,3$). Then:*

1. **Three distinct subgroups of index $2$ in $W(B_3)$:** *The group $W(B_3) \cong \mathfrak{S}_4 \times C_2$ contains three canonical subgroups of index $2$ (of order $24$), which must be strictly distinguished:*
   - *the group of proper rotations of the cube and octahedron $W(B_3)^+ = \mathrm{SO}(3) \cap W(B_3) \cong \mathfrak{S}_4$ ($\det|_{V_-} = +1$);*
   - *the pyritohedral subgroup $T_h = A_4 \times C_2$ (even permutations of the three axes $\mathfrak{A}_3 \cong \mathbb{Z}_3$ together with all $2^3 = 8$ sign changes, preserving the cyclic order of the axes);*
   - *the tetrahedral Coxeter subgroup $W(D_3) \cong \mathfrak{S}_4$ (all permutations of the axes with an even number of sign changes).*
2. **Dimension of the linear span of a single $6$-cycle versus a pair of $6$-cycles in $\mathrm{End}(V_-)$:** *Let $g_1 \in W(B_3)$ be an odd rotoinversion of order $6$ (for instance, $g_1(e_1) = e_2, g_1(e_2) = e_3, g_1(e_3) = -e_1$, generating an equatorial $6$-cycle on the vertices of $O_6$), and let $g_2 \in W(B_3)$ be a conjugate rotoinversion around an adjacent axis (for instance, $g_2(e_1) = e_3, g_2(e_3) = -e_2, g_2(e_2) = e_1$). Then:*
   - *the commutative subalgebra $\mathbb{R}[g_1] = \mathrm{span}\{I_3, g_1, g_1^2, \dots, g_1^5\} \subset \mathrm{End}(V_-)$ generated by a single equatorial $6$-cycle has dimension **exactly $3$ out of $9$** ($\dim \mathbb{R}[g_1] = 3$, since $g_1^3 = -I_3$);*
   - *the noncommutative subalgebra $\mathrm{Alg}(g_1, g_2) \subseteq \mathrm{End}(V_-)$ generated by the pair of non-collinear equatorial $6$-cycles $g_1, g_2$ coincides with the entire $9$-dimensional matrix algebra $\mathrm{End}(V_-) \cong M_3(\mathbb{R})$ (**$9$ out of $9$** standard matrix units).*

**Proof (analytical).**
1. On $V_- = \mathbb{R}^3$, the group $W(B_3)$ is generated by coordinate permutation matrices $P_\sigma$ ($\sigma \in \mathfrak{S}_3$) and diagonal sign changes $D_\varepsilon$ ($\varepsilon \in \{\pm 1\}^3$). The three nontrivial homomorphisms $W(B_3) \to \{\pm 1\}$—the determinant $\det(P_\sigma D_\varepsilon) = \mathrm{sgn}(\sigma)\prod \varepsilon_i$, the axis permutation sign $\mathrm{sgn}(\sigma)$, and the product of signs $\prod \varepsilon_i$—have as their kernels precisely $W(B_3)^+ \cong \mathfrak{S}_4$, $T_h = A_4 \times C_2$, and $W(D_3) \cong \mathfrak{S}_4$.
2. Since $g_1^3 = -I_3$, the minimal polynomial of the $3 \times 3$ matrix $g_1$ is $x^3 + 1 = (x+1)(x^2 - x + 1)$ of degree $3$, whence $\dim \mathbb{R}[g_1] = 3$. On the other hand, the subgroup $\langle g_1, g_2 \rangle \le W(B_3)$ contains $g_1^3 = -I_3$ and generates the entire group $W(B_3)$, for which the representation $V_-$ is absolutely irreducible over $\mathbb{R}$ (its commutant in $M_3(\mathbb{R})$ is trivial: any matrix commuting with all diagonal sign changes $D_\varepsilon$ is diagonal, and commuting with all permutations $P_\sigma$ makes it scalar). By Burnside's theorem for absolutely irreducible representations, $\mathrm{Alg}(g_1, g_2) = \mathbb{R}[W(B_3)] = \mathrm{End}(V_-) \cong M_3(\mathbb{R})$ has full dimension $9$. $\blacksquare$

> **Remark III.3.2 (On the duality between direct action on states and adjoint pullback of questions).** In `Chapter I.2` (`Theorem I.2.4`) it was shown that every direct map of states $f_\alpha : X \to X$ induces a contravariant pullback of questions $f_\alpha^* : \mathcal{Q} \to \mathcal{Q}$, $(f_\alpha^* q)(x) = q(f_\alpha(x))$, which in matrix representation is written via the transpose operator $F_\alpha^{\mathsf{T}}$: $\langle F_\alpha^{\mathsf{T}} \psi, \delta_x \rangle = \langle \psi, F_\alpha \delta_x \rangle$. This is the standard duality between direct pushforward of state indicators $F_\alpha$ (the Perron–Frobenius transfer operator) and contravariant pullback of question functions $F_\alpha^{\mathsf{T}}$ (the adjoint Koopman operator); in this book it is a purely linear-algebraic adjointness of the same type as $\mathrm{tr}(\rho\,\Phi^*(E)) = \mathrm{tr}(\Phi(\rho)\,E)$ on $\mathbb{C}^d$, allowing one to translate case transitions into adjoint questions without loss of completeness.

---

## §III.3.5. Verified Philological Map of Primary Sources and Summary Table of Epistemic Levels

For the reader's rigorous orientation, we compile all cited classical Indian primary sources into a single reference table specifying the exact text, sūtra/kārikā, and level in the epistemic hierarchy of `Chapter III.1` (`L1`: mathematical core; `L2`: textual fact of the primary source; `L4`: interpretive dictionary `REG-INTERP`).

### Table III.3.2. Verified Map of Sanskrit Primary Sources and Their Relation to the Core of DOT

| Tradition and Primary Source | Exact Citation (Sūtra / Kārikā) | Philological Content in the Primary Source (`L2`) | Matched Construction in DOT and Its Exact Status |
| :--- | :--- | :--- | :--- |
| **Sāṃkhya:** Īśvarakṛṣṇa, *Sāṃkhya-kārikā* (`SK`) | `SK 3, 22` ($25$ tattvas: $1 + 1 + 7 + 16$); `SK 19` (*sākṣitva*) | `SK 19`: *puruṣa* is defined as pure witness (*sākṣin*), distinct from three-guṇa *prakṛti*; `SK 20`: apparent agency arises from conjunction (*saṃyoga*). The image of crystal and flower (*kusumavac ca maṇiḥ*) belongs to the commentaries and *Sāṃkhya-sūtra* `2.35`. | Separation of the Observer's position $\mathcal{O} \notin X$ (`Introduction`, model typing) and failure of the role folding $q(D)=q(N)=C$ in `Lemma III.3.2` (`L1` $\leftrightarrow$ `L4`). |
| **Sāṃkhya:** *Sāṃkhya-kārikā* (`SK 11–13`) and commentaries of Gauḍapāda / Vācaspati Miśra | `SK 12` (*prīty-aprīti-viṣādātmakāḥ*); `SK 13` (*pradīpavac cārthato vṛttiḥ*) | The three guṇas (*sattva, rajas, tamas*) act cooperatively for the purpose of the witness like a lamp (*pradīpavat*). The explicit distribution "oil / wick / flame = three guṇas" belongs to the commentarial tradition rather than the literal text of `SK 13`. | Matching the three guṇas with the three cost components $(Z_C, Z_D, Z_F)$ is an **interpretive parallel of level `L4`** (`REG-INTERP`), not a theorem of the core. |
| **Sāṃkhya:** *Sāṃkhya-kārikā* (`SK 30, 32, 33, 35, 40, 50`) | `SK 30` (*catuṣṭaya*); `SK 32` ($13$ *karaṇas*); `SK 35` (*dvāra / dvārin*); `SK 50` ($5+28+9+8 = 50$) | The internal instrument (*antaḥkaraṇa*: *manas, ahaṃkāra, buddhi*) is the "gatekeeper" (*dvārin*), while the $10$ external indriyas are the "gates" (*dvārāṇi*). The sum of $50$ states of *pratyaya-sarga* in `SK 50`: $5\ \text{viparyaya} + 28\ \text{aśakti}\ (11+17) + 9\ \text{tuṣṭi} + 8\ \text{siddhi}$. | Shared triangle $\triangle(ME, MB, EB)$ in the gluing of two octahedra $O_6(\Lambda_4) \cup O_6(\Lambda_4') \subset J(5,2)$ (`Theorem III.3.1(3)`) and intersection $\mathrm{Indriya}_{11} \cap \mathrm{Antaḥkaraṇa}_3 = \{\mathrm{manas}\} \Rightarrow 13$ (`L1` $\leftrightarrow$ `L2/L4`). |
| **Yoga:** Patañjali, *Yoga-sūtra* (`YS`) | `YS 1.2–1.4` (*citta-vṛtti-nirodhaḥ*, *draṣṭuḥ svarūpe 'vasthānam*, *vṛtti-sārūpyam*); `YS 1.6`; `YS 1.41` | Under non-discrimination (*aviveka*) the seer conforms to the modifications of the instrument (*vṛtti-sārūpyam*, `YS 1.4`); when conflation ceases, the seer abides in its own form (`YS 1.3`); `YS 1.41`—image of a transparent crystal (*abhijātasyeva maṇer*). | Self-dual mirror code $C = \ker \Delta \subset \mathbb{F}_2^{2n}$ (`Proposition III.3.1`) and distinction between ideal reading and instrument distortion (`L1` $\leftrightarrow$ `L4`). |
| **Advaita Vedānta:** Gauḍapāda, *Māṇḍūkya-kārikā* (`MK`); Śaṅkara, *Brahma-sūtra-bhāṣya* (`BSB`) | `MU 3–7`; `MK 1.12–16` (*nidrā / svapna / turīya*); `BSB 1.1.1` (*adhyāsa-bhāṣya*); *Vivekacūḍāmaṇi* `93–94` (traditionally attributed to Śaṅkara) | In `BSB 1.1.1` Śaṅkara defines *adhyāsa* as transferring the properties of the subject ("I", *asmat*) onto the object ("this", *yuṣmat*) and vice versa. In `MK 1.12–16` *turīya* is free from both kinds of distortion: non-apprehension of the real (*agrahaṇa*) and misapprehension (*anyathā-grahaṇa*). | Two-arrow bridge scheme $(\iota, \mathcal{O}_\pi)$ (`Chapter III.1`): prohibition against identifying the model representation $\iota$ with the observer $\Gamma$ itself (`L1` $\leftrightarrow$ `L4`). |
| **Grammar and philosophy of language:** Pāṇini, *Aṣṭādhyāyī*; Bhartṛhari, *Vākyapadīya* | Pāṇini `1.4.23–55` (six *kārakas*); Bhartṛhari, *Vākyapadīya* `1.142`, `2.143–152` (*vaikharī, madhyamā, paśyantī* and *pratibhā*) | In Pāṇini, the $6$ *kārakas* define the role valency of a verb. In Bhartṛhari, the levels of speech (*vaikharī, madhyamā, paśyantī*) and the integral flash of sentence meaning (*pratibhā*) are related but conceptually distinct notions (they may be compared, but not literally equated). | Octahedron $O_6 \cong C_6(1,2)$ on three axes of case pairs (`Proposition III.3.2`) and generation of $\mathrm{End}(V_-)$ by a pair of $6$-cycles (`Lemma III.3.3`) (`L1` $\leftrightarrow$ `L2/L4`). |

*(Note: wherever Book II examines the Cayley–Dickson doubling tower $\mathbb{R} \to \mathbb{C} \to \mathbb{H} \to \mathbb{O}$ and the modular octonion algebra $\mathrm{Oct}(\mathbb{F}_2)$ with $72$ idempotents, the reader should refer to **`Chapter II.5`**, where those constructions are proved in full).*

---

## §III.3.6. Domain Bridge Passport for `Chapter III.3` (Role Graphs of Sāṃkhya, Advaita, and Pāṇini)

| No. | Passport Row | Content for Bridge `Chapter III.3` |
| :---: | :--- | :--- |
| **1** | **Subject and primary data** | Canonical enumerations of roles and relations in primary sources: the five-element and four-element role alphabets $\Lambda_5 = \{A, D, P_{\mathrm{wit}}, V, N\}$ and $\Lambda_4 \cup \Lambda_4' = \{S, C, M, E, B\}$ (`SK 3, 19–20, 30–35`), the six case roles *kāraka* (`Aṣṭādhyāyī 1.4.23–55`), and the conditions of non-superimposition (*adhyāsa*, `BSB 1.1.1`). |
| **2** | **Quantities, units, and procedure** | Invariants of finite graphs and groups: adjacency spectra of $\mathrm{KG}(5,2)$ and $J(5,2) = L(K_5)$, the Gram matrix $H_o = F_0^{\mathsf{T}} F_0$ on $2$-chains of the Möbius strip $M_5$, the number of square roots of the complement involutions $c_6 \in \mathfrak{S}_6$ and $c_8 \in \mathfrak{S}_8$, and the dimensions of subalgebras in $\mathrm{End}(V_-) \cong M_3(\mathbb{R})$. |
| **3** | **Split prior to fitting** | Definitions of adjacency predicates (disjointness $e \cap f = \varnothing$ for Kneser versus single-element intersection $|e \cap f| = 1$ for Johnson) and group representations of $W(B_3)$ are fixed prior to comparison with textual tables. |
| **4** | **Free choices and degrees of freedom** | At the level of the mathematical core (`Propositions III.3.1–III.3.2`, `Lemmas III.3.1–III.3.3`, `Theorems III.3.1–III.3.2`), there are **`0`** free fitting parameters. At the level of the dictionary `REG-INTERP`, the choice of nominal letter assignment for $\Lambda_5$ and $\Lambda_4$ is fixed in `Definition III.3.1`. |
| **5** | **Null and surrogate control** | 1) Non-role proper $3$-coloring of $\mathrm{KG}(5,2)$ versus the role folding $q : \Lambda_5 \to \Lambda_4'$ (`Lemma III.3.2`); 2) $6$-element complement involution $c_6 \in \mathfrak{S}_6$ ($0$ square roots) versus $12$ products of disjoint $4$-cycles for $c_8 \in \mathfrak{S}_8$ (`Theorem III.3.2`); 3) a single $6$-cycle ($\dim = 3/9$) versus a pair of non-collinear $6$-cycles ($\dim = 9/9$) in $\mathrm{End}(V_-)$ (`Lemma III.3.3`); 4) the rejected bridge $P_7 \not\cong \mathrm{PG}(2,2)$ (`Chapter III.1, §III.1.5`). |
| **6** | **Pre-declared comparison and full cost** | Exact match of the polynomial $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$, orthogonality $\mathcal{F}^{\mathsf{T}} \mathcal{F} = I_5$, intersection $\binom{\Lambda_4}{2} \cap \binom{\Lambda_4'}{2} = \triangle(ME, MB, EB)$, and dimensions $3/9$ versus $9/9$ under complete finite and analytical control. |
| **7** | **Falsification condition and reproducibility** | Any statement of the mathematical core of the chapter is falsified by a direct finite counterexample in $\mathbb{F}_2^6, \mathrm{KG}(5,2), J(5,2), \mathfrak{S}_6, \mathfrak{S}_8$, or $W(B_3)$ and is reproducible in `07_verify_full_book_III_v3_3.jl` (`GATE-III01-02, GATE-III03-01..04`); philological citations are verified against critical editions of `SK, YS, MK, BSB`, and the `Aṣṭādhyāyī`. |
| **8** | **Observer's position in the bridge ($\Gamma, \iota, \mathcal{O}_\pi$)** | In this bridge, the position of the Observer $\mathcal{O}$ (`sākṣin / puruṣa` in `SK 19` and `BSB 1.1.1`) is the direct subject of role analysis: the arrow $\iota$ embeds the $5$-element and $4$-element role schemes into the pair graphs $\mathrm{KG}(5,2)$ and $O_6(\Lambda_4) \cup O_6(\Lambda_4') \subset J(5,2)$, the arrow $\mathcal{O}_\pi$ reads out the preservation or destruction of edges under foldings and projections, and the role of the ungluable obstruction $\kappa \ne 0$ is played by the odd $5$-cycle of the Möbius strip $M_5$ and the failure of the role folding $q(D) = q(N) = C$ (`Lemma III.3.2`), which destroys the graph when the witness/decision is identified with the object. |

---

### What This Chapter Transmits to the Next (`Chapter III.3` $\to$ `Chapter III.4`)

In `Chapter III.3` we verified that the octahedron $O_6$, the hyperoctahedral group $W(B_3)$, its sign characters, and cycle parity form the combinatorial backbone for role and grammatical schemes. In the next chapter (`Chapter III.4`), we transfer these finite parity and cycle invariants to two algorithmic and probabilistic problems: rebuilding the triangular prism $\Pi_6$ into the octahedron $O_6$, Kirchhoff's cyclomatic rank $r_{\mathrm{cyc}} = |E| - |V| + c$ of the large-prime cofactor multigraph in the Kraitchik–Dixon congruence-of-squares method, and the exact $\mathfrak{S}_m$ gauge symmetry of hidden Markov models on unlabelled symbol sequences.
