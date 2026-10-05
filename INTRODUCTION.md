# Introduction

> **Русская версия:** [ru/INTRODUCTION.md](ru/INTRODUCTION.md) | **Volume I:** [VOLUME_I.md](VOLUME_I.md) | **Glossary:** [GLOSSARY.md](GLOSSARY.md)

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

The *metacenter* designates the role of a balancing fulcrum relative to which distinct presentations are correlated. It is not obliged to be a geometric center, a numerical zero, or a isolated point. To speak of a concrete metacenter, a model must specify what performs this role and under what rule. Zero, a center of symmetry, and the complex imaginary unit are therefore never conflated merely on the basis of resemblance in naming or position.

## Trajectory of the Book

First, a minimal finite model is introduced: two positions, possible states, and the reading of their distinction. On this model, the source state, question, action, and answer are disentangled. Next, we verify what auxiliary data are required for inverse assembly and continuation of action. Subsequently, the questions themselves become objects of analysis; relations among them are constructed, along with their graph-theoretic and geometric presentations.

Subsequent chapters examine transfers between domains, arithmetical and phase models, composite actions, and execution history. The appendices assemble finite tables, proofs, and verification routines. In transitions between domains, what is being compared is stated explicitly every time: not merely two similar-looking graphs or two equal scalar quantities, but elements of specified carriers and concrete mappings between them.

The first volume offers verifiable constructions within the enumerated models. It does not claim that all mathematical structures have already been unified into a single hierarchy, that every transition is universally necessary, or that a new foundation of physics has been discovered. Conditions of generality and potential practical utility demand independent proofs and comparative evaluations.

Therefore, it is beneficial to read each proposition through four guiding questions: **in which carrier is it formulated? which reading is chosen? what does the transition preserve? what remains unknown or demands a separate witness?** These questions define the operative methodology of the volume.
