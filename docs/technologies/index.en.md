---
description: "Technologies a tester should know: frontend, SQL, APIs, HTTP, authentication, Docker and Kubernetes."
---

# Technologies

Technologies a tester works with every day. You do not have to be a developer, but you need to understand how the system under test works to know where to look for defects and how to describe them.

| Area | Pages | Why a tester needs it |
|---|---|---|
| **Frontend** | [HTML](frontend/html.md), [CSS](frontend/css.md), [JavaScript](frontend/javascript.md) | reading the page structure in DevTools, locators in automation, errors in the console |
| **Backend** | [SQL](backend/sql.md) | checking that data was saved in the database, preparing test data |
| **API** | [API fundamentals](api_testing/api_fundamentals.md), [HTTP](api_testing/http.md), [Authentication](api_testing/authentication.md), [Automation](api_testing/api_automation.md) | testing logic without the UI, faster and more stable than UI tests |
| **DevOps** | [Docker](devops/docker.md), [Kubernetes](devops/kubernetes.md) | running test environments, reading logs, diagnosing failures |

!!! tip "Where to start"
    If you are just starting, read **HTML** and **HTTP** first, then **API fundamentals** and **SQL**. Docker and Kubernetes will help once you work in a team with its own environments.
