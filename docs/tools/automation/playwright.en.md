---
description: "Playwright for testers: installation, locators, auto-waiting, sample tests, the trace viewer and a comparison with Cypress and Selenium."
---

# Playwright

**Playwright** (Microsoft, open source) is a tool for automating **end-to-end** tests of web applications. One API drives browsers based on **Chromium** (Chrome, Edge), **Firefox** and **WebKit** (the Safari engine). Tests can be written in TypeScript or JavaScript, Python, Java and C#.

## Why Playwright?

- **auto-waiting**: before clicking or typing it waits until the element is visible, enabled and stable, so no `sleep` is needed,
- **many browsers and devices** from one configuration, including phone emulation,
- **test isolation**: every test gets a fresh browser context (separate cookies and storage),
- **many tabs, windows and domains** in one test,
- **trace viewer**: a recording of the test run with the DOM, screenshots, network and console at every step,
- **codegen**: recording actions in the browser and generating test code from them,
- **API tests** (`request`) in the same tool, e.g. to prepare data.

## Installation and running

```bash
npm init playwright@latest      # project, configuration and browsers
npx playwright test             # all tests, headless by default
npx playwright test --ui        # interactive mode
npx playwright codegen https://example.com
npx playwright show-report      # HTML report
```

## Sample test

```typescript title="tests/login.spec.ts"
import { test, expect } from "@playwright/test";

test.describe("Login", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/login");
  });

  test("logs the user in with valid credentials", async ({ page }) => {
    await page.getByLabel("E-mail").fill(process.env.TEST_USER!);
    await page.getByLabel("Password").fill(process.env.TEST_PASSWORD!);
    await page.getByRole("button", { name: "Log in" }).click();

    await expect(page).toHaveURL(/\/dashboard/);
    await expect(page.getByRole("heading", { name: /Welcome/ })).toBeVisible();
  });

  test("shows an error for a wrong password", async ({ page }) => {
    await page.getByLabel("E-mail").fill("jan@test.pl");
    await page.getByLabel("Password").fill("wrong-password");
    await page.getByRole("button", { name: "Log in" }).click();

    await expect(page.getByRole("alert")).toHaveText("Invalid e-mail or password");
  });
});
```

## Locators

Playwright recommends locators based on what the user sees, not on the DOM structure.

| Locator | Example | When |
|---|---|---|
| `getByRole` | `getByRole("button", { name: "Save" })` | first choice: buttons, links, headings, fields |
| `getByLabel` | `getByLabel("E-mail")` | form fields with a label |
| `getByText` | `getByText("Your cart is empty")` | elements without a role, messages |
| `getByTestId` | `getByTestId("cart-total")` | when there is no other stable way (`data-testid`) |
| `locator` | `locator("css=.price")` | CSS or XPath, as a last resort |

!!! tip "Locators and accessibility"
    If a button cannot be found with `getByRole` and its name, a screen reader often cannot announce it correctly either. That is a good reason to report an [accessibility problem](../../fundamentals/non_functional_testing.md#accessibility-testing).

## Configuration

```typescript title="playwright.config.ts"
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  retries: process.env.CI ? 1 : 0,
  use: {
    baseURL: "https://staging.example.com",
    trace: "on-first-retry",        // recording on the retry
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "mobile", use: { ...devices["Pixel 7"] } },
  ],
});
```

## Playwright, Cypress and Selenium

| | Playwright | [Cypress](cypress.md) | [Selenium](selenium.md) |
|---|---|---|---|
| **Languages** | TS/JS, Python, Java, C# | JS/TS | Java, Python, C#, JS, Ruby, Kotlin |
| **Browsers** | Chromium, Firefox, WebKit | Chromium, Firefox, WebKit (experimental) | all major ones, including real Safari |
| **Waiting** | automatic | automatic | explicit waits in code |
| **Many tabs and domains** | yes | limited | yes |
| **Parallel runs** | built in | paid service or own setup | Selenium Grid |
| **Debugging** | trace viewer, UI mode | time travel in the browser | logs, screenshots, external tools |

All three work well in [CI/CD](../ci_cd/github_actions.md). The choice depends on the team's language, the required browsers and the existing tests.
