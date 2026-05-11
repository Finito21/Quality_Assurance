# Czym jest API?

## Jak działa API?

## Endpoint

## Request i Response

## Format danych

### JSON

### XML



# Rodzaje API

## REST API

## SOAP API

## GraphQL

## gRPC

## WebSocket API



# HTTP

## Metody HTTP

### GET

### POST

### PUT

### PATCH

### DELETE

## Kody odpowiedzi HTTP

### Kody 2xx

### Kody 3xx

### Kody 4xx

### Kody 5xx

## Nagłówki HTTP



# Autoryzacja i uwierzytelnianie

## Bearer Token

## Basic Auth

## API Key

## OAuth 2.0

## Klucze API

## Tokeny



# Testowanie API

Testowanie API potwierdza, że działa ono zgodnie z oczekiwaniami. Przeprowadza się je w celu zapewnienia niezawodnosci funkcjonalności, bezpieczeństwa i wydajności. Testy mogą być uruchamiane ręcznie lub być zautomatyzowane.

API-first - strategia traktująca API jako najwyzszy priorytet. Aplikacje są konceptualizowane i tworzone jako zbiór usług wewnętrznych i zewnętrznych dostarczanych za pośrednictwem API. Umozliwia ciągłą weryfikacje jakości, kondycji i wydajności endpointów. 

## Korzyści z testowania API

## Rodzaje testów API - V

Istnieje wiele sposobów testowania API, a każdy z nich służy innemu celowi. W praktyce zespoły często łączą różne podejścia, aby stworzyć skuteczną strategię testowania.

### Testy kontraktowe (Contract Testing) - V

Testy kontraktowe sprawdzają, czy API działa zgodnie z ustalonym kontraktem, czyli specyfikacją określającą format zapytań i odpowiedzi. Dzięki nim można upewnić się, że nowe wersje aplikacji nie wprowadzają zmian łamiących ustalone zasady komunikacji między systemami.

### Testy jednostkowe (Unit Testing) - V

Testy jednostkowe API koncentrują się na pojedynczych endpointach. Ich celem jest sprawdzenie, czy endpoint zwraca poprawne odpowiedzi dla określonych danych wejściowych oraz czy prawidłowo obsługuje błędne lub niekompletne żądania.

### Testy end-to-end (E2E Testing) - V

Testy end-to-end (E2E) sprawdzają kompletny przepływ działania aplikacji z wykorzystaniem API - od rozpoczęcia procesu aż do uzyskania końcowego rezultatu. Odwzorowują rzeczywiste działania użytkownika, aby potwierdzić poprawną współpracę wszystkich elementów systemu. Testy te obejmują wykonywanie serii powiązanych operacji i weryfikację, czy cały scenariusz biznesowy przebiega prawidłowo. Mogą wykorzystywać wiele endpointów oraz różnych interfejsów API.

### Testy obciążeniowe (Load Testing) - V

Testy obciążeniowe służą do sprawdzenia, jak API zachowuje się przy dużej liczbie zapytań. Pozwalają ocenić wydajność systemu, czas odpowiedzi oraz stabilność działania pod wysokim obciążeniem.

### Testy bezpieczeństwa (Security Testing) - V

Testy bezpieczeństwa mają na celu wykrywanie podatności i zagrożeń związanych z API. Obejmują m.in. sprawdzanie ochrony przed nieautoryzowanym dostępem, atakami typu injection czy wyciekami danych.

### Testy integracyjne (Integration Testing) - V

Testy integracyjne sprawdzają współpracę API z innymi komponentami systemu. Ich zadaniem jest potwierdzenie poprawnej wymiany danych i komunikacji pomiędzy usługami lub modułami aplikacji.

### Testy funkcjonalne (Functional Testing) - V

Testy funkcjonalne weryfikują, czy API realizuje wymagania biznesowe i działa zgodnie ze specyfikacją. Polegają na wysyłaniu określonych żądań oraz porównywaniu rzeczywistych wyników z oczekiwanymi rezultatami.


## Co testujemy w API?

## Typowe błędy znajdowane podczas testowania API

- **Nieprawidłowy format danych** - API może zwracać dane w niepoprawnym formacie lub zawierać błędne wartości. Problemy mogą dotyczyć:
    - niepoprawnej struktury JSON lub XML,
    - brakujących pól,
    - błędnych typów danych,
    - niepoprawnych wartości.
-  **Nieprawidłowe kody odpowiedzi HTTP** - API może zwracać niewłaściwe statusy HTTP, które nie odpowiadają rzeczywistemu rezultatowi operacji. Przykładowo:
    - 200 OK mimo wystąpienia błędu,
    - 500 Internal Server Error przy błędzie walidacji danych,
    - brak 404 Not Found dla nieistniejącego zasobu.
- **Problemy z autoryzacją i uwierzytelnianiem** - Błędy związane z bezpieczeństwem API należą do najczęstszych i najgroźniejszych problemów. Problemy mogą obejmować:
    - brak wymaganej autoryzacji,
    - możliwość dostępu bez tokena,
    - wygasłe lub niepoprawnie obsługiwane tokeny,
    - niewłaściwe uprawnienia użytkowników.
- **Brak walidacji danych wejściowych** - API powinno poprawnie walidować dane przesyłane przez użytkownika. Brak odpowiedniej walidacji może prowadzić do błędów aplikacji lub luk bezpieczeństwa. Przykładowo:
    - możliwość przesłania pustych wartości,
    - akceptowanie zbyt długich danych,
    - brak sprawdzania wymaganych pól,
    - możliwość wykonania SQL Injection.
- **Problemy z wydajnością** - API może działać poprawnie funkcjonalnie, ale nie radzić sobie pod większym obciążeniem. Przykładowo:
    - długi czas odpowiedzi,
    - timeouty,
    - przeciążenie serwera,
    - spadek wydajności przy wielu użytkownikach.
- **Problemy ze skalowalnością** - Niektóre API działają poprawnie przy małej liczbie żądań, ale tracą stabilność przy większym ruchu. Może to prowadzić do:
    - błędów serwera,
    - utraty danych,
    - niedostępności usługi.

    
## Wyzwania podczas testowania API

## Najlepsze praktyki testowania API



# Monitorowanie API

## Monitoring API i Testing API

Mają one wspólny cel jakim jest zapewnienie niezawodności i wydajności API. Jednakże są przeprowadzane w różnych atapach SDLC.

## Logi API

## Metryki API