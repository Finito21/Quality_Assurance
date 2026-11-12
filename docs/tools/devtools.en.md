---
description: "Chrome DevTools for testers: Elements, Console, Network and Application, device emulation and diagnosing defects."
---

# DevTools

**DevTools** is a set of tools built into the browser that let you analyse and edit the page you are viewing. They make it easier to diagnose problems and check the implementation.

Opening: ++f12++ or ++ctrl+shift+i++ (macOS: ++cmd+option+i++).

## Tabs

| Tab | What it is for |
|---|---|
| **Elements** | HTML structure and CSS styles of elements, finding locators for automation |
| **Console** | JS messages, running JS code, error information |
| **Sources** | files loaded by the page and its source code, debugging JS (breakpoints) |
| **Network** | HTTP traffic: status, URL, method, time, size, headers, body |
| **Performance** | analysing rendering and script performance |
| **Memory** | analysing memory usage (leaks) |
| **Application** | cookies, Local Storage, Session Storage, clearing site data |
| **Security** | information about the SSL/TLS certificate |
| **Lighthouse** | audit: performance, accessibility, SEO, best practices |
| **Recorder** | recording and replaying actions (simple automation, export to Puppeteer) |
| **Device toolbar** | simulating resolutions and mobile devices (++ctrl+shift+m++) |

## Console: log types

!!! info "Info"
    Information about what is happening on the page.

!!! warning "Warnings"
    Something does not load, something could be improved, a feature will be removed in the next version.

!!! failure "Errors"
    Something went wrong, e.g. a JS error or a failed request to the server. **Always worth attaching to a bug report.**

## Network in a tester's practice

- viewing API requests and responses (status code, headers, payload, response),
- **filtering** (Fetch/XHR, JS, CSS, Img) and searching,
- checking how resources load (waterfall) and how fast the server responds,
- **throttling**: slowing down the connection (e.g. *Slow 3G*) or offline mode,
- **Preserve log**: keeping logs after a reload or redirect,
- **Copy as cURL / fetch**: quickly reproducing a request in the terminal or Postman,
- exporting to a **HAR** file to attach to a bug report.

## Application: browser data

| Storage | Lifetime |
|---|---|
| **Local Storage** | persistent, until removed manually |
| **Session Storage** | disappears when the tab / session is closed |
| **Cookies** | depends on `Expires` / `Max-Age`, sent with every request |

**Clear site data** lets you open the page “as a new user”.

## Handy tricks

- ++ctrl+f++ in Elements lets you test CSS selectors and XPath,
- ++ctrl+shift+p++ opens the command palette (e.g. *Capture full size screenshot*),
- right-click on an element: **Copy → Copy selector / Copy XPath**,
- `$0` in the console is the currently selected element.
