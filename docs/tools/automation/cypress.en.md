---
description: "Cypress for testers: installation, test structure, selectors and commands, a login test example, network stubbing and running tests in CI."
---

# Cypress

**Cypress** is a tool for testing the frontend of web applications. It lets you write, run and debug **end-to-end**, **component** and integration tests. Tests are written in JavaScript / TypeScript.

## Why Cypress?

- **easy start**: installed via npm, ready-made project structure,
- **full control**: runs in the same loop as the application, has access to the DOM and the network,
- **speed and stability**: automatically waits for elements,
- **time travel**: shows the application state at every step of the test,
- **CI/CD integration**, screenshots and recordings on failure.

| Test type | Description |
|---|---|
| **End-to-end** | checks the whole path: from user interaction, through business logic, to data |
| **Component / integration** | tests individual components in isolation and together with others |

## Installation and running

```bash
npm init -y
npm install cypress --save-dev
npx cypress open        # interactive mode
npx cypress run         # headless mode (CI)
```

## Sample test

```javascript title="cypress/e2e/login.cy.js"
describe("Login", () => {
  beforeEach(() => {
    cy.visit("/login");
  });

  it("logs the user in with valid credentials", () => {
    cy.get("[data-cy=email]").type("jan@test.pl");
    cy.get("[data-cy=password]").type(Cypress.env("TEST_PASSWORD"), { log: false }); // password from CYPRESS_TEST_PASSWORD
    cy.get("[data-cy=submit]").click();

    cy.url().should("include", "/dashboard");
    cy.contains("h1", "Welcome").should("be.visible");
  });

  it("shows an error for a wrong password", () => {
    cy.intercept("POST", "/api/login").as("login");
    cy.get("[data-cy=email]").type("jan@test.pl");
    cy.get("[data-cy=password]").type("wrong");
    cy.get("[data-cy=submit]").click();

    cy.wait("@login").its("response.statusCode").should("eq", 401);
    cy.get(".error").should("contain", "Invalid credentials");
  });
});
```

## Global configuration

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

## Useful VS Code extensions

- **JavaScript (ES6) code snippets**
- **Cypress Snippets**
- **vscode-icons**

!!! tip "Cypress vs Selenium"
    Cypress is quicker to set up and debug, but works only with JS/TS and has limitations (e.g. multiple browser tabs). Selenium supports many languages and browsers. A modern alternative to both is **[Playwright](playwright.md)**.
