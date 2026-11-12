---
description: "Grafana dla testera: dashboardy i panele, wyniki testów wydajnościowych na żywo, monitorowanie środowisk testowych i analiza logów."
---

# Grafana

**Grafana** to platforma open source do **wizualizacji i analizy danych**. Działa na serwerze, odczytuje dane z różnych źródeł i prezentuje je w formie dashboardów.

!!! note "Wizualizacja, nie zbieranie danych"
    Grafana sama **nie zbiera metryk**. Odczytuje je ze źródeł danych (Prometheus, InfluxDB, Loki, bazy SQL…). Przy bazach danych zapytania pisze się zwykle w **SQL**.

## Kluczowe pojęcia

| Pojęcie | Opis |
|---|---|
| **Data source** | źródło danych: Prometheus, InfluxDB, MySQL/PostgreSQL, Elasticsearch, Loki |
| **Dashboard** | zestaw paneli na jednym ekranie |
| **Panel** | pojedyncza wizualizacja: wykres, tabela, licznik, heatmapa |
| **Query** | zapytanie do źródła danych (SQL, PromQL, InfluxQL) |
| **Variables** | parametry dashboardu, np. wybór środowiska lub serwera |
| **Alerting** | powiadomienia po przekroczeniu progów (Slack, e-mail) |

## Grafana w pracy testera

- **wyniki testów wydajnościowych na żywo**: JMeter / k6 → InfluxDB → Grafana (czasy odpowiedzi, RPS, błędy),
- monitorowanie środowisk testowych (CPU, RAM, błędy aplikacji),
- dashboard **jakości**: liczba testów, pass rate, czas wykonania pipeline'ów,
- analiza logów (Loki) przy szukaniu przyczyny awarii.

```sql
-- przykładowy panel: średni czas odpowiedzi API w czasie
SELECT $__timeGroup(created_at, '1m') AS time,
       AVG(response_ms) AS avg_response
FROM api_requests
WHERE $__timeFilter(created_at)
GROUP BY 1
ORDER BY 1;
```
