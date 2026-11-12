---
description: "Tester job interview questions with sample answers: testing principles, test techniques, the defect lifecycle, APIs, SQL and test automation."
---

# Interview questions

Typical questions in an interview for a tester role (junior / mid) with short answers. Try to answer yourself first, then expand the answer. In an interview, an example from your own practice is better than a recited definition.

## Basics

??? question "How do QA, QC and testing differ?"
    **QA** (quality assurance) is about processes and preventing defects. **QC** (quality control) is about the product and finding defects. **Testing** is the main form of QC. More: [QA fundamentals](qa_fundamentals.md#qm-qa-and-qc).

??? question "How do an error, a defect and a failure differ?"
    A person makes an **error** (mistake), which introduces a **defect** into the code. When the faulty code is executed, a **failure** may occur, which is the visible effect. Not every defect causes a failure.

??? question "List the testing principles."
    Testing shows the presence, not the absence, of defects; exhaustive testing is impossible; early testing saves time and money; defects cluster together; tests wear out (pesticide paradox); testing is context dependent; the absence-of-defects fallacy. It helps to give an example for each principle.

??? question "How does verification differ from validation?"
    **Verification**: are we building the product right, i.e. according to the specification. **Validation**: are we building the right product, i.e. the one the user needs.

??? question "How does a retest differ from a regression test?"
    A **retest** (confirmation test) checks whether a specific fixed defect is gone. A **regression test** checks whether a change has broken other features that worked before.

??? question "How does a smoke test differ from a sanity test?"
    A **smoke test** is a broad, shallow check of a new build: does the application start and do the main features work. A **sanity test** is a narrow check of the area a change touched. Both are quick and decide whether further testing makes sense.

## Process and lifecycle

??? question "Describe the test process."
    Test planning, monitoring and control, analysis, design, implementation, execution and completion. The activities do not have to run in sequence: in Scrum all of them happen in every sprint. More: [Test process](qa_fundamentals.md#test-process).

??? question "What does a tester do in Scrum?"
    The tester is part of the team. They take part in refinement (asking about acceptance criteria, raising risks), planning, the Daily Scrum and the retrospective. They test stories during the sprint, automate regression and make sure the Definition of Done is met. They do not leave testing until the end of the sprint.

??? question "Describe the defect lifecycle."
    New → Assigned → In Progress → Resolved → Ready for Test → Closed, and if the retest fails: Reopened. A report can also be rejected (Rejected), marked as a duplicate (Duplicate), impossible to reproduce (Cannot Reproduce) or postponed (Deferred). More: [Defect lifecycle](test_management.md#defect-lifecycle).

??? question "How does severity differ from priority? Give an example."
    **Severity** describes the impact of a defect, **priority** the urgency of the fix. A typo in the company name on the home page: low severity, high priority. A crash in a rarely used annual report: high severity, low priority. More: [Severity vs priority](test_documentation.md#severity-vs-priority).

??? question "What should a good defect report contain?"
    A clear title, the environment and version, steps to reproduce, the expected and actual result, severity and priority, evidence (screenshot, recording, logs). One report describes one defect. Example: [Weak and good reports](test_documentation.md#weak-and-good-reports).

??? question "What do you do when a developer says the reported defect is not a defect?"
    I check the requirement or acceptance criteria and reproduce the problem again. If the requirement is unclear, I ask the product owner or analyst for a decision. I talk about facts and the impact on the user, not about who is right.

## Test techniques

??? question "Which test design techniques do you know?"
    Black-box: equivalence partitioning, boundary values, decision tables, state transitions. White-box: statement and branch coverage. Experience-based: error guessing, exploratory testing, checklists. More: [Test techniques](test_techniques.md).

??? question "A field accepts an age from 18 to 65. Which values will you test?"
    Equivalence partitions: e.g. 10 (invalid), 30 (valid), 80 (invalid). Boundary values (2-value version): 17, 18, 65, 66. Plus error guessing: an empty field, letters, a negative number, a fraction, spaces, a very large number.

??? question "How would you test a pen (a lift, a mug, a login form)?"
    This question checks your way of thinking, not your knowledge. Start with questions: who will use it, for what, what the requirements are. Then split the tests into functional (does it write), non-functional (comfort, durability: dropping it, frost, safety), negative (writing on a wet or greasy surface) and boundary (the last drop of ink).

## APIs, databases and tools

??? question "Which HTTP methods do you know and how does PUT differ from PATCH?"
    GET reads, POST creates, PUT replaces the whole resource, PATCH changes part of it, DELETE deletes. GET, PUT and DELETE are idempotent: calling them many times leads to the same state. More: [HTTP](../technologies/api_testing/http.md).

??? question "What do the codes 200, 201, 400, 401, 403, 404 and 500 mean?"
    200 OK, 201 resource created, 400 bad request, 401 not authenticated, 403 not authorised, 404 not found, 500 server error. The most common trap: 401 vs 403.

??? question "How would you test a REST endpoint?"
    A valid request (status code, body and schema of the response, headers), missing and invalid fields, wrong types, boundary values, a missing or wrong token, access to other users' resources, response time. I also check that the data was saved in the database. Tool: [Postman](../tools/api_testing_tools/postman.md).

??? question "How does INNER JOIN differ from LEFT JOIN?"
    INNER JOIN returns only rows matched in both tables. LEFT JOIN returns all rows from the left table and fills missing matches with `NULL`. Example on data: [SQL](../technologies/backend/sql.md#joins).

??? question "What does a tester use DevTools for?"
    The Console tab for JavaScript errors, Network for checking requests, status codes and timings, Elements for viewing and editing HTML and CSS, Application for cookies and local storage, device mode for responsiveness tests. More: [DevTools](../tools/devtools.md).

??? question "Which Git commands do you use every day?"
    `git clone`, `git status`, `git pull`, `git switch -c` (a new branch), `git add`, `git commit`, `git push`, and when something goes wrong `git log`, `git diff` and `git restore`. More: [Git basics](../tools/git/git_basics.md).

## Automation

??? question "What is worth automating and what is not?"
    Worth it: regression, smoke tests, API tests, tests with many data sets. Not worth it: one-off tests, features that change often, judging usability. More: [Test automation strategy](test_automation_strategy.md).

??? question "What is the test pyramid?"
    A model of proportions: fast component tests are the most numerous, integration and API tests are fewer, and slow E2E tests through the UI are the fewest. An inverted pyramid leads to a slow, brittle test suite.

??? question "What is a flaky test and how do you deal with it?"
    A test that sometimes passes and sometimes fails without code changes. Typical causes are fixed delays, dependencies between tests and shared data. Solutions: waiting for a condition, independent data, stable locators, quarantine and a fix.

## About you

??? question "Why do you want to become a tester?"
    Answer honestly and specifically: what interests you in testing, what you have already learned (a course, ISTQB, your own projects) and how you show it. It helps to have an example of a defect you found in a real application.

??? question "How do you learn and where do you get your knowledge?"
    Name specific sources (the ISTQB syllabus, tool documentation, courses, communities), practice projects (e.g. public demo applications) and what you took from them. List of sources: [Resources](../resources.md).
