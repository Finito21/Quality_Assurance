---
description: "Testy niefunkcjonalne według ISO/IEC 25010: wydajność, bezpieczeństwo, użyteczność, dostępność, kompatybilność i niezawodność."
---

# Testy niefunkcjonalne

Testy funkcjonalne sprawdzają, **co** system robi. Testy niefunkcjonalne sprawdzają, **jak dobrze** to robi: czy jest szybki, bezpieczny, dostępny, wygodny i odporny na awarie. Sylabus CTFL v4.0 opisuje te cechy na podstawie modelu jakości **ISO/IEC 25010**.

## Charakterystyki jakości (ISO/IEC 25010)

| Charakterystyka | Pytanie testera | Przykładowe testy |
|---|---|---|
| **Wydajność** | Czy system odpowiada szybko i wytrzymuje obciążenie? | [testy wydajnościowe](performance_testing.md), obciążeniowe, przeciążeniowe |
| **Kompatybilność** | Czy działa w różnych przeglądarkach i współpracuje z innymi systemami? | testy cross-browser, testy integracji |
| **Interakcja z użytkownikiem** | Czy jest łatwy w nauce, wygodny i dostępny? | testy użyteczności, testy dostępności |
| **Niezawodność** | Czy działa stabilnie i podnosi się po awarii? | testy odtwarzania, testy przełączania awaryjnego (failover) |
| **Bezpieczeństwo** | Czy chroni dane i odpiera ataki? | testy bezpieczeństwa, testy penetracyjne |
| **Utrzymywalność** | Czy łatwo go zmieniać i testować? | analiza statyczna, przeglądy kodu |
| **Elastyczność (przenaszalność)** | Czy da się go zainstalować i przenieść na inne środowisko? | testy instalacji, testy migracji |
| **Bezpieczeństwo użytkowania (safety)** | Czy nie zagraża ludziom i otoczeniu? | testy systemów krytycznych, np. medycznych |

Nazwy pochodzą z wersji normy z 2023 roku. Sylabus CTFL v4.0 opiera się na wersji z 2011 roku, w której zamiast interakcji z użytkownikiem jest **użyteczność**, a zamiast elastyczności **przenaszalność**; nie ma tam też bezpieczeństwa użytkowania. Charakterystyką funkcjonalną jest **przydatność funkcjonalna**, sprawdzana testami funkcjonalnymi.

!!! note "Kiedy testować"
    Testy niefunkcjonalne nie są „na koniec projektu”. Wymagania wydajności, bezpieczeństwa czy dostępności warto ustalić na początku, a sprawdzać je na każdym poziomie testów, także automatycznie w CI.

## Testy bezpieczeństwa

Tester nie musi być pentesterem, ale powinien znać typowe podatności i sprawdzać je w zwykłych testach. Punktem wyjścia są listy **OWASP Top 10** (aplikacje webowe) i **OWASP API Security Top 10**.

| Co sprawdzić | Przykład testu |
|---|---|
| **Kontrola dostępu** | czy po zmianie `id` w URL (`/orders/123` → `/orders/124`) widać cudze zamówienie |
| **Uwierzytelnianie** | blokada po wielu błędnych hasłach, wygasanie sesji, wylogowanie unieważnia token |
| **Walidacja danych wejściowych** | znaki specjalne `' " < >` w polach formularzy nie psują strony ani zapytań do bazy |
| **Ujawnianie informacji** | komunikaty błędów nie pokazują stack trace, wersji serwera ani zapytań SQL |
| **Dane wrażliwe** | hasła i tokeny nie trafiają do logów, URL ani odpowiedzi API |
| **Konfiguracja** | HTTPS wszędzie, nagłówki bezpieczeństwa (`Content-Security-Policy`, `Strict-Transport-Security`) |

Szczegóły dla API: [Uwierzytelnianie i autoryzacja](../technologies/api_testing/authentication.md), [HTTP](../technologies/api_testing/http.md).

!!! warning "Tylko za zgodą"
    Testy bezpieczeństwa wykonuje się wyłącznie na systemach, do których ma się pisemne upoważnienie, najlepiej na środowisku testowym. Skanowanie lub atakowanie cudzych systemów jest nielegalne.

Narzędzia: **OWASP ZAP** i **Burp Suite** (przechwytywanie i modyfikacja ruchu, skanowanie), skanery zależności, np. **Dependabot** lub **Snyk**.

## Testy dostępności

Dostępność (accessibility, a11y) oznacza, że z aplikacji mogą korzystać także osoby z niepełnosprawnościami: niewidome, słabowidzące, niesłyszące, z ograniczeniami ruchowymi. Standardem są wytyczne **WCAG 2.2**, zwykle na poziomie **AA**. W Unii Europejskiej wiele usług cyfrowych musi je spełniać na mocy Europejskiego aktu o dostępności (EAA).

| Co sprawdzić | Jak |
|---|---|
| **Obsługa klawiaturą** | przejście przez całą stronę klawiszem ++tab++, widoczny focus, brak pułapek klawiaturowych |
| **Teksty alternatywne** | obrazki niosące treść mają opis w `alt`, ozdobne mają `alt=""` |
| **Kontrast** | tekst ma kontrast co najmniej 4,5:1 z tłem (duży tekst 3:1) |
| **Formularze** | każde pole ma etykietę, błędy są opisane tekstem, nie tylko kolorem |
| **Struktura** | nagłówki w logicznej kolejności, poprawny atrybut `lang` strony |
| **Czytnik ekranu** | przejście kluczowej ścieżki z NVDA (Windows) lub VoiceOver (macOS, iOS) |
| **Powiększenie** | strona działa przy powiększeniu 200% i na wąskim ekranie |

Narzędzia: **axe DevTools**, **Lighthouse** w [DevTools](../tools/devtools.md), **WAVE**. Automaty wykrywają tylko część problemów, dlatego zawsze uzupełnia się je testem ręcznym.

## Testy użyteczności

Testy użyteczności sprawdzają, czy użytkownicy potrafią **skutecznie, sprawnie i z satysfakcją** wykonać swoje zadania.

- **Testy z użytkownikami**: kilka osób z grupy docelowej wykonuje zadania (np. „kup bilet na jutro”), a obserwator notuje, gdzie się gubią. Już 5 uczestników ujawnia większość poważnych problemów.
- **Ocena heurystyczna**: ekspert sprawdza interfejs według zasad, np. 10 heurystyk Nielsena (widoczny status systemu, zapobieganie błędom, spójność).
- **Ankiety**: np. kwestionariusz SUS po zakończeniu zadań.

## Testy kompatybilności i niezawodności

- **Cross-browser i urządzenia**: macierz przeglądarek, systemów i rozdzielczości ustala się na podstawie danych o użytkownikach. Pomagają [BrowserStack i podobne usługi](../tools/browser_tools.md).
- **Odtwarzanie po awarii**: co się dzieje po restarcie serwera, utracie połączenia z bazą, zerwaniu sieci w trakcie płatności.
- **Testy instalacji i aktualizacji**: czysta instalacja, aktualizacja z poprzedniej wersji, odinstalowanie.
