# Staged revision and submission checklists

Run the passes in order. A clean sentence-level pass cannot repair an unstable theorem or a misleading paper-level story.

## Contents

1. Gate 0: research scope and evidence provenance
2. Gate 1: mathematical-content boundary
3. Gate 2: contribution and scope
4. Gate 3: architecture
5. Gate 4: introduction and abstract
6. Gate 5: theorem and proof exposition
7. Gate 6: consistency
8. Gate 7: prose
9. Gate 8: publication hygiene
10. Gate 9: independent review, revision response, and final integrity
11. Minimum single-reader referee simulation
12. Change report format

## Gate 0: research scope and evidence provenance

- [ ] A Research Question Brief fixes the central objects, parameter regime, intended advance, in-scope and out-of-scope literature, and remaining uncertainty.
- [ ] A dated search ledger records databases or corpora, exact queries, terminology variants, citation-chain routes, filters, and inclusion/exclusion decisions.
- [ ] Every candidate source has an exact version, authoritative identifier or URL, access status, mathematical role, and verification status.
- [ ] Preprints, proceedings versions, journal versions, corrections, and errata have been reconciled rather than conflated.
- [ ] A claim-source matrix gives theorem/page/section locators and checks hypotheses, direction, parameter range, exceptions, and conclusion.
- [ ] Primary sources support exact theorem and priority claims whenever accessible; surveys and indexes are not used as silent substitutes.
- [ ] Novelty, priority, best-known, and optimality language is bounded by documented evidence and approved by the author.
- [ ] Counter-evidence searches test for earlier, stronger, corrected, differently named, or genuinely non-comparable results.
- [ ] Access failures and unverifiable claims remain visible and do not receive an implicit pass.

Exit condition: another researcher can see what was searched, what was found, what each source supports, and where uncertainty remains.

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

- [ ] Under this author's house style, the opening paragraph gives the precise central object or parameter, not generic field praise or a textbook notation inventory.
- [ ] After the central definition, the literature moves from the broad problem to the exact subarea and gap.
- [ ] Prior work is organized around the gap.
- [ ] Each cited result has a visible function and enough scope or bound information to locate it in the literature; the introduction is neither under-contextualized nor a citation dump.
- [ ] Literature coverage, ordering, and claim-level verification have been checked as separate tasks.
- [ ] The main theorem is stated, not merely described.
- [ ] Every central classification theorem is stated in the introduction rather than replaced by a forward reference or by a list of the cases that remain open.
- [ ] The contribution is separated clearly from cited results.
- [ ] The end of prior work and the start of the paper's own results are stated explicitly; a reader is not expected to infer authorship from theorem numbering or attribution alone.
- [ ] Each main result is introduced by the exact prior gap it closes, and any known base cases repeated inside a classification theorem are distinguished from the new parameter range.
- [ ] Tightness, limitations, or counterexamples are included when interpretively important.
- [ ] The proof idea and roadmap are concise.
- [ ] Proof methods in the abstract or introduction are presented as a conceptual mechanism, not a tool inventory.
- [ ] The penultimate paragraph or block contains the detailed nonstandard definitions and notation deferred from the opening; elementary definitions familiar to the intended readership are omitted.
- [ ] The final paragraph is only the section-by-section roadmap.
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
- [ ] Minimum dimensions and empty indexed families have been checked for vacuous truth; exception definitions and general bounds agree on the base case.
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
- [ ] Every referenced theorem/claim subitem has its own semantic label, and prose uses `\Cref` so the output includes the full path, such as `Theorem 2.3(ii)` or `Claim 4.1(2)`; no bare `part (ii)`, `item (3a)`, or `For (1)` remains.
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
- [ ] A dedicated West pass has checked Rules 1-92 in `douglas-west-mathematical-writing-checklist.md`; every applicable finding is resolved, and each intentional deviation records its venue, author, or project authority.
- [ ] The West pass covers formula grammar, definitions, hypotheses, quantifiers, comparisons, object/value distinctions, technical terminology, articles, antecedents, conjunctions, punctuation, and the recurrent non-native-English patterns; a clean regex scan is not accepted as completion.
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

## Gate 9: independent review, revision response, and final integrity

- [ ] Referee review remained read-only; reports were written separately from the submitted manuscript.
- [ ] Mathematical-validity, literature/contribution, exposition/notation, adversarial-reader, and editorial/venue lenses were run separately before synthesis.
- [ ] Every finding has a stable ID, exact location, severity, evidence, consequence, confidence, and smallest plausible repair.
- [ ] The synthesis traces every decision-driving point to a finding ID and does not invent or average away disagreements.
- [ ] No Accept or submission-ready verdict remains while a P0 or P1 issue is unresolved.
- [ ] Every editor and reviewer comment appears in the concern ledger; compound requests were split without losing the raw wording.
- [ ] Each promised action has one explicit commitment, required evidence type, target location, stance, and status.
- [ ] Reviewer requests that would make a theorem false, broaden scope without proof, or misstate a source are answered with evidence-based partial agreement or disagreement.
- [ ] Revisions are confined to identified blocks unless a structural rewrite received explicit authorization.
- [ ] Every response-letter claim has been independently checked against the actual revised manuscript.
- [ ] Re-review classifies each concern as fully addressed, partially addressed, not addressed, made worse, or cannot verify, and checks for new issues.
- [ ] The final integrity pass starts from the complete current draft, rechecks all high-risk claims and new citations, and reruns proof, TeX, compilation, and rendering audits.
- [ ] Any same-model-family review limitation and any intentional author override is disclosed.

Exit condition: all review concerns and revision commitments are traceable to evidence in the final manuscript, and the final audit certifies the current artifact rather than an earlier draft.

## Minimum single-reader referee simulation

For a full review or revision-response workflow, use **peer-review-and-revision-response.md**. As a compact minimum, read once without editing and answer:

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
