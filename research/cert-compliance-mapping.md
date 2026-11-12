# Sri Lanka CERT guideline compliance mapping

This mapping records what the national guideline requires and how far each requirement can be checked from public evidence. It does not state that any institution fails any requirement: nothing has been observed yet, and most requirements cannot be checked from outside.

## The guideline

*Website Security Guidelines for Government Organizations*, Version 1, issued 22 February 2022, published on Sri Lanka CERT's website ([Sri Lanka CERT, 2022](https://cert.gov.lk/wp-content/uploads/2023/07/Website-Security-Guidelines-for-Government-Organizations_2022.pdf)). The document was opened and read on 2026-11-11. It has no numbered sections; requirements are grouped below under its own stage headings. Whether a later version exists was not checked.

Every requirement below is labelled **CONFIRMED PUBLIC SECURITY REQUIREMENT**. Wording is paraphrased.

## How each requirement can be checked

| Class | Meaning |
| --- | --- |
| Publicly observable | A visitor's browser, or the domain name itself, shows whether it is met. |
| Documented by an official source | Not visible from outside, but an official publication may state it. |
| Not publicly verifiable | Internal practice. Only the institution or Sri Lanka CERT can confirm it. |
| Requires written authorization | Could be tested technically, but only with the institution's written permission. |

## Requirements and their class

| # | Area | What the guideline requires | Stage | Class | How this study will treat it |
| --- | --- | --- | --- | --- | --- |
| R1 | Domain | Use a `gov.lk` domain name. | Design | Publicly observable | Read from the domain name. |
| R2 | HTTPS | Enable HTTPS; deliver login forms, credentials and tokens only over HTTPS. | Design | Publicly observable (public pages only) | Checklist C01, C02. Login pages are not opened. |
| R3 | Stable CMS version | Use the latest stable version of the content management system. | Design | Publicly observable only if the site discloses its version; otherwise not publicly verifiable | Checklist C06. No version is inferred. |
| R4 | Input validation | Validate input on both client and server side. | Design | Requires written authorization | NOT TESTED. |
| R5 | Back-end authentication and MFA | Mutual TLS for back-end or CMS access; multi-factor authentication for anyone with that access; strong password policy; no shared credentials. | Design, Maintenance | Not publicly verifiable | NOT TESTED. Admin interfaces are never opened. |
| R6 | Third-party components | Limit plugins and third-party code; carry out a risk assessment before deploying any component. | Design | The risk assessment is not publicly verifiable. The presence of third-party scripts is publicly observable. | Checklist C08 records presence only. |
| R7 | Secure configuration and patching | Change default credentials; keep CMS, database, operating system and web server patched. | Design, Maintenance | Partly publicly observable (response headers, version banners); patch state itself is not publicly verifiable | Checklist C03, C06, C07. |
| R8 | Security assessment | Assessment through Sri Lanka CERT before release, at least once a year, and after an incident or significant change. | Design, Maintenance | Documented by an official source, where one exists; otherwise not publicly verifiable | Record only published statements. |
| R9 | Backup and recovery | Keep a current copy of the website on a host not connected to the Internet; keep regular backups. | Maintenance | Not publicly verifiable | Record only published statements. |

The guideline also covers procurement clauses, file-upload scanning, encryption of sensitive data, CAPTCHA, vendor maintenance agreements, administrator devices and secure disposal. These are internal and are not mapped per institution.

## Mapping by institution

Key: **Met (by name)** = shown by the domain name. **Not yet observed** = publicly observable, but no observation has been made. **NPV** = not publicly verifiable. **Auth** = requires written authorization. A numbered note marks a published statement that bears on the requirement.

| ID | R1 Domain | R2 HTTPS | R3 CMS version | R4 Input validation | R5 Back-end auth, MFA | R6 Third-party | R7 Config, patching | R8 Assessment | R9 Backup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV ¹ | NPV |
| DGP | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | Documented ² | NPV |
| MPA | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV ³ | NPV |
| NMRA | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV ⁴ |
| MOE | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | Documented ⁵ | NPV |
| IRD | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV |
| DIE | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV |
| DMT | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV |
| MODE | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV |
| SLR | Met (by name) | Not yet observed | Not yet observed | Auth | NPV | Not yet observed | Not yet observed | NPV | NPV |

### Notes

1. **MPS, R8.** After the January 2026 incident (INC-01), Sri Lanka CERT and ICTA were reported to have restored the site and reinforced its security. Whether a formal assessment was carried out is not stated.
2. **DGP, R8.** After the December 2024 incident (INC-02), Sri Lanka CERT officials were reported as saying they audited the old website and recommended a new one. This documents that a post-incident assessment took place. It is secondary reporting, and it says nothing about annual assessments or the current site.
3. **MPA, R8.** After the April 2026 incident (INC-04), a Sri Lanka CERT inquiry was reported. Whether it included a website assessment is not stated.
4. **NMRA, R9.** In the 2021 incident (INC-05), press reports said no backup of the deleted files was available. That concerned a back-end document system in 2021, not the website, and does not show the position today.

5. **MOE, R7 and R8.** After the April 2024 incident (INC-20), Daily Mirror reported Sri Lanka CERT as saying it had advised the Ministry to carry out a vulnerability assessment annually and that this had not been done; the same article said, without naming a source, that security patches and updates had not been applied. These reported statements describe the website before April 2024. They are secondary reporting, CERT's own statement was not found, and they say nothing about the current website. Separately, the Ministry's 2022 performance report tabled in Parliament records preliminary work on a cyber security action plan and the establishment of a ministry incident response team ([Ministry of Education, 2023](https://www.parliament.lk/uploads/documents/paperspresented/1688705066068348.pdf)).

All incident references are in the [historical incident timeline](../reports/historical-incident-timeline.md).

## What this mapping supports, and what it does not

- **Supported:** all ten institutions use a `gov.lk` domain, as the guideline requires.
- **Supported:** for four institutions, published reports show Sri Lanka CERT was involved after an incident.
- **Not supported:** any statement that an institution does or does not comply with R2 to R9. R2, R3, R6 and R7 await browser observation. R4 needs authorization. R5, R8 and R9 can only be confirmed by the institution or by Sri Lanka CERT.

## Related guideline for web applications

Sri Lanka CERT issued a separate guideline for web applications on the same date. All 32 of its requirements are mapped in [cert-web-application-guideline-mapping.md](cert-web-application-guideline-mapping.md).

## National context

Two published statements explain why R8 matters, without bearing on any one institution:

- In January 2025 a deputy minister was reported as saying that Sri Lanka CERT assessed government websites on request and that acting on its recommendations depended on each website's owner, and that the government intended to make this mandatory ([Sunday Times, 2025](https://www.sundaytimes.lk/250105/news/mandatory-slcert-recommendations-for-state-websites-583837.html)).
- In April 2024 the Sunday Times reported its own check of 130 official websites and said about 27 percent lacked a valid certificate; it did not name them ([Sunday Times, 2024](https://www.sundaytimes.lk/240421/news/several-govt-websites-face-danger-of-attack-554746.html)). That figure is the newspaper's and has not been reproduced here.

## Next steps

- [ ] Check Sri Lanka CERT's site for a later version of the guideline and for the technical guideline it cites
- [ ] After each site is verified and observed, replace "Not yet observed" with the scorecard result and its evidence reference
- [ ] Consider asking Sri Lanka CERT whether it publishes any summary of assessments carried out
