# IRD observation plan

Website assessment of `ird.gov.lk` has not started and must not start yet: the inventory lists its domain status as `PRELIMINARY`, and the [methodology](../methodology.md) requires `VERIFIED` first. This plan sets out the verification tasks, then the browser observations to carry out once they are done.

| | |
| --- | --- |
| Site | Inland Revenue Department, `ird.gov.lk` (site ID `IRD`) |
| Plan date | 2026-11-11 |
| Domain verification | `PRELIMINARY` (two checks passed on web-search evidence; no saved copies) |
| Research status | `NOT STARTED` |
| Background | [IRD public evidence review](../../reports/individual-sites/ird-public-evidence-review.md) |
| Blank scorecard | [`data/scorecards/IRD-scorecard.csv`](../../data/scorecards/IRD-scorecard.csv) |

## Part A — Domain verification task list

Complete all of these, then change `domain_verification_status` for IRD to `VERIFIED` in [`data/website-inventory.csv`](../../data/website-inventory.csv).

- [ ] Open the LK Domain Registry naming-structure page (IRD-PUB-01) and save a dated PDF to `evidence/sources/domain-verification/`
- [ ] Open the KPMG-republished IRD circular (IRD-PUB-02) and save a dated copy
- [ ] Open the Ministry of Finance departments page (IRD-PUB-03), record where the "Department of Inland Revenue" entry links to, and save a screenshot
- [ ] Look up `ird.gov.lk` in the LK Domain Registry's public WHOIS and save the result
- [ ] Optional, and not required for `VERIFIED`: as a historical research lead only, look up `inlandrevenue.gov.lk` (IRD-PUB-04) in the same WHOIS and note whether it is registered. Do not visit it, and do not treat it as a concern
- [ ] Update the inventory row and run `python3 scripts/build_dashboard.py` and `python3 scripts/validate.py`

## Part B — Public-record lookups (no contact with the website)

These query third-party services, not IRD's web server. Do each once and save the result page under `evidence/sources/IRD/`.

- [ ] **Certificate transparency.** Open <https://crt.sh/?q=ird.gov.lk>. Record issuer and validity dates of the current certificate for `www.ird.gov.lk`. Keep the saved page private. Do not visit other host names shown there and do not publish a list of them in this repository
- [ ] **DNS.** Using a public DNS lookup web tool, look up the name-server, mail and text records for `ird.gov.lk` and its DMARC record. Keep the raw output private. Record in this repository only whether SPF and DMARC records are published and their policy values, not IP addresses or mail-server names
- [ ] **LDFLK scorecard.** Extract the IRD row from the dataset and record its collection date and each field

## Part C — Passive browser observation guide

Start only when Part A is complete. This is carried out by a person in a normal browser. Nothing here is automated.

### Boundaries for this site

| Do | Do not |
| --- | --- |
| Load `https://www.ird.gov.lk/` and the public information pages linked from its menus (for example About, Publications, Downloads, Contact) | Open "Access to e-Services", taxpayer registration, TIN, payment or any login page |
| Read page source, the Network tab and the cookie list | Use the site search box or submit any form |
| Visit at most five public pages | Type in guessed URLs, admin paths or API addresses |
| Make one visit per day, on two separate days | Refresh repeatedly, use scripts, extensions, scanners or crawlers |

If a link leads to a login or e-service page, close the tab and record the item as `NOT TESTED`.

### Setup

1. Use Chrome or Firefox in a private window with extensions disabled.
2. Open developer tools (F12), select the Network tab and tick "Preserve log".
3. Note the date and time (Sri Lanka time) and your browser version.
4. Record each result in `data/scorecards/IRD-scorecard.csv` as you go.

### Checks

Each check follows the standard in the [assessment checklist](../assessment-checklist.md). Result values are `YES`, `NO`, `PARTIAL`, `NOT OBSERVED` or `NOT TESTED`.

| ID | What to do | What to save | If it cannot be done safely |
| --- | --- | --- | --- |
| C01 | Load `https://www.ird.gov.lk/`. Note whether it loads without a certificate warning. | Screenshot of page with address bar | `NOT TESTED` |
| C02 | In a new tab type `http://www.ird.gov.lk/`. In the Network tab read the first response's status code and `Location` header. Repeat once for `http://ird.gov.lk/`. | Screenshot of the first request's headers | `NOT TESTED` |
| C03a–f | Click the main document request. Read the response headers for the six headers listed in the checklist. Copy each value exactly, or record that it is absent. | One screenshot of the full response-header list | `NOT TESTED` |
| C04 | Open Application → Cookies (Chrome) or Storage → Cookies (Firefox). For each cookie note the name and the `Secure`, `HttpOnly` and `SameSite` columns. | Screenshot of the table with the Value column hidden or cropped | `NOT OBSERVED` if no cookies |
| C05 | Click the padlock → certificate. Note issuer, validity dates and subject names. Compare with the Part B certificate log result. | Screenshot of the certificate summary | Protocol versions and cipher suites are `NOT TESTED` |
| C06 | View page source (Ctrl+U). Look for a `generator` meta tag and for `Server`, `X-Powered-By` or platform-specific response headers. This is the check for the unconfirmed inference in IRD-PUB-07; without an explicit marker, record `NOT OBSERVED` and name no product. | Screenshot of the marker | `NOT OBSERVED` if no explicit marker |
| C07 | In the Network tab filter by JS. For each library note the version only if it appears in the file name, URL or the first comment lines of the file. | Screenshot showing the version text | `NOT OBSERVED` if no versions shown |
| C08 | In the JS filter, list hosts other than `ird.gov.lk`. In page source, check whether those `<script>` tags carry an `integrity` attribute. | Screenshot of the request list and one script tag | `NOT OBSERVED` if no third-party scripts |
| C09 | While doing the above, note any verbose error text, internal host names or paths, version banners or developer comments on the public pages visited. | Screenshot and the page URL | See the rule below |

**If something sensitive appears** (a credential, key or personal record): stop, do not copy the value, and follow the escalation rule in the [evidence guidelines](../../evidence/evidence-guidelines.md).

### After each visit

1. Name and file screenshots as the evidence guidelines describe, under `evidence/sources/IRD/`.
2. Check every screenshot for cookie values or personal data and crop them out.
3. Fill in the scorecard with the result and the evidence file name.
4. After the second visit, add rows to the [evidence register](../../evidence/evidence-register.csv) for results seen on both days.

## Part D — Items that are NOT TESTED

These cannot be determined passively. Each would need written authorization from IRD naming the target, the test types, the dates and a contact person, ideally against a staging system.

| Item | Why it is out of reach |
| --- | --- |
| RAMIS e-services login, session handling and access control | Authenticated system |
| Taxpayer and TIN registration forms | Requires form submission |
| e-Invoicing data interface (IRD-PUB-11) | Out of scope; API probing is prohibited |
| Online tax payment flow (IRD-PUB-12) | Out of scope; payment system |
| Server-side input validation and injection resistance | Requires crafted requests |
| TLS protocol versions and cipher suites | Requires active handshake testing, unless an existing published result is cited |
| Whether any advisory applies to the platform in use | Requires version confirmation and testing |
| Other host names found in certificate logs | Not in the inventory |

## Readiness

| Requirement | State |
| --- | --- |
| Domain `VERIFIED` | No — Part A outstanding |
| Public-record lookups done | No — Part B outstanding |
| Browser observation guide prepared | Yes |
| Blank scorecard prepared | Yes |
| Any technical result recorded | No |

The site is **not yet ready** for browser observation. It becomes ready when Part A is complete.
