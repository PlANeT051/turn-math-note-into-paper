# Section blueprints for a mathematics paper

Use these as functional blueprints, not mandatory templates. Omit moves that do not serve the manuscript.

## Title

A strong title identifies the central object and the actual result or relation. Prefer established terminology and searchable nouns. Avoid naming an early proof technique if the final paper's contribution is broader or conceptually different.

Check:

- Does the title agree with the strongest theorem actually proved?
- Are singular/plural forms and technical modifiers exact?
- Would a specialist understand the scope without reading the abstract?
- Does a subtitle add information rather than repeat the title?

## Abstract

Target one compact paragraph unless the venue prefers otherwise. A useful sequence is:

1. **Object/problem:** define the central object or parameter in words.
2. **Context/gap:** identify the known limitation or named question in one or two sentences.
3. **Result:** state the main theorem with material hypotheses, bounds, and exceptions.
4. **Relation:** say whether it resolves, sharpens, connects, or applies something—only when supported.
5. **Interpretation:** state tightness or conceptual significance if it helps the reader evaluate the result.

The abstract is not a miniature introduction. Exclude literature surveys, proof chronology, unexplained notation, and claims such as “novel” or “important” that the text does not substantiate.

Abstract test: a reader should be able to answer “what objects, what result, under what conditions, and why this result?” without opening the paper.

## Introduction

Assign one primary function to each paragraph.

### Opening: problem and vocabulary

- Under this author's house style, begin with the historical problem and the line of work that leads to the paper; do not open with a detailed notation block.
- Introduce the object through that mathematical problem, not through generic claims about the field.
- After the historical positioning, define the main parameter before stating detailed bounds or the paper's theorem.
- Give one concrete reason the problem matters: a canonical equivalence, application, or structural role.

### Prior work: map rather than catalogue

Group results by function:

- baseline or classical bound;
- best known result in the manuscript's regime;
- conjecture or obstruction;
- neighboring theory needed for the new conceptual bridge.

Use chronology only where it shows genuine progression. State theorem conditions accurately and attribute names consistently.

### Gap and contribution

Use a clean turn from known work to the present paper:

> The preceding bounds leave open ...

> For general graphs these two parameters are incomparable; the planar case behaves differently.

Then state the theorem. Do not make the reader infer the main contribution from several lemmas.

### Scope, tightness, and examples

Immediately explain important exceptions, sharp examples, or non-comparability. A small example or figure can prevent an overbroad reading of the theorem.

### Proof idea and roadmap

Give the conceptual mechanism, not a list of section titles. Mention sections only after explaining why the components are needed.

## Preliminaries and notation

Include only material used later. Order entries by first use or conceptual dependency.

- State conventions once: graph finiteness, simplicity, loops, parallel edges, sign notation, empty cases.
- Prefer semantic macros for recurring parameters and operators.
- Separate standard cited facts from new lemmas.
- Explain any nonstandard variant of a familiar definition.
- Avoid reproducing an entire textbook background when two definitions and one cited theorem suffice.

## Theorem and lemma presentation

Before a major theorem:

1. ensure every symbol is defined;
2. give the motivation or role if it is not obvious;
3. state all hypotheses in the theorem environment;
4. place exceptions in the statement, not only in the proof;
5. label the result semantically.

Before a technical lemma, add one sentence answering: “What will this lemma unlock?” This sentence may be omitted when the role is immediate.

## Long proof

A long proof benefits from a visible spine:

1. **Setup:** fix the object, extremal choice, or minimal counterexample.
2. **Strategy:** name the invariant, reduction, mapping, decomposition, or estimate.
3. **Structural claims:** isolate reusable consequences.
4. **Construction or estimate:** execute the central mechanism.
5. **Case closure:** show exhaustiveness and handle exceptions.
6. **Return:** explicitly derive the theorem statement.

Use subsections or named claims when they let the reader recover the strategy after interruption. Do not create a subsection for every small calculation.

## Examples, counterexamples, and figures

Use them to perform a logical job:

- show sharpness;
- distinguish two parameters;
- exhibit an exceptional graph or configuration;
- explain a construction used in the proof;
- make a reduction inspectable.

Introduce the job in prose, refer to the item by label, and give a caption that can be understood without reconstructing the entire paragraph.

## Discussion or conclusion

Optional in many mathematics papers. Add one when it can:

- distinguish what was proved from what remains open;
- explain a genuine limitation;
- formulate precise next questions;
- compare mechanisms that were not clear from the proofs.

Do not add a conclusion that merely repeats the abstract.

## End matter

Check venue requirements for:

- acknowledgments and funding;
- conflict-of-interest or data statements;
- AI-use disclosure;
- author affiliations and correspondence;
- MSC classifications and keywords;
- bibliography style and DOI formatting.
