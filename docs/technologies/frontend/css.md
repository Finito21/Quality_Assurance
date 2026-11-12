---
description: "CSS dla testera: selektory, model pudełkowy, widoczność elementów i responsywność, ze wskazówkami do pisania stabilnych lokatorów i testów UI."
---

# CSS

**CSS (Cascading Style Sheets)** służy do stylizacji strony: wyglądu, układu elementów i **responsywności**. Wykorzystuje **selektory** do wybierania elementów, a w bloku reguły zapisuje się deklaracje: pary właściwość i wartość.

```css
.przycisk:hover {
  background-color: #4f46e5;
  border-radius: 8px;
  transition: 0.2s;
}
```

## Selektory

| Selektor | Wybiera | Przykład |
|---|---|---|
| `element` | wszystkie elementy danego typu | `p` |
| `.klasa` | elementy z klasą | `.btn` |
| `#id` | element o danym id | `#login` |
| `[atrybut]` | elementy z atrybutem / wartością | `[data-testid="submit"]` |
| `A B` | element B będący potomkiem A | `div#band h2.w3-wide` |
| `A > B` | bezpośrednie dziecko | `ul > li` |
| `:hover`, `:nth-child(n)` | pseudoklasy | `a:hover` |

!!! tip "Selektory CSS w automatyzacji"
    Te same selektory wykorzystuje się w Cypress (`cy.get('.btn')`), Selenium (`By.CSS_SELECTOR`) oraz w JS (`document.querySelector`). Można je testować w zakładce **Elements** w DevTools (++ctrl+f++).

## Najczęściej używane właściwości

| Właściwość | Opis |
|---|---|
| `color`, `background-color` | kolor tekstu / tła |
| `opacity` | przezroczystość |
| `background-image`, `-repeat`, `-position` | obraz tła, powtarzanie, pozycja |
| `background-size: cover` | dopasowanie tła |
| `background-attachment: fixed` | tło nieruchome przy przewijaniu |
| `border` | obramowanie (`solid`, `dashed`) |
| `border-radius` | zaokrąglenie rogów |
| `margin` / `padding` | margines zewnętrzny / wewnętrzny |
| `text-align` | wyrównanie tekstu |
| `font-family`, `font-weight`, `font-style` | krój, grubość, kursywa |
| `text-decoration` | dekoracja (np. usunięcie podkreślenia linku) |
| `list-style-type: none` | usunięcie punktorów |
| `transition` | czas przejścia efektu |

## Model pudełkowy i `display`

Każdy element to prostokąt: **content → padding → border → margin**.

| Wartość `display` | Zachowanie |
|---|---|
| `block` | zajmuje całą szerokość, zaczyna się od nowej linii |
| `inline` | w linii z tekstem, ignoruje szerokość/wysokość |
| `inline-block` | w linii, ale respektuje wymiary |
| `flex` / `grid` | nowoczesne układy (flexbox, siatka) |
| `none` | element ukryty: nie zajmuje miejsca i znika też dla czytników ekranu |

Inne sposoby ukrywania mają inne skutki w testach: `visibility: hidden` zostawia puste miejsce, a `opacity: 0` zostawia element klikalny i dostępny z klawiatury. Narzędzia do automatyzacji traktują każdy z nich inaczej, np. zgłaszają, że element jest niewidoczny albo zasłonięty.

## Responsywność

```css
@media (max-width: 768px) {
  .menu { display: none; }
  .hamburger { display: block; }
}
```

!!! bug "Typowy błąd wizualny"
    Przy zwężeniu okna lub obrocie urządzenia **jednocześnie widać menu hamburgerowe i zwykłe menu** albo elementy na siebie nachodzą. Warto to sprawdzać w trybie **Device toolbar** w DevTools lub wtyczką ResolutionTest.
