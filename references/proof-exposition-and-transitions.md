# Proof exposition and reader-guiding transitions

Use this reference when a proof is mathematically present but reads like a sequence of deductions, when lemmas appear without a visible role, or when an early machine-generated draft sounds locally fluent but globally stiff.

## The central distinction

A proof can be rich in logical connectives and still be hard to follow. Words such as `since`, `thus`, `hence`, and `conversely` explain relations between adjacent statements. They do not by themselves tell the reader:

- why a lemma or construction is introduced at this point;
- which phase of the proof has begun;
- what an intermediate claim will make possible;
- how a completed subargument advances the theorem;
- when and why the main conclusion now follows.

Call the first kind **local logical continuity** and the second **reader guidance**. Publication-level exposition needs both.

Use this diagnostic: temporarily ignore the displayed mathematics and read only the opening and closing sentence of each proof paragraph. A reader should still be able to recover the argument's spine. If the remaining prose is only `thus`, `similarly`, and `it remains to show`, the proof is connective-rich but guidance-poor.

## Three scales of transition

### 1. Sentence scale: justify the next inference

Name the relation between adjacent statements: cause, consequence, equivalence, contrast, reduction, or completion. Keep the connective close to the inference it governs.

Do not use a connective as a substitute for its missing reason. `Therefore` is useful only when the preceding sentence makes the decisive premise visible.

### 2. Paragraph scale: state the job of the next block

At a real phase boundary, use a purpose or role sentence. Common jobs include:

- defining an object that will encode the obstruction;
- proving an invariant needed for a later construction;
- reducing the theorem to an auxiliary claim;
- handling the exceptional case left by the main argument;
- converting the combinatorial construction into the stated bound.

A good paragraph opening names that job in the vocabulary of the theorem. It should not narrate the act of writing.

Compare the functions, not the wording:

- Draft diary: `Now we define an ordering.`
- Reader-guiding purpose: `To construct the required spanning trees, we first obtain an ordering with the needed parity property.`

### 3. Proof-architecture scale: expose the route through the argument

Before a long proof, tell the reader what the proof will build or preserve and why that suffices. Before a major lemma, explain its role in the theorem. After a major claim, state explicitly how it is used.

For a nontrivial lemma introduction, combine only the elements that help:

1. **Role:** what later result needs the lemma;
2. **Provenance:** whether a related argument is known and where;
3. **Method choice:** what this proof does differently or directly.

For example, the prose may explain that a lemma is the final ingredient for the main theorem, note a related argument in the literature, and announce a direct inductive proof. Do not force all three elements when one clear role sentence is enough.

## A reliable long-proof spine

Use the following as a functional checklist, not a rigid template:

1. **Setup:** fix the objects and normalize notation.
2. **Strategy or invariant:** state what will be constructed, maintained, or reduced.
3. **Phase purpose:** explain why the next construction or claim is needed.
4. **Intermediate claim:** isolate the exact property that unlocks the construction.
5. **Claim proof:** establish the property with visible subcases or induction steps.
6. **Use of the claim:** return from the claim and perform the promised construction.
7. **Verification:** show that the constructed object has the required properties.
8. **Consequence and return:** translate those properties into the theorem's conclusion.

The most useful recurring sequence is:

> purpose → claim → proof of claim → explicit use of claim → construction → verification → consequence → return to theorem

This sequence prevents a common failure in which a correct claim is proved but the reader must infer why it was introduced.

## Writing the transitions

### Open the proof with strategy when the route is not immediate

The opening should identify the governing construction, invariant, reduction, or induction. Avoid listing every technical tool. A roadmap is selective: it identifies the spine, not the inventory.

### Introduce an intermediate claim by need

State the dependency before the claim when possible:

> To construct (X), it is enough to obtain (Y). We record the required property as a claim.

Then state (Y) precisely. The reader now knows both what must be checked and why it matters.

### Resume the main proof after the claim

Do not move silently from `\end{proof}` or the end of a claim to an unrelated construction. Reconnect the pieces:

> Using the ordering supplied by the claim, we now construct (X).

This sentence is often more valuable than another local `therefore`: it restores the main dependency chain after a nested argument.

### Interpret a construction before computing with it

After defining an object, state the property the definition is designed to enforce. After a displayed calculation, explain which requested conclusion it proves. A proof should not make the reader reverse-engineer the purpose of each definition.

### Close locally and globally

At the end of a claim, say what has been proved when the endpoint is not visually obvious. At the end of the theorem proof, convert the last property or equality into the exact claimed conclusion. If the theorem follows by combining named earlier results, name that combination.

## Paragraph design inside proofs

- Give each paragraph one dominant job: setup, construction, claim, case, verification, or consequence.
- Split a paragraph when the proof changes job, not merely when it becomes long.
- Keep the subject of a transition concrete: the ordering, tree, invariant, inequality, or lemma—not vague phrases such as `this fact` when several facts are available.
- When a case split is necessary, state why the cases are exhaustive and what remains common across them.
- Use `It remains to show ...` only for one sharply defined residual task. Do not use it to hide an unstable collection of cases.
- Place a short interpretation after a dense calculation or construction before moving to the next phase.
- Avoid giving routine and decisive steps equal rhetorical weight. Slow down at the mechanism that carries the proof.

## Failure modes to repair

### Tool inventory in the abstract or introduction

A list of theorem names, contractions, orientations, and polyhedra may sound technical without revealing the argument. State the conceptual mechanism there; reserve the complete tool chain for the proof roadmap or relevant section.

### Lemma procession

Several formally correct lemmas can read as unrelated obligations when none is introduced by role. Add a sentence that states what the next lemma supplies and where it will be used.

### Post-hoc explanation

A remark after the proof that explains which two steps were essential is evidence that the proof lacked advance guidance. Move enough of that explanation before or within the decisive steps; keep the remark only for genuinely additional insight.

### Connective saturation

Repeated `thus`, `hence`, and `therefore` can make every line sound conclusive while leaving the hierarchy flat. Replace some with purpose, phase, use, and return sentences.

### Discovery diary

Phrases such as `now we try`, `we got`, `we want to`, and `hence we got the proof` report the author's process. Rewrite them as mathematical dependencies: `to prove`, `it suffices`, `the claim yields`, and `combining ... proves`.

### Patchwork case analysis

Long strings of local cases, colored questions, and ad hoc fixes often signal an unstable architecture. Before polishing them, ask whether a stronger invariant, ordering, or auxiliary claim can replace the patchwork. Preserve uncertain mathematics and seek author verification; do not invent the new route.

### Overlong proof paragraph

Length alone is not the problem. A long paragraph becomes difficult when it performs multiple jobs without announcing the transitions. Identify the jobs first, then split or add structure.

## Background and citation architecture

Reader guidance begins before the proofs. Build a literature map by function rather than by citation count:

| Function | Question the introduction must answer |
|---|---|
| Problem anchor | What object or parameter is being studied, and why is it established? |
| Baseline | What classical theorem or complexity result fixes the starting point? |
| Adjacent regimes | What is known for nearby graph classes, parameter ranges, or variants? |
| Exact frontier | What result or limitation does the paper directly advance? |
| Conceptual neighbor | Which adjacent theory makes the new bridge intelligible? |
| Boundary evidence | Which example, exception, or non-comparability result prevents overreading? |

Every paragraph of prior work should serve at least one of these functions and lead toward the paper's question. More bibliography entries do not automatically produce better background. Verify that each cited source supports the adjacent claim and its hypotheses; prefer primary sources for theorem, bound, complexity, priority, and historical assertions.

Avoid two extremes:

- **under-contextualized:** only a few famous results are named, leaving the exact frontier and conceptual neighbor invisible;
- **citation dumping:** many results are listed chronologically without explaining how they locate the gap.

## Staged revision procedure

Revise a stiff proof in separate passes:

1. **Mathematical boundary:** preserve every claim and mark gaps; do not repair mathematics editorially.
2. **Architecture:** write a one-line function for each lemma, claim, and proof phase.
3. **Spine:** arrange those functions as setup, strategy, intermediate need, construction, verification, and return.
4. **Paragraph roles:** ensure each paragraph performs one primary job.
5. **Transitions:** add role, purpose, use, consequence, and closure sentences at genuine boundaries.
6. **Local logic:** check sentence-level reasons, connectives, references, and displayed equations.
7. **Compression:** remove diary prose, repeated conclusions, tool inventories, and explanations that have become redundant.
8. **Reader test:** read only paragraph openings and closings; then read the full proof without editing and note the first lost dependency.

Do not treat counts of transitions, paragraph length, or citations as quality scores. Use them only to locate passages for close reading.

## Final proof-transition gate

Before calling the exposition mature, check:

- a major lemma is introduced by its role;
- a long proof announces its strategy or invariant;
- each non-obvious construction is preceded by its purpose;
- each intermediate claim is followed by an explicit use;
- each phase ends with the consequence needed by the next phase;
- the final sentence returns to the theorem's exact conclusion;
- local connectives support rather than substitute for the proof architecture;
- the introduction supplies the background needed to understand why the theorem matters.
