---
description: "Browsers and extensions for testers: cross-browser testing, cloud device farms, screenshots and screen recordings, and extensions that speed up testing."
---

# Browsers and extensions

## Cross-browser testing

Each browser may **interpret** some elements **differently** (CSS, JS, forms, fonts). A basic set:

- Chrome
- Firefox / Firefox Developer Edition
- Edge
- Safari (WebKit engine, important for iOS)
- Opera

## BrowserStack

A cloud platform for testing web and mobile applications on **real devices and browsers** (full capabilities in the paid version). It integrates with Jira, GitLab, Jenkins and other tools.

| Mode | Description |
|---|---|
| **Live** | manual tests on a chosen browser, version, system and device |
| **Automate** | running automated tests (Selenium, Cypress, Playwright…) with reports |
| **Percy** | visual regression tests (comparing screenshots) |

Alternative: **TestMu AI** (formerly LambdaTest).

## Extensions for testers

| Extension | Use |
|---|---|
| **Bug Magnet** | ready-made valid and invalid data for forms (e-mails, numbers, special characters) |
| **LT Browser** (TestMu AI, formerly LambdaTest) | the page on different browsers, systems and resolutions, full-page screenshot |
| **ResolutionTest** | quick tests at different resolutions |
| **Bird Eats Bug** | screenshots and recordings with **console logs, requests** and system information |
| **Awesome Screenshot** | screenshots and recordings with editing |
| **Clear Cache** | quickly clearing the cache |
| **Page Ruler** | measuring element dimensions on the page |
| **Cookie-Editor** | viewing and editing cookies |
| **PixelPerfect** | overlaying a design on the page and comparing it pixel by pixel |

!!! question "Bug Magnet and creativity"
    Ready-made data sets speed up the work, but **do not replace thinking**. It is worth adding your own cases that come from the application's business logic.

!!! note "Designs"
    Today UI designs are most often delivered in **Figma**. Older designs may come as `.psd` files (Photoshop).

## Screenshots and recordings

=== "PicPick"

    Free for personal use (paid for commercial use). After taking a screenshot it opens an editor (arrows, text, blur).

    - full screen, a region, a **scrolling page** (whole or part),
    - colour picker with the colour code (HEX), magnifier,
    - pixel ruler, coordinates, protractor,
    - screen recording.

=== "ShareX"

    Free and open source (Windows). Screenshots and recordings (MP4 or GIF) via keyboard shortcuts, editing after capture, automatic actions after a screenshot (e.g. copying to the clipboard).
