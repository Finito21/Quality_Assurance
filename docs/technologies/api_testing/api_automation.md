---
description: "Automatyzacja testów API: asercje w Postmanie, łańcuchy żądań, dane testowe, walidacja schematu i uruchamianie kolekcji w CI przez Newmana."
---

# Automatyzacja testów API

**Automatyzacja testów API** to wykonywanie testów API przy użyciu narzędzi i skryptów, bez ręcznej ingerencji. Testy mogą być uruchamiane automatycznie, np. w pipeline CI/CD, w celu ciągłej weryfikacji działania API i szybszego wykrywania defektów.

## Co weryfikować?

- [x] **kod odpowiedzi** (np. `200`, `201`, `400`, `404`),
- [x] **czas odpowiedzi**,
- [x] **nagłówki**, np. `Content-Type`,
- [x] **strukturę body**, czyli zgodność ze **schematem** (JSON Schema),
- [x] **zawartość body**: konkretne wartości, liczba obiektów,
- [x] **ścieżki negatywne**: błędne dane, brak autoryzacji, nieistniejące zasoby.

## Testy w Postmanie

Testy pisze się w JavaScripcie w zakładce **Scripts → Post-response** (dawniej *Tests*), z użyciem obiektu `pm`.

```javascript
pm.test("Status 200", () => {
  pm.response.to.have.status(200);
});

pm.test("Czas odpowiedzi < 500 ms", () => {
  pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Zwrócono listę użytkowników", () => {
  const body = pm.response.json();
  pm.expect(body).to.be.an("array").that.is.not.empty;
  pm.expect(body[0]).to.have.property("email");
});

// zapis wartości do zmiennej na potrzeby kolejnych requestów
pm.collectionVariables.set("userId", pm.response.json()[0].id);
```

### Przykład: walidacja odpowiedzi błędu (RFC 9457 *Problem Details*)

Wymagania:

- `Content-Type` ma wartość `application/problem+json` (a nie `application/json` czy `text/html`),
- obecny jest nagłówek `x-correlation-id` (identyfikowalność / tracing),
- `correlationId` w body jest **identyczne** z wartością nagłówka,
- komunikat `detail` jest zgodny ze specyfikacją.

```javascript
const body = pm.response.json();

pm.test("Status 400", () => pm.response.to.have.status(400));

pm.test("Content-Type = application/problem+json", () => {
  pm.expect(pm.response.headers.get("Content-Type"))
    .to.include("application/problem+json");
});

pm.test("Nagłówek x-correlation-id istnieje i zgadza się z body", () => {
  const header = pm.response.headers.get("x-correlation-id");
  pm.expect(header).to.be.a("string").and.not.empty;
  pm.expect(body.correlationId).to.eql(header);
});

pm.test("Zgodność ze schematem Problem Details", () => {
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

## Dobre praktyki

!!! tip "Z doświadczenia"
    - **Testy na poziomie kolekcji lub folderu** zamiast kopiowania tych samych asercji do każdego requestu.
    - **Snippety** w Postmanie przyspieszają pisanie typowych asercji.
    - **Celowo zepsuj test** (np. oczekuj `201` zamiast `200`) i sprawdź, czy naprawdę kończy się niepowodzeniem. Test, który zawsze przechodzi, niczego nie sprawdza.
    - Projektuj testy **na podstawie specyfikacji API** (OpenAPI/Swagger), a nie tylko obecnego zachowania.
    - Bardzo duże kolekcje bywają w Postmanie nieporęczne. Pomagają czytelne nazwy requestów i podział na foldery.
    - Ostrożnie z **Postman Agent Mode** (AI) przy danych wrażliwych. Sprawdź, jakie dane trafiają do chmury.

## Uruchamianie w CI/CD: Newman

**Newman** to CLI dla kolekcji Postmana, które pozwala uruchamiać testy w Jenkinsie lub GitHub Actions.

```bash
npm install -g newman newman-reporter-htmlextra
newman run kolekcja.json -e srodowisko_qa.json -r cli,htmlextra
```

## Inne narzędzia do automatyzacji API

| Narzędzie | Język | Charakterystyka |
|---|---|---|
| **Postman + Newman** | JS | GUI + CLI, najłatwiejszy start |
| **SuperTest** | JS/TS | testy API w kodzie, często z Jest/Mocha |
| **REST Assured** | Java | standard w projektach Java |
| **requests + pytest** | Python | prosty i elastyczny zestaw |
| **Playwright (APIRequestContext)** | JS/TS/Python | API + UI w jednym frameworku |
| **SoapUI / ReadyAPI** | GUI / Groovy | REST i SOAP, testy funkcjonalne i obciążeniowe |
