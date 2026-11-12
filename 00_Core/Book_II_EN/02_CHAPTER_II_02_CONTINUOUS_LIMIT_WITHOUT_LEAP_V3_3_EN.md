# Chapter II.2. Continuous Continuation Without a Leap: Dyadic Gluing, Jets, the Cayley Transform, and Dual Numbers

In `Chapter II.1`, we established how a linear observer recovers the hidden memory space $V_{\min}$ of dimension $\operatorname{rank}\mathcal{H}$ from a discrete sequence of responses $(y_0, y_1, y_2, \dots)$. At each individual step, however, the instrument of Book I and `Chapter II.1` still outputs only a finite number of digits at discrete time ticks $t = 0, 1, 2, \dots$. In classical analysis and its applications, it is customary at this point to make a tacit leap: to assume that the measured quantity is "in reality" given from the outset by a real number $x \in \mathbb{R}$ with an infinite tail of digits, and that time flows continuously along a smooth curve $\gamma(t)$ with derivative $\dot{\gamma}(t) = J \gamma(t)$.

For a metatheory of the observer, such an unconditional leap is inadmissible. A genuine operational contract $\Gamma$ never hands the observer an actually infinite tape of digits all at once: it provides only a **coherent tower of finite precision windows** $m = 1, 2, 3, \dots$ together with a recalculation rule as the step is refined ($h \to 0$). Therefore, the second question of this volume reads:

> **How do a continuous continuum, smooth jets, and the derivative rigorously emerge from a coherent tower of finite discrete windows of the observer—and what exactly does the observer glue together or lose in this transition?**

The present chapter answers this question in four steps, nowhere resorting to uncontrolled limit leaps:
1. first, we connect the infinite sequence of Markov parameters $M_t = C B^t A$ from `Chapter II.1` to the rational transfer function via the formal $Z$-transform and show how the reciprocal substitution $z \leftrightarrow 1/z$ links the characteristic polynomial of the step operator $B$ to the denominator of the rational series of `Chapter I.8`;
2. second, on the tower of finite binary windows $\mathbb{Z}/2^m\mathbb{Z}$, we construct the projective limit of $2$-adic integers $\mathbb{Z}_2 = \varprojlim \mathbb{Z}/2^m\mathbb{Z}$ and the continuous dyadic map $\Phi : \mathbb{Z}_2 \to \mathbb{R}/\mathbb{Z}$: here we uncover the **first non-trivial gluing of indistinguishable histories** ($0.0111\ldots_2 = 0.1000\ldots_2 = 1/2$), where two completely distinct infinite branches of the binary question tree merge into a single real point on the dial;
3. next, on truncated jet spaces $J^m_0 = K[x]/(x^{m+1})$, we compare the true shift exponential $\exp(h J_a)$ with the explicit Euler method and with the symmetric Cayley–Padé transform $(I - \frac{h}{2}J_a)^{-1}(I + \frac{h}{2}J_a)$, proving exact algebraic agreement of the quadratic jet and computing the cubic remainder $-\frac{1}{12} h^3 J_a^3$;
4. finally, using the ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$, we give a purely algebraic definition of a tangent vector and first-order derivative, valid over any commutative ring or field $K$ without passing to the limit $\lim_{h \to 0}$.

---

## §II.2.1. Bridge from Chapter II.1: The Formal $Z$-Transform and Variable Duality $z \leftrightarrow 1/z$

In `Chapter I.8` (`Theorem I.8.3`), an infinite sequence $(s_0, s_1, s_2, \dots)$ was folded into a formal power series $S(w) = \sum_{t=0}^\infty s_t w^t \in K[[w]]$, whose rationality $S(w) = P(w)/Q(w)$ proved equivalent to the finiteness of the Hankel rank $\operatorname{rank}\mathcal{H}_s < \infty$. In the operator theory of linear systems (`Chapter II.1`), by contrast, the transfer function is customarily written in descending powers of the spectral variable $z$, so that multiplication by $z$ corresponds to a forward shift by one time step ($h_{t+1} = z h_t$). Let us show how these two conventions translate into each other under the reciprocal change of variables $w = 1/z$.

> **Lemma II.2.1 (Resolvent identity, formal $Z$-transform, and alignment of $w = 1/z$ with Book I).**  
> *Classical foundation.* Formal resolvent identity $(I - wA)^{-1} = \sum_{k \ge 0} w^k A^k$ in formal power series $K[[w]]$ and the unilateral $Z$-transform of linear systems. *Contribution of this book:* Unconditional algebraic alignment of the delay indeterminate $w = 1/z$ with the Hankel windows of Book I, separated explicitly from the analytic convergence disk $|z| > \rho(A)$.
> Let $(A, B, C)$ be a linear realization of dimension $d$ over a field $K$ with Markov parameters $M_t = C B^t A$ ($t \ge 0$), and let $\chi_B(z) = \det(z I_d - B) = z^d + c_{d-1} z^{d-1} + \cdots + c_0 \in K[z]$ be the characteristic polynomial of the step operator $B$.
> 1. In the ring of formal power series in the variable $w = 1/z$, the generating series of the Markov parameters coincides with the operator resolvent:
>    $$
>    \mathcal{M}(w) = \sum_{t=0}^\infty M_t w^t = C (I_d - w B)^{-1} A \in \mathrm{Hom}_K(U, Y)[[w]].
>    $$
> 2. In the spectral variable $z = 1/w$, the formal $Z$-transform of the impulse response takes the rational form
>    $$
>    H(z) = \sum_{t=0}^\infty M_t z^{-t-1} = w\,\mathcal{M}(w)\Big|_{w = 1/z} = C (z I_d - B)^{-1} A = \frac{1}{\chi_B(z)}\, C\,\mathrm{adj}(z I_d - B)\, A,
>    $$
>    where $\mathrm{adj}(z I_d - B)$ is the adjugate (classical adjoint) matrix of polynomials of degree $\le d-1$.
> 3. The reciprocal denominator polynomial in `Theorem I.8.3` of Book I is obtained from the characteristic polynomial $\chi_B(z)$ by reversing the order of coefficients under the substitution $z = 1/w$:
>    $$
>    \widetilde{\chi}_B(w) = w^d \chi_B(1/w) = \det(I_d - w B) = 1 + c_{d-1} w + \cdots + c_0 w^d,
>    $$
>    and its constant term equals $\widetilde{\chi}_B(0) = 1$, which guarantees the invertibility of $\widetilde{\chi}_B(w)$ in the ring of formal power series $K[[w]]$ regardless of whether the operator $B$ itself is invertible.

**Proof.**  
In the ring of formal matrix power series $K^{d \times d}[[w]]$, the element $I_d - w B$ has the geometric inverse series $\sum_{t=0}^\infty w^t B^t$, since $(I_d - w B)\sum_{t=0}^\infty w^t B^t = I_d$. Multiplying this identity on the left by $C$ and on the right by $A$ yields item 1. Substituting $w = z^{-1}$ and factoring $z^{-1}$ out of $(I_d - z^{-1} B)^{-1} = z(z I_d - B)^{-1}$ gives the formula of item 2, and Cramer's classical identity $(z I_d - B)\,\mathrm{adj}(z I_d - B) = \chi_B(z) I_d$ expresses $H(z)$ as a strictly proper rational fraction with denominator $\chi_B(z)$. Finally, $\det(I_d - w B) = w^d \det(w^{-1} I_d - B) = w^d \chi_B(w^{-1})$ yields the reciprocal polynomial $\widetilde{\chi}_B(w)$ with $\widetilde{\chi}_B(0) = \det I_d = 1$. $\blacksquare$

This lemma explains why in `Chapter I.8` we could work with non-invertible (including nilpotent) memory shifts: the transformation $z \leftrightarrow 1/z$ moves the singularity $z = 0$ of a non-invertible operator $B$ to the point at infinity $w = \infty$, leaving the origin $w = 0$ completely regular.

---

## §II.2.2. The Tower of Finite Binary Windows $\mathbb{Z}/2^m\mathbb{Z}$, the $2$-adic Limit $\mathbb{Z}_2$, and the First Gluing of Indistinguishables in $\mathbb{R}/\mathbb{Z}$

Let us now examine how the transition from a finite number of questions to infinite refinement is structured on the simplest numerical carrier of Book I—binary residues.

In `Chapter I.8`, the oracle-free observer investigated a number through a coherent tower of modular windows:
$$
\cdots \longrightarrow \mathbb{Z}/2^{m+1}\mathbb{Z} \xrightarrow{\;\pi_{m+1,m}\;} \mathbb{Z}/2^m\mathbb{Z} \longrightarrow \cdots \longrightarrow \mathbb{Z}/4\mathbb{Z} \xrightarrow{\;\pi_{2,1}\;} \mathbb{Z}/2\mathbb{Z},
$$
where the projection $\pi_{m+1,m}(x \bmod 2^{m+1}) = x \bmod 2^m$ simply forgets the most significant $(m+1)$-st binary digit while retaining the lowest $m$ bits. At level $m = 2$ ($\mathbb{Z}/4\mathbb{Z} = \{0,1,2,3\}$), this tower passes directly through the four-point scene $S_4$ (with bits $(b_0, b_1) \in \{0,1\}^2$, where $x \equiv b_0 + 2 b_1 \pmod 4$).

If the observer asks an infinite sequence of coherent questions $b_0, b_1, b_2, \dots \in \{0,1\}$, they determine an element of the projective limit—the ring of $2$-adic integers:
$$
\mathbb{Z}_2 = \varprojlim_{m \ge 1} \mathbb{Z}/2^m\mathbb{Z} = \left\{ (x_m)_{m \ge 1} \in \prod_{m=1}^\infty \mathbb{Z}/2^m\mathbb{Z} \;\middle|\; \pi_{m+1,m}(x_{m+1}) = x_m \;\forall m \ge 1 \right\}.
$$
Every element $x \in \mathbb{Z}_2$ is uniquely written as a formal binary series
$$
x = \sum_{k=0}^\infty b_k 2^k, \qquad b_k \in \{0,1\},
$$
whose $m$-th finite window is simply the partial sum of the lowest $m$ digits:
$$
x_m = \sum_{k=0}^{m-1} b_k 2^k \in \{0, 1, \dots, 2^m - 1\} \cong \mathbb{Z}/2^m\mathbb{Z}.
$$
Two $2$-adic states $x, y \in \mathbb{Z}_2$ are closer in the $2$-adic metric $|x - y|_2 = 2^{-\nu_2(x-y)}$ the longer they yield **identical answers across all finite windows** $x_1 = y_1, \dots, x_m = y_m$. The space $\mathbb{Z}_2$ is totally disconnected (homeomorphic to the Cantor discontinuum $\{0,1\}^{\mathbb{N}}$): it contains no continuous path between distinct points, because changing even a single bit $b_k$ permanently separates the branches of the question tree starting from depth $m = k + 1$.

How, then, does a connected continuous instrument dial—the interval $[0,1]$ or the phase circle $\mathbb{R}/\mathbb{Z}$—arise from this totally disconnected tree of answers?

At each finite level $m \ge 1$, define the *dyadic scaling reading* $\Phi_m : \mathbb{Z}/2^m\mathbb{Z} \to [0,1) \subset \mathbb{R}$, which maps the $m$-bit code $x_m = \sum_{k=0}^{m-1} b_k 2^k$ to a binary fraction with reversed weight order:
$$
\Phi_m(x_m) = \sum_{k=0}^{m-1} \frac{b_k}{2^{k+1}} = 0.b_0 b_1 \dots b_{m-1}\,_2 \in \left\{ 0, \frac{1}{2^m}, \frac{2}{2^m}, \dots, \frac{2^m - 1}{2^m} \right\}.
$$
When the next digit $b_m \in \{0,1\}$ is adjoined, the dial reading changes by at most $2^{-(m+1)}$:
$$
\bigl|\Phi_{m+1}(x_{m+1}) - \Phi_m(x_m)\bigr| = \frac{b_m}{2^{m+1}} \le \frac{1}{2^{m+1}}.
$$
Therefore, as $m \to \infty$, the sequence of finite readings $\Phi_m(x_m)$ converges uniformly in the standard real metric along every path of the tree $\mathbb{Z}_2$ and defines the limit map
$$
\Phi : \mathbb{Z}_2 \longrightarrow [0,1], \qquad \Phi\left(\sum_{k=0}^\infty b_k 2^k\right) = \sum_{k=0}^\infty \frac{b_k}{2^{k+1}},
$$
which, upon identifying the endpoints $0 \sim 1$, gives a continuous surjective map $\bar{\Phi} : \mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$.

From the construction it follows that **the map $\Phi$ is surjective, but not injective.**

> **Proposition II.2.1 (Dyadic gluing of indistinguishable tails in the transition $\mathbb{Z}_2 \to \mathbb{R}/\mathbb{Z}$).**  
> *Classical foundation.* Binary expansions on the circle $\mathbb{R}/\mathbb{Z}$ and the compact totally disconnected ring of $2$-adic integers $\mathbb{Z}_2$. *Contribution of this book:* Operational reading of the continuous surjection $\bar{\Phi} : \mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$ as gluing indistinguishable binary tails ($0.0111\ldots_2 = 0.1000\ldots_2$), together with a proof that $\bar{\Phi}$ is not an additive group homomorphism.
> 1. At each finite level $m \ge 1$, the map $\Phi_m : \mathbb{Z}/2^m\mathbb{Z} \to [0,1)$ is strictly injective (distinct $m$-bit answers yield distinct dial points separated by distance $\ge 2^{-m}$).
> 2. In the limit $m \to \infty$, the map $\Phi : \mathbb{Z}_2 \to [0,1]$ glues into one and the same dyadic rational point $r = \frac{2a+1}{2^{k+1}} \in (0,1)$ two completely distinct infinite answer histories $x^{(-)}, x^{(+)} \in \mathbb{Z}_2$ that diverge in the $(k+1)$-st window and in all subsequent windows $m > k$:
>    $$
>    \begin{aligned}
>    b^{(-)} &= (b_0, \dots, b_{k-1}, \,0,\, 1, 1, 1, 1, \dots), \\
>    b^{(+)} &= (b_0, \dots, b_{k-1}, \,1,\, 0, 0, 0, 0, \dots),
>    \end{aligned}
>    \qquad \Phi\bigl(x^{(-)}\bigr) = \Phi\bigl(x^{(+)}\bigr) = \sum_{j=0}^{k-1} \frac{b_j}{2^{j+1}} + \frac{1}{2^{k+1}}.
>    $$
>    In particular, for $k = 0$, the two opposite infinite branches
>    $$
>    x^{(-)} = \sum_{j=1}^\infty 2^j = -2 \in \mathbb{Z}_2 \quad (\text{code } 0.01111\ldots_2)
>    \qquad \text{and} \qquad
>    x^{(+)} = 1 \in \mathbb{Z}_2 \quad (\text{code } 0.10000\ldots_2),
>    $$
>    which lie at the maximum $2$-adic distance $|x^{(+)} - x^{(-)}|_2 = |3|_2 = 1$ in $\mathbb{Z}_2$, approach each other on the real dial at rate $|\Phi_m(x^{(+)}_m) - \Phi_m(x^{(-)}_m)| = 2^{-m} \to 0$ and are glued into the single midpoint $\Phi(x^{(-)}) = \Phi(x^{(+)}) = 1/2$.
> 3. At the same time, the continuous topological quotient map $\bar{\Phi} : \mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$ **is not an additive group homomorphism**: for example, $\bar{\Phi}(1) + \bar{\Phi}(1) = \frac{1}{2} + \frac{1}{2} \equiv 0 \pmod 1$, whereas $\bar{\Phi}(1 + 1) = \bar{\Phi}(2) = \frac{1}{4} \not\equiv 0 \pmod 1$, because carry propagation under addition in $\mathbb{Z}_2$ runs toward higher powers $2^{k+1}$ (deeper into future windows), whereas in the binary fraction $[0,1]$ it runs toward coarser powers $2^{-(k-1)}$.

**Proof.**  
At a finite level $m > k$, the difference between the dial readings for the histories $b^{(+)}$ and $b^{(-)}$ equals
$$
\Phi_m\bigl(x^{(+)}_m\bigr) - \Phi_m\bigl(x^{(-)}_m\bigr) = \frac{1}{2^{k+1}} - \sum_{j=k+1}^{m-1} \frac{1}{2^{j+1}} = \frac{1}{2^m} > 0.
$$
In the discrete topology of a finite window and in the $2$-adic metric, these two sequences never approach each other: $x^{(+)}_m \ne x^{(-)}_m$ for all $m \ge k+1$. In the Archimedean metric of the dial $[0,1]$, however, the gap between them equals $2^{-m}$, which eventually falls below the sensitivity threshold of any finite real instrument as $m \to \infty$. The quotient space of the totally disconnected compact space $\mathbb{Z}_2$ by the equivalence relation $x \sim_\Phi y \iff \bar{\Phi}(x) = \bar{\Phi}(y)$ (which glues the countable family of dyadic gaps together with the endpoints $-1 \sim 0$) is homeomorphic to the connected circle $\mathbb{R}/\mathbb{Z}$. For $x = 1 = 1\cdot 2^0$ one has $\bar{\Phi}(1) = 1/2$, while for $1 + 1 = 2 = 0\cdot 2^0 + 1\cdot 2^1$ one has $\bar{\Phi}(2) = 1/4 \ne 0 \equiv \bar{\Phi}(1) + \bar{\Phi}(1) \pmod 1$, proving item 3. $\blacksquare$

This proposition gives a precise operational answer to the question concerning the nature of the continuum: **the connected real continuum $[0,1]$ arises from the tree of discrete binary questions $\mathbb{Z}_2$ not by adding mystical "inter-point matter," but by quotient-gluing pairs of boundary histories $0111\ldots \sim 1000\ldots$ that the Archimedean metric of the dial ceases to distinguish.**

---

## §II.2.3. Infinitesimal Shift in Jet Space and the Second-Order Cayley–Padé Transform

Let us pass from a static dial to continuous motion in time. Suppose the observer studies smooth or polynomial functions in a neighborhood of the origin $x = 0$, retaining in memory only their derivatives up to order $m$ inclusive. Algebraically, this means passing to the quotient ring of truncated polynomials (*the space of $m$-jets*):
$$
J^m_0 = K[x] / (x^{m+1}) \cong \operatorname{span}_K \{ 1, x, x^2, \dots, x^m \}, \qquad \dim_K J^m_0 = m + 1,
$$
where $K$ is a field of characteristic $0$ (for example, $K = \mathbb{Q}$ or $K = \mathbb{R}$).

On the jet space $J^m_0$, the differentiation operator $J_a = a \frac{d}{dx}$ ($a \in K$) acts nilpotently:
$$
J_a(x^k) = k a x^{k-1} \quad (1 \le k \le m), \qquad J_a(1) = 0, \qquad J_a^{m+1} = 0.
$$
By virtue of the nilpotency $J_a^{m+1} = 0$, the shift exponential by a step $h \in K$ is in $J^m_0$ a **finite polynomial sum**, free of any questions regarding the convergence of an infinite series:
$$
E(h) = \exp(h J_a) = \sum_{k=0}^m \frac{h^k}{k!}\, J_a^k, \qquad \bigl(E(h) f\bigr)(x) = f(x + a h) \pmod{x^{m+1}}.
$$
Moreover, for any operator $J_a$ nilpotent on $J^m_0$ ($J_a^{m+1} = 0$), the operator $I - \frac{h}{2} J_a$ is **unipotent** and therefore strictly invertible for every $h \in K$: its inverse operator is given by the finite geometric sum
$$
\left(I - \frac{h}{2} J_a\right)^{-1} = \sum_{k=0}^m \left(\frac{h}{2}\right)^k J_a^k
$$
(while in a normed space of bounded operators, the invertibility condition for $I \pm \frac{h}{2} J_a$ holds whenever the step is sufficiently small, $\|h J_a\| < 2$, or whenever a skew-Hermitian generator $J_a^* = -J_a$ has purely imaginary spectrum).

Let us now compare the accuracy in powers of the step $h$ with which various one-step approximations reproduce the true shift $E(h) = \exp(h J_a)$.

> **Theorem II.2.1 (Cayley–Padé transform, quadratic jet matching, and the exact cubic defect $-\frac{1}{12}h^3 J_a^3$).**  
> *Classical foundation.* Cayley's rational transform $(I - \frac{h}{2}J_a)^{-1}(I + \frac{h}{2}J_a)$ (Cayley, 1846) and the $[1/1]$ diagonal Padé approximant to the matrix exponential $\exp(h J_a)$. *Contribution of this book:* Exact second-order jet agreement of the reversible rational step with $\exp(h J_a)$ without transcendental series, plus the exact cubic remainder coefficient $+\frac{1}{12}h^3 J_a^3$.
> Suppose three one-step transfer operators by step $h$ act on the jet space $J^m_0$ ($m \ge 3$):
> - the *true exponential shift* $E(h) = \exp(h J_a) = I + h J_a + \frac{h^2}{2} J_a^2 + \frac{h^3}{6} J_a^3 + \cdots$;
> - the *first-order explicit Euler step* $T_{\mathrm{Euler}}(h) = I + h J_a$;
> - the *symmetric Cayley step (diagonal Padé $[1/1]$ approximation)*
>   $$
>   T_{\mathrm{Cayley}}(h) = \left(I + \frac{h}{2} J_a\right)\left(I - \frac{h}{2} J_a\right)^{-1} = \left(I - \frac{h}{2} J_a\right)^{-1}\left(I + \frac{h}{2} J_a\right).
>   $$
> Then:
> 1. The explicit Euler step agrees with $E(h)$ only to first order and has the quadratic jet defect
>    $$
>    E(h) - T_{\mathrm{Euler}}(h) = \frac{h^2}{2} J_a^2 + \frac{h^3}{6} J_a^3 + O(h^4),
>    $$
>    and fails to satisfy the group time-reversal rule: $T_{\mathrm{Euler}}(h)\,T_{\mathrm{Euler}}(-h) = I - h^2 J_a^2 \ne I$.
> 2. The Cayley step is exactly reversible under sign reversal of the step:
>    $$
>    T_{\mathrm{Cayley}}(h)\,T_{\mathrm{Cayley}}(-h) = I,
>    $$
>    maps skew-symmetric generators ($J_a^{\mathsf{T}} = -J_a$) to orthogonal operators preserving the Euclidean norm, coincides with the true exponential $E(h)$ up to and including the quadratic term $h^2$, and has an exact leading cubic defect with rational coefficient $-1/12$:
>    $$
>    T_{\mathrm{Cayley}}(h) - E(h) = \left(\frac{1}{4} - \frac{1}{6}\right) h^3 J_a^3 + O(h^4) = \frac{1}{12} h^3 J_a^3 + O(h^4),
>    $$
>    that is,
>    $$
>    E(h) - T_{\mathrm{Cayley}}(h) = -\frac{1}{12} h^3 J_a^3 + O(h^4).
>    $$

**Proof.**  
Expanding the inverse operator $(I - \frac{h}{2} J_a)^{-1} = I + \frac{h}{2} J_a + \frac{h^2}{4} J_a^2 + \frac{h^3}{8} J_a^3 + O(h^4)$ and multiplying it by $I + \frac{h}{2} J_a$, we obtain the exact expansion of the Cayley step in powers of $h J_a$:
$$
\begin{aligned}
T_{\mathrm{Cayley}}(h) &= \left(I + \frac{h}{2} J_a\right)\left(I + \frac{h}{2} J_a + \frac{h^2}{4} J_a^2 + \frac{h^3}{8} J_a^3 + O(h^4)\right) \\
&= I + \left(\frac{1}{2} + \frac{1}{2}\right) h J_a + \left(\frac{1}{4} + \frac{1}{4}\right) h^2 J_a^2 + \left(\frac{1}{8} + \frac{1}{8}\right) h^3 J_a^3 + O(h^4) \\
&= I + h J_a + \frac{1}{2} h^2 J_a^2 + \frac{1}{4} h^3 J_a^3 + O(h^4).
\end{aligned}
$$
Subtracting the Taylor series of the exponential $E(h) = I + h J_a + \frac{1}{2} h^2 J_a^2 + \frac{1}{6} h^3 J_a^3 + O(h^4)$, we see that the terms of orders $h^0, h^1, h^2$ vanish identically, while at $h^3 J_a^3$ the remaining coefficient is
$$
\frac{1}{6} - \frac{1}{4} = -\frac{1}{12}.
$$
Reversibility under sign change $h \mapsto -h$ follows from the commutativity of the factors $(I + \frac{h}{2}J_a)$ and $(I - \frac{h}{2}J_a)^{-1}$:
$$
T_{\mathrm{Cayley}}(h)\,T_{\mathrm{Cayley}}(-h) = (I + \tfrac{h}{2}J_a)(I - \tfrac{h}{2}J_a)^{-1}(I - \tfrac{h}{2}J_a)(I + \tfrac{h}{2}J_a)^{-1} = I. \quad \blacksquare
$$

Let us see how the same cubic structure manifests itself in a smooth nonlinear reading—the logistic (sigmoid) instrument scale $\sigma(z) = (1 + e^{-z})^{-1}$.

> **Lemma II.2.2 (Odd symmetry of the centered sigmoid and saturation threshold).**  
> *Classical foundation.* Odd symmetry of the centered logistic function $\sigma(u) - \frac{1}{2} = \frac{1}{2}\tanh(u/2)$ and its power-series expansion around zero. *Contribution of this book:* Explicit unsaturated linear readout window around the threshold contrasted with tail collapse under clipping and scale saturation.
> Let a linear reading functional $L : V \to \mathbb{R}$ be given on the state space $V = \mathbb{R}^d$, and set $z = L(x) \in \mathbb{R}$. Consider the centered smooth response scale
> $$
> \widetilde{\sigma}(z) = \sigma(z) - \frac{1}{2} = \frac{1}{1 + e^{-z}} - \frac{1}{2} = \frac{1}{2}\tanh\left(\frac{z}{2}\right).
> $$
> Then the function $\widetilde{\sigma}(z)$ is strictly odd ($\widetilde{\sigma}(-z) = -\widetilde{\sigma}(z)$), its even derivatives vanish at the origin $z = 0$, and its Taylor expansion up to fifth order has exact rational coefficients:
> $$
> \widetilde{\sigma}(z) = \frac{1}{4} z - \frac{1}{48} z^3 + \frac{1}{480} z^5 - O(z^7), \qquad z = L(x).
> $$
> Consequently, near zero ($|z| \ll 1$), the nonlinear instrument agrees to first order with the linear question $\frac{1}{4} L(x)$ with relative cubic compression $-\frac{1}{12} z^2$ (since $-\frac{1/48}{1/4} = -\frac{1}{12}$), whereas at large deviations ($|z| \to \infty$) the response saturates at $\widetilde{\sigma}(z) \to \pm \frac{1}{2}$, losing sensitivity to further growth of $z = L(x)$.

**Proof.**  
The identity $\frac{1}{1+e^{-z}} - \frac{1}{2} = \frac{e^{z/2} - e^{-z/2}}{2(e^{z/2} + e^{-z/2})} = \frac{1}{2}\tanh(z/2)$ is verified by bringing to a common denominator. From the classical expansion $\tanh u = u - \frac{1}{3} u^3 + \frac{2}{15} u^5 - \cdots$, substituting $u = z/2$ yields
$$
\widetilde{\sigma}(z) = \frac{1}{2}\left(\frac{z}{2} - \frac{1}{3}\frac{z^3}{8} + \frac{2}{15}\frac{z^5}{32} - \cdots\right) = \frac{1}{4}z - \frac{1}{48}z^3 + \frac{1}{480}z^5 - \cdots,
$$
and the ratio of the cubic coefficient to the linear coefficient equals $(-1/48)/(1/4) = -1/12$. $\blacksquare$

---

## §II.2.4. The Ring of Dual Numbers $K[\varepsilon]/(\varepsilon^2)$ and Algebraic Differentiation Without Limits

In §II.2.3, to work with the exponential $\exp(h J_a)$, we used division by $k!$, which requires a field of characteristic $0$. Yet the observer's question regarding **first-order sensitivity** (the linear response to a small input perturbation) requires neither a limit transition $\lim_{h \to 0}$ nor division by integers.

Adjoin to an arbitrary commutative ring (or field) $K$ a formal infinitesimal element $\varepsilon$ subject to the single relation
$$
\varepsilon^2 = 0, \qquad \varepsilon \ne 0.
$$
The quotient ring $K[\varepsilon]/(\varepsilon^2) = \{ a + b\varepsilon : a, b \in K \}$ with componentwise addition and multiplication rule
$$
(a_1 + b_1 \varepsilon)(a_2 + b_2 \varepsilon) = a_1 a_2 + (a_1 b_2 + a_2 b_1)\varepsilon
$$
is called the *ring of dual numbers* over $K$. Observe that the nilpotent element $\varepsilon$ in the ring $K[\varepsilon]/(\varepsilon^2)$ is strictly isomorphic to the $2 \times 2$ Jordan shift block from `Chapter II.1`:
$$
a + b\varepsilon \;\longleftrightarrow\; \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} \in K^{2 \times 2}, \qquad \varepsilon \;\longleftrightarrow\; \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad \varepsilon^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.
$$

> **Proposition II.2.2 (Algebraic first-order Taylor formula and the Jacobian chain rule in dual numbers over an arbitrary commutative ring $K$).**  
> *Classical foundation.* Ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$ (Clifford, 1873), algebraic first-order Taylor expansion $P(x + \varepsilon v) = P(x) + \varepsilon\, dP(x)v$, and the Jacobi chain rule. *Contribution of this book:* Purely algebraic formulation of first-order jets and tangent question pushforwards over any commutative ring $K$ with zero limit passages $\Delta x \to 0$.
> Let $K$ be an **arbitrary commutative ring with unity** (including finite fields $\mathbb{F}_2, \mathbb{F}_p$ of any characteristic).
> 1. For every polynomial $P(x_1, \dots, x_n) \in K[x_1, \dots, x_n]$ and any vectors $x, v \in K^n$, the following exact algebraic identity holds in the ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$:
>    $$
>    P(x + \varepsilon v) = P(x) + \varepsilon \, dP_x(v), \qquad dP_x(v) = \sum_{j=1}^n \frac{\partial P}{\partial x_j}(x)\, v_j,
>    $$
>    where the formal partial derivatives $\frac{\partial P}{\partial x_j}$ are defined purely algebraically by the rule $\frac{\partial}{\partial x_j}(x_j^k) = k x_j^{k-1}$ without any division or limit transition whatsoever.
> 2. For any polynomial map $F = (F_1, \dots, F_m)^{\mathsf{T}} : K^n \to K^m$ and each standard basis vector $e_j \in K^n$, the coefficient of $\varepsilon$ in the vector $F(x + \varepsilon e_j) = F(x) + \varepsilon\,\partial_j F(x)$ extracts precisely the $j$-th column of the Jacobian matrix $J_F(x) \in K^{m \times n}$, and for the composition of two polynomial maps $G \circ F$, the associativity of substitution in dual numbers automatically yields the chain rule of differentiation:
>    $$
>    (G \circ F)(x + \varepsilon v) = G\bigl(F(x) + \varepsilon J_F(x)v\bigr) = G(F(x)) + \varepsilon\, J_G(F(x))\, J_F(x) v,
>    $$
>    that is, $J_{G \circ F}(x) = J_G(F(x))\, J_F(x)$.

**Proof.**  
It suffices to verify the identity of item 1 on monomials and invoke linearity. For a single variable, the binomial theorem together with $\varepsilon^2 = \varepsilon^3 = \cdots = 0$ gives
$$
(x_j + \varepsilon v_j)^k = x_j^k + k x_j^{k-1} \varepsilon v_j + \sum_{r=2}^k \binom{k}{r} x_j^{k-r} \varepsilon^r v_j^r = x_j^k + \varepsilon \, k x_j^{k-1} v_j,
$$
where the binomial coefficients $\binom{k}{r} \in \mathbb{Z}$ are integers, so division is never used and the argument remains valid in arbitrary characteristic (in particular, over $\mathbb{F}_2$, where $\frac{\partial}{\partial x}(x^2) = 2x = 0$ and indeed $(x + \varepsilon v)^2 = x^2 + \varepsilon^2 v^2 = x^2$). Multiplying such binomials according to the rule $(a_1 + b_1\varepsilon)(a_2 + b_2\varepsilon) = a_1 a_2 + (a_1 b_2 + a_2 b_1)\varepsilon$ yields the total differential formula of item 1 and the chain rule of item 2. $\blacksquare$

> **Historical-Mathematical Note (Synthetic differential geometry and microlinearity).**  
> The systematic construction of differential calculus and the geometry of smooth spaces on the basis of the ring of first-order infinitesimals $D = \{\varepsilon : \varepsilon^2 = 0\}$ (the Kock–Lawvere axiom, according to which every map $D \to R$ is uniquely represented in the form $\varepsilon \mapsto a + b\varepsilon$) forms the foundation of *synthetic differential geometry* (`SDG`), initiated by F. W. Lawvere (*Categorical Dynamics*, 1967) and developed by A. Kock (*Synthetic Differential Geometry*, Cambridge Univ. Press, 1981; for an accessible introduction, see also J. L. Bell, *A Primer of Infinitesimal Analysis*, Cambridge Univ. Press, 1998/2008). In the context of our monograph, the dual numbers $K[\varepsilon]/(\varepsilon^2)$ directly turn a tangent vector from a "limit of secants" into a **two-point infinitesimal window of the observer** $(f(x), d f_x(v))$, isomorphic to the minimal two-dimensional Jordan memory of `Chapter II.1`.

---

## §II.2.5. Historical-Philosophical Parallel: Transparency of the Instrument in `YS 3.3` and Consistency of the Window Limit

In the third chapter of Patañjali's *Yoga Sūtras* (`YS 3.3`), the classical definition of absorption (*samādhi*) is given:

> *tad evārtha-mātra-nirbhāsaṃ svarūpa-śūnyam iva samādhiḥ* —  
> "When in *samādhi* contemplation itself shines forth solely with the object known (*artha-mātra-nirbhāsam*) and becomes as though devoid of its own form (*svarūpa-śūnyam iva*), that is absorption."

Notice the grammatical precision of the original: the epithet *svarūpa-śūnyam iva* ("as though empty of its own form") refers not to the object, but to **the act of contemplation itself** (*dhyāna*), in which the mediator's own noise and distortions cease to obscure the distinguished structure.

In the mathematical architecture of the present chapter (outside the deductive premises of the theorems), this motif corresponds to the transition from a crude asymmetric step to symmetric jet matching:
- the explicit Euler step $I + h J_a$ introduces already at second order its own scale distortion ($T_{\mathrm{Euler}}(h)T_{\mathrm{Euler}}(-h) = I - h^2 J_a^2 \ne I$), which does not belong to the generator $J_a$ under study, but is imposed by the asymmetry of the difference scheme;
- the symmetric Cayley transform $T_{\mathrm{Cayley}}(h) = (I + \frac{h}{2}J_a)(I - \frac{h}{2}J_a)^{-1}$ and the ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$ render the transfer step itself algebraically transparent up to the required jet order: upon reversing the step $h \mapsto -h$, the instrument returns to the exact identity $I$, leaving no parasitic quadratic trace.

---

## §II.2.6. Chapter Summary and Bridge to Chapter II.3

The table below summarizes the results of `Chapter II.2` on continuous continuation.

#### Table II.2.1. Four Stages of Continuous and Infinitesimal Continuation in Chapter II.2

| Continuation stage | Finite window of the observer | Limit or quotient object | What is preserved and what is glued |
| :--- | :--- | :--- | :--- |
| Spectral resolvent (`Lemma II.2.1`) | Markov parameters $M_0, \dots, M_{2d-1}$ | Rational function $H(z) = C(zI - B)^{-1}A$ | Substitution $w = 1/z$ maps $\det(zI-B)$ to the reciprocal denominator $\det(I - wB)$ |
| Dyadic scale (`Prop. II.2.1`) | Modular window $\mathbb{Z}/2^m\mathbb{Z}$ (including $S_4$ at $m=2$) | Projective limit $\mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$ | Boundary tails $0111\ldots_2 \sim 1000\ldots_2$ indistinguishable in the Archimedean metric are glued |
| Jets and Cayley step (`Theorem II.2.1`) | Truncated jet $J^m_0 = K[x]/(x^{m+1})$ | Cayley step $(I+\frac{h}{2}J_a)(I-\frac{h}{2}J_a)^{-1}$ | Exact inversion $T(h)T(-h)=I$, agreement up to $O(h^2)$, remainder $-\frac{1}{12}h^3 J_a^3$ |
| Infinitesimal window (`Prop. II.2.2`) | Dual ring $K[\varepsilon]/(\varepsilon^2)$ | Algebraic differential $P(x+\varepsilon v) = P(x) + \varepsilon dP_x(v)$ | Jacobian rule $J_{G\circ F} = J_G J_F$ holds in any characteristic without $\lim_{h\to 0}$ |

In `Chapters II.1` and `II.2`, we moved along a **single** coherent tower of time or precision, where each finer window projected uniquely onto a coarser one ($\pi_{m+1,m}(x_{m+1}) = x_m$). What happens, however, when the observer has no single linear scale, but instead a family of distinct local windows $U_i$ overlapping pairwise (like the six two-point slices on the scene $S_4$ in `Chapter I.9`), and at each seam one must reconcile sign and orientation from `Chapter I.5`? This is the subject of **Chapter `II.3`**, which opens the second enrichment of the volume—the simplicial homological and cohomological theory of gluing.

---

## Summary Passport of Chapter II.2 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Lemma II.2.1` | Agreement of the series coefficients of $C(I - wB)^{-1}A$ with the Markov parameters $C B^t A$ and the identity $\widetilde{\chi}_B(w) = w^d \chi_B(1/w)$ | `GATE-II02-01` |
| `Proposition II.2.1` | Tower $\mathbb{Z}/2^m\mathbb{Z}$, injectivity of $\Phi_m$, convergence $|\Phi_m(x^{(+)}) - \Phi_m(x^{(-)})| = 2^{-m} \to 0$ while $|x^{(+)} - x^{(-)}|_2 = 1$, and non-homomorphism $\bar{\Phi}(1)+\bar{\Phi}(1) \not\equiv \bar{\Phi}(2)$ | `GATE-II02-02` |
| `Theorem II.2.1` and `Lemma II.2.2` | Symbolic computation in $\mathbb{Q}$: $T_{\mathrm{Cayley}}(h)T_{\mathrm{Cayley}}(-h) = I$, defect $-\frac{1}{12}h^3 J_a^3$, and coefficients of $\widetilde{\sigma}(z)$ ($1/4, -1/48, 1/480$) | `GATE-II02-03` |
| `Proposition II.2.2` | Exact verification of the Jacobian rule $J_{G\circ F}(x) = J_G(F(x))J_F(x)$ via dual numbers over $\mathbb{Q}$ and over $\mathbb{F}_2$ | `GATE-II02-04` |
