# Sri Lanka CERT web application guideline: requirement mapping

All 32 requirements of the guideline are listed below, each classed by how far it can be checked from public evidence. No requirement has been assessed for any institution, and this file makes no statement of compliance or non-compliance.

## The guideline

*Web Application Security Guidelines for Government Organizations*, Version 1, issued 22 February 2022, published on Sri Lanka CERT's website ([Sri Lanka CERT, 2022](https://cert.gov.lk/wp-content/uploads/2023/07/Web-Application-Security-Guidelines-for-Government-Organizations_2022.pdf)). It was opened and read on 2026-11-11. The document has no numbered clauses; the numbers below are added here, in the document's own order and under its own stage headings. Wording is paraphrased. Whether a later version exists was not checked.

It is a companion to the *Website Security Guidelines for Government Organizations* issued the same day, which is mapped in [cert-compliance-mapping.md](cert-compliance-mapping.md). The two overlap heavily; this one adds requirements for applications that provide services.

Every requirement is labelled **CONFIRMED PUBLIC SECURITY REQUIREMENT**.

## Classes

| Class | Meaning | How this study treats it |
| --- | --- | --- |
| Publicly observable | A visitor's browser, or the domain name, shows whether it is met. | Observed only on public, unauthenticated pages, after the domain is verified. |
| Officially documented | Not visible from outside, but an official publication may state it. | Recorded only when a published statement is found. |
| Not publicly verifiable | Internal practice. Only the institution or Sri Lanka CERT can confirm it. | Left as unknown. Never treated as unmet. |
| Requires written authorization | Could be tested technically, but only with the institution's written permission. | NOT TESTED. |

Where a requirement has parts that fall in different classes, both are given.

## Prior to development

| # | Requirement | Class | Note |
| --- | --- | --- | --- |
| 1 | Classify the criticality of the application's content and set security requirements accordingly, following CERT's Technical Guidelines. | Not publicly verifiable | Internal decision. |
| 2 | Include the mandatory security requirements from the Information and Cyber Security Implementation Guide in the tender document. | Officially documented | Checkable only where the tender document is published. |
| 3 | Include a tender clause requiring development and hosting in line with the Technical Guidelines. | Officially documented | As above. |

## Design and development

| # | Requirement | Class | Note |
| --- | --- | --- | --- |
| 4 | Develop the application following the Technical Guidelines for Web Application and Website Security. | Not publicly verifiable | |
| 5 | Use a `gov.lk` domain. | Publicly observable | Read from the domain name. |
| 6 | Validate input on both the client side and the server side. | Client side: publicly observable. Server side: requires written authorization | Server-side behaviour can only be shown by sending crafted input. |
| 7 | Restrict file uploads to the types the application specifies. | Requires written authorization | Would need an upload. |
| 8 | Take OWASP's web application security risks into account in development. | Not publicly verifiable | |
| 9 | Scan uploaded documents for malware; block encrypted or compressed files unless CERT approves an exception. | Not publicly verifiable | Testing it would require authorization. |
| 10 | Enable HTTPS; send login forms, credentials and tokens only over HTTPS. | Publicly observable for public pages | Login pages are out of scope and are not opened. |
| 11 | Use two-way SSL authentication for access to the back end or CMS. | Not publicly verifiable | Back-end interfaces are never approached. |
| 12 | Encrypt sensitive information in transit and at rest. | In transit: publicly observable. At rest: not publicly verifiable | |
| 13 | Apply integrity checks, such as digital signatures, to serialized objects. | Requires written authorization | |
| 14 | Limit third-party plugins and code, and assess their risk before deployment. | Presence of third-party scripts: publicly observable. The risk assessment: not publicly verifiable | |
| 15 | Harden the host server by removing or disabling unnecessary services. | Requires written authorization | Enumerating services is scanning. |
| 16 | Consider the Technical Guidelines' hosting-platform security requirements when selecting a host. | Not publicly verifiable | |
| 17 | Use CAPTCHA or two-factor authentication where possible, for example on login and contact forms. | Publicly observable for public forms | Presence can be seen without submitting a form. Effectiveness requires authorization. |
| 18 | Require multi-factor authentication for administrator access. | Not publicly verifiable | |
| 19 | Complete a security assessment through Sri Lanka CERT before production release. | Officially documented | Otherwise not publicly verifiable. |
| 20 | Obtain a legally binding assurance from the developer that the application meets the Technical Guidelines. | Not publicly verifiable | |
| 21 | Change or disable default and vendor-supplied passwords before production. | Requires written authorization | Never tested in this study. |
| 22 | Do not expose the database directly to users. | Requires written authorization | Checking would mean probing for services. |

## Deployment and maintenance

| # | Requirement | Class | Note |
| --- | --- | --- | --- |
| 23 | Host the application according to the secure hosting guidance in the Technical Guidelines. | Not publicly verifiable | |
| 24 | Grant access on a need-to-know, least-privilege basis; prohibit shared credentials. | Not publicly verifiable | |
| 25 | Secure and patch administrators' personal devices used for CMS access. | Not publicly verifiable | |
| 26 | Keep the application, CMS, database, operating system and web server patched. | Publicly observable only where a version is disclosed; otherwise not publicly verifiable | A disclosed version is not proof of patch level. |
| 27 | Route traffic through managed firewalls and a web application firewall; keep signatures updated. | Not publicly verifiable | Detecting a firewall by probing would require authorization. |
| 28 | Have Sri Lanka CERT carry out a security assessment at least annually, and after incidents, changes, standards updates or malware outbreaks. | Officially documented | Otherwise not publicly verifiable. |
| 29 | Carry out a comprehensive risk assessment before any change to the application or its environment. | Not publicly verifiable | |
| 30 | Maintain, back up and regularly archive audit trails. | Not publicly verifiable | |
| 31 | Keep an up-to-date copy of the application on a host not connected to the Internet, and keep regular backups. | Not publicly verifiable | |

## Retirement and disposal

| # | Requirement | Class | Note |
| --- | --- | --- | --- |
| 32 | Dispose of the application securely at decommissioning so that data cannot be recovered. | Not publicly verifiable | |

## Count by class

| Class | Requirements | Count |
| --- | --- | --- |
| Publicly observable (wholly or for public pages) | 5, 10, 17 | 3 |
| Mixed: one part publicly observable | 6, 12, 14, 26 | 4 |
| Officially documented | 2, 3, 19, 28 | 4 |
| Requires written authorization | 7, 13, 15, 21, 22 | 5 |
| Not publicly verifiable | 1, 4, 8, 9, 11, 16, 18, 20, 23, 24, 25, 27, 29, 30, 31, 32 | 16 |

Seven of the 32 requirements can be informed at all by passive observation, and four more only if an official body publishes a statement. Twenty-one cannot be checked by an outside researcher without authorization.

## Position for the ten institutions

The classification above applies equally to all ten institutions in the [inventory](../data/website-inventory.csv). For every institution, every requirement stands as follows:

- Requirement 5 is met by the domain name for all ten.
- Requirements 6 (client side), 10, 12 (in transit), 14 (presence), 17 and 26 are **not yet observed**.
- All remaining requirements are unknown.

Published statements that bear on a requirement for a named institution are listed here. Each is a statement about a past moment and none shows the present position.

| Institution | Requirement | Published statement | Source type | Incident |
| --- | --- | --- | --- | --- |
| Ministry of Education | 28 | Sri Lanka CERT was reported as saying it had advised an annual vulnerability assessment and that the Ministry had not carried one out before the April 2024 incident. | Secondary news; CERT's own statement not found | INC-20 |
| Ministry of Education | 26 | An article said, without naming its source, that security patches and updates had not been applied before the April 2024 incident. | Secondary news, unattributed | INC-20 |
| Department of Government Printing | 28 | A named CERT engineer was reported as saying CERT audited the old website after the December 2024 incident. | Secondary news | INC-02 |
| Department of Government Printing | 19 | The Government Printer was reported as saying the replacement website would be audited by CERT before going live. | Secondary news | INC-02 |
| Ministry of Public Security | 28 | Police said Sri Lanka CERT and ICTA restored the website after the January 2026 incident. Whether an assessment was carried out is not stated. | Secondary news of a police statement | INC-01 |
| National Medicines Regulatory Authority | 31 | Press reports said no backup existed for files deleted from a back-end system in 2021. | Secondary news | INC-05 |

Incident details are in the [historical incident timeline](../reports/historical-incident-timeline.md).

## Limits

- The requirement list comes from a reading of the published PDF through a text extraction. Check it against the original before quoting any requirement.
- The Technical Guidelines and the Minimum Information Security Standards that this guideline cites were not read. They contain the detailed controls.
- A guideline is not a statute. This file takes no position on whether following it is mandatory for any institution.
