# Author house style and editorial-comment protocol

This reference combines explicit author preferences with patterns supported by the two longitudinal manuscript histories. Keep those evidence classes separate: an explicit preference applies even if no exact string replacement occurs in the snapshots; a historical inference must be supported by a dated revision path.

## House-style lexical choices

Apply these choices by meaning, not by blind search-and-replace.

| Avoid in the stated use | Prefer | Boundary condition |
|---|---|---|
| `We compute ...` as a generic proof transition | `We have ...`, `Using ..., we obtain ...`, or the actual implication | `compute` remains correct for an algorithm, complexity claim, or genuine numerical/symbolic computation. |
| `Set $X=\cdots$.` when introducing an object | `Let $X=\cdots$.` | Do not replace the noun *set*, set operations, or an imperative that genuinely modifies data. Use `Choose` when an existential choice is being made. |
| `Write $X=\cdots$` or `We write ...` as a repeated notation/parameter transition | `Let`, `denote`, `represent`, or state the exact conditional parametrization | Under this house style, do not use imperative *write* as a default proof verb. A rare literal use about written notation may remain, but repeated use is a failed style pass. |
| `We argue that ...` as a proof announcement | `We prove that ...`, `We claim that ...`, or `It remains to prove ...` | State the exact status: a claim still needs its proof; a consequence may need no announcement. |
| `we got` | `we have`, `we obtain`, or `it follows that` | Match tense and logic rather than replacing mechanically. |
| `and we got the proof` | `This proves the lemma.` or a sentence that names the exact conclusion | The closing sentence must reconnect the last step to the formal statement. |
| `We shall prove ...` | `We prove ...` | Use the direct present tense for the proof now being given. |
| `We discover ...` for a result proved in the paper | `We prove`, `We show`, or `We observe` | Reserve *discover* for genuine historical discussion, not the logical status of a claim. |
| `It implies ...` with no grammatical antecedent | `This implies ...` or name the premise | If several facts precede it, identify which fact is used. |
| `satisfies that ...` | `satisfies ...` or `has the property that ...` | Preserve technical constructions whose accepted name contains *that*. |
| `the common vertex` for two edges | `a common endpoint` | Use *vertex* when the object is not specifically an edge endpoint. |
| `former neighbors` in a vertex ordering | `earlier neighbors` or `predecessors` | *Former* means previous in status; it does not encode an order relation. |
| `with smaller size` | `with fewer edges/vertices than $J$` | Name both the measured quantity and comparison object. |
| `Take the maximum ...` as a proof ending | `Since the bound holds for every $T$, maximizing over $T$ yields ...` | State the domain and the conclusion produced by optimization. |
| `By construction, ...` without a stated invariant | Name the defining clause that gives the property | `By construction` is acceptable only when one nearby construction has one unambiguous relevant property. |
| `It is easy/clear/obvious that ...` | Give the one-line reason or omit the phrase | Never hide case coverage, re-entry, preservation, or a contradiction step behind an ease claim. |
| `As usual, ...` inside a proof | State the convention locally and exactly, or cite the earlier place where it was fixed | Under this house style, *as usual* is not an acceptable warrant. In particular, define how empty ranges, cyclic indices, or degenerate cases are interpreted. |

Prefer exact mathematical verbs: `prove`, `establish`, `define`, `choose`, `construct`, `deduce`, `imply`, and `satisfy`. Do not make the prose artificially repetitive: `we have` is a precise replacement for a generic calculation announcement, not a universal sentence opener.

## Sentence and proof movement

- Introduce notation with `Let`; introduce a deliberate witness with `Choose`; specify a construction with `Define` or `Construct`.
- Treat integer parametrizations as case statements, not as algebraic throat-clearing. Separate the boundary case before introducing a repeated block: for example, handle (r=3) explicitly and, when (r>3), let (s\ge1) be determined by (r=2s+3). Do not hide the boundary in “Write (r=2s+3), where (s\ge0).”
- Say `We prove the claim by induction`, not `We argue ...`, when a proof follows.
- Replace an inventory of actions with a logical role: `To obtain the required pairing, we first order ...`.
- Replace `In the end of this section` by `At the end of this section` only when chronology matters; usually state the result's role instead.
- Use `Indeed,` only when the following sentence supplies the promised verification.
- Use `Conversely,` only for the reverse implication, not for an unrelated contrast.
- Name the comparison in `smaller`, the object in `feasible`, the variable in `take the maximum`, and the source of a contradiction.
- Put a nontrivial reason before its consequence when that makes the dependency explicit: `Since [specific equality or lemma], we have [conclusion]` is stronger than a conclusion followed by a parenthetical `since ...`.
- Keep `plane` for an embedded graph and `planar` for a graph that admits a plane embedding. Do not interchange them when a dual, face, or outer face is used.
- Quantify objects before using derived notation such as an odd-degree set, a dual edge set, or a selected face.
- Prefer `Equality holds for ...` to the non-idiomatic `reaches the equality`.

## Introduction order under this author's house style

Open with the problem's historical trajectory and the mathematical reason the object is being studied. After that positioning, give the exact definitions needed to state the frontier. Do not begin with a textbook block such as “All graphs are finite and simple,” a list of (V(G),E(G),\chi(G),\Delta(G)), or a full Cartesian-product adjacency definition.

An informal mention of the central object may be needed in the historical paragraph, but postpone the detailed notation and routine conventions to a preliminaries section. The preferred order is:

1. historical problem and prior line of work;
2. precise central definition and parameter;
3. known frontier and unresolved gap;
4. present results and their relation to that frontier;
5. proof mechanism and roadmap.

This is a reader-order rule, not a demand for a chronological citation catalogue. Group the history so that it leads to the exact definition and gap.

## What a high-value collaborator comment does

The two histories show that useful comments do not merely polish English. They expose a precise proof or presentation obligation at the smallest location where it becomes visible. Recurrent classes include:

- **definition/scope:** an object, symbol, or graph class is used before it is defined; `plane`/`planar`, arbitrary face/outer face, or theorem hypotheses do not match the argument;
- **logical warrant:** a claimed cut is not shown to be a cut, an edge set is called Eulerian without a reason, or a size comparison lacks its reference object;
- **invariant transfer:** a transformed graph must still be simple, connected, in the theorem's class, and outside named exceptions;
- **induction closure:** the actual base case is missing, or a constructed subgraph is called a spanning tree without proving vertex coverage, connectivity, and acyclicity;
- **case coverage:** conditions on a neighborhood or subcase universe are missing, a symmetry step is unnamed, or a claimed classification omits coincidences;
- **notation identity:** `T`, `T_\sigma`, a dual graph, or an indexed object changes meaning or is used with the wrong ambient graph;
- **literature function:** a claim needs a source, a historical paragraph needs reorganization, or a placeholder attribution is not acceptable;
- **architecture:** a definition is unused, a named notion is unhelpful, two lemmas should be one, or a proof route should be replaced rather than locally patched;
- **example/figure validity:** a purported planar example is not planar, a face is not necessarily outer, or a caption/diagram no longer matches the claim;
- **language with mathematical force:** `why?`, `not clear`, or `what is ...?` identifies a missing dependency rather than a cosmetic preference.

Short comments can be effective when anchored directly after the disputed symbol or claim. Outside such a precise anchor, write the missing obligation explicitly.

## Fix-or-comment decision rule

For every detected problem, choose exactly one path.

In an editing mode, “fix” means change the authorized working copy. In Audit mode or on protected source, it means report a precise `DIRECT FIX` (and, when useful, replacement text) without modifying the file.

### Fix it directly

Fix the text when all of the following hold:

1. the intended mathematical meaning is uniquely determined by the supplied manuscript;
2. the edit does not change a theorem's hypotheses, quantifiers, exceptions, or proof route;
3. the repair is editorial or mechanically verifiable—for example grammar, an established house-style verb, a stale `\Cref`, caption/label order, or an already-proved one-line implication;
4. the change can be checked by search, audit, compilation, or a direct source comparison.

### Leave a localized comment

Leave a comment when the repair requires an author choice, a new proof, a source not supplied, an uncertain figure adjacency, a changed theorem scope, or a choice between proof architectures. The comment must contain:

- the exact object or claim at issue;
- the missing definition, implication, case, invariant, source, or decision;
- why the omission matters to the current theorem or reader;
- the smallest check or repair that would resolve it.

Do not write only `unclear` in an issue report. A local macro call may be concise because its position supplies the object; the accompanying issue ledger must still state the obligation.

## Provenance and macro policy

Never impersonate a collaborator.

- Preserve genuine `\Zhou{...}` comments and their author attribution while they are unresolved.
- Do not insert a new `\Zhou{...}` call on Zhou's behalf unless the user explicitly declares that macro to be a generic editorial channel.
- For Codex-generated notes, use the project's neutral drafting macro, or propose a visibly neutral macro such as `\Editorial{...}` or `\CodexCheck{...}`. If the user explicitly requires use of an existing author macro, prefix the text with `[Codex check]` so provenance remains clear.
- Do not add a new macro to protected source or an audit-only task. Put the same issue in the report with an exact file/line locator.
- A live note is a blocker for `submission-ready`, regardless of its author or color.

## Comment lifecycle

Track each comment as an issue, not as colored prose that may be forgotten:

| Field | Required value |
|---|---|
| ID | Stable issue identifier |
| Location | File, line, environment, and nearby semantic label |
| Type | Logic, scope, definition, cases, citation, structure, language, figure, or TeX |
| Exact question | One checkable obligation |
| Owner | Author, collaborator, or editor/Codex |
| Status | Open, proposed fix, author-confirmed, resolved, or intentionally deferred |
| Resolution evidence | Revised text plus proof/source/compile/version evidence |

Use this lifecycle:

1. **Capture** the exact issue without broadening it.
2. **Classify** whether it is editorial or mathematical.
3. **Trace dependencies** if the issue affects a definition, lemma, theorem, example, or literature claim.
4. **Repair at the right scale.** Some comments need a word; others reveal that an entire route, named notion, or lemma decomposition should be replaced.
5. **Verify the resolution.** Recheck the object class, notation, case coverage, downstream references, compilation, and theorem-return sentence as applicable. A collaborator reply such as `modified` is not evidence unless the revised text actually discharges the obligation.
6. **Remove the live comment only when evidence exists.** Record deletion, rewrite, scope correction, citation addition, or author decision in the ledger.
7. **Recheck the final endpoint against the strongest recorded discharge.** If a later compression deletes the reason and leaves only `easy`, `clearly`, `as usual`, or a bare claim, classify it as a regression and restore the reason or reopen the check.

The histories contain several instructive patterns: a question about whether a constructed graph is planar invalidated an example; an outer-face assumption was generalized to an arbitrary face; missing definitions were repaired by quantifying objects before notation; repeated questions about why an inductively constructed object was a spanning tree exposed a proof-architecture problem and led to a rewritten route; and minimum-counterexample reductions required explicit exclusion of exceptional graphs rather than merely a vertex-count inequality. Generalize the proof obligation, not the paper-specific notation.

Treat the collaborator's method as a model, not every proposed sentence as unquestionable authority. One historical proposed outer-face statement later required its own scope correction. Verify every candidate repair against the theorem and the final proof.

## Final comment audit

Before claiming readiness:

- search case-insensitively for every known author-note macro and colored drafting command;
- inspect commented-out calls as well as live calls;
- require a resolution/evidence entry for every removed high-severity mathematical comment;
- verify that comments were not “resolved” only by deleting the sentence that exposed an unresolved dependency;
- compare the final manuscript with the strongest resolved version of each high-risk issue; do not let a concrete cut, connectivity, or exception argument regress into `easy to see`;
- propagate unresolved status to every dependent theorem and to the title/abstract if the main result is affected;
- report zero live notes only after the final TeX snapshot, not an intermediate file, has been checked.
