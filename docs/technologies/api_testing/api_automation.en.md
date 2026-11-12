---
description: "API test automation: Postman assertions, chained requests, test data, schema validation and running collections in CI with Newman."
---

# API test automation

**API test automation** means running API tests with tools and scripts, without manual intervention. Tests can run automatically, e.g. in a CI/CD pipeline, to continuously verify that the API works and to catch bugs faster.

## What to verify?

- [x] **status code** (e.g. `200`, `201`, `400`, `404`),
- [x] **response time**,
- [x] **headers**, e.g. `Content-Type`,
- [x] **body structure**, i.e. compliance with the **schema** (JSON Schema),
- [x] **body content**: specific values, number of objects,
- [x] **negative paths**: invalid data, missing authorisation, non-existent resources.

## Tests in Postman

Tests are written in JavaScript in the **Scripts → Post-response** tab (formerly *Tests*), using the `pm` object.

```javascript
pm.test("Status 200", () => {
  pm.response.to.have.status(200);
});

pm.test("Response time < 500 ms", () => {
  pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("A list of users was returned", () => {
  const body = pm.response.json();
  pm.expect(body).to.be.an("array").that.is.not.empty;
  pm.expect(body[0]).to.have.property("email");
  // store a value in a variable for the next requests
  pm.collectionVariables.set("userId", body[0].id);
});
```

### Example: validating an error response (RFC 9457 *Problem Details*)

Requirements:

- `Content-Type` is `application/problem+json` (not `application/json` or `text/html`),
- the `x-correlation-id` header is present (traceability / tracing),
- `correlationId` in the body is **identical** to the header value,
- the `detail` message matches the specification.

RFC 9457 makes all members optional (`type` defaults to `about:blank`), so the required fields below are the project's API contract, and `correlationId` is an extension member.

```javascript
const body = pm.response.json();

pm.test("Status 400", () => pm.response.to.have.status(400));

pm.test("Content-Type = application/problem+json", () => {
  pm.expect(pm.response.headers.get("Content-Type"))
    .to.include("application/problem+json");
});

pm.test("x-correlation-id header exists and matches the body", () => {
  const header = pm.response.headers.get("x-correlation-id");
  pm.expect(header).to.be.a("string").and.not.empty;
  pm.expect(body.correlationId).to.eql(header);
});

pm.test("Matches the Problem Details schema", () => {
  const schema = {
    type: "object",
    required: ["type", "title", "status", "detail"],
    properties: {
      type:   { type: "string" },
      title:  { type: "string" },
      status: { type: "integer" },
      detail: { type: "string" }
    }
  };
  pm.response.to.have.jsonSchema(schema);
});
```

## Good practices

!!! tip "From experience"
    - **Tests at collection or folder level** instead of copying the same assertions into every request.
    - **Snippets** in Postman speed up writing typical assertions.
    - **Break a test on purpose** (e.g. expect `201` instead of `200`) and check that it really fails. A test that never fails checks nothing.
    - Design tests **based on the API specification** (OpenAPI/Swagger), not only on the current behaviour.
    - Very large collections can be unwieldy in Postman. Clear request names and folders help.
    - Be careful with **Postman Agent Mode** (AI) and sensitive data. Check what data goes to the cloud.

## Running in CI/CD: Newman

**Newman** is a CLI for Postman collections that lets you run tests in Jenkins or GitHub Actions.

```bash
npm install -g newman newman-reporter-htmlextra
newman run collection.json -e qa_environment.json -r cli,htmlextra
```

## Other API automation tools

| Tool | Language | Characteristics |
|---|---|---|
| **Postman + Newman** | JS | GUI + CLI, easiest to start with |
| **SuperTest** | JS/TS | API tests in code, often with Jest/Mocha |
| **REST Assured** | Java | the standard in Java projects |
| **requests + pytest** | Python | simple and flexible combo |
| **Playwright (APIRequestContext)** | JS/TS/Python | API + UI in one framework |
| **SoapUI / ReadyAPI** | GUI / Groovy | REST and SOAP, functional and load tests |
