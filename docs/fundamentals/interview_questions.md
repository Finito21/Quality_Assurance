---
description: "Pytania rekrutacyjne dla testera z przykładowymi odpowiedziami: zasady testowania, techniki, cykl życia defektu, API i SQL."
---

# Pytania rekrutacyjne

Typowe pytania na rozmowie na stanowisko testera (junior / mid) z krótkimi odpowiedziami. Odpowiedź rozwiń, zanim ją przeczytasz: najpierw spróbuj odpowiedzieć sam. Na rozmowie lepiej podać własny przykład z praktyki niż recytować definicję.

## Podstawy

??? question "Czym różni się QA od QC i od testowania?"
    **QA** (zapewnianie jakości) dotyczy procesów i zapobiegania defektom. **QC** (kontrola jakości) dotyczy produktu i wykrywania defektów. **Testowanie** jest główną formą QC. Więcej: [Podstawy QA](qa_fundamentals.md#qm-qa-i-qc).

??? question "Czym różni się błąd, defekt i awaria?"
    Człowiek popełnia **błąd** (pomyłkę), przez który w kodzie powstaje **defekt**. Gdy wadliwy kod zostanie wykonany, może wystąpić **awaria**, czyli widoczny skutek. Nie każdy defekt powoduje awarię.

??? question "Wymień zasady testowania."
    Testowanie ujawnia obecność defektów, a nie ich brak; testowanie gruntowne jest niemożliwe; wczesne testowanie oszczędza czas i pieniądze; defekty się kumulują; testy się zużywają (paradoks pestycydów); testowanie zależy od kontekstu; przekonanie o braku defektów jest błędem. Dobrze dodać przykład do każdej zasady.

??? question "Czym różni się weryfikacja od walidacji?"
    **Weryfikacja**: czy budujemy produkt dobrze, czyli zgodnie ze specyfikacją. **Walidacja**: czy budujemy dobry produkt, czyli taki, którego potrzebuje użytkownik.

??? question "Czym różni się retest od testu regresji?"
    **Retest** (test potwierdzający) sprawdza, czy konkretny naprawiony defekt zniknął. **Test regresji** sprawdza, czy zmiana nie zepsuła innych, wcześniej działających funkcji.

??? question "Czym różni się smoke test od sanity testu?"
    **Smoke test** to szerokie, płytkie sprawdzenie nowego buildu: czy aplikacja się uruchamia i działają główne funkcje. **Sanity test** to wąskie sprawdzenie obszaru, którego dotyczyła zmiana. Oba są szybkie i decydują, czy warto testować dalej.

## Proces i cykl życia

??? question "Opisz proces testowy."
    Planowanie, monitorowanie i nadzór, analiza, projektowanie, implementacja, wykonanie i ukończenie testów. Czynności nie muszą iść po kolei: w Scrumie wszystkie odbywają się w każdym sprincie. Więcej: [Proces testowy](qa_fundamentals.md#proces-testowy).

??? question "Jak wygląda praca testera w Scrumie?"
    Tester jest częścią zespołu. Uczestniczy w refinemencie (pyta o kryteria akceptacji, zgłasza ryzyka), planowaniu, daily i retrospektywie. Testuje historyjki w trakcie sprintu, automatyzuje regresję i dba o spełnienie Definition of Done. Nie czeka z testami do końca sprintu.

??? question "Opisz cykl życia defektu."
    New → Assigned → In Progress → Resolved → Ready for Test → Closed, a jeśli retest się nie powiedzie: Reopened. Zgłoszenie może też zostać odrzucone (Rejected), oznaczone jako duplikat (Duplicate) albo odłożone (Deferred). Więcej: [Cykl życia defektu](test_management.md#cykl-zycia-defektu).

??? question "Czym różni się ważność od priorytetu? Podaj przykład."
    **Ważność** opisuje wpływ defektu, **priorytet** pilność naprawy. Literówka w nazwie firmy na stronie głównej: niska ważność, wysoki priorytet. Awaria rzadko używanego raportu rocznego: wysoka ważność, niski priorytet. Więcej: [Ważność a priorytet](test_documentation.md#waznosc-a-priorytet).

??? question "Co powinien zawierać dobry raport o defekcie?"
    Jednoznaczny tytuł, środowisko i wersję, kroki do odtworzenia, wynik oczekiwany i rzeczywisty, ważność i priorytet, dowody (zrzut ekranu, nagranie, logi). Jeden raport opisuje jeden defekt. Przykład: [Słaby i dobry raport](test_documentation.md#saby-i-dobry-raport).

??? question "Co zrobisz, gdy programista twierdzi, że zgłoszony defekt to nie defekt?"
    Sprawdzę wymaganie lub kryteria akceptacji i jeszcze raz odtworzę problem. Jeśli wymaganie jest niejasne, poproszę o decyzję właściciela produktu lub analityka. Rozmawiam o faktach i wpływie na użytkownika, nie o tym, kto ma rację.

## Techniki testowania

??? question "Jakie znasz techniki projektowania testów?"
    Czarnoskrzynkowe: klasy równoważności, wartości brzegowe, tablice decyzyjne, przejścia między stanami. Białoskrzynkowe: pokrycie instrukcji i gałęzi. Oparte na doświadczeniu: zgadywanie błędów, testowanie eksploracyjne, listy kontrolne. Więcej: [Techniki testowania](test_techniques.md).

??? question "Pole przyjmuje wiek od 18 do 65 lat. Jakie wartości przetestujesz?"
    Klasy równoważności: np. 10 (niepoprawna), 30 (poprawna), 80 (niepoprawna). Wartości brzegowe (wersja 2-wartościowa): 17, 18, 65, 66. Do tego zgadywanie błędów: pole puste, litery, liczba ujemna, ułamek, spacje, bardzo duża liczba.

??? question "Jak przetestujesz długopis (windę, kubek, formularz logowania)?"
    To pytanie sprawdza sposób myślenia, a nie wiedzę. Zacznij od pytań: kto będzie używał, do czego, jakie są wymagania. Potem podziel testy na funkcjonalne (czy pisze), niefunkcjonalne (wygoda, trwałość, bezpieczeństwo), negatywne (upadek, mróz) i graniczne (ostatnia kropla tuszu).

## API, bazy danych i narzędzia

??? question "Jakie znasz metody HTTP i czym różni się PUT od PATCH?"
    GET pobiera, POST tworzy, PUT zastępuje cały zasób, PATCH zmienia jego część, DELETE usuwa. GET, PUT i DELETE są idempotentne: wielokrotne wywołanie daje ten sam stan. Więcej: [HTTP](../technologies/api_testing/http.md).

??? question "Co oznaczają kody 200, 201, 400, 401, 403, 404 i 500?"
    200 OK, 201 utworzono zasób, 400 błędne żądanie, 401 brak uwierzytelnienia, 403 brak uprawnień, 404 nie znaleziono, 500 błąd serwera. Najczęstsza pułapka: 401 a 403.

??? question "Jak przetestujesz endpoint REST?"
    Poprawne żądanie (kod, treść i schemat odpowiedzi, nagłówki), brakujące i błędne pola, nieprawidłowe typy, wartości brzegowe, brak lub zły token, dostęp do cudzych zasobów, czas odpowiedzi. Sprawdzam też, czy dane zapisały się w bazie. Narzędzie: [Postman](../tools/api_testing_tools/postman.md).

??? question "Czym różni się INNER JOIN od LEFT JOIN?"
    INNER JOIN zwraca tylko wiersze dopasowane w obu tabelach. LEFT JOIN zwraca wszystkie wiersze z lewej tabeli, a brakujące dopasowania uzupełnia wartością `NULL`. Przykład na danych: [SQL](../technologies/backend/sql.md#join-y).

??? question "Do czego tester używa DevTools?"
    Zakładka Console do błędów JavaScript, Network do sprawdzania żądań, kodów odpowiedzi i czasów, Elements do podglądu i edycji HTML i CSS, Application do ciasteczek i local storage, tryb urządzenia do testów responsywności. Więcej: [DevTools](../tools/devtools.md).

??? question "Jakich poleceń Git używasz na co dzień?"
    `git clone`, `git status`, `git pull`, `git switch -c` (nowa gałąź), `git add`, `git commit`, `git push`, a przy problemach `git log`, `git diff` i `git restore`. Więcej: [Podstawy Git](../tools/git/git_basics.md).

## Automatyzacja

??? question "Co warto automatyzować, a czego nie?"
    Warto: regresję, smoke testy, testy API, testy z wieloma danymi. Nie warto: testów jednorazowych, często zmieniających się funkcji, oceny użyteczności. Więcej: [Strategia automatyzacji](test_automation_strategy.md).

??? question "Czym jest piramida testów?"
    Model proporcji: najwięcej szybkich testów modułowych, mniej integracyjnych i API, najmniej wolnych testów E2E przez UI. Odwrócona piramida daje wolny i kruchy zestaw testów.

??? question "Czym jest niestabilny (flaky) test i jak sobie z nim radzić?"
    Test, który raz przechodzi, a raz nie, bez zmian w kodzie. Typowe przyczyny to sztywne opóźnienia, zależności między testami i współdzielone dane. Rozwiązania: czekanie na warunek, niezależne dane, stabilne lokatory, kwarantanna i naprawa.

## O sobie

??? question "Dlaczego chcesz zostać testerem?"
    Odpowiedz szczerze i konkretnie: co Cię w testowaniu interesuje, czego już się nauczyłeś (kurs, ISTQB, własne projekty) i jak to pokazujesz. Dobrze mieć przykład defektu, który znalazłeś w prawdziwej aplikacji.

??? question "Jak się uczysz i skąd czerpiesz wiedzę?"
    Wymień konkretne źródła (sylabus ISTQB, dokumentacja narzędzi, kursy, społeczności), projekty do ćwiczeń (np. publiczne aplikacje demo) i co z nich wyniosłeś. Lista źródeł: [Źródła](../resources.md).
