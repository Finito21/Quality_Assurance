---
description: "JavaScript dla testera: zmienne, typy, tablice, funkcje i podstawy potrzebne w testach Cypress, Playwright i Postman."
---

# JavaScript

**JavaScript (JS)** to skryptowy język programowania, który razem z HTML i CSS stanowi podstawę nowoczesnych stron. Pozwala na:

- dynamiczne tworzenie i modyfikowanie treści,
- obsługę zdarzeń (kliknięcia, ruch myszy, wpisywanie tekstu),
- walidację formularzy i animacje,
- komunikację z serwerem bez przeładowania strony (AJAX / `fetch`).

!!! tip "JS w pracy testera"
    W JavaScripcie pisze się testy w **Postmanie** (zakładka *Scripts*, sekcja *Post-response*), **Cypressie**, Playwright i WebdriverIO. Przydaje się też w konsoli DevTools.

## Gdzie działa JS?

- **Po stronie klienta (przeglądarka)**: przyspiesza działanie strony, odciąża serwer, poprawia UX.
- **Po stronie serwera (Node.js)**: środowisko uruchomieniowe poza przeglądarką (API, backend, narzędzia CLI). Uruchomienie pliku: `node main.js`.

Podłączenie skryptu do HTML (zwykle na końcu `<body>`, żeby strona wczytała się szybciej):

```html
<script src="sciezka/do/pliku.js"></script>
```

## Zmienne i typy danych

```javascript
let wiek = 18;          // wartość można zmienić
const imie = "Alicja";  // wartości nie można nadpisać
// var - przestarzałe, nie należy go używać

let liczba = 27.34;           // number
let tekst = "Tomasz";         // string
let czyPelnoletni = true;     // boolean
let wynik = null;             // brak wartości
let x;                        // undefined
```

Zasady nazewnictwa: nazwa nie może zaczynać się od cyfry ani zawierać znaków `& + - .`, wielkość liter ma znaczenie (`wiek ≠ Wiek`), nie można używać słów kluczowych, a zwyczajowo stosuje się **camelCase**.

## Operatory

| Rodzaj | Operatory |
|---|---|
| Matematyczne | `+ - * / ** % ++ --` |
| Przypisania | `= += -= *= /= **= %=` |
| Porównania | `==` (wartość), `===` (wartość **i typ**), `!=`, `!==`, `> < >= <=` |
| Logiczne | `&&` (i), `\|\|` (lub), `!` (negacja) |
| Warunkowy | `warunek ? wyr1 : wyr2` |

!!! warning "Zawsze `===` zamiast `==`"
    `"5" == 5` daje `true`, a `"5" === 5` daje `false`. W asercjach porównuj wartość i typ.

## Tablice

```javascript
const tablica = ["Alicja", "Tomasz", "Olek", 2, true];
tablica[3];              // 2 (indeksowanie od 0)
```

| Metoda | Działanie |
|---|---|
| `.push(x)` / `.pop()` | dodaj / usuń z końca |
| `.shift()` | usuń z początku |
| `.indexOf(x)` | indeks elementu (`-1` gdy brak) |
| `.splice(i, n)` | usuń `n` elementów od indeksu `i` |
| `.join(" ")` | zamiana na string z separatorem |
| `.reverse()` / `.sort()` | odwrócenie / sortowanie **w miejscu** (zmieniają oryginał, tak jak `.splice()`); `.sort()` domyślnie porównuje jako tekst: `[10, 9, 1].sort()` daje `[1, 10, 9]`, dla liczb `.sort((a, b) => a - b)` |
| `a.concat(b)` | łączenie tablic |
| `.length` | liczba elementów (ostatni indeks to `length - 1`) |

### `map` i `forEach`

```javascript
const liczby = [10, 42, 50];

const podwojone = liczby.map((wartosc, index) => wartosc * 2); // zwraca NOWĄ tablicę
liczby.forEach(wartosc => console.log(wartosc));             // zwraca undefined
```

## Obiekty

```javascript
const osoba = {
  imie: "Tomasz",
  wiek: 29,
  adres: { miasto: "Rzeszów" }   // obiekt zagnieżdżony
};
osoba.adres.miasto;  // "Rzeszów"
```

To ta sama struktura co **JSON** w odpowiedziach API.

## Instrukcje warunkowe, pętle, funkcje

```javascript
if (wiek >= 18 && zgoda) { /* ... */ } else { /* ... */ }

switch (status) {
  case 200: console.log("OK"); break;
  case 404: console.log("Nie znaleziono"); break;
  default:  console.log("Inny kod");
}

for (let i = 0; i < 5; i++) { /* ... */ }
for (const el of tablica) { /* ... */ }

function dodaj(a, b) { return a + b; }
const odejmij = (a, b) => a - b;   // funkcja strzałkowa
```

Zmienne zadeklarowane w funkcji są dostępne tylko w niej (**zakres lokalny**).

## Asynchroniczność

Żądania sieciowe i większość akcji w narzędziach testowych są **asynchroniczne**: zwracają obietnicę (`Promise`), na której wynik trzeba poczekać słowem `await` wewnątrz funkcji `async`.

```javascript
async function pobierzUzytkownika(id) {
  const odpowiedz = await fetch(`/api/users/${id}`);
  const dane = await odpowiedz.json();
  return dane;
}
```

!!! warning "Brakujące `await`"
    Bez `await` test kończy się, zanim asercja się wykona, i przechodzi mimo defektu. W Playwright każda akcja i asercja `expect(...)` na lokatorze wymaga `await`.

## DOM

**DOM (Document Object Model)** to drzewiasta reprezentacja strony HTML. Dzięki niemu JS może zmienić dowolny element bez przeładowania strony.

```javascript
const naglowek = document.querySelector("div#band h2.w3-wide"); // pierwszy pasujący
const przyciski = document.querySelectorAll(".btn");            // wszystkie pasujące

naglowek.textContent;                    // pobranie tekstu
naglowek.style.color = "red";            // zmiana CSS
naglowek.classList.add("aktywny");       // dodanie klasy
naglowek.setAttribute("data-x", "1");    // atrybut

przyciski[0].addEventListener("click", () => alert("Klik!"));

const nowy = document.createElement("p");
nowy.textContent = "Nowy akapit";
document.body.appendChild(nowy);
```

## Klasy

Klasy to szablony do tworzenia obiektów (**instancji**). Zawierają **konstruktor** i **metody**, mogą **dziedziczyć** po innych klasach. Wykorzystuje się je m.in. we wzorcu **Page Object Model** w automatyzacji.

```javascript
class LoginPage {
  constructor(page) { this.page = page; }
  async login(user, pass) { /* ... */ }
}

class AdminLoginPage extends LoginPage { /* dziedziczy metodę login */ }
```
