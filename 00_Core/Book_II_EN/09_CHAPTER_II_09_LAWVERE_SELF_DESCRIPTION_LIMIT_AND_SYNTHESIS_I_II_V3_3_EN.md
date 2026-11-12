# Chapter II.9. The Limit of Self-Description (Lawvere's Theorem) and the Synthesis of What Is Proven, Modeled, and Open in Books I–II

In the concluding chapter of the Second Volume, we bring together and compare the results of Books I and II.

Let us recall how the `Introduction` to the First Volume began: we separated the observed state frame $X$ from the role-based position of the observer $\mathcal{O}$, fixing the typing condition $\mathcal{O} \notin X$ (a camera can photograph its own body in a mirror as part of the frame $X$, yet the act of framing itself and choosing the contract $\Gamma$ is not one of the points inside $X$). Throughout Book I, this condition remained an external rule for the careful typing of the contract $\Gamma$.

Now, equipped with the full apparatus of linear memory, topological gluing, group cohomology, and categorical morphisms, we can pose the internal mathematical question regarding the limit of self-description:

> **What happens if a system attempts to bypass the boundary $\mathcal{O} \notin X$ from within—that is, to single out inside its own state carrier $A$ a universal catalog of names capable of parametrizing all possible questions $A \to Y$ about the states of that very same carrier $A$?**

The concluding chapter of the Second Volume solves three problems:
1. we prove **Lawvere's diagonal fixed-point theorem** (F. W. Lawvere, 1969) in cartesian closed categories ($\mathbf{CCC}$), strictly separating the external typing rule $\mathcal{O} \notin X$, the internal impossibility of a point-surjective parametrization $A \to Y^A$ in the presence of an endomorphism $\alpha : Y \to Y$ without fixed points, and an explicit analysis of global points and the exponential $Y^A$ in the topos $\mathbf{Set}^{C_2}$;
2. we prove a cohomological theorem on phase lifting and the minimal number of memory classes for non-split group extensions (including the $64$-element non-abelian extension with the $2$-cocycle $\beta((g,u),(h,v)) = g_1 h_2 \in \mathbb{F}_2$, the stabilizer criterion via Shapiro's lemma, and the affine action of the group $\mathrm{AGL}_3(\mathbb{F}_2)$ on $64$ states with two orbits $8 + 56 = 64$ and a minimal quotient of index $8 = 168/21$);
3. finally, we compile into a single concluding panorama all **nine canonical regimes of minimal memory** of Books I–II, the map of the categories actually constructed, and the strict boundary obligations toward the domain-specific bridges of Book III.

---

## §II.9.1. A Universal Catalog of Questions Versus the Diagonal Argument: Lawvere's Theorem and the Exponential in $\mathbf{Set}^{C_2}$

Imagine a library of index cards $A$ stored inside the investigated world of states itself. Suppose the librarian claims that this catalog is universal: for **every** question $f : A \to Y$ with values in an answer alphabet $Y$ (for example, $Y = \{0, 1\}$ with the negation operation $\alpha(y) = 1 - y$, which has no fixed points: $\alpha(y) \ne y$), there exists in the set $A$ itself a code card $a_f \in A$, and a universal reading device $\varepsilon : A \times A \to Y$ takes the pair "(question card $a$, inspected card $b$)" and outputs the answer $\varepsilon(a, b) = f(b)$.

The very moment such a device $\varepsilon : A \times A \to Y$ is presented, the observer constructs a **diagonal counter-question**:
$$
g(b) = \alpha\bigl(\varepsilon(b, b)\bigr) \qquad (\forall b \in A),
$$
that is, asks every card $b$ about itself and inverts the resulting answer via the endomorphism $\alpha : Y \to Y$. If the catalog is truly complete, then the question $g : A \to Y$ must also have its own card $a_0 \in A$, for which $\varepsilon(a_0, b) = g(b)$ for all $b \in A$. Substituting the card $b = a_0$ itself into this equality, we obtain:
$$
\varepsilon(a_0, a_0) = g(a_0) = \alpha\bigl(\varepsilon(a_0, a_0)\bigr),
$$
meaning that the value $y_0 = \varepsilon(a_0, a_0) \in Y$ turns out to be a **fixed point** of the map $\alpha : Y \to Y$ ($\alpha(y_0) = y_0$). Conversely, if the answer alphabet $Y$ admits at least one transformation without fixed points (such as negation $\neg : \{0,1\} \to \{0,1\}$), then no internal card catalog $A$ can enumerate all questions $A \to Y$.

Let us formulate this argument in full generality for cartesian closed categories (F. W. Lawvere, *Diagonal arguments and cartesian closed categories*, Lecture Notes in Math. 92, 1969), paying special attention to the distinction between weak point-surjectivity and epimorphy.

> **Definition II.9.1 (Point-Surjectivity and Weak Point-Surjectivity in a Cartesian Closed Category).**  
> Let $\mathcal{C}$ be a cartesian closed category with terminal object $1$, finite products $A \times B$, and exponentials $Y^A$.
> 1. A morphism $e : A \to Y^A$ (or the evaluation morphism $\varepsilon : A \times A \to Y$ corresponding to it under currying) is called *weakly point-surjective* (in Lawvere's sense) if for every morphism $f : A \to Y$ there exists a global point (element) $a_f : 1 \to A$ such that for all global points $b : 1 \to A$ the equality of compositions holds:
>    $$
>    \varepsilon \circ \langle a_f, b \rangle = f \circ b : 1 \longrightarrow Y.
>    $$
> 2. A morphism $e : A \to Y^A$ is called *point-surjective* if for every morphism $f : A \to Y$ there exists a global point $a_f : 1 \to A$ representing $f$ as a morphism in $\mathcal{C}$: $\varepsilon \circ (a_f \times \mathrm{id}_A) \circ \lambda_A^{-1} = f$ (which is equivalent to the equality $e \circ a_f = \ulcorner f \urcorner : 1 \to Y^A$). In the category of sets $\mathbf{Set}$ (and in any well-pointed category where global points $1 \to A$ separate morphisms), the two notions coincide.

> **Theorem II.9.1 (Lawvere's Diagonal Fixed-Point Theorem and the Limit of Internal Self-Description).**  
> *Classical foundation.* Lawvere's diagonal fixed-point theorem (1969) rests on the categorical form of Cantor's diagonal argument. *Contribution of this book:* Separation of pointwise surjectivity from the exponential in $\mathbf{Set}^{C_2}$ ($|Y^A| = 4$, $|(Y^A)^{C_2}| = 2$) with the observer-stratification rule.
> 1. **(Direct Lawvere Theorem).** Suppose that in a cartesian closed category $\mathcal{C}$ there exists a weakly point-surjective morphism $e : A \to Y^A$ (with curried evaluation $\varepsilon : A \times A \to Y$). Then **every** endomorphism $\alpha : Y \to Y$ has a fixed global point $y_0 : 1 \to Y$ ($\alpha \circ y_0 = y_0$).
> 2. **(Contrapositive: Prohibition of a Universal Internal Catalog of Questions).** If the answer object $Y$ admits an endomorphism $\alpha : Y \to Y$ without fixed global points (in particular, in $\mathbf{Set}$ for any answer set $Y$ of cardinality $|Y| \ge 2$, where a cyclic shift or negation $\neg$ has no fixed points), then for no state carrier $A$ does there **exist** a weakly point-surjective parametrization $e : A \to Y^A$.
> 3. **(Epimorphy on Objects and the Exponential $Y^A$ in the Topos $\mathbf{Set}^{C_2}$).** In the category of sets with an involution $\mathbf{Set}^{C_2}$ ($C_2 = \{1, \sigma\}$, $\sigma^2 = 1$), which is not well-pointed, a categorical epimorphism need not induce a surjection on global points, while the exponential $Y^A$ is determined by the Yoneda formula:
>    - the global points $\mathrm{Hom}_{\mathbf{Set}^{C_2}}(1, X) = X^{C_2} = \{x \in X : \sigma x = x\}$ are the fixed points of the involution $\sigma$;
>    - if $A = C_2 = \{0, 1\}$ with the free action $\sigma(x) = 1 - x$, then the set of global points is empty: $A^{C_2} = \varnothing$, even though the canonical projection $p : A \twoheadrightarrow 1$ is surjective as a map of sets and is a categorical epimorphism in $\mathbf{Set}^{C_2}$ (the induced map $A^{C_2} = \varnothing \to 1^{C_2} = \{*\}$ is not surjective);
>    - if we take the answer object $Y = \{0, 1\}$ with the trivial action of $C_2$ ($\sigma y = y$) and the negation endomorphism $\alpha = \neg : Y \to Y$ (which has no fixed points in $Y^{C_2} = Y$), then for the free object $A = C_2$ the exponential $Y^A$ in $\mathbf{Set}^{C_2}$ has underlying set $Y^A(*) = \mathrm{Hom}_{\mathbf{Set}^{C_2}}(C_2 \times A, Y) \cong \mathrm{Hom}_{\mathbf{Set}}(A, Y) = Y^2 = \{00, 01, 10, 11\}$ of cardinality $4$ with coordinate swap $\sigma(u_0, u_1) = (u_1, u_0)$: it decomposes into two global points $(Y^A)^{C_2} = \{00, 11\}$ (neither of which lifts to $A$, since $A^{C_2} = \varnothing$) and a free two-element subobject of antisymmetric questions $Y_{\mathrm{anti}} = \{01, 10\} \cong A$, while all four equivariant morphisms $A \to Y^A$ have image sizes $1$ or $2$ (more generally, in any group presheaf topos $\mathbf{Set}^G$ one has $|Y^A| = |Y|^{|A|} > |A|$ whenever $|Y| \ge 2$, so no epimorphism $A \twoheadrightarrow Y^A$ exists in $\mathbf{Set}^G$).

**Proof.**  
1. Let $\Delta_A = \langle \mathrm{id}_A, \mathrm{id}_A \rangle : A \to A \times A$ be the diagonal morphism. For any endomorphism $\alpha : Y \to Y$, form the composition
$$
f = \alpha \circ \varepsilon \circ \Delta_A : A \xrightarrow{\;\Delta_A\;} A \times A \xrightarrow{\;\varepsilon\;} Y \xrightarrow{\;\alpha\;} Y.
$$
By the weak point-surjectivity of $\varepsilon$, for the morphism $f : A \to Y$ there exists a global point $a_f : 1 \to A$ such that for all $b : 1 \to A$ we have $\varepsilon \circ \langle a_f, b \rangle = f \circ b$. Substituting $b = a_f$ here and taking into account $\Delta_A \circ a_f = \langle a_f, a_f \rangle$, we find for the global point $y_0 = \varepsilon \circ \langle a_f, a_f \rangle : 1 \to Y$:
$$
y_0 = \varepsilon \circ \langle a_f, a_f \rangle = f \circ a_f = \alpha \circ \varepsilon \circ \Delta_A \circ a_f = \alpha \circ \varepsilon \circ \langle a_f, a_f \rangle = \alpha \circ y_0,
$$
that is, $y_0$ is a fixed global point of the morphism $\alpha$.
2–3. The contrapositive of item 1 immediately yields item 2. In item 3, the shearing isomorphism $C_2 \times A \xrightarrow{\sim} C_2 \times U(A)_{\mathrm{triv}}$, $(g, a) \mapsto (g, g^{-1}a)$, identifies equivariant maps $C_2 \times A \to Y$ with arbitrary set maps $U(A) \to U(Y)$, whence by the Yoneda lemma $Y^A(*) \cong Y^2 = \{00, 01, 10, 11\}$ with action $\sigma(u_0, u_1) = (u_1, u_0)$. Its fixed points are the constant pairs $(Y^A)^{C_2} = \{00, 11\}$, while the antisymmetric pairs form a free orbit $\{01, 10\} \cong A$. Since $A^{C_2} = \varnothing$, no global point $1 \to Y^A$ factors through $A$, and the images of the four equivariant maps $A \to Y^A$ (determined by sending $0 \in A$ to any element of $Y^2$) are $\{00\}$, $\{11\}$, and $\{01, 10\}$ of sizes $1, 1, 2, 2 < 4 = |Y^A|$. For an arbitrary group $G$, the same shearing isomorphism $G \times A \cong G \times U(A)_{\mathrm{triv}}$ gives $|U(Y^A)| = |Y|^{|A|}$, which for $|Y| \ge 2$ excludes pointwise surjective morphisms $A \to Y^A$ by Cantor's theorem. $\blacksquare$

> **Methodological Boundary (Exact Relationship Between the Rule $\mathcal{O} \notin X$ from the Introduction and Lawvere's Theorem).**  
> It is important not to conflate two distinct statements:
> 1. The notation $\mathcal{O} \notin X$ introduced in the `Introduction` to the First Volume is an **external typing convention for the operational contract $\Gamma$**: by definition, we distinguish the type of the state carrier $X$ from the type of the observation contract $\Gamma = (X, \mathcal{Q}, \mathcal{A}, \dots)$ itself. This convention is not "derived" from Lawvere's theorem; rather, it establishes the grammar of our language.
> 2. **Lawvere's Theorem (`Theorem II.9.1`)** is a rigorous internal theorem about what happens if one attempts to **fold** the external space of questions $\mathcal{Q} = Y^X$ inside the carrier $X$ itself via a surjective encoder $e : X \twoheadrightarrow Y^X$: as soon as $Y$ admits a fixed-point-free negation $\neg$, the diagonal question $g(x) = \neg \varepsilon(x, x)$ destroys the completeness of the internal encoding. The special case $Y = \{0,1\}$ in $\mathbf{Set}$ yields Cantor's classical theorem $|2^X| > |X|$ (in particular, already for $|X| = 3$, the three rows of a $3 \times 3$ matrix cannot enumerate all $2^3 = 8$ Boolean predicates on $X$).

---

## §II.9.2. Group Cohomology, Shapiro's Lemma, and Minimal Memory Quotients for Non-Split Extensions (Illustrated by the $64$-Element Group and the Affine Fano Group)

In `Chapter II.4` (§II.4.3), we encountered the first non-split central group extension $1 \to C_2 \to Q_8 \to V_4 \to 1$. Let us now generalize this construction to a general theorem characterizing when a non-split sign $2$-cocycle $\beta \in Z^2(G, \mathbb{F}_2)$ (we denote the $2$-cocycle by the letter $\beta$, reserving $\kappa$ for the parity charge of Book I) can be trivialized (untwisted into a direct product) upon passing to a transitive memory quotient set $X = G / K$.

Let $G$ be a finite group acting trivially on the phase fiber $\mathbb{F}_2 = \{0, 1\}$, and let
$$
0 \longrightarrow \mathbb{F}_2 \longrightarrow \widetilde{G}_\beta \xrightarrow{\;\pi\;} G \longrightarrow 1
$$
be the central extension defined by a normalized $2$-cocycle $\beta : G \times G \to \mathbb{F}_2$ ($\beta(g_1, g_2) \oplus \beta(g_1 g_2, g_3) = \beta(g_1, g_2 g_3) \oplus \beta(g_2, g_3)$) with the multiplication law in $\widetilde{G}_\beta = G \times \mathbb{F}_2$:
$$
(g_1, s_1)\cdot(g_2, s_2) = \bigl(g_1 g_2,\; s_1 \oplus s_2 \oplus \beta(g_1, g_2)\bigr).
$$
We ask: under what condition on a transitive $G$-set of memory classes $X = G/K$ (where $K \le G$ is the stabilizer of the base class $x_0 = eK \in X$) does there exist a phase gauge function $\lambda : X \times G \to \mathbb{F}_2$ (or a local splitting of the cocycle over the orbit $X$) that trivializes the cocycle $\beta$ along trajectories on $X$:
$$
\beta(g_1, g_2) = \lambda(x, g_1) \oplus \lambda(x \cdot g_1, g_2) \oplus \lambda(x, g_1 g_2) \qquad (\forall x \in X,\; g_1, g_2 \in G)?
$$

> **Theorem II.9.2 (Phase-Lifting Criterion via Shapiro's Lemma, the $64$-Element Extension with Cocycle $\beta$, and the Minimal $8$-Element Quotient of $\mathrm{AGL}_3(\mathbb{F}_2)$).**  
> *Classical foundation.* Cohomological classification of group extensions and the correspondence between $1$-cocycles and complements in semidirect products belong to classical group theory. *Contribution of this book:* Explicit computation of the $64$-element non-split extension $\widetilde{G}_\beta$ and the two orbits $8 + 56 = 64$ of the affine action of $\mathrm{GL}_3(\mathbb{F}_2)$ on $X_{64}$.
> 1. **(Stabilizer Restriction Criterion via Shapiro's Lemma).** For a transitive $G$-set $X = G/K$, the function space $\mathbb{F}_2[X] = \mathrm{Map}(G/K, \mathbb{F}_2)$ is canonically isomorphic to the coinduced $G$-module $\mathrm{Coind}_K^G(\mathbb{F}_2)$. By **Shapiro's lemma** for group cohomology (K. S. Brown, *Cohomology of Groups*, Springer, 1982, Ch. III, Prop. 6.2), the evaluation homomorphism at the basepoint $x_0 = eK$ defines a canonical isomorphism:
>    $$
>    H^2\bigl(G,\, \mathrm{Map}(G/K, \mathbb{F}_2)\bigr) \xrightarrow{\;\sim\;} H^2(K, \mathbb{F}_2),
>    $$
>    under which the diagonal embedding of the constant coefficient module $\mathbb{F}_2 \hookrightarrow \mathrm{Map}(G/K, \mathbb{F}_2)$ passes to the cohomology restriction homomorphism $\mathrm{Res}^G_K : H^2(G, \mathbb{F}_2) \to H^2(K, \mathbb{F}_2)$. Consequently, a $2$-cocycle $\beta \in Z^2(G, \mathbb{F}_2)$ becomes trivialized over the quotient set $X = G/K$ **if and only if its restriction to the stabilizer $K$ is cohomologous to zero**:
>    $$
>    \bigl[\beta|_{K \times K}\bigr] = 0 \quad \text{in } H^2(K, \mathbb{F}_2)
>    $$
>    (that is, the extension $\pi^{-1}(K) \twoheadrightarrow K$ splits over the subgroup $K$). In particular, if the order of the stabilizer $|K|$ is **odd**, then $H^2(K, \mathbb{F}_2) = 0$ (since multiplication by $|K|$ is invertible on $\mathbb{F}_2$ while simultaneously annihilating $H^2(K, \mathbb{F}_2)$); therefore, over any quotient $G/K$ with an odd-order stabilizer $|K|$, every $2$-cocycle $\beta \in Z^2(G, \mathbb{F}_2)$ is trivialized unconditionally.
> 2. **(Explicit $64$-Element Non-Abelian Model with Bilinear Cocycle $\beta((g,u),(h,v)) = g_1 h_2$).** Let $G = \mathbb{F}_2^2 \times \mathbb{F}_2^3$ be the elementary abelian $2$-group of order $32$ with elements $(g, u)$, where $g = (g_1, g_2) \in \mathbb{F}_2^2$ and $u = (u_1, u_2, u_3) \in \mathbb{F}_2^3$, and let the $2$-cocycle $\beta : G \times G \to \mathbb{F}_2$ be given by the bilinear form on the first two bits:
>    $$
>    \beta\bigl((g, u),\, (h, v)\bigr) = g_1 h_2 \in \mathbb{F}_2.
>    $$
>    Then the central extension $\widetilde{G}_\beta = G \times_\beta \mathbb{F}_2$ has order $64$ ($|\widetilde{G}_\beta| = 64$, with $\widetilde{G}_\beta \cong D_4 \times \mathbb{F}_2^3$). Because for the nonzero diagonal element $t = ((1,1), 0) \in G$ the value of the cocycle on the pair $(t, t)$ equals
>    $$
>    \beta(t, t) = 1 \cdot 1 = 1 \ne 0,
>    $$
>    the element $(t, 0) \in \widetilde{G}_\beta$ has square $(t, 0)^2 = (0, \beta(t,t)) = (0, 1) \ne (0,0)$ (order $4$). Therefore, the restriction of $\beta$ to any subgroup $K \le G$ containing a vector with $g_1 = g_2 = 1$ **does not split**, and a minimal subgroup $K \le G$ on which $\beta|_{K \times K}$ is cohomologous to zero must avoid the diagonal $g_1 = g_2 = 1$ (for example, $K = \{(0, g_2)\} \times \mathbb{F}_2^3$ or $\{(g_1, 0)\} \times \mathbb{F}_2^3$ of index $[G : K] = 2$).
> 3. **(Two Affine Orbits $8 + 56 = 64$ and the Minimal $8$-Class Quotient over the Fano Group $\mathrm{GL}_3(\mathbb{F}_2)$).** Let $G = \mathrm{GL}_3(\mathbb{F}_2)$ be the simple automorphism group of the Fano plane of order $168$, acting on the $3$-bit charge space $V = \mathbb{F}_2^3$. Since the first cohomology group with coefficients in the natural module is nontrivial, $H^1(\mathrm{GL}_3(\mathbb{F}_2), \mathbb{F}_2^3) \cong \mathbb{F}_2$, there exists a unique (up to coboundary) nontrivial $1$-cocycle $c : \mathrm{GL}_3(\mathbb{F}_2) \to \mathbb{F}_2^3$ defining a fixed-point-free affine action of $\mathrm{GL}_3(\mathbb{F}_2)$ on $V$ ($g \star v = g v \oplus c(g)$), and on the $64$-element square $X_{64} = \mathbb{F}_2^3 \times \mathbb{F}_2^3$ the diagonal affine-linear action decomposes into **exactly two transitive orbits**:
>    - a small orbit of cardinality **$8$** with stabilizer $K_{21} \le \mathrm{GL}_3(\mathbb{F}_2)$ of order $168 / 8 = \mathbf{21}$ (the Frobenius group $C_7 \rtimes C_3$ of odd order $21$);
>    - a large orbit of cardinality **$56$** ($8 + 56 = 64$) with stabilizer $K_3 \le \mathrm{GL}_3(\mathbb{F}_2)$ of order $168 / 56 = \mathbf{3}$ (a cyclic subgroup of odd order $3$).
>    Since both stabilizers $K_{21}$ and $K_3$ have **odd orders** ($21$ and $3$), by item 1 we have $H^2(K_{21}, \mathbb{F}_2) = H^2(K_3, \mathbb{F}_2) = 0$, and the nontrivial central extension $\widetilde{G} \twoheadrightarrow \mathrm{GL}_3(\mathbb{F}_2)$ splits completely over both orbits. At the same time, the **minimal number of memory classes** $X = \mathrm{GL}_3(\mathbb{F}_2) / K$ over which the $2$-torsion of the group $\mathrm{GL}_3(\mathbb{F}_2)$ splits is equal to **exactly $8$** ($[G : K_{21}] = 168 / 21 = 8$), because the only subgroups of smaller index $7$ in $\mathrm{GL}_3(\mathbb{F}_2)$ are isomorphic to $\mathfrak{S}_4$ (of order $24$) and contain Sylow $2$-subgroups $D_4$ of even order $8$, on which the $2$-cocycle does not vanish. Every equivariant projection $X_{64} \twoheadrightarrow \mathrm{GL}_3(\mathbb{F}_2)/K_{21}$ onto this minimal $8$-element quotient is uniquely determined by the images of the two base orbits (yielding, up to automorphism, exactly two canonical quotient maps).

**Proof.**  
1. A cochain $\lambda : G/K \times G \to \mathbb{F}_2$ is precisely a $1$-cochain of the group $G$ with values in the function module $\mathrm{Map}(G/K, \mathbb{F}_2)$ (with right shift of the argument), and the condition $\beta(g_1, g_2) = \lambda(x, g_1) \oplus \lambda(x \cdot g_1, g_2) \oplus \lambda(x, g_1 g_2)$ means that the image of the constant $2$-cocycle $\beta$ in $Z^2(G, \mathrm{Map}(G/K, \mathbb{F}_2))$ is the coboundary $\delta \lambda$. By Shapiro's lemma, $H^2(G, \mathrm{Map}(G/K, \mathbb{F}_2)) \cong H^2(K, \mathbb{F}_2)$ via evaluation at the base coset $x_0 = eK$, where $K$ acts trivially, which proves the criterion $[\beta|_{K \times K}] = 0$. If $2 \nmid |K|$, then by the transfer theorem $|K| \cdot H^2(K, \mathbb{F}_2) = 0$, while $|K| \equiv 1 \pmod 2$, whence $H^2(K, \mathbb{F}_2) = 0$.
2. For $\beta((g,u),(h,v)) = g_1 h_2$, the associativity of the extension follows from bilinearity: $\beta(a,b) \oplus \beta(a+b, c) = a_1 b_2 \oplus (a_1+b_1)c_2 = a_1(b_2+c_2) \oplus b_1 c_2 = \beta(a, b+c) \oplus \beta(b, c)$. In any group, a $2$-coboundary $(\delta \mu)(t, t) = \mu(t) \oplus \mu(t) \oplus \mu(2t) = \mu(0) = 0$ under the normalization $\mu(0) = 0$ vanishes on elements of order $2$ ($2t = 0$). Therefore, the equality $\beta(t, t) = 1 \ne 0$ at $t = ((1,1), 0)$ is a cohomological invariant and forbids trivialization on any subgroup $K \ni t$.
3. In the group $\mathrm{GL}_3(\mathbb{F}_2)$ of order $168 = 2^3 \cdot 3 \cdot 7$, the maximal subgroups are exhausted by two conjugacy classes of parabolic subgroups of order $24$ ($\cong \mathfrak{S}_4$, stabilizers of Fano points and lines, index $7$) and one conjugacy class of Frobenius groups $K_{21} \cong C_7 \rtimes C_3$ of odd order $21$ (normalizers of a Sylow $7$-subgroup, index $168/21 = 8$). Since all subgroups of index $< 8$ have index $7$ and order $24$ (they contain a Sylow $2$-subgroup $D_4$ of $\mathrm{GL}_3(\mathbb{F}_2)$, which maps injectively on the $2$-primary part of cohomology $H^2(\mathrm{GL}_3(\mathbb{F}_2), \mathbb{F}_2) \hookrightarrow H^2(D_4, \mathbb{F}_2)$), on no quotient of cardinality $< 8$ does the nontrivial $2$-cocycle split, whereas on the quotient of cardinality $8 = 168/21$ the stabilizer $K_{21}$ has odd order $21$ and $H^2(K_{21}, \mathbb{F}_2) = 0$. $\blacksquare$

---

## §II.9.3. Summary Panorama of the Nine Canonical Regimes of Minimal Memory in Books I–II

Throughout Books I and II, we have encountered the observer's problem in diverse mathematical settings: **what is the exact minimal volume of hidden memory (in states, dimensions, or bits) that the observer must retain in order to continue future answers without error and without losing nontrivial global twists?**

Let us compile all nine canonical regimes of minimal memory proven in Books I and II into a single reference table specifying their exact mathematical carrier, units of measurement, and place of proof.

#### Table II.9.1. Nine Canonical Regimes of the Observer's Minimal Memory in Books I and II

| No. | Canonical Memory Regime | Mathematical Carrier and Formula | Exact Threshold and Unit of Measurement | Where Proven in Books I–II |
| :---: | :--- | :--- | :--- | :--- |
| `1` | **Moore–Nerode Automaton History Memory** | Quotient set of histories $X / {\sim_\Gamma}$ across all future protocols | $|X / {\sim_\Gamma}|$ distinguishable automaton states | `Chapter I.3` (`Theorem I.3.1`) |
| `2` | **Reversible Extension with Trace and Cost of Trace Erasure (reversible extension with history register after C. H. Bennett, 1973)** | Injective embedding $x \mapsto (T(x), \sigma(x))$ with trace register $\Sigma$ | $\ge \max_y |T^{-1}(y)|$ branches in a fiber ($\log_2 M$ trace bits) | `Chapter I.4` (`Theorem I.4.1`) |
| `3` | **Ho–Kalman Linear Hankel Memory** | Skeletal factorization of the block Hankel operator $\mathcal{H} = \mathcal{O}\mathcal{R}$ | $d_{\min} = \operatorname{rank}_K \mathcal{H}$ linear coordinates over field $K$ | `Chapter I.8` (`Theorem I.8.3`) and `Chapter II.1` (`Theorem II.1.2`) |
| `4` | **Quadratic and Cubic Cayley Jet Window** | Quotient ring of jets $J^m_0 = K[x]/(x^{m+1})$ and dual numbers $K[\varepsilon]/(\varepsilon^2)$ | $\dim_K J^m_0 = m+1$ ($2$ coordinates for $\varepsilon^2 = 0$; $4$ for defect $-\frac{1}{12}h^3 J_a^3$) | `Chapter II.2` (`Theorem II.2.1`, `Prop. II.2.2`) |
| `5` | **Cohomological Twist Memory on the Nerve of a Cover** | Cochain complex $C^\bullet(\mathcal{N}; \mathbb{F}_2)$ of the chessboard octahedron $O_6$ | $\dim_{\mathbb{F}_2} H^1(\mathcal{N}(O_6); \mathbb{F}_2) = 3$ bits of holonomy around $4$ hollow holes ($\kappa = 1$, $\sum_{r=1}^4 h_r = 0$) | `Chapter I.9` (`Theorem I.9.3a`) and `Chapter II.3` (`Theorem II.3.1`) |
| `6` | **Non-Abelian Loop and Spinor Sign Memory** | Octahedral symmetry group $W(B_3) \cong \mathfrak{S}_4 \times C_2$ and quaternions $Q_8 \twoheadrightarrow V_4$ | $|W(B_3)| = 48$ ($19$ involutions); $|Q_8| = 8$ ($1$ involution $-I_2$, non-split over $V_4$) | `Chapter II.4` (`Theorem II.4.1`, `Prop. II.4.1`) |
| `7` | **Nonassociative Fano Memory and Symplectic Octonion Core** | Modular octonions $\mathrm{Oct}(\mathbb{F}_2)$, Paige loop $M_{120}$, and core $V_6 = I^\perp/\langle I\rangle$ | $\dim_{\mathbb{F}_2} \mathrm{Oct}(\mathbb{F}_2) = 8$ bits ($256$ el.); $\dim_{\mathbb{F}_2} V_6 = 6$ bits ($64$ el., $120 = 36 + 84$) | `Chapter II.5` (`Theorems II.5.1, II.5.2`) |
| `8` | **Quantum Branch Effect Memory and `MUB / SIC` Packings** | Effect closure $W_\infty \subseteq \mathrm{Herm}_d(\mathbb{C})$, qubit tetrahedron, and $64$ Hoggar lines | $\dim_{\mathbb{R}} W_\infty \le d^2$ real coordinates ($4$ at $d=2$; $9$ at $d=3$; $64$ at $d=8$) | `Chapters II.6–II.7` (`Prop. II.6.1`, `Theorems II.7.1, II.7.2`) |
| `9` | **Minimal Quotient Trivializing a $2$-Cocycle via Shapiro's Lemma** | Quotient set $G/K$ with condition $[\beta|_{K\times K}] = 0$ in $H^2(K, \mathbb{F}_2)$ | $8$ memory classes ($\mathrm{GL}_3(\mathbb{F}_2)/K_{21}$ for $|K_{21}| = 21$, $8 + 56 = 64$) | `Chapter II.9` (`Theorem II.9.2`) |

> **Remark on Distinguishing Real Dimension from Bit Volume.**  
> Let us draw the reader's attention to the strict distinction between units of measurement in rows `3, 7, 8, 9` of this table:
> - when `Chapter II.1` or `Chapter II.6` speaks of $8$ or $9$ coordinates in a vector space $V = \mathbb{R}^d$ or $\mathrm{Herm}_3(\mathbb{C}) \cong \mathbb{R}^9$, this refers to the **dimension of a continuous real vector space** ($\dim_{\mathbb{R}}$);
> - when `Chapter II.5` or `Chapter II.9` speaks of $6$ bits of the symplectic core $V_6 \cong \mathbb{F}_2^6$ ($2^6 = 64$ states) or $8$ finite classes of the quotient $\mathrm{GL}_3(\mathbb{F}_2)/K_{21}$ ($\log_2 8 = 3$ bits of orbit index), this refers to the **finite cardinality of a set over $\mathbb{F}_2$**. Nowhere in the monograph is the continuous real dimension $\dim_{\mathbb{R}}$ identified with the number of binary states without explicitly specifying a finite partition of the scale.

All nine thresholds of `Table II.9.1` obey the unified three-regime classification by the solution count $|\mathcal{R}| \in \{1, >1, 0\}$ of the observer's consistency problem:
- **$|\mathcal{R}| = 1$ (forced canonical invariant):** the minimal Nerode automaton (`I.3`), Hankel rank $r = \operatorname{rank}\mathcal{H}$ (`II.1`), the jet algebra $J^m_0$ (`II.2`), branch closure $W_\infty$ and Busch's measure on $\mathcal{E}(\mathcal{H})$ (`II.6`), and the rational orthogonal projector $P_\perp$ of rank $1687$ (`II.8`);
- **$|\mathcal{R}| > 1$ (gauge torsor of internal frames):** similarity conjugation of minimal realizations under $\mathrm{GL}_r(\mathbb{F})$ (`II.1`), connection choices in $W(B_3)$ and spinor lifts in $Q_8 \subset 2O$ (`II.4`), the affine torsor of $36 + 28 = 64$ quadratic forms over $V_6^*$ (`II.5`), and Gram-matrix freedom across the affine slice of a polynomial (`II.8`);
- **$|\mathcal{R}| = 0$ (gluing obstruction forcing the next tier):** non-zero parity charge $\kappa = 1$ on the six-slice nerve $O_6$ (`I.9`, `II.3`), the odd class $[\beta_{\mathrm{PM}}] \ne 0$ in the Peres–Mermin square (`II.7`), the non-splitting $2$-cocycle $\beta(t,t) = 1$ on $\widetilde{G}_\beta$, and the Lawvere–Cantor diagonal obstruction to any point-surjection $A \to Y^A$ (`II.9`).

---

## §II.9.4. Concluding Map of Constructed Categories in Books I–II and Strict Obligations Toward Book III

Let us now assemble all the mathematical categories and functors constructed and proven in Books I and II into a single structural map:

```text
   MAP OF PROVEN FUNCTORS AND TRANSITIONS IN BOOKS I AND II

   [Book I: Finite Core of the Contract Gamma]
    Partial automata and scenes (S_4, O_6)
         |                     |
         | Nerode quotient     | Nerve of a cover N(U)
         v                     v
    Minimal automaton     Simplicial complex (O_6, Book I.9)
         |                     |
   ======|=====================|======================================
   [Book II: Four Enrichments]
         |                     |
         v (Ch. II.1-II.2)     v (Ch. II.3-II.4)
    Linear realizations   Chain complexes C_*(K; R), homologies H_*,
    (A,B,C), Hankel H,    principal G-torsors (S_w), and connection W(B_3)
    jets J^m_0 and Cayley      |
         |                     | Whitney W_k / de Rham R_k (Ch. II.8)
         |                     v
         |                Piecewise-linear forms and Cahn-Hilliard flow
         |
         +---> Walsh-Bloch bridge E_lambda on S_4 (Ch. II.6-II.7)
                     |
                     v
               Quantum effects E(C^d), SIC tetrahedron, Hoggar (d=8),
               and Peres-Mermin obstruction [beta_PM] != 0 in Coker delta = F_2 (parallel to kappa = 1 on N(O_6))
```

Within this map, every transition is backed by a proven theorem and a machine verification gate. But what happens when a researcher steps outside the pure mathematics of Books I–II and seeks to apply these constructions to **external computational, algorithmic, or textual domains**—hidden states of artificial networks, large directed weighted graphs, classical philosophical-linguistic treatises (Sāṃkhya, Yoga, Advaita, Pāṇini's grammar), combinatorial capacity ladders, oracle-free divisor-graph algorithms, and positional statistics of manuscripts?

Let us record here the principal methodological law that will open **Book III**:
1. **No theorem of Books I and II is proven by appeal to an external subject matter**, and conversely—**no mathematical theorem of Books I and II by itself proves the structure of an external system or historical text** without an explicitly presented domain bridge $(\iota, \mathcal{O}_\pi)$.
2. Every comparison of a mathematical invariant of Books I–II with an external domain in Book III must carry a **complete bridge passport**:
   - an explicit encoding map from raw domain data into the mathematical carrier ($\iota$);
   - an explicit inverse reading rule in domain-specific units ($\mathcal{O}_\pi$);
   - the position of the Observer in the experiment (who defines the cut $\iota$, who reads $\mathcal{O}_\pi$, and what forms the hollow face of the nerve);
   - a surrogate (null) control and an exact criterion of refutation (falsification).

---

## §II.9.5. Historical-Philosophical Parallel: The Apophatic Limit *neti neti* (`BU 2.3.6`) and the Completion of the Instrument's Work (`SK 64–68`)

In the oldest Upaniṣad of the Indian tradition—the *Bṛhadāraṇyaka Upaniṣad* (`BU 2.3.6`, as well as `3.9.26, 4.2.4, 4.4.22, 4.5.15`)—the limit of attempts to exhaust the ground of observation by a finite list of predicates is expressed by the famous apophatic formula *neti neti* ("not this, not this"): no particular determination from an intra-worldly catalog is identical to that by which the catalog itself is upheld.

In the concluding verses of the *Sāṃkhya-kārikā* (`SK 64–68`), the same boundary is described from the side of the instrument of distinction itself (*prakṛti / buddhi*):
- in `SK 64`, through sustained practice of distinction (*tattvābhyāsāt*), there arises the unmistakable recognition *nāsmi na me nāham* ("I am not this instrument, nothing of it belongs to me, this closed loop is not I");
- in `SK 67`, it is explained why, after this recognition is attained, the conditioned carrier continues for some time to revolve by the inertia of the previously accumulated trace (*saṃskāra-vaśāt cakra-bhrama-vat*—like the potter's wheel from our `Chapter II.1`, where after the input is switched off, $u_t = 0$, the free response of memory $C B^t h_0$ continues to ring in the reading window);
- and in `SK 68`, once the inertia of the trace is exhausted and the purpose of distinction is fulfilled, the instrument completes its work.

These classical texts belong to their own philosophical tradition and do not enter into any deductive premise of our theorems. Yet within the architecture of the Second Volume they form an accompanying thread: from the inertia of linear memory in `Chapter II.1` (`SK 67`) to Lawvere's diagonal theorem in `Chapter II.9` (`BU 2.3.6`, `SK 64`), which rigorously proves why no internal catalog of states $A$ can close within itself all questions about itself.

---

## §II.9.6. Transition to Book III

The Second Volume is complete. The finite core of the First Volume has received four rigorous continuations—linear-dynamical, topological-cohomological, nonassociative-quantum, and cellular-categorical. In **Chapter `III.1`**, which opens the Third Volume, we will formulate the strict law for constructing a domain bridge $(\iota, \mathcal{O}_\pi)$ and test the mathematical bridges of the theory—from dynamics and resolvent filtration on directed weighted graphs to Kneser–Johnson role graphs and Pāṇini's formal grammar, oracle-free cofactor graphs, and hidden Markov models.

---

## Summary Passport of Chapter II.9 (for Verification and Formalization)

| Statement of the Chapter | Content of the Verified Invariant | `Julia` Gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Theorem II.9.1` | Verification of the Lawvere–Cantor diagonal prohibition on finite carriers and the exponential $Y^A$ in $\mathbf{Set}^{C_2}$ ($|A^{C_2}| = 0$, $|Y^A| = 4$, $|(Y^A)^{C_2}| = 2$, image sizes of $A \to Y^A$ equal to $1, 1, 2, 2$) | `GATE-II09-01` |
| `Theorem II.9.2` (items 1–2) | Verification of the $2$-cocycle $\beta((g,u),(h,v)) = g_1 h_2$ on the $64$-element extension $\widetilde{G}_\beta$, the nontriviality $\beta(t,t) = 1$ on the diagonal, and the splitting criterion via Shapiro's lemma | `GATE-II09-02` |
| `Theorem II.9.2` (item 3) | Exhaustive enumeration of the affine action of $\mathrm{AGL}_3(\mathbb{F}_2)$ (of order $1344$) on $X_{64} = \mathbb{F}_2^3 \times \mathbb{F}_2^3$: decomposition into two orbits $8 + 56 = 64$, odd orders of stabilizers $21$ and $3$, and minimal quotient index $8 = 168/21$ | `GATE-II09-03` |
| `Table II.9.1` and `§II.9.4` | Summary cross-check of all nine regimes of minimal memory of Books I–II, strict `v3.3` prose lint gate, and zero-`Float64` algebraic verifier check | `GATE-II09-04`, `GATE-II09-05`, `GATE-II-SYS-FLOAT` |
