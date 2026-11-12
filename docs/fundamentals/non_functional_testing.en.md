---
description: "Non-functional testing based on ISO/IEC 25010: performance, security, usability, accessibility, compatibility and reliability."
---

# Non-functional testing

Functional tests check **what** the system does. Non-functional tests check **how well** it does it: whether it is fast, secure, accessible, convenient and resilient to failures. The CTFL v4.0 syllabus describes these characteristics based on the **ISO/IEC 25010** quality model.

## Quality characteristics (ISO/IEC 25010)

| Characteristic | Tester's question | Example tests |
|---|---|---|
| **Performance efficiency** | Does the system respond quickly and handle the load? | [performance testing](performance_testing.md), load, stress |
| **Compatibility** | Does it work in different browsers and with other systems? | cross-browser tests, integration tests |
| **Interaction capability** | Is it easy to learn, convenient and accessible? | usability tests, accessibility tests |
| **Reliability** | Does it run stably and recover from failures? | recovery tests, failover tests |
| **Security** | Does it protect data and resist attacks? | security tests, penetration tests |
| **Maintainability** | Is it easy to change and test? | static analysis, code reviews |
| **Flexibility (portability)** | Can it be installed and moved to another environment? | installation tests, migration tests |
| **Safety** | Does it endanger people or the environment? | testing of critical systems, e.g. medical |

The names come from the 2023 edition of the standard. The CTFL v4.0 syllabus is based on the 2011 edition, which has **usability** instead of interaction capability and **portability** instead of flexibility, and no safety characteristic. The functional characteristic is **functional suitability**, checked with functional tests.

!!! note "When to test"
    Non-functional tests are not “for the end of the project”. Performance, security and accessibility requirements are worth agreeing at the start and checking at every test level, also automatically in CI.

## Security testing

A tester does not have to be a penetration tester, but should know the typical vulnerabilities and check them in everyday tests. The starting points are the **OWASP Top 10** (web applications) and the **OWASP API Security Top 10**.

| What to check | Example test |
|---|---|
| **Access control** | after changing the `id` in the URL (`/orders/123` → `/orders/124`), can you see someone else's order |
| **Authentication** | lockout after many wrong passwords, session expiry, logging out invalidates the token |
| **Input validation** | special characters `' " < >` in form fields do not break the page or database queries |
| **Information disclosure** | error messages do not show a stack trace, server version or SQL queries |
| **Sensitive data** | passwords and tokens do not end up in logs, URLs or API responses |
| **Configuration** | HTTPS everywhere, security headers (`Content-Security-Policy`, `Strict-Transport-Security`) |

Details for APIs: [Authentication and authorisation](../technologies/api_testing/authentication.md), [HTTP](../technologies/api_testing/http.md).

!!! warning "Only with permission"
    Security tests are run only on systems you have written authorisation to test, preferably on a test environment. Scanning or attacking other people's systems is illegal.

Tools: **OWASP ZAP** and **Burp Suite** (intercepting and modifying traffic, scanning), dependency scanners such as **Dependabot** or **Snyk**.

## Accessibility testing

Accessibility (a11y) means that people with disabilities can also use the application: blind, low-vision, deaf, or with motor impairments. The standard is **WCAG 2.2**, usually at level **AA**. In the European Union, many digital services must meet it under the European Accessibility Act (EAA).

| What to check | How |
|---|---|
| **Keyboard use** | going through the whole page with ++tab++, a visible focus, no keyboard traps |
| **Text alternatives** | images that carry content have an `alt` description, decorative ones have `alt=""` |
| **Contrast** | text has a contrast of at least 4.5:1 with the background (large text 3:1) |
| **Forms** | every field has a label, errors are described in text, not only by colour |
| **Structure** | headings in a logical order, a correct `lang` attribute on the page |
| **Screen reader** | going through a key journey with NVDA (Windows) or VoiceOver (macOS, iOS) |
| **Zoom** | the page works at 200% zoom and on a narrow screen |

Tools: **axe DevTools**, **Lighthouse** in [DevTools](../tools/devtools.md), **WAVE**. Automated tools find only some of the problems, so always add a manual test.

## Usability testing

Usability tests check whether users can complete their tasks **effectively, efficiently and with satisfaction**.

- **Tests with users**: a few people from the target group perform tasks (e.g. “buy a ticket for tomorrow”), and an observer notes where they get lost. As few as 5 participants reveal most serious problems.
- **Heuristic evaluation**: an expert checks the interface against principles, e.g. Nielsen's 10 heuristics (visibility of system status, error prevention, consistency).
- **Questionnaires**: e.g. the SUS questionnaire after the tasks.

## Compatibility and reliability testing

- **Cross-browser and devices**: the matrix of browsers, systems and resolutions is based on user data. [BrowserStack and similar services](../tools/browser_tools.md) help.
- **Recovery after failure**: what happens after a server restart, a lost database connection, a network drop during payment.
- **Installation and update tests**: a clean installation, an update from the previous version, uninstalling.
