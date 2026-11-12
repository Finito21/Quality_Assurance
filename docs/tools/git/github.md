---
description: "GitHub dla testera: issues, pull requesty, przegląd kodu i zgłaszanie defektów z szablonem."
---

# GitHub

**GitHub** to platforma do hostowania repozytoriów Git i współpracy nad kodem. Najczęściej korzystasz z niego przez przeglądarkę. Kiedy skończysz pracę lokalnie, wysyłasz ją (`git push`) na GitHub, aby inni mogli ją zobaczyć.

## Najważniejsze funkcje

| Funkcja | Zastosowanie |
|---|---|
| **Repozytoria** | przechowywanie kodu, publiczne lub prywatne |
| **Pull Requests** | propozycja zmian + **code review** przed scaleniem |
| **Issues** | zgłaszanie defektów i zadań, etykiety, przypisania |
| **Projects** | tablice Kanban do planowania pracy |
| **Actions** | CI/CD, np. automatyczne uruchamianie testów ([GitHub Actions](../ci_cd/github_actions.md)) |
| **Pages** | darmowy hosting stron statycznych (na nim działa ta strona) |
| **Releases / Tags** | oznaczanie wersji |

## Pull Request krok po kroku

1. Utwórz gałąź i wypchnij ją (`git push -u origin <gałąź>`).
2. Na GitHubie kliknij **Compare & pull request**.
3. Opisz **co** i **dlaczego** zmieniono, dodaj recenzentów.
4. Sprawdź wynik automatycznych testów (checks).
5. Po akceptacji: **Merge** i usunięcie gałęzi.

## Tester na GitHubie

- przegląd PR: zakładka **Files changed** pokazuje, co dokładnie się zmieniło,
- zgłaszanie defektów jako **Issues** z szablonem (kroki, wynik oczekiwany i rzeczywisty),
- obserwowanie wyników testów w zakładce **Actions**,
- trzymanie portfolio testerskiego (projekty, kolekcje, testy automatyczne).
