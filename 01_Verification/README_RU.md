# 01_Verification — Слой вычислительной верификации (чистая Julia 1.12+, `0` типов с плавающей точкой)

[English version](README.md) · [Методология v3.3](../00_Methodology/README_RU.md)

В этой папке находится единая однопоточная программа проверки для **Канонического Трёхтомника ТНР v3.3 (`77/77 GATES PASS` на английском и `77/77 GATES PASS` на русском = `154/154` гейта)**, глобального аудита целостности и ссылок репозитория и **Математического дополнения Хоггара/Фано/Цорна (`02_Supplements/01_Hoggar_Fano_Octonions_Certificates/`)**.

## 1. Единый мастер-верификатор на чистой Julia 1.12+ (без внешних пакетов и без плавающей точки)

Все верификаторы канонического трёхтомника редакции `v3.3` работают на стандартной библиотеке `Julia 1.12+` (`LinearAlgebra`, `Printf`, `SHA`, `Dates`, `Rational{BigInt}`) без внешних зависимостей и строго без вещественных типов с плавающей точкой (`GATE-I-SYS-FLOAT`, `GATE-II-SYS-FLOAT`, `GATE-III-SYS-FLOAT`).

Запуск полной проверки Трёхтомника (`77/77` гейтов EN + `77/77` гейтов RU + глобальный аудит ссылок и чистоты репозитория) одной командой из корня репозитория:

```bash
julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl
```

Запуск включая полный однопоточный пакет из 11 сертификатов Хоггара/Фано/Цорна (`--full`):

```bash
julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl --full
```

### Покнижные верификаторы Трёхтомника (`77/77 GATES PASS` EN + `77/77 GATES PASS` RU)

```bash
# Английское издание (77/77 GATES PASS)
julia --startup-file=no --threads=1 00_Core/Book_I_EN/11_verify_full_book_I_v3_3.jl      # 23/23 GATES PASS
julia --startup-file=no --threads=1 00_Core/Book_II_EN/11_verify_full_book_II_v3_3.jl    # 38/38 GATES PASS
julia --startup-file=no --threads=1 00_Core/Book_III_EN/07_verify_full_book_III_v3_3.jl   # 16/16 GATES PASS

# Русское издание (77/77 GATES PASS)
julia --startup-file=no --threads=1 00_Core/Книга_I/11_verify_full_book_I_v3_3.jl        # 23/23 GATES PASS
julia --startup-file=no --threads=1 00_Core/Книга_II/11_verify_full_book_II_v3_3.jl      # 38/38 GATES PASS
julia --startup-file=no --threads=1 00_Core/Книга_III/07_verify_full_book_III_v3_3.jl     # 16/16 GATES PASS
```

### Верификатор математического дополнения

```bash
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 02_Supplements/01_Hoggar_Fano_Octonions_Certificates/certificates_and_julia/run_all_math_certificates.jl
```

*(Пакет `20` семейств простых чисел полного схлопывания `OEIS A401173` к `Предложению I.8.1` опубликован в отдельном репозитории [`Nondual-Observer/total-collapse-primes-oeis`](https://github.com/Nondual-Observer/total-collapse-primes-oeis)).*
