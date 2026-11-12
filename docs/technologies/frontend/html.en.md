---
description: "HTML for testers: document structure, basic and semantic tags, forms, IDs and classes, and how page markup affects accessibility, testing and automation."
---

# HTML

**HTML (HyperText Markup Language)** defines the **structure** of a web page. Elements are described with **tags** in angle brackets `< >`.

!!! tip "Why should a tester know HTML?"
    The HTML structure is the basis for **locators** in automation (Selenium, Cypress), for analysing bugs in [DevTools](../../tools/devtools.md) and for accessibility testing.

## Document structure

```html
<!DOCTYPE html>               <!-- an HTML5 document -->
<html lang="en">
<head>
  <meta charset="UTF-8">      <!-- character encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- without it media queries do not work on phones -->
  <title>Page title</title>
  <link rel="icon" href="favicon.ico">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Page content</h1>
  <script src="main.js"></script>
</body>
</html>
```

The `<head>` section contains, among other things, the page title, character encoding, icon (favicon) and the linked CSS file.

## Basic tags

| Tag | Description |
|---|---|
| `<h1>` … `<h6>` | headings: `h1` the most important, `h6` the least |
| `<p>` | paragraph (always starts on a new line) |
| `<span>` | inline element (does not break the line) |
| `<div>` | generic block container |
| `<b>` / `<strong>` | bold: visual / semantic (important text) |
| `<i>` / `<em>` | italics: visual / semantic |
| `<a href="...">` | link |
| `<img src="..." alt="...">` | image (`alt` matters for accessibility) |
| `<form>`, `<input>`, `<button>` | forms |

## Lists

=== "Ordered"

    ```html
    <ol>
      <li>Item</li>
      <li>Item</li>
    </ol>
    ```

=== "Unordered"

    ```html
    <ul>
      <li>Item</li>
      <li>Item</li>
    </ul>
    ```

## IDs and classes

| Attribute | Rule | Example |
|---|---|---|
| `id` | **unique**, only one per page | `id="login-button"` |
| `class` | can appear **many times** | `class="btn btn-primary"` |

Good practice for automation: dedicated test attributes, e.g. `data-testid="submit"` or `data-cy="submit"`, which do not change when the look of the page changes.

## Semantic HTML5 tags

| Tag | Use |
|---|---|
| `<header>` | header of a page or section |
| `<nav>` | navigation |
| `<main>` | main content |
| `<section>` | grouping thematic content |
| `<article>` | self-contained content (e.g. a post) |
| `<footer>` | footer |

Semantics helps screen readers and SEO, and makes it easier to write stable locators.
