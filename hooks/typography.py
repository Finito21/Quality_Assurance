"""Polish typesetting: non-breaking spaces where a line must not break.

MkDocs hook that runs for every page after Markdown -> HTML conversion.
It only changes text outside of tags and outside of code blocks,
and only on Polish pages (English pages are left as they are).

Rules:
  1. one-letter words (a, i, o, u, w, z) never stay at the end of a line,
  2. abbreviations (np., tj., tzw., wg, tys. ...) stick to the next word,
  3. a number is not separated from its unit or from the next word,
  4. a relation sign (<, >, =, ≤, ≥, ±, ~) or § is not separated from the number,
  5. a dash never starts a line (non-breaking space before – and —).
"""

import re

NBSP = " "  # written as an escape so it stays visible in editors and diffs

# Tags whose content is left untouched.
SKIP_TAGS = {"pre", "code", "kbd", "samp", "script", "style", "svg", "textarea", "math"}

# Inline tags: text that ends right before one of these continues inside it,
# so "np. <code>200</code>" must still be glued.
INLINE_TAGS = {"a", "abbr", "b", "code", "em", "i", "kbd", "mark", "samp", "small", "span", "strong", "sub", "sup"}

# A tag is "<...>" where ">" inside a quoted attribute value does not end it;
# a comment is matched as a whole so its content is never treated as text.
TAG_RE = re.compile(r"(<!--.*?-->|<(?:[^>\"']|\"[^\"]*\"|'[^']*')*>)", re.S)
TAG_NAME_RE = re.compile(r"<\s*(/)?\s*([a-zA-Z0-9]+)")

LETTER = r"A-Za-zÀ-ÖØ-öø-ÿĀ-žА-я"
SPACE = r"[ \t\r\n]+"
# Stands in for the inline tag that follows a text chunk while the rules run.
NEXT = ""

RULES = [
    # 1. one-letter conjunctions and prepositions
    (re.compile(rf"(?<![{LETTER}0-9])([aiouwzAIOUWZ]){SPACE}(?=\S|$)"), rf"\1{NBSP}"),
    # 2. abbreviations with a full stop
    (re.compile(
        rf"(?<![{LETTER}])"
        rf"(np|tj|tzn|tzw|ul|nr|godz|ang|ds|im|św|dr|Dr|prof|Prof|inż|mgr|m\.in"
        rf"|rys|Rys|zob|Zob|por|Por|pkt|wg|Wg)\.{SPACE}(?=\S)"
    ), rf"\1.{NBSP}"),
    # 2a. abbreviations that also end sentences ("w 2025 r. Potem", "jest ok. Dalej"):
    #     glued only before a lowercase word, a number or an inline tag
    (re.compile(
        rf"(?<![{LETTER}])(ok|r|str|pt|tab|Tab|art)\.{SPACE}(?=[a-ząćęłńóśźż0-9{NEXT}])"
    ), rf"\1.{NBSP}"),
    # 2b. abbreviations written without a full stop
    (re.compile(rf"(?<![{LETTER}])(wg|Wg|mln|mld|tys|zł){SPACE}(?=\S)"), rf"\1{NBSP}"),
    # 3. number + unit / word
    (re.compile(rf"(?<=\d){SPACE}(?=[{LETTER}%°§{NEXT}])"), NBSP),
    # 4. relation sign or section sign + number
    (re.compile(rf"(&lt;|&gt;|[=≤≥±~×§]){SPACE}(?=[\d{NEXT}])"), rf"\1{NBSP}"),
    # 5. a dash never starts a line
    (re.compile(rf"{SPACE}(?=[–—][ \t\r\n])"), NBSP),
]


def _fix_text(text: str, before_inline: bool = False) -> str:
    if before_inline:
        text += NEXT
    for pattern, repl in RULES:
        text = pattern.sub(repl, text)
    return text.removesuffix(NEXT)


def _opens_inline(part: str) -> bool:
    m = TAG_NAME_RE.match(part)
    return bool(m) and not m.group(1) and m.group(2).lower() in INLINE_TAGS


def fix_typography(html: str) -> str:
    out = []
    skip_depth = 0
    parts = [p for p in TAG_RE.split(html) if p]
    for i, part in enumerate(parts):
        if part.startswith("<"):
            m = TAG_NAME_RE.match(part)
            if m:
                closing, name = m.group(1), m.group(2).lower()
                if name in SKIP_TAGS and not part.endswith("/>"):
                    skip_depth = max(skip_depth + (-1 if closing else 1), 0)
            out.append(part)
        elif skip_depth:
            out.append(part)
        else:
            before_inline = i + 1 < len(parts) and _opens_inline(parts[i + 1])
            out.append(_fix_text(part, before_inline))
    return "".join(out)


POLISH = "pl"


def page_language(page, config) -> str:
    """Locale of the page source: set by mkdocs-static-i18n, else the site language."""
    return getattr(page.file, "locale", None) or config["theme"]["language"]


def on_page_content(html, page, config, files):
    if page_language(page, config) != POLISH:
        return html
    return fix_typography(html)
