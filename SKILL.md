---
name: turn-math-note-into-paper
description: Transform mathematical research notes, proof sketches, partial LaTeX drafts, or rough manuscripts into publication-ready papers while preserving the author's mathematical claims. Use when Codex needs to plan, restructure, draft, polish, or longitudinally audit a mathematics paper; turn an idea-centered note into a reader-centered argument; repair stiff or machine-like proof exposition with paragraph- and architecture-level transitions; test case completeness and minimum-counterexample reductions without inventing mathematics; build the background and literature map; write or revise the title, abstract, introduction, related work, preliminaries, theorem exposition, proof roadmaps, examples, or end matter; normalize notation, citations, theorem environments, semantic labels, `\Cref` cross-references, display mathematics, paragraph spacing, TeX preambles, TikZ figures, author house style, and collaborator-note workflows; or run staged revision and submission-readiness checks.
---

# Turn a Math Note into a Paper

## Purpose

Convert discovery-order notes into a coherent mathematical article without inventing mathematics. Treat proof development and paper writing as related but distinct jobs: preserve the former, redesign the latter around what a reader must know and in what order.

## Non-negotiable rules

- Do not silently change a theorem-level claim, hypothesis, quantifier, exception, or still-used dependency. In an authorized restructure, an obsolete proof route may leave the reader-facing draft only after its removal is recorded and every uncertain or still-dependent mathematical fragment is preserved in the change map or quarantine.
- Never fill a proof gap, strengthen a theorem, assert novelty, or invent a citation. Mark unresolved items visibly.
- Do not insert a “standard” definition or convention that is absent from the source as if the author chose it. Either derive wording from supplied material or mark an editorial option for author confirmation.
- Separate verified facts from editorial suggestions. Use labels such as `MATHEMATICAL CHECK`, `CITATION NEEDED`, and `EDITORIAL OPTION`.
- Work on a copy or a new output file. Do not overwrite source notes unless the user asks.
- Keep the author's established notation and voice when they are consistent; standardize only where inconsistency impedes reading.
- Optimize for a mathematically mature reader: precise, restrained, explicit about scope, and free of promotional language.
- Do not force a conclusion section. Add one only when it contributes synthesis, limitations, or future questions not already handled by the introduction.
- In a mode that authorizes editing, fix an unambiguous editorial defect when doing so preserves the supplied mathematics. In Audit mode, report the exact `DIRECT FIX` without editing the source. If the repair requires a new proof, changed scope, unavailable source, uncertain figure geometry, or author choice, leave or propose a localized actionable comment and record it in the issue ledger.
- Preserve the provenance of genuine collaborator comments. Never manufacture a new `\Zhou{...}` comment as though Zhou wrote it; use a neutral editorial channel for Codex-generated checks unless the user explicitly instructs otherwise.
- Do not treat the supplied section order as an invariant. Preserve mathematical claims, but require the narrative architecture to justify itself against a dependency-driven alternative before sentence-level polishing begins.
- When an author supplies longitudinal histories or explicit house-style corrections, treat the surviving patterns and direct corrections as constraints for later work. Recheck them mechanically; do not rely on having “learned” them in an earlier conversation.

## Route the task

Choose the mode that matches the manuscript's evidence, not its surface polish:

1. **Scaffold** — the input is an idea, outline, or proof sketch. Produce a contribution ledger, dependency map, section plan, and marked manuscript skeleton.
2. **Restructure** — substantial mathematics exists, but the story follows discovery order or contains abandoned routes. Reorder, consolidate, and rewrite transitions while preserving claims.
3. **Polish** — the logical architecture is stable. Improve paragraph function, terminology, attribution, notation, cross-references, abstract, metadata, and sentence-level prose.
4. **Audit** — inspect an apparently finished TeX manuscript for unresolved notes, structural omissions, labels, citations, and publication hygiene.
5. **History audit** — compare ordered snapshots from the final text backward; distinguish surviving, rewritten, late-added, and deleted artifacts; reconstruct architecture changes; and keep textual survival separate from proof verification.

If the mode is unclear, inspect the manuscript and select it from evidence; do not stop merely to ask which label the user prefers.

Before choosing **Polish**, run an architecture challenge: state the paper's conceptual center, assign one function to every section, propose at least one plausible dependency-driven order, and explain why the current order should be retained. If the current order merely follows the source, opens with a textbook inventory instead of the precise central object, buries the broad-to-narrow literature funnel, mixes mathematically distinct result families, or makes a late theorem carry the real contribution, select **Restructure**.

Use honest readiness labels in reports:

- **plan toward readiness** — architecture and issues are mapped, but major content is missing;
- **editorial draft** — a coherent rewrite exists with marked checks;
- **content-stable** — claims and narrative appear aligned, subject to author verification;
- **submission-ready** — content, citations, source package, clean compilation, and venue requirements pass;
- **blocked** — required mathematics, sources, files, or author decisions are unavailable.

## Workflow

### 1. Protect and inventory the source

- Record all supplied files and identify the root TeX file, bibliography, figures, custom macros, and journal class.
- Preserve the source. Put revisions, reports, and temporary compilations elsewhere.
- Read the skill and TeX sources as UTF-8. On Windows, if punctuation appears as mojibake, reread with an explicit UTF-8 decoder before reporting corruption; do not confuse a shell-decoding error with file damage.
- Read the entire note before rewriting isolated sentences.
- Extract existing title candidates, theorem statements, definitions, proof dependencies, examples, limitations, citations, and unresolved annotations.
- When TeX is available, compile from the real root but audit a temporary flattened expansion. Prefer `latexpand --keep-comments <root.tex> --output <audit_flattened.tex>` followed by `python scripts/audit_tex.py <audit_flattened.tex>`; keeping comments prevents percent-escaped DOI/URL text such as `%3C` from truncating a source line, and the audit script removes actual comments before analysis. Do not treat a root-only audit as complete because the script does not expand `\input` or `\include`. If flattening is unavailable, audit every reachable TeX input and state that cross-file label/reference resolution remains limited.

### 2. Build a contribution ledger

Create a compact ledger before drafting prose. For each claimed contribution record:

| Field | Required content |
|---|---|
| Claim | Exact result, construction, method, or counterexample |
| Scope | Objects, hypotheses, parameter range, and exceptions |
| Status | Proved, sketched, conjectured, empirical, or unresolved |
| Relation | What prior result it extends, sharpens, unifies, or reframes |
| Evidence | Theorem/lemma/proof/example location in the source |
| Reader value | Why the result changes understanding or capability |
| Verification need | Mathematical or bibliographic checks still required |

Use the ledger to prevent the title, abstract, and introduction from claiming more than the manuscript establishes.
When evidence is missing, write `UNKNOWN — CITATION NEEDED` or `AUTHOR DECISION NEEDED`; do not infer novelty or reader value from plausibility.

### 3. Map logical dependencies

- List definitions and notation at first genuine need.
- Create a terminology registry for every recurring concept: preferred name, singular/plural, capitalization, hyphenation, symbol or macro, label prefix, and first-definition location.
- Draw a theorem-to-lemma dependency map and identify reusable proof mechanisms.
- Give every result node a proof-closure status: exact proof span, verified cited source, or unresolved. Propagate an unresolved node transitively to every dependent result; a stated lemma is not a proved lemma.
- Separate structural lemmas, technical estimates, small cases, constructions, and applications.
- Identify duplicate arguments and obsolete proof routes. Do not delete uncertain material silently; move it to an editorial appendix or report it.
- Choose section order by reader dependency, not by the chronology of discovery.
- For case-heavy or minimum-counterexample arguments, build a proof-obligation ledger before polishing prose. Distinguish a missing explanation from a possible mathematical gap.

Use this minimal dependency-map schema:

| Node | Kind | Depends on | Source location | Status | Proposed reader location |
|---|---|---|---|---|---|
| Stable semantic name | definition/result/example | prerequisite node names | supplied file/line or note heading | proved/sketched/unresolved | section/subsection |

### 4. Design the reader-facing architecture

Load `references/section-blueprints.md` when creating or substantially changing sections.

- Put the principal result where the introduction can state it precisely.
- Give each section one identifiable job and each subsection a content-bearing title.
- State a proof roadmap when the main argument has multiple mechanisms or dependencies.
- Place examples and figures where they clarify scope, tightness, non-comparability, or a construction—not as decoration.
- Keep preliminaries selective. Move standard background to concise definitions and citations; retain only material used later.
- Produce a short architecture decision before rewriting: `current order | alternative order | dependencies | reader benefit | decision`. The supplied order earns retention only if it is better for the reader.
- Split a source section when its parts serve different theorem families or dependency chains; merge sections that repeat one mechanism. A file boundary inherited from the source is not a mathematical structure.

### 5. Draft the mathematical exposition

Load `references/proof-exposition-and-transitions.md` when a proof is long, case-heavy, locally fluent but globally stiff, or being rebuilt from a proof sketch.
Also load `references/proof-logic-case-coverage-and-survival.md` for minimum-counterexample reductions, repeated object transformations, case-completeness questions, or longitudinal comparison of surviving and deleted proof material.
Load `references/latex-microformatting.md` whenever drafting, editing, or auditing TeX source.
Load `references/author-house-style-and-editorial-comments.md` whenever drafting, editing, or auditing prose or live collaborator notes.
Load `references/latex-project-structure-and-tikz.md` whenever changing or auditing a preamble, theorem environment, package list, figure, subfigure, or `tikzpicture`.

- State each theorem with complete hypotheses and stable notation before discussing its proof.
- Introduce a lemma by explaining its role when that role is not obvious from the statement.
- Distinguish local logical continuity (`since`, `thus`, `hence`) from reader guidance. A mature proof also says why a lemma is needed, what a construction will unlock, how an intermediate claim is used, and how the argument returns to the theorem.
- Start proofs with the setup and strategy; then organize long arguments around the spine `purpose → claim → explicit use → construction → verification → consequence → return`. Use named steps or cases only when they expose real structure.
- Give each proof paragraph one primary job. At genuine phase boundaries, add a role, purpose, use, consequence, or closure sentence rather than another generic connective.
- Make case coverage, symmetry reductions, exceptional configurations, and termination explicit. Supply a coverage reason: define the universe and splitting predicates, handle overlap and coincidences, justify symmetry, and close the cases back to one conclusion.
- Audit vacuous quantification and empty indexed families at the minimum dimension. A condition imposed only on objects indexed from (2) through (d) is automatically true when (d=1), and may silently move the base case into an exceptional class.
- For every reduction, verify that the new object re-enters the theorem's scope, is strictly smaller in the induction parameter, avoids named exceptions, preserves the required invariant, and lifts the conclusion back.
- Record the reduction arithmetic explicitly—at minimum the size change and parameter change—and check that they preserve the strict inequality needed for minimality.
- After proving an intermediate claim, reconnect it to the promised construction or bound. After a dense calculation, interpret the property it establishes.
- End a proof by reconnecting the last calculation or claim to the theorem's conclusion.
- Give numbered results, sections, figures, and tables stable semantic labels; use the project's consistent prefixes and place labels where the counter is set.
- Under this user's house style, use `\Cref` for internal theorem, lemma, equation, section, figure, and table references; do not hand-write `Lemma~\ref` or use bare `\ref`. Keep bibliographic citations in the project's citation system.
- Verify the semantic target of every cross-reference. Do not alter a proof or invent a dependency merely to make a stale reference true; remove the unsupported role claim or mark it for author confirmation.
- Treat blank source lines as real paragraph boundaries. Do not use stacked blank lines, `\\`, or arbitrary `\vspace` for ordinary exposition.
- Keep short, simple formulas inline; display central, referenced, structurally complex, or multi-line formulas in semantic `equation`/`align` environments, with sentence punctuation and no raw `$$`.
- Apply the author's lexical preferences by meaning: use `Let` to introduce an object, prefer an exact `we have`/`we obtain` consequence to generic `we compute`, and use `we prove` rather than `we argue` when announcing a proof. Do not perform blind global replacements.
- Under this house style, review every imperative `Write` and every `We write`. Prefer `Let`, `denote`, `represent`, or the exact conditional relation; repeated `write` is a failed prose pass even when each occurrence is grammatical.
- Do not use `as usual` as proof support. State the convention, boundary interpretation, symmetry, or earlier result explicitly.
- For parametrized periodic constructions, separate the boundary case before the repeated pattern. Handle \(r=3\) explicitly; only then introduce \(s\ge1\) for \(r=2s+3\), or give an equally explicit case formulation.
- Treat `plane`/`planar`, arbitrary face/outer face, graph/dual graph, and ambient-set subscripts as mathematical distinctions, not stylistic variants.

Do not spend time beautifying prose in a proof branch that may still be discarded. First stabilize the claim and proof architecture, then polish.

### 6. Write the introduction as an argument

Load `references/writing-patterns.md` for paragraph-level style and narrative moves.

Before drafting prose, build a citation map with these functions: problem anchor or complexity; broad baseline; adjacent regimes or subclasses; exact frontier and recent progress; conceptual neighbor; boundary or tightness evidence. Mark an empty function `CITATION NEEDED`; never invent a source.

Organize the literature from the broad problem toward the manuscript's exact regime. For every cited result, record enough of its object, scope, bound, and role to show how it locates the gap. Add literature in separate coverage, ordering, and claim-level verification passes; citation count is not a quality measure.

End the prior-work phase with an explicit contribution boundary. Do not expect attribution in a theorem heading, a change of citation density, or theorem numbering to tell the reader which results are new. Under this author's house style, make this boundary in ordinary prose, for example, “In this paper, we study ... Our first main result ...”; do not add a standalone bold `Our results` heading unless the author or venue requests one. Then introduce each main result by stating which cited gap it closes. If a formal theorem repeats known boundary cases for completeness, identify the known cases and the genuinely new range before the statement.

State every principal contribution formally in the introduction when its hypotheses and cases are needed to understand the paper's scope. Do not replace a central classification theorem with a forward reference to a later section or with a paragraph emphasizing only its unresolved cases. If the formal statement needs specialized notation, define the minimum notation immediately before it near the end of the introduction.

Under this author's explicit house style, open with the precise definition of the paper's central object or parameter. This opening may repeat the abstract's short definition. Do not replace it with “All graphs are finite and simple,” a list of routine symbols, or a full textbook definition of familiar objects. After the central definition, organize the literature from the broad problem to the exact subarea. Mention a complicated neighboring notion briefly when it first becomes relevant, but postpone its full definition and the remaining specialized notation until the end of the introduction unless a formal statement would otherwise be meaningless.

Build the introduction in this functional order, adapting rather than mechanically copying it:

1. Define the central object or parameter precisely and compactly.
2. Develop the literature from the broad problem to the manuscript's exact subarea.
3. State the known frontier and formulate the precise unresolved question, limitation, or conceptual disconnect.
4. Mark the transition from prior work to the present paper explicitly, then state the main theorem or theorems with their scope and exceptions.
5. Explain the contribution in relation to prior work, including tightness, limitations, counterexamples, or a proof idea only when they help interpretation.
6. In the penultimate paragraph or block, collect the detailed nonstandard definitions and notation needed later but not needed earlier to understand the formal results.
7. Use the final paragraph only for the section-by-section roadmap.

If a complex definition is indispensable to a theorem stated earlier, give the minimum precise version at first use and consolidate the remaining conventions in the penultimate block. Elementary definitions familiar to the intended readership need not be restated.

Prefer a chronological literature list only when chronology itself explains the problem's development. Otherwise organize prior work by mathematical role.

When the paper creates a bridge between two objects or parameters, motivate both sides, explain their general relation or non-relation, and use boundary examples before stating the restricted comparison theorem. Introduce each theorem or proposition by its role and state explicitly which results combine to yield the main theorem.

### 7. Write title, abstract, and keywords after the result stabilizes

- Make the title name the actual mathematical object and contribution; avoid titles inherited from an abandoned proof route.
- Make the abstract self-contained at the level of problem, gap/context, main result, scope, and significance.
- Define specialized terms or parameters before using symbols in the abstract.
- State exceptions and conditions that materially change the result.
- Omit citations, proof details, proof-tool inventories, and promotional adjectives unless a venue or context truly requires them. If method is central, describe the conceptual mechanism rather than listing every technical ingredient.
- Choose keywords that support discovery and do not merely repeat every title word.

Recheck that title, abstract, introduction, and theorem statements all describe the same contribution.

Whenever a main theorem, hypothesis, exception, equality case, or claimed application changes, immediately resynchronize the title, abstract, introduction contribution paragraph, roadmap, section names, figures/captions, and any discussion of future work.

### 8. Refactor and compress

- Delete or quarantine abandoned proof paths once the surviving route is verified by the author. Deletion from the reader-facing draft does not authorize silent loss: record the route in the change map, retain any still-dependent lemma, and quarantine uncertain mathematical content rather than discarding it.
- Merge repeated definitions, observations, and setup paragraphs.
- Replace diary-like transitions (`now we try`, `so we create`, `next we want`) with logical relations (`to prove`, `by contrast`, `it remains to show`).
- Reorder material so prerequisites precede uses and consequences follow the results they depend on.
- Preserve useful negative examples and failed comparisons when they clarify the theorem's boundary.
- If classifications and patch lemmas keep multiplying, pause local repair and test whether a stronger invariant, count, or structural lemma can replace the route.
- Treat repeated collaborator questions at the same invariant boundary---for example, repeated `why`, `proof incomplete`, or `what is the contradiction`---as evidence that the proof architecture itself may be defective. Do not keep accumulating local patches without first testing a replacement route.

Large deletion is acceptable when it removes a weaker narrative or obsolete proof architecture. Measure progress by coherence and support for the main claim, not by manuscript length.

### 9. Run separate consistency and prose passes

Do not mix every kind of revision in one pass. Use this order:

1. theorem and scope agreement;
2. logical structure and dependency order;
3. terminology and notation;
4. citations, attributions, labels, and cross-references;
5. proof spine, paragraph function, and reader-guiding transitions;
6. sentence-level grammar and concision;
7. title, abstract, keywords, authors, acknowledgments, disclosures, and venue metadata.

Use `references/revision-checklists.md` for the gates and final checklist.

### 10. Audit and verify

- Generate a temporary flattened TeX file from the root with `latexpand --keep-comments`, then run `python scripts/audit_tex.py <audit_flattened.tex> --json <report.json>`. Compile the original root separately. If the project cannot be flattened, audit every reachable input and disclose the script's cross-file limitation.
- The audit script intentionally exits nonzero when the selected `--fail-on` severity is found. Treat a parseable report/JSON plus expected finding exit as a successful audit with findings; distinguish it from a crash, unreadable input, or missing output.
- Resolve or report every error and warning; rerun until the remaining items are intentional.
- Compile the project when a LaTeX runtime is available. Inspect undefined references, citations, overfull boxes, theorem numbering, figure placement, and bibliography output.
- Compare the compiled first page with the contribution ledger: title, abstract, theorem scope, and terminology must agree.
- Search for live collaborator macros, colored notes, `TODO`, `xxx`, placeholder citations, duplicate words, and stale section references.
- Search case-insensitively for generic `write`, `as usual`, ease claims, and diary transitions. Review every hit in context, and compare the frequency with any supplied author-history corpus rather than accepting repetition because each sentence is locally grammatical.
- For every resolved mathematical comment, retain a discharge record and run a final backward regression check. If a concrete reason, case split, or invariant check has later been compressed to `easy`, `clearly`, `as usual`, or an unsupported assertion, restore the strongest justified explanation or reopen the comment.
- Render every page and perform a display-and-whitespace pass; zero stacked blank source lines does not establish good visual density.
- Treat a clean mechanical audit as necessary but not sufficient. Perform a final reader pass from beginning to end.

`audit_tex.py` checks source mechanics, not theorem agreement, proof correctness, novelty, whether an example satisfies a theorem's hypotheses, or whether a citation actually supports the adjacent claim. Check those separately with the contribution ledger, dependency map, source verification, and referee simulation.

Report citation verification at three distinct levels:

1. **internal resolution** — every citation key maps to an available bibliography entry;
2. **metadata verification** — author, title, venue, year, pages, and identifier match an authoritative record;
3. **claim-level verification** — the primary source actually supports the adjacent theorem, bound, priority, or historical claim with the stated hypotheses.

Publication readiness requires claim-level verification for high-risk assertions such as named theorems, numerical bounds, complexity results, priority, novelty, and optimality. Do not imply that metadata verification proves content support.

If the task is audit-only or the source is protected, do not “resolve” findings by editing it. Reporting all findings, blockers, and proposed repairs is the terminal action.

## Collaboration-note protocol

Localized author macros and colored annotations can be useful during development. Use each note as a concrete issue with an owner or decision, not as a substitute for prose. Before submission:

- maintain an issue ledger with `ID | location | type | severity | issue/question | owner | status | resolution/evidence`; classify at least mathematical gap, missing definition, citation, scope, example/figure, language, and LaTeX;
- repair an issue directly only when the intended meaning is unique and the edit is editorial or mechanically verifiable; otherwise leave a comment identifying the exact object, missing obligation, why it matters, and the smallest author decision or proof needed;
- preserve genuine collaborator attribution, and place new Codex/editorial comments in a neutral macro or in the report rather than impersonating an author;
- resolve, move to an issue report, or explicitly defer every live note;
- do not mark a comment resolved merely because its sentence was deleted; record whether the dependency was proved, cited, scope-corrected, replaced by a new route, or author-confirmed;
- remove live calls while allowing harmless macro definitions to remain only if the venue permits them;
- verify that resolving a note did not silently change a theorem's scope;
- require zero unexplained placeholders in the final TeX.

## Resource routing

- Read `references/section-blueprints.md` when drafting or reorganizing sections.
- Read `references/writing-patterns.md` when revising style, narrative, theorem exposition, or transitions.
- Read `references/proof-exposition-and-transitions.md` when revising proofs, diagnosing stiff machine-generated prose, or strengthening lemma roles and transitions within or between proof phases.
- Read `references/proof-logic-case-coverage-and-survival.md` when auditing version histories, distinguishing final survival from correctness, testing case completeness, or checking reductions and transformed objects.
- Read `references/latex-microformatting.md` whenever creating or changing TeX; it defines semantic labels, `\Cref`, blank-line and vertical-space rules, inline/display decisions, equation punctuation, and float conventions.
- Read `references/latex-project-structure-and-tikz.md` for preamble organization, environment definitions, package hygiene, TikZ source conventions, subfigures, accessibility, and compiled visual checks.
- Read `references/author-house-style-and-editorial-comments.md` whenever revising prose or handling collaborator notes; it defines this author's lexical preferences, the fix-or-comment boundary, annotation provenance, and the comment-resolution lifecycle.
- Read `references/revision-checklists.md` for staged reviews and submission readiness.
- Read `references/longitudinal-evidence.md` when coaching a long revision process, deciding whether a large rewrite is warranted, or explaining why the workflow uses separate discovery, architecture, and polish phases.
- Do **not** read `references/longitudinal-evidence.md` during a blind or single-snapshot Audit unless the user explicitly asks for historical comparison; it contains later-snapshot case evidence that can contaminate a forward audit.
- Run `scripts/audit_tex.py` whenever a TeX source is available. The script audits writing mechanics and project hygiene; it does not validate mathematics.

## Output contract

In Scaffold, Restructure, or Polish mode, unless the user requests a different deliverable, return:

1. a revised TeX file or a marked manuscript skeleton;
2. a short change map organized by structure, exposition, and prose;
3. the contribution ledger;
4. a list of unresolved mathematical and citation checks, clearly separated from editorial options;
5. the audit result and, when possible, compilation status.

In Audit mode, do not create a revised TeX file unless the user asks. Return:

1. the readiness label and verdict;
2. a contribution/scope consistency report;
3. the issue ledger, separated into mathematical, citation, editorial, and TeX/package findings;
4. mechanical audit and clean-compilation results;
5. the minimum repairs and author decisions required to advance to the next readiness state.

If the user requests a focused or concise audit, bound the report to that scope. State which passes were and were not run, surface any discovered blocker that invalidates the requested conclusion, and do not imply that omitted citation, proof, compile, or venue checks passed.

In History audit mode, keep every supplied snapshot read-only and return:

1. a final-artifact lineage table for introduction claims, transitions, formal statements, definitions, and proof mechanisms;
2. a deleted-route table that distinguishes incorrect/incomplete, scope-changing, architecturally obsolete, duplicative, discovery-only, moved, and merely immature material;
3. the reader-facing architecture timeline and theorem-dependency changes;
4. a proof-obligation and case-coverage ledger with `historically repaired`, `route replaced`, `textually unresolved`, and `author verification needed` kept distinct;
5. a collaborator-comment resolution table with first occurrence, first plausible repair, final-snapshot retention, outcome, and dated locators; never equate comment deletion with resolution;
6. residual endpoint issues and reusable revision rules, with dated evidence locators.

Never assign the **submission-ready** label while unresolved mathematical checks, invented/unverified citations, broken references, or unexplained placeholders remain. If the user says “publication-ready,” interpret it as this same strict gate.
