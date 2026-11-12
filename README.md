# QA Notes

[![Deploy docs](https://github.com/Finito21/Quality_Assurance/actions/workflows/deploy.yml/badge.svg)](https://github.com/Finito21/Quality_Assurance/actions/workflows/deploy.yml)
[![MkDocs Material](https://img.shields.io/badge/MkDocs-Material-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![ISTQB CTFL](https://img.shields.io/badge/ISTQB-CTFL%20v4.0-0b5394)](https://istqb.org/)

A structured, bilingual (Polish / English) knowledge base on **Quality Assurance and software testing**, based on self-study, a software testing courses, ISTQB CTFL preparation and hands-on work with QA tools.

**Website: https://finito21.github.io/Quality_Assurance/**

## Contents

| Section | Topics |
|---|---|
| **Fundamentals** | QA/QC, testing principles, test levels and types, test techniques, test documentation, test management, performance testing |
| **Technologies** | HTML, CSS, JavaScript, SQL, APIs (REST, SOAP, GraphQL, HTTP, authorisation), API test automation, Docker, Kubernetes |
| **Tools** | DevTools, browser extensions, Git/GitHub, Selenium, Cypress, Postman, SoapUI, Swagger, JMeter, Jenkins, GitHub Actions, Grafana, Jira, Confluence, Slack, TestLink, Xray |

Every page is available in Polish (default) and English. Use the language switcher in the site header.

## Repository structure

```
.
├── docs/                      site content
│   ├── fundamentals/
│   ├── technologies/
│   ├── tools/
│   ├── assets/                images and extra.css
│   ├── *.md                   Polish pages
│   └── *.en.md                English pages
├── hooks/typography.py        MkDocs hook for Polish typesetting rules
├── scripts/                   check_translations.py (PL/EN consistency and content-rule check)
├── tests/                     unit tests for the typography hook and the translation check
├── mkdocs.yml                 site configuration and navigation
├── requirements.in            direct Python dependencies
├── requirements.txt           hashed lock generated from requirements.in
├── .github/                   workflows (checks on PRs, deploy to Pages), Dependabot, PR template
├── .claude/settings.json      Claude Code project settings
└── CLAUDE.md                  guidance for Claude Code
```

## Running locally

The project uses Python 3.12 (pinned in `.python-version`, which CI reads too).

```bash
pip install -r requirements.txt
mkdocs serve
```

The site is available at `http://127.0.0.1:8000/Quality_Assurance/`.

Before pushing, run the same checks as CI:

```bash
python -m unittest discover -s tests   # unit tests for the hook and the translation check
python scripts/check_translations.py   # PL/EN pairs, nav, nav labels, one H1, no emoji
mkdocs build --strict                  # build without warnings
```

The same checks run automatically on every pull request (`.github/workflows/checks.yml`).
External links are checked once a week by `.github/workflows/links.yml` (lychee), outside the
pull request path so that a slow or rate-limiting site never blocks a merge.

## Dependencies

Direct dependencies are listed in `requirements.in`. `requirements.txt` is a lock file with every
transitive dependency pinned and hashed. After changing `requirements.in`, regenerate it with the
Python version from `.python-version` (another version can resolve a different lock):

```bash
pip install pip-tools
pip-compile --generate-hashes --strip-extras --allow-unsafe -o requirements.txt requirements.in
```

Dependabot updates both files once a month. GitHub Actions in `.github/workflows/` are pinned to
commit SHAs (with the version in a comment); Dependabot updates those pins as well.

### MkDocs status

MkDocs 1.x is no longer actively developed, and Material for MkDocs is in maintenance mode
(critical and security fixes only, announced until May 2027). MkDocs 2.0 drops plugin support and
cannot build this site, so Dependabot ignores MkDocs major updates. The planned successor is
[Zensical](https://zensical.org/) from the Material team; this site will move to it once Zensical
supports multilingual sites (mkdocs-static-i18n) and hooks, which `hooks/typography.py` needs.

## Adding or editing a page

1. Edit or create both versions: `page.md` (Polish) and `page.en.md` (English).
2. Add new pages to `nav` in `mkdocs.yml` and an English nav label under `nav_translations`.
3. Run `python -m unittest discover -s tests`, `python scripts/check_translations.py` and `mkdocs build --strict`.

## Deployment

Every push to `main` runs the checks workflow, which builds the site and uploads it as an artifact.
`.github/workflows/deploy.yml` then publishes that artifact with `actions/deploy-pages`.

Repository settings that the deployment relies on: Settings > Pages > Source is **GitHub Actions**,
and the `github-pages` environment only accepts deployments from `main`.

## License

- **Content** (`docs/`: text and images): [CC BY 4.0](LICENSE-CONTENT)
- **Code** (hooks, scripts, tests, styles, configuration): [MIT](LICENSE)
