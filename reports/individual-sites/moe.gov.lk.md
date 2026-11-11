# Security posture report: Ministry of Education

| | |
| --- | --- |
| Site ID | MOE |
| Domain | moe.gov.lk |
| Sector | Education |
| Report status | Not started |
| Observation dates | None yet |
| Evidence register rows | None yet |

> This site has not been assessed. Nothing below is a finding. Sections are filled in only from rows in the [evidence register](../../evidence/evidence-register.csv).

Published incidents and other public records for this institution are summarized separately in the [public-records summary](moe.gov.lk-public-records.md). They describe past events and are not observations of the site.

## 1. Executive summary

_To be written after assessment. State in three or four sentences what was looked at, the number of observations by severity, and the most useful recommendation._

## 2. Website overview

- **Institution:** Ministry of Education
- **Official domain:** moe.gov.lk
- **Sector:** Education
- **Domain verification:** see [`data/website-inventory.csv`](../../data/website-inventory.csv)
- **Purpose of the site:** _to be described from its public pages_

## 3. Assessment scope

Public, unauthenticated pages of `moe.gov.lk` reached by ordinary links. Logins, e-services, payment flows, APIs and unlinked paths are excluded. Full rules: [scope](../../research/scope.md).

_List the specific pages visited._

## 4. Methodology

Passive observation using the [assessment checklist](../../research/assessment-checklist.md), on two separate days, in a standard browser. No scanning, crawling, form submission or login attempt.

## 5. Observed configurations

_Copy results from this site's scorecard. Leave blank until observed._

| Check | Result | Evidence |
| --- | --- | --- |
| C01 HTTPS availability | | |
| C02 HTTP to HTTPS redirection | | |
| C03a Strict-Transport-Security | | |
| C03b Content-Security-Policy | | |
| C03c X-Frame-Options / frame-ancestors | | |
| C03d X-Content-Type-Options | | |
| C03e Referrer-Policy | | |
| C03f Permissions-Policy | | |
| C04 Cookie attributes | | |
| C05 TLS certificate | | |
| C06 Technology fingerprints | | |
| C07 JavaScript dependency versions | | |
| C08 Third-party scripts | | |
| C09 Public information disclosure | | |

## 6. Potential security concerns

_One short paragraph per register row with status `CONFIRMED OBSERVATION` or `SUSPECTED`. Describe hardening gaps as gaps, not as vulnerabilities._

## 7. Evidence references

_List register IDs and the evidence files that support them._

## 8. OWASP mapping

| Finding ID | OWASP category | Status |
| --- | --- | --- |
| | | |

## 9. Risk assessment

_Severity and confidence for each finding, with one sentence of reasoning each, following [risk classification](../../docs/risk-classification.md)._

| Finding ID | Severity | Confidence | Reasoning |
| --- | --- | --- | --- |
| | | | |

## 10. Recommendations

_Specific fixes, most useful first._

## 11. Limitations

Results reflect public pages on the dates given, seen from one location. They show configuration, not exploitability. See [research limitations](../../docs/research-limitations.md).

## 12. NOT TESTED items

The following cannot be determined passively and were not examined. Testing any of them would need written authorization from the institution naming the target, test types, dates and a contact person.

- Access control and authorization behaviour
- Authentication and session handling after login
- Input handling and injection resistance
- Server-side validation of client-side checks
- TLS protocol versions and cipher suites, unless an existing published result is cited
- Exploitability of any advisory matched to an observed version
- Logging, monitoring and incident response
