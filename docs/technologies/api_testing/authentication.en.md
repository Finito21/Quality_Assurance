---
description: "Authentication and authorisation in APIs: Basic, API keys, JWT, OAuth 2.0 and OpenID Connect, with test cases."
---

# Authentication and authorisation

| | Authentication | Authorisation |
|---|---|---|
| **Question** | *Who are you?* | *What are you allowed to do?* |
| **Example** | logging in with a username and password, a token | the `admin` role can delete users, the `user` role cannot |
| **Error in an API** | `401 Unauthorized` | `403 Forbidden` |

APIs most often use tokens, API keys and the OAuth 2.0 standard. Credentials are usually sent in the `Authorization` header ([HTTP headers](http.md#http-headers)).

## Bearer token

The client sends an **access token** received e.g. after logging in:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

- the token has a limited lifetime, and the server checks it on every request,
- it is often a **JWT (JSON Web Token)**: three Base64URL-encoded parts (header, payload, signature); the content can be read, e.g. on jwt.io, but cannot be changed without invalidating the signature.

## Basic Auth

The username and password joined with a colon and encoded in **Base64**:

```http
Authorization: Basic dGVzdGVyOnBhc3N3b3JkMTIz
```

!!! warning "Base64 is encoding, not encryption"
    Anyone who intercepts the header can read the username and password. Basic Auth is used only over HTTPS, mainly in test environments, simple integrations and internal systems.

## API keys

An **API key** is a unique identifier of an application (not a user), sent in a header (e.g. `X-API-Key`) or less often in the query.

- identifies the client and makes it possible to monitor API usage,
- allows rate limits and restricting access to selected resources,
- typical uses: public APIs, SaaS services, cloud platforms.

!!! danger "Keys in a repository"
    A key published in a Git repository must be treated as leaked and revoked immediately. Keys belong in environment variables or a secrets manager.

## OAuth 2.0

**OAuth 2.0** is a standard for **delegated access**: an application gets limited access to a user's resources without learning their password. It is used by Google, Microsoft and GitHub, among others. OAuth 2.0 is for authorisation; the sign-in itself ("Sign in with…") is done by **OpenID Connect**, built on top of it (the `id_token`).

| Element | Role |
|---|---|
| **Resource Owner** | the user who owns the data |
| **Client** | the application that wants access |
| **Authorization Server** | issues tokens after the user's consent |
| **Resource Server** | the API with the data, accepts the access token |
| **Access Token** | short-lived access token |
| **Refresh Token** | long-lived token used to get a new access token |
| **Scope** | range of permissions, e.g. `read:orders` |

```mermaid
sequenceDiagram
    accTitle: OAuth 2.0
    accDescr: The user signs in on the authorisation server, the application receives a code and exchanges it for tokens, then calls the API with the token in the Authorization header.
    participant U as User
    participant C as Application (Client)
    participant AS as Authorization Server
    participant RS as API (Resource Server)
    U->>C: Sign in with...
    C->>AS: redirect to login
    U->>AS: sign-in and consent to scope
    AS-->>C: authorisation code
    C->>AS: exchange code for tokens
    AS-->>C: access token + refresh token
    C->>RS: request with Authorization: Bearer
    RS-->>C: data
```

!!! tip "Authorization Code with PKCE"
    For public clients (SPAs, mobile apps) the **Authorization Code flow with PKCE** (RFC 7636) is recommended, while the **Implicit** and **Resource Owner Password** flows should not be used in new systems. Check that the server rejects a code exchange without a valid `code_verifier` and that `redirect_uri` is matched exactly, not just by prefix.

## What to test

| Scenario | Expected result |
|---|---|
| request without a token or key | `401` |
| expired, tampered or random token | `401` |
| JWT with `alg: none`, a changed payload or a wrong `aud` or `iss` | `401` (the signature and claims must be checked) |
| valid token, but no permission (role, scope) | `403` |
| access to another user's resource by changing the ID in the URL (IDOR) | `403` or `404`, never another user's data |
| logout | the token stops working, if the system supports revocation |
| token refresh | the new access token works, a used refresh token does not work again (if rotation is used) |
| many failed logins | attempt limit or lockout (`429` or a lockout message) |
| response and log content | no passwords, tokens or keys |

A `401` response should include a `WWW-Authenticate` header. In the OWASP API Security Top 10 (2023), IDOR is the **BOLA** category (API1).

Hands-on in Postman (the *Authorization* tab, saving a token to a variable): [Postman](../../tools/api_testing_tools/postman.md).
