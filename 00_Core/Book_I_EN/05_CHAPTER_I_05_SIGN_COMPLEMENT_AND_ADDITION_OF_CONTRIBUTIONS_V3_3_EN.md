# Chapter I.5. Sign, Complement, and Addition of Contributions

In the first four chapters of this book we worked in a world of presence and absence. However refined our operational contract $\Gamma = (X, \mathcal{Q}, \mathcal{A}, \mathrm{Dom}, \Pi, \Phi)$ was—whether the static intersection of windows in Chapter `I.1`, the two-door airlock of partial transitions in Chapter `I.2`, the minimal quotient of future memory in Chapter `I.3`, or the closed-loop executor with a branch-trace register in Chapter `I.4`—every observable event remained a **subset** $A \subseteq X$ of the finite state carrier.

In such a world, two signals arriving at the same point have only one fate: to merge without remainder. If a bulb on a console is already lit, a second pulse to the same terminal will not make it "twice as lit," much less extinguish it. Boolean union is idempotent:

$$\{x\} \cup \{x\} = \{x\}.$$

Yet even the simplest combinatorial experiments with overlapping paths confront the observer with a question of an altogether different kind: **how does one describe a scene in which two open paths arrive at one and the same slot with opposite signs and mutually cancel to zero?**

The present chapter opens the first explicitly declared **enrichment boundary** of Volume I. We will show why the arithmetic "minus" sign cannot be derived for free from the logical negation of a question, from the set-theoretic complement $X \setminus A$, or from a simple permutation of the vertices of the carrier. For alternative histories to be added and mutually canceled, a new algebraic contract must be entered into on the same finite set of slot names $X$—passing from the Boolean monoid of subsets to the free integer module of formal contributions $\mathbb{Z}[X]$. Once this transition is made, four constructions arise on finite lattices without a single real number or continuous angle, and they will run through all three volumes of our work: two-channel signed path cancellation and blocker-induced unblocking (`Ban-Go`), the shell geometry of the ternary record cube $\{-1,0,+1\}^3$, the discrete integer quarter-turn $J^2 = -I_2$, and the even checkerboard sublattice of the Hadamard transform.

---

## §I.5.1. A Tangible Scene: A Lightboard Versus a Bowl of White and Black Tokens

Let us place side by side on the laboratory bench two instruments built over **one and the same** finite set of named wells $X = \{x_1, x_2, \dots, x_n\}$.

**The first instrument—a presence lightboard.** In each well $x_k$ sits an ordinary indicator lamp with two positions: "off" (`0`) or "lit" (`1`). The state of the entire board is completely specified by the subset of lit lamps $A \subseteq X$. Feed two signal packets $A$ and $B$ to the input: a lamp lights up wherever at least one packet arrives, so the resulting state equals the union $A \cup B$. Try in this instrument to "annihilate" a lit lamp $\{x_1\}$ by adding to it the Boolean complement $X \setminus \{x_1\}$—all the other lamps on the board. Instead of darkness, **the entire board lights up**:

$$\{x_1\} \cup (X \setminus \{x_1\}) = X \neq \varnothing.$$

No addition of new signals on a lightboard can extinguish an already lit point: one cannot subtract from emptiness, nor can one add anything to a non-empty set to obtain the empty set $\varnothing$.

**The second instrument—a counting board with tokens of two colors.** Keep the exact same wells $X = \{x_1, \dots, x_n\}$, but instead of lamps drop into each well white tokens (contribution $+1$) and black tokens (contribution $-1$), with the rule that a opposite-color pair in the same well mutually cancels and is removed. Now the picture changes in two decisive respects:
1. **Accumulation of multiplicity instead of idempotent merging:** two white tokens dropped into well $x_1$ do not merge into a single token, but form the doubled contribution $+2\,e_{x_1}$.
2. **Exact mutual cancellation to zero balance:** one white token and one black token arriving via two different chutes into one and the same well $x_1$ mutually balance out and leave the well clear:

$$(+1)\,e_{x_1} + (-1)\,e_{x_1} = 0.$$

Let us formulate the discipline of this transition explicitly. Within our method, any transition from an older answer language to an enriched one requires declaring the new structural commitments:

1. **Boundary of new equipment.** Passing from subsets $\mathcal{P}(X)$ to integer linear combinations $\mathbb{Z}[X]$ is **not a theorem deducible from the axioms of Chapters `I.1–I.4`**, but a deliberate extension of the operational contract $\Gamma$: to the previous finite set of slots $X$ is adjoined the abelian group of integer multiplicities with addition and sign inversion.
2. **Finiteness of slots versus infinitude of the counter.** Even when the set of wells $X$ is finite (say, $|X| = 2$ or $|X| = 3$), the free abelian group $\mathbb{Z}[X]$ itself as the set of all formal sums is infinite, because one can pour arbitrarily many tokens of the same color into a single well. When we speak of the finite core of Book I, the finite objects are **the carrier of slots $X$**, the matrix of one-step transfer rules, and any explicitly declared reading window (for instance, the sign slice $\{-1, 0, +1\}^X$ or a bounded coefficient box $[-M, M]^X$).
3. **Strict distinction between a slot name and a contribution coefficient.** The expression $c_x e_x$ joins two objects of completely different types: $x \in X$ is the address of a well on the bench (an element of the carrier), whereas $c_x \in \mathbb{Z}$ is the count and color of tokens in that well (a scalar coefficient). Confusing a slot permutation $x \mapsto \sigma(x)$ with a coefficient sign flip $c_x \mapsto -c_x$ leads to error; below we analyze this distinction in detail.

---

## §I.5.2. Three Pitfalls of Naively Identifying Sign with Negation

Before writing out strict theorems, let us test three tempting guesses by which one often tries to obtain the "minus" sign from the purely Boolean resources of the opening chapters—and see exactly where each of them shipwrecks.

**Pitfall 1: "The Boolean complement $X \setminus A$ is just minus $A$."**  
In a Boolean algebra, complementation indeed enjoys a clean involution property: double complementation returns the original subset, $X \setminus (X \setminus A) = A$, just like $-(-v) = v$. Yet the resemblance ends the very instant we add an element to its supposed "inverse." In a group of contributions, the sum $v + (-v)$ must yield the neutral element of addition—the zero vector $0$ that leaves every other summand unchanged ($u + 0 = u$). In the monoid $(\mathcal{P}(X), \cup, \varnothing)$, the neutral element is the empty set $\varnothing$, whereas the union $A \cup (X \setminus A)$ yields the opposite pole—the entire space $X$, which absorbs every summand ($U \cup X = X$). And if one replaces union by symmetric difference $A \triangle B$ (addition modulo $2$ in $\mathbb{F}_2^X$), an inverse element appears, but the distinction between $+1$ and $-1$ vanishes: two identical white tokens begin to cancel each other ($e_x \oplus e_x = 0$), and any amplitude accumulation becomes impossible.

**Pitfall 2: "Just swap the two poles of a dipole, and the sign flips by itself."**  
Take a two-slot carrier $X = \{1, 2\}$ (the left and right pans of a scale) and the pan swap $\sigma(1) = 2$, $\sigma(2) = 1$. Extending it linearly to pairs of contributions $a e_1 + b e_2 \in \mathbb{Z}[\{1,2\}]$ gives the exchange operator $S(a e_1 + b e_2) = b e_1 + a e_2$. Does $S$ flip the sign of a vector? Feed in the symmetric total-weight mode $e_+ = e_1 + e_2$:

$$S(e_1 + e_2) = e_2 + e_1 = +(e_1 + e_2).$$

No sign flip occurred at all. The slot permutation $S$ multiplies by $-1$ **only on the antisymmetric difference mode** $e_- = e_1 - e_2$:

$$S(e_1 - e_2) = e_2 - e_1 = -(e_1 - e_2),$$

yet this very mode $e_1 - e_2 = (+1)e_1 + (-1)e_2$ cannot even be written down until a genuine "minus" sign has been introduced in the coefficient ring. Permuting vertices changes addresses on the bench, but never creates a negative coefficient out of positive ones.

**Pitfall 3: "Why bother with the infinite ring $\mathbb{Z}$ when we can just clamp the sum to the three labels $\{-1, 0, +1\}$?"**  
Wishing to stay on a finite set of three signed readings $\{-1, 0, +1\}$, it is natural to propose a saturation ("clamping") operation: set $\mathrm{clamp}(z) = \max(-1, \min(1, z))$ and define truncated addition $a \boxplus b := \mathrm{clamp}(a + b)$. Let us check on three tokens $(+1), (+1), (-1)$ whether the outcome depends on how the summands are grouped:
- if we first add the two white tokens and then add the black one:

$$(1 \boxplus 1) \boxplus (-1) = \mathrm{clamp}(2) \boxplus (-1) = 1 \boxplus (-1) = \mathbf{0};$$

- if we first cancel the second white token against the black one and then add the first white token:

$$1 \boxplus \bigl(1 \boxplus (-1)\bigr) = 1 \boxplus 0 = \mathbf{1}.$$

The answers diverge ($0 \neq 1$): the operation $\boxplus$ **loses associativity**. The result begins to depend on parenthesization, ceasing to be a well-defined sum of path contributions. And if, to save associativity, one replaces clamping by reduction modulo $3$ in the finite field $\mathbb{F}_3 = \{-1, 0, +1\}$, two positive steps suddenly turn into a negative step ($1 + 1 \equiv -1 \pmod 3$), destroying multiplicity accumulation. Note that the three properties by themselves—associativity of addition, existence of an additive inverse, and the inequality $1 + 1 \neq -1$—also hold in finite cyclic groups of larger period (for example, in $\mathbb{Z}/5\mathbb{Z}$, where $2 \not\equiv -1$ while $5 \equiv 0$). However, every finite modular ring imposes a cyclic wrap-around threshold $m \cdot 1 = 0$; once we refuse to impose an artificial wrap-around period and impose no extra relations between distinct slots $x \in X$, the universal (relation-free) choice is the free abelian group (**free $\mathbb{Z}$-module**) $\mathbb{Z}[X]$ over the ring of integers $\mathbb{Z}$.

---

## §I.5.3. The Free Module $\mathbb{Z}[X]$ and the Theorem on Non-Deducibility of Sign from Boolean Union

Let us consolidate the boundaries analyzed above in the first strict theorem of the chapter. For every vector $u = \sum_{x \in X} u_x e_x \in \mathbb{Z}[X]$ (where only finitely many integer coefficients $u_x \in \mathbb{Z}$ are non-zero), call the finite subset of active slots its **support**:

$$\mathrm{supp}(u) := \{x \in X \mid u_x \neq 0\} \subseteq X.$$

> **Theorem I.5.1 (Absence of non-trivial morphisms into the Boolean monoid, subadditivity of support, and failure of clamping).**  
> *Classical foundation.* Absence of non-zero additive inverses in the idempotent Boolean monoid $(2^X, \cup, \varnothing)$ and universal property of the free abelian group $\mathbb{Z}[X]$ on $X$. *Contribution of this book:* Strict derivation of the signed endowment boundary `B1` from the requirement of mutual contribution cancellation, functoriality $\mathbb{Z}[T_2 \circ T_1] = \mathbb{Z}[T_2]\mathbb{Z}[T_1]$, and explicit failure of associativity under nonlinear `clamp` truncation.
> Let $X$ be an arbitrary non-empty set, $(\mathcal{P}(X), \cup, \varnothing)$ the idempotent commutative monoid of subsets under union, and $(\mathbb{Z}[X], +, 0)$ the free $\mathbb{Z}$-module of formal integer contributions on $X$. Then:
> 1. Every monoid homomorphism $h : (\mathbb{Z}[X], +, 0) \to (\mathcal{P}(X), \cup, \varnothing)$ is trivial: $h(u) = \varnothing$ for all $u \in \mathbb{Z}[X]$.
> 2. The support map $\mathrm{supp} : \mathbb{Z}[X] \to \mathcal{P}(X)$ satisfies $\mathrm{supp}(0) = \varnothing$, $\mathrm{supp}(-u) = \mathrm{supp}(u)$, and the general inclusion $\mathrm{supp}(u + v) \subseteq \mathrm{supp}(u) \cup \mathrm{supp}(v)$, which becomes a strict proper inclusion on every mutually canceling pair ($u = e_x$, $v = -e_x \implies \varnothing \subsetneq \{x\}$).
> 3. Truncated addition $a \boxplus b = \max(-1, \min(1, a+b))$ on the set $\{-1,0,+1\}$ is non-associative: $(1 \boxplus 1) \boxplus (-1) = 0 \neq 1 = 1 \boxplus (1 \boxplus (-1))$.

*Proof.*  
1. Suppose $h : (\mathbb{Z}[X], +, 0) \to (\mathcal{P}(X), \cup, \varnothing)$ preserves the neutral element ($h(0) = \varnothing$) and maps sums to unions ($h(u + v) = h(u) \cup h(v)$). For any $u \in \mathbb{Z}[X]$ we have $u + (-u) = 0$, whence

$$h(u) \cup h(-u) = h\bigl(u + (-u)\bigr) = h(0) = \varnothing.$$

By definition of set union, $h(u) \subseteq h(u) \cup h(-u) = \varnothing$, so $h(u) = \varnothing$.  
2. If $x \in \mathrm{supp}(u + v)$, then $u_x + v_x \neq 0$, so $u_x$ and $v_x$ cannot both be zero; hence $x \in \mathrm{supp}(u) \cup \mathrm{supp}(v)$. For $u = e_x$ and $v = -e_x$, the sum is the zero vector with empty support $\varnothing$, whereas the union of supports is $\{x\} \neq \varnothing$.  
3. For $a=1, b=1, c=-1$, direct evaluation gives $\max(-1,\min(1,2)) = 1$, whence $(1 \boxplus 1) \boxplus (-1) = 1 \boxplus (-1) = 0$, whereas $1 \boxplus (1 \boxplus (-1)) = 1 \boxplus 0 = 1$. $\square$

---

## §I.5.4. The Ternary Record Cube $\{-1, 0, +1\}^3$: Shell Geometry `1 + 6 + 12 + 8 = 27` and Thirteen Axes

Although truncated addition $\boxplus$ does not form a group, the finite set of ternary signed reports itself arises legitimately whenever an observer reads the sign or elementary three-valued response (`-1`, `0`, `+1`) across **three independent channels** $(u_1, u_2, u_3)$ simultaneously.

Let us examine the geometry of the resulting finite carrier of records

$$T_3 = \{-1, 0, +1\}^3 \subset \mathbb{Z}^3, \qquad |T_3| = 3^3 = 27.$$

For each record $u = (u_1, u_2, u_3) \in T_3$, compute its Manhattan weight $|u|_1 = |u_1| + |u_2| + |u_3|$—it simply counts **how many of the three channels emitted a non-zero signed signal**. Since each absolute value $|u_k|$ equals $0$ or $1$, the entire cube of `27` records stratifies into four concentric shells around the silent center $(0,0,0)$:

```text
           SHELLS OF THE TERNARY RECORD CUBE  T_3 = {-1, 0, +1}^3  (|T_3| = 27)

   Weight |u|_1 = 0     Weight |u|_1 = 1        Weight |u|_1 = 2          Weight |u|_1 = 3
   [1 rest center]     [6 octahedron vertices] [12 cube edge midpoints]  [8 cube corners ±1]

                               (0,0,+1)              (+1,+1,0)            (-1,+1,+1) (+1,+1,+1)
                                  |                   \  |  /                 +---------+
      (0,0,0)            (0,-1,0)-+-(0,+1,0)     (-1,0,+1)(+1,0,+1)          /|        /|
      silence                  /  |                    / | \                +---------+ |
   of all 3 windows      (-1,0,0)|(+1,0,0)          (0,-1,-1)...           | |       | |
                               (0,0,-1)                                     +---------+

   |─────────── Ball of radius |u|_1 ≤ 2: exactly 19 records (1 zero + 18 non-zero) ───────────|
   |──────────────────── Full cube: 1 + 6 + 12 + 8 = 27 records (26 non-zero) ─────────────────|
```

**Reader's caption to `Fig. I.5.1`:** stratification of the ternary cube $T_3 = \{-1,0,+1\}^3$ by the number of active signed channels $|u|_1 \in \{0,1,2,3\}$. The shell of weight $1$ forms the $6$ axial vertices of the octahedron $(\pm 1, 0, 0)$ and their permutations; the shell of weight $2$ forms the $12$ edge midpoints of the cube $(\pm 1, \pm 1, 0)$, assembling into the vertices of the cuboctahedron; the shell of weight $3$ forms the $8$ diagonal corners $(\pm 1, \pm 1, \pm 1)$. The ball of at most two active channels $|u|_1 \le 2$ contains exactly $1 + 6 + 12 = 19$ records ($18$ non-zero and $1$ central zero).

Let us summarize all numbers of this construction in an exact verification table so that not a single shell is taken on faith:

| Shell $|u|_1$ | Counting formula $\binom{3}{k} 2^k$ | Number of records | Geometric meaning in $\mathbb{Z}^3$ | Number of projective axes $\{u, -u\}$ |
| :---: | :---: | :---: | :--- | :---: |
| **$0$** | $\binom{3}{0} \cdot 2^0 = 1 \cdot 1$ | **`1`** | Center of complete silence $(0,0,0)$ | `0` (defines no ray) |
| **$1$** | $\binom{3}{1} \cdot 2^1 = 3 \cdot 2$ | **`6`** | $6$ face centers of the cube (vertices of the octahedron $O_6$) | **`3`** coordinate axes |
| **$2$** | $\binom{3}{2} \cdot 2^2 = 3 \cdot 4$ | **`12`** | $12$ edge midpoints of the cube (vertices of the cuboctahedron) | **`6`** face bisectors |
| **$3$** | $\binom{3}{3} \cdot 2^3 = 1 \cdot 8$ | **`8`** | $8$ corner vertices of the sign cube $\{-1,+1\}^3$ | **`4`** space diagonals |
| **Total** | $(1 + 2)^3 = 3^3$ | **`27`** | Full ternary cube ($1$ zero + $26$ non-zero) | **`3 + 6 + 4 = 13`** axes |

The rightmost column of this table links directly to the next two chapters of the book. Central sign inversion $u \mapsto -u$ fixes only the zero center $(0,0,0)$ and partitions all $26$ non-zero records into **thirteen antipodal pairs** $\{u, -u\}$:

$$\frac{3^3 - 1}{2} = \frac{26}{2} = 13 = 3 + 6 + 4.$$

In Chapter `I.6` these $13$ antipodal pairs $\{u, -u\}$ of non-zero records $T_3 \setminus \{0\}$ will be placed in bijection with the $13$ points of the finite projective plane $\mathrm{PG}(2, 3) = (\mathbb{F}_3^3 \setminus \{0\}) / \{\pm 1\}$ over the three-element field $\mathbb{F}_3$ (while strictly distinguishing the operations themselves: integer addition in $\mathbb{Z}^3$ is not taken modulo `3` and sends the sum $(1,0,0)+(1,0,0)=(2,0,0)$ outside $T_3$, and in the full lattice $\mathbb{Z}^3$ the complete Manhattan ball $\|u\|_1 \le 2$ contains $19 + 6 = 25$ points due to the six doubled axial vectors $\pm 2 e_k \notin T_3$), whereas in Chapter `I.7` we will encounter the general ladder of projective ternary directions $(3^d - 1)/2$ ($1, 4, 13, 40, 121 = 11^2$) and Ljunggren's theorem.

At the same time, let us maintain strict methodological sobriety: the `27` elements of the cube $T_3$ form a **finite catalog of three-channel ternary records** (or, equivalently in the combinatorics of the cube $Q_3$, the catalog of its `27` non-empty faces: `8` vertices + `12` edges + `6` square faces + `1` three-dimensional cube itself, whereas including the empty face $\varnothing$ gives `28`). From the arithmetic identity $3^3 = 27$ alone **neither the dimension of a quantum state space nor any external numerical constant follows**: every applied model in Books II and III will carry its own explicitly verifiable operational contract.

---

## §I.5.5. Two-Channel Path Cancellation `Ban-Go`: When Blocking an Open Channel Turns On the Signal

We are now ready to witness the central dynamical phenomenon for whose sake sign was introduced into the theory. Compare two-step signal transport across two intermediate channels $k \in \{1, 2\}$ under two different algebraic equipments:
- **in the Boolean reachability semiring** $(\{0, 1\}, \lor, \land)$, where the matrix product of two ticks is computed by the rule "there exists at least one open intermediate path":

$$(A \odot B)_{ij} := \bigvee_{k=1}^{n} \bigl(A_{ik} \land B_{kj}\bigr);$$

- **in the integer ring of signed contributions** $(\mathbb{Z}, +, \cdot)$, where contributions along a single path multiply, while contributions of different paths sharing input $i$ and output $j$ add in the ordinary integer sum:

$$(M N)_{ij} := \sum_{k=1}^{n} M_{ik} N_{kj}.$$

To compare the two worlds on an equal footing, define on integer matrices $M \in \mathrm{Mat}_n(\mathbb{Z})$ the **support indicator** $s : \mathrm{Mat}_n(\mathbb{Z}) \to \mathrm{Mat}_n(\{0,1\})$ by setting

$$s(M)_{ij} := \begin{cases} 1, & \text{if } M_{ij} \neq 0, \\ 0, & \text{if } M_{ij} = 0. \end{cases}$$

Notice why it is specifically the non-zero support indicator $s(M)$ that is needed here rather than a naive rule "take absolute values on $\{-1,0,+1\}$": already after two steps integer amplitudes add and can take values $2$ or $-2$, leaving the set $\{-1,0,+1\}$, whereas the support indicator $s(M)$ is defined on all matrices over $\mathbb{Z}$.

Construct a two-step cascade with the simplest signed transition matrix $H_{\mathrm{go}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, in which all four one-step channels are open ($s(H_{\mathrm{go}}) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$), and only the edge $2 \to 2$ flips the sign of the contribution:

```text
   (a) BOOLEAN REACHABILITY ({0,1}, ∨, ∧)         (b) SIGNED PATH ADDITION IN Mat_2(Z)
       A blocker NEVER opens a blocked passage         Blocker P_1 UNBLOCKS a canceled transition!

             ┌──[channel k=1: 1 ∧ 1 = 1]──┐                 ┌──[channel k=1: (+1)(+1) = +1]──┐
      in 1 ──┤                            ├─> 1      in 1 ──┤                                ├─> 0 (BAN!)
             └──[channel k=2: 1 ∧ 1 = 1]──┘                 └──[channel k=2: (+1)(-1) = -1]──┘

      Both paths open:    (s(H) ⊙ s(H))_12 = 1     Both paths open: (H_go^2)_12 = (+1)+(-1) = 0
      Block channel 2:    (s(H)·P_1·s(H))_12 = 1   Block channel 2 with blocker P_1 = diag(1,0):
      (if it was 0, after blocking it stays 0!)    (H_go P_1 H_go)_12 = (+1)(+1) + 0 = 1 (GO!)
```

**Reader's caption to `Fig. I.5.2`:** the two-channel `Ban-Go` cell. In the left Boolean panel (a), the presence of a second open path can only maintain or add a one, never zero out an already existing passage. In the right signed panel (b), the upper path $1 \to 1 \to 2$ brings contribution $+1$ while the lower path $1 \to 2 \to 2$ brings contribution $(+1)(-1) = -1$; together they lock output $2$ (`Ban`), yet as soon as the lower channel is blocked by the diagonal shutter $P_1 = \mathrm{diag}(1,0)$, the cancellation disappears and the signal passes freely to output $2$ (`Go`).

> **Theorem I.5.2 (Monotonicity of Boolean reachability versus signed `Ban-Go` unblocking).**  
> *Classical foundation.* Monotonicity of matrix multiplication over the Boolean semiring $(\{0,1\}, \lor, \land)$ vs. signed path sums over the ring $\mathbb{Z}$ (signed graphs, Zaslavsky, 1982). *Contribution of this book:* `Ban-Go` prohibition theorem: non-existence of a Boolean support operation $s(A_2 A_1) = F(s(A_2), s(A_1))$ due to antiphase cancellation of two open paths, plus path revival upon inserting a shutter.
> 1. In the Boolean semiring $(\{0,1\}, \lor, \land)$, matrix multiplication is entrywise monotone: for any Boolean matrices $A, B \in \mathrm{Mat}_n(\{0,1\})$ and any diagonal blocker $P \le I_n$, we have $(A \odot P \odot B)_{ij} \le (A \odot B)_{ij}$. In particular, if a transition is forbidden when all channels are open ($(A \odot B)_{ij} = 0$), blocking some intermediate channels can never open it ($(A \odot P \odot B)_{ij} = 0$).
> 2. For the integer matrix $H_{\mathrm{go}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \in \mathrm{Mat}_2(\mathbb{Z})$, the square is $H_{\mathrm{go}}^2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2 I_2$, so the off-diagonal transition is mutually canceled ($(H_{\mathrm{go}}^2)_{12} = (H_{\mathrm{go}}^2)_{21} = 0$), whereas inserting the blocker $P_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ opens it:
>    $$H_{\mathrm{go}} P_1 H_{\mathrm{go}} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad s(H_{\mathrm{go}}^2)_{12} = 0 \neq 1 = \bigl(s(H_{\mathrm{go}}) \odot s(H_{\mathrm{go}})\bigr)_{12}.$$

*Proof.*  
1. For each $k \in \{1,\dots,n\}$, from $P_{kk} \in \{0,1\}$ follows the conjunction inequality $(A_{ik} \land P_{kk} \land B_{kj}) \le (A_{ik} \land B_{kj})$, and disjunction over $k$ preserves the order $\le$ on $\{0,1\}$. Consequently, $(A \odot B)_{ij} = 0$ implies $(A \odot P \odot B)_{ij} = 0$ (in particular, this holds identically across all $16 \times 16 = 256$ pairs of Boolean $2 \times 2$ matrices).  
2. Direct matrix multiplication over $\mathbb{Z}$ gives $(H_{\mathrm{go}}^2)_{11} = 1\cdot 1 + 1\cdot 1 = 2$, $(H_{\mathrm{go}}^2)_{12} = 1\cdot 1 + 1\cdot(-1) = 0$, $(H_{\mathrm{go}}^2)_{21} = 1\cdot 1 + (-1)\cdot 1 = 0$, $(H_{\mathrm{go}}^2)_{22} = 1\cdot 1 + (-1)\cdot(-1) = 2$. When $P_1$ is inserted, only the summand $k = 1$ survives, giving $(H_{\mathrm{go}} P_1 H_{\mathrm{go}})_{ij} = (H_{\mathrm{go}})_{i1} (H_{\mathrm{go}})_{1j} = 1 \cdot 1 = 1$ for all $i, j \in \{1, 2\}$. The support indicator $s$ does not preserve matrix multiplication: $s(H_{\mathrm{go}}^2)_{12} = s(2I_2)_{12} = 0$, whereas $(s(H_{\mathrm{go}}) \odot s(H_{\mathrm{go}}))_{12} = 1$. $\square$

Let us emphasize an important conceptual boundary (it will guard against hasty leaps when passing to Book II): the `Ban-Go` phenomenon just proved is a **purely algebraic cancellation of signed contributions in the ring $\mathbb{Z}$**. We have introduced neither a Hilbert space of states, nor unitary normalization (note that $H_{\mathrm{go}}^2 = 2I_2$ doubles the scale), nor Born's probabilistic rule $p = |\psi|^2$. Book I isolates the *minimal algebraic root* of alternative cancellation—the emergence of an additive inverse in the ring of edge weights; the full-fledged quantum scene with states, effects, and normalized channels will be erected over this root in Chapters `II.6–II.7`.

---

## §I.5.6. The Discrete Quarter-Turn $J^2 = -I_2$ Without Real Numbers and the Four Distinct "Imaginary Units" of the Book

In a standard textbook course, a square root of sign inversion is associated exclusively with the field of complex numbers $\mathbb{C}$ or with a continuous rotation of the Euclidean plane by the angle $\pi/2$. Let us ask, however, within the purely integer equipment of the present chapter: **can one obtain an exact operator whose square reverses the sign of every contribution without leaving two wells with integer token counts $\mathbb{Z}^2$?**

On the two-slot integer lattice $\mathbb{Z}^2$, consider the skew-symmetric map

$$J_{\mathbb{Z}} : \mathbb{Z}^2 \longrightarrow \mathbb{Z}^2, \qquad J_{\mathbb{Z}}(a, b) := (-b,\, a), \qquad J_{\mathbb{Z}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}).$$

Let us trace by hand the action of $J_{\mathbb{Z}}$ on a single white token in the first well $(1, 0)$:

```text
                        (0, +1)
                           ▲
         1st tick J_Z      │      2nd tick J_Z
       (1,0) ──► (0,1)     │    (0,1) ──► (-1,0)
                           │
        (-1, 0) ◄──────────┼──────────► (+1, 0)
                           │
         3rd tick J_Z      │      4th tick J_Z
      (-1,0) ──► (0,-1)    │   (0,-1) ──► (1,0)
                           ▼
                        (0, -1)
```

**Reader's caption to `Fig. I.5.3`:** the four-tick cycle of the operator $J_{\mathbb{Z}}(a,b) = (-b, a)$ on the integer cross of the lattice $\mathbb{Z}^2$. A single application transfers the contribution from the first component into the second with a quarter-cycle phase shift; a double application reverses the sign of both numbers in their original wells ($J_{\mathbb{Z}}^2(a,b) = (-a, -b)$); and only a fourfold application closes the cycle to the identity ($J_{\mathbb{Z}}^4 = I_2$).

> **Proposition I.5.1 (Integer realization of the square root of sign inversion and unsolvability on a single channel).**  
> *Classical foundation.* Real-integer matrix embedding of the ring of Gaussian integers $\mathbb{Z}[i] \hookrightarrow \mathrm{Mat}_2(\mathbb{Z})$ via the quarter-turn matrix $J_{\mathbb{Z}} = \bigl(\begin{smallmatrix}0 & -1\\ 1 & 0\end{smallmatrix}\bigr)$. *Contribution of this book:* Realization of the exact phase quarter-turn law $J_{\mathbb{Z}}^2 = -I_2$ on a pair of integer channels $\mathbb{Z}^2$ without introducing $\mathbb{C}$ or $\mathbb{R}$, contrasted with the absence of roots $z^2 = -1$ in a single channel $\mathbb{Z}$.
> 1. On the one-dimensional module $\mathbb{Z}$ there exists no endomorphism $\varphi \in \mathrm{End}_{\mathbb{Z}}(\mathbb{Z})$ satisfying $\varphi^2 = -\mathrm{id}_{\mathbb{Z}}$, since every endomorphism of $\mathbb{Z}$ is multiplication by an integer $m \in \mathbb{Z}$, and $m^2 \ge 0 \neq -1$.
> 2. On the two-dimensional module $\mathbb{Z}^2$, the matrix $J_{\mathbb{Z}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is invertible over $\mathbb{Z}$ ($\det J_{\mathbb{Z}} = +1$, $J_{\mathbb{Z}}^{-1} = -J_{\mathbb{Z}}$) and satisfies the exact relations
>    $$J_{\mathbb{Z}}^2 = -I_2, \qquad J_{\mathbb{Z}}^3 = -J_{\mathbb{Z}}, \qquad J_{\mathbb{Z}}^4 = I_2.$$

*Proof.* Every abelian group homomorphism $\varphi : \mathbb{Z} \to \mathbb{Z}$ is uniquely determined by the image of unity $m = \varphi(1) \in \mathbb{Z}$ via $\varphi(a) = m a$, whence $\varphi(\varphi(1)) = m^2 \ge 0$, ruling out $\varphi^2(1) = -1$. On $\mathbb{Z}^2$, the composition $J_{\mathbb{Z}}(J_{\mathbb{Z}}(a,b)) = J_{\mathbb{Z}}(-b, a) = (-a, -b) = -(a,b)$ gives $J_{\mathbb{Z}}^2 = -I_2$, from which $J_{\mathbb{Z}}^3 = -J_{\mathbb{Z}}$, $J_{\mathbb{Z}}^4 = (-I_2)^2 = I_2$, and $J_{\mathbb{Z}} (-J_{\mathbb{Z}}) = I_2$ follow immediately. $\square$

In the chapter where an operator squaring to $-I_2$ first appears, let us introduce a **notational separation across all three books**. Across different branches of mathematics and different chapters of our work, four completely distinct objects occur that must never be conflated under a vague label "structural imaginary unit." Let us separate them once and for all in an explicit table:

| Notation | Where introduced | Exact mathematical type | Primary defining property | What it must not be confused with |
| :---: | :---: | :--- | :--- | :--- |
| **$J_{\mathbb{Z}}$** | **Book I, Ch. `I.5`** | Lattice automorphism in $\mathrm{SL}_2(\mathbb{Z})$ on a pair of integer counters $\mathbb{Z}^2$ | $J_{\mathbb{Z}}(a,b)=(-b,a)$, $J_{\mathbb{Z}}^2 = -I_2$ without the field $\mathbb{R}$ or continuous angles | Does not act on a single scalar and defines no continuous rotation |
| **$i_{\mathrm{str}}[e]$** | **Book I, Ch. `I.1` (and `I.7`, `I.9`)** | Injective packaging code of a verified ensemble / expression $F : E \hookrightarrow C$ | Exact lossless unfolding $U(i_{\mathrm{str}}[e]) = e$ preserving seams | Is **never squared at all** and is neither a matrix nor a number |
| **$J_{\mathbb{R}}$** | **Book II, Ch. `II.2`** | Skew-symmetric generator in $\mathrm{Mat}_2(\mathbb{R})$ over the real field | Generates the continuous group $\exp(\theta J_{\mathbb{R}}) \in \mathrm{SO}(2)$ for all $\theta \in \mathbb{R}$ and the commutative subalgebra $\mathbb{R}[J_{\mathbb{R}}] \cong \mathbb{C}$ | Requires the axioms of the field $\mathbb{R}$ and limits; does not reduce to the four ticks of $J_{\mathbb{Z}}$ |
| **$i \in \mathbb{C}$** | **Book II, Ch. `II.2` (algebra $\mathbb{C}$) and Ch. `II.6` (quantum scene)** | Imaginary unit of the field $\mathbb{C} = \mathbb{R}[i]/(i^2+1)$ and amplitude scalar in a Hilbert space $\mathcal{H}$ | Built as a complex extension via $J_{\mathbb{R}}^2 = -I_2$ in `Ch. II.2`, and in `Ch. II.6` multiplies state vectors and enters Born's rule $p = |\psi|^2$ | Cannot be derived from a pair of integer counters alone without completing $\mathbb{R}$ and adopting the quantum contract |

This transparent boundary keeps the reading of subsequent chapters reliable: the reader always knows exactly which of the four machines is operating on the page at any given moment.

---

## §I.5.7. The Integer Hadamard Map $H(a,b) = (a+b, a-b)$ and the Checkerboard Parity Sublattice

Let us return to a pair of integer contributions $(a, b) \in \mathbb{Z}^2$ in two wells and ask the most natural paired question: what is their **sum** $u = a + b$ and what is their **difference** $v = a - b$? This linear map

$$H : \mathbb{Z}^2 \longrightarrow \mathbb{Z}^2, \qquad H(a, b) = (a + b,\; a - b),$$

given by the already familiar matrix $H_{\mathrm{go}} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ of determinant $\det H = -2$, teaches an instructive lesson about how **invertibility and rank of one and the same rule depend on the chosen scalar ring**.

Try inverting the formula $(u, v) = (a+b, a-b)$ in school algebra: adding and subtracting the equations immediately gives $a = \frac{u+v}{2}$ and $b = \frac{u-v}{2}$. Over the field of rational numbers $\mathbb{Q}$, where division by two is always legal, the problem is solved completely: $H_{\mathbb{Q}} : \mathbb{Q}^2 \xrightarrow{\sim} \mathbb{Q}^2$ is a bijective automorphism.

In the integer lattice $\mathbb{Z}^2$, however, an odd integer cannot be divided by two. Take the target pair $(u, v) = (1, 0) \in \mathbb{Z}^2$: the formula demands $a = 1/2 \notin \mathbb{Z}$ and $b = 1/2 \notin \mathbb{Z}$, so no integer pair $(a, b)$ maps to $(1, 0)$. Where, then, does the image $H(\mathbb{Z}^2)$ land? Because the difference $(a + b) - (a - b) = 2b$ is always even, the sum $u$ and the difference $v$ must have **the same parity** (both even or both odd), landing precisely on the black squares of the infinite checkerboard

$$\mathcal{L} := \bigl\{(u, v) \in \mathbb{Z}^2 \;\big|\; u \equiv v \pmod 2\bigr\} \subsetneq \mathbb{Z}^2.$$

And here an even subtler second trap awaits. Since the image of all of $\mathbb{Z}^2$ is precisely the even sublattice $\mathcal{L}$, and $\mathcal{L}$ itself is mapped by $H$ into itself, does the restriction $H|_{\mathcal{L}} : \mathcal{L} \to \mathcal{L}$ finally become a bijective automorphism on $\mathcal{L}$? Look at the checkerboard diagram:

```text
      INITIAL LATTICE  Z^2                      EVEN CHECKERBOARD SUBLATTICE  L ⊂ Z^2
   (all integer nodes (a, b) ∈ Z^2)             (nodes • with u ≡ v (mod 2); nodes · unreachable)

        b                                               v
        1 |  •     •     •                              2 |  ◎     ·     ◎     (◎ lie in H(L) = 2Z^2)
          |                                               |
        0 |  •     •    [•]  <-- (1,0) ∉ L              1 |  ·    (•)    ·     <-- (1,1) ∈ L, but (1,1) ∉ H(L)!
          |          (a=1,b=0)                            |     (u=1,v=1)
       -1 |  •     •     •                              0 |  ◎     ·     ◎
          +─────────────── a                              +─────────────────── u
            -1     0     1                                   0     1     2
```

**Reader's caption to `Fig. I.5.4`:** action of the integer Hadamard transform $H(a,b)=(a+b,a-b)$. The map $H$ bijectively sends the entire lattice $\mathbb{Z}^2$ onto the index-$2$ checkerboard sublattice $\mathcal{L}$ (points `•` and `◎` of equal parity). Yet if the input is restricted to nodes of $\mathcal{L}$ itself, the image shrinks by another factor of two—into the even sublattice of multiples of two $H(\mathcal{L}) = (2\mathbb{Z})^2$ (nodes `◎`): for instance, the point $(1,1)$ belongs to $\mathcal{L}$, but its unique preimage $(1,0)$ lies on a white square outside $\mathcal{L}$.

> **Theorem I.5.3 (Integer Hadamard map, the even sublattice $\mathcal{L}$, and rank change under change of scalar ring).**  
> *Classical foundation.* The map $H(a,b) = (a+b, a-b)$ is given by the classical order-2 Hadamard–Sylvester matrix (Sylvester, 1867); its Smith invariant factors (H. Smith, 1861) equal $1$ and $2$, whence index $2$ of the image and rank drop modulo $2$. *Contribution of this book:* Reading the even checkerboard sublattice $\mathcal{L} \subset \mathbb{Z}^2$ as the exact image $H(\mathbb{Z}^2)$, non-invertibility of the restriction $H|_{\mathcal{L}}$ over $\mathbb{Z}$ (witness $(1,1) \in \mathcal{L} \setminus 2\mathbb{Z}^2$), and rank drop to `1` over $\mathbb{F}_2$ motivating the localization $\mathbb{Z}[1/2]$ in Book II.
> Let $H : \mathbb{Z}^2 \to \mathbb{Z}^2$ be defined by $H(a,b) = (a+b, a-b)$, and let $\mathcal{L} = \{(u,v) \in \mathbb{Z}^2 \mid u \equiv v \pmod 2\}$. Then:
> 1. $H$ is injective on $\mathbb{Z}^2$, not surjective onto $\mathbb{Z}^2$ ($(1,0) \notin \mathrm{im}\,H$), and defines an isomorphism of free abelian groups $\mathbb{Z}^2 \xrightarrow{\sim} \mathcal{L}$ with inverse map $H^{-1}|_{\mathcal{L}}(u,v) = \bigl(\frac{u+v}{2}, \frac{u-v}{2}\bigr)$.
> 2. The sublattice $\mathcal{L}$ is invariant under $H$, but the restriction $H|_{\mathcal{L}} : \mathcal{L} \to \mathcal{L}$ is again non-surjective: $H(\mathcal{L}) = (2\mathbb{Z})^2 \subsetneq \mathcal{L}$, and the point $(1,1) \in \mathcal{L}$ has no preimage inside $\mathcal{L}$ ($H^{-1}(1,1) = (1,0) \notin \mathcal{L}$).
> 3. Under extension of scalars to the field $\mathbb{Q}$, the map $H_{\mathbb{Q}} : \mathbb{Q}^2 \xrightarrow{\sim} \mathbb{Q}^2$ is bijective ($\mathrm{rank}_{\mathbb{Q}} H_{\mathbb{Q}} = 2$), whereas under reduction modulo $2$ to the field $\mathbb{F}_2$ the matrix $H_{\mathbb{F}_2} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ drops to rank $1$ with image $\{(0,0),(1,1)\}$ and satisfies $H_{\mathbb{F}_2}^2 = 0$.

*Proof.*  
1. From $(a+b)-(a-b)=2b$ follows $\mathrm{im}\,H \subseteq \mathcal{L}$, while the formulas $a = \frac{(a+b)+(a-b)}{2}$ and $b = \frac{(a+b)-(a-b)}{2}$ prove injectivity of $H$ on $\mathbb{Z}^2$. If $(u,v) \in \mathcal{L}$, then $u - v = 2k$ ($k \in \mathbb{Z}$) and $u + v = 2(v + k)$ are both even, so $a = \frac{u+v}{2} \in \mathbb{Z}$, $b = \frac{u-v}{2} \in \mathbb{Z}$, and $H(a,b) = (u,v)$, whence $\mathrm{im}\,H = \mathcal{L}$. The pair $(1,0)$ has coordinates of opposite parity and does not lie in $\mathcal{L}$.  
2. If $(a,b) \in \mathcal{L}$, then $a \equiv b \pmod 2$, so both $a+b$ and $a-b$ are divisible by $2$, i.e., $H(\mathcal{L}) \subseteq (2\mathbb{Z})^2$. Conversely, for any pair $(2p, 2q) \in (2\mathbb{Z})^2$, the integers $a = p + q$ and $b = p - q$ have the same parity ($a - b = 2q$), lie in $\mathcal{L}$, and give $H(a,b) = (2p, 2q)$. By injectivity of $H$, the unique preimage of $(1,1) \in \mathcal{L}$ in $\mathbb{Z}^2$ is $(1,0) \notin \mathcal{L}$.  
3. In $\mathrm{Mat}_2(\mathbb{Q})$, the inverse matrix is $\frac{1}{2} H_{\mathbb{Q}}$. In $\mathrm{Mat}_2(\mathbb{F}_2)$, we have $-1 \equiv 1 \pmod 2$, whence $H_{\mathbb{F}_2}(a,b) = (a \oplus b, a \oplus b) \in \{(0,0), (1,1)\}$ has image dimension $1$, and $H_{\mathbb{F}_2}^2(a,b) = ((a\oplus b)\oplus(a\oplus b), (a\oplus b)\oplus(a\oplus b)) = (0,0)$. $\square$

Item (3) of this theorem exhibits the exact geometric consequence: in a signless world (over $\mathbb{F}_2$, where $+1 = -1$), the sum $a+b$ and the difference $a-b$ **collapse into one and the same parity question** $a \oplus b$, the matrix $H_{\mathbb{F}_2}$ loses half its rank, and its square $H_{\mathbb{F}_2}^2 = 0$ vanishes identically instead of yielding the doubled identity $2I_2$. Sign holds open the second dimension of distinction.

---

## §I.5.8. Categorical Consolidation of the Chapter

Let us gather the signed extension construction into our six-line categorical template linking bare state carriers with the linear algebra of contributions:

- **Objects:** arbitrary sets of slots $X \in \mathbf{Set}$ and abelian groups ($\mathbb{Z}$-modules) of signed contributions $M \in \mathbf{Ab}$.
- **Arrows:** maps of sets $f : X \to Y$ in $\mathbf{Set}$ and homomorphisms of abelian groups $\varphi : M \to N$ ($\varphi(u+v)=\varphi(u)+\varphi(v)$, $\varphi(0)=0$, $\varphi(-u)=-\varphi(u)$) in $\mathbf{Ab}$.
- **Identities and composition:** ordinary set-theoretic identities and composition, mapped under the free-module functor to $\mathbb{Z}[\mathrm{id}_X] = \mathrm{id}_{\mathbb{Z}[X]}$ and $\mathbb{Z}[g \circ f] = \mathbb{Z}[g] \circ \mathbb{Z}[f]$.
- **Preserved structure:** the basis embedding of pure states $\eta_X : X \hookrightarrow U(\mathbb{Z}[X])$, $x \mapsto e_x$, and the linear extension of every deterministic step $T : X \to Y$ to the contribution transfer operator $\mathbb{Z}[T]\bigl(\sum c_x e_x\bigr) = \sum c_x e_{T(x)}$.
- **Universal property:** the free abelian group functor $\mathbb{Z}[-] : \mathbf{Set} \to \mathbf{Ab}$ is left adjoint to the forgetful functor $U : \mathbf{Ab} \to \mathbf{Set}$:
  $$\mathrm{Hom}_{\mathbf{Ab}}\bigl(\mathbb{Z}[X],\, M\bigr) \;\xrightarrow{\;\sim\;}\; \mathrm{Hom}_{\mathbf{Set}}\bigl(X,\, U(M)\bigr), \qquad \Phi \longmapsto \Phi \circ \eta_X.$$
- **Exposed pitfall and failure mode:** (a) the adjunction $\mathbb{Z}[-] \dashv U$ freely generates formal sums and differences $e_x - e_y$, but **does not automatically turn them into physically preparable states of the original instrument** (the set of pure slots $\eta_X(X)$ is not closed under subtraction in $U(\mathbb{Z}[X])$); (b) an injective endomorphism with non-zero determinant in $\mathbf{Ab}$—such as the Hadamard map $H : \mathbb{Z}^2 \to \mathbb{Z}^2$ with $\det H = -2$—becomes an isomorphism after tensoring with $-\otimes_{\mathbb{Z}} \mathbb{Q}$, yet **is not invertible over the ring $\mathbb{Z}$ itself** and degenerates into a rank-$1$ nilpotent after tensoring with $-\otimes_{\mathbb{Z}} \mathbb{F}_2$.

---

### Historical-Philosophical Note: Polar Pairs Versus the Three Guṇas of Prakṛti

1. **Motif from the classical source.** In Īśvarakṛṣṇa's *Sāṃkhya-kārikā* (`SK 12–13`), the three constituents of Prakṛti—*sattva* (clarity and capacity for manifestation), *rajas* (impulse and mobilization), and *tamas* (weight, restraint, and form)—operate inseparably, like the wick, oil, and flame of a single lamp (`SK 13`), mutually suppressing, supporting, and generating one another, whereas paired opposites such as heat and cold or attraction and repulsion (*dvandva*, cf. *Yoga-sūtras* `YS 2.48`) belong to polar oscillations within already unfolded experience.
2. **Strict realization in TNR.** The mathematical core of the present chapter clarifies why **the arithmetic triad of signs $\{-1, 0, +1\}$ on a single scalar channel must never be identified with the three guṇas of Sāṃkhya**. The signs $+1$ and $-1$ in the module $\mathbb{Z}[X]$ are symmetric additive opposites along *one and the same* contribution axis ($e_x + (-e_x) = 0$), with $0$ as their neutral equilibrium of silence. By contrast, the three operational roles of a dynamical scene from Chapters `I.1–I.3`—the **distinction question** $q \in \mathcal{Q}$, the **partial transition action** $T_a$ ($a \in \mathcal{A}$), and the **retained equivalence memory** ${\sim_\Gamma}$ (not to be confused with the triple of non-degeneracy, typing, and visible-shift predicates $(Z_D, Z_C, Z_F)$ from Theorem `I.1.0b`), with which the three guṇas are compared in Chapter `III.3`—belong to **three distinct component types of the contract $\Gamma$**: an action cannot be "added to a memory to yield zero" the way a white token and a black token cancel in a single well.
3. **Boundary of the comparison.** Neither the lamp simile of `SK 13` nor the doctrine of paired opposites (*dvandva*) enters any premise of Theorems `I.5.1–I.5.3` or replaces the algebraic definition of a free $\mathbb{Z}$-module; on the contrary, strict typing in TNR protects both the mathematics and the reading of the Indian texts from superficially conflating three heterogeneous functional roles with three markings on a single number line.

---

### Transition to Chapter `I.6`

We have seen how on one and the same finite carrier of slots $X$, changing the algebra of weights (from Boolean union to signed integer addition, from the ring $\mathbb{Z}$ to the fields $\mathbb{Q}$ and $\mathbb{F}_2$) radically alters the laws of path propagation and the rank of operators. In the next **Chapter `I.6`** we take the symmetric geometric step on finite sets and finite fields $\mathbb{F}_2, \mathbb{F}_3, \mathbb{F}_4$: we place six fixed terminals on the bench and verify that changing the *connectivity question itself* assembles the exact same points now into three disconnected dumbbells $3K_2$, now into the connected octahedron $O_6$, now into the cycle $C_6$, while further closure of operations generates the Fano plane $\mathrm{PG}(2,2)$, the Petersen graph, and error-correcting codes.

---

### Verifiability Passport for Chapter `I.5` (`Book I v3.3`)

- **Canonical node of the book:** `N05` (`Equipment Boundary B1`: free module of signed contributions $\mathbb{Z}[X]$, `Ban-Go` path interference, ternary cube $\{-1,0,+1\}^3$, quarter-turn $J_{\mathbb{Z}}$, Hadamard parity lattice $\mathcal{L}$).
- **Exact `Julia 1.12.6` verifications (single-threaded, no `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gates `GATE-I05-A` (absence of inverses in the Boolean monoid, dipole $e_+/e_-$, failure of `clamp`, shells `1+6+12+8=27`, ball `19=1+18`, and `13` axes of the cube $\{-1,0,+1\}^3$) and `GATE-I05-B` (Boolean shutter monotonicity $(A\odot P\odot B)_{ij} \le (A\odot B)_{ij}$, signed cancellation breakdown under shutter $H_{\mathrm{go}} P_1 H_{\mathrm{go}} = \mathbf{1}_{2\times 2}$ vs $H_{\mathrm{go}}^2 = 2I_2$, cycle of $J_{\mathbb{Z}}$, Hadamard isomorphism $\mathbb{Z}^2 \xrightarrow{\sim} \mathcal{L}$, witness $(1,1)\in\mathcal{L}\setminus H(\mathcal{L})$, and rank drop to `1` over $\mathbb{F}_2$).
- **Index of `Lean 4` specifications (`status: planned`, full cards in Appendix `VP`):** `TNR.BookI.I05.sign_not_complement`, `TNR.BookI.I05.ternary_cube_shells_and_rays`, `TNR.BookI.I05.ban_go_signed_cancellation`, `TNR.BookI.I05.integer_quarter_turn`, `TNR.BookI.I05.hadamard_parity_image`, `TNR.BookI.I05.free_signed_extension`.
- **Full 8-point figure passports for `Figs. I.5.1–I.5.4` and certification statement registry:** recorded in [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
