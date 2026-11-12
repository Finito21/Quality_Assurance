---
description: "Swagger and OpenAPI: reading an API specification, trying endpoints from the docs and contract testing."
---

# Swagger / OpenAPI

The **OpenAPI Specification (OAS)** is a standard for describing REST APIs in a YAML or JSON file. **Swagger** is a set of tools for working with this specification.

| Tool | Used for |
|---|---|
| **Swagger UI** | interactive documentation in the browser with a **Try it out** button |
| **Swagger Editor** | editing the specification with a live preview |
| **Swagger Codegen / OpenAPI Generator** | generating clients and server stubs |

## Specification excerpt

```yaml
openapi: 3.0.3
info:
  title: Shop API
  version: 1.0.0
paths:
  /products/{id}:
    get:
      summary: Get a product
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
          description: Not found
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

## Swagger in a tester's work

- **source of truth**: the documentation says which endpoints, parameters, required fields and status codes exist, so it is the **basis for tests**,
- **Try it out**: quickly calling an endpoint by hand without Postman,
- **import into Postman**: *Import → OpenAPI link or file* creates a ready-made collection,
- **schema validation**: comparing the response with `components/schemas`,
- **testing the documentation**: a mismatch between the specification and the API's behaviour is also a defect.

!!! tip
    The documentation is often available at `/swagger`, `/swagger-ui`, `/api-docs` or `/docs`.
