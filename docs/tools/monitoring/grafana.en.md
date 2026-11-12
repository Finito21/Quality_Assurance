---
description: "Grafana for testers: dashboards and panels, watching performance test results live, monitoring test environments and analysing logs."
---

# Grafana

**Grafana** is an open-source platform for **data visualisation and analysis**. It runs on a server, reads data from various sources and presents it as dashboards.

!!! note "Visualisation, not data collection"
    Grafana itself **does not collect metrics**. It reads them from data sources (Prometheus, InfluxDB, Loki, SQL databases…). For databases, queries are usually written in **SQL**.

## Key concepts

| Concept | Description |
|---|---|
| **Data source** | where data comes from: Prometheus, InfluxDB, MySQL/PostgreSQL, Elasticsearch, Loki |
| **Dashboard** | a set of panels on one screen |
| **Panel** | a single visualisation: chart, table, counter, heatmap |
| **Query** | a query to the data source (SQL, PromQL, InfluxQL) |
| **Variables** | dashboard parameters, e.g. choosing the environment or server |
| **Alerting** | notifications when thresholds are exceeded (Slack, e-mail) |

## Grafana in a tester's work

- **live performance test results**: JMeter / k6 → InfluxDB → Grafana (response times, RPS, errors),
- monitoring test environments (CPU, RAM, application errors),
- a **quality** dashboard: number of tests, pass rate, pipeline duration,
- analysing logs (Loki) when looking for the cause of a failure.

```sql
-- sample panel: average API response time over time
SELECT $__timeGroup(created_at, '1m') AS time,
       AVG(response_ms) AS avg_response
FROM api_requests
WHERE $__timeFilter(created_at)
GROUP BY 1
ORDER BY 1;
```
