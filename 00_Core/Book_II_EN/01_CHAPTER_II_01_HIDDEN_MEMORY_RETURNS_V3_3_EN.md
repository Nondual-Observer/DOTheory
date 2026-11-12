# Chapter II.1. Hidden Memory Returns: The Linear Observer, Hankel Matrices, and Minimal Realization

> *Tat tvam asi* — That thou art.
>
> — Uddālaka Āruṇi, *Chāndogya Upaniṣad* (6.8.7)

Book I concluded at the boundary of the set-theoretic observation contract $\Gamma$. In `Chapter I.3`, we proved the Moore–Nerode theorem: if the observer has access only to an external protocol of questions and partial actions, then two histories are indistinguishable if and only if they yield identical answers under all admissible future continuations, and the equivalence classes of this indistinguishability form a minimal finite memory automaton. In `Chapter I.8`, the same problem appeared from the perspective of a scalar numerical sequence $(s_0, s_1, s_2, \dots)$: the observer views an infinite tape of samples through a finite sliding window and assembles Hankel tables $H_m = (s_{i+j})_{0 \le i,j < m}$ from them. By Kronecker's theorem (`Theorem I.8.3`), the finiteness of the rank of all such tables is equivalent to the fact that a finite linear recurrent memory is hidden behind the external sequence.

Within Book I, however, these two pictures—the automaton memory of Nerode classes and the numerical rank of Hankel matrices—had not yet been united into a single operator geometry. In `Chapter I.3`, states do not form a vector space and cannot be added to one another, whereas in `Chapter I.8` we dealt only with a scalar sequence without an explicitly written space of internal states, an input excitation operator, or an output reading operator. As soon as the observer acquires the right to add contributions (`Chapter I.5`) and multiply them by scalars from a field $K$, the first question of Volume Two arises:

> **How is the minimal hidden memory space of a linear observer structured—a space that cannot be seen in a single instantaneous frame, yet is uniquely recovered from the "past $\to$ future" transfer table?**

The present chapter opens **Enrichment I** (`Table I.9.3` of Book I) and provides a complete, constructive answer to this question. We will show that:
1. even when the observed output space is one-dimensional ($\dim_K Y = 1$), any attempt to compress the description of the system to an instantaneous scalar snapshot destroys trajectory predictability as soon as hidden memory modes are activated;
2. the block Hankel operator $\mathcal{H} = \mathcal{O}\mathcal{R}$, which connects past inputs to future readings, factors through the reachability operator $\mathcal{R}$ and the observability operator $\mathcal{O}$, and by the Ho–Kalman theorem its rank is equal to the exact dimension of the minimal linear realization $(A, B, C)$—the linear dual of the minimal Nerode automaton;
3. on the four-point scene $S_4 = \mathbb{F}_2^2$, shared across all chapters of Book I, a periodic traversal of the four states generates an explicit minimal linear realization in which one can directly see which memory coordinates hold the shift between the current frame and the future answer;
4. in the space of Boolean functions on the hypercube $D^n = \{0,1\}^n$, the linear degeneracy of a blind projector is measured by the exact dimension defect formula $2^n - (n+1)$, while in continuous quadratic memory functionals the requirement of preserving nearest-neighbor step interactions across all input vectors rigidly reduces the full coordinate permutation group $\mathfrak{S}_n$ to the dihedral group of shifts and reflections.

---

## §II.1.1. Entry from the Observer's Contract: Why a Single Instantaneous Frame Is Insufficient

Let us return to the baseline setup of Book I. Suppose the observer operates within an operational contract $\Gamma$ in which, at each discrete time step $t = 0, 1, 2, \dots$, they can apply an input action (an excitation question) $u_t$ from a finite-dimensional input vector space $U = K^p$ over a field $K$ and read on the instrument an output response $y_t$ in the observation space $Y = K^m$.

Suppose an investigator, accustomed to trusting only what is directly visible on the instrument dial at moment $t$, attempts to build a forecast according to the rule "the next visible frame $y_{t+1}$ is determined by the current visible frame $y_t$ and the current input $u_t$." In the simplest case of homogeneous evolution ($u_t = 0$), this would mean the existence of a linear operator $F : Y \to Y$ such that $y_{t+1} = F y_t$ holds for every trajectory.

Let us demonstrate on the most elementary example why this "memoryless screen" hypothesis collapses as soon as the carrier of the system contains even a single hidden degree of freedom orthogonal to the instantaneous reading.

Consider a two-dimensional internal state space $V = K^2$ with state vector $h_t = (h_{t,1}, h_{t,2})^{\mathsf{T}} \in K^2$, evolving according to the linear law
$$
h_{t+1} = B h_t, \qquad y_t = C h_t,
$$
where the step operator $B : K^2 \to K^2$ and the reading operator $C : K^2 \to K$ are given by the matrices
$$
B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad C = \begin{pmatrix} 1 & 0 \end{pmatrix}.
$$
The reading operator $C$ sees only the first coordinate, $y_t = h_{t,1}$, whereas the second coordinate $h_{t,2}$ at moment $t=0$ remains in the shadow ($\ker C = \{(0, c)^{\mathsf{T}} : c \in K\}$—the exact linear analogue of the indistinguishability fiber from `Chapter I.2`). Take two distinct initial states:
$$
h^{(1)}_0 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad h^{(2)}_0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}.
$$
At the initial moment $t = 0$, the instrument produces the exact same response on both states:
$$
y^{(1)}_0 = C h^{(1)}_0 = 1, \qquad y^{(2)}_0 = C h^{(2)}_0 = 1.
$$
To an instantaneous reading, the states $h^{(1)}_0$ and $h^{(2)}_0$ are indistinguishable: their difference $h^{(2)}_0 - h^{(1)}_0 = (0, 1)^{\mathsf{T}}$ lies entirely in the kernel $\ker C$. However, already at the very next step $t = 1$, the step operator $B$ transports the hidden second coordinate into the reading window:
$$
y^{(1)}_1 = C B h^{(1)}_0 = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 0,
\qquad
y^{(2)}_1 = C B h^{(2)}_0 = \begin{pmatrix} 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = 1.
$$
No operator $F : K \to K$ can simultaneously map the scalar $y_0 = 1$ to both $0$ and $1$. The reason for this divergence is transparent: at moment $t=0$, the second coordinate $h_{0,2}$ is invisible to the direct question $C$, but it **lives in the transferred question of the next step** $C B = (0, 1)$. In the terminology of `Chapter I.2`, the action $B$ performs the pullback (transfer) of the linear question $C \mapsto C B$, and in the terminology of `Chapter I.3`, the pair $(C, CB)$ exhausts the linear memory of depth $2$.

---

## §II.1.2. Working Example on the Backbone of Book I: Traversal of the Four-Point Scene $S_4$ and Its Hankel Rank

Before formulating the general theorems on block Hankel operators, let us examine how linear memory operates on the central object of Volume One—the four-point scene
$$
S_4 = \mathbb{F}_2^2 = \{00, 01, 10, 11\}.
$$
In `Chapter I.9` (`Theorem I.9.3a`), three basic binary questions (the coordinate partitions $X, C, B$) acted on the scene $S_4$, corresponding to the three non-trivial characters $\chi_{10}, \chi_{01}, \chi_{11}$ of the group $\mathbb{F}_2^2$. Suppose now that the system performs a deterministic cyclic traversal of the four points of the scene $S_4$:
$$
00 \longrightarrow 01 \longrightarrow 11 \longrightarrow 10 \longrightarrow 00 \longrightarrow \cdots
$$
(a Gray code traversal, where exactly one bit changes at each step), while the observer at each step $t = 0, 1, 2, \dots$ reads a scalar signal $s_t \in K$ (over the field $K = \mathbb{Q}$ or $K = \mathbb{F}_2$) using a chosen linear sensor.

Let us record what Hankel rank $\operatorname{rank} \mathcal{H}_s$ the observer sees depending on which question on $S_4$ they read:

1. **Constant sensor $q_{\mathrm{const}}(x) = 1$.** This generates the stationary sequence $s = (1, 1, 1, 1, \dots)$ with characteristic polynomial $\lambda - 1 = 0$. All Hankel minors of order $\ge 2$ vanish, and $\operatorname{rank} \mathcal{H}_s = 1$: the observer only needs to remember a single scalar state.
2. **Axial question $X(x_1, x_2) = x_1 + x_2 \pmod 2$ (checkerboard parity on $S_4$).** Along the traversal $00 \to 01 \to 11 \to 10$, the parity takes alternating values
   $$
   s^{(X)} = (0, 1, 0, 1, 0, 1, \dots), \qquad s^{(X)}_{t+2} = s^{(X)}_t.
   $$
   The two-dimensional Hankel window
   $$
   H_2(s^{(X)}) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
   $$
   is non-singular over any field $K$, and all windows $H_m(s^{(X)})$ for $m \ge 2$ have $\operatorname{rank} H_m(s^{(X)}) = 2$. Although the scene $S_4$ itself consists of $4$ points, the parity question $X$ glues opposite vertices of the square ($00 \sim 11$ and $01 \sim 10$), compressing the minimal linear memory to dimension $d_{\min} = 2$.
3. **Single-point indicator $q_{00}(x) = \delta_{x, 00}$ over the field $K = \mathbb{Q}$.** This generates the $4$-periodic impulse sequence
   $$
   s^{(00)} = (1, 0, 0, 0, 1, 0, 0, 0, \dots), \qquad s^{(00)}_{t+4} = s^{(00)}_t.
   $$
   The four-dimensional Hankel window takes the form
   $$
   H_4(s^{(00)}) = \begin{pmatrix}
   1 & 0 & 0 & 0 \\
   0 & 0 & 0 & 1 \\
   0 & 0 & 1 & 0 \\
   0 & 1 & 0 & 0
   \end{pmatrix}, \qquad \det H_4(s^{(00)}) = -1 \ne 0,
   $$
   and $\operatorname{rank} H_m(s^{(00)}) = 4$ holds for all $m \ge 4$. The minimal linear realization $(A, B, C)$ has dimension $4$ and recovers all four phases of the scene $S_4$:
   $$
   B = \begin{pmatrix}
   0 & 1 & 0 & 0 \\
   0 & 0 & 1 & 0 \\
   0 & 0 & 0 & 1 \\
   1 & 0 & 0 & 0
   \end{pmatrix}, \qquad
   A = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \qquad
   C = \begin{pmatrix} 1 & 0 & 0 & 0 \end{pmatrix}, \qquad
   s^{(00)}_t = C B^t A.
   $$
4. **Two-question sensor $(x_1, x_2) \in \mathbb{Q}^2$ along the Gray traversal $00 \to 01 \to 11 \to 10$.** If we consider the first coordinate $x_1 = (0, 0, 1, 1, 0, 0, 1, 1, \dots)$ over $\mathbb{Q}$, the sum of two half-periods is constant: $s_{t+2} + s_t = 1$, whence $s_{t+3} + s_{t+1} = 1$, and subtraction yields the third-order recurrence
   $$
   s_{t+3} - s_{t+2} + s_{t+1} - s_t = 0 \qquad \bigl((\lambda - 1)(\lambda^2 + 1) = 0\bigr).
   $$
   The Hankel matrix $H_3(x_1)$ has determinant
   $$
   \det \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} = -1 \ne 0,
   $$
   so $\operatorname{rank} \mathcal{H}_{x_1} = 3$: the third mode ($\lambda = 1$) stores the constant mean offset $1/2$, while the pair of complex-conjugate modes ($\lambda = \pm i$, i.e., the $90^\circ$ rotation from `Chapter I.5`) stores the phase of oscillation around that mean.

#### Table II.1.1. Hankel Rank and Minimal Memory Dimension under Traversal of the Scene $S_4$

| Observed question on $S_4$ | Generated sequence $(s_0, s_1, s_2, s_3, \dots)$ | Annihilating polynomial $P(\lambda)$ | Hankel rank $\operatorname{rank}\mathcal{H}_s$ | Meaning of the retained memory states |
| :--- | :---: | :---: | :---: | :--- |
| Constant $q_{\mathrm{const}}$ | $(1, 1, 1, 1, \dots)$ | $\lambda - 1$ | $1$ | Constant scale level only |
| Parity $X(x) = x_1 \oplus x_2$ | $(0, 1, 0, 1, \dots)$ | $\lambda^2 - 1$ | $2$ | Two checkerboard parts $\{00,11\}$ and $\{01,10\}$ |
| Coordinate $x_1$ (over $\mathbb{Q}$) | $(0, 0, 1, 1, \dots)$ | $(\lambda - 1)(\lambda^2 + 1)$ | $3$ | Mean level $+$ two-dimensional oscillator $\lambda^2 = -1$ |
| Vertex indicator $q_{00}$ | $(1, 0, 0, 0, \dots)$ | $\lambda^4 - 1$ | $4$ | Full distinction of all $4$ phases of the scene $S_4$ |

This example immediately makes tangible the central idea of the chapter: **the dimension of minimal internal memory is not the "size of the carrier in nature," but the exact number of independent future continuation modes distinguished by the observer's chosen question.**

---

## §II.1.3. The Operator Triple $(A, B, C)$, Hankel Factorization $\mathcal{H} = \mathcal{O}\mathcal{R}$, and the Ho–Kalman Theorem

Let us now pass to the general linear case. Let $K$ be an arbitrary field, $U = K^p$ the space of inputs, and $Y = K^m$ the space of outputs (instrument readings).

> **Definition II.1.1 (Linear system with memory and its Markov parameters).**  
> A *linear realization* of dimension $d$ over a field $K$ is a triple of linear operators $(A, B, C)$ with a hidden state space $V = K^d$:
> - $A : U \to V$ is the *write (input) operator*, converting an input impulse into an initial excitation of memory;
> - $B : V \to V$ is the *step (internal dynamics) operator*, updating the memory over a single time step;
> - $C : V \to Y$ is the *read (output) operator*, projecting the internal state onto the instrument dial.
>
> Given an input sequence $(u_0, u_1, \dots)$ and an initial state $h_0 \in V$, the system evolves according to the rule
> $$
> h_{t+1} = B h_t + A u_t, \qquad y_t = C h_t = C B^t h_0 + \sum_{k=0}^{t-1} C B^{t-1-k} A u_k.
> $$
> The sequence of unit-impulse response operators
> $$
> M_t = C B^t A \in \mathrm{Hom}_K(U, Y), \qquad t = 0, 1, 2, \dots,
> $$
> is called the sequence of *Markov parameters* of the realization $(A, B, C)$.

In this equation, two components of the external response $y_t$ are clearly visible:
- the first term $C B^t h_0$ is the *free (inertial) response* of the memory $h_0$ already accumulated in the past when the external input is turned off ($u_k = 0$);
- the second sum $\sum_{k=0}^{t-1} M_{t-1-k} u_k$ is the *forced convolution* of past input excitations with the Markov parameters $M_r = C B^r A$.

To separate the internal geometry of memory from the arbitrariness of choosing a basis in the space $V$, we introduce two canonical maps connecting the hidden space $V$ with the infinite past and the infinite future.

> **Definition II.1.2 (Reachability operator $\mathcal{R}$, observability operator $\mathcal{O}$, and block Hankel operator $\mathcal{H}$).**  
> For each window horizon $N \ge 1$, we define:
> 1. The *$N$-step reachability operator* $\mathcal{R}_N : U^N \to V$:
>    $$
>    \mathcal{R}_N (u_0, u_1, \dots, u_{N-1})^{\mathsf{T}} = \sum_{j=0}^{N-1} B^j A u_j = \begin{pmatrix} A & BA & B^2 A & \cdots & B^{N-1} A \end{pmatrix} \begin{pmatrix} u_0 \\ u_1 \\ \vdots \\ u_{N-1} \end{pmatrix}.
>    $$
> 2. The *$N$-step observability operator* $\mathcal{O}_N : V \to Y^N$:
>    $$
>    \mathcal{O}_N h = \begin{pmatrix} C h \\ C B h \\ \vdots \\ C B^{N-1} h \end{pmatrix} = \begin{pmatrix} C \\ CB \\ \vdots \\ CB^{N-1} \end{pmatrix} h.
>    $$
> 3. The *block Hankel matrix of order $N$*, $\mathcal{H}_N : U^N \to Y^N$, assembled from the Markov parameters $M_{i+j} = C B^{i+j} A$:
>    $$
>    \mathcal{H}_N = \begin{pmatrix}
>    M_0 & M_1 & M_2 & \cdots & M_{N-1} \\
>    M_1 & M_2 & M_3 & \cdots & M_N \\
>    \vdots & \vdots & \vdots & \ddots & \vdots \\
>    M_{N-1} & M_N & M_{N+1} & \cdots & M_{2N-2}
>    \end{pmatrix}.
>    $$
> As $N \to \infty$ (on the space of finitely supported input sequences $U^{(\mathbb{N})}$ and the space of all output trajectories $Y^{\mathbb{N}}$), these maps define the full operators $\mathcal{R} : U^{(\mathbb{N})} \to V$, $\mathcal{O} : V \to Y^{\mathbb{N}}$, and the infinite block Hankel operator $\mathcal{H} : U^{(\mathbb{N})} \to Y^{\mathbb{N}}$.

By the rule of block matrix multiplication itself, the $(i,j)$-th block of the product $\mathcal{O}_N \mathcal{R}_N$ equals $(C B^i)(B^j A) = C B^{i+j} A = M_{i+j}$. Thus, for every $N \ge 1$ (and in the limit $N = \infty$), we have the fundamental factorization:
$$
\mathcal{H}_N = \mathcal{O}_N \mathcal{R}_N, \qquad \mathcal{H} = \mathcal{O} \mathcal{R}.
$$

```text
   FACTORIZATION OF THE BLOCK HANKEL OPERATOR THROUGH HIDDEN MEMORY V

      Past inputs U^(N)                    Future readings Y^N
             |                                     ^
             |  Reachability operator R            |  Observability operator O
             v                                     |
             +-------->  Hidden memory V  ---------+
                      (minimal quotient:
                       Im(R) / (Im(R) ∩ Ker(O)))

      External transfer "past -> future":   H = O * R
      Minimal memory dimension:             d_min = rank(H)
```

This identity expresses the construction of Book I in linear form:
- the subspace $\operatorname{Im} \mathcal{R} \subseteq V$ consists of all states that can be excited by input protocols from the past (the linear analogue of reachable classes from `Chapter I.3`);
- the subspace $\ker \mathcal{O} \subseteq V$ consists of all "silent" states yielding a zero response $C B^i h = 0$ at all future steps $i \ge 0$ (the linear analogue of the indistinguishability kernel $\sim_\Gamma$ from `Chapter I.3`);
- the quotient space $\operatorname{Im}\mathcal{R} / (\operatorname{Im}\mathcal{R} \cap \ker \mathcal{O}) \cong \operatorname{Im}(\mathcal{O}\mathcal{R}) = \operatorname{Im}\mathcal{H}$ is precisely the **observer's minimal memory space**, purged of both unreachable parasitic coordinates and unobservable shadow modes.

Let us now state and prove the central theorems on observability, the Ho–Kalman minimal realization, and window stabilization.

> **Theorem II.1.1 (Cayley–Hamilton observability criterion and stabilization at a shift threshold $j_0$).**  
> *Classical foundation.* Kalman's observability criterion for finite-dimensional linear systems (Kalman, 1960) and stabilization of ascending kernel filtrations via the Cayley–Hamilton theorem. *Contribution of this book:* Shifted-window observability formula $(C B^{j_0}, \dots, C B^{j_0+r-1})|_{W_0}$ under delay threshold $j_0$, separating zero single-slice response from joint injectivity over horizon $r$.
> Let $\dim_K V = d < \infty$.
> 1. The descending chain of partial observability kernels $\ker \mathcal{O}_1 \supseteq \ker \mathcal{O}_2 \supseteq \cdots \supseteq \ker \mathcal{O}_N \supseteq \cdots$ stabilizes no later than step $N = d$:
>    $$
>    \ker \mathcal{O}_d = \ker \mathcal{O}_{d+1} = \cdots = \ker \mathcal{O} = \bigcap_{i=0}^{d-1} \ker(C B^i).
>    $$
>    The pair $(B, C)$ is completely observable ($\ker \mathcal{O} = \{0\}$) if and only if $\operatorname{rank} \mathcal{O}_d = d$. Dually, the pair $(A, B)$ is completely reachable ($\operatorname{Im}\mathcal{R} = V$) if and only if $\operatorname{rank} \mathcal{R}_d = d$.
> 2. Suppose a shift delay with threshold $j_0 \ge 0$ acts on the hidden space $V$: for some subspace of initial perturbations $W_0 \subseteq V$ of dimension $r_0 = \dim_K W_0 \ge 1$, one has $C B^t W_0 = \{0\}$ for all $0 \le t < j_0$, whereas the joint post-threshold window of length $r_0$, $\mathcal{O}_{[j_0, j_0+r_0-1]}|_{W_0} = (C B^{j_0}, \dots, C B^{j_0+r_0-1})^{\mathsf{T}}|_{W_0} : W_0 \to Y^{r_0}$, is injective (in particular, for $r_0 = 1$ the map $C B^{j_0}|_{W_0}$ itself is injective, while for $r_0 = 2$ and scalar output $\dim_K Y = 1$ the pair of rows $(C B^{j_0}, C B^{j_0+1})|_{W_0}$ is injective). Then any window of length $N \le j_0$ is completely blind to perturbations from $W_0$, whereas for every $h_0 \in W_0 \setminus \{0\}$ with non-vanishing leading response $C B^{j_0} h_0 \ne 0$, the reading window $0 \le t \le j_0 + r_0 - 1$ uniquely recovers both the delay threshold $j_0$ and the perturbation vector $h_0 \in W_0$.

**Proof.**  
1. By the Cayley–Hamilton theorem, the characteristic polynomial $\chi_B(\lambda) = \lambda^d + c_{d-1}\lambda^{d-1} + \cdots + c_0 \in K[\lambda]$ annihilates the operator $B$:
$$
B^d = -c_{d-1} B^{d-1} - \cdots - c_1 B - c_0 I_V.
$$
Multiplying this identity on the left by $C B^k$ ($k \ge 0$), we obtain by induction that every row of the block $C B^{d+k}$ is a linear combination of the first $d$ block rows $C, CB, \dots, C B^{d-1}$. Consequently, if a vector $h \in V$ satisfies $C B^i h = 0$ for all $0 \le i \le d-1$, then $C B^i h = 0$ holds for all $i \ge d$ as well, whence $\ker \mathcal{O} = \ker \mathcal{O}_d$. By the rank-nullity theorem, $\ker \mathcal{O}_d = \{0\}$ is equivalent to $\operatorname{rank} \mathcal{O}_d = d$. The reachability statement follows by passing to the dual operators $(B^{\mathsf{T}}, A^{\mathsf{T}})$.

2. Let $h_0 \in W_0 \setminus \{0\}$ satisfy $C B^{j_0} h_0 \ne 0$. By hypothesis, $y_t = C B^t h_0 = 0$ for all $0 \le t < j_0$, so any window of length $N \le j_0$ outputs the zero column on $h_0$ and cannot distinguish $h_0$ from the zero state (the shadow witness $(h_0, 0) \in \ker \mathcal{O}_{j_0}$). Conversely, on the index window $0 \le t \le j_0 + r_0 - 1$, the index of the first non-zero response $y_{j_0} = C B^{j_0} h_0 \ne 0$ uniquely fixes the delay threshold $j_0$, and the injectivity of the map $\mathcal{O}_{[j_0, j_0+r_0-1]}|_{W_0}$ uniquely recovers all $r_0$ coordinates of the vector $h_0 \in W_0$ from the sample vector $(y_{j_0}, \dots, y_{j_0+r_0-1})^{\mathsf{T}}$. $\blacksquare$

> **Theorem II.1.2 (Ho–Kalman theorem on minimal linear realization and canonical uniqueness).**  
> *Classical foundation.* The Ho–Kalman minimal linear realization theorem via block Hankel factorization (Ho and Kalman, 1966) and M. P. Schützenberger's theory of rational series (1961). *Contribution of this book:* Operational reading of the minimal state dimension $\dim V_{\min} = \operatorname{rank}\mathcal{H}_f$ as linear observer memory carrying the $\mathrm{GL}_r(K)$ basis gauge torsor ($|\mathcal{R}| > 1$).
> Let an infinite sequence of Markov parameters $(M_0, M_1, M_2, \dots)$ be given, where $M_t \in \mathrm{Hom}_K(U, Y)$, and let $\mathcal{H}$ be the corresponding infinite block Hankel operator.
> 1. A finite-dimensional linear realization $(A, B, C)$ of the sequence $(M_t)_{t \ge 0}$ exists if and only if $\operatorname{rank} \mathcal{H} = r < \infty$.
> 2. The smallest possible state space dimension among all realizations of the sequence $(M_t)$ is exactly equal to the rank of the Hankel operator:
>    $$
>    d_{\min} = \operatorname{rank} \mathcal{H}.
>    $$
>    Moreover, a minimal realization $(A_{\min}, B_{\min}, C_{\min})$ of dimension $r = \operatorname{rank} \mathcal{H}$ is constructed explicitly from any finite full-rank window $\mathcal{H}_N$ ($\operatorname{rank} \mathcal{H}_N = \operatorname{rank} \mathcal{H}_{N+1} = r$): if $\mathcal{H}_N = P Q$ is a full-rank (skeleton) factorization of the matrix $\mathcal{H}_N$ into a matrix of full column rank $P \in K^{mN \times r}$ and a matrix of full row rank $Q \in K^{r \times pN}$ with left and right inverses $P^+ P = I_r$, $Q Q^+ = I_r$, and $\sigma(\mathcal{H}_N)$ is the one-step shifted Hankel matrix $\bigl(M_{i+j+1}\bigr)_{0 \le i,j < N}$, then the triple
>    $$
>    A_{\min} = Q E_U, \qquad B_{\min} = P^+ \,\sigma(\mathcal{H}_N)\, Q^+, \qquad C_{\min} = E_Y^{\mathsf{T}} P
>    $$
>    (where $E_U : U \to U^N$ is the embedding into the first block and $E_Y^{\mathsf{T}} : Y^N \to Y$ is the projection onto the first block) satisfies $C_{\min} B_{\min}^t A_{\min} = M_t$ for all $t \ge 0$.
> 3. A realization $(A, B, C)$ of dimension $d$ is minimal ($d = \operatorname{rank}\mathcal{H}$) if and only if it is simultaneously completely reachable ($\operatorname{rank}\mathcal{R}_d = d$) and completely observable ($\operatorname{rank}\mathcal{O}_d = d$). Any two minimal realizations $(A_1, B_1, C_1)$ and $(A_2, B_2, C_2)$ of the same sequence $(M_t)$ are isomorphic: there exists a unique invertible memory coordinate change operator $S \in \mathrm{GL}_r(K)$ such that
>    $$
>    A_2 = S A_1, \qquad B_2 = S B_1 S^{-1}, \qquad C_2 = C_1 S^{-1}.
>    $$

**Proof.**  
1. If a realization $(A, B, C)$ of dimension $d$ exists, then the factorization $\mathcal{H} = \mathcal{O}\mathcal{R}$ through the space $V = K^d$ immediately yields the bound
$$
\operatorname{rank} \mathcal{H} = \operatorname{rank}(\mathcal{O}\mathcal{R}) \le \dim_K V = d < \infty.
$$
This also shows that every realization must have dimension $d \ge \operatorname{rank} \mathcal{H}$.

2. Conversely, suppose $\operatorname{rank} \mathcal{H} = r < \infty$. Choose a finite horizon $N$ on which the full rank $\operatorname{rank} \mathcal{H}_N = r$ is attained. On the column space $V_{\min} = \operatorname{Im}\mathcal{H} \cong K^r$, the row-shift operator $(y_0, y_1, y_2, \dots)^{\mathsf{T}} \mapsto (y_1, y_2, y_3, \dots)^{\mathsf{T}}$ is well-defined (since the columns of the shifted matrix $\sigma(\mathcal{H})$ are the columns of the original matrix $\mathcal{H}$ with the column index shifted by one). In the basis specified by the skeleton factorization $\mathcal{H}_N = P Q$, the shifted matrix $\sigma(\mathcal{H}_N)$ has the form $P B_{\min} Q$, whence $B_{\min} = P^+ \sigma(\mathcal{H}_N) Q^+$, and by induction $\sigma^t(\mathcal{H}_N) = P B_{\min}^t Q$. Extracting the top-left $(0,0)$ block by multiplying on the left by $E_Y^{\mathsf{T}}$ and on the right by $E_U$, we obtain
$$
M_t = E_Y^{\mathsf{T}} \sigma^t(\mathcal{H}_N) E_U = (E_Y^{\mathsf{T}} P) B_{\min}^t (Q E_U) = C_{\min} B_{\min}^t A_{\min},
$$
which proves the equality $d_{\min} = r = \operatorname{rank}\mathcal{H}$ for any input dimension $p = \dim_K U$ and any output dimension $m = \dim_K Y$.

3. If a realization $(A, B, C)$ of dimension $d$ is reachable and observable, then $\mathcal{R}_d$ is surjective and $\mathcal{O}_d$ is injective, so $\operatorname{rank}\mathcal{H}_d = \operatorname{rank}(\mathcal{O}_d \mathcal{R}_d) = d$. Conversely, if $d = \operatorname{rank}\mathcal{H}$, then in the inequality $r = \operatorname{rank}(\mathcal{O}_d \mathcal{R}_d) \le \min(\operatorname{rank}\mathcal{O}_d, \operatorname{rank}\mathcal{R}_d) \le d = r$ both operators $\mathcal{O}_d$ and $\mathcal{R}_d$ must have full rank $r$. Finally, for two minimal realizations $(A_1, B_1, C_1)$ and $(A_2, B_2, C_2)$, the equality $\mathcal{O}_1 \mathcal{R}_1 = \mathcal{H}_r = \mathcal{O}_2 \mathcal{R}_2$ with injective $\mathcal{O}_1, \mathcal{O}_2$ and surjective $\mathcal{R}_1, \mathcal{R}_2$ uniquely determines the operator $S = \mathcal{O}_2^+ \mathcal{O}_1 = \mathcal{R}_2 \mathcal{R}_1^+ \in \mathrm{GL}_r(K)$ conjugating the two triples. $\blacksquare$

> **Remark II.1.1 (The exact place of the Ho–Kalman theorem in the architecture of the monograph and the $|\mathcal{R}|$ regimes).**  
> In older laboratory notes, an imprecise caveat appeared suggesting that the Hankel rank behaves differently when $\dim Y = 1$ versus $\dim Y > 1$. Theorem II.1.2 removes this ambiguity: **for any dimensions of the input and output windows, the rank of the block Hankel operator $\operatorname{rank}\mathcal{H}$ is exactly equal to the dimension of the minimal state space $d_{\min}$.** The difference between the scalar case ($p = m = 1$, `Chapter I.8`) and the multivariable case ($p, m \ge 1$) consists solely in the fact that in the scalar case a minimal realization is determined up to similarity by a single characteristic recurrence polynomial, whereas for $p, m > 1$ the operator $B_{\min}$ may possess several Jordan blocks (invariant factors) read by different channels of the output $Y$. In terms of the solution count $|\mathcal{R}|$, this theorem cleanly separates two regimes: **canonical uniqueness ($|\mathcal{R}| = 1$)** belongs to the externally testable minimal dimension $d_{\min} = \operatorname{rank}\mathcal{H}$ and the similarity invariants of $B_{\min}$, whereas the choice of a specific internal memory basis forms a **gauge torsor ($|\mathcal{R}| > 1$)** under the action of the general linear group $S \in \mathrm{GL}_r(K)$.

---

## §II.1.4. Walsh–Fourier Decomposition on the Boolean Cube and the Cost of Linear Coarsening

In `Chapter I.5` and `Chapter I.6`, we saw how a canonical basis of signed characters arises on the finite abelian group $G = \mathbb{F}_2^n$ (the Boolean cube $D^n = \{0,1\}^n$). Let us now examine from the standpoint of the linear observer what happens when the instrument is capable of retaining in memory only **affine-linear** questions of degree $\le 1$ on the cube $D^n$, discarding all pairwise and higher-order interactions among the bits.

Let $K$ be a field of characteristic $\operatorname{char} K \ne 2$ (for example, $K = \mathbb{Q}$ or $K = \mathbb{R}$; recall that by the *zero field* in the function space $K^{D^n}$ we mean the identically zero function $0_{D^n}(x) \equiv 0$). The space of all scalar functions $f : D^n \to K$ has dimension $\dim_K K^{D^n} = 2^n$. For each bit mask vector $S = (s_1, \dots, s_n) \in \{0,1\}^n$ with Hamming weight $|S| = s_1 + \cdots + s_n$, define the Walsh character $w_S : D^n \to \{\pm 1\} \subset K$:
$$
w_S(x) = (-1)^{\langle S, x \rangle} = \prod_{i : s_i = 1} (-1)^{x_i}, \qquad x = (x_1, \dots, x_n) \in D^n.
$$
The characters $\{w_S\}_{S \in \{0,1\}^n}$ are pairwise orthogonal with respect to the normalized inner product
$$
\langle f, g \rangle = \frac{1}{2^n} \sum_{x \in D^n} f(x) g(x), \qquad \langle w_S, w_T \rangle = \delta_{S, T},
$$
and form an orthonormal basis of the space $K^{D^n}$. Moreover, the interaction degree $|S|$ decomposes the space $K^{D^n}$ into an orthogonal direct sum of graded layers:
$$
K^{D^n} = \bigoplus_{k=0}^n W_k, \qquad W_k = \operatorname{span}_K \{ w_S : |S| = k \}, \qquad \dim_K W_k = \binom{n}{k}.
$$
The subspace of affine-linear questions of degree $\le 1$ takes the form
$$
W_{\le 1} = W_0 \oplus W_1 = \operatorname{span}_K \{ 1, w_{e_1}, \dots, w_{e_n} \}, \qquad \dim_K W_{\le 1} = n + 1.
$$

> **Proposition II.1.1 (Defect of the linear projector on the Boolean cube $D^n$ and invisibility of pure interactions).**  
> *Classical foundation.* Walsh–Hadamard transform and character orthogonality on the elementary abelian group $\mathbb{F}_2^n$—classical harmonic analysis on the Boolean cube. *Contribution of this book:* Exact characterization of the $(2^n - n - 1)$-dimensional shadow kernel of a first-order linear projector, blind to all pure higher-order parities $k \ge 2$ (including $\beta = x \oplus c$ on $S_4$).
> Let $\Pi_{\le 1} : K^{D^n} \to W_{\le 1}$ be the orthogonal projector onto the subspace of affine-linear questions:
> $$
> (\Pi_{\le 1} f)(x) = \widehat{f}(\varnothing) + \sum_{i=1}^n \widehat{f}(\{i\})\,(-1)^{x_i}, \qquad \widehat{f}(S) = \langle f, w_S \rangle.
> $$
> 1. A function $f \in K^{D^n}$ lies in the kernel of the linear projector ($\Pi_{\le 1} f = 0_{D^n}$, meaning that the linear observer cannot distinguish it from the identically zero function $0_{D^n}$ either by its mean value or by any single-bit marginal) if and only if $f$ expands exclusively in interaction characters of order $|S| \ge 2$:
>    $$
>    f \in \ker \Pi_{\le 1} = \bigoplus_{k=2}^n W_k \Longleftrightarrow \widehat{f}(\varnothing) = 0 \text{ and } \widehat{f}(\{i\}) = 0 \quad (\forall i = 1, \dots, n).
>    $$
> 2. The dimension of the blind kernel of the linear observer on the cube $D^n$ equals
>    $$
>    \dim_K \ker \Pi_{\le 1} = 2^n - (n + 1) = \sum_{k=2}^n \binom{n}{k}.
>    $$
>    In particular, already on the four-point scene $S_4 = D^2$ ($n = 2$), there arises exactly one one-dimensional direction of blindness, $\dim_K \ker \Pi_{\le 1} = 4 - 3 = 1$, spanned by the parity character $w_{11}(x_1, x_2) = (-1)^{x_1 + x_2}$; and on the three-bit cube $D^3$ ($n = 3$, the carrier of the eight triangles of the nerve $O_6$ from `Chapter I.9`), the dimension of the blind kernel equals $2^3 - 4 = 4$ (the three pairwise characters $w_{110}, w_{101}, w_{011}$ and the triple parity character $w_{111}(x) = (-1)^{x_1 + x_2 + x_3}$, corresponding to the charge $\kappa = x_1 \oplus x_2 \oplus x_3$).

**Proof.**  
Since the family $\{w_S\}_{S \in \{0,1\}^n}$ forms a basis of the $2^n$-dimensional space $K^{D^n}$, and the first $n+1$ characters ($S = \varnothing$ and the singletons $S = \{i\}$) span the image $\operatorname{Im}\Pi_{\le 1} = W_{\le 1}$ of dimension $n+1$, the orthogonal complement $\ker \Pi_{\le 1} = W_{\le 1}^\perp$ is linearly spanned by the remaining $2^n - (n+1)$ characters $\{w_S : |S| \ge 2\}$. For $n=2$, the unique such character is $w_{11}(x_1, x_2) = (-1)^{x_1+x_2}$, while for $n=3$ there are exactly $\binom{3}{2} + \binom{3}{3} = 3 + 1 = 4$ of them. $\blacksquare$

This proposition translates the combinatorial phenomenon of `Chapter I.9` into the language of linear algebra: **why is the triple parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ invisible to all one-bit and two-bit marginals?** Because the corresponding character $w_{111}(x_0, c_0, b_0) = (-1)^{x_0 + c_0 + b_0}$ lies in the top layer $W_3$ and is orthogonal to the entire subspace $W_0 \oplus W_1 \oplus W_2$. For a linear instrument to detect the mode $w_{111}$, it requires a question of degree $3$ encompassing all three axes simultaneously.

---

## §II.1.5. Quadratic Neighborhood Energy on the Memory Window and Symmetry Reduction $\mathfrak{S}_n \to D_n$

When the observer records in a window of length $n$ a vector of consecutive samples $\zeta = (\zeta_1, \zeta_2, \dots, \zeta_n)^{\mathsf{T}} \in \mathbb{R}^n$, the ordering of the coordinates $\zeta_1, \zeta_2, \dots, \zeta_n$ carries the arrow of the discrete step $t \mapsto t+1$. If we evaluated the vector $\zeta$ solely by its Euclidean norm
$$
\|\zeta\|_2^2 = \sum_{i=1}^n \zeta_i^2,
$$
then any permutation of samples $\pi \in \mathfrak{S}_n$ would preserve this measure: the Euclidean norm is completely blind to which samples stood next to each other in time.

As soon as coupling between adjacent time steps (a difference gradient along a chain or a cyclic window) is included in the quality or energy functional of memory, the group of admissible permutation symmetries shrinks sharply.

> **Proposition II.1.2 (Reduction of the coordinate permutation group under preservation of nearest-neighbor step energy).**  
> *Classical foundation.* Permutation representations of the symmetric group $\mathfrak{S}_n$ and automorphism groups of path and cycle graphs. *Contribution of this book:* Symmetry reduction from full channel permutations $\mathfrak{S}_n$ to the dihedral or reflection subgroup once a nearest-neighbor quadratic step-energy functional is imposed.
> Suppose two quadratic neighborhood forms are given on the window space $\mathbb{R}^n$ ($n \ge 4$):
> 1. The *open path neighborhood form*
>    $$
>    Q_{\mathrm{path}}(\zeta) = \sum_{i=1}^{n-1} \zeta_i \zeta_{i+1} = \frac{1}{2}\,\zeta^{\mathsf{T}} A_{P_n} \zeta,
>    $$
>    where $A_{P_n}$ is the adjacency matrix of the simple path $P_n$ on the vertices $\{1, \dots, n\}$.
> 2. The *cyclic neighborhood form*
>    $$
>    Q_{\mathrm{cycle}}(\zeta) = \sum_{i=1}^{n} \zeta_i \zeta_{i+1 \pmod n} = \frac{1}{2}\,\zeta^{\mathsf{T}} A_{C_n} \zeta,
>    $$
>    where $A_{C_n}$ is the adjacency matrix of the simple cycle $C_n$.
>
> Then:
> - a coordinate permutation $\pi \in \mathfrak{S}_n$ preserves the form $Q_{\mathrm{path}}(P_\pi \zeta) = Q_{\mathrm{path}}(\zeta)$ **for all vectors $\zeta \in \mathbb{R}^n$** if and only if $\pi$ is either the identity permutation $\mathrm{id}$ or the full time reversal $\rho(i) = n + 1 - i$ (the group $\mathrm{Aut}(P_n) \cong C_2$ of order $2$);
> - a coordinate permutation $\pi \in \mathfrak{S}_n$ preserves the form $Q_{\mathrm{cycle}}(P_\pi \zeta) = Q_{\mathrm{cycle}}(\zeta)$ **for all vectors $\zeta \in \mathbb{R}^n$** if and only if $\pi$ belongs to the dihedral group $D_n = \mathrm{Aut}(C_n)$ of order $2n$, generated by the cyclic shift $i \mapsto i + 1 \pmod n$ and the reflection $i \mapsto n + 1 - i$.

**Proof.**  
Since the matrix $A$ is symmetric, equality of the quadratic forms $\zeta^{\mathsf{T}} P_\pi^{\mathsf{T}} A P_\pi \zeta = \zeta^{\mathsf{T}} A \zeta$ for all vectors $\zeta \in \mathbb{R}^n$ is, by the polarization identity
$$
A_{ij} = \frac{1}{2}\bigl(Q(e_i + e_j) - Q(e_i) - Q(e_j)\bigr),
$$
equivalent to the matrix equality $P_\pi^{\mathsf{T}} A P_\pi = A$, i.e., to the condition that the permutation $\pi \in \mathfrak{S}_n$ is an automorphism of the graph with adjacency matrix $A$.
- For the simple path $P_n$, only the two endpoint vertices $\{1, n\}$ have degree $1$, while all internal vertices have degree $2$. Any automorphism of the graph $P_n$ must map the set of endpoints $\{1, n\}$ to itself and preserve distances along the path, leaving exactly two maps: $\pi(i) = i$ and $\pi(i) = n + 1 - i$.
- For the simple cycle $C_n$ ($n \ge 4$), the image of vertex $1$ can be chosen in $n$ ways, and the image of its neighbor $2$ in exactly two ways (the two neighbors of $\pi(1)$ on the cycle), after which the entire traversal of the cycle is uniquely determined. This yields precisely the dihedral group $D_n$ consisting of $n$ cyclic shifts and $n$ reflections. $\blacksquare$

> **Remark II.1.2 (Why the clause "for all vectors $\zeta \in \mathbb{R}^n$" is essential).**  
> On an individual special vector $\zeta$ (for instance, on a constant vector $\zeta = (c, c, \dots, c)^{\mathsf{T}}$), the value $Q_{\mathrm{path}}(\zeta) = (n-1)c^2$ does not change under any permutation $\pi \in \mathfrak{S}_n$ whatsoever. It is precisely the requirement of invariance of the quadratic sensor across the **entire** space of input windows $\mathbb{R}^n$ that turns the algebraic identity of forms into a geometric automorphism of the memory connectivity graph.

---

## §II.1.6. Historical-Philosophical Parallel: The Inertia of the Potter's Wheel (`SK 67`) and the Free Memory Response $C B^t h_0$

In Īśvarakṛṣṇa's classical *Sāṃkhyakārikā* (`SK 67`), the famous image of the potter's wheel is given: even after the potter has withdrawn their hand and ceased to push the wheel (*uparatā*), the wheel continues to spin for some time by the force of the previously accumulated impulse (*saṃskāra-vaśāt cakra-bhrama-vad dhṛta-śarīraḥ*).

In the operator equation of the linear observer (`Definition II.1.1`),
$$
y_t = \underbrace{C B^t h_0}_{\substack{\text{free response of}\\ \text{accumulated memory } h_0}} + \underbrace{\sum_{k=0}^{t-1} C B^{t-1-k} A u_k}_{\substack{\text{forced response to}\\ \text{current inputs } u_0, \dots, u_{t-1}}},
$$
this image receives a transparent structural correspondence (which does not enter into the hypotheses of the mathematical theorems):
- applying external inputs $u_k$ through the write operator $A$ corresponds to actively driving the wheel;
- the moment when external driving ceases ($u_t = 0$ for $t \ge t_0$) switches off the second sum, but does not instantaneously annihilate the observed output $y_t$, provided the vector of accumulated internal state $h_{t_0}$ does not lie in the invisible kernel $\ker \mathcal{O}$;
- the decaying or periodic continuation $y_t = C B^{t-t_0} h_{t_0}$ over the horizon $t \ge t_0$ is governed exclusively by the spectrum of the internal step operator $B$ on the minimal memory space $V_{\min}$ of dimension $\operatorname{rank}\mathcal{H}$.

---

## §II.1.7. Chapter Summary and Bridge to Chapter II.2

The table below compares the constructions of Book I with their linear operator continuations.

#### Table II.1.2. Translation of the Finite Memory Automaton of Book I into the Language of Linear Operators of Chapter II.1

| Construction of Book I (`Chapters I.2, I.3, I.8`) | Linear enrichment in `Chapter II.1` | Main theorem / formula |
| :--- | :--- | :--- |
| Instantaneous indistinguishability fiber $q^{-1}(y)$ | Kernel of the instantaneous reading operator $\ker C \subseteq V$ | $y_0^{(1)} = y_0^{(2)} \iff h_0^{(1)} - h_0^{(2)} \in \ker C$ |
| Pullback of a question along an action $q \circ T_a$ | Shifted reading row $C B^t$ at step $t$ | What is invisible in $C$ becomes visible in $C B^t$ |
| Nerode history indistinguishability relation $\sim_\Gamma$ | Full observability kernel $\ker \mathcal{O} = \bigcap_{i=0}^{d-1} \ker(C B^i)$ | Stabilization of the kernel chain at $N = d$ (`Theorem II.1.1`) |
| Reachable set of the automaton from the initial state | Image of the reachability operator $\operatorname{Im} \mathcal{R} = \operatorname{Im}\mathcal{R}_d$ | Dual stabilization by Cayley–Hamilton |
| Minimal quotient automaton $X / {\sim_\Gamma}$ | Minimal Ho–Kalman realization $V_{\min} = \operatorname{Im}\mathcal{R} / (\operatorname{Im}\mathcal{R} \cap \ker \mathcal{O})$ | $\dim_K V_{\min} = \operatorname{rank} \mathcal{H}$ (`Theorem II.1.2`) |
| Triple parity charge $\kappa = x_0 \oplus c_0 \oplus b_0$ | Top Walsh character $w_{111} \in \ker \Pi_{\le 1} \cap \ker \Pi_{\le 2}$ | Defect $\dim_K \ker \Pi_{\le 1} = 2^n - (n+1)$ (`Prop. II.1.1`) |

In `Chapter II.1`, the time step $t \in \mathbb{N}$ remained a discrete counting tick. Yet in control theory, analysis, and differential geometry, the observer constantly passes from discrete steps $h_t \mapsto h_{t+1}$ to continuous time and infinitesimal generators $\dot{h} = J h$. How can one construct this transition without attributing actual infinite precision to a finite instrument and without losing algebraic control over the step error? This is the subject of **Chapter `II.2`**.

---

## Summary Passport of Chapter II.1 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `§II.1.1–II.1.2` | Traversal of the four-point scene $S_4$: Hankel ranks $1, 2, 3, 4$ and explicit minimal Ho–Kalman realization | `GATE-II01-01` |
| `Theorem II.1.1` | Stabilization $\ker \mathcal{O}_d = \ker \mathcal{O}$ and perturbation recovery of $W_0$ on the window $0 \le t \le j_0 + r_0 - 1$ at shift threshold $j_0$ | `GATE-II01-02` |
| `Theorem II.1.2` | Skeleton assembly of the minimal Ho–Kalman realization $(A_{\min}, B_{\min}, C_{\min})$ (scalar and multivariable $p=m=2$ cases) and verification of $C_{\min} B_{\min}^t A_{\min} = M_t$ | `GATE-II01-03` |
| `Proposition II.1.1` | Orthogonality of Walsh characters on $D^n$, defect $2^n - (n+1)$, and vanishing $\Pi_{\le 1}(w_{111}) = 0$ | `GATE-II01-04` |
| `Proposition II.1.2` | Exhaustive enumeration of $\mathfrak{S}_n$: stabilizer of $Q_{\mathrm{path}}$ of order $2$ ($\cong C_2$) and stabilizer of $Q_{\mathrm{cycle}}$ of order $2n$ ($\cong D_n$) | `GATE-II01-05` |
