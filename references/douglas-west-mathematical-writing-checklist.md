# Douglas B. West mathematical-writing checklist

Use this reference for English-language mathematical prose. It paraphrases every numbered rule in the supplied Chinese translation of Douglas B. West's writing guide. Apply the rules semantically rather than by blind replacement, and let an explicit venue requirement or a confirmed author house style override a local preference. Never use a prose rule to change a mathematical claim.

## Contents

1. Use protocol
2. Paper structure and mathematical sentence style (Rules 1-27)
3. Terminology and notation (Rules 28-57)
4. English usage and punctuation (Rules 58-81)
5. Frequent non-native-English errors (Rules 82-92)
6. Audit protocol

## 1. Use protocol

- During drafting, consult the relevant rule at the point of use.
- During Polish or Audit mode, run a separate West pass after theorem/scope, architecture, notation, citation, and proof-logic passes have stabilized.
- Record a finding by rule number, exact location, observed phrase, and proposed repair. Mark a rule `not applicable` only after checking its object class.
- Treat examples below as patterns, not text to paste. Check the surrounding grammar and the manuscript's definitions before editing.
- Separate preferences from errors. For example, punctuation after `Hence` or notation for graph joins may be a house-style choice, whereas a dangling modifier or an undefined symbol is a defect.

## 2. Paper structure and mathematical sentence style

1. **Abstract, introduction, and conclusion.** Make the abstract a concise, self-contained account of the results and the terminology needed to understand them; do not use it as a bibliography. Use the introduction to state the problem, situate related results, explain the paper's structure or methods when useful, and give essential definitions. Add a conclusion only when it helps readers assess the contribution, limitations, or next questions; a mathematical paper need not end with stock concluding phrases.

2. **Definitions.** Visually distinguish a term at its defining occurrence, normally with italics. Prefer the direct form “An object has property *term* if condition holds” to `called` or `said to be`. Italicize the complete defined noun phrase, but only the adjectival property word when the term is used predicatively. Do not insert a comma between a subject and its defining predicate.

3. **`where` versus `such that`.** After a formula containing an undefined symbol, use a comma and `where` to introduce the symbol's definition. Use `such that` to restrict an already defined variable or object.

4. **Avoid double-duty definitions.** Do not describe or use an object before defining it, and do not make one clause both define a mathematical object and use it as though already defined. Introduce the object, its ambient class, and its notation in a grammatically complete order; avoid defining a symbol and a new object through one overloaded equality.

5. **Treat formulas as grammatical units.** Decide whether a displayed or inline expression functions as a noun or as a relation. Usually treat a formula as a noun phrase and supply an English verb; otherwise a relation symbol may supply the verb, but do not accidentally give the sentence two verbs. Split a sentence when a formula would have to play both roles. Exceptions include object-introduction verbs (`Let`, `Set`, `Put`, `Choose`) followed by an equality and membership expressions naturally read as `in`.

6. **Separate adjacent formulas.** Do not join two independent formulas with only a comma. Insert words that state the relation (`and`, `where`, `it follows that`, `we have`) or rewrite the sentence. When a formula names one object, identify its type in prose instead of leaving a comma to carry the grammar.

7. **Do not start a sentence with a bare symbol.** Introduce a noun phrase such as `The graph (G)` or rewrite the sentence. A numbered theorem statement may begin with a formula only when its label or environment supplies a legitimate grammatical lead-in.

8. **Lists of mathematical objects.** For two parallel grammatical objects, use `and` rather than a comma. For three or more, use an explicit coordinated list and a serial comma when needed for clarity. Distinguish a list of variables from a pair of conditions on each variable; membership notation such as `(x,y\in V(G))` may be read as a unit when the convention is clear.

9. **Do not hide grammar in parentheses.** Parentheses and comma fragments should not replace needed words or independent clauses. Write restrictions and exceptions as prose, for example `an edge (xy) other than (e)` and `for (k\le m) with (k) even`, rather than compressed parenthetical qualifications.

10. **Do not compare prose with symbols.** A phrase such as `maximum degree` cannot stand on one side of `\le`. Either compare mathematical quantities or write a complete verbal assertion. In prose, prefer words over logical glyphs such as `\forall`, `\exists`, `\Rightarrow`, and `iff` unless the formal notation itself is the object of discussion.

11. **Avoid `Let hypothesis. Then conclusion.`** Use `If hypothesis, then conclusion` for an implication. If the setup is long, introduce the objects first and then state the implication in a complete sentence. At sentence start, reserve `Then` for genuine temporal sequence; use `Now`, `Next`, or, preferably, the mathematical role. Avoid the hybrid `Let ..., then ...` construction.

12. **Hypothesis words.** An `If` clause normally takes `then`, preceded by a comma when the clause comes first. Omit `then` only when readability improves and recast the clause with `When` or `For`. A fronted `When`, `For`, `Since`, or `Because` clause normally takes a comma. Do not follow causal `Since` or `Because` with `then` or `so` as a second conclusion marker.

13. **Causal `as` and `for`.** Use them cautiously because they are easy to misread, especially for non-native readers. Prefer `because` or `since` when the causal relation could be unclear. Distinguish causal `for` from a following noun phrase introduced by prepositional `for`.

14. **`Therefore`, `Hence`, and `Thus`.** Use a conclusion word to open the sentence that states the conclusion, not as a floating filler. Follow the project punctuation convention consistently. West treats `Therefore` as an introductory adverb normally followed by a comma and often leaves short `Hence`/`Thus` unpunctuated for mathematical flow; a venue may choose differently.

15. **Place theorem attributions next to the fact they support.** Avoid the ambiguous tail `..., by Theorem X, ...`. Prefer `By Theorem X, premise/conclusion` or `Since premise, Theorem X implies conclusion`, so the cited theorem's exact role is visible.

16. **`so` versus `so that`.** Use `so` as a coordinating conjunction for a consequence and normally precede it with a comma. Use `so that` for purpose or manner, not merely to pad a short conclusion; write `We have (x^2=0), so (x=0)`.

17. **`such that` versus `so that`.** Use `such that` to restrict a noun (`a graph such that ...`) and `so that` to describe the intended effect of an action (`color the graph so that ...`).

18. **`assume`, `suppose`, and `let`.** Use `assume` for an accepted premise and `suppose` for a temporary hypothesis, especially in contradiction. Prefer `Suppose for a contradiction that ...` or `Toward a contradiction, suppose that ...`; avoid malformed `By way of contradiction`. Use `that` when a full clause follows and omit it before a noun phrase or compact symbolic hypothesis when natural. Use `Let` to introduce an object or assign a value, not `Suppose x is ...` when no hypothesis is intended. Avoid `Let that ...`.

19. **Quantifiers.** Avoid ambiguous `any`. For universal claims, prefer `each`, `every`, `for every`, or `an arbitrary` as grammar requires. Do not let `not any` obscure `no`. Use articles carefully: `a bipartite graph has no odd cycle` may sound existential; `every bipartite graph has no odd cycle` is explicit. Add `must` only when it clarifies necessity.

20. **Quantifier placement.** Put a quantifier before the formula it governs when logic would otherwise be ambiguous. In prose, place it where readers encounter the scope naturally: `For every bipartite graph (G), ...` and `For (1\le i\le n), (a_i\in S)`.

21. **`less` and `fewer`.** Use `less` for a measured quantity and `fewer` for countable objects: `the number of edges is less than (k)`, but `the graph has fewer than (k) edges`.

22. **Compare like kinds.** Do not compare a set directly with an integer or say one set is `larger` when its cardinality is meant. Compare sizes or numbers of elements explicitly. Use a counting function such as `(\binom nk)` only after defining what it counts.

23. **`estimate` is not `bound`.** In English, an estimate is an approximation, whereas a bound is a proved upper or lower limit. Write `we prove an upper bound` when that is the claim; reserve `estimate` for actual approximation.

24. **Plural symbols.** Do not form a plural with an apostrophe (`the (a_i)'s`). Write `the (a_i)`, `the elements (a_1,\ldots,a_n)`, or another unambiguous noun phrase.

25. **Do not nest proof environments.** Finish or suspend the current proof before starting another named proof. Use an internal claim with its own proof paragraph rather than a second `proof` environment inside the first.

26. **`best possible`.** Treat it as a fixed adjectival phrase without `the`: `This result is best possible`. Prefer `sharp` or, better, state exactly what cannot be improved (`the constant in the upper bound cannot be improved`). Use optimality language only after verifying it.

27. **Numbers versus number words.** In mathematical prose, use numerals for mathematical values (`degree 3`, `length 4`, `a 4-vertex path`) and words when merely counting ordinary objects (`two vertices`, `four edges`, `a path with four vertices`). Rewrite when a word/numeral choice changes the mathematical reading, as with an invariant equal to `1` versus one invariant of a given type.

## 3. Terminology and notation

28. **Definition symbol `:=`.** Use it only when the symbol is being defined at that occurrence. Do not write `Consider a coloring of ([n]:=...)`; define `([n])` first or use `where ([n]=...)`. When `:=` is unfamiliar or stylistically disallowed, write `let ... be` or `is defined to be`.

29. **Set-builder punctuation.** Use a colon for `such that` in set-builder notation and reserve the vertical bar for cardinality, divisibility, conditioning, or other established meanings. In TeX, use `\colon`, with spacing after it, not a raw text colon or a crowded bar.

30. **Sequence, series, and list.** A sequence is an indexed function, a series is a sum (finite or infinite), and a finite ordered collection may be called a list. Do not call every finite list a sequence or every family a series. Prefer `degree list` or `vertex degrees` when the object is not being used as a sequence.

31. **Generic lists must allow small length.** Avoid writing `(v_1,v_2,\ldots,v_n)` when (n=1) is allowed, because displaying (v_2) presupposes a second term. Use `(v_1,\ldots,v_n)` unless the second term carries information.

32. **Do not make a relation define a list.** `Let (x_1\le\cdots\le x_n) be a list` gives the display two jobs. Write `Let (x_1,\ldots,x_n) be integers such that ...` or `indexed in nondecreasing order`. Use `\cdots` for centered relational chains and `\ldots` for comma-separated lists.

33. **Do not equate a variable with a list of values.** Replace `for (m=1,2,\ldots,n)` by `for (m\in\{1,\ldots,n\})` or `for (1\le m\le n)`. Apply the same rule to short lists such as `(i\in\{1,2})`.

34. **Big-O notation.** Do not read `(f(n)=O(n^2))` as an ordinary symmetric equality. Prefer `(f(n)) is (O(n^2))`, `(f\in O(n^2))`, or the project's formally defined relation. If an equality convention is retained, ensure the surrounding algebra does not exploit symmetry incorrectly.

35. **Operators and their values.** A function or graph parameter is not its value. Write `(\Delta(G))` for the maximum-degree value of (G); define `(\Delta=\Delta(G))` only when one fixed graph is in scope. Do not write forms such as `(\Delta n)` when the intended indexed value is `(\Delta_n)` or `(\Delta(G_n))`.

36. **Hyphenate parameterized modifiers.** Use `(k)-connected graphs`, `(k+1)-connected`, `(n)-vertex graph`, `(p)-group`, `(k)-edge-connected graph`, and `(k)-edge-coloring`. Parenthesize compound parameter expressions before the hyphen. Place the hyphen at the correct semantic level: `(k)-edge-coloring` means (k) modifies `edge-coloring`.

37. **Vertex and edge terminology.** Use unmodified standard terms for vertex notions when the context already names vertices (`connectivity`, `chromatic number`). Add `edge-` for the edge analogue (`edge-connectivity`, `edge-chromatic number`). Keep compound conventions consistent: `edge-coloring` but `list coloring`. When `disjoint` is unqualified, state whether vertex- or edge-disjointness is meant.

38. **Two-word adjectival terms.** Hyphenate a multiword concept when it precedes and modifies a noun: `vertex-transitive graph`, `polynomial-time algorithm`, `graph-theoretic technique`, `straight-line drawing`. Remove the hyphen in predicate/adverbial use when the words no longer form a compound modifier (`runs in polynomial time`).

39. **Adverbs and `well-`.** Do not hyphenate ordinary adverb-adjective combinations such as `strongly connected` or `simply connected`. Treat established compounds such as `well-known` and `well-defined` consistently; use `well-defined function` when the compound modifies a noun, and `the function is well defined` if that is the selected house convention.

40. **Endpoint path notation.** Do not let TeX render an endpoint separator as subtraction. Treat the endpoints as separate parameters and use the project's standard form, preferably an `(x,y)`-path (consistent with `(f,g)`-factor and `(x,y)`-chain), rather than an ambiguous `(x-y)` mathematical expression.

41. **Order and size of a graph.** Because `order` and `size` can be ambiguous, prefer `number of vertices` and `number of edges` on first use, or define `(n=|V(G)|)` and `(m=|E(G)|)`. Use `order`/`size` later only when the manuscript fixes their meanings consistently.

42. **A graph is not a set.** Do not write `(v\in G)` or `(e\in G)`; write `(v\in V(G))` and `(e\in E(G))`. Avoid ambiguous `(|G|)` and `(\|G\|)` unless explicitly defined. Use `(G-v)` and `(G-e)` only when context makes the operation clear. For `(A\subseteq V(G))`, distinguish `(|A|)` from the number of edges in `(G[A])`.

43. **Directed graphs and hypergraphs.** Once the context fixes directed graphs, avoid needless repetition in `directed edge/path/cycle`; retain the modifier only to contrast with an undirected or weak notion. Prefer `edge` to `hyperedge` when the context is exclusively hypergraphs, unless the distinction matters.

44. **Components are connected by definition.** Write `components`, not `connected components`, unless contrasting different component notions.

45. **`maximal` versus `maximum`.** `Maximal` means inclusion-maximal; `maximum` means greatest by a specified numerical objective. Do not use `maximal` for a number (`maximal degree`, `maximal number of edges`). Prefer `largest`/`smallest` or `maximum`/`minimum` consistently and state the optimized quantity.

46. **Multi-letter mathematical names.** Typeset multi-letter operators and invariants in roman/operator form rather than as products of italic variables, for example `\dim`, `\operatorname{cr}`, `\operatorname{ch}`, and `\operatorname{Mad}` according to project conventions.

47. **Induction language.** Write `We use induction on (n)` or `We prove the claim by induction on (n)`, not `We induct on (n)`. Cite `the induction hypothesis`, not merely `by induction`, when invoking the smaller-case assumption.

48. **Clique versus complete subgraph.** A clique is a vertex set whose induced subgraph is complete; a complete subgraph is a graph. Prefer `clique of size 5` or `5-clique` and distinguish maximal from maximum cliques.

49. **Isomorphism classes and copies.** Symbols such as `(P_n)`, `(C_n)`, and `(K_n)` often name isomorphism types rather than a particular subgraph. Write `contains a path on (n) vertices`, `contains a copy of (H)`, or `has a subgraph isomorphic to (H)` when a concrete copy is intended. Do not use an indefinite article before a class symbol unless the convention explicitly treats it as an object.

50. **Proper colorings.** State `proper (k)-coloring` or `proper (k)-edge-coloring` unless the manuscript has explicitly defined unqualified colorings to be proper. If another established modifier such as `acyclic` or `dynamic` already includes properness by definition, avoid redundant `proper`.

51. **Partitions and parts.** A partition is the collection of blocks/parts, not an individual part and not every member being partitioned. For bipartite graphs, call the two vertex classes `parts` (or a precisely defined alternative), and avoid the potentially confusing `partite sets` unless the manuscript establishes it.

52. **`pairwise` versus `mutually`.** For a binary relation applied to all pairs in a collection, prefer `pairwise` (`pairwise orthogonal`, `pairwise independent`) to ambiguous `mutually`. Reserve `mutual` for genuinely symmetric two-party relationships or established terminology.

53. **Pairwise relations.** `Disjoint sets` conventionally means pairwise disjoint, so `pairwise` may be redundant but can aid clarity. Apply the same logic to other binary relations such as `isomorphic`: include `pairwise` only when it resolves scope or prevents a non-pairwise reading.

54. **Disjoint union and join.** Do not use one symbol, especially `+`, for both disjoint union and graph join. Select distinct, defined symbols; `\mathbin\diamondplus`/`\sqcup` may denote disjoint union and another explicit symbol may denote join. Do not borrow logical disjunction or a symbol already used for another graph product.

55. **`between`.** In ordinary mathematical English, `between (u) and (v)` suggests separation, not necessarily incidence. Prefer `an edge joining (u) and (v)` for endpoints. `An edge between two faces` is acceptable when the planar dual interpretation is intended.

56. **Set difference.** Use `\setminus` for set difference and reserve graph deletion notation such as `(G-e)` for deleting an edge. Avoid `(G\setminus e)` and ambiguous combinations such as `(G\setminus H)` unless explicitly defined. For ordinary sets, `(A-B)` may be clearer when it matches the project convention.

57. **`left side`, not `left-hand side`.** Prefer `left side` and `right side`; do not create the nonstandard noun phrase `hand side`.

## 4. English usage and punctuation

58. **Introductory words and phrases.** Separate introductory items such as `Nevertheless`, `For example`, `To the contrary`, and `On the other hand` with a comma. A short one-word time phrase may omit it (`In 1995`), whereas a longer phrase normally takes it (`In August of 1995`). Apply the same convention to mathematical conclusion words consistently.

59. **Quotation marks and sentence punctuation.** When quoted material is a complete sentence, place its terminal punctuation with the quotation according to the adopted style. When the quoted string is only a token or formula within the outer sentence, keep logical punctuation outside the closing quotation mark unless it belongs to the quoted material.

60. **`that` and `which`.** Use `that` for a restrictive clause identifying which objects are meant; use comma + `which` for a nonrestrictive clause commenting on all objects already identified. Use `which` in constructions such as `all of which` and `the only one of which`. Check the article and antecedent rather than applying a blind substitution.

61. **Nearest antecedent.** Place a relative clause immediately after the noun it modifies. Rewrite sentences in which `which`, `that`, or `where` would grammatically attach to the wrong object.

62. **Do not use a bare `This` for a whole argument.** A standalone `This` refers naturally to the nearest noun. When it summarizes a preceding discussion, add a noun: `This discussion implies`, `This inequality implies`, or name the exact premise.

63. **`every`, `distinct`, and `unique`.** `Every` is singular: write `every value` or `all values`. `Distinct` means pairwise different; do not claim `Every value is distinct`. `Unique` means exactly one, not merely different from others; do not use it to assert injectivity or pairwise distinct images.

64. **No contractions in formal prose.** Replace `can't`, `won't`, and similar forms with full words.

65. **Avoid `i.e.` and `e.g.` in formal mathematical prose.** Prefer `that is` and `for example`. If a venue permits the abbreviations, punctuate them correctly and do not confuse restatement with example.

66. **`different from`.** Write `A differs from B` or `A is different from B`, not `differs than` or `different than` in formal prose.

67. **Articles with abstract notions and parameter values.** Omit `the` for a concept in general (`chromatic number`) and use it for a specific object's value (`the chromatic number of this graph`). Write `the graph has chromatic number 3` and `the vertex has degree 3`, not `a degree 3` or `the degree 3`. Abstract nouns such as `value`, `degree`, `compensation`, and `transitivity` normally take no article when used as general properties.

68. **Possessives and named results.** A person's possessive can supply definiteness: write `Greene's theorem`, not `the Greene's theorem`. For joint names, prefer a hyphenated title such as `the Greene-Kleitman theorem` or `the theorem of Greene and Kleitman` rather than an awkward shared possessive.

69. **Capitalization of theorem names.** Capitalize a generic label when it forms part of a unique formal title (`the Cauchy-Schwarz Inequality`) and use lowercase for descriptive or customary non-title phrases (`the Chinese remainder theorem`, `the Hungarian method`). Follow the project's verified naming convention consistently.

70. **Nouns and adjectival forms.** Use the established adjective where the noun names a person or object: `Hamiltonian cycle`, `Eulerian circuit`, not `Hamilton cycle` or `Euler circuit`. Preserve fixed noun forms such as `Fibonacci numbers`, `Catalan numbers`, and the conventional `Eulerian numbers`.

71. **Conjunctions and commas.** A conjunction joins grammatical units; a comma marks a useful pause but should not obstruct logical flow. Put a comma before `and`, `but`, `then`, or coordinating `so` when it joins independent clauses. Omit it when the conjunction joins predicates or smaller units with one subject. Check scope when a conditional conclusion itself contains `and`.

72. **Semicolons.** Use a semicolon between closely related independent clauses when no conjunction is present. Do not place a semicolon immediately before `and`, `but`, `then`, or `so` merely to make a stronger pause.

73. **Do not separate subject from verb with an unnecessary comma.** In particular, do not put a comma before the main verb after a long subject or before `and` when it joins two predicates sharing one subject.

74. **Serial comma.** In a list of three or more items, use a comma before the final `and` when it prevents grouping ambiguity. In mathematical lists with conditions, use it whenever the final item could otherwise appear to modify only its neighbor.

75. **Appositives.** Set off a nonrestrictive renaming noun phrase with commas on both sides. Omit commas when the appositive is short and essential to identifying the noun. Do not place only one comma around an internal appositive.

76. **Prefer active voice.** Use an active mathematical subject and verb when it clarifies agency or logic (`It suffices to show`) rather than a needlessly passive construction (`It is sufficient to show`). Retain passive voice when the actor is irrelevant and the sentence reads better.

77. **`above` and `below` follow the noun.** Write `the graph above`, `the figure below`, `the graph shown above`, or use a numbered `\Cref`; do not write `the above graph` or `the below figure`.

78. **`either ... or`.** Use `either` when it clarifies paired scope. Omit it when `or` already states mutually exclusive alternatives unambiguously or when `either` would attach to the wrong grammatical unit.

79. **Tense.** Use simple past for completed work (`In Section 3 we analyzed`, `in [4] we showed`), simple present for what the current paper now establishes (`in Section 4 we show`), and future only for a genuinely forthcoming action. Avoid unnecessary perfect progressive constructions such as `we have been proving`.

80. **`non` compounds.** Most established `non` words are closed (`nonsingular`, `nontrivial`, `nonzero`, `nonconstructive`, `nonempty`, `nonnegative`, `nonneighbor`, `nonadjacent`). Use a hyphen for an unusual or potentially confusing coinage such as `non-word` or `non-edge`, and keep the choice consistent.

81. **Citation placement.** Put a reference immediately after the author name or claim it supports, not after a long description of consequences. Readers should be able to identify the source before interpreting the attributed result.

## 5. Frequent non-native-English errors

82. **`bound on`.** Write `a bound on (x)` or `an upper bound of (k) on (x)`, not `the bound of (x)`. Distinguish the bounded object from the numerical bound.

83. **`few` versus `a few`.** `Few` means not many and often implies inadequacy; `a few` means several. `We prove few good results` disparages the paper, whereas `we prove a few good results` counts several.

84. **`the usual`.** When `usual` identifies the standard member of a class, include the article: `the usual chromatic number`.

85. **`special case`, not `partial case`.** A restricted instance of a theorem or conjecture is a special case; proving it may be a partial result.

86. **`pass through`.** A path passes through a vertex; bare `pass` normally means go past without entering.

87. **`cannot`, `may be`, `maybe`, and `possibly`.** Use `cannot` for impossibility. Avoid separated `can not` when the intended meaning is ordinary negation. Use `may be` as verb phrase (`It may be true`), `maybe` as sentence adverb (`Maybe the proof works`), and preferably `possibly` in formal prose.

88. **Uncountable nouns.** Treat `work`, `research`, and `access` as uncountable in their ordinary academic senses: `This is work of mine`, `joint work with`, `research`, and `limited access`; not `a work`, `a joint research`, or `an access`. Retain countable uses such as `a work of art` or `the complete works`.

89. **`evidently`, `clearly`, and evidence phrases.** Do not use `evidently` as a synonym for `clearly`; in ordinary English it means `apparently` or `the evidence suggests`. Prefer the actual reason to either adverb. Write `as shown by` (or the grammatical `as evidenced by` when evidence is genuinely meant), not the calque `as evidence by`.

90. **`principal` versus `principle`.** `Principal` is normally an adjective meaning foremost (`principal minor`); `principle` is a noun meaning rule, idea, or method (`the Pigeonhole Principle`).

91. **No comma around a complement.** Do not insert a comma before or after copular `is` merely because the subject is long. Do not put a comma between `show` and its `that`-clause.

92. **Repair recurrent calques.** Use the following forms:

    - `discuss`, not `discuss about`;
    - `study`, not `study about`;
    - `equals` or `is equal to`, not `equals to`;
    - `contradicts`, not `contradicts to`;
    - `conditions necessary for`, not `necessary the conditions of`;
    - `make precise` or the adjective `precise`, not verbal `to precise`;
    - `the same argument` or `a similar argument`, not `a same argument`;
    - `decompose into`, not `decompose to`;
    - use a real verb such as `join` rather than using `to be` as a fabricated technical verb;
    - `especially` or `special`, not `specially` when that form is nonstandard in the intended sense;
    - `ordinary coloring` or the explicitly defined proper coloring, not an unexplained `usual coloring`;
    - `We consider`, not `We have a pick up`.

## 6. Audit protocol

Run the West pass only after mathematical and structural stability:

1. Check Rules 1-27 against abstract/introduction/conclusion, definitions, every theorem statement, and representative proof paragraphs.
2. Build or update the terminology registry while checking Rules 28-57; record every symbol, compound, capitalization choice, and object/value distinction.
3. Check Rules 58-81 sentence by sentence, including displayed mathematics as part of its surrounding sentence.
4. Search mechanically for the phrases in Rules 64-66, 77, 80, and 82-92, then inspect every hit in context.
5. For each edit, verify that hypotheses, quantifiers, implication direction, object class, and notation scope are unchanged.
6. Report completion as `West 1-92 checked`, followed by any intentional deviations and their authority (venue, author, or established project convention). A clean regex search is not completion; the semantic rules require a reader pass.
