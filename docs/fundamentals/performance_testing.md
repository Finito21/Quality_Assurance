---
description: "Testy wydajnościowe: rodzaje (obciążeniowe, przeciążeniowe, długotrwałe, skokowe), najważniejsze metryki, planowanie testu i analiza wyników."
---

# Testy wydajnościowe

**Testy wydajnościowe** sprawdzają, jak system radzi sobie z obciążeniem, skalowaniem, czasem reakcji i przetwarzaniem dużej ilości danych. Pozwalają wykryć słabe punkty, **zanim** zrobią to użytkownicy, i uniknąć awarii na produkcji. Duże testy obciążeniowe wykonuje się zwykle przed wydaniem lub przed skalowaniem infrastruktury, ale zgodnie z zasadą shift left krótkie testy wydajności warto uruchamiać wcześniej i regularnie, np. w [CI/CD](../tools/ci_cd/github_actions.md).

## Rodzaje testów

| Rodzaj | Pytanie, na które odpowiada |
|---|---|
| **Wydajnościowe (performance)** | Jaki jest czas odpowiedzi i przepustowość przy typowym ruchu? |
| **Obciążeniowe (load)** | Czy system działa poprawnie przy oczekiwanym obciążeniu, od typowego do szczytowego? |
| **Pojemnościowe (capacity)** | Ilu użytkowników lub transakcji system obsłuży, zanim przekroczy dopuszczalne progi? |
| **Przeciążeniowe (stress)** | Co się stanie powyżej normy? Gdzie jest punkt załamania i czy system się podnosi? |
| **Skokowe (spike)** | Jak system reaguje na nagły wzrost ruchu (np. start promocji)? |
| **Wytrzymałościowe (soak / endurance)** | Czy przy długotrwałym obciążeniu nie pojawiają się wycieki pamięci i degradacja? |
| **Skalowalności** | Czy dodanie zasobów proporcjonalnie zwiększa wydajność? |

## Najważniejsze metryki

- **Czas odpowiedzi (response time)**: od wysłania żądania do otrzymania pełnej odpowiedzi. Liczy się średnia, ale przede wszystkim percentyle **p95 / p99**: p95 = 500 ms oznacza, że 95% żądań trwało nie dłużej niż 500 ms,
- **Opóźnienie (latency)**: czas oczekiwania na pierwszy bajt odpowiedzi, bez czasu przesyłania całości. Narzędzia nie zawsze odróżniają te pojęcia, więc warto sprawdzić, co dokładnie mierzą,
- **Przepustowość**: **RPS** (requests per second) lub TPS,
- **Error rate**: odsetek błędnych odpowiedzi (np. 5xx, timeouty),
- **Liczba równoczesnych użytkowników**,
- **Zużycie zasobów**: CPU, RAM, I/O, połączenia do bazy.

!!! tip "Jaki czas odpowiedzi jest akceptowalny?"
    Orientacyjnie, wg progów Jakoba Nielsena: do **0,1 s** reakcja jest odbierana jako natychmiastowa, do **1 s** użytkownik zauważa opóźnienie, ale nie traci wątku, a po około **10 s** traci uwagę. Konkretne progi ustala się w **kryteriach akceptacji** (np. *p95 < 500 ms przy 1000 równoczesnych użytkowników*).

## Przygotowanie testu

- **Model obciążenia**: jakie scenariusze wykonują użytkownicy, w jakich proporcjach, z jakim **czasem namysłu (think time)** między krokami. Najlepiej oprzeć go na danych z produkcji, np. z logów lub analityki.
- **Narastanie obciążenia (ramp-up)**: użytkowników dodaje się stopniowo, aby zobaczyć, przy jakim poziomie system zaczyna zwalniać.
- **Środowisko zbliżone do produkcji**: wyniki z małego serwera testowego nie przenoszą się liniowo na produkcję. Jeśli środowisko jest słabsze, trzeba to opisać i odpowiednio skalować progi.
- **Dane testowe**: realistyczna wielkość bazy danych; pusta baza daje zbyt optymistyczne wyniki.
- **Monitorowanie**: w trakcie testu zbiera się metryki serwerów i bazy, np. w [Grafanie](../tools/monitoring/grafana.md), żeby znaleźć wąskie gardło.

## Narzędzia

| Narzędzie | Do czego |
|---|---|
| [**Apache JMeter**](../tools/performance/jmeter.md) | tworzenie, uruchamianie i analiza testów wydajnościowych (GUI + CLI) |
| **Gatling** | testy jako kod (Scala/Java/Kotlin), czytelne raporty HTML |
| **k6** | testy pisane w JavaScript, dobra integracja z CI i Grafaną |
| **Locust** | testy pisane w Pythonie, rozproszone uruchamianie, podgląd w przeglądarce |
| **Artillery** | scenariusze w YAML lub JavaScript, także dla WebSocket i Playwright |
| **LoadRunner** | rozwiązanie komercyjne (OpenText) dla dużych organizacji |
| **oha** | lekkie narzędzie CLI do szybkiego obciążenia jednego endpointu |
| [**Grafana**](../tools/monitoring/grafana.md) | dashboardy i analiza wyników w czasie rzeczywistym |

## Postman a JMeter

=== "Postman nie nadaje się do"

    - testów wydajnościowych na dużą skalę,
    - tysięcy równoległych requestów,
    - pomiaru RPS / latency / p95 / p99,
    - symulacji wielu użytkowników.

=== "JMeter nie nadaje się do"

    - szybkiego debugowania pojedynczego requestu,
    - eksploracji API,
    - czytelnych testów biznesowych,
    - wygodnej pracy „developerskiej”.
