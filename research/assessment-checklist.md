# Passive security assessment checklist

Nine checks are applied to every site, each answerable from one normal browser visit or from an existing public record. Record results in a copy of [`data/scorecard-template.csv`](../data/scorecard-template.csv).

## Before you start

- The site's inventory row reads `VERIFIED`.
- Use an ordinary desktop browser with a fresh private window, no extensions that alter requests.
- Open developer tools (F12) before loading the page so the Network tab captures the first request.
- Visit the home page and, at most, a handful of public pages linked from it. Do not type in guessed paths.
- Note the date and time in Sri Lanka time.

## Result values

`YES`, `NO`, `PARTIAL`, `NOT OBSERVED` (looked, nothing to see) or `NOT TESTED` (cannot be determined passively).

## Checks

### C01 HTTPS availability

- **How.** Load `https://<domain>/`. Check that the page loads with no certificate warning.
- **Sufficient evidence.** Screenshot showing the address bar with the padlock and the loaded page, with date.
- **Record.** `YES` if it loads cleanly; `NO` if it fails or warns.

### C02 HTTP to HTTPS redirection

- **How.** In a new tab, type `http://<domain>/`. In the Network tab, look at the first response's status and `Location` header.
- **Sufficient evidence.** Screenshot of the Network tab showing the first request, its status code and the `Location` value.
- **Record.** `YES` for a 301/308 to HTTPS; `PARTIAL` for a temporary (302/307) or script-based redirect; `NO` if the page is served over HTTP.

### C03 Security headers

- **How.** In the Network tab, select the main document request and read its response headers. Check each of the six below.
- **Sufficient evidence.** One screenshot of the full response-header list for the main document, with the URL visible.
- **Record.** One scorecard row per header: `YES` if present, `NO` if absent. Copy the header value into the notes column.

| ID | Header | What a sound value looks like |
| --- | --- | --- |
| C03a | `Strict-Transport-Security` | `max-age` of at least six months |
| C03b | `Content-Security-Policy` | Present, without `unsafe-inline` in `script-src` |
| C03c | `X-Frame-Options` or CSP `frame-ancestors` | `DENY` or `SAMEORIGIN` |
| C03d | `X-Content-Type-Options` | `nosniff` |
| C03e | `Referrer-Policy` | Any value other than `unsafe-url` |
| C03f | `Permissions-Policy` | Present |

A missing header is a hardening gap. It is not evidence of an exploitable flaw.

### C04 Cookie attributes

- **How.** After the page has loaded, open Application (Chrome) or Storage (Firefox) and list the cookies set for the domain. Note `Secure`, `HttpOnly` and `SameSite` for each. Do not log in.
- **Sufficient evidence.** Screenshot of the cookie table. Record cookie names and flags only; never record cookie values.
- **Record.** `YES` if all cookies carry `Secure` and a `SameSite` value; `PARTIAL` if some do; `NO` if none; `NOT OBSERVED` if no cookies are set.

### C05 TLS certificate information

- **How.** Search the domain in a public certificate transparency log viewer such as <https://crt.sh>. Note issuer, validity dates and names covered for the current certificate. The browser's own certificate viewer may be used to cross-check.
- **Sufficient evidence.** Link to the log entry plus a saved copy of the page.
- **Record.** `YES` if the current certificate is valid, unexpired and issued by a publicly trusted authority; `NO` otherwise. Protocol versions and cipher suites are `NOT TESTED` unless an existing published result is cited.

### C06 Technology fingerprints

- **How.** View page source. Look for explicit markers: a `generator` meta tag, well-known asset paths, or `Server` and `X-Powered-By` response headers.
- **Sufficient evidence.** Screenshot of the marker itself. A guess from the look of the site is not evidence.
- **Record.** `YES` with the technology named in notes if an explicit marker exists; `NOT OBSERVED` if none. Note separately whether a version number is disclosed.

### C07 JavaScript dependency versions

- **How.** In page source or the Network tab, list script files. Take the version only from the file name, URL or the banner comment at the top of the file.
- **Sufficient evidence.** Screenshot showing the URL or banner that states the version. Compare with the library's public advisory list and save that advisory link.
- **Record.** `YES` if all identified versions are current or have no known advisory; `NO` if any has a published advisory; `NOT OBSERVED` if no versions are identifiable. Whether an advisory is exploitable on this site is always `NOT TESTED`.

### C08 Third-party script references

- **How.** In the Network tab, filter by JS and list the hosts other than the site's own domain. In page source, check whether those `<script>` tags carry an `integrity` attribute.
- **Sufficient evidence.** Screenshot of the Network tab filtered to scripts, and of one representative `<script>` tag.
- **Record.** `YES` if all third-party scripts use `integrity`, or there are none; `PARTIAL` or `NO` otherwise. List the hosts in notes.

### C09 Public information disclosure

- **How.** While doing the checks above, note anything a public page should not show: verbose error text, internal hostnames or file paths, version banners, developer comments, or email addresses and keys embedded in scripts.
- **Sufficient evidence.** Screenshot of the page and the location of the item. If it looks like a credential or personal data, stop: record only the URL and that it exists, do not copy the value, and follow the escalation rule in the [evidence guidelines](../evidence/evidence-guidelines.md).
- **Record.** `NOT OBSERVED` if nothing is seen; `YES` if something is, with a neutral description.

## What this checklist never does

It does not request paths the site does not link to, submit any form, send altered or repeated requests, or use any scanner. A question that would need those is written into the register as `NOT TESTED`.

## After the visit

1. Save evidence files as described in the [evidence guidelines](../evidence/evidence-guidelines.md).
2. Add a register row for each result that is a concern or a notable fact.
3. Repeat the visit on another day before marking anything `CONFIRMED OBSERVATION`.
