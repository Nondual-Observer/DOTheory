# Distinction and Observability Theory (DOT) — Volume I

> **Русская версия:** [ru/README.md](ru/README.md) | [ru/VOLUME_I.md](ru/VOLUME_I.md)
> **Terminology & Conceptual Concordance:** [GLOSSARY.md](GLOSSARY.md)

[![Code license: CC BY-NC-SA 4.0](https://img.shields.io/badge/Code-CC%20BY--NC--SA%204.0-yellow.svg)](LICENSE)
[![Theory license: CC BY-NC-SA 4.0](https://img.shields.io/badge/Theory-CC%20BY--NC--SA%204.0-blue.svg)](LICENSE-THEORY.md)

DOT (*Distinction and Observability Theory*; Russian title: *Теория Наблюдаемого Различения*, abbreviated ТНР) is a research program investigating how a single mathematical structure is described across different representations and what must be preserved so that the transition between descriptions does not lose essential connections.

## Where the Question Begins

Suppose we are given numbers $x$ and $y$, but we record only their difference:

\[
d = x - y.
\]

If we add the same number $t$ to both participants, the difference remains unchanged: $(x + t) - (y + t) = d$. Thus, this reading preserves a specific relation. However, from $d$ alone one cannot reconstruct the original $x$ and $y$: for this, an additional fulcrum is required. And if a subsequent question depends on the participants themselves, a single preserved difference may not suffice.

This is a standard elementary mathematical example, not a new arithmetic theorem. It illustrates the central problem addressed by this volume: to determine precisely what a chosen representation preserves, what it conceals, and what auxiliary data are required for an answer, an action, or a reconstruction.

## What DOT Investigates

DOT examines transitions between mathematical representations — for example, between a table of states, a logical query, a graph, an algebraic rule, and a geometric model. For every transition, the following are explicitly specified:

- the source object and its relations;
- the chosen reading — which aspect of the object is exhibited;
- the action and the question that must be transported;
- the data that remain accessible;
- the conditions under which the result can be continued forward or unfolded back.

The "hidden side" here does not denote anything mystical: it refers simply to the differences of the source model that are not visible in the current notation. The "observer" is a formal role of reading and obtaining an answer, not an assertion about human consciousness or physical measuring apparatus. The *metacenter* is the name of the role of a balancing fulcrum relative to which distinct presentations are coordinated; in each specific model, its realization and governing law must be stated separately.

## Contents of the First Volume

The volume constructs and verifies finite models, beginning with a pair of states and advancing to questions, actions, memory, and joint reconstruction. The same analytic method is then applied to graph-theoretic and geometric constructions, arithmetic, phase models, and computational examples. Mere visual resemblance between figures or numerical coincidence is never accepted as proof of a connection: for every bridge, carriers, mappings, and preserved work are explicitly specified.

The first volume is a working draft. A second volume is planned for later publication; it will develop phase and operator actions, geometric and topological representations, spectral properties, and transitions toward continuous structures.

The book does not claim that all mathematics can be deduced from a single universal structure; nor does it announce a new physical theory or computational supremacy. The results pertain strictly to explicitly specified models, while the universality of the method remains an open problem.

## How to Read

1. [Introduction](INTRODUCTION.md) explains the motivating problem without requiring prior acquaintance with the DOT vocabulary.
2. [Volume I](VOLUME_I.md) contains all chapters and technical appendices.
3. The text distinguishes explicit epistemic statuses:
   - **[Def]** — chosen definition or specification (*[П]*),
   - **[Th]** — statement with substantiated proof (*[Т]*),
   - **[Ext]** — standard external mathematical tool (*[В]*),
   - **[CE]** — counterexample (*[К]*),
   - **[Comp]** — finite computational verification (*[Ч]*),
   - **[Interp]** — methodological or conceptual interpretation (*[И]*),
   - **[Open]** — open research question (*[О]*),
   - **[Prem]** — initial research premise (*[Исх]*).
   These markers ensure that the chosen model, mathematical proof, and working hypothesis are never conflated.

The release includes self-contained, portable finite verification scripts:
- **Julia:** [A3 reduction](verification/verify_a3_cover.jl), [Aₙ root family limits](verification/verify_an_rank_limits.jl), [H3 root reduction](verification/verify_h3.jl), [Pauli local windows](verification/verify_pauli_local_windows.jl).
- **Python:** [action composition algebra](verification/tnr_action_algebra_check.py), [operational hinge](verification/tnr_operational_hinge_check.py), [local closure](verification/tnr_local_closure_check.py), [unified operational structure](verification/tnr_unified_operational_structure_check.py), [divisor factorization lattice](verification/tnr_factorization_lattice_check.py), [descent closure and memory](verification/tnr_descent_closure_memory_check.py).

For Python dependencies, install via `python3 -m pip install -r requirements.txt`. Then execute, for instance, `julia verification/verify_a3_cover.jl` or `python3 verification/tnr_action_algebra_check.py`. The included Julia scripts require only the Julia standard library. Finite computational checks support reasoning, but do not substitute for general mathematical proofs.

This repository contains the first volume, not the complete research archive. Bibliographic references are incomplete and will be checked and expanded in a later version; many of the mathematical structures used here are standard and are not claimed as new in themselves.

License terms are specified in [`LICENSE`](LICENSE) and [`LICENSE-THEORY.md`](LICENSE-THEORY.md).

## Supporting the Research

This is an independent, open research project. Support helps fund larger computational experiments, further formalization, and reproducible research tools, while allowing the work to remain independent and openly available.

| Currency | Network | Address |
|---|---|---|
| Bitcoin | BTC | `bc1qlaxsrum7fxpml57nsrtkjfkkxl5v3xtj4d0uxe` |
| USDT | TRC20 | `TM8U2EqVaT3tjvG6NyuKTqY4F5qc2A69Sy` |
| Ethereum | ETH | `0x4fFc68f0d55d19Fa5EBd5f6570a41E100aFe4a98` |
