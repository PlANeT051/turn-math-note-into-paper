# LaTeX micro-formatting for mathematics papers

Use these conventions when creating, restructuring, polishing, or auditing TeX. Venue and document-class requirements take precedence, but do not vary conventions casually within one project.

## Contents

1. Labels and semantic prefixes
2. Cross-references with `\Cref`
3. Paragraphs, blank lines, and vertical space
4. Inline versus displayed mathematics
5. Display environments, numbering, and punctuation
6. Theorem, proof, figure, and table blocks
7. Compact model examples
8. Final micro-format check

## 1. Labels and semantic prefixes

Give every numbered theorem-like result, section, figure, and table a stable semantic label. Label an equation when the prose refers to it or when later rearrangement could make a textual locator ambiguous.

Use descriptive lowercase keys rather than document-order numbers or dates:

| Object | Prefix | Example |
|---|---|---|
| theorem | `thm:` | `\label{thm:main-bound}` |
| lemma | `lem:` | `\label{lem:cut-reduction}` |
| proposition | `prop:` | `\label{prop:leaf-block}` |
| corollary | `cor:` | `\label{cor:cubic-case}` |
| claim | `clm:` | `\label{clm:matching-exists}` |
| definition | `def:` | `\label{def:frustration-index}` |
| observation | `obs:` | `\label{obs:balanced-cut}` |
| conjecture | `conj:` | `\label{conj:girth-five}` |
| section/subsection | `sec:` / `subsec:` | `\label{sec:small-graphs}` |
| equation | `eq:` | `\label{eq:key-count}` |
| figure/table | `fig:` / `tab:` | `\label{fig:exceptional-graphs}` |

Placement rules:

- Put a theorem-like label immediately after the environment opening: `\begin{lemma}\label{lem:key}`.
- Put a section label immediately after the section command.
- Put a figure or table label immediately **after** `\caption{...}`, because the caption advances the counter.
- Put an equation label inside its numbered `equation`, `align`, or related environment.
- Give a referenced theorem or claim subitem its own semantic label. Configure the `enumerate` reference so `\Cref` prints the complete parent path (for example, `Theorem 2.3(ii)`), not merely `(ii)`.
- Do not put `\label` in a starred, unnumbered environment.
- Do not reuse a label, leave an empty label, or keep labels for deleted objects.
- Keep a label stable when prose moves; rename it only when its mathematical meaning changes.

## 2. Cross-references with `\Cref`

Use `cleveref` semantic references for internal mathematical objects. Under this user's house style, use capitalized `\Cref` consistently:

```tex
By \Cref{lem:cut-reduction}, the reduced graph is admissible.
Combining \Cref{eq:key-count,eq:degree-sum} proves \Cref{thm:main-bound}.
The exceptional configurations are shown in \Cref{fig:exceptional-graphs}.
```

For a referenced subitem, use an explicit reference format and typed label:

```tex
\begin{theorem}\label{thm:classification}
\begin{enumerate}[label=\textup{(\roman*)},
  ref=\thetheorem\textup{(\roman*)}]
\item\label[theorem]{thm:classification-bipartite} The bipartite case holds.
\end{enumerate}
\end{theorem}

By \Cref{thm:classification-bipartite}, the bipartite case is complete.
```

Rules:

- Do not write `Lemma~\ref{...}`, `Theorem~\ref{...}`, `Figure~\ref{...}`, or a bare `\ref{...}`.
- Use one `\Cref{...}` for several objects of the same or mixed types instead of manually repeating their names.
- Use `\Crefrange{...}{...}` only for a genuine consecutive range.
- Do not use a vague locator such as “the above lemma” when a label is available.
- Do not write partial internal locators such as `part~(ii)`, `item~(3a)`, `For (1)`, or `in (2)`. Label the subitem and use `\Cref{...}` so the rendered reference includes its theorem or claim number.
- Do not use a bare parenthesized integer for mathematical data when it can be mistaken for a numbered locator. State what the value denotes; for example, write “the corresponding cycle has length \(4\).”
- Check that the referenced result actually performs the stated role. A compiling hyperlink is not proof of a correct dependency.
- If prose says a lemma is used but the proof does not use it, do not retrofit the proof merely to justify the cross-reference. Remove the stale role sentence when clearly editorial, or mark `AUTHOR DECISION NEEDED` when the intended dependency is uncertain.
- Literature citations are different: retain the project's `\cite`, `\textcite`, `\parencite`, or equivalent bibliography command. `\Cref` is not a bibliographic citation command.
- Retain `\pageref` only when a page number itself is genuinely needed.
- If `cleveref` is absent and the user authorizes TeX edits, load it once in the preamble after packages that define counters, normally after `hyperref`. Respect journal-class restrictions and existing package order.
- Define `\crefname`/`\Crefname` once for custom environments when automatic names are wrong; do not hard-code object names throughout the prose.

## 3. Paragraphs, blank lines, and vertical space

A completely blank source line starts a new paragraph. Use it only when the logical job changes: setup to claim, claim to consequence, one proof phase to another, or one introduction function to another.

- Use exactly one blank source line between distinct prose paragraphs and between top-level blocks such as a theorem, its proof, the following paragraph, or a float.
- Do not insert a blank line merely because an equation is displayed. If the sentence continues after the display, keep the prose and display in the same paragraph.
- Do not put blank lines inside a short theorem statement or between every sentence of a proof.
- Use a new paragraph before a genuinely new proof phase or case family, not before every local deduction.
- Do not use `\\` to imitate a paragraph break.
- Multiple consecutive blank source lines do not create a principled “larger blank”; normalize them to one.
- Let the document class and semantic environments control normal space around sections, theorems, proofs, figures, tables, lists, and displays.
- Use `\smallskip`, `\medskip`, or `\bigskip` only for a deliberate repeated structure not already handled by an environment—for example, consistently separated case headings in a long proof. Use the same command for equivalent units.
- Avoid manual `\vspace` and `\\[<length>]` for ordinary exposition. Use them only for a verified layout requirement, never to conceal weak paragraph structure or force a float/page break.

“Large blank space” is therefore a semantic decision, not a count of empty source lines. Before adding it, ask which structural boundary it represents.

After compiling, run a separate **display-and-whitespace pass**. Source compliance is not enough: a sequence of short displayed formulas, one-line paragraphs, floats, or drafting boxes can still leave a visually sparse page. Inspect every page and ask whether each display is load-bearing. Merge a short parametrization or routine equality into prose when it remains readable, and keep displays for recurrences, piecewise definitions, referenced formulas, and decisive calculations. Do not compress mathematics merely to increase page density.

## 4. Inline versus displayed mathematics

Keep mathematics inline when it is short, unnumbered, grammatically simple, and readable without interrupting the sentence—for example, a symbol, a short relation such as `\(x\in X\)`, or a compact bound such as `\(F(G)\le n/3\)`.

Use a separate display when at least one of the following holds:

- the formula is a main theorem, key invariant, recurrence, or conclusion that deserves visual emphasis;
- it will be referenced later and therefore needs a number and label;
- it contains a multi-step equality/inequality chain;
- it contains a large fraction, sum, product, integral, matrix, cases definition, long set-builder expression, or nested quantifiers that impede the prose line;
- two or more formulas must be aligned or compared;
- keeping it inline would make the surrounding sentence hard to parse or likely to overrun the line.

Do not display a short formula merely for decoration. Do not compress a load-bearing multi-line derivation into inline math merely to save space.

## 5. Display environments, numbering, and punctuation

- Never use raw `$$ ... $$`.
- Use `equation` for one numbered formula and `equation*` (or the project's consistent unnumbered display convention) when no reference is needed.
- Use `align` for a derivation whose relation symbols should align. Use `align*` when no line needs a number.
- If several aligned lines form one referenced result, put `aligned` inside one `equation` so the display receives one number.
- Use `gather` only for multiple centered formulas that do not share an alignment point.
- Number only formulas that are referenced or structurally important. Do not label every display.
- Align at meaningful relation symbols such as `=`, `\le`, `\ge`, or `\Longrightarrow`; do not break lines solely by visual length when it hides the logical steps.
- Put short explanatory text inside math with `\text{...}` rather than raw italic letters.
- Treat a display as part of its surrounding sentence. Put the required comma, semicolon, or period at the end of the displayed formula.
- Use a colon before a display only when the preceding grammar genuinely introduces a list, definition, or announced formula.
- Do not capitalize the first word after a display unless a new sentence begins. Do not create a new paragraph after a display unless the logical job changes.

## 6. Theorem, proof, figure, and table blocks

### Theorem-like environments

- Keep hypotheses and conclusions inside the environment; keep motivation and proof intuition outside.
- Give every numbered result a semantic label, even if it is not yet referenced, so later restructuring does not require fragile numbering edits.
- Introduce a non-obvious lemma's role in the preceding prose and refer to it with `\Cref` afterward.
- Let the `proof` environment supply the end-of-proof mark; do not add a manual square unless a nested proof or custom environment requires it.
- Use real paragraphs inside long proofs. A blank line should correspond to a change of proof function.

### Figures and tables

- Refer to every figure and table in the prose with `\Cref`; do not leave an orphan float.
- Put the float near its first meaningful reference, subject to the class's float behavior.
- Use `\centering` rather than wrapping float contents in a `center` environment.
- Write a caption that identifies the object and explains the relevant comparison, convention, or takeaway without requiring the surrounding paragraph.
- Keep caption style—sentence or phrase, capitalization, and final punctuation—consistent across the paper.
- Place `\label` immediately after `\caption`.
- Do not use manual vertical space to force a float into a particular page unless the compiled layout has been inspected and the venue permits it.

## 7. Compact model examples

### Result, display, and proof closure

```tex
\begin{lemma}\label{lem:key-count}
Every vertex of \(X_3\) has at least two neighbors in \(Y_2\).
\end{lemma}

\begin{proof}
Fix \(x\in X_3\). We first exclude the two exceptional adjacency patterns.

By \Cref{lem:first-obstruction,lem:second-obstruction}, at most one neighbor of
\(x\) lies outside \(Y_2\). Therefore
\begin{equation}\label{eq:x3-degree}
  d_{Y_2}(x)\ge 2.
\end{equation}
This proves the claim.
\end{proof}

Double-counting the edges between \(X_3\) and \(Y_2\), and using
\Cref{eq:x3-degree}, gives
\begin{equation}\label{eq:key-count}
  2|X_3|\le e(X_3,Y_2)\le 2|Y_2|.
\end{equation}
Hence \(|X_3|\le |Y_2|\), as required.
```

There is no blank source line around either display because each is grammatically embedded in its paragraph. There is a blank line inside the proof only where setup changes to the main deduction.

### Figure

```tex
The five exceptional signatures are shown in \Cref{fig:exceptional-signatures}.

\begin{figure}[t]
  \centering
  \includegraphics[width=.82\linewidth]{exceptional-signatures}
  \caption{The exceptional signatures; negative edges are drawn in red.}
  \label{fig:exceptional-signatures}
\end{figure}
```

## 8. Final micro-format check

- Every numbered result, section, figure, and table has one unique semantic label.
- Every internal object reference uses `\Cref`; no manual `Theorem~\ref` or bare `\ref` remains.
- Every referenced theorem/claim subitem resolves to a complete path; no bare part, item, or parenthesized-number locator remains.
- Every cross-reference describes a real mathematical or expository relation; no proof dependency was invented merely to resolve a stale reference.
- Every figure/table label follows its caption and every float is referenced in prose.
- Every referenced equation is numbered and labeled; unreferenced routine displays are unnumbered.
- No raw `$$`, manual paragraph `\\`, stacked blank lines, or unexplained `\vspace` remains.
- No paragraph consists only of a routine parametrization such as “Write (r=2s+3)” when the statement can be integrated into the mathematical case that uses it.
- Blank lines correspond to genuine paragraph or proof-phase boundaries.
- Long or load-bearing formulas are displayed; short formulas remain inline.
- Displays use the correct environment, align at meaningful relations, and carry sentence punctuation.
- The compiled PDF has been inspected for equation breaks, float placement, theorem spacing, overfull boxes, and hyperlink targets.
