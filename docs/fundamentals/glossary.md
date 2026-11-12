---
description: "Słownik pojęć testowania po polsku i angielsku zgodny z terminologią ISTQB: defekt, awaria, przypadek testowy i inne."
---

# Słownik pojęć

Najczęściej używane pojęcia z testowania, z angielskim odpowiednikiem, który spotkasz w ogłoszeniach, narzędziach i na egzaminie ISTQB. Pełny, oficjalny słownik jest w serwisie [ISTQB Glossary](https://glossary.istqb.org/) (również po polsku).

## Podstawy

| Pojęcie | Po angielsku | Znaczenie |
|---|---|---|
| **Awaria** | failure | widoczny skutek defektu: system nie robi tego, co powinien |
| **Błąd (pomyłka)** | error, mistake | pomyłka człowieka, która prowadzi do defektu |
| **Defekt** | defect, bug | wada w kodzie lub innym produkcie pracy |
| **Przedmiot testów** | test object | to, co jest testowane: moduł, system, dokument |
| **Podstawa testów** | test basis | wszystko, z czego wynikają testy: wymagania, historyjki, projekt |
| **Wyrocznia testowa** | test oracle | źródło oczekiwanego wyniku, np. specyfikacja |
| **Warunek testowy** | test condition | aspekt do sprawdzenia, np. „logowanie zablokowanym kontem” |
| **Przypadek testowy** | test case | warunki wstępne, dane, kroki i oczekiwany wynik jednego testu |
| **Testalia** | testware | wszystkie produkty testowania: plany, przypadki, skrypty, dane, raporty |
| **Weryfikacja** | verification | sprawdzenie zgodności ze specyfikacją |
| **Walidacja** | validation | sprawdzenie, czy produkt spełnia potrzeby użytkownika |

## Rodzaje testów

| Pojęcie | Po angielsku | Znaczenie |
|---|---|---|
| **Test potwierdzający (retest)** | confirmation testing | sprawdzenie, czy naprawiony defekt rzeczywiście zniknął |
| **Test regresji** | regression testing | sprawdzenie, czy zmiana nie zepsuła działających funkcji |
| **Smoke test** | smoke test | szybkie sprawdzenie, czy build nadaje się do dalszych testów |
| **Testowanie statyczne** | static testing | ocena bez uruchamiania kodu, np. przegląd wymagań |
| **Testowanie dynamiczne** | dynamic testing | testy z uruchomionym oprogramowaniem |
| **Testowanie eksploracyjne** | exploratory testing | jednoczesne poznawanie, projektowanie i wykonywanie testów |
| **Testowanie pielęgnacyjne** | maintenance testing | testy systemu już używanego, po zmianach lub migracji |
| **Testy end-to-end (E2E)** | end-to-end testing | sprawdzenie pełnej ścieżki użytkownika przez wszystkie warstwy systemu |

## Proces i zarządzanie

| Pojęcie | Po angielsku | Znaczenie |
|---|---|---|
| **Plan testów** | test plan | cele, zakres, podejście, zasoby i harmonogram testów |
| **Kryteria wejścia / wyjścia** | entry / exit criteria | warunki rozpoczęcia i zakończenia czynności testowej |
| **Pokrycie** | coverage | jaka część elementów (wymagań, kodu) została sprawdzona testami |
| **Ryzyko produktowe** | product risk | ryzyko, że produkt nie spełni potrzeb, np. błędne obliczenia |
| **Ryzyko projektowe** | project risk | ryzyko dla projektu, np. opóźnienia, brak ludzi |
| **Ważność** | severity | jak poważny jest wpływ defektu |
| **Priorytet** | priority | jak pilnie trzeba naprawić defekt |
| **Macierz śledzenia** | traceability matrix | powiązania wymagań z testami i defektami |
| **Raport z ukończenia testów** | test completion report | podsumowanie testów po zakończeniu poziomu lub projektu |
| **Definition of Done (DoD)** | Definition of Done | kryteria, które musi spełnić historyjka, by uznać ją za ukończoną |

## Środowisko i automatyzacja

| Pojęcie | Po angielsku | Znaczenie |
|---|---|---|
| **Środowisko testowe** | test environment | sprzęt, oprogramowanie i dane, na których wykonuje się testy |
| **Build** | build | konkretna, zbudowana wersja aplikacji |
| **Atrapa** | mock | zastępnik komponentu, który dodatkowo sprawdza, czy został wywołany w oczekiwany sposób |
| **Zaślepka** | stub | zastępnik komponentu, który zwraca z góry ustalone odpowiedzi |
| **Niestabilny test** | flaky test | test, który raz przechodzi, a raz nie, bez zmian w kodzie |
| **Lokator** | locator | sposób wskazania elementu strony w teście automatycznym |
| **Potok CI/CD** | pipeline | automatyczny ciąg kroków: budowanie, testy, wdrożenie |
| **Tryb headless** | headless mode | uruchomienie przeglądarki bez okna, np. w CI |
