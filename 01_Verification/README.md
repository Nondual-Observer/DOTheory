# 01_Verification — Verification Layer (Pure Julia 1.12+, Zero Floating-Point Types)

[Русская версия](README_RU.md) · [Methodology v3.3](../00_Methodology/README.md)

This folder contains the single-threaded verification runner for the **Canonical Three-Volume Edition v3.3 (`77/77 GATES PASS` in English & `77/77 GATES PASS` in Russian = `154/154` gates)**, the global repository link and hygiene audit, and the **Hoggar/Fano/Zorn Supplement (`02_Supplements/01_Hoggar_Fano_Octonions_Certificates/`)**.

## 1. Master Julia Verification Suite (Zero External Dependencies, Zero Floating-Point Arithmetic)

All canonical `v3.3` trilogy verifiers run on standard-library **Julia 1.12+** (`LinearAlgebra`, `Printf`, `SHA`, `Dates`, `Rational{BigInt}`) with zero external packages required and strictly zero floating-point types (`GATE-I-SYS-FLOAT`, `GATE-II-SYS-FLOAT`, `GATE-III-SYS-FLOAT`).

Run the Trilogy verifiers (`77/77` EN + `77/77` RU + global repository integrity check) in one command from the repository root:

```bash
julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl
```

Or run including the exhaustive 11-script single-threaded Hoggar/Fano/Zorn certificate suite (`--full`):

```bash
julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl --full
```

### Individual Book Verifiers (`77/77 GATES PASS` EN + `77/77 GATES PASS` RU)

```bash
# English Edition Verifiers (77/77 GATES PASS)
julia --startup-file=no --threads=1 00_Core/Book_I_EN/11_verify_full_book_I_v3_3.jl      # 23/23 GATES PASS
julia --startup-file=no --threads=1 00_Core/Book_II_EN/11_verify_full_book_II_v3_3.jl    # 38/38 GATES PASS
julia --startup-file=no --threads=1 00_Core/Book_III_EN/07_verify_full_book_III_v3_3.jl   # 16/16 GATES PASS

# Russian Edition Verifiers (77/77 GATES PASS)
julia --startup-file=no --threads=1 00_Core/Книга_I/11_verify_full_book_I_v3_3.jl        # 23/23 GATES PASS
julia --startup-file=no --threads=1 00_Core/Книга_II/11_verify_full_book_II_v3_3.jl      # 38/38 GATES PASS
julia --startup-file=no --threads=1 00_Core/Книга_III/07_verify_full_book_III_v3_3.jl     # 16/16 GATES PASS
```

### Supplement & Companion Verifiers

```bash
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 02_Supplements/01_Hoggar_Fano_Octonions_Certificates/certificates_and_julia/run_all_math_certificates.jl
```

*(For the 20 families of Total Collapse Primes `OEIS A401173` accompanying `Proposition I.8.1`, see the companion repository [`Nondual-Observer/total-collapse-primes-oeis`](https://github.com/Nondual-Observer/total-collapse-primes-oeis)).*
