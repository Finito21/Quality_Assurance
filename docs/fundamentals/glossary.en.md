---
description: "Glossary of testing terms in Polish and English, aligned with ISTQB terminology: defect, failure, test case and more."
---

# Glossary

The most common testing terms, with the Polish equivalent used on the Polish version of this site and in Polish job ads. The full, official glossary is the [ISTQB Glossary](https://glossary.istqb.org/) (also available in Polish).

## Basics

| Term | In Polish | Meaning |
|---|---|---|
| **Failure** | <span lang="pl">awaria</span> | a visible effect of a defect: the system does not do what it should |
| **Error (mistake)** | <span lang="pl">błąd, pomyłka</span> | a human mistake that leads to a defect |
| **Defect (bug)** | <span lang="pl">defekt</span> | a flaw in the code or another work product |
| **Test object** | <span lang="pl">przedmiot testów</span> | what is being tested: a component, a system, a document |
| **Test basis** | <span lang="pl">podstawa testów</span> | everything tests are derived from: requirements, user stories, design |
| **Test oracle** | <span lang="pl">wyrocznia testowa</span> | the source of the expected result, e.g. the specification |
| **Test condition** | <span lang="pl">warunek testowy</span> | an aspect to check, e.g. “logging in with a locked account” |
| **Test case** | <span lang="pl">przypadek testowy</span> | preconditions, data, steps and the expected result of one test |
| **Testware** | <span lang="pl">testalia</span> | all products of testing: plans, cases, scripts, data, reports |
| **Verification** | <span lang="pl">weryfikacja</span> | checking compliance with the specification |
| **Validation** | <span lang="pl">walidacja</span> | checking whether the product meets the user's needs |

## Types of testing

| Term | In Polish | Meaning |
|---|---|---|
| **Confirmation testing (retest)** | <span lang="pl">test potwierdzający</span> | checking that a fixed defect is really gone |
| **Regression testing** | <span lang="pl">test regresji</span> | checking that a change has not broken working features |
| **Smoke test** | <span lang="pl">smoke test</span> | a quick check that a build is fit for further testing |
| **Static testing** | <span lang="pl">testowanie statyczne</span> | evaluation without running the code, e.g. a requirements review |
| **Dynamic testing** | <span lang="pl">testowanie dynamiczne</span> | tests with the software running |
| **Exploratory testing** | <span lang="pl">testowanie eksploracyjne</span> | learning, designing and running tests at the same time |
| **Maintenance testing** | <span lang="pl">testowanie pielęgnacyjne</span> | testing a system already in use, after changes or a migration |
| **End-to-end (E2E) testing** | <span lang="pl">testy end-to-end</span> | checking a complete user journey through all layers of the system |

## Process and management

| Term | In Polish | Meaning |
|---|---|---|
| **Test plan** | <span lang="pl">plan testów</span> | objectives, scope, approach, resources and schedule of testing |
| **Entry / exit criteria** | <span lang="pl">kryteria wejścia / wyjścia</span> | conditions for starting and finishing a test activity |
| **Coverage** | <span lang="pl">pokrycie</span> | which share of items (requirements, code) the tests have exercised |
| **Product risk** | <span lang="pl">ryzyko produktowe</span> | the risk that the product does not meet needs, e.g. wrong calculations |
| **Project risk** | <span lang="pl">ryzyko projektowe</span> | a risk to the project, e.g. delays, lack of people |
| **Severity** | <span lang="pl">ważność</span> | how serious the impact of a defect is |
| **Priority** | <span lang="pl">priorytet</span> | how urgently a defect needs to be fixed |
| **Traceability matrix** | <span lang="pl">macierz śledzenia</span> | links between requirements, tests and defects |
| **Test completion report** | <span lang="pl">raport z ukończenia testów</span> | a summary of testing after a test level or project ends |
| **Definition of Done (DoD)** | <span lang="pl">Definition of Done</span> | criteria a user story must meet to be considered done |

## Environment and automation

| Term | In Polish | Meaning |
|---|---|---|
| **Test environment** | <span lang="pl">środowisko testowe</span> | hardware, software and data that tests run on |
| **Build** | <span lang="pl">build</span> | a specific, built version of the application |
| **Mock, stub** | <span lang="pl">atrapa, zaślepka</span> | a stand-in for a real component or service in a test |
| **Flaky test** | <span lang="pl">niestabilny test</span> | a test that sometimes passes and sometimes fails without code changes |
| **Locator** | <span lang="pl">lokator</span> | a way to point to a page element in an automated test |
| **Pipeline** | <span lang="pl">potok CI/CD</span> | an automated sequence of steps: build, tests, deployment |
| **Headless mode** | <span lang="pl">tryb headless</span> | running a browser without a window, e.g. in CI |
