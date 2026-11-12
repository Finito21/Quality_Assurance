---
description: "Jenkins: a Jenkinsfile pipeline, test stages, JUnit reports and integration with test tools."
---

# Jenkins

**Jenkins** is an open-source **CI/CD** server (Continuous Integration / Continuous Delivery) for automating development and testing processes. It runs as a server that **reacts to code changes**: it builds the application, runs tests (unit, integration, E2E) and deploys new versions.

## CI vs CD

- **Continuous Integration**: every change in the repo is automatically built and tested.
- **Continuous Delivery**: the application is always ready to be deployed (deployment after approval).
- **Continuous Deployment**: a change that passes the tests goes to production automatically.

## Use in a tester's work

- automatically running **Selenium / Cypress / API (Newman)** tests after every deployment or commit,
- generating test **reports** (JUnit, Allure, HTML),
- notifications about results (**Slack**, e-mail),
- integration with **Git, Docker, Kubernetes, Jira**,
- nightly (scheduled) runs of the full regression suite.

## Pipeline as code (Jenkinsfile)

```groovy title="Jenkinsfile"
pipeline {
    agent any

    triggers { cron('H 2 * * *') }   // every day at about 2:00

    stages {
        stage('Checkout') {
            steps { git branch: 'main', url: 'https://github.com/org/project.git' }
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
        failure { slackSend channel: '#qa', message: "Tests are failing: ${env.BUILD_URL}" }
    }
}
```

## Concepts

| Concept | Description |
|---|---|
| **Job / Project** | a defined task to execute |
| **Pipeline** | a sequence of stages described in a `Jenkinsfile` |
| **Build** | a single run of a job |
| **Agent / Node** | the machine that runs the build |
| **Plugin** | an extension (Git, Slack, Allure, Docker…) |
| **Artifacts** | output files kept after a build (reports, screenshots) |
