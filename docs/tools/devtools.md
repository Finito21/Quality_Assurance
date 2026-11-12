---
description: "Chrome DevTools dla testera: Elements, Console, Network i Application, emulacja urządzeń i diagnozowanie defektów."
---

# DevTools

**DevTools** to zestaw narzędzi wbudowanych w przeglądarkę, które pozwalają analizować i edytować oglądaną stronę. Ułatwiają diagnozowanie problemów i sprawdzanie implementacji.

Otwieranie: ++f12++ lub ++ctrl+shift+i++ (macOS: ++cmd+option+i++).

## Zakładki

| Zakładka | Do czego służy |
|---|---|
| **Elements** | struktura HTML i style CSS elementów, szukanie lokatorów do automatyzacji |
| **Console** | komunikaty z JS, uruchamianie kodu JS, informacje o błędach |
| **Sources** | publiczne pliki i kod strony, debugowanie JS (breakpointy) |
| **Network** | ruch HTTP: status, adres, metoda, czas, rozmiar, nagłówki, body |
| **Performance** | analiza wydajności renderowania i skryptów |
| **Memory** | analiza zużycia pamięci (wycieki) |
| **Application** | cookies, Local Storage, Session Storage, czyszczenie danych strony |
| **Security** | informacje o certyfikacie SSL/TLS |
| **Lighthouse** | audyt: wydajność, dostępność, SEO, dobre praktyki |
| **Recorder** | nagrywanie i odtwarzanie akcji (prosta automatyzacja, eksport do Puppeteer) |
| **Device toolbar** | symulacja rozdzielczości i urządzeń mobilnych (++ctrl+shift+m++) |

## Console: typy logów

!!! info "Info"
    Informacje o tym, co dzieje się na stronie.

!!! warning "Warnings"
    Coś się nie wczytuje, coś można usprawnić, funkcja będzie wycofana w kolejnej wersji.

!!! failure "Errors"
    Coś poszło nie tak, np. błąd JS albo nieudane żądanie do serwera. **Zawsze warto dołączyć do zgłoszenia defektu.**

## Network w praktyce testera

- podgląd żądań i odpowiedzi API (status code, nagłówki, payload, response),
- **filtrowanie** (Fetch/XHR, JS, CSS, Img) i wyszukiwanie,
- sprawdzanie, jak ładują się zasoby (waterfall) i jak szybko odpowiada serwer,
- **throttling**: spowolnienie internetu (np. *Slow 3G*) albo tryb offline,
- **Preserve log**: zachowanie logów po przeładowaniu i przekierowaniu,
- **Copy as cURL / fetch**: szybkie odtworzenie requestu w terminalu lub Postmanie,
- eksport do pliku **HAR** jako załącznik do zgłoszenia defektu.

## Application: dane przeglądarki

| Magazyn | Czas życia |
|---|---|
| **Local Storage** | trwały, do ręcznego usunięcia |
| **Session Storage** | znika po zamknięciu karty / sesji |
| **Cookies** | zależnie od `Expires` / `Max-Age`, wysyłane z każdym requestem |

**Clear site data** pozwala wejść na stronę „jak nowy użytkownik”.

## Przydatne triki

- ++ctrl+f++ w Elements pozwala testować selektory CSS i XPath,
- ++ctrl+shift+p++ otwiera paletę komend (np. *Capture full size screenshot*),
- prawy klik na elemencie: **Copy → Copy selector / Copy XPath**,
- `$0` w konsoli to aktualnie zaznaczony element.
