# Czym jest testowanie?

Testowanie to proces oceny jakości oprogramowania poprzez wykrywanie błędów oraz weryfikację, czy system spełnia określone wymagania.

# Cel testowania

Podstawowym celem testowania oprogramowania jest budowanie zaufania do jakości produktu oraz zapobieganie awariom dzięki wczesnemu wykrywaniu niezgodności w procesie wytwarzania. Obejmuje ono ocenę i weryfikację produktów pracy, takich jak wymagania, projekt i kod, a także sprawdzenie spełnienia zobowiązań wynikających z umów, standardów, prawa i oczekiwań interesariuszy. Istotnym zadaniem testowania jest wykrywanie defektów i zagrożeń oraz dostarczanie rzetelnych informacji wspierających świadome decyzje dotyczące systemu.

# Podstawowe pojęcia

- Błąd (error) – pomyłka człowieka prowadząca do powstania defektu w kodzie.
- Defekt (defect/bug) – nieprawidłowość w kodzie lub działaniu programu.
- Awaria (failure) – efekt działania defektu w czasie wykonania.(zdarzenie, w którym moduł lub system nie wykonuje wymaganej funkcji w określonym zakresie)

# Zasady testowania (ISTQB)

1.	Testowanie ujawnia obecność błędów, nie ich brak.
2.	Pełne testowanie jest niemożliwe.
3.	Wczesne testowanie oszczędza czas i koszty.
4.	Defekty koncentrują się w określonych obszarach systemu.
5.	Paradoks pestycydów – te same testy przestają wykrywać nowe błędy, trzeba je regularnie aktualizować.
6.	Testowanie zależy od kontekstu (np. testy systemów medycznych różnią się od testów gier).
7.	Brak błędów nie oznacza, że system jest użyteczny lub spełnia potrzeby użytkownika.

# Modele cyklu życia oprogramowania

- Sekwencyjne - zakładają wykonanie poszczególnych czynności wytwórczych po kolei liniowo. Nowa faza nie może rozpocząć się dopóki nie skończy się poprzednia.
    - kaskadowy (waterfall) - czynności testowe starują gdy wszystkie inne czynności wytwórcze zostaną ukończone. Model ten stosowany jest gdy jest bardzo dokładna dokumentacja i znane wymagania, które się nie zmienią.
    - Model V – w przeciwieństwie do kaskadowego wprowadza zasadę wczesnego testowania. Testowanie następuje w każdej fazie.
- Iteracyjno-przyrostowe  - oprogramowanie wytwarzane jest w krótkich cyklach. Funkcjonalności rosną przyrostowo  
    - RUP – elastyczna struktura procesów, w której definiuje się poszczególne procesy. Procesy te dostosowuje się do potrzeb projektu. Poszczególne iteracje trwają długo(2-3 miesiące) 
    - SCRUM – najpopularniejszy. Dzieli wytwarzanie oprogramowania na krótkie iteracje(sprinty) o tej samej długości. Częste zmiany.  Dlatego testowanie staje się wyzwaniem więc zamiast długotrwałego planowania stosuje się testowanie eksploracyjne czy automatyzowanie dużych ilości testów zwłaszcza testów regresji
    - Kanban – nie narzuca stałych iteracji czasowych. Proces wytwórczy organizowany jest w oparciu o wizualne karty zadań na tablicy oraz limity pracy w toku (WIP). Kolejne funkcjonalności przekazywane są do produkcji w miarę ich ukończenia, gdy pojawi się na nie zapotrzebowanie. Metoda ta kładzie nacisk na płynność przepływu, szybkie wykrywanie wąskich gardeł i elastyczne reagowanie na zmiany priorytetów.
    - Model spiralny Boehma – jest to model modeli dlatego, że można uzyskać z niego każdy model cyklu życi. Przed każdym kolejnym cyklem produkcyjnym jest azaliza ryzyka.. Tworzy się w nim eksperymentalne elementy przyrostowe, które mogą być przebudowane a nawet porzucone w dalszych etapach.

# Poziomy testów

- Testy jednostkowe/modułowe (Unit tests) – testują małe fragmenty kodu, wykonywane przez programistów.
- Testy integracyjne – sprawdzają współpracę między modułami lub systemami.
- Testy systemowe – obejmują test całej aplikacji jako całości.
- Testy akceptacyjne – weryfikują zgodność z oczekiwaniami klienta lub użytkownika. Można je również podzielić ze względu na miejsce wykonywania:
    - Alfa – w siedzibie producenta w środowisku testowym
    - Beta – testowanie przez klienta na własnym środowisku docelowym 

# Cykl życia defektu (Defect Life Cycle)

Now → Assigned → Fixed → Retested → Closed (czasem: Reopened → Retested → Closed)

# Rodzaje testów

Ze względu czy kod jest uruchamiany w trakcie testu:
- Statyczne – testowanie można wykonać bez konieczności uruchamiania testowanego obiektu.(testowane specyfikacje, projektu architektury czy kod oprogramowania)
Zalety: wczesne testowanie
    - Analiza statyczna
    - Przegląd  
        - Inspekcja
        - Przegląd techniczny
        - Przejrzenie
        - Przegląd nieformalny
- Dynamiczne – testowanie może wymagać uruchomionego modułu lub systemu. Np. Aplikacji internetowej uruchomionej na środowisku testowym.

Ze względu na cel:
- Funkcjonalne – sprawdzają czy system działa zgodnie z wymaganiami, czyli co system robi.
Przykład: logowanie, wyszukiwanie produktu, walidacja formularza.
- Niefunkcjonalne – badają jak system działa, czyli jego jakość, wydajność, bezpieczeństwo, użyteczność.
Przykład: testy wydajnościowe, bezpieczeństwa, obciążeniowe.

Ze względu na podejście:
- Czarnoskrzynkowe (Black-box) – tester nie zna kodu, testuje na podstawie specyfikacji i interfejsu użytkownika.
Przykład: test logowania z poprawnymi i błędnymi danymi.
- Białoskrzynkowe (White-box) – tester zna strukturę kodu i testuje jego wewnętrzną logikę.
Przykład: testowanie warunków logicznych, ścieżek w kodzie (unit testy).
- Bazujace na doświadczeniu -> nie bazuje na dokumencie formalnym

Ze względu na sposób wykonania:
- Manualne – tester wykonuje testy ręcznie, krok po kroku, bez użycia skryptów.
Dobre dla testów eksploracyjnych, UX, walidacji funkcjonalności.
- Automatyczne – testy wykonywane są przez skrypty lub narzędzia (np. Selenium, Postman, Jenkins).
Stosowane przy testach regresyjnych i powtarzalnych.

Testy związane ze zmianami:
- Potwierdzające – retesty stosuje się je zawsze po naprawie defektu. Czy defekt został rzeczywiści naprawiony
- Regresyjne – upewniają się, że nowa zmiana nie zepsuła istniejących funkcji. Często się je automatyzuje.

Przykładowe typy testów
- Smoke tests – szybka weryfikacja, czy aplikacja działa po wdrożeniu, czy główne funkcje działają (czy „się uruchamia”).
- Sanity tests – sprawdzenie, czy konkretna poprawka działa zgodnie z oczekiwaniami.
- Eksploracyjne – tester spontanicznie bada aplikację bez gotowych przypadków testowych, szukając nieoczywistych błędów.
- Pielęgnacyjne – testy po wydaniu oprogramowania do użytku.

# Proces przeglądu produktów pracy

1.	Planowanie
2.	Rozpoczęcie przeglądu
3.	Przegląd indywidualny
4.	Przekazanie informacji o problemach i analiza problemów
5.	Usunięcie defektów i raportowanie

# Proces testowy (wg ISTQB)

1.	Planowanie testów  -> plan testów(cel, podejście, techniki, harmonogram)
2.	Monitorowanie testów  -> raporty z testów(oszacowanie jakości modułu na podstawie rezultatów, czy konieczne dalsze testy, sprawdzenie rezultatów)
3.	Analiza testów -> warunki testowe (analiza specyfikacji, diagramów, wymagań)
4.	Projektowanie testów -> Przypadki testowe, zbiory testów
5.	Implementacja testów -> tworzenie zestawów testowych, przygotowanie danych tetsowych
6.	Wykonywanie testów ->dokumentacja (wykonanie testów), raport o defektach
7.	Ukończenie testów -> koniec

# Role w przeglądzie formalnym

1.	Autor
2.	Kierownictwo
3.	Facylitator(moderator) – rola mediatora
4.	Lider przeglądu
5.	Przeglądający
6.	Protokolant

# Weryfikacja a walidacja

- Weryfikacja (Verification) – czy system jest zbudowany zgodnie ze specyfikacją („czy robimy to dobrze?”).
- Walidacja (Validation) – czy system spełnia potrzeby użytkownika („czy robimy to, czego oczekuje klient?”).

# Przypadek testowy

- Nazwę testu
- Warunki wstępne
- Kroki do wykonania
- Dane wejściowe
- Oczekiwany rezultat
- Rzeczywisty rezultat
- Status (pass/fail)

# Raport z błędu (bug report)

- Identyfikator
- Tytuł
- Opis
- Data zgłoszenia
- Autor
- Priorytet
- Status zgłoszenia
- Identyfikacje elementu testowego
- Kroki do odtworzenia
- Rzeczywisty rezultat
- Oczekiwany rezultat
- Faza cyklu zycia oprogramowania
- Załączniki (np. screeny, logi, video)

# Techniki projektowania przypadków testowych
- Podział na klasy/zakresy równoważności – np. pole „wiek”: <0 (błędne), 0–120 (poprawne), >120 (błędne).
- Analiza wartości brzegowych – testowanie granicznych wartości danych.
- Tablice decyzyjne – sprawdzanie różnych kombinacji warunków i akcji.
- Testy oparte na scenariuszach (Use case) – testowanie pełnych ścieżek użytkownika.

# Specyfikacja wymagań
Specyfikacja to dokument w którym zawarto wszystkie oczekiwania funkcjonalne i niefunkcjonalne stawiane systemowi. SRS i BRS różnia się ale są powiazane
- SRS- specyfikacja wymagań oprogramowania 
- BRS- specyfikacja wymagań biznesowych 

Zawiera:
- Nazwa produktu
- Imiona i nazwiska jego autorów
- Wersja dokumentu
- Historia zmian
- Spis treści
- Charakterystyka firmy
- Opis przyszłego/aktualnego systemu
- Słownik pojęć
- Opis wymagań funkcjonalnych
- Opis wymagań niefunkcjonalnych
- Lista wymagań z priorytetyzacją i use-case
- Model systemu


# Dodatkowe pojęcia
- Traceability Matrix (RTM) – mapa powiązań między wymaganiami a przypadkami testowymi.
- Test Pyramid – proporcje testów: najwięcej jednostkowych, mniej integracyjnych, najmniej UI.
- Exit Criteria – warunki zakończenia testów (np. 95% przypadków zakończonych sukcesem, brak krytycznych defektów).

---
- Analiza wartości brzegowych itd. W którym poziomie testów
- ATTD ITD. Przypomnieć!
- Rodzaje przglądu !!!!
- Kwadrat testowy
- Jakie narzędzia w jakiej  czynności testowej
- Śledzenie powiązań!!!
