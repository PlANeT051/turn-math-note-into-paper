#!/usr/bin/env python3
"""Audit a mathematics TeX manuscript for editorial and project hygiene.

The audit is intentionally mechanical.  It does not validate mathematics,
novelty, or the accuracy of bibliography metadata.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


VERSION = "1.6.0"
SEVERITY_RANK = {"info": 0, "warning": 1, "error": 2}
THEOREM_ENVS = {
    "theorem",
    "lemma",
    "proposition",
    "corollary",
    "conjecture",
    "claim",
    "observation",
    "definition",
}
THEOREM_LABEL_PREFIXES = {
    "theorem": "thm:",
    "lemma": "lem:",
    "proposition": "prop:",
    "corollary": "cor:",
    "conjecture": "conj:",
    "claim": "clm:",
    "observation": "obs:",
    "definition": "def:",
}
NUMBERED_DISPLAY_ENVS = {
    "equation",
    "align",
    "alignat",
    "flalign",
    "gather",
    "multline",
}
MOJIBAKE_PATTERN = re.compile(r"(?:\ufffd|Ã|Â|â€|鈥|锟|銆)")
GRAPHIC_EXTENSIONS = (".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    file: str
    line: int
    message: str


def strip_tex_comment(line: str) -> tuple[str, str]:
    """Return active text and comment, respecting escaped percent signs."""
    for index, char in enumerate(line):
        if char != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index], line[index + 1 :]
    return line, ""


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalize_macro_name(value: str) -> str:
    return value.strip().lstrip("\\")


def discover_note_macros(active_text: str) -> set[str]:
    """Find custom macros whose definitions visibly implement draft notes."""
    note_macros: set[str] = set()
    definition = re.compile(
        r"\\(?:newcommand|renewcommand|providecommand|def)\s*"
        r"(?:\{\s*)?\\([A-Za-z@]+)(?:\s*\})?"
        r"(?:\s*\[[^\]]+\])?\s*\{(.{0,500}?)\}",
        re.DOTALL,
    )
    note_body = re.compile(
        r"(?:text)?color|colorbox|marginpar|todo|fixme|comment|author.note|draft",
        re.IGNORECASE,
    )
    for match in definition.finditer(active_text):
        if note_body.search(match.group(2)):
            note_macros.add(match.group(1))
    return note_macros


def bibliography_keys(tex_path: Path, active_text: str) -> tuple[set[str], set[str], bool]:
    inline_keys = set(
        re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", active_text)
    )
    keys = set(inline_keys)
    found_source = bool(keys)

    resource_patterns = (
        r"\\bibliography\{([^}]+)\}",
        r"\\addbibresource(?:\[[^\]]*\])?\{([^}]+)\}",
    )
    resources: list[str] = []
    for pattern in resource_patterns:
        for match in re.finditer(pattern, active_text):
            resources.extend(part.strip() for part in match.group(1).split(","))

    for resource in resources:
        resource_path = Path(resource)
        if resource_path.suffix.lower() != ".bib":
            resource_path = resource_path.with_suffix(".bib")
        if not resource_path.is_absolute():
            resource_path = tex_path.parent / resource_path
        if not resource_path.exists():
            continue
        found_source = True
        try:
            bib_text = resource_path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        keys.update(
            match.group(1).strip()
            for match in re.finditer(
                r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", bib_text, re.MULTILINE
            )
        )
    return keys, inline_keys, found_source


def collect_citation_keys(active_text: str) -> dict[str, int]:
    citations: dict[str, int] = {}
    pattern = re.compile(
        r"\\(?:[A-Za-z]*cite[A-Za-z]*|cite)\*?\s*"
        r"(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}"
    )
    for match in pattern.finditer(active_text):
        line = line_for_offset(active_text, match.start())
        for key in match.group(1).split(","):
            clean_key = key.strip()
            if clean_key:
                citations.setdefault(clean_key, line)
    return citations


def issue_counts(issues: Sequence[Issue]) -> dict[str, int]:
    counts = Counter(issue.severity for issue in issues)
    return {level: counts.get(level, 0) for level in ("error", "warning", "info")}


class TexAuditor:
    def __init__(self, path: Path, explicit_note_macros: Iterable[str] = ()) -> None:
        self.path = path.resolve()
        self.raw = self.path.read_text(encoding="utf-8-sig", errors="replace")
        self.lines = self.raw.splitlines()
        split_lines = [strip_tex_comment(line) for line in self.lines]
        self.active_lines = [parts[0] for parts in split_lines]
        self.comment_lines = [parts[1] for parts in split_lines]
        self.active_text = "\n".join(self.active_lines)
        self.note_macros = discover_note_macros(self.active_text)
        self.note_macros.update(normalize_macro_name(name) for name in explicit_note_macros)
        self.issues: list[Issue] = []
        self.structure: dict[str, object] = {}

    def add(self, severity: str, category: str, line: int, message: str) -> None:
        self.issues.append(
            Issue(severity, category, str(self.path), max(1, line), message)
        )

    def audit(self) -> dict[str, object]:
        self.audit_structure()
        self.audit_placeholders()
        self.audit_environment_balance()
        self.audit_labels_and_references()
        self.audit_citations()
        self.audit_theorem_labels()
        self.audit_equation_labels()
        self.audit_figures_and_inputs()
        self.audit_preamble_and_tikz()
        self.audit_style_smells()
        self.issues.sort(
            key=lambda item: (
                item.file,
                item.line,
                -SEVERITY_RANK[item.severity],
                item.category,
                item.message,
            )
        )
        return {
            "path": str(self.path),
            "structure": self.structure,
            "summary": issue_counts(self.issues),
            "issues": [asdict(issue) for issue in self.issues],
        }

    def audit_structure(self) -> None:
        sections = [
            {
                "level": match.group(1),
                "title": re.sub(r"\s+", " ", match.group(2)).strip(),
                "line": line_for_offset(self.active_text, match.start()),
            }
            for match in re.finditer(
                r"\\(section|subsection|subsubsection)\*?\s*\{([^}]*)\}",
                self.active_text,
            )
        ]
        standalone = bool(
            re.search(r"\\documentclass(?:\[[^\]]*\])?\{", self.active_text)
            or re.search(r"\\begin\{document\}", self.active_text)
        )
        author_command = re.search(
            r"\\author(?:\[[^\]]*\])?\s*\{", self.active_text
        )
        empty_author = re.search(
            r"\\author(?:\[[^\]]*\])?\s*\{\s*\}", self.active_text
        )
        official_keyword_pattern = re.compile(
            r"\\(?:keywords?|keyword)\s*\{|\\begin\{keywords?\}",
            re.IGNORECASE,
        )
        manual_keyword_pattern = re.compile(
            r"\\(?:textbf|textit|emph|paragraph)\s*\{\s*Keywords?\s*:?\s*\}"
            r"|\{\s*\\(?:bf|it)\s+Keywords?\s*\}",
            re.IGNORECASE,
        )
        official_keywords = bool(official_keyword_pattern.search(self.active_text))
        manual_keywords = bool(manual_keyword_pattern.search(self.active_text))
        self.structure = {
            "standalone_root": standalone,
            "line_count": len(self.lines),
            "sections": sections,
            "has_title": bool(re.search(r"\\title(?:\[[^\]]*\])?\s*\{", self.active_text)),
            "has_author_command": bool(author_command),
            "has_author": bool(author_command and not empty_author),
            "has_abstract": bool(re.search(r"\\begin\{abstract\}", self.active_text)),
            "has_keywords": official_keywords or manual_keywords,
            "keywords_mode": (
                "command_or_environment"
                if official_keywords
                else "manual"
                if manual_keywords
                else "missing"
            ),
            "note_macros": sorted(self.note_macros),
        }
        if not standalone:
            return
        required = (
            (r"\\begin\{document\}", "missing-document", "Missing \\begin{document}."),
            (r"\\end\{document\}", "missing-document", "Missing \\end{document}."),
            (r"\\title(?:\[[^\]]*\])?\s*\{", "missing-title", "No title command found."),
            (r"\\author(?:\[[^\]]*\])?\s*\{", "missing-author", "No author command found."),
            (r"\\begin\{abstract\}", "missing-abstract", "No abstract environment found."),
        )
        for pattern, category, message in required:
            if not re.search(pattern, self.active_text):
                self.add("error", category, 1, message)
        empty_fields = (
            (r"\\title(?:\[[^\]]*\])?\s*\{\s*\}", "empty-title", "Title is empty."),
            (r"\\author(?:\[[^\]]*\])?\s*\{\s*\}", "empty-author", "Author field is empty."),
            (r"\\begin\{abstract\}\s*\\end\{abstract\}", "empty-abstract", "Abstract is empty."),
        )
        for pattern, category, message in empty_fields:
            match = re.search(pattern, self.active_text, re.DOTALL)
            if match:
                self.add(
                    "error",
                    category,
                    line_for_offset(self.active_text, match.start()),
                    message,
                )
        if not any(item["title"].strip().lower() == "introduction" for item in sections):
            self.add("warning", "missing-introduction", 1, "No section titled Introduction found.")
        if not self.structure["has_keywords"]:
            self.add(
                "info",
                "missing-keywords",
                1,
                "No keyword command/environment found; verify the venue requirement.",
            )
        elif manual_keywords and not official_keywords:
            match = manual_keyword_pattern.search(self.active_text)
            self.add(
                "info",
                "manually-typeset-keywords",
                line_for_offset(self.active_text, match.start()) if match else 1,
                "Keywords are manually typeset rather than supplied through a keyword command/environment; verify the target class and venue convention.",
            )

    def audit_placeholders(self) -> None:
        active_patterns = (
            (r"\b(?:TODO|FIXME|TBD)\b", "error", "draft-placeholder", "Unresolved drafting marker."),
            (r"\bxxx\b", "error", "draft-placeholder", "Unresolved 'xxx' placeholder."),
            (r"\[\s*(?:citation needed|cite|ref)\s*\]", "error", "draft-placeholder", "Unresolved bracketed citation/reference placeholder."),
            (r"\?\?+", "warning", "draft-placeholder", "Question-mark placeholder or unresolved output marker."),
            (r"\\textcolor\s*\{\s*(?:red|orange|magenta|blue)\s*\}\s*\{", "warning", "colored-draft-text", "Colored text may be a live drafting annotation."),
            (r"\\color\s*\{\s*(?:red|orange|magenta)\s*\}", "warning", "colored-draft-text", "Colored text may be a live drafting annotation."),
        )
        for macro in sorted(self.note_macros):
            definition = re.search(
                rf"\\(?:newcommand|renewcommand|providecommand|def)\s*(?:\{{\s*)?\\{re.escape(macro)}\b",
                self.active_text,
            )
            if definition:
                self.add(
                    "info",
                    "draft-note-macro-definition",
                    line_for_offset(self.active_text, definition.start()),
                    f"Draft-note macro \\{macro} is defined; remove it if the submission package should contain no drafting machinery.",
                )
        for line_number, line in enumerate(self.active_lines, 1):
            is_definition = bool(
                re.search(r"\\(?:newcommand|renewcommand|providecommand|def)\b", line)
            )
            for pattern, severity, category, message in active_patterns:
                if is_definition and category == "colored-draft-text":
                    continue
                if re.search(pattern, line, re.IGNORECASE):
                    self.add(severity, category, line_number, message)
            if not is_definition:
                for macro in sorted(self.note_macros):
                    if re.search(rf"\\{re.escape(macro)}\s*\{{", line):
                        self.add(
                            "error",
                            "live-note-macro",
                            line_number,
                            f"Live collaborator/draft note macro \\{macro} found.",
                        )

            if MOJIBAKE_PATTERN.search(line):
                self.add(
                    "error",
                    "encoding-corruption",
                    line_number,
                    "Possible mojibake or replacement character found.",
                )

        for line_number, comment in enumerate(self.comment_lines, 1):
            if re.search(r"\b(?:TODO|FIXME|TBD|xxx)\b", comment, re.IGNORECASE):
                self.add(
                    "warning",
                    "draft-comment",
                    line_number,
                    "Draft marker remains in a TeX comment; verify that submitted source may include it.",
                )
            if MOJIBAKE_PATTERN.search(comment):
                self.add(
                    "error",
                    "encoding-corruption",
                    line_number,
                    "Possible mojibake or replacement character found in a TeX comment.",
                )
            for macro in sorted(self.note_macros):
                if re.search(rf"\\{re.escape(macro)}\s*\{{", comment):
                    self.add(
                        "warning",
                        "commented-note-macro",
                        line_number,
                        f"Commented collaborator/draft note macro \\{macro} remains in the source.",
                    )
            if re.search(r"\\bibitem(?:\[[^\]]*\])?\{", comment):
                self.add(
                    "info",
                    "commented-bibitem",
                    line_number,
                    "Commented bibliography item remains in the source; verify it is not obsolete drafting material.",
                )

        substantial_comments = [
            number
            for number, comment in enumerate(self.comment_lines, 1)
            if comment.strip()
            and (
                comment.lstrip().startswith("\\")
                or len(re.findall(r"[A-Za-z]{2,}", comment)) >= 5
            )
        ]
        runs: list[list[int]] = []
        for number in substantial_comments:
            if not runs or number > runs[-1][-1] + 3:
                runs.append([number])
            else:
                runs[-1].append(number)
        for run in runs:
            if len(run) >= 3:
                self.add(
                    "info",
                    "commented-out-content",
                    run[0],
                    f"A block of {len(run)} commented TeX lines remains; verify it is intentional for submission.",
                )

    def audit_environment_balance(self) -> None:
        stack: list[tuple[str, int]] = []
        token_pattern = re.compile(r"\\(begin|end)\{([^}]+)\}")
        for match in token_pattern.finditer(self.active_text):
            action, environment = match.group(1), match.group(2)
            line = line_for_offset(self.active_text, match.start())
            if action == "begin":
                stack.append((environment, line))
                continue
            if not stack:
                self.add(
                    "error",
                    "environment-balance",
                    line,
                    f"\\end{{{environment}}} has no matching begin.",
                )
                continue
            open_environment, open_line = stack.pop()
            if open_environment != environment:
                self.add(
                    "error",
                    "environment-balance",
                    line,
                    f"\\end{{{environment}}} closes \\begin{{{open_environment}}} from line {open_line}.",
                )
        for environment, line in stack:
            self.add(
                "error",
                "environment-balance",
                line,
                f"\\begin{{{environment}}} has no matching end.",
            )

    def audit_labels_and_references(self) -> None:
        label_entries: list[tuple[str, int]] = []
        label_pattern = r"\\label(?:\[[^\]]+\])?\{([^}]*)\}"
        for match in re.finditer(label_pattern, self.active_text):
            label = match.group(1).strip()
            line = line_for_offset(self.active_text, match.start())
            if not label:
                self.add("error", "empty-label", line, "Empty \\label{} found.")
                continue
            label_entries.append((label, line))
        label_counts = Counter(label for label, _ in label_entries)
        first_lines = {label: line for label, line in label_entries}
        for label, count in sorted(label_counts.items()):
            if count > 1:
                self.add(
                    "error",
                    "duplicate-label",
                    first_lines[label],
                    f"Label '{label}' is defined {count} times.",
                )

        refs: dict[str, int] = {}
        ref_pattern = re.compile(
            r"\\(?:Crefrange|crefrange|Cref|cref|ref|eqref|pageref|autoref|vref)"
            r"\*?\s*\{([^}]+)\}"
        )
        for match in ref_pattern.finditer(self.active_text):
            line = line_for_offset(self.active_text, match.start())
            for label in match.group(1).split(","):
                clean_label = label.strip()
                if clean_label:
                    refs.setdefault(clean_label, line)
        for label, line in sorted(refs.items()):
            if label not in label_counts:
                self.add(
                    "error",
                    "undefined-reference",
                    line,
                    f"Reference target '{label}' is not defined in this file.",
                )

        for label, line in label_entries:
            if re.search(r"\s", label):
                self.add(
                    "warning",
                    "label-whitespace",
                    line,
                    f"Label '{label}' contains whitespace; use a stable semantic identifier without spaces.",
                )
            if label not in refs:
                self.add(
                    "info",
                    "unused-label",
                    line,
                    f"Label '{label}' is not referenced in this file.",
                )

        bare_ref = re.compile(r"\\ref\*?\s*\{([^}]*)\}")
        for match in bare_ref.finditer(self.active_text):
            line = line_for_offset(self.active_text, match.start())
            source_line = self.active_lines[line - 1]
            if re.search(r"\\(?:newcommand|renewcommand|providecommand|def)\b", source_line):
                continue
            self.add(
                "warning",
                "bare-ref",
                line,
                "Bare \\ref found; use semantic \\Cref under this project's house style.",
            )

        incomplete_subitem_patterns = (
            re.compile(
                r"\b(?:part|parts|item|items)\s*~?\s*\((?:[ivxlcdm]+|\d+[a-z]?)\)",
                re.IGNORECASE,
            ),
            re.compile(
                r"\b(?:for|in)\s*~?\s*\((?:[ivxlcdm]+|\d+[a-z]?)\)\s*[,;:]",
                re.IGNORECASE,
            ),
        )
        for pattern in incomplete_subitem_patterns:
            for match in pattern.finditer(self.active_text):
                self.add(
                    "warning",
                    "incomplete-internal-locator",
                    line_for_offset(self.active_text, match.start()),
                    f"Partial internal locator '{match.group(0)}' found; label the theorem or claim subitem and use \\Cref so the rendered reference includes the complete parent path.",
                )

        ambiguous_singleton = re.compile(
            r"\b(?:sequence|case|condition|formula|equation|identity|alternative)\s+is\s+\\\(\s*\d+[a-z]?\s*\\\)",
            re.IGNORECASE,
        )
        for match in ambiguous_singleton.finditer(self.active_text):
            self.add(
                "warning",
                "ambiguous-parenthesized-data",
                line_for_offset(self.active_text, match.start()),
                "A bare parenthesized value can be mistaken for an equation or item number; state what the value denotes or use explicit sequence/set notation.",
            )

    def audit_citations(self) -> None:
        citations = collect_citation_keys(self.active_text)
        keys, inline_keys, found_source = bibliography_keys(self.path, self.active_text)
        placeholder = re.compile(r"^(?:xxx|todo|tbd|cite|citation)$", re.IGNORECASE)
        for key, line in sorted(citations.items()):
            if placeholder.match(key):
                self.add(
                    "error",
                    "placeholder-citation",
                    line,
                    f"Citation key '{key}' is a placeholder.",
                )
            elif found_source and key not in keys:
                self.add(
                    "error",
                    "undefined-citation",
                    line,
                    f"Citation key '{key}' was not found in the available bibliography source.",
                )
        if citations and not found_source:
            first_line = min(citations.values())
            self.add(
                "warning",
                "bibliography-unavailable",
                first_line,
                "Citations exist, but no readable inline or external bibliography source was found; citation verification is a readiness blocker until the source is supplied.",
            )
        for key in sorted(inline_keys - set(citations)):
            match = re.search(
                rf"\\bibitem(?:\[[^\]]*\])?\{{{re.escape(key)}\}}", self.active_text
            )
            line = line_for_offset(self.active_text, match.start()) if match else 1
            self.add(
                "info",
                "uncited-bibitem",
                line,
                f"Inline bibliography item '{key}' is not cited.",
            )

    def audit_theorem_labels(self) -> None:
        environment_names = "|".join(sorted(THEOREM_ENVS, key=len, reverse=True))
        pattern = re.compile(
            rf"\\begin\{{({environment_names})\}}(.*?)\\end\{{\1\}}",
            re.DOTALL,
        )
        for match in pattern.finditer(self.active_text):
            environment = match.group(1)
            body = match.group(2)
            line = line_for_offset(self.active_text, match.start())
            nested = re.search(r"\\begin\{", body)
            labels = list(re.finditer(r"\\label(?:\[[^\]]+\])?\{([^}]*)\}", body))
            labels_before_nested = [
                label for label in labels if nested is None or label.start() < nested.start()
            ]
            if not labels_before_nested:
                self.add(
                    "warning",
                    "unlabeled-result",
                    line,
                    f"{environment.capitalize()} environment has no result label near its opening.",
                )
                continue

            label_match = labels_before_nested[0]
            label = label_match.group(1).strip()
            expected_prefix = THEOREM_LABEL_PREFIXES[environment]
            if label and not label.startswith(expected_prefix):
                label_line = line_for_offset(
                    self.active_text, match.start(2) + label_match.start()
                )
                self.add(
                    "warning",
                    "result-label-prefix",
                    label_line,
                    f"{environment.capitalize()} label '{label}' should use prefix '{expected_prefix}'.",
                )

            leading = body[: label_match.start()]
            if not re.fullmatch(r"\s*(?:\[[^\]]*\]\s*)?", leading):
                label_line = line_for_offset(
                    self.active_text, match.start(2) + label_match.start()
                )
                self.add(
                    "info",
                    "result-label-placement",
                    label_line,
                    f"Place the {environment} label immediately after the environment opening (and optional title).",
                )

    def audit_equation_labels(self) -> None:
        environment_names = "|".join(
            sorted(NUMBERED_DISPLAY_ENVS, key=len, reverse=True)
        )
        pattern = re.compile(
            rf"\\begin\{{({environment_names})(\*?)\}}(.*?)\\end\{{\1\2\}}",
            re.DOTALL,
        )
        for match in pattern.finditer(self.active_text):
            environment, star, body = match.group(1), match.group(2), match.group(3)
            line = line_for_offset(self.active_text, match.start())
            labels = list(re.finditer(r"\\label(?:\[[^\]]+\])?\{([^}]*)\}", body))
            if star and labels:
                self.add(
                    "warning",
                    "label-in-unnumbered-display",
                    line,
                    f"{environment}* is unnumbered but contains a label.",
                )
            if not star and not labels and not re.search(r"\\tag\*?\s*\{", body):
                self.add(
                    "info",
                    "numbered-display-without-label",
                    line,
                    f"Numbered {environment} display has no label; number only displays that need stable reference.",
                )
            for label_match in labels:
                label = label_match.group(1).strip()
                if label and not label.startswith("eq:"):
                    label_line = line_for_offset(
                        self.active_text, match.start(3) + label_match.start()
                    )
                    self.add(
                        "warning",
                        "equation-label-prefix",
                        label_line,
                        f"Display label '{label}' should use prefix 'eq:'.",
                    )

    def audit_figures_and_inputs(self) -> None:
        float_pattern = re.compile(
            r"\\begin\{((?:figure|table)\*?)\}(.*?)\\end\{\1\}", re.DOTALL
        )
        for float_match in float_pattern.finditer(self.active_text):
            environment = float_match.group(1)
            kind = environment.rstrip("*")
            body = float_match.group(2)
            line = line_for_offset(self.active_text, float_match.start())
            captions = list(
                re.finditer(r"\\caption(?:\[[^\]]*\])?\s*\{([^}]*)\}", body)
            )
            if not captions:
                self.add(
                    "warning",
                    f"missing-{kind}-caption",
                    line,
                    f"{kind.capitalize()} environment has no caption.",
                )
            elif any(not caption.group(1).strip() for caption in captions):
                self.add(
                    "error",
                    f"empty-{kind}-caption",
                    line,
                    f"{kind.capitalize()} environment has an empty caption.",
                )
            labels = list(re.finditer(r"\\label(?:\[[^\]]+\])?\{([^}]*)\}", body))
            if not labels:
                self.add(
                    "warning",
                    f"unlabeled-{kind}",
                    line,
                    f"{kind.capitalize()} environment has no label for stable cross-referencing.",
                )
            else:
                expected_prefix = "fig:" if kind == "figure" else "tab:"
                label_match = labels[0]
                label = label_match.group(1).strip()
                label_line = line_for_offset(
                    self.active_text, float_match.start(2) + label_match.start()
                )
                if label and not label.startswith(expected_prefix):
                    self.add(
                        "warning",
                        f"{kind}-label-prefix",
                        label_line,
                        f"{kind.capitalize()} label '{label}' should use prefix '{expected_prefix}'.",
                    )
                if captions and label_match.start() < captions[0].start():
                    self.add(
                        "warning",
                        f"{kind}-label-before-caption",
                        label_line,
                        f"Place the {kind} label after its caption so it receives the correct counter value.",
                    )

        graphic_dirs = [self.path.parent]
        for outer in re.finditer(
            r"\\graphicspath\s*\{((?:\s*\{[^}]*\}\s*)+)\}", self.active_text
        ):
            for directory in re.findall(r"\{([^}]*)\}", outer.group(1)):
                if directory.strip() and "\\" not in directory:
                    graphic_dirs.append(self.path.parent / directory.strip())

        for graphic in re.finditer(
            r"\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}", self.active_text
        ):
            value = graphic.group(1).strip()
            line = line_for_offset(self.active_text, graphic.start())
            if not value or "\\" in value or "#" in value:
                self.add(
                    "info",
                    "dynamic-graphic-path",
                    line,
                    f"Graphic path '{value}' is empty or macro-generated and was not resolved mechanically.",
                )
                continue
            candidate = Path(value)
            search_paths: list[Path] = []
            for directory in graphic_dirs:
                base = candidate if candidate.is_absolute() else directory / candidate
                if base.suffix:
                    search_paths.append(base)
                else:
                    search_paths.extend(base.with_suffix(extension) for extension in GRAPHIC_EXTENSIONS)
            if not any(path.exists() for path in search_paths):
                self.add(
                    "error",
                    "missing-graphic",
                    line,
                    f"Included graphic '{value}' was not found relative to the TeX file or graphicspath.",
                )

        for included in re.finditer(
            r"\\(?:input|include)\s*\{([^}]+)\}", self.active_text
        ):
            value = included.group(1).strip()
            line = line_for_offset(self.active_text, included.start())
            if not value or "\\" in value or "#" in value:
                continue
            candidate = Path(value)
            if not candidate.suffix:
                candidate = candidate.with_suffix(".tex")
            if not candidate.is_absolute():
                candidate = self.path.parent / candidate
            if not candidate.exists():
                self.add(
                    "error",
                    "missing-input",
                    line,
                    f"Included TeX file '{value}' was not found relative to the root file.",
                )

    def audit_preamble_and_tikz(self) -> None:
        begin_document = re.search(r"\\begin\{document\}", self.active_text)
        if not begin_document:
            return

        body_offset = begin_document.end()
        body = self.active_text[body_offset:]
        preamble_only_commands = (
            (r"\\(?:documentclass|usepackage)\b", "error", "package-command-in-body", "Document-class or package loading command occurs after \\begin{document}."),
            (r"\\(?:newtheorem|theoremstyle)\b", "warning", "theorem-definition-in-body", "Theorem configuration occurs after \\begin{document}; keep global environments in the preamble."),
            (r"\\(?:DeclareMathOperator|crefname|Crefname)\b", "warning", "global-definition-in-body", "A global operator or cleveref definition occurs after \\begin{document}; keep it in the preamble."),
            (r"\\(?:title|author|date)\b", "warning", "metadata-in-body", "Document metadata occurs after \\begin{document}; keep it in the preamble."),
        )
        for pattern, severity, category, message in preamble_only_commands:
            for match in re.finditer(pattern, body):
                self.add(
                    severity,
                    category,
                    line_for_offset(self.active_text, body_offset + match.start()),
                    message,
                )

        global_macro = re.compile(
            r"\\(?:newcommand|renewcommand|providecommand|newenvironment|renewenvironment)\b"
        )
        for match in global_macro.finditer(body):
            self.add(
                "info",
                "macro-definition-in-body",
                line_for_offset(self.active_text, body_offset + match.start()),
                "A command or environment is defined after \\begin{document}; move project-wide definitions to the preamble unless the scope is intentionally local.",
            )

        package_entries: list[tuple[str, int, int]] = []
        for match in re.finditer(
            r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}", self.active_text
        ):
            for package in match.group(1).split(","):
                clean_package = package.strip()
                if clean_package:
                    package_entries.append(
                        (
                            clean_package,
                            match.start(),
                            line_for_offset(self.active_text, match.start()),
                        )
                    )
        package_names = {package for package, _, _ in package_entries}
        if "color" in package_names and "xcolor" in package_names:
            line = min(
                line for package, _, line in package_entries if package in {"color", "xcolor"}
            )
            self.add(
                "warning",
                "redundant-color-packages",
                line,
                "Both 'color' and 'xcolor' are loaded; use 'xcolor' alone unless a class-specific reason is documented.",
            )
        first_position = {
            package: min(position for name, position, _ in package_entries if name == package)
            for package in package_names
        }
        if (
            "hyperref" in first_position
            and "cleveref" in first_position
            and first_position["cleveref"] < first_position["hyperref"]
        ):
            line = min(
                line for package, _, line in package_entries if package == "cleveref"
            )
            self.add(
                "warning",
                "package-order",
                line,
                "'cleveref' is loaded before 'hyperref'; the usual order is hyperref followed by cleveref unless the class documents otherwise.",
            )
        for bibliography_package in ("natbib", "biblatex"):
            if (
                bibliography_package in first_position
                and "hyperref" in first_position
                and first_position["hyperref"] < first_position[bibliography_package]
            ):
                line = min(
                    line
                    for package, _, line in package_entries
                    if package == bibliography_package
                )
                self.add(
                    "info",
                    "package-order",
                    line,
                    f"'{bibliography_package}' is loaded after 'hyperref'; the usual generic order is bibliography support, then hyperref, then cleveref, subject to the document class.",
                )

        tikz_matches = list(re.finditer(r"\\begin\{tikzpicture\}", self.active_text))
        self.structure["tikzpicture_count"] = len(tikz_matches)
        if not tikz_matches:
            return
        if "tikz" not in package_names and not re.search(
            r"\\RequirePackage(?:\[[^\]]*\])?\{[^}]*\btikz\b[^}]*\}",
            self.active_text,
        ):
            self.add(
                "warning",
                "tikz-package-unseen",
                line_for_offset(self.active_text, tikz_matches[0].start()),
                "A tikzpicture is present, but this root file does not visibly load TikZ; verify the class or an included preamble supplies it.",
            )
        for match in re.finditer(r"\\tikzstyle\s*\{", self.active_text):
            self.add(
                "warning",
                "legacy-tikz-style",
                line_for_offset(self.active_text, match.start()),
                "Legacy \\tikzstyle syntax found; prefer \\tikzset or '/.style=' definitions.",
            )

    def audit_style_smells(self) -> None:
        duplicate_word = re.compile(r"\b([A-Za-z]{2,})\s+\1\b", re.IGNORECASE)
        ease_claim = re.compile(r"\b(?:obviously|clearly|trivially|it is easy to see)\b", re.IGNORECASE)
        diary = re.compile(
            r"\b(?:now we (?:consider|create|define|prove|show)|next we (?:consider|prove|show)|we want to (?:prove|show))\b",
            re.IGNORECASE,
        )
        boundary_parametrization = re.compile(
            r"(?:r\s*=\s*2\s*s\s*\+\s*3.{0,120}s\s*\\ge(?:q)?\s*0|"
            r"s\s*\\ge(?:q)?\s*0.{0,120}r\s*=\s*2\s*s\s*\+\s*3)",
            re.IGNORECASE,
        )
        house_style_patterns = (
            (
                re.compile(r"\bwe\s+compute\b", re.IGNORECASE),
                "house-style-compute",
                "Generic 'we compute' found; under this house style, state the consequence with 'we have/obtain' unless an actual computation is meant.",
            ),
            (
                re.compile(r"\bwe\s+argue\b", re.IGNORECASE),
                "house-style-argue",
                "'We argue' found; use 'we prove', 'we claim', or the exact logical relation under this house style.",
            ),
            (
                re.compile(r"(?:^|[.!?]\s+)Set\s+(?=\$|\\\(|\\\[)"),
                "house-style-set",
                "Sentence-level 'Set' introduces a mathematical object; prefer 'Let' unless this is an imperative modification of an existing object.",
            ),
            (
                re.compile(r"\b(?:we\s+)?write\b", re.IGNORECASE),
                "house-style-write",
                "Generic 'Write/We write' found; under this house style, use 'Let', 'denote', 'represent', or the exact conditional parametrization unless literal writing is meant.",
            ),
            (
                re.compile(r"\bas\s+usual\b", re.IGNORECASE),
                "unsupported-as-usual",
                "'As usual' is not a proof warrant under this house style; state the convention, boundary case, symmetry, or cited earlier rule explicitly.",
            ),
            (
                re.compile(r"\bnow\s+(?:suppose|assume|let|consider)\b", re.IGNORECASE),
                "temporal-proof-transition",
                "Temporal proof transition found; name the remaining case or the mathematical purpose instead.",
            ),
            (
                re.compile(r"\bwe\s+got\b", re.IGNORECASE),
                "informal-proof-verb",
                "Informal 'we got' found; use 'we have', 'we obtain', or 'it follows that'.",
            ),
            (
                re.compile(r"\bwe\s+shall\s+prove\b", re.IGNORECASE),
                "house-style-proof-tense",
                "Use the direct present-tense 'we prove' for the proof now being given.",
            ),
            (
                re.compile(r"\bwe\s+discover\b", re.IGNORECASE),
                "discovery-order-verb",
                "'We discover' narrates the research process; use 'we prove', 'we show', or 'we observe' according to the claim's status.",
            ),
            (
                re.compile(r"\breaches?\s+the\s+equality\b", re.IGNORECASE),
                "nonidiomatic-equality",
                "Use 'equality holds' or 'attains the bound' instead of 'reaches the equality'.",
            ),
            (
                re.compile(r"\bsatisf(?:y|ies)\s+that\b", re.IGNORECASE),
                "nonidiomatic-satisfies-that",
                "Use 'satisfies ...' or 'has the property that ...' rather than 'satisfies that'.",
            ),
            (
                re.compile(r"\bIt\s+implies\b"),
                "vague-antecedent",
                "'It implies' has a vague antecedent; use 'This implies' or name the premise.",
            ),
            (
                re.compile(r"\bthe\s+common\s+vertex\b", re.IGNORECASE),
                "edge-endpoint-wording",
                "If two edges are meant, prefer 'a common endpoint' to 'the common vertex'.",
            ),
            (
                re.compile(r"\bformer\s+neighbors?\b", re.IGNORECASE),
                "ordering-wording",
                "For a vertex ordering, use 'earlier neighbors' or 'predecessors'; 'former' does not encode order.",
            ),
            (
                re.compile(r"\bin\s+the\s+end\s+of\s+this\s+section\b", re.IGNORECASE),
                "nonidiomatic-section-transition",
                "Use 'at the end of this section' if chronology matters, or state the next result's mathematical role.",
            ),
        )
        west_style_patterns = (
            (
                re.compile(
                    r"\b(?:can['’]t|won['’]t|isn['’]t|aren['’]t|wasn['’]t|weren['’]t|"
                    r"don['’]t|doesn['’]t|didn['’]t|hasn['’]t|haven['’]t|hadn['’]t|"
                    r"couldn['’]t|shouldn['’]t|wouldn['’]t|mustn['’]t|let['’]s|it['’]s|"
                    r"(?:we|they|you)['’](?:re|ve|ll|d))\b",
                    re.IGNORECASE,
                ),
                "west-contraction",
                "West Rule 64: avoid contractions in formal mathematical prose.",
            ),
            (
                re.compile(r"(?<![A-Za-z])(?:i\.e\.|e\.g\.)(?![A-Za-z])", re.IGNORECASE),
                "west-latin-abbreviation",
                "West Rule 65: prefer 'that is' or 'for example' to 'i.e.' or 'e.g.'.",
            ),
            (
                re.compile(r"\b(?:different|differs?)\s+than\b", re.IGNORECASE),
                "west-different-than",
                "West Rule 66: use 'different from' or 'differs from'.",
            ),
            (
                re.compile(
                    r"\bthe\s+(?:above|below)\s+(?:argument|claim|corollary|definition|"
                    r"discussion|equation|example|figure|graph|lemma|proof|proposition|"
                    r"result|section|table|theorem)\b",
                    re.IGNORECASE,
                ),
                "west-above-below-position",
                "West Rule 77: prefer the postpositive form, such as 'the theorem above'.",
            ),
            (
                re.compile(r"\b(?:left|right)-hand\s+side\b", re.IGNORECASE),
                "west-hand-side",
                "West Rule 57: prefer 'left side' or 'right side'.",
            ),
            (
                re.compile(r"\b(?:discuss(?:es|ed|ing)?|stud(?:y|ies|ied|ying))\s+about\b", re.IGNORECASE),
                "west-verb-about",
                "West Rule 92: use 'discuss' or 'study' without 'about'.",
            ),
            (
                re.compile(r"\bequals\s+to\b", re.IGNORECASE),
                "west-equals-to",
                "West Rule 92: use 'equals' or 'is equal to', not 'equals to'.",
            ),
            (
                re.compile(r"\bcontradicts?\s+to\b", re.IGNORECASE),
                "west-contradicts-to",
                "West Rule 92: use 'contradicts' without 'to'.",
            ),
            (
                re.compile(r"\ba\s+same\s+(?:argument|proof|reasoning)\b", re.IGNORECASE),
                "west-a-same",
                "West Rule 92: use 'the same' or 'a similar', not 'a same'.",
            ),
            (
                re.compile(
                    r"\bdecompos(?:e|es|ed|ing)\b(?:(?!\b(?:into|according)\b)[^.;:!?]){0,60}\bto\b",
                    re.IGNORECASE,
                ),
                "west-decompose-to",
                "West Rule 92: use 'decompose into'.",
            ),
            (
                re.compile(r"\bcan\s+not\b", re.IGNORECASE),
                "west-can-not",
                "West Rule 87: use the single word 'cannot' in this construction.",
            ),
            (
                re.compile(r"\bbounds?\s+of\b", re.IGNORECASE),
                "west-bound-of",
                "West Rule 82: normally use 'bound on', then verify the mathematical relation.",
            ),
            (
                re.compile(r"\bpartial\s+case\b", re.IGNORECASE),
                "west-partial-case",
                "West Rule 85: use 'special case' for an instance and 'partial result' for incomplete progress.",
            ),
            (
                re.compile(r"\ba\s+(?:joint\s+)?(?:work|research)\b|\ban\s+access\b", re.IGNORECASE),
                "west-uncountable-noun",
                "West Rule 88: 'work', 'research', and 'access' are normally uncountable in these uses.",
            ),
            (
                re.compile(r"\bnecessary\s+(?:the\s+)?conditions?\s+of\b", re.IGNORECASE),
                "west-necessary-conditions",
                "West Rule 92: prefer 'conditions necessary for' and verify the logical direction.",
            ),
            (
                re.compile(r"\bto\s+precise\b", re.IGNORECASE),
                "west-precise-as-verb",
                "West Rule 92: use 'make precise'; 'precise' is not a verb here.",
            ),
            (
                re.compile(r"\bas\s+evidence\s+by\b", re.IGNORECASE),
                "west-evidence-by",
                "West Rule 89: use 'as shown by' or the grammatical 'as evidenced by'.",
            ),
            (
                re.compile(r"\b(?:the\s+)?usual\s+coloring\b", re.IGNORECASE),
                "west-usual-coloring",
                "West Rule 92: name the coloring convention explicitly, such as 'proper coloring'.",
            ),
            (
                re.compile(r"\bwe\s+have\s+a\s+pick\s+up\b", re.IGNORECASE),
                "west-pick-up",
                "West Rule 92: replace this calque with the intended verb, often 'we consider'.",
            ),
            (
                re.compile(r"\bspecially\b", re.IGNORECASE),
                "west-specially",
                "West Rule 92: check whether 'especially' or the adjective 'special' is intended; retain 'specially' only in its genuine sense.",
            ),
        )
        # High-confidence prefilters adapted and rewritten from the upstream
        # Academic Research Skills writing-quality checklist; see the bundled
        # upstream attribution reference. These are review signals, not bans.
        research_suite_style_patterns = (
            (
                re.compile(
                    r"\b(?:it\s+is\s+important\s+to\s+note\s+that|"
                    r"it\s+is\s+worth\s+mentioning\s+that|"
                    r"it\s+should\s+be\s+noted\s+that|"
                    r"it\s+goes\s+without\s+saying\s+that)\b",
                    re.IGNORECASE,
                ),
                "research-suite-throat-clearing",
                "Throat-clearing opener found; state the mathematical claim or reason directly.",
            ),
            (
                re.compile(
                    r"\b(?:this\s+section\s+will\s+(?:discuss|examine|explore|present)|"
                    r"the\s+following\s+(?:paragraph|section)\s+(?:discusses|examines|explores|presents)|"
                    r"we\s+now\s+turn\s+our\s+attention\s+to)\b",
                    re.IGNORECASE,
                ),
                "research-suite-meta-writing",
                "Meta-writing found; usually begin with the section's actual claim, object, or purpose.",
            ),
            (
                re.compile(r"\bin\s+order\s+to\b", re.IGNORECASE),
                "research-suite-in-order-to",
                "Review 'in order to'; plain 'to' is usually more concise.",
            ),
            (
                re.compile(
                    r"\b(?:delv(?:e|es|ed|ing)\s+into|"
                    r"serves?\s+as\s+a\s+testament\s+to|"
                    r"in\s+today['’]s\s+rapidly\s+evolving|"
                    r"at\s+the\s+end\s+of\s+the\s+day|"
                    r"with\s+that\s+being\s+said)\b",
                    re.IGNORECASE,
                ),
                "research-suite-cliche",
                "Generic academic cliché found; replace it with the exact mathematical action or relation.",
            ),
        )
        blank_run_start: int | None = None
        stacked_blank_runs: list[tuple[int, int]] = []
        for index, raw_line in enumerate(self.lines):
            if not raw_line.strip():
                if blank_run_start is None:
                    blank_run_start = index
                continue
            if blank_run_start is not None:
                run_length = index - blank_run_start
                if blank_run_start > 0 and run_length >= 2:
                    stacked_blank_runs.append((blank_run_start + 1, run_length))
                blank_run_start = None
        if stacked_blank_runs:
            first_line = stacked_blank_runs[0][0]
            longest = max(length for _, length in stacked_blank_runs)
            self.add(
                "info",
                "stacked-blank-lines",
                first_line,
                f"Found {len(stacked_blank_runs)} interior runs of consecutive blank source lines (longest: {longest}); one blank line is sufficient for a paragraph boundary.",
            )
        write_hit_lines: list[int] = []
        em_dash_count = 0
        em_dash_first_line: int | None = None
        for line_number, line in enumerate(self.active_lines, 1):
            duplicate = duplicate_word.search(line)
            if duplicate:
                self.add(
                    "warning",
                    "duplicate-word",
                    line_number,
                    f"Repeated word '{duplicate.group(1)} {duplicate.group(1)}'.",
                )
            if ease_claim.search(line):
                self.add(
                    "info",
                    "unsupported-ease-word",
                    line_number,
                    "Ease claim found; omit it or state the reason if the step matters.",
                )
            if diary.search(line):
                self.add(
                    "info",
                    "discovery-order-transition",
                    line_number,
                    "Diary-like transition found; consider naming the logical purpose instead.",
                )
            if boundary_parametrization.search(line):
                self.add(
                    "warning",
                    "boundary-parametrization",
                    line_number,
                    "The parametrization r=2s+3 is paired with s>=0; handle r=3 explicitly, then use s>=1 for the repeated pattern.",
                )
            for pattern, category, message in house_style_patterns:
                matches = list(pattern.finditer(line))
                if matches:
                    severity = "warning" if category == "unsupported-as-usual" else "info"
                    self.add(severity, category, line_number, message)
                    if category == "house-style-write":
                        write_hit_lines.extend([line_number] * len(matches))
            for pattern, category, message in west_style_patterns:
                if pattern.search(line):
                    self.add("info", category, line_number, message)
            for pattern, category, message in research_suite_style_patterns:
                if pattern.search(line):
                    self.add("info", category, line_number, message)
            em_dash_hits = (
                line.count("—")
                + len(re.findall(r"(?<!-)---(?!-)", line))
                + len(re.findall(r"\\textemdash\b", line))
            )
            if em_dash_hits:
                em_dash_count += em_dash_hits
                if em_dash_first_line is None:
                    em_dash_first_line = line_number
            if "$$" in line:
                self.add(
                    "warning",
                    "plain-tex-display",
                    line_number,
                    "Use a LaTeX display environment instead of '$$'.",
                )
            if re.search(r"\\(?:bf|it|rm|tt|sf|sl)\b", line):
                self.add(
                    "warning",
                    "deprecated-font-command",
                    line_number,
                    "Deprecated font switch found; prefer a scoped LaTeX font command.",
                )
            if re.search(r"\s+[,.;:]", line) and not re.search(r"\\(?:quad|qquad|;|:|,)\s*[,.;:]", line):
                self.add(
                    "info",
                    "punctuation-spacing",
                    line_number,
                    "Whitespace appears immediately before punctuation.",
                )

        if em_dash_count > 3 and em_dash_first_line is not None:
            self.add(
                "info",
                "research-suite-em-dash-density",
                em_dash_first_line,
                f"Found {em_dash_count} em dashes; review whether commas, parentheses, or separate sentences would make the prose more precise.",
            )

        if len(write_hit_lines) > 1:
            self.add(
                "warning",
                "repeated-house-style-write",
                write_hit_lines[0],
                f"Generic 'Write/We write' occurs {len(write_hit_lines)} times; under this house style, repeated use fails the prose pass even if an isolated literal notation use could be justified.",
            )

        packages: dict[str, list[int]] = {}
        package_pattern = re.compile(r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}")
        for match in package_pattern.finditer(self.active_text):
            line = line_for_offset(self.active_text, match.start())
            for package in match.group(1).split(","):
                clean_package = package.strip()
                if clean_package:
                    packages.setdefault(clean_package, []).append(line)
        for package, lines in sorted(packages.items()):
            if len(lines) > 1:
                self.add(
                    "warning",
                    "duplicate-package",
                    lines[0],
                    f"Package '{package}' is loaded {len(lines)} times.",
                )


def expand_paths(values: Sequence[str]) -> list[Path]:
    paths: list[Path] = []
    for value in values:
        path = Path(value).expanduser()
        if path.is_dir():
            paths.extend(sorted(path.rglob("*.tex")))
        else:
            paths.append(path)
    unique: dict[str, Path] = {}
    for path in paths:
        unique[str(path.resolve()).lower()] = path
    return [unique[key] for key in sorted(unique)]


def render_human(report: dict[str, object]) -> str:
    lines = [f"TeX editorial audit {report['version']}"]
    for file_report in report["files"]:
        summary = file_report["summary"]
        lines.append(
            f"\n{file_report['path']}\n"
            f"  errors={summary['error']} warnings={summary['warning']} info={summary['info']}"
        )
        for issue in file_report["issues"]:
            lines.append(
                f"  {issue['severity'].upper():7} L{issue['line']:<5} "
                f"[{issue['category']}] {issue['message']}"
            )
    total = report["summary"]
    lines.append(
        f"\nTOTAL files={len(report['files'])} errors={total['error']} "
        f"warnings={total['warning']} info={total['info']}"
    )
    lines.append("This audit does not validate mathematical correctness or novelty.")
    return "\n".join(lines)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit TeX manuscripts for editorial and publication hygiene."
    )
    parser.add_argument("paths", nargs="+", help="TeX file or directory to audit")
    parser.add_argument(
        "--json",
        metavar="OUTPUT",
        help="also write the full report as JSON; use '-' for stdout-only JSON",
    )
    parser.add_argument(
        "--note-macro",
        action="append",
        default=[],
        help="custom live-note macro name to flag; repeat as needed",
    )
    parser.add_argument(
        "--fail-on",
        choices=("none", "error", "warning"),
        default="error",
        help="exit nonzero at this severity (default: error)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.json == "-" and hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="strict")
    paths = expand_paths(args.paths)
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"error: file not found: {path}", file=sys.stderr)
        return 2
    non_tex = [path for path in paths if path.suffix.lower() != ".tex"]
    if non_tex:
        for path in non_tex:
            print(f"error: not a .tex file: {path}", file=sys.stderr)
        return 2
    if not paths:
        print("error: no TeX files found", file=sys.stderr)
        return 2

    files = [TexAuditor(path, args.note_macro).audit() for path in paths]
    all_issues = [
        Issue(**issue)
        for file_report in files
        for issue in file_report["issues"]
    ]
    report: dict[str, object] = {
        "tool": "audit_tex.py",
        "version": VERSION,
        "files": files,
        "summary": issue_counts(all_issues),
        "disclaimer": "Mechanical editorial audit only; mathematics and novelty are not validated.",
    }
    json_text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.json == "-":
        sys.stdout.write(json_text)
    else:
        print(render_human(report))
        if args.json:
            output = Path(args.json).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json_text, encoding="utf-8")

    if args.fail_on == "none":
        return 0
    threshold = SEVERITY_RANK[args.fail_on]
    return 1 if any(SEVERITY_RANK[issue.severity] >= threshold for issue in all_issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
