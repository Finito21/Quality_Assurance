---
description: "HTTP for testers: methods, idempotency, status codes, headers and typical defects found at the protocol level."
---

# HTTP: methods, codes, headers

**HTTP (HyperText Transfer Protocol)** is the protocol a client (browser, mobile app, Postman) uses to talk to a server in the request → response model. The structure of a request and a response is described in [API fundamentals](api_fundamentals.md#how-does-an-api-work).

HTTP is **stateless**: every request is handled independently of the previous ones. To recognise a user across requests, cookies, a session ID or tokens are used ([Authentication and authorisation](authentication.md)).

```http
POST /api/orders HTTP/1.1
Host: shop.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{"productId": 15, "quantity": 2}
```

## HTTP methods

| Method | Use | Body | Safe | Idempotent |
|---|---|---|---|---|
| `GET` | read a resource | no | yes | yes |
| `POST` | create a resource or run an operation (login, payment) | yes | no | no |
| `PUT` | replace the whole resource | yes | no | yes |
| `PATCH` | partially change a resource | yes | no | depends on implementation |
| `DELETE` | delete a resource | usually no | no | yes |
| `HEAD` | like `GET`, but headers only | no | yes | yes |
| `OPTIONS` | allowed methods, CORS preflight request | no | yes | yes |

**Safe**
:   Does not change server state.

**Idempotent**
:   Sending the same request many times leaves the server in the same state as sending it once. Two identical `POST` requests may create two orders, two identical `PUT` requests leave the resource in the same state.

### What to watch for in tests

| Method | Typical defects |
|---|---|
| `GET` | the endpoint changes data, sensitive data in the URL (ends up in logs and history), stale data from cache, wrong handling of query parameters |
| `POST` | no validation, duplicates when resent, wrong status code (`200` instead of `201`), no body size limit |
| `PUT` | fields not sent in the body get cleared, another user's changes overwritten during concurrent edits |
| `PATCH` | fields that were not sent get changed, changed fields not validated, inconsistent data |
| `DELETE` | deletion without permissions, deleting a resource used by other records, the resource still visible through cache |

!!! tip "Concurrency and duplicates"
    - Concurrent edits: with an `If-Match` header and a stale `ETag`, the server should return `412 Precondition Failed` instead of overwriting another user's changes.
    - Resending a `POST`: with the same `Idempotency-Key` header, no second resource should be created.
    - A `429` or `503` response should include a `Retry-After` header.

!!! info "Hard delete and soft delete"
    With a **hard delete** the record is removed from the database. With a **soft delete** it is marked as deleted (e.g. `deleted_at`). Check that a "deleted" resource does not come back in lists, search or reports.

## HTTP status codes

| Class | Meaning |
|---|---|
| **1xx** | informational, e.g. `101 Switching Protocols` (WebSocket) |
| **2xx** | success |
| **3xx** | redirection |
| **4xx** | client error: a problem in the request |
| **5xx** | server error: the request was valid, but the server failed to handle it |

### 2xx: success

| Code | When |
|---|---|
| `200 OK` | the request succeeded, the response contains data |
| `201 Created` | a resource was created (usually after `POST`), often with a `Location` header |
| `202 Accepted` | the request was accepted for background processing |
| `204 No Content` | success with no body, e.g. after `DELETE` |

### 3xx: redirection

| Code | When |
|---|---|
| `301 Moved Permanently` | the resource has moved permanently |
| `302 Found` | temporary redirect |
| `304 Not Modified` | the resource has not changed, the client can use its cached copy |
| `307` / `308` | temporary / permanent redirect that keeps the method and body |

Typical defects: redirect loops, redirects to a missing resource, `POST` turned into `GET` after a `301` or `302` redirect.

### 4xx: client error

| Code | When |
|---|---|
| `400 Bad Request` | invalid request: wrong format, validation error |
| `401 Unauthorized` | missing or invalid authentication (no token, expired token) |
| `403 Forbidden` | the user is known but has no permission |
| `404 Not Found` | the resource does not exist |
| `405 Method Not Allowed` | the method is not allowed for this endpoint |
| `409 Conflict` | conflict with the resource state, e.g. e-mail already taken |
| `415 Unsupported Media Type` | unsupported request `Content-Type` |
| `422 Unprocessable Content` | valid format but invalid data (used instead of `400` by some APIs) |
| `429 Too Many Requests` | rate limit exceeded |

!!! tip "401 or 403?"
    `401`: the server does not know who you are. `403`: it knows, but you have no access. Mixing them up is a common defect. A good pattern for error bodies is the **Problem Details** format (RFC 9457).

### 5xx: server error

| Code | When |
|---|---|
| `500 Internal Server Error` | an unhandled exception in the application |
| `501 Not Implemented` | the server does not support the function or method |
| `502 Bad Gateway` | a proxy server received an invalid response from the next server |
| `503 Service Unavailable` | the service is temporarily unavailable (overload, maintenance) |
| `504 Gateway Timeout` | a proxy server did not get a response in time |

!!! warning "An unexpected 5xx is a bug report"
    A `500` after sending invalid data means the server does not validate input. The correct response is `400` or `422` with a clear message. A `5xx` response should also never reveal a stack trace or infrastructure details. Planned situations are the exception, e.g. `503 Service Unavailable` with a `Retry-After` header during maintenance.

!!! note "Good to know"
    `418 I'm a teapot` started as an April Fools' joke (RFC 2324) and is not used in real APIs.

## HTTP headers

Headers are `Name: value` pairs sent in requests and responses. They define the data format, authentication, caching, security and how the message is handled. Header names are **case-insensitive**.

### Common headers

| Header | Where | Role | What to test |
|---|---|---|---|
| `Content-Type` | both | body format, e.g. `application/json`, `multipart/form-data` | a wrong type should return `415` or `400`, not `500` |
| `Accept` | request | response format accepted by the client | unsupported format: `406 Not Acceptable` |
| `Authorization` | request | credentials: `Bearer`, `Basic` | missing, expired or tampered token: `401` |
| `Cookie` / `Set-Cookie` | request / response | session and data stored in the browser | `HttpOnly`, `Secure`, `SameSite` flags on the session cookie |
| `Cache-Control` | both | caching rules, e.g. `no-store`, `max-age=3600` | private data must not end up in a shared cache |
| `Location` | response | URL of a new resource (`201`) or a redirect (`3xx`) | whether it points to the right resource |
| `Host` | request | server domain, required in HTTP/1.1 | |
| `User-Agent` | request | identifies the client, e.g. a browser, `PostmanRuntime`, `curl` | easy to fake, so it must not be used for security |
| `Origin` | request | origin of a browser request, used by CORS | |
| `Access-Control-Allow-Origin` | response | domains allowed to read the response (CORS) | `*` on endpoints that require login |
| `Referer` | request | the page the request came from | must not carry tokens or personal data in the URL |

!!! note "Good to know"
    The spelling `Referer` (instead of the correct `Referrer`) is a typo from the original specification that stayed in the standard.

### Headers in API testing

Incorrect headers are a frequent cause of integration bugs and security gaps. In tests, check:

- the response when a required header is missing or has an invalid value,
- whether the response `Content-Type` matches the actual content,
- security headers: `Strict-Transport-Security`, `X-Content-Type-Options`, `Content-Security-Policy`,
- whether the response reveals unnecessary information, e.g. the server version in `Server` or `X-Powered-By`,
- a `431 Request Header Fields Too Large` response for very large headers instead of a `5xx` error.
