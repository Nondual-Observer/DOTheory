# Chapter I.7. Addition and Multiplication: Additive and Divisor Questions About a Number

In Chapter `I.6` we verified on finite sets of six, seven, and fifteen elements that a bare list of vertices does not yet define any geometry: until an exact question of adjacency is declared in the operational contract $\Gamma = (X, \mathcal{Q}, \mathcal{A}, \mathrm{Dom}, \Pi, \Phi)$, the very same six terminals with equal right turn out to be three disconnected dumbbells $3K_2$, a connected octahedron $O_6$, or a hexagonal cycle $C_6$.

Let us now transfer this principle to the oldest and most familiar object of mathematics—**the natural and integer number**. School habit accustoms us to look at the number $6$, $12$, or $30$ as a single self-evident entity that "simultaneously has" both neighbors $n \pm 1$ and divisors $d \mid n$. However, from the observer's standpoint, addition and multiplication define on the very same set of numbers **two non-isomorphic operational contracts**. What in the additive window appears as a uniform infinite staircase of single steps $+1$, in the divisor window decomposes into multidimensional lattices of prime powers; and equations at the junction of sum and product ($1 + \pi(N) = N/2$, $x + y + z = xyz$, divisibility of a triangular sum by a primorial, or squareness of the number of projective ternary directions) exhibit rigid, at times completely unexpected finite windows of solvability.

The task of the present chapter is twofold. First, we will learn to strictly separate additive and multiplicative questions about one and the same numerical carrier, tracing the geometry of finite divisor lattices $D(N)$—from the Boolean cube of squarefree numbers to the rectangular towers of prime powers, which in Chapter `I.8` will become the working basis of modular windows. Second, on four classical number-theoretic problems we will practice a verification rule: **distinguishing a pattern that accidentally holds on the first small examples from an invariant proved across the entire domain of the contract**, and indicating the boundary beyond which a finite table gives way to an external analytic theorem.

---

## §I.7.1. Six Tokens Under Two Contracts and Loss of History in a Value

Let us pour six identical wooden tokens onto the table. The tokens themselves lie motionless, but we can conclude two completely different operational contracts regarding the number $6$.

**Contract one—additive counting ($\Gamma_{\mathrm{add}}$).** Let us line up the tokens in a row and allow one elementary action: push up one more token ($T_{+1}(n) = n + 1$) or remove an extreme one ($T_{-1}(n) = n - 1$ for $n \ge 1$). In this window, every positive integer has at most two immediate neighbors at a distance of one step: next to six stand five and seven, while two and three are separated from it by four and three successive ticks.

**Contract two—divisor packing ($\Gamma_{\mathrm{div}}$).** Let us ask differently: into what equal packs without remainder can this pile of tokens be decomposed? Now an elementary step connects a number $a$ with a number $b$ if $b$ is obtained from $a$ by multiplication by a single prime factor ($b = p \cdot a$). For six, the set of all its positive divisors is $V = \{1, 2, 3, 6\}$, and five and seven disappear altogether from its local window, whereas two and three turn out to be its immediate neighbors from below.

Let us place both edge rules onto **one and the same four-element carrier of labels** $V = \{1, 2, 3, 6\}$ and compare the resulting graphs:

```text
   ONE AND THE SAME CARRIER:  V = {1, 2, 3, 6}  (|V| = 4)

   (a) Additive step question |a - b| = 1          (b) Immediate covering question a | b
       [2 edges, disconnected graph P_3 ⊔ K_1]         [4 edges, connected square Q_2 ≅ C_4]

                                                                 6
        1 ─── 2 ─── 3         (6)                              /   \
                           isolated                           2     3
                                                               \   /
                                                                 1
```

**Reader's caption to `Fig. I.7.1`:** change of the connectivity graph on the four numbers $V = \{1, 2, 3, 6\}$ upon changing the operational question. In the additive window (a), the numbers $1, 2, 3$ form a short chain of length two, while $6$ is cut off into a separate isolated component. In the divisor window of immediate coverings (b), the very same four numbers assemble into a closed two-dimensional cube $Q_2$: from $1$ lead two independent prime steps ($\times 2$ and $\times 3$), converging at $6$.

Alongside the distinction of graphs on a single carrier stands **the distinction between an expression tree and a computed numerical value**. Look at three elementary arithmetic expressions:

$$e_1 = 2 + 2, \qquad e_2 = 2 \cdot 2, \qquad e_3 = 2^2.$$

The evaluation map $\mathrm{val} : E \to \mathbb{N}_0$ sends all three expressions to one and the same number $\mathrm{val}(e_1) = \mathrm{val}(e_2) = \mathrm{val}(e_3) = 4$. In the terms of Chapter `I.1`, the four on the display is a **non-injective reading window**, whose fiber over the answer $4$ contains at least three different construction histories. As long as we are interested only in the number of tokens in the resulting pile, compression to the number $4$ is sufficient. But as soon as the next step of experience depends on the *mode of generation*, the stored number is no longer enough. For instance, if we replace the base parameter $2 \mapsto x$ and pass to the functions $x + x = 2x$, $x \cdot x = x^2$, and $x^x$ (which already at $x = 3$ give three different answers $6 \neq 9 \neq 27$), the value $4$ does not contain these distinctions: the operation tree was erased during evaluation and, in order to preserve future behavior, must be stored in memory separately.

Let us now prove strictly that the additive and multiplicative worlds on natural numbers cannot be aligned by any renaming of elements—neither with zero nor without zero.

> **Proposition I.7.1 (Non-isomorphism of the additive and multiplicative structures of the natural series).**  
> *Classical foundation.* Non-isomorphism of the singly generated additive monoid $(\mathbb{N}, +, 0)$ and the freely countably generated multiplicative monoid $(\mathbb{N}_+, \cdot, 1)$, plus distributivity of the divisor lattice $D(N)$—classical arithmetic. *Contribution of this book:* Comparison of additive and divisor graphs on the shared four-element carrier $\{1,2,3,6\}$ ($P_3 \sqcup K_1$ vs. $Q_2$) and Booleanness criterion $D(N) \iff \mu(N) \ne 0$ with complement failure on squared floors of $D(12)$ and $D(45)$.
> 1. On the carrier of non-negative integers $\mathbb{N}_0 = \{0, 1, 2, \dots\}$, the commutative monoids $(\mathbb{N}_0, +, 0)$ and $(\mathbb{N}_0, \cdot, 1)$ are not isomorphic even as semigroups.
> 2. On the carrier of positive integers $\mathbb{Z}_{>0} = \{1, 2, 3, \dots\}$, if addition is shifted into the operation $a \oplus_1 b := a + b - 1$ with the same neutral element $1$, the monoids $(\mathbb{Z}_{>0}, \oplus_1, 1)$ and $(\mathbb{Z}_{>0}, \cdot, 1)$ are still not isomorphic.

*Proof.*  
1. In the multiplicative semigroup $(\mathbb{N}_0, \cdot)$ there exists an absorbing element $z = 0$ satisfying the identity $z \cdot n = z$ for all $n \in \mathbb{N}_0$. In the additive semigroup $(\mathbb{N}_0, +)$ no absorbing element exists: for any candidate $a \in \mathbb{N}_0$, the element $a + 1$ is strictly greater than $a$ and therefore $a + 1 \neq a$. Every isomorphism of semigroups preserves the property of an element being absorbing; consequently, there is no isomorphism.  
2. The monoid $(\mathbb{Z}_{>0}, \oplus_1, 1)$ is isomorphic to $(\mathbb{N}_0, +, 0)$ via the bijection $n \mapsto n - 1$ and is generated by a **single** element $2$ (whose multiples under the operation $\oplus_1$ exhaust all $1, 2, 3, \dots$). Suppose that the multiplicative monoid $(\mathbb{Z}_{>0}, \cdot, 1)$ is also generated by a single element $g \in \mathbb{Z}_{>0}$. Then the numbers $2$ and $3$ must be positive integer powers of $g$: $g^u = 2$ and $g^v = 3$ ($u, v \ge 1$), whence $2^v = g^{uv} = 3^u$, which is impossible due to the parity of the left-hand side and the oddness of the right-hand side. Consequently, $(\mathbb{Z}_{>0}, \cdot, 1)$ is not a monogenic monoid and is not isomorphic to $(\mathbb{Z}_{>0}, \oplus_1, 1)$. $\square$

Let us emphasize the exact meaning of what has been proved: the absence of an isomorphism of monoids does not at all mean that addition and multiplication are isolated from each other by a wall—on the contrary, all of number theory lives on their interaction in the ring $\mathbb{Z}$. It means only that **one cannot mechanically transfer properties of the additive step to the divisor step by coincidence of the carrier**: every transfer requires exhibiting a specific morphism and specifying which exact predicate it preserves.

---

## §I.7.2. Geometry of Divisor Windows $D(N)$: Boolean Cubes vs. Primary Towers

Let us look in more detail at how the finite divisor window $D(N) = \{d \in \mathbb{Z}_{>0} \mid d \mid N\}$ of an arbitrary positive integer $N$ is organized. By the fundamental theorem of arithmetic, the number $N$ factors uniquely up to the order of factors into prime powers:

$$N = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}, \qquad e_j \ge 1.$$

Every positive divisor $d \mid N$ is uniquely encoded by the tuple of exponents $(a_1, \dots, a_k)$, where $0 \le a_j \le e_j$ for all $j = 1, \dots, k$. Under this encoding:
- the divisibility relation $d \mid d'$ is equivalent to the coordinatewise inequality of exponents $a_j \le a'_j$;
- the greatest common divisor $\gcd(d, d')$ takes the coordinatewise minimum $\min(a_j, a'_j)$;
- the least common multiple $\operatorname{lcm}(d, d')$ takes the coordinatewise maximum $\max(a_j, a'_j)$.

From this one immediately sees the decisive geometric distinction between **squarefree numbers** (for which all exponents $e_j = 1$) and numbers divisible by the square of a prime ($e_j \ge 2$). Let us compare in a single figure three reference divisor lattices—for $N = 30 = 2 \cdot 3 \cdot 5$, $N = 12 = 2^2 \cdot 3$, and $N = 45 = 3^2 \cdot 5$:

```text
   (a) SQUAREFREE WINDOW D(30), 30 = 2·3·5        (b) NON-SQUAREFREE WINDOWS D(12) AND D(45)
       All exponents e_j = 1:                         Exponent e_1 = 2 stretches the cube into a 3×2 tower!
       Boolean 3-cube Q_3 (8 vertices, 12 edges)      (6 vertices, 7 covering edges — NOT a Boolean algebra!)

                     30                                    D(12), 12 = 2^2·3       D(45), 45 = 3^2·5
                   /  |  \
                 6   10   15                                  4 ────► 12              9 ────► 45
                /|   /|   /|                                  ▲        ▲              ▲        ▲
               2 +--5-+--3 |                                  2 ────►  6              3 ────► 15
               | /  | /  | /                                  ▲        ▲              ▲        ▲
               |/   |/   |/                                   1 ────►  3              1 ────►  5
                    1
       Complement d |-> 30/d separates into (1, 30):  Failure of complement d |-> N/d on the middle floor:
       for d = 2: gcd(2, 15) = 1, lcm(2, 15) = 30     in D(12) at d=2 we have 12/d=6, but gcd(2,6)=2 ≠ 1!
                                                      in D(45) at d=3 we have 45/d=15, but gcd(3,15)=3 ≠ 1!
```

**Reader's caption to `Fig. I.7.2`:** comparison of Boolean and non-Boolean divisor lattices. For the squarefree number $30 = 2 \cdot 3 \cdot 5$, each prime factor is either absent ($0$) or enters once ($1$), so the covering diagram of $D(30)$ is precisely the three-dimensional binary cube $Q_3$ from Chapter `I.6`, and the symmetry map $\nu_{30}(d) = 30/d$ forms a true Boolean complement. For the numbers $12 = 2^2 \cdot 3$ and $45 = 3^2 \cdot 5$, an intermediate power floor appears ($2$ between $1$ and $4$; $3$ between $1$ and $9$): on this middle floor, the reflection $d \mapsto N/d$ ceases to yield a coprime pair.

It is precisely this middle floor of a non-Boolean lattice ($3$ vs. $9$ inside $D(45)$) that in the next Chapter `I.8` will become the key to the primary saturation theorem: in order to slice the composite modulus $45$ into independent residue rings by the Chinese Remainder Theorem, the raw divisor $3$ will have to be raised by squaring to the full primary block $9 = 3^2$.

---

## §I.7.3. Three Traps of a Finite Window When Combining the Contracts $\Gamma_{\mathrm{add}}$ and $\Gamma_{\mathrm{div}}$

In `§§I.7.1–I.7.2` we established that on one and the same set of numbers one can conclude two structurally incompatible contracts: **the additive counting contract** $\Gamma_{\mathrm{add}}$ (where a step is the shift $n \mapsto n + 1$, and windows are initial segments $W_N = \{1, 2, \dots, N\}$) and **the multiplicative-divisor contract** $\Gamma_{\mathrm{div}}$ (where questions test divisibility $d \mid n$, and windows are divisor lattices $D(N)$). What happens when a finite observer tries to link the answers of both contracts across a finite observation window $W_N$?

The first natural support of any researcher is to compute the first five or ten values of $N$ and compare the readings of the additive and multiplicative sensors in a table. There is nothing wrong with this, as long as we remember three operational traps of finite inspection that arise specifically at the junction of $\Gamma_{\mathrm{add}}$ and $\Gamma_{\mathrm{div}}$:

1. **Trap of prolonged equilibrium in the window $W_N$.** The prime-counting function $\pi(N)$ (the counter of atoms of the contract $\Gamma_{\mathrm{div}}$ inside the additive window $W_N$) grows more slowly than half of the even window $N/2$, but on a small segment their difference freezes at one in three consecutive even windows ($N = 10, 12, 14$). To an observer tracking only the number of primes and not uncovering the complementary class of odd composite numbers, it might seem that such equilibrium windows will return again and again.
2. **Trap of a silently substituted carrier $X$ in the contract $\Gamma$.** The equation balancing sum and product $x + y + z = xyz$ has on positive integers $X_+ = \mathbb{Z}_{>0}^3$ a unique ordered triple $(1, 2, 3)$. Yet one need only imperceptibly expand the declared carrier of the contract from $\mathbb{Z}_{>0}^3$ to all integer triples $\mathbb{Z}^3$ (adding zero and negative signs from `Chapter I.5`) for uniqueness to instantly shatter into an infinite family of trivial balances $(-a, 0, a)$.
3. **Trap of a delayed primary floor ($q^2$).** The rule "the additive triangular sum $A(p) = 1 + 2 + \dots + p$ divides the multiplicative primorial $p\#$ of all primes up to $p$" holds at $p = 3$ and $p = 5$ (where both factors are squarefree); the first failure along the even square $2^2 \mid 4$ occurs at $p = 7$, while the first failure along the odd square $3^2 \mid 9$ hides all the way until the seventh prime number $p = 17$. In exactly the same way, in the staircase of projective ternary directions $R_d = (3^d - 1)/2$, squares appear at $d = 1, 2, 5$ ($1^2, 2^2, 11^2$), but a finite search by itself never replaces a theorem about all $d > 5$.

Let us examine these problems in turn, showing each time how the observer's position in DOT replaces empirical guessing from a small window $W_N$ by an exact structural invariant of the joint contract $\Gamma_{\mathrm{add}} \vee \Gamma_{\mathrm{div}}$.

---

## §I.7.4. Equilibrium Window $1 + \pi(N) = N/2$ and Counting Odd Composite Numbers

Let $\pi(N)$ denote the number of prime numbers on the segment $\{1, 2, \dots, N\}$ (by standard definition, the number one is not prime: $\pi(1) = 0$, $\pi(2) = 1$, $\pi(3) = 2$). Let us pose an exact question about the additive-multiplicative balance of a window of length $N$: **for which positive integers $N \in \mathbb{Z}_{>0}$ does one together with all prime numbers up to $N$ make up exactly half of the window?**

$$1 + \pi(N) = \frac{N}{2}.$$

Let us compile a verification table over the first even values $N = 2m$ (for odd $N$ the right-hand side is fractional while the left-hand side is integer, so odd $N$ drop out immediately):

| Even window $N = 2m$ | Half-window $m = N/2$ | Primes $\le N$ | $1 + \pi(N)$ | Odd composites $\le N$ (count $c(N)$) | Does $1+\pi(N)=N/2$ hold? |
| :---: | :---: | :--- | :---: | :--- | :---: |
| **$2$** | `1` | `2` ($\pi=1$) | `2` | none ($c = 0$) | no (`2 > 1`) |
| **$4$** | `2` | `2, 3` ($\pi=2$) | `3` | none ($c = 0$) | no (`3 > 2`) |
| **$6$** | `3` | `2, 3, 5` ($\pi=3$) | `4` | none ($c = 0$) | no (`4 > 3`) |
| **$8$** | `4` | `2, 3, 5, 7` ($\pi=4$) | `5` | none ($c = 0$) | no (`5 > 4`) |
| **`10`** | **`5`** | `2, 3, 5, 7` ($\pi=4$) | **`5`** | **`9 = 3²`** (**$c = 1$**) | **YES (`5 = 5`)** |
| **`12`** | **`6`** | `2, 3, 5, 7, 11` ($\pi=5$) | **`6`** | **`9 = 3²`** (**$c = 1$**) | **YES (`6 = 6`)** |
| **`14`** | **`7`** | `2, 3, 5, 7, 11, 13` ($\pi=6$) | **`7`** | **`9 = 3²`** (**$c = 1$**) | **YES (`7 = 7`)** |
| **$16$** | `8` | `2, 3, 5, 7, 11, 13` ($\pi=6$) | `7` | `9 = 3², 15 = 3·5` ($c = 2$) | no (`7 < 8`) |
| **$18$** | `9` | `2..17` ($\pi=7$) | `8` | `9, 15` ($c = 2$) | no (`8 < 9`) |

The fifth column of the table instantly turns the mysterious triple $\{10, 12, 14\}$ into a transparent theorem across the entire infinite ray $\mathbb{Z}_{>0}$.

> **Theorem I.7.1 (Exact equilibrium window $1 + \pi(N) = N/2$).**  
> *Classical foundation.* Elementary counting of even, prime, and odd composite integers on an initial segment $\{1,\dots,N\}$ of the natural numbers. *Contribution of this book:* Exact balance identity $m = \pi(2m) + c_{\mathrm{odd}}(2m)$ and complete proof that the equilibrium window $2(1 + \pi(N)) = N$ cuts out across all of $\mathbb{N}$ precisely the three integers $N \in \{10, 12, 14\}$ (corresponding to the unique odd composite $9$).
> In the domain of all positive integers $N \in \mathbb{Z}_{>0}$, the equality $1 + \pi(N) = N/2$ holds if and only if $N \in \{10, 12, 14\}$.

*Proof.* Since $1 + \pi(N) \in \mathbb{Z}$, the number $N$ must be even: $N = 2m$ ($m \in \mathbb{Z}_{>0}$). On the segment $\{1, 2, \dots, 2m\}$ there lie exactly $m$ odd numbers. Let us partition this set of odd numbers into three disjoint classes:
1. the unit itself $\{1\}$ ($1$ element);
2. all odd prime numbers $\le 2m$—since the unique even prime number $2$ already belongs to the segment $\{1,\dots,2m\}$, there are exactly $\pi(2m) - 1$ such odd primes;
3. all odd composite numbers $\le 2m$, whose count we denote by $c(2m) \ge 0$.

Adding the cardinalities of the three disjoint pieces, we obtain an exact identity for all $m \ge 1$:

$$m = 1 + \bigl(\pi(2m) - 1\bigr) + c(2m) = \pi(2m) + c(2m).$$

Substituting $m = \pi(N) + c(N)$ into the target equation $1 + \pi(N) = m$, we see that **for even $N = 2m$ it is equivalent to the condition $c(N) = 1$** (for odd $N$ the right-hand side $N/2$ is non-integer, so for instance odd $N = 9$ has $c(9) = 1$, but $1 + \pi(9) = 5 \neq 9/2$): on the segment from $1$ to even $N$ there must lie exactly one odd composite number. The smallest odd composite number is $3 \cdot 3 = 9$, and the next one after it is $3 \cdot 5 = 15$ (the numbers $11$ and $13$ are prime). Since the function $c(N)$ is non-decreasing as $N$ grows, the equality $c(N) = 1$ holds precisely for $9 \le N \le 14$. Intersecting this interval with the evenness $N = 2m$, we obtain the exhaustive list of solutions $N \in \{10, 12, 14\}$. $\square$

Let us appreciate the beauty of this simple derivation: we used no asymptotic estimates of the distribution of prime numbers—we simply chose the right partition of the odd half of the window and saw that the equation $1 + \pi(N) = N/2$ in reality asks: *"which even boundaries lie between the first odd composite number $9$ and the second odd composite number $15$?"*.

---

## §I.7.5. The Equation $x + y + z = xyz$ and the Satellite of a Prime Number: Cost of the Domain and the Hidden Square

Let us consider a second classical problem, where sum and product meet face to face without any auxiliary functions:

$$x + y + z = x y z.$$

Let us show how the answer to this question is entirely governed by **the declared domain of the carrier in the contract $\Gamma$**.

> **Theorem I.7.2 (Uniqueness of the positive triple for $x + y + z = xyz$ and splitting upon changing the domain).**  
> *Classical foundation.* The equation $x + y + z = xyz$ in natural numbers is a classical elementary Diophantine problem with the unique solution $\{1, 2, 3\}$ up to permutation. *Contribution of this book:* Model of how the solution count $|\mathcal{R}|$ shifts upon expanding the observer's carrier: the unique ordered triple $(1,2,3)$ in $\mathbb{N}_+^3$, $6$ permutations without ordering, and the infinite axial family $(-a, 0, a)$ upon passing to $\mathbb{Z}^3$.
> 1. In the domain of ordered positive integer triples $1 \le x \le y \le z$, the equation $x + y + z = xyz$ has the unique solution $(x, y, z) = (1, 2, 3)$.
> 2. In the domain of all unordered positive triples $\mathbb{Z}_{>0}^3$, there are exactly $3! = 6$ solutions (all permutations of $(1,2,3)$); and when the domain is expanded to all integer triples $\mathbb{Z}^3$, an infinite family of solutions $(-a, 0, a)$ ($a \in \mathbb{Z}$) arises alongside the signed reflections $(-3, -2, -1)$.

*Proof.*  
1. Let $1 \le x \le y \le z$ and $x + y + z = xyz$. If we assume $x \ge 2$, then also $y \ge 2$, whence the product $xyz \ge 2 \cdot 2 \cdot z = 4z$, whereas the sum does not exceed $x + y + z \le z + z + z = 3z$, contradicting the inequality $4z > 3z$ for $z \ge 1$. Consequently, necessarily $x = 1$. Substituting $x = 1$, we rewrite the equality $1 + y + z = yz$ in factored form:

$$yz - y - z + 1 = 2 \quad \Longleftrightarrow \quad (y - 1)(z - 1) = 2.$$

Since $0 \le y - 1 \le z - 1$ are non-negative integer divisors of the prime number $2$, the only option is $y - 1 = 1$ and $z - 1 = 2$, which gives $(x, y, z) = (1, 2, 3)$.  
2. Since the numbers $1, 2, 3$ are pairwise distinct, removing the ordering condition on $\mathbb{Z}_{>0}^3$ yields exactly $3! = 6$ triples. In the ring of all integers $\mathbb{Z}$, any triple $(-a, 0, a)$ gives the sum $(-a) + 0 + a = 0$ and the product $(-a) \cdot 0 \cdot a = 0$, forming an infinite ray of solutions. $\square$

Let us now pass to the third test—**the problem of the satellite of a prime number**, where the combination of an additive sum and a multiplicative primorial demonstrates the treachery of small tables. With each odd prime number $p \ge 3$ we associate two quantities:
- **the additive triangular sum** of the first $p$ natural numbers

$$A(p) := 1 + 2 + \dots + p = p \cdot \frac{p + 1}{2} = p \, h(p), \qquad h(p) := \frac{p + 1}{2} \in \mathbb{Z}_{>0};$$

- **the multiplicative primorial**—the product of all prime numbers not exceeding $p$:

$$p\# := \prod_{\substack{q \le p \\ q \text{ prime}}} q.$$

Let us ask: **when does the additive sum $A(p)$ evenly divide the multiplicative primorial $p\#$?**

| Odd prime $p$ | Half-sum $h(p) = (p+1)/2$ | Triangular sum $A(p) = p \cdot h(p)$ | Primorial $p\#$ | Is $h(p)$ squarefree? | Does $A(p) \mid p\#$? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$3$** | `2` | `6` | `6` | yes (`2`) | **YES** (`6 ∣ 6`) |
| **$5$** | `3` | `15` | `30` | yes (`3`) | **YES** (`15 ∣ 30`) |
| **`7`** | **`4 = 2²`** | `28` | `210` | **NO (`2² ∣ 4`)** | **NO** (`28 ∤ 210`, first failure) |
| **$11$** | `6 = 2·3` | `66` | `2 310` | yes (`2·3`) | **YES** (`66 ∣ 2 310`) |
| **$13$** | `7` | `91` | `30 030` | yes (`7`) | **YES** (`91 ∣ 30 030`) |
| **`17`** | **`9 = 3²`** | `153` | `510 510` | **NO (`3² ∣ 9`)** | **NO** (`153 ∤ 510 510`, failure at $3^2$) |
| **$19$** | `10 = 2·5` | `190` | `9 699 690` | yes (`2·5`) | **YES** (`190 ∣ 9 699 690`) |

> **Theorem I.7.3 (Squarefreeness criterion of the half-sum for the divisibility $A(p) \mid p\#$).**  
> *Classical foundation.* Factorization of the primorial $p\# = \prod_{q \le p} q$ into first-power primes and arithmetic of triangular numbers $T_p = p(p+1)/2$. *Contribution of this book:* Exact criterion for membership of the prime satellite $A(p) = p(p+1)/2$ in the Boolean divisor lattice of the primorial $D(p\#)$ via squarefreeness of the half-step $h(p) = (p+1)/2$, explaining the first squared breakdowns at $p = 7$ ($h=4$) and $p = 17$ ($h=9$).
> For every odd prime number $p \ge 3$, the triangular sum $A(p) = p(p+1)/2$ divides the primorial $p\#$ if and only if the integer $h(p) = (p+1)/2$ is squarefree (is not divisible by the square of any prime number $q^2$).

*Proof.* For $p \ge 3$, the integer $h(p) = (p+1)/2$ satisfies the strict inequalities $2 \le h(p) < p$. Therefore all prime divisors of $h(p)$ are strictly less than $p$; in particular, $\gcd(p, h(p)) = 1$, and every prime divisor $q \mid h(p)$ is already present among the factors of the primorial $p\# = \prod_{q \le p} q$. By definition of the primorial, each prime $q \le p$ enters the canonical factorization of $p\#$ in the **first** power ($v_q(p\#) = 1$). Since $A(p) = p \cdot h(p)$ and $\gcd(p, h(p)) = 1$, the divisibility $p \cdot h(p) \mid p\#$ is equivalent to the inequalities $v_q(h(p)) \le v_q(p\#) = 1$ holding for all primes $q < p$, which by definition means the squarefreeness of $h(p)$. $\square$

In classical number theory, the indicator of squarefreeness is the square of the Möbius function $\mu(h(p))^2 = 1$ (that is, $\mu(h(p)) \neq 0$). Let us place a useful terminological note of caution here: in the next Chapter `I.8`, when comparing the least common multiple with addition, we will encounter the integer multiplicative-additive gap $\Delta_\otimes(a,b) = \operatorname{lcm}(a,b) - (a+b)$, while in Chapter `I.9` and in Volume II we will encounter the topological Möbius strip with a flip of the sign sheet along a non-trivial cycle. These three constructions belong to different floors of the book and are never identified with one another.

---

## §I.7.6. Staircase of Projective Ternary Rays $(3^d - 1)/2$, the Square $121 = 11^2$, and the Boundary of Ljunggren's External Theorem

In Chapter `I.5` (`§I.5.4`), studying the three-dimensional ternary cube of signed records $T_3 = \{-1, 0, +1\}^3$ of $27$ elements, we found that its $26$ non-zero vectors fold into $13$ pairs of opposite directions $\{u, -u\}$. Let us now ascend to an arbitrary dimension $d \ge 1$ and consider the $d$-dimensional cube of ternary records

$$T_d = \{-1, 0, +1\}^d \subset \mathbb{Z}^d, \qquad |T_d| = 3^d.$$

Discarding the single zero center $(0, \dots, 0)$ and identifying each non-zero record $u$ with the opposite record $-u$ (since $u \neq -u$ in $\mathbb{Z}^d$ for $u \neq 0$, all classes contain exactly $2$ elements each), we obtain the exact number of **projective ternary directions** in dimension $d$ (which is also the number of points of the finite projective space $\mathrm{PG}(d-1, 3)$ over the field $\mathbb{F}_3$):

$$R_d := \frac{3^d - 1}{2} = 1 + 3 + 3^2 + \dots + 3^{d-1}.$$

Let us ask a clean question at the junction of the geometric progression of powers of three and multiplicative squares: **for which dimensions $d \ge 1$ is the number of projective ternary directions $R_d$ equal to the square of an integer $y^2$?**

Let us inspect the first steps of this staircase and compare each with objects of the book already familiar to us:

| Dimension $d$ | Sum of powers $1 + 3 + \dots + 3^{d-1}$ | Value $R_d = (3^d - 1)/2$ | Geometric carrier in the book | Is it a perfect square $y^2$? |
| :---: | :--- | :---: | :--- | :---: |
| **`1`** | $1$ | **`1`** | Single sign axis $\{\pm 1\}$ (`Ch. I.5`) | **YES: $1 = 1^2$** |
| **`2`** | $1 + 3$ | **`4`** | $4$ directions of pencils of parallel lines in $\mathrm{AG}(2,3)$ (`12` lines, `3` per pencil), i.e. $4$ points of $\mathrm{PG}(1,3)$ (`Ch. I.6`) | **YES: $4 = 2^2$** |
| **$3$** | $1 + 3 + 9$ | **`13`** | $13$ axes of the cube $T_3$ (`Ch. I.5`) and $13$ points of the plane $\mathrm{PG}(2,3)$ (`Ch. I.6`) | no ($3^2 < 13 < 4^2$) |
| **$4$** | $1 + 3 + 9 + 27$ | **`40`** | $40$ points of the three-dimensional space $\mathrm{PG}(3,3)$ | no ($6^2 < 40 < 7^2$) |
| **`5`** | $1 + 3 + 9 + 27 + 81$ | **`121`** | $121 = 1 + 120$ directions in $T_5$ ($\mathrm{PG}(4,3)$) | **YES: $121 = 11^2$.** |
| **$6$** | $1 + \dots + 243$ | **`364`** | $\mathrm{PG}(5,3)$ | no ($19^2 = 361 < 364$) |
| **$7$** | $1 + \dots + 729$ | **`1 093`** | $\mathrm{PG}(6,3)$ | no ($33^2 = 1089 < 1093$) |

The appearance of the exact square $121 = 11^2$ on the fifth step ($1 + 3 + 9 + 27 + 81 = 121$, where beyond the first unit exactly $120$ new directions are added) singles out dimension $d = 5$ among small ternary lattices. But what happens further on—at $d = 50$, $d = 1000$, or $d = 10^{100}$? Here our book demonstrates the rule of scientific honesty: **a finite computer search (for instance, up to $d = 40$ in exact `BigInt` integer arithmetic) certifies the absence of new squares only within the verified window, whereas the global uniqueness of $d \in \{1, 2, 5\}$ rests on a classical external theorem of algebraic number theory**, which we cite explicitly with its own status.

> **Proposition I.7.2 (Specialization of Ljunggren's theorem for projective ternary directions).**  
> *Classical foundation.* The Nagell–Ljunggren Diophantine equation $\frac{x^n - 1}{x - 1} = y^2$ and W. Ljunggren's theorem (1943) on squares among base-$3$ repunits. *Contribution of this book:* Interpretation of $(3^d - 1)/2$ as the count of projective axes in the ternary cube $\{-1,0,+1\}^d$, exact finite certification of squares `1, 4, 121` ($d \in \{1, 2, 5\}$) for $d \le 40$, and explicit separation of the external Diophantine reference `[Ljunggren 1943]` for all $d \ge 1$.
> For $d \in \{1, 2, 5\}$, the number of projective ternary directions $R_d = (3^d - 1)/2$ is a perfect square ($1^2, 2^2, 11^2$). The absence of any other solutions for all $d \ge 3$ follows from the theorem of W. Ljunggren (`[Ljunggren 1943]`): the Diophantine equation $\frac{x^n - 1}{x - 1} = y^2$ in integers $x > 1,\, n > 2,\, y > 0$ has exactly two solutions—$(x, n, y) = (3, 5, 11)$ and $(x, n, y) = (7, 4, 20)$ ($1 + 7 + 49 + 343 = 400 = 20^2$).

Let us immediately place a methodological safeguard for Book III as well: the arithmetic identity $1 + 3 + 9 + 27 + 81 = 121 = 1 + 120 = 11^2$ is an exact arithmetic property of the fifth power of three and the projective geometry $\mathrm{PG}(4,3)$, but **by itself it does not identify two different combinatorial objects merely by coincidence of the number $120$** (for example, the order of the symmetric group $|\mathfrak{S}_5| = 5! = 120$, the number of unit modular octonions in Paige's loop $M_{120}$ in Book II, or the number of three-element subsets of a ten-element set $\binom{10}{3} = 120$). Any comparison between such constructions must be built through an explicitly exhibited morphism and its own operational contract, not through numerical coincidence of cardinalities.

---

## §I.7.7. Finite Divisor Product and Euler's Formal Pentagonal Law

Let us conclude our survey of connections between addition and multiplication with an identity that throws a bridge from our finite divisor lattices $D(N)$ to infinite generating series—and in doing so again requires a maximally careful distinction between finite rational algebra, formal power series, and analytic convergence.

In classical analysis, the celebrated Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1} = \sum_{n=1}^\infty n^{-s}$ requires the real or complex domain $\mathrm{Re}(s) > 1$ and a limiting passage, which do not yet exist in the finite core of Book I. However, its **exact finite prototype on the divisor lattice $D(N)$ of any fixed number $N$** lives entirely in the field of rational numbers $\mathbb{Q}$ and is proved by pure expansion of parentheses without a single limit.

> **Lemma I.7.1 (Finite divisor identity in $\mathbb{Q}$ and polynomial pentagonal substitution).**  
> *Classical foundation.* Finite multiplicative factorization over prime-power floors and Euler's pentagonal number theorem $\prod_{k \ge 1}(1 - t^k) = \sum_{m \in \mathbb{Z}} (-1)^m t^{m(3m-1)/2}$ in $\mathbb{Z}[[t]]$. *Contribution of this book:* Separating the exact finite identity in the window $D(N)$ over $\mathbb{Q}$ (`13/4 < 15/4` on $N=360$) and coefficientwise formal equality in $\mathbb{Z}[[t]]$ from illegitimate pointwise substitution $t = 1$ without a topology of convergence.
> 1. Let $N = \prod_{j=1}^{k} p_j^{e_j}$ be the canonical factorization of a positive integer, and let $s \in \mathbb{Z}_{\ge 0}$. Then in the field of rational numbers $\mathbb{Q}$ the exact finite equality holds:
>    $$\prod_{j=1}^{k} \bigl(1 + p_j^{-s} + p_j^{-2s} + \dots + p_j^{-e_j s}\bigr) \;=\; \sum_{d \in D(N)} d^{-s}.$$
> 2. On the residue class $x = 6k \mp 1 \in \mathbb{Z}$ coprime to $6$, the integer quotient $\frac{x^2 - 1}{24}$ coincides with the generalized pentagonal number:
>    $$\frac{(6k \mp 1)^2 - 1}{24} \;=\; \frac{k(3k \mp 1)}{2} \qquad (\forall\, k \in \mathbb{Z}).$$
>    In particular, for every prime number $p \ge 5$ (which has the form $p = 6k \mp 1$), the quantity $(p^2 - 1)/24$ is an integer pentagonal number, while the polynomial identity itself holds for all $k \in \mathbb{Z}$ (including composite $6k \mp 1$, such as $25 = 5^2$ at $k = 4$, where $(25^2 - 1)/24 = 26$).

*Proof.*  
1. Expand the finite product of $k$ parentheses by distributivity in the field $\mathbb{Q}$: each term is obtained by choosing exactly one exponent $a_j \in \{0, 1, \dots, e_j\}$ from the $j$-th parenthesis and is equal to $\prod_{j=1}^k p_j^{-a_j s} = \bigl(\prod_{j=1}^k p_j^{a_j}\bigr)^{-s}$. By the uniqueness of prime factorization, the correspondence $(a_1,\dots,a_k) \leftrightarrow d = \prod_{j=1}^k p_j^{a_j}$ is a bijection onto the set of positive divisors $D(N)$ (at $s = 0$ both sides in $\mathbb{Z}$ simply count the cardinality $|D(N)| = \prod_{j=1}^k (e_j + 1)$).  
2. In the polynomial ring $\mathbb{Q}[k]$, the numerator equals $(36k^2 \mp 12k + 1) - 1 = 12k(3k \mp 1)$; dividing by $24$, we obtain $k(3k \mp 1)/2$. Since of the two numbers $k$ and $3k \mp 1$ one is even for any integer $k$, the value always lies in $\mathbb{Z}$ regardless of the arithmetic nature of the number $6k \mp 1$. $\square$

The very same generalized pentagonal exponents $\omega(k) = \frac{k(3k \mp 1)}{2}$ ($1, 2, 5, 7, 12, 15, 22, 26, \dots$) govern the celebrated pentagonal theorem of L. Euler (`[Euler 1783]`) in the ring of **formal power series** $\mathbb{Z}[[t]]$:

$$\prod_{m=1}^{\infty} (1 - t^m) \;=\; 1 + \sum_{k=1}^{\infty} (-1)^k \Bigl(t^{k(3k-1)/2} + t^{k(3k+1)/2}\Bigr).$$

Note why this infinite equality is completely legitimate to mention without the topology of the field $\mathbb{R}$: in the ring of formal series $\mathbb{Z}[[t]]$, the coefficient at each fixed power $t^n$ is determined by a **finite product** $\prod_{m=1}^{n} (1 - t^m)$ (all factors with $m > n$ give $1$ modulo $t^{n+1}$). Once again let us draw an honest line between verification and proof: direct computation in `Julia` instantly confirms the coincidence of all coefficients up to $t^{100}$, whereas the truth of the formula for all $n \ge 0$ is Euler's general combinatorial theorem (Franklin's involution on Ferrers diagrams of partitions of $n$ into distinct parts).

---

## §I.7.8. Categorical Anchoring of the Chapter

Let us return to the divisor window $D(N)$ from `§I.7.2` and write it down as an exact thin category separating Boolean cuts from primary towers:

- **Objects:** all positive divisors $d \in D(N)$ of a fixed integer $N \in \mathbb{Z}_{>0}$.
- **Morphisms:** in the thin category $\mathbf{Div}(N)$, between two objects $d, e \in D(N)$ there is exactly one arrow $d \to e$ if $d \mid e$, and no arrows otherwise.
- **Identities and composition:** reflexivity $d \mid d$ gives the identity morphism $\mathrm{id}_d$, and transitivity $(d \mid e \land e \mid f \implies d \mid f)$ gives the unique possible composition of arrows.
- **Preserved structure:** the categorical product of two divisors coincides with $\gcd(d, e)$, the categorical coproduct with $\operatorname{lcm}(d, e)$, the initial object is $1$, the terminal object is $N$, and the dualizing involution $\nu_N(d) = N/d$ defines an isomorphism of the opposite category $\mathbf{Div}(N)^{\mathrm{op}} \xrightarrow{\sim} \mathbf{Div}(N)$.
- **Universal property:** the canonical factorization $N = \prod_{j=1}^k p_j^{e_j}$ generates an isomorphism of categories with products and coproducts between $\mathbf{Div}(N)$ and the Cartesian product of linear exponent chains $\prod_{j=1}^k \{0 \to 1 \to \dots \to e_j\}$.
- **Detected trap and failure:** the contravariant self-duality $\nu_N(d) = N/d$ turns the distributive lattice $\mathbf{Div}(N)$ into a **Boolean algebra** if and only if the number $N$ is squarefree ($e_j = 1$ for all $j$). As soon as even one prime enters squared ($N = 12 = 2^2 \cdot 3$ or $N = 45 = 3^2 \cdot 5$), a failure of the complement laws arises on the middle floor: for $d = 2$ in $D(12)$ we have $\nu_{12}(2) = 6$, but $\gcd(2, 6) = 2 \neq 1$ and $\operatorname{lcm}(2, 6) = 6 \neq 12$.

---

### Historical-Philosophical Note: The Form-Generation Tree in Pāṇini and the Boundary of Sāṃkhya's Numerical Lists

1. **Motif of the classical source.** In the ancient Indian grammar of Pāṇini (*Aṣṭādhyāyī*, c. 4th century BCE), one and the same phonetic surface of a word-form can arise from different chains of application of general rules (*utsarga*) and local exceptions (*apavāda*), indexed by auxiliary marker-labels (*it / anubandha*, *Aṣṭādhyāyī* `1.3.2–1.3.9`), which upon recognition and indexing are immediately subject to unconditional deletion by rule `1.3.9` (*tasya lopaḥ*), yet leave a procedural trace in selecting subsequent sūtras (cf. `1.1.62` *pratyayalope pratyayalakṣaṇam*). Nearby, in classical Sāṃkhya (*Sāṃkhya-kārikā* `SK 3, 22, 46–51`), fixed mnemonic lists are widely used (`25` *tattvas*, `13` instruments *karaṇa*, `50` divisions of *pratyayasarga*).
2. **Strict realization in DOT.** Pāṇini's mechanism gives an exact historical prototype of the distinction analyzed in `§I.7.1` between **the generation tree of an expression $e \in E$** (containing hidden markers of history) and **the flat output value $\mathrm{val}(e)$** after an erasing reading (*lopa*): as long as the markers are retained in the intermediate record, subsequent rules distinguish homonymous stems, but after final erasure the surface form alone does not allow one to uniquely invert the derivation.
3. **Boundary of comparison.** We strictly separate the operational architecture of rules with markers (which in Chapter `III.3` is compared with finite rewriting automata) from any attempts to bring traditional numerical lists of Sāṃkhya (`13`, `25`, `50`) closer to the number-theoretic quantities of the present chapter (such as $R_3 = 13$ ternary rays or $6k \mp 1 = 25$ at $k=4$): the mnemonic lists of a philosophical school do not serve as premises, witnesses, or explanations for a single arithmetic theorem of DOT.

---

### Transition to Chapter `I.8`

We have seen how the internal geometry of the divisor window $D(N)$ of a single number is organized and why non-Boolean primary floors ($3^2$ in $45$, $2^2$ in $12$) violate a naive decomposition into coprime pieces. In the next **Chapter `I.8`** we will turn these lattices into an active computational tool: we will find out how several modular or divisor windows assemble into a single residue ring, draw the strict boundary of **an oracle-free observer on a composite modulus $N = pq$** (who does not know the prime factors $p$ and $q$ in advance), and then transfer the very same question about a finite window to infinite numerical sequences using Hankel matrices.

---

### Verifiability Passport of Chapter `I.7` (`Book I v3.3`)

- **Canonical node of the book:** `N07` (non-isomorphism of additive and multiplicative structures, Boolean and non-Boolean divisor lattices $D(N)$, equilibrium window $1+\pi(N)=N/2$, domain of the equation $x+y+z=xyz$, satellite criterion $A(p)\mid p\#$, projective ternary rays and boundary of Ljunggren's theorem, finite divisor product and formal Euler series).
- **Exact `Julia 1.12.6` verifications (single-threaded mode, `Int / BigInt / Rational{BigInt}`, without `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gates `GATE-I07-A` (graphs on $\{1,2,3,6\}$, lattices $D(6), D(30), D(12), D(45)$, and equilibrium $1+\pi(N)=N/2$ for $N\le 500$ with the identity $m=\pi(2m)+c(2m)$) and `GATE-I07-B` ($x+y+z=xyz$ with all $6$ permutations of $(1,2,3)$ and integer triples $(-a,0,a)$, satellite $A(p)\mid p\#$ with failures $p=7, 17$ and $(6k\mp 1)^2-1\equiv 0\pmod{24}$, $(3^d-1)/2$ up to $d=40$, finite Euler on $D(360)$ in $\mathbb{Q}$, and pentagonal series up to $t^{100}$).
- **Specification index `Lean 4` (`status: planned`, full cards in Appendix `VP`):** `TNR.BookI.I07.additive_multiplicative_not_isomorphic`, `TNR.BookI.I07.divisor_lattice_complement`, `TNR.BookI.I07.prime_count_small_solutions`, `TNR.BookI.I07.xyz_ordered`, `TNR.BookI.I07.satellite_squarefree_criterion`, `TNR.BookI.I07.ljunggren_specialization`, `TNR.BookI.I07.divisor_product`, `TNR.BookI.I07.pentagonal_substitution`.
- **Full 8-point passports of figures `Fig. I.7.1–I.7.2` and statement certification registry:** moved to [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
