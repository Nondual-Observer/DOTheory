# Chapter I.8. Finite Windows, Oracle-Free Contract, and Hankel Matrices

> *"Seeing through a small window does not yet mean knowing the hidden axes of the whole; yet whenever the trace in the window obeys a strict recurrence law, the size of the hidden linear memory betrays itself without a single glance inside the box."*

Imagine that a large number is not shown to you in full—you are allowed to learn only its remainders upon division by $3$, by $5$, and by $7$. When are these remainders enough to reconstruct the number, and when are they not? And what is one to do if the divisors themselves are unknown? With these two questions the chapter begins.

In **Chapter `I.7`** we verified that the additive counting scale and the multiplicative divisor lattice $D(N)$ cannot be reduced to one another by any permutation of names, while the appearance of even a single squared prime factor ($N = 12 = 2^2 \cdot 3$ or $N = 45 = 3^2 \cdot 5$) turns the Boolean cube of coprime features into a multi-story primary tower without classical complements. Now we will take the next constructive step and ask: **what exactly is a finite observer capable of learning about a large number or an infinite stream of numbers if only finite observation windows and honest arithmetic operations are available?**

Two connected problems are examined in the chapter:
1. **Spatial unfolding across finite modular and divisor windows (`§§I.8.1–I.8.3`).** A single fixed integer $x$ or an unknown divisor $d \mid N$ is observed simultaneously through several small windows—remainders $x \bmod m_i$ or greatest common divisors $\gcd(m_i, r)$. We will show when such windows assemble into complete knowledge of the whole (the Chinese Remainder Theorem and the theorem on gluing a cover by $\operatorname{lcm}$), why on a composite modulus $N = pq$ with unknown factors an explicit **oracle-free contract** of an honest observer is required, and how iterative squaring of a probe $x_{k+1} = \gcd(N, x_k^2)$ completes a partial catch into an entire primary tower.
2. **Temporal unfolding along a numerical sequence (`§§I.8.4–I.8.6`).** Instead of several parallel moduli, the observer has a single window sliding along an infinite sequence of responses $a = (a_0, a_1, a_2, \dots)$ over a field $K$. Here the table of shifted windows turns into the infinite **Hankel matrix** $H(a)_{i,j} = a_{i+j}$, its finite rank exactly measures the volume of hidden linear memory (Kronecker's theorem), reduction modulo a prime $p$ vividly shows the collapse of resonant modes when frequencies coincide, and passing to a nonlinear polynomial step over $\mathbb{F}_p$ reveals finite compression basins and their strict arithmetic limits.

---

## §I.8.1. Two Gears of One Clock and the Honest Observer's Contract on a Composite Modulus

Let us begin with a simple tabletop mechanism. Suppose two meshed toothed wheels with marked zero teeth rotate before us: the first wheel has $m_1 = 9$ teeth (remainders $0, 1, \dots, 8$), the second has $m_2 = 5$ teeth (remainders $0, 1, 2, 3, 4$). At each click of the shaft both wheels turn by one tooth simultaneously, so that after $x$ clicks the instrument displays a pair of remainders

$$\Phi_{9,5}(x) \;=\; (x \bmod 9,\; x \bmod 5) \;\in\; \mathbb{Z}/9\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z}.$$

Will both readings repeat before the shaft makes $9 \cdot 5 = 45$ clicks? For both wheels to return to zero simultaneously, the number of steps $x$ must be divisible by both $9$ and $5$. Since $\gcd(9, 5) = 1$, the least positive common multiple equals $\operatorname{lcm}(9, 5) = 45$. Thus all $45$ states of the large wheel $\mathbb{Z}/45\mathbb{Z}$ map into the $9 \times 5 = 45$ pairs of readings **without a single collision and without a single omission**. Moreover, we can write down an explicit inverse assembler without guessing $x$ by brute force. Let us find two basis numbers ("orthogonal keys"):
- the number $e_1 = 10$ is a multiple of $5$, but upon division by $9$ gives remainder $1$: $\Phi_{9,5}(10) = (1, 0)$;
- the number $e_2 = 36$ is a multiple of $9$, but upon division by $5$ gives remainder $1$: $\Phi_{9,5}(36) = (0, 1)$.

These two keys modulo $45$ satisfy three orthogonal idempotent relations: their sum equals $10 + 36 = 46 \equiv 1 \pmod{45}$, the square of each coincides with itself ($10^2 = 100 \equiv 10 \pmod{45}$, $36^2 = 1296 \equiv 36 \pmod{45}$), and their product vanishes ($10 \cdot 36 = 360 = 8 \cdot 45 \equiv 0 \pmod{45}$). Therefore any pair of readings $(a, b) \in \mathbb{Z}/9\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z}$ is instantly assembled into a unique residue modulo $45$ by the linear formula

$$x \;\equiv\; 10a + 36b \pmod{45}.$$

For instance, if the first wheel shows $a = 7$ and the second $b = 3$, then $10 \cdot 7 + 36 \cdot 3 = 70 + 108 = 178 = 3 \cdot 45 + 43$, and indeed $43 = 4 \cdot 9 + 7 = 8 \cdot 5 + 3$. The first wheel $m_1 = 9 = 3^2$ is composite and does not decompose into two smaller wheels of $3$ teeth each ($\gcd(3, 3) = 3 \neq 1$), but with five it is coprime ($\gcd(9, 5) = 1$), and therefore the decomposition between the whole primary towers $3^2$ and $5^1$ works faultlessly.

What will happen if we replace the wheels with a pair sharing a common divisor: $m_1 = 4$ and $m_2 = 6$, where $\gcd(4, 6) = 2 > 1$ and $m_1 m_2 = 24$? Then both wheels always show **the same parity**: for even $x$ both remainders are even, for odd $x$ both are odd. Out of the $4 \times 6 = 24$ conceivable pairs $(a, b)$, exactly half (all $12$ opposite-parity pairs, such as $(0 \bmod 4,\; 1 \bmod 6)$) are **unreachable altogether**, while every reachable pair repeats modulo $24$ twice (thus $x = 0$ and $x = 12$ are indistinguishable and give $(0, 0)$, because the true period of the mechanism equals $\operatorname{lcm}(4, 6) = 12$, not $24$).

Let us formulate the law of modular windows in general form.

> **Theorem I.8.1 (Chinese Remainder Theorem for pairwise coprime windows).**  
> *Classical foundation.* Classical Chinese Remainder Theorem for coprime moduli and compatibility criterion for systems of congruences modulo non-coprime integers (Ore, 1952). *Contribution of this book:* Oracle-free observation contract on a composite modulus $N = pq$: separating the hidden torus isomorphism $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$ from the open Euclidean probe $\gcd(N, r)$ (`60` silent invertible residues vs. `16` axial hits on $N = 77$).
> Let the positive integer moduli $m_1, m_2, \dots, m_k \in \mathbb{Z}_{>0}$ be pairwise coprime: $\gcd(m_i, m_j) = 1$ for all $i \neq j$, and let $N = m_1 m_2 \cdots m_k$. Then the joint reading of remainders
> $$\Phi(x \bmod N) \;=\; (x \bmod m_1,\; x \bmod m_2,\; \dots,\; x \bmod m_k)$$
> is an **isomorphism of commutative rings with unity**
> $$\mathbb{Z}/N\mathbb{Z} \;\xrightarrow{\;\sim\;}\; \mathbb{Z}/m_1\mathbb{Z} \times \mathbb{Z}/m_2\mathbb{Z} \times \dots \times \mathbb{Z}/m_k\mathbb{Z}.$$
> The inverse map is given by the explicit formula $\Phi^{-1}(a_1,\dots,a_k) \equiv \sum_{i=1}^k e_i a_i \pmod N$, where $M_i = N/m_i$, $u_i \equiv M_i^{-1} \pmod{m_i}$ (existing thanks to $\gcd(M_i, m_i) = 1$), and $e_i = M_i u_i \bmod N$ is a family of pairwise orthogonal idempotents ($e_i^2 \equiv e_i$, $e_i e_j \equiv 0$ for $i \neq j$, $\sum_{i=1}^k e_i \equiv 1 \pmod N$).

*Proof.* By definition of reduction modulo $m_i \mid N$, the map $\Phi$ preserves zero, unity, addition, and multiplication, i.e., is a ring homomorphism. If $x \in \ker \Phi$, then $m_i \mid x$ for all $i = 1, \dots, k$; since the moduli are pairwise coprime, their least common multiple equals the product $N = \prod_{i=1}^k m_i$, whence $N \mid x$, and thus $\ker \Phi = \{0\}$. An injective map between two finite sets of the same cardinality $N = \prod_{i=1}^k m_i$ is automatically bijective. For the keys $e_i = M_i u_i$, when $j \neq i$ the number $m_j$ divides $M_i = N/m_i$, so $e_i \equiv 0 \pmod{m_j}$, whereas modulo $m_i$ we have $e_i \equiv M_i u_i \equiv 1 \pmod{m_i}$. Consequently, $\Phi(e_i)$ is the $i$-th standard basis vector with unity in the $i$-th position and zeros elsewhere, whence by linearity $\Phi\bigl(\sum_i e_i a_i\bigr) = (a_1, \dots, a_k)$. $\square$

It might seem that Theorem `I.8.1` completely settles the question: every composite ring $\mathbb{Z}/N\mathbb{Z}$ for $N = pq$ ($p \neq q$ odd primes) is simply the direct product of two fields $\mathbb{F}_p \times \mathbb{F}_q$. At the same time, one must distinguish between the existence of a decomposition and the ability to compute it from the available data.

**Who exactly holds the gears $p$ and $q$ in their hands?** Imagine that external nature has handed the observer **only the number $N = pq$ itself** (say, in our pedagogical model $N = 77$, and in a real problem an $N$ of hundreds of decimal digits), but **has communicated neither $p$ nor $q$**. The hidden torus $\mathbb{F}_p \times \mathbb{F}_q$ objectively exists inside $\mathbb{Z}/N\mathbb{Z}$: every residue $x \in \mathbb{Z}/N\mathbb{Z}$ has two objective hidden coordinates $(x \bmod p,\; x \bmod q)$, and two "axes of zero divisors"—the multiples of $p$ (where the first coordinate equals $0$) and the multiples of $q$ (where the second coordinate equals $0$). However, the observer himself sees only the flat scale $\{0, 1, \dots, N-1\}$. He can add, subtract, and multiply residues modulo $N$, but cannot directly compute either $x \bmod p$ or the orthogonal idempotents $e_1, e_2$ (after all, knowing a non-trivial idempotent $e_1 \notin \{0, 1\}$ immediately decomposes $N$ into factors via $\gcd(N, e_1) = q$ and $\gcd(N, e_1 - 1) = p$).

What, then, is the sole legitimate instrument connecting flat computations modulo $N$ with the hidden axes of the torus $\mathbb{F}_p \times \mathbb{F}_q$? It is the Euclidean algorithm—**the divisor probe** $\delta_N(r) = \gcd(N, r)$, which runs in time polynomial in the number of bits without any prior knowledge of the decomposition of $N$.

```text
  HIDDEN GEOMETRY OF THE TORUS Z/pZ × Z/qZ       OPEN WINDOW OF THE REAL EXECUTOR (given only N)
  (visible only to an external oracle with (p,q)) (only +, -, · mod N and Euclidean gcd are available)

   x mod q ^                                      Input: public modulus N = 77 (factors hidden)
        10 | .  *  .  .  .  .  .                           |
         8 | .  x=8=(1,8)      .                           v
         4 | .  y=15=(1,4)     .                  Ring step: r = P(x) mod N  (e.g., r = x - 1)
         1 | .  1=(1,1)        .                           |
         0 +---------------------> x mod p                 v
           0  1  2  3  4  5  6                    Euclidean probe: d = gcd(N, r) ∈ {1, p, q, N}
           ^                                        • d = 1  (60 invertible residues): axes missed
           | axis x ≡ 0 (mod 7): 10 non-zero points • d = N  (residue r ≡ 0): trivial coincidence
             immediately yield gcd(77, r) = 7!      • 1 < d < N (16 axis points): FACTOR FOUND!
```
**Fig. I.8.1.** The hidden torus $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$ and the oracle-free observer's contract on the example $N = 77 = 7 \cdot 11$.  
On the left is the true two-dimensional CRT lattice $(x \bmod 7,\; x \bmod 11)$: two invertible residues $x = 8 \mapsto (1, 8)$ and $y = 15 \mapsto (1, 4)$ lie on the same vertical line $x \equiv 1 \pmod 7$, but neither touches the zero axes ($\gcd(77, 8) = \gcd(77, 15) = 1$). On the right is the circuit of the real executor: without knowing the number $7$, it computes the open polynomial $r = x - 1 \bmod 77$, shifting the entire vertical line $x \equiv 1 \pmod 7$ directly onto the vertical zero axis $r \equiv 0 \pmod 7$, after which the Euclidean probe $\gcd(77, 7) = 7$ and $\gcd(77, 14) = 7$ legitimately extracts the hidden factor.

Let us check the balance of forces on the pedagogical modulus $N = 77 = 7 \cdot 11$ across all $77$ residues $r \in \{0, 1, \dots, 76\}$:
- exactly $\varphi(77) = (7 - 1)(11 - 1) = 60$ residues are coprime to $77$ and return the silent answer $\gcd(77, r) = 1$;
- exactly $1$ residue ($r = 0$, the intersection of both zero axes) returns the trivial answer $\gcd(77, 0) = 77$;
- exactly $77 - 60 - 1 = 16$ non-zero non-invertible residues lie on the two punctured axes of zero divisors: $10$ multiples of seven ($7, 14, 21, 28, 35, 42, 49, 56, 63, 70$) return $\gcd(77, r) = 7$, and $6$ multiples of eleven ($11, 22, 33, 44, 55, 66$) return $\gcd(77, r) = 11$.

From this follows a strict methodological contract, which we fix for the entire book.

> **Definition I.8.1 (Contract of an oracle-free algorithm on a composite modulus).**  
> An algorithm on input $N \in \mathbb{Z}_{>1}$ is called **oracle-free (honest with respect to the unknown decomposition of $N$)** if every one of its elementary steps uses exclusively:
> 1. the public integer $N$ and constants chosen prior to presenting the hidden divisors;
> 2. the ring operations of addition, subtraction, and multiplication modulo $N$ (as well as integer division with remainder by numbers already discovered by the algorithm);
> 3. congruence testing $u \equiv v \pmod N$ and the Euclidean probe $\delta_N(r) = \gcd(N, r)$.
>
> No appeal to the hidden projections $x \bmod p$, the order of the multiplicative group $\mathbb{F}_p^\times$, the Legendre symbol $\left(\frac{x}{p}\right)$ modulo an unknown prime $p \mid N$, or the CRT idempotents $e_i$ **is permitted inside the executor's code**; the hidden geometry of the CRT is used exclusively in the external mathematical proof of correctness and in estimating the probability that $P(x) \bmod N$ hits the axes of zero divisors.

---

## §I.8.2. Three Traps of Finite Windows: Oracle Leak, Gluing Blindness, and Initial Impulse

Before building the general algebra of divisor and sequence windows, let us single out three characteristic errors on which intuition most often stumbles when working with partial observations of a number.

### Trap 1. Substituting a Hidden Coordinate for an Oracle-Free Step ("Oracle Leak")
When a researcher studies a composite number $N = pq$ on paper, knowing $p = 7$ and $q = 11$ in advance, they see beautiful symmetries inside the field $\mathbb{F}_7$: for instance, by Fermat's Little Theorem, for any $a \not\equiv 0 \pmod 7$ the number $a^{6} - 1$ is divisible by $7$. If one imperceptibly writes the exponent $p - 1$ or the condition "choose $x$ with $x \bmod p = 1$" into a step of the algorithm, on small examples the program will instantly decompose $N$—but only because the answer was secretly fed to its input. The contract of `Definition I.8.1` places a strict barrier against such self-deceptive leakage: if a step uses $r = a^M - 1 \bmod N$, then the exponent $M$ must be built from open small numbers without the slightest participation of the unknown $p$ (as in Pollard's classical $p-1$ method, where $M = \operatorname{lcm}(1, 2, \dots, B)$ is chosen from an open smoothness bound $B$, while the hidden condition $(p-1) \mid M$ explains only for which $p$ the probe $\gcd(N, r)$ will succeed).

### Trap 2. Loss of Multiplicity of a Primary Floor When Splitting a Window Without the Original Probe
Suppose the modulus $N = A \cdot B$ is split into two factors $A$ and $B$, and two local observers have reported to us only their partial catches $d_A = \gcd(A, r)$ and $d_B = \gcd(B, r)$, having erased the probe $r$ itself. If $\gcd(A, B) = 1$, then $\gcd(N, r) = d_A \cdot d_B$ is recovered unconditionally. Yet as soon as $A$ and $B$ share a common prime floor, information is irreversibly lost. Take $N = 25 = 5 \cdot 5$, $A = 5$, $B = 5$:
- for the probe $r_1 = 20$, both local windows see $(d_A, d_B) = (\gcd(5, 20),\, \gcd(5, 20)) = (5, 5)$, whereas the true greatest common divisor with the modulus equals $\gcd(25, 20) = 5$;
- for the probe $r_2 = 25$, both windows see **the very same pair** $(d_A, d_B) = (\gcd(5, 25),\, \gcd(5, 25)) = (5, 5)$, whereas the true greatest common divisor equals $\gcd(25, 25) = 25$.

No function $f(d_A, d_B)$ can simultaneously output $5$ and $25$ on one and the same input $(5, 5)$: without retaining the probe $r$ itself (or without covering the entire tower $25$ by at least one of the windows), the second floor of the power of five disappears into a blind spot.

### Trap 3. Confusing the Degree of the Denominator of a Rational Series with the Full Hankel Rank
Let us now move to an infinite sequence $a = (a_0, a_1, a_2, \dots)$ and its generating series $F(t) = \sum_{n=0}^{\infty} a_n t^n$. Very often a careless rule is stated: *"the rank of the Hankel matrix of a sequence equals the degree of the denominator $Q(t)$ of its rational generating function $P(t)/Q(t)$"*. Let us test this statement on a tiny sequence with a single delayed impulse:

$$a \;=\; (0,\; 1,\; 0,\; 0,\; 0,\; \dots), \qquad F(t) \;=\; t \;=\; \frac{t}{1}.$$

Here the irreducible denominator is $Q(t) = 1$, and its degree is $\deg Q = 0$. If the Hankel rank equaled $\deg Q$, the Hankel matrix would be zero. Meanwhile, its top-left $2 \times 2$ corner has the form

$$H^{(2)}(a) \;=\; \begin{pmatrix} a_0 & a_1 \\ a_1 & a_2 \end{pmatrix} \;=\; \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \det H^{(2)}(a) \;=\; -1 \;\neq\; 0,$$

while all rows and columns with indices $\ge 2$ are identically zero, so that the true rank equals $\operatorname{rank}_K H(a) = 2 \neq 0$. Why did two units of memory arise where identical zero reigns in the tail? Because the recurrence relation begins to act only after working through the initial transient segment of length $\deg P$, and the Hankel matrix actually counts **both the persistent pole modes of the denominator $Q$ and the finite delay of the numerator $P$**, yielding the exact formula $\max(\deg P + 1,\; \deg Q)$.

---

## §I.8.3. Three Regimes of Divisor Memory: Primary Saturation, Probe Transfer, and Cover Gluing

Let us return to the oracle-free probe $\delta_N(r) = \gcd(N, r)$ and show how to handle non-Boolean primary towers of a modulus $N$ without loss.

### Regime 1. Primary Saturation of a Single Probe by Squaring
Suppose the probe has caught a non-trivial divisor $x_0 = \gcd(N, r)$, but has hooked only the lower floor of some primary tower. For instance, at $N = 360 = 2^3 \cdot 3^2 \cdot 5$ and $r = 6$, the initial catch equals $x_0 = \gcd(360, 6) = 6 = 2^1 \cdot 3^1$. It is too early to divide $360$ by $6$: the quotient $360 / 6 = 60 = 2^2 \cdot 3 \cdot 5$ is still not coprime to $6$ ($\gcd(6, 60) = 6$), and we cannot apply the Chinese Remainder Theorem to the pair $(6, 60)$. How can one extract in an oracle-free manner from $x_0$ the **entire** tower of twos and threes entering $N$? It suffices to iteratively square the current catch under the protection of $\gcd(N, \cdot)$:

$$x_{k+1} \;=\; \gcd(N,\; x_k^2) \qquad (k = 0, 1, 2, \dots).$$

Let us trace this process on $N = 360$ starting from $x_0 = 6$:
- step 1: $x_1 = \gcd(360,\; 6^2) = \gcd(360, 36) = 36 = 2^2 \cdot 3^2$;
- step 2: $x_2 = \gcd(360,\; 36^2) = \gcd(360, 1296) = 72 = 2^3 \cdot 3^2$;
- step 3: $x_3 = \gcd(360,\; 72^2) = \gcd(360, 5184) = 72 = x_2$ — **saturation is reached.**

Now the complementary factor equals $360 / 72 = 5$, and the strict coprime splitting $\gcd(72, 5) = 1$ holds, ready for Theorem `I.8.1`. In exactly the same way, on $N = 45 = 3^2 \cdot 5$ from $x_0 = 3$ one step gives $x_1 = \gcd(45, 9) = 9$ and the coprime splitting $45 = 9 \cdot 5$.

> **Lemma I.8.1 (Law of primary saturation of a probe).**  
> *Classical foundation.* $p$-adic valuations $v_p(x)$ and greatest-common-divisor algorithms in the ring of integers. *Contribution of this book:* Oracle-free primary saturation iteration $x_{k+1} = \gcd(N, x_k^2)$ doubling the valuations of all captured prime factors and reaching the full primary floor in at most $\lceil \log_2 \max_{p \mid N} v_p(N) \rceil$ steps.
> For any $N \in \mathbb{Z}_{\ge 2}$ (at $N = 1$ the sequence is constant $x_k \equiv 1$ in $0$ steps) and initial divisor $x_0 = \gcd(N, r) \mid N$, the sequence $x_{k+1} = \gcd(N, x_k^2)$ grows monotonically with respect to divisibility and in at most $K = \lceil \log_2(\max_{p \mid N} v_p(N)) \rceil \le \lceil \log_2 \log_2(N + 1) \rceil$ steps stabilizes at the **saturated primary block**
> $$x_K \;=\; N_{\mathrm{sat}}(x_0) \;=\; \prod_{p \mid x_0} p^{v_p(N)}, \qquad \gcd\!\bigl(N_{\mathrm{sat}}(x_0),\; N / N_{\mathrm{sat}}(x_0)\bigr) \;=\; 1.$$

*Proof.* For each prime $p$, the exponent $v_p(x_{k+1}) = \min\bigl(v_p(N),\, 2 v_p(x_k)\bigr)$, whence by induction $v_p(x_k) = \min\bigl(v_p(N),\, 2^k v_p(x_0)\bigr)$. If $p \nmid x_0$, then $v_p(x_0) = 0$ and $v_p(x_k) = 0$ for all $k$ (no extraneous prime factors are mixed in). If instead $p \mid x_0$, then $v_p(x_0) \ge 1$, and as soon as $2^k \ge v_p(N)$, we have $v_p(x_k) = v_p(N)$, and hence $p \nmid (N / x_K)$. $\square$

Let us note an important **boundary caveat**: if the entire modulus is a power of a single prime number, for example $N = 9 = 3^2$, and a proper divisor $x_0 = 3$ is found, then saturation will yield $x_1 = \gcd(9, 9) = 9 = N$. This is not a loss of information (after all, $9$ truly has no coprime non-trivial decomposition $9 = A \cdot B$ with $\gcd(A, B) = 1$), but a direct reminder that primary saturation splits off **coprime blocks**, whereas testing whether a number is a pure power $N = m^k$ ($k \ge 2$) is performed by a separate exact integer root extraction.

### Regime 2. Transferring a Probe to a Submodulus and the 7-Step Lift with Retained $r$
How should probe results be transmitted between a large modulus $N$ and its divisors $A, B \mid N$? When passing from a larger modulus to its divisor, information descends without distortion. When reconstructing from two non-coprime parts $N = AB$, the local values $(d_A, d_B)$ alone are insufficient. In a distributed or hierarchical computation, two local executors have already found $d_A = \gcd(A, r)$ and $d_B = \gcd(B, r)$ on their smaller registers $A$ and $B$; in order not to rerun the Euclidean algorithm from scratch at the full bit-length of the large modulus $N$, the central node first assembles the already discovered part of the divisor $D = \operatorname{lcm}(d_A, d_B)$, reduces both the modulus and the probe by $D$ ($N' = N/D$, $r' = r/D$), and picks up the missing multiplicity of shared primary towers with a single reduced call $C = \gcd(N', r')$.

> **Lemma I.8.2 (Exact downward descent and recovery of $\gcd(N, r)$ when retaining the probe).**  
> *Classical foundation.* Arithmetic of $p$-adic minima and sums $\min(a+b, c)$ for greatest common divisors and least common multiples. *Contribution of this book:* Separation of three divisor-memory regimes of local windows $m_A, m_B \mid N$, counterexample of losing the squared floor on $N = 25$ from $(g_A, g_B)$ alone, and explicit 7-operation formula recovering $\gcd(N, r)$ when retaining the probe $r$.
> 1. **Unconditional descent to a divisor:** for any divisor $A \mid N$ and any $r \in \mathbb{Z}$, one has $\gcd(A, \gcd(N, r)) = \gcd(A, r)$.
> 2. **Seven-step lift to a product $N = AB$ via the reduced cofactor with retained $r$:** suppose two local windows have computed the partial answers $d_A = \gcd(A, r)$ and $d_B = \gcd(B, r)$ and retained the probe $r$ (its residue modulo $N$ suffices). Set
>    $$g = \gcd(d_A, d_B), \quad q_A = d_A / g, \quad D = q_A \cdot d_B = \operatorname{lcm}(d_A, d_B), \quad N' = N / D, \quad r' = r / D, \quad C = \gcd(N', r').$$
>    Then $D \mid \gcd(N, r)$, the residual step $C = \gcd(N', r')$ is executed on the reduced modulus $N' = N/D \le N$ (with $C = 1$ automatically whenever $\gcd(d_A, d_B) = 1$), and the product $D \cdot C$ is equal to $\gcd(N, r)$ for any (including non-coprime) $A$ and $B$ with $N = AB$.

*Proof.*  
1. The greatest common divisor is associative and commutative on the lattice of positive integers: since $A \mid N$, we have $\gcd(A, N) = A$, whence $\gcd(A, \gcd(N, r)) = \gcd(\gcd(A, N), r) = \gcd(A, r)$.  
2. Since $d_A \mid A \mid N$ and $d_B \mid B \mid N$, as well as $d_A \mid r$ and $d_B \mid r$, the least common multiple $D = \operatorname{lcm}(d_A, d_B)$ divides both $N$ and $r$, i.e., $D \mid \gcd(N, r)$, and the divisions $N' = N/D$ and $r' = r/D$ are entirely integer. By homogeneity of the greatest common divisor, $\gcd(N, r) = \gcd(D N', D r') = D \cdot \gcd(N', r') = D \cdot C$. $\square$

Let us check this formula on both of our examples. In the trap $N = 25 = 5 \cdot 5$ ($A = B = 5$), both points $r_1 = 20$ and $r_2 = 25$ give $D = \operatorname{lcm}(5, 5) = 5$ and $N' = 25/5 = 5$, but the retained probe instantly separates them at the sixth step: for $r_1 = 20$ we obtain $r'_1 = 4$ and $C_1 = \gcd(5, 4) = 1 \implies D C_1 = 5$, while for $r_2 = 25$ we obtain $r'_2 = 5$ and $C_2 = \gcd(5, 5) = 5 \implies D C_2 = 25$. On the composite modulus $N = 360 = 20 \cdot 18$ at $r = 72$, we have $d_{20} = \gcd(20, 72) = 4$, $d_{18} = \gcd(18, 72) = 18$, whence $D = \operatorname{lcm}(4, 18) = 36$, and the residual pick-up $C = \gcd(360/36,\, 72/36) = \gcd(10, 2) = 2$ returns the exact answer $36 \cdot 2 = 72 = \gcd(360, 72)$.

Let us also make a small terminological caution here: when comparing the multiplicative gluing $\operatorname{lcm}(a, b)$ with the additive sum $a + b$, it is convenient to consider the integer **multiplicative-additive gap** $\Delta_\otimes(a, b) = \operatorname{lcm}(a, b) - (a + b)$ (for example, $\Delta_\otimes(2, 3) = 6 - 5 = +1 > 0$ for coprime $2$ and $3$, whereas on the coinciding pair $\Delta_\otimes(2, 2) = 2 - 4 = -2 < 0$). To avoid confusion between different chapters, we call $\Delta_\otimes$ specifically the *multiplicative-additive gap*, never confusing it either with the classical arithmetic Möbius function $\mu(n) \in \{-1, 0, +1\}$ or with the topological Möbius strip that will appear when analyzing gluing obstructions in **Chapter `I.9`**.

### Regime 3. Error-Free Gluing of a Full Cover of Divisor Windows
When does a family of local divisor windows $m_1, \dots, m_k \mid N$ after all reconstruct an unknown divisor $d \mid N$ **without storing any external probe $r$ at all**? Precisely when the windows jointly cover the full height of every primary tower of the number $N$, i.e., $\operatorname{lcm}(m_1, \dots, m_k) = N$.

> **Theorem I.8.2 (Gluing a divisor from a pairwise compatible cover by $\operatorname{lcm}$).**  
> *Classical foundation.* Distributivity of the divisor lattice $(D(N), \gcd, \operatorname{lcm})$ via prime-exponent valuations $v_p$. *Contribution of this book:* Sheaf-like gluing theorem for divisor windows: bijection $d \mapsto (\gcd(d, m_i))_i$ and inverse assembly $d = \operatorname{lcm}_i d_i$ between all divisors of $N$ and local families compatible on pairwise seams $\gcd(m_i, m_j)$ (`36 → 9` on $D(12) \times D(18)$).
> Let the moduli $m_1, \dots, m_k \mid N$ satisfy the full cover condition $\operatorname{lcm}(m_1, \dots, m_k) = N$. Then the map of reading local traces
> $$d \;\longmapsto\; \bigl(\gcd(d, m_1),\; \gcd(d, m_2),\; \dots,\; \gcd(d, m_k)\bigr)$$
> defines a bijection between the lattice of all divisors $D(N)$ and the set of all tuples $(d_1, \dots, d_k) \in D(m_1) \times \dots \times D(m_k)$ that are pairwise compatible on the intersections of the windows:
> $$\gcd\bigl(d_i,\; \gcd(m_i, m_j)\bigr) \;=\; \gcd\bigl(d_j,\; \gcd(m_i, m_j)\bigr) \qquad (\forall\, i, j),$$
> and the inverse assembly is unique and given by the formula $d = \operatorname{lcm}(d_1, \dots, d_k)$.

*Proof.* If $d_i = \gcd(d, m_i)$, then by associativity of $\gcd$ both sides of the compatibility condition equal $\gcd(d, \gcd(m_i, m_j))$, and for any prime $p \mid N$ it follows from $\operatorname{lcm}_i m_i = N$ that there exists an index $i_*$ with $v_p(m_{i_*}) = v_p(N) \ge v_p(d)$, whence $\max_i v_p(d_i) = \max_i \min(v_p(d), v_p(m_i)) = v_p(d)$, i.e., $\operatorname{lcm}(d_1, \dots, d_k) = d$. Conversely, let the tuple $(d_1, \dots, d_k)$ be pairwise compatible and set $d = \operatorname{lcm}_i d_i \mid \operatorname{lcm}_i m_i = N$. Fix an index $i$ and a prime $p$; let the index $j$ attain the maximum $v_p(d) = v_p(d_j)$. Pairwise compatibility for the pair $(i, j)$ in the exponents of $p$ states:
$$\min\bigl(v_p(d_i),\; v_p(m_i),\; v_p(m_j)\bigr) \;=\; \min\bigl(v_p(d_j),\; v_p(m_i),\; v_p(m_j)\bigr).$$
Since $d_i \mid m_i$ and $d_j \mid m_j$, we have $v_p(d_i) \le v_p(m_i)$ and $v_p(d_j) \le v_p(m_j)$, so the equality simplifies to $\min(v_p(d_i), v_p(m_j)) = \min(v_p(d_j), v_p(m_i))$. But $v_p(d_i) \le v_p(d) = v_p(d_j) \le v_p(m_j)$, so the left-hand side is simply equal to $v_p(d_i)$, while the right-hand side equals $\min(v_p(d), v_p(m_i)) = v_p(\gcd(d, m_i))$. By the arbitrariness of the prime $p$, we obtain $\gcd(d, m_i) = d_i$ for each $i$. $\square$

This is vividly seen on $N = 36 = 2^2 \cdot 3^2$ and two overlapping windows $m_1 = 12 = 2^2 \cdot 3$ and $m_2 = 18 = 2 \cdot 3^2$ (here they are not coprime: the intersection window equals $\gcd(12, 18) = 6$, but their union covers both towers in full: $\operatorname{lcm}(12, 18) = 36$). Both $D(12)$ and $D(18)$ have $6$ divisors each ($36$ arbitrary pairs), yet the condition of trace coincidence on the common seam $\gcd(d_1, 6) = \gcd(d_2, 6)$ carves out from the $36$ pairs exactly $9$ compatible pairs—precisely one for each of the $9$ divisors of $36$ (for instance, the pair $(d_1, d_2) = (12, 18)$ is compatible on six, since $\gcd(12, 6) = 6 = \gcd(18, 6)$, and assembles into $d = \operatorname{lcm}(12, 18) = 36$; by contrast, the pairs $(4, 18)$ and $(4, 9)$ are rejected by the seam, since $\gcd(4, 6) = 2$, whereas $\gcd(18, 6) = 6$ and $\gcd(9, 6) = 3$). Let us remember this construction: already in the next **Chapter `I.9`** we will see that on two overlapping windows local agreement is always sufficient for gluing, whereas on **three or more** windows a closed cohomological obstruction can arise.

---

## §I.8.4. From Modular Windows to a Sequence Window: Hankel Matrices and Three Steps of Memory

Let us now make a deliberate turn of viewpoint. In `§§I.8.1–I.8.3` the object of observation rested in place while we applied different arithmetic windows $m_1, \dots, m_k$ to it. Imagine now that the observation window is single, but step by step the system outputs an infinite sequence of scalar responses

$$a \;=\; (a_0,\; a_1,\; a_2,\; a_3,\; \dots), \qquad a_n \in K,$$

where $K$ is some field (for example, the field of rational numbers $\mathbb{Q}$ or a finite prime residue field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$). At step $i$ we can launch the shifted tail of the sequence $R_i(a) = (a_i, a_{i+1}, a_{i+2}, \dots)$ and compare it with all previous tails through finite windows of length $m$. Writing the tails $R_0, R_1, R_2, \dots$ as rows one beneath another, we obtain the infinite symmetric **Hankel matrix** of the sequence $a$ and the family of its finite corner windows $H^{(m)}(a)$ of size $m \times m$:

$$H(a) \;=\; (a_{i+j})_{i,j \ge 0} \;=\; \begin{pmatrix} a_0 & a_1 & a_2 & a_3 & \cdots \\ a_1 & a_2 & a_3 & a_4 & \cdots \\ a_2 & a_3 & a_4 & a_5 & \cdots \\ a_3 & a_4 & a_5 & a_6 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}, \qquad H^{(m)}(a) \;=\; (a_{i+j})_{0 \le i, j \le m-1}.$$

So that the reader may form a unified panorama of the entire monograph, let us compare three kindred constructions of hidden memory that unfold successively from the beginning of Book I to the beginning of Book II:

| Step | Where introduced | What is observed from outside | What algebra is permitted to the observer | What measures the volume of hidden memory |
| :--- | :---: | :--- | :--- | :--- |
| **1. Discrete Nerode memory** | `Ch. I.3` | Trajectory of answers $\bigl(\beta(T^n x)\bigr)_{n \ge 0}$ from a finite alphabet | Only testing set-theoretic coincidence of tails (without addition) | Number $|X / {\sim_\Gamma}|$ of distinct classes of reachable tails |
| **2. Scalar Hankel memory** | **`Ch. I.8`** | Single numerical sequence $a = (a_n)_{n \ge 0}$ over a field $K$ | Linear combinations of shifted tails $R_i(a)$ with coefficients from the field $K$ | **Hankel rank** $\operatorname{rank}_K H(a) = \dim_K \operatorname{span}\{R_i(a)\}_{i \ge 0}$ |
| **3. Block operator memory** | `Ch. II.1` | Stream of multidimensional response matrices $M_n = C B^n F : U \to Y$ | Operator composition and quotient space of reachable states modulo indistinguishable ones | Dimension of minimal Kalman–Ho realization $\dim_K W_{\min}$ |

This table removes any sense of a leap: the Hankel matrix is precisely **the linearized Nerode construction from Chapter `I.3`**, applied to the shift operator $S(a_0, a_1, a_2, \dots) = (a_1, a_2, a_3, \dots)$ in the vector space of sequences $K^{\mathbb{N}}$. Indeed, the $i$-th row of the matrix $H(a)$ is $R_i = S^i(a)$. To say that the rank of the matrix $H(a)$ is finite and equal to $r$ is to say that the entire infinite family of shifts $\{a,\, Sa,\, S^2 a,\, \dots\}$ fits inside a finite-dimensional $S$-invariant subspace of dimension $r$. Two instructive examples immediately show how linear Hankel memory differs from purely set-theoretic counting of Nerode tails and what computational cost this difference carries:
- on the alternating sequence $a_n = (-1)^n$ over $\mathbb{Q}$, comparing tails without addition and scalar multiplication sees **`2` distinct tails** $(1, -1, 1, \dots)$ and $(-1, 1, -1, \dots) = -a$, whereas the linear span folds them onto a single line ($S a = -a$), giving Hankel rank **`1`**;
- on the unboundedly growing geometric progression $a_n = 2^n$ over $\mathbb{Q}$, there are **countably many** set-theoretic tails $2^k(1, 2, 4, \dots)$ (a Nerode automaton with finitely many states is impossible), whereas the Hankel rank is still equal to **`1`** ($S a = 2a$): the finite dimension `1` of linear memory is achieved here at the price of linear growth of the bit-length of the rational register itself by `1` bit per tick (`Chapter I.4`), whereas reduction modulo an odd prime $p$ turns the very same trajectory into a genuine finite cycle of period $\operatorname{ord}_p(2)$. At the same time, the appeal to countable algebraic carriers ($\mathbb{N}$, $\mathbb{Z}[X]$, $K[t]$, formal series $K[[t]]$) is completely legitimate already within Book I, since every coefficient and every finite Hankel minor is computed by a finite number of arithmetic operations without limiting passages, metrics, or analytic convergence.

```text
  HANKEL MATRIX H(a): CONSTANCY ON ANTIDIAGONALS i + j = n AND ROW SHIFT R_{i+1} = S(R_i)

           j=0   j=1   j=2   j=3
    R_0 [  a_0   a_1   a_2   a_3  ... ]  <-- original sequence a
    R_1 [  a_1   a_2   a_3   a_4  ... ]  <-- single shift S(a)
    R_2 [  a_2   a_3   a_4   a_5  ... ]  <-- double shift S^2(a)
    R_3 [  a_3   a_4   a_5   a_6  ... ]  <-- if R_r = c_1 R_{r-1} + ... + c_r R_0, then
                                             also R_{r+k} = c_1 R_{r+k-1} + ... + c_r R_k for all k >= 0!
```
**Fig. I.8.2.** Structure of the Hankel matrix $H(a)_{i,j} = a_{i+j}$ as a table of shifts of a single stream of observations.  
Along each antidiagonal $i + j = n$ stands one and the same measurement $a_n$, and passing from row $R_i$ to row $R_{i+1}$ coincides with discarding the first sample $S(a)_n = a_{n+1}$. Therefore the very first linear dependence among rows $R_0, \dots, R_r$ is automatically reproduced by the shift $S^k$ across the entire infinite depth of the table and is equivalent to a linear recurrence law with constant coefficients.

Let us prove Kronecker's classical theorem in an exact algebraic form that explicitly retains both the pole denominator $Q(t)$ and the initial transient numerator $P(t)$ from Trap 3.

> **Theorem I.8.3 (Kronecker's criterion for finite Hankel rank and rationality of a series).**  
> *Classical foundation.* Kronecker's theorem (1881) on the equivalence between finite rank of an infinite Hankel matrix $H(a)_{i,j} = a_{i+j}$ and rationality of the generating series $\sum_{n \ge 0} a_n t^n = P(t)/Q(t)$. *Contribution of this book:* Reading the Hankel matrix as the linear counterpart of the Nerode quotient "past shifts vs. future delays" with exact formula $\mathrm{rk}_K H(a) = \max(\deg Q, \deg P + 1)$ for $P \ne 0$, accounting for the $+1$ transient-impulse shift.
> Let $a = (a_n)_{n \ge 0}$ be a sequence of elements of a field $K$, and let $F(t) = \sum_{n=0}^{\infty} a_n t^n \in K[[t]]$ be its formal generating series. The following three conditions are equivalent:
> 1. The rank of the infinite Hankel matrix $H(a) = (a_{i+j})_{i,j \ge 0}$ over the field $K$ is finite: $\operatorname{rank}_K H(a) = r < \infty$ (that is, the supremum of the ranks of all finite submatrices equals $r$).
> 2. Starting from some index $n_0 \ge 0$, the sequence satisfies a linear recurrence relation $a_{n+d} + q_1 a_{n+d-1} + \dots + q_d a_n = 0$ ($n \ge n_0$).
> 3. The formal series $F(t)$ is rational and is uniquely written as an irreducible fraction $F(t) = \frac{P(t)}{Q(t)}$ with $P, Q \in K[t]$, $Q(0) = 1$, and $\gcd(P, Q) = 1$.
>
> When these conditions hold, the Hankel rank is expressed through the degrees of the irreducible polynomials $P$ and $Q$ by the exact formula (with the convention $\deg 0 = -\infty$):
> $$\operatorname{rank}_K H(a) \;=\; \max\bigl(\deg P + 1,\; \deg Q\bigr),$$
> and the first $r$ rows $R_0, R_1, \dots, R_{r-1}$ form a basis of the row space of the matrix $H(a)$.

*Proof.*  
**(1 $\implies$ 2 $\implies$ 3).** Let $\dim_K \operatorname{span}\{R_i\}_{i \ge 0} = r < \infty$. Since $R_{i+1} = S(R_i)$, in the chain $R_0, R_1, \dots, R_r$ there is a first row $R_m$ ($m \le r$) that is a linear combination of the preceding ones: $R_m + c_1 R_{m-1} + \dots + c_m R_0 = 0$. Applying the linear shift $S^k$ for any $k \ge 0$, we obtain $R_{m+k} + c_1 R_{m+k-1} + \dots + c_m R_k = 0$, so all rows of the matrix lie in $\operatorname{span}(R_0, \dots, R_{m-1})$, whence $m = r$ and $R_0, \dots, R_{r-1}$ are linearly independent. Writing out the equality for $R_r$ coordinatewise, we have $a_{n+r} + c_1 a_{n+r-1} + \dots + c_r a_n = 0$ for all $n \ge 0$, which gives condition (2) with $n_0 = 0$ and $d = r$. Let us now show in general form the implication **(2 $\implies$ 3)** for an arbitrary recurrence onset threshold $n_0 \ge 0$: suppose $a_{n+d} + q_1 a_{n+d-1} + \dots + q_d a_n = 0$ for all $n \ge n_0$. Multiply the formal series $F(t) = \sum_{n=0}^{\infty} a_n t^n$ by the polynomial $\widetilde{Q}(t) = 1 + q_1 t + \dots + q_d t^d$ ($\widetilde{Q}(0) = 1$). The coefficient of the product $\widetilde{P}(t) = \widetilde{Q}(t) F(t)$ at each power $t^{n+d}$ with $n \ge n_0$ (i.e., at all powers $t^m$ with $m \ge n_0 + d$) equals $a_{n+d} + q_1 a_{n+d-1} + \dots + q_d a_n = 0$, so all terms of degree $\ge n_0 + d$ vanish and $\widetilde{P}(t) \in K[t]$ is a polynomial of degree $< n_0 + d$ (in particular, at $n_0 = 0$ and $d = r$ we have $\deg \widetilde{P} \le r - 1$). Dividing $\widetilde{P}$ and $\widetilde{Q}$ by their greatest common divisor with constant term $1$, we obtain the unique irreducible representation $F(t) = P(t)/Q(t)$ with $Q(0) = 1$ and $\gcd(P, Q) = 1$.  
**(3 $\implies$ 1 and the exact rank formula).** Conversely, let $F(t) = P(t)/Q(t)$ be irreducible, $Q(t) = 1 + q_1 t + \dots + q_d t^d$ ($\deg Q = d$, $q_d \neq 0$ for $d \ge 1$), and $m_* = \max(\deg P + 1, d)$. In the ring of formal series, the equality $Q(t) F(t) = P(t)$ means that for all $l \ge \deg P + 1$ the coefficient of $t^l$ in $Q(t) F(t)$ equals zero. Consider the shift operator $Q_{\mathrm{rev}}(S) = S^d + q_1 S^{d-1} + \dots + q_d I$; the vector $w = Q_{\mathrm{rev}}(S) a$ has coordinates $w_n = a_{n+d} + q_1 a_{n+d-1} + \dots + q_d a_n$, equal to the coefficient of $t^{n+d}$ in $Q(t) F(t) = P(t)$. Therefore $w_n = 0$ for all $n + d \ge \deg P + 1$, that is, $S^e w = 0$ for $e = \max(0, \deg P + 1 - d)$. Thus the polynomial $M(S) = S^e Q_{\mathrm{rev}}(S)$ of degree $e + d = \max(\deg P + 1, d) = m_*$ annihilates the sequence $a$: $M(S) a = 0$, whence $\operatorname{rank}_K H(a) \le m_*$. Suppose there exists an annihilating polynomial $A(S) = S^r + b_1 S^{r-1} + \dots + b_r I$ of smaller degree $r < m_*$. Then from the first step of the proof $F(t) = \widetilde{P}(t)/\widetilde{Q}(t)$ with $\deg \widetilde{P} \le r - 1$ and $\deg \widetilde{Q} \le r$; by uniqueness of the irreducible fraction, $P \mid \widetilde{P}$ and $Q \mid \widetilde{Q}$, whence $\deg P \le r - 1$ and $\deg Q \le r$, i.e., $m_* = \max(\deg P + 1, \deg Q) \le r$—a contradiction. Hence $\operatorname{rank}_K H(a) = m_* = \max(\deg P + 1, \deg Q)$. $\square$

See how transparently this theorem covers all extreme cases: for the identically zero sequence $a \equiv 0$ we have $P(t) = 0$ ($\deg 0 = -\infty$) and $Q(t) = 1$ ($\deg Q = 0$), so the formula gives $\operatorname{rank}_K H(0) = \max(-\infty, 0) = 0$ (empty row basis); for the delayed impulse from Trap 3, $a = (0, 1, 0, 0, \dots)$, we have $P(t) = t$ ($\deg P = 1$) and $Q(t) = 1$ ($\deg Q = 0$), so $e = \max(0, 2 - 0) = 2$, the minimal annihilating shift operator is $S^2 a = 0$, and the Hankel rank equals $\max(1 + 1, 0) = 2$. And for every non-zero purely periodic or exponential-polynomial sequence without an initial transient ($\deg P < \deg Q$), the formula immediately yields the familiar equality $\operatorname{rank}_K H(a) = \deg Q$.

---

## §I.8.5. Power Sum $s_n = 1^n + 2^n + 4^n$ and Drop of Hankel Rank Modulo a Prime

Let us now join **both hemispheres of the chapter** in a single calculation: take an integer sequence of finite Hankel rank and look at it through modular windows $\bmod p$.

Suppose a hidden system consists of three independent geometric modes with multipliers $1, 2, 4$ and outputs the integer power sum

$$s_n \;=\; 1^n + 2^n + 4^n \qquad (n = 0, 1, 2, \dots): \qquad 3,\; 7,\; 21,\; 73,\; 273,\; 1057,\; 4161,\; \dots$$

Its generating series equals the sum of three simple fractions:

$$F(t) \;=\; \frac{1}{1 - t} + \frac{1}{1 - 2t} + \frac{1}{1 - 4t} \;=\; \frac{3 - 14t + 14t^2}{1 - 7t + 14t^2 - 8t^3},$$

so for all $n \ge 0$ the third-order recurrence law $s_{n+3} = 7 s_{n+2} - 14 s_{n+1} + 8 s_n$ holds. Let us write out the $4 \times 4$ corner window of the Hankel matrix $H^{(4)}(s)$ and compute its leading principal minors $\Delta_1, \Delta_2, \Delta_3, \Delta_4$ over $\mathbb{Z}$:

$$H^{(4)}(s) \;=\; \begin{pmatrix} 3 & 7 & 21 & 73 \\ 7 & 21 & 73 & 273 \\ 21 & 73 & 273 & 1057 \\ 73 & 273 & 1057 & 4161 \end{pmatrix}, \qquad \begin{aligned} \Delta_1 &= 3, \\ \Delta_2 &= 3 \cdot 21 - 7^2 = 14 = 2 \cdot 7, \\ \Delta_3 &= \det H^{(3)}(s) = 36 = 2^2 \cdot 3^2, \\ \Delta_4 &= \det H^{(4)}(s) = 0. \end{aligned}$$

Where does the number $\Delta_3 = 36 = 6^2$ come from? Notice that the block $H^{(3)}(s)$ factors into the product of the transposed Vandermonde matrix of the nodes $(1, 2, 4)$ with itself:

$$H^{(3)}(s) \;=\; V^\top V, \qquad V \;=\; \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2^2 \\ 1 & 4 & 4^2 \end{pmatrix}, \qquad \det V \;=\; (2 - 1)(4 - 1)(4 - 2) \;=\; 1 \cdot 3 \cdot 2 \;=\; 6,$$

whence $\Delta_3 = (\det V)^2 = 6^2 = 36$. This Vandermonde factorization instantly reveals the internal mechanics of modular windows: the determinant $\Delta_3 = 2^2 \cdot 3^2$ vanishes modulo a prime $p$ if and only if **two of the three frequencies $\{1, 2, 4\}$ merge with each other modulo $p$** (under the convention $0^0 = 1$ at the zero sample $n = 0$, the mere passage of a non-zero node into $0 \bmod p$ by itself does not annihilate the determinant of $V$ if all three node residues in $\mathbb{F}_p$ remain pairwise distinct—for instance, for the nodes $\{0, 1, 2\}$ over $\mathbb{F}_5$; but for our triple $\{1, 2, 4\}$, at $p = 3$ the nodes $4 \equiv 1 \pmod 3$ merge, while at $p = 2$ both even modes $2 \equiv 4 \equiv 0 \pmod 2$ merge with each other).

> **Lemma I.8.3 (Law of non-increase and modular collapse of Hankel rank).**  
> *Classical foundation.* Vandermonde determinant of an exponential sum $s_n = \sum_{j=1}^r \lambda_j^n$ and rank reduction of integer matrices modulo a prime $p$. *Contribution of this book:* Mechanism of Hankel rank drop under collision of characteristic roots modulo $p$ (`[1, 2, 3, 3]` for $1^n + 2^n + 4^n$ over $\mathbb{F}_{2,3,5,7}$) and safeguard against stopping early at a spurious vanishing intermediate minor ($\Delta_2 = 14 \equiv 0 \pmod 7$ while $\Delta_3 = 36 \equiv 1 \pmod 7$).
> For any integer sequence $s \in \mathbb{Z}^{\mathbb{N}}$ and any prime $p$, reduction of the sequence modulo $p$ ($\bar{s}_n = s_n \bmod p \in \mathbb{F}_p$) does not increase the Hankel rank: $\operatorname{rank}_{\mathbb{F}_p} H(\bar{s}) \le \operatorname{rank}_{\mathbb{Q}} H(s)$. On the reference stream $s_n = 1^n + 2^n + 4^n$ ($\operatorname{rank}_{\mathbb{Q}} H(s) = 3$), the modular window distinguishes three exact regimes:
> 1. for all primes $p \ge 5$ (in particular, $p = 5$ and $p = 7$), the nodes $1, 2, 4 \bmod p$ are non-zero and pairwise distinct, $\Delta_3 = 36 \not\equiv 0 \pmod p$, and all three degrees of memory are fully visible: $\operatorname{rank}_{\mathbb{F}_p} H(\bar{s}) = 3$ (moreover, at $p = 7$ the intermediate minor $\Delta_2 = 14 \equiv 0 \pmod 7$ vanishes accidentally, yet $\Delta_3 \equiv 1 \pmod 7$ retains rank $3$);
> 2. at $p = 3$, the frequency $4 \equiv 1 \pmod 3$ merges with the frequency $1$: the stream turns into $\bar{s}_n \equiv 2 \cdot 1^n + 2^n \pmod 3 = (0, 1, 0, 1, \dots)$, the minor $\Delta_3 = 36 \equiv 0 \pmod 3$ is extinguished, while $\Delta_2 = 14 \equiv 2 \pmod 3$ remains non-zero, and the rank drops to $\operatorname{rank}_{\mathbb{F}_3} H(\bar{s}) = 2$;
> 3. at $p = 2$, both even modes $2^n$ and $4^n$ vanish already from $n = 1$, and at $n = 0$ they give $1 + 1 + 1 = 3 \equiv 1 \pmod 2$, so that the entire stream turns into the unit constant $(1, 1, 1, 1, \dots)$ and compresses to $\operatorname{rank}_{\mathbb{F}_2} H(\bar{s}) = 1$.

*Proof.* Every minor of order $k$ that equals zero in $\mathbb{Z}$ remains zero after reduction modulo $p$, so $\operatorname{rank}_{\mathbb{F}_p} H(\bar{s}) \le \operatorname{rank}_{\mathbb{Q}} H(s)$. For $s_n = 1^n + 2^n + 4^n$, the equality $\Delta_4 = 0$ and the recurrence identity $s_{n+3} = 7 s_{n+2} - 14 s_{n+1} + 8 s_n$ are preserved under reduction modulo any $p$, so the rank does not exceed $3$. For $p \ge 5$, the number $36 = 2^2 \cdot 3^2$ is not divisible by $p$, hence $\det_{\mathbb{F}_p} H^{(3)}(\bar{s}) \neq 0$ and the rank equals $3$. At $p = 3$, we have $\bar{s}_n = (2 + (-1)^n) \bmod 3$, whence $F_{\mathbb{F}_3}(t) = \frac{t}{1 - t^2}$ with $\deg Q = 2 > \deg P = 1$ and rank $2$ by Theorem `I.8.3`. At $p = 2$, we have $\bar{s}_n = 1$ for all $n \ge 0$, $F_{\mathbb{F}_2}(t) = \frac{1}{1 - t}$, and the rank equals $1$. $\square$

Notice in passing an instructive detail at $p = 7$: the second-order corner minor $\Delta_2 = 14$ is divisible by $7$, and a naive algorithm that stops checking the rank at the very first zero corner minor $\Delta_k = 0$ would erroneously conclude that the rank over $\mathbb{F}_7$ equals $1$. Meanwhile, the next corner minor $\Delta_3 = 36 \equiv 1 \pmod 7$ is non-zero, restoring the true rank $3$: on symmetric Hankel matrices with zero intermediate windows, the rank must be verified by full Gaussian elimination (or by the Berlekamp–Massey algorithm taking jump length into account), not by blindly stopping at the first singular minor.

---

## §I.8.6. Nonlinear Polynomial Compression Over $\mathbb{F}_p$: The Odd Cubic and the Boundary of Global Collapse

In the preceding section, the transition from step $n$ to step $n+1$ was linear. Let us now pose the closing question of the chapter: **what happens in a finite modular window $\mathbb{F}_p$ if the iteration step is given by a nonlinear polynomial with the odd sign symmetry from Chapter `I.5`?**

Consider the simplest sign attractor $T_0 = \{-1, 0, +1\} \subset \mathbb{F}_p$ for primes $p \ge 5$ and construct the canonical odd interpolation polynomial of degree three that sends the non-zero nodes $\{\pm 1, \pm 2, \pm 3\}$ inside the sign pair $\{\pm 1\}$, flipping the sign on the first two shells and retaining it on the third:

$$K_2(0) = 0, \quad K_2(\pm 1) = \mp 1, \quad K_2(\pm 2) = \mp 1, \quad K_2(\pm 3) = \pm 1 \quad\Longrightarrow\quad K_2(u) \;=\; \frac{u^3 - 7u}{6}.$$

Since the denominator equals $6 = 2 \cdot 3$, for any prime $p \ge 5$ the inverse element $6^{-1} \bmod p$ is uniquely defined, and the formula $u \mapsto K_2(u) \bmod p$ defines a finite map $\mathbb{F}_p \to \mathbb{F}_p$. Moreover, thanks to oddness $K_2(-u) \equiv -K_2(u) \pmod p$, opposite residues $\pm u$ move strictly mirror-wise: it suffices to track only the $(p + 1)/2$ unsigned representatives $\{0, 1, 2, \dots, (p-1)/2\}$.

Let us trace the fate of all residues across three successive prime windows $p = 5, 7, 11$:

| Prime field $\mathbb{F}_p$ | Inverse $6^{-1} \bmod p$ | Action of $K_2(u) \bmod p$ on the half-scale $0 \le u \le (p-1)/2$ | Do all orbits fall into $T_0 = \{-1, 0, +1\}$? |
| :---: | :---: | :--- | :--- |
| **$\mathbb{F}_5$** | $6 \equiv 1 \implies 6^{-1} = 1$ | $0 \mapsto 0;\; 1 \mapsto 4 \equiv -1;\; 2 \mapsto (8 - 14) \equiv 4 \equiv -1$ | **YES** (all $5$ residues compress in $1$ step) |
| **$\mathbb{F}_7$** | $6 \equiv -1 \implies 6^{-1} = 6$ | $0 \mapsto 0;\; 1 \mapsto 6 \equiv -1;\; 2 \mapsto 6 \equiv -1;\; 3 \mapsto 1$ | **YES** (all $7$ residues compress in $1$ step) |
| **$\mathbb{F}_{11}$** | $6 \cdot 2 = 12 \equiv 1 \implies 6^{-1} = 2$ | $0 \mapsto 0;\; 1 \mapsto 10 \equiv -1;\; 2 \mapsto 10;\; 3 \mapsto 1;\; \mathbf{4 \mapsto 6 \equiv -5};\; \mathbf{5 \mapsto 4}$ | **NO.** Closed 4-cycle $5 \to 4 \to 6 \to 7 \to 5$ |

Let us pause at the window $p = 11$. On the nodes $0, \pm 1, \pm 2, \pm 3$ the polynomial worked exactly as in the integers, instantly pulling $7$ out of the $11$ elements of the field into the core $\{-1, 0, +1\}$. Yet the very first residues outside the interpolation box—four and five—formed in $\mathbb{F}_{11}$ a self-sustaining non-trivial cycle of length $4$:

$$K_2(5) \equiv 2(125 - 35) = 180 \equiv 4, \quad K_2(4) \equiv 2(64 - 28) = 72 \equiv 6 \equiv -5, \quad K_2(6) \equiv -4 \equiv 7, \quad K_2(7) \equiv -(-5) = 5 \pmod{11}!$$

In the unsigned quotient space $\mathbb{F}_{11}/\{\pm 1\}$ this is a 2-cycle $\{5\} \leftrightarrow \{4\}$, forever separated from the attractor $\{0, 1\}$.

> **Proposition I.8.1 (Properties of the odd compression cubic and infinitude of prime windows with non-trivial fixed points).**  
> *Classical foundation.* Arithmetic of finite prime fields $\mathbb{F}_p$, Gauss's law of quadratic reciprocity, and infinitude of primes satisfying $\left(\frac{13}{p}\right) = +1$. *Contribution of this book:* Complete dynamical analysis of the odd interpolation polynomial $K_2(u) = (u^3 - 7u)/6$ modulo $p$: single-step collapse of the entire field into the ternary core $\{-1,0,+1\}$ precisely for $p \in \{5, 7\}$, birth of the 4-cycle `5 → 4 → 6 → 7` at $p = 11$, and fixed points $u^2 \equiv 13 \pmod p$.
> The map $K_2(u) = (u^3 - 7u)/6 \bmod p$ is well-defined over every prime field $\mathbb{F}_p$ for $p \ge 5$, commutes with sign flip $K_2(-u) = -K_2(u)$, sends $T_0 = \{-1, 0, +1\}$ into itself ($0 \mapsto 0$, $\pm 1 \mapsto \mp 1$), and in one step contracts the entire field $\mathbb{F}_p$ into $T_0$ for $p \in \{5, 7\}$, but already at $p = 11$ possesses an external 4-cycle $(5 \to 4 \to 6 \to 7 \to 5)$ outside $T_0$. Moreover, there exist infinitely many prime numbers $p$ for which the map $K_2$ has in $\mathbb{F}_p \setminus T_0$ two fixed points $u_* \neq 0, \pm 1$ ($K_2(u_*) = u_*$) and consequently does not contract $\mathbb{F}_p$ into $T_0$.

*Proof.* The formulas at $p = 5, 7, 11$ were verified above by direct calculation in $\mathbb{F}_p$ (with $K_2(1) = -1$ and $K_2(-1) = 1$ for all $p \ge 5$). The fixed-point equation $K_2(u) \equiv u \pmod p$ for $p \ge 5$ is equivalent to
$$u^3 - 7u \equiv 6u \pmod p \quad\Longleftrightarrow\quad u(u^2 - 13) \equiv 0 \pmod p.$$
If a prime $p \ge 5$, $p \neq 13$, divides at least one value of the quadratic polynomial $G(n) = n^2 - 13$ ($n \in \mathbb{Z}$), then in $\mathbb{F}_p$ there exist two opposite roots $u_* \equiv \pm n \pmod p$ of the congruence $u^2 \equiv 13 \pmod p$. For $p \ge 5$ these roots cannot lie in $T_0 = \{-1, 0, +1\}$, since $0^2 - 13 = -13 \not\equiv 0 \pmod p$ (for $p \neq 13$) and $(\pm 1)^2 - 13 = -12 = -2^2 \cdot 3 \not\equiv 0 \pmod p$ (for $p \ge 5$). It remains to verify by elementary means (without appealing to analytic number theory) that there are infinitely many prime divisors of the set of values $\{n^2 - 13 : n \in \mathbb{Z}_{>0}\}$: if their finite list were exhausted by primes $p_1, \dots, p_m$, then for $M = p_1 \cdots p_m$ and any $t \ge 1$, upon substituting $n = 13 M t$ the number
$$G(13 M t) = 13^2 M^2 t^2 - 13 = 13 \bigl(13 M^2 t^2 - 1\bigr)$$
would have a factor $13 M^2 t^2 - 1 > 1$ (for $t \ge 1$) coprime both to $13$ and to each $p_i \mid M$. Therefore any prime divisor $q \mid (13 M^2 t^2 - 1)$ is a new prime number $q \notin \{13, p_1, \dots, p_m\}$, for which the congruence $13 M^2 t^2 \equiv 1 \pmod q$, after multiplying both sides by $13$, gives $(13 M t)^2 = 13 \cdot 13 M^2 t^2 \equiv 13 \pmod q$, i.e., the residue $u_* = 13 M t \bmod q$ satisfies $u_*^2 \equiv 13 \pmod q$, a contradiction. (In particular, already at $p = 17, 23, 29, 43, 53, 61, 79, 101, 103, 107, 113, 127, 131, 139, 157, 173, 181, 191, 197$ the quadratic residue $u^2 \equiv 13 \pmod p$ gives two fixed points outside $T_0$; Schur's analogous elementary lemma on the infinitude of prime divisors of a non-constant integer polynomial rules out global collapse for an infinite set of primes $p$ (refuting complete collapse for all sufficiently large $p$) for any polynomial $f(u)$ for which $f(u) - u$ or $f(f(u)) - u$ has a non-constant divisor without roots in $T_0$.) $\square$

Let us note as an external reference landmark the scale of this phenomenon in an external computational survey of polynomial compression maps over $\mathbb{F}_p$ (which lies beyond the self-contained core of the present book): for a systematic family of `18` interpolation compression polynomials (`16` non-constant maps and `2` constant reference maps), an exhaustive sweep of all primes $p \le 10^6$ detects exactly `184` pairs of complete collapse $(f, p)$ for non-constant maps, while targeted finite certificates in the window $p \le 10^{10}$ bring this number to `223` certified pairs—vividly illustrating that global compression of an entire field $\mathbb{F}_p$ into three sign poles is a rare resonance of small and medium windows rather than a universal identity of large characteristics.

---

## §I.8.7. Categorical Anchoring of the Chapter

Let us summarize the linear hemisphere of the chapter in a strict categorical form for observable shift systems over a field $K$:

- **Objects:** triples $(W, S_W, \ell)$, where $W$ is a vector space over a field $K$, $S_W : W \to W$ is a linear step endomorphism, and $\ell : W \to K$ is a linear functional of single-shot window reading.
- **Morphisms:** a morphism $\varphi : (W, S_W, \ell) \to (W', S_{W'}, \ell')$ in the category $\mathbf{LinObs}_K$ is a $K$-linear map $\varphi : W \to W'$ intertwining the step ($\varphi \circ S_W = S_{W'} \circ \varphi$) and preserving the window ($\ell' \circ \varphi = \ell$).
- **Identities and composition:** the identity linear operator $\mathrm{id}_W$ and ordinary composition of linear maps.
- **Preserved structure:** every initial state vector $w \in W$ generates an observable scalar sequence $\mathcal{O}(w) = \bigl(\ell(S_W^n w)\bigr)_{n \ge 0} \in K^{\mathbb{N}}$, and every morphism in $\mathbf{LinObs}_K$ preserves the observed trace: $\mathcal{O}'(\varphi(w)) = \mathcal{O}(w)$.
- **Universal property:** the space of all sequences $(K^{\mathbb{N}}, S, \mathrm{ev}_0)$ with the left shift $S(a)_n = a_{n+1}$ and reading of the zeroth term $\mathrm{ev}_0(a) = a_0$ is the **terminal (couniversal) object** of the category $\mathbf{LinObs}_K$: the map $\mathcal{O} : W \to K^{\mathbb{N}}$ is the unique morphism from $(W, S_W, \ell)$ to $(K^{\mathbb{N}}, S, \mathrm{ev}_0)$. Moreover, the image of the cyclic subspace $\operatorname{span}\{S_W^n w\}_{n \ge 0}$ under the action of $\mathcal{O}$ coincides precisely with the row space of the Hankel matrix $H(\mathcal{O}(w))$, and its dimension equals $\operatorname{rank}_K H(\mathcal{O}(w))$.
- **Detected trap and failure:** when passing from the field $K = \mathbb{Q}$ to modular reduction over a ring $\mathbb{Z}/N\mathbb{Z}$ with composite $N$ (or with shared window divisors $\gcd(m_1, m_2) > 1$), linear independence and division by a leading minor lose their force on zero divisors—therefore over a composite modulus one examines the oracle-free probe $\gcd(N, r)$ from `§§I.8.1–I.8.3`, while over prime fields $\mathbb{F}_p$ the Hankel rank can drop abruptly when roots of the denominator merge (`Lemma I.8.3`).

---

### Historical-Philosophical Note: Inference from a Visible Sign (*anumāna / liṅga*) in Nyāya and Sāṃkhya

1. **Motif of the classical source.** In the classical Indian epistemology of Nyāya (*Nyāya-sūtras* `1.1.5`) and Sāṃkhya (*Sāṃkhya-kārikā* `SK 5–6`), alongside direct perception (*pratyakṣa*) stands strict logical inference (*anumāna*) about an object not directly observed from its visible mark-sign (*liṅga*) on the basis of an invariable concomitant connection (*vyāpti*)—the classic example of inferring hidden fire on a distant mountain from an observed plume of smoke (*sāmānyato dṛṣṭam* in `SK 6` specifically singles out the cognition of structures that are in principle supersensible from their lawful manifestations), whereas a fallacious sign (*hetvābhāsa*), occurring both with and without fire, is rejected as a logical error.
2. **Strict realization in DOT.** This epistemological motif finds a twofold mathematical realization in the present chapter: first, in **the oracle-free contract of `Definition I.8.1`**, where the hidden axes of the torus $\mathbb{F}_p \times \mathbb{F}_q$ are inaccessible to direct perception, and the sole legitimate sign of hitting an axis is a non-trivial response of the Euclidean probe $1 < \gcd(N, r) < N$; second, in **Kronecker's Theorem `I.8.3`**, where the finite rank $r$ of the infinite Hankel matrix $H(a)$ unerringly determines the minimal dimension of the hidden linear memory (whereas in a finite observed window $H^{(m)}(a)$ of size $m \times m$, the rank is guaranteed to coincide with the global rank $r$ only after reaching the threshold $m \ge r$, provided not all initial samples lie in a smaller subspace). Conversely, the irreversible loss of the floor $25$ from the pair $(d_A, d_B) = (5, 5)$ without retained $r$ (`Trap 2`) and the spurious vanishing of the intermediate minor $\Delta_2 \equiv 0 \pmod 7$ alongside a non-zero $\Delta_3 \equiv 1 \pmod 7$ give exact mathematical specimens of a fallacious sign (*hetvābhāsa*).
3. **Boundary of comparison.** The classical doctrine of *anumāna* and *sāmānyato dṛṣṭam* clarifies the philosophical discipline of valid inference from a trace in a window, but by itself contains neither the Euclidean algorithm, nor complexity bounds for decomposing a composite number $N = pq$, nor Kronecker's theorem on rational series.

---

### Transition to Chapter `I.9`

In `Theorem I.8.2` we saw an encouraging fact: if a system of divisor windows $m_1, \dots, m_k \mid N$ is carved out of a single already existing ambient number $N$, then pairwise agreement of traces on the intersections $\gcd(m_i, m_j)$ suffices to assemble a single global divisor $d = \operatorname{lcm}_i d_i$. But is the world always arranged so cloudless when the ambient whole **is not given in advance**, and the observer has only a collection of local windows that are pairwise compatible on every common seam? In the concluding **Chapter `I.9`** of Book I we will discover that already on three windows pairwise compatibility of all seams is compatible with the complete absence of a global state, measure this obstruction by exact cohomologies over $\mathbb{F}_2$ on the four-state scene $S_4$, and bind together the results of the nine chapters of the first volume.

---

### Verifiability Passport of Chapter `I.8` (`Book I v3.3`)

- **Canonical node of the book:** `N08` (Chinese Remainder Theorem, contract of an oracle-free algorithm on a composite modulus $N=pq$, three regimes of divisor memory: primary saturation, descent/lift with probe $r$, and cover gluing by $\operatorname{lcm}$, Kronecker's theorem on Hankel rank taking the transient numerator into account, modular rank collapse on $s_n = 1^n + 2^n + 4^n$, odd compression cubic $K_2(u)$ over $\mathbb{F}_p$).
- **Exact `Julia 1.12.6` verifications (single-threaded mode, `Int / BigInt / Rational{BigInt}`, without `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gates `GATE-I08-A` (CRT on $N=45$, failure on $(4,6)$, oracle-free decomposition $60+1+16=77$ on $N=77$, saturation $x_{k+1}=\gcd(N,x_k^2)$ on $N=45, 360$, counterexample $N=25$, 7-operation lift with recovery of $r$, and cover bijection `36 -> 9` on $N=36$) and `GATE-I08-B` (transient impulse $(0,1,0,\dots)$ of rank $2$, minors $(3,14,36,0)$ with rank drops over $\mathbb{F}_2, \mathbb{F}_3$, cubic $K_2(u)$ at $p=5, 7$, and 4-cycle $5\to 4\to 6\to 7\to 5$ at $p=11$).
- **Specification index `Lean 4` (`status: planned`, full cards in Appendix `VP`):** `TNR.BookI.I08.crt_two_coprime`, `TNR.BookI.I08.algorithm_no_oracle_leak`, `TNR.BookI.I08.primary_saturation`, `TNR.BookI.I08.gcd_transfer_and_recovery`, `TNR.BookI.I08.lcm_cover_gluing`, `TNR.BookI.I08.hankel_rational_equivalence`, `TNR.BookI.I08.hankel_rank_mod_prime`, `TNR.BookI.I08.odd_cubic_collapse_and_cycle`.
- **Full 8-point passports of figures `Fig. I.8.1–I.8.2` and statement certification registry:** moved to [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
