---
description: "Uwierzytelnianie i autoryzacja w API: Basic, klucze API, JWT, OAuth 2.0 i OpenID Connect, z przypadkami testowymi i typowymi lukami bezpieczeństwa."
---

# Uwierzytelnianie i autoryzacja

| | Uwierzytelnianie (authentication) | Autoryzacja (authorization) |
|---|---|---|
| **Pytanie** | *Kim jesteś?* | *Co możesz zrobić?* |
| **Przykład** | logowanie loginem i hasłem, token | rola `admin` może usuwać użytkowników, rola `user` nie |
| **Błąd w API** | `401 Unauthorized` | `403 Forbidden` |

W API najczęściej stosuje się tokeny, klucze API i standard OAuth 2.0. Dane uwierzytelniające przesyła się zwykle w nagłówku `Authorization` ([Nagłówki HTTP](http.md#nagowki-http)).

## Bearer Token

Klient przesyła **token dostępowy** otrzymany np. po zalogowaniu:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

- token ma ograniczony czas ważności, serwer sprawdza go przy każdym żądaniu,
- często jest to **JWT (JSON Web Token)**: trzy części zakodowane w Base64URL (nagłówek, dane, podpis); zawartość można odczytać, np. na jwt.io, ale nie można jej zmienić bez unieważnienia podpisu. Dane są tylko zakodowane, a nie zaszyfrowane, więc nie mogą zawierać haseł ani innych danych wrażliwych.

## Basic Auth

Login i hasło połączone dwukropkiem i zakodowane w **Base64**:

```http
Authorization: Basic dGVzdGVyOmhhc2xvMTIz
```

!!! warning "Base64 to kodowanie, a nie szyfrowanie"
    Każdy, kto przechwyci nagłówek, odczyta login i hasło. Basic Auth stosuje się tylko przez HTTPS, głównie w środowiskach testowych, prostych integracjach i systemach wewnętrznych.

## Klucze API

**Klucz API (API key)** to unikalny identyfikator aplikacji (nie użytkownika), przesyłany w nagłówku (np. `X-API-Key`) lub rzadziej w query.

- identyfikuje klienta i pozwala monitorować użycie API,
- pozwala nakładać limity żądań i ograniczać dostęp do wybranych zasobów,
- typowe zastosowania: publiczne API, usługi SaaS, platformy chmurowe.

!!! danger "Klucze w repozytorium"
    Klucz opublikowany w repozytorium Git trzeba uznać za ujawniony i od razu go unieważnić. Klucze przechowuje się w zmiennych środowiskowych lub menedżerze sekretów.

## OAuth 2.0

**OAuth 2.0** to standard **delegowania dostępu**: aplikacja dostaje ograniczony dostęp do zasobów użytkownika bez poznania jego hasła. Używają go m.in. Google, Microsoft i GitHub. OAuth 2.0 służy do autoryzacji; samo logowanie („Zaloguj przez…”) realizuje zbudowany na nim **OpenID Connect** (token `id_token`).

| Element | Rola |
|---|---|
| **Resource Owner** | użytkownik, do którego należą dane |
| **Client** | aplikacja, która chce uzyskać dostęp |
| **Authorization Server** | wydaje tokeny po zgodzie użytkownika |
| **Resource Server** | API z danymi, przyjmuje access token |
| **Access Token** | krótkotrwały token dostępu |
| **Refresh Token** | długotrwały token do pobrania nowego access tokena |
| **Scope** | zakres uprawnień, np. `read:orders` |

```mermaid
sequenceDiagram
    accTitle: OAuth 2.0
    accDescr: Użytkownik loguje się na serwerze autoryzacji, aplikacja dostaje kod i wymienia go na tokeny, a potem wywołuje API z tokenem w nagłówku Authorization.
    participant U as Użytkownik
    participant C as Aplikacja (Client)
    participant AS as Authorization Server
    participant RS as API (Resource Server)
    U->>C: Zaloguj przez...
    C->>AS: przekierowanie do logowania (state, code_challenge)
    U->>AS: logowanie i zgoda na zakres
    AS-->>C: kod autoryzacyjny
    C->>AS: wymiana kodu na tokeny (code_verifier)
    AS-->>C: access token + refresh token
    C->>RS: żądanie z Authorization: Bearer
    RS-->>C: dane
```

!!! tip "Authorization Code z PKCE"
    Dla aplikacji publicznych (SPA, mobilnych) zaleca się przepływ **Authorization Code z PKCE** (RFC 7636), a przepływów **Implicit** i **Resource Owner Password** nie używa się już w nowych systemach. Warto sprawdzić, czy serwer odrzuca wymianę kodu bez poprawnego `code_verifier`, czy `redirect_uri` jest weryfikowany dokładnie, a nie tylko po prefiksie, oraz czy aplikacja odrzuca odpowiedź z wartością `state`, której nie wysłała (ochrona przed CSRF).

## Co testować

| Scenariusz | Oczekiwany wynik |
|---|---|
| żądanie bez tokena lub klucza | `401` |
| wygasły, zmodyfikowany lub losowy token | `401` |
| JWT z `alg: none`, zmienionym payloadem albo złym `aud` lub `iss` | `401` (podpis i deklaracje muszą być sprawdzane) |
| JWT z wygasłym `exp` albo `nbf` z przyszłości | `401` |
| JWT podpisany `HS256` kluczem publicznym, gdy serwer oczekuje `RS256` (pomylenie algorytmów) | `401` |
| poprawny token, ale brak uprawnień (rola, scope) | `403` |
| dostęp do cudzego zasobu przez zmianę ID w URL (IDOR) | `403` lub `404`, nigdy dane innego użytkownika |
| wylogowanie | token przestaje działać, jeśli system obsługuje unieważnianie |
| odświeżenie tokena | nowy access token działa, użyty refresh token nie działa ponownie (jeśli stosowana rotacja) |
| wiele błędnych logowań | limit prób lub blokada (`429` lub komunikat o blokadzie) |
| treść odpowiedzi i logów | brak haseł, tokenów i kluczy |

Odpowiedź `401` musi zawierać nagłówek `WWW-Authenticate` (RFC 9110), więc jego brak to defekt. IDOR to w OWASP API Security Top 10 (2023) kategoria **BOLA** (API1).

Praktyka w Postmanie (zakładka *Authorization*, zapisywanie tokena do zmiennej): [Postman](../../tools/api_testing_tools/postman.md).
