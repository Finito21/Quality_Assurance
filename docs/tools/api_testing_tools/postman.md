---
description: "Postman w pracy testera: kolekcje, zmienne i środowiska, skrypty testowe pm.* oraz uruchamianie testów w CI."
---

# Postman

**Postman** to narzędzie do testowania i debugowania API. Pozwala wysyłać żądania HTTP i analizować odpowiedzi w wygodnym interfejsie graficznym.

## Funkcje

<div class="grid cards" markdown>

-   **Żądania HTTP**: wszystkie metody, nagłówki, body, autoryzacja
-   **Kolekcje**: grupowanie i organizacja requestów
-   **Testy automatyczne**: asercje w JavaScripcie
-   **Środowiska i zmienne**: test / staging / prod
-   **Runner**: uruchamianie całych kolekcji
-   **Mock Servers**: udawany backend
-   **Monitors**: cykliczne uruchamianie i statystyki
-   **Dokumentacja API**: generowana z kolekcji

</div>

## Podstawowe pojęcia

| Pojęcie | Przykład / opis |
|---|---|
| **Base URL** | `https://api.example.com` |
| **Endpoint** | `/users`, `/products/1` |
| **Query params** | `/users?status=active&role=admin` (zaczynają się od `?`, łączone `&`, służą do filtrowania) |
| **Path param / ID** | `/products/1`, czyli konkretny obiekt |
| **Body** | zakładka *Body → raw → JSON* |

### JSON w skrócie

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 3999.99,
  "available": true,
  "tags": ["elektronika", "komputery"],
  "producer": { "name": "ACME", "country": "PL" }
}
```

`{ }` to obiekt, `[ ]` to tablica, stringi w `" "`, liczby i wartości logiczne bez cudzysłowów, obiekty mogą być zagnieżdżane.

## Autoryzacja

- **Bearer Token**: token podawany w nagłówku `Authorization: Bearer <token>`. Można go otrzymać od programisty lub pobrać requestem logowania i zapisać do zmiennej.
- **Basic Auth**: login i hasło kodowane w **Base64** (to kodowanie, a nie szyfrowanie, więc tylko przez HTTPS).
- **API Key**, **OAuth 2.0**: patrz [Uwierzytelnianie i autoryzacja](../../technologies/api_testing/authentication.md).

## Zmienne

Składnia: `{{nazwaZmiennej}}`

| Zakres | Opis | Priorytet |
|---|---|---|
| **Lokalne** | tylko dla jednego requestu / wykonania | najwyższy |
| **Danych (data)** | z pliku CSV/JSON w Runnerze | |
| **Środowiskowe** | zależne od środowiska (test, prod) | |
| **Kolekcji** | tylko dla danej kolekcji | |
| **Globalne** | dostępne wszędzie | najniższy |

```javascript
pm.environment.set("token", pm.response.json().accessToken);
pm.collectionVariables.get("userId");
```

## Testy

Testy pisze się w JavaScripcie (zakładka **Scripts → Post-response**). Można sprawdzać kod odpowiedzi, czas odpowiedzi, strukturę i zawartość body, liczbę obiektów oraz zapisywać dane do zmiennych.

Przykłady i dobre praktyki: **[Automatyzacja testów API](../../technologies/api_testing/api_automation.md)**.

## Pierwszy test krok po kroku

Ćwiczenie na publicznym, darmowym API do nauki **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)**. Zwraca przykładowe dane i nie zapisuje zmian, więc niczego nie zepsujesz.

1. **Środowisko**: *Environments → +*, nazwa `JSONPlaceholder`, zmienna `baseUrl` = `https://jsonplaceholder.typicode.com`. Wybierz środowisko w prawym górnym rogu.
2. **Kolekcja**: *Collections → +*, nazwa `Ćwiczenia API`.
3. **Request**: w kolekcji *Add request*, metoda `GET`, adres `{{baseUrl}}/users/1`, kliknij **Send**. Odpowiedź ma kod `200 OK` i dane jednego użytkownika w JSON.
4. **Testy**: w zakładce *Scripts → Post-response* wklej:

    ```javascript
    pm.test("Kod odpowiedzi 200", () => {
      pm.response.to.have.status(200);
    });

    pm.test("Odpowiedź w mniej niż 1 s", () => {
      pm.expect(pm.response.responseTime).to.be.below(1000);
    });

    pm.test("Użytkownik ma id 1 i poprawny e-mail", () => {
      const user = pm.response.json();
      pm.expect(user.id).to.eql(1);
      pm.expect(user.email).to.match(/^\S+@\S+\.\S+$/);
    });

    // zapisanie danych do użycia w kolejnym requeście
    pm.collectionVariables.set("userId", pm.response.json().id);
    ```

5. Kliknij **Send** jeszcze raz i otwórz zakładkę *Test Results*: wszystkie testy powinny być zielone.
6. **Drugi request**: `GET {{baseUrl}}/posts?userId={{userId}}` z testem, że każdy post należy do tego użytkownika:

    ```javascript
    pm.test("Wszystkie posty należą do użytkownika", () => {
      const userId = Number(pm.collectionVariables.get("userId"));
      pm.response.json().forEach((post) => pm.expect(post.userId).to.eql(userId));
    });
    ```

7. **Test negatywny**: `GET {{baseUrl}}/users/9999` powinien zwrócić `404`. Dopisz test na ten kod.
8. **Runner**: kliknij kolekcję → *Run* i uruchom wszystkie requesty naraz.

!!! tip "Co dalej"
    Dodaj request `POST {{baseUrl}}/posts` z body w JSON i sprawdź, czy odpowiedź ma kod `201` i zawiera wysłane pola. Potem uruchom kolekcję z wiersza poleceń przez Newman.

## Collection Runner

Uruchamia całe kolekcje lub foldery z testami. Pozwala:

- ustawić **liczbę iteracji** i **opóźnienia** między requestami,
- wybrać **środowisko**,
- podać plik z danymi (**data-driven testing**),
- zaplanować uruchomienia (harmonogram) lub uruchomić ręcznie.

W CI kolekcje uruchamia się przez **Newman** lub **Postman CLI**.

## Examples i Mock Servers

**Examples** to zapisane przykładowe pary request + response. Pokazują innym, jak poprawnie zbudować body.

**Mock Server** to udawany serwer API zwracający zdefiniowane odpowiedzi (na podstawie Examples). Przydaje się, gdy:

- backend jeszcze nie istnieje,
- API jest niestabilne lub niedostępne,
- testujesz frontend lub integrację,
- chcesz ćwiczyć bez ryzyka zmiany prawdziwych danych.

## Monitors

Cykliczne uruchamianie kolekcji w chmurze Postmana ze statystykami: liczba testów, błędy, czas odpowiedzi.

## Postman i Git

Kolekcje można trzymać w repozytorium (eksport JSON albo natywna integracja Postmana z Gitem). Plik w katalogu `.postman/` łączy lokalne repo z **workspace w chmurze Postmana**. Przy pracy wyłącznie lokalnej warto pilnować, żeby w repo nie zostawały odwołania do nieistniejących kolekcji i środowisk.
