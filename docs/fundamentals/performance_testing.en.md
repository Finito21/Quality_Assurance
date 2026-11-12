---
description: "Performance testing: types (load, stress, soak), metrics, planning and analysing the results."
---

# Performance testing

**Performance tests** check how the system handles load, scaling, response time and processing large amounts of data. They help find weak points **before** users do and avoid failures in production. Large load tests are usually run before a release or before scaling the infrastructure, but in line with shift left, short performance checks are worth running earlier and regularly, e.g. in [CI/CD](../tools/ci_cd/github_actions.md).

## Types of tests

| Type | Question it answers |
|---|---|
| **Performance** | What are the response time and throughput under typical traffic? |
| **Load** | Can the system handle the expected maximum load? |
| **Stress** | What happens above normal load? Where is the breaking point and does the system recover? |
| **Spike** | How does the system react to a sudden traffic increase (e.g. the start of a sale)? |
| **Soak / endurance** | Do memory leaks or degradation appear under prolonged load? |
| **Scalability** | Does adding resources increase performance proportionally? |

## Key metrics

- **Response time**: from sending a request to receiving the complete response. The average matters, but above all the **p95 / p99** percentiles: p95 = 500 ms means that 95% of requests took no longer than 500 ms,
- **Latency**: the time waiting for the first byte of the response, without the time to transfer all of it. Tools do not always distinguish the two, so check what exactly they measure,
- **Throughput**: **RPS** (requests per second) or TPS,
- **Error rate**: share of failed responses (e.g. 5xx, timeouts),
- **Number of concurrent users**,
- **Resource usage**: CPU, RAM, I/O, database connections.

!!! tip "What response time is acceptable?"
    Roughly, according to Jakob Nielsen's limits: up to **0.1 s** a response feels instant, up to **1 s** the user notices the delay but keeps their train of thought, and after about **10 s** they lose focus. Specific thresholds are set in the **acceptance criteria** (e.g. *p95 < 500 ms with 1000 concurrent users*).

## Preparing a test

- **Workload model**: which scenarios users perform, in what proportions and with what **think time** between steps. It is best based on production data, e.g. logs or analytics.
- **Ramp-up**: users are added gradually to see at what level the system starts to slow down.
- **Production-like environment**: results from a small test server do not scale linearly to production. If the environment is weaker, document it and scale the thresholds accordingly.
- **Test data**: a realistic database size; an empty database gives overly optimistic results.
- **Monitoring**: collect server and database metrics during the test, e.g. in [Grafana](../tools/monitoring/grafana.md), to find the bottleneck.

## Tools

| Tool | Used for |
|---|---|
| [**Apache JMeter**](../tools/performance/jmeter.md) | creating, running and analysing performance tests (GUI + CLI) |
| **Gatling** | tests as code (Scala/Java/Kotlin), clear HTML reports |
| **k6** | tests written in JavaScript, good integration with CI and Grafana |
| **Locust** | tests written in Python, distributed runs, live view in the browser |
| **Artillery** | scenarios in YAML or JavaScript, also for WebSocket and Playwright |
| **LoadRunner** | commercial solution (OpenText) for large organisations |
| **oha** | lightweight CLI tool for quickly loading a single endpoint |
| [**Grafana**](../tools/monitoring/grafana.md) | dashboards and real-time analysis of results |

## Postman vs JMeter

=== "Postman is not suited for"

    - large-scale performance testing,
    - thousands of parallel requests,
    - measuring RPS / latency / p95 / p99,
    - simulating many users.

=== "JMeter is not suited for"

    - quickly debugging a single request,
    - exploring an API,
    - readable business tests,
    - convenient “developer-style” work.
