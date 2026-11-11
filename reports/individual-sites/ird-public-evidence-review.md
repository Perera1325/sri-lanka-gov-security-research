# IRD public evidence review

| | |
| --- | --- |
| Site | Inland Revenue Department, `ird.gov.lk` (site ID `IRD`) |
| Review date | 2026-11-11 (revised the same day after a source-verification pass; see [review report](../../docs/reviews/pr-1-ird-evidence-review.md)) |
| Method | Web search and reading of existing third-party publications only |
| Requests made to ird.gov.lk | None |
| Website assessment status | Not started (domain status is `PRELIMINARY`) |

This review collects what has already been published about the IRD website and the systems around it. It contains no observation of the website itself, assigns no severity and identifies no vulnerability or security concern.

## How to read this document

### Labels

| Label | Meaning here |
| --- | --- |
| VERIFIED PUBLIC FACT | A named, published source states this. It is a fact about what was published, not about the live site. |
| OBSERVED CONFIGURATION | Seen directly on the site in a browser. **No entry has this label.** |
| POTENTIAL SECURITY CONCERN | Published evidence that points to a security weakness. **No entry has this label.** |
| NOT TESTED | Cannot be determined without activity outside the passive scope. |
| NO EVIDENCE AVAILABLE | Looked for and not found, could not be retrieved, or reported only by a source that cannot be relied on. |

### Source types

| Source type | Meaning | Entries |
| --- | --- | --- |
| Primary | Published by the body responsible for the fact | 01, 03, 14, 19 |
| Official document, republished | An IRD document hosted by a third party; the original sits on IRD's own site, which has not been visited | 02, 07, 11, 12 |
| Secondary news | A news outlet reporting on a decision, report or warning | 09, 10, 13, 17 |
| Third-party directory | A listing maintained by an unrelated organization | 04 |
| None | No usable source | 05, 06, 08, 15, 16, 18 |

### Confidence

| Confidence | Rule applied |
| --- | --- |
| High | Primary source or official document, and the cited statement was read in it. |
| Medium | Secondary news that attributes the fact to a named official body, or a primary source where the relevant part was not fully seen, or a document old enough that the position may have changed. |
| Low | A single unattributed or company-sourced report, an old directory entry, or an inference. |

Confidence describes how well the source supports the statement as published. It is not a rating of security risk.

### Limits that apply to every entry

- Entries 10, 13, 14, 17 and 18 were opened and read on the review date (14 only in part). All other entries were read as search-result excerpts.
- No source has yet been saved. Before any entry is relied on or cited, open the source, read it in full and save a dated copy under `evidence/sources/IRD/`.
- Third-party records describe the past and do not prove anything about the site today.

These entries use `IRD-PUB-nn` IDs. They are background records, not site observations, so they are not in the [evidence register](../../evidence/evidence-register.csv), which remains empty.

## 1. Domain ownership and official identity

### IRD-PUB-01 — gov.lk is a restricted namespace

- **Label:** VERIFIED PUBLIC FACT
- **Source type:** Primary (domain registry)
- **Observation date:** 2026-11-11
- **Source URL:** <https://domains.lk/lk-domain-naming-structure/>
- **Description:** The LK Domain Registry states that `gov.lk` is a closed second-level domain for government organizations and departments, with registrations handled by LGII under ICTA's domain policy. The page carries no visible publication date.
- **Evidence type:** Registry policy page
- **Confidence:** High
- **Security relevance:** Supports that a `gov.lk` name can be registered only by a government body.
- **Limitations:** A namespace rule, not a record for this specific domain.
- **Recommended next step:** Save a dated copy. Use the registry's public WHOIS, or the registry contact listed on that page, for the specific record.

### IRD-PUB-02 — The Department's own notices name the domain

- **Label:** VERIFIED PUBLIC FACT
- **Source type:** Official document, republished
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2025/april-2025/Tax-Flash-News-Circulars-Issued-by-the-Department-of-Inland-Revenue.pdf>
- **Description:** A KPMG Sri Lanka tax bulletin dated April 2025 reproduces an IRD circular whose letterhead gives `www.ird.gov.lk` as the Department's website. Other IRD notices republished by third parties, dated between 2021 and 2026, give the same domain.
- **Evidence type:** Official circular reproduced in a third-party bulletin
- **Confidence:** High
- **Security relevance:** Independent naming of the domain, which is the second verification check.
- **Limitations:** A reproduced copy. The circular's own issue date was not captured.
- **Recommended next step:** Save a dated copy of this PDF and of one other independent source, and record the circular's number and date.

### IRD-PUB-03 — The Ministry of Finance lists the Department

- **Label:** VERIFIED PUBLIC FACT
- **Source type:** Primary (government website)
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.treasury.gov.lk/web/ta-about/section/departments>
- **Description:** The Ministry of Finance website's menu of departments includes the Department of Inland Revenue.
- **Evidence type:** Government website navigation
- **Confidence:** Medium
- **Security relevance:** Confirms the institution's place in government. It does not by itself confirm the domain.
- **Limitations:** The excerpt read did not show where the menu entry links to.
- **Recommended next step:** Open the page in a browser and record the link target.

### IRD-PUB-04 — Historical research lead: an older domain name in a directory

- **Label:** VERIFIED PUBLIC FACT (historical lead only)
- **Source type:** Third-party directory
- **Observation date:** 2026-11-11
- **Source URL:** <https://edirc.repec.org/data/dirgvlk.html>
- **Description:** The EDIRC directory of economics institutions lists `inlandrevenue.gov.lk` as the Department's homepage. The entry carries no date.
- **Evidence type:** Third-party directory listing
- **Confidence:** Low
- **Security relevance:** None established. This is recorded as a lead about the Department's naming history, not as a current concern.
- **Limitations:** Directory entries can be many years out of date. Nothing is known about the name's current registration or use, and no claim is made about it.
- **Recommended next step:** Check the name's registration through the registry's public WHOIS only. Do not visit or probe it.

## 2. Public DNS information

### IRD-PUB-05 — No DNS records retrieved

- **Label:** NO EVIDENCE AVAILABLE
- **Source type:** None
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** No existing published DNS record for `ird.gov.lk` was retrieved in this review.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Public DNS records would show name servers and whether email-authentication records are published.
- **Limitations:** Absence here reflects this review's reach, not the domain.
- **Recommended next step:** Manual lookup with a public DNS lookup service, as set out in the [observation plan](../../research/observations/IRD-observation-plan.md). Also pull the IRD row from the LDFLK scorecard dataset.

## 3. Certificate transparency

### IRD-PUB-06 — Certificate log not retrieved

- **Label:** NO EVIDENCE AVAILABLE
- **Source type:** None
- **Observation date:** 2026-11-11
- **Source URL:** <https://crt.sh/?q=ird.gov.lk> (not reachable from the research environment)
- **Description:** The public certificate transparency search could not be opened from the environment used for this review, so no certificate data is recorded.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Logs show the issuer and validity period of certificates issued for the domain.
- **Limitations:** Nothing was seen.
- **Recommended next step:** Open the URL above in a browser and save the result privately. Record in this repository only the issuer and validity dates for `www.ird.gov.lk`. Do not publish a list of other host names found there.

## 4. Publicly identified technologies and related advisories

### IRD-PUB-07 — Published IRD links follow a recognizable URL pattern

- **Label:** VERIFIED PUBLIC FACT for the published links only. The technology identification is an **unconfirmed inference** and carries no label.
- **Source type:** Official document, republished
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2025/october-2025/Tax%20Flash%20News%20-%20Inland%20Revenue%20Department%20Reminds%20Taxpayers%20to%20Update%20Profile%20Information.pdf>
- **Description:** An IRD public notice dated 8 October 2025, reproduced by KPMG, prints links to the Department's public guidance pages whose paths end in the form `/sitepages/<page>.aspx`. **Unconfirmed inference:** this path form is commonly associated with Microsoft SharePoint. The site's platform has not been identified.
- **Evidence type:** URLs printed in an official notice
- **Confidence:** High that the links were published in this form; Low for the inference
- **Security relevance:** None at present. A platform would need to be confirmed by an explicit marker before any comparison with vendor advisories.
- **Limitations:** A URL form is not an explicit marker and can be produced by other software. It indicates nothing about product, edition, version or patch level.
- **Recommended next step:** Checklist item C06 in the browser: look for an explicit marker. Until then, do not describe the site as running any named product.

### IRD-PUB-08 — No advisory mapped

- **Label:** NO EVIDENCE AVAILABLE
- **Source type:** None
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** No product or version for the website has been identified, so no security advisory has been matched to it.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Matching advisories to an unconfirmed product would be speculation.
- **Limitations:** Even with a confirmed version, whether an advisory applies to this site would be NOT TESTED.
- **Recommended next step:** Revisit after C06 and C07 are completed in the browser.

## 5. Publicly documented third-party arrangements (context only, out of scope)

Entries 09 to 12 describe back-end, API and payment arrangements. They are recorded **only as context** for understanding who is involved in IRD's digital services. These systems are out of scope, will not be examined, and no technical detail about them is recorded here.

### IRD-PUB-09 — Cabinet approved engaging NCS to upgrade RAMIS

- **Label:** VERIFIED PUBLIC FACT (context only)
- **Source type:** Secondary news
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.ft.lk/news/Sri-Lanka-moves-toward-electronic-invoicing-with-RAMIS-upgrade/56-785139>
- **Description:** Daily FT reported on 3 December 2025 that the Cabinet of Ministers approved engaging Singapore-based NCS to upgrade the Revenue Administration Management Information System (RAMIS). Daily Mirror carried a matching report on the same date. Earlier press reports describe NCS as the system's original solution provider; that history has not been checked against a primary source.
- **Evidence type:** Two news reports of a Cabinet decision
- **Confidence:** Medium
- **Security relevance:** Context only: identifies a vendor relationship behind IRD's e-services.
- **Limitations:** Secondary reporting. Describes the back-end tax system, not the public website.
- **Recommended next step:** Locate the Cabinet Office's published decision and cite it as the primary source.

### IRD-PUB-10 — A local firm was reported in 2018 to support RAMIS

- **Label:** VERIFIED PUBLIC FACT (context only, historical)
- **Source type:** Secondary news, company-sourced
- **Observation date:** 2026-11-11
- **Source URL:** <https://ft.lk/it-telecom-tech/N-Able-successfully-completes-2-years-of-partnership-with-RAMIS-customer-support-centre/50-648569>
- **Description:** A Daily FT article dated 2 February 2018 states that N*Able had completed two years running the RAMIS customer support centre as a partner of NCS. The article relies on the company's own account.
- **Evidence type:** News article based on a company statement
- **Confidence:** Low as to the present arrangement
- **Security relevance:** Context only.
- **Limitations:** More than eight years old and promotional in tone. Whether the arrangement continues is unknown.
- **Recommended next step:** Treat as historical unless a current, independent source is found.

### IRD-PUB-11 — IRD has announced an e-invoicing data link for VAT

- **Label:** VERIFIED PUBLIC FACT (context only). The interface is out of scope and NOT TESTED.
- **Source type:** Official document, republished
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmgsites/lk/pdf/kpmg-tax-news/2026/may/Notice-to-the-VAT-Registered-Persons-VAT-Invoice-Data-Integration.pdf>
- **Description:** IRD notice SEC/PN/VAT/2026-03, dated 4 May 2026 and reproduced by KPMG, announces a National e-Invoicing System under which VAT-registered persons' systems transmit invoice data to RAMIS through a web interface, introduced in phases. The notice also states an intention to use Sri Lanka Customs data to pre-fill certain schedules.
- **Evidence type:** Official notice reproduced by a third party
- **Confidence:** High
- **Security relevance:** Context only: shows that system-to-system data exchange is part of IRD's services.
- **Limitations:** The notice describes policy and phasing. No technical detail was sought or recorded.
- **Recommended next step:** None. Any examination would require written authorization from IRD.

### IRD-PUB-12 — Online tax payment is made through commercial banks

- **Label:** VERIFIED PUBLIC FACT (context only). The payment flow is out of scope and NOT TESTED.
- **Source type:** Official document, republished
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.taxadvisor.lk/data/uploads/overview_and_quick_guides_09_02_2021.pdf>
- **Description:** An IRD user guide for its Online Tax Payments Platform, hosted by a tax-information site in a file dated 9 February 2021, describes taxpayers paying through their own bank's internet banking, with LankaClear handling the transfer between the bank and IRD. Third-party tax news reported the platform as effective from 8 February 2021.
- **Evidence type:** Official user guide hosted by a third party
- **Confidence:** Medium
- **Security relevance:** Context only: according to the guide, the taxpayer starts the payment in the bank's system.
- **Limitations:** The guide is from 2021 and the arrangement may have changed. It was read as an excerpt.
- **Recommended next step:** None within passive scope.

## 6. Existing public assessments and reported incidents

### IRD-PUB-13 — A World Bank review was reported to comment on IRD's IT capacity

- **Label:** VERIFIED PUBLIC FACT (context only)
- **Source type:** Secondary news
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.ft.lk/top-story/Underperforming-Rs-10-b-RAMIS-system-at-risk/26-781759>
- **Description:** Daily FT reported on 17 September 2025 that the World Bank's *Sri Lanka Public Finance Review – Towards a Balanced Fiscal Adjustment* described weaknesses in IT capacity, governance and vendor management at IRD in relation to RAMIS.
- **Evidence type:** News report of an institutional review
- **Confidence:** Medium
- **Security relevance:** None stated by the source. The article does not mention information security.
- **Limitations:** Secondary reporting of a review about tax administration performance. It is not a security assessment and says nothing about the website.
- **Recommended next step:** Read the World Bank report itself and cite it directly if it is used.

### IRD-PUB-14 — The Auditor General reports annually on the Department

- **Label:** VERIFIED PUBLIC FACT (context only)
- **Source type:** Primary (National Audit Office)
- **Observation date:** 2026-11-11
- **Source URL:** <https://naosl.gov.lk/web/images/audit-reports/upload/2024/1-Min_Dep/1-XXV/Head-246-Department-of-Inland-Revenue-E.pdf>
- **Description:** The National Audit Office's report on Head 246, Department of Inland Revenue, for the year ended 31 December 2024 records, among other matters, an error in data supplied through RAMIS that was later corrected.
- **Evidence type:** Official audit report
- **Confidence:** High for the statement above
- **Security relevance:** None found. In the portion read, the report makes no information-security observation.
- **Limitations:** A financial audit. Roughly the first three-fifths of the document was read.
- **Recommended next step:** Read the remainder and record whether any information-systems section exists.

### IRD-PUB-15 — No public technical assessment of the website found

- **Label:** NO EVIDENCE AVAILABLE
- **Source type:** None
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** No published technical security assessment specific to `ird.gov.lk` was found. The LDFLK government website scorecard was not located by search.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** There is no prior baseline to compare against.
- **Limitations:** A search miss is not proof that none exists.
- **Recommended next step:** Extract the IRD row from the LDFLK scorecard dataset and record its date and fields.

### IRD-PUB-16 — No reported compromise of the IRD website found

- **Label:** NO EVIDENCE AVAILABLE
- **Source type:** None
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** Searches found no report of a breach or defacement of the IRD website or RAMIS. For clarity: an intrusion reported by [News 1st on 22 April 2026](https://english.newsfirst.lk/2026/4/22/hackers-infiltrate-sri-lanka-s-finance-ministry-system-probe-underway-into-theft) concerned the External Resources Department of the Ministry of Finance, a separate department, and is not attributed to IRD.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** None.
- **Limitations:** Unreported incidents would not appear in a news search.
- **Recommended next step:** None.

### IRD-PUB-17 — CERT was reported to warn of callers impersonating IRD

- **Label:** VERIFIED PUBLIC FACT (context only)
- **Source type:** Secondary news
- **Observation date:** 2026-11-11
- **Source URL:** <https://hirunews.lk/english/470166/scammers-pose-as-inland-revenue-officials-in-new-fraud-attempt>
- **Description:** Hiru News reported on 4 June 2026 that Sri Lanka CERT warned the public about telephone callers posing as IRD officials who then sought to send a payment link by messaging app or email, and that IRD does not send payment links to taxpayers.
- **Evidence type:** News report of a CERT warning
- **Confidence:** Medium
- **Security relevance:** Context only: the Department's name has been used in fraud against taxpayers. The report indicates no weakness in IRD's website or systems.
- **Limitations:** Secondary reporting; CERT's own notice was not located.
- **Recommended next step:** Look for the original warning on Sri Lanka CERT's site and cite that instead.

### IRD-PUB-18 — National monitoring of IRD: not confirmed

- **Label:** NO EVIDENCE AVAILABLE (an unattributed report is noted)
- **Source type:** None usable
- **Observation date:** 2026-11-11
- **Source URL:** <https://themorningtelegraph.com/41586/>
- **Description:** An article dated 25 April 2026 on one news site says that the National Cyber Security Operations Centre monitors 37 government institutions and names the Inland Revenue Department among them. The article attributes this to no official or document, and no primary confirmation was found.
- **Evidence type:** Single unattributed news statement
- **Confidence:** Low
- **Security relevance:** None established.
- **Limitations:** One secondary source of unknown reliability. Not to be cited as fact.
- **Recommended next step:** Look for a statement from Sri Lanka CERT or the Ministry of Digital Economy. Drop the entry if none is found.

### IRD-PUB-19 — A national guideline exists for government websites

- **Label:** VERIFIED PUBLIC FACT
- **Source type:** Primary (Sri Lanka CERT)
- **Observation date:** 2026-11-11
- **Source URL:** <https://cert.gov.lk/wp-content/uploads/2023/07/Website-Security-Guidelines-for-Government-Organizations_2022.pdf>
- **Description:** Sri Lanka CERT has published *Website Security Guidelines for Government Organizations* (2022). The portion read refers to serving content over HTTPS and to protecting access to a site's back end.
- **Evidence type:** Official guideline
- **Confidence:** High
- **Security relevance:** Provides a local standard against which later browser observations can be compared.
- **Limitations:** Only an excerpt was read. Whether a later edition exists was not checked.
- **Recommended next step:** Read in full, confirm it is the current edition, and map checklist items C01 to C09 to its requirements.

## Summary

| Label | Count | Entries |
| --- | --- | --- |
| VERIFIED PUBLIC FACT | 13 | 01, 02, 03, 04, 07, 09, 10, 11, 12, 13, 14, 17, 19 |
| OBSERVED CONFIGURATION | 0 | |
| POTENTIAL SECURITY CONCERN | 0 | |
| NOT TESTED | 0 entries | Out-of-scope systems noted within 11 and 12 |
| NO EVIDENCE AVAILABLE | 6 | 05, 06, 08, 15, 16, 18 |

| Confidence | Entries |
| --- | --- |
| High | 01, 02, 07 (published links only), 11, 14, 19 |
| Medium | 03, 09, 12, 13, 17 |
| Low | 04, 10, 18, and the inference in 07 |
| Not applicable | 05, 06, 08, 15, 16 |

No severity is assigned to any entry, and nothing here is a finding against the IRD website.
