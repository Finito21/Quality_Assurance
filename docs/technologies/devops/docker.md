---
description: "Docker dla testera: obrazy, kontenery, najważniejsze komendy i środowisko testowe w Docker Compose."
---

# Docker

**Docker** to platforma open source do tworzenia, uruchamiania i zarządzania aplikacjami w **kontenerach**. Izoluje środowiska, dzięki czemu aplikacja działa tak samo niezależnie od systemu i konfiguracji serwera, bez problemu typu „u mnie działa”.

## Podstawowe pojęcia

| Pojęcie | Opis |
|---|---|
| **Kontener** | lekkie, izolowane środowisko z aplikacją i jej zależnościami, działa jak proces w systemie |
| **Obraz (image)** | szablon, z którego tworzy się kontenery |
| **Dockerfile** | plik z instrukcjami budowy obrazu (system bazowy, komendy, porty) |
| **Docker Hub** | publiczne repozytorium obrazów (nginx, mysql, python, jenkins…) |
| **Wolumen (volume)** | trwałe miejsce na dane poza cyklem życia kontenera |

## Najważniejsze komendy

| Komenda | Co robi |
|---|---|
| `docker ps` | działające kontenery |
| `docker ps -a` | wszystkie kontenery (także zatrzymane) |
| `docker images` | lista lokalnych obrazów |
| `docker pull <image>` | pobranie obrazu z Docker Huba |
| `docker run <image>` | uruchomienie nowego kontenera |
| `docker stop <id>` | zatrzymanie kontenera |
| `docker rm <id>` / `docker rmi <image>` | usunięcie kontenera / obrazu |
| `docker exec -it <container> bash` | wejście do środka kontenera |
| `docker logs <container>` | logi kontenera |

## Docker Compose

Narzędzie do definiowania i uruchamiania **wielu kontenerów jako jednej aplikacji** (np. aplikacja + baza + cache) w pliku `docker-compose.yml`.

```yaml
services:
  app:
    image: moja-aplikacja:latest
    ports: ["8080:8080"]
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: test
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 10
```

```bash
docker compose up -d     # uruchomienie w tle
docker compose down      # zatrzymanie i usunięcie kontenerów
docker compose down -v   # to samo, plus usunięcie wolumenów (czysta baza)
```

!!! warning "`depends_on` nie czeka na gotowość usługi"
    Samo `depends_on: [db]` czeka tylko na start kontenera, nie na to, aż baza przyjmuje połączenia, co daje niestabilne błędy „connection refused”. Dlatego w przykładzie baza ma `healthcheck`, a aplikacja czeka na `service_healthy`.

## Docker w pracy testera

- szybkie postawienie **środowiska testowego** lub bazy z danymi testowymi,
- uruchamianie testów w powtarzalnym środowisku w CI (np. obraz `cypress/included`),
- **Selenium Grid** w kontenerach do testów na wielu przeglądarkach,
- analiza błędów przez `docker logs` i `docker exec`.
