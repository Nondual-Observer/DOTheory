# Appendix C. Hopf/Borromean Bridge

Status: bridge document / protocol for topological preimages.

This document fixes the place of Möbius-, Hopf-, and Borromean-type readings relative to the strict finite core. The source is finite: $Q_3$, $X_{\mathrm{adm}}$, relations $R_1, R_2, R_3$, transport $T$, axial factorization, and exact axial presentations. Topological preimages receive a separate bridge status.

---

## C.0. Abstract and Document Route

The Hopf/Borromean bridge connects three finite structures of rank $3$ with three topological readings.

The first structure is an axial pair

$$
\begin{aligned}
H_i=\{I_i^-,I_i^+\}.
\end{aligned}
$$

It gives a two-pole carrier of one axis. In the topological reading, such a pair may be matched with a pair of Hopf-linked circles, but only after a separate topological carrier and embedding have been specified.

The second structure is the half-return of transport

$$
\begin{aligned}
T^3(I_i^\eta)=I_i^{-\eta}.
\end{aligned}
$$

It is a finite $Z_2$-holonomy on $X_{\mathrm{adm}}$. In the topological reading, this half-return corresponds to the motif of Möbius monodromy: one circuit changes the sign in a two-point fiber.

The third structure is the decomposition of the whole six-position carrier into three axial pairs:

$$
\begin{aligned}
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
\end{aligned}
$$

In the topological reading, this triple may be matched with a Borromean triad of blocks. This reading does not assert the presence of literal Borromean rings inside the finite core. It fixes only the schema: three blocks hold a common motif that is not reducible to one selected pair.

Document route:

$$
\begin{aligned}
\text{strict rank-3 source}
\to
\text{axial pairs}
\to
\text{exact axial presentations}
\to
\text{finite }Z_2\text{-holonomy}
\to
\text{Hopf/Möbius/Borromean readings}
\to
\text{status boundary}.
\end{aligned}
$$

Main boundary: $R_3=3K_2$, $T^3$, and $X_{\mathrm{adm}}\cong I_3\times\Sigma$ are objects of the strict finite core. The Möbius band, the Hopf link, and the Borromean link do not belong to that core. They become native objects only in a separate topological layer with specified carriers, embeddings, and invariants.

---

## C.1. Source Strict Layer

Rank $3$ defines the full carrier:

$$
\begin{aligned}
Q_3=\mathbb{F}_2^3.
\end{aligned}
$$

Admissible carrier:

$$
\begin{aligned}
X_{\mathrm{adm}}=Q_3\setminus\{000,111\}.
\end{aligned}
$$

On $X_{\mathrm{adm}}$, the Hamming relations are defined by:

$$
\begin{aligned}
R_k=\{(x,y)\in X_{\mathrm{adm}}\times X_{\mathrm{adm}}:
x\neq y,\ d_H(x,y)=k\},
\qquad
k=1,2,3.
\end{aligned}
$$

Graph-readings:

$$
\begin{aligned}
(X_{\mathrm{adm}},R_1)\cong C_6,
\end{aligned}
$$

$$
\begin{aligned}
(X_{\mathrm{adm}},R_2)\cong K_3\sqcup K_3,
\end{aligned}
$$

$$
\begin{aligned}
(X_{\mathrm{adm}},R_3)\cong 3K_2.
\end{aligned}
$$

Union relation:

$$
\begin{aligned}
R_{12}=R_1\cup R_2,
\qquad
(X_{\mathrm{adm}},R_{12})\cong K_{2,2,2}.
\end{aligned}
$$

The strict source for the Hopf/Borromean bridge is the relation $R_3$ and axial factorization:

$$
\begin{aligned}
X_{\mathrm{adm}}\cong I_3\times\Sigma,
\qquad
I_3=\{I_1,I_2,I_3\},
\qquad
\Sigma=\{-,+\}.
\end{aligned}
$$

---

## C.2. Axial Pairs

For $i\in\{1,2,3\}$:

$$
\begin{aligned}
H_i=\{I_i^-,I_i^+\}\subset X_{\mathrm{adm}}.
\end{aligned}
$$

The three axial pairs decompose the carrier:

$$
\begin{aligned}
X_{\mathrm{adm}}=H_1\sqcup H_2\sqcup H_3.
\end{aligned}
$$

The relation $R_3$ restricts to each pair as $K_2$:

$$
\begin{aligned}
(H_i,R_3|_{H_i})\cong K_2.
\end{aligned}
$$

The whole $R_3$-structure:

$$
\begin{aligned}
(X_{\mathrm{adm}},R_3)
\cong
H_1\sqcup H_2\sqcup H_3
\cong
3K_2.
\end{aligned}
$$

This is a native finite layer. The Hopf term adds no new strict object to this layer.

---

## C.3. Axial Presentations

For each axial pair, define a reading:

$$
\begin{aligned}
\pi_i:H_i\to\{I_i\},
\end{aligned}
$$

$$
\begin{aligned}
\pi_i(I_i^-)=I_i,
\qquad
\pi_i(I_i^+)=I_i.
\end{aligned}
$$

Recovery datum:

$$
\begin{aligned}
\mathrm{rec}_i(I_i) &=
(H_i,R_3|_{H_i}).
\end{aligned}
$$

Axial presentation:

$$
\begin{aligned}
\Pi_i^{\mathrm{ax},(3)} &=
(H_i,R_3|_{H_i},\pi_i,\mathrm{rec}_i).
\end{aligned}
$$

This presentation is exact: the unique fiber of the reading is $H_i$, and recovery returns that fiber together with the induced relation.

Conceptual formula of the strict layer:

$$
\begin{aligned}
\text{one axial invariant}
\quad
\longmapsto
\quad
\text{two polar manifestations}.
\end{aligned}
$$

---

## C.4. Finite Holonomy

Transport $T$ on $X_{\mathrm{adm}}$ is constructed after choosing an orientation on the $C_6$-reading of the relation $R_1$:

$$
\begin{aligned}
T:X_{\mathrm{adm}}\to X_{\mathrm{adm}},
\qquad
T^6=\mathrm{id}_{X_{\mathrm{adm}}}.
\end{aligned}
$$

Half-return:

$$
\begin{aligned}
T^3(x)=x+111.
\end{aligned}
$$

In axial notation:

$$
\begin{aligned}
T^3(I_i^\eta)=I_i^{-\eta}.
\end{aligned}
$$

Strict status:

$$
\begin{aligned}
T^3
\end{aligned}
$$

is finite $Z_2$-holonomy on $X_{\mathrm{adm}}$.

Bridge-reading:

$$
\begin{aligned}
T^3
\quad
\text{is read as}
\quad
\text{Möbius-type monodromy}.
\end{aligned}
$$

A literal Möbius band requires its own topological carrier:

$$
\begin{aligned}
p:E\to S^1,
\qquad
p^{-1}(\theta)\cong\Sigma,
\end{aligned}
$$

with monodromy swap after one circuit. This carrier has bridge status.

---

## C.5. Hopf-Type Reading

For each strict axial pair:

$$
\begin{aligned}
H_i=\{I_i^-,I_i^+\},
\end{aligned}
$$

the bridge-target is a two-component topological pair:

$$
\begin{aligned}
\mathcal H_i=(L_i^-,L_i^+),
\end{aligned}
$$

where $L_i^-$ and $L_i^+$ are oriented closed curves in an ambient $3$-manifold, for example in $S^3$.

Literal Hopf condition:

$$
\begin{aligned}
\mathrm{lk}(L_i^-,L_i^+)=\pm1.
\end{aligned}
$$

Bridge-handoff:

$$
\begin{aligned}
I_i^-\mapsto L_i^-,
\qquad
I_i^+\mapsto L_i^+,
\end{aligned}
$$

$$
\begin{aligned}
R_3|_{H_i}
\quad
\mapsto
\quad
\text{linked two-component relation}.
\end{aligned}
$$

Status:

$$
\begin{aligned}
(H_i,R_3|_{H_i})\cong K_2
\end{aligned}
$$

is native strict data.

$$
\begin{aligned}
\mathcal H_i
\end{aligned}
$$

is Hopf-target data after an embedding model has been specified.

Hopf-type reading is defined by the bridge formula:

$$
\begin{aligned}
\text{one axial invariant in two polar manifestations}
\quad
\leadsto
\quad
\text{two linked boundary components}.
\end{aligned}
$$

---

## C.6. Borromean Block-Triad

Strict finite source:

$$
\begin{aligned}
\mathcal B_3=\{H_1,H_2,H_3\}.
\end{aligned}
$$

Each $H_i$ is a two-point axial block. The triad of blocks is fixed after the factorization:

$$
\begin{aligned}
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\end{aligned}
$$

Borromean-type bridge reading:

$$
\begin{aligned}
(H_1,H_2,H_3)
\quad
\leadsto
\quad
\text{three block-components held as one triadic dependency}.
\end{aligned}
$$

Literal Borromean rings consist of three topological components with nontrivial triple linking and trivial pairwise linking. The strict finite source defines different data:

$$
\begin{aligned}
3\text{ axial blocks},
\qquad
2\text{ polar states in each block}.
\end{aligned}
$$

A compatible topological target has the block-level form:

$$
\begin{aligned}
\mathcal L_{\mathrm{block}} &=
(\mathcal H_1,\mathcal H_2,\mathcal H_3),
\end{aligned}
$$

where each $\mathcal H_i$ may have Hopf-type structure.

Status:

$$
\begin{aligned}
\mathcal B_3
\end{aligned}
$$

is native finite block data.

$$
\begin{aligned}
\text{Borromean block-triad}
\end{aligned}
$$

has bridge-readable status.

$$
\begin{aligned}
\text{literal six-component topological link}
\end{aligned}
$$

has not-yet status until explicit curves, ambient space, and linking invariants have been specified.

---

## C.7. Möbius, Hopf-Band, Hopf Pair

The three topological names have different roles.

Möbius avatar:

$$
\begin{aligned}
\text{one circuit}
\quad
\mapsto
\quad
\text{fiber swap}.
\end{aligned}
$$

Strict source:

$$
\begin{aligned}
T^3(I_i^\eta)=I_i^{-\eta}.
\end{aligned}
$$

Hopf-band avatar:

$$
\begin{aligned}
\text{annular/twisted surface with two boundary components}.
\end{aligned}
$$

Bridge-role:

$$
\begin{aligned}
I_i^-,
\ I_i^+
\end{aligned}
$$

are read as two boundary components of one axial block.

Hopf pair:

$$
\begin{aligned}
\mathrm{lk}(L_i^-,L_i^+)=\pm1.
\end{aligned}
$$

Bridge-role:

$$
\begin{aligned}
H_i
\end{aligned}
$$

is realised as a linked pair after an embedding has been specified.

Status discipline:

$$
\begin{aligned}
\text{finite }Z_2\text{-holonomy}
\end{aligned}
$$

has native status.

$$
\begin{aligned}
\text{Möbius/Hopf/Hopf-band}
\end{aligned}
$$

have bridge-target status.

---

## C.8. Legacy Labels

Earlier notes used the labels:

$$
\begin{aligned}
D,\quad F,\quad C.
\end{aligned}
$$

In the current strict architecture, these labels are not native names of the axial carrier. The native carrier is:

$$
\begin{aligned}
I_3=\{I_1,I_2,I_3\}.
\end{aligned}
$$

Diagrams may use a label map:

$$
\begin{aligned}
\lambda:I_3\to\{D,F,C\}.
\end{aligned}
$$

Such a map has readable status. In proofs, it is used only after the target layer defines $D,F,C$ as its own carrier labels.

---

## C.9. Status Table

| Object / Claim | Strict Core Status | Hopf/Borromean Bridge Status |
|---|---:|---:|
| $X_{\mathrm{adm}}$ | native | source carrier |
| $R_3=3K_2$ | native | source relation for axial pairs |
| $H_i=\{I_i^-,I_i^+\}$ | native | source block |
| $\Pi_i^{\mathrm{ax},(3)}$ | native exact presentation | source presentation |
| $T^3(I_i^\eta)=I_i^{-\eta}$ | native finite holonomy | Möbius-readable monodromy |
| $p:E\to S^1$ with swap monodromy | outside strict core | Möbius bridge carrier |
| Hopf link $(L_i^-,L_i^+)$ | outside strict core | bridge target after embedding |
| $\mathrm{lk}(L_i^-,L_i^+)=\pm1$ | outside strict core | topological verification |
| $(H_1,H_2,H_3)$ | native finite block triad | Borromean-readable source |
| literal six-component link | not-yet | requires explicit construction |
| physical interpretation | outside strict core | downstream interpretation |

---

## C.10. Necessary Figures

### Figure C1. $R_3=3K_2$

Show three disjoint $K_2$-pairs:

$$
\begin{aligned}
H_1,\quad H_2,\quad H_3.
\end{aligned}
$$

Purpose: strict finite source for Hopf-type reading.

### Figure C2. Axial Factorization

Show:

$$
\begin{aligned}
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\end{aligned}
$$

Rows: $I_1,I_2,I_3$. Columns: $-,+$.

Purpose: show that a Hopf-type pair belongs to one axial invariant.

### Figure C3. Half-Return $T^3$

Show the $C_6$-cycle and the three antipodal jumps:

$$
\begin{aligned}
I_i^-\leftrightarrow I_i^+.
\end{aligned}
$$

Purpose: finite $Z_2$-holonomy before Möbius reading.

### Figure C4. Möbius Target Schema

Show base circle $S^1$, two-point fiber $\Sigma$, and monodromy swap after one circuit.

Purpose: bridge carrier for Möbius-readable $T^3$.

### Figure C5. Hopf Pair per Axis

Show two linked curves $L_i^-,L_i^+$ with label:

$$
\begin{aligned}
\mathrm{lk}=\pm1.
\end{aligned}
$$

Purpose: topological target of one axial pair.

### Figure C6. Borromean Block-Triad

Show three blocks:

$$
\begin{aligned}
\mathcal H_1,\quad\mathcal H_2,\quad\mathcal H_3.
\end{aligned}
$$

Each block contains two polar components. The block-level dependency is shown separately from internal Hopf-pair linking.

Purpose: separate ordinary Borromean rings from $3$ two-component blocks.

### Figure C7. Status Boundary

Show:

$$
\begin{aligned}
\text{strict finite core}
\to
\text{Möbius/Hopf bridge}
\to
\text{literal topological link model}.
\end{aligned}
$$

Purpose: preserve the boundary between finite relations and topological embedding.

---

## C.11. What Is Fixed

The Hopf/Borromean layer has correct bridge status.

Strict finite source:

$$
\begin{aligned}
(X_{\mathrm{adm}},R_3)\cong 3K_2,
\qquad
X_{\mathrm{adm}}\cong I_3\times\Sigma.
\end{aligned}
$$

Exact axial presentations:

$$
\begin{aligned}
\Pi_i^{\mathrm{ax},(3)} &=
(H_i,R_3|_{H_i},\pi_i,\mathrm{rec}_i).
\end{aligned}
$$

Finite holonomy:

$$
\begin{aligned}
T^3(I_i^\eta)=I_i^{-\eta}.
\end{aligned}
$$

Bridge readings:

$$
\begin{aligned}
T^3
\leadsto
\text{Möbius-type monodromy},
\end{aligned}
$$

$$
\begin{aligned}
H_i
\leadsto
\text{Hopf-type axial pair},
\end{aligned}
$$

$$
\begin{aligned}
(H_1,H_2,H_3)
\leadsto
\text{Borromean block-triad}.
\end{aligned}
$$

Literal topological models require explicit carriers, embeddings, and linking invariants. Until these data are specified, they remain outside the strict finite core.
