# Longitudinal evidence behind the workflow

## Corpus and boundary

The workflow was derived from two complete-as-supplied LaTeX revision corpora comprising 129 paired source snapshots and structured diffs:

- a long-form signed-graph paper: 108 daily snapshots from 2025-05-27 through 2025-11-26;
- a rapidly reframed planar-graph paper: 21 scheduled snapshots from 2026-07-11 through 2026-07-17.

The first supplied folder stops at 2025-11-26 even though a separate historical export was previously described as containing two later modification days. Conclusions here use only the 108 source/diff pairs actually available in the analysis folder. All 129 available TeX files had paired parseable diff JSON.

This is a case-based evidence base, not a universal statistical study. Use the recurring mechanisms as practical guidance, not as claims about every field or journal.

## Case A: note scaffold to stable long paper

### Initial state

The first source was a 380-line note-like draft with a lowercase working title, a placeholder abstract, generic section names, sample citation text, colored to-do notes, and proof prose that followed the order of discovery. It already contained mathematical substance, but little reader-facing context.

The author identified this initial draft as their own writing. Do not infer AI authorship from rough grammar, missing background, incomplete cases, or discovery-order exposition; those are development-state signals, not provenance signals.

### Development pattern

| Period | Observable change | Writing lesson |
|---|---|---|
| 27–29 May | Rapid growth from 380 to about 950 lines; labels, cross-references, figures, and theorem naming appeared | Install semantic structure early enough to support refactoring |
| Early June | Proof material expanded beyond 2,200 lines; the outline and small-case thresholds changed repeatedly | Do not over-polish an unstable proof architecture |
| 14 June | More than a thousand inserted and a thousand deleted lines across over 200 blocks | Global rewrites can be normal when notation and proof organization mature |
| 19 June | The first substantive abstract appeared after extensive proof development | Treat an early abstract as provisional; rewrite after the real theorem emerges |
| July–August | Several large deletion waves removed hundreds to nearly two thousand lines; proof routes were consolidated | Productive revision often means deleting a valid but narratively weaker route |
| 12 August | The manuscript shrank from roughly 2,800 to 1,570 lines while adopting a new key-lemma architecture | Coherence and dependency order matter more than accumulated length |
| September–October | Title order, discussion, acknowledgments, literature, and terminology stabilized | Framing and end matter become reliable after the core result stabilizes |
| Late October–November | New root-file packaging, author metadata, a fuller abstract, literature framing, grammar, and attribution passes | Separate submission packaging and copyediting from proof discovery |

### Endpoint

The stable supplied manuscript had about 1,752 lines, a contribution-centered title, a substantive abstract, a literature-led introduction, precise section names, extensive semantic cross-referencing, and no live collaborator annotations or placeholders. The final two supplied snapshots were identical, giving evidence of content stability rather than merely a last edit. Its source still retained technical debt such as repeated or obsolete packages, commented drafting macros, raw display syntax, and some prose that could receive another copyedit; stability is not the same as a clean submission package.

### Strongest transferable observations

- The final outline represented logical dependency, not the chronology of exploration.
- The proof architecture passed through three centers: an injection-based route, a matching-and-path-classification route, and finally a key counting inequality. The decisive 12–13 August rewrite did not merely shorten prose; it replaced a case-proliferating architecture with a more stable invariant.
- The abstract and introduction lagged proof development but were repeatedly aligned once the theorem stabilized.
- Final-artifact lineage showed that mathematical statements often had recognizable early ancestors while their exact wording stabilized much later. Reader-guiding transitions were especially late: most exact-final transition paragraphs appeared only in the last month. Track theorem survival and transition survival separately.
- Early and intermediate annotations exposed incomplete classifications, indistinguishable neighboring cases, and reduction checks such as connectivity and smaller-counterexample scope. These are signals to require a case-coverage certificate and a reduction re-entry ledger, not merely another connective sentence.
- Local author-note macros functioned well as an issue tracker during development, provided live calls reached zero before the endpoint.
- Major deletion events were not regressions; they removed abandoned architectures.
- Late revisions focused on scope language, citation and attribution, terminology, grammar, metadata, and first-page framing.
- Global terminology migrations—title word order, set names, label names, negative-edge notation, hyphenation, and capitalization—show why a terminology registry and stale-name search are necessary after a proof refactor.
- Endpoint survival was not a correctness certificate: the stable source still contained several “easy/clear” assertions at reduction and transformed-cut steps, including at least one place where an earlier draft had contained a fuller justification. A longitudinal audit must mark such artifacts `final-needs-check` instead of treating retention as approval.

## Case B: polished-looking draft to a stronger conceptual paper

### Initial state

The first 514-line source already looked like a complete article: title, real abstract, keywords, introduction, preliminaries, theorem chain, proof roadmap, and bibliography were present. The decisive work was therefore not “write missing sections,” but identify a better conceptual contribution.

The author identified the earliest principal proof as output from GPT-5.6 Pro and the late proof rewrite as the preferred human-authored model. This provenance is treated as case-specific evidence, not as a claim about all model-generated or human prose. The useful contrast is observable in the text: the early proof contained many local connectives but almost no high-level role or purpose transitions, whereas the late proof made the dependency between an intermediate claim, the promised construction, and the theorem conclusion explicit.

### Development pattern

| Period | Observable change | Writing lesson |
|---|---|---|
| 11 July | A self-contained feedback-vertex-set paper existed | Surface completeness does not guarantee the strongest narrative |
| 12 July morning | Title and abstract pivoted toward frustration index; a new theorem chain linked parameters | Frame the paper around the most informative mathematical relation |
| 12 July evening | Roughly half the draft was removed and the proof route rebuilt | Be willing to discard a complete-looking but weaker organization |
| 13–14 July | Literature, main theorem, conceptual bridge, examples, and many collaborator notes developed rapidly | Collaborative annotations are most useful when localized and concrete |
| 14 July | Purpose and role sentences appeared before a new parameter and a key lemma, while the main proof still relied on dense case patches | Good signposting helps, but cannot compensate for an unstable proof architecture |
| 15 July | The central proof was rebuilt around a vertex-ordering invariant and an intermediate claim, then explicitly resumed with the promised spanning-tree construction | Organize a long proof as purpose, claim, use, construction, verification, and return |
| 15–16 July | Proofs, citations, terminology, and references consolidated | Perform consistency after the conceptual pivot, not before it |
| 17 July | Small attribution, grammar, duplicate-word, and notation fixes; final checkpoints nearly unchanged | Stable endpoints are characterized by small, global-consistency edits |

### Endpoint

The final approximately 680-line paper had a new title and abstract, an expanded literature narrative, a theorem relating feedback vertex sets to maximum frustration index, examples delimiting general-graph comparability, a planar theorem, T-join machinery, and an explicit AI disclosure. It did not add a conclusion section because the introduction already performed the needed synthesis.

The content narrative had stabilized, but the supplied endpoint was not literally submission-clean: it retained an empty author field, a commented author note and discarded text, raw `$$` displays, at least one mojibake string, and a few residual phrasing or notation inconsistencies. This distinction is essential: **content maturity and source-package readiness are separate gates**.

### Strongest transferable observations

- A manuscript's story may need to pivot even when every standard section already exists.
- Count meaningful transitions by function, not by words such as `thus` or `hence`. The initial proof was locally connective-rich but reader-guidance-poor.
- A role sentence before a lemma, a strategy sentence at a proof opening, a purpose sentence before a construction, an explicit use after a claim, and a return to the theorem do different jobs; one cannot replace the others.
- If a remark after the proof explains which steps were essential, move enough of that explanation into the proof so it guides rather than merely debriefs the reader.
- Title, abstract, introduction, theorem order, and section names must all change when the conceptual center changes.
- Background matured by function: from five citations on complexity, general planar graphs, and the target conjecture to sixteen citations covering restricted classes, the exact large-girth frontier, recent adjacent work, and the conceptual bridge. The lesson is functional coverage, not citation quantity.
- Counterexamples can be expository infrastructure: they prevent readers from overgeneralizing a comparison.
- The final pass should normalize attribution and notation and catch mundane errors such as duplicate words.
- A conclusion is optional; contribution clarity is not.
- A visually mature PDF can still conceal encoding damage, commented drafting material, empty metadata, or obsolete LaTeX; audit the source separately.

## Cross-case synthesis

### Collaborator-comment trajectories

The histories were also audited specifically for genuine `\Zhou{...}` calls, excluding macro definitions and retaining commented-out calls when they documented a real earlier review issue.

- In Case A, 1,095 calls collapsed to 161 exact texts and 157 contextual threads: 45 primarily concerned cases, 32 reductions, 29 scope, 23 wording, 14 citations, 10 other logical issues, and 4 LaTeX/notation issues. The final supplied snapshot had no live calls.
- In Case B, 111 calls collapsed to 54 exact texts and 30 semantic issues. All 111 occurrences were mapped to an issue and 80 checkpoint-diff blocks recorded their addition, persistence, revision, or deletion. The final supplied snapshot had no live calls.

These counts describe a development process, not error rates or author attribution for later repairs. A daily or scheduled endpoint can show that a genuine Zhou comment existed; it cannot by itself prove who wrote the response.

Several dated paths justify the comment protocol:

- On 29 May in Case A, “this is not a cut” identified that a proposed lift-back set could fail to be a cut. The 30 May revision split the construction according to whether a particular edge belonged to the cut. This is a proof repair, not copyediting.
- From 5 June onward in Case A, reduced objects repeatedly had to be checked against five named exceptions. A smaller vertex count alone did not license minimum-counterexample re-entry.
- On 18 August in Case A, a `why` prompted a concrete explanation that two reduced graphs remained 2-edge-connected. The final manuscript later deleted that reason and reverted to `It is easy to see`. Comment disappearance therefore cannot certify resolution; a final backward check must ensure that the strongest discharge evidence survives.
- During 14–15 July in Case B, repeated questions about why an old tree remained spanning after a vertex split exposed a defective invariant. The successful repair replaced the local extension argument with an odd-predecessor ordering and reconstructed the tree. Repeated comments at the same invariant boundary are a signal to change proof architecture.
- During 13–17 July in Case B, comments corrected `planar`/`plane`, outer/arbitrary face, undefined ambient sets, and a non-planar witness. These are theorem-domain and example-membership checks even when they appear as one-word edits.
- A proposed outer-face formulation in Case B later required its own correction to an arbitrary face. Learn the collaborator's way of forming precise obligations; still verify every proposed replacement.

The transferable rule is **fix or query, then verify**. Repair a deterministic editorial defect directly. When scope, proof, case coverage, a reduction invariant, citation support, or figure validity is uncertain, leave one localized falsifiable query in a neutral editorial voice. Do not impersonate the historical collaborator. Do not remove the query until the revised text, proof, source, author decision, or route replacement is recorded, and recheck the endpoint for regression.

Both histories show that comments can legitimately lead to five different outcomes: local repair, scope correction, supporting citation, replacement of an entire proof route, or deletion of unused material. “The macro call disappeared” is not a sixth resolution type.

### Cross-case revision model

Both histories support a multi-scale revision model:

1. **Content inventory:** find what is actually claimed and supported.
2. **Architecture:** choose the strongest contribution and order dependencies.
3. **Narrative:** define the problem, map the literature, locate the gap, state and interpret the theorem.
4. **Compression:** remove obsolete routes and duplicated setup.
5. **Consistency:** normalize terminology, notation, labels, citations, and attributions.
6. **Publication finish:** abstract, metadata, disclosures, grammar, compilation, and removal of drafting artifacts.

Reversing this order wastes effort. Copyediting prose before a conceptual pivot produces clean paragraphs that may later be deleted.

Do not merge the last two states. A manuscript may be **content-stable** while still failing the **submission gate** because its source contains comments, placeholders, encoding damage, raw display syntax, empty author data, or venue-incompatible packaging.

### Lexical negative evidence

A direct scan of all supplied snapshots gives a useful house-style constraint. In Case A, generic `Write`/`We write` occurs at most once in any snapshot and once in the final snapshot. In Case B, it occurs twice in the earliest snapshots and zero times in the final snapshot. The phrase `as usual` occurs in none of the 129 snapshots. These are not universal frequency targets, but they make repeated imperative `write` and any proof-bearing `as usual` strong review signals for this author's manuscripts.

The same evidence also shows why counts alone are insufficient: the endpoint of Case A still contains several ease claims that deserve logical review. Use lexical counts to find passages, then inspect the proof obligation in context.

## Quantitative signals observed

The following are diagnostic signals, not targets:

- In the long case, line count rose from 380 to more than 2,200, later fell by over one thousand lines during consolidation, and stabilized near 1,750.
- The long case's first real abstract appeared weeks after the first proof scaffold.
- Its largest consolidation replaced over two thousand changed lines in one daily diff.
- In the rapid case, one evening rewrite deleted 268 lines from a roughly 500-line paper, and the largest collaborative checkpoint touched 59 separate diff blocks.
- Several scheduled checkpoints were identical. A timeline should distinguish “no change” from missing data.
- Late-stage diffs in both cases were small and disproportionately concerned framing, names, notation, references, and grammar.

Do not use word count, line count, citation count, or number of sections as a quality score. Use change shape to identify the likely revision phase.

## Limits of inference

- Diff metadata can show which author made a recorded operation, but a daily endpoint diff alone cannot reliably attribute surviving text when intermediate versions are omitted.
- Identical scheduled snapshots do not imply inactivity outside the captured system; they only show no source difference at those checkpoints.
- The analysis intentionally does not certify the theoretical derivations.
- Venue-specific style still overrides generic guidance.
