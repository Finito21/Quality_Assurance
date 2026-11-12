---
description: "GitHub for testers: issues and labels, pull requests, code review of test changes and reporting defects with an issue template."
---

# GitHub

**GitHub** is a platform for hosting Git repositories and collaborating on code. It is used mainly through the browser. When you finish working locally, you send your work (`git push`) to GitHub so others can see it.

## Key features

| Feature | Use |
|---|---|
| **Repositories** | storing code, public or private |
| **Pull Requests** | proposing changes + **code review** before merging |
| **Issues** | reporting bugs and tasks, labels, assignments |
| **Projects** | Kanban boards for planning work |
| **Actions** | CI/CD, e.g. running tests automatically ([GitHub Actions](../ci_cd/github_actions.md)) |
| **Pages** | free hosting for static sites (this site runs on it) |
| **Releases / Tags** | marking versions |

## Pull request step by step

1. Create a branch and push it (`git push -u origin <branch>`).
2. On GitHub, click **Compare & pull request**.
3. Describe **what** was changed and **why**, add reviewers.
4. Check the result of the automated tests (checks).
5. After approval: **Merge** and delete the branch.

## A tester on GitHub

- reviewing PRs: the **Files changed** tab shows exactly what changed,
- reporting bugs as **Issues** with a template (steps, expected and actual result),
- following test results in the **Actions** tab,
- keeping a testing portfolio (projects, collections, automated tests).
