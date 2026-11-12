# Chapter II.8. Cells, Limits, Variational Flows, and Rational `SOS` Certificates on Fano Flags

In `Chapters II.3–II.7`, we studied obstructions to global assembly and the geometry of questions on a **single fixed** finite complex—the nerve of six slices of the octahedron $O_6$, the triangulation of the projective plane $\mathbb{R}P^2$, the Fano plane $\mathrm{PG}(2, \mathbb{F}_2)$, or a finite system of quantum contexts. Now we turn to the fourth enrichment from `Table I.9.3` of Book I and ask how the observer works with a **sequence of refined cellular meshes** $K_h$ ($h \to 0$) and polynomial Lyapunov functionals defined on them:

> **Suppose you have computed something on a mesh of a thousand cells. Can you assert the same for an infinitely fine mesh as $h \to 0$? How do vertex values on a nerve graph (such as the octahedron $O_6$) spontaneously split into two levels while conserving their sum? And how can one prove the non-negativity of a polynomial on the unit sphere rigorously—without floating-point rounding and without gaps between mesh nodes?**

The present chapter answers this question in four steps:
1. we strictly separate **five distinct mathematical levels** of cellular approximation, which in applied literature are routinely conflated into the single unsubstantiated claim "computed on a mesh—hence proved in the limit";
2. using piecewise-linear Whitney differential forms $W_k$ and the de Rham simplex reading operator $R_k$, we prove the exact cellular identities $R_k W_k = \mathrm{id}_{C^k}$ and $d W_k = W_{k+1} \delta_k$, and show why under mesh subdivision $K' \to K$ the induced map $s^*$ defines an isomorphism of simplicial cohomology $H^\bullet(K; R) \xrightarrow{\sim} H^\bullet(K'; R)$, even though the pointwise reconstruction $W_k R_k \omega$ differs from a smooth form $\omega$ by $O(h)$;
3. on an arbitrary finite graph (and in particular on the graph of our octahedron of six slices $O_6$), we construct the **semi-discrete Cahn–Hilliard gradient flow**
   $$
   \dot{u} = -M\, L\,\bigl(\gamma L u + F'(u)\bigr),
   $$
   where $L = D_1^{\mathsf{T}} D_1 \succeq 0$ is the combinatorial graph Laplacian, $M > 0$ is the mobility (transport coefficient), and $\gamma > 0$ is the gradient (edge) penalty coefficient (we denote it by $\gamma$, keeping the symbol $\kappa = x_0 \oplus c_0 \oplus b_0$ reserved exclusively for the parity charge of Book I), and we prove the strict decrease of the Lyapunov functional $\frac{dE_h}{dt} = -M\,\mu^{\mathsf{T}} L \mu \le 0$ together with exact conservation of the sum of vertex values $\mathbf{1}^{\mathsf{T}}\dot{u} = 0$, describing spontaneous two-level value splitting $u_v \to \pm 1$;
4. finally, for high-degree polynomials, we replace grid sampling with exact rational sum-of-squares certificates (`SOS`, the factorization $G = L D L^{\mathsf{T}}$ in `Rational{BigInt}`) and apply this method to the **$21$-dimensional flag space of the Fano plane** $\mathbb{Q}^{21}$ carrying the affine-monomial symmetry group $\mathrm{AGL}_3(\mathbb{F}_2) = \mathbb{F}_2^3 \rtimes \mathrm{GL}_3(\mathbb{F}_2)$ of order $1344 = 8 \cdot 168$, proving the invariant decomposition of the cubic Veronese space $\dim \mathrm{Sym}^3(\mathbb{Q}^{21}) = 1771 = 84 + 1687$.

---

## §II.8.1. Five Levels of Transition from a Finite Cell to the Continuous Limit

Let us first formulate the methodological principle that protects the observer from substituting a finite mesh computation for an analytic theorem.

When an investigator replaces a smooth domain $\Omega \subset \mathbb{R}^n$ with a family of triangulations (simplicial meshes) $K_h$ having maximum simplex diameter $h = \max_{\tau \in K_h} \mathrm{diam}(\tau)$, letting $h \to 0$ by itself (and all the more so merely increasing the number of vertices $N \to \infty$ in one part of the domain) does not yet guarantee convergence of any kind. Between an identity on a single finite mesh and a theorem on the continuous limit lie **five strictly distinct mathematical levels**:

1. **Level 1 (Exact combinatorial-algebraic identity on a single fixed mesh $K_h$).** This level includes the boundary identity $\partial_{k-1}\partial_k = 0$ and coboundary identity $\delta_{k+1}\delta_k = 0$ (`Chapter II.3`), the positive semidefiniteness of the combinatorial Laplacian $L = D_1^{\mathsf{T}} D_1 \succeq 0$, and conservation laws on a single mesh. These properties hold for every $h > 0$ without any analytic assumptions whatsoever.
2. **Level 2 (Uniform shape regularity of cells and $h$-uniform a priori bound).** As $h \to 0$, the simplices of the mesh $K_h$ must not degenerate into flat "needles" (the ratio of simplex diameter to inscribed ball radius must remain uniformly bounded: $h_\tau / \rho_\tau \le \sigma_0 < \infty$; otherwise interpolation constants blow up as $\sin^{-1}\theta_{\min} \to \infty$, as in Schwarz's classical lantern counterexample), and the discrete solutions $u_h$ must satisfy a uniform energy bound $\|u_h\|_{V_h} \le C$ independent of $h$.
3. **Level 3 (Compactness and embedding into a common comparison function space).** To compare solutions $u_h$ living on different meshes $K_h$, the observer must specify a reconstruction (embedding) operator $W_h : V_h \to \mathcal{V}$ into a single Banach or Sobolev space $\mathcal{V}$ and prove precompactness of the family $\{W_h u_h\}_{h>0}$ (extraction of a subsequence $W_{h_j} u_{h_j} \rightharpoonup u^*$ in an explicitly declared weak or strong topology).
4. **Level 4 (Consistency of approximation and variational limit).** One must prove that the limit $u^*$ of any such subsequence genuinely satisfies the weak integral identity (or the $\Gamma$-limit of the variational functional) of the continuous problem.
5. **Level 5 (Uniqueness of the limit solution and convergence of the full sequence).** Only if the limiting continuous problem possesses a **unique** solution $u^*$ does compactness together with subsequence convergence imply convergence of the **entire** sequence $W_h u_h \to u^*$ as $h \to 0$; in the presence of non-uniqueness (for instance, under spontaneous symmetry breaking between two levels $+u^*$ and $-u^*$), different meshes $K_h$ may converge to different branches.

---

## §II.8.2. The de Rham Map $R_k$, Whitney Forms $W_k$, and Cohomology Isomorphism under Subdivision

Let us show how Level 1 and Level 3 meet in Whitney's classical theory of geometric integration and finite elements (H. Whitney, *Geometric Integration Theory*, 1957).

Let $K$ be a geometric simplicial complex with barycentric coordinates $\lambda_0, \lambda_1, \dots, \lambda_n$ ($\lambda_i \ge 0$, $\sum_{i=0}^n \lambda_i = 1$) on each simplex.
- The *de Rham reading map* $R_k : \Omega^k(K) \to C^k(K; \mathbb{R})$ maps a smooth differential $k$-form $\omega$ to a simplicial $k$-cochain by integrating over each oriented $k$-simplex $\sigma$:
  $$
  (R_k \omega)(\sigma) = \int_\sigma \omega.
  $$
  By Stokes' theorem, the de Rham reading intertwines the exterior derivative $d$ with the simplicial coboundary $\delta_k$ from `Chapter II.3`:
  $$
  R_{k+1}(d\omega)(\tau) = \int_\tau d\omega = \int_{\partial\tau} \omega = (R_k \omega)(\partial\tau) = (\delta_k R_k \omega)(\tau), \qquad \text{that is, } R_{k+1} d = \delta_k R_k.
  $$
- The reverse *Whitney reconstruction map* $W_k : C^k(K; \mathbb{R}) \to \Omega^k_{\mathrm{PL}}(K)$ assigns to each basis $k$-simplex $\sigma = [v_{i_0}, \dots, v_{i_k}]$ the piecewise-linear Whitney differential $k$-form
  $$
  W_k(\sigma) = k! \sum_{r=0}^k (-1)^r \lambda_{i_r}\, d\lambda_{i_0} \wedge \cdots \wedge \widehat{d\lambda_{i_r}} \wedge \cdots \wedge d\lambda_{i_k}.
  $$
  In particular, for $k = 0$, the Whitney form of a vertex $v_i$ is simply its barycentric hat function $W_0([v_i]) = \lambda_i$, while for $k = 1$, the Whitney form of an oriented edge $[v_i, v_j]$ equals
  $$
  W_1([v_i, v_j]) = \lambda_i\, d\lambda_j - \lambda_j\, d\lambda_i.
  $$

> **Proposition II.8.1 (Exact algebraic Whitney–de Rham identities, pointwise reconstruction defect $W_k R_k \ne \mathrm{id}$, and cohomological invariance under subdivision).**  
> *Classical foundation.* Whitney forms (1957), the de Rham map, and cohomology invariance under subdivision are classical constructions. *Contribution of this book:* Explicit rational verification of the one-sided identity $R_1 W_1 = \mathrm{id}$ and the reconstruction defect inside a cell.
> 1. On any simplicial mesh $K$, the reading operator $R_k$ and the Whitney reconstruction operator $W_k$ satisfy two exact algebraic identities:
>    $$
>    R_k W_k = \mathrm{id}_{C^k(K;\mathbb{R})}, \qquad d W_k = W_{k+1} \delta_k.
>    $$
>    Thus, $W_\bullet$ is a cochain embedding of the simplicial cochain complex into the complex of piecewise-linear differential forms, and $R_\bullet$ is a left inverse to it.
> 2. In the opposite order, the composition $W_k R_k : \Omega^k(K) \to \Omega^k_{\mathrm{PL}}(K)$ is a projector onto the finite-dimensional subspace of Whitney forms and **does not coincide** with the identity operator on smooth forms ($W_k R_k \omega \ne \omega$): for instance, on the unit interval $\sigma = [0, 1]$ with $\lambda_0 = 1 - x$, $\lambda_1 = x$, the smooth $1$-form $\omega = x\,dx$ has integral $R_1(\omega)([0,1]) = \int_0^1 x\,dx = \frac{1}{2}$, whereas its Whitney reconstruction is the constant form $W_1 R_1(\omega) = \frac{1}{2} W_1([0,1]) = \frac{1}{2}\bigl((1-x)dx - x(-dx)\bigr) = \frac{1}{2}\,dx \ne x\,dx$, differing from $\omega$ by the zero-mean linear mode $(x - \frac{1}{2})dx$.
> 3. Let $K'$ be a simplicial subdivision of the complex $K$ (for instance, splitting a triangle $\Delta^2 = [v_0, v_1, v_2]$ by the median from vertex $v_2$ to the midpoint $m$ of edge $[v_0, v_1]$ into two smaller triangles $[v_0, m, v_2]$ and $[m, v_1, v_2]$). Then the chain subdivision operator $s_\bullet : C_\bullet(K; R) \to C_\bullet(K'; R)$, mapping $[v_0, v_1] \mapsto [v_0, m] + [m, v_1]$ and $[v_0, v_1, v_2] \mapsto [v_0, m, v_2] + [m, v_1, v_2]$, commutes with the boundary operator ($\partial'_k s_k = s_{k-1} \partial_k$, since the internal cut edge $[m, v_2]$ enters the boundaries of the two new triangles with opposite signs and cancels), while the adjoint cochain restriction operator $s^* : C^\bullet(K'; R) \to C^\bullet(K; R)$ commutes with the coboundary ($\delta_k s^* = s^* \delta'_k$) and **induces a canonical isomorphism of simplicial cohomology groups**:
>    $$
>    s^* : H^k(K'; R) \xrightarrow{\;\sim\;} H^k(K; R).
>    $$

**Proof.**  
1. Along the edge $[v_i, v_j]$ itself, we have $\lambda_i + \lambda_j = 1 \implies d\lambda_i = -d\lambda_j$, so the restriction of $\lambda_i d\lambda_j - \lambda_j d\lambda_i$ to $[v_i, v_j]$ equals $(\lambda_i + \lambda_j) d\lambda_j = d\lambda_j$, whose integral from $\lambda_j = 0$ to $\lambda_j = 1$ equals $1$, whereas on all other edges either $\lambda_i \equiv 0$ or $\lambda_j \equiv 0$, yielding $R_1 W_1 = \mathrm{id}$. The exterior derivative $d(\lambda_i d\lambda_j - \lambda_j d\lambda_i) = 2\,d\lambda_i \wedge d\lambda_j$ coincides with the sum of the Whitney forms $W_2([v_i, v_j, v_k])$ over all triangles containing the edge $[v_i, v_j]$ (since $\sum_k \lambda_k = 1 \implies \sum_k d\lambda_k = 0$), whence $d W_1 = W_2 \delta_1$.
3. Under subdivision of the triangle $\Delta^2 = [v_0, v_1, v_2]$ by the median $[m, v_2]$, we have:
$$
\begin{aligned}
\partial'_2 s_2([v_0, v_1, v_2]) &= \partial'_2([v_0, m, v_2] + [m, v_1, v_2]) \\
&= \bigl([m, v_2] - [v_0, v_2] + [v_0, m]\bigr) + \bigl([v_1, v_2] - [m, v_2] + [m, v_1]\bigr) \\
&= \bigl([v_0, m] + [m, v_1]\bigr) + [v_1, v_2] - [v_0, v_2] = s_1(\partial_2[v_0, v_1, v_2]),
\end{aligned}
$$
whence by duality $\delta s^* = s^* \delta'$. Since the chain embedding $s_\bullet$ is a chain homotopy equivalence (with left inverse given by a simplicial approximation to the identity map $K' \to K$), the induced map $s^*$ on cohomology is bijective. $\blacksquare$

---

## §II.8.3. Semi-Discrete Cahn–Hilliard Gradient Flow on a Nerve Graph: Spontaneous Two-Level Value Splitting and Sum Conservation

Let us now see how on a discrete graph $G = (V, E)$ (for instance, on the $1$-skeleton of our octahedron of six slices $O_6$ from `Chapter I.9` and `Chapter II.4`, having $|V| = 6$ vertices and $|E| = 12$ edges) a dynamic **two-level value splitting** $u_v \approx +1$ and $u_v \approx -1$ arises while the sum of vertex values $\sum_{v \in V} u_v = \mathrm{const}$ is strictly conserved.

Denote by $D_1 \in \mathbb{R}^{|E| \times |V|}$ the oriented vertex-to-edge incidence matrix of the graph $G$ (the coboundary operator $\delta_0$ from `Chapter II.3`, where for each oriented edge $e = (u \to v)$ the row entry is $(D_1 u)_e = u_v - u_u$; we use the notation $D_1$ rather than $B$ to avoid confusing the incidence matrix with the memory step operator $B$ of `Chapter II.1`). Then the symmetric combinatorial graph Laplacian matrix
$$
L = D_1^{\mathsf{T}} D_1 \in \mathbb{R}^{|V| \times |V|}, \qquad u^{\mathsf{T}} L u = \|D_1 u\|_2^2 = \sum_{(u,v) \in E} (u_v - u_u)^2 \ge 0,
$$
is positive semidefinite ($L \succeq 0$), and its kernel $\ker L = \ker D_1$ has dimension equal to the number of connected components of the graph $G$ (for a connected graph such as the octahedron $O_6$, the kernel $\ker L = \operatorname{span}\{\mathbf{1}\}$ is one-dimensional and spanned by the constant vector $\mathbf{1} = (1, 1, \dots, 1)^{\mathsf{T}}$, $L \mathbf{1} = 0$).

Define on the space of vertex fields $u \in \mathbb{R}^{|V|}$ the Lyapunov functional (the discrete Ginzburg–Landau functional on the graph) with seam gradient penalty parameter $\gamma > 0$ (we write $\gamma$ so as not to encroach upon the parity charge symbol $\kappa$ of Book I) and double-well potential $F(u) = \sum_{v \in V} f(u_v)$ (for instance, $f(s) = \frac{1}{4}(s^2 - 1)^2$ with two minima at the binary states $s = \pm 1$):
$$
E_h(u) = \frac{\gamma}{2}\, u^{\mathsf{T}} L u + \sum_{v \in V} f(u_v) = \frac{\gamma}{2} \sum_{(u,v) \in E} (u_v - u_u)^2 + \sum_{v \in V} f(u_v).
$$
The gradient of this functional with respect to the vertex field $u$ is the vector of *variational potential* $\mu \in \mathbb{R}^{|V|}$:
$$
\mu = \nabla_u E_h(u) = \gamma L u + F'(u), \qquad F'(u)_v = f'(u_v).
$$

If the system evolved according to ordinary Allen–Cahn gradient descent $\dot{u} = -M \mu$, the sum of values $\mathbf{1}^{\mathsf{T}} u$ would not be conserved, and the entire field would roll into a single well ($+\mathbf{1}$ or $-\mathbf{1}$). To compel the system to **split values into two levels within the carrier itself while keeping their sum invariant**, $\sum_{v \in V} u_v = \mathrm{const}$ (conservative distinction), the gradient flow is taken in the $H^{-1}$-metric of the graph via an outer edge-flux divergence operator $-M L$:

> **Theorem II.8.1 (Semi-discrete conservative Cahn–Hilliard flow on a graph: exact equation, Lyapunov functional decrease, and conservation of the sum of values).**  
> *Classical foundation.* Conservative Cahn–Hilliard gradient flows and their discrete analogues on graphs are established constructions. *Contribution of this book:* Explicit free-energy dissipation law on the octahedron graph $O_6$ with spectrum $L_{O_6} = \{0, 4^{\times 3}, 6^{\times 2}\}$.
> Suppose on a graph $G = (V, E)$ with combinatorial Laplacian $L = D_1^{\mathsf{T}} D_1 \succeq 0$, constant mobility $M > 0$, and gradient term coefficient $\gamma > 0$, the semi-discrete Cahn–Hilliard equation is given by:
> $$
> \dot{u} = -M\, L\, \mu = -M\, L\,\bigl(\gamma L u + F'(u)\bigr), \qquad \mu = \gamma L u + F'(u).
> $$
> Then along every smooth trajectory $u(t)$, two strict conservation and dissipation laws hold:
> 1. **(Exact conservation of the sum of values on each connected component of the graph).** Since $\mathbf{1}^{\mathsf{T}} L = (L \mathbf{1})^{\mathsf{T}} = 0$, the time derivative of the total field vanishes identically:
>    $$
>    \frac{d}{dt}\left(\sum_{v \in V} u_v(t)\right) = \mathbf{1}^{\mathsf{T}} \dot{u} = -M\,(\mathbf{1}^{\mathsf{T}} L)\,\mu = 0.
>    $$
> 2. **(Strict monotonic decrease of the Lyapunov functional $E_h(u)$).** The time derivative of the functional $E_h$ along the flow is non-positive for any potential $F(u)$:
>    $$
>    \frac{d}{dt} E_h(u(t)) = \langle \nabla_u E_h(u),\, \dot{u} \rangle = \mu^{\mathsf{T}} (-M L \mu) = -M\,\mu^{\mathsf{T}} D_1^{\mathsf{T}} D_1 \mu = -M\,\|D_1 \mu\|_2^2 \le 0,
>    $$
>    and on a connected graph equality $\frac{dE_h}{dt} = 0$ is attained if and only if the variational potential $\mu = \gamma L u + F'(u) = c\,\mathbf{1}$ is constant across all vertices of the graph ($D_1 \mu = 0$).
> 3. **(Spontaneous binary distinction on the octahedron graph $O_6$).** On the graph of the octahedron of six slices $O_6$ ($|V| = 6$, $|E| = 12$), the Laplacian $L_{O_6} = 4 I_6 - A_{O_6}$ has eigenvalues:
>    - $\lambda_0 = 0$ (multiplicity $1$, the constant mode $\mathbf{1}$, frozen by the sum conservation law $\mathbf{1}^{\mathsf{T}} \dot{u} = 0$);
>    - $\lambda_1 = 4$ (multiplicity $3$, the three dipole modes $e_{X_0} - e_{X_1}$, $e_{C_0} - e_{C_1}$, $e_{B_0} - e_{B_1}$, separating the opposite poles of the three questions $X, C, B$ of Book I);
>    - $\lambda_2 = 6$ (multiplicity $2$, the quadrupole modes).
>    For the double-well potential $f(s) = \frac{1}{4}(s^2 - 1)^2$ with $f''(0) = -1 < 0$, the operator $-\,M L(\gamma L - I)$ linearized around the homogeneous state $u = 0$ has on the three dipole modes ($\lambda_1 = 4$) a positive instability growth rate $4 M (1 - 4\gamma) > 0$ whenever $0 < \gamma < 1/4$: the homogeneous "undistinguished" state $u = 0$ loses stability, and the Cahn–Hilliard flow spontaneously separates opposite vertices of the octahedron into binary poles $+u_*$ and $-u_*$.

**Proof.**  
The identity $\mathbf{1}^{\mathsf{T}} L = 0$ follows from the fact that each row of the matrix $D_1$ contains exactly one $+1$ and one $-1$, so $D_1 \mathbf{1} = 0$ and $L \mathbf{1} = D_1^{\mathsf{T}}(D_1 \mathbf{1}) = 0$. By the chain rule, $\frac{d}{dt}E_h(u(t)) = (\nabla_u E_h(u))^{\mathsf{T}} \dot{u} = \mu^{\mathsf{T}}(-M L \mu) = -M (D_1 \mu)^{\mathsf{T}}(D_1 \mu) = -M \|D_1 \mu\|_2^2 \le 0$. Finally, in the octahedron graph $O_6$, each of the $6$ vertices has degree $4$ and is non-adjacent only to its antipode, so $A_{O_6} = J_6 - I_6 - P_{\mathrm{antipod}}$, where $P_{\mathrm{antipod}}$ has eigenvalues $+1$ (on the $3$ even pair sums) and $-1$ (on the $3$ odd dipole differences $e_{X_0}-e_{X_1}, e_{C_0}-e_{C_1}, e_{B_0}-e_{B_1}$). On the three dipole differences, $J_6 v = 0$ and $P_{\mathrm{antipod}} v = -v$, whence $A_{O_6} v = 0 - v - (-v) = 0$ and $L_{O_6} v = 4 v$ ($\lambda_1 = 4$). On this $3$-dimensional subspace, the linearization of $\dot{u} = -M L(\gamma L u - u)$ reduces to multiplication by $-M \lambda_1 (\gamma \lambda_1 - 1) = 4M(1 - 4\gamma) > 0$ for $\gamma < 1/4$. $\blacksquare$

> **Methodological Note on Operator Ordering.**  
> Swapping the mobility factor $M$ and the gradient coefficient into the form $-L(M L u + F'(u))$ violates scale consistency and breaks the dissipation identity when $M \ne \gamma$. In `Theorem II.8.1`, the outer divergence $-M L$ acts on the full variational gradient $\mu = \gamma L u + F'(u)$, guaranteeing the identity $\frac{dE_h}{dt} = -M \mu^{\mathsf{T}} L \mu \le 0$.

---

## §II.8.4. Rational `SOS` Non-Negativity Certificates and the $21$-Dimensional Flag Space of the Fano Plane (Decomposition $84 + 1687 = 1771$)

Let us turn to the concluding problem of the chapter: how can one prove the global non-negativity of a polynomial $P(x) \ge 0$ ($\forall x \in \mathbb{R}^d$) infallibly, in exact rational arithmetic `Rational{BigInt}`, without relying on sampling a finite grid of points (between whose nodes a polynomial can dip into negative values, like the saddle $f(x,t) = x^2 - t^2$, which is non-negative on the slice $t = 0$ yet negative for $|t| > |x|$)?

The classical algebraic method consists in representing a homogeneous polynomial of even degree $2m$ as a **sum of squares** (`SOS`) via the vector of all basis monomials of degree $m$, $z_m(x) \in \mathbb{R}^N$ ($N = \binom{d+m-1}{m}$), and a symmetric **Gram matrix** $G \in \mathrm{Sym}_N(\mathbb{Q})$:
$$
P(x) = z_m(x)^{\mathsf{T}} G\, z_m(x).
$$
Note a structural point that the verifier must control: for one and the same polynomial $P(x)$ in dimension $d \ge 2$, the Gram matrix $G$ is **not unique** (because quadratic products of monomials in $z_m(x)$ obey syzygies such as $(x^2)(y^2) = (xy)^2$).
For example, for the manifestly non-negative biquadratic polynomial in two variables
$$
P(x, y) = (x^2 + y^2)^2 = x^4 + 2 x^2 y^2 + y^4,
$$
in the quadratic monomial basis $z_2(x, y) = (x^2,\, xy,\, y^2)^{\mathsf{T}}$, one can write both the positive semidefinite diagonal Gram matrix $G_{\mathrm{PSD}} = \mathrm{diag}(1, 2, 1) \succeq 0$ (with spectrum $\{2, 1, 1\}$ and sum of squares $(x^2)^2 + 2(xy)^2 + (y^2)^2 \ge 0$) and the indefinite Gram matrix
$$
G_{\mathrm{bad}} = \begin{pmatrix} 1 & 0 & 2 \\ 0 & -2 & 0 \\ 2 & 0 & 1 \end{pmatrix}, \qquad
z_2^{\mathsf{T}} G_{\mathrm{bad}} z_2 = x^4 + 4 x^2 y^2 - 2(xy)^2 + y^4 = (x^2 + y^2)^2,
$$
whose eigenvalues are **$3, -1, -2$** (two negative eigenvalues $-1$ and $-2$, with the diagonal entry $(G_{\mathrm{bad}})_{2,2} = -2 < 0$ already negative). Therefore, a genuine certificate of non-negativity $P(x) \ge 0$ consists in exhibiting a **specific** rational Gram matrix $G \succeq 0$ together with its exact rational Cholesky–Gauss triangular factorization
$$
G = L D L^{\mathsf{T}}, \qquad L \in \mathbb{Q}^{N \times N} \text{ unit lower-triangular}, \quad D = \mathrm{diag}(d_1, \dots, d_N), \quad d_i \in \mathbb{Q}_{\ge 0},
$$
which turns the inequality $P(x) = \sum_{i=1}^N d_i \bigl((L^{\mathsf{T}} z_m(x))_i\bigr)^2 \ge 0$ into a finite rational identity.

In particular, to certify a lower bound $Q(A) \ge q\,\|A\|_2^4$ for a homogeneous quartic form $Q(A)$ on the unit sphere $\|A\|_2 = 1$, it suffices to decompose into a sum of squares the homogeneous degree-six polynomial (with the Pólya–Reznick multiplier $\|A\|_2^2$):
$$
P_6(A) = \|A\|_2^2\,\bigl(Q(A) - q\,\|A\|_2^4\bigr) = z_3(A)^{\mathsf{T}} G\, z_3(A), \qquad G = L D L^{\mathsf{T}} \succeq 0,
$$
where $z_3(A)$ is the vector of degree-three monomials (the Veronese embedding into $\mathrm{Sym}^3$).

Let us now examine how the Veronese spaces $\mathrm{Sym}^2$ and $\mathrm{Sym}^3$ are structured on the natural geometric carrier continuing `Chapter II.5`—the **$21$-dimensional space of incident flags of the Fano plane** $\mathbb{Q}^{21}$.

Recall that the projective Fano plane $\mathrm{PG}(2, \mathbb{F}_2)$ from `Chapter I.6` and `Chapter II.5` consists of $7$ points and $7$ lines, with each of the $7$ lines containing exactly $3$ points. A pair $(p, \ell)$ ("point $p$ on line $\ell$") is called an *incident flag* of the Fano plane; in total there are exactly
$$
7 \times 3 = 21
$$
such flags. Assign to each of the $21$ flags a basis coordinate $A_{p,\ell}$ in the space $V_{21} = \mathbb{Q}^{21}$ (partitioned into $7$ three-dimensional line blocks of $3$ coordinates each). On this $21$-dimensional space, the **split affine-monomial group** naturally acts:
$$
G_{1344} = \mathbb{F}_2^3 \rtimes \mathrm{GL}_3(\mathbb{F}_2) \cong \mathrm{AGL}_3(\mathbb{F}_2) \qquad (|G_{1344}| = 8 \cdot 168 = 1344),
$$
where the simple automorphism group of the Fano plane $\mathrm{GL}_3(\mathbb{F}_2) \cong \mathrm{PSL}_2(7)$ of order $168$ transitively permutes the $21$ flags, while the normal elementary abelian translation subgroup $\mathbb{F}_2^3$ of order $8$ acts by signed characters $(-1)^{\langle u, p\rangle}$ ($u \in \mathbb{F}_2^3$) on the point coordinates within each line block (since the sum of the three points on any Fano line vanishes, $p_1 \oplus p_2 \oplus p_3 = 0$, the product of the three signs along every line equals $+1$).

> **Theorem II.8.2 (Invariant decomposition of the Veronese spaces $\mathrm{Sym}^2(\mathbb{Q}^{21})$ and $\mathrm{Sym}^3(\mathbb{Q}^{21})$ on Fano flags and the rational projector $P_\perp$ with partition $84 + 1687 = 1771$).**  
> *Classical foundation.* Isotypic character decomposition (Frobenius, Schur) and sum-of-squares representations via positive semidefinite Gram matrices (Hilbert, 1888; Choi–Lam–Reznick, 1995; Parrilo, 2000; Lasserre, 2001; Gatermann–Parrilo, 2004). *Contribution of this book:* Isotypic splitting $231 = 42 + 7\cdot 27$ and $1771 = 189 + 7\cdot 226$ on the $21$ flags of the Fano plane and the explicit rational orthogonal projector $P_{\perp,c}$ of codimension $84$ ($1771 - 84 = 1687$).
> Let $V_{21} = \mathbb{Q}^{21}$ be the flag space of the Fano plane carrying the action of the affine-monomial group $G_{1344} = \mathbb{F}_2^3 \rtimes \mathrm{GL}_3(\mathbb{F}_2)$ of order $1344$.
> 1. The dimensions of the quadratic and cubic symmetric monomial spaces equal
>    $$
>    \dim_{\mathbb{Q}} \mathrm{Sym}^2(V_{21}) = \binom{21 + 2 - 1}{2} = 231, \qquad
>    \dim_{\mathbb{Q}} \mathrm{Sym}^3(V_{21}) = \binom{21 + 3 - 1}{3} = 1771.
>    $$
> 2. Under the action of the normal subgroup of signed characters $\mathbb{F}_2^3 \trianglelefteq G_{1344}$, the spaces $\mathrm{Sym}^2(V_{21})$ and $\mathrm{Sym}^3(V_{21})$ split into orthogonal direct sums of the invariant (even) sector and seven non-trivial character sectors $u \in \mathbb{F}_2^3 \setminus \{0\}$ ($7$ isomorphic blocks permuted transitively by $\mathrm{GL}_3(\mathbb{F}_2)$):
>    $$
>    231 = 42 + 7 \times 27, \qquad 1771 = 189 + 7 \times 226.
>    $$
> 3. The cubic Veronese vectors $z_3(u) \in \mathrm{Sym}^3(V_{21})$ generated by the $84$ two-channel fiducial states $u_{a,b;s_1,s_2} \in \mathbb{Q}^{21}$ ($1 \le a < b \le 7$, $s_1, s_2 \in \{\pm 1\}$, where on the pair of points $a, b$ with joining Fano line $L_{ab} = \{a, b, a \oplus b\}$ the coordinates equal $A_{a,L_{ab}} = 1$, $A_{a,L'} = 2s_1$ for $L' \ne L_{ab}$ and $A_{b,L_{ab}} = s_2$, $A_{b,L''} = 2s_1 s_2$ for $L'' \ne L_{ab}$, while vanishing on the remaining $5$ points) span inside each of the $7$ non-trivial blocks of dimension $226$ an exact $12$-dimensional subspace (verified by Gaussian elimination in exact rational arithmetic `Rational{BigInt}`), which across all $7$ blocks yields an invariant subspace of dimension
>    $$
>    r = 7 \times 12 = 84,
>    $$
>    and an orthogonal complement of dimension
>    $$
>    1771 - 84 = 1687 \qquad \bigl(189 + 7 \times (226 - 12) = 189 + 7 \times 214 = 1687\bigr).
>    $$
> 4. The orthogonal projector $P_\perp \in \mathrm{Sym}_{1771}(\mathbb{Q})$ onto the $1687$-dimensional orthogonal complement of the rank-$84$ subspace has exact rational matrix entries, satisfies $P_\perp^2 = P_\perp$, $P_\perp \succeq 0$ ($\operatorname{rank} P_\perp = 1687$), and defines a canonical $G_{1344}$-invariant non-negative polynomial `SOS` form of degree six:
>    $$
>    S_6(A) = z_3(A)^{\mathsf{T}} P_\perp\, z_3(A) = \|P_\perp z_3(A)\|_2^2 \ge 0 \qquad (\forall A \in \mathbb{R}^{21}),
>    $$
>    which vanishes identically on the entire $84$-dimensional subspace of model cubic states. Furthermore, transferring any such model `SOS` bound to an approximate finite-element form $Q_h$ requires an explicit coefficientwise error budget: from $Q_{\mathrm{orig}} \ge \widetilde{Q} - (\delta + \varepsilon + \eta)$ and $\widetilde{Q} \ge q$ follows the strict inequality $Q_{\mathrm{orig}} \ge q - \delta - \varepsilon - \eta$.

**Proof.**  
1. The multiset combination formulas give $\binom{22}{2} = \frac{22 \cdot 21}{2} = 231$ and $\binom{23}{3} = \frac{23 \cdot 22 \cdot 21}{6} = 1771$.
2. Each of the $21$ coordinates $A_{p,\ell}$ transforms under $\mathbb{F}_2^3$ according to the character of the point $p \in \mathbb{F}_2^3 \setminus \{0\}$ (each of the $7$ points lies on $3$ lines, so each of the $7$ non-zero characters $\chi_p$ has multiplicity $3$). In $\mathrm{Sym}^2(V_{21})$, the trivial character $p \oplus p' = 0$ arises if and only if $p = p'$: for each of the $7$ points there are $\binom{3+2-1}{2} = 6$ quadratic monomials, yielding $7 \times 6 = 42$ invariant monomials, while the remaining $231 - 42 = 189$ monomials are equidistributed across the $7$ non-zero characters $p \oplus p' \ne 0$: $189 / 7 = 27$. In $\mathrm{Sym}^3(V_{21})$, a monomial $A_{p_1,\ell_1} A_{p_2,\ell_2} A_{p_3,\ell_3}$ has total character $p_1 \oplus p_2 \oplus p_3 \in \mathbb{F}_2^3$: since for any $p \ne 0$ in characteristic $2$ one has $p \oplus p \oplus p = p \ne 0$ and $p \oplus p \oplus q = q \ne 0$, the sum $p_1 \oplus p_2 \oplus p_3 = 0$ vanishes if and only if $\{p_1, p_2, p_3\}$ is an unordered triple of distinct collinear points forming one of the $7$ lines of the Fano plane $\mathrm{PG}(2,2)$. For each of the $7$ lines, choosing independently one of the $3$ flag coordinates at each of the $3$ points of the line gives $3^3 = 27$ cubic monomials, whence the dimension of the subspace of $\mathbb{F}_2^3$-invariants in $\mathrm{Sym}^3(V_{21})$ equals
$$
\dim \mathrm{Sym}^3(V_{21})^{\mathbb{F}_2^3} = 7 \times 3^3 = \frac{1771 - 7 \cdot 37}{8} = \frac{1512}{8} = \mathbf{189}
$$
(when counted via character traces, each of the $7$ non-zero elements of $\mathbb{F}_2^3$ has on $V_{21}$ exactly $9$ eigenvalues $+1$ and $12$ eigenvalues $-1$, giving trace $\binom{9+1}{2} + \binom{12+1}{2} - 9\cdot 12 = 45 + 78 - 108 = +15$ on $\mathrm{Sym}^2(V_{21})$ and trace $\binom{9+2}{3} + 9\binom{12+1}{2} - \binom{12+2}{3} - 12\binom{9+1}{2} = 867 - 904 = -37$ on $\mathrm{Sym}^3(V_{21})$). Each of the $7$ non-trivial characters in $\mathrm{Sym}^3(V_{21})$ has dimension $(1771 - 189)/7 = 1582 / 7 = \mathbf{226}$ ($189 + 7\cdot 226 = 1771$). Within each of the $7$ isotypic blocks of dimension $226$, the cubic span of the $12$ fiducial vectors has rank exactly $12$ (while in the invariant block of dimension $189$ all fiducial vectors vanish), giving total rank $7 \times 12 = 84$ and orthogonal complement dimension $1771 - 84 = 1687$. $\blacksquare$

---

## §II.8.5. Chapter Summary and Bridge to the Concluding Chapter II.9

Let us summarize the results of `Chapter II.8` on cellular models and limits.

#### Table II.8.1. Cellular Identities, Variational Flows, and Rational `SOS` Certificates in Chapter II.8

| Level and problem of the observer | Mathematical construction in `Chapter II.8` | Proved identity / certificate |
| :--- | :--- | :--- |
| Separation of levels $h > 0$ and $h \to 0$ | Five levels of cellular approximation (`§II.8.1`) | Identity on one mesh $\ne$ uniform bound $\ne$ compactness $\ne$ limit |
| Gluing of cochains and differential forms | de Rham reading $R_k$ and Whitney forms $W_k$ (`Prop. II.8.1`) | $R_k W_k = \mathrm{id}$, $d W_k = W_{k+1}\delta_k$; subdivision $s^*$ yields isomorphism $H^\bullet(K') \cong H^\bullet(K)$ |
| Spontaneous two-level value splitting on a nerve graph ($O_6$) | Semi-discrete Cahn–Hilliard flow $\dot{u} = -M L(\gamma L u + F'(u))$ (`Theorem II.8.1`) | Sum conservation $\mathbf{1}^{\mathsf{T}}\dot{u} = 0$ and dissipation $\frac{dE_h}{dt} = -M\|D_1\mu\|_2^2 \le 0$; instability of the $3$ dipole modes on $O_6$ |
| Exact certification of polynomial non-negativity | Rational Gram factorization $G = L D L^{\mathsf{T}}$ on Fano flags $\mathbb{Q}^{21}$ (`Theorem II.8.2`) | $231 = 42 + 7\cdot 27$, $1771 = 189 + 7\cdot 226$, rank $7\cdot 12 = 84$, and complement $1771 - 84 = 1687$ |

All four analytic, topological, algebraic, and quantum enrichments of Volume Two have now been constructed. In the concluding **Chapter `II.9`**, we pose the final, foundational question to the entire architecture of Books I and II: **can an observer, inside their own state carrier $A$, enumerate and encode all possible questions $A \to Y$ about themselves (Lawvere's diagonal theorem)?** And what is the complete synthesis of proved theorems, minimal memory spaces, and open domain bridges at the boundary with the third volume?

---

## Summary Passport of Chapter II.8 (for the Verifier and Formalization)

| Statement of the chapter | Content of the verified invariant | `Julia` gate (`11_verify_full_book_II_v3_3.jl`) |
| :--- | :--- | :--- |
| `Proposition II.8.1` | Verification of the Whitney identities $R_1 W_1 = \mathrm{id}$, the defect $W_1 R_1(x\,dx) = \frac{1}{2}dx \ne x\,dx$, and the subdivision chain identity $\partial'_2 s_2 = s_1 \partial_2$ | `GATE-II08-01` |
| `Theorem II.8.1` | Exact rational verification of the semi-discrete Cahn–Hilliard flow $\dot{u} = -M L(\gamma L u + F'(u))$ on the octahedron graph $O_6$: sum conservation $\mathbf{1}^{\mathsf{T}}\dot{u} = 0$, dissipation $\mu^{\mathsf{T}}\dot{u} = -M\mu^{\mathsf{T}}L\mu < 0$, and exact eigenspaces of $L_{O_6}$ with spectrum $\{0, 4^{\times 3}, 6^{\times 2}\}$ | `GATE-II08-02` |
| `§II.8.4` | Exact integer comparison of Gram matrices for $(x^2+y^2)^2$: eigenvectors for spectrum $\{3, -1, -2\}$ of $G_{\mathrm{bad}}$ and rational factorization $G_{\mathrm{PSD}} = L D L^{\mathsf{T}} \succeq 0$ | `GATE-II08-03` |
| `Theorem II.8.2` | Exhaustive enumeration of the group $G_{1344}$ on $\mathbb{Q}^{21}$: character decompositions $231 = 42 + 7\cdot 27$, $1771 = 189 + 7\cdot 226$, exact rank $12 \times 7 = 84$, explicit rational projector $P_{\perp,c}^2 = P_{\perp,c}$ ($\mathrm{tr}\,P_{\perp,c} = 214$) in `Rational{BigInt}`, and codimension $189 + 7\cdot 214 = 1687$ | `GATE-II08-04` |
