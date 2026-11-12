# Chapter II.3. When Local Sections Fail to Glue: Boundary Sign, the Nerve of Six Slices, and Homology of Obstructions

In the concluding chapter of Volume One (`Chapter I.9`, `Theorems I.9.3` and `I.9.3a`), we examined a fundamental property of local observations: **pairwise compatibility of local observations does not guarantee the existence of a single global state.** On the four-point scene $S_4 = \mathbb{F}_2^2 = \{00, 01, 10, 11\}$, the six two-point slices $X_0, X_1, C_0, C_1, B_0, B_1$ intersect pairwise in a single point along all $12$ edges of the octahedron $O_6$, yet out of the $8$ triangular faces of this octahedron, the four faces with even parity charge $\kappa = x_0 \oplus c_0 \oplus b_0 = 0$ are filled by points of the scene $S_4$, whereas the four faces with odd charge $\kappa = 1$ turn out to be **hollow holes** ($X_i \cap C_j \cap B_k = \varnothing$). On this nerve there arose a presheaf of local gauges $\mathcal{S}_w$ that is locally trivial on every edge yet possesses no global section whatsoever ($\mathcal{S}_w(\mathcal{N}) = \varnothing$).

In `Table I.9.3` of Book I, a direct promise was made: in Volume Two we would unite the **algebra of sign and mutual cancellation from `Chapter I.5`** with the **geometry of gluing and the nerve of a covering from `Chapter I.9`**, turning the combinatorial checking of cycles into a general simplicial theory of chain complexes, homology, and cohomology over an arbitrary coefficient ring $R$.

The present chapter addresses the third question of Volume Two:

> **How does the edge orientation sign from `Chapter I.5` generate the boundary operator $\partial$ satisfying the law $\partial_1 \partial_2 = 0$, how does a violation of the sheaf axiom itself differ from a cohomological obstruction $[w] \ne 0$ of a genuine torsor sheaf $\mathcal{S}_w$, and how does the coefficient ring $R$ govern the visibility of torsion under gluing?**

---

## §II.3.1. Sign from Chapter I.5 Meets Gluing from Chapter I.9: Seam Orientation and the Identity $\partial_{k-1}\partial_k = 0$

Recall why the observer in `Chapter I.5` needed a signed ring ($\mathbb{Z}$ instead of $\mathbb{N}$): without sign, it is impossible to distinguish a forward step along an arrow $u \to v$ from a return step $v \to u$, and impossible to write the law of **mutual cancellation of oppositely directed contributions** $(+1) + (-1) = 0$.

In `Chapter I.9`, we checked gluing consistency on a triangle of three windows $(U_0, U_1, U_2)$ over the field $\mathbb{F}_2$, where $+1 \equiv -1 \pmod 2$ and the direction of edge traversal did not affect the sum $w_{01} \oplus w_{12} \oplus w_{02}$. As soon as local data take values in an abelian group or a module over a ring $R$ (for example, $R = \mathbb{Z}$ or $R = \mathbb{Q}$—clock offsets, potential differences, fluxes across a boundary), however, the direction of transition from window $U_i$ to window $U_j$ becomes decisive: if the dial reading shifts by $+w_{01}$ under the transition $U_0 \to U_1$, then under the reverse transition $U_1 \to U_0$ it must shift by $-w_{01}$.

Let us see what happens when we traverse the boundary of an oriented triangle (a two-dimensional simplex $\Delta^2 = [v_0, v_1, v_2]$ with three ordered vertices $v_0 < v_1 < v_2$):
1. the triangle $[v_0, v_1, v_2]$ has three boundary edges, obtained by successively deleting one of the vertices $v_0, v_1, v_2$ with alternating sign $(-1)^i$:
   $$
   \partial_2 [v_0, v_1, v_2] = +[v_1, v_2] - [v_0, v_2] + [v_0, v_1] = [v_0, v_1] + [v_1, v_2] - [v_0, v_2];
   $$
2. for each oriented edge $[v_i, v_j]$, the boundary $\partial_1$ is the difference between its head and its tail (the signed dipole from `Chapter I.5`):
   $$
   \partial_1 [v_i, v_j] = [v_j] - [v_i];
   $$
3. applying $\partial_1$ to the boundary of the triangle $\partial_2 [v_0, v_1, v_2]$ yields
   $$
   \partial_1 \partial_2 [v_0, v_1, v_2] = \bigl([v_2] - [v_1]\bigr) - \bigl([v_2] - [v_0]\bigr) + \bigl([v_1] - [v_0]\bigr) = 0!
   $$

```text
   SIGN OF CHAPTER I.5 AS THE BOUNDARY CANCELLATION MECHANISM ∂₁∂₂ = 0 ON TRIANGLE Δ²

                      v₁
                     /  \
        +[v₀,v₁]   /    \   +[v₁,v₂]
       (-[v₀]+[v₁])/  Δ²  \(-[v₁]+[v₂])
                  /        \
                v₀ --------> v₂
                   -[v₀,v₂]
                 (+[v₀]-[v₂])

    Each vertex enters the boundary ∂₁(∂₂[v₀,v₁,v₂]) exactly twice:
    once as the head of an incoming edge (+) and once as the tail of an outgoing edge (-).
    The sign from Chapter I.5 cancels all three vertices completely: ∂₁∂₂ = 0.
```

Here is the synthesis of `Chapter I.5` and `Chapter I.9` promised in Book I: **the sign $(-1)^i$ in the simplicial boundary operator is precisely the accounting of the fact that every intermediate vertex (and every internal gluing seam between two adjacent triangles) is traversed twice in opposite directions and therefore cancels out.**

Let us formulate this construction in general form for an arbitrary simplicial complex $K$ and a commutative coefficient ring $R$ with unity.

> **Definition II.3.1 (Chain complex $C_\bullet(K; R)$, cochain complex $C^\bullet(K; R)$, homology, and cohomology).**  
> Let $K$ be a finite simplicial complex with a linearly ordered vertex set $V(K)$.
> 1. For each $k \ge 0$, the module of *oriented $k$-chains* $C_k(K; R)$ is the free $R$-module generated by the ordered $k$-simplices $\sigma = [v_0, v_1, \dots, v_k] \in K_k$ ($v_0 < v_1 < \cdots < v_k$). The *boundary homomorphism* $\partial_k : C_k(K; R) \to C_{k-1}(K; R)$ is defined on basis simplices by the alternating sum of faces:
>    $$
>    \partial_k [v_0, v_1, \dots, v_k] = \sum_{i=0}^k (-1)^i [v_0, \dots, \widehat{v_i}, \dots, v_k], \qquad \partial_0 = 0,
>    $$
>    where the hat $\widehat{v_i}$ denotes omission of the vertex $v_i$.
> 2. The dual *module of $k$-cochains* $C^k(K; R) = \mathrm{Hom}_R(C_k(K; R), R)$ consists of functions $c : K_k \to R$ assigning to each $k$-simplex a weight from the ring $R$, and the *coboundary operator* $\delta_k : C^k(K; R) \to C^{k+1}(K; R)$ is adjoint to $\partial_{k+1}$:
>    $$
>    (\delta_k c)\bigl([v_0, \dots, v_{k+1}]\bigr) = c\bigl(\partial_{k+1}[v_0, \dots, v_{k+1}]\bigr) = \sum_{i=0}^{k+1} (-1)^i c\bigl([v_0, \dots, \widehat{v_i}, \dots, v_{k+1}]\bigr).
>    $$

> **Lemma II.3.1 (Fundamental identity $\partial_{k-1}\partial_k = 0$ and $\delta_{k+1}\delta_k = 0$).**  
> *Classical foundation.* The identities $\partial^2 = 0$ and $\delta^2 = 0$ are the classical fundamental identities of simplicial chains and cochains (Poincaré; Čech cochains; Eilenberg–Steenrod axiomatics, 1952). *Contribution of this book:* Use of this identity as the consistency condition for the observer's local records on the nerve of slices.
> For any simplicial complex $K$, any commutative ring $R$, and any $k \ge 1$, the following identities hold:
> $$
> \partial_{k-1} \circ \partial_k = 0, \qquad \delta_{k} \circ \delta_{k-1} = 0.
> $$
> Consequently, the image $\operatorname{Im}\partial_{k+1} = B_k(K; R)$ (*the module of $k$-boundaries*) is contained in the kernel $\ker \partial_k = Z_k(K; R)$ (*the module of $k$-cycles*), and the image $\operatorname{Im}\delta_{k-1} = B^k(K; R)$ (*the module of $k$-coboundaries*) is contained in the kernel $\ker \delta_k = Z^k(K; R)$ (*the module of $k$-cocycles*), which well-defines the $R$-modules of simplicial homology and cohomology:
> $$
> H_k(K; R) = Z_k(K; R) / B_k(K; R), \qquad H^k(K; R) = Z^k(K; R) / B^k(K; R).
> $$

**Proof.**  
Expanding the double sum $\partial_{k-1}\partial_k[v_0, \dots, v_k]$, we observe that the $(k-2)$-face with omitted vertices $\widehat{v_i}$ and $\widehat{v_j}$ for $i < j$ appears in the sum exactly twice:
- once when $v_j$ is deleted first at step $\partial_k$ with sign $(-1)^j$, and then $v_i$ (occupying the $i$-th position) is deleted at step $\partial_{k-1}$ with sign $(-1)^i$, yielding the sign $(-1)^{i+j}$;
- a second time when $v_i$ is deleted first at step $\partial_k$ with sign $(-1)^i$, after which the vertex $v_j$ shifts to the $(j-1)$-st position and is deleted at step $\partial_{k-1}$ with sign $(-1)^{j-1}$, yielding the opposite sign $(-1)^{i+j-1} = -(-1)^{i+j}$.
In any commutative ring $R$, the sum of these two contributions vanishes: $(-1)^{i+j} + (-1)^{i+j-1} = 0$. The dual identity $\delta_k \delta_{k-1} c = c \circ (\partial_k \partial_{k+1}) = 0$ follows automatically. $\blacksquare$

---

## §II.3.2. Pairwise Correspondence Locks, the Möbius Triangle, and Complete Computation of the Class $[w] \ne 0$ on the Octahedron $O_6$

Let us now apply the apparatus of §II.3.1 to the problem of reconciling local windows of the observer. Suppose a finite covering (or system of observation contexts) is equipped with a family of local state sets $\Omega_v$ over vertices $v \in V$ and pairwise compatibility relations (transition locks) $\mathcal{R}_{uv} \subseteq \Omega_u \times \Omega_v$ along edges $(u,v) \in E$.

Whenever the observer attempts to continue a local state along a two-edge path $v_1 \to v_2 \to v_3$, they take the set-theoretic composition of the two binary relations:
$$
\mathcal{R}_{12} \circ \mathcal{R}_{23} = \bigl\{ (a_1, a_3) \in \Omega_1 \times \Omega_3 \;\big|\; \exists a_2 \in \Omega_2 : (a_1, a_2) \in \mathcal{R}_{12} \text{ and } (a_2, a_3) \in \mathcal{R}_{23} \bigr\}.
$$
If, in addition, on the triangle $\Delta^2 = [v_1, v_2, v_3]$ a direct constraint is specified on the pair $(v_1, v_3)$—a binary relation $\mathcal{R}_{13} \subseteq \Omega_1 \times \Omega_3$, which lifts into the cube $\Omega_1 \times \Omega_2 \times \Omega_3$ as the cylindrical subset
$$
\widetilde{\mathcal{R}}_{13} = \mathcal{R}_{13} \times \Omega_2 = \bigl\{ (a_1, a_2, a_3) \in \Omega_1 \times \Omega_2 \times \Omega_3 \;\big|\; (a_1, a_3) \in \mathcal{R}_{13} \bigr\} \subseteq \Omega_1 \times \Omega_2 \times \Omega_3,
$$
then a globally compatible triple $(a_1, a_2, a_3)$ on the triangle exists if and only if the triple intersection is non-empty:
$$
\mathcal{S}(\Delta^2) = \bigl(\mathcal{R}_{12} \times \Omega_3\bigr) \cap \bigl(\Omega_1 \times \mathcal{R}_{23}\bigr) \cap \widetilde{\mathcal{R}}_{13} \ne \varnothing,
$$
which, under projection onto the outer coordinates $\Omega_1 \times \Omega_3$, is strictly equivalent to the non-emptiness of the intersection of the composition with the direct lock:
$$
(\mathcal{R}_{12} \circ \mathcal{R}_{23}) \cap \mathcal{R}_{13} \ne \varnothing.
$$

Take the binary local phase alphabet $\Omega_1 = \Omega_2 = \Omega_3 = \{0,1\} \cong \mathbb{F}_2$. On the first two edges, place identity locks $\mathcal{R}_{12} = \mathrm{id} = \{(0,0), (1,1)\}$ and $\mathcal{R}_{23} = \mathrm{id} = \{(0,0), (1,1)\}$, and on the closing edge $(v_1, v_3)$ place the inversion (Möbius twist) lock $\mathcal{R}_{13} = \mathrm{flip} = \{(0,1), (1,0)\}$. Then:
- each pair of vertices individually has exactly two admissible compatible states ($|\mathcal{R}_{12}| = |\mathcal{R}_{23}| = |\mathcal{R}_{13}| = 2$);
- every open path of two edges has exactly two global continuations;
- yet on the closed triangle, the composition $\mathcal{R}_{12} \circ \mathcal{R}_{23} = \mathrm{id}$ is disjoint from $\mathcal{R}_{13} = \mathrm{flip}$:
  $$
  (\mathrm{id} \circ \mathrm{id}) \cap \mathrm{flip} = \{(0,0), (1,1)\} \cap \{(0,1), (1,0)\} = \varnothing!
  $$
In the language of cochains over $R = \mathbb{F}_2$, this means that the edge $1$-cochain of twists $w([v_1,v_2]) = 0$, $w([v_2,v_3]) = 0$, $w([v_1,v_3]) = 1$ has a non-zero coboundary on the face of the triangle $\Delta^2 = [v_1, v_2, v_3]$:
$$
(\delta_1 w)\bigl([v_1, v_2, v_3]\bigr) = w([v_2,v_3]) \oplus w([v_1,v_3]) \oplus w([v_1,v_2]) = 0 \oplus 1 \oplus 0 = 1 \ne 0.
$$
As long as the triangle $\Delta^2$ itself is filled by a two-dimensional face (meaning that the triple intersection of windows in the nerve is non-empty and requires simultaneous compatibility across all three windows), the condition $w \in Z^1(\Delta^2; \mathbb{F}_2)$ is violated already locally: $\delta_1 w \ne 0$.

What happens, however, when **the interior of the triangle is removed**—that is, when the triple of windows itself forms a **hollow hole** in the nerve, like the four odd faces of the octahedron $O_6$ in **Theorem I.9.3** and **Theorem I.9.3a** of Book I?

Let us carry out the complete computation of the cohomology $H^1(\mathcal{N}; \mathbb{F}_2)$ for the scene used throughout our book.

> **Theorem II.3.1 (Explicit cohomological computation on the nerve of six slices $\mathcal{N}(O_6)$ from Theorems I.9.3 and I.9.3a).**  
> *Classical foundation.* Simplicial cochains and cohomology of two-dimensional cell complexes over $\mathbb{F}_2$ (Alexandroff, 1928; Čech, 1932). *Contribution of this book:* Explicit matrix computation $\operatorname{rank}\delta_0 = 5$, $\operatorname{rank}\delta_1 = 4$, and $\dim_{\mathbb{F}_2} H^1(\mathcal{N}(O_6); \mathbb{F}_2) = 3$ on the checkerboard octahedron nerve of the six slices of $S_4$.
> Let $\mathcal{N}$ be the simplicial nerve of the six two-point slices $V(\mathcal{N}) = \{X_0, X_1, C_0, C_1, B_0, B_1\}$ of the four-point scene $S_4 = \mathbb{F}_2^2$, constructed in `Theorem I.9.3` of Book I:
> - the vertex set has $|V(\mathcal{N})| = 6$;
> - the edge set has $|E(\mathcal{N})| = 12$ (all pairs of slices from different axes, forming the $1$-skeleton of the octahedron $O_6$);
> - the set of filled two-dimensional faces $|F(\mathcal{N})| = 4$ consists of the exact four even triangles ($\kappa = i \oplus j \oplus k = 0$):
>   $$
>   F(\mathcal{N}) = \bigl\{ [X_0, C_0, B_0],\; [X_0, C_1, B_1],\; [X_1, C_0, B_1],\; [X_1, C_1, B_0] \bigr\},
>   $$
>   whereas the four odd triangles ($\kappa = i \oplus j \oplus k = 1$: $\{X_0, C_0, B_1\}$, $\{X_0, C_1, B_0\}$, $\{X_1, C_0, B_0\}$, $\{X_1, C_1, B_1\}$) have empty triple intersection in $S_4$ and **are absent from $F(\mathcal{N})$**.
>
> Then for the cochain complex $C^\bullet(\mathcal{N}; \mathbb{F}_2)$:
> 1. The dimension of the space of $0$-coboundary gauges $\operatorname{Im}(\delta_0 : C^0(\mathcal{N};\mathbb{F}_2) \to C^1(\mathcal{N};\mathbb{F}_2))$ equals $6 - 1 = 5$ (since the octahedron graph is connected, $\dim \ker \delta_0 = 1$).
> 2. The four even faces in $F(\mathcal{N})$ are pairwise edge-disjoint and partition the $12$ edges of the octahedron into four disjoint triples ($4 \times 3 = 12$). Therefore, the four rows of the matrix $\delta_1 : C^1(\mathcal{N}; \mathbb{F}_2) \to C^2(\mathcal{N}; \mathbb{F}_2)$ have pairwise disjoint supports and are linearly independent: the rank of the operator $\delta_1$ equals $4$, and the dimension of the space of $1$-cocycles equals
>    $$
>    \dim_{\mathbb{F}_2} Z^1(\mathcal{N}; \mathbb{F}_2) = 12 - 4 = 8.
>    $$
> 3. The first simplicial cohomology group of the nerve of six slices has dimension $3$:
>    $$
>    H^1(\mathcal{N}; \mathbb{F}_2) = Z^1(\mathcal{N}; \mathbb{F}_2) / B^1(\mathcal{N}; \mathbb{F}_2) \cong \mathbb{F}_2^3 \qquad (8 - 5 = 3, \quad \chi(\mathcal{N}) = 6 - 12 + 4 = -2 = \dim H^0 - \dim H^1),
>    $$
>    and the holonomies $(h_1(u), h_2(u), h_3(u), h_4(u)) \in \mathbb{F}_2^4$ of any cocycle $u \in Z^1(\mathcal{N}; \mathbb{F}_2)$ around the four hollow holes ($\kappa = 1$) are bound by the single global conservation law $h_1(u) \oplus h_2(u) \oplus h_3(u) \oplus h_4(u) = \sum_{\tau \in F(\mathcal{N})} (\delta_1 u)(\tau) = 0$ (since each of the $12$ edges of the octahedron belongs to exactly one even face and one odd hole), leaving $4 - 1 = 3$ independent cohomological generators.
> 4. In particular, the edge $1$-cochain $w \in C^1(\mathcal{N}; \mathbb{F}_2)$ from `Theorem I.9.3a` ($w(X_{x_0}, C_{c_0}) = x_0 \oplus c_0$, $w(X_{x_0}, B_{b_0}) = b_0$, $w(C_{c_0}, B_{b_0}) = 0$), which equals $1$ on the four edges $\{X_0 C_1, X_1 C_0, X_0 B_1, X_1 B_1\}$ and $0$ on the remaining eight edges, has zero coboundary $\delta_1 w = 0$ on all four filled faces $\tau \in F(\mathcal{N})$ (i.e., $w \in Z^1(\mathcal{N}; \mathbb{F}_2)$ is a genuine $1$-cocycle), yet yields the holonomy vector $(1,1,1,1) \ne (0,0,0,0)$ around the four hollow holes ($\kappa = 1$) and therefore is not equal to $\delta_0 g$ for any vertex gauge $g \in C^0(\mathcal{N}; \mathbb{F}_2)$:
>    $$
>    [w] \ne 0 \quad \text{in } H^1(\mathcal{N}; \mathbb{F}_2) \Longleftrightarrow \mathcal{S}_w(\mathcal{N}) = \varnothing.
>    $$

**Proof.**  
1. Connectedness of the $1$-skeleton of the octahedron $O_6$ implies that $\delta_0 g = 0 \iff g(u) = g(v)$ for all edges $(u,v) \in E(\mathcal{N})$, so $\ker \delta_0 = \{0, \mathbf{1}\}$ has dimension $1$, whence $\dim_{\mathbb{F}_2} B^1(\mathcal{N}; \mathbb{F}_2) = 6 - 1 = 5$.

2. Each of the $12$ edges of the octahedron—for instance, the edge $(X_0, C_0)$—is incident to exactly two triangles of the skeleton: one even face $[X_0, C_0, B_0]$ ($\kappa = 0$, belonging to $F(\mathcal{N})$) and one odd hole $[X_0, C_0, B_1]$ ($\kappa = 1$, not belonging to $F(\mathcal{N})$). Therefore, the four rows of the matrix $\delta_1 : \mathbb{F}_2^{12} \to \mathbb{F}_2^4$, corresponding to the four filled faces in $F(\mathcal{N})$, have pairwise disjoint supports of three edges each ($4 \times 3 = 12$) and are consequently linearly independent over $\mathbb{F}_2$: $\operatorname{rank}_{\mathbb{F}_2} \delta_1 = 4$. Hence $\dim_{\mathbb{F}_2} Z^1(\mathcal{N}; \mathbb{F}_2) = 12 - 4 = 8$ and $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 8 - 5 = 3$. On any cocycle $u \in Z^1(\mathcal{N}; \mathbb{F}_2)$, the sum of holonomies around all four odd holes equals the sum of values of $u$ over all $12$ edges, which simultaneously equals the sum of $(\delta_1 u)(\tau)$ over all four even faces and therefore vanishes: $h_1(u) \oplus h_2(u) \oplus h_3(u) \oplus h_4(u) = 0$.

3. For the cochain $w$ from `Theorem I.9.3a`, the sums of weights on the four filled faces ($\kappa = 0$) equal:
- on $[X_0, C_0, B_0]$: $0 \oplus 0 \oplus 0 = 0$;
- on $[X_0, C_1, B_1]$: $1 \oplus 1 \oplus 0 = 0$;
- on $[X_1, C_0, B_1]$: $1 \oplus 1 \oplus 0 = 0$;
- on $[X_1, C_1, B_0]$: $0 \oplus 0 \oplus 0 = 0$.
Thus $\delta_1 w = 0$ on $C_2(\mathcal{N}; \mathbb{F}_2)$, and $w \in Z^1(\mathcal{N}; \mathbb{F}_2)$. If there existed a vertex gauge $g \in C^0(\mathcal{N}; \mathbb{F}_2)$ satisfying $\delta_0 g = w$, then the sum of $\delta_0 g$ around any closed $3$-cycle of edges in the graph $O_6$ would equal $(g(u)\oplus g(v)) \oplus (g(v)\oplus g(z)) \oplus (g(z)\oplus g(u)) = 0$. Around the hollow triangles $\kappa = 1$ (for example, the cycle $X_0 - C_0 - B_1 - X_0$), however, the sum of weights of $w$ equals $0 \oplus 0 \oplus 1 = 1 \ne 0$. This contradiction proves that $[w] \ne 0$ in $H^1(\mathcal{N}; \mathbb{F}_2)$ and that $\mathcal{S}_w$ has no global sections. $\blacksquare$

---

## §II.3.3. Two Fundamentally Distinct Obstructions: Violation of the Sheaf Axiom ($\mathcal{G}$) versus a Non-Trivial Class $[w] \ne 0$ of a Genuine Torsor ($\mathcal{S}_w$)

In reading the literature on contextuality and sheaf theory, two completely distinct phenomena are frequently conflated, as both lead to local data failing to assemble into an expected global answer. Let us separate them with full rigor on the partially ordered set (poset) of open windows of a covering.

Let $(P, \le)$ be the poset of open sets of a covering (ordered by inclusion $V \subseteq U$), and let $\mathcal{F} : P^{\mathrm{op}} \to \mathbf{Set}$ (or $\mathbf{Ab}$) be a presheaf of observation data with restriction maps $\rho^U_V : \mathcal{F}(U) \to \mathcal{F}(V)$ for $V \subseteq U$. Recall that a presheaf $\mathcal{F}$ is called a **sheaf** (satisfies the locality/separation and gluing axioms) if for every covering $U = \bigcup_i U_i$ and every compatible family of local sections $s_i \in \mathcal{F}(U_i)$ agreeing on all pairwise overlaps ($\rho^{U_i}_{U_i \cap U_j}(s_i) = \rho^{U_j}_{U_i \cap U_j}(s_j)$), there exists a **unique** global section $s \in \mathcal{F}(U)$ satisfying $\rho^U_{U_i}(s) = s_i$.

Let us now compare two model objects:

### Phenomenon A: A Presheaf $\mathcal{G}$ That Is Not Itself a Sheaf (a Global Invariant Is Lost under Cutting)

Suppose the space $X = \{x_1, x_2\}$ consists of two points covered by two single-point windows $U_1 = \{x_1\}$ and $U_2 = \{x_2\}$ with empty intersection $U_1 \cap U_2 = \varnothing$. Define on the open subsets $U \subseteq X$ the parity presheaf $\mathcal{G}$ with values in $\mathbb{F}_2$: on the whole two-point space $X$ it records the joint parity $\kappa(b_1, b_2) = b_1 \oplus b_2 \in \mathbb{F}_2^2 / \{(0,0), (1,1)\} \cong \mathbb{F}_2$ of a bit pair, whereas upon restriction to either proper single-point window $U_i$ it loses the relative comparison between the two points and vanishes:
$$
\mathcal{G}(X) = \mathbb{F}_2 \quad (\text{global charge } \kappa = b_1 \oplus b_2 \in \{0,1\}), \qquad \mathcal{G}(U_1) = \{0\}, \qquad \mathcal{G}(U_2) = \{0\}, \qquad \mathcal{G}(\varnothing) = \{0\},
$$
with zero restriction maps $\rho^X_{U_i}(\kappa) = 0$.

Then on the covering $X = U_1 \cup U_2$, the local sections $s_1 = 0 \in \mathcal{G}(U_1)$ and $s_2 = 0 \in \mathcal{G}(U_2)$ are trivially compatible on the overlap $U_1 \cap U_2$, yet in $\mathcal{G}(X) = \{0, 1\}$ they correspond to **two distinct** global states $\kappa = 0$ and $\kappa = 1$ simultaneously ($\rho^X_{U_i}(0) = \rho^X_{U_i}(1) = 0$). Here the **separation (locality) axiom of a sheaf** is violated: the global property $\kappa \in \mathcal{G}(X)$ is not determined by its local projections onto the parts $U_1$ and $U_2$ at all (just as in `Proposition II.1.1` the character $w_{11}$ on $S_4$ vanishes in all one-bit projections while remaining non-zero on the whole scene $S_4$).

### Phenomenon B: A Genuine Sheaf / $\mathbb{F}_2$-Torsor $\mathcal{S}_w$ Possessing No Global Sections Due to the Topology of the Nerve ($[w] \ne 0$)

The presheaf of local gauges $\mathcal{S}_w$ on the simplicial nerve $\mathcal{N}(O_6)$ from `Theorem II.3.1` (and `Theorem I.9.3a`) is structured in a completely different way. On every individual simplex $\sigma \in \mathcal{N}$ (on every vertex, each of the $12$ edges, and each of the $4$ filled faces $\tau \in F(\mathcal{N})$, where $\delta_1 w(\tau) = 0$), the set of admissible gauges $\mathcal{S}_w(\sigma)$ is non-empty and consists of exactly two mutually opposite gauges ($|\mathcal{S}_w(\sigma)| = 2$, a free transitive action of the group $\mathbb{F}_2$). Moreover, on any contractible subcomplex (for example, on the star of any vertex or on any spanning tree of the octahedron), compatible local sections glue uniquely.

The reason that no global section exists on the entire nerve $\mathcal{N}(O_6)$ ($\mathcal{S}_w(\mathcal{N}) = \varnothing$) lies **not in a defect of the local gluing rule**, but in the non-trivial cohomological twist class $[w] \in H^1(\mathcal{N}; \mathbb{F}_2)$ around the hollow cycles of the nerve.

#### Table II.3.1. Distinguishing the Two Types of Obstructions to Global Assembly

| Feature | Phenomenon A: Non-sheaf presheaf $\mathcal{G}$ | Phenomenon B: Torsor presheaf $\mathcal{S}_w$ on the nerve $\mathcal{N}$ |
| :--- | :--- | :--- |
| Local sections on windows $U_i$ | Exist ($\mathcal{G}(U_i) = \{0\}$) | Exist and form an $\mathbb{F}_2$-torsor ($|\mathcal{S}_w(U_i)| = 2$) |
| Is a state determined by its restrictions to windows? | **No** (the separation axiom fails: $\kappa = 0$ and $\kappa = 1$ yield identical zeros on $U_i$) | **Yes** (on the covering $V(\mathcal{N})$, two global sections agreeing on all vertices coincide identically) |
| Gluing on a contractible tree of windows | Non-unique or loses the global charge | Exists and is unique once a base vertex is fixed |
| Cause of the obstruction on the whole space | The property is non-local by the very nature of the question (top Walsh character $w_{111}$) | Non-trivial cohomology class $[w] \ne 0$ in $H^1(\mathcal{N}; \mathbb{F}_2)$ around hollow holes |

---

## §II.3.4. Dependence of Homology and Cohomology on the Coefficient Ring $R$: Torsion of $\mathbb{R}P^2$ and the Smith Normal Form

In `Theorem II.3.1`, we worked over the field $\mathbb{F}_2$, where $2 = 0$ and sign does not differ from parity. Let us now show why passing from the field $\mathbb{F}_2$ to the ring of integers $\mathbb{Z}$ and the field of rational numbers $\mathbb{Q}$ is essential for the observer: there exist two-dimensional gluings with a Möbius twist whose obstruction is **visible over $\mathbb{Z}$ and $\mathbb{F}_2$, yet completely disappears (becomes invisible) under averaging over the field $\mathbb{Q}$ or $\mathbb{R}$.**

A classical example of such a gluing is provided by the real projective plane $\mathbb{R}P^2$—the closed non-orientable surface obtained by gluing antipodal points of the boundary of a disk (or by attaching a disk along the boundary loop of a Möbius band, which traverses its core twice).

Take the minimal $6$-vertex simplicial triangulation $K_{\mathbb{R}P^2}$ of the projective plane (obtained as the quotient of the $12$-vertex icosahedron by the antipodal involution): it contains
$$
f_0 = 6 \text{ vertices } \{1,2,3,4,5,6\}, \qquad f_1 = 15 \text{ edges (the complete graph } K_6\text{)}, \qquad f_2 = 10 \text{ triangles:}
$$
$$
\begin{aligned}
F(K_{\mathbb{R}P^2}) = \bigl\{ &[1,2,3],\; [1,2,4],\; [1,3,5],\; [1,4,6],\; [1,5,6], \\
&[2,3,6],\; [2,4,5],\; [2,5,6],\; [3,4,5],\; [3,4,6] \bigr\}.
\end{aligned}
$$
The Euler characteristic of this complex equals $\chi(K_{\mathbb{R}P^2}) = 6 - 15 + 10 = 1$.

> **Theorem II.3.2 (Smith normal form and coefficient sensitivity of the homology and cohomology of $\mathbb{R}P^2$ over $\mathbb{Z}, \mathbb{F}_2, \mathbb{Q}$).**  
> *Classical foundation.* Smith normal form of integer boundary matrices (H. Smith, 1861), the universal coefficient theorem, and cellular homology of the real projective plane $\mathbb{R}P^2$. *Contribution of this book:* Contrast between visibility of $\mathbb{Z}/2\mathbb{Z}$ torsion over $\mathbb{Z}$ and $\mathbb{F}_2$ ($H^2(\mathbb{R}P^2;\mathbb{F}_2) \cong \mathbb{F}_2$) and complete blindness of the rational window $H^1(\mathbb{R}P^2;\mathbb{Q}) = H^2(\mathbb{R}P^2;\mathbb{Q}) = 0$.
> For the minimal triangulation $K = K_{\mathbb{R}P^2}$ with integer boundary matrices $\partial_1 \in \mathbb{Z}^{6 \times 15}$ and $\partial_2 \in \mathbb{Z}^{15 \times 10}$:
> 1. The Smith normal form ($\mathrm{SNF}$) of the matrix $\partial_1$ over the ring $\mathbb{Z}$ has $5$ unit invariant factors $\mathrm{diag}(1, 1, 1, 1, 1, 0)$, whence $\operatorname{rank}_{\mathbb{Z}} \partial_1 = 5$ and the group of $1$-cycles $Z_1(K; \mathbb{Z}) = \ker \partial_1 \cong \mathbb{Z}^{10}$ is free of rank $15 - 5 = 10$.
> 2. The Smith normal form of the integer matrix $\partial_2 \in \mathbb{Z}^{15 \times 10}$ has full rank $10$, but its $10$ invariant factors are
>    $$
>    d(\partial_2) = (1, 1, 1, 1, 1, 1, 1, 1, 1, \,2\,).
>    $$
>    The tenth invariant factor $d_{10} = 2$ means that the fundamental cycle $\gamma$ of the projective plane is not itself the boundary of an integer $2$-chain ($\gamma \notin \operatorname{Im}\partial_2$), whereas its **doubling** $2\gamma$ coincides with the sum of all $10$ oriented triangles ($2\gamma \in \operatorname{Im}\partial_2$): upon a single traversal of the gluing seam, the two edges arrive with the same sign and add up to $2\gamma$ rather than canceling.
> 3. Consequently, the homology and cohomology groups of the complex $K_{\mathbb{R}P^2}$ change under variation of the coefficient ring $R \in \{\mathbb{Z}, \mathbb{F}_2, \mathbb{Q}\}$ as follows:
>
> | Coefficient ring $R$ | $H_0(K; R)$ | $H_1(K; R)$ | $H_2(K; R)$ | $H^1(K; R)$ | $H^2(K; R)$ | Does the instrument detect the Möbius twist? |
> | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
> | Integers $\mathbb{Z}$ | $\mathbb{Z}$ | $\mathbb{Z}/2\mathbb{Z}$ | $0$ | $0$ | $\mathbb{Z}/2\mathbb{Z}$ | **Yes** (torsion of order $2$ in $H_1$ and $H^2$) |
> | Binary field $\mathbb{F}_2$ | $\mathbb{F}_2$ | $\mathbb{F}_2$ | $\mathbb{F}_2$ | $\mathbb{F}_2$ | $\mathbb{F}_2$ | **Yes** ($2 \equiv 0 \pmod 2$, the rank of $\partial_2$ drops from $10$ to $9$) |
> | Rational field $\mathbb{Q}$ | $\mathbb{Q}$ | $0$ | $0$ | $0$ | $0$ | **No** ($2$ is invertible in $\mathbb{Q}$, torsion vanishes) |

**Proof.**  
Over the principal ideal domain $\mathbb{Z}$, there exist unimodular integer matrices $U \in \mathrm{GL}_{15}(\mathbb{Z})$ and $V \in \mathrm{GL}_{10}(\mathbb{Z})$ bringing the matrix $\partial_2$ to its diagonal Smith normal form $U \partial_2 V = \mathrm{diag}(1, \dots, 1, 2)$. Since $\partial_1 \partial_2 = 0$, the image $\operatorname{Im}\partial_2$ lies in the free submodule $Z_1(K; \mathbb{Z}) \cong \mathbb{Z}^{10}$ of rank $10$, and the quotient module $H_1(K; \mathbb{Z}) = Z_1(K;\mathbb{Z}) / \operatorname{Im}\partial_2$ is isomorphic to $\mathbb{Z}/1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/1\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}$, while $\ker \partial_2 = 0 \implies H_2(K; \mathbb{Z}) = 0$. For the cochain complex $C^\bullet(K; \mathbb{Z})$, the transposed matrix $\delta_1 = \partial_2^{\mathsf{T}} \in \mathbb{Z}^{10 \times 15}$ has the same invariant factors $(1,\dots,1,2)$, whence $\ker \delta_1 = B^1(K;\mathbb{Z}) \implies H^1(K;\mathbb{Z}) = 0$, and the cokernel is $H^2(K;\mathbb{Z}) = \mathbb{Z}^{10} / \operatorname{Im}\partial_2^{\mathsf{T}} \cong \mathbb{Z}/2\mathbb{Z}$ (in full agreement with the universal coefficient formula $H^2(K;\mathbb{Z}) \cong \mathrm{Ext}^1_{\mathbb{Z}}(H_1(K;\mathbb{Z}), \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$).
- Upon reduction modulo $2$ ($R = \mathbb{F}_2$), the factor $d_{10} = 2$ becomes $0 \pmod 2$: the rank of $\partial_2 \bmod 2$ drops from $10$ to $9$, the kernel $H_2(K; \mathbb{F}_2) = \ker(\partial_2 \bmod 2)$ becomes one-dimensional ($\cong \mathbb{F}_2$, the fundamental class modulo $2$), and $\dim_{\mathbb{F}_2} H_1(K; \mathbb{F}_2) = 10 - 9 = 1$.
- Over the field $R = \mathbb{Q}$, the number $2$ is invertible ($1/2 \in \mathbb{Q}$): since $2\gamma = \partial_2 c_2$, the cycle $\gamma = \partial_2(\frac{1}{2} c_2)$ becomes an exact boundary of a rational $2$-chain, the rank of $\partial_2$ over $\mathbb{Q}$ remains equal to $10$, and all higher homology and cohomology groups vanish: $H_1(K;\mathbb{Q}) = H_2(K;\mathbb{Q}) = H^1(K;\mathbb{Q}) = H^2(K;\mathbb{Q}) = 0$. $\blacksquare$

This result carries a vital methodological lesson for the observer: **if an instrument immediately converts discrete integer or binary readings into averaged real/rational means (dividing by $2$), it becomes completely blind to the $2$-torsion ($\mathbb{Z}/2\mathbb{Z}$) of non-orientable gluings.** To retain the Möbius twist and the parity charge $\kappa$, the observer must preserve arithmetic over $\mathbb{Z}$ or $\mathbb{F}_2$.

---

## §II.3.5. Chapter Summary and Bridge to Chapter II.4

The table below summarizes the results of `Chapter II.3` on local and global gluing.

#### Table II.3.2. From the Sign of Chapter I.5 and the Nerve of Chapter I.9 to Homology and Cohomology of Chapter II.3

| Object and question of the observer | Mathematical construction in `Chapter II.3` | Verified gluing criterion |
| :--- | :--- | :--- |
| Sign of seam traversal direction (`Chapter I.5`) | Alternating sign $(-1)^i$ in $\partial_k$ and $\delta_k$ | Identity $\partial_{k-1}\partial_k = 0$: a twice-traversed seam cancels (`Lemma II.3.1`) |
| Triangle of three windows with inversion | Composition of relations $(\mathcal{R}_{12} \circ \mathcal{R}_{23}) \cap \mathcal{R}_{13} = \varnothing$ | Local coboundary $\delta_1 w(\Delta^2) = 1 \ne 0$ |
| Checkerboard octahedron of six slices $\mathcal{N}(O_6)$ on $S_4$ (`Theorems I.9.3, I.9.3a`) | $6$ vertices, $12$ edges, $4$ even faces ($\kappa=0$), and $4$ hollow holes ($\kappa=1$) | $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$; the cochain $w$ is a genuine cocycle ($\delta_1 w = 0$), yet $[w] \ne 0$ (`Theorem II.3.1`) |
| Loss of a global property versus cycle twist | Non-sheaf presheaf $\mathcal{G}$ versus genuine torsor $\mathcal{S}_w$ | In $\mathcal{G}$ separation fails; in $\mathcal{S}_w$ local gluing is exact, yet $\mathcal{S}_w(\mathcal{N}) = \varnothing$ (`Table II.3.1`) |
| Visibility of the Möbius twist depending on the scale $R$ | Smith normal form $\mathrm{SNF}(\partial_2) = \mathrm{diag}(1,\dots,1,2)$ on $\mathbb{R}P^2$ | Torsion $\mathbb{Z}/2\mathbb{Z}$ is visible over $\mathbb{Z}$ and $\mathbb{F}_2$, but vanishes over $\mathbb{Q}$ (`Theorem II.3.2`) |

In `Chapter II.3`, weights on edges and simplices took values in a **commutative** ring $R$ ($\mathbb{F}_2, \mathbb{Z}, \mathbb{Q}$), and therefore the result of traversing a loop did not depend on the choice of basepoint or the order of composition of non-commuting transformations. What happens, however, when elements of a non-commutative symmetry group $G$ (such as a permutation group, the quaternion group $Q_8$, the full symmetry group of the octahedron $W(B_3) = \mathrm{Aut}(O_6)$, or the braid group $B_3$) are transported along the edges of the nerve? This is the subject of **Chapter `II.4`**.

---

## Summary Passport of Chapter II.3 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Lemma II.3.1` and `§II.3.2` | Identity $\partial_1 \partial_2 = 0$ and emptiness of the intersection $(\mathrm{id}\circ\mathrm{id}) \cap \mathrm{flip} = \varnothing$ in the Möbius triangle | `GATE-II03-01` |
| `Theorem II.3.1` | Complete computation on the nerve $\mathcal{N}(O_6)$ of the scene $S_4$: $\operatorname{rank}\delta_0 = 5$, $\operatorname{rank}\delta_1 = 4$, $\dim H^1(\mathcal{N};\mathbb{F}_2) = 3$, $\delta_1 w = 0$, and absence of a gauge $w = \delta_0 g$ among all $64$ vectors $g \in \mathbb{F}_2^6$ | `GATE-II03-02` |
| `Theorem II.3.2` | Computation of the Smith normal form $\mathrm{SNF}(\partial_2)$ for the $6$-vertex triangulation of $\mathbb{R}P^2$ with invariant factor $d_{10} = 2$ and rank verification over $\mathbb{Z}, \mathbb{F}_2, \mathbb{Q}$ | `GATE-II03-03` |
| `§II.3.3` (`Table II.3.1`) | Comparison of the violation of separation in the presheaf $\mathcal{G}$ with local contractibility and the absence of a global section in the torsor $\mathcal{S}_w$ | `GATE-II03-04` |
