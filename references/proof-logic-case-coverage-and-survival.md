# Proof logic, case coverage, and textual survival

Use this reference when a manuscript has a long version history, a case-heavy proof, a minimum-counterexample argument, repeated graph transformations, or a proof route that has accumulated many patch lemmas.

The central distinction is:

- **textual survival** asks whether an idea or sentence remains in the final manuscript;
- **expository maturity** asks whether it is stated clearly, precisely, and in the right place;
- **logical support** asks whether every proof obligation is actually discharged;
- **mathematical correctness** remains an author/referee judgment unless the argument has been independently verified.

Never use survival as a certificate of correctness. A final version can retain a grammatical error, an unsupported “easy” step, or a hidden case gap.

## 1. Audit a version history from the final text backward

Start with final artifacts rather than with every early sentence. Inventory:

1. introduction claims and literature functions;
2. section- and proof-level transition paragraphs;
3. theorem, lemma, proposition, corollary, and conjecture statements;
4. definitions and notation on which those statements depend;
5. proof mechanisms and named constructions.

For each final artifact, trace the earliest recognizable ancestor, major semantic rewrites, the first near-final formulation, and the first exact-final formulation. Record one of these statuses:

| Status | Meaning |
|---|---|
| `early-survivor` | The mathematical and rhetorical function was present early and remained |
| `rewritten-survivor` | The underlying idea survived, but scope, hypotheses, terminology, or prose changed materially |
| `late-addition` | The final artifact entered only after the proof or paper architecture stabilized |
| `deleted-route` | It belonged to an abandoned proof or narrative architecture |
| `temporary-scaffold` | It organized discovery but was not intended as final exposition |
| `final-needs-check` | It survives in the endpoint but still has a language, support, or logic concern |

Use semantic matching, not exact string matching alone. Renamed objects, relabeled theorems, split or merged paragraphs, and changed notation can hide continuity. Conversely, shared vocabulary is not enough to claim that two statements are the same theorem.

For every lineage claim, cite the dated snapshot and a short locator. If authorship metadata is available, keep it separate from text comparison: a daily endpoint diff can identify what changed that day, but cannot assign an earlier unchanged substring to an author without the intermediate event chain.

For every high-risk collaborator comment, also perform a forward resolution check: locate the first version that appears to discharge it, classify the repair, and then verify that the decisive reason survives in the final snapshot. A comment can disappear while a detailed connectivity, cut-validity, exception, or case-coverage argument later regresses to `easy to see`.

Do not infer human or AI provenance from stiffness, grammar errors, missing transitions, or proof incompleteness. Record provenance only when the user supplies it or reliable authorship metadata supports it.

## 2. Interpret deletion by function

Classify deleted material before drawing a lesson:

- **incorrect or incomplete** — a proof note, counterexample, or later correction exposes a defect;
- **scope-changing** — hypotheses, exceptions, equality cases, or the claimed bound changed;
- **architecturally obsolete** — a different invariant or dependency chain replaced the route;
- **duplicative** — another lemma or paragraph performs the same job more directly;
- **discovery-only** — exploratory classifications, questions, or provisional notation helped find the proof;
- **expositorily immature** — the claim may be useful, but its wording, placement, or motivation failed;
- **moved** — the content survives elsewhere and must not be counted as deleted substance.

Do not describe all large deletions as “polish.” A proof architecture can be abandoned even when many local calculations are usable. Preserve the mathematical reason for the change in the analysis.

## 3. Build a proof-obligation ledger

For each theorem and each nontrivial lemma, create:

| Result | Intended conclusion | Direct dependencies | Proof mechanism | Open obligations | Evidence location | Status |
|---|---|---|---|---|---|---|

An obligation is smaller and more testable than “check the proof.” Typical obligations are:

- a construction is well-defined;
- a transformed object remains in the theorem's class;
- an invariant or objective value is preserved or changes by the stated amount;
- a smaller counterexample is genuinely smaller;
- a claimed cut, path, cycle, matching, or partition has the required property;
- a counting identity counts each object exactly once or with the stated multiplicity;
- a case list covers all possibilities;
- an equality condition is necessary as well as sufficient;
- an exception family is excluded or handled;
- the last derived fact implies the stated conclusion.

Mark each obligation `discharged`, `textually under-justified`, `historically repaired`, `author verification needed`, or `open`. Never silently supply a missing mathematical argument.

### Require a proof-closure certificate

For every result node, record exactly one of:

- `proved at <span>` — a complete proof is present at a precise source span;
- `proved by <verified citation>` — the cited source and applicable hypotheses have been checked;
- `assumed/provisional` — the manuscript deliberately postpones or assumes it and says where closure will occur;
- `unresolved` — the result is statement-only, lives inside a drafting note, contains an explicit incomplete marker, or lacks the claimed proof.

Propagate `unresolved` transitively through the dependency graph. A clean conditional proof of the main theorem remains conditional when its key lemma or any transitive dependency is unresolved. Require an explicit return sentence when the deferred proof finally closes the earlier conditional argument.

## 4. Require a case-coverage certificate

A list headed “Case 1, Case 2, ...” is not evidence of completeness. Every substantial case split should answer:

1. **Universe** — what configurations are being classified?
2. **Splitting predicates** — which exact properties determine the branches?
3. **Coverage** — why does every configuration satisfy at least one branch?
4. **Disjointness or overlap** — is this a partition or merely a cover? If branches overlap, why is that harmless?
5. **Symmetry** — which relabeling, switching, reversal, or isomorphism identifies omitted-looking cases?
6. **Coincidences** — what changes when nominally distinct vertices, sets, paths, or endpoints coincide?
7. **Boundary values** — are empty, singleton, equality, minimum-size, and maximum-size cases included?
8. **Closure** — after the last case, what common conclusion has been established?

Use a compact certificate:

| Branch | Predicate | Symmetric representatives omitted | Coincidences/boundaries | Conclusion | Coverage reason |
|---|---|---|---|---|---|

Red flags include:

- successive patches named after newly discovered configurations;
- “otherwise” with no stated negation of the earlier predicates;
- the same subcase appearing twice under different notation;
- an unexplained jump from “at least one of” to “without loss of generality”;
- diagrams treated as if they enumerate all embeddings;
- a proof note asking “what is the difference?” between adjacent cases;
- removal of a completeness comment without adding a mathematical coverage sentence.

When a classification keeps growing, stop sentence-level polishing. Ask whether a stronger invariant, counting identity, or structural lemma can replace the enumeration.

## 5. Audit minimum-counterexample and reduction arguments

Every reduction from an alleged minimum counterexample `G` to a new object `G'` needs a re-entry certificate. Adapt these fields to the theorem:

| Obligation | Question |
|---|---|
| Well-defined | Are all added, deleted, identified, or switched elements specified unambiguously? |
| Object class | Is `G'` still simple/multi-, signed/unsigned, finite, and otherwise of the required type? |
| Degree condition | Is the required subcubic, cubic, regular, or degree constraint preserved? |
| Connectivity | Is `G'` connected, 2-edge-connected, or otherwise inside the theorem's domain? |
| Size decrease | Is the induction/minimality parameter strictly smaller? |
| Parameter relation | How do cuts, signatures, frustration, weight, or another objective transfer between `G` and `G'`? |
| Exception exclusion | Why is `G'` not one of the small or named exceptional objects? |
| Lift back | How does a solution or contradiction for `G'` return to `G`? |

Do not compress two or more of these into “it is easy to see” when they carry the contradiction. If a historical draft contains the missing verification and the final version deletes it, flag the final step for restoration or author confirmation.

Add a one-line arithmetic certificate for quantitative reductions:

| Reduction | Size change `Δn` | Parameter change/bounds `ΔF` | Strict target before | Strict target after | Valid? |
|---|---:|---:|---|---|---|

Do the algebra with the exact strict or non-strict inequality used by the counterexample. A claimed loss of one versus two units can change whether minimality yields a contradiction.

## 6. Audit transformed cuts, signatures, and local replacements

For a transformed set or cut, verify separately:

1. it is actually a cut in the transformed or original object;
2. every edge whose status changes is listed;
3. signs, weights, or membership are transported under a stated map;
4. the claimed positive/negative imbalance or objective change follows from an explicit count;
5. the reverse transformation reconstructs a legal object;
6. no exceptional adjacency or vertex coincidence invalidates the argument.

A displayed equality is not a substitute for defining the correspondence that makes it true.

### Equality characterizations need two independent proofs

For a statement of the form “equality holds if and only if the object has structure `S`,” audit four layers separately:

1. **additivity or composition** — prove how the optimized parameter behaves across blocks, sums, or glued components;
2. **if direction** — exhibit a legal object/signature/solution and prove it is optimal, not merely that it has the advertised value;
3. **only-if direction** — show that every strict deviation from `S` forces slack in the bound;
4. **local loss** — when deleting a block or replacing a gadget, prove both inequalities behind an asserted exact change such as `F(G')=F(G)-c`.

Keep construction closure, parameter transfer, and structure identification separate. Counting the negative edges in one representative signature supplies an upper bound; it does not by itself prove the frustration index equals that count.

## 7. Distinguish logical transitions from connective words

Proof maturity is visible at several scales:

- **section transition** — why the next section is needed;
- **lemma-role transition** — what later step the lemma unlocks;
- **proof-roadmap transition** — the phases of a long proof;
- **construction-purpose transition** — why an auxiliary object is introduced;
- **claim-use transition** — how the proved claim is now used;
- **case-closure transition** — why the cases cover the universe and yield one conclusion;
- **theorem-return transition** — how the final fact proves the announced result.

Words such as `thus`, `hence`, and `next` provide local cohesion but do not perform these jobs automatically. Track the first appearance and stabilization of functional transitions separately from theorem statements; in real histories, theorem ideas can stabilize months before reader guidance does.

For auxiliary-graph degree sums, enumerate degree-zero classes before replacing a vertex-set cardinality by a sum over positive degrees. If `Y=Y_0\cup Y_1\cup\cdots`, prove `Y_0=\emptyset` or retain `|Y_0|` in the identity.

## 8. Decide whether to repair or replace a proof route

Prefer local repair when the dependency spine is stable and the missing obligations are few and independent. Consider architectural replacement when several of these occur together:

- the number of types and subtypes keeps increasing;
- each new configuration needs a new patch lemma;
- the same invariant is recomputed in many cases;
- annotations repeatedly question coverage or distinguishability;
- the argument is much longer than the theorem's conceptual content;
- deleting one classification layer reveals a simpler global count or inequality.

Before replacing a route, inventory any reusable definitions, structural lemmas, examples, and counterexamples. After replacement, search globally for stale terminology, labels, roadmap promises, figures, and introduction claims inherited from the old architecture.

## 9. Report findings without overstating them

Separate four kinds of findings:

1. **verified historical fact** — directly supported by snapshots or diffs;
2. **textual defect** — grammar, missing definition, weak transition, or unsupported ease word;
3. **logical obligation not explicit in the manuscript** — the proof may be correct, but the text does not discharge the step;
4. **possible mathematical gap** — a concrete unresolved condition that requires author or expert verification.

For the last two, state the exact premise, missing implication, and affected result. Do not announce that a theorem is false merely because the exposition is incomplete.

Recommended history-audit deliverables:

1. a final-artifact lineage table;
2. a deleted-route table with functional reasons;
3. a reader-facing architecture timeline;
4. a proof-obligation and case-coverage ledger;
5. residual endpoint issues;
6. a short set of transferable revision rules.
