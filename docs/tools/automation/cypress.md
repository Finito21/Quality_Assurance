---
description: "Cypress: instalacja, struktura testów, selektory, przykład testu logowania i uruchamianie w CI."
---

# Cypress

**Cypress** to narzędzie do testowania frontendu aplikacji webowych. Umożliwia pisanie, uruchamianie i debugowanie testów **end-to-end**, **komponentowych** i integracyjnych. Testy pisze się w JavaScripcie lub TypeScripcie.

## Dlaczego Cypress?

- **łatwy start**: instalacja przez npm, gotowa struktura projektu,
- **pełna kontrola**: działa w tej samej pętli co aplikacja, ma dostęp do DOM i sieci,
- **szybkość i stabilność**: automatyczne czekanie na elementy,
- **time travel**: podgląd stanu aplikacji w każdym kroku testu,
- **integracja z CI/CD**, zrzuty i nagrania przy niepowodzeniu.

| Typ testu | Opis |
|---|---|
| **End-to-end** | sprawdza całą ścieżkę: od interakcji użytkownika, przez logikę biznesową, po dane |
| **Komponentowe / integracyjne** | testuje pojedyncze komponenty w izolacji i w połączeniu z innymi |

## Instalacja i uruchomienie

```bash
npm init -y
npm install cypress --save-dev
npx cypress open        # tryb interaktywny
npx cypress run         # tryb headless (CI)
```

## Przykładowy test

```javascript title="cypress/e2e/login.cy.js"
describe("Logowanie", () => {
  beforeEach(() => {
    cy.visit("/login");
  });

  it("loguje użytkownika poprawnymi danymi", () => {
    cy.get("[data-cy=email]").type("jan@test.pl");
    cy.get("[data-cy=password]").type("Haslo123!");
    cy.get("[data-cy=submit]").click();

    cy.url().should("include", "/dashboard");
    cy.contains("h1", "Witaj").should("be.visible");
  });

  it("pokazuje błąd przy złym haśle", () => {
    cy.intercept("POST", "/api/login").as("login");
    cy.get("[data-cy=email]").type("jan@test.pl");
    cy.get("[data-cy=password]").type("zle");
    cy.get("[data-cy=submit]").click();

    cy.wait("@login").its("response.statusCode").should("eq", 401);
    cy.get(".error").should("contain", "Nieprawidłowe dane");
  });
});
```

## Konfiguracja globalna

```javascript title="cypress.config.js"
const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "https://staging.example.com",
    viewportWidth: 1366,
    viewportHeight: 768,
    defaultCommandTimeout: 8000,
    video: false,
  },
});
```

## Przydatne rozszerzenia VS Code

- **JavaScript (ES6) code snippets**
- **Cypress Snippets**
- **vscode-icons**

!!! tip "Cypress a Selenium"
    Cypress jest szybszy w konfiguracji i debugowaniu, ale działa tylko z JS/TS i ma ograniczenia (np. wiele kart przeglądarki). Selenium obsługuje wiele języków i przeglądarek. Współczesną alternatywą dla obu jest **[Playwright](playwright.md)**.
