---
description: "Slack for testers: team and alert channels, notifications from CI, threads and good practice when communicating about defects and releases."
---

# Slack

**Slack** is a communication platform for teamwork: topic channels, direct messages, threads, voice and video calls. It integrates with many tools and lets you receive notifications from them.

## Slack in a tester's work

- quick contact with developers: clarifying requirements, reporting a blocker,
- channels such as `#qa`, `#bugs`, `#deployments`,
- **CI/CD notifications** (Jenkins, GitHub Actions) about test results,
- notifications from [Jira](../test_management/jira.md) about issue status changes,
- monitoring alerts ([Grafana](../monitoring/grafana.md)).

!!! warning "Slack is not a bug tracker"
    A bug reported only in chat is easily lost. Always move what was agreed in the conversation to a Jira issue and add a link to the thread.

!!! danger "Sensitive data"
    Do not send passwords or tokens (e.g. API tokens) in open channels. Use a password or secrets manager.
