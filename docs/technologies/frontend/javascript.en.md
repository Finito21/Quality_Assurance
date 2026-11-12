---
description: "JavaScript for testers: variables, types, arrays, functions and the basics needed for Cypress, Playwright and Postman tests."
---

# JavaScript

**JavaScript (JS)** is a scripting language which, together with HTML and CSS, is the foundation of modern websites. It allows you to:

- create and modify content dynamically,
- handle events (clicks, mouse movement, typing),
- validate forms and run animations,
- communicate with the server without reloading the page (AJAX / `fetch`).

!!! tip "JS in a tester's work"
    JavaScript is used to write tests in **Postman** (the *Scripts* tab, *Post-response* section), **Cypress**, Playwright and WebdriverIO. It is also handy in the DevTools console.

## Where does JS run?

- **Client side (browser)**: speeds up the page, takes load off the server, improves UX.
- **Server side (Node.js)**: a runtime outside the browser (APIs, backend, CLI tools). Running a file: `node main.js`.

Linking a script in HTML (usually at the end of `<body>`, so the page loads faster):

```html
<script src="path/to/file.js"></script>
```

## Variables and data types

```javascript
let age = 18;           // value can be changed
const name = "Alice";   // value cannot be reassigned
// var - outdated, not used

let number = 27.34;           // number
let text = "Thomas";          // string
let isAdult = true;           // boolean
let result = null;            // no value
let x;                        // undefined
```

Naming rules: do not start with a digit, no `& + - .` characters, names are case-sensitive (`age ≠ Age`), do not use keywords, use **camelCase**.

## Operators

| Kind | Operators |
|---|---|
| Arithmetic | `+ - * / ** % ++ --` |
| Assignment | `= += -= *= /= **= %=` |
| Comparison | `==` (value), `===` (value **and type**), `!=`, `!==`, `> < >= <=` |
| Logical | `&&` (and), `\|\|` (or), `!` (not) |
| Conditional | `condition ? expr1 : expr2` |

!!! warning "Always `===` instead of `==`"
    `"5" == 5` gives `true`, while `"5" === 5` gives `false`. In assertions, compare both the value and the type.

## Arrays

```javascript
const array = ["Alice", "Thomas", "Alex", 2, true];
array[3];                // 2 (indexing starts at 0)
```

| Method | What it does |
|---|---|
| `.push(x)` / `.pop()` | add / remove at the end |
| `.shift()` | remove from the start |
| `.indexOf(x)` | index of an element (`-1` if missing) |
| `.splice(i, n)` | remove `n` elements starting at index `i` |
| `.join(" ")` | convert to a string with a separator |
| `.reverse()` / `.sort()` | reverse / sort **in place** (they change the original, like `.splice()`); `.sort()` compares as strings by default: `[10, 9, 1].sort()` gives `[1, 10, 9]`, for numbers use `.sort((a, b) => a - b)` |
| `a.concat(b)` | merge arrays |
| `.length` | number of elements (the last index is `length - 1`) |

### `map` and `forEach`

```javascript
const numbers = [10, 42, 50];

const doubled = numbers.map((value, index) => value * 2); // returns a NEW array
numbers.forEach(value => console.log(value));            // returns undefined
```

## Objects

```javascript
const person = {
  name: "Thomas",
  age: 29,
  address: { city: "Rzeszów" }   // nested object
};
person.address.city;  // "Rzeszów"
```

This is the same structure as **JSON** in API responses.

## Conditionals, loops, functions

```javascript
if (age >= 18 && consent) { /* ... */ } else { /* ... */ }

switch (status) {
  case 200: console.log("OK"); break;
  case 404: console.log("Not found"); break;
  default:  console.log("Other code");
}

for (let i = 0; i < 5; i++) { /* ... */ }
for (const el of array) { /* ... */ }

function add(a, b) { return a + b; }
const subtract = (a, b) => a - b;   // arrow function
```

Variables declared inside a function are only available inside it (**local scope**).

## Asynchronous code

Network requests and most actions in test tools are **asynchronous**: they return a promise (`Promise`) whose result you wait for with `await` inside an `async` function.

```javascript
async function getUser(id) {
  const response = await fetch(`/api/users/${id}`);
  const data = await response.json();
  return data;
}
```

!!! warning "A missing `await`"
    Without `await` the test ends before the assertion runs and passes despite the defect. In Playwright every action and every `expect(...)` assertion on a locator needs `await`.

## DOM

The **DOM (Document Object Model)** is a tree representation of an HTML page. It lets JS change any element without reloading the page.

```javascript
const heading = document.querySelector("div#band h2.w3-wide"); // first match
const buttons = document.querySelectorAll(".btn");             // all matches

heading.textContent;                    // read the text
heading.style.color = "red";            // change CSS
heading.classList.add("active");        // add a class
heading.setAttribute("data-x", "1");    // attribute

buttons[0].addEventListener("click", () => alert("Click!"));

const newEl = document.createElement("p");
newEl.textContent = "New paragraph";
document.body.appendChild(newEl);
```

## Classes

Classes are templates for creating objects (**instances**). They contain a **constructor** and **methods**, and can **inherit** from other classes. They are used, among other things, in the **Page Object Model** pattern in automation.

```javascript
class LoginPage {
  constructor(page) { this.page = page; }
  async login(user, pass) { /* ... */ }
}

class AdminLoginPage extends LoginPage { /* inherits the login method */ }
```
