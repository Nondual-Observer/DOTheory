# Readings of the observer-duality: bridges to classical mathematics and physics

**What this is.** Volume 7 establishes, in the native language of the corpus: the structure of the observer is a **duality** — orientation (the rotation $T$) and weight (the grading $H$), sharing the common horizon $\partial+\delta$ and diverging on the weight; the weight is the **irreducible axis of the observer**. This document **reads** that same duality through established external languages: Lie theory, finite fields, number theory, quantum information, Fourier analysis.

Each reading is a **translation, not a foundation**: the corpus is self-contained and stands without them. The readings ground the theory in known mathematics and give it operational meaning. The scope of each is marked: **(r3)** — rank 3; **(all-rank)** — all ranks. Full computations and checks are in `_TNR_Research/` (verifiers cited).

---

## Reading 1. Lie and Wedderburn: rotation and weight are one algebra **(r3)**

Native fact (Volume 7): $T$ and $\mathfrak{sl}_2$ form one structure whose real part is the weight and whose imaginary part is the rotation. In external language this is the **Wedderburn decomposition**:
$$\langle\partial,\delta,H,T\rangle\big|_{Q_3}\;\cong\;M_4(\mathbb R)\oplus M_2(\mathbb C),\qquad \dim=16+8=24.$$
The real block $M_4(\mathbb R)$ carries the **weight** ($\mathfrak{sl}_2$); the complex block $M_2(\mathbb C)$ carries the **rotation** (the imaginary unit is the 120° turn of the three axes). Adjoining the reflection $\sigma$ realifies the complex block: $\langle\mathfrak{sl}_2,T,\sigma\rangle = M_4(\mathbb R)\oplus M_4(\mathbb R) = 32$.

This is **Schur–Weyl duality** — the formal name for the native "weight ⟂ orientation": the collective $\mathfrak{sl}_2$ and the axis permutations $S_n$ are mutual commutants. The §8.3 lock has four equivalent faces: commutators ($[T,\partial+\delta]=0$, $[T,\partial-\delta]\ne0$) · Wedderburn (real ⊕ complex) · group (proper $\det+1$ ⟂ improper $\det-1$) · torsion (irrationality of $E$). *Details: `Tom7_8_3_Rank3_RESOLVED_RU.md`, `Sigma_Galois_Unifies_8_3_and_7_5_RU.md`.*

## Reading 2. Finite field: the horizontal is a field operation, the weight is not **(all-rank)**

The cube is the additive group of the field $GF(2^n)$; axis multiplication (Singer) is the multiplicative side; Frobenius $x\mapsto x^2$ is Galois. The affine group $AGL(1,2^n)$ ($x\mapsto ax+b$) is **sharply 2-transitive**, so the algebra of field operations is
$$A_{\text{field}}=\mathbb C\oplus M_{2^n-1}(\mathbb C),\qquad\dim=1+(2^n-1)^2.$$
And then — the external proof of the native **irreducibility of the weight**:
$$\mathfrak{sl}_2\cap A_{\text{field}}=\langle\partial+\delta\rangle\quad\forall n.$$
The field sees from $\mathfrak{sl}_2$ exactly the horizontal $\partial+\delta$; the vertical $\{\partial-\delta,H\}$ is outside the field at every rank. The reason: $\partial+\delta$ fixes the constant vector (the observer's mean), while the weight moves it. $\sigma$=Frobenius conjugates the complex block ($\sigma J\sigma=-J$, $i\mapsto-i$), linking Reading 1 with Reading 3. *Details: `Weight_NonField_AllRank_RU.md`, `Fermat_Mersenne_Duality_RU.md`.*

## Reading 3. Number theory: Fermat and Mersenne as the `±1` faces **(arithmetic)**

The `±1` polarity of $\kappa$ is imprinted in the numbers. The identity $2^{2k}-1=(2^k-1)(2^k+1)$ separates the **Mersenne** factor $2^k-1$ (axis count, $|PG(n-2,2)|$, the Singer cycle) and the **Fermat-shaped** $2^k+1$ (the operator tower $|B_k|+1$). Frobenius $\sigma$ fixes the Mersenne face, inverts the Fermat one. The product of Fermat primes $\prod F_j=2^{2^{k+1}}-1$ is the axis count at a ladder rank; by Gauss–Wantzel these ranks are compass-constructible. Five Fermat primes are known ⇒ the "fully Fermat" ladder ends at **rank 33**. Full circle: $|U_5|=30=2\cdot3\cdot5=2\cdot F_0\cdot F_1$.

The shared root with improperness: $2^{n-1}-1$ is **odd** at all ranks — this gives both $\det(\kappa|U_n)=-1$ (the screw's improperness) and per-level non-closure (the Singer period is coprime to doubling). *(The irrationality of the torsion $E$ is a separate, stronger fact of Erdős; it does not reduce to this parity.)* *Details: `Fermat_Mersenne_Duality_RU.md`.*

## Reading 4. Quantum information: the observer = a protected qubit **(r3 + all-rank)**

Rank 3 is **three qubits** $(\mathbb C^2)^{\otimes 3}$. Then:
- $\mathfrak{sl}_2=\{\partial,\delta,H\}$ = the **collective spin** $su(2)$ = the algebra of collective **noise**;
- $\kappa=X^{\otimes 3}$ = a **collective π-pulse** (the Weyl element);
- the §8.3 lock (weight ⟂ orientation) = **Schur–Weyl duality** (noise ⟂ logical);
- the protected inner layer ($2\cdot V_{1/2}$) = a **noiseless subsystem: one logical qubit**, on which the noise acts trivially; the axis permutations are logical gates.

**Rank 3 = the minimal number of qubits to protect a qubit** (Knill–Laflamme–Viola 2000) = the DOT "first stable scene." Forcedness ⟺ minimality is **one**: both = "$S_n$ is first non-abelian at $n=3$" (the first 2-dimensional standard representation), and that representation is at once the Borromean three-axis carrier and the protected qubit. The dimension-formula brick $d_j=\binom{n}{j}-\binom{n}{j-1}$ = the dimensions of protected subsystems (all-rank). *Details: `Observer_DFS_Dictionary_RU.md`, `Forcedness_Minimality_and_Det_E_RU.md`.*

## Reading 5. The continuous shadow: Euler–Fourier and the helicoid **(all-rank spectrally)**

Discrete and continuous are sampling and flow of one generator. $e^{i\pi}=-1$ is the **spectral face** of the operator identity $T^3=\kappa$. The chain Euler→Laplace→Fourier: $\partial=I-T$, $L=\partial^\dagger\partial=D-A$, $\lambda_L=|1-e^{i\theta}|^2$. The **root Fourier of DOT is Walsh–Hadamard** on the cube (universal at all ranks); the lift on the spectral side is the tensor $H^{\otimes n}$. The helicoid (Volume 4) is built explicitly as the screw $S(t)=\exp(t(\omega L_z+vP_z))$; its total torsion over the infinite tower of ranks is the **Erdős–Borwein constant** $E=\sum 1/(2^m-1)\approx1.6067$, irrational — the screw never closes even in the limit. *Details: `Discrete_Continuous_From_One_Triple_RU.md`, `Helicoid_Explicit_Screw_RU.md`, `Screw_From_Delta_Obstruction_RU.md`, `Synthesis_Two_Axes_Helicoid_RU.md`.*

---

## The through-thread: one polarity `±1`

All five readings are facets of one polarity, set by the single invariant $\kappa$:

| `+1` (proper) | `−1` (improper) |
|---|---|
| weight ($\mathfrak{sl}_2$, vertical) | orientation ($T$, rotation) |
| real block $M_4(\mathbb R)$ | complex block $M_2(\mathbb C)$ |
| Mersenne $2^k-1$ (axes, $\|PG\|$) | Fermat $2^{2^k}+1$ (tower) |
| observer (DC mode) | $\kappa$ (Nyquist mode) |
| Frobenius fixed point $\sigma$ | Frobenius inversion ($i\mapsto-i$) |
| noise sector (exposed) | protected qubit (noiseless) |

## Scope and discipline

Readings 1, 4 are mostly **rank-3** (the concrete algebra $M_4(\mathbb R)\oplus M_2(\mathbb C)$, the protected qubit); Readings 2 (weight-out-of-field), 3 (numbers), 5 (spectrum) and the DFS dimensions are **all-rank**. The corpus (Volumes 0–9) is self-contained and depends on none of these languages; they are translations that ground and illuminate. The presentation is affirmative: explored-and-rejected alternatives are not included here (they are in the verifier lab `_TNR_Research/`).

**Checks (all pass, 0 FAIL):** 16 counting verifiers in `_TNR_Research/` (256 PASS) plus descriptive ones; the single index is `_TNR_Research/00_MASTER_MAP_RU.md`.
