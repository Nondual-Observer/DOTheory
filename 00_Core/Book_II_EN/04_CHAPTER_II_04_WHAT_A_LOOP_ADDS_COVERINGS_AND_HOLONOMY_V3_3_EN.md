# Chapter II.4. What a Loop Adds: Coverings, Discrete Connection, Torsors, and the Symmetry Group of the Observer's Octahedron

In `Chapter II.3`, we studied how local slices of the observer glue along a simplicial nerve when the transition data on the edges take values in a commutative coefficient ring $R$ ($\mathbb{F}_2$, $\mathbb{Z}$, or $\mathbb{Q}$). In that abelian regime, the obstruction to global assembly is measured by the first cohomology group $H^1(\mathcal{N}; R)$ and does not depend on the order in which the observer traverses loops meeting at a single vertex.

In the geometry of fiber bundles, the theory of group-labeled graphs, and the combinatorics of scenes of distinction, however, what is transported along each transition edge $e = (u, v)$ between two local windows $U_u$ and $U_v$ is an **invertible transformation of the internal fiber** (not reducible in general to a scalar number)—an element of a symmetry group $G$ that need not be commutative at all. When the observer transports a local frame along a closed loop $\gamma$ in the overlap graph and returns to the initial window $U_{v_0}$, they discover that the frame has rotated or permuted its states under the action of a *holonomy (monodromy)* element $g_\gamma \in G$.

From this arises the fourth question of Volume Two, directly announced in `Table I.9.3` of Book I:

> **How are discrete connections, parallel transport, and principal $G$-torsors structured on the overlap graph of the observer's windows, how does the non-abelian symmetry group of the octahedron $W(B_3) \cong \mathfrak{S}_4 \times C_2$ govern the four-point scene $S_4$ and the parity charge $\kappa$ of Book I, and what false identifications are prohibited by covering theory?**

The present chapter provides a complete answer to this question:
1. first, we introduce a **discrete $G$-connection** on an overlap graph, parallel transport along paths, curvature (holonomy around elementary faces), and principal $G$-torsors, showing how the two-window Möbius gluing on the circle $S^1$ generates the canonical double covering;
2. second, we erect the **central geometric bridge between Books I and II**: we prove that the Weyl group $W(B_3) \cong \mathfrak{S}_4 \times C_2$ of order $48$ is the full automorphism group $\mathrm{Aut}(O_6)$ of the octahedron of six slices from `Theorem I.9.3a`, where the tetrahedral subgroup $W(D_3) = T_d \cong \mathfrak{S}_4$ preserves the charge $\kappa$ and permutes the four filled faces $T_+$ (precisely the four points of the scene $S_4 = \mathbb{F}_2^2$), the subgroup of proper rotations $W(B_3)^+ \cong \mathfrak{S}_4$ permutes the four main diagonals of the cube (opposite face pairs, reversing $\kappa$ on its $12$ odd rotations), while the central inversion $C_2 = \{\pm I_3\}$ swaps the four filled faces ($\kappa = 0$) and the four hollow holes ($\kappa = 1$), reversing the parity charge $\kappa \mapsto \kappa \oplus 1$;
3. next, we investigate non-abelian finite transport groups—the quaternion group $Q_8 \subset \mathrm{GL}_2(\mathbb{F}_3)$ and the projective quotient of the odd sector by the central inversion $\{\pm I_2\}$, writing out all $8$ matrices of $Q_8$, distinguishing left and right actions, and proving the non-splitting of the extension $Q_8 \twoheadrightarrow V_4$ in contrast to the split extension $W(B_3) \cong \mathfrak{S}_4 \times C_2$;
4. finally, we formulate the exact criterion for lifting and factoring a homomorphism (`Theorem II.4.2`) and demonstrate on the three-strand braid group $B_3$ why the homological abelianization $\mathbb{Z}$ loses the non-commutative memory of trajectory braiding.

---

## §II.4.1. Discrete Connection on the Window Graph, Loop Holonomy, and the Two-Window Möbius Band

Let us first fulfill the promise of `Table I.9.3` of Book I and give a rigorous definition of a discrete connection and a principal $G$-torsor on the overlap graph (or cell complex) of the observer's windows.

> **Definition II.4.1 (Discrete $G$-connection, parallel transport, curvature, and principal $G$-torsor).**  
> Let $\mathcal{K} = (V, E, F)$ be a connected two-dimensional cellular or simplicial complex (the nerve of a covering of the observer's windows), and let $G$ be a group (not necessarily abelian) with identity element $1_G$.
> 1. A *discrete $G$-connection* on the graph $(V, E)$ is an assignment to each oriented edge $e = (u \to v)$ of a transport element $\Omega(u \to v) = g_{vu} \in G$ satisfying the inversion condition under reversal of edge orientation:
>    $$
>    \Omega(v \to u) = \Omega(u \to v)^{-1} \qquad \bigl(g_{uv} = g_{vu}^{-1}\bigr).
>    $$
> 2. *Parallel transport* along an oriented path $\gamma = (v_0 \to v_1 \to \cdots \to v_k)$ is the path-ordered product of edge transitions:
>    $$
>    \mathrm{Hol}_\Omega(\gamma) = g_{v_k v_{k-1}} \cdots g_{v_2 v_1} g_{v_1 v_0} \in G.
>    $$
>    If the path $\gamma$ is closed ($v_k = v_0$), the element $\mathrm{Hol}_\Omega(\gamma) \in G$ is called the *holonomy (or monodromy)* of the connection $\Omega$ along the loop $\gamma$ based at $v_0$. If $\gamma = \partial f$ is the boundary of a two-dimensional cell $f \in F$, the holonomy $\mathrm{Curv}_\Omega(f) = \mathrm{Hol}_\Omega(\partial f)$ is called the *discrete curvature* of the connection on the face $f$. A connection is called *flat* on $\mathcal{K}$ if $\mathrm{Curv}_\Omega(f) = 1_G$ for all filled faces $f \in F$.
> 3. A *change of local frames* (gauge relabeling of windows) is a family of elements $h_v \in G$ ($v \in V$) transforming the connection according to the rule
>    $$
>    g'_{vu} = h_v\, g_{vu}\, h_u^{-1}.
>    $$
>    Under a change of local frames, the holonomy of a closed loop $\gamma$ based at vertex $v_0$ is conjugated by the element $h_{v_0}$:
>    $$
>    \mathrm{Hol}_{\Omega'}(\gamma) = h_{v_0}\,\mathrm{Hol}_\Omega(\gamma)\,h_{v_0}^{-1}.
>    $$
> 4. A *principal $G$-torsor (principal bundle)* $\mathcal{P}$ over the complex $\mathcal{K}$ associated with a flat connection $\Omega$ is a system of fibers $P_v$ ($v \in V$), on each of which the group $G$ acts freely and transitively on the right ($p \cdot g$), equipped with parallel identifications along edges $\tau_{vu} : P_u \xrightarrow{\sim} P_v$, $\tau_{vu}(p \cdot g) = \tau_{vu}(p)\cdot g$, that are compatible around all filled faces $f \in F$.

Let us see how this construction operates on the simplest example of a closed loop—the circle $S^1 = \mathbb{R}/2\pi\mathbb{Z}$ covered by two open arcs $U_+ = (-\frac{2\pi}{3}, \frac{2\pi}{3})$ and $U_- = (\frac{\pi}{3}, \frac{5\pi}{3})$. Each of the arcs $U_+$ and $U_-$ individually is contractible (having length $\frac{4\pi}{3} < 2\pi$), but their intersection splits into **two disjoint connected components** (two gluing windows):
$$
U_+ \cap U_- = W_{\mathrm{left}} \sqcup W_{\mathrm{right}}, \qquad W_{\mathrm{left}} = \left(\frac{\pi}{3}, \frac{2\pi}{3}\right), \quad W_{\mathrm{right}} = \left(-\frac{2\pi}{3}, -\frac{\pi}{3}\right) \equiv \left(\frac{4\pi}{3}, \frac{5\pi}{3}\right).
$$
The bipartite incidence graph between the two charts $\{U_+, U_-\}$ and the two overlap components $\{W_{\mathrm{left}}, W_{\mathrm{right}}\}$ is a cycle of four edges $C_4$ with Euler characteristic $\chi(S^1) = 2 - 2 = 0$ and first homology group $H_1(S^1; \mathbb{Z}) \cong \mathbb{Z}$.

Specify over $U_+$ and $U_-$ local fibers of binary phase $\{+1, -1\} \cong C_2$ (or a real fiber coordinate $t \in [-1, 1]$):
- in the left overlap window $W_{\mathrm{left}}$, impose the identity gluing $\Omega_{\mathrm{left}} = +1$ ($t_+ = t_-$);
- in the right overlap window $W_{\mathrm{right}}$, impose the sign-reversing gluing $\Omega_{\mathrm{right}} = -1$ ($t_+ = -t_-$).

Then in each of the two windows $U_+$ and $U_-$ individually the bundle is completely trivial, yet upon a full traversal of the loop $U_+ \xrightarrow{W_{\mathrm{left}}} U_- \xrightarrow{W_{\mathrm{right}}} U_+$, the holonomy of the connection equals
$$
\mathrm{Hol}_\Omega(S^1) = (+1)\cdot(-1) = -1 \ne +1.
$$
No change of frame signs $h_+ , h_- \in \{\pm 1\}$ in the charts $U_+, U_-$ can turn both twists into $+1$, because the product $(h_- (+1) h_+^{-1})(h_+ (-1) h_-^{-1}) = -1$ is independent of the choice of frames. For the real interval $[-1,1]$ this yields the classical non-orientable Möbius band, while for the discrete fiber $\{\pm 1\}$ it yields the connected double covering of the circle $\widetilde{S}^1 \xrightarrow{2:1} S^1$, in which returning to the initial phase $+1$ requires a **double** traversal of the base loop: $(-1)^2 = +1$.

> **Remark II.4.1 (Why arc length $< 2\pi$ is required in the two-window covering condition).**  
> If both arcs are expanded to full punctured circles of length $2\pi$ (for example, $U_+ = S^1 \setminus \{\pi\}$ and $U_- = S^1 \setminus \{0\}$), the intersection $U_+ \cap U_- = S^1 \setminus \{0, \pi\}$ still consists of two open semicircles $W_{\mathrm{upper}}$ and $W_{\mathrm{lower}}$, and the holonomy around $S^1$ equals $-1$. If, however, one takes arcs of length $\ge 2\pi$ covering the entire circle without punctures, the intersection ceases to split into two contractible components and Leray's theorem on computing cohomology from the nerve of a covering becomes inapplicable, because the charts themselves cease to be contractible.

---

## §II.4.2. The Observer's Octahedron $O_6$: The Weyl Group $W(B_3) \cong \mathfrak{S}_4 \times C_2$ as a Bridge Between $S_4$, $\mathcal{S}_w$, and Charge $\kappa$

Let us now link the theory of $G$-connections and symmetry groups directly to the constructions of Book I (`Theorem I.9.3` and `Theorem I.9.3a`).

Recall the structure of the nerve of six slices $\mathcal{N}(O_6)$ of the four-point scene $S_4 = \mathbb{F}_2^2 = \{00, 01, 10, 11\}$:
- the six vertices of the octahedron $O_6$ are placed in three-dimensional space $\mathbb{R}^3$ along the three coordinate axes and correspond to the six two-point slices of the three binary questions $X, C, B$:
  $$
  \begin{aligned}
  X_0 &= (+1, 0, 0), \quad & X_1 &= (-1, 0, 0), \\
  C_0 &= (0, +1, 0), \quad & C_1 &= (0, -1, 0), \\
  B_0 &= (0, 0, +1), \quad & B_1 &= (0, 0, -1);
  \end{aligned}
  $$
- the eight triangular faces of the octahedron $O_6$ (one in each octant $(\pm 1, \pm 1, \pm 1)$) are indexed by bit triples $(i, j, k) \in \mathbb{F}_2^3$ and carry the triple parity charge from `Chapter I.9`:
  $$
  \kappa(i, j, k) = i \oplus j \oplus k \in \mathbb{F}_2.
  $$
  The four even faces ($\kappa = 0$) correspond to the four points of the scene $S_4 = \{00, 01, 10, 11\}$ and are filled in the nerve $\mathcal{N}$, whereas the four odd faces ($\kappa = 1$) are hollow holes ($X_i \cap C_j \cap B_k = \varnothing$).

What is the full symmetry group of this object, and how does it act on the four-point scene $S_4$, the presheaf $\mathcal{S}_w$, and the parity charge $\kappa$?

> **Theorem II.4.1 (Theorem on the observer's octahedron: $W(B_3) \cong \mathfrak{S}_4 \times C_2 = \mathrm{Aut}(O_6)$, action on $S_4$, and inversion of the charge $\kappa$).**  
> *Classical foundation.* The isomorphism $W(B_3) \cong \mathfrak{S}_4 \times C_2 \cong \mathrm{Aut}(O_6)$ is a classical fact about the hyperoctahedral symmetry group of the cube and octahedron; signed edge labels and their inversion belong to the language of signed graphs and gain graphs (Harary, 1953; Zaslavsky, 1982–1989). *Contribution of this book:* Separation of the subgroup $W(D_3) \cong \mathfrak{S}_4$ (preserving charge $\kappa$ and the nerve $\mathcal{N}(O_6)$) from the proper rotation subgroup $W(B_3)^+ \cong \mathfrak{S}_4$ (preserving $\kappa$ on $A_4$ and inverting $\kappa$ on $12$ odd rotations).
> Let $W(B_3) \subset \mathrm{O}_3(\mathbb{Z})$ be the signed hyperoctahedral Weyl group (the group of all $3 \times 3$ integer monomial matrices having exactly one non-zero entry $\pm 1$ in each row and each column).
> 1. The group $W(B_3)$ has order $3! \cdot 2^3 = 6 \cdot 8 = 48$ and coincides with the full group of combinatorial automorphisms $\mathrm{Aut}(O_6)$ of the graph of the octahedron of six slices (mapping antipodal pairs of vertices $\{X_0, X_1\}, \{C_0, C_1\}, \{B_0, B_1\}$ to antipodal pairs).
> 2. The four even faces of the octahedron ($\kappa = 0$), corresponding to the four points of the scene $S_4 = \{00, 01, 10, 11\}$, form in $\mathbb{R}^3$ the vertices of a regular inscribed tetrahedron $T_+$, while the four hollow holes ($\kappa = 1$) form the vertices of the dual antipodal tetrahedron $T_- = -T_+$. The four pairs of opposite faces of the octahedron $\{(i,j,k), (i\oplus 1, j\oplus 1, k\oplus 1)\}$ stand in one-to-one correspondence with the four points of the scene $S_4$.
> 3. Every element $M = P_\pi D_\varepsilon \in W(B_3)$ factors uniquely into an axis-permutation matrix $P_\pi$ ($\pi \in \mathfrak{S}_3$, $\det P_\pi = \mathrm{sgn}(\pi)$) and a diagonal sign matrix $D_\varepsilon = \mathrm{diag}(\varepsilon_1, \varepsilon_2, \varepsilon_3)$ ($\varepsilon_r \in \{\pm 1\}$). Inside $W(B_3)$, two distinct subgroups of order $24$ isomorphic to $\mathfrak{S}_4$ act as follows:
>    - **the charge- and nerve-preserving subgroup** $W(D_3) = T_d = \{P_\pi D_\varepsilon \in W(B_3) : \det D_\varepsilon = +1\}$ preserves the parity charge $\kappa = i \oplus j \oplus k$ (mapping filled faces $T_+$ to $T_+$ and hollow holes $T_-$ to $T_-$) and acts faithfully on the four points of the scene $S_4 \cong T_+$ as the full symmetric group:
>      $$
>      W(D_3) = \mathrm{Aut}(\mathcal{N}(O_6)) \cong \mathfrak{S}_4 = \mathrm{Sym}(S_4);
>      $$
>    - **the proper rotation subgroup** $W(B_3)^+ = \{M \in W(B_3) : \det M = \mathrm{sgn}(\pi)\det D_\varepsilon = +1\} \cong \mathfrak{S}_4$ acts faithfully by all $24$ permutations on the **four main diagonals of the cube** (the four pairs of opposite faces), preserving the charge $\kappa$ on the $12$ even tetrahedral rotations $A_4 = W(B_3)^+ \cap W(D_3)$ and **reversing the charge $\kappa \mapsto \kappa \oplus 1$** on the $12$ odd rotations $W(B_3)^+ \setminus A_4$ (such as $90^\circ$ turns about the coordinate axes).
> 4. The central spatial inversion $z_0 = -I_3 \in W(B_3)$ ($\det(-I_3) = \det D_{-I_3} = -1$) swaps each vertex with its antipode ($X_0 \leftrightarrow X_1$, $C_0 \leftrightarrow C_1$, $B_0 \leftrightarrow B_1$), leaves each of the $4$ pairs of opposite faces in place, yet **reverses the parity charge of all eight faces**:
>    $$
>    \kappa(-I_3 \cdot (i, j, k)) = (i\oplus 1) \oplus (j\oplus 1) \oplus (k\oplus 1) = \kappa(i, j, k) \oplus 1,
>    $$
>    swapping the four filled faces $T_+$ and the four hollow holes $T_-$. Since $-I_3 \notin W(D_3)$ and $-I_3 \notin W(B_3)^+$, the group $W(B_3)$ admits two canonical direct-product decompositions:
>    $$
>    W(B_3) = W(D_3) \times \{\pm I_3\} = W(B_3)^+ \times \{\pm I_3\} \cong \mathfrak{S}_4 \times C_2.
>    $$
> 5. The presheaf of local gauges $\mathcal{S}_w$ from `Theorem I.9.3a` is a principal $\mathbb{F}_2$-torsor over the nerve $\mathcal{N}(O_6)$ associated with the flat $\mathbb{F}_2$-connection $\Omega_w(e) = (-1)^{w(e)} \in \{\pm 1\} \cong C_2$, whose holonomy equals $+1$ around all four filled faces ($\kappa = 0$) and $-1$ around all four hollow holes ($\kappa = 1$).

**Proof.**  
1. Every automorphism of the octahedron graph $O_6$ must preserve graph distances: each vertex has exactly one vertex at distance $2$ (its antipode along the same axis) and four neighbors at distance $1$. Therefore, every automorphism permutes the three antipodal axis pairs $\{X_0, X_1\}, \{C_0, C_1\}, \{B_0, B_1\}$ ($3! = 6$ ways) and independently chooses the orientation within each of the three pairs ($2^3 = 8$ ways), which yields precisely the group of $3 \times 3$ signed monomial matrices $W(B_3)$ of order $6 \cdot 8 = 48$.

2–4. On the set of eight octants $\mathbb{F}_2^3 = \{(i,j,k)\}$, a matrix $M = P_\pi D_\varepsilon$ acts by permuting coordinates via $\pi \in \mathfrak{S}_3$ (which preserves $i \oplus j \oplus k$) and adding modulo $2$ the sign-flip bit vector $\delta(\varepsilon) \in \mathbb{F}_2^3$, where $(-1)^{\delta_1 \oplus \delta_2 \oplus \delta_3} = \det D_\varepsilon$. Hence the parity charge $\kappa(i,j,k) = i \oplus j \oplus k$ is preserved if and only if $\det D_\varepsilon = +1$, singling out the tetrahedral subgroup $W(D_3) = T_d$ of order $6 \cdot 4 = 24$ ($12$ even proper rotations with $\mathrm{sgn}(\pi) = \det D_\varepsilon = +1$ and $12$ improper reflections/rotoreflections with $\mathrm{sgn}(\pi) = -1, \det D_\varepsilon = +1$), which acts faithfully by all $24$ permutations on the four vertices of $T_+ \cong S_4$. Meanwhile, the matrix determinant equals $\det M = \mathrm{sgn}(\pi)\det D_\varepsilon$: inside the proper rotation subgroup $W(B_3)^+$ ($\det M = +1$), the condition $\mathrm{sgn}(\pi) = -1$ forces $\det D_\varepsilon = -1$, so the $12$ odd rotations of the cube reverse $\kappa \mapsto \kappa \oplus 1$ ($T_+ \leftrightarrow T_-$), whereas the action of $W(B_3)$ on the four main diagonals of the cube has kernel $\{\pm I_3\}$ and restricts to a bijection $W(B_3)^+ \xrightarrow{\sim} \mathfrak{S}_4$. Since the central inversion $-I_3$ has both $\det D_{-I_3} = -1$ and $\det(-I_3) = -1$, the intersections $W(D_3) \cap \{\pm I_3\} = W(B_3)^+ \cap \{\pm I_3\} = \{+I_3\}$ are trivial, yielding both direct products $W(B_3) = W(D_3) \times \{\pm I_3\} = W(B_3)^+ \times \{\pm I_3\} \cong \mathfrak{S}_4 \times C_2$.

5. On each edge $e \in E(\mathcal{N})$, the condition $(g_u, g_v) \in \mathcal{S}_w(e) \iff g_v - g_u = w(e) \pmod 2$ defines the parallel transport $\tau_{vu}(g_u) = g_u \oplus w(e)$ with structure group $G = \mathbb{F}_2 \cong C_2$. By `Theorem II.3.1`, the sum of weights $w$ equals $0 \pmod 2$ on all filled faces ($\kappa = 0$) and $1 \pmod 2$ around all hollow holes ($\kappa = 1$), proving item 5. $\blacksquare$

> **Important Structural Corollary (Two distinct index-$2$ subgroups in $W(B_3)$).**  
> Inside the group $W(B_3)$ of order $48$, there are two geometrically distinct subgroups of index $2$ (of order $24$) that must not be conflated:
> - **the group of proper rotations of the cube and octahedron** $W(B_3)^+ = \{ M \in W(B_3) : \det M = +1 \} \cong \mathfrak{S}_4$ (which does not contain $-I_3$ and permutes all $4$ pairs of opposite faces as $\mathfrak{S}_4$);
> - **the parity-charge-preserving group** (the subgroup $W(D_3) \subset W(B_3)$ in which the number of coordinate sign flips is even, so that $\kappa(i,j,k) = i\oplus j\oplus k$ is invariant)—it is also isomorphic to $\mathfrak{S}_4$ (acting by all $24$ permutations on the $4$ filled faces $T_+ \cong S_4$);
> - whereas the third index-$2$ subgroup—the **pyritohedral group** $T_h = A_4 \times \{\pm I_3\} \cong A_4 \times C_2$ (even permutations of the axes with arbitrary sign flips)—contains $-I_3$ but realizes only even permutations $A_4$ on the main diagonals.

---

## §II.4.3. The Non-Abelian Quaternion Group $Q_8 \subset \mathrm{GL}_2(\mathbb{F}_3)$, the Quotient by $\{\pm I_2\}$, and the Non-Split Extension $Q_8 \twoheadrightarrow V_4$

In `Theorem II.4.1`, the extension $1 \to C_2 \to W(B_3) \to \mathfrak{S}_4 \to 1$ turned out to be **split**: inside $W(B_3)$ there was a subgroup $W(B_3)^+ \cong \mathfrak{S}_4$ projecting isomorphically onto the quotient group. One naturally asks: does every central extension with fiber $C_2 = \{\pm I\}$ split and allow the observer to choose a global group-theoretic section?

A negative answer is provided by the famous non-abelian quaternion group $Q_8 = \{\pm 1, \pm \mathbf{i}, \pm \mathbf{j}, \pm \mathbf{k}\}$ of order $8$, which is naturally realized inside the general linear group $\mathrm{GL}_2(\mathbb{F}_3)$ over the three-element field $\mathbb{F}_3 = \{0, 1, 2\} \equiv \{0, +1, -1\}$.

Let us write out explicitly the matrices of the generators $\mathbf{I}, \mathbf{J}, \mathbf{K} \in \mathrm{SL}_2(\mathbb{F}_3) \subset \mathrm{GL}_2(\mathbb{F}_3)$:
$$
\mathbf{I} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \equiv \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}, \qquad
\mathbf{J} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad
\mathbf{K} = \mathbf{I}\mathbf{J} = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix} \equiv \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \pmod 3.
$$
Let us verify that all $8$ matrices of the subgroup $Q_8 = \{ \pm I_2, \pm \mathbf{I}, \pm \mathbf{J}, \pm \mathbf{K} \} \subset \mathrm{SL}_2(\mathbb{F}_3)$ are **pairwise distinct** over the field $\mathbb{F}_3$ ($-1 \equiv 2 \ne 1 \pmod 3$) and satisfy Hamilton's relations $\mathbf{I}^2 = \mathbf{J}^2 = \mathbf{K}^2 = \mathbf{I}\mathbf{J}\mathbf{K} = -I_2$:

#### Table II.4.1. All $8$ Pairwise Distinct Matrices of the Quaternion Group $Q_8 \subset \mathrm{SL}_2(\mathbb{F}_3)$ and Their Projection to $V_4 = Q_8 / \{\pm I_2\}$

| Element $q \in Q_8$ | Matrix in $\mathrm{SL}_2(\mathbb{F}_3)$ (in residues $\{0,1,2\}$) | Square $q^2 \pmod 3$ | Element order | Class in quotient $Q_8 / \{\pm I_2\} \cong V_4$ |
| :---: | :---: | :---: | :---: | :---: |
| $+1$ | $I_2 = \bigl(\begin{smallmatrix} 1 & 0 \\ 0 & 1 \end{smallmatrix}\bigr)$ | $+I_2$ | $1$ | $\bar{1} = (0,0)$ |
| $-1$ | $-I_2 = \bigl(\begin{smallmatrix} 2 & 0 \\ 0 & 2 \end{smallmatrix}\bigr)$ | $+I_2$ | $2$ | $\bar{1} = (0,0)$ |
| $+\mathbf{i}$ | $+\mathbf{I} = \bigl(\begin{smallmatrix} 0 & 2 \\ 1 & 0 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{i}} = (1,0)$ |
| $-\mathbf{i}$ | $-\mathbf{I} = \bigl(\begin{smallmatrix} 0 & 1 \\ 2 & 0 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{i}} = (1,0)$ |
| $+\mathbf{j}$ | $+\mathbf{J} = \bigl(\begin{smallmatrix} 1 & 1 \\ 1 & 2 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{j}} = (0,1)$ |
| $-\mathbf{j}$ | $-\mathbf{J} = \bigl(\begin{smallmatrix} 2 & 2 \\ 2 & 1 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{j}} = (0,1)$ |
| $+\mathbf{k}$ | $+\mathbf{K} = \bigl(\begin{smallmatrix} 2 & 1 \\ 1 & 1 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{k}} = (1,1)$ |
| $-\mathbf{k}$ | $-\mathbf{K} = \bigl(\begin{smallmatrix} 1 & 2 \\ 2 & 2 \end{smallmatrix}\bigr)$ | $-I_2$ | $4$ | $\bar{\mathbf{k}} = (1,1)$ |

On the $8$ non-zero vectors of the plane $S_{\mathrm{odd}} = \mathbb{F}_3^2 \setminus \{(0,0)\}$, the group $Q_8$ acts freely and transitively:
- under the **left action** $q \cdot v$, choosing any reference vector $v_0 \in S_{\mathrm{odd}}$ (for instance, $v_0 = (1,0)^{\mathsf{T}}$) defines a bijection $Q_8 \xrightarrow{\sim} S_{\mathrm{odd}}$, $q \mapsto q v_0$, turning $S_{\mathrm{odd}}$ into a left principal $Q_8$-torsor;
- under the **right action** $v^{\mathsf{T}} \cdot q$, the multiplication order is reversed ($(q_1 q_2)^{-1} = q_2^{-1} q_1^{-1}$), which corresponds to quaternion conjugation $q \mapsto \bar{q}$;
- upon taking the quotient of $S_{\mathrm{odd}}$ by the central sign subgroup $\{\pm I_2\}$, one obtains the $4$-element projective line $\mathbb{P}^1(\mathbb{F}_3) = S_{\mathrm{odd}} / \{\pm I_2\}$, on which the quotient group $Q_8 / \{\pm I_2\} \cong V_4 \cong \mathbb{F}_2^2$ (the Klein four-group, isomorphic under addition to our four-point scene $S_4$) acts freely and transitively as an abelian $V_4$-torsor.

> **Proposition II.4.1 (Non-splitting of the extension $1 \to \{\pm I_2\} \to Q_8 \to V_4 \to 1$ and spectral distinction of involutions in $W(B_3)$, $\mathrm{GL}_2(\mathbb{F}_3)$, and $Q_8$).**  
> *Classical foundation.* Hamilton's quaternion group $Q_8$ (1843) and the cohomological non-splitting of the central extension $1 \to C_2 \to Q_8 \to V_4 \to 1$. *Contribution of this book:* Absence of a homomorphic section of quarter-turns over the Klein four-group $V_4$ ($|\mathcal{R}| = 0$) and triple spectral separation of $W(B_3)$, $\mathrm{GL}_2(\mathbb{F}_3)$, and $Q_8$ by elements of orders $2$ and $4$.
> 1. The short exact sequence of groups
>    $$
>    1 \longrightarrow \{\pm I_2\} \longrightarrow Q_8 \xrightarrow{\;\pi\;} V_4 \longrightarrow 1
>    $$
>    **does not split**: there exists no group homomorphism $s : V_4 \to Q_8$ such that $\pi \circ s = \mathrm{id}_{V_4}$. Every set-theoretic section $s : V_4 \to Q_8$ inevitably has non-trivial multiplicative curvature (a $2$-cocycle $\beta(a, b) = s(a)s(b)s(a+b)^{-1} \in \{\pm I_2\}$), because all three non-trivial elements of $V_4$ have order $2$, whereas all $6$ preimages $\pm \mathbf{I}, \pm \mathbf{J}, \pm \mathbf{K}$ in $Q_8$ have order $4$ and square to $-I_2 \ne +I_2$.
> 2. Counting the number of elements of order $2$ (involutions $g^2 = I, g \ne I$) yields a strict invariant ruling out false isomorphisms among the three transport groups:
>    - in the octahedron symmetry group $W(B_3)$ of order $48$, there are exactly **$19$ involutions** ($1$ central inversion $-I_3$, $3+3=6$ reflections and half-turns of axes without coordinate permutation, and $6 \times 2 = 12$ transpositions of axis pairs with matched signs);
>    - in the general linear group $\mathrm{GL}_2(\mathbb{F}_3)$ of order $48$, there are exactly **$13$ involutions** ($1$ central matrix $-I_2$ of determinant $+1$ and $12$ reflections of trace $0$ and determinant $-1$);
>    - in the quaternion group $Q_8$ of order $8$, there is exactly **$1$ involution** (the unique central element $-I_2$).
>    Since the numbers $19, 13, 1$ are pairwise distinct, the groups $W(B_3)$ and $\mathrm{GL}_2(\mathbb{F}_3)$ (despite having identical orders $|W(B_3)| = |\mathrm{GL}_2(\mathbb{F}_3)| = 48$) **are not isomorphic**, and $Q_8$ contains no subgroup isomorphic to $V_4$.

**Proof.**  
1. If there existed a homomorphism $s : V_4 \to Q_8$ with $\pi \circ s = \mathrm{id}_{V_4}$, then for the non-zero element $\bar{\mathbf{i}} \in V_4$ its image $s(\bar{\mathbf{i}}) \in \{\pm \mathbf{I}\}$ would satisfy $s(\bar{\mathbf{i}})^2 = s(2\bar{\mathbf{i}}) = s(0) = +I_2$, whereas $(\pm \mathbf{I})^2 = -I_2 \ne +I_2$.
2. Direct classification of conjugacy classes of order-$2$ matrices in $W(B_3) \subset \mathrm{O}_3(\mathbb{Z})$ and in $\mathrm{GL}_2(\mathbb{F}_3)$ by their characteristic polynomials $(x-1)(x+1) = x^2 - 1$ and $(x+1)^2$ yields $19$, $13$, and $1$ involutions, respectively. Since any group isomorphism preserves the number of elements of each order, the pairwise distinctness of $19, 13, 1$ rules out any isomorphism. $\blacksquare$

---

## §II.4.4. Criterion for Factoring a Homomorphism and the Non-Abelian Braid Group $B_3$ versus Its Abelianization $\mathbb{Z}$

Let us generalize the obstruction of §II.4.3 to a general algebraic rule for descending and lifting group representations of a loop, removing the logical imprecision of earlier draft formulations.

> **Theorem II.4.2 (Algebraic criterion for factoring through an epimorphism and loss of non-commutative memory under abelianization of the braid group $B_3$).**  
> *Classical foundation.* Item 1 is the classical universal property of a quotient group (homomorphism theorem); the abelianization $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ is a classical fact about Artin's braid group (1925). *Contribution of this book:* Reading abelianization as the loss of noncommutative memory of permutation order.
> 1. **(Universal property of a quotient group).** Let $p : G \twoheadrightarrow \overline{G}$ be a surjective group homomorphism with kernel $N = \ker p \trianglelefteq G$, and let $f : G \to H$ be a group homomorphism. The homomorphism $f$ factors through $p$ (meaning that there exists a unique group homomorphism $\bar{f} : \overline{G} \to H$ satisfying $f = \bar{f} \circ p$) **if and only if** the kernel of the projection is annihilated by the map $f$:
>    $$
>    \ker p \subseteq \ker f \quad \bigl(\text{that is, } f(n) = 1_H \text{ for all } n \in \ker p\bigr).
>    $$
>    Conversely, if there exists at least one element $n \in \ker p$ that the observer in $H$ distinguishes from the identity ($f(n) \ne 1_H$), then no map $\bar{f} : \overline{G} \to H$ can satisfy the relation $f = \bar{f} \circ p$.
> 2. **(The three-strand braid group $B_3$ and its homological blindness).** Let $B_3$ be Artin's braid group on three strands, presented by the generators $\sigma_1, \sigma_2$ (crossings of adjacent strands) and the Yang–Baxter (braid) relation
>    $$
>    B_3 = \langle \sigma_1, \sigma_2 \mid \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \rangle.
>    $$
>    The substitution $x = \sigma_1 \sigma_2 \sigma_1$ and $y = \sigma_1 \sigma_2$ defines an isomorphism $B_3 \cong \langle x, y \mid x^2 = y^3 \rangle$ (the trefoil knot group), since $\sigma_1 = y^{-1} x$ and $\sigma_2 = x^{-1} y^2$.
>    Then:
>    - upon passing to the abelianization $p_{\mathrm{ab}} : B_3 \twoheadrightarrow B_3^{\mathrm{ab}} = B_3 / [B_3, B_3]$, the relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2$ in additive notation $(2\bar{\sigma}_1 + \bar{\sigma}_2) - (\bar{\sigma}_1 + 2\bar{\sigma}_2) = \bar{\sigma}_1 - \bar{\sigma}_2 = 0$ identifies the two generators ($\bar{\sigma}_1 = \bar{\sigma}_2$), and the Smith normal form of the relation matrix $(1, -1)$ yields the infinite cyclic group
>      $$
>      B_3^{\mathrm{ab}} \cong \mathbb{Z}, \qquad p_{\mathrm{ab}}(\sigma_1^{a_1} \sigma_2^{b_1} \cdots) = \sum (a_i + b_i) \in \mathbb{Z}
>      $$
>      (the algebraic crossing number, or linking number, modulo sign from `Chapter II.3`);
>    - in the non-abelian group $B_3$ itself, however, the elements $\sigma_1$ and $\sigma_2$ do not commute: under the standard epimorphism onto the permutation group of the three strands $f : B_3 \twoheadrightarrow \mathfrak{S}_3$, $\sigma_1 \mapsto (12)$, $\sigma_2 \mapsto (23)$, the commutator element $c = \sigma_1 \sigma_2^{-1} \in \ker p_{\mathrm{ab}}$ ($p_{\mathrm{ab}}(c) = 1 - 1 = 0$) maps to a cycle of length $3$:
>      $$
>      f(\sigma_1 \sigma_2^{-1}) = (12)(23) = (123) \ne \mathrm{id}_{\mathfrak{S}_3},
>      $$
>      while the elements $\sigma_1^3$ and $\sigma_1 \sigma_2 \sigma_1$, having the same exponent weight $p_{\mathrm{ab}}(\sigma_1^3) = p_{\mathrm{ab}}(\sigma_1 \sigma_2 \sigma_1) = 3$, map to distinct permutations $(12)^3 = (12)$ and $(12)(23)(12) = (13)$. Consequently, $\ker p_{\mathrm{ab}} \not\subseteq \ker f$, and even the finite permutation of strand endpoints $\mathfrak{S}_3$ cannot be recovered from the abelian homology $B_3^{\mathrm{ab}} \cong \mathbb{Z}$.

**Proof.**  
1. If $f = \bar{f} \circ p$, then for any $n \in \ker p$ we have $f(n) = \bar{f}(p(n)) = \bar{f}(1_{\overline{G}}) = 1_H$, so $\ker p \subseteq \ker f$. Conversely, if $\ker p \subseteq \ker f$, then on each coset $g \ker p$ the value $f(gn) = f(g)f(n) = f(g)$ is constant, and setting $\bar{f}(p(g)) = f(g)$ yields a well-defined group homomorphism $\bar{f} : \overline{G} \to H$, unique by the surjectivity of $p$.
2. In the group $\langle x, y \mid x^2 = y^3 \rangle$, set $\sigma_1 = y^{-1}x$ and $\sigma_2 = x^{-1}y^2$; then $\sigma_1 \sigma_2 = y^{-1} y^2 = y$ and $\sigma_1 \sigma_2 \sigma_1 = y(y^{-1}x) = x$, while the relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 \iff x = (x^{-1}y^2)x \iff x^2 = y^3$. In the abelianization $\mathbb{Z}^2 / \operatorname{Im}\binom{2}{-3}$, the relation matrix $R = (2, -3)^{\mathsf{T}}$ has $\gcd(2, -3) = 1$ and Smith normal form $(1, 0)^{\mathsf{T}}$ (since $\bigl(\begin{smallmatrix} 1 & 1 \\ 3 & 2 \end{smallmatrix}\bigr)\binom{2}{-3} = \binom{-1}{0}$), whence the quotient group is free of rank $2 - 1 = 1$: $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ with generator $p_{\mathrm{ab}}(\sigma_1) = p_{\mathrm{ab}}(\sigma_2) = 1$. Meanwhile, in $\mathfrak{S}_3$ we have $(12)(23)(12) = (13) = (23)(12)(23)$, so $f : B_3 \twoheadrightarrow \mathfrak{S}_3$ is a well-defined homomorphism, yet $f(\sigma_1 \sigma_2^{-1}) = (123) \ne \mathrm{id}$, whereas $p_{\mathrm{ab}}(\sigma_1 \sigma_2^{-1}) = 0$. $\blacksquare$

---

## §II.4.5. Historical-Philosophical Parallel: The Standpoint *Naya* and the Danger of Unconditional Descent (*Sanmati-tarka*)

In the classical Jaina logic of many-sidedness (*anekāntavāda*), systematized by Siddhasena Divākara in his treatise *Sanmati-tarka* (`I.1–28`), a precise distinction is drawn between *naya* (a legitimate partial standpoint from which an object is examined under a fixed epistemic commitment) and *durnaya / nayābhāsa* (a pseudo-standpoint that arises the moment a single partial slice is declared exhaustive of the whole and blindly extended to properties lying in the kernel of its projection).

In the mathematical structure of `Theorem II.4.2` (outside the deductive premises of the proofs), this distinction receives a transparent operational meaning:
- the abelian projection $p_{\mathrm{ab}} : B_3 \twoheadrightarrow \mathbb{Z}$ (or the projection $Q_8 \twoheadrightarrow V_4$ modulo $\{\pm I_2\}$) is completely legitimate for those questions $f$ that are constant on the kernel $\ker p$ (for instance, counting the net number of half-twists of a braid);
- an error arises precisely when the observer forgets the condition $\ker p \subseteq \ker f$ and attempts to recover from the abelian winding number the non-commutative strand permutation $f(\sigma_1 \sigma_2^{-1}) = (123)$, or attempts to globally split the quaternion spinor sign $\{\pm I_2\}$ over $V_4$.

---

## §II.4.6. Chapter Summary and Bridge to Chapter II.5

The table below summarizes the results of `Chapter II.4` on parallel transport and holonomy.

#### Table II.4.2. Non-Abelian Loop Memory, Connection, and Symmetries of the Observer's Octahedron in Chapter II.4

| Object and problem of the observer | Construction in `Chapter II.4` | Key invariant and theorem |
| :--- | :--- | :--- |
| Parallel transport between windows | Discrete $G$-connection $\Omega(u\to v) = g_{vu} \in G$ and principal $G$-torsor | Conjugation of holonomy under frame change $\mathrm{Hol}_{\Omega'}(\gamma) = h_{v_0}\mathrm{Hol}_\Omega(\gamma)h_{v_0}^{-1}$ (`Def. II.4.1`) |
| Two-window covering of the circle $S^1$ | Intersection $U_+ \cap U_- = W_{\mathrm{left}} \sqcup W_{\mathrm{right}}$ of $2$ components | Holonomy $(+1)(-1) = -1$ yields the Möbius band and double covering (`§II.4.1`) |
| Symmetries of the checkerboard octahedron $O_6$ on the scene $S_4$ (`Theorem I.9.3a`) | Weyl group $W(B_3) \cong \mathfrak{S}_4 \times C_2$ of order $48$ | $W(D_3) \cong \mathfrak{S}_4$ preserves $\kappa$ and permutes the $4$ points of $S_4$; $W(B_3)^+ \cong \mathfrak{S}_4$ permutes the $4$ diagonals; $-I_3$ reverses $\kappa \mapsto \kappa \oplus 1$ (`Theorem II.4.1`) |
| Quaternion transport over $\mathbb{F}_3$ | Subgroup $Q_8 \subset \mathrm{SL}_2(\mathbb{F}_3)$ and quotient $S_{\mathrm{odd}} / \{\pm I_2\} \cong \mathbb{P}^1(\mathbb{F}_3)$ | Extension $Q_8 \twoheadrightarrow V_4$ does not split; involution counts $19, 13, 1$ are pairwise distinct (`Prop. II.4.1`) |
| Descent of a representation through a quotient $p : G \twoheadrightarrow \overline{G}$ | Criterion $\ker p \subseteq \ker f$ and braid group $B_3 \cong \langle x, y \mid x^2 = y^3 \rangle$ | $\mathrm{SNF}$ gives $B_3^{\mathrm{ab}} \cong \mathbb{Z}$, yet $\sigma_1 \sigma_2^{-1} \in \ker p_{\mathrm{ab}}$ gives $(123) \ne \mathrm{id}$ in $\mathfrak{S}_3$ (`Theorem II.4.2`) |

In `Chapter II.4`, we dropped commutativity of multiplication ($ab \ne ba$ in $W(B_3)$, $Q_8$, and $B_3$), but the law of path composition itself remained **associative**: $(ab)c = a(bc)$. Yet already in Book I (`Chapter I.6`), on the seven non-zero vectors of the three-bit charge space $\mathbb{F}_2^3 \setminus \{0\}$, there arose the projective Fano plane $\mathrm{PG}(2, \mathbb{F}_2)$ of $7$ points and $7$ lines. What happens if we define multiplication of basis directions along the seven lines of the Fano plane and equip them with a signed cocycle? We then take the next step from `Table I.9.3`—stepping beyond associativity into the world of alternative octonion algebras, the Paige loop of order $120$, and the Cayley–Dickson doubling tower. This is the subject of **Chapter `II.5`**.

---

## Summary Passport of Chapter II.4 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `§II.4.1` and `Theorem II.4.1` | Holonomy of the two-window Möbius band and exhaustive enumeration of $W(B_3) = \mathrm{Aut}(O_6)$ of order $48$: $W(D_3) \cong \mathfrak{S}_4$ preserves $\kappa$, $W(B_3)^+ \cong \mathfrak{S}_4$ permutes the $4$ cube diagonals ($12$ even + $12$ $\kappa$-reversing), and $-I_3$ reverses $\kappa \mapsto \kappa \oplus 1$ | `GATE-II04-01` |
| `Table II.4.1` and `Proposition II.4.1` | Pairwise distinctness of the $8$ matrices of $Q_8 \subset \mathrm{SL}_2(\mathbb{F}_3)$, free action on $S_{\mathrm{odd}}$, quotient by $\{\pm I_2\}$, absence of a section $V_4 \to Q_8$, and involution counts $19, 13, 1$ | `GATE-II04-02` |
| `Theorem II.4.2` | Verification of the presentation isomorphism $B_3 \cong \langle x, y \mid x^2 = y^3 \rangle$, computation of $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ via Smith normal form, and non-triviality of the image of $\sigma_1 \sigma_2^{-1}$ in $\mathfrak{S}_3$ | `GATE-II04-03` |
