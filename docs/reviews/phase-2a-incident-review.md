# Review report: Phase 2a historical incidents

| | |
| --- | --- |
| Review date | 2026-11-11 |
| Scope | Incident records for six institutions: Public Security, Government Printing, Public Administration, Railways, NMRA and Education |
| Method | Re-opening the main news source for each record and re-reading it for attribution |
| Website testing | None. No request was made to any of the websites concerned |
| Outcome | One record added, five corrected, incident data restructured into five separate fields |

Each incident below is a past event. None of the statements describes the present state of any website, and none is a claim of a current vulnerability.

## The five-way separation

The incident file now has a column for each category, so they cannot be merged by accident.

| Category | Column in `data/historical-incidents.csv` |
| --- | --- |
| Confirmed historical incident | `confirmed_details` (what an official body said) |
| Reported allegations | `alleged_or_unconfirmed_details` |
| Official investigation announcements | `investigation_announced` |
| Unknown investigation outcomes | `investigation_outcome` (`UNKNOWN`, `NOT APPLICABLE` or `KNOWN: …`) |
| Confirmed remediation | `remediation_confirmed` |

## Ministry of Education — INC-20 (new)

| Category | What the sources support |
| --- | --- |
| Confirmed incident | The Ministry's website was accessed without authorization on 4 April 2024 and a message was posted on it. The Ministry acknowledged the incident. A Sri Lanka CERT engineer was reported as saying initial investigation pointed to a local individual. |
| Reported, attributed to Sri Lanka CERT | CERT had advised an annual vulnerability assessment and the Ministry had not carried one out. CERT recommended a new website instead of reinstating the old one. |
| Reported, unattributed | Security patches and updates had not been applied. The article states this without naming who said it. |
| Allegations | The posted message's claims about its author and about security flaws. A Ministry official's statement that no information was compromised is an official claim that was not independently confirmed. |
| Investigation announced | A probe led by Sri Lanka CERT and the Telecommunications Regulatory Commission (reported 6 April 2024). CERT's findings were to go to the Minister and then to the CID (reported 10 April 2024). |
| Confirmed remediation | A Ministry official said the site was restored on 5 April 2024. |
| Unknown | The investigation's outcome. Whether a new website was launched. Whether assessments are now carried out. |

Primary source status: Sri Lanka CERT's own statement or report was **not found**. The record rests on Daily Mirror's report of 10 April 2024, opened and read in this review. The Ministry's 2022 performance report, a primary document, records earlier work on a cyber security action plan but does not concern the incident.

## Ministry of Public Security — INC-01 (corrected)

| Category | What the sources support |
| --- | --- |
| Confirmed incident | The Police Media Division said there were multiple instances of unauthorized access to the website, after which the state emblem displayed irregularly. |
| Allegations | None recorded. |
| Investigation announced | Complaint filed with the CID on 9 January 2026 by the Ministry Secretary on the Minister's instruction; CID investigation opened; internal ministry inquiry. |
| Confirmed remediation | Sri Lanka CERT and ICTA took measures to restore the website, per the police statement. |
| Unknown | Dates and method of access; whether data was accessed; the outcome. |

**Correction:** the earlier record said only that the site was "targeted". The police statement's wording (multiple instances of unauthorized access) and the complaint date are now recorded.

## Department of Government Printing — INC-02 (corrected)

| Category | What the sources support |
| --- | --- |
| Confirmed incident | Sri Lanka CERT confirmed the site was hacked and content altered, 30–31 December 2024. A named CERT engineer was reported as saying CERT's audit found critical vulnerabilities in the old site and that CERT recommended replacing it. |
| Allegations | None recorded. |
| Investigation announced | Cabinet spokesman, 31 December 2024. Police said on 2 February 2025 that investigations continued with no arrests. |
| Confirmed remediation | Restored 2 January 2025 per CERT; core documents back online by February 2025 without the old features. The Government Printer said a replacement site would be audited by CERT before going live. |
| Unknown | Outcome of the investigation; whether the replacement site has gone live. |

**Correction:** the audit statement is now attributed to the named engineer in the Sunday Times of 5 January 2025, which becomes the main source. The police statement of February 2025 was added.

## Ministry of Public Administration — INC-03 and INC-04 (INC-04 corrected)

| Category | INC-03 (30 May 2020) | INC-04 (April 2026) |
| --- | --- | --- |
| Confirmed incident | The Air Force's Cyber Security Centre said the homepage was defaced. | The Minister said a complaint about an apparent cyberattack on the website was lodged with the CID, and that no highly sensitive information was compromised. |
| Allegations | Attribution. | A forum listing claimed to offer data from the site; press descriptions of its contents are unconfirmed. |
| Investigation announced | None found. | CID tasked with investigating. |
| Confirmed remediation | None found. | None found. |
| Unknown | Everything after the report. | Outcome; what was accessed. |

**Correction:** the earlier record listed a Sri Lanka CERT inquiry as confirmed. The article states it without attribution, and the CERT officer quoted there was speaking about a different incident. It is now recorded as reported and unattributed.

## Sri Lanka Railways — INC-11 (corrected)

| Category | What the sources support |
| --- | --- |
| Confirmed incident | Railway officials said a cyberattack on 14 June 2026 affected the website's timetable section only. The Minister of Transport said on social media that the newly launched site was heavily attacked within hours of launch. |
| Allegations | None recorded. |
| Investigation announced | None found. No source mentions an inquiry or Sri Lanka CERT. |
| Confirmed remediation | The affected section was disabled; the Department said the website was back online on 15 June. |
| Unknown | The type of attack; when the timetable section returned; the site's launch date. |

**Correction:** `investigation_outcome` is now `NOT APPLICABLE`, because no investigation was announced. The conflicting reports on restoration (15 June and 17 June) are both recorded.

## National Medicines Regulatory Authority — INC-05 (corrected)

| Category | What the sources support |
| --- | --- |
| Confirmed incident | Files were found deleted from the Authority's back-end document system on 9 July 2021. Police said on 28 September 2021 that the CID had arrested an engineer of the contracted vendor. |
| Allegations | That the deletion was intentional (police), that it was an error (vendor), and that it was part of a wider conspiracy (state counsel in court). None was established in any source read. |
| Investigation announced | CID investigation with university forensic assistance. |
| Confirmed remediation | None confirmed. Recovery efforts were reported. |
| Unknown | The outcome of the prosecution; how much was recovered. |

**Correction:** competing explanations are now recorded as allegations and kept out of the confirmed column. This was a back-end system, not the public website.

## Summary across the six institutions

| Institution | Confirmed incidents | Investigation announced | Outcome | Remediation confirmed |
| --- | --- | --- | --- | --- |
| Education | 1 | Yes | Unknown | Site restored |
| Public Security | 1 | Yes | Unknown | Site restored |
| Government Printing | 1 | Yes | Unknown | Site restored; replacement planned |
| Public Administration | 2 | Yes, for 2026 | Unknown | None found |
| Railways | 1 | None found | Not applicable | Site back online |
| NMRA | 1 (back-end) | Yes | Unknown | None confirmed |

## Other changes in this review

- `investigation_status` was renamed `investigation_announced`; `remediation` was renamed `remediation_confirmed`; `investigation_outcome`, `additional_source_urls` and `sources_opened` were added.
- The Government Information Center moved to the reserve list to keep the selection at ten. Its "no incident found" record (INC-18) is kept, since incident IDs are never reused.
- The national research matrix is now generated from the data files, so it cannot drift from them.

## Unresolved source-verification tasks

- [ ] Locate Sri Lanka CERT's own statement, report or annual-report entry for INC-20, INC-02, INC-01 and INC-04
- [ ] Locate the Police Media Division release for INC-01
- [ ] Open the Sunday Times article of 5 January 2025 in full (INC-02 main source, read as an excerpt)
- [ ] Find the Ministry of Education's own statement of 5–6 April 2024
- [ ] Establish whether the Education and Government Printing replacement websites were launched, from published announcements only
- [ ] Search court reporting for the outcome of the INC-05 prosecution
- [ ] Check Hansard and parliamentary committee records for statements on any of the six
- [ ] Complete domain verification for moe.gov.lk through the government portal and one other government source
- [ ] Save dated copies of every source
