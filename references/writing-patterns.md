# Writing patterns for publication-level mathematical prose

These patterns were distilled from longitudinal revision histories rather than from isolated final manuscripts. The histories show what changed, when it changed, and which kinds of rewriting survived to the stable versions.

## The governing shift: discovery order to reader order

Notes record what the author tried. Papers present what the reader needs.

| Discovery-order habit | Reader-order revision |
|---|---|
| Introduce objects when they happened to appear | Define them just before their first meaningful use |
| Preserve every attempted proof route | Keep the route supporting the final theorem; archive the rest |
| Announce actions: “now we create...” | State purpose and logical relation: “to establish the bound, define...” |
| Let local lemmas drive the title and outline | Let the final contribution drive title, abstract, and sections |
| Explain motivation after technical work | Give the reader the problem, gap, and theorem before the proof machinery |

Do not assume that a complete-looking source already follows reader order. Before copyediting, propose a second plausible section order based on theorem dependencies and contribution. Retain the source order only after this comparison.

## Paragraph architecture

Give each paragraph one main job. A reliable mathematical paragraph often has:

1. a topic sentence naming the claim or purpose;
2. definitions, evidence, or deductions that perform that purpose;
3. a closing sentence that states the consequence or transitions to the next task.

Split a paragraph when it changes from history to contribution, definition to proof, or one proof case to another. Merge adjacent one-sentence paragraphs when they form one logical unit.

## Logical transitions

Name the relation instead of narrating time.

| Weak diary transition | Strong logical transition |
|---|---|
| Now we consider ... | To handle the remaining case, consider ... |
| So we create ... | Define ... so that ... |
| Next we want to prove ... | It remains to prove ... |
| It is easy to see ... | By [specific definition/claim], ... |
| Clearly ... | State the one-line reason, or omit the adverb |

Useful relation families:

- purpose: `To prove`, `For this purpose`, `To isolate the obstruction`;
- consequence: `Therefore`, `Consequently`, `Combining ... yields`;
- contrast: `By contrast`, `This fails without`, `For general graphs, however`;
- scope: `Under this additional hypothesis`, `Except for`, `In the planar case`;
- closure: `These cases are exhaustive`, `Substituting this bound completes the proof`.

Avoid starting many consecutive sentences with the same transition.

Under this author's house style, do not use `Write`/`We write` as a recurring notation verb, and do not use `as usual` to carry a convention or proof obligation. Replace the former with the exact act (`Let`, `denote`, `represent`, `choose`) and the latter with the convention itself.

## Definitions and notation

- Introduce the mathematical noun before its symbol when possible.
- Use one term for one concept. Do not alternate casually between “minimum deletion set,” “feedback set,” and an acronym unless the relation is defined.
- Distinguish an object from its size and a parameter from an optimizing set.
- State conventions that affect edge cases.
- Use semantic LaTeX commands for recurring operators and names.
- Keep notation local when it is used in only one proof.
- Do not rename notation merely to make it look different from a cited source.

After a major refactor, search globally for the old name, macro, label prefix, and symbol.

## Theorem statements

Write theorem statements for later quotation.

- Make them grammatically complete.
- Put all hypotheses and exceptions in the environment.
- Specify whether graphs are finite, simple, connected, planar, signed, or subcubic when the surrounding convention does not remove ambiguity.
- Use exact inequalities and quantifiers; do not paraphrase a bound differently in the abstract.
- Keep commentary and proof intuition outside the formal statement.
- Attribute named or borrowed results in a uniform form.

## Proof exposition

### Begin with strategy

For a nontrivial proof, tell the reader what is being fixed and what mechanism will finish the argument. A useful opening is more specific than “We prove the theorem.”

### Make dependencies visible

Refer to the exact claim, equation, or construction. Avoid “by the above” when several candidates exist. Use semantic labels so reordering does not create stale references.

### Manage cases

State the partition before entering the cases. Use parallel headings or opening sentences. At the end, say why no case remains.

### Explain calculations at the right level

Do not translate every algebraic step into prose. Do explain:

- why the quantity was chosen;
- where an inequality becomes strict;
- why a denominator is nonzero;
- which hypothesis licenses the estimate;
- how the final expression matches the theorem.

### Avoid unsupported ease claims

Words such as “obvious,” “clear,” and “trivial” rarely help. Replace them with the reason when the step matters; omit them when it does not.

## Literature and attribution

- Cite the primary source for a theorem when feasible.
- Cite a survey for orientation, not as a substitute for the original result when priority matters.
- State what the cited work proves and under which conditions.
- Verify author names, hyphenation, theorem names, dates, and bibliography keys.
- Separate established literature from the present contribution with an explicit sentence.
- Do not rely on author attribution in a theorem heading or on theorem numbering to mark that boundary. End the literature phase explicitly in ordinary prose, using this author's established pattern “In this paper, ... Our first main result ...”; do not insert a standalone bold `Our results` heading. Introduce each result by the precise earlier gap it addresses.
- If a theorem restates known base cases or boundary dimensions to make a classification self-contained, identify those cases as recalled and isolate the genuinely new range.
- Never manufacture a plausible BibTeX record. Use a visible placeholder until verified.

For this author's introductions, define the paper's central object or parameter in the opening paragraph, then develop the historical line from the broad problem to the exact subarea and gap. This order does not license a textbook notation dump: omit elementary definitions familiar to the intended readership, mention complicated neighboring notions only as needed, and collect the remaining specialized definitions near the end. Use the penultimate paragraph or block for those detailed definitions and the final paragraph only for the roadmap.

## Contribution language

Prefer factual verbs:

- `prove`, `establish`, `characterize`, `construct`, `extend`, `sharpen`, `recover`, `relate`, `apply`.

Use `resolve`, `settle`, `first`, `new`, `optimal`, or `best possible` only when the manuscript and verified literature support them. Show significance through the mathematical relation rather than adjectives.

## Title and abstract alignment

A manuscript can pivot after a complete-looking proof draft. When the final conceptual contribution changes, revise all framing:

- title;
- first abstract sentence and result sentence;
- introduction's gap and main-theorem paragraph;
- section titles;
- keywords and terminology.

Do not leave the narrative attached to the first proof route.

## Revision timing

Longitudinal evidence supports this order:

1. grow enough technical material to identify the real result;
2. stabilize theorem scope and proof architecture;
3. delete abandoned routes and reorganize by dependency;
4. write the real abstract and literature framing;
5. perform notation, attribution, grammar, and metadata passes;
6. make small late changes rather than reopening architecture without cause.

This is not a rule that the abstract must always be written late. An early abstract can act as a hypothesis about the paper, but it must be rewritten after the contribution stabilizes.

## Sentence-level style

- Prefer concrete subjects and active mathematical verbs.
- Keep subject and verb near each other when notation is dense.
- Use the present tense for statements in the paper and the past tense for historical actions when needed.
- Prefer `because`, `since`, or an explicit displayed implication over a chain of vague “thus” sentences.
- Remove throat-clearing phrases such as “It should be mentioned that.”
- Avoid promotional openings and generic claims about broad importance.
- Use punctuation as part of displayed mathematics; equations belong to sentences.
- Spell out a number at the beginning of a sentence or rewrite the sentence.
- Check articles, agreement, singular/plural technical nouns, and spacing around inline mathematics.

## What stable final manuscripts tend to contain

- a precise contribution-centered title;
- a self-contained abstract;
- an introduction that defines, situates, states, interprets, and previews;
- content-bearing section titles;
- complete theorem statements and stable labels;
- proof roadmaps for multi-part arguments;
- examples tied to scope or tightness;
- consistent notation and attribution;
- acknowledgments/disclosures required by context;
- no live collaborator notes or unexplained placeholders.

They do not necessarily contain a separate conclusion, a long preliminary section, or every technically correct argument developed during discovery.
