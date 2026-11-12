# Дополнение 01: Чётность таблицы знаков Хоггара ($K_n$), октонионы Цорна $\mathrm{Oct}(\mathbb{F}_2)$ и 36 подгрупп Фано (`11/11` сертификатов Julia)

[English version](README.md)

Дополнение включает математическую заметку и `11` автономных однопоточных проверочных программ на языке `Julia`. Они расширяют **Книгу II (Главы II.5 и II.7)** Канонического Трёхтомника v3.3:

1. **[`02_МАТЕМАТИЧЕСКАЯ_ЗАМЕТКА_ЧЁТНОСТЬ_ХОГГАРА_И_36_ПОДГРУПП_ФАНО.md`](02_МАТЕМАТИЧЕСКАЯ_ЗАМЕТКА_ЧЁТНОСТЬ_ХОГГАРА_И_36_ПОДГРУПП_ФАНО.md)** *(English: [`02_MATHEMATICAL_NOTE_HOGGAR_PARITY_AND_36_FANO_SUBGROUPS_EN.md`](02_MATHEMATICAL_NOTE_HOGGAR_PARITY_AND_36_FANO_SUBGROUPS_EN.md))*:
   - **Утверждение A (Чётность таблицы знаков и замкнутая формула $K_n$):** инвариантное сравнение $e \equiv 1 + K \pmod 2$ для Паули-ковариантных SIC-фидуциалов в $\mathbb{C}^8$ и аналитическая формула $K_n = \frac{1}{4}\bigl(\frac{16^n + 4^n}{2} - 10^n\bigr)$ ($K_3 = 270$).
   - **Утверждение B (`12 096` автоморфизмов Цорна и `36` подгрупп Фано):** конструктивный вывод $|\mathrm{Aut}(\mathrm{Oct}(\mathbb{F}_2))| = 72 \times 168 = 12\,096$ с полной проверкой всех $12\,096^2 = 146\,313\,216$ композиций и явный координатный словарь между `36` парами идемпотентов Цорна $\{e, 1+e\}$, `36` квадратичными формами плюс-типа на $\mathbb{F}_2^6$, `36` подгруппами Леви $\mathrm{GL}_3(2) \subset \mathrm{PSU}_3(3)$ и `36` вещественными структурами Паули $J_c^2 = I$.
2. **[`certificates_and_julia/`](certificates_and_julia/)**:
   - [`run_all_math_certificates.jl`](certificates_and_julia/run_all_math_certificates.jl) — единый однопоточный запуск всех `11` математических скриптов (`study_41`: `01, 04, 06, 10, 10b, 12`; `audit_111`: `03, 04, 09, 15, 16`) со сверкой эталонных JSON-сертификатов.

## Запуск проверки

Команду нужно выполнять из корня репозитория:

```bash
JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 02_Supplements/01_Hoggar_Fano_Octonions_Certificates/certificates_and_julia/run_all_math_certificates.jl
```
