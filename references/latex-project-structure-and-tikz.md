# LaTeX project structure and TikZ figures

Use this reference whenever a task creates, reorganizes, or audits a root TeX file or a `tikzpicture`. A historical endpoint is evidence about the author's preferences, not automatic proof that every surviving package or command is ideal.

## Preamble boundary

Everything that configures the document belongs before `\begin{document}` unless a package or class explicitly requires otherwise. This includes:

- `\documentclass` and class options;
- package loading;
- theorem, proof, and list environments;
- `\crefname`/`\Crefname` declarations;
- operators and semantic notation macros;
- TikZ libraries and reusable styles;
- drafting-note macros;
- title, author, date, and other document metadata.

Do not define an author-note macro, theorem environment, or global figure style in the body merely because it was introduced late during drafting. Move it to the appropriate preamble block when the file is cleaned.

## Organize the preamble by responsibility

Use a stable order, adapting it to the document class rather than treating the following as an inflexible package list:

1. document class and encoding/language/font configuration;
2. core mathematics and theorem support;
3. layout, lists, tables, and captions;
4. graphics, `xcolor`, TikZ, and TikZ libraries;
5. bibliography support;
6. links, with `hyperref` normally before `cleveref`;
7. theorem environments and `cleveref` names;
8. semantic operators and notation macros;
9. reusable TikZ styles;
10. temporary collaboration-note macros, visibly marked as drafting-only;
11. title and author metadata.

Check class and package documentation before changing an order-sensitive pair. Do not load both `color` and `xcolor`; use `xcolor` when its features are needed. Consolidate repeated `\usepackage` calls and comma-separated package lists. Remove a package only after searching for its commands and compiling from a clean state.

## Environment discipline

- Give theorem families deliberate numbering. If several kinds share a theorem counter, declare that relationship explicitly rather than repairing numbers by hand.
- Define every theorem-like environment before its first use and give both `\crefname` and `\Crefname` singular/plural names where defaults are inadequate.
- Use one canonical proof environment. A custom proof variant must have a real semantic purpose, not merely different spacing.
- Put an attribution in an environment's optional title, for example `\begin{lemma}[Author~\cite{key}]`; do not simulate an optional title with a braced group at the start of the theorem body.
- Define recurring mathematical functions with `\DeclareMathOperator` or a semantic macro; do not reproduce typography manually throughout the paper.
- Keep project-specific notation separate from generic formatting commands.
- Keep drafting macros easy to find and remove. A submission may retain harmless definitions only if venue policy permits, but it must contain no live calls.
- Do not copy stale template code, duplicate color packages, unused environments, or one-off macros into a new paper.
- After a major rewrite, audit unused packages, macros, theorem environments, TikZ styles, and bibliography commands. Remove them one at a time with a clean compile rather than by guesswork.

## A maintainable TikZ block

Wrap a paper figure in the correct float and keep the source order predictable:

```tex
\begin{figure}[htbp]
  \centering
  \begin{tikzpicture}[
      vertex/.style={circle, draw, thick, minimum size=2.4mm, inner sep=0pt},
      selected/.style={vertex, fill=blue!65},
      positive/.style={draw=gray!75},
      negative/.style={draw=red!75!black, densely dotted}
    ]
    % Vertices
    \node[vertex] (left) at (0,0) {};
    \node[selected] (right) at (2,0) {};

    % Edges
    \draw[positive] (left) -- (right);

    % Labels
    \node[above] at (left) {$u$};
    \node[above] at (right) {$v$};
  \end{tikzpicture}
  \caption{The configuration used in the proof of \Cref{lem:semantic-name}.}
  \label{fig:semantic-name}
\end{figure}
```

The example illustrates structure, not mandatory colors or dimensions. Match established project conventions when they are coherent.

## TikZ source rules

- Name nodes and reusable paths semantically (`left-end`, `cut-vertex`, `face-a`), not only by drawing order (`n17`). Short mathematical names such as `(u)` are appropriate when they match the text.
- Declare nodes before drawing edges when practical. Group the source by function—vertices, ordinary edges, exceptional edges, labels—and use short comments to expose that structure.
- Use `\node` to place text. Do not use `\draw ... node` when no path is being drawn.
- Put a repeated visual vocabulary in `\tikzset` in the preamble; keep a style local only when it is genuinely figure-specific.
- Encode a mathematical distinction by more than color when possible: combine color with dashing, dotting, shape, fill, or a legend. Verify grayscale and color-vision readability.
- Keep node sizes, line widths, arrow tips, and label distances consistent across related figures.
- Do not retain an arrow-tip option such as `>=latex` in a picture that draws no arrows.
- Treat `scale` carefully: it scales coordinates but not all text and node dimensions unless `transform shape` is used. Decide intentionally; do not add `transform shape` merely to shrink a crowded figure.
- Avoid unexplained negative `\vspace`, manual line breaks, or invisible nodes used only to force placement. Repair the bounding box, float structure, or coordinates instead.
- Keep labels outside edges and nodes where possible, and check that crossings, parallel edges, arrowheads, and dotted styles remain legible at final column width.
- Use loops or parameterized coordinates only when they make the structure clearer. Eight opaque `\foreach` expressions are not better than a small explicit drawing.
- Keep the mathematical notation in the figure identical to the surrounding prose.

## Figures and subfigures

- A standalone figure gets one informative `\caption` followed immediately by one semantic `\label{fig:...}`.
- Labels must be stable identifiers without spaces; prefer `fig:wagner-comparison` to `fig:twisted cube`.
- A subfigure may have its own caption and label only when the text genuinely refers to it. Give the parent figure a caption and label describing the shared comparison.
- Align related subfigures deliberately and use widths that fit the target layout. Do not rely on a fortunate local rendering.
- Captions should tell the reader what distinction or construction matters; they should not reproduce a proof paragraph.
- Introduce or interpret every substantive figure in the prose and refer to it with `\Cref`.
- Do not put a label on a bare `tikzpicture`; put it after the caption whose counter it should inherit.

## Verification gate

Source inspection cannot establish that a TikZ figure is correct. Compile and visually inspect:

1. geometry and incidence against the mathematical description;
2. planarity or embedding claims;
3. labels, signs, directions, multiplicities, and highlighted sets;
4. cropping, baseline, whitespace, and float placement;
5. legibility at the final one- or two-column size;
6. consistency between subfigures, caption, and prose;
7. hyperlinks and `\Cref` output.

If the geometry cannot be verified from the supplied mathematics, leave a localized `FIGURE CHECK` rather than silently guessing coordinates or adjacencies.
