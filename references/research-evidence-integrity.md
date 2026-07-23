# Research evidence and integrity protocol for mathematics papers

This protocol adapts the research, source-verification, claim-audit, and integrity-gate ideas credited in [upstream-academic-research-skills-attribution.md](upstream-academic-research-skills-attribution.md). Use it for Research mode, literature mapping, citation audits, novelty or priority claims, and any manuscript whose introduction depends on external mathematical results.

## Contents

1. Operating boundary
2. Research brief
3. Search ledger
4. Source registry
5. Claim-source matrix
6. Verification ladder
7. Mathematics-specific source hierarchy
8. Novelty and absence claims
9. Counter-evidence search
10. Pre-review integrity gate
11. Final integrity gate
12. Mathematics-specific AI failure modes
13. Required deliverables

## 1. Operating boundary

- Preserve the distinction between discovering sources, verifying bibliographic records, and confirming that a source supports a particular mathematical claim.
- Never infer a theorem statement from an abstract, search snippet, citation graph, review, or another paper's paraphrase when the primary source is available.
- Never describe a search as exhaustive unless the documented method warrants that word.
- Treat missing full text as an access limitation, not permission to guess.
- Keep literature evidence separate from proof evidence. A cited theorem may establish a dependency; it does not prove a new lemma that is not actually contained in the source.
- Apply venue and author conventions only after claim truth, theorem scope, and source support are stable.

## 2. Research brief

Before searching, record:

| Field | Required content |
|---|---|
| Research question | One answerable mathematical question or classification target |
| Central objects | Graph classes, algebraic structures, functions, parameters, or other objects |
| Parameter regime | Ranges, boundary cases, asymptotic regime, and excluded cases |
| Known baseline | Results already supplied or independently verified |
| Intended advance | Extension, sharpening, unification, construction, obstruction, or exposition |
| In scope | Exact theorem families, terminology, periods, and source languages |
| Out of scope | Nearby topics that should not expand the search |
| Uncertainty | What is conjectural, remembered imperfectly, or citation-dependent |
| Deliverable | Research map, bibliography, paper plan, citation audit, or manuscript |

If the question is vague, offer a small set of candidate formulations and explain how each changes the search and proof obligations. Do not pretend that a plausible formulation is the author's chosen problem.

## 3. Search ledger

Make the search reproducible enough for another reader to understand its limits:

| Search ID | Source/index | Query or route | Date | Filters | Snowball path | Result count | Inclusion decision |
|---|---|---|---|---|---|---:|---|

Record:

- databases, publisher sites, bibliographic indexes, preprint servers, author pages, and citation chains actually used;
- exact keyword, subject-classification, author, theorem-name, and citation queries;
- the last search date;
- forward and backward citation searches from anchor papers;
- variant terminology, translated terms, older notation, and alternative spellings;
- inclusion and exclusion reasons;
- access failures and sources known only through secondary references.

Do not count repeated queries as broader coverage. Expand the conceptual vocabulary or source family when the search stalls.

## 4. Source registry

Assign every candidate a stable source ID:

| Field | Required content |
|---|---|
| Source ID | Stable local identifier |
| Exact metadata | Authors, title, venue, year, volume, pages |
| Version | Preprint, accepted manuscript, published version, correction, or erratum |
| Identifier | DOI, arXiv ID, ISBN, or authoritative record |
| Authoritative URL | Publisher, repository, or verified author page |
| Source type | Primary paper, monograph, survey, thesis, proceedings, informal note |
| Access | Full text, partial text, metadata only, or inaccessible |
| Role | Problem anchor, theorem source, historical context, comparison, or discovery lead |
| Verification status | Unchecked, existence verified, metadata verified, content verified |

Reconcile version families. Record theorem numbering and wording for the exact version cited; do not combine a theorem locator from a preprint with metadata from a later version without checking both.

## 5. Claim-source matrix

Create one row for every externally supported high-risk claim:

| Claim ID | Manuscript location | Exact claim | Claim class | Source ID | Source locator | Required hypotheses/scope | What the source establishes | Verdict | Action |
|---|---|---|---|---|---|---|---|---|---|

High-risk classes include:

- exact theorem, lemma, bound, equality case, classification, or complexity attribution;
- priority, novelty, best-known, sharpness, and optimality statements;
- historical sequences and claims that one result strengthens another;
- definitions attributed to a person or paper;
- claims that a known theorem applies to the manuscript's object class;
- negative statements asserting that no result, construction, or counterexample is known.

Use exact locators when possible: theorem number, proposition number, page, section, displayed equation, or quoted hypothesis range. A DOI alone is not a claim locator.

## 6. Verification ladder

Report the highest completed level for each claim:

1. **Internal resolution** — the citation key resolves to a bibliography entry.
2. **Existence** — an authoritative record confirms that the source exists.
3. **Metadata** — authors, title, venue, year, pages, and identifier agree.
4. **Content** — the primary source contains the cited result or statement.
5. **Constraint alignment** — hypotheses, object class, parameter range, exception set, implication direction, and bound match the manuscript's wording.
6. **Version alignment** — the cited version, theorem locator, corrections, and later changes are reconciled.

Use these verdicts:

| Verdict | Meaning |
|---|---|
| VERIFIED | The claim and its constraints match the source |
| VERIFIED_WITH_SCOPE_NOTE | Support is valid only after an explicit limitation is stated |
| MINOR_MISMATCH | Metadata or paraphrase needs correction without changing substance |
| MAJOR_DISTORTION | The manuscript strengthens, broadens, reverses, or misstates the source |
| UNVERIFIABLE_ACCESS | The source appears to exist, but content is unavailable |
| UNVERIFIABLE | The cited source does not establish the claim |
| UNCITED | The claim requires external support but has none |

Do not let an inaccessible source pass a submission-readiness gate for a theorem-level, priority, or optimality claim unless the author explicitly accepts and records the risk.

## 7. Mathematics-specific source hierarchy

Use sources according to the claim, not one universal prestige score:

1. Prefer the published primary paper, official correction, or authoritative accepted version for exact theorem content and priority.
2. Use a verified preprint when it is the only accessible primary text, while recording version and publication status.
3. Use monographs and surveys to orient the field, identify terminology, and discover primary sources; verify exact attributions in the primary source when feasible.
4. Use bibliographic indexes and DOI records for existence and metadata, not theorem content.
5. Use theses, lecture notes, slides, blogs, forums, and informal correspondence as discovery leads or clearly labeled context, not as silent substitutes for primary verification.

A famous source can still be wrong for the adjacent claim. A recent source is not automatically better than the original theorem source. Judge fitness for the claim.

## 8. Novelty and absence claims

- Never certify global novelty from a finite search.
- Bind any novelty statement to the documented search when possible: databases or corpora, date range, last search date, terminology, and nearest prior work.
- Prefer precise relational claims such as “extends Theorem X from class A to class B” to global superlatives.
- Distinguish “we found no such result in the documented search” from “no such result exists.”
- Record the nearest result even when it falls short, and state the exact missing hypothesis, range, construction, or conclusion.
- Require author confirmation for absolute words such as first, only, new, best known, and no previous work.

## 9. Counter-evidence search

For every central positioning claim, deliberately search for:

- an earlier source with the same conclusion;
- a stronger theorem whose scope contains the claimed advance;
- a counterexample or exceptional parameter value;
- an erratum, withdrawal, or later correction;
- a terminology variant that hides the same concept;
- a result in an adjacent subfield stated with different notation;
- evidence that the claimed comparison is non-comparable rather than stronger.

Record convergence and divergence. Do not remove conflicting sources merely because they complicate the introduction.

## 10. Pre-review integrity gate

Before referee simulation:

1. Verify every bibliography entry's existence and metadata.
2. Verify all high-risk claims through constraint alignment.
3. Verify every citation in the abstract and every externally supported main-contribution sentence.
4. Sample lower-risk contextual citations and record the sampling rule.
5. Reconcile preprint, proceedings, journal, correction, and erratum versions.
6. Run the counter-evidence search for novelty and optimality claims.
7. Compare the title, abstract, introduction, and theorem statements with the contribution ledger.
8. Mark every inaccessible or unresolved item; do not downgrade it to a stylistic note.

The gate passes only when no major distortion, unverifiable theorem-level claim, fabricated reference, or unresolved scope mismatch remains.

## 11. Final integrity gate

After revision and re-review, audit the current final draft from scratch:

- recheck all references, including newly added sources;
- recheck all high-risk claim-source rows rather than only the previous findings;
- compare each revised claim with its earlier epistemic strength and scope;
- verify that no hedge, exception, hypothesis, or limitation disappeared without authorization;
- verify every response-letter claim against the actual revised manuscript;
- rerun proof-dependency, TeX, citation, and compilation audits;
- record remaining access limitations and intentional author overrides.

A previous pass does not certify a changed manuscript.

## 12. Mathematics-specific AI failure modes

For each mode, record **CLEAR**, **SUSPECTED**, **INSUFFICIENT EVIDENCE**, or **NOT APPLICABLE**, with a locator and reason:

1. **Invented mathematical content** — a theorem, lemma, example, computation, or proof step was added without supplied or independently verified support.
2. **Hallucinated citation** — the source, metadata, theorem locator, or attributed result is fabricated or conflated.
3. **Theorem-source mismatch** — the source result exists but has different hypotheses, direction, range, exception, or conclusion.
4. **Hidden proof shortcut** — an ease phrase, symmetry claim, reduction, induction step, or “standard” argument conceals an unproved obligation.
5. **Bug or contradiction reframed as insight** — a failed computation, malformed example, or inconsistent case is narrated as a surprising theorem instead of being diagnosed.
6. **False novelty or optimality** — an absolute priority, sharpness, or best-possible claim outruns the documented search or proof.
7. **Version and artifact drift** — the manuscript cites one version, uses another theorem number, or presents a figure/table/computation inconsistent with its source.
8. **Revision strength drift** — a revision silently strengthens, broadens, weakens, or removes a qualifier from a claim without a reviewer request or author decision.
9. **Early frame lock** — later exposition is polished around a problem statement or architecture that no longer matches the actual main theorem.

Any SUSPECTED item affecting a principal theorem, proof closure, citation reality, novelty, or scope blocks a submission-ready label. INSUFFICIENT EVIDENCE remains an explicit author decision, never an implicit pass.

## 13. Required deliverables

Return the artifacts appropriate to the task:

1. Research Question Brief and scope boundary.
2. Search ledger and source registry.
3. Literature map organized by mathematical role, not chronology alone.
4. Claim-source matrix with completed verification levels.
5. Counter-evidence and nearest-prior-work report.
6. Pre-review or final integrity report with failure-mode statuses.
7. A concise list of inaccessible sources, author overrides, and unresolved verification needs.
