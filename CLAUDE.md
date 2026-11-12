# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project

**QA Notes** is a bilingual (Polish / English) knowledge base about Quality Assurance and software testing, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages at <https://finito21.github.io/Quality_Assurance/>.

Polish is the default language of the site. English is a full translation, not a subset.

## Commands

```bash
pip install -r requirements.txt     # install locked dependencies (hashed)
mkdocs serve                        # local preview at http://127.0.0.1:8000/Quality_Assurance/
python -m unittest discover -s tests   # tests for the typography hook and the translation check
python scripts/check_translations.py   # PL/EN pages in sync, nav and nav labels, one H1, no emoji
mkdocs build --strict               # build check
```

Run all three checks before finishing any change. CI runs them too and blocks deployment on failure.

Never run `mkdocs gh-deploy` locally. Deployment happens only in CI (`.github/workflows/deploy.yml`) on every push to `main`: it calls `checks.yml` and publishes the uploaded build with `actions/deploy-pages`.

Direct dependencies go in `requirements.in`; `requirements.txt` is a hashed lock generated with `pip-compile` (see README). Never edit the lock by hand.

## Layout

```
docs/
  index.md / index.en.md        home page (hero + cards)
  fundamentals/                 ISTQB theory: techniques, documentation, management, performance
  technologies/                 frontend, backend (SQL), API, DevOps
  tools/                        DevTools, Git, automation, API tools, CI/CD, monitoring, test management, collaboration
  resources.md                  sources
  assets/images/                images used by pages
  assets/stylesheets/extra.css  all custom styling (light + dark scheme)
overrides/404.html              bilingual 404 page (GitHub Pages serves one root 404)
hooks/typography.py             MkDocs hook: Polish non-breaking-space rules
scripts/check_translations.py   CI check: every page exists in PL and EN, is in nav (no dead nav entries), nav titles have EN labels,
                                EN has no Polish text (front matter included), one H1 and a description per page, no emoji/icon shortcodes/&nbsp;
tests/                          unit tests for the typography hook and the translation check (stdlib unittest)
.github/ISSUE_TEMPLATE/         issue forms: content error, translation
.github/dependabot.yml          dependency and Actions updates
.github/workflows/checks.yml    tests, translation check, strict build, site artifact; on PRs and called by deploy
.github/workflows/deploy.yml    on push to main: calls checks.yml, then deploys the artifact to Pages
.github/workflows/links.yml     weekly external link check (lychee), not on PRs
.python-version                 Python version for CI and for regenerating the lock
mkdocs.yml                      site config, nav, i18n, link/anchor validation, markdown extensions
requirements.in / .txt          direct dependencies / hashed lock
```

## Rules for content

- **Every page exists in two languages.** `page.md` is Polish, `page.en.md` is English (mkdocs-static-i18n, `suffix` structure). When you add or change a page, update both files in the same change.
- **New pages must be added to `nav` in `mkdocs.yml`.** Add an English label for any new nav title under `plugins.i18n.languages[en].nav_translations`.
- **Anchor links differ between languages.** Headings are translated, so `#raport-o-defekcie` in Polish is `#defect-report` in English. Fix both when renaming a heading.
- **No emojis, no decorative icons** (`:material-...:` shortcodes, flag emojis), **no header logo, no heading permalinks.** Use plain text; replace an icon that carries meaning with words.
- **Polish typography** is handled by `hooks/typography.py` at build time. Do not insert `&nbsp;` by hand; extend the hook's `RULES` instead and add a test in `tests/test_typography.py`.
- **One `#` (H1) per page**, as the page title. Sections are `##` and `###`.
- **Every page has a `description`** in its front matter (120-160 characters, in the page's language); it becomes the meta description used in search results.
- **URLs are directory-style** (`/tools/devtools/`). Link to other pages by their `.md` path; MkDocs converts the links.
- **Content is CC BY 4.0, code is MIT** (`LICENSE-CONTENT`, `LICENSE`).
- Keep pages concise and practical, written from a tester's point of view. Prefer tables, short lists, admonitions (`!!! tip`, `!!! warning`), content tabs and Mermaid diagrams over long prose.
- Translate comments, identifiers and strings inside code samples and Mermaid labels together with the prose (the translation check scans them on English pages).
- Polish quoted on purpose on an English page (e.g. the glossary) goes in `<span lang="pl">…</span>`; the check skips it and screen readers switch language.
- Give every Mermaid diagram an `accTitle:` line (and `accDescr:` when the text around it does not explain it).
- Abbreviation tooltips live in `includes/abbreviations.md`, appended to every page.

## Rules for styling

- All custom CSS lives in `docs/assets/stylesheets/extra.css`.
- Define colours as variables for both schemes (`[data-md-color-scheme="default"]` and `[data-md-color-scheme="slate"]`) and check both light and dark mode.
- Check narrow screens (phone width) for the home page hero and cards.

## Repository conventions

- Repository-level files (README, CLAUDE.md, code comments, commit messages) are written in **English**.
- Commit messages: short imperative subject (`Add …`, `Fix …`, `Translate …`), one logical change per commit.
- Work on a branch, never commit directly to `main`. Open pull requests with the `/pr` command (`.claude/commands/pr.md`), which fills in `.github/pull_request_template.md`.
- Do not commit the generated `site/` directory.
