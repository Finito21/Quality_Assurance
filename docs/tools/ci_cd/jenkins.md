---
description: "Jenkins: pipeline w Jenkinsfile, etapy z testami, raporty JUnit i integracja z narzędziami testowymi."
---

# Jenkins

**Jenkins** to serwer **CI/CD** typu open source (Continuous Integration / Continuous Delivery) do automatyzacji procesów programistycznych i testerskich. Działa jako serwer, który **reaguje na zmiany w kodzie**: buduje aplikację, uruchamia testy (jednostkowe, integracyjne, E2E) i wdraża nowe wersje.

## CI a CD

- **Continuous Integration**: każda zmiana w repo jest automatycznie budowana i testowana.
- **Continuous Delivery**: aplikacja jest zawsze gotowa do wdrożenia (wdrożenie po zatwierdzeniu).
- **Continuous Deployment**: zmiana, która przejdzie testy, trafia na produkcję automatycznie.

## Zastosowanie dla testera

- automatyczne uruchamianie testów **Selenium / Cypress / API (Newman)** po każdym wdrożeniu lub commicie,
- generowanie **raportów** z testów (JUnit, Allure, HTML),
- powiadomienia o wynikach (**Slack**, e-mail),
- integracja z **Git, Docker, Kubernetes, Jira**,
- nocne (cykliczne) uruchomienia pełnej regresji.

## Pipeline jako kod (Jenkinsfile)

```groovy title="Jenkinsfile"
pipeline {
    agent any

    triggers { cron('H 2 * * *') }   // codziennie ok. 2:00

    stages {
        stage('Checkout') {
            steps { git branch: 'main', url: 'https://github.com/org/projekt.git' }
        }
        stage('Install') {
            steps { sh 'npm ci' }
        }
        stage('API tests') {
            steps { sh 'npx newman run tests/api.json -e env/qa.json -r junit --reporter-junit-export results/api.xml' }
        }
        stage('E2E tests') {
            steps { sh 'npx cypress run' }
        }
    }

    post {
        always  { junit allowEmptyResults: true, testResults: 'results/*.xml' }
        failure { slackSend channel: '#qa', message: "Testy nie przechodzą: ${env.BUILD_URL}" }
    }
}
```

## Pojęcia

| Pojęcie | Opis |
|---|---|
| **Job / Project** | zdefiniowane zadanie do wykonania |
| **Pipeline** | ciąg etapów (stages) opisany w `Jenkinsfile` |
| **Build** | pojedyncze uruchomienie joba |
| **Agent / Node** | maszyna wykonująca build |
| **Plugin** | rozszerzenie (Git, Slack, Allure, Docker…) |
| **Artifacts** | pliki wynikowe zachowane po buildzie (raporty, zrzuty) |
