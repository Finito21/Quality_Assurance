---
description: "Swagger i OpenAPI: czytanie specyfikacji API, testowanie endpointów z dokumentacji i testy kontraktowe."
---

# Swagger / OpenAPI

**OpenAPI Specification (OAS)** to standard opisu API REST w pliku YAML lub JSON. **Swagger** to zestaw narzędzi do pracy z tą specyfikacją.

| Narzędzie | Do czego |
|---|---|
| **Swagger UI** | interaktywna dokumentacja w przeglądarce z przyciskiem **Try it out** |
| **Swagger Editor** | edycja specyfikacji z podglądem na żywo |
| **Swagger Codegen / OpenAPI Generator** | generowanie klientów i szkieletów serwera |

## Fragment specyfikacji

```yaml
openapi: 3.1.0
info:
  title: Sklep API
  version: 1.0.0
paths:
  /products/{id}:
    get:
      summary: Pobierz produkt
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: integer }
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Product"
        "404":
          description: Nie znaleziono
components:
  schemas:
    Product:
      type: object
      required: [id, name, price]
      properties:
        id:    { type: integer }
        name:  { type: string }
        price: { type: number }
```

## Swagger w pracy testera

- **źródło prawdy**: dokumentacja mówi, jakie są endpointy, parametry, wymagane pola i kody odpowiedzi, więc to **podstawa testów**,
- **Try it out**: szybkie ręczne wywołanie endpointu bez Postmana,
- **import do Postmana**: *Import → link lub plik OpenAPI* tworzy gotową kolekcję,
- **walidacja schematu**: porównanie odpowiedzi z `components/schemas`,
- **testowanie dokumentacji**: rozbieżność między specyfikacją a zachowaniem API to też defekt.

!!! tip
    Adres dokumentacji często znajdziesz pod `/swagger`, `/swagger-ui`, `/api-docs` lub `/docs`.
