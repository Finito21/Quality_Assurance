---
description: "Slack w pracy testera: kanały zespołu, powiadomienia z CI i dobre praktyki komunikacji o defektach."
---

# Slack

**Slack** to platforma komunikacyjna do pracy zespołowej: kanały tematyczne, wiadomości prywatne, wątki, rozmowy głosowe i wideo. Integruje się z wieloma narzędziami i pozwala otrzymywać z nich powiadomienia.

## Slack w pracy testera

- szybki kontakt z programistami: doprecyzowanie wymagań, informacja o blokerze,
- kanały typu `#qa`, `#bugs`, `#deployments`,
- **powiadomienia z CI/CD** (Jenkins, GitHub Actions) o wynikach testów,
- powiadomienia z [Jiry](../test_management/jira.md) o zmianie statusu zgłoszeń,
- alerty z monitoringu ([Grafana](../monitoring/grafana.md)).

!!! warning "Slack to nie bug tracker"
    Błąd zgłoszony tylko na czacie łatwo zginie. Ustalenia z rozmowy zawsze przenieś do zgłoszenia w Jirze i dołącz link do wątku.

!!! danger "Dane wrażliwe"
    Nie przesyłaj na otwartych kanałach haseł ani tokenów (np. tokenów do API). Używaj menedżera haseł lub sekretów.
