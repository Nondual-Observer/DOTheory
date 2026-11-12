# Article-by-Article Certification Registry and Attribution Index of the 103 Statements of the Three-Volume DOT Monograph (`v3.3`)

This registry compiles all `103` formal statements—theorems, lemmas, and propositions (`57` in Book I, `31` in Book II, and `15` in Book III)—across the `23` chapters of canonical edition `v3.3`.

## 1. Five Epistemic Statuses and the Two-Part Attribution Standard

Throughout all twenty-three chapters, directly beneath the heading of every formal statement an italicized two-part attribution note `*Classical foundation.* ... *Contribution of this book:* ...` explicitly separates classical mathematical structures and primary sources from the operational framework of DOT. In the summary tables of Appendices `VP` and in the present registry, each of the `103` statements is assigned one of five verbal epistemic statuses together with the exact gate of the single-threaded `Julia 1.12.6` verifier (operating strictly in exact integer, rational, and algebraic arithmetic with zero floating-point types):

1. **`Classical result in operational notation`** (`26` statements) — a classical theorem formulated in the notation of the operational contract $\Gamma$ with an explicit citation to the primary source and verified on a finite window.
2. **`Extension of a classical theorem within contract Γ`** (`40` statements) — a classical mathematical core for which this book proves an exact operational condition within contract $\Gamma$ (accounting for partial admissibility domains $\mathrm{Dom}(T_a), \mathrm{Dom}(q)$, a shift threshold $j_0$, reading tolerance $\eta_{\mathrm{read}}$, the three-component cost ledger $(Z_D, Z_C, Z_F)$, or a descent condition across a seam).
3. **`Original proved result of this book`** (`27` statements) — original theorems and exact finite classifications proved analytically in this book and verified by exhaustive enumeration in `Julia`.
4. **`Two-arrow structural correspondence (bridge)`** (`2` statements) — a two-arrow correspondence $(\iota, \mathcal{O}_\pi)$ linking a mathematical construction to an external model in Book III that satisfies the eight-row bridge passport and null/surrogate controls.
5. **`Proved prohibition / counterexample`** (`8` statements) — a rigorously proved obstruction, finite counterexample, or non-recoverability witness when an operational hypothesis is dropped.

---

## 2. Summary Certification Table of All 103 Statements (Books I, II, III)

| No. | Statement | File and Line | Epistemic Status | `Julia` Gate |
| :-: | :--- | :--- | :--- | :--- |
| `1` | **Theorem I.1.0a** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:19`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L19) | Classical result in operational notation | `GATE-I01-A` |
| `2` | **Theorem I.1.0b** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:67`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L67) | Original proved result of this book | `GATE-I01-A` |
| `3` | **Lemma I.1.1** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:139`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L139) | Extension of a classical theorem within contract Γ | `GATE-I01-A` |
| `4` | **Theorem I.1.1** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:150`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L150) | Extension of a classical theorem within contract Γ | `GATE-I01-B` |
| `5` | **Theorem I.1.2** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:178`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L178) | Original proved result of this book | `GATE-I01-B` |
| `6` | **Theorem I.1.3** | [`01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:213`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L213) | Extension of a classical theorem within contract Γ | `GATE-I01-B` |
| `7` | **Theorem I.2.1** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:65`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L65) | Extension of a classical theorem within contract Γ | `GATE-I02-A` |
| `8` | **Theorem I.2.2** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:79`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L79) | Extension of a classical theorem within contract Γ | `GATE-I02-A` |
| `9` | **Lemma I.2.1** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:98`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L98) | Proved prohibition / counterexample | `GATE-I02-A` |
| `10` | **Theorem I.2.3** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:115`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L115) | Extension of a classical theorem within contract Γ | `GATE-I02-A` |
| `11` | **Lemma I.2.2** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:154`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L154) | Original proved result of this book | `GATE-I02-B` |
| `12` | **Theorem I.2.4** | [`02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:201`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L201) | Original proved result of this book | `GATE-I02-B` |
| `13` | **Lemma I.3.1** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:80`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L80) | Extension of a classical theorem within contract Γ | `GATE-I03-A` |
| `14` | **Lemma I.3.2** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:90`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L90) | Extension of a classical theorem within contract Γ | `GATE-I03-A` |
| `15` | **Theorem I.3.1** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:109`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L109) | Extension of a classical theorem within contract Γ | `GATE-I03-A` |
| `16` | **Lemma I.3.3** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:141`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L141) | Extension of a classical theorem within contract Γ | `GATE-I03-A` |
| `17` | **Lemma I.3.4** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:154`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L154) | Extension of a classical theorem within contract Γ | `GATE-I03-A` |
| `18` | **Theorem I.3.2** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:178`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L178) | Extension of a classical theorem within contract Γ | `GATE-I03-B` |
| `19` | **Lemma I.3.5** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:201`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L201) | Original proved result of this book | `GATE-I03-B` |
| `20` | **Lemma I.3.6** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:217`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L217) | Proved prohibition / counterexample | `GATE-I03-B` |
| `21` | **Theorem I.3.3** | [`03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:239`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L239) | Original proved result of this book | `GATE-I03-B` |
| `22` | **Theorem I.4.1** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:39`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L39) | Extension of a classical theorem within contract Γ | `GATE-I04-A` |
| `23` | **Theorem I.4.2** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:57`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L57) | Original proved result of this book | `GATE-I04-A` |
| `24` | **Theorem I.4.3** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:90`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L90) | Extension of a classical theorem within contract Γ | `GATE-I04-B` |
| `25` | **Lemma I.4.1** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:106`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L106) | Classical result in operational notation | `GATE-I04-A` |
| `26` | **Lemma I.4.2** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:115`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L115) | Proved prohibition / counterexample | `GATE-I04-B` |
| `27` | **Lemma I.4.3** | [`04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:143`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L143) | Extension of a classical theorem within contract Γ | `GATE-I04-B` |
| `28` | **Theorem I.5.1** | [`05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:77`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L77) | Extension of a classical theorem within contract Γ | `GATE-I05-A` |
| `29` | **Theorem I.5.2** | [`05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:178`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L178) | Proved prohibition / counterexample | `GATE-I05-B` |
| `30` | **Proposition I.5.1** | [`05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:218`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L218) | Classical result in operational notation | `GATE-I05-B` |
| `31` | **Theorem I.5.3** | [`05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:271`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L271) | Extension of a classical theorem within contract Γ | `GATE-I05-B` |
| `32` | **Theorem I.6.1** | [`06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:69`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L69) | Extension of a classical theorem within contract Γ | `GATE-I06-A` |
| `33` | **Lemma I.6.1** | [`06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:94`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L94) | Classical result in operational notation | `GATE-I06-A` |
| `34` | **Theorem I.6.2** | [`06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:154`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L154) | Extension of a classical theorem within contract Γ | `GATE-I06-B` |
| `35` | **Theorem I.6.3** | [`06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:193`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L193) | Original proved result of this book | `GATE-I06-B` |
| `36` | **Theorem I.6.4** | [`06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:211`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L211) | Original proved result of this book | `GATE-I06-B` |
| `37` | **Proposition I.7.1** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:44`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L44) | Classical result in operational notation | `GATE-I07-A` |
| `38` | **Theorem I.7.1** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:130`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L130) | Original proved result of this book | `GATE-I07-A` |
| `39` | **Theorem I.7.2** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:157`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L157) | Classical result in operational notation | `GATE-I07-B` |
| `40` | **Theorem I.7.3** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:191`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L191) | Original proved result of this book | `GATE-I07-B` |
| `41` | **Proposition I.7.2** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:227`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L227) | Classical result in operational notation | `GATE-I07-B` |
| `42` | **Lemma I.7.1** | [`07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:241`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L241) | Classical result in operational notation | `GATE-I07-B` |
| `43` | **Theorem I.8.1** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:35`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L35) | Classical result in operational notation | `GATE-I08-A` |
| `44` | **Lemma I.8.1** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:129`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L129) | Original proved result of this book | `GATE-I08-A` |
| `45` | **Lemma I.8.2** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:141`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L141) | Original proved result of this book | `GATE-I08-A` |
| `46` | **Theorem I.8.2** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:159`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L159) | Original proved result of this book | `GATE-I08-A` |
| `47` | **Theorem I.8.3** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:212`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L212) | Classical result in operational notation | `GATE-I08-B` |
| `48` | **Lemma I.8.3** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:253`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L253) | Extension of a classical theorem within contract Γ | `GATE-I08-B` |
| `49` | **Proposition I.8.1** | [`08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:290`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L290) | Original proved result of this book | `GATE-I08-B` |
| `50` | **Proposition I.9.1** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:57`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L57) | Proved prohibition / counterexample | `GATE-I09-A` |
| `51` | **Theorem I.9.1** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:100`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L100) | Extension of a classical theorem within contract Γ | `GATE-I09-A` |
| `52` | **Theorem I.9.2** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:111`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L111) | Extension of a classical theorem within contract Γ | `GATE-I09-A` |
| `53` | **Lemma I.9.1** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:158`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L158) | Classical result in operational notation | `GATE-I09-A` |
| `54` | **Theorem I.9.3** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:217`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L217) | Original proved result of this book | `GATE-I09-A` |
| `55` | **Theorem I.9.3a** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:227`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L227) | Original proved result of this book | `GATE-I09-A` |
| `56` | **Proposition I.9.2** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:267`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L267) | Extension of a classical theorem within contract Γ | `GATE-I09-B` |
| `57` | **Theorem I.9.4** | [`09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:285`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L285) | Extension of a classical theorem within contract Γ | `GATE-I09-B` |
| `58` | **Theorem II.1.1** | [`01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:201`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L201) | Extension of a classical theorem within contract Γ | `GATE-II01-02` |
| `59` | **Theorem II.1.2** | [`01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:220`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L220) | Classical result in operational notation | `GATE-II01-03` |
| `60` | **Proposition II.1.1** | [`01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:279`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L279) | Extension of a classical theorem within contract Γ | `GATE-II01-04` |
| `61` | **Proposition II.1.2** | [`01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:312`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L312) | Extension of a classical theorem within contract Γ | `GATE-II01-05` |
| `62` | **Lemma II.2.1** | [`02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:21`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L21) | Extension of a classical theorem within contract Γ | `GATE-II02-01` |
| `63` | **Proposition II.2.1** | [`02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:88`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L88) | Extension of a classical theorem within contract Γ | `GATE-II02-02` |
| `64` | **Theorem II.2.1** | [`02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:143`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L143) | Classical result in operational notation | `GATE-II02-03` |
| `65` | **Lemma II.2.2** | [`02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:191`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L191) | Classical result in operational notation | `GATE-II02-03` |
| `66` | **Proposition II.2.2** | [`02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:229`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L229) | Classical result in operational notation | `GATE-II02-04` |
| `67` | **Lemma II.3.1** | [`03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:66`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L66) | Classical result in operational notation | `GATE-II03-01` |
| `68` | **Theorem II.3.1** | [`03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:123`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L123) | Original proved result of this book | `GATE-II03-02` |
| `69` | **Theorem II.3.2** | [`03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:217`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L217) | Classical result in operational notation | `GATE-II03-03` |
| `70` | **Theorem II.4.1** | [`04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:86`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L86) | Original proved result of this book | `GATE-II04-01` |
| `71` | **Proposition II.4.1** | [`04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:154`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L154) | Extension of a classical theorem within contract Γ | `GATE-II04-02` |
| `72` | **Theorem II.4.2** | [`04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:177`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L177) | Classical result in operational notation | `GATE-II04-03` |
| `73` | **Theorem II.5.1** | [`05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:49`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L49) | Classical result in operational notation | `GATE-II05-01` |
| `74` | **Theorem II.5.2** | [`05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:109`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L109) | Extension of a classical theorem within contract Γ | `GATE-II05-02, GATE-II05-03` |
| `75` | **Proposition II.5.1** | [`05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:186`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L186) | Classical result in operational notation | `GATE-II05-04` |
| `76` | **Proposition II.5.2** | [`05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:216`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L216) | Classical result in operational notation | `GATE-II05-04` |
| `77` | **Theorem II.6.1** | [`06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:85`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L85) | Original proved result of this book | `GATE-II06-01` |
| `78` | **Proposition II.6.1** | [`06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:134`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L134) | Extension of a classical theorem within contract Γ | `GATE-II06-02, GATE-II06-03` |
| `79` | **Theorem II.6.2** | [`06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:170`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L170) | Classical result in operational notation | `GATE-II06-03, GATE-II06-04` |
| `80` | **Proposition II.7.1** | [`07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:23`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L23) | Classical result in operational notation | `GATE-II07-01` |
| `81` | **Theorem II.7.1** | [`07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:42`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L42) | Extension of a classical theorem within contract Γ | `GATE-II07-01` |
| `82` | **Theorem II.7.2** | [`07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:87`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L87) | Classical result in operational notation | `GATE-II07-02` |
| `83` | **Theorem II.7.3** | [`07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:155`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L155) | Extension of a classical theorem within contract Γ | `GATE-II07-03, GATE-II07-04` |
| `84` | **Proposition II.8.1** | [`08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:55`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L55) | Classical result in operational notation | `GATE-II08-01` |
| `85` | **Theorem II.8.1** | [`08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:103`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L103) | Extension of a classical theorem within contract Γ | `GATE-II08-02` |
| `86` | **Theorem II.8.2** | [`08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:175`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L175) | Original proved result of this book | `GATE-II08-04` |
| `87` | **Theorem II.9.1** | [`09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md:42`](Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md#L42) | Extension of a classical theorem within contract Γ | `GATE-II09-01` |
| `88` | **Theorem II.9.2** | [`09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md:87`](Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md#L87) | Original proved result of this book | `GATE-II09-02, GATE-II09-03` |
| `89` | **Proposition III.1.1** | [`01_CHAPTER_III_01_HOW_TO_CONSTRUCT_A_DOMAIN_BRIDGE_V3_3_EN.md:80`](Book_III_EN/01_CHAPTER_III_01_HOW_TO_CONSTRUCT_A_DOMAIN_BRIDGE_V3_3_EN.md#L80) | Proved prohibition / counterexample | `GATE-III01-01, GATE-III01-02` |
| `90` | **Lemma III.2.1** | [`02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md:15`](Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md#L15) | Proved prohibition / counterexample | `GATE-III02-01` |
| `91` | **Proposition III.2.1** | [`02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md:84`](Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md#L84) | Extension of a classical theorem within contract Γ | `GATE-III02-02, GATE-III02-03` |
| `92` | **Proposition III.3.1** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:17`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L17) | Extension of a classical theorem within contract Γ | `GATE-III03-01` |
| `93` | **Lemma III.3.1** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:36`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L36) | Original proved result of this book | `GATE-III03-01` |
| `94` | **Theorem III.3.1** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:85`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L85) | Two-arrow structural correspondence (bridge) | `GATE-III01-02, GATE-III03-02` |
| `95` | **Lemma III.3.2** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:122`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L122) | Proved prohibition / counterexample | `GATE-III03-02` |
| `96` | **Theorem III.3.2** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:141`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L141) | Original proved result of this book | `GATE-III03-03` |
| `97` | **Proposition III.3.2** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:176`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L176) | Original proved result of this book | `GATE-III03-04` |
| `98` | **Lemma III.3.3** | [`03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:193`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L193) | Original proved result of this book | `GATE-III03-04` |
| `99` | **Lemma III.4.1** | [`04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:23`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L23) | Original proved result of this book | `GATE-III04-01` |
| `100` | **Theorem III.4.1** | [`04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:40`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L40) | Extension of a classical theorem within contract Γ | `GATE-III04-02` |
| `101` | **Theorem III.4.2** | [`04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:91`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L91) | Two-arrow structural correspondence (bridge) | `GATE-III04-03` |
| `102` | **Theorem III.5.1** | [`05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md:26`](Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md#L26) | Extension of a classical theorem within contract Γ | `GATE-III05-01` |
| `103` | **Lemma III.5.1** | [`05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md:50`](Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md#L50) | Classical result in operational notation | `GATE-III05-01` |

---

## 3. Article-by-Article Cards of the 103 Statements (Separating Classical Foundation and Contribution of This Book)

### 1. Theorem I.1.0a

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:19`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L19)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-A`
- *Classical foundation.* Partitioning a set by the kernel of a map $\mathrm{Eq}(q)$ and its invariance under injective renaming of the output scale $\tau \circ q$—elementary set theory. *Contribution of this book:* Primacy of the partition $\mathrm{Eq}(q)$ over answer labels as the opening rule of the operational scene contract, together with a finite counterexample of coarsening under non-injective $\tau$.

### 2. Theorem I.1.0b

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:67`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L67)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-A`
- *Classical foundation.* Boolean conditions on finite maps and pairwise counterexamples of axiom independence—classical axiomatic method. *Contribution of this book:* Exact hierarchy and pairwise independence of the operational triads $(Z_D, Z_C, Z_F)$ and $(C_{\mathrm{div}}, C_{\mathrm{type}}, C_{\mathrm{step}})$ with minimal finite failure witnesses.

### 3. Lemma I.1.1

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:139`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L139)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-A`
- *Classical foundation.* Canonical factorization of a map through its equivalence kernel and criterion for descending an operation onto a congruence—standard universal algebra. *Contribution of this book:* Separating the set-theoretic pair kernel $\mathrm{Eq}(q)$ from the algebraic zero preimage $\ker_{\mathrm{alg}}(q)$ and explicit failure of quotient descent on the saturating semigroup $(\{0,1,2,3\}, \oplus_{\mathrm{sat}})$.

### 4. Theorem I.1.1

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:150`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L150)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-B`
- *Classical foundation.* Joint map into the Cartesian product of two binary scales $\{0,1\}^2$ and counting four intersection cells—elementary finite combinatorics. *Contribution of this book:* Criterion for the birth of the minimal four-state polar cell $S_4$ from a pair of independent binary questions and exact fraction `24/256` of question pairs on a four-point carrier.

### 5. Theorem I.1.2

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:178`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L178)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-B`
- *Classical foundation.* The affine group $\mathbb{F}_2^2 \rtimes \mathrm{GL}_2(2)$, free transitive actions ($\mathbb{F}_2$-torsors), and Belnap's four-valued lattice $\mathcal{F}_4$—classical finite algebra and logic. *Contribution of this book:* Simultaneous triad of equally rightful `2+2` partitions $(q_x, q_c, \beta = x \oplus c)$, mutual decoders $d_c, d_x$ on a fixed support, contrast between involutions $\sigma$ (`0` fixed points) and $\mathrm{swap}$ (`2`), and non-coincidence of Boolean difference with scalar difference on $\mathcal{F}_4$.

### 6. Theorem I.1.3

- **Location in the three-volume monograph:** [`Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md:213`](Book_I_EN/01_CHAPTER_I_01_OPERATIONAL_CONTRACT_QUESTION_AND_FOUR_STATE_SCENE_V3_3_EN.md#L213)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I01-B`
- *Classical foundation.* The construction $L \times_K R$ is the classical fibered product (pullback) in the category of sets $\mathbf{Set}$, and its universal property is standard. *Contribution of this book:* Reading the pullback as a coupled whole of two observers sharing a seam ($8$ joint states of the cube $Q_3$ inside $16$ pairs of $S_4 \times S_4$) and criterion for unique descent of a compatible pair of steps.

### 7. Theorem I.2.1

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:65`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L65)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-A`
- *Classical foundation.* Laws of composition of partial maps are properties of the classical category $\mathbf{Par}$ (equivalent to pointed sets); relative complement of domains of definition is Boolean algebra of subsets. *Contribution of this book:* Contravariant transfer of readings $T^\sharp q$ along a partial step separating blocking $\bot_A \notin X$ from the false answer $0$, plus exact criterion of joint partial descent.

### 8. Theorem I.2.2

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:79`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L79)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-A`
- *Classical foundation.* The calculus of binary relations goes back to Peirce–Schröder–Tarski relation algebra (category $\mathbf{Rel}$), and the adjunction $\exists_R \dashv \forall_R$ is a classical Galois connection (Lawvere, 1969). *Contribution of this book:* Strict typing of modal preimages $\exists_R, \forall_R$ by reading direction and minimal counterexamples on dead-end states showing where replacing $\forall_R$ by $R^{-1}$ breaks the adjunction.

### 9. Lemma I.2.1

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:98`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L98)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-A`
- *Classical foundation.* Composition of binary relations over the Boolean semiring vs. integer multiplication of path matrices—standard distinction between categories $\mathbf{Rel}$ and $\mathbf{Mat}_{\mathbb{Z}}$. *Contribution of this book:* Explicit finite witness of path-multiplicity erasure (`2 → 1`) under relational composition that forgets an intermediate seam.

### 10. Theorem I.2.3

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:115`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L115)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-A`
- *Classical foundation.* The adjoint triad $\exists_\pi \dashv \pi^* \dashv \forall_\pi$ and the Beck–Chevalley base-change condition along a pullback square—classical categorical logic (Lawvere, 1969; Bell, 1988). *Contribution of this book:* Operational definition of the shadow boundary $\partial_\pi(S) = (\exists_\pi S \cap \mathrm{im}\,\pi) \setminus \forall_\pi S$, saturation criterion $S = \pi^{-1}(\pi(S))$ (`4/16` on $S_4$), and counterexamples when surjectivity of $\pi$ or the pullback condition is dropped.

### 11. Lemma I.2.2

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:154`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L154)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-B`
- *Classical foundation.* Zhegalkin algebraic normal form (1927) of Boolean functions on $\mathbb{F}_2^2$ and laws of contraposition in classical propositional calculus. *Contribution of this book:* Filtration `16 → 8 → 6` of predicates on $S_4$ (all functions / affine / balanced non-constant) and exact boundary between classical reasoning inside a fixed slice `L.1` and `6/16` failures of naive contraposition under a partial step.

### 12. Theorem I.2.4

- **Location in the three-volume monograph:** [`Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md:201`](Book_I_EN/02_CHAPTER_I_02_PARTIAL_ACTIONS_RELATIONS_AND_QUESTION_TRANSFER_V3_3_EN.md#L201)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I02-B`
- *Classical foundation.* Parallel transport around a closed circuit, holonomy on a two-sheeted fiber, and transposition of linear operators in the dual space. *Contribution of this book:* Explicit holonomy formula $H_3 = \mathrm{swap}^\kappa$ ($\kappa = x_0 \oplus c_0 \oplus b_0$) on the triangle of two-point regime slices of $S_4$, exact violation counts `3200 / 2688 / 2560` out of `9216` for naive transitivity, and duality $F_\alpha / F_\alpha^\top$.

### 13. Lemma I.3.1

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:80`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L80)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-A`
- *Classical foundation.* Coincidence of word and adaptive indistinguishability for deterministic transitions—classical theorem of automaton experiment theory (Moore, 1956). *Contribution of this book:* Extension of the equivalence between unconditional and adaptive indistinguishability to scenes with partial actions $\mathrm{Dom}(T_a)$ and partial readings, plus refinement `4 → 5 → 6` on the octahedral carrier $V_6$.

### 14. Lemma I.3.2

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:90`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L90)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-A`
- *Classical foundation.* Invariant subsets and absorbing fibers of dynamical systems and finite automata. *Contribution of this book:* Criterion for invariance of the active zero fiber under an admissible transition library and separation of dynamically silent microstates from the observable future.

### 15. Theorem I.3.1

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:109`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L109)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-A`
- *Classical foundation.* The minimal quotient $X / {\sim_\Gamma}$ is the classical Myhill (1957) – Nerode (1958) congruence and Moore automaton minimization (1956); its universality is standard. *Contribution of this book:* Separating descent of static reading from autonomous descent of partial transitions, exact stabilization bound $k_* \le \max(|X|-1, 0)$, and dual description via the counter-directed tower of Boolean subalgebras $B_k$.

### 16. Lemma I.3.3

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:141`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L141)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-A`
- *Classical foundation.* Duality between finite partitions and atomic Boolean subalgebras, and reduction of Mealy automata to Moore automata—classical automata theory. *Contribution of this book:* Synchronous anti-isomorphism $\mathrm{Atoms}(B_k) = X/{\sim_k}$ for contracts with partial steps, partial readings, and instantaneous Mealy outputs (`256 + 625 + 6561` verified machines).

### 17. Lemma I.3.4

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:154`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L154)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-A`
- *Classical foundation.* Cylindrical closure and natural join of projections in relational algebra (Codd, 1970). *Contribution of this book:* Exact criterion for lossless set reconstruction from a family of windows and quantitative counterexamples of cylindrical inflation (`16 vs 32` on $Q_3^2$ and `64 vs 65` on $Q_4^2$).

### 18. Theorem I.3.2

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:178`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L178)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-B`
- *Classical foundation.* Criterion for existence of an induced Markov kernel on a quotient is the classical Kemeny–Snell lumpability condition (1960); telescoping total-variation bound is standard. *Contribution of this book:* Reading strict lumpability as a requirement on the observer's quotient memory, explicit 7-state counterexample of trace equivalence without lumpability, and witness $\mathrm{TV} = 1$ under coinciding one-dimensional marginals.

### 19. Lemma I.3.5

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:201`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L201)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-B`
- *Classical foundation.* Cartesian products of graphs $K_2 \square P_3$, step-by-step partition refinement, and Markov lumpability verification—standard finite constructions. *Contribution of this book:* Explicit 64-state six-bit testbed $X_{64} = (\mathbb{F}_2^2)^3$ exhibiting the Nerode refinement staircase `4 → 6 → 8 → 8`, active corridor $K_2 \square P_3$, and breakdown of quotient descent under asymmetric perturbation.

### 20. Lemma I.3.6

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:217`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L217)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-B`
- *Classical foundation.* Point separation by a family of functions vs. completeness of linear observables on the space of signed measures (finite-dimensional linear algebra). *Contribution of this book:* Minimal four-point counterexample $S_4$: the pair of coordinate windows $(q_x, q_c)$ uniquely separates all $4$ points yet has rank $3 < 4$ on distributions (`24` pairs of indistinguishable laws with an invisible parity kernel $\beta$).

### 21. Theorem I.3.3

- **Location in the three-volume monograph:** [`Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md:239`](Book_I_EN/03_CHAPTER_I_03_WHAT_IT_MEANS_TO_PRESERVE_ALL_FUTURE_DISTINCTIONS_V3_3_EN.md#L239)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I03-B`
- *Classical foundation.* Full transformation monoid $\mathcal{T}_4$ of cardinality $4^4 = 256$ and structural classes of Green's relations (Green, 1951). *Contribution of this book:* Exhaustive decomposition `256 = 64 + 96 + 96` (`96 = 48 + 36 + 12`) of all endomorphisms of the cell $S_4$ relative to the window $q_x$ into memory-preserving (`64`), memory-doubling (`96`), and autonomy-breaking maps.

### 22. Theorem I.4.1

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:39`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L39)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-A`
- *Classical foundation.* Distinction between open-loop and closed-loop control in automata theory and reversible computation with history retention (Bennett, 1973; Toffoli, 1980). *Contribution of this book:* Strict separation of feedback from a program tape already on `Fin 2` and contrast between the order-`4` reversible trace gate $T_{\mathrm{rev}}$ (`8 → 8`, cycles `1+1+2+4`) and erasing overwrite $T_{\mathrm{ret}}$ (`8 → 4`) on $S_8$.

### 23. Theorem I.4.2

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:57`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L57)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-A`
- *Classical foundation.* Pigeonhole–Moore state-count lower bounds, synthesis of finite feedback automata, and orthogonal cyclic Latin squares over $\mathbb{Z}/3\mathbb{Z}$. *Contribution of this book:* Exact memory bounds in a restricted library on the grid $D_M^2$: $C_{\min}(\mathrm{A}) = 11$ ($M=7$), general formula $C_{\min}(D_M) = 2M + 5$ ($19$ at $M=7$, class `B`), and closed-form constructive realizations $Q_{11}, Q_{19}$ (via squares $A_{(u+w)\bmod 3}, B_{(-u+w)\bmod 3}$), and $Q_{22}$ (`139` commands).

### 24. Theorem I.4.3

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:90`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L90)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-B`
- *Classical foundation.* The code of pairwise comparisons is the classical binary linear `[6, 3, 3]_2` cut-space code of the complete graph $K_4$, equivalent to the shortened `[7, 4, 3]_2` Hamming code (weight enumerator $1 + 4z^3 + 3z^4$). *Contribution of this book:* Exact model of three-layer equivariant single-error correction linking four site values, polling permutations in $\mathfrak{S}_4$ (`384` signed-permutation symmetries), and the comparison syndrome.

### 25. Lemma I.4.1

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:106`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L106)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-A`
- *Classical foundation.* Factorization of a map $u_* : R \to U$ through a projection $q : X \to Y$ if and only if $\mathrm{Eq}(q)|_R \subseteq \mathrm{Eq}(u_*)$—standard descent lemma for maps. *Contribution of this book:* Interpreting violation of kernel inclusion $\mathrm{Eq}(q)|_R \nsubseteq \mathrm{Eq}(u_*)$ as the exact operational threshold forcing an internal controller memory register $Q$.

### 26. Lemma I.4.2

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:115`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L115)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-B`
- *Classical foundation.* Non-transitivity of threshold proximity relations (Poincaré–Zeeman–Bell chains) and telescoping total-variation bounds for Markov kernels. *Contribution of this book:* Counterexample `{0, 3/5, 6/5}` refuting quotient partitioning by approximate tolerance, paired with an exact rational bound on trajectory divergence over horizon $H$.

### 27. Lemma I.4.3

- **Location in the three-volume monograph:** [`Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md:143`](Book_I_EN/04_CHAPTER_I_04_EXECUTOR_FEEDBACK_AND_FULL_COST_V3_3_EN.md#L143)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I04-B`
- *Classical foundation.* Shifting arc costs by vertex-potential differences $c'(u,v) = c(u,v) + \phi(u) - \phi(v)$ is classical potential reweighting (Gallai, 1958; Johnson, 1977); constant maps are left zeros in $\mathrm{End}(X)$. *Contribution of this book:* Proof of gauge non-recoverability of step costs from closed-cycle sums, connection of irreversible reset with the monoid left zero (`19 683` triples), and pairwise irreducibility of the five coordinates of the cost vector $\mathcal{C}$.

### 28. Theorem I.5.1

- **Location in the three-volume monograph:** [`Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:77`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L77)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I05-A`
- *Classical foundation.* Absence of non-zero additive inverses in the idempotent Boolean monoid $(2^X, \cup, \varnothing)$ and universal property of the free abelian group $\mathbb{Z}[X]$ on $X$. *Contribution of this book:* Strict derivation of the signed endowment boundary `B1` from the requirement of mutual contribution cancellation, functoriality $\mathbb{Z}[T_2 \circ T_1] = \mathbb{Z}[T_2]\mathbb{Z}[T_1]$, and explicit failure of associativity under nonlinear `clamp` truncation.

### 29. Theorem I.5.2

- **Location in the three-volume monograph:** [`Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:178`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L178)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-I05-B`
- *Classical foundation.* Monotonicity of matrix multiplication over the Boolean semiring $(\{0,1\}, \lor, \land)$ vs. signed path sums over the ring $\mathbb{Z}$ (signed graphs, Zaslavsky, 1982). *Contribution of this book:* `Ban-Go` prohibition theorem: non-existence of a Boolean support operation $s(A_2 A_1) = F(s(A_2), s(A_1))$ due to antiphase cancellation of two open paths, plus path revival upon inserting a shutter.

### 30. Proposition I.5.1

- **Location in the three-volume monograph:** [`Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:218`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L218)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I05-B`
- *Classical foundation.* Real-integer matrix embedding of the ring of Gaussian integers $\mathbb{Z}[i] \hookrightarrow \mathrm{Mat}_2(\mathbb{Z})$ via the quarter-turn matrix $J_{\mathbb{Z}} = \bigl(\begin{smallmatrix}0 & -1\\ 1 & 0\end{smallmatrix}\bigr)$. *Contribution of this book:* Realization of the exact phase quarter-turn law $J_{\mathbb{Z}}^2 = -I_2$ on a pair of integer channels $\mathbb{Z}^2$ without introducing $\mathbb{C}$ or $\mathbb{R}$, contrasted with the absence of roots $z^2 = -1$ in a single channel $\mathbb{Z}$.

### 31. Theorem I.5.3

- **Location in the three-volume monograph:** [`Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md:271`](Book_I_EN/05_CHAPTER_I_05_SIGN_COMPLEMENT_AND_ADDITION_OF_CONTRIBUTIONS_V3_3_EN.md#L271)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I05-B`
- *Classical foundation.* The map $H(a,b) = (a+b, a-b)$ is given by the classical order-2 Hadamard–Sylvester matrix (Sylvester, 1867); its Smith invariant factors (H. Smith, 1861) equal $1$ and $2$, whence index $2$ of the image and rank drop modulo $2$. *Contribution of this book:* Reading the even checkerboard sublattice $\mathcal{L} \subset \mathbb{Z}^2$ as the exact image $H(\mathbb{Z}^2)$, non-invertibility of the restriction $H|_{\mathcal{L}}$ over $\mathbb{Z}$ (witness $(1,1) \in \mathcal{L} \setminus 2\mathbb{Z}^2$), and rank drop to `1` over $\mathbb{F}_2$ motivating the localization $\mathbb{Z}[1/2]$ in Book II.

### 32. Theorem I.6.1

- **Location in the three-volume monograph:** [`Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:69`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L69)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I06-A`
- *Classical foundation.* Cycle and cut spaces of a graph are Kirchhoff's classic (1847); $O_6$ is the line graph $L(K_4)$, and the identity $M M^\top = N^\top N$ over $\mathbb{F}_2$ relates the incidence matrix to the line-graph adjacency matrix. *Contribution of this book:* Pairwise non-isomorphism of the graphs `3K_2, O_6, C_6, 2C_3` on the shared carrier $A_6$ of balanced questions of $S_4$, non-isomorphism $L(Q_3) \not\cong L(O_6)$, face split `8 = 4 + 4` of $O_6$, and binary bicycle code `[12, 3, 6]_2`.

### 33. Lemma I.6.1

- **Location in the three-volume monograph:** [`Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:94`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L94)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I06-A`
- *Classical foundation.* The hyperoctahedral group $W(B_3)$ of order $48$, the general linear group $\mathrm{GL}_2(\mathbb{F}_3)$ of order $48$, and the binary octahedral group $2O \subset \mathrm{SL}_2(\mathbb{F}_9)$—classical finite group theory. *Contribution of this book:* Separating three non-isomorphic groups of the same cardinality `48` purely by the operational invariant of order-`2` element counts (`19`, `13`, and the unique central involution `1` in $2O$).

### 34. Theorem I.6.2

- **Location in the three-volume monograph:** [`Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:154`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L154)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I06-B`
- *Classical foundation.* The Petersen graph is the classical Kneser graph $KG(5,2)$ (Petersen, 1898; Kneser, 1955; Lovász, 1978), strongly regular with parameters $(10, 3, 0, 1)$; its symplectic model in $W(3,2)$ and Klein correspondence in $\mathrm{PG}(5,2)$ belong to classical finite geometry. *Contribution of this book:* Carving out $KG(5,2)$ as the complement of a five-point elliptic ovoid $O_5$ in $W(3,2)$ (`15 - 5 = 10`), two-sheeted bipartite Desargues cover $KG(5,2) \times K_2$ without a global section, and proof of natural role-descent failure $KG(5,2) \not\to O_6$.

### 35. Theorem I.6.3

- **Location in the three-volume monograph:** [`Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:193`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L193)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I06-B`
- *Classical foundation.* The rows of the incidence operator of the Fano plane $\mathrm{PG}(2,2)$ over $\mathbb{F}_2$ generate the classical `[7, 4, 3]_2` Hamming code (1950), orthogonal to the `[7, 3, 4]_2` simplex code; the Levi graph of $\mathrm{PG}(2,2)$ is the Heawood graph $H_{14}$. *Contribution of this book:* Exact sequence $\nu_W \circ \delta_7 = 0$ with rank-`3` syndrome $\nu_W = J_7 \oplus \delta_7$, $|\det_{\mathbb{Z}} \delta_7| = 24$ (`24` matchings of $H_{14}$), Fano book in $\mathrm{PG}(3,2)$ (`120 = 15 × 8`), and explicit enumeration of all $2^{12} = 4096$ linear right sections of $\delta_4$.

### 36. Theorem I.6.4

- **Location in the three-volume monograph:** [`Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md:211`](Book_I_EN/06_CHAPTER_I_06_GRAPHS_FINITE_FIELDS_AND_STRUCTURES_ON_A_SINGLE_CARRIER_V3_3_EN.md#L211)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I06-B`
- *Classical foundation.* Existence of permutation square roots by parity of even-cycle counts and orbit counting via the Cauchy–Frobenius (Burnside) lemma—classical combinatorial group theory. *Contribution of this book:* Contrast in solvability of the phase equation $J^2 = C_{2m}$ in $\mathfrak{S}_{2m}$ (`0` roots at $2m=6$ vs. `12` roots at $2m=8$) and exact hierarchy of orbit compression on $\mathbb{F}_2^7$ under $C_7 \subset \mathrm{Frob}_{21} \subset \mathrm{GL}_3(2)$ (`20 → 12 → 10` and `18 → 10 → 8`).

### 37. Proposition I.7.1

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:44`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L44)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-A`
- *Classical foundation.* Non-isomorphism of the singly generated additive monoid $(\mathbb{N}, +, 0)$ and the freely countably generated multiplicative monoid $(\mathbb{N}_+, \cdot, 1)$, plus distributivity of the divisor lattice $D(N)$—classical arithmetic. *Contribution of this book:* Comparison of additive and divisor graphs on the shared four-element carrier $\{1,2,3,6\}$ ($P_3 \sqcup K_1$ vs. $Q_2$) and Booleanness criterion $D(N) \iff \mu(N) \ne 0$ with complement failure on squared floors of $D(12)$ and $D(45)$.

### 38. Theorem I.7.1

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:130`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L130)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-A`
- *Classical foundation.* Elementary counting of even, prime, and odd composite integers on an initial segment $\{1,\dots,N\}$ of the natural numbers. *Contribution of this book:* Exact balance identity $m = \pi(2m) + c_{\mathrm{odd}}(2m)$ and complete proof that the equilibrium window $2(1 + \pi(N)) = N$ cuts out across all of $\mathbb{N}$ precisely the three integers $N \in \{10, 12, 14\}$ (corresponding to the unique odd composite $9$).

### 39. Theorem I.7.2

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:157`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L157)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-B`
- *Classical foundation.* The equation $x + y + z = xyz$ in natural numbers is a classical elementary Diophantine problem with the unique solution $\{1, 2, 3\}$ up to permutation. *Contribution of this book:* Model of how the solution count $|\mathcal{R}|$ shifts upon expanding the observer's carrier: the unique ordered triple $(1,2,3)$ in $\mathbb{N}_+^3$, $6$ permutations without ordering, and the infinite axial family $(-a, 0, a)$ upon passing to $\mathbb{Z}^3$.

### 40. Theorem I.7.3

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:191`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L191)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-B`
- *Classical foundation.* Factorization of the primorial $p\# = \prod_{q \le p} q$ into first-power primes and arithmetic of triangular numbers $T_p = p(p+1)/2$. *Contribution of this book:* Exact criterion for membership of the prime satellite $A(p) = p(p+1)/2$ in the Boolean divisor lattice of the primorial $D(p\#)$ via squarefreeness of the half-step $h(p) = (p+1)/2$, explaining the first squared breakdowns at $p = 7$ ($h=4$) and $p = 17$ ($h=9$).

### 41. Proposition I.7.2

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:227`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L227)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-B`
- *Classical foundation.* The Nagell–Ljunggren Diophantine equation $\frac{x^n - 1}{x - 1} = y^2$ and W. Ljunggren's theorem (1943) on squares among base-$3$ repunits. *Contribution of this book:* Interpretation of $(3^d - 1)/2$ as the count of projective axes in the ternary cube $\{-1,0,+1\}^d$, exact finite certification of squares `1, 4, 121` ($d \in \{1, 2, 5\}$) for $d \le 40$, and explicit separation of the external Diophantine reference `[Ljunggren 1943]` for all $d \ge 1$.

### 42. Lemma I.7.1

- **Location in the three-volume monograph:** [`Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md:241`](Book_I_EN/07_CHAPTER_I_07_ADDITION_AND_MULTIPLICATION_ADDITIVE_AND_DIVISOR_QUESTIONS_V3_3_EN.md#L241)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I07-B`
- *Classical foundation.* Finite multiplicative factorization over prime-power floors and Euler's pentagonal number theorem $\prod_{k \ge 1}(1 - t^k) = \sum_{m \in \mathbb{Z}} (-1)^m t^{m(3m-1)/2}$ in $\mathbb{Z}[[t]]$. *Contribution of this book:* Separating the exact finite identity in the window $D(N)$ over $\mathbb{Q}$ (`13/4 < 15/4` on $N=360$) and coefficientwise formal equality in $\mathbb{Z}[[t]]$ from illegitimate pointwise substitution $t = 1$ without a topology of convergence.

### 43. Theorem I.8.1

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:35`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L35)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-A`
- *Classical foundation.* Classical Chinese Remainder Theorem for coprime moduli and compatibility criterion for systems of congruences modulo non-coprime integers (Ore, 1952). *Contribution of this book:* Oracle-free observation contract on a composite modulus $N = pq$: separating the hidden torus isomorphism $\mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z}$ from the open Euclidean probe $\gcd(N, r)$ (`60` silent invertible residues vs. `16` axial hits on $N = 77$).

### 44. Lemma I.8.1

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:129`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L129)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-A`
- *Classical foundation.* $p$-adic valuations $v_p(x)$ and greatest-common-divisor algorithms in the ring of integers. *Contribution of this book:* Oracle-free primary saturation iteration $x_{k+1} = \gcd(N, x_k^2)$ doubling the valuations of all captured prime factors and reaching the full primary floor in at most $\lceil \log_2 \max_{p \mid N} v_p(N) \rceil$ steps.

### 45. Lemma I.8.2

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:141`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L141)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-A`
- *Classical foundation.* Arithmetic of $p$-adic minima and sums $\min(a+b, c)$ for greatest common divisors and least common multiples. *Contribution of this book:* Separation of three divisor-memory regimes of local windows $m_A, m_B \mid N$, counterexample of losing the squared floor on $N = 25$ from $(g_A, g_B)$ alone, and explicit 7-operation formula recovering $\gcd(N, r)$ when retaining the probe $r$.

### 46. Theorem I.8.2

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:159`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L159)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-A`
- *Classical foundation.* Distributivity of the divisor lattice $(D(N), \gcd, \operatorname{lcm})$ via prime-exponent valuations $v_p$. *Contribution of this book:* Sheaf-like gluing theorem for divisor windows: bijection $d \mapsto (\gcd(d, m_i))_i$ and inverse assembly $d = \operatorname{lcm}_i d_i$ between all divisors of $N$ and local families compatible on pairwise seams $\gcd(m_i, m_j)$ (`36 → 9` on $D(12) \times D(18)$).

### 47. Theorem I.8.3

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:212`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L212)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-B`
- *Classical foundation.* Kronecker's theorem (1881) on the equivalence between finite rank of an infinite Hankel matrix $H(a)_{i,j} = a_{i+j}$ and rationality of the generating series $\sum_{n \ge 0} a_n t^n = P(t)/Q(t)$. *Contribution of this book:* Reading the Hankel matrix as the linear counterpart of the Nerode quotient "past shifts vs. future delays" with exact formula $\mathrm{rk}_K H(a) = \max(\deg Q, \deg P + 1)$ for $P \ne 0$, accounting for the $+1$ transient-impulse shift.

### 48. Lemma I.8.3

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:253`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L253)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-B`
- *Classical foundation.* Vandermonde determinant of an exponential sum $s_n = \sum_{j=1}^r \lambda_j^n$ and rank reduction of integer matrices modulo a prime $p$. *Contribution of this book:* Mechanism of Hankel rank drop under collision of characteristic roots modulo $p$ (`[1, 2, 3, 3]` for $1^n + 2^n + 4^n$ over $\mathbb{F}_{2,3,5,7}$) and safeguard against stopping early at a spurious vanishing intermediate minor ($\Delta_2 = 14 \equiv 0 \pmod 7$ while $\Delta_3 = 36 \equiv 1 \pmod 7$).

### 49. Proposition I.8.1

- **Location in the three-volume monograph:** [`Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md:290`](Book_I_EN/08_CHAPTER_I_08_FINITE_WINDOWS_ORACLE_FREE_CONTRACT_AND_HANKEL_MATRICES_V3_3_EN.md#L290)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I08-B`
- *Classical foundation.* Arithmetic of finite prime fields $\mathbb{F}_p$, Gauss's law of quadratic reciprocity, and infinitude of primes satisfying $\left(\frac{13}{p}\right) = +1$. *Contribution of this book:* Complete dynamical analysis of the odd interpolation polynomial $K_2(u) = (u^3 - 7u)/6$ modulo $p$: single-step collapse of the entire field into the ternary core $\{-1,0,+1\}$ precisely for $p \in \{5, 7\}$, birth of the 4-cycle `5 → 4 → 6 → 7` at $p = 11$, and fixed points $u^2 \equiv 13 \pmod p$.

### 50. Proposition I.9.1

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:57`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L57)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* Pairwise consistency of projections in relational databases and sheaf theory vs. global compatibility and higher-order parity (XOR) constraints on $\mathbb{F}_2^3$. *Contribution of this book:* Paired minimal refutation of naive reductionism on the cube $\mathbb{F}_2^3$: the hollow triangle of three pairwise surjective windows with empty global intersection ($|\mathcal{R}| = 0$) and complete 2-invisibility of the even subspace $E_{\mathrm{even}}$ in all pairwise marginals ($|\mathcal{R}| > 1$).

### 51. Theorem I.9.1

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:100`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L100)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* The universal property of seam gluing is the classical universal property of the fibered product (pullback) in the category $\mathbf{Set}$. *Contribution of this book:* Criterion for a coupled step of two partial contracts without requiring a global endomorphism on the full seam scale $K$, plus exact condition for the birth of phantom pairs (`2 → 4`) upon seam coarsening.

### 52. Theorem I.9.2

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:111`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L111)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* Associativity of sequential gluing is the classical canonical isomorphism of iterated fibered products $(A \times_B C) \times_D E \cong A \times_B (C \times_D E)$. *Contribution of this book:* Transfer of canonical pullback associativity to chains of operational contracts together with their partial steps and readings (`64 → 16 = 16` trajectories), contrasted with path-multiplicity loss in relational composition.

### 53. Lemma I.9.1

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:158`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L158)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* Simplicial nerve of a finite cover (Alexandroff, 1928) and Čech coboundary complex $\delta_1 \circ \delta_0 = 0$ over $\mathbb{F}_2$ (Čech, 1932). *Contribution of this book:* Direct operational reading of 0-cochains as vertex gauges of local windows, 1-cocycles as edge shifts compatible on filled faces, and $H^1(\mathcal{N}; \mathbb{F}_2)$ as a gauge-invariant gluing obstruction.

### 54. Theorem I.9.3

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:217`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L217)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* Simplicial cohomology of two-dimensional cell and simplicial complexes over $\mathbb{F}_2$ and linear algebra of coboundary ranks. *Contribution of this book:* Construction of the nerve $\mathcal{N}$ of the six two-element slices of $S_4$ as a checkerboard octahedron (`6` vertices, `12` edges, `4` filled and `4` hollow faces) and exact computation $\mathrm{rk}\,\delta_0 = 5$, $\mathrm{rk}\,\delta_1 = 4$, $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$.

### 55. Theorem I.9.3a

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:227`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L227)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-A`
- *Classical foundation.* Presheaves of sets and $\mathbb{F}_2$-torsors (principal homogeneous bundles with structure group $\mathbb{F}_2$) over a simplicial nerve (Leray, 1945–1950). *Contribution of this book:* Backbone Theorem of Book I: exact equivalence between odd holonomy charge $\kappa = c_0 \oplus x_0 \oplus b_0 = 1$ from Chapter `I.2` and the `4` hollow faces of $\mathcal{N}$, plus explicit torsor presheaf $\mathcal{S}_w$ having `2` local sections everywhere and `0` global sections.

### 56. Proposition I.9.2

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:267`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L267)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-B`
- *Classical foundation.* Simplicial cohomology of the two-dimensional sphere $S^2 \cong \partial\Delta_4$: $H^1(\partial\Delta_4; \mathbb{F}_2) = 0$ and $H^2(\partial\Delta_4; \mathbb{F}_2) \cong \mathbb{F}_2$. *Contribution of this book:* Minimal finite model of a second-order obstruction: sealing all one-dimensional loops by four triangular faces kills $H^1$, yet an odd 2-cocycle $w = (0,0,0,1)$ yields `0` out of `64` solutions of $\delta_1 \eta = w$ vs. `8` solutions for an even face sum.

### 57. Theorem I.9.4

- **Location in the three-volume monograph:** [`Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md:285`](Book_I_EN/09_CHAPTER_I_09_PAIRWISE_COMPATIBILITY_GLUING_OBSTRUCTION_AND_SYNTHESIS_BOOK_I_V3_3_EN.md#L285)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-I09-B`
- *Classical foundation.* Criterion for existence of a left inverse map (retraction $U \circ F = \mathrm{id}_E$) on a non-empty set $E \ne \varnothing$ via injectivity of $F$—basic set and category theory. *Contribution of this book:* Concluding architectural dichotomy of Volume I between non-injective Nerode future-memory compression ($X \twoheadrightarrow X/{\sim_\Gamma}$, irreversible without a trace) and the reversible `Fold / Unfold` pair $F : E \hookrightarrow B \times H$ retaining an auxiliary history register $H$.

### 58. Theorem II.1.1

- **Location in the three-volume monograph:** [`Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:201`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L201)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II01-02`
- *Classical foundation.* Kalman's observability criterion for finite-dimensional linear systems (Kalman, 1960) and stabilization of ascending kernel filtrations via the Cayley–Hamilton theorem. *Contribution of this book:* Shifted-window observability formula $(C B^{j_0}, \dots, C B^{j_0+r-1})|_{W_0}$ under delay threshold $j_0$, separating zero single-slice response from joint injectivity over horizon $r$.

### 59. Theorem II.1.2

- **Location in the three-volume monograph:** [`Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:220`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L220)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II01-03`
- *Classical foundation.* The Ho–Kalman minimal linear realization theorem via block Hankel factorization (Ho and Kalman, 1966) and M. P. Schützenberger's theory of rational series (1961). *Contribution of this book:* Operational reading of the minimal state dimension $\dim V_{\min} = \operatorname{rank}\mathcal{H}_f$ as linear observer memory carrying the $\mathrm{GL}_r(K)$ basis gauge torsor ($|\mathcal{R}| > 1$).

### 60. Proposition II.1.1

- **Location in the three-volume monograph:** [`Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:279`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L279)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II01-04`
- *Classical foundation.* Walsh–Hadamard transform and character orthogonality on the elementary abelian group $\mathbb{F}_2^n$—classical harmonic analysis on the Boolean cube. *Contribution of this book:* Exact characterization of the $(2^n - n - 1)$-dimensional shadow kernel of a first-order linear projector, blind to all pure higher-order parities $k \ge 2$ (including $\beta = x \oplus c$ on $S_4$).

### 61. Proposition II.1.2

- **Location in the three-volume monograph:** [`Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md:312`](Book_II_EN/01_CHAPTER_II_01_HIDDEN_MEMORY_RETURNS_V3_3_EN.md#L312)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II01-05`
- *Classical foundation.* Permutation representations of the symmetric group $\mathfrak{S}_n$ and automorphism groups of path and cycle graphs. *Contribution of this book:* Symmetry reduction from full channel permutations $\mathfrak{S}_n$ to the dihedral or reflection subgroup once a nearest-neighbor quadratic step-energy functional is imposed.

### 62. Lemma II.2.1

- **Location in the three-volume monograph:** [`Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:21`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L21)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II02-01`
- *Classical foundation.* Formal resolvent identity $(I - wA)^{-1} = \sum_{k \ge 0} w^k A^k$ in formal power series $K[[w]]$ and the unilateral $Z$-transform of linear systems. *Contribution of this book:* Unconditional algebraic alignment of the delay indeterminate $w = 1/z$ with the Hankel windows of Book I, separated explicitly from the analytic convergence disk $|z| > \rho(A)$.

### 63. Proposition II.2.1

- **Location in the three-volume monograph:** [`Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:88`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L88)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II02-02`
- *Classical foundation.* Binary expansions on the circle $\mathbb{R}/\mathbb{Z}$ and the compact totally disconnected ring of $2$-adic integers $\mathbb{Z}_2$. *Contribution of this book:* Operational reading of the continuous surjection $\bar{\Phi} : \mathbb{Z}_2 \twoheadrightarrow \mathbb{R}/\mathbb{Z}$ as gluing indistinguishable binary tails ($0.0111\ldots_2 = 0.1000\ldots_2$), together with a proof that $\bar{\Phi}$ is not an additive group homomorphism.

### 64. Theorem II.2.1

- **Location in the three-volume monograph:** [`Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:143`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L143)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II02-03`
- *Classical foundation.* Cayley's rational transform $(I - \frac{h}{2}J_a)^{-1}(I + \frac{h}{2}J_a)$ (Cayley, 1846) and the $[1/1]$ diagonal Padé approximant to the matrix exponential $\exp(h J_a)$. *Contribution of this book:* Exact second-order jet agreement of the reversible rational step with $\exp(h J_a)$ without transcendental series, plus the exact cubic remainder coefficient $+\frac{1}{12}h^3 J_a^3$.

### 65. Lemma II.2.2

- **Location in the three-volume monograph:** [`Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:191`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L191)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II02-03`
- *Classical foundation.* Odd symmetry of the centered logistic function $\sigma(u) - \frac{1}{2} = \frac{1}{2}\tanh(u/2)$ and its power-series expansion around zero. *Contribution of this book:* Explicit unsaturated linear readout window around the threshold contrasted with tail collapse under clipping and scale saturation.

### 66. Proposition II.2.2

- **Location in the three-volume monograph:** [`Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md:229`](Book_II_EN/02_CHAPTER_II_02_CONTINUOUS_LIMIT_WITHOUT_LEAP_V3_3_EN.md#L229)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II02-04`
- *Classical foundation.* Ring of dual numbers $K[\varepsilon]/(\varepsilon^2)$ (Clifford, 1873), algebraic first-order Taylor expansion $P(x + \varepsilon v) = P(x) + \varepsilon\, dP(x)v$, and the Jacobi chain rule. *Contribution of this book:* Purely algebraic formulation of first-order jets and tangent question pushforwards over any commutative ring $K$ with zero limit passages $\Delta x \to 0$.

### 67. Lemma II.3.1

- **Location in the three-volume monograph:** [`Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:66`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L66)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II03-01`
- *Classical foundation.* The identities $\partial^2 = 0$ and $\delta^2 = 0$ are the classical fundamental identities of simplicial chains and cochains (Poincaré; Čech cochains; Eilenberg–Steenrod axiomatics, 1952). *Contribution of this book:* Use of this identity as the consistency condition for the observer's local records on the nerve of slices.

### 68. Theorem II.3.1

- **Location in the three-volume monograph:** [`Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:123`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L123)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-II03-02`
- *Classical foundation.* Simplicial cochains and cohomology of two-dimensional cell complexes over $\mathbb{F}_2$ (Alexandroff, 1928; Čech, 1932). *Contribution of this book:* Explicit matrix computation $\operatorname{rank}\delta_0 = 5$, $\operatorname{rank}\delta_1 = 4$, and $\dim_{\mathbb{F}_2} H^1(\mathcal{N}(O_6); \mathbb{F}_2) = 3$ on the checkerboard octahedron nerve of the six slices of $S_4$.

### 69. Theorem II.3.2

- **Location in the three-volume monograph:** [`Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md:217`](Book_II_EN/03_CHAPTER_II_03_WHEN_LOCAL_SECTIONS_FAIL_TO_GLUE_V3_3_EN.md#L217)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II03-03`
- *Classical foundation.* Smith normal form of integer boundary matrices (H. Smith, 1861), the universal coefficient theorem, and cellular homology of the real projective plane $\mathbb{R}P^2$. *Contribution of this book:* Contrast between visibility of $\mathbb{Z}/2\mathbb{Z}$ torsion over $\mathbb{Z}$ and $\mathbb{F}_2$ ($H^2(\mathbb{R}P^2;\mathbb{F}_2) \cong \mathbb{F}_2$) and complete blindness of the rational window $H^1(\mathbb{R}P^2;\mathbb{Q}) = H^2(\mathbb{R}P^2;\mathbb{Q}) = 0$.

### 70. Theorem II.4.1

- **Location in the three-volume monograph:** [`Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:86`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L86)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-II04-01`
- *Classical foundation.* The isomorphism $W(B_3) \cong \mathfrak{S}_4 \times C_2 \cong \mathrm{Aut}(O_6)$ is a classical fact about the hyperoctahedral symmetry group of the cube and octahedron; signed edge labels and their inversion belong to the language of signed graphs and gain graphs (Harary, 1953; Zaslavsky, 1982–1989). *Contribution of this book:* Separation of the subgroup $W(D_3) \cong \mathfrak{S}_4$ (preserving charge $\kappa$ and the nerve $\mathcal{N}(O_6)$) from the proper rotation subgroup $W(B_3)^+ \cong \mathfrak{S}_4$ (preserving $\kappa$ on $A_4$ and inverting $\kappa$ on $12$ odd rotations).

### 71. Proposition II.4.1

- **Location in the three-volume monograph:** [`Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:154`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L154)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II04-02`
- *Classical foundation.* Hamilton's quaternion group $Q_8$ (1843) and the cohomological non-splitting of the central extension $1 \to C_2 \to Q_8 \to V_4 \to 1$. *Contribution of this book:* Absence of a homomorphic section of quarter-turns over the Klein four-group $V_4$ ($|\mathcal{R}| = 0$) and triple spectral separation of $W(B_3)$, $\mathrm{GL}_2(\mathbb{F}_3)$, and $Q_8$ by elements of orders $2$ and $4$.

### 72. Theorem II.4.2

- **Location in the three-volume monograph:** [`Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md:177`](Book_II_EN/04_CHAPTER_II_04_WHAT_A_LOOP_ADDS_COVERINGS_AND_HOLONOMY_V3_3_EN.md#L177)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II04-03`
- *Classical foundation.* Item 1 is the classical universal property of a quotient group (homomorphism theorem); the abelianization $B_3^{\mathrm{ab}} \cong \mathbb{Z}$ is a classical fact about Artin's braid group (1925). *Contribution of this book:* Reading abelianization as the loss of noncommutative memory of permutation order.

### 73. Theorem II.5.1

- **Location in the three-volume monograph:** [`Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:49`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L49)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II05-01`
- *Classical foundation.* Associativity of the group algebra $K[\mathbb{F}_2^3]$ and representation of the octonions as the twisted group algebra $\mathbb{R}_\sigma[\mathbb{F}_2^3]$ with a sign $2$-cocycle and its $3$-coboundary on the Fano plane (Albuquerque and Majid, 1999). *Contribution of this book:* Direct passage from the unsigned commutative-associative Fano table of Book I to the alternative octonion algebra by choosing a sign $2$-cocycle $\sigma$, verified exhaustively across all $512$ basis triples.

### 74. Theorem II.5.2

- **Location in the three-volume monograph:** [`Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:109`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L109)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II05-02, GATE-II05-03`
- *Classical foundation.* Zorn's vector-matrix model of split octonions and Paige's simple Moufang loops (1956) are classical constructions. *Contribution of this book:* Separation of the trace split $64 + 56 = 120$ from the quadratic split $36 + 84 = 120$ with an exhaustive check of all $120^3$ Moufang triples.

### 75. Proposition II.5.1

- **Location in the three-volume monograph:** [`Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:186`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L186)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II05-04`
- *Classical foundation.* Cayley–Dickson doubling and the appearance of zero divisors in sedenions belong to classical nonassociative algebra. *Contribution of this book:* Explicit integer zero-divisor witnesses and exhaustive enumeration of all $84$ elementary quartets.

### 76. Proposition II.5.2

- **Location in the three-volume monograph:** [`Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md:216`](Book_II_EN/05_CHAPTER_II_05_NONASSOCIATIVE_STEP_FANO_AND_OCTONIONS_V3_3_EN.md#L216)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II05-04`
- *Classical foundation.* Eightfold periodicity of real Clifford algebras $\mathrm{Cl}_{0,n+8} \cong \mathrm{Cl}_{0,n} \otimes \mathrm{Mat}_{16}(\mathbb{R})$ (Cartan, 1908; Bott, 1959; Atiyah–Bott–Shapiro, 1964) and Morita equivalence. *Contribution of this book:* Explicit integer realization of eight anticommuting skew-symmetric generators $\Gamma_1,\dots,\Gamma_8 \in \mathrm{Mat}_{16}(\mathbb{Z})$ built from left multiplication by octonion basis units.

### 77. Theorem II.6.1

- **Location in the three-volume monograph:** [`Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:85`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L85)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-II06-01`
- *Classical foundation.* The Pauli basis and the representation of Hermitian matrices via real coefficients are known in linear algebra; the Walsh transform is based on characters. *Contribution of this book:* Quantum threshold filtration of Boolean tables $16 \to 8 \to 2$ on scene $S_4$ across $|\lambda| = 1/\sqrt{3}$ and $|\lambda| = 1$.

### 78. Proposition II.6.1

- **Location in the three-volume monograph:** [`Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:134`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L134)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II06-02, GATE-II06-03`
- *Classical foundation.* Stabilization of an ascending chain of subspaces in at most $\dim - 1$ steps is a classical linear-algebraic argument (Schützenberger, 1961; Carlyle–Paz, 1971; Tzeng, 1992). *Contribution of this book:* Quantum Nerode equivalence formulated as an observer indistinguishability relation on effects.

### 79. Theorem II.6.2

- **Location in the three-volume monograph:** [`Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md:170`](Book_II_EN/06_CHAPTER_II_06_STATE_EFFECT_AND_FUTURE_QUANTUM_QUESTION_V3_3_EN.md#L170)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II06-03, GATE-II06-04`
- *Classical foundation.* Gleason's theorem (1957) on subspace measures for $d \ge 3$ and Busch's theorem (2003) on effect valuations for $d \ge 2$ are classical results. *Contribution of this book:* Comparison of the two domains of applicability and explicit analysis of the qubit exception $d = 2$ via Busch's trine.

### 80. Proposition II.7.1

- **Location in the three-volume monograph:** [`Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:23`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L23)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II07-01`
- *Classical foundation.* The bound $k \le d + 1$ and complete families of mutually unbiased bases in prime-power dimensions are classical results of Ivanović (1981) and Wootters–Fields (1989). *Contribution of this book:* Formulation of explicit families at $d = 2, 3$ as sets of mutually complementary observer questions.

### 81. Theorem II.7.1

- **Location in the three-volume monograph:** [`Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:42`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L42)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II07-01`
- *Classical foundation.* The tetrahedron of four equiangular complex lines and symmetric informationally complete families have been studied previously (Zauner, 1999; Renes et al., 2004). *Contribution of this book:* Coincidence of the qubit `SIC` tetrahedron with the boundary points $2E_{1/\sqrt{3}}(\delta_s)$ of the four-state scene $S_4$.

### 82. Theorem II.7.2

- **Location in the three-volume monograph:** [`Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:87`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L87)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II07-02`
- *Classical foundation.* Hoggar's sixty-four equiangular lines (1982) and frame potentials (Welch, 1974; Benedetto–Fickus, 2003) are classical constructions. *Contribution of this book:* Exact matrix calculation in $\mathbb{Q}(i)$ and verification of the third frame-potential gap $\Phi_3 - \Phi_3^{\mathrm{Welch}} = 7/810 > 0$.

### 83. Theorem II.7.3

- **Location in the three-volume monograph:** [`Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md:155`](Book_II_EN/07_CHAPTER_II_07_QUBIT_HOGGAR_AND_LIMITS_OF_GLOBAL_ASSIGNMENT_V3_3_EN.md#L155)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II07-03, GATE-II07-04`
- *Classical foundation.* The Peres–Mermin square (1990) and the Abramsky–Brandenburger sheaf-theoretic description of contextuality (2011) are published classical results. *Contribution of this book:* Exact comparison with the parity obstruction $\kappa$ in the one-dimensional cokernel over $\mathbb{F}_2$ and the three-level hierarchy of global sections $|\mathcal{S}_e(X)| = 16 \supsetneq 5 \supsetneq 0$.

### 84. Proposition II.8.1

- **Location in the three-volume monograph:** [`Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:55`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L55)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-II08-01`
- *Classical foundation.* Whitney forms (1957), the de Rham map, and cohomology invariance under subdivision are classical constructions. *Contribution of this book:* Explicit rational verification of the one-sided identity $R_1 W_1 = \mathrm{id}$ and the reconstruction defect inside a cell.

### 85. Theorem II.8.1

- **Location in the three-volume monograph:** [`Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:103`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L103)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II08-02`
- *Classical foundation.* Conservative Cahn–Hilliard gradient flows and their discrete analogues on graphs are established constructions. *Contribution of this book:* Explicit free-energy dissipation law on the octahedron graph $O_6$ with spectrum $L_{O_6} = \{0, 4^{\times 3}, 6^{\times 2}\}$.

### 86. Theorem II.8.2

- **Location in the three-volume monograph:** [`Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md:175`](Book_II_EN/08_CHAPTER_II_08_CELLS_LIMITS_VARIATIONAL_AND_SOS_CERTIFICATES_V3_3_EN.md#L175)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-II08-04`
- *Classical foundation.* Isotypic character decomposition (Frobenius, Schur) and sum-of-squares representations via positive semidefinite Gram matrices (Hilbert, 1888; Choi–Lam–Reznick, 1995; Parrilo, 2000; Lasserre, 2001; Gatermann–Parrilo, 2004). *Contribution of this book:* Isotypic splitting $231 = 42 + 7\cdot 27$ and $1771 = 189 + 7\cdot 226$ on the $21$ flags of the Fano plane and the explicit rational orthogonal projector $P_{\perp,c}$ of codimension $84$ ($1771 - 84 = 1687$).

### 87. Theorem II.9.1

- **Location in the three-volume monograph:** [`Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md:42`](Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md#L42)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-II09-01`
- *Classical foundation.* Lawvere's diagonal fixed-point theorem (1969) rests on the categorical form of Cantor's diagonal argument. *Contribution of this book:* Separation of pointwise surjectivity from the exponential in $\mathbf{Set}^{C_2}$ ($|Y^A| = 4$, $|(Y^A)^{C_2}| = 2$) with the observer-stratification rule.

### 88. Theorem II.9.2

- **Location in the three-volume monograph:** [`Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md:87`](Book_II_EN/09_CHAPTER_II_09_LAWVERE_SELF_DESCRIPTION_LIMIT_AND_SYNTHESIS_I_II_V3_3_EN.md#L87)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-II09-02, GATE-II09-03`
- *Classical foundation.* Cohomological classification of group extensions and the correspondence between $1$-cocycles and complements in semidirect products belong to classical group theory. *Contribution of this book:* Explicit computation of the $64$-element non-split extension $\widetilde{G}_\beta$ and the two orbits $8 + 56 = 64$ of the affine action of $\mathrm{GL}_3(\mathbb{F}_2)$ on $X_{64}$.

### 89. Proposition III.1.1

- **Location in the three-volume monograph:** [`Book_III_EN/01_CHAPTER_III_01_HOW_TO_CONSTRUCT_A_DOMAIN_BRIDGE_V3_3_EN.md:80`](Book_III_EN/01_CHAPTER_III_01_HOW_TO_CONSTRUCT_A_DOMAIN_BRIDGE_V3_3_EN.md#L80)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-III01-01, GATE-III01-02`
- *Classical foundation.* Quotienting the polynomial ring $K[x]$ by the Lagrange interpolation node ideal and rank bounds for orthogonal block slices of matrices. *Contribution of this book:* Uniting the polynomial continuation torsor $P_c(x)$ and the rank-one slice counterexample $P_i A P_i$ over $\mathbb{Q}$ and $\mathbb{F}_2$ into a single algebraic falsification test for domain bridges.

### 90. Lemma III.2.1

- **Location in the three-volume monograph:** [`Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md:15`](Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md#L15)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-III02-01`
- *Classical foundation.* Signed graphs (F. Harary, 1953) and commutation conditions for permutation matrices with diagonal and weighted operators. *Contribution of this book:* Proving the insufficiency of an unsigned weight matrix $W$ without transmission signs $\sigma$, retention coefficients $\alpha$, and fixed output-channel bindings.

### 91. Proposition III.2.1

- **Location in the three-volume monograph:** [`Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md:84`](Book_III_EN/02_CHAPTER_III_02_DIRECTED_WEIGHTED_GRAPHS_AND_FILTRATION_V3_3_EN.md#L84)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-III02-02, GATE-III02-03`
- *Classical foundation.* Neumann series and the random-walk resolvent on a directed graph (L. Katz, 1953; PageRank core, 1998). *Contribution of this book:* Contrasting the conservative resolvent $\widetilde{P}_\tau$ (`0` mass loss and preserved strong connectivity) against threshold edge truncation as a carrier substitution.

### 92. Proposition III.3.1

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:17`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L17)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-01`
- *Classical foundation.* Binary self-dual code with generator matrix $[I_n \mid I_n]$ and exchange-involution projectors $\frac{1}{2}(I \pm \sigma)$. *Contribution of this book:* Operational reading of $C = \ker\Delta = C^\perp \subset \mathbb{F}_2^{2n}$ as the error-free mirror code linking an external pattern to its internal trace.

### 93. Lemma III.3.1

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:36`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L36)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-01`
- *Classical foundation.* Geometry of the three-dimensional Boolean cube $Q_3$, the complete tripartite graph $K_{2,2,2} \cong O_6$, and cyclic coordinate shifts. *Contribution of this book:* Identifying the equatorial hexagon $C_6$ and the two filled triangular $\mathbb{Z}_3$-orbits of weights $1$ and $2$ on $Q_3 \setminus \{000,111\}$.

### 94. Theorem III.3.1

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:85`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L85)
- **Statement status:** Two-arrow structural correspondence (bridge)
- **Machine certificate (`Julia 1.12.6`):** `GATE-III01-02, GATE-III03-02`
- *Classical foundation.* Kneser graph $\mathrm{KG}(5,2)$ (L. Lovász, 1978), Johnson graph $J(5,2) = L(K_5)$, and minimal triangulation of the Möbius strip $M_5$. *Contribution of this book:* Proving the polynomial identity $H_o = \frac{1}{6}(K^2 - 7K + 13I_5)$, the $D_{10}$-equivariant isometry $\mathcal{F} : C_2(M_5) \to \ker(A_{\mathrm{KG}}-I_{10})$, and the gluing of two octahedra along $\triangle(ME,MB,EB)$.

### 95. Lemma III.3.2

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:122`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L122)
- **Statement status:** Proved prohibition / counterexample
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-02`
- *Classical foundation.* Proper colorings of the Petersen graph ($\chi = 3$) and induced maps on pair graphs. *Contribution of this book:* Proving that the role folding $q(D)=q(N)=C$ destroys edges of $\mathrm{KG}(5,2)$ and that no proper $3$-coloring of $\mathrm{KG}(5,2)$ is induced by any folding of the base alphabet $\Lambda_5$.

### 96. Theorem III.3.2

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:141`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L141)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-03`
- *Classical foundation.* Classical criterion for square roots of permutations via even-length cycle counts. *Contribution of this book:* Contrasting the impossibility of $r^2 = c_6$ in $\mathfrak{S}_6$ ($0$ solutions) against the $12$ solutions of $r^2 = c_8$ in $\mathfrak{S}_8$, each pairing antipodes with zero invariant pairs.

### 97. Proposition III.3.2

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:176`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L176)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-04`
- *Classical foundation.* Circulant graph $C_6(1,2)$ on $\mathbb{Z}_6$ and step-length partition of octahedral edges. *Contribution of this book:* Decomposing $E(O_6) = E(C_6) \sqcup E(C_3^{\mathrm{even}}) \sqcup E(C_3^{\mathrm{odd}})$ ($12 = 6 + 3 + 3$) across the three axes of case-role pairs in Pāṇini's scheme.

### 98. Lemma III.3.3

- **Location in the three-volume monograph:** [`Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md:193`](Book_III_EN/03_CHAPTER_III_03_SAMKHYA_YOGA_ADVAITA_AND_PANINI_V3_3_EN.md#L193)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-III03-04`
- *Classical foundation.* Representations of the hyperoctahedral group $W(B_3)$ and Burnside's theorem for absolutely irreducible representations (with trivial commutant $\mathbb{R}\cdot I_3$). *Contribution of this book:* Separating the three index-$2$ subgroups of $W(B_3)$ and contrasting the algebra span of a single equatorial $6$-cycle ($3/9$) against a non-collinear pair ($9/9$) in $\mathrm{End}(V_-)$.

### 99. Lemma III.4.1

- **Location in the three-volume monograph:** [`Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:23`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L23)
- **Statement status:** Original proved result of this book
- **Machine certificate (`Julia 1.12.6`):** `GATE-III04-01`
- *Classical foundation.* Edge deletion/addition on the $6$-vertex prism $K_3 \square K_2$ and the even-weight linear code in $\mathbb{F}_2^5$. *Contribution of this book:* Exact edge and triangle balance when rebuilding the prism $\Pi_6$ into the octahedron $O_6$ ($\Delta|E| = -3 + 6 = +3$, $\Delta N_\triangle = +6$) and the $4$-dimensional even kernel.

### 100. Theorem III.4.1

- **Location in the three-volume monograph:** [`Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:40`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L40)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-III04-02`
- *Classical foundation.* Congruence of squares of Kraitchik (1926) and Dixon (1981), Kirchhoff's cyclomatic rank (1847), and the two-large-prime cofactor graph of Lenstra and Manasse (1994). *Contribution of this book:* Formulating the oracle-free relation-merging contract with zero access to $(p,q)$ and working through trivial versus splitting cycles on $N = 2537$.

### 101. Theorem III.4.2

- **Location in the three-volume monograph:** [`Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md:91`](Book_III_EN/04_CHAPTER_III_04_PRISM_REBUILDING_COFACTOR_GRAPHS_AND_HIDDEN_MARKOV_MODELS_V3_3_EN.md#L91)
- **Statement status:** Two-arrow structural correspondence (bridge)
- **Machine certificate (`Julia 1.12.6`):** `GATE-III04-03`
- *Classical foundation.* Invariance of hidden Markov model likelihood under state permutations $\mathfrak{S}_m$ (T. Petrie, 1969). *Contribution of this book:* Formalizing the relabelling gauge torsor $|\mathcal{R}| = m!$ as an exact impossibility barrier against deducing external semantics from monolingual sequence statistics without a bilingual anchor, accompanied by a finite binary-alphabet witness.

### 102. Theorem III.5.1

- **Location in the three-volume monograph:** [`Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md:26`](Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md#L26)
- **Statement status:** Extension of a classical theorem within contract Γ
- **Machine certificate (`Julia 1.12.6`):** `GATE-III05-01`
- *Classical foundation.* Equivalence testing and minimization of finite deterministic automata (E. F. Moore, 1956; J. E. Hopcroft and R. M. Karp, 1971). *Contribution of this book:* Contrasting $O(|X|\cdot|\Sigma|)$ verification of an exhibited certificate $\phi : X \to M$, a counterexample to necessity without minimality of $M$, and $X \times M$ traversal.

### 103. Lemma III.5.1

- **Location in the three-volume monograph:** [`Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md:50`](Book_III_EN/05_CHAPTER_III_05_VERIFICATION_PROGRAM_AND_CRITERIA_FOR_THE_NEXT_STEP_V3_3_EN.md#L50)
- **Statement status:** Classical result in operational notation
- **Machine certificate (`Julia 1.12.6`):** `GATE-III05-01`
- *Classical foundation.* Discrete Grönwall lemma for the linear recurrent inequality $e_{t+1} \le L e_t + \varepsilon$. *Contribution of this book:* Explicit trajectory-divergence budget and logarithmic prediction horizon for approximate dynamical bridges across all three regimes ($L < 1, L = 1, L > 1$).
