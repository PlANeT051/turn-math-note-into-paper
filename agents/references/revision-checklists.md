# Staged revision and submission checklists

Run the passes in order. A clean sentence-level pass cannot repair an unstable theorem or a misleading paper-level story.

## Gate 1: mathematical-content boundary

- [ ] The source claims, hypotheses, exceptions, and proof gaps have been inventoried.
- [ ] No editorial rewrite silently changes a quantifier, graph class, bound, or definition.
- [ ] Unproved or partially proved statements are visibly marked.
- [ ] Proposed stronger statements are labeled as options, not inserted as facts.
- [ ] Citation claims awaiting verification are marked `CITATION NEEDED`.
- [ ] Editorially supplied “standard” definitions or conventions are marked for author confirmation rather than presented as sourced mathematics.

Exit condition: the author can distinguish supplied mathematics from editorial reconstruction.

## Gate 2: contribution and scope

- [ ] A contribution ledger exists.
- [ ] The main theorem is identifiable and fully stated.
- [ ] The gap or prior limitation is precise.
- [ ] The paper's relation to prior work is supported rather than promotional.
- [ ] Important exceptions, tight examples, and limits are visible.
- [ ] Title, abstract, introduction, and theorem agree on scope.

Exit condition: a specialist can say exactly what the paper contributes.

## Gate 3: architecture

- [ ] Before retaining the supplied order, an architecture challenge compared it with at least one dependency-driven alternative.
- [ ] Every inherited section, subsection, and theorem placement has an explicit reader-facing reason; “this is the order in the source” is not a reason.
- [ ] Sections follow logical dependency rather than discovery chronology.
- [ ] Each section has one recognizable job.
- [ ] Subsection titles describe content rather than generic actions.
- [ ] Definitions precede meaningful use.
- [ ] A terminology/notation registry fixes names, symbols, hyphenation, label prefixes, and first-definition locations.
- [ ] Major lemmas have an explained role.
- [ ] Long proofs have a roadmap and visible spine.
- [ ] The literature has a functional map: problem anchor, broad baseline, adjacent regimes, exact frontier, conceptual neighbor, and boundary evidence as applicable.
- [ ] Obsolete proof routes and duplicate setup are removed or quarantined.
- [ ] Examples and figures support scope, construction, or sharpness.

Exit condition: a reader can navigate the argument before checking every proof line.

## Gate 4: introduction and abstract

- [ ] Under this author's house style, the introduction opens with the historical problem and literature trajectory, not a detailed definition/notation block or generic field praise.
- [ ] After the historical trajectory has established the problem, the central object or parameter is defined before detailed prior theorems or the paper's new results.
- [ ] Prior work is organized around the gap.
- [ ] Each cited result has a visible function and enough scope or bound information to locate it in the literature; the introduction is neither under-contextualized nor a citation dump.
- [ ] Literature coverage, ordering, and claim-level verification have been checked as separate tasks.
- [ ] The main theorem is stated, not merely described.
- [ ] The contribution is separated clearly from cited results.
- [ ] Tightness, limitations, or counterexamples are included when interpretively important.
- [ ] The proof idea and roadmap are concise.
- [ ] Proof methods in the abstract or introduction are presented as a conceptual mechanism, not a tool inventory.
- [ ] The abstract answers: object, result, conditions, and significance.
- [ ] The abstract contains no unexplained notation or unsupported superlatives.
- [ ] Keywords are accurate and useful for discovery.

Exit condition: title, abstract, and introduction form a faithful compressed model of the paper.

## Gate 5: theorem and proof exposition

- [ ] Formal statements are grammatical and self-contained under stated conventions.
- [ ] Every symbol in a statement is defined.
- [ ] Proof openings identify setup and strategy when nontrivial.
- [ ] Every major lemma or proposition is introduced by its role in the dependency chain.
- [ ] Every result node has an exact proof span or verified cited source; unresolved status is propagated to all dependent results.
- [ ] Every non-obvious construction is preceded by its purpose.
- [ ] Every intermediate claim is followed by an explicit statement of how it is used.
- [ ] Paragraph boundaries reveal changes of job: setup, construction, claim, case, verification, consequence, or return.
- [ ] Local connectives support, rather than substitute for, the proof's reader-facing architecture.
- [ ] Claims and equations are referred to by stable labels.
- [ ] Every substantial case split names its universe and splitting predicates.
- [ ] Case splits state why they cover all configurations; overlap, boundary values, and coincident objects are handled.
- [ ] Symmetry reductions identify the exact relabeling, switching, reversal, or isomorphism being used.
- [ ] Every minimum-counterexample reduction verifies object class, degree/connectivity hypotheses, strict size decrease, invariant transfer, exception exclusion, and lift-back.
- [ ] Every quantitative reduction records `Δ(size)` and `Δ(parameter)` and checks the exact strict/non-strict threshold algebra.
- [ ] Every transformed cut, signature, or local replacement is shown to be legal and to have the claimed parameter change.
- [ ] Every transformed minimum-counterexample object is checked against all named exceptional graphs or excluded boundary cases; a size inequality alone is not used as a substitute.
- [ ] Every named “third neighbor,” “other endpoint,” unique block, chosen face, or analogous derived object is proved to exist (and to be unique when uniqueness is used) before notation is introduced.
- [ ] Degree sums account for degree-zero classes or prove them empty before omitting them.
- [ ] Every equality characterization proves composition/additivity, the `if` and `only if` directions, and both inequalities behind any claimed exact local loss.
- [ ] Calculations identify the hypothesis or invariant doing the work.
- [ ] Proof endings explicitly return to the claimed conclusion.
- [ ] Reading only proof-paragraph openings and closings still reveals the main dependency spine.
- [ ] “Clearly,” “obviously,” “easily,” and “trivially” do not hide a re-entry, coverage, preservation, or contradiction step.
- [ ] Each unresolved collaborator comment names a checkable proof obligation, and every removed mathematical comment has resolution evidence rather than mere deletion.
- [ ] A backward regression pass confirms that no concrete explanation which once discharged a comment has later been weakened to an ease claim, vague convention, or unsupported assertion.

Exit condition: the prose exposes the logic without pretending to certify correctness.

## Gate 6: consistency

- [ ] One term denotes one concept.
- [ ] Parameter, optimizing set, and cardinality are not conflated.
- [ ] Notation, capitalization, hyphenation, and singular/plural forms are stable.
- [ ] Theorem attributions and author names use one convention.
- [ ] Every numbered theorem-like result, section, figure, and table has one unique semantic label with the project prefix.
- [ ] Theorem-like and section labels follow their environment/heading openings; figure and table labels occur immediately after captions.
- [ ] Internal object references use `\Cref`; no manual `Lemma~\ref`, `Figure~\ref`, or bare `\ref` remains.
- [ ] Every `\Cref` points to the intended object after reordering; custom cleveref names are defined once where necessary.
- [ ] Every cross-reference states a real dependency or comparison; no proof was changed merely to make a stale reference true.
- [ ] Bibliography keys exist and cited results have been verified.
- [ ] High-risk borrowed results record a precise theorem/lemma locator when the source supplies one, and that result's object class, hypotheses, constants, and conclusion match the adjacent use.
- [ ] High-risk external claims have claim-level primary-source verification; metadata lookup alone is not treated as content verification.
- [ ] Figures have referenced captions and consistent notation.
- [ ] Every external graphic/input file exists and every figure has a nonempty caption and stable label.
- [ ] `plane`/`planar`, arbitrary face/outer face, graph/dual graph, and all ambient-set subscripts are used consistently with the proof.

Exit condition: global searches reveal no stale names or references from earlier architectures.

## Gate 7: prose

- [ ] Each paragraph has a primary function.
- [ ] Topic sentences name a purpose or claim.
- [ ] Transitions express logical relations rather than writing chronology.
- [ ] Sentences have concrete subjects and nearby verbs.
- [ ] Displayed equations are punctuated as parts of sentences.
- [ ] Short simple formulas remain inline; central, referenced, long, nested, or multi-step formulas are displayed.
- [ ] Numbered displays are referenced or structurally important; routine unreferenced displays are unnumbered.
- [ ] Multi-line derivations use an appropriate `align`/`aligned` structure and align at meaningful relations.
- [ ] Blank source lines mark genuine paragraph or proof-phase changes, not every display or local deduction.
- [ ] Duplicate words, missing articles, agreement errors, and spacing around math are fixed.
- [ ] Promotional, vague, and meta-writing phrases are removed.
- [ ] House style has been applied semantically: objects are normally introduced with `Let`; generic `we compute` is replaced by the actual consequence; proof announcements use `we prove` rather than `we argue`; and no blind replacement has altered a legitimate technical use.
- [ ] Repeated imperative `Write`/`We write` transitions have been replaced by `Let`, `denote`, `represent`, or an exact conditional parametrization.
- [ ] No proof uses `as usual` as a warrant; every convention and boundary interpretation is stated exactly.
- [ ] Integer parametrizations separate minimum or empty-repetition cases before the general repeated pattern.
- [ ] The author's voice remains recognizable.

Exit condition: the text is precise and unobtrusive enough that the mathematics, not the drafting process, controls attention.

## Gate 8: publication hygiene

- [ ] Root file, document class, title, authors, affiliations, and corresponding-author details are correct.
- [ ] The preamble has no duplicate or obsolete packages, unused drafting macros, or stale template code.
- [ ] Packages, theorem environments, `cleveref` names, semantic macros, reusable TikZ styles, drafting macros, and metadata occur in deliberate preamble blocks before `\begin{document}`.
- [ ] Order-sensitive packages have been checked; in particular, `hyperref` normally precedes `cleveref`, and `color` is not redundantly loaded alongside `xcolor`.
- [ ] Abstract, keywords, MSC codes, acknowledgments, funding, conflicts, data statements, and AI disclosure follow venue policy.
- [ ] No live `TODO`, `xxx`, placeholder citation, colored note, or collaborator macro call remains.
- [ ] For every high-risk removed comment, the final snapshot still contains the proof, citation, scope correction, or replacement route that resolved it; no concrete reason has regressed to an ease word.
- [ ] Commented-out proofs, author conversations, and obsolete bibliography entries have been removed or intentionally retained.
- [ ] No mojibake, replacement characters, or unintended Unicode corruption remains.
- [ ] No duplicate or undefined labels remain.
- [ ] No raw `$$`, stacked blank lines, manual paragraph `\\`, or unexplained `\vspace`/`\\[<length>]` remains.
- [ ] Citations resolve and the bibliography uses the required style.
- [ ] The project compiles from a clean state.
- [ ] First page, theorem numbering, figures, tables, hyperlinks, and page breaks have been visually inspected.
- [ ] A page-by-page display-and-whitespace pass has checked that short displays, one-line paragraphs, floats, and drafting boxes do not create unjustified visual gaps.
- [ ] Every TikZ figure has been visually checked for mathematical incidence, planarity/embedding claims, signs or directions, accessibility beyond color alone, cropping, and legibility at final column width.
- [ ] Overfull boxes and compilation warnings are resolved or documented.
- [ ] Source files contain no private drafting comments that should not be submitted.

Exit condition: the package can be sent to the venue without unexplained drafting artifacts.

## Referee simulation

Read once without editing and answer:

1. What is the main result in one exact sentence?
2. Why was it not already contained in the cited results?
3. Which hypotheses are essential, and where are exceptions discussed?
4. What is the proof's central mechanism?
5. Where would a skeptical reader first lose the dependency chain?
6. Which claim relies on the least clearly verified citation?
7. Does any title or abstract phrase overstate the theorem?
8. Is any section present only because it records the authors' discovery path?

Turn each uncertain answer into an issue before calling the manuscript ready.

## Change report format

Report revisions under four headings:

- **Structural changes:** reordered, merged, split, or removed material.
- **Expository changes:** definitions, theorem statements, roadmaps, examples, and transitions.
- **Mechanical changes:** notation, references, grammar, metadata, and LaTeX hygiene.
- **Author decisions needed:** mathematical checks, citations, scope choices, and optional reframings.
