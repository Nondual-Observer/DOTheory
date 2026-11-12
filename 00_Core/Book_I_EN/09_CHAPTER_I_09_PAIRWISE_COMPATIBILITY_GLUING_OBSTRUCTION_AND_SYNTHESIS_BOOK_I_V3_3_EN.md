# Chapter I.9. Pairwise Compatibility, Gluing Obstruction, and Architectural Synthesis of Book I

> *"Two neighboring windows with a non-empty common trace on the seam always fit together into their fibered product; yet already three windows around an empty core can close up in such a way that every neighbor agrees with its neighbor, while no unified state of the whole exists at all."*

Eight preceding chapters have led us from the first act of binary distinction on an empty board (`Ch. I.1`) to modular and sequential windows (`Ch. I.8`). Throughout this entire path we either descended from a whole carrier $X$ to its partial projections, quotients, and windows, or assembled an answer back from individual observations. In `Theorem I.8.2` this inverse assembly proceeded without a cloud: when the divisor windows $m_1, \dots, m_k \mid N$ were carved out of a single pre-existing number $N = \operatorname{lcm}_i m_i$, pairwise agreement of traces on all intersections $\gcd(m_i, m_j)$ sufficed to uniquely reconstruct the common divisor $d$.

In the concluding chapter of Book I we will pose the main structural question about the limits of local knowledge: **is pairwise agreement of local windows always sufficient for a single global object to stand behind them?** The negative answer and the algebraic description of the obstruction link the local and global conditions of the finite core of DOT. We will see:
1. how already on three binary windows there arises **a gap between pairwise compatibility and global existence**, as well as a mirror phenomenon—**a ternary parity constraint invisible in every pairwise window** (`§I.9.1`);
2. how exact gluing of two and several systems along a common seam is organized (**the fibered product** $L \times_K R$ and associative composition of contracts, `§§I.9.2–I.9.3`);
3. how the language of finite **cochains and first cohomology $H^1$ over the field $\mathbb{F}_2$** translates a geometric "Möbius twist" on a cycle of windows into an exact linear-algebraic calculation, including on the nerve of the six two-point slices of our scene $S_4$ (`§I.9.4`), and how on the hollow tetrahedron the obstruction rises to the $H^2$ floor (`§I.9.5`);
4. how **reversible structural unfolding of a code** ($U \circ F = \mathrm{id}_E$) differs in principle from **behavioral Nerode memory compression** (`§I.9.6`);
5. finally, in **`§I.9.7`** we will assemble a unified architectural synthesis of the entire Book I: we will carry one and the same four-state scene $S_4$ through all nine chapters from `I.1` to `I.9`, bring together into a strict anti-numerological table all reference finite carriers of the first volume, and outline the boundary of transition to the operator-topological world of Book II.

---

## §I.9.1. Three Local Locks Without a Common Key and Invisibility of Ternary Parity in Pairwise Windows

Let us place three two-valued toggle switches $x, y, z \in \{0, 1\}$ on the table, but cover them with a lid having three sliding slots so that each of three inspectors simultaneously sees **only two** switches:
- the first inspector looks through window $U_{xy}$ at the pair $(x, y)$ and requires **coincidence**: $x = y$, admitting the local list $R_{xy} = \{(0, 0),\, (1, 1)\}$;
- the second inspector looks through window $U_{yz}$ at the pair $(y, z)$ and also requires **coincidence**: $y = z$, admitting the list $R_{yz} = \{(0, 0),\, (1, 1)\}$;
- the third inspector looks through window $U_{xz}$ at the pair $(x, z)$ and requires **opposition**: $x \neq z$, admitting the list $R_{xz} = \{(0, 1),\, (1, 0)\}$.

Let us compare the inspectors' reports pairwise. Each of the three local windows is non-empty (containing exactly two admissible states). On the common switch $y$, the first and second inspectors are in complete agreement: both permit $y = 0$ and $y = 1$, and together for the triple $(x, y, z)$ the first two windows leave two joint solutions $(0, 0, 0)$ and $(1, 1, 1)$. In exactly the same way, the second and third inspectors get along well with each other (admitting $(1, 0, 0)$ and $(0, 1, 1)$), as do the first and third (admitting $(0, 0, 1)$ and $(1, 1, 0)$). **Any two windows out of the three glue together.**

Yet let us try to set all three switches at once: from the first window $x = y$, from the second $y = z$, whence by transitivity of equality $x = z$—which is directly forbidden by the third window $x \neq z$. The set of global solutions is empty.

Alongside this classic "impossible triangle", on the very same three-bit cube $\mathbb{F}_2^3 = \{0, 1\}^3$ lives a second, even subtler phenomenon. Suppose the global subset of states is **non-empty** and consists of the four triples with an even sum of bits:

$$E_{\mathrm{even}} \;=\; \bigl\{(x_1, x_2, x_3) \in \mathbb{F}_2^3 \;:\; x_1 \oplus x_2 \oplus x_3 = 0\bigr\} \;=\; \bigl\{(0,0,0),\; (0,1,1),\; (1,0,1),\; (1,1,0)\bigr\}.$$

Let us look at this four-element set through all three pairwise projections $\pi_{12}, \pi_{13}, \pi_{23} : \mathbb{F}_2^3 \to \mathbb{F}_2^2$:
- in the window of the first two coordinates, $\pi_{12}(E_{\mathrm{even}}) = \{(0,0),\, (0,1),\, (1,0),\, (1,1)\} = \mathbb{F}_2^2$;
- in the window of the first and third coordinates, $\pi_{13}(E_{\mathrm{even}}) = \{(0,0),\, (0,1),\, (1,1),\, (1,0)\} = \mathbb{F}_2^2$;
- in the window of the second and third coordinates, $\pi_{23}(E_{\mathrm{even}}) = \{(0,0),\, (1,1),\, (0,1),\, (1,0)\} = \mathbb{F}_2^2$.

Every pairwise window sees **all four possible bit combinations once each**—precisely the same picture (both in carrier and even in uniform frequencies $1/4$) as is given by the full eight-element cube $\mathbb{F}_2^3$, where there is no connection among the switches at all.

```text
  (a) HOLLOW TRIANGLE OF CONSTRAINTS               (b) EVEN TETRAHEDRON E_even ⊂ F_2^3 (4 POINTS)
      (pairwise compatibility without global)          (rigid 3-law invisible in all 2-windows)

                y ∈ {0,1}                                    (0,1,1)*---------*(1,1,0)
               /         \                                         /|        /|
      x = y   /           \   y = z                               / |       / |
             /             \                                     *---------*  |
            /               \                                    |  |      |  |
     x ∈ {0,1} =========== z ∈ {0,1}                             |  *(0,0,0)--*
                 x != z                                          | /       | /
   Any 2 edges have 2 solutions;                                 *(1,0,1)--*
   traversing all 3 edges flips the bit: x -> x⊕1!    Projections π_12, π_13, π_23 yield all of F_2^2!
```
**Fig. I.9.1.** Two polar failures of naive reduction of the whole to pairs on the cube $\mathbb{F}_2^3$.  
In panel `(a)`, the three binary constraints $x = y$, $y = z$, $x \neq z$ form a discrete Möbius strip over a cycle of three vertices: along any unclosed path of two edges compatible values exist, but a full circuit around the cycle flips the bit phase and destroys all global sections. In panel `(b)`, the four marked vertices $x_1 \oplus x_2 \oplus x_3 = 0$ are bound by the rigid deterministic law $x_3 = x_1 \oplus x_2$, yet no two-dimensional coordinate window sees the slightest prohibition: in every pair of coordinates all four points of $\mathbb{F}_2^2$ are permitted.

Let us record both of these facts in the first strict statement of the chapter.

> **Proposition I.9.1 (Two boundaries of pairwise observation on three coordinates).**  
> *Classical foundation.* Pairwise consistency of projections in relational databases and sheaf theory vs. global compatibility and higher-order parity (XOR) constraints on $\mathbb{F}_2^3$. *Contribution of this book:* Paired minimal refutation of naive reductionism on the cube $\mathbb{F}_2^3$: the hollow triangle of three pairwise surjective windows with empty global intersection ($|\mathcal{R}| = 0$) and complete 2-invisibility of the even subspace $E_{\mathrm{even}}$ in all pairwise marginals ($|\mathcal{R}| > 1$).
> On the product of three two-valued carriers $\{0, 1\}^3$, two mutually complementary properties hold:
> 1. **Local compatibility without global gluing:** the family of pairwise relations $R_{xy} = \{x = y\}$, $R_{yz} = \{y = z\}$, $R_{xz} = \{x \neq z\}$ is pairwise compatible on each shared coordinate and any pair of relations out of the three is jointly satisfiable, yet the intersection of all three cylinders is empty: $\{(x,y,z) \in \{0,1\}^3 : (x,y)\in R_{xy},\, (y,z)\in R_{yz},\, (x,z)\in R_{xz}\} = \varnothing$.
> 2. **Ternary constraint under complete freedom of all pairs:** the subset $E_{\mathrm{even}} = \{x_1 \oplus x_2 \oplus x_3 = 0\}$ consists of $4$ elements (half of the cube $\mathbb{F}_2^3$), yet its projection onto each of the three pairs of coordinates bijectively covers the entire square $\mathbb{F}_2^2$; cylinder reconstruction from all pairwise projections $\bigcap_{i<j} \pi_{ij}^{-1}(\pi_{ij}(E_{\mathrm{even}})) = \mathbb{F}_2^3$ is strictly wider than $E_{\mathrm{even}}$.

*Proof.* In item 1, for any global solution $(x, y, z)$, addition modulo $2$ of the three conditions $x \oplus y = 0$, $y \oplus z = 0$, and $x \oplus z = 1$ gives on the left-hand side $(x \oplus x) \oplus (y \oplus y) \oplus (z \oplus z) = 0$, and on the right-hand side $0 \oplus 0 \oplus 1 = 1$—a contradiction $0 = 1$ in $\mathbb{F}_2$; when any single equation is dropped, the two remaining ones define two free bijections to the middle variable and have exactly $2$ solutions. In item 2, the equation $x_1 \oplus x_2 \oplus x_3 = 0$ uniquely expresses any third coordinate through the other two ($x_3 = x_1 \oplus x_2$ and cyclic permutations), so all three projections $\pi_{12}, \pi_{13}, \pi_{23} : E_{\mathrm{even}} \to \mathbb{F}_2^2$ are bijective, and the preimage of the entire square $\mathbb{F}_2^2$ under each projection coincides with all of $\mathbb{F}_2^3$. $\square$

Compare this result with **Chapter `I.6`** (`§I.6.3`): there we saw that if the 3-element lines of the Fano plane $\mathrm{PG}(2, 2)$ are replaced by their pairwise shadow (the 2-section), the specific geometry of the seven triples dissolves without a trace into the complete graph $K_7$. Now the cause of this phenomenon is laid bare to the limit: **between the level of pairs and the level of triples runs a genuine structural boundary**, on one side of which live ordinary graphs and binary gluings, and on the other—hypergraphs, 3-ary parity laws, and simplicial obstructions.

---

## §I.9.2. Three Traps of Naive Gluing of Local Descriptions

Before writing down the exact theorems on seam gluing and cohomology, let us examine three subtle traps that await a researcher when combining several local modules.

### Trap 1. Erasure of the Intermediate Seam Under Composition of Relations $E_{12} \circ E_{01}$
Suppose a process passes through three successive layers of states $S_0 \to S_1 \to S_2$ (say, $S_0 = S_1 = S_2 = \{0, 1\}$), where at the first step the transitions $E_{01} = \{(0, 0),\, (0, 1)\} \subset S_0 \times S_1$ are admissible, and at the second step the transitions $E_{12} = \{(0, 0),\, (1, 0)\} \subset S_1 \times S_2$ are admissible. How should one describe the two-step system? If we simply multiply the relations by the rules of the category $\mathbf{Rel}$:
$$E_{12} \circ E_{01} \;=\; \bigl\{(s_0, s_2) \in S_0 \times S_2 \;:\; \exists\, s_1 \in S_1,\; (s_0, s_1) \in E_{01} \land (s_1, s_2) \in E_{12}\bigr\} \;=\; \{(0, 0)\},$$
then we obtain **only a single** pair of endpoints $(0, 0)$. Two genuinely distinct trajectories—the upper path $0 \to 0 \to 0$ and the lower path $0 \to 1 \to 0$ (those very two interferometer arms from `Ch. I.5`, capable of mutually canceling each other when endowed with sign)—have merged into a single point under relational composition, because the existential quantifier $\exists s_1$ erased the memory of *which point of the seam $S_1$* the system passed through. To preserve both histories $(0, 0, 0)$ and $(0, 1, 0)$ without loss, gluing must be performed by **the fibered product** $E_{01} \times_{S_1} E_{12}$ (where $|E_{01} \times_{S_1} E_{12}| = 2 \neq 1 = |E_{12} \circ E_{01}|$).

### Trap 2. False Requirement of Global Dynamics on Unreachable Points of the Seam
Suppose the left subsystem $(L, T_L)$ and the right subsystem $(R, T_R)$ look at a common seam alphabet $K$ through reading maps $p_L : L \to K$ and $p_R : R \to K$. It is often assumed that for a compatible joint step $(T_L, T_R)$ on the glued space $L \times_K R = \{(\ell, r) : p_L(\ell) = p_R(r)\}$, on the seam $K$ itself there must necessarily exist a single autonomous step $\tau : K \to K$ closing the squares $p_L \circ T_L = \tau \circ p_L$ and $p_R \circ T_R = \tau \circ p_R$ on all of $K$. This is **redundant (and false as a necessary condition)** in two cases:
1. if the images $p_L(L)$ and $p_R(R)$ intersect only along a proper part of the seam $K_0 = p_L(L) \cap p_R(R) \subsetneq K$, then behavior outside $K_0$ does not participate in any glued pair $(\ell, r) \in L \times_K R$ at all: for instance, when $K = \{0, 1\}$, $L = \{a, b, c\}$ with reading $p_L(a) = p_L(b) = 1,\, p_L(c) = 0$, $R = \{r\}$ with $p_R(r) = 0$, and steps $T_L(a) = a,\, T_L(b) = c,\, T_L(c) = c$, $T_R(r) = r$, the one-element glued set $L \times_K R = \{(c, r)\}$ is invariant under $(T_L, T_R)$, even though no map $\tau : K \to K$ with the property $p_L \circ T_L = \tau \circ p_L$ exists ($p_L(a) = p_L(b) = 1$, yet $p_L(T_L(a)) = 1 \neq 0 = p_L(T_L(b))$);
2. even when both readings $p_L, p_R$ are surjective onto $K_0$, the new seam value $p_L(T_L(\ell)) = p_R(T_R(r))$ may be uniquely determined on $K_0$ only thanks to the coincidence $p_L(\ell) = p_R(r)$: if both $p_L : L \twoheadrightarrow K$ and $p_R : R \twoheadrightarrow K$ are surjective onto all of $K$, then preservation of $L \times_K R$ indeed forces a unique autonomous seam law $\tau : K \to K$, but in the general case the exact necessary and sufficient condition is the equality $p_L(T_L(\ell)) = p_R(T_R(r))$ **specifically for all compatible pairs** $(\ell, r) \in L \times_K R$.

### Trap 3. Confusing Reversible Code Unfolding with Behavioral Nerode Compression
In applied discussions, two diametrically opposite operations are often called by one and the same word "folding":
- **structural packing** of an expression tree $e \in E$ into a code $F(e) \in S$ (for instance, a Gödel or syntactic encoding), admitting unambiguous unpacking $U(F(e)) = e$;
- **behavioral factorization** $F_{\mathrm{beh}} : E \twoheadrightarrow E / {\sim_\Gamma}$ from `Chapter I.3`, which glues together different past histories having the same future response.

As we will strictly prove in `§I.9.6`, mixing these two arrows in calculations is impermissible: the first map must be **injective**, whereas the second by its very nature is **non-injective** wherever non-trivial memory compression occurs, and therefore in principle has no unambiguous inverse decoder $U$.

---

## §I.9.3. Gluing Along a Common Seam and Canonical Associativity of Contract Composition

Let us pass from cautions to exact assembly constructions. Suppose two finite (or arbitrary) state domains $L$ and $R$ are linked by a common compatibility window ("seam") $K$ via seam-reading maps $p_L : L \to K$ and $p_R : R \to K$. **The fibered product** (or *gluing along the seam $K$*) is the subset of the Cartesian product

$$L \times_K R \;=\; \bigl\{(\ell, r) \in L \times R \;:\; p_L(\ell) = p_R(r)\bigr\},$$

equipped with the natural projections $\pi_L(\ell, r) = \ell$ and $\pi_R(\ell, r) = r$, on which the commutative square $p_L \circ \pi_L = p_R \circ \pi_R$ closes.

> **Theorem I.9.1 (Universal property of seam gluing and criterion of a coupled step).**  
> *Classical foundation.* The universal property of seam gluing is the classical universal property of the fibered product (pullback) in the category $\mathbf{Set}$. *Contribution of this book:* Criterion for a coupled step of two partial contracts without requiring a global endomorphism on the full seam scale $K$, plus exact condition for the birth of phantom pairs (`2 → 4`) upon seam coarsening.
> 1. **Universality of static gluing:** for any carrier $W$ and any pair of maps $f_L : W \to L$, $f_R : W \to R$ compatible on the seam ($p_L \circ f_L = p_R \circ f_R$), there exists a unique map $h : W \to L \times_K R$ for which $\pi_L \circ h = f_L$ and $\pi_R \circ h = f_R$, namely $h(w) = \bigl(f_L(w),\, f_R(w)\bigr)$.
> 2. **Criterion of coupled dynamics:** a pair of local steps $T_L : L \to L$ and $T_R : R \to R$ induces a well-defined joint step $T_{L \times_K R}(\ell, r) = \bigl(T_L(\ell),\, T_R(r)\bigr)$ on the glued carrier $L \times_K R$ if and only if for every glued pair $(\ell, r) \in L \times_K R$ the equality $p_L(T_L(\ell)) = p_R(T_R(r))$ holds. In the special case where there exists a seam map $\tau : K \to K$ with the properties $p_L \circ T_L = \tau \circ p_L$ and $p_R \circ T_R = \tau \circ p_R$, the coupling condition holds automatically, and the seam itself moves deterministically according to the law $\tau$.

*Proof.*  
1. If $h(w) = (u(w), v(w)) \in L \times_K R$ satisfies $\pi_L \circ h = f_L$ and $\pi_R \circ h = f_R$, then $u(w) = f_L(w)$ and $v(w) = f_R(w)$, which proves uniqueness; the condition $p_L(f_L(w)) = p_R(f_R(w))$ guarantees that the pair $(f_L(w), f_R(w))$ falls into the subset $L \times_K R$ for every $w \in W$.  
2. The coordinatewise pair $(T_L(\ell), T_R(r))$ belongs to $L \times_K R$ for all $(\ell, r) \in L \times_K R$ by definition of the set $L \times_K R$ if and only if $p_L(T_L(\ell)) = p_R(T_R(r))$. If a seam morphism $\tau$ is given, then whenever $p_L(\ell) = p_R(r)$ we have $p_L(T_L(\ell)) = \tau(p_L(\ell)) = \tau(p_R(r)) = p_R(T_R(r))$. $\square$

What happens when we assemble a long chain of three (and any finite number of) modules $A$, $B$, $C$, where $A$ is sewn to $B$ along a first seam $K_1$ ($p_A : A \to K_1$, $q_B : B \to K_1$), while $B$ is simultaneously sewn to $C$ along a second seam $K_2$ ($p_B : B \to K_2$, $q_C : C \to K_2$)? Does the result of the assembly depend on whether we first join the left pair $(A \times_{K_1} B)$ and then attach $C$ to it along the projection $p_B \circ \pi_B : A \times_{K_1} B \to K_2$, or start with the right pair $B \times_{K_2} C$?

> **Theorem I.9.2 (Associativity of sequential gluing of contracts along a chain of seams).**  
> *Classical foundation.* Associativity of sequential gluing is the classical canonical isomorphism of iterated fibered products $(A \times_B C) \times_D E \cong A \times_B (C \times_D E)$. *Contribution of this book:* Transfer of canonical pullback associativity to chains of operational contracts together with their partial steps and readings (`64 → 16 = 16` trajectories), contrasted with path-multiplicity loss in relational composition.
> Suppose seam-reading diagrams $A \xrightarrow{p_A} K_1 \xleftarrow{q_B} B \xrightarrow{p_B} K_2 \xleftarrow{q_C} C$ are given. Then the re-parenthesization map
> $$\alpha\bigl((a, b),\, c\bigr) \;=\; \bigl(a,\, (b, c)\bigr)$$
> defines a canonical isomorphism of the glued carriers
> $$(A \times_{K_1} B) \times_{K_2} C \;\xrightarrow{\;\sim\;}\; A \times_{K_1} (B \times_{K_2} C),$$
> identifying both assemblies with the set of compatible triples $\{(a, b, c) \in A \times B \times C : p_A(a) = q_B(b) \land p_B(b) = q_C(c)\}$. If the local steps $T_A, T_B, T_C$ are pairwise compatible on the seams $K_1$ and $K_2$, then the isomorphism $\alpha$ intertwines the joint steps of both assemblies.

*Proof.* An element $((a, b), c)$ belongs to the left assembly if and only if $(a, b) \in A \times_{K_1} B$ (i.e., $p_A(a) = q_B(b)$) and $(p_B \circ \pi_B)(a, b) = q_C(c)$ (i.e., $p_B(b) = q_C(c)$). Symmetrically, $(a, (b, c))$ belongs to the right assembly if and only if $p_B(b) = q_C(c)$ and $p_A(a) = (q_B \circ \pi'_B)(b, c) = q_B(b)$. The conditions are identical, so $\alpha$ is bijective and coordinatewise preserves $(T_A(a), T_B(b), T_C(c))$. $\square$

Let us illustrate this theorem on a concrete three-block chain of four-state cells $A = B = C = \{0, 1\}^2$ with seams $p_A(a_1, a_2) = a_2$, $q_B(b_1, b_2) = b_1$ and $p_B(b_1, b_2) = b_2$, $q_C(c_1, c_2) = c_1$: out of the $4 \times 4 \times 4 = 64$ triples, the conditions of the two single-bit seams $a_2 = b_1$ and $b_2 = c_1$ carve out exactly $64 / (2 \cdot 2) = 16$ compatible states in both the left and right parenthesizations, while the local steps $T_A(a_1, a_2) = (a_1 \oplus a_2,\, a_2 \oplus 1)$, $T_B(b_1, b_2) = (b_1 \oplus 1,\, b_2)$, $T_C(c_1, c_2) = (c_1,\, c_1 \oplus c_2)$ preserve both seams ($\tau_1(k) = k \oplus 1$ and $\tau_2(k) = k$) across all $16$ states.

> **Corollary I.9.1 (Composition of partial contract simulations and the trap of premature seam coarsening).**  
> 1. **Vertical composition of simulations:** if $\Gamma_1, \Gamma_2, \Gamma_3$ are three operational contracts sharing a common signature of questions and partial actions, and the maps $f : X_1 \to X_2$ and $g : X_2 \to X_3$ are strict simulations (preserving the answers of all questions $q^{(2)} \circ f = q^{(1)}$, exactly reflecting and preserving domains of admissibility $x \in D_a^{(1)} \iff f(x) \in D_a^{(2)}$, and intertwining steps $f(T_a^{(1)} x) = T_a^{(2)} f(x)$ on $D_a^{(1)}$, and similarly for $g$), then the composite map $g \circ f : X_1 \to X_3$ is also a strict contract simulation and preserves full protocol equivalence ($x \sim_{\Gamma_1} y \iff (g \circ f)(x) \sim_{\Gamma_3} (g \circ f)(y)$).  
> 2. **Inadmissibility of coarsening the seam prior to gluing:** replacing the seam alphabet $K$ by a non-injective quotient $\pi : K \twoheadrightarrow \overline{K}$ prior to taking the fibered product always satisfies the inclusion $L \times_K R \subseteq L \times_{\overline{K}} R$ and strictly enlarges the carrier with spurious incompatible pairs if and only if $\pi$ glues together two distinct values that are actually attained on the left and on the right ($k_1 \in p_L(L),\, k_2 \in p_R(R)$ with $k_1 \neq k_2$ and $\pi(k_1) = \pi(k_2)$): already for $L = R = K = \{0, 1\}$, $p_L = p_R = \mathrm{id}_K$, the true gluing $L \times_K R = \{(0, 0),\, (1, 1)\}$ contains `2` synchronized states, whereas compressing the seam to a one-point set $\overline{K} = \{*\}$ inflates $L \times_{\{*\}} R = L \times R$ to `4` pairs, adding `2` phantom states $(0, 1)$ and $(1, 0)$ that do not lift to any true pair on the seam $K$.

Notice the decisive geometric difference between `Theorem I.9.2` and `Proposition I.9.1(1)`: **an unclosed linear chain (or any finite tree without cycles) of non-empty local windows with surjective restriction maps onto every intermediate seam always has global states**, because a choice of state in the root window extends step by step along the branches to the leaves without self-intersections. An obstruction under surjective seams is born at the exact instant when the seams close into a **cycle**.

---

## §I.9.4. Cochains and the $H^1$ Obstruction Over $\mathbb{F}_2$: From the Hollow Triangle to the Nerve of the Six Slices of $S_4$

To unerringly detect and count closed twists on an arbitrary network of overlapping windows, let us introduce the minimal and elementary apparatus of **simplicial cochains over the field $\mathbb{F}_2 = \{0, 1\}$**—the sole homological tool that requires neither edge orientations, nor limits, nor infinite spaces, since in $\mathbb{F}_2$ every element is its own opposite ($-1 \equiv +1 \pmod 2$).

Let $X = (V, E, F)$ be a finite two-dimensional simplicial complex consisting of a set of vertices $V$, a set of unordered edges $E \subseteq \binom{V}{2}$, and a set of filled triangular faces $F \subseteq \binom{V}{3}$ (where all three edges of every face $\{u, v, t\} \in F$ belong to $E$). Form three finite-dimensional vector spaces over the field $\mathbb{F}_2$:
- **0-cochains** $C^0(X; \mathbb{F}_2) = \{g : V \to \mathbb{F}_2\}$—local recalibrations (renamings of zeros and ones) at the vertices;
- **1-cochains** $C^1(X; \mathbb{F}_2) = \{w : E \to \mathbb{F}_2\}$—compatibility bits on the edges ($w(uv) = 0$ means direct gluing $x_u = x_v$, while $w(uv) = 1$ means gluing with a flip $x_u = x_v \oplus 1$);
- **2-cochains** $C^2(X; \mathbb{F}_2) = \{f : F \to \mathbb{F}_2\}$—discrepancies around filled triangular faces.

Connect them by two linear **coboundary operators** $\delta_0 : C^0 \to C^1$ and $\delta_1 : C^1 \to C^2$:

$$(\delta_0 g)(uv) \;=\; g(u) \oplus g(v) \quad (uv \in E), \qquad (\delta_1 w)(uvt) \;=\; w(uv) \oplus w(ut) \oplus w(vt) \quad (uvt \in F).$$

Let us verify the identity $\delta_1 \circ \delta_0 = 0$: for any vertex gauge $g \in C^0$ and any filled face $uvt \in F$, each vertex enters the boundary of the triangle in exactly two edges, so

$$(\delta_1(\delta_0 g))(uvt) \;=\; \bigl(g(u) \oplus g(v)\bigr) \oplus \bigl(g(u) \oplus g(t)\bigr) \oplus \bigl(g(v) \oplus g(t)\bigr) \;=\; 0 \pmod 2!$$

Every coboundary $\delta_0 g \in B^1(X; \mathbb{F}_2) = \operatorname{im} \delta_0$ is a **1-cocycle**, i.e., lies in $Z^1(X; \mathbb{F}_2) = \ker \delta_1$ ($B^1 \subseteq Z^1$). The quotient space

$$H^1(X; \mathbb{F}_2) \;=\; Z^1(X; \mathbb{F}_2) \,\big/\, B^1(X; \mathbb{F}_2), \qquad \dim_{\mathbb{F}_2} H^1(X; \mathbb{F}_2) \;=\; \dim_{\mathbb{F}_2} Z^1 - \dim_{\mathbb{F}_2} B^1 \;=\; (|E| - \operatorname{rank}\delta_1) - \operatorname{rank}\delta_0$$

is called **the first cohomology group of the complex $X$ over $\mathbb{F}_2$**. What is its direct operational meaning for the observer? The equation of global compatibility of local bits $x_u \oplus x_v = w(uv)$ across all edges $uv \in E$ is solvable if and only if $w = \delta_0 x \in B^1(X; \mathbb{F}_2)$. Thus:
- the condition $\delta_1 w = 0$ ($w \in Z^1$) tests **local compatibility on all filled triple intersections** $uvt \in F$;
- a non-zero class $[w] \neq 0$ in $H^1(X; \mathbb{F}_2)$ certifies **global unsolvability of the system under complete compatibility of all triple faces**—none of the $2^{|V|}$ vertex recalibrations is capable of eliminating an odd number of flips around hollow cycles.

Let us first see how this formula separates the hollow and filled triangles in the scene from `§I.9.1`.

> **Lemma I.9.1 (Hollow triangle $\Delta_3^{(1)}$ vs. filled simplex $\Delta_3$).**  
> *Classical foundation.* Simplicial nerve of a finite cover (Alexandroff, 1928) and Čech coboundary complex $\delta_1 \circ \delta_0 = 0$ over $\mathbb{F}_2$ (Čech, 1932). *Contribution of this book:* Direct operational reading of 0-cochains as vertex gauges of local windows, 1-cocycles as edge shifts compatible on filled faces, and $H^1(\mathcal{N}; \mathbb{F}_2)$ as a gauge-invariant gluing obstruction.
> Suppose on three vertices $V = \{1, 2, 3\}$ and three edges $E = \{12, 23, 13\}$ a 1-cochain $w = (0, 0, 1)$ is given (the equations $x_1 = x_2$, $x_2 = x_3$, $x_1 \neq x_3$).
> 1. On the **hollow triangle** $\Delta_3^{(1)} = (V, E, \varnothing)$ without a two-dimensional face, the operator $\delta_1$ is zero, so $w \in Z^1(\Delta_3^{(1)}; \mathbb{F}_2) = C^1$, whereas $\operatorname{rank}\delta_0 = 2$ and $\dim_{\mathbb{F}_2} H^1(\Delta_3^{(1)}; \mathbb{F}_2) = 3 - 0 - 2 = 1$: the cochain $w$ represents the unique non-trivial class $[w] \neq 0$ in $H^1(\Delta_3^{(1)}; \mathbb{F}_2) \cong \mathbb{F}_2$.
> 2. On the **filled triangle** $\Delta_3 = (V, E, \{123\})$, the 2-face $123$ appears, on which $(\delta_1 w)(123) = 0 \oplus 0 \oplus 1 = 1 \neq 0$: the cochain $w$ **ceases to be a 1-cocycle** ($w \notin Z^1(\Delta_3; \mathbb{F}_2)$), the contradiction is detected directly inside the triple window $123$, and the cohomology group itself is trivial: $H^1(\Delta_3; \mathbb{F}_2) = 0$ ($\operatorname{rank}\delta_1 = 1$, $3 - 1 - 2 = 0$).

Let us apply this construction to the four-element scene $S_4 = \{(x, c) : x, c \in \{0, 1\}\}$. Recall that on $S_4$ three binary questions are given: the visible bit $q_x(x, c) = x$, the hidden trace $q_c(x, c) = c$, and the parity question $q_\beta(x, c) = x \oplus c$. Each of them partitions $S_4$ into a pair of two-point slices (fibers of constant answer), yielding a cover of $S_4$ by **six two-point windows**:

$$\begin{aligned}
X_0 &= \{x = 0\} = \{00,\, 01\}, &\qquad X_1 &= \{x = 1\} = \{10,\, 11\}, \\
C_0 &= \{c = 0\} = \{00,\, 10\}, &\qquad C_1 &= \{c = 1\} = \{01,\, 11\}, \\
B_0 &= \{x \oplus c = 0\} = \{00,\, 11\}, &\qquad B_1 &= \{x \oplus c = 1\} = \{01,\, 10\}.
\end{aligned}$$

Let us construct **the nerve $\mathcal{N}$ of this cover**: the vertices are the $6$ slices $\{X_0, X_1, C_0, C_1, B_0, B_1\}$ themselves, two slices with a non-empty intersection are joined by an edge, and a triple of slices with a non-empty **triple** intersection in $S_4$ is declared a filled 2-face. How is this nerve organized as a geometric object?
- Parallel fibers of a single question are disjoint ($X_0 \cap X_1 = C_0 \cap C_1 = B_0 \cap B_1 = \varnothing$), while any two slices from **different** questions intersect in exactly one state of $S_4$. Thus the 1-skeleton of the nerve has $6$ vertices and $12$ edges—it is once again our **octahedron graph** $K_{2,2,2}$ familiar from `Chapter I.6`.
- The octahedron has $2 \times 2 \times 2 = 8$ triangular cycles of the form $(X_i, C_j, B_k)$. In which of them is the triple intersection $X_i \cap C_j \cap B_k$ non-empty? In the intersection $X_i \cap C_j$ lies the unique point $(i, j) \in S_4$, and it falls into $B_k$ if and only if $i \oplus j = k$, i.e., $i \oplus j \oplus k = 0$.

Thus the nerve $\mathcal{N}$ is a **checkerboard half-filled octahedron**: exactly **four** of its triangular faces ($i \oplus j \oplus k = 0$) are spanned by two-dimensional cells (corresponding to the four points $00, 01, 10, 11 \in S_4$), while the remaining **four** triangular faces ($i \oplus j \oplus k = 1$) remain unfilled.

Let us define on the $12$ edges of the nerve $\mathcal{N}$ an explicit 1-cochain of flips $w \in C^1(\mathcal{N}; \mathbb{F}_2)$ by the rules

$$w(X_i, C_j) \;=\; i \oplus j, \qquad w(X_i, B_k) \;=\; k, \qquad w(C_j, B_k) \;=\; 0 \qquad (i, j, k \in \{0, 1\})$$

and bring all $8$ triangles of the octahedron together into a full verification table.

#### Table I.9.1. Complete Calculation of All 8 Triangles of the Nerve of the Six Slices of $S_4$ and the Cochain $w$

| # | Triple of slices $(X_i, C_j, B_k)$ | Parity $i \oplus j \oplus k$ | Triple intersection $X_i \cap C_j \cap B_k$ in $S_4$ | Face status in nerve $\mathcal{N}$ | Edge weights $(w_{XC},\, w_{XB},\, w_{CB})$ | Cycle sum $w_{XC} \oplus w_{XB} \oplus w_{CB}$ |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: |
| `1` | $(X_0, C_0, B_0)$ | $0$ | $\{00\}$ | **Filled** ($\in F$) | $(0,\, 0,\, 0)$ | **`0`** ($\delta_1 w = 0$) |
| `2` | $(X_0, C_1, B_1)$ | $0$ | $\{01\}$ | **Filled** ($\in F$) | $(1,\, 1,\, 0)$ | **`0`** ($\delta_1 w = 0$) |
| `3` | $(X_1, C_0, B_1)$ | $0$ | $\{10\}$ | **Filled** ($\in F$) | $(1,\, 1,\, 0)$ | **`0`** ($\delta_1 w = 0$) |
| `4` | $(X_1, C_1, B_0)$ | $0$ | $\{11\}$ | **Filled** ($\in F$) | $(0,\, 0,\, 0)$ | **`0`** ($\delta_1 w = 0$) |
| `5` | $(X_0, C_0, B_1)$ | $1$ | $\varnothing$ | *Hollow hole* ($\notin F$) | $(0,\, 1,\, 0)$ | **`1`** (twist) |
| `6` | $(X_0, C_1, B_0)$ | $1$ | $\varnothing$ | *Hollow hole* ($\notin F$) | $(1,\, 0,\, 0)$ | **`1`** (twist) |
| `7` | $(X_1, C_0, B_0)$ | $1$ | $\varnothing$ | *Hollow hole* ($\notin F$) | $(1,\, 0,\, 0)$ | **`1`** (twist) |
| `8` | $(X_1, C_1, B_1)$ | $1$ | $\varnothing$ | *Hollow hole* ($\notin F$) | $(0,\, 1,\, 0)$ | **`1`** (twist) |

```text
  NERVE N OF THE SIX TWO-POINT SLICES OF SCENE S_4: CHECKERBOARD OCTAHEDRON (4 FILMS + 4 HOLES)

                         B_0 {00,11}
                        /   |    \
                       / [00|11]  \      [00], [01], [10], [11] — 4 FILLED faces:
                      /     |      \       on each of them the weight sum of w equals 0 (δ_1 w = 0)!
               X_0 ---------|------- C_1
                |  \ (hole) | [01] /  |  (hole) — 4 HOLLOW faces X_i ∩ C_j ∩ B_k = ∅:
                |   \       |     /   |    around each hole the weight sum of w equals 1!
               C_0 ---------|------- X_1
                      \ [10]|      /     Result over F_2: |V|=6, |E|=12, |F|=4, χ = 6-12+4 = -2,
                       \    |     /      rank δ_0 = 5, rank δ_1 = 4  ==>  dim H^1(N; F_2) = 3!
                         B_1 {01,10}
```
**Fig. I.9.2.** The checkerboard octahedron of the nerve $\mathcal{N}$ of the six slices of the four-state scene $S_4$.  
The six vertices correspond to the two-point fibers of the three questions $q_x, q_c, q_\beta$, the twelve edges to single-point pairwise intersections, and the four spanned triangular films to the four states $00, 01, 10, 11 \in S_4$ themselves. The cochain $w$ is compatible on all four points of $S_4$ ($\delta_1 w = 0$), yet carries a unit twist around each of the four empty faces and is not eliminated by any of the $64$ vertex gauges.

In `Table I.9.1` the splitting of local and global regimes is seen with complete clarity: on all four real states of the world $S_4$ (rows `1–4`) the sum of flips equals zero, i.e., $w$ is **a genuine 1-cocycle** ($\delta_1 w = 0$). If the observer checks compatibility not only on edges, but even on all non-empty triple intersections of their windows, they will detect not a single flaw. And nevertheless, in rows `5–8` around each of the four empty triangular holes the sum of flips equals $1$—a global assignment of bits to the six slices **does not exist**.

> **Theorem I.9.3 (Cohomological passport of the nerve of the six slices of $S_4$).**  
> *Classical foundation.* Simplicial cohomology of two-dimensional cell and simplicial complexes over $\mathbb{F}_2$ and linear algebra of coboundary ranks. *Contribution of this book:* Construction of the nerve $\mathcal{N}$ of the six two-element slices of $S_4$ as a checkerboard octahedron (`6` vertices, `12` edges, `4` filled and `4` hollow faces) and exact computation $\mathrm{rk}\,\delta_0 = 5$, $\mathrm{rk}\,\delta_1 = 4$, $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$.
> The nerve $\mathcal{N}$ of the cover of the four-state scene $S_4 = \mathbb{F}_2^2$ by the six two-point fibers $X_0, X_1, C_0, C_1, B_0, B_1$ is a connected two-dimensional simplicial complex with $6$ vertices, $12$ edges, $4$ two-dimensional faces, and Euler characteristic $\chi(\mathcal{N}) = 6 - 12 + 4 = -2$. Over the field $\mathbb{F}_2$, the ranks of the coboundary operators equal $\operatorname{rank}_{\mathbb{F}_2} \delta_0 = 5$ and $\operatorname{rank}_{\mathbb{F}_2} \delta_1 = 4$, whence
> $$\dim_{\mathbb{F}_2} Z^1(\mathcal{N}; \mathbb{F}_2) = 12 - 4 = 8, \qquad \dim_{\mathbb{F}_2} B^1(\mathcal{N}; \mathbb{F}_2) = 5, \qquad \dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 8 - 5 = 3,$$
> while the second cohomology group is trivial: $H^2(\mathcal{N}; \mathbb{F}_2) = 0$. The 1-cochain $w$ exhibited above lies in $Z^1(\mathcal{N}; \mathbb{F}_2) \setminus B^1(\mathcal{N}; \mathbb{F}_2)$: none of the $2^6 = 64$ vertex gauges $g \in C^0(\mathcal{N}; \mathbb{F}_2)$ satisfies the equation $\delta_0 g = w$.

*Proof.* Since the octahedron graph is connected, the kernel $\ker \delta_0$ consists of exactly the two constant functions ($g \equiv 0$ and $g \equiv 1$), whence $\operatorname{rank}_{\mathbb{F}_2} \delta_0 = 6 - 1 = 5$. Each of the four filled faces $F_1 = (X_0, C_0, B_0)$, $F_2 = (X_0, C_1, B_1)$, $F_3 = (X_1, C_0, B_1)$, $F_4 = (X_1, C_1, B_0)$ contains its own private edge of type $(C_j, B_k)$ that does not enter any of the other three filled faces: the edge $C_0 B_0$ enters only $F_1$, $C_1 B_1$ enters only $F_2$, $C_0 B_1$ enters only $F_3$, and $C_1 B_0$ enters only $F_4$. Consequently, in the $4 \times 12$ matrix $\delta_1$ over the four columns of edges $(C_j, B_k)$ stands the $4 \times 4$ identity submatrix $I_4$, which immediately gives $\operatorname{rank}_{\mathbb{F}_2} \delta_1 = 4$ and surjectivity of $\delta_1 : C^1 \twoheadrightarrow C^2$ ($H^2 = 0$), and by the dimension formula $\dim_{\mathbb{F}_2} H^1 = 12 - 5 - 4 = 3$. Finally, by `Table I.9.1`, $\delta_1 w = 0$, yet on the hollow triple $(X_0, C_0, B_1)$ any coboundary $\delta_0 g$ would give the sum $(g(X_0)\oplus g(C_0)) \oplus (g(X_0)\oplus g(B_1)) \oplus (g(C_0)\oplus g(B_1)) = 0 \neq 1 = w(X_0 C_0) \oplus w(X_0 B_1) \oplus w(C_0 B_1)$, so $w \notin B^1$. $\square$

Let us bind together the results of Book I (`Chapters I.1 → I.2 → I.6 → I.9`), joining the dynamic transfer holonomy from `Theorem I.2.4`, the checkerboard partition of the triangles of the octahedron $O_6$ from `Theorem I.6.1`, and the presheaf formulation of contextuality in the spirit of S. Abramsky and A. Brandenburger (`2011`).

> **Theorem I.9.3a (Backbone Theorem of Book I: return holonomy $H_3$, checkerboard octahedron $O_6$, and the $\mathbb{F}_2$-torsor presheaf $\mathcal{S}_w$).**  
> *Classical foundation.* Presheaves of sets and $\mathbb{F}_2$-torsors (principal homogeneous bundles with structure group $\mathbb{F}_2$) over a simplicial nerve (Leray, 1945–1950). *Contribution of this book:* Backbone Theorem of Book I: exact equivalence between odd holonomy charge $\kappa = c_0 \oplus x_0 \oplus b_0 = 1$ from Chapter `I.2` and the `4` hollow faces of $\mathcal{N}$, plus explicit torsor presheaf $\mathcal{S}_w$ having `2` local sections everywhere and `0` global sections.
> Let the three binary questions $q_x(x,c) = x$, $q_c(x,c) = c$, $q_\beta(x,c) = x \oplus c$ and their six two-point slices $X_{x_0}, C_{c_0}, B_{b_0}$ ($x_0, c_0, b_0 \in \mathbb{F}_2$) be fixed on the four-state scene $S_4 = \mathbb{F}_2^2$.
> 1. **Isomorphism of the 1-skeleton of the nerve $\mathcal{N}$ and the octahedron $O_6$ (`Chapter I.6`):** associating each slice with that unique non-constant affine question from $A_6$ for which the given slice is the fiber of answer `1` ($X_1 \leftrightarrow q_x$, $X_0 \leftrightarrow q_x \oplus 1$, $C_1 \leftrightarrow q_c$, $C_0 \leftrightarrow q_c \oplus 1$, $B_1 \leftrightarrow q_\beta$, $B_0 \leftrightarrow q_\beta \oplus 1$) defines an isomorphism of the 1-skeleton of the nerve $\mathcal{N}$ with the octahedron graph $O_6 \cong K_{2,2,2}$ from `Theorem I.6.1`, sending antipodal pairs of fibers of a single question into the $3$ diagonals of the complement $3K_2$.
> 2. **Threefold equivalence on each of the $8$ triangles $(C_{c_0}, X_{x_0}, B_{b_0})$:** for any triple of indices $(c_0, x_0, b_0) \in \mathbb{F}_2^3$, the following three conditions are equivalent:
>    - **(a) Dynamic holonomy defect (`Chapter I.2`, `Theorem I.2.4`):** traversing the triple of slices $C_{c_0} \xrightarrow{\varphi_{12}} X_{x_0} \xrightarrow{\varphi_{23}} B_{b_0} \xrightarrow{\varphi_{13}^{-1}} C_{c_0}$ along the unique local transfer bijections $\varphi_{ij}$ that leave fixed the single-point pairwise intersections $p_{12} \in C_{c_0} \cap X_{x_0}$, $p_{23} \in X_{x_0} \cap B_{b_0}$, and $p_{13} \in C_{c_0} \cap B_{b_0}$ yields inversion of the second bit $H_3 = \mathrm{swap}_{C_{c_0}}$ (defect index $\kappa(c_0, x_0, b_0) = c_0 \oplus x_0 \oplus b_0 = 1$);
>    - **(b) Geometric cavity in the octahedron (`Chapter I.6`, `Theorem I.6.1`):** the triple intersection of the slices is empty ($C_{c_0} \cap X_{x_0} \cap B_{b_0} = \varnothing$), i.e., the triangle belongs to the quadruple of hollow faces $H_F$ of the nerve $\mathcal{N}$ (whereas at $\kappa = 0$ the intersection $C_{c_0} \cap X_{x_0} \cap B_{b_0} = \{(x_0, c_0)\}$ is a singleton, $H_3 = \mathrm{id}$, and the triangle belongs to the quadruple of filled faces $H_R$);
>    - **(c) Cohomological twist of the cocycle $w \in Z^1(\mathcal{N}; \mathbb{F}_2)$:** the sum of flips of the 1-cocycle $w$ along the boundary of the triangle equals $w(X_{x_0}, C_{c_0}) \oplus w(X_{x_0}, B_{b_0}) \oplus w(C_{c_0}, B_{b_0}) = (x_0 \oplus c_0) \oplus b_0 \oplus 0 = \kappa(c_0, x_0, b_0) = 1$.
> 3. **Presheaf realization ($\mathbb{F}_2$-torsor of local slice orientations $\mathcal{S}_w$):** define on the simplicial complex $\mathcal{N}$ a presheaf of sets $\mathcal{S}_w$ assigning to each vertex $U \in V(\mathcal{N})$ the two-element set of local bit labels $\mathcal{S}_w(U) = \mathbb{F}_2$, to each edge $e = UV \in E(\mathcal{N})$ the two-element set of compatible pairs $\mathcal{S}_w(UV) = \{(s_U, s_V) \in \mathbb{F}_2^2 \mid s_U \oplus s_V = w(UV)\}$ with restriction projections onto $U$ and $V$, and to each filled 2-face $\sigma = X_i C_j B_k \in F(\mathcal{N})$ ($i \oplus j \oplus k = 0$) the set of compatible triples $\mathcal{S}_w(\sigma) = \{(s_X, s_C, s_B) \in \mathbb{F}_2^3 \mid s_X \oplus s_C = i \oplus j,\; s_X \oplus s_B = k,\; s_C \oplus s_B = 0\}$. Then:
>    - over every window $U$, every double seam $UV$, and every one of the $4$ filled triple faces $\sigma \in F(\mathcal{N})$, the set of local sections is non-empty and contains exactly `2` elements ($|\mathcal{S}_w(U)| = |\mathcal{S}_w(UV)| = |\mathcal{S}_w(\sigma)| = 2$), and all restriction maps are surjective;
>    - the set of global sections of the presheaf is empty: $\Gamma(\mathcal{N}, \mathcal{S}_w) = \{g \in C^0(\mathcal{N}; \mathbb{F}_2) \mid \delta_0 g = w\} = \varnothing$, since $[w] \neq 0 \in H^1(\mathcal{N}; \mathbb{F}_2)$.

*Proof.*  
1. Every non-constant affine question on $S_4$ divides $S_4$ into two complementary two-point fibers coinciding with one of the pairs $\{X_0, X_1\}$, $\{C_0, C_1\}$, or $\{B_0, B_1\}$. Two fibers intersect in one point in $S_4$ if and only if the questions corresponding to them are non-collinear (i.e., their sum in $A_6 \cup \{0, 1\}$ is non-constant), which coincides with the definition of an edge in $O_6$ (`Theorem I.6.1`).  
2. The pairwise intersections of the slices equal $p_{12} = (x_0, c_0) \in C_{c_0} \cap X_{x_0}$, $p_{23} = (x_0, x_0 \oplus b_0) \in X_{x_0} \cap B_{b_0}$, and $p_{13} = (c_0 \oplus b_0, c_0) \in C_{c_0} \cap B_{b_0}$. All three points coincide ($p_{12} = p_{23} = p_{13}$) if and only if $c_0 = x_0 \oplus b_0$, i.e., $\kappa = c_0 \oplus x_0 \oplus b_0 = 0$; in this case the common point $(x_0, c_0)$ lies in $C_{c_0} \cap X_{x_0} \cap B_{b_0}$, all three bijections $\varphi_{ij}$ leave it in place, and $H_3 = \mathrm{id}_{C_{c_0}}$. If instead $\kappa = 1$, then $C_{c_0} \cap X_{x_0} \cap B_{b_0} = \varnothing$, the points $p_{12} \neq p_{13}$ form the two distinct elements of the two-point slice $C_{c_0}$, $\varphi_{12}(p_{12}) = p_{12} \neq p_{23}$ in $X_{x_0}$, whence $\varphi_{23}(\varphi_{12}(p_{12})) \neq p_{23}$ in $B_{b_0}$, i.e., it coincides with the second point $p_{13} \in B_{b_0}$, and $\varphi_{13}^{-1}(p_{13}) = p_{13} \neq p_{12}$, which yields the transposition $H_3 = \mathrm{swap}_{C_{c_0}}$. The equality of the circulation of $w$ to $(x_0 \oplus c_0) \oplus b_0 \oplus 0 = \kappa$ is verified by direct substitution of the definition of $w$.  
3. On every filled face $\sigma = X_i C_j B_k$ one has $i \oplus j = k$, so the third equation $s_C \oplus s_B = 0$ is the sum of the first two $(s_X \oplus s_C) \oplus (s_X \oplus s_B) = (i \oplus j) \oplus k = 0$, and to each choice of $s_X \in \{0, 1\}$ corresponds a unique compatible triple $(s_X,\, s_X \oplus i \oplus j,\, s_X \oplus k) \in \mathcal{S}_w(\sigma)$, whence $|\mathcal{S}_w(\sigma)| = 2$. A global section $g \in \Gamma(\mathcal{N}, \mathcal{S}_w)$, on the other hand, is by definition a solution of $\delta_0 g = w$, which does not exist by `Theorem I.9.3`. $\square$

Let us retain here the exact distinction of carriers: the equality $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$ refers **to the two-dimensional complex of the nerve $\mathcal{N}$ of the six slices** (describing the space of twisted transition laws between slices around the four empty triples), and **not** to the discrete four-point set $S_4$ itself (for which $H^1(S_4; \mathbb{F}_2) = 0$ and all four global states $00, 01, 10, 11$ exist; they fill the four faces of the nerve).

---

## §I.9.5. Higher Obstruction $H^2$ on the Hollow Tetrahedron $\partial\Delta_4$ and Bridge to Oriented Complexes of Book II

Can it happen that **all** one-dimensional cycles are already sealed ($H^1 = 0$), there are no hidden twists on the edges at all, and an unsolvable obstruction hides on the next floor—between two-dimensional faces around a three-dimensional cavity?

Take the simplest closed two-dimensional shell—**the boundary of the tetrahedron** $\partial\Delta_4$ (the subscript $4$ here indicates the number of vertices $|V| = 4$ of the three-dimensional simplex, which under dimensional indexing is written as $\partial\Delta^3$): it has $4$ vertices $V = \{1, 2, 3, 4\}$, all $6$ edges of the complete graph $K_4$, and all $4$ triangular faces $F = \{123,\, 124,\, 134,\, 234\}$, but **an empty interior** (the 3-simplex $1234$ is absent).

```text
  HOLLOW TETRAHEDRON ∂Δ_4: ALL EDGE CYCLES SEALED (H^1 = 0), YET AN EMPTY CAVITY INSIDE (H^2 ≅ F_2)

                 (1)                 • Vertices: 4, edges: 6, triangular faces: 4 (hollow sphere)
                / | \                • Each of the 6 edges enters EXACTLY 2 triangular faces!
               /  |  \               • Therefore the sum of boundaries (δ_1 b) over all 4 faces is ALWAYS 0 mod 2:
              /  (4)  \                  - face vector f_odd  = (1,0,0,0) has 0 solutions out of 64;
             /  /   \  \                 - face vector f_even = (1,1,0,0) has 8 solutions out of 64!
           (2)---------(3)           • Result: H^1(∂Δ_4; F_2) = 0, but H^2(∂Δ_4; F_2) ≅ F_2!
```
**Fig. I.9.3.** The hollow tetrahedron $\partial\Delta_4$ as the minimal carrier of the two-dimensional gluing obstruction $H^2(\partial\Delta_4; \mathbb{F}_2) \cong \mathbb{F}_2$.  
Since any three vertices are joined by a filled triangular face, no one-dimensional Möbius strip can persist on the edges ($H^1 = 0$). However, every edge belongs to exactly two faces of the shell, and therefore the sum of the values of any coboundary $\delta_1 b$ over all four faces must be even: an odd charge on the faces cannot be generated by any assignment of bits on the edges.

> **Proposition I.9.2 (Two-dimensional obstruction on the hollow tetrahedron $\partial\Delta_4$).**  
> *Classical foundation.* Simplicial cohomology of the two-dimensional sphere $S^2 \cong \partial\Delta_4$: $H^1(\partial\Delta_4; \mathbb{F}_2) = 0$ and $H^2(\partial\Delta_4; \mathbb{F}_2) \cong \mathbb{F}_2$. *Contribution of this book:* Minimal finite model of a second-order obstruction: sealing all one-dimensional loops by four triangular faces kills $H^1$, yet an odd 2-cocycle $w = (0,0,0,1)$ yields `0` out of `64` solutions of $\delta_1 \eta = w$ vs. `8` solutions for an even face sum.
> On the boundary of the tetrahedron $\partial\Delta_4$ ($|V|=4$, $|E|=6$, $|F|=4$) over the field $\mathbb{F}_2$, the equalities $\operatorname{rank}_{\mathbb{F}_2} \delta_0 = 3$ and $\operatorname{rank}_{\mathbb{F}_2} \delta_1 = 3$ hold, as a consequence of which
> $$H^1(\partial\Delta_4; \mathbb{F}_2) \;=\; 0, \qquad H^2(\partial\Delta_4; \mathbb{F}_2) \;=\; C^2(\partial\Delta_4; \mathbb{F}_2) \,\big/\, \operatorname{im}\delta_1 \;\cong\; \mathbb{F}_2.$$
> The equation $\delta_1 b = f$ with respect to an edge 1-cochain $b \in C^1(\partial\Delta_4; \mathbb{F}_2)$ is solvable if and only if the sum of the values of the 2-cochain $f$ over all four faces equals zero in $\mathbb{F}_2$: in particular, for $f_{\mathrm{odd}} = (1, 0, 0, 0)$ among all $2^6 = 64$ cochains $b$ there are **`0` solutions**, while for $f_{\mathrm{even}} = (1, 1, 0, 0)$ there are exactly **`8` solutions** ($|\ker \delta_1| = |Z^1| = 2^3 = 8$).

*Proof.* Connectedness of $K_4$ gives $\operatorname{rank}\delta_0 = 4 - 1 = 3$ and $\dim B^1 = 3$. Each of the $6$ edges enters exactly $2$ of the $4$ faces, so the sum of all four rows of the $4 \times 6$ matrix $\delta_1$ equals the zero row modulo $2$, i.e., $\operatorname{rank}\delta_1 \le 3$. On the other hand, the three faces $123, 124, 134$ meeting at vertex $1$ contain respectively the edges $23, 24, 34$ of the opposite base, each of which does not enter the other two of these three faces. Thus the first three rows form the $3 \times 3$ identity submatrix $I_3$ over the columns $(23, 24, 34)$, whence $\operatorname{rank}\delta_1 = 3$. We obtain $\dim H^1 = 6 - 3 - 3 = 0$, $\dim \ker \delta_1 = 6 - 3 = 3$ ($2^3 = 8$ solutions for every solvable equation), and $\dim H^2 = 4 - 3 = 1$ with the unique linear compatibility condition $f(123) \oplus f(124) \oplus f(134) \oplus f(234) = 0$. $\square$

Here it is fitting to make an important remark on the threshold of Book II. Why in `§§I.9.4–I.9.5` did we not need orientation arrows on edges and traversal directions on faces? Only because we worked over the field $\mathbb{F}_2$, where $+1 = -1$ and a twofold occurrence of a vertex or edge cancels by itself ($1 \oplus 1 = 0$). As soon as in **Chapter `II.3`** we wish to count flows, circulations, and conservation laws with **integer, rational, or real charges** (in a coefficient ring $R$ where $1 + 1 = 2 \neq 0$), we will need to combine the simplicial geometry of the present chapter with **the sign involution of Chapter `I.5`**, introducing the alternating boundary operator $\partial_n[v_0, \dots, v_n] = \sum_{k=0}^n (-1)^k [v_0, \dots, \widehat{v}_k, \dots, v_n]$. Thus two independent lines of Book I—the doctrine of sign (`I.5`) and the doctrine of gluing (`I.9`)—will merge into the chain and cochain complexes of Book II.

---

## §I.9.6. Exact Code Foldability ($U \circ F = \mathrm{id}_E$) vs. Behavioral Compression

Before summing up the overall result of Book I, let us close the question from `Trap 3` (`§I.9.2`), which links expression trees from `Chapter I.7` with Nerode memory from `Chapter I.3`.

In `Chapter I.7` (`§I.7.1`) we distinguished the syntactic tree of an expression $e \in E$ (for example, `2 + 2`, `2 · 2`, and `2^2`) and its static numerical value $\mathrm{val}(e) = 4$ (where gluing by $\mathrm{val}$ alone corresponds to a zero reading horizon without contextual continuations, whereas in a general contract $\Gamma$ with further operations and steps, behavioral equivalence $e_1 \sim_\Gamma e_2$ requires coincidence of **all future protocol responses** $\mathrm{beh}_\Gamma(e_1) = \mathrm{beh}_\Gamma(e_2)$). In computer science, logic, and DOT itself, one often needs to **pack** a complex composite description or experimental protocol $e \in E$ into a compact internal code $i_{\mathrm{str}}[e] = F(e) \in S$ inside some code carrier $S$ so that at any moment one can unfold this description back and perform any syntactic operation on it. When is such a two-way "fold–unfold" discipline possible without a single ambiguity?

> **Theorem I.9.4 (Criterion of exact foldability and its incompatibility with non-trivial quotient compression).**  
> *Classical foundation.* Criterion for existence of a left inverse map (retraction $U \circ F = \mathrm{id}_E$) on a non-empty set $E \ne \varnothing$ via injectivity of $F$—basic set and category theory. *Contribution of this book:* Concluding architectural dichotomy of Volume I between non-injective Nerode future-memory compression ($X \twoheadrightarrow X/{\sim_\Gamma}$, irreversible without a trace) and the reversible `Fold / Unfold` pair $F : E \hookrightarrow B \times H$ retaining an auxiliary history register $H$.
> Let $E$ be a non-empty set of structural descriptions (expressions or histories), and let $S$ be a set of codes.
> 1. **Exact structural encoding:** a packing map $F : E \to S$ ($e \mapsto i_{\mathrm{str}}[e]$) possesses a left inverse decoder $U : S \to E$ with the property $U(F(e)) = e$ for all $e \in E$ if and only if $F$ is **injective** (in which case the restriction of the decoder $U|_{F(E)} : F(E) \xrightarrow{\sim} E$ onto the image $S_0 = F(E) \subseteq S$ is **uniquely** determined, whereas outside the image on $S \setminus F(E)$ the values of $U$ may be extended by an arbitrary default element $e_* \in E$). On the image $S_0 = F(E)$, every $m$-ary operation $\omega : E^m \to E$ is uniquely transferred to codes by the formula $\widetilde{\omega}(s_1, \dots, s_m) = F\bigl(\omega(U(s_1), \dots, U(s_m))\bigr)$, satisfying the identity $U\bigl(\widetilde{\omega}(F(e_1), \dots, F(e_m))\bigr) = \omega(e_1, \dots, e_m)$.
> 2. **Irreversibility of behavioral compression:** let $\sim_\Gamma$ be a non-trivial equivalence of observable behavior on $E$ (so that there exist $e_1 \neq e_2$ in $E$ with $e_1 \sim_\Gamma e_2$), and let $F_{\mathrm{beh}} : E \twoheadrightarrow E / {\sim_\Gamma}$ be the canonical quotient projection (`Ch. I.3`). Then **there exists no** map $U : E / {\sim_\Gamma} \to E$ for which $U(F_{\mathrm{beh}}(e)) = e$ for all $e \in E$; not all syntactic operations on $E$ descend to the quotient $E / {\sim_\Gamma}$, but precisely those for which $\sim_\Gamma$ is a congruence.

*Proof.*  
1. If $U \circ F = \mathrm{id}_E$, then $F(e_1) = F(e_2)$ implies $e_1 = U(F(e_1)) = U(F(e_2)) = e_2$, i.e., $F$ is injective, and on every element of the image $s = F(e) \in F(E)$ the value $U(s) = e$ is uniquely forced by the equality $U(F(e)) = e$. Conversely, let $F$ be injective and choose a fixed default element $e_* \in E$ (existing since $E \neq \varnothing$). Set $U(s) = e$ for $s = F(e) \in F(E)$ (unambiguously by injectivity of $F$) and $U(s) = e_*$ for $s \in S \setminus F(E)$; then $U(F(e)) = e$ for all $e \in E$, and the formula for $\widetilde{\omega}$ is verified by direct substitution $U(F(\omega(\dots))) = \omega(\dots)$.  
2. If $e_1 \neq e_2$ yet $F_{\mathrm{beh}}(e_1) = F_{\mathrm{beh}}(e_2) = c$, then for any map $U$ the element $U(c)$ cannot simultaneously equal the two distinct elements $e_1$ and $e_2$. Transfer of an operation $\omega$ across the quotient projection by the universal property of a quotient (`Theorem I.2.1`) exists and is unique if and only if $e_r \sim_\Gamma e'_r$ ($r = 1,\dots,m$) implies $\omega(e_1,\dots,e_m) \sim_\Gamma \omega(e'_1,\dots,e'_m)$. $\square$

This theorem puts the final period on distinguishing two types of arrows in DOT (already preserved in the notation of the book: $i_{\mathrm{str}}[e] = F(e)$ for the injective structural code of an expression vs. the integer quarter-turn $J_{\mathbb{Z}}(a,b) = (-b, a)$ in `Ch. I.5`, and vs. $\pi_\Gamma : X \twoheadrightarrow X/{\sim_\Gamma}$ for erasing memory compression). **Reducing the cardinality of the set of codes $|S| < |E|$ without gluing together at least two distinct descriptions $e_1 \neq e_2 \in E$ is impossible on finite sets by the pigeonhole principle** (at a fixed binary word length this requires $b \ge \lceil \log_2 |E| \rceil$ bits for $|E|$ distinct objects; of course, if the very same $|E|$ objects were previously written as redundant strings of greater length $L > \lceil \log_2 |E| \rceil$, reversible compression of word length down to $\lceil \log_2 |E| \rceil$ bits is completely legitimate and preserves the bijection $F(E) \cong E$, while the cost of the dictionary and decoder is accounted for separately by the five-dimensional passport of `Chapter I.4`): the observer always consciously chooses whether to store the full syntactic passport $F(e)$ (retaining at least $|E|$ distinguishable codes) or to compress the carrier to the minimal Nerode automaton $E/{\sim_\Gamma}$ (preserving 100% predictability of future answers of the contract $\Gamma$, while forever letting go of the erased distinctions of the past).

---

## §I.9.7. Architectural Synthesis of Book I: One Scene $S_4$ Through Nine Chapters, Passport of Finite Cardinalities, and Boundary of Book II

We have reached the summit of Book I. Let us look back over the entire route traversed—from the `Introduction` and `Chapter I.1` to `Chapter I.9`—and verify that before us is not a scattering of separate mathematical topics, but **a unified edifice**, built upon one and the same primary foundation without a single hidden leap.

### 1. Nine Steps of One and the Same Four-State Scene $S_4 = \{(x, c) \in \{0, 1\}^2\}$
To see this unity before our eyes, let us trace how **one and the same tiny four-element carrier** $S_4 = \{00, 01, 10, 11\}$ passed through all nine chapters of Book I, acquiring at each step precisely that new structure which the observer's next question demanded:

| Chapter | What question is posed to the scene $S_4$ | What exactly is revealed on $S_4$ (or its minimal endowment) |
| :---: | :--- | :--- |
| **`I.1`** | How to distinguish all $4$ states by binary sensors? | A single question $q_x(x,c)=x$ cuts $S_4$ only in half (`2` classes); a pair of independent questions $(q_x, q_c)$ yields the Cartesian grid $2 \times 2 = 4$ without collisions. |
| **`I.2`** | When does the coarse reading $\beta(x,c) = x \oplus c$ withstand a step $T$ and where is partial admissibility $\bot$ needed? | For $T_{\mathrm{or}}(x,c) = (x, x \lor c)$, the pair of witnesses `01` and `10` lies in the same fiber $\beta = 1$, yet diverges after the step (`01 \mapsto 01`, `10 \mapsto 11`), generating a non-empty shadow $\partial_\beta(T_{\mathrm{or}}^*\beta) \neq \varnothing$ and a partial vestibule. |
| **`I.3`** | How to uncover the invisible bit $c$ while looking only through the window $q_x$ along time? | Under the swap action $T_{\mathrm{swap}}(x,c) = (c, x)$, the two-step window $\bigl(q_x(s),\, q_x(T_{\mathrm{swap}} s)\bigr) = (x, c)$ stabilizes the Nerode partition `2 → 4 → 4` and builds the minimal Moore automaton. |
| **`I.4`** | What does it cost to make an irreversible step on $S_4$ reversible without loss? | Erasing a bit requires an external trace log: extending $S_4 \hookrightarrow S_8 = \{0,1\}^3$ by the reversible step $R(x,c,z) = (x\oplus c,\, c,\, z\oplus x\oplus c)$ yields a bijection of order $4$ ($R^2 \neq \mathrm{id}$, $R^4 = \mathrm{id}$). |
| **`I.5`** | How to cancel alternative paths between states of a single slice of $S_4$? | On the module of contributions $\mathbb{Z}[S_4] \cong \mathbb{Z}^4$ with the sign involution of pole exchange (`Boundary B1`), the two-dimensional Hadamard block $H_{\mathrm{go}} = \begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}$ on a fiber of $S_4$ annihilates the off-diagonal transition $(H_{\mathrm{go}}^2)_{12} = 1 - 1 = 0$. |
| **`I.6`** | What geometry do the non-constant questions on $S_4$ themselves form? | Out of the $2^4 = 16$ Boolean functions on $S_4$, single out the $8$ affine ones ($\mathbb{F}_2^3$) and the $6$ non-constant affine questions $A_6$: three adjacency contracts turn $A_6$ into $3K_2$ (`3` edges), the octahedron $O_6$ (`12` edges), and the cycle $C_6$ (`6` edges). |
| **`I.7`** | Can $S_4$ be identified with the addition scale and the divisibility lattice? | The four-element divisor lattice $D(6) = \{1, 2, 3, 6\} \cong \{0, 1\}^2 = S_4$ by two coprime features ($2 \mid d$, $3 \mid d$) forms the Boolean diamond $S_4$, whereas on $D(4) = \{1, 2, 4\}$ the square $2^2$ breaks the Cartesian grid $S_4$ into a chain. |
| **`I.8`** | How do modular windows and Hankel rank behave on four-element carriers? | The coprime window $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{F}_2 \times \mathbb{F}_3$ splits by the CRT, whereas the ring $\mathbb{Z}/4\mathbb{Z}$ of cardinality $|S_4| = 4$ (unlike $\mathbb{F}_2 \times \mathbb{F}_2$) contains the nilpotent $2^2 \equiv 0$; the shift trace of $T_{\mathrm{swap}}$ on $S_4$ has Hankel rank `2`. |
| **`I.9`** | Do local data on the six two-point slices of $S_4$ always glue together? | The nerve of the six slices $X_0, X_1, C_0, C_1, B_0, B_1$ of the scene $S_4$ forms a checkerboard octahedron with $4$ films and $4$ holes, carrying a three-dimensional gluing obstruction $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$. |

### 2. Anti-Numerological Passport of the Finite Carriers of Book I
Throughout Book I, a whole series of memorable finite cardinalities has arisen before the reader: `4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 19, 27, 35, 48`. In popular literature, such coincidences of numbers are often turned into vague symbolism. The discipline of DOT is diametrically opposite: **every number in the book is the exact value of an explicit combinatorial formula on a strictly exhibited carrier**, and coincidence of the cardinalities of two sets by itself never implies isomorphism of their structures. Let us bring all `14` reference finite cardinalities of Book I together into a single reference schedule.

#### Table I.9.2. Summary Passport of the 14 Reference Finite Cardinalities of Book I

| Cardinality | Exact formula of origin | Canonical carrier and its chapter in Book I | Caution against false identification |
| :---: | :--- | :--- | :--- |
| **`4`** | $2^2$ | Minimal two-bit scene $S_4 = \mathbb{F}_2^2$ (`I.1–I.9`); Boolean divisor diamond $D(6)$ (`I.7`); even tetrahedron $E_{\mathrm{even}} \subset \mathbb{F}_2^3$ (`I.9`) | `4` elements in $\mathbb{Z}/4\mathbb{Z}$ and in $\mathbb{F}_2^2$ are non-isomorphic as groups and rings |
| **`6`** | $2^3 - 2 = \binom{4}{2}$ | $6$ non-constant affine questions $A_6$ on $S_4$ (`I.6`); $6$ slices of the nerve $\mathcal{N}$ and $6$ edges of the tetrahedron $\partial\Delta_4$ (`I.9`); $|D(12)| = 3 \cdot 2 = 6$ (`I.7`) | On the very same $6$ points $A_6$ live three non-isomorphic graphs $3K_2, O_6, C_6$; $D(12)$ is non-Boolean |
| **`7`** | $2^3 - 1$ | $7$ points and $7$ lines of the Fano projective plane $\mathrm{PG}(2, 2)$ (`I.6`) | The pairwise 2-section of Fano equals the featureless $K_7$ and loses the structure of 3-lines |
| **`8`** | $2^3$ | Three-bit cube $Q_3 = \mathbb{F}_2^3$ (`I.4, I.6`); Boolean divisor cube $D(30)$ (`I.7`); $8$ faces of the octahedron (`I.9`) | In the nerve $\mathcal{N}$ (`I.9`), the $8$ triangles split into $4$ filled and $4$ hollow ones |
| **`9`** | $3^2$ | Affine plane $\mathrm{AG}(2, 3) = \mathbb{F}_3^2$ (`I.6`); divisor lattice $D(36)$ (`I.8`) | $\mathrm{AG}(2,3) = \mathbb{F}_3^2$ is an affine plane of $9$ points with $12$ lines in $4$ parallel pencils (for the field $\mathbb{F}_9$ an irreducible quadratic polynomial is needed), while $D(36)$ is the square of chains $\{0,1,2\}^2$ |
| **`10`** | $\binom{5}{2}$ | Petersen graph (pairs of $5$ elements with disjointness edges, `I.6`); window $N=10$ in $1+\pi(N)=N/2$ (`I.7`) | The Petersen graph is non-planar and has no Hamiltonian cycle |
| **`12`** | $6 \cdot 4 / 2$ | $12$ edges of the octahedron $O_6$ (`I.6`) and of the nerve $\mathcal{N}$ (`I.9`); $12$ edge midpoints of the cube (shell $\|x\|_1 = 2$ of the ternary cube $T_3$, `I.5`); window $N=12$ (`I.7`) | Coincidence of the number $12$ does not relate the edges of the octahedron to the even window of primes |
| **`13`** | $(3^3 - 1)/2$ | $13$ projective sign axes of the cube $T_3$ (`I.5, I.7`) and $13$ points of the plane $\mathrm{PG}(2, 3)$ (`I.6`) | Here the coincidence is **legitimate**: the rays $\mathbb{F}_3^3\setminus\{0\}/\{\pm 1\}$ are indeed the points of $\mathrm{PG}(2,3)$, but not Sāṃkhya's list of `13` *karaṇas*. |
| **`14`** | $7 + 7$ | Bipartite Levi–Heawood incidence graph of the Fano plane (`I.6`); extreme window $N=14$ in $1+\pi(N)=N/2$ (`I.7`) | The Heawood graph reconstructs $\mathrm{PG}(2,2)$ only together with the labeling of the two parts (points vs. lines) |
| **`15`** | $2^4 - 1$ | Three-dimensional projective space $\mathrm{PG}(3, 2)$ over $\mathbb{F}_2$ (`I.6`) | Contains $35$ lines and $15$ Fano planes |
| **`19`** | $1 + 6 + 12$ | Saturated ball of Manhattan radius $\le 2$ in the ternary cube $T_3 = \{-1, 0, +1\}^3$ (`I.5`) | Obtained by discarding the $8$ corner vertices $\{\pm 1\}^3$ from $27$, not as the prime field $\mathbb{F}_{19}$ |
| **`27`** | $3^3$ | Full ternary sign cube $T_3 = \{-1, 0, +1\}^3 = 1 + 6 + 12 + 8$ (`I.5`) | In `I.5` this is a cube in $\mathbb{Z}^3$ with truncation, not the affine space $\mathbb{F}_3^3$ modulo $3$ |
| **`35`** | $\frac{(2^4-1)(2^3-1)}{2^2-1}$ | Set of all $35$ lines of the projective space $\mathrm{PG}(3, 2)$ (Klein quadric over $\mathbb{F}_2$, `I.6`) | Equals $\binom{7}{3} = 35$ in count, but carries the non-trivial geometry of line intersection |
| **`48`** | $2^3 \cdot 3!$ | Group of signed permutations (hyperoctahedral group $W(B_3)$) of the ternary cube $T_3$ and octahedron $O_6$ (`I.5, I.6`) | Contains the proper subgroup of cube rotations of order $24 \cong \mathfrak{S}_4$ (not to be confused with the $4$-point scene $S_4 = \mathbb{F}_2^2$) |

### 3. Boundary of the Finite Core of Book I, Four "Quarter-Turn / Code" Objects, and Map of Enrichments of Book II
All of Book I observed a strict ascetic vow: **not once in our proofs did we rely on limiting passages, continuity, real or complex numbers, metric completeness, analytic convergence of series, or smooth derivatives**. The entire edifice of chapters `I.1–I.9` is built exclusively by means of finite sets and partial maps, countable algebraic and syntactic carriers ($\mathbb{N}$, $\mathbb{Z}[X]$, $K[t]$, formal series $K[[t]]$ without limit topology), exact rational weights, and finite-dimensional linear algebra over $\mathbb{Q}$ and $\mathbb{F}_p$. Let us record the exact internal boundary of this finite core as a verifiable corollary.

> **Corollary I.9.2 (Completeness of the finite core on protocols of arbitrary length and refinement of memory upon expanding a contract).**  
> 1. **Finiteness of the action semigroup and unbounded horizon:** on any finite carrier $|X| = n$, the monoid of all partial transformations $\mathrm{Par}(X, X)$ is finite and has cardinality $(n + 1)^n$ (for instance, $3^2 = 9$ at $n = 2$ and $5^4 = 625$ at $n = 4$). Therefore, under any fixed contract $\Gamma = (X, \mathcal{Q}, \Omega)$, the action-generated semigroup image $\langle \Omega \rangle \subseteq \mathrm{Par}(X, X)$ is finite, and the quotient $X / {\sim_\Gamma}$ stabilized in at most $\max(n - 1, 0)$ steps (`Theorem I.3.1`) unerringly predicts the answers to **all finite protocols $w \in \Omega^*$ of arbitrarily large length**.  
> 2. **Monotonic refinement of memory upon expanding the action library:** if new admissible actions are adjoined to the contract $\Gamma = (X, \mathcal{Q}, \Omega)$ ($\Omega \subseteq \Omega'$, contract $\Gamma'$), then future indistinguishability can only refine (${\sim_{\Gamma'}} \subseteq {\sim_\Gamma}$, whence $|X / {\sim_\Gamma}| \le |X / {\sim_{\Gamma'}}|$): already on the four-state cell $S_4 = \{0, 1\}^2$ with window $q_x(x, c) = x$, at $\Omega = \{\mathrm{id}\}$ the minimal memory has `2` classes, whereas adding the swap $T_{\mathrm{swap}}(x, c) = (c, x)$ splits the hidden fiber and increases the minimal memory to `4` classes (`2 < 4`).

Before crossing the threshold of the second volume, let us reproduce from `Chapter I.5` (`§I.5.6`) the exact demarcation table of four mathematically distinct objects that in careless conversation are easily confused under the shared name of "structural or imaginary unit" (throughout the entire book, the notation $i_{\mathrm{str}}[e] = F(e)$ is reserved **exclusively** for the first of them—the injective structural code with a left inverse decoder $U(F(e)) = e$):

| Notation | Where it lives and in which chapter introduced | Exact definition and main property | What this object does NOT do |
| :--- | :--- | :--- | :--- |
| **`i_str[e] = F(e)`** (or $i_{\mathrm{str},\Pi}[E]$) | Finite core (`Ch. I.1, I.5, I.7, I.9`) | Injective structural packing of an ensemble or expression tree $e \in E$ into a code $F(e) \in S$ with a left inverse decoder $U(F(e)) = e$ (`Theorem I.9.4`) | It is **neither a number nor a linear operator**; squaring $i_{\mathrm{str}}[e]$ or writing $(i_{\mathrm{str}}[e])^2 = -\mathrm{id}$ is meaningless |
| **`J_Z`** | Signed module $\mathbb{Z}^2$ (`Ch. I.5`, `Proposition I.5.1`) | Integer quarter-turn operator $J_{\mathbb{Z}}(a,b) = (-b, a) = \begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ with the property $J_{\mathbb{Z}}^2 = -I_2$ and $J_{\mathbb{Z}}^4 = I_2$ | Is not a scalar (requires a pair of channels $\mathbb{Z}^2$) and gives neither division by $2$ nor a continuous angle |
| **`J_R`** | Real planes $\mathbb{R}^{2n}$ (`Ch. II.2, II.5`) | Real skew-symmetric operator of complex structure $J_{\mathbb{R}}^2 = -I_{2n}$, embedding $\mathbb{C}$ into $M_2(\mathbb{R})$ | Does not turn the scalar field $\mathbb{R}$ itself into an algebraically closed field without passing to pairs |
| **`i in C`** | Field of complex numbers $\mathbb{C} = \mathbb{R}[i]/(i^2+1)$ (`Ch. II.2, II.5–II.7`) | Scalar imaginary unit $i^2 = -1$, multiplying each individual complex channel by a scalar and defining the unitary phase $e^{i\varphi}$ | Is not derived from the finite core of Book I alone without adjoining the field $\mathbb{R}$ and the quotient $\mathbb{R}[t]/(t^2+1)$ |

Now we can accurately match the completed core of Book I with the actual route of the nine chapters of Book II (`Ch. II.1–II.9`).

#### Table I.9.3. Boundary Between the Core of Book I and the Explicit Enrichments of the Nine Chapters of Book II

| What is fully constructed in the core of Book I (`Ch. I.1–I.9`) | What is in principle ABSENT in Book I without new axioms and endowments | Where and what explicit enrichment is introduced in Book II (`Ch. II.1–II.9`) |
| :--- | :--- | :--- |
| Partitions, quotients, Nerode memory $X/{\sim_\Gamma}$, Moore/Mealy automata, and scalar Hankel rank (`I.1–I.3, I.8`) | Multidimensional block linear systems with an eliminated hidden sector and an operator memory kernel under Schur reduction | **Enrichment 1 (`Ch. II.1`):** block linear dynamics over a field $K$, Schur complement, delayed memory kernel, and minimal realization |
| Finite differences, ternary lattices (`I.5`), exact identities on $D(N)$, and formal series without convergence (`I.7–I.8`) | Archimedean completeness of $\mathbb{R}$, topology of limits, continuous phase, and infinitesimal tangent shift | **Enrichment 2 (`Ch. II.2`):** field $\mathbb{R}$, limit and derivative, Cayley transform, and ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$ |
| Sign involution (`I.5`), seam gluing, and cohomologies $H^1, H^2$ only over $\mathbb{F}_2$ without orientations (`I.9`) | Oriented chains with torsion over $\mathbb{Z}$, parallel transport of frames along loops, and cohomological group extensions | **Enrichment 3 (`Ch. II.3–II.4`):** chain and cochain complexes over rings $R$ (`II.3`), connection on graphs, holonomy, and 2-cocycles of extensions (`II.4`) |
| Signed quarter-turn $J_{\mathbb{Z}}$ (`I.5`), finite projective geometries (`I.6`), rational couplings (`I.3–I.4`), and finite self-report (`Introduction`) | Division algebras and positive quantum states, qubit geometry and contextuality, SOS certificates, and the general theorem on the limit of self-description | **Enrichment 4 (`Ch. II.5–II.9`):** division algebras (`II.5`), states and effects (`II.6`), qubit, Hoggar, and contextuality (`II.7`), variational and SOS certificates (`II.8`), Lawvere's theorem and synthesis of Books I–II (`II.9`) |

---

## §I.9.8. Categorical Anchoring of the Chapter

Let us conclude the formal part of Book I with a categorical definition uniting all local-to-global gluing problems of the present chapter into a single scheme of presheaves and sheaves of sets:

- **Objects:** contravariant functors (**presheaves of sets**) $\mathcal{F} : \mathcal{U}^{\mathrm{op}} \to \mathbf{Set}$ on a thin category $\mathcal{U}$ of open cover windows and their intersections (where arrows $V \hookrightarrow U$ are inclusions of subwindows, to which correspond trace restriction maps $\mathrm{res}^U_V : \mathcal{F}(U) \to \mathcal{F}(V)$).
- **Morphisms:** natural transformations of presheaves $\eta : \mathcal{F} \Rightarrow \mathcal{G}$ (families of local recodings $\eta_U : \mathcal{F}(U) \to \mathcal{G}(U)$ commuting with all restrictions onto seams).
- **Identities and composition:** the pointwise identity transformation $\mathrm{id}_{\mathcal{F}}$ and pointwise composition of natural transformations.
- **Preserved structure:** compatible families of local data $\bigl(s_i \in \mathcal{F}(U_i)\bigr)_{i \in I}$ satisfying the condition of pairwise coincidence on all double seams $\mathrm{res}^{U_i}_{U_i \cap U_j}(s_i) = \mathrm{res}^{U_j}_{U_i \cap U_j}(s_j)$ are sent by any morphism $\eta$ again into compatible families.
- **Universal property (sheaf condition as an equalizer):** a presheaf $\mathcal{F}$ is a **sheaf** with respect to a cover $\{U_i\}_{i \in I}$ of an object $X$ if the canonical diagram
  $$\mathcal{F}(X) \;\longrightarrow\; \prod_{i} \mathcal{F}(U_i) \;\rightrightarrows\; \prod_{i, j} \mathcal{F}(U_i \cap U_j)$$
  is an **equalizer** in the category $\mathbf{Set}$—that is, every family of local states $(s_i)$ that is pairwise compatible on the seams glues uniquely into a global state $s \in \mathcal{F}(X)$ (this is precisely how gluing of divisors along an $\operatorname{lcm}$-cover in `Theorem I.8.2` is organized, whereas for two autonomous carriers $L, R$ over a seam $K$ in `Theorem I.9.1`, the fibered product $L \times_K R$ itself is by definition given as the equalizer of the pair of seam readings in $\mathbf{Set}$).
- **Detected trap and failure:** when for a presheaf $\mathcal{F}$ on a cover $\{U_i\}$ the sheaf condition fails or the system of local equations is twisted along cycles of the nerve of the cover, the equalizer of the two right-hand arrows can have non-empty pairwise compatible local pairs while the set of global solutions is empty (`Proposition I.9.1(1)`), and for the linear $\mathbb{F}_2$-torsor and parity systems constructed in the present chapter, the obstruction to solvability is measured by cohomology classes in $H^1(\mathcal{N}; \mathbb{F}_2)$ (`Theorem I.9.3`) and $H^2(\partial\Delta_4; \mathbb{F}_2)$ (`Proposition I.9.2`).

---

### Historical-Philosophical Note: Untying the Apparent Gluing (*saṃyoga*) and the Dancer's Exit from the Stage at the Finale of the *Sāṃkhya-kārikā*

1. **Motif of the classical source.** The concluding stanzas of Īśvarakṛṣṇa's *Sāṃkhya-kārikā* (`SK 59, 62–68`) sum up the entire path of discriminative knowledge (*viveka-khyāti*) with a vivid theatrical image: just as a dancer (*nartakī*), having shown a performance to the spectators in the hall, ceases her dance and withdraws from the stage (`SK 59`), Prakṛti ceases generating new engaging scenes before the witness-Puruṣa as soon as the boundary between them has been clearly seen (`SK 64`: *nāsmi na me nāham*—literally "I am not, not mine, not I"; in Gauḍapāda's classical commentary unfolded as "I am not action, nothing in the coupling belongs to me, I am not the bearer of ego"). Moreover, in `SK 62` and `SK 66` it is emphasized that the witness himself was never actually bound or remade by the mechanics of the stage, while in `SK 66` (*dṛṣṭā mayety upekṣaka eko dṛṣṭāham ity uparamaty anyā; saty api saṃyoge na prayojanam asti sargasya*) it is specifically stipulated that even while contact persists (*saty api saṃyoge*), the motive for new generation is exhausted.
2. **Strict realization in DOT.** This final image of classical Sāṃkhya closes the historical-philosophical arc of the entire Book I (begun in the `Introduction` and carried through `I.1`, `I.3`, `I.5`, and `I.7`): throughout nine chapters, the observer's position $\mathcal{O} \notin X$ held the changing reading contracts $\Gamma$, allowing partitions, hidden memory, reversible traces, signed cancellations, and simplicial twists to unfold within the finite scene, without itself turning into any element of the carrier $X$. And the separation drawn in the present chapter between **true reversible structure**, **erasing quotient compression** (`Theorem I.9.4`), and **the cohomological obstruction of false global gluing** (`Theorem I.9.3`) provides an exact mathematical instrument against mistaking locally smooth seams for a non-existent global identity.
3. **Boundary of comparison.** The soteriological goal of Sāṃkhya and Yoga—the final liberation of consciousness (*kaivalya*, `SK 68`, `YS 4.34`) through the cessation of identification—belongs to spiritual and philosophical practice; in the mathematical architecture of DOT, the completion of Book I signifies not the cessation of inquiry, but a strictly controlled transition from the fully verified finite core to the linear-operator, topological, and probabilistic contracts of Book II.

---

### Transition to Book II

Book I is complete. In our hands is the fully verified finite core of Distinction-Observation Theory: from the first binary cut and shadow detector to the minimal memory of automata, reversible extensions with a trace, signed cancellation, finite incidence geometries, oracle-free modular windows, scalar Hankel matrices, and simplicial gluing obstructions. In **Chapter `II.1`**, which opens the second volume, we will take the first step beyond the set-theoretic core of `Table I.9.3`—endowing the state space with a linear structure over a field $K$ and turning the hidden memory construction from `Chapters I.3` and `I.8` into the general operator theory of observability, reachability, and minimal realization of linear dynamical systems.

---

### Verifiability Passport of Chapter `I.9` (`Book I v3.3`)

- **Canonical node of the book:** `N09` (pairwise compatibility without a global section and invisibility of 3-parity in 2-windows, universal property of the fibered product $L \times_K R$ and associative composition of contracts along seams, cohomologies $H^1$ and $H^2$ over $\mathbb{F}_2$ on the hollow triangle, the checkerboard octahedron of the 6 slices of $S_4$, and the hollow tetrahedron $\partial\Delta_4$, criterion $U \circ F = \mathrm{id}_E$ vs. Nerode quotient compression, cross-chapter synthesis of $S_4$ across `I.1–I.9`, passport of 14 finite cardinalities, and boundary of Book II).
- **Exact `Julia 1.12.6` verifications (single-threaded mode, exact integer and $\mathbb{F}_2$ arithmetic, without `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gates `GATE-I09-A` (hollow triangle, 2-projection invisibility of $E_{\mathrm{even}} \subset \mathbb{F}_2^3$, associativity of contract gluing `64 -> 16 = 16` and path-multiplicity loss `2 -> 1`, witness of a non-surjective seam without a global $\tau : K \to K$, phantom pairs `2 -> 4` upon coarsening the seam prior to gluing, all $8$ triangles of the nerve of the 6 slices of $S_4$, $\dim H^1 = 3$ with exhaustive check of all $64$ gauges, and presheaf $\mathcal{S}_w$) and `GATE-I09-B` (hollow tetrahedron $\partial\Delta_4$ with $H^2 \cong \mathbb{F}_2$, criterion $U \circ F = \mathrm{id}_E$, finite bound $|\mathrm{Par}(X,X)| = (n+1)^n$, memory refinement `2 -> 4` upon expanding the action library, and formulas of all canonical finite cardinalities `4..48`).
- **Specification index `Lean 4` (`status: planned`, full cards in Appendix `VP`):** `TNR.BookI.I09.pairwise_not_global`, `TNR.BookI.I09.even_parity_two_projections`, `TNR.BookI.I09.seam_pullback`, `TNR.BookI.I09.contract_composition`, `TNR.BookI.I09.h1_obstruction_s4_nerve`, `TNR.BookI.I09.hollow_tetrahedron_h2`, `TNR.BookI.I09.fold_unfold_vs_quotient`, `TNR.BookI.I09.finite_library_boundary`, `TNR.BookI.I09.extension_refines_future_partition`.
- **Full 8-point passports of figures `Fig. I.9.1–Fig. I.9.3` and statement certification registry:** moved to [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
