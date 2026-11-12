# Introduction to the Book. From the Mathematical Object to Distinction and the Observer's Position

> *Neti, neti* — not this, not this.
>
> — Yājñavalkya, *Bṛhadāraṇyaka Upaniṣad* (2.3.6)

Place a sphere, a cylinder, and a cone of the same diameter behind a screen and look at them from above. You will see three identical circles. Nothing in the objects themselves has changed—what has changed is only which question you are permitted to ask them. This book begins with precisely that question: what must be given to an observer in order to distinguish one thing from another at all, and not confuse them at the next step?

Below we walk through three entry points into mathematics—through a ready-made object, through a frame of reference, and through the conditions of distinction—and show why the third entry point leads to its own ladder of mathematical languages. This essay opens the entire three-volume corpus of **Distinction Observable Theory (DOT)** and precedes the first formal theorem: using examples and engineering diagrams, it explains *why* such a shift of perspective is needed and which habitual conflations of concepts it untangles.

This Introduction defines the scope of questions and the direction of reading, but in no line does it substitute for rigorous proofs. Throughout all subsequent chapters of the book, four levels of statement are distinguished: **definition** (how the introduced concept is constructed), **adopted condition** (under what explicitly stated rules the scene is considered), **proved consequence** (what necessarily follows from the premises, accompanied for claimed necessary conditions by an explicit finite counterexample showing how dropping that condition alters the conclusion), and **accompanying historical-philosophical parallel** (which helps reveal the affinity of questions across different eras, but never enters the premises of any mathematical deduction).

---

## Part I. Three Entry Points into Mathematics: Ready-Made Object, Frame of Reference, and Conditions of Distinction

### 1. The Familiar Entry Point: Mathematics of a Ready-Made Object

Open almost any classical textbook on algebra, geometry, or analysis, and you will encounter the same established way of posing a problem. The opening sentence immediately places an **already singled-out object** on the table: *"Let a set of points be given…,"* *"Let a group of transformations be specified…,"* *"Consider a smooth space and a function on it…"*

From the moment the object is declared, the researcher's task is clear: determine its internal properties, find its symmetries, classify admissible operations, and establish what remains invariant under transformations. Meanwhile, the question of **how this object was singled out from the background, relative to what reference its features were noticed, and what trace must be retained so as not to confuse it at the next step** remains outside the problem statement. To prove a theorem about a finite group or a right triangle, a mathematician does not need to describe the anatomy of their own eye, the lighting of the room, or a logbook of laboratory measurements.

In this bracketing-out of the circumstances of observation lies the immense liberating power of the classical object-centered approach. By abstracting away from the contingencies of who first noticed a structure and how, mathematics makes its conclusions portable: a proved theorem holds for every object of the declared class and is verifiable by any reader. Note immediately that the word "object" in this approach does not mean an immobile stone—the subject of study may equally well be a process, a wave, an algorithm, a relation, or an entire category. What is at issue is specifically the **order in which the question is posed**: the object and its elements are treated as already distinguished before the first line of reasoning begins.

Yet what happens when the very possibility of singling out an object, not losing it under a change of viewpoint, and relying on it in the next action ceases to be self-evident?

---

### 2. The Second Entry Point: Frame of Reference, Multi-View Projection Drawing, and Dependence on the Medium of Description

Let us take one step back from the "object in itself" to the **manner of its presentation**—a step familiar to every engineer, surveyor, and cartographer.

Imagine a drafting table and three idealized solids of revolution behind a screen: a **sphere**, a **right circular cylinder**, and a **right circular cone** of common diameter $D$, placed upright so that the axes of the cylinder and cone point strictly along the line of sight of an overhead window. Suppose only a single viewing window from above at a known scale—the plan view—is open to us. In all three cases we will see in that window **one and the same circle of diameter $D$**.

```text
   Diagram 1 (Illustrative mini-scene of projective reading, not a state-transition graph):
   Three distinct solids of common diameter D read from above and upon adding a shared side view

        Hidden solids               Window 1: top view only         Window 2: orthogonal side view
   ┌─────────────────────┐        ┌─────────────────────────┐     ┌──────────────────────────────┐
   │  1) Sphere (diam D) │ ─────► │          ( ○ )          │     │    ( ○ )   +     ( ○ )       │
   │  2) Cylinder (upr.) │ ─────► │          ( ○ )          │     │    ( ○ )   +     [ ▭ ]       │
   │  3) Cone (upright)  │ ─────► │          ( ○ )          │     │    ( ○ )   +     / △ \       │
   └─────────────────────┘        └─────────────────────────┘     └──────────────────────────────┘
                                   In the first window all three   A shared side view across the axis
                                   yield the same circle of diam D separates all three classes of solids
```

**Reader's caption to `Diagram 1`:** the three solids on the left represent three test specimens of common diameter $D$; Window 1 reads the orthogonal plan along the vertical axis, while Window 2 adds a shared side view perpendicular to the vertical axis of the cylinder and cone; the arrows denote the operation of reading a silhouette, not a physical transformation of a spatial solid into a flat figure.

Before us is a simple yet instructive situation. Nobody altered the solids themselves, and nobody violated the laws of logic. Yet the sufficiency of the window depends entirely on what question and what subsequent action we pose:
- suppose a horizontal circular ring of inner diameter $D_{\text{ring}}$ is placed beneath the solid with no obstacles below it, and the part is lowered strictly vertically along the window axis without tilting (leaving the boundary case of exact contact $D_{\text{ring}} = D$ to a separate clearance convention). Then for $D_{\text{ring}} > D$ each of the three solids will pass through the ring, while for $D_{\text{ring}} < D$ none of the three will pass—**together with the specified scale and these stated conditions, a single top view is completely sufficient**;
- however, if we are required to distinguish the three shape classes themselves, the top circle alone no longer suffices: as soon as we open a second, **shared side view perpendicular to the vertical axis**, the silhouette splits into a circle, a rectangle, and an isosceles triangle. The same difference is vividly illustrated by an idealized mechanical model in which the part is tipped by `90°` onto its lateral surface on a rigid horizontal plane and rolls without slipping under a small push: the sphere rolls in the chosen direction, the cylinder rolls straight across its generator, and the cone traces an arc around its fixed apex. Three objects that coincided in the first reading window diverge under a change of viewpoint and testing regime.

In exactly the same way, **choosing a frame of reference and a standard unit** operates in surveying and everyday measurement. When an ancient surveyor stretched a rope with twelve equidistant knots into a triangle with sides `3`, `4`, and `5`, two distinct tasks were combined: *laying off the chosen unit along the ground* (which depends on which rope was adopted as the unit of measurement) and *the stable ratio of sides*, which yields a right angle regardless of step length. If we shift the zero point of a thermometer or an altitude scale, the numerical readings of all points shift, yet their mutual differences are preserved—under one indispensable condition: we must remember **relative to which zero and which unit** each number was recorded. If readings in degrees Celsius and Fahrenheit are dumped into a single table with the scale labels erased, the accurately recorded numbers lose their meaning.

> **Historical excursus: how twentieth-century mathematics brought dependence on medium and viewpoint inside the formalism** *(the survey box below may be skipped on a first reading by proceeding directly to `§3`)*
>
> In the twentieth century, pure mathematics itself—long before any discussion of DOT and not at all for the sake of "psychology of consciousness"—discovered rigorous ways to incorporate dependence on the ambient medium and viewpoint directly into the mathematical apparatus. Let us name the principal interlocutors along this path while immediately drawing clear boundaries:
>
> 1. **The intuitionistic gesture of L. E. J. Brouwer (`1948–1949`).** Brouwer observed that even natural counting rests on an earlier event—the splitting of a lived moment into a retained trace of the past and a new "now" (*two-ity*). He refused to treat infinite totalities as ready-made prior to an act of construction. In Brouwer, however, the source of construction was the internal flow of time of an individual subject, whereas we require a language of verifiable relations and protocols that does not depend on the introspection of an individual person.
> 2. **Arrows instead of isolated things (S. Eilenberg and S. Mac Lane, `1945`) and the gluing of local views (A. Grothendieck, M. Artin, and J.-L. Verdier, *SGA 4*, `1963–1973`).** Category theory showed that a mathematical object is recognized not by the "internal substance of its points," but by the admissible maps (arrows) relating it to other objects and how those arrows compose. In algebraic geometry, Grothendieck's school went further: instead of a single all-seeing survey of a space, the foreground was taken by a system of local patches, rules for restricting data to smaller regions, and conditions under which pieces agreeing on overlaps glue into a coherent whole (*sheaves* and *topoi*). Grothendieck was solving geometric and cohomological problems rather than building a theory of the observer—yet he created a precise language of local presentations and compatibility checks.
> 3. **The medium of description as a subject of logic (F. W. Lawvere and M. Tierney) and the local mathematics of John Lane Bell (`1986–1988`).** Lawvere and Tierney discovered that passing to the study of all objects *relative to a chosen base* (a slice category over a base) changes perspective in a completely rigorous way: a variable quantity depending on a base parameter behaves inside the new medium as a single unified object, and the medium itself determines the internal logic of admissible judgments. J. L. Bell showed that mathematics can operate across many local "universes"—topoi—rather than a single absolute one. DOT accepts this lesson, but asks a question one step earlier: who chooses *which* of them to work in, and by what rule? Choosing a medium of description is already an act of distinction, and we will record its conditions explicitly.
>
> > **For the specialist: namesakes J. L. Bell and J. S. Bell, and local topoi.** The Canadian logician and philosopher of mathematics **John Lane Bell** is **not** **John Stewart Bell**, the author of the correlation inequalities we will meet in Book II. On the basis of topos theory, J. L. Bell formulated a clear picture of **local mathematics**: instead of a single "absolute universe of sets," a mathematician works across a multitude of local frameworks, and when translating a statement from one framework to another one must carefully check which part of the logic is preserved and which is lost.  
> > At the same time, choosing a ready-made topos in J. L. Bell is not yet the *act of distinction* itself: the ambient medium there is already given as a whole. To outline the direction of our comparison right away (without attributing any specific numerical threshold to Bell's own texts and without contesting topos theory), let us note two distinctions on our own simple models: first, in our illustrative threshold model of proximity on a ruler (where marks within `1` cm are called "close"), the point `0` is close to `0.6` cm, `0.6` cm is close to `1.2` cm, yet the outer marks `0` and `1.2` cm are **not** close to each other—approximate threshold proximity is non-transitive, whereas an exact question always cuts its domain into disjoint classes without模糊 edges (all of **Book I** is built from such exact cuts, while continuous tolerances and smooth infinitesimals are introduced separately and explicitly only in **Book II**); second, the geometric inclusion of a piece inside a single object must not be confused with the combination of two subsystems in which their possible states multiply or couple across a shared regime (two two-way toggle switches on a panel yield `2 × 2 = 4` combined positions, not a simple sum of pieces).
>
> 4. **Observing systems (H. von Foerster, `1976–1979`), the view from within a model (O. E. Rössler, `1994–1998`), and the mark of distinction (G. Spencer-Brown, `1969`).** Beyond pure geometry, second-order cybernetics and the calculus of indications raised the question of the very act of drawing a boundary. Von Foerster proposed viewing stable objects as repeatable eigenstates of a recursive coordination loop, while Rössler in his *endophysics* program contrasted the complete external description of a model world with the interface accessible to a subsystem living inside that world. Finally, George Spencer-Brown in *Laws of Form* began directly with the injunction "draw a distinction" and a single unindexed corner-mark that simultaneously denotes *naming the marked side* and *crossing the boundary*.  
>    Why not stop at one of these three schemes? Tiny examples immediately reveal three precise obstacles:
>    - *Stability need not be a frozen point:* if a metronome ticks steadily "left — right — left — right," the switching step on the two extreme positions has **no fixed point at all**, yet the switching rhythm itself is completely stable and perfectly observable. Thus the stability of a scene rests not on a frozen state, but on preserving the rules of reading and transition.
>    - *The view from within a model starts too late for our purpose:* to single out an observer as a subsystem inside a model world, that world with its states and laws must already be constructed in advance; we are interested in an earlier question—how the sides and the conditions of their distinction are introduced in the first place.
>    - *The operation of reading must not be fused into a single symbol with the operation of switching:* look at an ordinary wall light switch. If you **look twice in a row** at the switch without touching it (`repeated reading`), you receive the same answer "on" twice, and the lamp does not even flicker. But if you **press the switch twice** (`repeated transition action`), the light in the room actually turns off and turns back on. In an address-free calculus of a single mark, naming and crossing the boundary are fused into one symbol; in DOT, reading an answer and taking an actual step across states have distinct types and are never conflated.

---

### 3. The Third Entry Point—the Turn of DOT: From the Conditions of Distinction and the Observer's Position to the Ladder of Mathematical Languages

Let us now compare all three perspectives on a single simple diagram:

```text
   Diagram 2 (Conceptual map of the three entry points into mathematical description, not a state graph):

   [1. FROM READY-MADE OBJECT]       [2. FROM FRAME & MEDIUM]            [3. FROM DISTINCTION & OBSERVER (DOT)]
   The object and its elements       The object is given through a       The initial question is posed earlier:
   are treated as already singled    chosen viewpoint, standard,         under what conditions is it possible
   out before the problem begins.    projection, or local medium.        to draw a distinction, retain its trace,
   Question: "What are the           Question: "How does the record      and legitimately take the next step?
   properties of this structure?"    transform under change of base?"    How do the languages of description
                                                                         grow step by step from these conditions?
```

**Reader's caption to `Diagram 2`:** the three columns compare three levels of posing the initial question in mathematics, not three states of any system and not three sequential steps in time.

These three entry points **do not cancel or destroy one another**. Distinction Observable Theory uses the full rigor of ordinary mathematical proof and does not declare classical mathematics "wrong." Its own design is different: **to place at the very beginning neither a ready-made thing nor even a ready-made coordinate grid, but the minimal conditions under which an act of distinguishing two interacting sides is possible at all, leaves a retainable trace, and allows work to continue**.

As soon as we start from this point and forbid ourselves from smuggling ready-made numbers, coordinate axes, or a continuous space into the problem, the central theme of the book opens up. DOT does not attempt to "deduce all theorems of world mathematics out of nothing." **As the questions grow more complex, we will derive which structures are sufficient for the chosen tasks and which additional operational requirements make a given mathematical language necessary; where multiple formal realizations are possible for a single task, we will exhibit them and their equivalence conditions explicitly:**

1. As long as there is only **a single two-sided cut** ("this way" or "that way" by an explicit test rule), there is not yet a zero, a one, or addition—to hold the boundary itself, a **partition of the domain into two non-empty classes**, invariant under relabeling of the two tags, is sufficient.
2. When **two independent two-sided questions** (for instance, about a specimen and a reference comparison regime) are addressed to the same scene and their joint completeness is required, a **four-state polar cell** is born, together with a derived question of agreement or disagreement between the sides and a law of **invertible recovery** of one side from the comparison result and the retained reference.
3. When a single reading is followed by a **chain of admissible actions** (some of which may be blocked in a given position), the task of not losing future answers leads to **partial transitions, minimal sufficient memory, and the behavioral quotient system** *(while a partial transition can equivalently be written as a total map if an absorbing rejection state is explicitly adjoined—the choice between these representations is governed by the adopted typing contract)*.
4. When **mutual cancellation of opposite contributions** must be accounted for, idempotent Boolean union ("or") no longer suffices: it cannot cancel opposites, so **sign and additive balance** are introduced *(for cyclic cancellation modulo `3`, $\mathbb{Z}_3 = \{-1, 0, +1\}$ suffices, and for projective rays in Chapter `I.6`, the finite field $\mathbb{F}_3$; however, when signed contributions must be summed across an arbitrary finite number of places without cyclic wrap-around $1 + 1 \equiv -1$ and without imposing extraneous relations between places, the universal choice in Chapter `I.5` is the free abelian group $\mathbb{Z}[X]$ over the ring of integers $\mathbb{Z}$)*.
5. When the admissible questions themselves and the ways of gluing them are investigated on finite carriers under explicitly stated symmetry and incidence conditions, the finite architecture of **Book I** unfolds: **graphs under different edge predicates on the same vertices, the six-vertex octahedron of balanced questions of the four-state scene, the seven-point Fano plane, finite fields, divisor lattices, modular residue arithmetic, and the cohomological gluing obstruction**—entirely without relying on the real line.
6. Finally, when the hidden part of the state returns to the visible window with a delay, and additional requirements of continuous continuation and local phase gluing are imposed between discrete ticks, **Book II** introduces—with a complete list of new axioms—**linear memory spaces, real numbers, quarter-turn operators, cochains and holonomy on graphs, nonassociative sign tables, and quantum measurement instruments**.

Before crossing the threshold of Chapter I.1 and writing down the first formal definition, let us learn to see the anatomy of the act of distinction itself and the place of the observer within it—directly through living examples of ordinary experience.

---

## Part II. Anatomy of Distinction and the Place of the Observer: Four Illustrative Scenes

### 1. You Are Already Inside Distinction—and Where the Boundary of Formalization Lies

Let us begin without mysticism from what is happening at this very second. You are reading this line. That means distinction is already in full swing: the dark contour of each letter is separated from the light field of the page, one word is separated from its neighbor, and the meaning of the phrase just read is compared with the preceding one. We do not need to invent an artificial world "prior to all experience" in order to meet distinction—we use it continuously, like breathing.

When discussing the observer, two meanings must be kept distinct. Whenever the words "observer" or "consciousness" are spoken in conversation, two completely different things are easily lumped together. Let us separate them at the threshold and never conflate them again:

- **First—living subjective experience (*qualia*) and the inner experience of a subject:** *what it is like from within* to see a saturated red color, taste water, or feel pain. Many people experience a certain continuity of their inner perspective across age-related changes of body, habits, knowledge, and worldview. **However, subjective experience and its philosophical interpretations are not proved by the examples of this book: DOT in principle does NOT turn this side into a mathematical object and does not place it inside its mathematical core.** Any attempt to declare a formula on paper to be "the feeling of red itself" would be a substitution of the subject matter.
- **Second—the working structural instrument of distinction, correlation, and trace retention:** that by virtue of which we parse a signal: **distinguish** one letter from another, **compare** a part against a standard, **notice** a change of regime, and **retain** the outcome in memory for the next step. An operational apparatus consisting of relations, access boundaries, actions, and memory admits mathematical formalization and constitutes the subject of DOT.

The easiest way to see how available distinctions depend on the mode of reading is through a brief everyday scene involving one and the same signal.

---

### 2. Scene One: One and the Same Film Recording Before Two Viewers

Imagine two viewers sitting side by side before the same screen, watching under identical image and sound conditions the same recording of an intense conversation in a rare language: the first viewer speaks the language fluently, while the second knows not a single word of it.

Let us examine what they strictly share and where the divide lies:
- the light and sound stream is **one and the same**: the screen glows identically, and the speakers send the exact same acoustic wave into the room;
- the second viewer is neither blind nor deaf: they clearly distinguish the actors' faces and gestures, pauses, rises and falls of intonation, and even recurring proper names;
- yet **the lexical-semantic channel of distinguishing utterances is closed to them**: two sentences of opposite meaning in the unfamiliar language merge under that question into an indistinguishable speech stream, whereas for the first viewer in the very same recording they are sharply separated.

This scene immediately frees us from the habit of thinking that all distinctions reside in things like ready-made stickers independent of the testing protocol. The set of accessible distinctions is determined by the encounter of the tested stream with the chosen question and the configured mode of reading.

---

### 3. Scene Two: Room, Camera, and Mirror—Separating the Role of the Observer from Instrument States

As soon as the word "observer" is uttered, a natural question arises: how does the operation of observation itself relate to the physical device of the instrument, which after all can also be seen in a mirror or included in a model? To prevent **role confusion** (without declaring self-representation impossible), let us consider an example with a camera and a mirror.

Take an ordinary photograph of a room. The photograph shows a desk, a window, and a section of wall. The camera itself is not in the picture—and yet the method of photography participates in organizing the frame: it sets the viewpoint, perspective, and boundaries of what falls inside the rectangle of the photograph versus what remains outside its edges (for example, a desk lamp behind the photographer's back is not visible in the frame, even though the desk is lit by its light).

Now place a **mirror** on the desk in the room so that the camera on its tripod is reflected in it, and take a new photograph (or photograph yourself in the mirror). The mirror and the self-portrait vividly show that **partial self-representation is entirely possible**—and in exactly the same way, in a finite mathematical model of four states $X = \{(d, m) \mid d, m \in \{0, 1\}\}$, an instrument can have an internal cell of its own memory $m$, read it via the question $q(d, m) = m$, and toggle it via the step $T(d, m) = (d, 1 - m)$.

```text
   Diagram 3 (Illustrative mini-scene "Room, active shooting position, and mirror", not a state graph):

      Role of conducting the shot in contract (O)     Resulting frame (domain X of current photograph)
     ┌────────────────────────────────┐            ┌─────────────────────────────────────────────┐
     │  Rule of viewpoint, exposure,  │  shooting  │  Desk, window, wall                         │
     │  frame bounds, and protocol    │ ─────────► │     ┌───────────────────────────────┐       │
     │  for comparing photographs     │            │     │ Mirror on desk:               │       │
     └────────────────────────────────┘            │     │   [image of camera body]      │       │
        ▲                                          │     └───────────────────────────────┘       │
        │ Distinguished by role in contract        └─────────────────────────────────────────────┘
        └─ from an image detail inside X             The camera reflected in the mirror belongs to X,
                                                     but is not identical to the whole operation of obtaining X
```

**Reader's caption to `Diagram 3`:** the horizontal arrow denotes the operation of obtaining a photograph according to the chosen shooting rule, while the return note emphasizes the distinction in role between the overall operation of specifying the experiment and a depicted detail inside the frame.

Let us look closely at what this comparison shows:
- the camera reflected in the mirror (or the memory bit $m$ inside the state $(d, m)$) is **an element or component of the carrier $X$ under consideration**; if you cover the mirror with your palm on the printed photograph, the rest of the room picture does not vanish;
- whereas the organization of the experiment itself—the choice of question, admissible steps, and before/after comparison—operates in a different role. If a second photographer stands in the doorway and photographs the entire room from the side together with the first camera and its internal components, the former instrument will enter the extended model $X'$ in its entirety, but now within the framework of a **new, extended observation contract**.

The same shift of role is easy to notice across three beats of ordinary reasoning:
1. You look at a desk and distinguish it from the floor—the subject under consideration is *the desk*.
2. You turn the question toward *your own previous judgment about the desk*—now that judgment is included in the domain under consideration, but is held by the next working question.
3. As soon as you make this second step the subject of analysis as well, it too passes into the body of discussed data within a wider frame.

Therefore, in our operational contract we adopt a clear typing rule: **we distinguish the role of holding the question and protocol from the states themselves that are examined within that contract**. The notation $\mathcal{O} \notin X$ in the chapters of this book records **precisely this chosen boundary of our model** (and not a universal empirical ban on all self-representation): an image of a camera or a memory state of an instrument may belong to $X$, but it is not identified in type with the entire operation by which the contract is specified and verified; and in another, extended model $X'$, one can explicitly observe the internal states of the former instrument as well.

To prevent confusion around the everyday words **"center"** and **"external"** when reading the mathematical chapters, let us immediately separate their meanings:

- **Three distinct meanings of the word "center":**
  1. *A fixed state inside the system itself*—for example, the rest position of a pendulum that does not move under a given step ($T_a(x_*) = x_*$).
  2. *A chosen neutral zero of a scale*—the zero mark of a scale wherever the required algebraic structure has been explicitly specified on the set of answers. *(The geometric midpoint of a drawing may, if desired, be chosen as the coordinate origin, but by itself need not coincide with the zero of a scale; and neither a fixed state, nor a scale zero, nor the middle of a figure is the observer's position.)*
  3. *The organizing center of work—the observer's position*—the role of holding the contract ($\mathcal{O} \notin X$), from which the question, admissible action, and comparison protocol are specified. *(Meanwhile, an imaginary "all-seeing oracle" that supposedly reports the hidden state for free, bypassing the instrument and window, is strictly forbidden by the rules of the model.)*

- **Four distinct meanings of the word "external":**
  1. *Structural exteriority of the holding position*—the role boundary $\mathcal{O} \notin X$ adopted in the contract (which, when a second photographer appears in the doorway, shifts to the outer contour of the new contract $\Gamma'$);
  2. *External complement of a chosen group inside a shared state space*—the remaining part of the domain $U \setminus E$ outside a singled-out ensemble $E$;
  3. *Stepping outside the domain of admissibility of a given question or action*—the situation $X \setminus \mathrm{Dom}(q)$ or $X \setminus \mathrm{Dom}(T_a)$, where the chosen instrument is inapplicable or a button is locked by a safety catch;
  4. *An explicitly specified coupling of an open system with an external environment in an extended model*—coupling the transitions of a system $X$ and an environment $E_{\text{env}}$ on the product $X \times E_{\text{env}}$: for instance, in a discrete coupling model the step $(x, e) \mapsto (x \oplus e, e)$ flips or preserves $x$ depending on the environment state $e$, in contrast to the isolated step $(x, e) \mapsto (x, e)$. *(At the same time, a strict distinction is maintained between the legitimate workbench of the mathematician, who specifies the full model in order to test the limits of a window, and a forbidden executive oracle that bypasses the window.)*

---

### 4. Scene Three: The Lever Balance and the Hidden Ternary Structure of Any Pair `a ≠ b`

Let us now look at the simplest record of difference one can find on a blackboard: $a \neq b$ ("$a$ is distinct from $b$"). On the surface, it looks as though only two elements participate here—the left letter and the right letter. From this arises the illusion that pure duality lies at the very foundation of the world.

Place an ordinary mechanical **two-pan lever balance** in front of us, and the hidden anatomy of any pair becomes immediately visible:

```text
   Diagram 4 (Illustrative mini-scene of a lever balance and the hidden triad of comparison, not a state graph):

                Left pan (contribution x)      Right pan (standard / reference c)
                     \_____/                              \_____/
                        │                                    │
                        └──────────────────▲─────────────────┘
                                           │
                          Fixed fulcrum of the beam (holding the correlation):
                          it is NOT a third pan, yet without it the two pans
                          fall apart into two disconnected saucers on the table!
```

**Reader's caption to `Diagram 4`:** the two pans represent the two compared sides of the scene, while the triangular prism beneath the beam represents the shared condition of their mechanical coupling and comparison, which is not a third weighed load.

For a statement comparing two sides to make sense, **three irreducible things** operate simultaneously:
1. the first side of the comparison (the left pan—the tested specimen);
2. the second, reference side of the comparison (the right pan—the chosen standard weight);
3. **the shared beam with its fixed fulcrum**, which brings both pans into a single act of comparison and is itself neither the left pan, nor the right pan, nor any "third intermediate answer" between the outcomes "balanced" and "tilted." *(Note strictly: in a sharp binary choice between "balanced" and "tilted" on a pair of discrete tokens there is no third intermediate answer—the third element is specifically the retained relation of comparison.)*

On this same balance, two further principles of DOT—often confused in haste—become clear:

- **The distinction between the two sides of a relation is NOT the same thing as the inequality of their current values.** Place identical hundred-gram weights on both the left and right pans. The balance comes to level equilibrium: the weight values coincide. Has the distinction between the left pan (the tested contribution) and the right pan (the reference standard) vanished as a result? Not at all: before us are still two distinct places of the scene, and the question *"do the values on the two sides coincide?"* is one of the most informative questions one can ask of the pair.
- **The signal "balanced / tilted" alone does not allow one to recover the sides without the retained reference.** Suppose the balance is enclosed in a housing with only a flag on the beam visible outside: "matched" (both pans at the same level) or "mismatched" (one higher than the other), where each pan can hold either a light token or a heavy token. If the flag shows "matched," you do not know whether two light tokens or two heavy tokens lie inside. Yet as soon as you **retain in memory which reference token you placed on the right reference pan**, the state of the left pan is recovered uniquely and without loss from the flag reading and the known reference. Conversely, if you write only the word "matched" in your notebook and forget which standard it was compared against, the return path is cut off.

---

### 5. Scene Four: The Dialogue "Are You Ready to Start? — Yes" and Two Sealed Boxes with Buttons

Let us now bring everything we have seen into a complete picture of the working scene of DOT. In early drafts it is easy to confuse *the observer's position* with *the act of observation itself*, calling both by the same word. Let us separate them once and for all using two vivid examples—one human and one laboratory.

**First example—a brief exchange between two people.** Two colleagues have agreed in advance to begin starting up an apparatus only after explicit confirmation of readiness. The first sends a message: *"Are you ready to start?"* The second replies: *"Yes."*

Now imagine that the next morning a narrow slip of paper is found in the corridor with a single word written on it: **"Yes."** If more than a single question was ever discussed in that laboratory (someone might have asked *"Are you ready to start?"* while someone else asked *"Shall we postpone the launch until tomorrow?"*), the detached label "Yes" by itself determines nothing. In an elementary exchange between two interlocutors, **three working components** are clearly visible, none of which can be discarded or fused with its neighbor:

1. **The distinguished sides and states ($X$)**—the situations or participant states to which the question is addressed. Here it is important to remember the boundary of inference: the received sign *"Yes"* certifies that *a confirmation was received in the communication channel*, but by itself is not yet identical to the person's hidden internal state (whether they actually checked all instruments or replied mechanically).
2. **The library of admissible questions ($\mathcal{Q}$) and partial actions ($\Omega$) with their domains of admissibility**—the pre-established context of agreement: the list of admissible questions with their domains of applicability $\mathrm{Dom}(q)$, the address of the question to which the answer is bound, and the available elementary steps $T_a$ with their domains of admissibility $\mathrm{Dom}(T_a)$. Neither of the two interlocutors as a living person is identical to this rule; moreover, one and the same researcher may move from one working position to another during the course of a day.
3. **The executed protocol and retained history trace**—the concrete chain or tree of steps performed within an admissible position: asking the question, receiving the answer *"Yes"*, checking the button safety catch, and retaining the trace of the first step in order to choose the second. The condition of admissibility and the step itself do not coincide: **the contract library specifies the conditions of legitimacy and meaning of a step, whereas the protocol is the actual event of its execution and memory accumulation**. *(The overall coordinating frame of holding the contract is fixed by the typing rule $\mathcal{O} \notin X$: it is not equal to any individual utterance or detail inside $X$, yet requires no separate "fourth mathematical letter" beyond the working core.)*

> **Single-sentence definition of the working observer of Book I:** across all theorems of the first volume, the working mathematical core of the observer is the **triple $\Gamma_{\text{core}} = (X, \mathcal{Q}, \Omega)$**—the carrier of candidate states $X$, the family of partial questions $\mathcal{Q}$ with their domains of applicability, and the family (semigroup) of partial actions and finite protocols $\Omega$ with their domains of admissibility.

**Second example—two sealed boxes on a laboratory bench.** Why is even a pair "set of states + single question" insufficient to describe an actual experiment? Place two externally identical closed boxes on a bench—Box **A** and Box **B**. On the lid of each glows the same **green** indicator window, and next to it sit two continuation buttons: Button `1` ("shift") and Button `2` ("regime flip").

Judging solely by the instantaneous color of the window, Boxes **A** and **B** look like twins. Yet as soon as you reach for the buttons, two decisive differences appear:
- on Box **A** both buttons press freely, whereas on Box **B** Button `2` is mechanically locked by a safety catch in the current internal position—this action is **inadmissible** here (and a mechanical button lock is not at all the same thing as an allowed press after which a lamp shows "no");
- if on both boxes you press the allowed Button `1`, on Box **A** the window stays green, whereas on Box **B** it switches to red.

Thus, before our eyes and without a single artificial symbol, the complete **operational contract of a scene** assembles itself—the contract with which mathematical work begins in Chapter `I.1`: to speak meaningfully of an observable system, one must specify the **domain of candidate states**, the **family of admissible questions** (with a separate marker where a question is applicable at all), the **set of elementary actions** with their domains of admissibility (where a button presses and where a lock engages), the **rules for composing multi-step protocols**, and the **method of final reading of the record**.

For the class of **non-degenerate dynamic scenes** studied in this book, we separately formulate three exact conditions (where the third pertains specifically to the problem of detectable change and is not required for every static measurement):
1. **Non-degeneracy of distinction $(Z_D)$:** among the admissible questions there is at least one that takes at least two distinct answers on its domain (if a green slip of paper is glued over the box window, such a "window" distinguishes no states).
2. **Purity of typing and explicit rejection marker $(Z_C)$:** the role of holding the contract is not identified with an element of $X$ ($\mathcal{O} \notin X$), and the signal "the question or step is inapplicable here" (safety lock) is strictly separated from the substantive answer "no / zero." *(The first two conditions are compatible with non-constant static reading without state change in a formal model—for instance, on $X=\{0,1\}$ with active question $q_1(x)=x$ and identity step $T(x)=x$, as well as throughout the static logic of Chapter `I.2`; meanwhile, the existence of a distinguishing question $q_1$ in the family $\mathcal{Q}$ does not prevent a constant reading $q_2(x)=0$ from sitting alongside it, while any claim about a concrete physical measurement additionally specifies the instrument itself, accessible states, its coupling to the object, and the test protocol.)*
3. **Observable efficacy of continuation $(Z_F)$:** when, beyond static reading, the problem of **change detectable through the window** is posed, there must exist an admissible step carrying some readable state into a new readable state **with a change in the answer to at least one question**. *(In Chapter `I.1` we prove an important asymmetry: under valid typing, such a visible shift of answer strictly implies non-degeneracy of distinction, whereas the converse fails not only in a static scene $T=\mathrm{id}$, but also under "hidden motion"—already on three internal states in a box, a step can permute two parts inside a single fiber of a binary sensor without changing the color of the lamp.)*

---

### Historical-Philosophical Note: The Historical Fork of Sāṃkhya, Yoga, and Advaita, the Question of the Instrument, and the Limit of Self-Report

1. **Motif of the classical sources and historical divergence without conflating schools.** Long before category theory, finite automata, and cybernetics, Indian philosophical thought posed the question of why the position of the seer must not be conflated with the changing states of the cognitive instrument. Here we turn to classical **Sāṃkhya**, **Yoga**, and **Advaita Vedānta** not as different labels for a single doctrine, but with respect for their own historically distinct answers.  
   Classical Sāṃkhya (Īśvarakṛṣṇa's *Sāṃkhyakārikā*, `SK 3, 12–13, 18–21`) strictly distinguishes two irreducible principles: a plurality of non-acting witnesses *Puruṣa* (`SK 18`, *sākṣin*, *draṣṭṛ*) and unproduced active primal nature *Prakṛti* (not derived from any unitary *Brahman*), which unfolds the world of experience and the operation of the internal instrument (*antaḥkaraṇa*) through the joint operation of three constituents, the *guṇas* (*sattva, rajas, tamas*). In the related yet distinct language of Patañjali's *Yoga Sūtras* (`YS 1.2–1.4`), yoga is defined as the cessation of the modifications of the mind-field (*yogaś citta-vṛtti-nirodhaḥ*): then the seer abides in its own form (*tadā draṣṭuḥ svarūpe 'vasthānam*), whereas otherwise there is identification with the ongoing modifications (*vṛtti-sārūpyam itaratra*). Advaita Vedānta (cf. *Chāndogya Upaniṣad* `6.2.1`, *Māṇḍūkya Upaniṣad* `7`, *Dṛg-Dṛśya-Viveka* `1–5`), by contrast, poses the question of the non-dual ground (*Brahman*) prior to any division into seer and seen and investigates the status of apparent superimposition and reflection (*adhyāsa*, *pratibimba*). To fuse these schools into a single "generic classical cosmogony" would distort each of them.

2. **Authorial articulation in DOT and the joint execution of the three sides of an instrument.** In the authorial design of DOT, these interlocutors help bring into sharp relief an engineering and logical problem: how does the position of posing a question and holding a contract differ from the changing states of an instrument, and how do clarity of display, transition action, and retention of constraints combine within the instrument itself? In the famous image of the lamp (`SK 12–13`, *pradīpavat*), wick, oil, and flame shine only through the cooperative work of differing parts. Translating this motif into the language of verifiable finite circuits, we must in every case specify the assignment of functions explicitly and test joint necessity relative to a concrete task: if we take three binary enable gates $s, r, t \in \{0, 1\}$ and output $y = s r t x$, then for $x = 1$ disabling any one of the three gates zeroes the output (joint necessity proved by direct substitution); whereas for a different task, say $y = s r x$, the third gate is redundant. Thus the necessity of three factors is proved relative to an explicitly declared goal and circuit, not deduced from the mere presence of three names. In this parallel, *sattva* corresponds to accessibility and clarity of the instrument window (but **not** *Puruṣa* itself), *rajas* as an image of transformation (though not a quantitative measure of effort), and *tamas* as an image of domain restriction and trace retention (which by no means reduces to breakdown or useless noise).

3. **Boundary of exteriority and the limit of self-description.** Hereafter in the book we build our own finite mathematical model, all rules and proofs of which are written out independently of the philosophical motif (`0` incoming arrows into the core theorems). The notation $\mathcal{O} \notin X$ records within a chosen contract $\Gamma$ the role boundary between the position of holding questions and the states of the object; it in no way forbids including the memory of a former instrument inside the extended space $X'$ of a new contract $\Gamma'$. Equally carefully formulated is the limit of complete self-description (to which we return in Book II): from the Cantor–Lawvere theorem on the impossibility of a surjection $X \twoheadrightarrow \mathcal{P}(X)$ follows the impossibility of an *exhaustive* internal enumeration of all subsets of $X$, but **not** the impossibility of all internal self-reporting—already the identity question $q(x) = x$ on a two-element carrier $\{0, 1\}$ provides an exact binary report of the state. Mathematical role distinction in a contract neither licences declaring an internal state of an automaton to be "*Puruṣa*" nor refutes the possibility of consciousness in any system by a single diagonal argument (a systematic analysis is given in Book III, Chapter `III.3`).

---

## Part III. Where Binary Logic `{0, 1}` Comes From, Where Its Boundary Lies, and How to Read This Book

### 1. Local Birth of `{0, 1}`: Why DOT Neither Abolishes Ordinary Binary Logic Nor Treats It as the Bottom of the World

We can now answer the question: **how does familiar binary logic (`0` and `1`, "yes / no," operations `AND`, `OR`, `NOT`) arise in a theory that begins with the act of distinction and the observer's position, and why does this require inventing no "special quantum or mystical logic"?**

The answer consists of three simple steps.

**Step one: the cut itself is older than the names `0` and `1`.** Imagine two engineers who wire two indicator lamps to the very same pressure threshold sensor, but swap the leads: for the first engineer, high pressure is labeled `1` ("green") and low pressure `0` ("red"); for the second, the exact same high pressure is labeled `0` and low pressure `1`. Both engineers perform **one and the same distinction** on the set of states: they partition all possible states into the exact same two non-empty classes. Until we specifically agree on rules of calculation, neither of the two parts of the cut is singled out as an "algebraic zero," and answers cannot yet be added to one another.

**Step two: two different floors where duality appears in reasoning.** So as not to confuse checking the rules of a game with making a move inside the game, let us separate two completely different binary choices:
1. *On the ground floor (well-formedness of the frame and admissibility of a step):* we check whether the conditions of the scene itself are intact and whether pressing the chosen button is permitted in the current state (`admitted` vs. `blocked / rejected`). This is a check of contract validity, not an answer about the properties of the object.
2. *Inside an already held window (substantive binary answer):* once the position is fixed, the domain of admissibility is verified, and a sharp two-sided question is posed inside that window, each admissible state yields a unique binary answer **"yes / no" (`1 / 0`)**.

**Step three: the full family of logical predicates over a fixed total window forms a classical Boolean algebra.** Fix a single concrete total window reading $\pi : X \to Y = \mathrm{im}\,\pi$ and consider **all logical predicates of its possible outcomes (including the identically false `0` and identically true `1`)**, alongside the non-constant two-sided cuts tested by an individual sensor (non-constant cuts by themselves are not closed under `AND` and `OR`, since $p \land \neg p$ is constantly false and $p \lor \neg p$ is constantly true). All such predicates have the form of a composition $p \circ \pi$, where $p : Y \to \{0, 1\}$, and **precisely this full family of $2^{|Y|}$ predicates forms a classical distributive Boolean algebra** with connectives `AND`, `OR`, `NOT` and the law of excluded middle. Consequently, **binary logic in DOT is completely legitimate and exact locally—over any fixed total window on its domain of applicability**, whereas partiality with rejection marker $\bot$, incompleteness of a single window relative to a hidden layer, and switching windows are described separately.

---

### 2. Four Distinct Meanings of the Word "Not" That Must Never Be Conflated

A vast number of false paradoxes in discussions of logic and observation arise because ordinary language uses the single short word "not" or "no" to name four operations of completely different structure. Let us summarize them in a clear reference table:

| Kind of "Negation" | What It Acts On | Illustrative Example in Our Scenes | What Happens to the Scene Partition |
| :--- | :--- | :--- | :--- |
| **1. Prohibition / admissibility lock** | An ill-posed setup or an inadmissible button | Button `2` on Box **B** is locked by a safety catch; a question is asked outside the instrument's domain | Cuts off an illegitimate step (returns a distinct rejection marker $\bot$), **not** a transition to another state and **not** the answer `0` |
| **2. Logical complement / label swap (`unary NOT`)** | Selecting the opposite part of an already drawn cut or swapping labels `{0, 1}` | Singling out "the whole frame except the mirror" or swapping the red and green lamp wires on the same sensor | Swaps the chosen class and its complement (labels `0 ↔ 1`), while **the partition boundary dividing states into two groups remains identical.** *(The word "unary" means an operation of one argument—not to be confused with a "unitary" operator in geometry)* |
| **3. Switching the scene states themselves** | The actual contents of the tested system | Swapping tokens on the balance pans: (a) replacing the token on one pan with the opposite weight, or (b) simultaneously replacing both tokens **each with its opposite weight** | Actually permutes the states of the carrier: a single change on one pan flips the balance flag, whereas **simultaneously replacing both tokens each with its opposite weight changes the state while leaving the "matched" fiber in place** *(an arbitrary replacement of two tokens need not preserve equilibrium)* |
| **4. Sign inversion of a contribution with mutual cancellation** | A directed contribution in **a single chosen linear balance** (introduced in Chapter `I.5`) | Adding opposite integer contributions `+1` and `-1` in a unified additive balance | Produces **mutual cancellation `+1 + (−1) = 0` in the chosen linear count**, which does not exist in Boolean union (`1 ∨ 1 = 1`; two physical pushes under different conditions need not automatically cancel each other) |

Keeping this table in view suffices to never confuse a jammed button with repainting a bulb on a control panel, flipping a part inside an instrument, or algebraically subtracting contributions.

---

### 3. What Happens at the Window Boundary: Three Reading Statuses from a Single Projection Drawing

What happens when we remain within a single fixed window, but ask about a property of the object that cuts across the hidden "shadow" of that window?

Let us return to our first drawing from Part I (`Diagram 1`) and **now add to the previous three idealized solids of common diameter $D$ a fourth candidate** (which was not present in the first diagram): an upright **cubic block** resting on the horizontal table with a square base of side $D$ (whose diagonal is $D\sqrt{2} > D$). Suppose only the **top view** at a known scale is open to us, currently showing an even **circle of diameter $D$**, while beneath the table a horizontal circular ring of inner diameter $D_{\text{ring}}$ strictly larger than $D$ and smaller than $D\sqrt{2}$ ($D < D_{\text{ring}} < D\sqrt{2}$) is prepared with no obstacles below. No mystical "half-truth" needs to be introduced inside the window—directly on the visible circular silhouette, relative to different questions, **three transparent statuses** arise:

1. **Guaranteed by the current window:** ask *"In our idealized model, under vertical lowering without tilting along the window axis, will this part pass through the ring of inner diameter $D_{\text{ring}} > D$?"* Whichever of the three solids of diameter $D$ hidden behind the circle stands there (sphere, right circular cylinder, or right circular cone), the answer is certainly affirmative—the entire hidden fiber behind the circle possesses this property, whereas the added cubic block with base diagonal $D\sqrt{2} > D_{\text{ring}}$ fails to pass through this ring, so the question is nontrivial on the four candidates while simultaneously resolved unambiguously within the circular window fiber *(and for a narrow ring $D_{\text{ring}} < D$, all three solids of this fiber are equally guaranteed to be excluded)*.
2. **Compatible with the window, but requiring a new viewpoint (the boundary shadow of the window):** ask *"Is the object before us a sphere?"* The circle of diameter $D$ visible from above is **compatible** with its being a sphere, but **does not guarantee** it, because an upright cylinder and cone of diameter $D$ produce the exact same circular plan view. Precisely this boundary strip between "compatible" and "guaranteed" measures the shadow of the current window and signals to the observer: to resolve the question binarily, an orthogonal side view must be added.
3. **Excluded already by the current window:** ask *"Is this the added upright cubic block with base side $D$?"* The top view alone showing a circular silhouette is completely sufficient to answer a firm "excluded"—no object in the hidden fiber behind the circle has a square plan view.

A sharp property is resolved by a binary "yes / no" without remainder inside a given window **if and only if the second—boundary—strip is empty**. In Chapter I.2 of the first book, this intuitive rule of three statuses will receive a rigorous mathematical formulation via adjoint operations of question transfer along the window map.

---

### 4. The Central Spine of Book I, Comparison with Classical Theories, and Plan of the Three Volumes

This Introduction has shown:
- how posing the problem **from the conditions of distinction and the working observer $(X, \mathcal{Q}, \Omega)$** differs both from the classical discourse on ready-made objects and from merely choosing a ready-made coordinate medium;
- why in any living distinction a holding correlation operates behind the visible pair of sides, why the distinguished states $X$, the library of questions and actions $(\mathcal{Q}, \Omega)$, and the executed protocol with its retained trace do not merge into one another, and why the relative exteriority of the observation position ($\mathcal{O} \notin X$) is a model typing rule free of mysticism;
- how rigorous classical binary logic is born locally inside any fixed window, how the four meanings of "negation" differ, and how the boundary shadow of a window indicates the need for a next step or a second viewpoint.

**The Central Spine of Book I (unified progression of Chapters `I.1 → I.2 → I.3 → I.6 → I.9`).**  
So that the reader can see from the outset how the chapters of the first volume interlock into a single continuous deduction, let us trace the connection across its main constructions:
1. In **Chapter `I.1`**, a pair of independent two-sided questions $q_x$ and $q_c$ generates the four-state scene $S_4 = \{0, 1\}^2$ and the derived agreement question $\beta = q_x \oplus q_c$. Together they define three canonical partitions of $S_4$ and **six two-element slices** $X_0, X_1, C_0, C_1, B_0, B_1$.
2. In **Chapter `I.2`**, choosing one slice from each pair forms a closed triangular route of three windows $\bigl(\Omega_1(c_0), \Omega_2(x_0), \Omega_3(b_0)\bigr) = (C_{c_0}, X_{x_0}, B_{b_0})$. On this loop arises the canonical **loop holonomy $H_3 = \mathrm{swap}_{\Omega_3}^{\kappa}$** with binary defect $\kappa = x_0 \oplus c_0 \oplus b_0 \in \mathbb{F}_2$.
3. In **Chapter `I.3`**, the coordinate-exchange action `swap` on the same cell $S_4$ forces the observer to retain all four states as future equivalence classes, turning the pullback of questions against the step into an exact measure of required memory.
4. In **Chapter `I.6`**, the six balanced two-sided questions on $S_4$ (corresponding to those same six slices) form the vertices of the **six-vertex octahedron $O_6 \cong K_{2,2,2}$**, where an edge connects pairs of slices intersecting in exactly one state of $S_4$.
5. Finally, in **Chapter `I.9`**, this very same octahedron $O_6$ turns out to be the **one-dimensional skeleton of the nerve $\mathcal{N}$ of the cover** by the six two-element slices of $S_4$: its four triangular faces with holonomy defect $\kappa = 0$ are filled by actual states $(x, c) \in S_4$, whereas the four triangular faces with nontrivial holonomy $\kappa = 1$ ($H_3 = \mathrm{swap}$) **remain hollow** ($X_{x_0} \cap C_{c_0} \cap B_{b_0} = \varnothing$), generating the cohomological gluing obstruction $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$. Thus the local holonomy of `Chapter I.2`, the combinatorial geometry of the octahedron of `Chapter I.6`, and the cohomological barrier to a global section in `Chapter I.9` prove to be three facets of one and the same theorem about the three questions $q_x, q_c, \beta$.

**Positioning: What Is Known in Classical Mathematical Theories and What DOT Specifically Adds.**  
Since this book claims novelty in the **structural links** across disciplines, let us immediately compare its apparatus with its closest classical predecessors that likewise placed experiment, trajectory, or measurement context ahead of a ready-made state space:

| Classical Apparatus and Authors | What Is Already Proved in Classical Theory | What the Observer's Position in DOT Specifically Adds and Connects |
| :--- | :--- | :--- |
| **Gedanken-experiments on sequential machines and Nerode equivalence** (*E. F. Moore, 1956; J. Myhill, 1957; A. Nerode, 1958*) | States of an automaton ("black box") are distinguished by input-output experiments; quotienting by future words yields the minimal Moore automaton | In `Chapter I.3`, future equivalence is built over a contract with **partial actions and a distinct rejection marker $\bot$**, extended to **branching adaptive protocol trees** (separating stochastic laws with identical marginals), and linked by duality to the tower of subalgebras of pulled-back questions from `Chapter I.2` |
| **Behavioral approach to open systems** (*J. C. Willems, 1989–2007*) | A system is defined as a behavior $\mathcal{B} \subseteq \mathbb{W}^{\mathbb{T}}$ without an a priori input/output split; interconnection of subsystems is intersection over shared variables (*tearing, zooming, linking*) | In `Chapters I.1, I.4, I.9`, the fiber product along a seam $E_L \times_K E_R$ is augmented by the **autonomous memory cost of a feedback controller** (the gap theorem `11` vs. `19 / 22` without an external clock), accounting for rejection domains and the exact condition under which pairwise seams fail to extend to a global behavior ($H^1 \neq 0$) |
| **Formal concept analysis and adjoint transfer quantifiers** (*F. W. Lawvere, 1969–1970; B. Ganter, R. Wille, 1982–1999*) | A formal context $(G, M, I)$ links extent and intent of concepts via a Galois connection; a map $\pi : X \to Y$ induces the adjoint functor triad $\exists_\pi \dashv \pi^* \dashv \forall_\pi$ | In `Chapter I.2`, the difference between upper and lower images $\partial_\pi(S) = \exists_\pi(S) \setminus \forall_\pi(S)$ is identified with the **shadow boundary of a window and the three operational reading statuses** ("guaranteed / compatible / excluded"), and on a cycle of three windows is extended to the canonical holonomy bijection $H_3$ |
| **Linear realization theory and Hankel matrices** (*L. Kronecker, 1881; B. L. Ho, R. E. Kalman, 1965–1966*) | Finite rank of an infinite Hankel matrix $H_f$ is equivalent to rationality of the series and gives the dimension of the minimal linear realization $(A, B, C)$ | In `Chapter I.8`, the Hankel matrix is derived as the **linear projection of Nerode equivalence** (`Chapter I.3`) when passing from a tabular observer to a linear reading functional on a finite window, and is joined with the **oracle-free executor contract** over a composite modulus $\mathbb{Z}/N\mathbb{Z}$ |
| **Sheaf-theoretic contextuality and nonlocality** (*S. Abramsky, A. Brandenburger, 2011*) | Measurement scenarios are described by a presheaf of distributions $\mathcal{E}$ over a cover of compatible measurement contexts; contextuality is the absence of a global section in $\Gamma(\mathcal{M}, \mathcal{E})$ | In `Chapters I.2, I.6, I.9`, it is shown that already on the deterministic carrier $S_4$ the six two-element slices of the three basic questions $q_x, q_c, \beta$ form the octahedral nerve $\mathcal{N}$, where **the holonomy $H_3 = \mathrm{swap}$ from `Chapter I.2` exactly marks the hollow faces of $\mathcal{N}$**, and the presheaf of local slice orientations yields the obstruction $\dim_{\mathbb{F}_2} H^1(\mathcal{N}; \mathbb{F}_2) = 3$ |

> **On Classical Mathematical Structures and the Specific Contribution of This Book.**
>
> To the mathematical reader we state plainly: nearly all individual constructions in this book are classical, and in the statements of theorems we indicate their provenance via the line "*Classical foundation*" immediately beneath the heading. The book draws upon the algebra of relations of Peirce–Schröder–Tarski, Galois connections and Lawvere's triad of adjoint quantifiers, Moore–Nerode–Myhill automaton minimization, Kronecker–Kalman–Schützenberger Hankel realization, Čech cohomology, Zaslavsky's signed and gain graphs, Cayley–Dickson doubling and Albuquerque–Majid twisted group algebras, Kraus–Busch–Tsirelson quantum effects and instruments, and the Cantor–Lawvere diagonal theorem. The book neither rediscovers nor claims priority for any of these classical theorems.
>
> The proper subject of DOT is the **unified operational assembly from the observer's position $\Gamma$**. It shows specifically which breakdown of distinction at the preceding tier forces the introduction of the next classical structure; where the exact boundary of admissible descent lies (the reading domain $\mathrm{Dom}(q)$, separating reading descent from transition descent, the oracle-free executor contract); and what constructive invariants emerge at the seams: the four-state scene $S_4$ with its finite affine-balanced filtration $16 \to 8 \to 6$ (`Chapter I.2`) and quantum threshold effect filtration $16 \to 8 \to 2$ (`Chapter II.6`), the spine on the bipartite-faced octahedron $O_6$ with its $\mathbb{F}_2$-torsor presheaf, the Möbius–Petersen intertwining identity $6H_o = K^2 - 7K + 13I_5$, and the classification of square roots of the complement involution in $\mathfrak{S}_6$ and $\mathfrak{S}_8$.
>
> Therefore, in each formal statement it is helpful to distinguish two layers: the classical fact, which can be found in the literature, and the contribution of this book—how that fact is read from the observer's position and where it leads next.

**Two Constructive Engines Across the Trilogy (`Π_k → Π_{k+1}` and the Three Regimes `|R| ∈ {1, >1, 0}`).**  
Across all three volumes, one and the same mechanism drives every transition from a lower tier to a higher structure without *ad hoc* postulates:
1. **Five-beat shift of the observer window ($\Pi_k \to \Pi_{k+1}$):** fix the carrier $X$ and the currently accessible reading window $m_{\mathrm{acc}} : X \to B$ ($\mathcal{O} \notin X$); exhibit an explicit shadow witness pair $(s, t) \in \ker m_{\mathrm{acc}}$ ($s \neq t$, $m_{\mathrm{acc}}(s) = m_{\mathrm{acc}}(t)$); apply an admissible continuation $T \in \mathcal{A}$ that splits the pair on a future question ($q(Ts) \neq q(Tt)$ or $T(s) = \bot \neq T(t)$); after direct proof, contravariant pullback ($T^* q = q \circ T$), and a finite countermodel upon dropping a premise, the former dynamic probe $q \circ T$ crystallizes into a new coordinate of the enlarged memory $m'_{\mathrm{acc}} = (m_{\mathrm{acc}}, q \circ T)$.
2. **Three-regime solution count $|\mathcal{R}|$:** every problem of recovery, descent, or gluing of local data within a fixed class falls into one of three exact regimes—**$|\mathcal{R}| = 1$** (forced canonical invariant: pair transposition in `I.1`, minimal Nerode quotient $X/{\sim_\Gamma}$ in `I.3`, cube antipode $\kappa$ in `I.6`), **$|\mathcal{R}| > 1$** (gauge freedom of scale or frame: `48` symmetries of $W(B_3)$ and `4096` Fano sections in `I.6`, coboundaries $B^1$ in `I.9, II.3`, hidden-label permutations $\mathfrak{S}_m$ in `III.4`), or **$|\mathcal{R}| = 0$** (boundary obstruction within the current language that forces the next tier of mathematical structure: absence of subtraction in $(\mathcal{P}(X),\cup)$ in `I.5`, absence of a scalar root $z^2 = -1$ in $\mathbb{Z}$ and of $r^2 = c_6$ in $\mathfrak{S}_6$ in `I.5–I.6`, hollow faces of the nerve $\mathcal{N}(O_6)$ with $H^1 \neq 0$ in `I.9, II.3`, Kochen–Specker and Peres–Mermin contextuality obstructions in `II.6–II.7`, and the Cantor–Lawvere diagonal barrier in `II.9`).

From here begins the step-by-step construction of the theory itself, divided into **three books** with strict dependency control (no concept from a later tier is used before it has been explicitly introduced and verified):

- **Book I (`Chapters I.1–I.9`) — Finite Distinction, Memory, Graphs, Arithmetic, and Cost Without Continuous Coordinates.**  
  Immediately following this Introduction, opening **Chapter `I.1`** translates the scene conditions examined here into the language of exact definitions and theorems: first it fixes the formal passport of the **operational contract $\Gamma$**, the theorem on the primacy of a two-class partition over label names, and the exact conditions of non-degeneracy and coupling on finite countermodels; then it grows the **four-state polar cell** out of a pair of independent questions, verifies both of its symmetric recovery decoders, and derives the law of coupling two systems along a shared seam. Next, `Chapters I.2–I.9` develop partial actions and question transfer, minimal memory of all future distinctions, feedback and the full autonomous cost of an executor, the emergence of the sign `±1`, finite graphs and projective geometries (including the octahedron of questions and the Fano plane), arithmetic laws on divisor lattices, oracle-free modular windows with Hankel matrices, and the cohomological obstruction to global gluing together with the summary architecture of the finite library.
- **Book II (`Chapters II.1–II.9`) — Hidden Return, Continuous Continuation, Phase Geometry, and the Quantum Bridge.**  
  Here, with an explicit list of new axioms, we introduce the algebra of delayed return of hidden memory, real numbers and smooth quarter-turn flows, cochains, lifts, and holonomy on graphs, the sign tables of Fano and the octonions, quantum states, measurement instruments, and contextuality, culminating in the strict boundary of complete self-description in closing Chapter `II.9`.
- **Book III (`Chapters III.1–III.5`) — Domain Bridges, Verifications, and Program for the Next Step.**  
  The constructions of the first two books are tested against domain-bridge passports across independent mathematical, algorithmic, and textual models: on finite directed weighted graphs and random-walk resolvents, in a systematic comparison with classical Sāṃkhya–Yoga, Advaita, and Pāṇini's formal grammar, and in oracle-free large-prime cofactor graphs and the gauge symmetry of hidden Markov models.

Every step in the chapters is accompanied by a hand-reproducible finite example, a clear caption for every diagram, and an independent machine verification of finite witnesses in `Julia`. We begin this construction in **Chapter `I.1`**.

---

### Verifiability Passport of the Introduction (`Book I v3.3`)

- **Canonical book node:** `E0` (introductory conceptual essay to the entire three-volume DOT corpus; five-beat shift of the observer window $\Pi_k \to \Pi_{k+1}$ and solution-count classification $|\mathcal{R}| \in \{1, >1, 0\}$; historical fork of Sāṃkhya, Yoga, and Advaita without conflating schools; local birth of Boolean algebra and three reading statuses at the window boundary).
- **Exact `Julia 1.12.6` verifications (single-threaded mode, no `Float64`):** [`11_verify_full_book_I_v3_3.jl`](11_verify_full_book_I_v3_3.jl) — gate `GATE-I-E0` (period-`2` cycle without fixed points, non-transitivity of threshold proximity on `0, 3/5, 6/5`, joint necessity of gates $y = s r t x$ vs. redundancy in $y = s r x$, partial internal self-report $q(d,m)=m$ on $X=\{0,1\}^2$ vs. Cantor–Lawvere theorem $X \not\twoheadrightarrow \mathcal{P}(X)$, Boolean subalgebra of $2^{|Y|}$ window predicates).
- **Connection to formal threshold theorems:** rigorous statements and proofs of the threshold propositions of the Introduction are placed in `§I.1.0` of Chapter `I.1` (`TNR.BookI.E0.partition_relabel`, `status: planned` in Appendix `VP`).
- **Consolidated appendices and academic bibliography:** placed in [`10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md`](10_APPENDICES_GR_VP_AD_BOOK_I_V3_3_EN.md).
