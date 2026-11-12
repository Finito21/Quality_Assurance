---
description: "Przeglądarki i wtyczki dla testera: testy w wielu przeglądarkach, chmurowe farmy urządzeń i przydatne rozszerzenia."
---

# Przeglądarki i wtyczki

## Testowanie na różnych przeglądarkach

Każda przeglądarka może **różnie interpretować** niektóre elementy (CSS, JS, formularze, czcionki). Podstawowy zestaw:

- Chrome
- Firefox / Firefox Developer Edition
- Edge
- Safari (silnik WebKit, istotny dla iOS)
- Opera

## BrowserStack

Platforma chmurowa do testowania aplikacji webowych i mobilnych na **prawdziwych urządzeniach i przeglądarkach** (pełne możliwości w wersji płatnej). Integruje się z Jirą, GitLabem, Jenkinsem i innymi narzędziami.

| Tryb | Opis |
|---|---|
| **Live** | ręczne testy na wybranej przeglądarce, wersji, systemie i urządzeniu |
| **Automate** | uruchamianie testów automatycznych (Selenium, Cypress, Playwright…) z raportami |
| **Percy** | wizualne testy regresji (porównywanie zrzutów) |

Alternatywa: **TestMu AI** (dawniej LambdaTest).

## Wtyczki dla testera

| Wtyczka | Zastosowanie |
|---|---|
| **Bug Magnet** | gotowe poprawne i niepoprawne dane do formularzy (e-maile, liczby, znaki specjalne) |
| **LT Browser** (TestMu AI, dawniej LambdaTest) | strona na różnych przeglądarkach, systemach i rozdzielczościach, zrzut całej strony |
| **ResolutionTest** | szybkie testy na różnych rozdzielczościach |
| **Bird Eats Bug** | zrzuty i nagrania wraz z **logami konsoli, requestami** i informacjami o systemie |
| **Awesome Screenshot** | zrzuty i nagrania z edycją |
| **Clear Cache** | szybkie czyszczenie pamięci podręcznej |
| **Page Ruler** | mierzenie wymiarów elementów na stronie |
| **Cookie-Editor** | podgląd i edycja ciasteczek |
| **PixelPerfect** | nałożenie projektu graficznego na stronę i porównanie piksel do piksela |

!!! question "Bug Magnet a kreatywność"
    Gotowe zestawy danych przyspieszają pracę, ale **nie zastępują myślenia**. Warto dopisywać własne przypadki wynikające z logiki biznesowej aplikacji.

!!! note "Projekty graficzne"
    Projekty UI najczęściej dostarczane są dziś w **Figmie**. Starsze projekty bywają w plikach `.psd` (Photoshop).

## Zrzuty ekranu i nagrania

=== "PicPick"

    Bezpłatny do użytku prywatnego (komercyjnie płatny). Po zrobieniu zrzutu otwiera edytor (strzałki, tekst, rozmycie).

    - cały ekran, fragment, **przewijana strona** (całość lub fragment),
    - pipeta z kodem koloru (HEX), lupa,
    - linijka w pikselach, współrzędne, kątomierz,
    - nagrywanie ekranu.

=== "ShareX"

    Darmowy i open source (Windows). Zrzuty i nagrania (MP4 lub GIF) pod skrótami klawiszowymi, edycja po zrobieniu zrzutu, automatyczne akcje po zrzucie (np. kopiowanie do schowka).
