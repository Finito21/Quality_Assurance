---
description: "Postman for testers: collections, variables and environments, pm.* test scripts and running tests in CI."
---

# Postman

**Postman** is a tool for testing and debugging APIs. It lets you send HTTP requests and analyse responses in a convenient graphical interface.

## Features

<div class="grid cards" markdown>

-   **HTTP requests**: all methods, headers, body, authorisation
-   **Collections**: grouping and organising requests
-   **Automated tests**: assertions in JavaScript
-   **Environments and variables**: test / staging / prod
-   **Runner**: running whole collections
-   **Mock Servers**: a fake backend
-   **Monitors**: scheduled runs and statistics
-   **API documentation**: generated from collections

</div>

## Basic concepts

| Concept | Example / description |
|---|---|
| **Base URL** | `https://api.example.com` |
| **Endpoint** | `/users`, `/products/1` |
| **Query params** | `/users?status=active&role=admin` (start with `?`, joined with `&`, used for filtering) |
| **Path param / ID** | `/products/1`, i.e. a specific object |
| **Body** | the *Body → raw → JSON* tab |

### JSON in a nutshell

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 3999.99,
  "available": true,
  "tags": ["electronics", "computers"],
  "producer": { "name": "ACME", "country": "PL" }
}
```

`{ }` is an object, `[ ]` is an array, strings go in `" "`, numbers and booleans go without quotes, objects can be nested.

## Authorisation

- **Bearer Token**: a token sent in the `Authorization: Bearer <token>` header. You can get it from a developer or fetch it with a login request and store it in a variable.
- **Basic Auth**: username and password encoded in **Base64** (that is encoding, not encryption, so use it only over HTTPS).
- **API Key**, **OAuth 2.0**: see [Authentication and authorisation](../../technologies/api_testing/authentication.md).

## Variables

Syntax: `{{variableName}}`

| Scope | Description | Priority |
|---|---|---|
| **Local** | only for one request / run | highest |
| **Data** | from a CSV/JSON file in the Runner | |
| **Environment** | depend on the environment (test, prod) | |
| **Collection** | only for a given collection | |
| **Global** | available everywhere | lowest |

```javascript
pm.environment.set("token", pm.response.json().accessToken);
pm.collectionVariables.get("userId");
```

## Tests

Tests are written in JavaScript (the **Scripts → Post-response** tab). You can check the status code, response time, the structure and content of the body, the number of objects, and store data in variables.

Examples and good practices: **[API test automation](../../technologies/api_testing/api_automation.md)**.

## Your first test step by step

An exercise on a free public API for learning, **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)**. It returns sample data and does not save changes, so you cannot break anything.

1. **Environment**: *Environments → +*, name `JSONPlaceholder`, variable `baseUrl` = `https://jsonplaceholder.typicode.com`. Select the environment in the top right corner.
2. **Collection**: *Collections → +*, name `API exercises`.
3. **Request**: in the collection, *Add request*, method `GET`, URL `{{baseUrl}}/users/1`, click **Send**. The response has the status `200 OK` and one user's data in JSON.
4. **Tests**: in the *Scripts → Post-response* tab, paste:

    ```javascript
    pm.test("Status code is 200", () => {
      pm.response.to.have.status(200);
    });

    pm.test("Response in under 1 s", () => {
      pm.expect(pm.response.responseTime).to.be.below(1000);
    });

    pm.test("User has id 1 and a valid e-mail", () => {
      const user = pm.response.json();
      pm.expect(user.id).to.eql(1);
      pm.expect(user.email).to.match(/^\S+@\S+\.\S+$/);
    });

    // store data for use in the next request
    pm.collectionVariables.set("userId", pm.response.json().id);
    ```

5. Click **Send** again and open the *Test Results* tab: all tests should be green.
6. **Second request**: `GET {{baseUrl}}/posts?userId={{userId}}` with a test that every post belongs to that user:

    ```javascript
    pm.test("All posts belong to the user", () => {
      const userId = Number(pm.collectionVariables.get("userId"));
      pm.response.json().forEach((post) => pm.expect(post.userId).to.eql(userId));
    });
    ```

7. **Negative test**: `GET {{baseUrl}}/users/9999` should return `404`. Add a test for that code.
8. **Runner**: click the collection → *Run* and run all requests at once.

!!! tip "Next steps"
    Add a `POST {{baseUrl}}/posts` request with a JSON body and check that the response has the status `201` and contains the fields you sent. Then run the collection from the command line with Newman.

## Collection Runner

Runs whole collections or folders with tests. It lets you:

- set the **number of iterations** and **delays** between requests,
- choose the **environment**,
- provide a data file (**data-driven testing**),
- schedule runs or run them manually.

In CI, collections are run with the **Postman CLI** (recommended by Postman) or the older **Newman**.

## Examples and Mock Servers

**Examples** are saved sample request + response pairs. They show others how to build a correct body.

A **Mock Server** is a fake API server that returns predefined responses (based on Examples). It is useful when:

- the backend does not exist yet,
- the API is unstable or unavailable,
- you are testing the frontend or an integration,
- you want to practise without the risk of changing real data.

## Monitors

Scheduled runs of a collection in the Postman cloud with statistics: number of tests, errors, response time.

## Postman and Git

Collections can be kept in a repository (JSON export or Postman's native Git integration). A file in the `.postman/` directory links the local repo with a **workspace in the Postman cloud**. When working only locally, make sure the repo does not keep references to collections and environments that no longer exist.
