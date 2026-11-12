---
description: "Selenium WebDriver dla testera: konfiguracja z Selenium Manager, lokatory, jawne oczekiwania, wzorzec Page Object i przykładowy test w Pythonie."
---

# Selenium

**Selenium** to zestaw narzędzi open source do **automatyzacji testów aplikacji webowych**. Symuluje zachowanie użytkownika w przeglądarce: klikanie, wpisywanie tekstu, sprawdzanie wyników.

## Komponenty

| Komponent | Opis |
|---|---|
| **WebDriver** | API do sterowania przeglądarkami (Chrome, Firefox, Edge, Safari) |
| **IDE** | wtyczka do nagrywania prostych testów bez programowania |
| **Grid** | równoległe uruchamianie testów na wielu przeglądarkach i maszynach |

Obsługiwane języki: Java, Python, C#, JavaScript, Ruby, Kotlin.

## Przykładowy test (Python + pytest)

```python
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logowanie():
    driver = webdriver.Chrome()  # Selenium Manager sam pobiera pasujący sterownik
    try:
        driver.get("https://example.com/login")
        driver.find_element(By.ID, "username").send_keys(os.environ["TEST_USER"])
        driver.find_element(By.ID, "password").send_keys(os.environ["TEST_PASSWORD"])
        driver.find_element(By.ID, "login").click()

        powitanie = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.welcome"))
        )
        assert "Witaj" in powitanie.text
    finally:
        driver.quit()
```

Dane logowania pochodzą ze zmiennych środowiskowych, a nie z kodu. W CI ustawia się je jako sekrety, np. w [GitHub Actions](../ci_cd/github_actions.md). Od wersji 4.6 **Selenium Manager** automatycznie pobiera sterownik przeglądarki, więc nie trzeba instalować `chromedriver` ręcznie.

## Lokatory

| Strategia | Przykład | Uwagi |
|---|---|---|
| `By.ID` | `"login"` | najszybszy i najstabilniejszy |
| `By.CSS_SELECTOR` | `"[data-testid='submit']"` | zalecany |
| `By.XPATH` | `"//button[text()='Zaloguj']"` | elastyczny, ale kruchy |
| `By.NAME`, `By.CLASS_NAME`, `By.LINK_TEXT` | | przydatne pomocniczo |

!!! warning "Unikaj `time.sleep()`"
    Stosuj **jawne oczekiwania** (`WebDriverWait` + `expected_conditions`), aby testy były szybkie i stabilne.

## Dobre praktyki

- wzorzec **Page Object Model**: lokatory i akcje strony w osobnych klasach,
- stabilne lokatory (`data-testid`) zamiast długich XPath,
- testy niezależne od siebie, każdy przygotowuje własne dane,
- uruchamianie w CI (Jenkins / GitHub Actions), najlepiej w trybie **headless**.

## Zastosowanie

- automatyzacja **testów regresji**,
- weryfikacja krytycznych ścieżek biznesowych (logowanie, rejestracja, zamówienie),
- testy cross-browser z Selenium Grid lub BrowserStack.
