---
description: "GitHub Actions dla testera: workflow z testami API i E2E, artefakty, bezpieczeństwo i przykład z tego repozytorium."
---

# GitHub Actions

**GitHub Actions** to wbudowany w GitHub system **CI/CD**. Workflowy definiuje się w plikach YAML w katalogu `.github/workflows/` i uruchamiają się one automatycznie na zdarzenia w repozytorium (push, pull request, harmonogram).

## Pojęcia

| Pojęcie | Opis |
|---|---|
| **Workflow** | plik YAML opisujący proces automatyzacji |
| **Event (`on`)** | zdarzenie uruchamiające: `push`, `pull_request`, `schedule`, `workflow_dispatch` |
| **Job** | zestaw kroków na jednej maszynie (runnerze), joby mogą działać równolegle |
| **Step** | pojedyncza komenda (`run`) lub gotowa akcja (`uses`) |
| **Runner** | maszyna wykonująca job (`ubuntu-latest`, `windows-latest`…) |
| **Secrets** | zaszyfrowane zmienne (tokeny, hasła): `${{ secrets.NAZWA }}` |
| **Artifacts** | pliki zachowane po workflow (np. raporty z testów) |

## Przykład: testy API i E2E przy każdym PR

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
      - uses: cypress-io/github-action@v7 # testy na środowisku z baseUrl (np. staging)
      - uses: actions/upload-artifact@v7
        if: failure()
        with:
          name: cypress-screenshots
          path: cypress/screenshots
```

!!! warning "Bezpieczeństwo workflow"
    W prawdziwym projekcie przypinaj akcje firm trzecich do pełnego SHA commita zamiast tagu (`@v7`), ustaw minimalne `permissions` (np. `contents: read`) i nigdy nie wstawiaj `${{ github.event.* }}` bezpośrednio do `run:`. Sekrety trzymaj w *Secrets*, nie w repozytorium.

## Przykład z tego repozytorium

Ta strona jest sprawdzana i publikowana automatycznie przez GitHub Actions po każdym pushu na `main` (pliki `.github/workflows/checks.yml` i `deploy.yml`). Workflow `deploy.yml` wywołuje workflow `checks.yml` (testy, kontrola tłumaczeń, build `--strict`), a dopiero po jego sukcesie publikuje zbudowaną stronę:

```yaml
jobs:
  checks:
    uses: ./.github/workflows/checks.yml
  deploy:
    needs: checks
    steps:
      - uses: actions/deploy-pages@v5
```

## Jenkins a GitHub Actions

| | Jenkins | GitHub Actions |
|---|---|---|
| Hosting | własny serwer | chmura GitHub (lub self-hosted runner) |
| Konfiguracja | `Jenkinsfile` (Groovy) + GUI | YAML w repo |
| Rozszerzenia | pluginy | akcje z Marketplace |
| Najlepszy dla | dużych, złożonych środowisk firmowych | projektów na GitHubie |
