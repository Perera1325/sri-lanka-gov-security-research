# Sri Lanka Government Web Security Posture – Research Plan (Phase 0)

Plan date: 11 November 2026 · Status: complete · This file is the Phase 0 baseline and is preserved as written. Later phases refine it in the other files under `research/`.

## Summary

This is phase 0 of the project: scope, rules, ten verified official domains, and a passive-only method. No site has been assessed yet, and this document contains no findings.

- Ten sites across eight public sectors are selected, each tied to a public source that names the domain as official.
- Verification so far rests on published sources found by web search. Registry confirmation of each domain is still an open step (see Next steps).
- Nothing in this plan involves scanning, form submission, login attempts or any other interaction beyond what an ordinary visitor's browser does.
- Anything that would need active verification will be recorded as NOT TESTED until written authorization exists.

## Objectives and scope

The project aims to describe the publicly observable security posture of ten Sri Lankan government websites and hand any credible observation to the owning institution through official channels.

**In scope**

- The public, unauthenticated pages of the ten domains listed below.
- Public third-party records about those domains: certificate transparency logs, DNS records, published datasets, news and official reports.
- General research on OWASP Top 10 risk classes and on risks of AI-assisted code, kept separate from site-specific claims.

**Out of scope**

- Subdomains that host logins, payments or e-services, beyond noting that they exist.
- Any authenticated area, admin interface, API probing or parameter manipulation.
- Personal data of any kind.

**Limitations**

- Passive observation shows configuration, not exploitability. A missing header is a hardening gap, not a proven vulnerability.
- Technology fingerprints from public pages can be wrong or out of date; each one needs a confidence level.
- There is no reliable passive way to tell whether a site was built with AI assistance. That question stays at the level of general risk research unless an institution has stated it publicly.

## Rules of engagement

Every activity in this project must pass one test: an ordinary member of the public could do the same thing in a browser, or the data already exists in a public third-party record.

| Allowed | Not allowed without written authorization |
| --- | --- |
| Viewing public pages and their HTML, CSS and JavaScript in a browser | Vulnerability scanners, crawlers, fuzzers, directory brute-forcing |
| Reading response headers and cookie attributes of a normal page load | Sending crafted payloads (SQL injection, XSS, path traversal) |
| Looking up DNS records, certificate transparency logs and WHOIS | Login attempts, password resets, authentication bypass |
| Using existing public datasets and published reports | Submitting forms, creating accounts, touching payment flows |
| Reading public documentation and public code repositories | Accessing admin interfaces or any non-public path |
| | Downloading or recording personal or confidential data |
| | Load or denial-of-service testing |

Two cautions apply even inside the allowed column.

- Online checkers such as TLS or header graders connect to the target on your behalf. Their traffic is light and ordinary, but prefer already-published results and keep any fresh lookups to one per site.
- If a page exposes something that looks sensitive (a key, a personal record, an internal path), stop, do not open or copy it further, note only its location, and report it to Sri Lanka CERT.

Unauthorized access to computer systems is an offence under Sri Lankan law (Computer Crime Act, No. 24 of 2007). This plan is not legal advice; confirm the legal position with a qualified person before going beyond passive observation.

## The ten websites

Ten sites cover all eight sectors in the brief. Each domain is matched to a public source that names it as the institution's official site; verification date for all rows is 11 November 2026.

| # | Institution | Domain | Sector | Source naming the domain |
| --- | --- | --- | --- | --- |
| 1 | Inland Revenue Department | ird.gov.lk | Financial and taxation | [IRD notice republished by KPMG](https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2025/april-2025/Tax-Flash-News-Circulars-Issued-by-the-Department-of-Inland-Revenue.pdf) |
| 2 | Department of Immigration and Emigration | immigration.gov.lk | Immigration | [Sri Lanka Embassy in Germany, government links](https://srilanka-botschaft.de/important-government-links/) |
| 3 | Department for Registration of Persons | drp.gov.lk | Public administration | [Ministry of Digital Economy institution page](https://mode.gov.lk/docs/institutions/DRP_old) |
| 4 | Department of Motor Traffic | dmt.gov.lk | Transportation | [Airport and Aviation Services notice](https://www.airport.lk/services/Temporary%20Driving%20License%20for%20International%20Tourists%20at%20BIA.pdf) |
| 5 | Sri Lanka Railways | railway.gov.lk | Transportation | [Sri Lanka High Commission in Pakistan, public notice](https://www.slhcpakistan.org/?p=116789) |
| 6 | Government Information Center | gic.gov.lk | Government information services | [GIC, About us](https://gic.gov.lk/gic/index.php/about-us.html) |
| 7 | Ministry of Digital Economy | mode.gov.lk | Digital government infrastructure | gov.lk name, restricted by the [LK Domain Registry](https://domains.lk/lk-domain-naming-structure/); site identifies itself as the [Ministry](https://mode.gov.lk) |
| 8 | Registrar General's Department | rgd.gov.lk | Public records | [Sri Lanka Embassy in Germany, government links](https://srilanka-botschaft.de/important-government-links/) |
| 9 | Parliament of Sri Lanka | parliament.lk | Parliament and legislative services | [Sri Lanka Embassy in Germany, government links](https://srilanka-botschaft.de/important-government-links/) |
| 10 | ICT Agency of Sri Lanka (ICTA) | icta.lk | Government technology institution | ICTA's own [project page](https://www.icta.lk/projects/digital-government/gov-lk-website-platform); independent confirmation still open |

Notes on individual rows:

- **Row 4.** Older official documents use motortraffic.gov.lk. Record both names and confirm which one the department currently treats as primary.
- **Row 5.** Sri Lanka Railways has publicly warned about fraudulent booking sites that imitate it, so use only the railway.gov.lk name. The booking subdomain handles payments and is out of scope.
- **Rows 9 and 10.** These two do not sit under gov.lk, so the registry restriction does not apply to them. They need the extra check described in the next section.
- **Reserve list.** cert.gov.lk (Sri Lanka CERT), cbsl.gov.lk (Central Bank) and gov.lk (national portal) can replace any site that turns out to be unsuitable.

## How the domains were verified

A domain counts as verified when two independent checks agree; seven of the ten currently pass both, and rows 7, 9 and 10 pass one.

1. **Registry rule.** The LK Domain Registry states that gov.lk is a closed second-level domain open only to government organizations and departments, with registrations handled by Lanka Government Information Infrastructure (LGII) under ICTA's domain policy ([LK Domain Registry, n.d.](https://domains.lk/lk-domain-naming-structure/)). Rows 1 to 8 are gov.lk names.
2. **Independent naming.** A separate official or reputable source (another government body, a diplomatic mission, or a published departmental notice) names the same domain for the same institution. These are the links in the table.

Status of the three exceptions (mode.gov.lk passes the registry rule but still needs a second government source that links to it):

- **parliament.lk** is named by a Sri Lankan diplomatic mission, and its documents are cited across government. It is not a gov.lk name, so add a registry WHOIS lookup showing the registrant.
- **icta.lk** is so far supported only by ICTA's own pages and by Sri Lanka CERT's description of ICTA as the government agency for IT infrastructure and policy ([Sri Lanka CERT, 2021](https://cert.gov.lk/wp-content/uploads/2023/07/2021_english.pdf)). Add a WHOIS lookup and one government page that links to icta.lk.

The verification in this document comes from published sources found by web search on the date above. Before any assessment starts, repeat it yourself and save a dated screenshot or PDF of each source.

## Assessment methodology

The assessment runs in five phases, each using only the allowed sources, and the same checklist is applied to every site so results are comparable.

1. **Baseline record.** For each site, record the date, the exact URL visited, and whether it loads over HTTPS and redirects from HTTP.
2. **Configuration review.** From one normal page load, note the security headers present or absent (HSTS, Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Referrer-Policy), cookie attributes on unauthenticated cookies (Secure, HttpOnly, SameSite), and any server or software version shown in headers. Take certificate details from certificate transparency logs.
3. **Technology and frontend review.** From page source, note the CMS or framework only where a reliable marker exists, the JavaScript libraries and their stated versions, and third-party scripts. Compare stated versions against public advisories. Do not fetch paths that the page itself does not link to.
4. **Risk mapping.** Map each observation to an OWASP Top 10 (2021) category and label it as *observed weakness*, *theoretical risk* or *NOT TESTED*. Anything that would need a request an ordinary visitor would not make is NOT TESTED by definition.
5. **Review and disclosure decision.** Re-check each observation on a second day, assign severity and confidence, and decide whether it meets the bar for disclosure.

**Useful existing data.** The LDFLK government website scorecard dataset covers SSL, domain compliance and email authentication for these institutions. Use it as the first evidence source and as a cross-check on your own observations.

**AI-assisted development strand.** Treat this as a literature review of risks in AI-generated code (missing server-side validation, hardcoded secrets, absent authorization checks, weak dependency management). Link it to a specific site only if the institution or its vendor has publicly said AI tools were used.

## Evidence register and risk classification

Every observation gets one row in the register, and nothing enters the report without one. The register is empty today.

| Field | What to record |
| --- | --- |
| ID | Site code plus sequence, for example IRD-01 |
| Website and URL | Institution name and the exact public URL |
| Date and time | Of the observation, in Sri Lanka time |
| Component | The public page, header, cookie or script concerned |
| Observation | What was seen, in one or two factual sentences |
| Evidence source | Browser view, certificate log, dataset or report, with link or saved file name |
| Technical explanation | Why it matters, with an OWASP category |
| Status | Confirmed observation, suspected, or NOT TESTED |
| Potential impact | What could follow if the weakness were exploitable |
| Remediation | The specific fix |
| Severity | Critical, High, Medium, Low or Informational |
| Confidence | High, Medium or Low, with the reason |

Severity follows what was observed, not what might be possible.

| Severity | When it applies in a passive study |
| --- | --- |
| Critical or High | Only for directly visible exposure, such as credentials or personal data on a public page. Report to Sri Lanka CERT at once and record no details. |
| Medium | A confirmed weakness with a known attack path, such as no HTTPS on a page that collects data, or a library version with a published serious advisory. |
| Low | A hardening gap, such as a missing security header or a cookie without SameSite. |
| Informational | Version disclosure, technology fingerprints, and every NOT TESTED item. |

A NOT TESTED entry also states what authorization would be needed: a signed letter from the institution naming the target, the test types, the dates and a contact person, with testing done in a staging environment where possible.

## Responsible disclosure path

Disclosure drafts are written only for observations that are confirmed, reproducible by a second look, and rated Low or above. None exist yet, so no drafts are included.

- **Primary channel.** Sri Lanka CERT asks that incidents be submitted through its official reporting portal, and lists 101 as its hotline ([Sri Lanka CERT, n.d.](https://cert.gov.lk/report_incident)). Confirm the current process on that page before sending anything.
- **Institution contact.** Where an institution publishes a security or webmaster contact, copy it only after CERT has acknowledged the report, or as CERT advises.
- **Content of a report.** Site, URL, date, what was observed, how to see it in a browser, why it matters, and the suggested fix. No exploit steps, and no personal data.
- **Publication.** Publish site-specific details only after the institution has fixed the issue or CERT agrees. Aggregate statistics can be published earlier.
- **Sending.** Every message is reviewed and sent manually by the researcher.

## Next steps

- [ ] Run a WHOIS lookup at the LK Domain Registry for parliament.lk and icta.lk, and find a second government source linking to mode.gov.lk
- [ ] Save dated copies of every verification source in the table
- [ ] Confirm whether dmt.gov.lk or motortraffic.gov.lk is the department's primary domain
- [ ] Pull the rows for these ten institutions from the LDFLK scorecard dataset
- [x] Create the evidence register with the fields above (see `evidence/evidence-register.csv`)
- [ ] Do the phase 1 baseline record for all ten sites on one day
- [ ] Decide whether to ask Sri Lanka CERT or ICTA for a letter acknowledging the study before phase 2

## References

Government Information Center. (n.d.). *About us*. <https://gic.gov.lk/gic/index.php/about-us.html>

Information and Communication Technology Agency of Sri Lanka. (2025). *gov.lk website platform*. <https://www.icta.lk/projects/digital-government/gov-lk-website-platform>

LK Domain Registry. (n.d.). *LK domain naming structure*. <https://domains.lk/lk-domain-naming-structure/>

Ministry of Digital Economy. (n.d.). *Department for Registration of Persons (DRP)*. <https://mode.gov.lk/docs/institutions/DRP_old>

Sri Lanka CERT. (2021). *Annual report 2021*. <https://cert.gov.lk/wp-content/uploads/2023/07/2021_english.pdf>

Sri Lanka CERT. (n.d.). *Report incident*. <https://cert.gov.lk/report_incident>

Sri Lanka Embassy in Germany. (n.d.). *Important government links*. <https://srilanka-botschaft.de/important-government-links/>

Sri Lanka High Commission in Pakistan. (n.d.). *Public notice*. <https://www.slhcpakistan.org/?p=116789>
