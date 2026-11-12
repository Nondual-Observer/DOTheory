# Supplement 01: Hoggar Sign-Table Parity ($K_n$), Zorn Octonions $\mathrm{Oct}(\mathbb{F}_2)$, and 36 Fano Subgroups (`11/11` Julia Certificates)

[Русская версия](README_RU.md)

This supplement contains a mathematical note and `11` standalone, single-threaded `Julia` verification programs. They extend **Book II (Chapters II.5 and II.7)** of the Canonical Three-Volume Edition v3.3:

1. **[`02_MATHEMATICAL_NOTE_HOGGAR_PARITY_AND_36_FANO_SUBGROUPS_EN.md`](02_MATHEMATICAL_NOTE_HOGGAR_PARITY_AND_36_FANO_SUBGROUPS_EN.md)** *(Russian: [`02_МАТЕМАТИЧЕСКАЯ_ЗАМЕТКА_ЧЁТНОСТЬ_ХОГГАРА_И_36_ПОДГРУПП_ФАНО.md`](02_МАТЕМАТИЧЕСКАЯ_ЗАМЕТКА_ЧЁТНОСТЬ_ХОГГАРА_И_36_ПОДГРУПП_ФАНО.md))*:
   - **Proposition A (Sign-Table Parity & Closed Formula for $K_n$):** Invariant parity congruence $e \equiv 1 + K \pmod 2$ for Pauli-covariant SIC fiducials in $\mathbb{C}^8$, and closed analytical formula $K_n = \frac{1}{4}\bigl(\frac{16^n + 4^n}{2} - 10^n\bigr)$ ($K_3 = 270$).
   - **Proposition B ($12\,096$ Zorn Automorphisms & 36 Fano Subgroups):** Constructive derivation of $|\mathrm{Aut}(\mathrm{Oct}(\mathbb{F}_2))| = 72 \times 168 = 12\,096$ verified across all $12\,096^2 = 146\,313\,216$ ordered pairs, and explicit coordinate bijection between the `36` Zorn idempotent pairs $\{e, 1+e\}$, `36` plus-type quadratic forms on $\mathbb{F}_2^6$, `36` Levi subgroups $\mathrm{GL}_3(2) \subset \mathrm{PSU}_3(3)$, and `36` real Pauli structures $J_c^2 = I$.
2. **[`certificates_and_julia/`](certificates_and_julia/)**:
   - [`run_all_math_certificates.jl`](certificates_and_julia/run_all_math_certificates.jl) — executes all `11` mathematical scripts (`study_41`: `01, 04, 06, 10, 10b, 12`; `audit_111`: `03, 04, 09, 15, 16`) in single-threaded CPU/BLAS mode and verifies all JSON certificates.

## Run Verification

Run this command from the repository root:

```bash
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 02_Supplements/01_Hoggar_Fano_Octonions_Certificates/certificates_and_julia/run_all_math_certificates.jl
```
