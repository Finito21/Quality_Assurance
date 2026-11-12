---
description: "Selenium WebDriver: setup, locators, waits, the Page Object pattern and a sample test in Python."
---

# Selenium

**Selenium** is an open-source set of tools for **automating tests of web applications**. It simulates user behaviour in the browser: clicking, typing text, checking results.

## Components

| Component | Description |
|---|---|
| **WebDriver** | API for controlling browsers (Chrome, Firefox, Edge, Safari) |
| **IDE** | browser extension for recording simple tests without programming |
| **Grid** | running tests in parallel on many browsers and machines |

Supported languages: Java, Python, C#, JavaScript, Ruby, Kotlin.

## Sample test (Python + pytest)

```python
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()  # Selenium Manager downloads a matching driver
    try:
        driver.get("https://example.com/login")
        driver.find_element(By.ID, "username").send_keys(os.environ["TEST_USER"])
        driver.find_element(By.ID, "password").send_keys(os.environ["TEST_PASSWORD"])
        driver.find_element(By.ID, "login").click()

        greeting = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.welcome"))
        )
        assert "Welcome" in greeting.text
    finally:
        driver.quit()
```

The credentials come from environment variables, not from the code. In CI they are set as secrets, e.g. in [GitHub Actions](../ci_cd/github_actions.md). Since version 4.6, **Selenium Manager** downloads the browser driver automatically, so there is no need to install `chromedriver` by hand.

## Locators

| Strategy | Example | Notes |
|---|---|---|
| `By.ID` | `"login"` | fastest and most stable |
| `By.CSS_SELECTOR` | `"[data-testid='submit']"` | recommended |
| `By.XPATH` | `"//button[text()='Log in']"` | flexible but brittle |
| `By.NAME`, `By.CLASS_NAME`, `By.LINK_TEXT` | | useful as a fallback |

!!! warning "Avoid `time.sleep()`"
    Use **explicit waits** (`WebDriverWait` + `expected_conditions`) to keep tests fast and stable.

## Good practices

- the **Page Object Model** pattern: page locators and actions in separate classes,
- stable locators (`data-testid`) instead of long XPaths,
- tests independent of each other, each one prepares its own data,
- running in CI (Jenkins / GitHub Actions), preferably in **headless** mode.

## Use cases

- automating **regression tests**,
- verifying critical business paths (login, registration, ordering),
- cross-browser tests with Selenium Grid or BrowserStack.
