# Distinction and Observability Theory (DOT) — Volume I

> **Русская версия:** [ru/VOLUME_I.md](ru/VOLUME_I.md) | **README:** [README.md](README.md) | **Glossary:** [GLOSSARY.md](GLOSSARY.md)

## The Whole, Distinction, and Preserved Continuation

## Table of Contents

1. [Chapter 1. The Whole and Preserved Distinction](#v1-chapter-1)
2. [Chapter 2. Act and Counter-Question](#v1-chapter-2)
3. [Chapter 3. Sufficiency, Memory, and Assembly](#v1-chapter-3)
4. [Chapter 4. Questions as Objects](#v1-chapter-4)
5. [Chapter 5. Domains and Arithmetical Input](#v1-chapter-5)
6. [Chapter 6. Phase and Continuation](#v1-chapter-6)
7. [Chapter 7. Composite Action and Return to the Scene](#v1-chapter-7)

- [Appendix A. Addresses, Domains, and Relation Types](#v1-appendix-A)
- [Appendix B. Finite Tables, Memory, and Recovery](#v1-appendix-B)
- [Appendix C. Arithmetical Foundations and Algebras](#v1-appendix-C)
- [Appendix D. Phase, Topology, and Geometric Equipment](#v1-appendix-D)
- [Appendix E. Quantum and Linguistic Tests of Coordination](#v1-appendix-E)
- [Appendix F. Source, Cost, and Continuation of Computation](#v1-appendix-F)

---

# Introduction

## What Remains After Transitioning to Another Notation?

A single object can be described by different mathematical means. A pair of numbers — by their difference; a set of states — by a table or a graph; a transformation — by a rule or a sequence of steps. Each representation is convenient for certain questions and may conceal information necessary for others.

Consider two numbers $x$ and $y$ and retain only their difference:

\[
d = x - y.
\]

The difference does not change if both numbers are shifted simultaneously by the same quantity $t$:

\[
(x + t) - (y + t) = x - y.
\]

Therefore, $d$ is invariant under an overall shift. However, an invariant is not a complete copy of the original pair: the record $d = 3$, for instance, is compatible with $(x, y) = (3, 0)$, $(4, 1)$, and infinitely many other pairs. To reconstruct the participants, a fulcrum is required — for example, a known value of $y$. If a subsequent step acts specifically on $x$, one must verify that the compressed record allows that action to be executed without losing essential information.

There is no novel assertion about arithmetic here. There is a foundational research question: **how to verify that transitioning to a more compact representation preserves precisely the work needed downstream?** The answer depends on the source model, admissible actions, and questions, rather than merely on the numerical coincidence of final outputs.

## Subject Matter of the First Volume

Distinction and Observability Theory (DOT) studies the construction and coordination of mathematical representations. It traces how a specified object is presented in another form, which relations and actions are carried over with it, and what data must be retained to answer a counter-question or unfold the original construction.

For every specific transition, it is essential to name at least its source carrier, reading rule, mapping into the new notation, and required preservation. If two sides of a transition are employed — direct presentation of the object and pullback of a question back to the source data — one must verify that both pertain to the same underlying realization. Coincidence of answers does not yet demonstrate coincidence of sources, preservation of history, or the capability to execute any arbitrary subsequent action.

In this book:

- **state** — an element of an explicitly specified set of possible realizations;
- **question** or **reading** — a rule that extracts an answer from a state;
- **action** — an admissible transformation of states;
- **projection** — a chosen mapping that may discard certain distinctions;
- **memory** — data retained accessible for subsequent action or reconstruction.

These are brief navigational landmarks rather than universal definitions for all mathematical domains. In the chapters, every term receives a concrete carrier and law. For example, "whole" denotes here a specified system of participants, relations, and admissible transformations, rather than "everything in existence" without qualification. The "hidden side" is that which the chosen reading does not exhibit. The "observer" is a formal role associated with selecting and obtaining a reading; it is not an assertion about human consciousness.

The *metacenter* designates the role of a balancing fulcrum relative to which distinct presentations are correlated. It is not obliged to be a geometric center, a numerical zero, or an isolated point. To speak of a concrete metacenter, a model must specify what performs this role and under what rule. Zero, a center of symmetry, and the complex imaginary unit are therefore never conflated merely on the basis of resemblance in naming or position.

## Trajectory of the Book

First, a minimal finite model is introduced: two positions, possible states, and the reading of their distinction. On this model, the source state, question, action, and answer are disentangled. Next, we verify what auxiliary data are required for inverse assembly and continuation of action. Subsequently, the questions themselves become objects of analysis; relations among them are constructed, along with their graph-theoretic and geometric presentations.

Subsequent chapters examine transfers between domains, arithmetical and phase models, composite actions, and execution history. The appendices assemble finite tables, proofs, and verification routines. In transitions between domains, what is being compared is stated explicitly every time: not merely two similar-looking graphs or two equal scalar quantities, but elements of specified carriers and concrete mappings between them.

The first volume offers verifiable constructions within the enumerated models. It does not claim that all mathematical structures have already been unified into a single hierarchy, that every transition is universally necessary, or that a new foundation of physics has been discovered. Conditions of generality and potential practical utility demand independent proofs and comparative evaluations.

Therefore, it is beneficial to read each proposition through four guiding questions: **in which carrier is it formulated? which reading is chosen? what does the transition preserve? what remains unknown or demands a separate witness?** These questions define the operative methodology of the volume.

---

<a id="v1-chapter-1"></a>

# Chapter 1 The Whole and Preserved Distinction

We begin with the problem of coordinating representations. The names of the participants in a certain relation are known, but presently we exhibit only whether their values coincide. What remains accessible? Is it possible to reconstruct the participants, execute a subsequent action, or answer another question? These operations must be distinguished on a concrete example before constructing a general notation.

A bound whole here is a specification with named participants, admissible combinations, and a linking law. It cannot be derived from a naked count of parts. The first reduced presentation is constructed within this specification; then we verify which work it preserves and what requires an auxiliary fulcrum.

In this chapter, we describe from an external frame over named finite tables. Ordinary language, membership, functions, equality, and composition are employed as declared mathematical tools. A structural unit denotes a single presented composite whole together with its disclosure; digits in numerical reading and the complex imaginary unit receive their own types.

Epistemic statuses of propositions: [Prem] — initial research premise; [Def] — definition or chosen condition; [Th] — statement with proof/substantiation; [Ext] — borrowed mathematical tool; [CE] — counterexample; [Comp] — finite computational check; [Interp] — interpretation; [Open] — open problem. Preliminary mention of a subsequent result does not permit its use as a foundation.

## Stance of Description

<a id="tnr-P01"></a><a id="tnr-П01"></a>

### P01 Where and Wherewith We Observe

We already distinguish whenever we name an object, assert a law, or check an answer [Prem]. DOT adopts the premise "there is nothing except distinction" as its own ontological foundation. The finite mathematical results below follow from explicitly specified models; this foundation itself does not determine their carriers, number of bits, or geometry.

For a considered task, we explicitly name the source device, the method of its presentation, and the work that must be preserved [Def]. The act of distinction is carried out by means of already accessible language. We do not describe from an unconditional "nowhere": language itself and the law of admissibility enter the stance of description even when they are not the immediate objects of analysis.

A frame links an object with the conditions of admissible description. One side consists of the realizations under consideration; the other consists of the means and constraints of their presentation; the common admissibility law determines which notation pertains to this task. This is a composite apparatus. The count of its named fields does not establish independent dimensions.

The external frame of the book describes mathematical tasks; the internal frame of an example describes the rows of a single table. When a table becomes the object of a subsequent task, the level of objecthood shifts. The means of the former description may now acquire their own addresses. A free binary bit is added only upon an additional independent choice, rather than at the mere emergence of a name.

Verification question: which tools have already been utilized in this notation, and where are they named? The boundary of disclosure here is the declared mathematical language. We do not pass it off as the result of the first definition.

## The First Bound Specification

<a id="tnr-P02"></a><a id="tnr-П02"></a>

### P02 Conjugate Whole

Let us choose two named positions: participant $x$ and a second position $c$. Each admits two labels, $a$ and $b$. In this example, all four combinations are permitted [Def]. The third role is their distinction: labels coincide or differ. The position $c$ can serve as a fulcrum of comparison, but as yet it is neither a fixed value, nor a midpoint, nor a coordinate zero.

| x | c | Distinction |
|---|---|---|
| a | a | coincide |
| a | b | differ |
| b | a | differ |
| b | b | coincide |

The whole $E$ retains the positions, admissible values, and the linking law. The set of these four rows is denoted by $S$; a row is a single realization of $E$. Describing the whole table does not imply knowing which row is currently presented to an observing participant.

In counting positions, there are two positions; in counting joint realizations, there are four rows; in counting roles of the law, there are participant, second position, and distinction. The third role depends on the first two: it is the bond of the pair, not a third free choice. These counts belong to different projections of a single construction.

A whole contains more than a bare inventory of values. For example, a task permitting only rows with identical labels has the same two positions, but a different jointness and two realizations. Therefore, the count of positions does not recover the governing law [CE].

Verification question: can the admissible combinations be reconstructed from the specified scalar? Here, a table or an equivalent rule is required.

<a id="tnr-P03"></a><a id="tnr-П03"></a>

### P03 Paired Inversion and Symmetry Law

Let us introduce the inversion $\sigma$, which simultaneously exchanges $a \leftrightarrow b$ in both positions [Def]. It partitions the rows into two pairs: $aa$ with $bb$, and $ab$ with $ba$. Applying inversion twice returns the initial row; the label distinction is preserved.

Another map swaps $x$ and $c$. It also returns the row after two applications, but leaves $aa$ and $bb$ fixed. The coincidence of the laws of two-step return does not make these two maps the same action.

A pair is introduced together with the law of common membership and inversion. In the projection of a single answer "coincide", two possible representatives are visible. The answer itself does not distinguish one of them. If the entire pair is protected, inversion preserves it; if a marked representative is protected, one must retain the orientation.

We have not yet introduced a metric, a segment midpoint, or a continuous phase. The symmetry of this table is verified by its permutation. For a geometric center, a dedicated construction will be needed. For a coordination fulcrum — the law relative to which it correlates presentations. Neither follows merely from the presence of a pair.

Verification question: which inversion is chosen, and what does it preserve — an individual participant, the pair, or the answer?

<a id="tnr-P04"></a><a id="tnr-П04"></a>

### P04 Cut and Inverse Assembly

A cut presents named parts of a single source whole [Def]. For a row of the table, we separate the values of $x$ and $c$, retaining the address of the source row and the names of the positions. Inverse assembly places the values back and verifies the common law.

Extraction and assembly are two operations of a single apparatus. Their conjugation is the condition for recovering declared content. Two similar parts with different origins do not become parts of the same realization merely because their values fit the table.

Assembly reconstructs from the parts a coordinated presentation of the source whole, rather than pulling a question about the result back to the source data. The latter operation will be constructed in Chapter 2. Inverse disclosure, counter-question, and inverse action are not identified in advance.

If values are protected, it suffices to retain both values and the order of positions. If the concrete act of acquisition is protected, its provenance and event will also be required. Numerical coincidence of the assembled pair is then weaker than returning the former whole.

A cut is not obliged to destroy a part. The hidden part may remain at its address, even though it is not exhibited by the current reading. If it is genuinely discarded and cannot be deduced from what remains, inverse disclosure becomes inaccessible. This is a loss of data, not a preserved folding.

Verification question: is the former row returned with membership, or merely an admissible row of similar appearance?

<a id="tnr-P05"></a><a id="tnr-П05"></a>

### P05 Disclosable Structural Unit

Let us denote a single presentation of the composite $E$ by $i_{\mathrm{str},\Pi}[E]$ [Def]. Here $\Pi$ is a declared reading. The notation is admissible when the content, the disclosure address, and the external links essential for the subsequent work are preserved.

Folding makes $E$ a single participant in a new relation. Disclosure returns its internal apparatus. Their joint law requires that the returned content perform the declared work and pertain to the same source whole. For a paired apparatus, what is folded is not two unrelated labels, but the pair together with the law of inversion and membership.

The scalar "one" here counts presented participants. Inside a participant there may be a pair, an action, a table, or a history. Their complexity does not vanish. In our table, the folded $E$ remains a task with four realizations.

The standard numerical unit is the result of an appropriate count. The complex $i$ possesses a different law and will be realized separately. Replacing an arithmetic digit with complex $i$ would alter an arithmetic formula; hence, such a substitution does not follow from structural notation.

Verification question: where does the disclosure of this name lead? A name lacking accessible content and return conditions is not considered a constructed structural unit.

<a id="tnr-P06"></a><a id="tnr-П06"></a>

### P06 Name, Equality, and the Next Level

Three operations are distinguished in notation [Def]. Naming binds a symbol to a structure. Equality establishes coincidence of values or objects within a declared type. Object-level lift incorporates the former structure as a participant in a new relation.

For example, the numerical equality of the sum of three numbers to their product communicates nothing about the addresses of the arguments and the tree of operations. These data may be preserved in the term itself, but cannot be recovered from the bare result.

The equality sign does not create a new independent bit. The statement itself, together with its arguments, operations, witness, and mode of disclosure, can become a new object. In that case, an enclosing task describes this proposition; its composition must be stated explicitly.

The nesting principle is formulated as follows: the former whole becomes a participant in a new relation, while the new whole preserves the method of unfolding the former. For a concrete construction, the inclusion map, compatibility conditions, and returned work are specified.

We denote the level of objecthood by $\ell$: on this level, the participants are rows of the table. At level $\ell+1$, the object can be the table itself with its governing law and disclosure. This is a description from an enclosing task. It is not identical to the transition from $n$ to $n+1$ independent binary positions: such a transition requires an additional independent distinction.

Verification question: what precisely has changed — name, value, access, or the type of the object under consideration?

## The First Presentation and Question

<a id="tnr-P07"></a><a id="tnr-П07"></a>

### P07 Presentation, Rule, and Source Domain of the Question

The chosen presentation $m_{\mathrm{acc}}: S \to B$ extracts from realization $s$ a value in the accessible carrier $B$ [Def]. For instance, it may distinguish only whether labels coincide. The index $\mathrm{acc}$ distinguishes this access map from the geometric fulcrum $m$, which appears later. On $B$, a family of rules $\Omega(B)$ is specified; a chosen rule $h \in \Omega(B)$ yields an answer. The realization of the question on the source states has the form

\[
q = h \circ m_{\mathrm{acc}}.
\]

The source projecting domain of the question is $B$, on which $h$ is defined. The argument domain of the complete question is $S$. Their roles are distinct. The frame $\Gamma$ determines the accessible presentation and the admissible family of rules.

A question as a structure retains provenance $\Gamma$, map $m_{\mathrm{acc}}$, domain $B$, permitted family $\Omega(B)$, and chosen $h$. These positions are bound by types: the codomain of $m_{\mathrm{acc}}$ is the domain of $h$; $h$ belongs to the permitted family; $\Gamma$ permits obtaining $m_{\mathrm{acc}}$. The bare count of fields does not generate the graph of this structure. The address of a question indicates both the carrier of the argument and the locus from which its rule is specified.

The rule and the obtained answer are distinct objects. One can know the truth table of a question without knowing its value on an unknown realization. One can know an answer without possessing access to another rule on the same full carrier.

After a change of projection, an identical truth table $q$ can be obtained from another source device. If provenance is protected, such questions are not conflated. This distinction becomes critical during counter-transport. It does not vanish when a question is folded into a single named device.

Verification question: whence is the question specified, what precisely is accessible to the answering participant, and by what rule was the answer obtained?

<a id="tnr-P08"></a><a id="tnr-П08"></a>

### P08 Preimage and the Underside of the Answer

The preimage of answer $b$ consists of all realizations yielding it under the chosen reading [Ext]. For the question concerning label agreement, one answer groups $aa$ and $bb$, while the other groups $ab$ and $ba$. The current answer determines the pair, but not its marked representative.

By the *underside* of this reading we designate the essential distinctions within the preimage that are not exhibited by a single answer [Def]. Here, the underside of the answer is the distinction between representatives of a single pair. The law, external frame, and hidden participant perform distinct roles; they must not be conflated under the generic term "background" without addresses. Visible and hidden positions are not obliged to be independent or equinumerous.

In our table, an additional value of one named position determines the second participant. This assertion relies upon the chosen law and the accessible auxiliary fulcrum. If the law changes, the former disclosure must be re-verified.

A preimage is not an inverse function: from a single answer, one cannot select a concrete row without justification. At the same time, the entire pair can be an accurately reconstructed target. Therefore, the question "is it completely reconstructed?" demands naming the object to be reconstructed.

Verification question: is the answer, pair, row, address, or history protected? The answer changes the necessary composition of the record.

## Chapter Summary

The first representation is constructed: we know the source task, its paired law, cut, preserved folding, and question with its source projecting domain. A single answer retains the pair, but not its marked orientation. An auxiliary fulcrum reconstructs the participants only by virtue of the preserved law.

The observer is so far specified only by the stance of examination and access to the presentation. An intrinsic strategy of choice has not yet been built. The metacenter is not yet specified as a universal point: each realization of its role must exhibit its own fulcrum and transition law.

The next chapter introduces action upon the same whole. The two boundaries of action will be bound by an admissible rule and a concrete realization. The counter-question will preserve its provenance, even when its current table changes.

Sources of disclosure: primitive map, executable origin, source domain of the question. The complete addressed glossary is preserved alongside the book. Verification code: initial glossary, question transfer.

<a id="v1-chapter-2"></a>

# Chapter 2 Act and Counter-Question

The first chapter constructed a bound specification and distinguished its source realizations, presentation, and question. Now it is necessary to coordinate these representations with action: what will become of the participants, and how will a question about the result be posed on the source data? Merely preserving the former answer may prove insufficient for this purpose.

We continue to work with the same named table. The external description knows the governing law and mappings, but a concrete participant may have access to only a single presentation. Therefore, the forward transformation of state, the counter-transfer of the question, and the common realization linking both readings are constructed separately. The inverse assembly of Chapter 1, inverse action, and counter-question will be distinguished by their operative work and domain.

<a id="tnr-P09"></a><a id="tnr-П09"></a>

## P09 Fulcrum of Distinction

Let us assign the second position $c$ as the fulcrum of comparison [Def]. $x$ and $c$ belong to the same row; their distinction is determined by their relation. We select the role of position $c$, rather than a single fixed value across the entire table: in different rows, $c$ receives different labels. If one were to fix a concrete label for $c$ in advance, the scope of examination would contract to two rows. That is an independent choice, not a consequence of the word "fulcrum."

Such a fulcrum is relative to the chosen comparison. It is not a geometric midpoint and does not specify the complete apparatus of an observer. Later, in P30, the midpoint of question tables will be constructed in real space. The choice of a comparison participant and the derivation of that midpoint obey different laws; the shared investigable role of a coordination fulcrum does not make them the same object.

Upon simultaneous exchange of labels in both positions, the answer is preserved. Altering only one position changes the answer. The roles are distinguishable, even though the table admits a coordinated transposition of participants.

When changing the representation of a fulcrum, one must state how it is presented anew, what the answer map is, and how this is coordinated with the source task. Merely declaring an alternative viewpoint is insufficient for recovering a hidden representative. Specifying a fulcrum also does not replace the map that transports the entire presentation.

Verification question: which fulcrum is retained, and is it transported together with the question?

<a id="tnr-P10"></a><a id="tnr-П10"></a>

## P10 Binary Comparison Table

Now let us exhibit the former table in binary numerical reading: labels are encoded by values $0$ and $1$, and their distinction by XOR [Ext]. Under this change of notation, the names of positions, the four admissible rows, and the comparison law are preserved. Here, digits are elements of $\mathbb{F}_2$; they do not denote a new absolute background or the structural unit of Chapter 1.

\[
\beta = x \oplus c.
\]

| x | c | β |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

$S$ contains four states of two free positions. The three roles $x, c, \beta$ are bound by law; from any two, the third is recovered [Th]. For example, $x = \beta \oplus c$. The third value is not an additional free bit.

With access restricted to $\beta$, each preimage contains two states. The maps $\{\mathrm{Id}, \sigma\}$ form a group of two elements: $\sigma^2 = \mathrm{Id}$. On each preimage, $\sigma$ leaves no state fixed, but maps it to the unique alternative. This is a free and transitive action; such a carrier is termed a torsor of this group [Ext]. The action specifies a pair, but does not select a marked side.

Verification question: does the number three count the role-positions of the law or independent data? In this model, there are two independent bits.

<a id="tnr-P11"></a><a id="tnr-П11"></a>

## P11 Action, Identity, and Inversion

Changing the numerical notation has not yet altered the source state. For such alteration, an admissible action is now specified — a map $T: D_T \subseteq S_0 \to S_1$ [Def]. It possesses a source domain, an admissibility condition, and a result law. The endpoints of an arrow do not by themselves determine an action; transporting an action into another representation will require coordinating these data as well.

In our example, let us define the maps:

\[
T_x(x, c) = (x \oplus 1, c), \qquad \sigma(x, c) = (x \oplus 1, c \oplus 1),
\]
\[
T_{\mathrm{mix}}(x, c) = (x \oplus c, c), \qquad T_{\mathrm{erase}}(x, c) = (0, c).
\]

The first three maps admit inverse actions. The last erases $x$: two distinct states map to one. It nevertheless remains a well-defined action. Identity leaves a state invariant; repeated inversion $\sigma$ yields the identity.

The partial action $T_{\mathrm{guard}}(x, c) = (x \oplus 1, c)$ is permitted only when $c = 0$. Prohibition at $c = 1$ is not a false answer: it is the absence of an admissible execution. The domain of an action is part of the construction.

Verification question: which states are admitted, and on what domain does an inverse action exist?

<a id="tnr-P12"></a><a id="tnr-П12"></a>

## P12 Two Transfers and the Source Provenance of the Question

Let a question about the result be specified in its native frame $\Gamma_1$: $m_1: S_1 \to B_1$, permitted rule family $\Omega_1(B_1)$, chosen $h_1 \in \Omega_1(B_1)$, $h_1: B_1 \to \{0, 1\}$, $q_1 = h_1 \circ m_1$. Here $m_1$ is an access map, and $B_1$ is the carrier on which the rule is defined. Forward transfer alters the state via $T$. Counter-transfer pulls the question back to the source state:

\[
T^*q_1 = q_1 \circ T = h_1 \circ m_1 \circ T.
\]

For every admissible $s$, the following identity holds:

\[
q_1(T s) = (T^*q_1)(s).
\]

This is the coordination of two works [Th]: to obtain the result of the action and read it, or to read the source participant using the transported question. The equality follows from the composition of maps and pertains to the same admissible $s$. It establishes a common evaluation law, but does not yet assert that the given act has been executed.

Here, $T^{-1}$ is not required. An inverse action, when it exists, reconstructs a state from the result. Inverse disclosure returns content according to a preserved record and its address. A counter-question inverts nothing in that manner: it establishes a probe of the source state through $T$. Consequently, a question is pulled back even along an erasing action. Reciprocity pertains to the types of maps, not to the backward propagation of causes in time.

The source $\Gamma_1, B_1, m_1, \Omega_1$, and $h_1$ are preserved in the structure of the transported question; $B_1$ remains the domain of $h_1$. The current domain of the transported question is $D_T$. The possibility of expressing this question through the current access $m_0: S_0 \to B_0$ and rules permitted in the current frame is verified separately. An identical truth table does not return the source address and does not certify such access.

For the future question $\beta$, the map $T_{\mathrm{mix}}$ yields

\[
\beta(T_{\mathrm{mix}}(x, c)) = x.
\]

The counter-question currently has the truth table of $x$, but originates from future $\beta$. The question $x$, originally defined via access to $x$, and this transported question differ in provenance. This distinction persists whenever the transition law or acquisition history is protected.

Verification question: whence is the question specified, to which stage does it pertain, and is its current preimage accessible?

<a id="tnr-P13"></a><a id="tnr-П13"></a>

## P13 Common Realization and Witness

For the coordination of representations to pertain to an accomplished work, let us name its realization. An act is a concrete admissible realization of a chosen action [Def]. In the witness, the source participant, the rule $T$, the chosen question with its source frame and domain, admissibility, and the event timestamp are retained. The final state is deduced via $T$; the answer — via the question. Which additional fields are protected is determined by the frame.

The connecting third element unfolds in two works. The common evaluation law coordinates readings (P12). The witness of the given act demonstrates that both readings pertain to a single admissible realization and event within the declared frame. Coincidence of values alone is insufficient. Two distinct events may possess identical $s, T, q$, and answer, yet differ in order or provenance. A fulcrum of comparison or a center pointer does not replace such a witness.

For example, reading $\beta$ before $T_x$ and after it is linked by a single event. Reading the same answer after another act cannot be substituted as its witness if a concrete trajectory is protected.

The external description knows all possible rows; an executable act contains the chosen row. Conflating these levels turns a known law into the ostensibly already obtained answer of an unknown realization.

Verification question: do both transfers employ the same source participant and the same event?

<a id="tnr-P14"></a><a id="tnr-П14"></a>

## P14 Composition Order and History

If $T_1$ is executed first, followed by $T_2$, the resulting action is $T_2 \circ T_1$ [Ext]. The counter-question is transported in the reverse order of composition:

\[
(T_2 \circ T_1)^*q = T_1^*(T_2^*q).
\]

The order of execution and function notation differ by convention. Arrow direction, event sequence, and inversion law possess distinct addresses. Counter-composition preserves the provenance of a question about the final result; it does not become a sequence of inverse actions.

Composition of concrete acts additionally demands a shared intermediate participant: the input of the second must disclose precisely the output of the first. Coinciding values, event identifiers from distinct logs, or identical reduced answers do not certify this. A composite witness retains both source events. If the execution frame changes, an explicit law of its coordination is necessary; a bare new frame label does not replace it.

History retains the sequence of acts and essential sources. Two applications of $\sigma$ return the state and answer, but form a different history than the absence of actions. If only the final state is required, they may be identified; if trajectory or cost is protected, they cannot.

Compressing history into a resulting action is admissible relative to a declared task. The detailed word is preserved on the underside only when it remains addressable. A forgotten sequence cannot be reconstructed from a bare result without an auxiliary law.

Verification question: is the operator, state, action word, or paid history protected?

<a id="tnr-P15"></a><a id="tnr-П15"></a>

## P15 Observer as an Access Role

Now let us check which of the constructed representations are accessible to a participant. The observer role is defined by which presentation is accessible, which rules may be specified, and what is preserved for continuation [Def]. In frame $\Gamma_\beta$, $\beta$ is accessible; on its two values, one may specify constant answers, the identity rule, and negation. Knowledge of the full table $S$ by the external description does not grant this role free access to $x$.

When $\beta$ and $c$ are presented, the participant reconstructs $x$. When only $\beta$ is presented, the participant recovers only a symmetric pair. Distinct access roles pertain to the same full carrier $S$.

For now, the choice of a concrete question is a condition of the experimental setup. An intrinsic strategy of choice with justification and cost will be the subject of Chapter 7. Seven non-zero questions do not by themselves choose a question on behalf of an observer.

Verification question: what can a participant obtain through action, and what is merely permitted by the external mathematical description?

<a id="tnr-P16"></a><a id="tnr-П16"></a>

## P16 Interface and Encompassing Coordination

The constructed representations must function cooperatively rather than remain an inventory of disparate records. An interface links the whole, answer acquisition, and subsequent admissible acts [Def]. Its structure unfolds through the current presentation, accessible questions, the library of actions, required traces, and the frame of protected work. Fields are not chosen independently: the output of an action must admit subsequent presentation; a question must originate from an accessible device; memory must support the required continuation.

The three named roles now possess a substantive connection. The whole retains admissible jointness. The act realizes a specific distinction. The interface links an answer with its provenance and subsequent action. Coordination is disclosed through these relations and maps; the bare name of an interface specifies neither a fulcrum nor a transition. Enclosing $\Gamma$ establishes what work is deemed sufficient. It does not automatically constitute a fourth free bit.

In $\Gamma$, the declared specification law is distinguished from the current execution regime. The law establishes carriers, questions, and preservation conditions; current access and residual resource determine what is actually permitted now. The mark of a given event belongs to its witness, rather than becoming known from a general rule alone. If past expenditure alters subsequent admissibility, it is recorded in the continuation state or in an explicitly updated frame. These roles are bound by execution conditions; their enumeration does not prescribe a new fixed rank.

From a full interface, a concrete act cannot be obtained without the mark of the chosen realization or data that reconstruct it. From an act, one can read the source or terminal boundary via a specified map. Therefore, a state is included in an act through a boundary role, and an act in an interface through the admissibility law and realization, not by naive embedding of unlabelled sets.

Verification question: through which maps are state, question, and concrete act recovered from the general name of an interface?

<a id="tnr-P17"></a><a id="tnr-П17"></a>

## P17 Full Disclosure of the First Act

Let us trace both trajectories on a single event. Consider the source row $s = (0, 1)$, action $T_{\mathrm{mix}}$, and future question $\beta$, defined via access to $\beta$ in the result frame. The result is $(1, 1)$, and the answer is $0$. The counter-question $x$ gives the same answer on the source row. The source $\beta$ was equal to $1$: state and answer have transformed consistently. The transported table $x$ is still disclosed as a question originating from future $\beta$, not as a new unaddressed access to $x$.

In this event, there are two transfers and the realization that binds them. In the frame with access restricted to $\beta$, it cannot be modeled from the former answer alone across all states. Rows $(0, 0)$ and $(1, 1)$ have $\beta = 0$, yet their future answers after $T_{\mathrm{mix}}$ are $0$ and $1$.

The refinement $m_0(s) = (\beta(s), c)$ reconstructs $x$ and permits reading the transported question. If current $\beta$ is also protected, this joint record retains both works. If only future $x$ is protected, presentation of $x$ suffices. Required memory depends on the target.

The former pair is now incorporated into the act, and the act into the verifiable access apparatus. Source state, result representation, and the question directed to it are coordinated; disclosure returns maps, frame, and shared witness. The next chapter will establish which reduced representation preserves this work and the required continuation. Inverse disclosure of the apparatus must not be conflated with the inverse execution of an action.

Verification question: which work does the chosen record preserve, and which cases still remain indistinguishable?

Detailed finite tables and multi-layer recovery are provided in Appendix B. Here, the critical conclusion for the next transition is: a question is transported together with its source reading, rather than substituted by a coincident answer.

<a id="v1-chapter-3"></a>

# Chapter 3 Sufficiency, Memory, and Assembly

The previous chapter coordinated action on source states with a question directed at its result. Now we ask whether the same work can be executed on an alternative, reduced representation. A single presentation may preserve a current answer while losing a necessary subsequent one; likewise, a retained value is not obliged to determine the admissibility or origin of a concrete act.

Sufficiency is therefore established relative to a chosen specification, question, and continuation. Memory functions here to coordinate representations: it retains precisely those distinctions and connections without which the transition ceases to function. We remain within a finite tabular frame; the objects of study become reduction maps, action descent conditions, and methods for refining insufficient representations.

<a id="tnr-P18"></a><a id="tnr-П18"></a>

## P18 Protected Work

First, let us name the work that the new representation must preserve. Let the full realization belong to $X$, the reduced representation be given by a surjective map $r: X \twoheadrightarrow B$, and the protected result be $p: X \to V$ [Def]. The codomain $B$ is chosen precisely as the set of employed records. $p$ may interrogate a state, a part of a state, the address of an act, or a trace.

The word "full" refers to declared $X$. For a state, this denotes the values and relations of the chosen carrier; for an act — additionally its rule, question, and essential provenance; for a history — the sequence of required realizations. One cannot, by recovering a state, automatically claim to have recovered all three types.

Protected work is specified prior to evaluating a representation and belongs to a declared frame. Altering $p$, the library of actions, or permitted access changes the problem. The same latent choice may be immaterial to a current answer yet indispensable to a future action. Therefore, the demand to coordinate representations does not mean an unconditional requirement to reconstruct everything: first, one must state precisely what must be returned or continued.

Verification question: which result must be returned, from what data, and following which continuation?

<a id="tnr-P19"></a><a id="tnr-П19"></a>

## P19 Sufficiency and the Negative Principle

A record $r$ is sufficient for $p$ if there exists $\bar{p}: B \to V$ such that $p = \bar{p} \circ r$ [Def]. An equivalent criterion is:

\[
r(s) = r(t) \implies p(s) = p(t).
\]

Proof [Th]. Given the existence of $\bar{p}$, identical records yield identical results. Conversely, if $p$ is constant on every preimage, define $\bar{p}(b) = p(s)$ for any $s$ with $r(s) = b$. The value does not depend on the choice of $s$; every $b$ has a representative, so the map is well-defined and unique.

Thus is constructed the transition from a reduced representation to a protected result. The map $\bar{p}$ is not obliged to return the source realization from $X$ or the provenance of its question: those are separate objectives. Its existence also does not establish the invertibility of action $T$. Coordination of a given result is weaker than invertibility of the entire representation.

The negative condition of preservation is now exact: a reduction that merges cases with distinct declared works is prohibited. A witness of insufficiency is a pair of realizations $s, t$ with identical $r$ and distinct $p$. The prohibition pertains to this task, rather than generating it from a vacuum of assumptions.

In DOT, three requirements are maintained [Def]: $Z^D$ protects essential distinctions; $Z^f$ protects admissibility, action results, and required traces; $Z^c$ protects coordinated re-description of classes. Their common object is the preserved representation of a single task. $Z^D$ for each $p$ is expressed by the criterion above. The other two requirements are disclosed below.

If only $\beta$ is protected, recording $\beta$ is sufficient. For future $\beta$ after $T_{\mathrm{mix}}$, it is insufficient: the transported question $x$ distinguishes rows $00$ and $11$. To preserve current $\beta$ alongside this future question, the record must be refined.

Verification question: is a concrete witness of loss exhibited, or is the prohibition merely declared?

<a id="tnr-P20"></a><a id="tnr-П20"></a>

## P20 Descent of Partial Action

A single coordinated answer is not yet sufficient to execute an action on a new representation. An action $T: D_T \subseteq X \to Y$ descends through records $r: X \twoheadrightarrow B$ and $r': Y \twoheadrightarrow B'$ if there exists a partial action $\bar{T}$ on $B$ with the same admissibility and

\[
r' \circ T = \bar{T} \circ r.
\]

Two conditions are necessary and sufficient [Th]. For all $s, t$ with $r(s) = r(t)$:

\[
s \in D_T \iff t \in D_T;
\]
\[
s, t \in D_T \implies r'(Ts) = r'(Tt).
\]

The first condition makes the domain of $\bar{T}$ independent of the representative; the second does the same for its value. Defining $\bar{T}(r(s)) = r'(Ts)$ on admissible classes yields the required map. The converse follows from its single-valuedness. This coordinates two methods of obtaining the result representation: first execute $T$ and then read $r'$, or first read $r$ and execute $\bar{T}$. It does not require the invertibility of $r$ or $T$; counter-questions continue to be transported by composition as in P12.

For $T_{\mathrm{guard}}$, rows $00$ and $11$ share $\beta = 0$, but only the first is admissible. Even a constant future answer cannot eliminate this loss. For $T_{\mathrm{mix}}$, admissibility is identical, but future $\beta$ values differ. These represent two distinct obstacles.

$Z^f$ demands the descent of declared operations and protected traces. A trace descends by the same criterion of constancy on preimages in the corresponding carrier of histories. An action map and a history record belong to different types.

Descent is preserved under composition [Th]. Let $T: X_0 \rightharpoonup X_1$ and $U: X_1 \rightharpoonup X_2$ descend together with admissibility through $r_0, r_1, r_2$. Then the domain of $UT$ consists of $s \in D_T$ with $Ts \in D_U$ and is saturated with respect to $r_0$. Indeed, identical $r_0$ yield identical admissibility for $T$ and identical $r_1(Ts)$; the latter determine admissibility for $U$ and the final $r_2(UTs)$. Therefore,

\[
r_2 UT = (\bar{U} \bar{T}) r_0.
\]

Here, three reading positions and two actions are bound by a shared intermediate $r_1$; the count of positions does not specify an independent geometry or free rank. The conditions are sufficient for step-by-step assembly, but not necessary for a single composite action: a subsequent step may erase a former distinction. Composing maps does not replace verifying the actual junction of events (P14). Complete substantiation, the counter-question, and the limits of preserving cost and history are disclosed in the composition analysis.

Descent through a reduced record must be distinguished from an invertible change of description of the source carrier. For a coordinated re-description $g: X \to X'$, invertible on the declared domain, and a new reading $r_{\mathrm{new}}: X' \to B_{\mathrm{new}}$, $Z^c$ requires

\[
r(s) = r(t) \iff r_{\mathrm{new}}(g(s)) = r_{\mathrm{new}}(g(t)).
\]

This yields a bijection of classes. To transfer the full specification, questions, admissibility, and actions must also be transported. Given maps $g_0: X \to X'$, $g_1: Y \to Y'$, and $T': D_{T'} \subseteq X' \to Y'$, one requires $g_1 T = T' g_0$ on the corresponding domain. For actions within a single carrier under a single map $g$, this contracts to $g T = T' g$. For example, exchanging $0$ and $1$ preserves classes of the identity reading, but alters the formula of the constant action "output 0". A bare bijection of classes does not transfer the entire grammar.

Verification question: does the record determine admissibility and the next class, or merely the current value?

<a id="tnr-P21"></a><a id="tnr-П21"></a>

## P21 Refinement Order and the Cost of Independent Answers

If a chosen representation does not preserve the required work, one must specify how to refine it. A presentation $r_2$ refines $r_1$ if $r_1 = f \circ r_2$ for some map $f$ [Def]. From $r_2$, $r_1$ is recovered. Mutual refinement signifies identical discriminated classes, even if the names of answers differ.

The count of classes does not determine their composition. Two readings with two answers may distinguish different pairs of states. Therefore, a partition is retained by preimages, rather than by its cardinal size alone.

On five free binary positions, if three values are known and no additional relations exist, four compatible states remain. To reconstruct all five values, at least two additional binary answers are required [Th]: a single answer distinguishes at most two cases. Two answers are sufficient if they genuinely distinguish all four cases. Their independence and accessibility require verification; repeating a question does not increase discriminating power.

If only a single inaccessible feature is protected, one new answer may suffice. If it is already deduced from what has been retained, no new answer is needed. If the accessible library cannot distinguish the remaining states, no amount of repetition solves the problem.

The rank of the full carrier, the size of the current preimage, and the number of required new questions are distinct quantities. Transferring data into memory or another presentation does not render them known in advance.

Verification question: do the new answers genuinely separate the target preimage, and by what action can they be obtained?

<a id="tnr-P22"></a><a id="tnr-П22"></a>

## P22 Coarsest Stable Memory

Let us construct a representation coordinated not only with a single current answer, but also with an accepted library of continuations. In a finite deterministic task, let us choose protected current answers and a finite library of partial actions [Def]. The initial partition groups states by these answers. Next, we split each class by the admissibility of all actions and by the classes of their results. We iterate until no new divisions occur.

The resulting partition is stable: within a single class, protected answers, admissibility, and subsequent classes are identical. This permits executing the accepted library on the classes and preserving the results of any finite admissible word.

The algorithm terminates [Th], because every genuine refinement increases the number of classes, which cannot exceed the finite number of states. Any other stable refinement of the initial record must refine every intermediate step: it preserves initial answers, admissibility, and subsequent classes of its own, and hence also the coarser classes already constructed. By induction, it refines the terminal outcome. The outcome is the coarsest stable record for the given task.

The resulting record can be used as the continuation state for precisely this task. This is minimality with respect to distinction, not an optimization of physical memory, query costs, or computation time. Changing the library of actions or the source family of protected questions demands a fresh verification.

The same terminal relation can be defined as agreement on protected answers after all finite words of actions, including the admissibility of each word. Inapplicability is recorded separately from a standard answer. One-step stability preserves these tests by induction, while agreement across all words preserves subsequent classes. This explains the connection of the finite algorithm to required continuations; exhaustive enumeration of words is unnecessary for its execution.

For protected $\beta$ and action $\sigma$, the initial two classes suffice. Adding $T_{\mathrm{mix}}$ splits both pairs and demands all four states. Adding partial $T_{\mathrm{guard}}$ also splits pairs by admissibility.

History may be an essential part of $X$. If it is not included in the terminal state and is protected separately, the algorithm on four rows does not demonstrate sufficiency for arbitrary histories. The carrier must be refined prior to applying the theorem.

Verification question: relative to which library is memory stable, and in what partial order is it minimal?

<a id="tnr-P23"></a><a id="tnr-П23"></a>

## P23 Joint Assembly of Readings

Coordinating several representations requires a shared source, not merely compatible values. Let $q_j: X \to B_j$ pertain to a single full realization in the declared frame. The joint record

\[
Q(s) = (q_1(s), \ldots, q_k(s)), \qquad R = \operatorname{im} Q \subseteq \prod_j B_j
\]

retains only realizable combinations [Def]. Each projection returns its own reading. If $Q$ is injective, a unique inverse assembly of state exists on $R$. For target $p$, constancy of $p$ on preimages of $Q$ is sufficient.

This inverse assembly unfolds the state from a joint representation. Its mere existence does not establish the invertibility of action $T$ and does not replace counter-transfer $q \circ T$. If an addressed question or act must be reconstructed, its provenance must belong to $X$ and to the protected work, or be recovered from separately preserved foundations.

In our example, $(\beta, c)$ returns $x$ and the full state $S$. Assembly requires named positions and a shared source. Substituting $\beta$ from one event and $c$ from another may produce an admissible row that is not the former realization.

A joint record is a relational structure. Its set of admissible words, its sufficiency, and the correctness of actual execution require distinct verifications. An admissible result with a precisely reconstructed act may still fail to correspond to an intended action.

Verification question: do several answers originate from a single realization, or merely share an identical form?

<a id="tnr-P24"></a><a id="tnr-П24"></a>

## P24 Local Closure

The boundary of a working representation depends on which continuations have been permitted. Closure is defined relative to a carrier and a list of rules [Def]. For facts, one may add deducible facts; for questions — compose permitted queries; for partitions — attain stable refinement. These operations must not be proclaimed as a single law without a map between their types.

In the inclusion order, closure typically demands extensivity, monotonicity, and idempotence [Ext]. These properties must be verified for the chosen operator. A closed set contains everything required by the given rule, but not "everything in existence."

On a fixed $X$ and within a fixed library of tests $\Omega$, there exists a classical Galois connection reversing the inclusion order [Ext, Th]. $\operatorname{Eq}(P)$ joins states on which all $p \in P$ coincide; $\operatorname{Inv}(R)$ contains accessible tests constant on relation $R$. Then

\[
P \subseteq \operatorname{Inv}(R) \iff R \subseteq \operatorname{Eq}(P).
\]

Both sides test the same pairs of states and queries. However, this static correspondence does not add future questions. For $P = \{\beta\}$, all questions in $\operatorname{Inv}(\operatorname{Eq}(P))$ are constant on $\beta$-classes; $x$ is not included, even though $T_{\mathrm{mix}}^*\beta = x$ is required downstream. P22 additionally closes tests under pushforwards/pullbacks by chosen actions and their admissibility conditions. The distinction between these two operations is maintained in full analysis (§7).

The arithmetical example $2 \cdot 3 - (2 + 3) = 1$ in numerical reading recovers the original unit as the difference of two results. To render this a local cycle of actions, one must preserve arguments, operations, and access. Numerical equality alone is insufficient for computational closure.

In the factorization branch, closure of known divisors under GCD, LCM, and complement does not automatically include saturation of prime multiplicities. A separate action possesses its own question and foundation. This example will be disclosed in Chapter 7.

Verification question: which rules terminate local work, and what is excluded from their closure?

<a id="tnr-P25"></a><a id="tnr-П25"></a>

## P25 Existence, Access, and Cost

The constructed coordination of maps does not guarantee that a participant can make use of it. Three circumstances are verified separately [Def]: the map is mathematically defined; its values distinguish protected cases; the correct value can be obtained by an admissible action at a declared cost.

The composition $q \circ T$ always defines a question on the domain of the action. But if the current participant knows only $\beta$, the transported question $x$ may be inaccessible. Evaluating the truth table of all possible answers does not reveal the value of an unknown row.

A natural number $N$ uniquely determines its prime factorization. The unknown nature of this factorization prior to computation does not imply the existence of multiple distinct factorizations for a single exact $N$. The loss of the exponent list under reduced reading represents an authentic informational loss. These two situations demand distinct verifications.

Preserved addressed memory also carries a cost of access and usage entitlement. Re-reading a paid source and computing a new fact are distinct actions. Presenting an ostensibly known latent answer at the moment of choosing an action would violate the declared computation frame.

Verification question: by what permitted method was the required unknown value obtained?

<a id="tnr-P26"></a><a id="tnr-П26"></a>

## P26 False Docking and the Common Third Participant

Pairwise compatibility does not guarantee global jointness [Th]. In the tripartite law $x \oplus c = \beta$, any given pair of values admits a unique third. Yet the triple $x = 0, c = 0, \beta = 1$ has no realization. Distinct pairwise witnesses do not join into a shared witness.

In like manner, false docking arises. Suppose a first event terminates in $b$, a presented second event begins in $c$, and the reduced record does not distinguish $b$ and $c$. On the answers, two edges are connected, but these two events do not yet constitute a single source path. Even if the second action is permitted on $b$, executing it on $b$ would have been a different event. For the given path, a shared intermediate participant or a certified transfer of precisely that participant is needed.

The connecting third element of two flows consists of the conditions of shared source, admissibility, answer coordination, and continuation. When protecting a concrete act, these conditions unfold as a shared witness of the same event and its frame. It is not replaced by the intersection point of drawn axes, a constructed fulcrum, or a pointer to that fulcrum. For two records with identical answers, their relation to a single event must also be verified.

When criteria P19–P20 and task transfer conditions are met, the negative requirements $D, F, C$ yield a positive result: protected queries and traces descend, admissible actions compose on classes, and coordinated re-descriptions yield class bijections. The proofs follow from constructing maps on preimages and induction on the length of an admissible word. Full task transfer additionally transports all operations and domains.

Verification question: where is the shared participant through whom the parts are joined?

## Chapter Summary

The transition to a reduced representation now possesses rigorous conditions: the protected result must be recoverable through it, the action must preserve admissibility and the subsequent class, and joint assembly must pertain to a single source. Memory supports this work; it does not replace the subject of study. The underside, access, and cost have been named, and a finite mechanism of stable refinement has been obtained. For multiple readings, jointness is preserved, and for a concrete continuation — a shared witness.

In the next chapter, questions themselves will become the objects of new representations. Their count, graph, composition law, and linear presentation will be distinct readings of a single explicitly chosen family. For each transition, a new carrier must be declared and the source of the former question preserved. The preservation criterion remains invariant; shifting the object level does not by itself introduce an independent binary bit.

Detailed finite and multi-layered realizations are disclosed in Appendix B. Their conditions pertain to chosen models and are not proclaimed as a universal law for every carrier.

<a id="v1-chapter-4"></a>

# Chapter 4 Questions as Objects

Hitherto we have constructed the representation of a state and transported a question alongside an action. Now the very apparatus of a question becomes the object of new representations. This is the first thoroughly analyzed transition between levels of description: a former relation acquires its own address, yet retains its source, governing law, and mode of disclosure. Memory and sufficiency will verify precisely what is preserved under such a transition.

We remain within a finite frame. The source carrier consists of four states:

\[
S = \{00, 01, 10, 11\}, \qquad s = (x, c), \qquad \beta = x \oplus c.
\]

Binary values here belong to numerical reading. The structural $i_{\mathrm{str}}[E]$ designates the preserved folding of a device and does not substitute for a numerical unit. The complex unit is not yet introduced in this chapter.

Questions will be read as truth tables, vertices, edges, and participants in a composition law. Each transition receives a dedicated domain and a distinct relation. Real geometry appears only after declaring a field and a metric. Finite recovery examples are provided in Appendix B.

<a id="tnr-P27"></a><a id="tnr-П27"></a>

## P27 Graph and Object-Level Lift of Relations

Stance of description — graph reading of former $S$, domains DM05 and DM03. Foundations: P05, P06, P23, and P10. The standard definition of a finite undirected graph is borrowed: vertices and explicitly chosen pairs of adjacent vertices [Ext].

If adjacent states are defined as those differing by a single bit, we obtain a 4-cycle (square). Its four edges represent elementary flips of $x$ or $c$. If we permit comparing any pair of distinct states, we obtain the complete graph $K_4$ with six edges. The vertex carrier is identical; immediate adjacencies differ.

The next lift makes each edge $\{s, t\}$ an individual participant. Its disclosure returns the two source endpoints and the address of the former graph. One may define a new adjacency: two such participants are adjacent if the source edges share an endpoint. This is the **line graph** of the source graph. Here the word "line" designates a graph-theoretic construction, not a vector space.

$K_4$ has six edges. Each edge is opposed by a unique disjoint edge; with all four other edges, it shares an endpoint. Therefore,

\[
L(K_4) = K_{2,2,2},
\]

the octahedron graph. Its structural scalar six counts the former edges that have become vertices. Twelve new edges count pairs of relations sharing a common participant. A binary rank is not assigned to this graph merely from the number six.

The transition preserves incidence: a new position knows its source endpoints. If only the upper drawing is retained without these addresses, the named source states cannot be automatically recovered from it. The former whole has become the foundation of the new, rather than vanishing upon a shift of role.

Verification question: what does a new vertex denote — a state or a relation between two states? Via which map are its endpoints recovered? If the square is replaced by $K_4$, which new comparisons are genuinely added?

<a id="tnr-P28"></a><a id="tnr-П28"></a>

## P28 Local Windows and Eight Affine Questions

Stance of description — the space of truth tables of functions on $S$, domains DM01 and DM03. Foundations: P27 and P10. Binary arithmetic and function composition are borrowed [Ext]. The four states of $S$ possess two independent bits; a question on them is a distinct type of element.

In an arbitrary binary truth table, an answer can be chosen independently in each of the four rows. Therefore, there are sixteen questions in total. Any such question is uniquely written as

\[
q(x, c) = k \oplus ax \oplus dc \oplus exc, \qquad k, a, d, e \in \mathbb{F}_2.
\]

These are four independent coefficients of the table. The condition $e = 0$ isolates eight **affine questions** [Def]. Let us designate this family by $W$. Its addressing rank is three. The choice of affinity is a condition of the present environment, not a consequence of the bare existence of four states.

To align addresses with a color cube, choose the basis $x, c, 1 \oplus x \oplus c$:

\[
q_{rgb}(x, c) = rx \oplus gc \oplus b(1 \oplus x \oplus c).
\]

The letters $r, g, b$ are binary coefficients. The color nomenclature assists in distinguishing addresses; physical properties of color are not transported into this map. The constant unit question is denoted by $u$, and the constant zero question by $0_W$.

The eight addresses of family $W$ possess three free addressing bits. These are not eight free coefficients of a single question: the present question is still defined on the four rows of $S$. An arbitrary rule whose argument becomes the octet $W$ itself will be a new object; its eight coefficients appear in P32.

| Question Address | Name | Table on rows 00 01 10 11 |
|---|---|---|
| 000 | $0_W$ | 0000 |
| 100 | $x$ | 0011 |
| 010 | $c$ | 0101 |
| 001 | $\bar{\beta}$ | 1001 |
| 011 | $\bar{x}$ | 1100 |
| 101 | $\bar{c}$ | 1010 |
| 110 | $\beta$ | 0110 |
| 111 | $u$ | 1111 |

The complement $\bar{q} = q \oplus u$ flips every answer and preserves the unoriented partition of $S$ into two sides. Under a different basis, the address of the constant question may change; its type and complementation law are preserved by addressed transfer.

Now let us restore provenance to the question. For access $m_\beta: S \to B_\beta$, $m_\beta(s) = \beta(s)$, the carrier $B_\beta = \mathbb{F}_2$ contains two values. All rules on it form

\[
\Omega(B_\beta) = \operatorname{Map}(B_\beta, \mathbb{F}_2).
\]

Four rules realize the local window $\{0_W, u, \beta, \bar{\beta}\}$. Two accessible values and four rules over them belong to different types; the local window does not provide an arbitrary question from $W$.

The question itself retains $\Gamma, m, B, \Omega, h$, and the realized truth table has the form $q = h \circ m$. If state and affine question are chosen independently, there are $4 \cdot 8 = 32$ joint realizations. The answer is already determined by this pair, so it adds no new free bit.

Verification question: does the word 110 refer to a state or to a question? Why does knowledge of $\beta$ permit specifying four local rules, yet fail to disclose $x$? What changes if affinity is removed?

<a id="tnr-P29"></a><a id="tnr-П29"></a>

## P29 Active Scene and Shared Face Witness

Stance of description — graph on questions and its relation to source states, domain DM05. Foundations: P28 and P27. Let us introduce the active scene:

\[
A_6 = W \setminus \{0_W, u\}.
\]

Its six questions are balanced: each has two answers 0 and two answers 1. The support $\operatorname{supp}(q) = \{s: q(s) = 1\}$ is a 2-element subset of $S$, which corresponds to an edge of $K_4$. All six such subsets occur exactly once.

Adjacency is defined by the intersection of supports in a single state. Complementary questions possess disjoint supports. All other pairs are adjacent. Thus emerge three opposite axes:

\[
\{x, \bar{x}\}, \qquad \{c, \bar{c}\}, \qquad \{\beta, \bar{\beta}\}
\]

and the twelve edges of the octahedron. Opposition here is the complementation of answers on a single $S$, not the negation of a real vector; geometric realization appears separately.

From each axis, one endpoint may be chosen. This yields eight triangular faces. Their pairwise relations do not yet determine whether three chosen "yes" answers can be obtained simultaneously.

| Question Triple | Shared State with Three "Yes" Answers |
|---|---|
| $\bar{x}, \bar{c}, \bar{\beta}$ | 00 |
| $\bar{x}, c, \beta$ | 01 |
| $x, \bar{c}, \beta$ | 10 |
| $x, c, \bar{\beta}$ | 11 |
| $\bar{x}, \bar{c}, \beta$ | None |
| $\bar{x}, c, \bar{\beta}$ | None |
| $x, \bar{c}, \bar{\beta}$ | None |
| $x, c, \beta$ | None |

For the first four triples, the XOR sum of all questions equals $u$; for the remaining four, it equals $0_W$. In the latter case, three unit answers would violate this law. Pairwise compatibility exists across all eight faces; a shared witness exists in only four.

This is the precise locus of the third structure: the source state binds multiple answers into a single realization. If only the octahedral graph is communicated, the distinction between the two quadruples of faces is lost. For actions, an event address is additionally required, since a single state can participate in multiple acts.

Verification question: why is each of the questions $\bar{x}, \bar{c}, \beta$ compatible with the other two separately, yet the entire triple lacks a shared witness? What data must be added to the graph to detect this failure?

<a id="tnr-P30"></a><a id="tnr-П30"></a>

## P30 Affine Center and Three Axes

The stance of description shifts: truth tables of questions are represented as real vectors of four coordinates. Domains DM07 and DM08; foundations P29 and P09. The field $\mathbb{R}$, coordinatewise operations, and the standard inner product are borrowed [Ext]. The binary XOR sum and the real sum possess distinct addresses.

In this representation, each complementary pair possesses a single midpoint:

\[
m = \frac{q + \bar{q}}{2} = (1/2, 1/2, 1/2, 1/2).
\]

Coordinate reading of the center yields one-half. Changing the origin $q \mapsto q - m$ translates that same center to the zero vector. This is an explicit connection between two representations, not an identification of all usages of zero. The metacenter here is the role of a relative coordination fulcrum for precisely these pairs in the chosen representation. It is realized by the constructed midpoint $m$; the existence of one and the same fulcrum across all mathematical domains does not follow from this.

Let us unfold the types of the transition. Inclusion of tables, centering, and new presentation have the form

\[
\iota: W \hookrightarrow A = \mathbb{R}^S, \qquad C_m: A \longrightarrow A, \quad C_m(a) = a - m, \qquad \chi: W \longrightarrow A.
\]

The map $C_m$ is defined on the whole of $A$, is invertible via $v \mapsto v + m$, and is affine, though not linear relative to the former zero. The point $m$ itself is not this map. Pointing to the constructed fulcrum also belongs to a distinct type:

\[
\eta_m: \{*\} \longrightarrow A, \quad \eta_m(*) = m, \qquad \eta_0: \{*\} \longrightarrow A, \quad \eta_0(*) = 0_A.
\]

Thus, the fulcrum $m$, pointer $\eta_m$, and transfer $C_m$ are not interchangeable. Two typed diagrams are coordinated by a common centering map:

\[
\chi = C_m \circ \iota, \qquad \eta_0 = C_m \circ \eta_m.
\]

The first transports truth tables; the second — their fulcrum. The source and target carriers $A$ coincide as sets, but perform different work. Four carrier loci $W, \{*\}, A, A$ and five maps are structural scalars of this relational record; they do not prove a dimension of four, five free bits, or a tetrahedron. One-point pointers are admissible as set maps; a linear map from a zero-dimensional space could not select a non-zero $m$. The law of constructing a fulcrum resides in the average of complementary tables, rather than emerging from a pointer alone.

In subsequent real formulas, the short names $x, c, \beta$ denote their truth tables after $\iota$. For the active scene, the domain can be restricted:

\[
H = \left\{a \in A : \sum_{s \in S} a(s) = 2\right\} = m + V_0, \qquad V_0 = \left\{v \in A : \sum_{s \in S} v(s) = 0\right\}.
\]

Then $\iota: A_6 \hookrightarrow H$ and $C_m: H \to V_0$. One cannot substitute full transfer with the map $C_m: A \to V_0$: for $C_m(0_A) = -m$, the coordinate sum is $-2$. The domain of full presentation and the domain of active restriction are distinct.

Let

\[
v_x = x - m, \qquad v_c = c - m, \qquad v_\beta = \beta - m.
\]

Each vector has two coordinates equal to $1/2$ and two equal to $-1/2$. Their squared lengths equal one, and their pairwise inner products equal zero. Consequently, the centered scene

\[
\{\pm v_x, \pm v_c, \pm v_\beta\}
\]

is a regular octahedron in a 3-dimensional subspace of $\mathbb{R}^4$. Here the number three counts real independent directions; the source state continues to possess two independent bits.

For $m$, the squared length equals one, and the inner product with each of $v_x, v_c, v_\beta$ equals zero, since the sum of coordinates of these vectors is zero. Therefore, $m, v_x, v_c, v_\beta$ form an orthonormal basis of the whole of $A$, so that $A = V_0 \oplus \mathbb{R}m$. The constant pair is not destroyed: $\chi(0_W) = -m$, $\chi(u) = m$. The complete centered octet has the form

\[
\chi(W) = \{\pm m, \pm v_x, \pm v_c, \pm v_\beta\}.
\]

Its convex hull is the 4-dimensional cross-polytope (16-cell), with eight vertices, 24 edges, and 16 tetrahedral 3-faces. The active octahedron lies in $V_0$. The coefficient cube of addresses $W$ has only 12 edges: this is a different adjacency on the same eight questions. The real reading $3+1$ is not four free binary coordinates and does not claim physical spacetime.

The center $m$ is not a binary question: its values equal one-half. Nor is it a state of $S$ or the chosen fulcrum $c$. Its source consists of table pairs, its field is real, its law is the arithmetic mean, and its new origin is subtraction of $m$.

Center and deviation together reconstruct the pair $m - v, m + v$. A bare center without deviation selects neither an axis, nor a scale, nor a marked endpoint. Thus the inverse explanatory direction is preserved: opposites determine the center, while the center determines their presentation only in conjunction with the necessary underside.

Inverse disclosure of a table is performed by adding $m$. A counter-question has a different form: a rule $h$ on the target presentation is pulled back as $h \circ \chi$, preserving its native domain. For example, $h_s(v) = 1/2 + v(s)$ on $A$ has real output, while on $\chi(W)$ it returns the binary answer $h_s(\chi(q)) = q(s)$. Full conditions and self-application of the two diagrams are disclosed in the metacenter study (§§4–7 and 12–13); color transport of a relative fulcrum is examined in Appendix E7.

Verification question: is $m$ an accessible answer of a binary observer? What data beyond the center are required to disclose a chosen pair of opposites?

<a id="tnr-P31"></a><a id="tnr-П31"></a>

## P31 Fano Law of Questions and Scene Windows

Stance of description — incidence on non-zero affine questions, domains DM05 and DM06. Foundations P28 and P29. Retaining XOR as the composition law, define

\[
L_7 = W \setminus \{0_W\}.
\]

For distinct non-zero $a, b$, the triple $\{a, b, a \oplus b\}$ constitutes a line. Every pair of points determines a unique line; every line contains three points. Twenty-one pairs partition by threes, yielding seven lines. This is the Fano plane: points are questions, lines are their composition law. Over $\mathbb{F}_2$, a non-zero vector already represents its 1-dimensional subspace.

Three lines passing through $u$ contain complementary pairs. The other four lines coincide with the four faces of the octahedron lacking a shared true state. Thus, the composition law and joint satisfiability are rigorously linked, but perform distinct works. A Fano line is not a trajectory of three events: ordering and admissible actions must be specified separately.

The local window $\{0_W, u, q, \bar{q}\}$ is closed under XOR. Its three non-zero questions form a Fano line; the two balanced endpoints form an axis of the octahedron. The source domain $B$ contains access values; this window contains rules realized on $S$. Their maps preserve the distinction of types.

Select $q_* \in A_6$, for instance $\beta$, and denote $V_5 = A_6 \setminus \{q_*\}$. Then

\[
V_5 \sqcup \{q_*\} = A_6 = L_7 \setminus \{u\}, \qquad L_7 \sqcup \{0_W\} = W.
\]

These are two presentations of a single active scene. The first restores the marked question to five alternatives. The second separates the constant question from the non-zero law, retaining it in the background. Disclosing the scene must preserve $S, W, q_*$, and, for an act, the shared event address.

In the inherited adjacency, $V_5$ is a square pyramid: the endpoint opposite to $q_*$ is connected to four equatorial vertices forming a square. The scalars five, six, seven, and eight here count questions of a specific family. The Petersen graph possesses a different carrier and does not automatically follow from a quintuple.

Now let us execute an authentic counter-flow. Under

\[
T(x, c) = (x \oplus c, c),
\]

the future question $\beta$ pulls back to current $x$. Along with it, the window $\{0, u, \beta, \bar{\beta}\}$ pulls back to $\{0, u, x, \bar{x}\}$, and the quintuple without $\beta$ to the quintuple without $x$. Both assemblies again yield the same sextuple. Source $B_{\beta, 1}, \Gamma_1, m_1, h_1$ remain in the provenance of the transported question.

An observer with access currently restricted to $\beta$ cannot yet express this $x$. If current $\beta$ is protected, access to $(\beta, c)$ is required. Moving a question within a complete environment and refining access are distinct transitions.

Completeness depends on actions. On $S$, there exist 256 total maps. The transfer $q \mapsto q \circ T$ preserves $A_6$ for exactly 24 permutations, $W$ for 64 affine maps, and all sixteen questions for all 256. Proofs of these numbers are given in Appendix B.

Verification question: what does Fano retain beyond seven names? Why do two assemblies $5/7 \to 6$ not substitute for the counter-transfer of a question? How does erasing a coordinate cause a former background question to become manifest?

<a id="tnr-P32"></a><a id="tnr-П32"></a>

## P32 Alternating Law and Two Quadruples

Stance of description — extension of the carrier of law realizations, domains DM01, DM06, and DM08. Foundations P10, P30, and P31. The former constant condition now becomes an object of choice:

\[
\beta = x \oplus c \oplus \varepsilon.
\]

Independence of $\varepsilon$ is declared. We obtain eight joint rows $(x, c, \beta, \varepsilon)$, but only three independent bits: $\beta$ is determined by the rest. For fixed $\varepsilon$, the former quadruple of realizations remains. Two values of the law yield two such quadruples.

If $\varepsilon$ is forgotten and $(x, c, \beta)$ is presented, the two quadruples differ by the parity of the sum of three values. In the real cube $\{0, 1\}^3$, each quadruple has all pairwise distances equal to $\sqrt{2}$, and thus constitutes a regular tetrahedron. Together they fill the eight vertices of the cube. This is a declared geometric realization, not a new degree of freedom derived from a drawing.

Partitioning vertices is not partitioning the cube's volume: the union of these two solids does not fill the cube, although their convex hull is the cube. For color correlation, choose coordinate naming $(r, g, b) = (x, c, \beta)$ separately; it does not identify states of the alternating law with questions of $W$. In this presentation, the intersection is a regular octahedron with vertices $m_{RGB} \pm \frac{1}{2}e_j$, where $m_{RGB} = (1/2, 1/2, 1/2)$. Its vertices are not the six source binary RGB/CMY colors; the hull of that source sextuple forms another, metrically irregular octahedron. The map between readings is disclosed in E7 and D5.

The paired exchange $\varepsilon \mapsto \varepsilon \oplus 1$ requires a coordinated exchange of $\beta$. Altering only the parameter while retaining the former triple violates the law. The overarching structure is the table of admissible joint rows; it binds both copies and determines permitted disclosure.

The new octet consists of states of the alternating law. Former $W$ consisted of questions on fixed four states. Their cardinalities coincide, but their types, actions, and sources differ. An additional map between them may be chosen; numerical coincidence of the number eight is insufficient.

There is also a third meaning of an octet. Here $(r, g, b)$ once again denotes address coefficients of question P28, not the color naming of an alternating-law state from the preceding paragraph. If the argument of a new binary rule $h$ is this address of a question from $W$, then the complete rule is uniquely expressed as

\[
h = \theta_\varnothing \oplus \theta_r r \oplus \theta_g g \oplus \theta_b b \oplus \theta_{rg} rg \oplus \theta_{rb} rb \oplus \theta_{gb} gb \oplus \theta_{rgb} rgb.
\]

The eight coefficient positions partition by degree as $1 + 3 + 3 + 1$. Their indices are addressed by three bits, and freely specifying all eight $\theta$ values yields $2^8 = 256$ laws. The argument rank remains three; the rank of the full family of laws is eight. For address $x_T$ with ones at positions $T \subseteq \{r, g, b\}$, we have $h(x_T) = \bigoplus_{S \subseteq T} \theta_S$: the function value at a vertex is not obliged to equal the homonymous coefficient. Now the object of analysis is a question about the law of the former question, rather than a ninth free bit. Complete coefficient and color realization preserves both readings and their invertible transformation.

Verification question: which former condition has become independent? Why do four role fields contain three free bits? What must be transported alongside $\varepsilon$ to avoid violating the law?

<a id="tnr-P33"></a><a id="tnr-П33"></a>

## P33 Distinctions, Fulcrum, and Position Order

Stance of description — reconstruction of four named binary positions, domains DM03, DM05, and DM14. Foundations P14, P22, P10, P23, and P27. This is a new carrier: $\{0, 1\}^4$ has sixteen states. It is not identical to the former 4-row $S$.

Let $\pi$ specify the order of reading names, and $y_i = x_{\pi(i)}$ be the observed sequence. The comparison graph retains relative distinctions $d_{ij} = y_i \oplus y_j$. Three comparisons with the initial position already suffice for the relative state:

\[
d_{01}, \quad d_{02}, \quad d_{03}.
\]

Comparison possesses its own projecting provenance: $m_{ij}(y) = (y_i, y_j)$ presents a pair in $B_{ij} = \mathbb{F}_2^2$, while the XOR rule returns $d_{ij}$. The fulcrum reads a single value in $\mathbb{F}_2$. Order is presented in the permutation family of four names. These three layers are therefore not three identical binary questions, even if stored together.

Overall complementation of all $y_i$ preserves each comparison. Therefore, a connected comparison graph leaves exactly two possible states. The fulcrum $a = y_0$ selects the side of this pair:

\[
y_0 = a, \qquad y_i = a \oplus d_{0i}.
\]

Combinatorial ordering reconstructs the addresses:

\[
x_{\pi(i)} = y_i.
\]

The three layers read distinct works of a single realization. The graph returns relative distinctions; the fulcrum — absolute values; order — binding to names. Their shared foundation is the same reading act and its coordinated positions. Without it, identical local data can erroneously join foreign realizations.

Order has four positions and 24 permutations. These 24 choices do not constitute an integer number of free binary bits. Sixteen states of four positions and the choice of order together yield $16 \cdot 24 = 384$ realizations. Value repetitions do not destroy distinctions of order if reading history is protected.

If all six comparisons are retained, redundant conditions arise:

\[
d_{ij} \oplus d_{jk} \oplus d_{ik} = 0.
\]

Two distinct valid comparison sextuples differ in at least three places. Therefore, under the condition "at most one comparison is corrupted," the nearest valid sextuple is uniquely determined. This is an auxiliary theorem derived from the complete graph and declared noise model; an inverse formula alone does not prove it. Fulcrum and order must be protected separately, as shown in Appendix B.

Verification question: is the state, order, or only their equivalence class reconstructed? Why does a fulcrum not replace $\pi$? What data remain if the shared event is forgotten?

<a id="tnr-P34"></a><a id="tnr-П34"></a>

## P34 Six Centers and Twelve Relations

Stance of description — real realization of the octahedron and new reading of its edges, domains DM05 and DM08. Foundations P27, P29, and P30. Let $e_1, e_2, e_3$ denote the three orthonormal directions of the scene; its vertices have the form $\pm e_i$.

For edge $\{v, w\}$, introduce a new position:

\[
r_{vw} = v + w.
\]

This is twice the midpoint of the former edge. The scale is named; the address of the new position retains both endpoints. In total, there are twelve such positions: four sign choices for each of the three pairs of distinct axes.

Edges emanating from former vertex $e_1$ yield four new positions:

\[
e_1 + e_2, \quad e_1 - e_2, \quad e_1 + e_3, \quad e_1 - e_3.
\]

Their two opposite pairs have a common mean $e_1$. Consequently, the former vertex has become the center of two conjugate pairs of the next level. The same construction holds for all six vertices. Each new position belongs to two such quadruples; the count of incidences is $6 \cdot 4 = 12 \cdot 2 = 24$.

The center of a lower position is reconstructed from upper opposites given preserved map, scale, and incidence. The bare number twelve does not define this inverse assembly. The scalar here counts edge positions, not independent binary coordinates.

On the new positions, there are at least two natural adjacencies. If all pairs of former edges sharing an endpoint are joined, we obtain $L(O_6)$ with 36 edges: in each of the six quadruples there are six pairs. If we take geometric edges of the convex hull of twelve vectors, we obtain the cuboctahedron with 24 edges: in each quadruple, a square remains.

Discarded diagonal connections of the square do not vanish from the source incidence. They are absent only in the chosen exterior graph. This is an example of two graph domains on a single carrier that cannot be identified merely by a vertex list.

There is also an exact assembly of two former wholes. Let $O_1 = \operatorname{conv}\{\pm e_i\}$ denote the source convex solid; the sextuple $O_6$ counts its vertices. In the same coordinates, define:

\[
C_1 = \{x : |x_i| \le 1\}, \qquad O_2 = \{x : |x_1| + |x_2| + |x_3| \le 2\}.
\]

The cuboctahedron equals $C_1 \cap O_2$. Its six square faces originate from the cube, and eight triangular faces from the octahedron. A new vertex is simultaneously the midpoint of an edge of each source. The octahedron here is twice as large as source $O_1$; without preserving this scale, the intersection would contract to $O_1$.

Two streams of conditions converge upon a single admissible point, while a third structure retains both provenances of its boundaries. This does not mean the entire solid is a single intersection line: the shared seam of surfaces is a graph of 24 edges. A counter-question under action on a point is still transported by rule P12, with its native norm domain and threshold, rather than replaced by a geometric designation.

Further disclosure in Appendix D5 links this sector to the tetrahedral pair and golden pair. The complete atlas preserves independent proofs, scales, and separate projections.

Verification question: which map renders the former vertex a center? What is preserved in the new position beyond coordinates? Why does the edge count change from 36 to 24 without altering the vertex count? Which sources and scale unfold from the new joint solid?

<a id="tnr-P35"></a><a id="tnr-П35"></a>

## P35 Passport of Finite Graph Transition

Stance of description — comparison of graph presentations with provenance, domains DM05 and DM16. Foundations P27, P31, and P34. A passport retains carrier, adjacency relation, map from source, excluded positions, protected connections, and admissible subsequent actions. These are interrelated roles of a record, not automatically six vertices of a new octahedron.

Forward construction of a passport transports the source into a new presentation; inverse disclosure verification asks which source and law can be recovered from it. A common address correspondence links these passes. This is not in itself the counter-transfer of a question: that requires a concrete map $T$, target question $q$, and rule $q \circ T$. If only the name of a figure is retained, the backward pass breaks off already at its provenance.

Return to the six color addresses distinct from $000$ and $111$. Complementary pairs possess Hamming distance three. If adjacency is chosen strictly by whole distance classes, eight variants are possible:

| Admissible Distances | Graph on Six Addresses |
|---|---|
| None | Six isolated vertices |
| 1 | 6-cycle ($C_6$) |
| 2 | Two disjoint triangles ($2 K_3$) |
| 3 | Three complement edges ($3 K_2$) |
| 1 and 2 | Octahedron ($K_{2,2,2}$) |
| 1 and 3 | $K_{3,3}$ |
| 2 and 3 | Triangular prism |
| 1, 2, and 3 | Complete graph ($K_6$) |

Eight is the number of subsets of three distance classes, not the count of all graphs on six labels. If every edge is selected independently, there are $2^{15}$ possible graphs. Choosing a relation is an autonomous action upon a presentation and must possess an address.

The abstract octahedron admits 48 vertex permutations: permutation of three axes and independent exchange of endpoints of each axis. But symmetry of the visible graph may fail to lift to its source.

For the color cube, symmetries consist of coordinate permutations and XOR by a fixed mask. Preserving the polar pair $\{000, 111\}$ admits only masks $000$ and $111$. Therefore, 12 of the 48 symmetries of the active sextuple lift into the source cube. If zero and the XOR law are also protected, only six coordinate permutations remain.

For the octahedron of questions, provenance is different: four rows of $S$ and four faces with a shared witness. Their jointness is preserved by 24 of the 48 symmetries, corresponding to permutations of $S$. Overall complementation of all answers preserves the graph, but swaps the two quadruples of faces and does not originate from a permutation of states. Results 12 and 24 pertain to different provenance conditions.

The volume now possesses a disclosable tract: state, chosen presentation, local question, active scene, question law, and full chosen carrier are linked by named maps. Transitions preserve whence they were obtained. The next chapter compares such apparatuses across distinct mathematical domains.

Verification question: which precise symmetry does the passport admit — graph symmetry, jointness-preserving symmetry, or symmetry lifting to the source cube? Which connections must be preserved for the new whole to disclose the former?

Complete finite tables, the proof of stable refinement, and an error-tolerant recovery example are assembled in Appendix B. The map of projections and color preserves the source of distinctions among these readings. Dedicated finite verification scripts are available for the [A3 reduction](verification/verify_a3_cover.jl), the [Aₙ family](verification/verify_an_rank_limits.jl), the [H3 model](verification/verify_h3.jl), and [Pauli local windows](verification/verify_pauli_local_windows.jl).

<a id="v1-chapter-5"></a>

# Chapter 5 Domains and Arithmetic Input

The preceding chapters constructed states, questions, acts, and reduced presentations. Now these constructions themselves become objects of comparison: one must reconcile different mathematical representations of the same operation. We ask which law belongs to each domain and what must be transferred along with it. Memory retains the origin of a transition, while sufficiency verifies whether the protected operation can be executed after changing representation. Numbers exhibit the size of a chosen structure; its relations are unfolded separately.

In this chapter, the locus of description is an addressed atlas of devices and maps between them. This is a subject-matter level above an individual model, not an additional free bit within the model. Ordinary numbers, sets, fields, and algebras are employed as declared mathematical instruments. Their own theorems are not deduced from the number of slots in a passport.

<a id="tnr-P36"></a><a id="tnr-П36"></a>
## 5.1 The Passport as an Unfoldable Device

Domain DM16. Projection — a device is examined through its carrier, relations, reading, and conditions of further operation. Grounds: P07, P11, P19.

**Definition.** The passport of a device is an addressed specification

\[
\mathscr D=(C,R,Q,\Gamma),
\]

where $C$ contains instantiations of the designated types, $R$ specifies their admissible connections, $Q$ contains selected readings, and $\Gamma$ indicates the protected operation, access, and permitted continuation. Here $\Gamma$ unfolds the already introduced interface frame.

The four positions constitute the structural scalar of this presentation: they possess distinct roles and associated domains. The relations $R$ are defined on $C$; the maps $Q$ read instantiations of $C$; the requirements $\Gamma$ apply to these maps and admissible modifications. Permuting the four fields is not itself declared a symmetry. A tetrahedron would require six additional defined relations between the positions.

The forward traversal of a passport specifies a device and obtains an answer. The reverse unfolding links the answer to compatible instantiations, a question, and a preserved origin address; a single answer cannot recover this data without the necessary memory. The counter-transfer of a question is a distinct map \(q\mapsto q\circ T\) via a designated action. The common third is that very same admissible case on which these operations are reconciled. A passport may be folded into \(i_{\mathrm{str},\Pi}[\mathscr D]\), retaining access to the four roles and their governing laws. Such a name does not replace the contents.

For the end-to-end model, $C$ contains four rows \((x,c)\); $R$ includes the law \(\beta=x\oplus c\); $Q$ selects questions from a declared family; $\Gamma$ defines actions and the preservation goal. In the reverse side of a concise passport remain tables, event addresses, and detailed memory. The binary rank of $C$ equals two; the four roles of the passport do not increase it to four.

Verification question: can each field be unfolded without a circular loop of mere names and return a concrete instantiation?

<a id="tnr-P37"></a><a id="tnr-П37"></a>
## 5.2 Different Operations of Changing Representation

Domains DM16 and DM04. Projection — maps between presentations of a single task. Grounds: P36, P23, P32.

We distinguish four operations already encountered. **Redescription** has an inverse map on the domain in use. **Reduction** (coarsening) partitions instantiations into classes and requires verification of sufficiency. **Extension** embeds the prior carrier into a new one. **Change of law** alters the admissible actions or relations while preserving the carrier. These four types form a working structural scalar of the route, rather than an exhaustive catalogue of all mathematical maps.

In the binary example, renaming four rows is reversible. The reading $\beta$ merges them pairwise. Adding a free parameter $\varepsilon$ to the law \(\beta=x\oplus c\oplus\varepsilon\) generates eight instantiations. Adding a mixing action to the prior library alters the sufficiency of the old reading, even if the state set remains unchanged.

Color coordinates provide an analogous distinction. Full RGB notation and full HSL notation can be mutually reconstructed according to a declared rule, provided degenerate cases are taken into account: for gray colors, hue is not uniquely defined. A single hue coordinate $H$ already discards saturation and lightness. This is a reduction, not a complete change of representation.

If a future operation inquires about the prior hue mark of a gray, that mark must remain in memory: it cannot be recovered from the gray color itself. The selected frames Lab \(4+2\) and HSL \(6+2\) count reference poles and hues, rather than independent coordinates of the complete models. Appendix E7 separates such finite sampling from coordinate transformation, reduction, and new geometric adjacency.

For every transition, the domain, origin address, action, and returned content are retained. Only reversible redescription guarantees an inverse transition of the same type. Under reduction, reverse unfolding typically returns a preimage rather than a unique former participant. A counter-question is defined by composition with the forward map and does not require its invertibility.

Verification question: have we renamed the prior, grouped cases into classes, added new cases, or altered the law?

<a id="tnr-P38"></a><a id="tnr-П38"></a>
## 5.3 Transferring an Action Together with a Question

Domain DM16. Projection — a single protected act is presented on two carriers. Grounds: P37, P22.

Let \(F:S\to S'\) map states, $T$ and $T'$ be actions, $q$ and $q'$ questions, and \(f:B\to B'\) an answer map. Reconciliation takes the form

\[
FT=T'F,\qquad q'F=fq.
\]

These equalities are verified on the declared domain. If admissibility is protected, it is required that

\[
s\in D_T\quad\Longleftrightarrow\quad F(s)\in D_{T'}.
\]

If the original answer is protected, there must exist a map for recovering it from the target representation on the image in use. History, connections, and cost receive distinct maps when included in the protected operation. Thus, transfer becomes a structural whole: two presented sides, a reconciled law, and the unfolding of their shared operation.

When $F$ is invertible, an action transfers by conjugation \(T'=FTF^{-1}\). The counter-question transfers via the same source act: \(q'T'F=fqT\). Under a reduction $F$, such a law is admissible only after verifying the constancy of the required results and admissibility across preimages.

State transfer \(s\mapsto F(s)\), the inverse map \(F^{-1}\), action conjugation, and the counter-question belong to different types. The target question itself returns as \(q'\circ F\), with preserved source \(\Gamma',B',m',h'\), if \(q'=h'\circ m'\). For RGB$\to$Lab, the encoding, white reference, and complete transformation route must be declared. Its nonlinearity does not allow one to treat selected Euclidean model rotations as conjugate without a separate verification of \(FT=T'F\). Coincidence of the metacentre role also does not prove coincidence of coordinate midpoints; an exact color example is provided in E7. Finite verifications of transfer are found in the definition projection verification and the color test suite.

The counterexample is straightforward. On \(\{0,1\}\), the identity action may be permitted only at 0. The same transition rule on a target carrier may be permitted at both values. The answers and transition formulas coincide, but admissibility has changed. Coincidence of the result table did not protect the interface.

Verification question: what is returned from the target representation — an answer, a state, the right of action, or the entire act?

<a id="tnr-P39"></a><a id="tnr-П39"></a>
## 5.4 Two Indices of Domains and Relations

Domains DM16 and DM17. Projection — a classification reading of an already constructed corpus. Grounds: P36, P27, P37.

A subject domain indicates what we operate upon and which native tools we employ. A family of relations indicates the species of law. A single domain contains multiple laws; a single law operates across multiple domains. Their connection is a multivalued correspondence, unfolded by concrete models.

| Domain | Native Operation |
|---|---|
| DM01 Binary and Logical | Values, conditions, NOT, XOR, truth, and joint consistency |
| DM02 Numerical and Arithmetical | Counting, magnitudes, fractions, and arithmetic operations |
| DM03 Combinatorial | Places, subsets, cuts, and orders |
| DM04 Order and Closures | Refinement, inclusion, fixed point, and saturation |
| DM05 Graph and Incidence | Vertices, links, paths, and multi-place membership |
| DM06 Algebraic | Composition, identity, inversion, and commutator |
| DM07 Linear and Multilinear | Field, dependencies, basis, kernel, and pairing |
| DM08 Geometric and Metric | Point, angle, norm, scale, and spatial instantiation |
| DM09 Topological | Continuity, cells, paths, gluings, and coverings |
| DM10 Dynamical | Admissible step, direction, and update |
| DM11 Analytical | Limit, derivative, exponential, and regularity |
| DM12 Spectral | Frequencies and eigenspaces of a specified operator |
| DM13 Measure and Probability | Weight, distribution, mixture, and correlation |
| DM14 Information and Recovery | Preimage, sufficiency, code, and error |
| DM15 Computation and Memory | Word of actions, program, trace, and access |
| DM16 Representations and Reconciliation | Maps, addresses, joint transfer, and unfolding |
| DM17 Subject Meaning and Language | Role, naming, question, and scene participant |

The second index preserves R1–R12: distinction and equivalence; order; incidence; algebra; linearity; affinity and convexity; projectivity; metric and quadratic forms; topology and fibrations; transfer; measure; product and joint consistency.

The atlas itself is a structural whole with 17 subject headings, 12 headings of laws, and addresses of instantiations. Its elements are not independent bits. The completeness and absolute minimality of these lists are not proven. Appendix A preserves the detailed correspondence; arithmetical, phase, and quantum instantiations are unfolded in Appendices C–E.

Verification question: does the named domain possess its own carrier and law, or merely a slot in a list?

<a id="tnr-P40"></a><a id="tnr-П40"></a>
## 5.5 An Expression and Its Numerical Reading

Domains DM02 and DM06. Projection — an expression tree is read as a numerical value. Grounds: P36, P05, P06.

Here 0 and 1 are ordinary numerical values of the respective operations. The structural unit \(i_{\mathrm{str}}[E]\) remains the name of unfolded content; the complex unit $i$ will be introduced by a separate law in the next chapter.

**Definition.** An expression is constructed from named arguments and operations with declared input arities and domains. Parentheses preserve the composition tree. A numerical reading evaluates the value of this tree.

The identity map, NOT, inversion, and factorial are unary. Addition, multiplication, and binary logic connectives are binary. Exponentiation employs a base and an exponent; its domain depends on the numerical carrier. Subtraction requires admissible differences; division requires a non-zero denominator and an accepted quotient law.

The expressions \(2+2\), \(2\cdot2\), and \(2^2\) share the same value 4, but involve different operations. From the bare answer 4, the tree cannot be recovered. Equality of numerical results is not an invertible folding of expressions. Folding requires a preserved record with an unfolding address.

Even familiar inverse pairs possess domains: \(x\mapsto x+a\) and \(x\mapsto x-a\) are inverse on a suitable numerical carrier; \(x\mapsto x^2\) without sign restriction lacks a unique inverse function. The factorial counts permutations of $n$ distinguishable positions; it is not a general inverse operation of exponentiation.

Verification question: is the value of the expression protected, or also its arguments, parentheses, and executed order?

<a id="tnr-P41"></a><a id="tnr-П41"></a>
## 5.6 Additive Partitions and Divisors

Domains DM02 and DM03. Projection — two distinct devices are read as scalars. Grounds: P40, P27.

For four ordered units, there are three positions for potential boundaries. The boundary mask receives three free bits and eight instantiations: from \((4)\) to \((1,1,1,1)\). A part of length $k$ unfolds into $k$ units with order preserved. Complementing the mask changes partition and gluing; it does not automatically alter the values of the units.

A different cube emerges from the divisors of \(30=2\cdot3\cdot5\). Given the prime factorisation, an address \((a,b,c)\in\{0,1\}^3\) signifies \(d=2^a3^b5^c\). An edge alters one exponent; the complement \(d\mapsto30/d\) alters all three. Both models contain eight positions, but a boundary between neighbors and a prime factor have different types.

For a known \(N=\prod p_j^{e_j}\), divisors are specified by coordinates \(0\le a_j\le e_j\). The divisibility order is the coordinatewise order, and the number of divisors equals \(\prod(e_j+1)\). When \(e_j=2\), three exponent values appear, yielding a chain of three vertices. A cyclic group of order three does not yet arise from this.

For example,

\[
97155=3^2\cdot5\cdot17\cdot127
\]

has 24 divisors: a 3-element chain for exponent 3 and three binary slots. This is a product of chains, not a 16-state binary cube. Reading the parity of the first exponent merges 0 and 2; the sizes of its preimages are unequal. Reverse assembly requires the full exponent or another sufficient ground.

Verification question: have states, path orders, or independent boundaries been counted? The law \(2^n\) and the number \(n!\) answer different questions.

<a id="tnr-P42"></a><a id="tnr-П42"></a>
## 5.7 Three Changes of the Natural Sequence

Domains DM02 and DM03. Projection — a single natural sequence is read by three counters. Grounds: P40, P41.

For an integer \(n\ge1\), define \(a(n)\) as the number of primes \(p\le n\), \(\ell(n)\) as the number of prime powers \(p^k\le n\) with \(k\ge1\), and \(f(n)=n-1\) as the number of positions from 2 to $n$. In this notation, the triple is a structural scalar of coupled accumulations. All its changes originate from a single source $n$.

The increment from \(n-1\) to $n$ is

\[
\begin{cases}
(1,1,1),&n\text{ is prime},\\
(0,1,1),&n=p^k,\ k>1,\\
(0,0,1),&n\text{ has at least two prime directions}.
\end{cases}
\]

These are nested masks \(111,011,001\), read as numbers \(7,3,1\) in the chosen binary order. They encode the event of the counters, not the number $n$ itself. Three admissible masks do not imply three independent bits of the event.

For \(n\ge1\), a multiplicative presentation also appears: \(A_n=\prod_{p\le n}p\), \(L_n=\operatorname{lcm}(1,\ldots,n)\), and \(F_n=n!\). At a prime $p$, all three change; at a prime power of $p$, $L$ and $F$ change; at a mixed composite, only $F$ changes. The exponents of these products preserve more data than the three counters.

The common source and factorisation of $n$ link both representations. The mask itself does not compute an unknown factorisation. Designating a new prime as a "new axis" is possible only after its recognition; this is a structural ordering of the sequence's formation, not a formula for prime distribution.

Verification question: was the event signature computed from an independently obtained classification, or used in place of a primality proof?

<a id="tnr-P43"></a><a id="tnr-П43"></a>
## 5.8 Numerical Carriers and Laws of Algebras

Domains DM02, DM06, and DM07. Projection — value inclusion, dimension, cardinality, and multiplication properties are tracked separately. Grounds: P40, P39.

The chain \(\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\subset\mathbb C\) expands admissible values: counting, additive opposites, fractions, continuous quantities, and complex roots. The algebraic closure of $\mathbb C$ means the existence of roots of non-constant polynomials over it, but does not preclude larger fields. [Definition of algebraic closure](https://stacks.math.columbia.edu/tag/09GP).

The Cayley–Dickson construction operates differently:

\[
\mathbb R\subset\mathbb C\subset\mathbb H\subset\mathbb O.
\]

The real dimensions are 1, 2, 4, 8. Complex multiplication is commutative and associative; quaternion multiplication is associative but non-commutative; octonion multiplication is alternative and non-associative. Further doubling is possible, but no longer preserves the class of normed division algebras over the reals. It is to this class that Hurwitz's limit applies. [Construction and conditions](https://math.ucr.edu/home/baez/octonions/node5.html).

Cardinality answers a third question. $\mathbb N, \mathbb Z, \mathbb Q$ are countable; $\mathbb R, \mathbb C$ have the cardinality of the continuum. Dimension over a chosen field and the cardinality of a set are not interchangeable.

In a chosen octonionic basis, three independent labels distinguish a cube of subalgebras: $\mathbb R$, three complex, three quaternionic, and $\mathbb O$. These are eight full algebras with inclusions. Their active sextet comprises three pairs \((C_a,H_{bc})\), \((C_b,H_{ac})\), \((C_c,H_{ab})\). In each pair, the intersection is $\mathbb R$, and the joint span is $\mathbb O$; these two limits are retained in the background.

Six inclusions form a cycle. Additional links of joint generation of two $C$ and the intersection of two $H$ form two triangles. Jointly we obtain an octahedron with typed edges. This graph does not replace the multiplication table. The full coordinate catalog and bounds are located in Appendix C.

Verification question: does an edge signify inclusion, intersection, generation/span, or an action on an element?

<a id="tnr-P44"></a><a id="tnr-П44"></a>
## 5.9 Candidate Facts and Arithmetical Closure

Domains DM04 and DM15. Projection — accessible grounds and still-admissible partitions of an integer $N$. Grounds: P42, P22–P25.

**Definition.** A protected arithmetical domain contains known facts with their provenance, admissible candidates, questions, and an action library. A candidate satisfies the already known constraints. A fact is obtained by a permitted action or deduced from accessible facts according to a designated rule. An operator that could answer a question is not considered an executed reading.

If known $d$ divide $N$, closure under GCD, LCM, and the complement \(d\mapsto N/d\) constructs a family of accessible divisors. It is not obliged to contain all divisors of $N$. For \(N=45\), the facts 1, 3, 45 yield under these rules 1, 3, 15, 45; the divisor 9 is absent. Saturation \(x\mapsto\gcd(N,x^2)\) is an additional action with a different law.

The accessibility of a ground, the determinacy of a required answer, the admissibility of a command, and its actual execution are verified separately. For 15, the set \(\{1,3,5,15\}\) is already closed under the chosen operations; closure is not identical to a proof of completeness for an arbitrary $N$. Conversely, a closed \(\{1,N\}\) does not in itself prove the completeness of the divisor list or the primality of $N$. These are distinct properties requiring distinct verifications.

A local connection between operations also possesses its own address:

\[
2\cdot3-(2+3)=1.
\]

Here the numerical unit is returned as the difference of two results over the same pair. For arbitrary $a,b$, the difference is \(ab-a-b=(a-1)(b-1)-1\); it is not always unity nor a universal source of primes.

Under state reduction, necessary facts, tolerances, and subsequent questions are preserved. Lattice coordinates under a known factorisation do not provide an unknown factorisation. The residue pair \(xy\equiv N\pmod{2^m}\) is also not obliged to be a finite integer partition of $N$.

Verification question: did the new representation obtain an independent reduction, deduce the prior, or merely rename a candidate?

<a id="tnr-P45"></a><a id="tnr-П45"></a>
## 5.10 Six Roles of the Computational Whole

Domains DM15 and DM16. Projection — a role-based reading of a complete computational device. Grounds: P16, P22, P23, P36, P44.

The record \(\mathfrak F=(N,F,Q,A,H,\Gamma)\) unfolds the current whole $N$, facts $F$, questions $Q$, actions $A$, trace $H$, and frame $\Gamma$. The six slots constitute the structural scalar of this reading, not an assertion of six fields in every implementation or of six free variables.

The chosen three pairs possess substantive connections. **$N$/$\Gamma$:** the subject is placed within the domain of admissible consideration. **$F$/$H$:** a fact receives evidence of provenance from the instantiated trace. **$A$/$Q$:** an action transfers state; a question is transferred in a counter-manner. The reverse traversal $F\to H$ does not return a unique complete history; it accesses the preserved origin of the fact.

The common third must not be concealed in a diagram. It is a single admissible event, its origin address, a substantiated answer, and a preserved right of continuation. It is this that unites the forward flow of action and the counter-flow of question. If a question is given as \(h\circ m\), its projecting $\Gamma, B, m, h$ remain in the record even after transfer \(h\circ m\circ T\).

These connections can be arranged on three geometric axes after choosing an framing. The arrangement is a conjugation scheme; $N$ and $\Gamma$ do not turn into interchangeable data. The geometric symmetry of an octahedron does not permit arbitrary permutation of facts, questions, and trace.

The sextet folds into \(i_{\mathrm{str},\Pi}[\mathfrak F]\) if the vocabulary unfolds the roles and the addresses of their interface. The upper mark of a name adds no independent bit. In the next chapter we investigate separately when a paired law truly receives a complex instantiation.

In executable self-application, these roles are distributed among state, methods, policy, and ledger, rather than necessarily assembled in a single six-field record. A single verified executor can open two address-distinct child branches according to an authorized cut, preserving parent and ground. However, the general computable transfer of an arbitrary question \(q\circ T\) requires a separate rule; it does not arise from the mere presence of these fields. Subject elevation of the entire ledger preserves its unfolding and right of continuation, but assigns no new rank by the count of its constituents.

Verification question: how does each pair act on a single event, and what connects both sides beyond adjacency in a diagram?

<a id="v1-chapter-6"></a>

# Chapter 6 Phase and Continuation

A pair of hidden states does not yet specify an imaginary unit. One requires an action law connecting its two presentations. Here we construct and reconcile finite, linear, and continuous representations of such a law. Path memory and the sufficiency of a reduced reading will verify the admissibility of continuation. We then return to the arithmetic tower, where a single new bit also proves to be a sign of lifting, yet possesses its own distinct group law.

The locus of description in this chapter changes explicitly: first finite tables, then the real linear plane, the complex carrier, and path topology. The numbers 1, −1, and $i$ in complex formulas carry their ordinary numerical meaning. The structural unit \(i_{\mathrm{str}}[E]\) designates an unfoldable whole and is not substituted in place of these numbers.

<a id="tnr-P46"></a><a id="tnr-П46"></a>
## 6.1 One Visible Exchange and Two Complete Laws

Domains DM06 and DM10. Projection — two binary slots \((v,s)\) are read solely by $v$. Grounds: P11, P10.

Consider two permutations of four states:

\[
U(v,s)=(v\oplus1,s),\qquad
V(v,s)=(v\oplus1,s\oplus v).
\]

The visible answer $v$ flips to the opposite value each time. However,

\[
U^2=I,\qquad V^2(v,s)=(v,s\oplus1),\qquad V^4=I.
\]

After two steps, $U$ returns the full state, whereas $V$ returns only the answer $v$. The hidden $s$ has changed. The structural scalar four here counts states of two independent positions; the law $V$ forms a cycle of order four, while the law $U$ forms two disjoint exchanges. They are not determined by the number of states alone.

Inverse actions exist: \(U^{-1}=U\), \(V^{-1}=V^3\). The counter-question \(q\circ V\) is defined by the same event, even if only $v$ is read. If recovering the complete state after two steps is protected, the compressed $v$ is insufficient: $s$ is required, or sufficient addressed memory of its change.

Nor does a square graph select an algebra. Cyclic steps $\pm1$ on $C_4$ and two independent switches on $C_2^2$ yield the same square graph. The first law contains an element of order four; in the second, all non-identity elements have order two.

Here the prior reduction criterion P19–P20 in DM14 applies. If a free involution $\tau$ on $E$ has orbits \(\{e,\tau e\}\), and $\pi$ reads these pairs, the protected reading $f$ is expressed through $\pi$ precisely when \(f(\tau e)=f(e)\). A partial action \(T:D\to E\) descends together with admissibility precisely when \(\tau(D)=D\) and \(\pi(T\tau e)=\pi(Te)\) on $D$ [Th]. The lower answer preserves the unlabeled pair; a labeled participant and necessary history require separate protection. In the present example, \(\tau(v,s)=(v,s\oplus1)=V^2(v,s)\), and \(\pi(v,s)=v\). The number two counts participants of a single answer, not real dimension. The proof and distinction between types of continuation are unfolded in D1 and D4.

Verification question: did an answer, a full participant, an operator, or the entire instantiated history return?

<a id="tnr-P47"></a><a id="tnr-П47"></a>
## 6.2 Linear Instantiation of the Imaginary Unit

Domains DM06 and DM07. Projection — a finite cycle is placed on the real plane with a chosen basis. Grounds: P46, P30, P43.

**Definition.** A complex structure on a real space is a linear operator $J$ satisfying \(J^2=-I\). On the plane we choose

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The coordinate pair \((a,b)\) is read as \(z=a+ib\), and the action of $J$ as multiplication by the complex unit $i$. Now the imaginary unit possesses its own law, rather than merely a central position in a diagram.

The connection to the prior four states is given by the map

\[
z(v,s)=(-1)^s i^v.
\]

It is invertible between the four addresses and \(\{1,i,-1,-i\}\), with \(z(V(v,s))=i z(v,s)\). The end-to-end finite whole has not vanished: its law has become the restriction of the linear action to four named points.

A quarter-turn is $J$, a half-turn is $-I$, three-quarters is $-J$, and a full turn is $I$. The choice of orientation distinguishes $J$ and $-J$. Under the standard Euclidean metric, $J$ is orthogonal; this is a metric framing of the named plane, not a deduction from the bare order four.

The real dimension equals two. The finite four addresses have binary rank two; the entire plane is not a finite four-slot carrier. Its zero vector is fixed under $J$, but does not belong to the four chosen non-zero points.

On a single equipped oriented Euclidean plane, one can reconcile a quarter-turn $J$ with a six-beat rotation $R$. If $G$ is a rotation by \(\pi/6\), then \(J=G^3\), \(R=G^2\), \(J^2=R^3=G^6=-I\), and \(J^4=R^6=G^{12}=I\). A shared finite cycle $C_{12}$ emerges, rather than twelve independent distinctions. The chosen directions of Lab and HSL admit this common mathematical framework; conjugation of their real color transformations is not thereby proven. The conditions are unfolded in D1 and E7.

Verification question: is an operator with square $-I$ presented on the declared sector?

<a id="tnr-P48"></a><a id="tnr-П48"></a>
## 6.3 The Exponential and Counter-Phases

Domains DM11 and DM10. Projection — continuous continuation of the linear action $J$. Grounds: P47, P14.

The matrix exponential defines

\[
R_\theta=e^{\theta J}=\cos\theta\,I+\sin\theta\,J,
\qquad R_{\theta+\phi}=R_\theta R_\phi.
\]

This identity is obtained by separating even and odd terms of the power series with \(J^2=-I\). Thus Euler's formula continues the already chosen law. The exponential and the real parameter are analytical instruments of this instantiation.

A reconciled pair of directions takes the form \(R_\theta, R_{-\theta}\); they are mutually inverse. The state evolves to \(R_\theta z\), while the question toward this result evolves to \(q\circ R_\theta\). Their third structure remains that same original $z$, the chosen question, and the instantiated parameter. Inverting the action and counter-transferring the question belong to different types even here.

For \(\theta=0,\pi/2,\pi,3\pi/2,2\pi\), one obtains \(I,J,-I,-J,I\). For a non-zero participant, the period of complete return is \(2\pi\). A reading that identifies $z$ and $-z$ returns already after a half-turn.

A single $R_\theta$ stores $\theta$ only modulo \(2\pi\). The traversal history may additionally store the sign of direction and the winding number. A zero parameter, a zero vector, and a zero winding number are three different subjects. The structural unit of this family must unfold the law and chosen parameter, and when protecting the path, its trace as well.

Verification question: what angle and whose return does the record protect?

<a id="tnr-P49"></a><a id="tnr-П49"></a>
## 6.4 The Square Answer and the Sign of the Lifted Path

Domains DM09 and DM14. Projection — a non-zero complex participant is read by its square. Grounds: P48, P20.

Let \(q:\mathbb C^*\to\mathbb C^*\), \(q(z)=z^2\), where \(\mathbb C^*=\mathbb C\setminus\{0\}\). The preimage of each answer is a pair \(\{z,-z\}\). It constitutes an intact two-sheeted relation; a single answer value does not select a labeled sheet.

A continuous answer path and a chosen initial root specify a unique continuous continuation of the root. For example,

\[
w(t)=e^{it},\qquad z(t)=e^{it/2},\qquad 0\le t\le2\pi.
\]

The answer makes one full turn and returns to 1, while the participant traverses from 1 to $-1$. After two turns of the answer (that is, $t=4\pi$), the participant returns. The numbers \(2\pi,4\pi\) here refer to the answer angle $t$; the participant's angle is $t/2$.

If the action \(z\mapsto iz\) is permitted, on the squared answer it takes the form \(w\mapsto-w\). For the shift \(z\mapsto z+2\), no such map from the bare square exists: $z=1$ and $z=-1$ share the same prior answer, but have new squares 9 and 1. Their tolerances coincide, but the protected results differ.

Zero is excluded not for notational convenience. At zero the two roots coincide; there the map is not a two-sheeted covering. The pair of roots, the labeled root, and the history of its continuation receive separate addresses and recovery conditions.

Verification question: are the initial sheet and the answer path retained, or only the terminal square?

<a id="tnr-P50"></a><a id="tnr-П50"></a>
## 6.5 Full Radial-Phase Representation

Domains DM11 and DM16. Projection — a non-zero complex representative is redescribed without loss. Grounds: P48, P36, P38.

For \(B\in\mathbb C^*\), define

\[
P(B)=B,\qquad
L(B)=(\log|B|,B/|B|).
\]

The map $L$ is invertible: \((r,\zeta)\mapsto e^r\zeta\), where \(r\in\mathbb R\), \(\zeta\in S^1\). The pair of radius and phase is connected by this assembly law. Locally it has two real parameters, but globally the phase coordinate remains a point on the circle, not a chosen real argument.

Thus $P$ and $L$ are two complete presentations of a single whole. The forward traversal unfolds the representative into scale and phase; the reverse assembly recovers it. The counter-question to the record $L$ takes the form \(q\circ L\) and is not this assembly. Their common source $B$ and constant domain \(\mathbb C^*\) are retained in the passport. At $B=0$, the record $L$ is undefined.

One may choose an argument on a domain with a branch cut. Then the domain conditions become part of $\Gamma$, and crossing the cut requires matching branches. A detached record of a number $\theta$ without this domain is not a global full redescription of $S^1$.

Verification question: is the phase held by a circle point or by a real parameter with a declared branch rule?

<a id="tnr-P51"></a><a id="tnr-П51"></a>
## 6.6 Five Operations and Three Levels of Sufficiency

Domains DM08 and DM14. Projection — five maps on a single domain \(\mathbb C^*\). Grounds: P50, P49.

Fix a known non-zero normalisation $\eta$. In addition to $P$ and $L$, define

\[
X(B)=\{B,-B\},\qquad
A(B)=B^2/\eta,\qquad
H(B)=|B|^2.
\]

The structural scalar five counts the operations of these maps and their relations. $P$ and $L$ return the representative; $X$ and $A$ return the sign-equivalence class; $H$ preserves only the squared radius. On the full domain, three levels of sufficiency emerge:

\[
P\simeq L,\qquad X\simeq A,\qquad H.
\]

Equivalence of $X$ and $A$ signifies equality of their preimages under known $\eta$, rather than identical answer types. From $A$ we obtain the root pair $\pm\sqrt{\eta A}$. From $H$ we obtain an entire circle of compatible $B$. Under shared normalisation, \(H=|\eta|\,|A|\); equality \(H=|A|\) requires \(|\eta|=1\).

The sign quotient preserves radius. Full complex projectivisation of a one-dimensional complex space would identify all non-zero representatives, and is therefore a different operation. Restricting $B$ to the positive real ray eliminates sign and phase, making $H$ sufficient for $B$ on that domain. It alters the problem, rather than restoring what was lost on the original domain.

Preserving the class $X$ does not license arbitrary continuation. Even the shift by 2 from the preceding section does not descend through $X$ or $A$. The family of permitted actions remains part of the sufficiency level.

Verification question: are preimages compared on the same domain and under the same normalisation?

<a id="tnr-P52"></a><a id="tnr-П52"></a>
## 6.7 Local Unfolding and Global Gluing

Domain DM09. Projection — covering and path continuation. Grounds: P48, P49, P22, P23.

On a small arc of a circle, a root can be chosen continuously. On the entire circle, no such choice is possible: a traversal from the previous example returns the opposite root. Local unfoldings are linked by $\pm1$ transitions on overlaps. To glue a path, one must retain not only the current answer, but also the transition law between its local presentations.

A related example is provided by the Möbius strip:

\[
M=([0,2\pi]\times[-1,1])/((0,t)\sim(2\pi,-t)).
\]

The projection onto \(\theta\bmod2\pi\) has an interval as transverse content. Choose parallel transport with constant $t$ in the rectangular strip before gluing. One traversal of the base under this transport reverses the sign of the retained transverse coordinate $t$. An arbitrary path in the strip is not required to preserve this coordinate; the transport law is an additional framing. Two disconnected strips possess no such gluing rule. Discrete exchange of sheets, reversing base direction, and motion along the base are different actions.

The covering of the square map and the Möbius strip are likewise not a single carrier: in the former, the preimage consists of two points; in the latter, of an interval. What coincides is the verifiable motif of return with side reversal. Transition between models requires declaring precisely which operation is transferred.

The structural whole of a gluing contains domains, overlap maps, their reconciliation law, and the initial reference of the path. Its topological type is not deduced from the number of poles or the label "two flows." Appendix D preserves additional proof references.

Verification question: is a gluing rule specified, or merely several identically labeled local diagrams?

<a id="tnr-P53"></a><a id="tnr-П53"></a>
## 6.8 Surfaces and Spectral Questions

Domains DM09 and DM12. Projection — special structures on already constructed relations. Grounds: P52, P39.

The torus $S^1\times S^1$ retains two independent circular coordinates. The real projective plane \(S^2/(x\sim-x)\) retains an unoriented axis in place of a labeled direction. Their preimages and continuation laws differ. The shared language of the whole requires naming precisely these maps.

The Hopf map provides another exact example. On \(S^3=\{(z_1,z_2):|z_1|^2+|z_2|^2=1\}\), define

\[
h(z_1,z_2)=
(2\operatorname{Re}(z_1\overline z_2),
2\operatorname{Im}(z_1\overline z_2),
|z_1|^2-|z_2|^2)\in S^2.
\]

A common phase \((z_1,z_2)\mapsto e^{i\theta}(z_1,z_2)\) does not alter the answer. Its preimage is a circle of shared phase. This is not the sign pair of the quadratic reading: the composition of the hidden is different here. Normalisation, complex coordinates, and circle action belong to the passport of this instantiation.

A spectral reading requires a concrete operator. For example, for the cyclic shift $P$ on words of length $r$, complex characters diagonalize $P$. On the same address set, independent XOR switches have a different set of characters and a different composition law. A bare list of eigenvalues does not recover the matrix, its named basis, and its framing.

Topology and spectrum here become participants in cross-domain comparison. Their complete examinations belong to the proof appendices and Volume II. They are not declared additional primitive inputs based solely on a resemblance of shape.

Verification question: which map and which operator connect the new instantiation with the prior whole?

<a id="tnr-P54"></a><a id="tnr-П54"></a>
## 6.9 Vertical Phase Lift of Factors

Domains DM02, DM06, and DM12. Projection — refinement of a modular factor pair over a fixed base node. Grounds: P48, P42, P44.

For an odd $N$, define

\[
\mathcal F_n(N)=\{(x,y)\in((\mathbb Z/2^n)^\times)^2:
xy\equiv N\pmod{2^n}\}.
\]

A unit $u$ acts in pairs: \(u\cdot(x,y)=(ux,u^{-1}y)\). The product and membership in a single whole are preserved. The set of pairs is a torsor: the transition between any two pairs is unique, but an internal group identity requires choosing a basepoint.

**Theorem.** For \(m\ge2\), \(h\ge1\), the preimage of a fixed pair under the reduction \(\mathcal F_{m+h}(N)\to\mathcal F_m(N)\) is a torsor of the cyclic group

\[
K_{m,h}=\langle1+2^m\rangle\cong C_{2^h}.
\]

The proof is given in Appendix D. Here $m$ is the modulus exponent, and $h$ is the additional precision. They are not numbers of semantic windows. The entire fiber \(\mathcal F_n(N)\) for \(n\ge3\) possesses the torsor law \(C_2\times C_{2^{n-2}}\), not a single cycle.

Choose reconciled basepoints \(f_h^0\) and a generator $g$. Then \(f_h(t)=g^t f_h^0\) receives the phase address \(z_h=e^{2\pi it/2^h}\). On adjacent levels,

\[
z_{h+1}^2=z_h,\qquad z_{h+1}=\pm\sqrt{z_h}.
\]

The new free choice is the sign of the root following this calibration. State reduction coarsens $t$; the counter-transfer of the lower character doubles its frequency. These two operations are reconciled by a single base node, but possess different directions and element types.

For \(m=1, h=2\), the kernel is $C_2^2$, not $C_4$. Horizontal $h$ independent features generally possess the group $C_2^h$; for \(h\ge2\), this is not isomorphic to the vertical $C_{2^h}$. Coincidence of size $2^h$ does not transfer group, graph, or Fourier transform.

The phase address of a presented candidate is computable from that candidate and the basepoint. It does not select an unknown valid integer factor. A local modular pair may continue without becoming a finite positive partition of $N$. Obtaining independent information to choose a branch remains a separate computational problem.

Verification question: has a base node been specified, basepoints reconciled, and the condition $m\ge2$ verified before declaring a cyclic law? Finite test code: color bridge, geometric atlas, golden coordinates, phase inclusion.

The next chapter applies these distinctions to composite computation. There, the prior whole becomes an input to a new relation, together with its source, trace, and right of continuation.

<a id="v1-chapter-7"></a>

# Chapter 7 Composite Action and Return to the Scene

The constructed instruments for reconciling representations are now applied to computation and to the formulation of the theory itself. A prior whole becomes a participant in a subsequent relation; its content, provenance, and conditions of further employment do not vanish. Memory and sufficiency verify the integrity of these transitions rather than substituting for their subject matter.

The locus of description in this chapter is the framework of composite processes. The arithmetic example pertains to DM02, DM04, DM14, and DM15; addressed reconciliation pertains to DM16. The numbers within it are arithmetic values. The structural unit \(i_{\mathrm{str},a}[E]\) continues to signify a folded device with accessible unfolding. The number of fields in a program does not in itself determine binary rank.

<a id="tnr-P55"></a><a id="tnr-П55"></a>
## 7.1 A Tree of Unfoldable Wholes

Chapter 3 already introduced assembly with a shared witness, and Chapter 5 the divisor relation. Now individual wholes become participants in a tree. The root task retains the question, admissible actions, and overall frame. A partition (cut) creates two child tasks, each with its own side address.

In the arithmetic presentation, the partition \(N=AB\) preserves the product. However, the equality \(25=5\cdot5\) does not make two child occurrences into a single participant. The left and right positions possess identical numerical content, but distinct relations to the parent. Merging their addresses destroys multiplicity and fails to unfold the original tree.

Such a tree is a structural whole not because it is enumerated in a single record. It is bound by parental relations, named sides, and a recovery law. The paired presentation is partition and assembly; the shared third structure is the source node with the actual ground of the cut. A new node can be folded into $i_{\mathrm{str}}$ only while preserving these connections.

The complete product of the leaves reconstructs the original number when each leaf is retained with its multiplicity. An unfinished leaf also belongs to the result. Halting under budget exhaustion does not transform it into a proven prime factor, nor does it remove it from the whole.

The level of description here is higher than the individual child tasks: their joint device has become the subject. A new freedom of binary choice does not yet follow from this. The number of leaves, tree depth, degree of unfolding, and history length are distinct readings of the tree.

In a verified execution, an authorized cut opens two address-distinct child tasks concurrently. If resources suffice for only one side, the transition is not executed: parent and ground remain preserved, and neither child task is declared created. Thus the complete elevation of the tree is defined by a transition law, rather than by adding a nameless binary digit.

The numerical compression \(3\cdot3\cdot3\cdot3\to3^4\) retains the base and multiplicity. It does not abolish the four addresses of sides, events, and histories. The power reading of a verified ledger unfolds them by a shared address; an action upon an individual participant still requires its own distinct locus. Prior to primality events for all participants, this is a group of parts rather than an authenticated prime factorisation.

Short verification: can both sides, their parent, and not-yet-executed work be recovered from the final record? If only the product of numbers returns, a numerical reading is preserved, but not necessarily the computation tree.

<a id="tnr-P56"></a><a id="tnr-П56"></a>
## 7.2 Choice as an Executable Act

The role of accessing questions does not choose the next question on its own. For this, a distinct law over admissible actions is required. We transition from the projection of an individual execution to the projection of decision: which actions are currently presented, why one of them is admissible, and on what ground it was chosen.

For a concrete choice, the question, presented menu, admission conditions, ground of preference, chosen action, and its actual execution are preserved. These roles are bound together: the question defines the required operation; admission restricts the menu; the ground compares the remaining variants; execution produces an event and expenditure. This is the structural composition of a choice, not six independent coordinates.

One may present two different menus, in each of which the same action is chosen. The routes after the choice will coincide, but the prior possibilities differed. If a future verification concerns whether an alternative was accessible, the mere name of the executed command is insufficient.

A verification question for a choice belongs to the decision domain. For example: "by what accessible ground is this partition authorized?" It is not equal to an inverse arithmetic operation and is not in itself a counter-transfer. For the latter, a definite action $T$, a question to its output $q$, and a rule \(q\circ T\) are required. The initial domain of choice verification consists of preserved facts and current menu conditions, rather than the not-yet-obtained result of a future trial.

Admissibility does not prove optimality. One may specify a correct policy that is more costly than another correct policy. A choice based on a precomputed unknown answer is not an investigable method of obtaining that answer: it has already employed the objective as a concealed premise.

Short verification: does the record of choice return its genuine menu and ground, or merely a justification invented after the result?

<a id="tnr-P57"></a><a id="tnr-П57"></a>
## 7.3 A Paid Source in a Child Task

Consider a concrete route for \(N=45\). The original whole includes the number, already obtained facts, posed questions, and action history. The route is verified within the frame of this execution: a command must possess an accessible ground, and its result must retain address and provenance. Possible generalisations to recursive trees are distinguished from assertions concerning this specific case.

For \(N=45\), a paid trial with operand \(r=3\) yields

\[
d=\gcd(45,3)=3.
\]

A number, initial stage, and event address are obtained. The subsequent question may require the full block of multiplicities for already discovered prime directions. Then saturation is performed:

\[
x_0=d,\qquad x_{k+1}=\gcd(N,x_k^2).
\]

Here 3 transitions to 9, then remains 9. The raw trial answer is 3, while the saturated block is 9. They do not replace one another: the first answers the prior question, whereas the second organizes a new partition.

For \(N=\prod p^{e_p}\), the saturation law unfolds as

\[
v_p(x_k)=\min(e_p,2^k v_p(d)).
\]

Non-zero valuations attain the bounds of $N$; zero valuations remain zero. This analysis proves the law, but the program does not obtain an unknown factorisation of $N$: it executes squarings and GCDs.

Ordinary closure under GCD, LCM, and complementation does not automatically include saturation. For example, from \(1,3,45\) those operations produce \(1,3,15,45\), but not 9. Different action libraries produce different closures.

The saturated block permits the partition

\[
45=9\cdot5.
\]

The two child readings of the same source are

\[
d_A=\gcd(9,3)=3,\qquad d_B=\gcd(5,3)=1.
\]

Distinct side addresses, a single source operand, and a single trial event are preserved. The new cut does not create two independently paid trials.

To observe the counter-flow, define the source record as \(s=(N,r,d,\text{stage},\text{event})\), where \(d=\gcd(N,r)\). For a fixed positive \(A\mid N\), the transfer $T_A$ returns the child record \((A,r,\gcd(A,d),\text{source address},\text{side})\); the stage is preserved to verify the completeness of the source question. This construction utilizes the paid $d$, rather than a new precomputed trial. The reading $m_A$ on the child carrier returns the obtained GCD; the source domain of its numerical answer consists of divisors of $A$. The question rule here returns this value. On the parent, the same question is expressed by the law

\[
\gcd(A,\gcd(N,r))=\gcd(A,r),\qquad A\mid N.
\]

Thus the task transfers to the child, while its question returns to the source origin. The question structure, stage, and chosen side are preserved. This is an arithmetic instantiation of the general law \(q(Ts)=(q\circ T)(s)\), rather than invertibility of the cut.

On the raw cut \(45=3\cdot15\), the same source would yield child answers 3 and 3. Their stage completeness differs from that on the cut \(9\cdot5\). Therefore further admission is recomputed for the current whole under the preserved initial stage; it is not copied from an alien intermediate feature.

Direct transfer of a question to a child task is admissible if the parent's question was indeed posed before the partition and its answer pertains to the same source. Arithmetic equality alone is insufficient: answer address and execution stage are verified separately. Transfer across multiple cuts requires re-specifying source and conditions at each transition; tree depth does not by itself substantiate such a chain.

Short verification: should assembly return the original 3 or the new block 9? The correct answer depends on the preserved question; in this chain, the original 3 is restored.

<a id="tnr-P58"></a><a id="tnr-П58"></a>
## 7.4 Assembly Correction and the Full Route

Child answers are not sufficient under every partition. We transition to the projection of recovering the prior scalar answer, preserving the source operand and total multiplicity.

Let \(N=AB\), \(d_A=\gcd(A,r)\), and \(d_B=\gcd(B,r)\). Then

\[
D=\operatorname{lcm}(d_A,d_B),\qquad
C=\gcd\!\left(\frac ND,\frac rD\right),
\qquad
\gcd(N,r)=DC.
\]

The divisions are exact: $D$ divides both $N$ and $r$. The formula holds also for $r=0$. This is a general law of arithmetic recovery, not the acquisition of an unknown trial without a source operand.

For the proof, consider the valuation of a single prime. If the exponents in \(A,B,r\) are \(a,b,t\), the exponent of $D$ is \(\delta=\min(\max(a,b),t)\). In $C$ there remains \(\min(a+b-\delta,t-\delta)\); the sum equals \(\min(a+b,t)\), which is the exponent of \(\gcd(N,r)\). For $r=0$, directly \(D=\operatorname{lcm}(A,B)\), \(C=N/D\), and the result is $N$.

On the partition \(25=5\cdot5\), the source operands 20 and 0 yield identical child readings 5 and 5. However, the parental answers are 5 and 25. In the first case, \(D=5, C=1\); in the second, \(D=5, C=5\). A bare LCM loses shared multiplicity; a simple product errs in the first case.

When $A$ and $B$ are coprime, the correction is always the numerical unit, and the parental answer equals \(d_A d_B\). Proper saturation yields precisely such a partition. Hence the type of partition predicts the law of any future scalar GCD, but not its unknown value.

If saturation reaches all of $N$, no proper partition yet exists. For example, \(d=15\) on 45 saturates to 45, and \(d=3\) on 9 to 9. This is not a proof of primality. Incomplete support of the detected divisor was a necessary condition for a proper saturated partition.

In a specified tariff, the overall upper assembly is counted as an independent action costing seven arithmetic operations: two GCDs, three divisions, and two multiplications. Verification prior to execution establishes sources, sides, stage, and reserve, but does not compute the unknown future correction to choose a route. This is the cost of the chosen implementation, rather than a universal bound on all assembly methods.

A separate reread mode returns the already stored parental answer. It is not a new reconstruction from two reduced child inputs. The absence of a new GCD does not make memory, addressing, and access-right verification costless.

The full route verifies the source event, membership in a paid whole, two distinct child occurrences, and the overall frame. A numerically true answer originating from an alien event fails this verification.

Cost is composed of lower operation and upper recovery; tariff, execution time, and allocated memory are different readings of cost. After upper assembly, the lower process cannot be continued under the prior limit without renegotiating the frame. In the model under consideration, the new local limit is specified by the sum of already consumed local resource and the accessible shared remainder. The sequence of frame and action changes is verified, not merely the terminal limit.

Under recursive partitioning, the number law \(N=\prod_i A_i\) does not become a product law for GCD answers. On four parts 3 of the number 81, the shared operand 3 yields four answers 3; their product 81 is not equal to the parental answer 3. After discarding the operand, a reduced reading may conceal a missing power, even though the full prior answer remains in history. The exact multileaved law and power reading are provided in Appendix F. Their availability as mathematical readings does not mean each is already implemented as an authorized command.

Short verification: was the answer returned from a preserved source or reconstructed anew from child data? Both routes can be valid, but their grounds and cost differ.

There is also a positive case of complete assembly without correction [Th]. Choose windows \(m_i\mid N\) with \(\operatorname{lcm}_i m_i=N\). Known local answers \(d_i\mid m_i\) glue to a unique \(d=\operatorname{lcm}_i d_i\) if and only if their restrictions to each shared window \(\gcd(m_i,m_j)\) coincide:

\[
\gcd(d_i,\gcd(m_i,m_j))=\gcd(d_j,\gcd(m_i,m_j)).
\]

Then \(\gcd(d,m_i)=d_i\). For each prime, some window contains the full multiplicity of $N$, and its local exponent determines the overall maximum and all restrictions. This proof does not supply unknown local answers: they must be obtained by authorized actions. Under an incomplete cover, multiple global divisors may remain. The full law and reverse-side size are in §§15–16; see the new finite verification of composition and gluing.

<a id="tnr-P59"></a><a id="tnr-П59"></a>
## 7.5 Definition as an Autonomous Act

Now the introduction of a concept itself becomes the subject. This is not the first application of the method: definitions in previous chapters already possessed grounds, projection, device, and unfolding. Here the same order is considered at the methodological level of description.

A definition gathers accessible content into a new name. The reverse verification of unfolding asks what prior relation this name returns. To designate it a counter-transfer is legitimate only after specifying the introduction map and a question to its result: then composition returns precisely that question to the grounds. The shared third structure is an addressed correspondence between grounds, introduction, and verifiable result. If a name unfolds only into another unexplained name, a sound introduction is not achieved.

In the role-based reading, six slots are used: presented whole $N$, accessible grounds $F$, protected question $Q$, admissible construction $A$, witness $H$, and frame $\Gamma$. Their connections are more important than their count. The frame permits utilizing the grounds; the construction answers the question; the witness links the obtained object to that same source whole.

The chosen presentation \(N/\Gamma,\ F/H,\ Q/A\) retains three conjugate pairs. It does not permit arbitrarily swapping semantic fields. To make this sextet into a geometric octahedron requires separate maps and equipment; the role scalar six does not replace them.

The definition's own address indicates not only its name and position in the book, but also carrier, domain, projection, state of accessible grounds, and the level from which it is described. The number Pxx is a textual address. Color or a binary word appears only after choosing the corresponding map.

The prior whole becomes an object of higher level while preserving unfolding. An equals sign, an additional pair of parentheses, or a new title do not by themselves prove a new independent bit. The numerical unit, structural \(i_{\mathrm{str}}\), and complex $i$ possess distinct addresses and laws.

Short verification: from which projection is the definition itself written, what remains in its reverse side, and is that reverse-side ground accessible?

<a id="tnr-P60"></a><a id="tnr-П60"></a>
## 7.6 Independent Subject Testings

Another subject domain can confirm a transferred law, reveal an omitted condition, or produce a rejection. Comparison is conducted through reconciled actions rather than visual resemblance of figures.

The algebraic example provides the first boundary: an identical graph of subalgebra inclusions does not recover multiplication. A geometric presentation must preserve action properties or honestly name their forgetting. Similarly, a single square graph admits different composition laws for its steps.

The quantum test separates binary addresses of the computational basis, six stabilizer directions of a single qubit, and finite operator geometries. These are distinct carriers. Linking them under a single interface requires maps, a probabilistic law, and measurement conditions. The central extension class is compared after transfer to a shared named base; coincidence on a subgroup does not become global equality.

The linguistic test exhibits an equally concrete failure: if two sounds occupy a single table cell, yet a grammatical rule treats them differently, the table is insufficient. A new cell name or a more symmetrical diagram does not recover the required distinction. One must refine the cell's contents relative to that rule.

The color test compares reversible coordinate representations, finite frameworks, and reduced readings. It shows that an identical set of six references does not determine a metric or action, and that two models sharing a lightness role do not necessarily pose the same question. Under RGB$\to$Lab, the rule \([L^*>50]\) returns as composition with the declared transformation map and is not replaced by the rule \([L_{\mathrm{HSL}}>1/2]\). The details of this example are presented in Appendix E.

The algebraic test is unfolded in Chapter 5 and Appendix C; the quantum, linguistic, and color tests in Appendix E. They do not constitute a fourth "universal triple" atop the beginning. Each retains subject meaning, an external source, and its own domain of action.

Short verification: has the law of admissibility and result been transferred, or has only an identical diagram been found so far?

<a id="tnr-P61"></a><a id="tnr-П61"></a>
## 7.7 Return to the Active Scene

The culmination is not another list of concepts, but the original scene with accessible unfolding. We return to the source $S$ of four states and the chosen family $W$ of eight affine questions. Constant questions are denoted \(0_W, u\); the active sextet is \(A_6=W\setminus\{0_W,u\}\).

Fix \(q_*=\beta\). The five remaining active questions form $V_5$, while all non-zero questions form $L_7$. Then

\[
V_5\sqcup\{q_*\}=A_6,\qquad L_7\setminus\{u\}=A_6.
\]

The first map gathers the chosen question with alternatives. The second presents the active part of the Fano law, holding $u$ in the background. The common source, choice, and consistency must coincide. From an unlabeled sextet alone, one cannot recover which question was chosen.

These two assemblies of the scene do not yet execute an act. Therefore, take the real action \(T(x,c)=(x\oplus c,c)\) and the future question \(q_1=\beta\). Its initial device remains \(q_1=h_1\circ m_{\beta,1}\), where \(h_1(b)=b\). The counter-transfer is

\[
q_0=T^*q_1=h_1\circ m_{\beta,1}\circ T=x.
\]

On the actual initial state \((x,c)=(0,1)\), the forward step yields \((1,1)\). The future answer is 0, and the counter-question $x$ on the initial state also yields 0. Both pertain to the same event. The initial rule was still specified on the future domain $\beta$, rather than the current $x$.

The current \(\beta=1\) does not by itself allow one to obtain this answer in advance: another initial state \((1,0)\) yields the same \(\beta=1\), but a counter-answer \(x=1\). The joint reading \((\beta,c)\) expresses it as \(x=\beta\oplus c\). The shift in projection required a concrete additional distinction.

For this invertible $T$, the quintet without future $\beta$ transfers to the quintet without current $x$, while the septet transfers with $u$ retained. The two presentations converge again in the source active sextet. The source $S$, environment $W$, both question addresses, and the event are not lost.

Thus the exposition unfolded several reconciled representations of the chosen environment and concluded with a concrete functioning node of the sextet. The quintet and septet serve as its two grounds; the real counter-question unites the scene with instantiation. This is a substantive closure of this example, rather than a demand that every representation necessarily reduce to six slots.

The reverse verification of the volume traverses the same route: from the final proposition to the question, its source domain, action, common source, and accepted notation instruments. The preserved map allows this to be accomplished without reconstructing grounds from the author's memory.

Short verification: can one recover not only the terminal bit, but also what was asked, from where the question was posed, and what event instantiated it?

<a id="tnr-P62"></a><a id="tnr-П62"></a>
## 7.8 Boundary of the First Volume

The first volume presented a conditional method for constructing, transforming, and reconciling mathematical representations: distinguish a whole, execute an action, preserve the essential reverse side, and unfold a new presentation into the prior. In finite models, exact criteria of sufficiency, refinement, consistency, and recovery have been constructed. Memory and the right of continuation verify these transitions relative to a designated operation. The linear, arithmetic, phase, and subject branches received their own carriers and conditions.

The universal necessity of three axes, the completeness of the domain atlas, a general observer strategy, and computational optimality are not proven. The semantic windows 0–8 are retained as a map of distinct operations. Describing the chosen octet from an encompassing level does not become a ninth independent binary digit by its number alone.

The next volume must investigate the composition of the maps already named, the global consistency of windows, and newly admissible operations. With each extension, it will specify what became the subject, which prior law changed, and how unfolding is preserved.

The first volume itself becomes the \(i_{\mathrm{str}}[E]\) of subsequent investigation: a single presented whole with an accessible map of internal relations. Its conclusion consists in the preserved capacity to continue, rather than in declaring all of mathematics completed.

This example illustrates several mechanisms of self-application: addressed partitioning, preserving a common source, answer assembly, and accounting for the cost of continuation. It does not prove an accelerated general integer factorisation algorithm. Finite verifications are provided by programs for [action algebra check](verification/tnr_action_algebra_check.py), [operational hinge check](verification/tnr_operational_hinge_check.py), [local closure check](verification/tnr_local_closure_check.py), [unified operational structure check](verification/tnr_unified_operational_structure_check.py), [factorization lattice check](verification/tnr_factorization_lattice_check.py), and [descent closure memory check](verification/tnr_descent_closure_memory_check.py).

<a id="v1-appendix-A"></a>

# Appendix A Addresses, Domains, and Relation Types

This appendix unfolds the book's addresses from a level above its constructions. It connects the subject matter, the original projection, and the locus of application. An index of addresses does not substitute for a definition: each name returns a carrier, a map, a law, and an unfolding condition.

## What a Structural Address Contains

A definition retains its textual identifier Pxx, frame $\Gamma$, domain DM, subject type, carrier, presentation map, structural scalar, and established variety of rank. These roles are linked: type selects an admissible carrier; the map is defined upon it; rank pertains to a specific count; the frame admits a concrete operation. Their count does not establish an independent geometric figure.

A question address additionally returns the source \(\Gamma, B, m_{\mathrm{acc}}, \Omega, h\) and its instantiation \(q=h\circ m_{\mathrm{acc}}\). The designation $m_{\mathrm{acc}}$ refers to the presentation of accessible data; the geometric reference $m$ has a different type. For a transferred question, the action $T$ and its domain are also preserved. A current table may happen to coincide with that of a question of different origin. When origin is protected, identical tables do not constitute a single address.

The encompassing level displays the prior device as a subject. It is not automatically added to the binary rank. For example, describing all affine questions is a level above $S$, but the questions possess three independent tabular parameters, while $S$ has two free slots. The general level of description is not computed from these two numbers.

## Different Addressable Carriers of the Small Example

| Name | Element Type | Structure and Law | Established Count |
|---|---|---|---|
| $S$ | State | \((x,c)\), \(\beta=x\oplus c\) | Four states, two free bits |
| $B_\beta$ | Accessible value | \(\beta(s)\) | Two values, one bit |
| \(\Omega(B_\beta)\) | Rule on accessible value | All functions \(B_\beta\to\mathbb F_2\) | Four rules, two free tabular positions |
| $W$ | Affine question on $S$ | \(k\oplus ax\oplus dc\) | Eight questions, three free parameters |
| $U$ | Arbitrary question on $S$ | Four free table values | Sixteen questions, rank 4 |
| $A_6$ | Balanced question of $W$ | Three complement pairs | Six addresses within $W$; not a full binary carrier |
| $L_7$ | Non-zero question of $W$ | Fano XOR-lines | Seven addresses; not seven independent bits |
| $V_5(q_*)$ | Scene question other than selected | $A_6$ without focal $q_*$ | Five addresses; square pyramid graph |
| Act | Instantiation of action | Admissibility, source participant, $T$, question, and event | Count depends on declared library |

The textual identifiers P01–P62 are introduction addresses. They do not denote dimensions, bit weights, or model ranks. The exact card contents reside in the glossary, and the machine-readable record in the registry.

The concise questions of the book also receive addresses Q-Pxx. Their source frame is the definition to which they pertain; the projecting domain $B_{\mathrm{P}xx}$ contains the extracted subject, projection, law, unfolding, and evidence. The rule $h_{\mathrm{P}xx}$ answers according to the designated check, with \(q_{\mathrm{P}xx}=h_{\mathrm{P}xx}\circ m_{\mathrm{P}xx}\). When a definition is modified, the question transfers to the prior card via the map of that modification. This address does not coincide with the internal binary question $\beta$: the type of its argument is the definition itself.

For the 62 control questions, $\Gamma, B, m, h$ are specified. Here $m$ is an extraction map, not a geometric center. Finite verifications establish the presence of addresses and selected mathematical instantiations; automatic resolution of all natural-language queries is not claimed. A substantive answer requires producing the specified evidence or a reasoned refusal.

## Color Binary Map of Questions

Choose the basis \(x, c, \neg\beta\) for $W$. The color address $r,g,b$ defines the question

\[
q_{rgb}=rx\oplus gc\oplus b(1\oplus x\oplus c).
\]

This is the code of a question, not a state. The numerical values of the coefficients belong to $\mathbb F_2$. In this map we obtain:

| Address | Question | Table on 00, 01, 10, 11 |
|---|---|---|
| 000 | 0 | 0000 |
| 001 | \(\neg\beta\) | 1001 |
| 010 | $c$ | 0101 |
| 011 | \(\neg x\) | 1100 |
| 100 | $x$ | 0011 |
| 101 | \(\neg c\) | 1010 |
| 110 | \(\beta\) | 0110 |
| 111 | $u$ | 1111 |

Complementing a question is the XOR of its address with 111. Therefore, axes form address pairs 001/110, 010/101, 011/100; in standard binary enumeration, these are 1/6, 2/5, 3/4. The "/" symbol here separates opposite addresses rather than evaluating a rational fraction.

In the basis \(u, x, c\), the code takes the form \((k,a,d)=(b, r\oplus b, g\oplus b)\). Question $\beta$ receives the code 011, although in the color map it had 110. The vertex index changes with the basis; the question subject is preserved by an explicit map. The constant question $u$ has color address 111 and a different address in another basis.

Hamming distance is determined by the chosen code. Binary carry when passing $7\to8$ flips four bits in the standard numerical code; in Gray code, adjacent addresses flip only one. Neither distance in itself proves the necessity of a definition, the primality of a number, or informational surprise. For the latter, a probabilistic model is required.

## Two Octets and Two Different Ranks

The questions $W$ have eight addresses, each composed of three independent coefficients. If these addresses themselves become arguments to an arbitrary binary rule, the new rule possesses eight independently selectable answers. Therefore,

\[
|W|=2^3=8,\qquad |\operatorname{Map}(W,\mathbb F_2)|=2^8=256.
\]

The second space is not another cube of the same rank. For fixed three argument coordinates, the rule uniquely takes the form

\[
h(r,g,b)=\theta_\varnothing\oplus\theta_r r\oplus\theta_g g\oplus\theta_b b
\oplus\theta_{rg}rg\oplus\theta_{rb}rb\oplus\theta_{gb}gb\oplus\theta_{rgb}rgb.
\]

The eight coefficient slots are organized as 1 + 3 + 3 + 1: constant, individual responses, pairwise, and triple. Their addresses are subsets of three coordinates; the coefficients are eight free bits. The chosen release sequence of coefficients 0, 1, 2, 4, 3, 5, 6, 7 yields families of 1, 2, 4, ..., 256 rules. This is an exact eight-stage model, not a prescription of a unique order nor a classification of eight mathematical domains.

A color label here denotes a coefficient slot, whereas in the source table it denotes the question itself on $S$. Linking these uses requires an address map; coincidence of labels does not imply equality of their subject roles.

## Address of the Constructed Reference

The metacentre is the role of a reconciliation reference, rather than an additional unconditioned entity. In P30 it is instantiated relative to a declared real presentation of questions. The address distinguishes the reference $m$, the pointer $\eta_m$ from a single-point carrier, and the translation $C_m$ of the entire space. The pointer selects a point, but does not itself establish the midpoint law or translate the remaining points.

The constant pair of questions remains at distinct addresses even when its projection falls into a single center. The full real presentation has a constant direction and a three-dimensional deviation sector. A reduced reading into this sector requires naming the lost distinction; it does not become Fano merely by possessing seven distinct images.

When transferring a reference or coordinates, the subject map, pointer, and counter-question are verified separately. Reverse unfolding requires original data and does not substitute for the latter check. Addressed investigation of the metacentre specifies the exact carriers and boundaries of these operations.

## Seventeen Working Domain Families

The families retain their established names and identifiers. These are pointers to native operations; they overlap and do not claim to provide an exhaustive classification of mathematics.

| Family | Primitives and Law | Where Active in the Book |
|---|---|---|
| DM01 Binary and Logical | Values, NOT, XOR, conditions, consistency | Chapters 1–4, binary addressing |
| DM02 Numerical and Arithmetical | Number, zero, unit, fraction, arithmetic operation | Chapters 5–7, numerical readings |
| DM03 Combinatorial | Places, partitions, subsets, permutations | Partition, order, and tree; Chapters 1, 4, 5, 7 |
| DM04 Order and Closures | Refinement, inclusion, stability, saturation | Chapter 3 and arithmetic branch |
| DM05 Graph and Incidence | Vertices, edges, path, multi-place incidence | Chapters 2, 4, Appendices B, D |
| DM06 Algebraic | Composition, identity, inversion, commutator | Actions, Fano, algebras, and phase |
| DM07 Linear and Multilinear | Field, basis, image, kernel, pairing | Question center, linear proofs |
| DM08 Geometric and Metric | Point, simplex, angle, scale, norm | Chapter 4 and framings of Chapter 6 |
| DM09 Topological | Path, cells, gluing, covering | Chapter 6, Appendix D |
| DM10 Dynamical | Admissible step, direction, stage, continuation | Chapters 2, 3, 6, 7 |
| DM11 Analytical | Limit, derivative, exponential, logarithm | Chapter 6, Appendices D, C |
| DM12 Spectral | Character, frequency, eigenspace | Phase channels and proof linear layer |
| DM13 Measure and Probability | Weight, normalisation, mixture, correlation | Appendices D, E, and subject tests |
| DM14 Information and Recovery | Preimage, sufficiency, code, error | Chapters 1–4, 6, 7 |
| DM15 Computation and Memory | Word of actions, program, branch, trace | Chapters 2, 3, 7 |
| DM16 Representations and Reconciliation | Map, address, joint transfer, unfolding | End-to-end operation across the volume |
| DM17 Subject Meaning and Language | Role, name, question, scene participant | Locus of description and self-application |

A single domain does not possess a unique natural rank. In DM01 there already exist values $B$, states $S$, and the question space $W$ of different sizes. In DM05 edges may become vertices of a subsequent graph, but receive their own adjacency separately. In DM15 an act becomes an input to a tree, yet preserves its history and provenance.

## Twelve Working Genera of Relations

This is another index, intersecting with the domains. An operator is introduced with its own law; a symbol does not by itself define order, equivalence, or a metric.

| Genus | What Must Be Specified |
|---|---|
| R1 Distinction and Equivalence | Identity criterion of representation, classes, and preimages |
| R2 Order | Comparison relation; where required, greatest lower and least upper bounds |
| R3 Incidence | Participant types and rule of joint inclusion |
| R4 Algebraic Composition | Operation domain, table or law, identity, and inversion conditions |
| R5 Linear and Multilinear | Field, addition, scalar action, pairing |
| R6 Affine and Convex | Admissible combinations, deviation ratios, convexity conditions |
| R7 Projective | Which representatives are identified and what remains distinguishable |
| R8 Metric and Quadratic | Distance or form, its axioms and signature; a form is not always a norm |
| R9 Topological | Neighborhoods, continuity, preimages, gluing |
| R10 Transfer Along Paths | Local identifications and their composition; possible hidden return |
| R11 Measure and Probability | Events, weights, and normalisation; a conditional answer requires non-zero probability |
| R12 Joint Multi-Place | Admissible carrier subset of a product; consistency law and independence conditions |

A sign quotient in R7 preserves scale and is not full projectivisation. An indefinite quadratic form in R8 does not become a distance. The presence of an edge in R3 does not define an algebraic product in R4. These distinctions are protected by an address.

## Self-Application of the Index

The domain table folds content into concise names. Reverse unfolding returns native primitives and the locus of their operation. A shared correspondence links the name to a concrete source and verification. The number 17 here counts selected domain families, rather than primary dimensions.

Verification questions: what type of object is hidden behind the address; what is considered its scalar; from which domain does the question originate; which actions are elevated to the source whole; where is the reverse side and its unfolding located?

The address of a definition is specified by its chosen carrier, projection, and law. Its number or position in the table of contents does not substitute for this passport; when shifting projection, the question and mode of reverse unfolding are specified anew.

<a id="v1-appendix-B"></a>

# Appendix B Finite Tables, Memory, and Recovery

This is a proof supplement to Chapters 2–4. The locus of description is finite named tables with partial deterministic actions. Functions, partitions, binary arithmetic, and Hamming distance are standard. For each result, its domain is stated: preservation of answer, admissibility, continuation, or state and order. The universality of these models is not assumed.

## B1 Four States and Five Actions

Retain \(S=\{00,01,10,11\}\), \(\beta=x\oplus c\). Define

\[
T_x(x,c)=(x\oplus1,c),\quad
\sigma(x,c)=(x\oplus1,c\oplus1),\quad
T_m(x,c)=(x\oplus c,c),\quad
E(x,c)=(0,c).
\]

The partial action $G$ coincides with $T_x$ when $c=0$ and is prohibited when $c=1$.

| Source | $x$ | $c$ | $\beta$ | $T_x$ | $\sigma$ | $T_m$ | $E$ | $G$ |
|---|---|---|---|---|---|---|---|---|
| 00 | 0 | 0 | 0 | 10 | 11 | 00 | 00 | 10 |
| 01 | 0 | 1 | 1 | 11 | 10 | 11 | 01 | Prohibited |
| 10 | 1 | 0 | 1 | 00 | 01 | 10 | 00 | 00 |
| 11 | 1 | 1 | 0 | 01 | 00 | 01 | 01 | Prohibited |

Prohibition is not a zero answer. In implementation it carries a distinct address indicating absence of admissibility; an admissible answer of zero remains an ordinary value.

The counter-questions to future $\beta$ are respectively \(\bar\beta, \beta, x, c\); for $G$, one obtains the question \(\bar\beta\) restricted to $c=0$. The transfer preserves the source $B_{\beta,1}$, the identity answer rule, and the map \(m_1=\beta\). The current table of $x$ does not yet make $x$ accessible to an observer with only current $\beta$.

For each admissible source, \(q_1(Ts)=(T^*q_1)(s)\) is verified. A witness additionally binds both records to a single ledger and event. Numerical equality does not by itself distinguish two repeated instantiations.

## B2 Descent Condition and Its Failure

Let \(m:S\twoheadrightarrow B\) be an accessible reading. A map $f$ is expressed through $m$ if and only if it is constant on every fiber (preimage) of $m$. For a partial map, identical admissibility within each fiber is also required.

Necessity follows from \(f=\widehat f\circ m\). For sufficiency, define \(\widehat f(b)\) by any participant of \(m^{-1}(b)\): constancy makes the choice unique. For a fiber on which the action is prohibited, the descended map is likewise prohibited.

For \(m=\beta\), the fibers are \(\{00,11\}\) and \(\{01,10\}\). On the first fiber, the question $x$ distinguishes rows; hence \(T_m^*\beta\) does not descend. Under $G$, each fiber mixes an authorized and a prohibited state; even a constant question cannot resolve this admissibility insufficiency.

The refinement \(m'=(\beta,c)\) distinguishes all four states and expresses the transferred $x$ via the rule \(h'(b,c)=b\oplus c\). This is recovery from two accessible distinctions, not cost-free knowledge of a hidden state.

## B3 The Coarsest Stable Memory

Given a finite set $S$, fixed protected answers, and a finite family of partial actions. An initial partition $P_0$ groups states sharing identical protected answers. Define $P_{k+1}$ by the state signature: its class in $P_k$, the admissibility of all actions, and the classes of all admissible results in $P_k$.

Each step only refines the partition. The number of classes cannot exceed $|S|$; hence after finitely many strict refinements, a fixed partition $P_*$ is reached.

Within a single class of $P_*$, source answers, all action admissions, and subsequent classes coincide. Induction on the length of an action word demonstrates that states within a single class yield identical answers and identical possibilities for every finite continuation.

Let $R$ be any other stable partition preserving initial answers. It refines $P_0$. If it refines $P_k$, stability forces it to distinguish all mismatched admissions and result classes of $P_k$; consequently, it refines $P_{k+1}$. Therefore $R$ refines $P_*$.

Thus $P_*$ is the coarsest sufficient partition. Minimality pertains to the classes of this given finite task, not to code cost, information-acquisition route, or full history memory.

To protect $\beta$ under \(\{T_x,\sigma\}\), two classes suffice. Adding $T_m$ or $G$ requires four classes. The carrier $S$ does not grow: previously hidden distinctions are brought to light. Exhaustive enumeration of all fifteen partitions confirms this result independently of the general proof.

## B4 Question Tables and the Full Carrier

Every binary function on $S$ possesses a unique form

\[
q=k\oplus ax\oplus dc\oplus exc.
\]

The proof is constructive: \(k=q(00)\), \(a=q(10)\oplus k\), \(d=q(01)\oplus k\), and \(e=q(00)\oplus q(01)\oplus q(10)\oplus q(11)\). This reconstructs all four initial rows.

| Family | Elements | What Is Counted |
|---|---|---|
| All questions | Sixteen tables | Four independent answers |
| $W$ | \(0,u,x,\bar x,c,\bar c,\beta,\bar\beta\) | Three affine coefficients |
| $L_7$ | \(W\setminus\{0\}\) | Seven non-zero questions |
| $A_6$ | \(W\setminus\{0,u\}\) | Six balanced questions |
| $V_5$ | \(A_6\setminus\{q_*\}\) | Five alternatives to a designated question |
| $\mathcal P_q$ | \(0,u,q,\bar q\) | Four local rules on two accessible values |

The three Fano lines through $u$ are \(\{u,x,\bar x\}\), \(\{u,c,\bar c\}\), and \(\{u,\beta,\bar\beta\}\). The remaining four lines are:

\[
\{x,c,\beta\},\quad \{x,\bar c,\bar\beta\},\quad
\{\bar x,c,\bar\beta\},\quad \{\bar x,\bar c,\beta\}.
\]

Their XOR sum is zero; therefore three true answers cannot hold simultaneously. The other four faces of the octahedron have XOR sum 1 and share a single state each. The centered real vectors \(x-m, c-m, \beta-m\) are pairwise orthogonal, since products of their four coordinates produce two positive and two negative terms of $1/4$ each.

## B5 Which Actions Preserve the Family

There exist \(4^4=256\) total mappings \(S\to S\). All binary questions are closed under transfer across any such mapping: composition again yields a binary truth table on $S$.

To preserve $W$, it is necessary and sufficient that both coordinates of $T$ be affine functions. Necessity follows by transferring $x$ and $c$; sufficiency by substituting these coordinates into any affine question. Each coordinate has eight possibilities, giving 64 actions.

Preserving $A_6$ requires that the preimage of any two-element subset of $S$ contain two elements. If the sizes of the four single-point preimages are $n_i$, then \(n_i+n_j=2\) for all \(i\ne j\). Thus all \(n_i=1\), meaning $T$ is a permutation. Conversely, any permutation preserves balance. There are \(4!=24\) such actions.

Erasure $E$ maps $x$ to the zero question, removing the transfer from the active sextet. The nonlinear map \((x,c)\mapsto(xc,c)\) transforms $x$ into $xc$, ejecting it from $W$. Hence the completeness of the octet is conditional on the chosen action. These 256 cases were verified in the window survey.

## B6 Recovery of State and Order

The new carrier consists of four named binary slots. For a permutation $\pi$, set \(y_i=x_{\pi(i)}\), \(a=y_0\), and \(d_{ij}=y_i\oplus y_j\). The reverse assembly takes the form

\[
y_0=a,\qquad y_i=a\oplus d_{0i},\qquad x_{\pi(i)}=y_i.
\]

Without the reference, $y$ and $\bar y$ remain ambiguous. Without the order, assignment to names remains ambiguous, and under identical values the order history is lost as well. Without comparisons, the reference supplies only a single value. A shared act binds the three layers; an arbitrary mixture of alien layers is not a recovery of the original instantiation.

Under six comparisons \((01,02,03,12,13,23)\), eight valid words are possible. Aligning the reference \(y_0=0\), we obtain:

| $y_1y_2y_3$ | Comparison Word |
|---|---|
| 000 | 000000 |
| 001 | 001011 |
| 010 | 010101 |
| 011 | 011110 |
| 100 | 100110 |
| 101 | 101101 |
| 110 | 110011 |
| 111 | 111000 |

If two value assignments differ in $r$ positions, the comparison words differ on edges between changed and unchanged positions, that is, in \(r(4-r)\) positions. For distinct relative states, $r\in\{1,2,3\}$; the minimum distance is 3. This is a linear \([6,3,3]\) code: six stored bits, three information bits, and minimum distance three.

## B7 One Error in Each Layer

Declare an error model: at most one incorrect bit in comparisons; at most one incorrect bit in the triple repetition of the reference; at most one corrupted copy among three records of the entire permutation. These are three independent bounds on admissible error, not an assertion regarding arbitrary memory corruption.

Comparisons are corrected by selecting the valid codeword at distance at most one. If two such codewords existed, the distance between them would not exceed two, contradicting the minimum distance three. The reference is recovered by majority vote among three bits. The permutation order is recovered by agreement of two out of three complete copies. The copies retain identical names and domains of instantiation.

Following correction, the reverse assembly B6 is applied. It recovers state and order for each of the \(16\cdot24=384\) source instantiations. This is a concrete multilayer protection; its redundant copies and verification incur cost. Minimality of redundancy across all three layers is not asserted.

If corruption alters the source itself and consistently replaces all copies, this model cannot detect it. Defense against arbitrary forgery, address errors, or law violation requires different conditions. Recoverability from correct data, error detection, error correction, and authentication of provenance are distinct operations.

## B8 Boundary of the Finite Kernel

On $S$, concrete questions, admissions, compositions, shared events, and stable classes are verified. The source projecting domain is stored within the question even when current truth tables coincide. Shifting roles yields new carriers of questions, rules, and comparisons; matching cardinalities does not make them a single space.

These proofs do not prescribe an optimal observer strategy, do not establish the universality of eight stages, and do not turn a structural folding into a complex unit. Further equipping must specify its field, actions, map from this kernel, and preserved operation. In this way, the finite result remains an unfoldable part of a new whole. Verification scripts: composition, independent regressions, multilayer recovery.

<a id="v1-appendix-C"></a>

# Appendix C Arithmetical Foundations and Algebras

This appendix unfolds Chapters 5 and 7 in numerical, combinatorial, and algebraic projections. Units in arithmetic formulas carry their ordinary numerical meaning. The structural unit is a distinct addressed presentation of a proof or device. The proofs of general identities given below do not imply re-verification of the entire historical corpus.

## C1 Divisor Coordinates and Path Counts

Let \(N=\prod_{j=1}^r p_j^{e_j}\) be known, where the primes are distinct. The uniqueness of prime factorisation establishes a bijection between divisors of $N$ and vectors \((a_1,\ldots,a_r)\) with \(0\le a_j\le e_j\). Divisibility corresponds to coordinatewise comparison. GCD and LCM take componentwise minimum and maximum; the complement \(d\mapsto N/d\) maps \(a_j\mapsto e_j-a_j\).

Therefore, the number of states in the divisor lattice is \(\prod_j(e_j+1)\). Under the step of multiplying by a single prime, the number of shortest paths from 1 to $N$ is

\[
\frac{(\sum_j e_j)!}{\prod_j e_j!}.
\]

Proof: a path is a word containing $e_j$ identical steps of direction $j$; permuting identical steps does not create new paths. The state address and the order of arrival are distinct data of a single whole. For squarefree $N$, the states form a cube of $2^r$ positions, and paths form $r!$ orderings.

In particular, \(97155=3^2\cdot5\cdot17\cdot127\) has 24 divisors and 60 shortest paths. The number 24 is not in itself a rank, a dimension, or the order of a natural action group.

## C2 Three Signatures of a Natural Event

Here the counters $a, \ell, f$ follow the definitions in P42. An integer $n$ is either prime, or possesses a single prime axis with exponent greater than one, or possesses multiple prime axes. Uniqueness of factorisation renders these cases mutually exclusive and exhaustive for $n\ge2$. A new position always increments $f$; a prime power increments $\ell$; a new prime increments $a$. Hence the signatures 111, 011, 001.

For the products $A_n, L_n, F_n$, the event types are the same, but the data completeness differs. The exponent of $p$ in $L_n$ is the maximal $k$ such that \(p^k\le n\). It increases only at a prime power. The exponent in \(F_n=n!\) equals \(\sum_{k\ge1}\lfloor n/p^k\rfloor\); each new $n$ adds the exponents of its factorisation. The exponent in $A_n$ is 0 or 1 according to the presence of a prime axis.

The shared source ensures reconciliation between representations. No signature supplies the value of the unknown next prime. Flags, triangular readings, orders, and analytical bounds pertain to distinct projections of the natural sequence. The Euler product and explicit formulas for primes are classical foundations, not new deductions of this chapter.

## C3 Assembly of Child GCDs

Let $A, B$ be positive integers, \(N=AB\), \(r\in\mathbb Z\), \(d_A=\gcd(A,r)\), and \(d_B=\gcd(B,r)\). Set \(D=\operatorname{lcm}(d_A,d_B)\) and \(C=\gcd(N/D,r/D)\). The division $r/D$ is exact since $D$ divides $r$, including when $r=0$. Then

\[
\gcd(N,r)=DC,\qquad C\mid\gcd(A,B).
\]

For a single prime with exponents $a,b,t$, the exponent of $D$ is \(\min(\max(a,b),t)\). The exponent of $C$ is \(\min(a+b,t)-\min(\max(a,b),t)\). Their sum gives the exponent of the parental GCD. For $r=0$, we obtain \(D=\operatorname{lcm}(A,B)\) and \(C=\gcd(A,B)\). A coprime partition gives $C=1$ for any $r$.

The two numbers $d_A, d_B$ are not always sufficient. For \(25=5\cdot5\), operands $r=5$ and $r=25$ yield identical child answers 5, 5, but different parental answers 5 and 25. Correcting for shared multiplicity is an indispensable reverse side of reduced assembly.

For positive $N$ and an initial positive divisor \(x_0=d\mid N\), the saturation \(x_{k+1}=\gcd(N,x_k^2)\) preserves the prime support of $d$ and doubles non-zero exponents up to their bounds in $N$. The limit \(S_N(d)=\prod_{p\mid d}p^{v_p(N)}\) is coprime to $N/S_N(d)$. A proper partition exists only under non-empty, incomplete support of $d$. The equality $S_N(d)=N$ does not prove the primality of $N$. For an arbitrary $x$ not dividing $N$, preservation of support is not asserted.

Any computational deployment of this formula requires separately specifying initial stages, tariff, accessible sources, and executed actions. The proof of the identity given here does not authenticate a specific program run.

### Multiple Parts and the Exact Reverse Side of Numerical Reading

Let \(k\ge1\), and let all $A_i$ be positive integers; consider a partition \(N=\prod_{i=1}^k A_i\) and answers \(d_i=\gcd(A_i,r)\) for a single shared integer $r$. We describe from the arithmetical frame above this partition: the full $r$ is not currently retained; only the named parts and child answers are known. Define

\[
D=\operatorname{lcm}_i d_i,\qquad K=\frac{N}{\operatorname{lcm}_i A_i},\qquad
R=\prod_i\frac{A_i}{d_i},\qquad
H=\frac K{S_K(\gcd(K,R))}.
\]

Here $S_K$ is the saturation within $K$ defined above; \(S_K(1)=1\). For the source answers, it is necessary that \(d_i\mid A_i\) and \(\gcd(A_i,D)=d_i\). When these conditions are satisfied, among all integer operands compatible with the child answers, the parental answers form precisely the following family, where $C$ ranges over positive divisors of $H$:

\[
\boxed{\{D C:C\mid H\}.}
\]

The proof proceeds by prime valuations; for $r=0$ we take \(v_p(0)=+\infty\), and for negative $r$ we use the valuation of its absolute value. Let \(a_i=v_p(A_i)\), \(b_i=v_p(d_i)\), and \(d=\max_i b_i\). If at least one \(b_i<a_i\), the overall valuation of $r$ is already fixed: it equals $d$. There is no hidden correction on this axis. Such an axis enters $R$, and if present in $K$, it is eliminated by saturation. If all \(b_i=a_i\), all that is known is \(v_p(r)\ge\max_i a_i=d\). The correction to the parental answer can take any valuation from zero to \(\sum_i a_i-\max_i a_i=v_p(K)\). These and only these axes remain in $H$. Choosing their valuations is independent; the operand \(r=DC\) realizes each listed answer and preserves the specified child answers.

For \(N=3^4\) and four parts \(A_i=3\), the answers \(d_i=3\) yield \(D=3, H=27\). The possible parental answers are 3, 9, 27, 81. Four leaf addresses and their history retain the partition, but four identical numerical answers do not retain the multiplicity of the shared operand.

This is the exact reverse side of **this reduced numerical reading**. Additional data from the real source may narrow the family; a retained parental answer can eliminate ambiguity. The formula for $H$ does not mean its calculation is cost-free or an authorized command of the program. A power reading \(3^4\) retains multiplicity, but requires separate addressing of participants.

## C4 Coordinate Subalgebras and Selected Cubes

In a fixed standard octonionic basis \(e_u\), \(u\in\mathbb F_2^3\), the product of basis elements carries the label \(u\oplus v\) and an additional sign. A coordinate subalgebra is the real span of a closed set of these labels. A non-empty set contains 0, since \(u\oplus u=0\); closure under XOR signifies a linear subspace. The empty set separately defines the zero algebra.

There are: the zero algebra, one $\mathbb R$, seven $\mathbb C$, seven $\mathbb H$, and one $\mathbb O$: 17 in total. Immediate inclusions form 36 edges: 1 + 7 + 21 + 7. This is a finite coordinate sample, not the set of all real subalgebras. The correspondence between label subspaces and these algebras is set out by [Baez](https://math.ucr.edu/home/baez/octonions/node4.html).

Three independent labels $a,b,c$ distinguish a cube of eight subalgebras generated by subsets of this triple. There are \(7\cdot6\cdot4=168\) ordered bases; the ordering of three chosen generators does not alter the cube, yielding 28 selected cubes. Complementary $C/H$ in such a cube intersect in $\mathbb R$ and jointly span $\mathbb O$.

The sign table and parenthesization order are preserved separately. In \(\mathrm{Cl}_{3,0}\), labels also add via XOR, but \(e_j^2=1\), distinct generators anti-commute, and the algebra is associative. It possesses the same coordinate-closure graph yet different subalgebra types. Consequently, an identical graph does not supply identical multiplication.

In this selected coordinate model, there are 17 nodes and 28 cubes. These numbers pertain to the fixed basis and chosen generator family; they do not classify all real subalgebras and do not specify a universal rank. Sign and norm constructions require additional equipping.

## C5 Boundary of Factorisation Inference

A known factorisation provides divisor coordinates. An obtained proper divisor can provide a useful cut. Saturation can predict the type of future assembly in advance. None of these assertions delivers an unknown divisor without additional work.

The period, residue, character, or phase address of a candidate are evaluated within the same frame alongside the cost of obtaining them. An admissible candidate, an executed trial, and a confirmed factor have distinct addresses. A new acceleration of factorisation, a prime distribution law, and the optimality of a chosen policy are not proven in the first volume. Computational examples are provided in the verification scripts for [action algebra check](verification/tnr_action_algebra_check.py), [operational hinge check](verification/tnr_operational_hinge_check.py), [local closure check](verification/tnr_local_closure_check.py), [unified operational structure check](verification/tnr_unified_operational_structure_check.py), [factorization lattice check](verification/tnr_factorization_lattice_check.py), and [descent closure memory check](verification/tnr_descent_closure_memory_check.py).

<a id="v1-appendix-D"></a>

# Appendix D Phase, Topological, and Geometric Framing

The locus of description is the proof instantiations of Chapter 6 on the designated carriers and the reconciliation of their representations. The complex law, metric, regularity, and gluing are specified separately. Memory and sufficiency verify the transfer of the chosen action and question. The structural unit of each instantiation preserves these conditions together with an unfolding address.

## D1 From Finite Cycle to Linear Action

For \(V(v,s)=(v\oplus1,s\oplus v)\), we have \(V^2(v,s)=(v,s\oplus1)\) and \(V^4=I\). The map \(z(v,s)=(-1)^s i^v\) is injective on four states. When $v=0$, the action $V$ transforms $z$ to $iz$; when $v=1$, it flips $s$ and again transforms $z$ to $iz$. This is an exact connection between selected carriers, rather than an identification of every four-slot object with the complex plane.

On the real plane, \(J(a,b)=(-b,a)\) satisfies \(J^2=-I\). Expanding the exponential into even and odd powers yields \(e^{\theta J}=\cos\theta\,I+\sin\theta\,J\). Standard orientation and metric turn this law into a rotation. Without a named metric, an assertion regarding an angle would be an additional framing.

On this same equipped plane, set \(G=e^{(\pi/6)J}\) and \(R=G^2\). Then the quarter-turn is \(G^3=J\), the six-beat rotation is $R$, with \(J^2=R^3=G^6=-I\) and \(G^{12}=I\). Subgroups of orders four and six share the common subgroup \(\{I,-I\}\) and jointly generate $C_{12}$, since \(JR^{-1}=G\). Any common finite cycle containing these orders must have an order divisible by four and six; thus twelve is minimal. This reconciles the chosen laws on a single plane, but does not prove conjugation of the real RGB$\to$Lab transfer with Euclidean rotations. The color study (§8) preserves the native domain of this assertion.

The proof of criterion P46 rests on representative independence: \(\bar f(\pi e)=f(e)\) is uniquely defined precisely when both participants of each fiber share the same value. For an action, the formula \(\bar T(\pi e)=\pi(Te)\) additionally requires a common admission for both participants. Sequentially descended actions compose according to P20; event composition separately preserves the shared intermediate source. A free involution and this descent do not by themselves establish a complex structure $J^2=-I$.

For the square map \(q(z)=z^2\), the forward state map conceals the sign. The lifted continuous path retains the chosen initial root. A continuous global section over $S^1$ is impossible: a single traversal maps the root to its opposite, contradicting the return of the section at the initial point.

## D2 The Vertical Cyclic Kernel

Let $N$ be odd, $m\ge2$, and $h\ge1$. The kernel of the unit reduction is

\[
K_{m,h}=\{1+2^m k\pmod{2^{m+h}}:0\le k<2^h\}.
\]

For odd $c$ and $k\ge2$, we have

\[
(1+2^k c)^2-1=2^{k+1}c(1+2^{k-1}c),
\]

whence its binary 2-adic valuation is $k+1$. Induction yields \(v_2((1+2^m)^{2^j}-1)=m+j\). The order of \(g=1+2^m\) modulo \(2^{m+h}\) is exactly $2^h$; that is, $g$ generates the entire kernel.

The action \(u\cdot(x,y)=(ux,u^{-1}y)\) preserves the product and the lower pair. For two pairs in the same fiber, the unique connecting element \(u=x'x^{-1}\) belongs to $K$. Thus the fiber is a torsor of $K$. Origin coordinates within it require a basepoint; cardinality and cyclicity do not select one automatically.

The exception is essential. For $m=1, h=2$, the kernel consists of four units modulo 8, each non-identity element having square 1. This is $C_2^2$, not $C_4$. The full group of units for $n\ge3$ is \(C_2\times C_{2^{n-2}}\). Consequently, the cyclic lifting rule requires the stated conditions and does not transfer automatically to the first level.

## D3 Phase Calibration and the Counter-Character

Fix an odd representative $x_0$ of the lower coordinate and the basepoint \(f_h^0=(x_0,Nx_0^{-1})\pmod{2^{m+h}}\). Then \(f_h(t)=g^t f_h^0\) receives the phase address \(z_h=e^{2\pi it/2^h}\). Under reconciled reduction, \(t_{h+1}=t_h+2^h b_h\), whence \(z_{h+1}^2=z_h\).

The sign pair $\pm$ specifies two lifts of a given lower answer. The counter-transfer of character \(\chi_j(t)=e^{2\pi ijt/2^h}\) possesses frequency $2j$ at the upper level. A primitive upper character does not transfer from below: its square transfers. The source of the question is the lower cyclic kernel and its chosen basepoint; the argument of the transferred question is the upper kernel.

Upon changing basepoint to \(g^a f^0\) and generator to $g^u$ ($u$ odd), the address changes as \(t'=u^{-1}(t-a)\). Unreconciled basepoints introduce an additional multiplier into the squaring law. Hence the lifting sign pertains to the declared calibration, rather than automatically to the most significant bit of a factor.

If $q=2^h$, the upper address $t=u+qb$ obeys the law

\[
(u,b)*(v,c)=
((u+v)\bmod q,\ b\oplus c\oplus\lfloor(u+v)/q\rfloor).
\]

The carry couples the lower coordinate to the new bit. For $q\ge2$, the extension \(C_2\to C_{2q}\to C_q\) does not split into a direct product: every lift of the lower generator has order $2q$. Therefore the notation "lower address and bit" does not turn the actions into independent XOR switches.

This composition memory is not identified with Pauli cocycles or $\kappa$ on other bases. Coincidence of the labels "sign" or "center" does not identify their carriers and laws. None of these records by itself provides an independent reading that selects an unknown factor.

## D4 Topological Carriers and Sources

The quadratic covering has two-point fibers. The Möbius strip \(([0,2\pi]\times[-1,1])/((0,t)\sim(2\pi,-t))\) has intervals as fibers over the base. The projective plane identifies antipodal directions of the sphere. The Hopf map in P53 identifies the common complex phase of a coordinate pair and has a circle as its fiber. A pair, an interval, and a circle are distinct hidden carriers.

The two-sheeted covering of the base is isolated on the boundary of the Möbius strip $|t|=1$: over each lower locus sit two sides, and a single traversal interchanges them. The entire strip preserves interval fibers. A topological covering requires local triviality; a graph covering requires unique lifting of adjacent edges; a central extension requires a group homomorphism with central kernel. These conditions belong to distinct framings. The Hopf map with circular fiber and a measurement instrument with branch operations are not encompassed by a single two-sheeted criterion. The map of exact types and boundaries connects these branches via P19–P20 without identifying them.

Verifying the norm of the Hopf formula is direct: \(4|z_1|^2|z_2|^2+(|z_1|^2-|z_2|^2)^2=(|z_1|^2+|z_2|^2)^2=1\). When \(z_1\ne0\), the answer specifies \(|z_1|^2\) and \(z_1\overline z_2\); after choosing the phase of $z_1$, $z_2$ is determined. In the special case $z_1=0$, the phase of $z_2$ remains. This unfolds the circle of shared phase without confusing it with a binary sign.

General foundations of coverings and cell complexes are presented in [Hatcher's textbook](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). The phase constructions given here are distinct equipped examples; they do not deduce a single topological structure for all domains.

A spectral carrier requires an operator, a field, and domain conditions. Full matrices, normal forms, and spectral calculations from earlier appendices are preserved via the coverage map. Curvature, variational certificates, and global spectral limits continue in Volume II; they are not deduced by Euler's formula alone.

<a id="v1-geometry-two-sources"></a>
## D5 Geometric Reconciliation of Two Sources

The locus of description is Euclidean geometry following the finite kernel P27–P35. The convex hull and polar dual \(P^\circ=\{y:y\cdot x\le1\ \forall x\in P\}\) relative to a designated center 0 are standard. This zero is the coordinate expression of the chosen reference of this framing after centering, not a universal metacentre of all representations. The constructed reference, its pointer, and the translation map preserve different types in P30. For selected regular polytopes, all vertices have squared norm $R^2$; the maximum product of distinct vertices $a_e$ is attained precisely on edges. The scale \(c=(R^2+a_e)/2\) equals the squared norm of an edge midpoint. Denote the hull of all midpoints by $M(P)$.

Under this framing, three exact assemblies are obtained:

| Two Sources | Reconciled Scale | Shared Object |
|---|---|---|
| Two opposite tetrahedra with vertices of two parities \((\pm1,\pm1,\pm1)\) | $c=1$ | Octahedron: 6 vertices, 12 edges, 8 faces |
| Cube $C_1$ and octahedron $O_2$ | $c=2$ | Cuboctahedron: 12 vertices, 24 edges, 14 faces |
| Icosahedron $I$ and dodecahedron \(D=\varphi^2I^\circ\), \(\varphi=(1+\sqrt5)/2\) | $c=\varphi^2$ | Icosidodecahedron: 30 vertices, 60 edges, 32 faces |

In each row, \(P\cap cP^\circ=M(P)=M(cP^\circ)\). The intersection of corner truncations leaves precisely the edge midpoints. A prior edge becomes a vertex; prior vertices and faces become two families of faces; a corner $(v,f)$ becomes an edge. Therefore \(V_M=E_P\), \(E_M=2E_P\), and \(F_M=V_P+F_P\). These counts follow from addressed incidence, rather than specifying it on their own.

The reverse inclusion requires excluding other intersection vertices, rather than merely verifying membership of midpoints. For the named regular polytopes, this is accomplished by classifying active constraints and displaying each midpoint as a vertex in the complete proof (§2). Sufficient metric conditions remain part of the proposition; the general case in another dimension does not follow from this table.

For the golden row, the real presentation \(I_{\mathbb R}\subset\mathbb R^3\) and the phase presentation \(I_i=iI_{\mathbb R}\subset i\mathbb R^3\) are explicitly distinguished. The map \(F_i(x)=ix\) transfers all coordinates: \((0,\pm1,\pm\varphi)\) becomes \((0,\pm i,\pm i\varphi)\), and the two other cyclic families transfer likewise. The inverse unfolding is \(F_i^{-1}(z)=-iz\). Geometry is preserved by the Hermitian metric; polarity is taken within the chosen real sheet and satisfies \((iP)^{\circ_i}=iP^\circ\). Therefore \(D_i=iD_{\mathbb R}\) and \(K_i=iK_{\mathbb R}\).

The numerical $\pm1$ are coordinate readings after removing the declared phase, not an equality $i=1$. The parameter $\varphi$ remains real. Complex $i$ and structural $i_{\mathrm{str}}$ are distinguished. The phase sheet is real 3-dimensional; full $\mathbb C^3$ is real 6-dimensional. A fixed map adds no free bit. For the prior question \(q_{\mathbb R}(x)=[n\cdot x\le b]\), the phase question is \(q_i(z)=q_{\mathbb R}(-iz)\), whence \(q_i\circ F_i=q_{\mathbb R}\). The rule domain and threshold remain real, while the phase and transition address are retained in the frame. Unfolding the transfer restores the omitted connection with the source phase branch.

The shared polytope preserves the symmetries of the sources under joint transfer. However, a shared center or an unnamed graph does not recover the original polytopes. A metric, scale, and constraint labels are required. When one family of faces vanishes due to scale change, its source hyperplanes are stored separately. Cell counts are not assigned as free binary ranks.

For the tetrahedron, two readings of a single edge—the midpoint \((t_i+t_j)/2\) and the directed half-difference \((t_j-t_i)/2\)—yield $O_6$ and the 12-slot cuboctahedral carrier. The folding \((i,j)\mapsto\{i,j\}\) is a two-sheeted covering of the selected graphs. The four stellar faces of $O_6$ lift to eight triangles; the four cyclic faces lift to 6-cycles with reversed hidden orientation. The second family is linked to the four Fano lines without the constant question. This is not a covering of filled surfaces, nor an identity of path with XOR law.

For the icosahedron, the sets of midpoints and directed half-differences likewise coincide after scaling by $\varphi$, but their preimages differ. The midpoint conceals the order of the two endpoints; the half-difference conceals the choice between two parallel edges. A single shared source allows reconciliation of these readings; the single number thirty does not.

Thus the five Platonic solids, the cuboctahedral continuation, and the Fano law enter a single addressed atlas, rather than merging into a single figure or algebra. Detailed conditions and treatments belong to separate research notes and are not included in this publication folder. Additional finite checks of root models: [A3](verification/verify_a3_cover.jl) and [H3](verification/verify_h3.jl). This branch instantiates the principle "a prior whole became a participant in a new relation"; the universality of such an assembly remains open.

<a id="v1-appendix-E"></a>

# Appendix E Quantum and Linguistic Tests of Reconciliation

Subject-matter models verify the reconciliation of representations on equipped carriers. Quantum, linguistic, and color laws are adopted within their own native domains, rather than deduced from the number of slots in a general passport. The locus of description is the comparison of states, questions, events, and accessible continuation; memory and sufficiency verify the integrity of the transition. In the quantum model, the structural unit denotes the passport of this device, not a qubit by itself.

## E1 One Qubit and Two Counter-Transfers

A state is specified by a positive $2\times2$ density matrix $\rho$ of trace 1. A binary question is specified by effects \(E_0, E_1\ge0\), with \(E_0+E_1=I\). The presentation \(m_E(\rho)=(\operatorname{Tr}(E_0\rho), \operatorname{Tr}(E_1\rho))\) belongs to the space of binary distributions $B$. A rule $h$ on $B$ can select the probability of the second answer. Then \(q=h\circ m_E\).

$B$ is the projecting domain of this rule; $\rho$ is the argument on the source quantum carrier. The distribution is not an already obtained outcome of a single measurement. The frame additionally declares preparation, permitted actions, and access to samples.

For a unitary action \(T_U(\rho)=U\rho U^\dagger\), we have

\[
\operatorname{Tr}(E_1U\rho U^\dagger)
=\operatorname{Tr}(U^\dagger E_1U\rho).
\]

The state transfers forward; the effect of the question transfers in a counter-manner. The shared third structure is a single source state, the same operator, and the preserved probabilistic pairing. The projecting source \((\Gamma, B, m_E, h)\) remains known in the reading \(h\circ m_E\circ T_U\).

For a complete channel \(\Phi(\rho)=\sum_a K_a\rho K_a^\dagger\), the normalisation \(\sum_a K_a^\dagger K_a=I\) is assumed. The counter-map also exists: \(\Phi^*(E)=\sum_a K_a^\dagger E K_a\). It does not require physical reversal of the channel. For an individual branch, the trace may decrease; its output is not normalised without non-zero probability. For example, a $Z$-measurement with discarded outcome erases off-diagonal elements; the original coherence cannot be recovered by the mere name of a counter-question.

If the conditional output of a measurement is protected, a probability distribution alone is insufficient. Branch operations—an instrument—are required; if intermediate interventions are protected, a multi-step specification is needed. This is the quantum instantiation of the distinction between answer, act, and continuation introduced in the opening chapters.

## E2 Finite Addresses and Different Octahedra

The matrices

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}
\]

yield \(X^2=Z^2=I\) and \(XZ=-ZX\). Consequently, \(J=XZ\) satisfies \(J^2=-I\) and coincides with the planar operator in P47. The sign equipment of the pair is presented here by matrices. On density matrices, the action \(T_J(\rho)=J\rho J^\dagger\) already has square identity: the overall sign $-I$ cancels. The four-beat operator law and the two-beat return of this state are different protected operations.

On the Bloch sphere, the six states \((I\pm X)/2, (I\pm Y)/2, (I\pm Z)/2\) are located at the vertices of an octahedron. Its vertices are states, not six independent outcomes of concurrently executed questions. Each antipodal pair belongs to a single chosen measurement.

On three qubits, a different octahedron appears: vertices \(X_1, Z_1, X_2, Z_2, X_3, Z_3\), with edges denoting commutation across different slots; within a single pair, operators anti-commute. A face selects one generator from each pair. A chosen commuting triple $g_1, g_2, g_3$ specifies seven non-zero products \(g(u)=\prod_j g_j^{u_j}\); the Fano lines carry labels \(\{u, v, u\oplus v\}\).

The computational basis \(|x\rangle\), \(x\in\mathbb F_2^3\), contains eight addresses; the operators $X_j$ switch them along the edges of a cube. The full quantum carrier contains superpositions and mixed states and is not exhausted by eight addresses. Complete Pauli labels without global phase comprise 63 non-identity operators, not seven. Our selected Fano plane is a single commuting sector, not the entire operator geometry. Finite verification of local windows is available in the [Julia program](verification/verify_pauli_local_windows.jl).

It is typing that connects these objects. The cube addresses basis states, the octahedron selects generators, and the Fano plane composes actions of a chosen context. An identical number or figure does not transform their elements into a single genus.

## E3 What Preservation of Quantum Operation Means

A classical hidden address is not a quantum superposition. A graph permutation is not automatically an authorized quantum action. Preserving an operator does not guarantee preservation of history or the possibility of late intervention. For each comparison, the operation is fixed first: probability, conditional output, unknown output with external reference, or specified future questions.

In measurement-based quantum computation, subsequent questions may depend on prior answers. The general theory is established; the [foundational paper of Raussendorf and Briegel](https://arxiv.org/abs/quant-ph/0108118) defines the measurement-based computation model. DOT employs it as a test of addresses, counter-questions, and sufficient memory, without claiming this principle as its own new invention.

In the quantum example, the accessible ledger, already disclosed information, data deducible by law, and genuinely lost distinctions are distinguished separately. Every assertion concerning memory requires concrete access conditions and a class of authorized future questions.

A reduction in classical memory relative to designated future questions does not imply a reduction in the count of quantum actions. A code guarantee protects a declared error class, not arbitrary quantum noise or an erroneous prior measurement. Comparing utility requires a single library, identical access, and identical protected operations.

## E4 Central Sign and Complete History

The sign lift of an action may follow the law \(U_g U_h=(-1)^{c(g,h)}U_{gh}\). Changing representatives \(U_g\mapsto(-1)^{f(g)}U_g\) alters $c$ by a coboundary. Comparing classes requires a shared base, a reconciled group map, and such an explicit section alteration. A single central sign does not store the entire word of executed actions.

In a separate Pauli–Mermin construction, extensions linked to the groups $S_3$, $S_4$, $\mathrm{Dic}_3$, and the binary octahedral group $2O$ are considered. It is critical not to confuse group embedding, its action on labels, and the quotient map: these mappings possess distinct kernels.

The original Pauli sign on $C_2^4$ and $\kappa$ on $\mathrm{GL}(3,2)$ are not identified on their distinct bases. A global instantiation of $\kappa$ on a larger carrier is likewise not a renaming of the source Pauli sign. Full cohomological and normalizer constructions belong to the continuation in Volume II; here they certify the necessity of preserving law along with representation.

## E5 Status of the Cross-Domain Result

The general functioning of the language has been verified on specific models: state, question, action, provenance, memory, and continuation receive separate carriers and reconciled maps. The complete index of correspondences and source checks is preserved in the quantum compilation.

A universal metagrammar, the necessity of a single ladder of ranks, new quantum physics, historical priority, and practical superiority do not follow from these examples. The open task is to verify whether this same addressed language delivers new sufficient representations or useful transformations under honest comparison of identical problems.

## E6 Sanskrit: Cell Content and the Counter-Question

The locus of description is a local grammatical model in DM17, reconciled with DM16 and DM14. The frame $\Gamma$ fixes the right vowel environment, chosen rules, and application conditions; full derivation of a word is not included here. The carrier \(U=\{i,e,ai,u,o,au\}\) contains six named sounds, rather than six independent binary values.

The traditional table of place and aperture (document 52) provides for cell contents. In its coarse reading $P$, the sounds $i/e/ai$ receive one address, and $u/o/au$ another. The connectedness of the 18 occupied cells does not imply the sufficiency of a single address for grammar.

The cross-cutting reading $G$ distinguishes three grades: basic, guna, and vriddhi. The structural scalar of this restricted model is a sextet with two partitions: $P$ yields two triples, and $G$ yields three pairs. The joint reading $(P,G)$ is injective, since each class intersection contains a single sound. The family conjugation $i\leftrightarrow u$, $e\leftrightarrow o$, $ai\leftrightarrow au$ preserves $G$; it is a symmetry of the chosen table, not a universal rule of language.

In color addressing, one can assign $i/e/ai$ the labels 100/010/001 and $u/o/au$ 011/101/110. This is a chosen three-bit address, not a deduction of a natural linguistic rank. A prism arises from shared family or grade; an octahedron from another relation linking different grades. Six elements do not by themselves prove either of these graphs.

The local rule [Panini 6.1.77](https://www.bodharesearch.in/library/sections/ashtadhyayi/6.1.77) replaces vowels of the $ik$ class with corresponding semivowels before a vowel under authorized conditions. On $U$ it admits $i\to y$ and $u\to v$, but not $e\to y$. For $e$ a different route applies: [6.1.78](https://www.bodharesearch.in/library/sections/ashtadhyayi/6.1.78) yields $e\to ay$; on the selected sextet, the remaining substitutions are $ai\to\bar ay$, $o\to av$, and $au\to\bar av$. Exceptions, priorities, and subsequent rules must be verified in the full grammar separately.

An act here is a partial substitution $T$ on a sound with its environment. The interface defines which output and which applicability are protected. The observer is the role of selecting reading and task, not an extra sound in the table. The resulting $y/ay/\bar ay$ and $v/av/\bar av$ are sequences on the output carrier; they are not the prior cell addresses.

Two counter-flows are coupled by a single instantiation: $T$ transfers the input forward, and the output question $h$ returns as \(h\circ T\). The source of $h$ is the domain of output sequences. The third structure retains the same input, environment, rule, and applicability witness; without it, question composition could conflate distinct grammatical acts.

Therefore the equality $P(i)=P(e)$ does not permit executing $T$ on a single address: even the admissibility criterion for 6.1.77 differs. For this isolated rule, preserving family and $ik$-membership suffices; these are four input classes, rather than necessarily all six names. For the joint local substitutions 6.1.77–78, the reading $(P,G)$ retains all six distinct inputs and outputs.

Under reading $P$, the grade $G$ resides in the reverse side; under reading $G$, the family remains there. Memory means access to this distinction and environment prior to verifying continuation. It does not arise from renaming addresses. Even reverse assembly of the six local substitutions requires known output bounds and restricted initial $U$; the invertibility of the entire grammar is not established.

Verification question: from which output domain is $h$ specified, does it distinguish $y$ and $ay$, is the applicability of $T$ known, and where are grade and environment stored? The answer fixes the sufficiency of the current representation, rather than the "rank of Sanskrit in general."

Musical and Sanskrit analogies serve as motifs for the question of rule transfer, but do not by themselves establish a shared octahedron or path count. For example, 22 is not the edge count of a 5-cube. In every such juxtaposition, carrier, rule, and admissible reading are specified separately.

<a id="v1-colour-representations"></a>
## E7 Color Representations and Reconciliation of Questions

In this example, binary addresses, coordinate color values, finite frameworks, and questions regarding them are distinguished. Physical perception, white point, metric, and color gamut do not follow from address bits. Only the explicitly indicated mathematical instantiation is considered below, not a complete model of color vision or a universal transformation between color systems.

Begin with three named binary slots \((r,g,b)\). Their eight addresses correspond to chosen RGB vertices: 000 to black K, 111 to white W, single bits to R, G, B, and pairs to Y, M, C. The same addresses can be matched with the eight coefficient indices in P32. This is a correspondence of positions, not an equality of color, coefficient, and answer. The argument has address rank 3; a full rule on eight arguments has eight free coefficients and 256 instantiations. Its values are related to coefficients by the law \(h(x_T)=\bigoplus_{S\subseteq T}\theta_S\).

Even complementation belongs to different types. Index permutation \(S\leftrightarrow S^c\) maps position $r$ to $gb$. Argument inversion \(x\mapsto\mathbf1\oplus x\) transforms rule $r$ into \(1\oplus r\) and acts on coefficients as \((T\theta)_S=\bigoplus_{U\supseteq S}\theta_U\). A constant rule remains constant under argument replacement, but index complementation swaps the constant and triple slots. The label "RGB/CMY" is insufficient to determine the law.

On the full coordinate carrier \(X_{RGB}=[0,1]^3\), an ideal coordinate change \((C,M,Y)=\mathbf1-(R,G,B)\) preserves color: RGB red receives CMY coordinates \((0,1,1)\). The same formula as an action within RGB changes red to cyan. Real inks are not modeled here. The four names RGB, CMY, HSL, and Lab can be compared, but do not by themselves establish two independent binary distinctions or a shared square-edge law.

Partition the eight RGB vertices into \(T_+=\operatorname{conv}(R,G,B,W)\) and \(T_-=\operatorname{conv}(K,C,M,Y)\). These are two regular tetrahedra sharing the relative reference \(m_{RGB}=(1/2,1/2,1/2)\). Their joint convex hull is the cube, but the union of bodies does not fill the cube. Setting \(u=2v-\mathbf1\), joint sign inequalities yield \(|u_1|+|u_2|+|u_3|\le1\). Consequently, the intersection is a regular octahedron with vertices \(m_{RGB}\pm\tfrac12e_j\). The six source RGB/CMY colors possess only coordinates 0 and 1; their hull is another, metrically non-regular octahedron with edges of lengths 1 and $\sqrt2$. Selecting active vertices and intersecting prior wholes are distinct constructions. Hamming-distance adjacency described in P35 is also chosen separately.

The linear decomposition of full color is

\[
t(v)=\frac{r+g+b}{3},\qquad p(v)=v-t(v)\mathbf1,
\qquad v=p(v)+t(v)\mathbf1.
\]

The representation \((p,t)\) is complete; $p$ alone conceals the common achromatic component. On the binary octet, six colors map to a regular hexagon, and K and W to a single center. The source triples have $t=1/3$ and $t=2/3$, and do not lie in a single plane. The seven visible loci can be termed "six plus a folded polar pair," provided the center stores its unfolding address. A question descends through $p$ precisely when \(h(K)=h(W)\). On the continuous cube, the entire gray axis maps to the center: recovery requires the coordinate $t$, not a single hidden bit. Gluing K to W is incompatible with XOR; hence this septet is not a Fano plane.

Lab features three coordinates \(L^*, a^*, b^*\), defined via XYZ relative to a specified white stimulus. The chosen axial frame

\[
(L_0,\pm a_0,0),\quad(L_0,0,\pm b_0),\quad
(L_0\pm\ell,0,0)
\]

contains four chromatic plane directions and two lightness poles. For \(L_0=\ell=a_0=b_0=50\), it forms a regular octahedron in the chosen Euclidean coordinate metric. Membership of the four chromatic points in a concrete gamut is not established. The count $4+2$ enumerates poles; the four planar directions are not four independent dimensions, and the lightness pair does not in itself define counter-flows. Polar LCh representation is given by \(C^*=\sqrt{a^2+b^2}\), \(h=\operatorname{atan2}(b,a)\), \(a=C^*\cos h\), \(b=C^*\sin h\). At \(C^*=0\), the angle does not distinguish color. The quarter-turn \(J(a,b)=(-b,a)\) realizes \(J^2=-I\) on the equipped plane, but its admissibility on a bounded gamut requires verification.

HSL employs periodic hue $H$, saturation $S$, and lightness $L$, constructed from encoded sRGB coordinates. The six chosen RGB/CMY hues have angles \(0,60,120,180,240,300\) degrees at \(S=1, L=1/2\); black and white have \(L=0,1\). This is an 8-point frame \(6+2\), not the entire model and not eight coordinates. At zero saturation, hue is inactive. Placing the sextet on the equator and the two limits at the poles produces a hexagonal bipyramid with 18 edges instead of the 12 edges of the RGB cube: preserving reference names does not preserve adjacency. Nor does HSL coincide with the orthogonal projection $p$. For example, in the sector \(R\ge G\ge B\) with \(R>B\) and \(\tau=(G-B)/(R-B)\), the HSL hue angle is \(60^\circ\tau\), whereas the linear color plane angle is \(\operatorname{atan2}(\sqrt3\tau,2-\tau)\); at \(\tau=1/3\), they differ.

The divergence of actions emerges outside the small framework. The RGB complement \(D(v)=\mathbf1-v\) transfers as

\[
D_{HSL}(H,S,L)=(H+180^\circ,S,1-L),
\]

whereas a half-turn of hue alone takes the form

\[
P_{HSL}(H,S,L)=(H+180^\circ,S,L),\qquad
P_{RGB}(v)=(\max v+\min v)\mathbf1-v.
\]

Hue is read modulo a full turn; on gray it does not distinguish color. The actions coincide precisely when \(L=1/2\), in particular on the source sextet. Thus this finite sample conceals the divergence of their laws. The common cycle $C_{12}$ for four and six directions from D1 likewise does not prove conjugation of the real nonlinear RGB$\to$Lab map with these rotations.

For an actual transition \(F:X_{RGB}\to X_{Lab}\), encoding, XYZ matrix, white reference, and, under reference change, chromatic adaptation are fixed. Without clipping on an invertible domain, color may be preserved, but not Euclidean distance or geometric midpoint. Encoded sRGB gray \((1/2,1/2,1/2)\) under the reconciled route has \(L^*\approx53.389\), not 50; this number does not pertain to the midpoint of linear RGB. The metacentre serves as a relative reference of a designated presentation, not an unvarying shared coordinate point across all models.

The question \(q_{Lab}(y)=[L^*(y)>50]\) pulls back to RGB as \(q_{Lab}\circ F\), preserving its original domain, threshold, and frame. It is not equal to the question \([L_{HSL}>1/2]\): on mid-gray, the first answer is true, and the second false. The forward flow transfers color; the counter-flow transfers the question; and the joint instantiation certifies

\[
\operatorname{ev}(F(x),q)=\operatorname{ev}(x,q\circ F).
\]

Reverse color reconstruction, counter-transfer of a question, and preservation of history are distinct operations. Equality of answers does not automatically recover the original gray hue, source address, or right of a new action. The next subject test must transfer concrete actions and a question family, and then verify their descent under chosen reductions.

Finally, the six shortest paths from 000 to 111, specified by the order of three switches, form a cycle $C_6$ under adjacent transposition. Their reverse paths yield a directionally counter-family with shared endpoints, but a vertex here is an entire path, not an individual color. Two path orientations do not replace the transfer \(q\circ F\). Checks of all 256 rules, graphs, and paths, exact formulas, and numerical Lab examples reside in the color verification program; the full XYZ route with adaptation and Lab-frame gamut coverage are not yet verified by that script. These limitations remain subject continuations, rather than unconditioned primitives of the first volume.

<a id="v1-appendix-F"></a>

# Appendix F Source, Cost, and Continuation of Computation

This appendix examines a verified computational route as a composite whole. Its parts are bound together by provenance, admissibility conditions, and the capacity to unfold the result. Memory, sufficiency, and cost authenticate concrete transitions; they do not replace the subject matter with the count of fields in a record.

The locus of description is the execution frame over already specified actions. The primary domains are DM15 and DM16. The index of sources is a structural whole via the correspondence "source result — new locus — verified preservation." Its length is not declared a binary rank.

## F.1 What a Computational Route Preserves

For an individual act, the following are necessary: the source whole, genuinely accessible grounds, the question with its projecting domain, the chosen admissible action, the event, and the subsequent frame. Connections are verified together: the action answers the given question; the source belongs to the given whole; the event authenticates this instantiation; the frame permits continuation.

Two reconciled pointers pertain to the same event. The forward pointer unfolds the source state and the actual result. The counter-pointer unfolds the future question, its original reading and rule, then their transfer to the source argument via \(q\circ T\). The third structure is the admissible joint instantiation, rather than the numerical coincidence of answer values. A reconstructive unfolding of an old record is not termed a counter-question without this composition map.

A chosen question has the structure \(q=h\circ m\), where \(m:S\to B\). Under transfer, the source $B$, the rule family $\Omega(B)$, the chosen $h$, and the frame are preserved. If the question is expressed through another current access, a witness to that expression is appended without replacing the prior source.

The verification mechanism must reject an alien parent, duplicate child sides, an alien source, a substituted stage, and unauthorized expenditure of the shared reserve. Arithmetic equality alone does not authenticate any of these conditions.

## F.2 Exact Arithmetical Test

For positive integers $A, B$, \(N=AB\), and an integer operand \(r\ge0\), child readings \(d_A=\gcd(A,r)\) and \(d_B=\gcd(B,r)\) are defined. The full assembly takes the form

\[
D=\operatorname{lcm}(d_A,d_B),\qquad
C=\gcd(N/D,r/D),\qquad
d=DC.
\]

When the parts are coprime, $C=1$, but under overlap this condition cannot be substituted in advance. On \(25=5\cdot5\), identical child answers admit parental answers 5 and 25. The required supplement pertains to shared multiplicity.

For \(N=45\), consider a concrete chain. A trial with $r=3$ yields \(\gcd(45,3)=3\). Saturation \(x\mapsto\gcd(45,x^2)\) transforms 3 to 9. The partition \(45=9\cdot5\) and transfer of the same operand yield child answers 3 and 1. Their assembly restores the parental answer 3. Each step preserves the shared source and the posed question.

This is a specific route, not a general factor-search algorithm. A partition is admissible when its ground is genuinely obtained and paid for within the declared frame. The parent, its facts, and the source question remain accessible. For complete prime factorisation, the primality of all leaves must be proved; exhausting the menu or budget does not establish this. Transfer across multiple partitions requires separate preservation of source and question at each step.

Reading a stored parental answer and computing the general correction are different modes of obtaining a result. The first preserves the source; the second pays for a new reconstruction. Neither converts prior known information into a new unknown factor.

Saturation is an autonomous action. It retains the support of an already known divisor with full multiplicities; ordinary closure under GCD, LCM, and complementation may fail to produce the same block. Reaching all of $N$ does not certify primality, nor does it create a proper two-part cut.

Obtaining child answers and verifying their consistency with the parental question are distinct phases. The arithmetic assembly formula pertains to explicitly given answers; it does not confirm that those answers were obtained by authorized actions.

For a finite non-empty family of positive parts \(N=\prod_i A_i\), the numerical reconstruction of the product and the reconstruction of a shared GCD answer remain different laws. Suppose only $A_i$ and \(d_i=\gcd(A_i,r)\) are retained, while the shared integer operand is forgotten. Define

\[
D=\operatorname{lcm}(d_i),\qquad
K=\frac{N}{\operatorname{lcm}(A_i)},\qquad
T=\prod_i\frac{A_i}{d_i},\qquad
H=\frac{K}{S_K(\gcd(K,T))}.
\]

Here $S_K(z)$ is the maximal divisor of $K$ with prime support contained in $z$; it is obtained by saturating the support via GCD. Numerical compatibility requires \(\gcd(A_i,D)=d_i\) for all $i$. Under these conditions, the possible parental answers constitute precisely \(\{DC:C\mid H\}\) over the domain of all integer operands consistent with the retained answers. If at least one part is not saturated by its answer in a prime direction, its exponent fixes the operand's exponent; saturation removes this freedom from $K$. If all parts are saturated, there remains the range from the maximum part exponent to their sum. Each admissible answer is realized by choosing \(r=DC\). Thus the numerical reverse side of the reduced reading is unfolded, not a new independent source.

Additional data concerning a specific inquiry, its stage, or admissible operands may narrow this family. Numerical compatibility likewise does not authenticate a shared paid source. A full history containing the prior answer does not acquire the ambiguity of a reduced reading limited to leaves. On four parts 3 of the number 81, identical answers 3 yield \(D=3, H=27\), meaning possible answers 3, 9, 27, 81; the product of the four answers does not restore the prior answer 3.

Power compression of groups \((a_j,m_j,d_j)\) preserves

\[
N=\prod_j a_j^{m_j},\qquad K=N/\operatorname{lcm}(a_j),\qquad
D=\operatorname{lcm}(d_j),\qquad
H=K/S_K\!\left(\gcd\!\left(K,\prod_j a_j/d_j\right)\right).
\]

Repeated powers inside the final saturation can be dropped, since for \(m_j\ge1\) they share the same prime support. Multiplicities remain in $N$ and $K$. Four readings \(\gcd(3,r)\) are not replaced by a single \(\gcd(3^4,r)\): the latter preserves more distinctions of exponent. When questions or answers differ across numerically equal parts, they must not be tacitly merged into a single group.

A power-type notation can preserve base and multiplicity, but is not obliged to preserve the addresses of individual participants, questions, and history. If these distinctions matter for the subsequent action, they are retained separately. A mathematically deducible correction and an authorized program command likewise remain distinct entities.

## F.3 Cost and the Right of Continuation

The computational frame restricts more than the operation count. It defines authorized sources, objective, tariff, memory bounds, and termination conditions. The contents of a preserved record, an executed reading, and an accessible fact play distinct roles.

Under a single selected tariff, the overall upper reconstruction is assessed at seven arithmetic operations. Preparation, addressing, provenance verification, and actual memory bytes are not fully included in this estimate. Therefore the absence of a new arithmetic evaluation during a reread does not imply zero total cost.

The upper assembly is verified jointly with the lower tree. Following its execution, the lower process does not resume automatically: first a new frame is negotiated taking into account the already consumed resource. In the model under consideration, the local bound is specified as

\[
\text{local.max\_work}=\text{local.spent}+\text{global.remaining}.
\]

The sequence of frame and action changes must be preserved: a single terminal limit value does not authenticate the entire route. Accessibility of data, determinacy of the answer, admission, and actual execution remain distinct coordinates.

The method does not select a trial based on its precomputed unknown answer. Prior to selection, only genuinely accessible grounds and proved prediction of the law are permitted. A proper saturated partition allows predicting a unit correction for a future scalar GCD; it does not predict the operand and answer of a future trial.

These constraints pertain to a concrete execution. Their presence does not prove the impossibility of other algorithms. Verifying methodology and proving computational advantage remain distinct tasks.
