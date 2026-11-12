---
description: "GitHub Actions for testers: a workflow with API and E2E tests, artifacts, security and an example from this repository."
---

# GitHub Actions

**GitHub Actions** is the **CI/CD** system built into GitHub. Workflows are defined in YAML files in the `.github/workflows/` directory and run automatically on repository events (push, pull request, schedule).

## Concepts

| Concept | Description |
|---|---|
| **Workflow** | a YAML file describing the automation process |
| **Event (`on`)** | the triggering event: `push`, `pull_request`, `schedule`, `workflow_dispatch` |
| **Job** | a set of steps on one machine (runner), jobs can run in parallel |
| **Step** | a single command (`run`) or a ready-made action (`uses`) |
| **Runner** | the machine that runs a job (`ubuntu-latest`, `windows-latest`…) |
| **Secrets** | encrypted variables (tokens, passwords): `${{ secrets.NAME }}` |
| **Artifacts** | files kept after a workflow (e.g. test reports) |

## Example: API and E2E tests on every PR

```yaml title=".github/workflows/tests.yml"
name: Tests

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  api-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: 22
      - run: npm install -g newman
      - run: newman run tests/api.json -e env/qa.json

  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: cypress-io/github-action@v7 # runs against the baseUrl environment (e.g. staging)
      - uses: actions/upload-artifact@v7
        if: failure()
        with:
          name: cypress-screenshots
          path: cypress/screenshots
```

!!! warning "Workflow security"
    In a real project pin third-party actions to a full commit SHA instead of a tag (`@v7`), set minimal `permissions` (e.g. `contents: read`) and never put `${{ github.event.* }}` directly into `run:`. Keep secrets in *Secrets*, not in the repository.

## Example from this repository

This site is checked and published automatically by GitHub Actions after every push to `main` (the `.github/workflows/checks.yml` and `deploy.yml` files). The `deploy.yml` workflow calls `checks.yml` (tests, translation check, `--strict` build) and publishes the built site only if it succeeds:

```yaml
jobs:
  checks:
    uses: ./.github/workflows/checks.yml
  deploy:
    needs: checks
    steps:
      - uses: actions/deploy-pages@v5
```

## Jenkins vs GitHub Actions

| | Jenkins | GitHub Actions |
|---|---|---|
| Hosting | your own server | GitHub cloud (or a self-hosted runner) |
| Configuration | `Jenkinsfile` (Groovy) + GUI | YAML in the repo |
| Extensions | plugins | actions from the Marketplace |
| Best for | large, complex corporate environments | projects on GitHub |
