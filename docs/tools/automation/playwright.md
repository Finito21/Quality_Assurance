---
description: "Playwright dla testera: instalacja, lokatory, automatyczne oczekiwanie, przykładowe testy, trace viewer i porównanie z Cypressem i Selenium."
---

# Playwright

**Playwright** (Microsoft, open source) to narzędzie do automatyzacji testów aplikacji webowych **end-to-end**. Jednym API steruje przeglądarkami opartymi na **Chromium** (Chrome, Edge), **Firefox** i **WebKit** (silnik Safari). Testy można pisać w TypeScripcie lub JavaScripcie, Pythonie, Javie i C#.

## Dlaczego Playwright?

- **automatyczne czekanie**: przed kliknięciem lub wpisaniem tekstu czeka, aż element będzie widoczny, aktywny i stabilny, więc nie potrzeba `sleep`,
- **wiele przeglądarek i urządzeń** z jednej konfiguracji, także emulacja telefonów,
- **izolacja testów**: każdy test dostaje świeży kontekst przeglądarki (osobne ciasteczka i storage),
- **wiele kart, okien i domen** w jednym teście,
- **trace viewer**: nagranie przebiegu testu z DOM, zrzutami, siecią i konsolą w każdym kroku,
- **codegen**: nagrywanie akcji w przeglądarce i generowanie z nich kodu testu,
- **testy API** (`request`) w tym samym narzędziu, np. do przygotowania danych.

## Instalacja i uruchomienie

```bash
npm init playwright@latest      # projekt, konfiguracja i przeglądarki
npx playwright test             # wszystkie testy, domyślnie headless
npx playwright test --ui        # tryb interaktywny
npx playwright codegen https://example.com
npx playwright show-report      # raport HTML
```

## Przykładowy test

```typescript title="tests/logowanie.spec.ts"
import { test, expect } from "@playwright/test";

test.describe("Logowanie", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/login");
  });

  test("loguje użytkownika poprawnymi danymi", async ({ page }) => {
    await page.getByLabel("E-mail").fill(process.env.TEST_USER!);
    await page.getByLabel("Hasło").fill(process.env.TEST_PASSWORD!);
    await page.getByRole("button", { name: "Zaloguj" }).click();

    await expect(page).toHaveURL(/\/dashboard/);
    await expect(page.getByRole("heading", { name: /Witaj/ })).toBeVisible();
  });

  test("pokazuje błąd przy złym haśle", async ({ page }) => {
    await page.getByLabel("E-mail").fill("jan@test.pl");
    await page.getByLabel("Hasło").fill("zle-haslo");
    await page.getByRole("button", { name: "Zaloguj" }).click();

    await expect(page.getByRole("alert")).toHaveText("Nieprawidłowy e-mail lub hasło");
  });
});
```

## Lokatory

Playwright zaleca lokatory oparte na tym, co widzi użytkownik, a nie na strukturze DOM.

| Lokator | Przykład | Kiedy |
|---|---|---|
| `getByRole` | `getByRole("button", { name: "Zapisz" })` | pierwszy wybór: przyciski, linki, nagłówki, pola |
| `getByLabel` | `getByLabel("E-mail")` | pola formularza z etykietą |
| `getByText` | `getByText("Koszyk jest pusty")` | elementy bez roli, komunikaty |
| `getByTestId` | `getByTestId("cart-total")` | gdy nie ma innego stabilnego sposobu (`data-testid`) |
| `locator` | `locator("css=.price")` | CSS lub XPath, w ostateczności |

!!! tip "Lokatory a dostępność"
    Jeśli przycisku nie da się znaleźć przez `getByRole` z nazwą, to często również czytnik ekranu go nie ogłosi poprawnie. To dobry sygnał do zgłoszenia [problemu z dostępnością](../../fundamentals/non_functional_testing.md#testy-dostepnosci).

## Konfiguracja

```typescript title="playwright.config.ts"
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  retries: process.env.CI ? 1 : 0,
  use: {
    baseURL: "https://staging.example.com",
    trace: "on-first-retry",        // nagranie przy ponownej próbie
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "mobile", use: { ...devices["Pixel 7"] } },
  ],
});
```

## Playwright, Cypress i Selenium

| | Playwright | [Cypress](cypress.md) | [Selenium](selenium.md) |
|---|---|---|---|
| **Języki** | TS/JS, Python, Java, C# | JS/TS | Java, Python, C#, JS, Ruby, Kotlin |
| **Przeglądarki** | Chromium, Firefox, WebKit | Chromium, Firefox, WebKit (eksperymentalnie) | wszystkie główne, także prawdziwe Safari |
| **Czekanie** | automatyczne | automatyczne | jawne oczekiwania w kodzie |
| **Wiele kart i domen** | tak | ograniczone | tak |
| **Równoległość** | wbudowana | płatna usługa lub własna konfiguracja | Selenium Grid |
| **Debugowanie** | trace viewer, tryb UI | time travel w przeglądarce | logi, zrzuty, zewnętrzne narzędzia |

Wszystkie trzy dobrze działają w [CI/CD](../ci_cd/github_actions.md). Wybór zależy od języka zespołu, wymaganych przeglądarek i istniejących testów.
