# 1. API - V

**API** - To interfejs programowania aplikacji. To zestaw protokołów i narzędzi umożliwiających komunikację pomiędzy składnikami oprogramowania i aplikacjami sieciowymi oraz wymianę danych między oddzielnymi systemami. Api dostarcza interfejsu, który określa jak programy mogą się ze sobą komunikować, jakie dane można wymieniać i jak korzystać z udostępnionych funkcji.  Łatwo umożliwiają integracje, rozszerzalność oraz gotowe funkcje dzięki czemu nie trzeba ich pisać od nowa. Umożliwia pobranie danych np. bazy danych czy serwisów.

---

## 1.1. Cykl życia API - V

**Cykl życia API** - to proces obejmujący wszystkie etapy tworzenia i utrzymania API, od projektowania i implementacji, przez testowanie oraz wdrożenie, aż po monitorowanie, rozwój i utrzymanie kolejnych wersji interfejsu.

---

## 1.2. Klient API - V

**Klient API** - to narzędzie lub aplikacja umożliwiająca wysyłanie żądań do API oraz odbieranie odpowiedzi z serwera. Klient API ułatwia testowanie, debugowanie oraz analizowanie działania interfejsów API. Np. Postman i Insomnia.

---

## 1.3. Dokumentacja API - V

**Dokumentacja API** - zbiór informacji opisujących sposób korzystania z API oraz jego integracji z innymi systemami. Zawiera m.in. dostępne endpointy, metody, parametry, sposób autoryzacji oraz przykłady zapytań i odpowiedzi.

---

## 1.4. Jak działa API? - V

API (Application Programming Interface) umożliwia komunikację między aplikacjami, systemami lub urządzeniami poprzez wymianę danych. Działa na zasadzie modelu żądanie → odpowiedź (request → response).

#### 1. Klient API wysyła żądanie

Proces rozpoczyna klient API, np. aplikacja mobilna, strona internetowa lub inny system. Żądanie może zostać wywołane przez działanie użytkownika, np. kliknięcie przycisku „Zaloguj”, wyszukanie produktu lub pobranie danych.

#### 2. Żądanie API (API Request)

Żądanie wysyłane do serwera API zazwyczaj zawiera:

- Endpoint - adres URL wskazujący konkretny zasób lub funkcję API, np. /users lub /orders.
- Metodę HTTP - określa rodzaj operacji
- Parametry - dodatkowe informacje przekazywane do API, np. identyfikator użytkownika lub filtr wyszukiwania.
- Nagłówki (Headers) - dane techniczne, np. typ danych lub token autoryzacyjny.
- Body (treść żądania) - dane przesyłane do serwera, np. formularz rejestracyjny w formacie JSON.

#### 3. Serwer API przetwarza żądanie

Serwer API odbiera żądanie i wykonuje odpowiednie operacje, takie jak:

- weryfikacja użytkownika,
- walidacja danych,
- komunikacja z bazą danych,
- przetworzenie logiki biznesowej,
- przygotowanie odpowiedzi.

#### 4. API zwraca odpowiedź

Po przetworzeniu żądania serwer odsyła odpowiedź do klienta. Odpowiedź zwykle zawiera:

- Kod statusu HTTP - informację o wyniku operacji,
- Response Headers - dodatkowe informacje techniczne.
- Response Body - właściwe dane lub komunikat błędu.

---

## 1.5. Typy API - V

- **Private API** - nazywane również Internal API, to interfejsy dostępne wyłącznie wewnątrz organizacji. Służą do komunikacji pomiędzy wewnętrznymi systemami, aplikacjami lub usługami firmy.


- **Public API** - interfejsy udostępniane zewnętrznym użytkownikom oraz developerom. Umożliwiają integrację aplikacji z usługami lub funkcjonalnościami dostępnymi publicznie.

- **Partner API** - interfejsy udostępniane wybranym partnerom biznesowym. Dostęp do nich jest ograniczony i wymaga odpowiedniej autoryzacji lub umowy pomiędzy organizacjami.

---

# 2. Rodzaje API

## REST API - V
- REST API to interfejs programistyczny oparty na architekturze REST (Representational State Transfer), wykorzystywany do komunikacji pomiędzy klientem a serwerem przy użyciu protokołu HTTP.
- Komunikacja w REST API odbywa się najczęściej z wykorzystaniem formatów JSON lub XML, jednak JSON jest obecnie najpopularniejszym standardem.
- REST API wykorzystuje standardowe metody HTTP do wykonywania operacji na zasobach, takie jak GET, POST, PUT, PATCH oraz DELETE.
- Każdy zasób w REST API posiada unikalny adres URL zwany endpointem.
- REST API jest bezstanowe (stateless), co oznacza, że każde żądanie zawiera wszystkie informacje potrzebne do jego obsługi, a serwer nie przechowuje informacji o poprzednich żądaniach klienta.
- Dane przesyłane pomiędzy klientem a serwerem mogą znajdować się w nagłówkach HTTP, parametrach zapytania, ścieżce URL lub body requestu.
- REST API jest często wykorzystywane w aplikacjach webowych, mobilnych oraz systemach opartych na mikroserwisach.
- Dzięki swojej prostocie, wydajności oraz łatwej integracji REST API jest obecnie najpopularniejszym typem API.

---

## SOAP API - V

- SOAP API to interfejs oparty na protokole SOAP (Simple Object Access Protocol), wykorzystywany do wymiany danych pomiędzy aplikacjami.
- SOAP API korzysta głównie z formatu XML do przesyłania wiadomości pomiędzy klientem a serwerem.
- Komunikacja w SOAP opiera się na ściśle określonych zasadach oraz standardach definiujących strukturę wiadomości i sposób wymiany danych.
- SOAP może działać z wykorzystaniem różnych protokołów transportowych, takich jak HTTP, SMTP czy FTP.
- Każda wiadomość SOAP posiada określoną strukturę XML zawierającą informacje o żądaniu, odpowiedzi oraz dodatkowych metadanych.
- SOAP wykorzystuje WSDL (Web Services Description Language), czyli dokument opisujący dostępne operacje API, parametry oraz typy danych.
- Dzięki ścisłej standaryzacji SOAP API zapewnia wysoki poziom bezpieczeństwa, niezawodności oraz integralności danych.
- SOAP API jest często wykorzystywane w systemach enterprise, bankowości, systemach finansowych oraz integracjach wymagających wysokiego poziomu bezpieczeństwa.
- W porównaniu do REST API SOAP jest bardziej rozbudowany, bardziej restrykcyjny oraz zwykle trudniejszy w implementacji i utrzymaniu.


## GraphQL

## gRPC



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

## Typowe błędy znajdowane podczas testowania API - V

- **Nieprawidłowy format danych** - API może zwracać dane w niepoprawnym formacie lub zawierać błędne wartości. Problemy mogą dotyczyć:
    - niepoprawnej struktury JSON lub XML,
    - innego oczekiwanego formatu np. JSON zamiast XML,
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

- **Problemy z dokumentacją API** - Nieaktualna lub niekompletna dokumentacja API może utrudniać integrację oraz testowanie systemu. Najczęstsze problemy:
    - brak opisanych endpointów,
    - nieaktualne przykłady requestów,
    - brak informacji o parametrach,
    - niespójność dokumentacji z rzeczywistym działaniem API.
- **Problemy z kompatybilnością wersji API** - Zmiany w nowych wersjach API mogą powodować problemy z działaniem istniejących aplikacji lub integracji korzystających ze starszych wersji interfejsu. Może to prowadzić do:
    - błędów integracji,
    - problemów z kompatybilnością,
    - uszkodzenia funkcjonalności aplikacji.
- **Luki bezpieczeństwa** - Testowanie API pomaga wykrywać podatności bezpieczeństwa mogące prowadzić do wycieku danych lub nieautoryzowanego dostępu do systemu. Najczęstsze zagrożenia:
    - SQL Injection,
    - Cross-Site Scripting (XSS),
    - brak szyfrowania danych,
    - ujawnianie wrażliwych informacji,
    - brak limitowania liczby żądań.

- **Niepoprawna konfiguracja CORS** - Błędna konfiguracja mechanizmu CORS może powodować problemy z komunikacją pomiędzy frontendem a API. Może to skutkować:
    - blokowaniem żądań między domenami,
    - problemami bezpieczeństwa,
    - błędnym działaniem aplikacji frontendowej.

- **Problemy ze współbieżnością** - W przypadku wielu jednoczesnych żądań mogą pojawić się problemy związane z równoczesnym dostępem do danych. Najczęstsze problemy:
    - nadpisywanie danych,
    - duplikacja rekordów,
    - race conditions,
    - nieprzewidywalne działanie aplikacji.
- **Problemy z integracją systemów** - API często komunikuje się z innymi aplikacjami, usługami lub bazami danych. Problemy integracyjne mogą powodować:
    - niespójność danych,
    - błędne działanie procesów biznesowych,
    - problemy z komunikacją między systemami.


    
## Wyzwania podczas testowania API

## Najlepsze praktyki testowania API

- **Utworzenie dedykowanego środowiska testowego** - testy należy przeprowadzać na dedykowanym środowisku testowym (odzwierciedlającym warunki produkcyjne i zawierajacym dane pozorowane) przed wdrożeniem zmian na środowisku produkcyjnym
- **Automatyzacja testów** - dzięki niej można ograniczyć występowanie błędu ludzkiego oraz możliwe jest wyliczenie pokrycia 
- **Wykonywanie testów przez cały cykl życia API** - pozwala identyfikować i rozwiązywać problemy tak szybko jak jest to możliwe.
- **Tworzenie testów wielokrotnego użytku** - pomimo, że kazdy endpoint powinien być testowany indywidulanie, to mogąistnieć uniwersalne regóły np. 
    - Każda odpowiedź na żądanie musi być w określonym czasie, 
    - wszystkie odpowiedzi w formacie JSON
- **Odpowiednia organizacja testów** - oznaczanie testów zgodnie z przeznaczeniem i ich grupowanie. Oddzielne zestawy testów dla każdego zasobu API i odzielnie testy jednostkowe od testów kompleksowych. Pomaga to uniknąć duplikowania testów.


# Monitorowanie API

## Monitoring API i Testing API

Mają one wspólny cel jakim jest zapewnienie niezawodności i wydajności API. Jednakże są przeprowadzane w różnych atapach SDLC.

## Logi API

## Metryki API