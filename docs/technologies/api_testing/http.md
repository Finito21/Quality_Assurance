---
description: "HTTP dla testera: metody, idempotentność, kody statusu, nagłówki i typowe defekty wykrywane na poziomie protokołu."
---

# HTTP: metody, kody, nagłówki

**HTTP (HyperText Transfer Protocol)** to protokół, którym klient (przeglądarka, aplikacja mobilna, Postman) komunikuje się z serwerem w modelu żądanie → odpowiedź. Budowę żądania i odpowiedzi opisuje strona [Podstawy API](api_fundamentals.md#jak-dziaa-api).

HTTP jest **bezstanowy**: każde żądanie jest obsługiwane niezależnie od poprzednich. Aby rozpoznać użytkownika między żądaniami, stosuje się cookies, identyfikator sesji lub tokeny ([Uwierzytelnianie i autoryzacja](authentication.md)).

```http
POST /api/orders HTTP/1.1
Host: shop.example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{"productId": 15, "quantity": 2}
```

## Metody HTTP

| Metoda | Zastosowanie | Body | Bezpieczna | Idempotentna |
|---|---|---|---|---|
| `GET` | pobranie zasobu | nie | tak | tak |
| `POST` | utworzenie zasobu lub wykonanie operacji (logowanie, płatność) | tak | nie | nie |
| `PUT` | zastąpienie całego zasobu | tak | nie | tak |
| `PATCH` | częściowa zmiana zasobu | tak | nie | zależy od implementacji |
| `DELETE` | usunięcie zasobu | zwykle nie | nie | tak |
| `HEAD` | jak `GET`, ale tylko nagłówki | nie | tak | tak |
| `OPTIONS` | dozwolone metody, zapytanie wstępne CORS (preflight) | nie | tak | tak |

**Bezpieczna (safe)**
:   Nie zmienia stanu serwera.

**Idempotentna (idempotent)**
:   Wielokrotne wysłanie tego samego żądania daje ten sam stan serwera co jednokrotne. Dwa identyczne `POST` mogą utworzyć dwa zamówienia, dwa identyczne `PUT` zostawią zasób w tym samym stanie.

### Na co uważać przy testach

| Metoda | Typowe defekty |
|---|---|
| `GET` | endpoint zmienia dane, wrażliwe dane w URL (trafiają do logów i historii), nieaktualne dane z cache, błędna obsługa parametrów query |
| `POST` | brak walidacji, duplikaty po ponownym wysłaniu, zły kod statusu (`200` zamiast `201`), brak limitu rozmiaru body |
| `PUT` | pola niewysłane w body zostają wyczyszczone, nadpisanie zmian innego użytkownika przy równoczesnej edycji |
| `PATCH` | zmiana pól, których nie wysłano, brak walidacji zmienianych pól, niespójne dane |
| `DELETE` | usunięcie bez uprawnień, usunięcie zasobu używanego przez inne rekordy, zasób nadal widoczny przez cache |

!!! tip "Współbieżność i duplikaty"
    - Równoczesna edycja: z nagłówkiem `If-Match` i nieaktualnym `ETag` serwer powinien zwrócić `412 Precondition Failed`, a nie nadpisać cudze zmiany.
    - Ponowne wysłanie `POST`: z tym samym nagłówkiem `Idempotency-Key` nie powinien powstać drugi zasób.
    - Odpowiedź `429` lub `503` powinna zawierać nagłówek `Retry-After`.

!!! info "Hard delete i soft delete"
    Przy **hard delete** rekord znika z bazy. Przy **soft delete** zostaje oznaczony jako usunięty (np. `deleted_at`). Warto sprawdzić, czy „usunięty” zasób nie wraca w listach, wyszukiwarce ani raportach.

## Kody odpowiedzi HTTP

| Klasa | Znaczenie |
|---|---|
| **1xx** | informacyjne, np. `101 Switching Protocols` (WebSocket) |
| **2xx** | sukces |
| **3xx** | przekierowanie |
| **4xx** | błąd po stronie klienta: problem w żądaniu |
| **5xx** | błąd po stronie serwera: żądanie poprawne, ale serwer go nie obsłużył |

### 2xx: sukces

| Kod | Kiedy |
|---|---|
| `200 OK` | żądanie wykonane, odpowiedź zawiera dane |
| `201 Created` | zasób utworzony (zwykle po `POST`), często z nagłówkiem `Location` |
| `202 Accepted` | żądanie przyjęte do przetworzenia w tle |
| `204 No Content` | sukces bez body, np. po `DELETE` |

### 3xx: przekierowanie

| Kod | Kiedy |
|---|---|
| `301 Moved Permanently` | zasób przeniesiony na stałe |
| `302 Found` | przekierowanie tymczasowe |
| `304 Not Modified` | zasób się nie zmienił, klient może użyć wersji z cache |
| `307` / `308` | przekierowanie tymczasowe / stałe z zachowaniem metody i body |

Typowe defekty: pętle przekierowań, przekierowanie do nieistniejącego zasobu, `POST` zamieniony w `GET` po przekierowaniu `301` lub `302`.

### 4xx: błąd klienta

| Kod | Kiedy |
|---|---|
| `400 Bad Request` | niepoprawne żądanie: zły format, błąd walidacji |
| `401 Unauthorized` | brak lub niepoprawne uwierzytelnienie (brak tokena, token wygasł) |
| `403 Forbidden` | użytkownik jest znany, ale nie ma uprawnień |
| `404 Not Found` | zasób nie istnieje |
| `405 Method Not Allowed` | metoda niedozwolona dla tego endpointu |
| `409 Conflict` | konflikt ze stanem zasobu, np. e-mail już zajęty |
| `415 Unsupported Media Type` | nieobsługiwany `Content-Type` żądania |
| `422 Unprocessable Content` | poprawny format, ale błędne dane (stosowany zamiast `400` w części API) |
| `429 Too Many Requests` | przekroczony limit żądań |

!!! tip "401 czy 403?"
    `401`: serwer nie wie, kim jesteś. `403`: wie, ale nie masz dostępu. Pomylenie tych kodów to częsty defekt. Dobrym wzorcem treści błędu jest format **Problem Details** (RFC 9457).

### 5xx: błąd serwera

| Kod | Kiedy |
|---|---|
| `500 Internal Server Error` | nieobsłużony wyjątek w aplikacji |
| `501 Not Implemented` | serwer nie obsługuje danej funkcji lub metody |
| `502 Bad Gateway` | serwer pośredniczący dostał błędną odpowiedź od kolejnego serwera |
| `503 Service Unavailable` | usługa chwilowo niedostępna (przeciążenie, prace serwisowe) |
| `504 Gateway Timeout` | serwer pośredniczący nie doczekał się odpowiedzi |

!!! warning "Nieoczekiwane 5xx to zgłoszenie"
    Błąd `500` po wysłaniu niepoprawnych danych oznacza, że serwer nie waliduje wejścia. Poprawna odpowiedź to `400` lub `422` z czytelnym komunikatem. Odpowiedź `5xx` nie powinna też ujawniać stack trace ani szczegółów infrastruktury. Wyjątkiem są sytuacje zaplanowane, np. `503 Service Unavailable` z nagłówkiem `Retry-After` podczas prac serwisowych.

!!! note "Warto wiedzieć"
    `418 I'm a teapot` powstał jako żart primaaprilisowy (RFC 2324) i nie jest używany w prawdziwych API.

## Nagłówki HTTP

Nagłówki to pary `Nazwa: wartość` przesyłane w żądaniu i odpowiedzi. Określają format danych, uwierzytelnienie, cache, bezpieczeństwo i sposób obsługi komunikatu. Nazwy nagłówków **nie rozróżniają wielkości liter**.

### Najczęściej używane nagłówki

| Nagłówek | Gdzie | Rola | Co testować |
|---|---|---|---|
| `Content-Type` | oba | format body, np. `application/json`, `multipart/form-data` | zły typ powinien dać `415` lub `400`, nie `500` |
| `Accept` | żądanie | format odpowiedzi akceptowany przez klienta | nieobsługiwany format: `406 Not Acceptable` |
| `Authorization` | żądanie | dane uwierzytelniające: `Bearer`, `Basic` | brak, wygasły lub zmodyfikowany token: `401` |
| `Cookie` / `Set-Cookie` | żądanie / odpowiedź | sesja i dane zapisane w przeglądarce | flagi `HttpOnly`, `Secure`, `SameSite` na ciasteczku sesji |
| `Cache-Control` | oba | zasady cache, np. `no-store`, `max-age=3600` | dane prywatne nie mogą trafiać do cache współdzielonego |
| `Location` | odpowiedź | adres nowego zasobu (`201`) lub przekierowania (`3xx`) | czy wskazuje właściwy zasób |
| `Host` | żądanie | domena serwera, wymagany w HTTP/1.1 | |
| `User-Agent` | żądanie | identyfikacja klienta, np. przeglądarka, `PostmanRuntime`, `curl` | łatwo go podmienić, więc nie może służyć do zabezpieczeń |
| `Origin` | żądanie | źródło żądania z przeglądarki, używane przez CORS | |
| `Access-Control-Allow-Origin` | odpowiedź | domeny, które mogą czytać odpowiedź (CORS) | `*` przy endpointach wymagających logowania |
| `Referer` | żądanie | strona, z której przyszło żądanie | nie powinien zawierać tokenów ani danych osobowych w URL |

!!! note "Warto wiedzieć"
    Pisownia `Referer` (zamiast poprawnego `Referrer`) to literówka z oryginalnej specyfikacji, która została w standardzie.

### Nagłówki w testach API

Niepoprawne nagłówki to częsta przyczyna błędów integracji i luk bezpieczeństwa. W testach warto sprawdzić:

- odpowiedź przy braku wymaganego nagłówka i przy niepoprawnej wartości,
- czy `Content-Type` odpowiedzi zgadza się z faktyczną treścią,
- nagłówki bezpieczeństwa: `Strict-Transport-Security`, `X-Content-Type-Options`, `Content-Security-Policy`,
- czy odpowiedź nie ujawnia zbędnych informacji, np. wersji serwera w `Server` lub `X-Powered-By`,
- odpowiedź `431 Request Header Fields Too Large` przy bardzo dużych nagłówkach zamiast błędu `5xx`.
