---
description: "HTML dla testera: struktura dokumentu, tagi podstawowe i semantyczne, formularze, identyfikatory i klasy oraz wpływ budowy strony na testy i automatyzację."
---

# HTML

**HTML (HyperText Markup Language)** służy do definiowania **struktury** strony internetowej. Elementy opisuje się za pomocą **znaczników (tagów)** w nawiasach ostrych `< >`.

!!! tip "Dlaczego tester powinien znać HTML?"
    Struktura HTML to podstawa **lokatorów** w automatyzacji (Selenium, Cypress), analizy błędów w [DevTools](../../tools/devtools.md) i testów dostępności.

## Struktura dokumentu

```html
<!DOCTYPE html>               <!-- dokument w standardzie HTML5 -->
<html lang="pl">
<head>
  <meta charset="UTF-8">      <!-- kodowanie znaków (polskie litery) -->
  <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- bez tego telefon renderuje stronę w szerokości desktopu i media queries nie pasują do ekranu -->
  <title>Tytuł strony</title>
  <link rel="icon" href="favicon.ico">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Treść strony</h1>
  <script src="main.js"></script>
</body>
</html>
```

Sekcja `<head>` zawiera m.in. tytuł strony, kodowanie znaków, ikonę (favicon) i podpięcie pliku CSS.

## Podstawowe znaczniki

| Znacznik | Opis |
|---|---|
| `<h1>` … `<h6>` | nagłówki: `h1` najważniejszy, `h6` najmniej istotny |
| `<p>` | akapit (zawsze zaczyna się w nowej linii) |
| `<span>` | element liniowy (nie łamie linii) |
| `<div>` | uniwersalny kontener blokowy |
| `<b>` / `<strong>` | pogrubienie: wizualne / semantyczne (ważny tekst) |
| `<i>` / `<em>` | kursywa: wizualna / semantyczna |
| `<a href="...">` | link |
| `<img src="..." alt="...">` | obraz (`alt` ważny dla dostępności) |
| `<form>`, `<input>`, `<button>` | formularze |

## Listy

=== "Numerowana"

    ```html
    <ol>
      <li>Element</li>
      <li>Element</li>
    </ol>
    ```

=== "Punktowana"

    ```html
    <ul>
      <li>Element</li>
      <li>Element</li>
    </ul>
    ```

## Identyfikatory i klasy

| Atrybut | Zasada | Przykład |
|---|---|---|
| `id` | **unikalny**, tylko jeden na stronie | `id="login-button"` |
| `class` | może występować **wielokrotnie** | `class="btn btn-primary"` |

Dobre praktyki dla automatyzacji: dedykowane atrybuty testowe, np. `data-testid="submit"` albo `data-cy="submit"`, które nie zmieniają się przy zmianach wyglądu.

## Semantyczne znaczniki HTML5

| Znacznik | Zastosowanie |
|---|---|
| `<header>` | nagłówek strony lub sekcji |
| `<nav>` | nawigacja |
| `<main>` | główna treść |
| `<section>` | grupowanie tematycznej treści |
| `<article>` | niezależna treść (np. post) |
| `<footer>` | stopka |

Semantyka pomaga czytnikom ekranu, SEO i ułatwia pisanie stabilnych lokatorów.
