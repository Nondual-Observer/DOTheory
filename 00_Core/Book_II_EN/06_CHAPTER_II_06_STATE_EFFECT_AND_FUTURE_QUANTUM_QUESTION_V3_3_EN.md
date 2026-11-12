# Chapter II.6. State, Effect, and the Future Quantum Question: The Walsh–Bloch Bridge and Branch Closure

The four-point scene of Book I has exactly $16$ yes/no questions. What happens to them if we allow answers not only of "yes" or "no," but also "with weight $0.3$"? Which of the $16$ questions survive such a relaxation, and which cease to be admissible? The answer turns out to be threshold-governed: at each value of the contrast $\lambda$, a specific subset of questions survives, and we will determine the critical values exactly. The preceding five chapters enriched the observer's finite core with linear memory, smooth jets, simplicial homology, non-abelian connection on the octahedron $O_6$, and nonassociative multiplication along Fano lines; now comes the quantum enrichment of the operational contract $\Gamma$ announced in `Table I.9.3` of Book I.

Let us fix from the very outset a clear methodological boundary: in the present chapter, a finite-dimensional complex Hilbert space $\mathcal{H} = \mathbb{C}^d$ ($d \ge 2$), the cone of positive semidefinite Hermitian operators, and the probabilistic Born trace rule $p = \mathrm{tr}(\rho E)$ **are explicitly adopted as premises of a new mathematical model**, rather than "derived from nothing" by the pure combinatorics of Book I. Our task is to establish how the observer's contract $\Gamma$ is structured inside this operator model and what exact structural bridges connect it to the four-point scene $S_4 = \mathbb{F}_2^2$ and the Nerode memory theorem (`Chapter I.3`).

The central question of the chapter consists of three parts:

> **How do the $16$ Boolean questions of the four-point scene $S_4 = \mathbb{F}_2^2$ map into Hermitian qubit operators $\mathrm{Herm}_2(\mathbb{C})$, and at what contrast thresholds $\lambda$ do they become admissible quantum effects $0 \preceq E \preceq I_2$? How is the quantum analogue of the Nerode theorem structured for branching quantum instruments $\mathcal{I}_{a,o}$? And why does the Gleason–Busch theorem depend essentially on whether the observer's contract is specified only on orthogonal projectors or on the entire convex cone of effects?**

---

## §II.6.1. The Quantum Observer Contract $\Gamma$: States, Effects, and Post-Action Divergence

Let us transfer the observer's operational contract from `Chapter I.1` and `Chapter I.3` into a finite-dimensional complex Hilbert space $\mathcal{H} = \mathbb{C}^d$ ($d \ge 2$). Consider the real vector space of all Hermitian operators
$$
\mathrm{Herm}_d(\mathbb{C}) = \{ A \in \mathrm{Mat}_d(\mathbb{C}) : A^\dagger = A \}, \qquad \dim_{\mathbb{R}} \mathrm{Herm}_d(\mathbb{C}) = d^2,
$$
equipped with the Hilbert–Schmidt inner product $\langle A, B \rangle = \mathrm{tr}(AB)$ and the Löwner partial order ($A \preceq B \iff B - A$ is positive semidefinite).

> **Definition II.6.1 (Quantum operational contract of the observer $\Gamma$ in dimension $d$).**  
> A *quantum operational contract of the observer* in the space $\mathcal{H} = \mathbb{C}^d$ is a quadruple
> $$
> \Gamma = \bigl(\mathcal{S}(\mathcal{H}),\; \mathcal{E}_0,\; \mathcal{A},\; \{\mathcal{I}_{a,o}\}_{a\in\mathcal{A},\, o\in\Omega_a}\bigr),
> $$
> in which:
> 1. The *state space* $\mathcal{S}(\mathcal{H}) = \{ \rho \in \mathrm{Herm}_d(\mathbb{C}) : \rho \succeq 0,\; \mathrm{tr}\,\rho = 1 \}$ consists of density matrices;
> 2. The *initial repertoire of terminal questions (effects)* $\mathcal{E}_0 \subseteq \mathcal{E}(\mathcal{H})$ is chosen inside the order interval of *quantum effects*
>    $$
>    \mathcal{E}(\mathcal{H}) = \{ E \in \mathrm{Herm}_d(\mathbb{C}) : 0 \preceq E \preceq I_d \},
>    $$
>    where for each state $\rho \in \mathcal{S}(\mathcal{H})$ and effect $E \in \mathcal{E}(\mathcal{H})$ the probability of the answer "yes" equals $\mathrm{tr}(\rho E) \in [0,1]$, while the negation of the question $\neg E$ corresponds to the complementary effect $I_d - E \in \mathcal{E}(\mathcal{H})$;
> 3. The *family of quantum instruments (actions with outcome reading)* $\{\mathcal{I}_{a,o}\}$ assigns to each action $a \in \mathcal{A}$ and each classical dial outcome $o \in \Omega_a$ a completely positive linear superoperator map $\mathcal{I}_{a,o} : \mathrm{Herm}_d(\mathbb{C}) \to \mathrm{Herm}_d(\mathbb{C})$ (given by Kraus operators $K_{a,o,j}$ via $\mathcal{I}_{a,o}(\rho) = \sum_j K_{a,o,j} \rho K_{a,o,j}^\dagger$) whose total channel $\Phi_a = \sum_{o \in \Omega_a} \mathcal{I}_{a,o}$ is trace-preserving ($\mathrm{tr}\,\Phi_a(\rho) = \mathrm{tr}\,\rho$).

Let us show immediately how the central situation of `Chapter I.3` and `Chapter II.1` is reproduced within this contract: **two states yielding the exact same answer to today's question diverge after an admissible action.**

Suppose in the two-level qubit space $\mathcal{H} = \mathbb{C}^2$ we are given two pure states $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ and $|-\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ with density matrices $\rho_\pm = |\pm\rangle\langle\pm| = \frac{1}{2}(I_2 \pm \sigma_x)$, while today's terminal question is the computational basis projector $P_0 = |0\rangle\langle 0| = \frac{1}{2}(I_2 + \sigma_z)$. Under a direct reading of the question $P_0$, both states yield the exact same probability $1/2$:
$$
\mathrm{tr}(\rho_+ P_0) = \frac{1}{2}, \qquad \mathrm{tr}(\rho_- P_0) = \frac{1}{2},
$$
because the state difference $\rho_+ - \rho_- = \sigma_x$ is trace-orthogonal to the question $P_0$: $\mathrm{tr}(\sigma_x P_0) = 0$. If, however, the contract $\Gamma$ contains the unitary Hadamard action $H = \frac{1}{\sqrt{2}}\bigl(\begin{smallmatrix} 1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr)$, which maps $|+\rangle \mapsto |0\rangle$ and $|-\rangle \mapsto |1\rangle$, then the transferred question (reading through effect evolution—the dual Heisenberg picture) $H^\dagger P_0 H = |+\rangle\langle +|$ immediately separates these states to opposite poles of certainty:
$$
\mathrm{tr}\bigl(H \rho_+ H^\dagger P_0\bigr) = \mathrm{tr}\bigl(\rho_+ (H^\dagger P_0 H)\bigr) = 1, \qquad
\mathrm{tr}\bigl(H \rho_- H^\dagger P_0\bigr) = 0.
$$

---

## §II.6.2. The Walsh–Bloch Bridge: How the $16$ Boolean Tables of the Scene $S_4$ Map into Qubit Effects ($16 \to 8 \to 2$)

Let us now connect the space of Hermitian qubit operators $\mathrm{Herm}_2(\mathbb{C})$ to the backbone construction of Book I—the four-point scene
$$
S_4 = \mathbb{F}_2^2 = \{00, 01, 10, 11\}.
$$
In `Chapter I.9` and `Chapter II.1` (§II.1.4), we saw that the space of all functions on the four-point scene $S_4$ is four-dimensional and possesses a canonical orthonormal basis of four Walsh characters:
- the trivial character $w_{00}(s) = 1$;
- the three non-trivial signed characters $\chi_1 = w_{10}$, $\chi_2 = w_{01}$, $\chi_3 = w_{11}$ (corresponding to the three coordinate questions $X, C, B$ on $S_4$), each taking the value $+1$ on two points of the scene $S_4$ and $-1$ on the other two points:

| Point $s \in S_4$ | $w_{00}(s)$ | $\chi_1(s) = (-1)^{s_1}$ | $\chi_2(s) = (-1)^{s_2}$ | $\chi_3(s) = (-1)^{s_1 \oplus s_2}$ |
| :---: | :---: | :---: | :---: | :---: |
| $00$ | $+1$ | $+1$ | $+1$ | $+1$ |
| $01$ | $+1$ | $+1$ | $-1$ | $-1$ |
| $10$ | $+1$ | $-1$ | $+1$ | $-1$ |
| $11$ | $+1$ | $-1$ | $-1$ | $+1$ |

On the other hand, the $4$-dimensional real space of Hermitian qubit operators $\mathrm{Herm}_2(\mathbb{C})$ has an orthogonal basis consisting of the identity matrix $I_2$ and the three traceless Pauli matrices
$$
\sigma_1 = \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$
satisfying $\mathrm{tr}(\sigma_j) = 0$ and $\frac{1}{2}\mathrm{tr}(\sigma_j \sigma_k) = \delta_{jk}$.

Assign to each Boolean question $q : S_4 \to \{0,1\}$ (there are exactly $2^4 = 16$ such tables on $S_4$) its Walsh expansion
$$
q(s) = c_0(q) + \sum_{j=1}^3 c_j(q)\,\chi_j(s), \qquad
c_0(q) = \frac{1}{4}\sum_{s \in S_4} q(s) = \frac{|q|}{4}, \quad
c_j(q) = \frac{1}{4}\sum_{s \in S_4} q(s)\,\chi_j(s),
$$
where $|q| \in \{0, 1, 2, 3, 4\}$ is the Hamming weight (the number of ones in the table of the question $q$), and define the one-parameter family of linear **Walsh–Bloch** maps $E_\lambda : \mathbb{R}^{S_4} \to \mathrm{Herm}_2(\mathbb{C})$ with contrast parameter $\lambda \in \mathbb{R}$:
$$
E_\lambda(q) = c_0(q)\, I_2 + \lambda \sum_{j=1}^3 c_j(q)\,\sigma_j = c_0(q)\, I_2 + \lambda\, \mathbf{c}(q)\cdot \boldsymbol{\sigma}.
$$

> **Theorem II.6.1 (Three-level filtration $16 \to 8 \to 2$ of the Boolean questions of the scene $S_4$ under the Walsh–Bloch map into a qubit).**  
> *Classical foundation.* The Pauli basis and the representation of Hermitian matrices via real coefficients are known in linear algebra; the Walsh transform is based on characters. *Contribution of this book:* Quantum threshold filtration of Boolean tables $16 \to 8 \to 2$ on scene $S_4$ across $|\lambda| = 1/\sqrt{3}$ and $|\lambda| = 1$.
> For the Walsh–Bloch map $E_\lambda : \{0,1\}^{S_4} \to \mathrm{Herm}_2(\mathbb{C})$, the following exact relations hold:
> 1. **(Preservation of logical complement).** For every $\lambda \in \mathbb{R}$ and every Boolean table $q : S_4 \to \{0,1\}$, the negation of a question $\neg q = 1 - q$ corresponds to the operator complement to the identity:
>    $$
>    E_\lambda(\neg q) = I_2 - E_\lambda(q),
>    $$
>    and the normalized trace $\frac{1}{2}\mathrm{tr}\,E_\lambda(q) = c_0(q) = |q|/4$ coincides with the classical fraction of "yes" answers on the scene $S_4$. For $\lambda \ne 0$, the map $E_\lambda : \mathbb{R}^{S_4} \to \mathrm{Herm}_2(\mathbb{C})$ is an isomorphism of $4$-dimensional real vector spaces, whereas at $\lambda = 0$ it degenerates into the one-dimensional trace $E_0(q) = \frac{|q|}{4} I_2$, gluing together all questions of the same Hamming weight.
> 2. **(Euclidean norms of the Walsh vectors $\mathbf{c}(q)$ by Hamming weight).** For each of the $16$ Boolean questions $q \in \{0,1\}^{S_4}$, the mean $c_0(q)$ and the Euclidean length of the three-dimensional vector of Walsh coefficients $\|\mathbf{c}(q)\|_2 = \sqrt{c_1(q)^2 + c_2(q)^2 + c_3(q)^2}$ depend solely on the Hamming weight $|q|$:
>    - for the $2$ constant questions ($|q| = 0$ and $|q| = 4$): $c_0 \in \{0, 1\}$, $\|\mathbf{c}(q)\|_2 = 0$;
>    - for the $6$ balanced two-point slices ($|q| = 2$, i.e., the six vertices of the octahedron $O_6$: $X_0, X_1, C_0, C_1, B_0, B_1$): $c_0 = \frac{1}{2}$, and the vector $\mathbf{c}(q)$ has exactly one non-zero component $\pm \frac{1}{2}$, whence $\|\mathbf{c}(q)\|_2 = \frac{1}{2}$;
>    - for the $4$ single-point indicators ($|q| = 1$) and the $4$ three-point questions ($|q| = 3$): $c_0 = \frac{1}{4}$ (respectively $\frac{3}{4}$), and all three coordinates satisfy $c_j(q) = \pm \frac{1}{4}$, whence $\|\mathbf{c}(q)\|_2 = \sqrt{3 \cdot (1/16)} = \frac{\sqrt{3}}{4}$.
> 3. **(Three thresholds of quantum admissibility $0 \preceq E_\lambda(q) \preceq I_2$: the steps $16 \to 8 \to 2$).** Since the eigenvalues of the Hermitian matrix $E_\lambda(q) = c_0 I_2 + \lambda \mathbf{c}\cdot\boldsymbol{\sigma}$ equal $c_0 \pm |\lambda|\,\|\mathbf{c}\|_2$, the quantum effect condition $0 \preceq E_\lambda(q) \preceq I_2$ ($\iff |\lambda|\,\|\mathbf{c}(q)\|_2 \le \min(c_0(q), 1 - c_0(q))$) carves out inside the $16$ Boolean questions of the scene $S_4$ exactly three regimes:
>    - **Regime I (Full embedding of all $16$ questions, $|\lambda| \le \frac{1}{\sqrt{3}}$):** all $16$ Boolean tables of the scene $S_4$ map into admissible quantum effects $E_\lambda(q) \in \mathcal{E}(\mathbb{C}^2)$. At the critical boundary $\lambda = \frac{1}{\sqrt{3}}$, the four single-point questions ($|q| = 1$) attain a zero lower eigenvalue $\frac{1}{4} - \frac{1}{\sqrt{3}}\frac{\sqrt{3}}{4} = 0$, becoming rank-$1$ operators.
>    - **Regime II (Survival of the $8$ even questions of the octahedron and constants, $\frac{1}{\sqrt{3}} < |\lambda| \le 1$):** all $8$ odd-weight questions ($|q| \in \{1, 3\}$) lose positive semidefiniteness (exiting the effect cone), whereas exactly **$8$ tables of even weight** ($2$ constants $|q| \in \{0,4\}$ and the **$6$ two-point slices of the octahedron $O_6$** with $|q| = 2$) remain admissible effects. At the second critical boundary $\lambda = 1$, the six slices of the octahedron $O_6$ become exact orthogonal Pauli projectors $\frac{1}{2}(I_2 \pm \sigma_j)$ with spectrum $\{0, 1\}$.
>    - **Regime III (Survival of only the $2$ constants, $|\lambda| > 1$):** the six slices of the octahedron $O_6$ also exit the interval $[0, I_2]$ (their spectrum $\frac{1}{2}(1 \pm |\lambda|)$ acquires a negative eigenvalue), and only the **$2$ trivial questions** $0$ and $I_2$ remain in the effect cone.

**Proof.**  
By Parseval's identity on the group $S_4 = \mathbb{F}_2^2$, the sum of squares of all four Walsh coefficients equals
$$
c_0(q)^2 + \|\mathbf{c}(q)\|_2^2 = \frac{1}{4}\sum_{s \in S_4} q(s)^2 = \frac{|q|}{4} = c_0(q),
$$
whence for every Boolean question $q : S_4 \to \{0,1\}$ we obtain the identity
$$
\|\mathbf{c}(q)\|_2 = \sqrt{c_0(q)\bigl(1 - c_0(q)\bigr)}.
$$
Substituting $c_0 \in \{0, \frac{1}{4}, \frac{1}{2}, \frac{3}{4}, 1\}$ immediately gives $\|\mathbf{c}\|_2 = 0$ for $|q| \in \{0,4\}$; $\|\mathbf{c}\|_2 = \sqrt{\frac{1}{2}\cdot\frac{1}{2}} = \frac{1}{2}$ for $|q| = 2$ (threshold $|\lambda|\cdot \frac{1}{2} \le \frac{1}{2} \iff |\lambda| \le 1$); and $\|\mathbf{c}\|_2 = \sqrt{\frac{1}{4}\cdot\frac{3}{4}} = \frac{\sqrt{3}}{4}$ for $|q| \in \{1,3\}$ (threshold $|\lambda|\cdot \frac{\sqrt{3}}{4} \le \frac{1}{4} \iff |\lambda| \le \frac{1}{\sqrt{3}}$). This completes the proof of all three steps $16 \to 8 \to 2$. $\blacksquare$

Observe the consequence of the proved identity $\|\mathbf{c}(q)\|_2 = \sqrt{c_0(1-c_0)}$: **the two classical quantum thresholds on the Bloch sphere—the tetrahedral threshold $\lambda = 1/\sqrt{3}$ and the projective Pauli threshold $\lambda = 1$—coincide numerically with the ratios $\min(c_0, 1-c_0) / \sqrt{c_0(1-c_0)}$ for the single-point questions of the scene $S_4$ ($c_0 = 1/4$) and the two-point slices of the octahedron $O_6$ ($c_0 = 1/2$).**

---

## §II.6.3. Branch Closure of Effects $W_\infty$ (Quantum Nerode Theorem) and Duality of Reading via State Evolution and via Effect Evolution

Let us now examine how the minimal memory subspace of future questions—the exact quantum analogue of the Moore–Nerode theorem (`Chapter I.3`) and the observable subspace of `Chapter II.1`—is constructed within the quantum contract $\Gamma = (\mathcal{S}(\mathcal{H}), \mathcal{E}_0, \mathcal{A}, \{\mathcal{I}_{a,o}\})$.

If the observer performs an instrument action $a \in \mathcal{A}$, records on the dial an outcome $o \in \Omega_a$ (which updates the state according to $\rho \mapsto \mathcal{I}_{a,o}(\rho)$), and then asks a terminal question $E \in \mathcal{E}(\mathcal{H})$, the joint probability of obtaining first the outcome $o$ and then the answer "yes" to the question $E$ equals
$$
\mathrm{tr}\bigl(\mathcal{I}_{a,o}(\rho)\, E\bigr) = \mathrm{tr}\bigl(\rho\, \mathcal{I}_{a,o}^\dagger(E)\bigr),
$$
where $\mathcal{I}_{a,o}^\dagger : \mathrm{Herm}_d(\mathbb{C}) \to \mathrm{Herm}_d(\mathbb{C})$ is the Hilbert–Schmidt adjoint operator defining reading via effect evolution (the dual Heisenberg picture; $\mathcal{I}_{a,o}^\dagger(E) = \sum_j K_{a,o,j}^\dagger E K_{a,o,j}$). We call the direct action $\rho \mapsto \Phi(\rho)$ reading via state evolution (the Schrödinger picture). Throughout this book, the two pictures mean solely the linear-algebraic adjointness $\mathrm{tr}(\rho\,\Phi^\dagger(E)) = \mathrm{tr}(\Phi(\rho)\,E)$ on $\mathbb{C}^d$; no physical interpretation enters the premises.

Construct inductively an ascending chain of real subspaces of transferred questions in $\mathrm{Herm}_d(\mathbb{C})$:
$$
W_0 = \operatorname{span}_{\mathbb{R}}(\mathcal{E}_0 \cup \{I_d\}), \qquad
W_{n+1} = W_n + \sum_{a \in \mathcal{A},\, o \in \Omega_a} \mathcal{I}_{a,o}^\dagger(W_n), \qquad
W_\infty = \bigcup_{n=0}^\infty W_n.
$$

> **Proposition II.6.1 (Stabilization of the branch closure $W_\infty$ in $\le d^2 - 1$ steps and quantum Nerode equivalence).**  
> *Classical foundation.* Stabilization of an ascending chain of subspaces in at most $\dim - 1$ steps is a classical linear-algebraic argument (Schützenberger, 1961; Carlyle–Paz, 1971; Tzeng, 1992). *Contribution of this book:* Quantum Nerode equivalence formulated as an observer indistinguishability relation on effects.
> 1. In the space $\mathrm{Herm}_d(\mathbb{C})$ of real dimension $d^2$, the chain of subspaces $W_0 \subseteq W_1 \subseteq W_2 \subseteq \cdots$ stabilizes no later than step $N = d^2 - 1$:
>    $$
>    W_{d^2 - 1} = W_{d^2} = W_\infty.
>    $$
> 2. Two quantum states $\rho_1, \rho_2 \in \mathcal{S}(\mathcal{H})$ yield identical probabilities across all possible branching protocols $(a_1, o_1), \dots, (a_k, o_k)$ followed by any terminal question $E \in \mathcal{E}_0$ if and only if their difference is orthogonal to the closure $W_\infty$:
>    $$
>    \rho_1 \sim_\Gamma \rho_2 \Longleftrightarrow \mathrm{tr}\bigl((\rho_1 - \rho_2) X\bigr) = 0 \quad (\forall X \in W_\infty) \Longleftrightarrow \rho_1 - \rho_2 \in W_\infty^\perp.
>    $$
>    The dimension of the minimal linear quantum memory of the contract $\Gamma$ equals $\dim_{\mathbb{R}} W_\infty \le d^2$.
> 3. **(Trace-preservation criterion and asymmetry of the adjoint $\dagger$).** A total completely positive channel $\Phi = \sum_{o \in \Omega_a} \mathcal{I}_{a,o}$ is trace-preserving ($\mathrm{tr}\,\Phi(\rho) = \mathrm{tr}\,\rho$ for all $\rho$, i.e., is a `CPTP` channel) if and only if the adjoint channel $\Phi^\dagger$ (reading via effect evolution) is **unital** ($\Phi^\dagger(I_d) = I_d$). Moreover, the class of `CPTP` channels is **not closed** under taking the adjoint $\Phi \mapsto \Phi^\dagger$: for the reset (memory erasure) channel to a fixed state $|0\rangle\langle 0|$,
>    $$
>    \Phi_{\mathrm{reset}}(\rho) = \mathrm{tr}(\rho)\,|0\rangle\langle 0| = |0\rangle\langle 0|\rho|0\rangle\langle 0| + |0\rangle\langle 1|\rho|1\rangle\langle 0| + \cdots,
>    $$
>    the adjoint map takes the form $\Phi_{\mathrm{reset}}^\dagger(E) = \langle 0|E|0\rangle\, I_d$; it is unital ($\Phi_{\mathrm{reset}}^\dagger(I_d) = I_d$), yet fails to preserve trace for $d \ge 2$, since $\mathrm{tr}\,\Phi_{\mathrm{reset}}^\dagger(|0\rangle\langle 0|) = \mathrm{tr}(I_d) = d \ne 1 = \mathrm{tr}(|0\rangle\langle 0|)$.

**Proof.**  
1. Since $\dim_{\mathbb{R}} W_0 \ge 1$ ($I_d \in W_0$) and at each step prior to stabilization the dimension strictly increases ($\dim W_{k+1} \ge \dim W_k + 1$) inside the $d^2$-dimensional space $\mathrm{Herm}_d(\mathbb{C})$, strict increase can occur at most $d^2 - 1$ times; as soon as $W_{n+1} = W_n$, linearity implies $W_{n+k} = W_n$ for all $k \ge 1$.
2. The probability of any finite branch $(a_1, o_1), \dots, (a_k, o_k)$ with final effect $E \in \mathcal{E}_0$ equals $\mathrm{tr}(\rho\, \mathcal{I}_{a_1,o_1}^\dagger \cdots \mathcal{I}_{a_k,o_k}^\dagger(E))$, and the linear span of all such operators is precisely $W_\infty$.
3. The identity $\mathrm{tr}(\Phi(\rho)) = \mathrm{tr}(\Phi(\rho) I_d) = \mathrm{tr}(\rho\,\Phi^\dagger(I_d))$ equals $\mathrm{tr}(\rho)$ for all $\rho \in \mathrm{Herm}_d(\mathbb{C})$ if and only if $\Phi^\dagger(I_d) = I_d$. For the reset channel, $\mathrm{tr}(\Phi_{\mathrm{reset}}(\rho) E) = \mathrm{tr}(\rho)\langle 0|E|0\rangle = \mathrm{tr}(\rho (\langle 0|E|0\rangle I_d))$, whence $\Phi_{\mathrm{reset}}^\dagger(E) = \langle 0|E|0\rangle I_d$ and $\mathrm{tr}(\Phi_{\mathrm{reset}}^\dagger(|0\rangle\langle 0|)) = d \ge 2$. $\blacksquare$

Let us also examine the informational capacity of finite projective windows in dimension $d = 3$ ($\mathcal{H} = \mathbb{C}^3$, where the real dimension of the space of Hermitian matrices equals $\dim_{\mathbb{R}} \mathrm{Herm}_3(\mathbb{C}) = 3^2 = 9$). If the observer selects a finite family of pure projectors $P_k = |\psi_k\rangle\langle\psi_k| \in \mathrm{Herm}_3(\mathbb{C})$ ($k = 1, \dots, N$), this family is informationally complete (distinguishes all states $\rho \in \mathcal{S}(\mathbb{C}^3)$, i.e., $\operatorname{span}_{\mathbb{R}}\{P_k\} = \mathrm{Herm}_3(\mathbb{C})$) if and only if the rank of the Hilbert–Schmidt Gram matrix $\operatorname{rank}(P_1, \dots, P_N)$ reaches the full dimension $d^2 = 9$. In particular:
- if a family of $N = 12$ rays is assembled from $4$ orthonormal bases (for instance, $4$ mutually unbiased bases `MUB` in $\mathbb{C}^3$; see `Chapter II.7`), then in each of the $4$ bases the sum of the three projectors equals the same identity $P_{b,1} + P_{b,2} + P_{b,3} = I_3$, introducing $3$ linear dependencies among the $12$ projectors and exhausting the entire $9$-dimensional memory $\mathrm{Herm}_3(\mathbb{C})$ ($\operatorname{rank} = 12 - 3 = 9$);
- conversely, if an even larger window of $N = 16$ projectors is chosen inside a proper subalgebra (for instance, only real symmetric projectors in $\mathrm{Sym}_3(\mathbb{R}) \subset \mathrm{Herm}_3(\mathbb{C})$ or projectors failing to capture imaginary antisymmetric coherences), its linear span stalls at dimension $\le 6 < 9$, leaving a $3$-dimensional imaginary subspace in the blind kernel $W_0^\perp$. Here too, what is decisive is not the raw number of questions $N$, but their rank in $\mathrm{Herm}_d(\mathbb{C})$.

---

## §II.6.4. Gleason's Theorem ($d \ge 3$), the Counterexample on Qubit Projectors ($d = 2$), and Busch's Theorem on the Full Effect Cone

Let us conclude the chapter with an illustration of how **changing the repertoire of admissible questions in the observer's contract changes the mathematical conclusion regarding the state space**.

Suppose the observer assigns to each question $E$ a probability $v(E) \in [0,1]$ such that on orthogonal resolutions of the identity $\sum_i E_i = I_d$ the probabilities add up to unity: $\sum_i v(E_i) = 1$. Must such a probability law be given by the Born rule $v(E) = \mathrm{tr}(\rho E)$ for some density matrix $\rho \in \mathcal{S}(\mathcal{H})$?

The answer changes dramatically depending on which questions belong to the contract:

> **Theorem II.6.2 (The Gleason–Busch bifurcation: projectors versus the full effect interval $\mathcal{E}(\mathcal{H})$).**  
> *Classical foundation.* Gleason's theorem (1957) on subspace measures for $d \ge 3$ and Busch's theorem (2003) on effect valuations for $d \ge 2$ are classical results. *Contribution of this book:* Comparison of the two domains of applicability and explicit analysis of the qubit exception $d = 2$ via Busch's trine.
> 1. **(Gleason's theorem on orthogonal projectors for $d \ge 3$, A. M. Gleason, 1957).** When the dimension of the Hilbert space satisfies $d \ge 3$, every non-negative measure $v : \mathcal{P}(\mathcal{H}) \to [0,1]$ on the lattice of orthogonal projectors $\mathcal{P}(\mathcal{H}) = \{P \in \mathrm{Herm}_d(\mathbb{C}) : P^2 = P\}$ satisfying $v(P_1) + \cdots + v(P_d) = 1$ for every orthonormal basis extends uniquely to a linear trace functional $v(P) = \mathrm{tr}(\rho P)$ with a density matrix $\rho \in \mathcal{S}(\mathcal{H})$ (because for $d \ge 3$ orthogonal bases are intertwined along shared one-dimensional rays).
> 2. **(Breakdown on qubit projectors at $d = 2$).** When $d = 2$, every non-trivial orthonormal basis consists of just a single pair of antipodal points $\{P_{\mathbf{n}}, P_{-\mathbf{n}}\}$ on the Bloch sphere $S^2$ ($P_{\mathbf{n}} + P_{-\mathbf{n}} = I_2$), and distinct antipodal pairs **are pairwise disjoint**. Therefore, the condition $v(P_{\mathbf{n}}) + v(P_{-\mathbf{n}}) = 1$ constrains each axis $\pm \mathbf{n}$ completely independently of all others: any function $f : S^2 \to [0,1]$ satisfying $f(-\mathbf{n}) = 1 - f(\mathbf{n})$ (for instance, a discontinuous hemisphere indicator $f(\mathbf{n}) \in \{0,1\}$) defines a valid projective measure on $\mathcal{P}(\mathbb{C}^2)$ that **cannot be represented** in the form $\mathrm{tr}(\rho P_{\mathbf{n}}) = \frac{1}{2}(1 + \mathbf{r}\cdot\mathbf{n})$ for any Bloch vector $\mathbf{r} \in \mathbb{R}^3$.
> 3. **(Busch's theorem on the full space of effects for every $d \ge 2$, P. Busch, 2003).** If, however, the observer's contract includes **the entire convex interval of quantum effects** $\mathcal{E}(\mathcal{H}) = \{E \in \mathrm{Herm}_d(\mathbb{C}) : 0 \preceq E \preceq I_d\}$, then for **every** dimension $d \ge 2$ (including the qubit $d = 2$), every valuation function $v : \mathcal{E}(\mathcal{H}) \to [0,1]$ satisfying the three axioms:
>    - non-negativity: $v(E) \ge 0$ for all $E \in \mathcal{E}(\mathcal{H})$;
>    - normalization: $v(I_d) = 1$;
>    - finite additivity on effects: $v(E_1 + \cdots + E_k) = v(E_1) + \cdots + v(E_k)$ whenever $E_1 + \cdots + E_k \preceq I_d$,
>    is uniquely given by a density matrix $\rho \in \mathcal{S}(\mathcal{H})$ according to the Born rule:
>    $$
>    v(E) = \mathrm{tr}(\rho E) \qquad \bigl(\forall E \in \mathcal{E}(\mathcal{H})\bigr).
>    $$
>    Moreover, on individual non-projective resolutions of the identity (such as the symmetric planar *trine* of three effects $E_k = \frac{2}{3}|\psi_k\rangle\langle\psi_k|$ at $120^\circ$ angles, where $E_1 + E_2 + E_3 = I_2$), an additive measure cannot take deterministic values $\{0,1\}$ on the rays, while the totality of **all** rational effect splittings $\frac{1}{m} E$ in $\mathcal{E}(\mathbb{C}^2)$ forces $v$ to be $\mathbb{R}$-linear on $\mathrm{Herm}_2(\mathbb{C})$.

**Proof of item 3 (after P. Busch, 2003).**  
From finite additivity for $E \in \mathcal{E}(\mathcal{H})$ and positive integers $m \le n$, we have $n v(\frac{1}{n} E) = v(E)$, whence $v(\frac{m}{n} E) = \frac{m}{n} v(E)$ for all rationals $\frac{m}{n} \in [0,1]$. If $0 \preceq A \preceq B \preceq I_d$, then $B - A \in \mathcal{E}(\mathcal{H})$ and $v(B) = v(A) + v(B-A) \ge v(A)$ (monotonicity). For any real $\alpha \in [0,1]$, choose rationals $q_k \uparrow \alpha \downarrow r_k$; from monotonicity $q_k v(E) = v(q_k E) \le v(\alpha E) \le v(r_k E) = r_k v(E)$, homogeneity $v(\alpha E) = \alpha v(E)$ follows. Then for any $A, B \in \mathrm{Herm}_d^+(\mathbb{C})$ and small $t > 0$ such that $t(A+B) \preceq I_d$, we have $v(t(A+B)) = v(tA) + v(tB)$, which extends to a positive linear functional on all of $\mathrm{Herm}_d(\mathbb{C})$. By the Riesz representation theorem in a finite-dimensional space with inner product $\langle \rho, E \rangle = \mathrm{tr}(\rho E)$, there exists a unique Hermitian operator $\rho \succeq 0$ with $\mathrm{tr}\,\rho = v(I_d) = 1$ such that $v(E) = \mathrm{tr}(\rho E)$. $\blacksquare$

---

## §II.6.5. Historical-Philosophical Parallel: The Pure Witness (`YS 2.20`) and the Separation of the Contract $\Gamma$ from the Instrument $\mathcal{I}_{a,o}$

In the second chapter of the *Yoga Sūtras* (`YS 2.20`), Patañjali formulates the relationship between the seer (*draṣṭṛ*) and the modifications of the mind (*pratyaya*):

> *draṣṭā dṛśi-mātraḥ śuddho 'pi pratyayānupaśyaḥ* —  
> "The seer is pure seeing (*dṛśi-mātraḥ*); though pure in itself, it perceives in accordance with the mental presentations set before it (*pratyayānupaśyaḥ*)."

In the architecture of our chapter (outside the deductive premises of the operator theorems), this formula precisely warns against conflating three distinct levels:
- the prepared state $\rho \in \mathcal{S}(\mathcal{H})$;
- the specific instrument channel $\mathcal{I}_{a,o}$, which perturbs the state upon reading and discards invisible coherences;
- and the position of the observer specifying the operational contract $\Gamma$ itself: the choice of the question repertoire $\mathcal{E}_0$ and actions $\mathcal{A}$ determines which subspace $W_\infty$ will be visible in the experiment, yet the contract itself is not one of the density matrices inside $\mathcal{S}(\mathcal{H})$.

---

## §II.6.6. Chapter Summary and Bridge to Chapter II.7

The table below summarizes the results of `Chapter II.6` on states and effects.

#### Table II.6.1. Quantum Enrichment of the Observer's Contract in Chapter II.6

| Construction of Book I | Quantum enrichment in `Chapter II.6` | Main result |
| :--- | :--- | :--- |
| Four-point scene $S_4 = \mathbb{F}_2^2$ and $16$ Boolean tables | Walsh–Bloch map $E_\lambda(q) = c_0 I_2 + \lambda \mathbf{c}\cdot\boldsymbol{\sigma}$ | Three-level filtration of effects $16 \to 8 \to 2$ with thresholds $\lambda = 1/\sqrt{3}$ and $\lambda = 1$ (`Theorem II.6.1`) |
| Moore–Nerode memory classes (`Chapter I.3`) | Branch closure of effects $W_\infty \subseteq \mathrm{Herm}_d(\mathbb{C})$ | Stabilization in $\le d^2 - 1$ steps; $\rho_1 \sim_\Gamma \rho_2 \iff \rho_1 - \rho_2 \in W_\infty^\perp$ (`Prop. II.6.1`) |
| Forward state transfer versus pullback of questions (`Chapter I.2`) | Total channel $\Phi$ (state evolution) and adjoint channel $\Phi^\dagger$ (effect evolution) | $\Phi$ is trace-preserving $\iff \Phi^\dagger(I_d) = I_d$; the reset channel shows non-closure of `CPTP` under $\dagger$ |
| Dependence of inference on the question repertoire $\mathcal{Q}$ | Projectors $\mathcal{P}(\mathcal{H})$ versus full effect cone $\mathcal{E}(\mathcal{H})$ | Non-Born measures exist on $\mathcal{P}(\mathbb{C}^2)$, whereas on $\mathcal{E}(\mathbb{C}^2)$ Busch's theorem yields $v(E) = \mathrm{tr}(\rho E)$ (`Theorem II.6.2`) |

In `Theorem II.6.1`, we discovered the critical threshold $\lambda = 1/\sqrt{3}$ at which the four single-point questions of the scene $S_4$ ($|q| = 1$) first touch the boundary of the effect cone and become rank-$1$ operators. What geometric figure do these four questions form on the Bloch sphere, and how does the parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ of Book I manifest itself in quantum contextuality? This is the subject of **Chapter `II.7`**.

---

## Summary Passport of Chapter II.6 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Theorem II.6.1` | Exhaustive enumeration of the $16$ Boolean tables on $S_4$: verification of $E_\lambda(\neg q) = I_2 - E_\lambda(q)$, the identity $\|\mathbf{c}(q)\|_2 = \sqrt{c_0(1-c_0)}$, and the filtration of admissible effects $16 \to 8 \to 2$ at $\lambda \in \{1/\sqrt{3}, 1, 2\}$ | `GATE-II06-01` |
| `Proposition II.6.1` (items 1–2) | Construction of the branch closure chain $W_0 \subset W_1 \subset \cdots = W_\infty$, stabilization in $\le d^2 - 1$ steps, and verification of the completeness of $12$ `MUB` projectors versus the incompleteness of $16$ real projectors in $\mathrm{Herm}_3(\mathbb{C})$ | `GATE-II06-02` |
| `Proposition II.6.1` (item 3) | Verification of $\Phi^\dagger(I_d) = I_d$ for `CPTP` channels and $\mathrm{tr}(\Phi_{\mathrm{reset}}^\dagger(|0\rangle\langle 0|)) = d \ne 1$ for the reset channel | `GATE-II06-03` |
| `Theorem II.6.2` | Verification of a discontinuous antipodal valuation on the projectors $\mathcal{P}(\mathbb{C}^2)$ and linearity of a Busch measure on the effect cone $\mathcal{E}(\mathbb{C}^2)$ | `GATE-II06-04` |
