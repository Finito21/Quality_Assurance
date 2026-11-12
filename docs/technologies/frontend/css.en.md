---
description: "CSS for testers: selectors, the box model, element visibility and responsiveness, useful for locators and UI tests."
---

# CSS

**CSS (Cascading Style Sheets)** is used to style a page: its look, the layout of elements and **responsiveness**. It uses **selectors** to pick elements, and inside a selector block you write rules made of properties.

```css
.button:hover {
  background-color: #4f46e5;
  border-radius: 8px;
  transition: 0.2s;
}
```

## Selectors

| Selector | Selects | Example |
|---|---|---|
| `element` | all elements of a given type | `p` |
| `.class` | elements with a class | `.btn` |
| `#id` | the element with a given id | `#login` |
| `[attribute]` | elements with an attribute / value | `[data-testid="submit"]` |
| `A B` | descendant B inside A | `div#band h2.w3-wide` |
| `A > B` | direct child | `ul > li` |
| `:hover`, `:nth-child(n)` | pseudo-classes | `a:hover` |

!!! tip "CSS selectors in automation"
    The same selectors are used in Cypress (`cy.get('.btn')`), Selenium (`By.CSS_SELECTOR`) and in JS (`document.querySelector`). You can try them out in the **Elements** tab in DevTools (++ctrl+f++).

## Most commonly used properties

| Property | Description |
|---|---|
| `color`, `background-color` | text / background colour |
| `opacity` | transparency |
| `background-image`, `-repeat`, `-position` | background image, repetition, position |
| `background-size: cover` | fitting the background |
| `background-attachment: fixed` | background stays still while scrolling |
| `border` | border (`solid`, `dashed`) |
| `border-radius` | rounded corners |
| `margin` / `padding` | outer / inner spacing |
| `text-align` | text alignment |
| `font-family`, `font-weight`, `font-style` | typeface, weight, italics |
| `text-decoration` | decoration (e.g. removing a link underline) |
| `list-style-type: none` | removing bullets |
| `transition` | duration of a transition effect |

## Box model and `display`

Every element is a rectangle: **content → padding → border → margin**.

| `display` value | Behaviour |
|---|---|
| `block` | takes the full width, starts on a new line |
| `inline` | flows with the text, ignores width/height |
| `inline-block` | flows inline but respects dimensions |
| `flex` / `grid` | modern layouts (flexbox, grid) |
| `none` | element hidden and invisible to the user |

## Responsiveness

```css
@media (max-width: 768px) {
  .menu { display: none; }
  .hamburger { display: block; }
}
```

!!! bug "A typical visual bug"
    When the window is narrowed or the device is rotated, **both the hamburger menu and the regular menu are visible at the same time**, or elements overlap. It is worth checking this in DevTools **Device toolbar** mode or with the ResolutionTest extension.
