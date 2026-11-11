# IRD public evidence review

| | |
| --- | --- |
| Site | Inland Revenue Department, `ird.gov.lk` (site ID `IRD`) |
| Review date | 2026-11-11 |
| Method | Web search of existing third-party publications only |
| Requests made to ird.gov.lk | None |
| Website assessment status | Not started (domain status is `PRELIMINARY`) |

This review collects what third parties have already published about the IRD website and the systems around it. It contains no observation of the website itself and identifies no vulnerability.

## How to read this document

Each entry carries one of five labels.

| Label | Meaning here |
| --- | --- |
| VERIFIED PUBLIC FACT | Stated in a named, published source. It is a fact about what was published, not about the live site. |
| OBSERVED CONFIGURATION | Seen directly on the site in a browser. **No entry has this label yet.** |
| POTENTIAL SECURITY CONCERN | A published statement that points to a risk area worth attention. Not a finding. |
| NOT TESTED | Cannot be determined without activity outside the passive scope. |
| NO EVIDENCE AVAILABLE | Looked for and not found, or could not be retrieved in this review. |

**Limits that apply to every entry.** Sources were read as search-result excerpts on the review date, not as saved full pages. Before any entry is relied on or cited, open the source, read it in full and save a dated copy under `evidence/sources/IRD/`. Third-party records describe the past and do not prove anything about the site today.

These entries use `IRD-PUB-nn` IDs. They are background records, not site observations, so they are not in the [evidence register](../../evidence/evidence-register.csv), which remains empty.

## 1. Domain ownership and official identity

### IRD-PUB-01 — gov.lk is a restricted namespace

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://domains.lk/lk-domain-naming-structure/>
- **Description:** The LK Domain Registry states that `gov.lk` is a closed second-level domain for government organizations and departments, with registrations handled by LGII under ICTA's domain policy.
- **Evidence type:** Registry policy page
- **Confidence:** High
- **Security relevance:** Supports that `ird.gov.lk` could only have been registered by a government body.
- **Limitations:** A namespace rule, not a record for this specific domain.
- **Recommended next step:** Save a dated copy. Ask LGII (`hostmaster@gov.lk`, listed on the same page) or use the registry's public WHOIS for the specific record.

### IRD-PUB-02 — The Department's own notices name the domain

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2025/april-2025/Tax-Flash-News-Circulars-Issued-by-the-Department-of-Inland-Revenue.pdf>
- **Description:** A 2025 IRD circular, republished by KPMG Sri Lanka, gives the Department's address, `www.ird.gov.lk` as its website and `@ird.gov.lk` email contacts. Other IRD notices from 2021 to 2026 republished by third parties give the same domain.
- **Evidence type:** Official document republished by a third party
- **Confidence:** High
- **Security relevance:** Independent naming of the domain, which is the second verification check.
- **Limitations:** Republished copy; the original sits on the site itself.
- **Recommended next step:** Save a dated copy of this PDF and one other independent source.

### IRD-PUB-03 — The Ministry of Finance lists the Department

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.treasury.gov.lk/web/ta-about/section/departments>
- **Description:** The Ministry of Finance website lists the Department of Inland Revenue among its departments.
- **Evidence type:** Government website navigation
- **Confidence:** Medium
- **Security relevance:** Confirms the institution's place in government. A link from this page to `ird.gov.lk` would be a strong second source.
- **Limitations:** The excerpt read did not show where the menu entry links to.
- **Recommended next step:** Open the page in a browser and record the link target.

### IRD-PUB-04 — An older domain name appears in a directory

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://edirc.repec.org/data/dirgvlk.html>
- **Description:** The EDIRC directory lists `http://www.inlandrevenue.gov.lk/` as the Department's homepage.
- **Evidence type:** Third-party directory
- **Confidence:** Low as to current relevance
- **Security relevance:** Old official names matter for impersonation risk if they lapse or point elsewhere.
- **Limitations:** Directory entries can be many years out of date. Nothing is known about the name's current state.
- **Recommended next step:** Check the name's registration through the registry's public WHOIS only. Do not probe it.

## 2. Public DNS information

### IRD-PUB-05 — No DNS records retrieved

- **Label:** NO EVIDENCE AVAILABLE
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** No existing published DNS record for `ird.gov.lk` was retrieved in this review.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Name servers, mail records and the SPF and DMARC text records indicate hosting arrangements and email-spoofing protections.
- **Limitations:** Absence here reflects this review's reach, not the domain.
- **Recommended next step:** Manual lookup with a public DNS lookup service, as set out in the [observation plan](../../research/observations/IRD-observation-plan.md). Also pull the IRD row from the LDFLK scorecard dataset.

## 3. Certificate transparency

### IRD-PUB-06 — Certificate log not retrieved

- **Label:** NO EVIDENCE AVAILABLE
- **Observation date:** 2026-11-11
- **Source URL:** <https://crt.sh/?q=ird.gov.lk> (not reachable from the research environment)
- **Description:** The public certificate transparency search could not be opened from the environment used for this review, so no certificate data is recorded.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Logs show issuer, validity period and the host names certificates were issued for.
- **Limitations:** None recorded; nothing was seen.
- **Recommended next step:** Open the URL above in a browser and save the result page. Host names found there are noted only; out-of-scope hosts are not visited.

## 4. Publicly identified technologies and related advisories

### IRD-PUB-07 — Published IRD links follow a recognizable URL pattern

- **Label:** VERIFIED PUBLIC FACT (the inference below is unconfirmed)
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2025/october-2025/Tax%20Flash%20News%20-%20Inland%20Revenue%20Department%20Reminds%20Taxpayers%20to%20Update%20Profile%20Information.pdf>
- **Description:** IRD notices publish links of the form `/en/eServices/sitepages/Registration.aspx?menuid=…` and `/en/eServices/Lists/…/Attachments/…`. **Inference:** this path structure is characteristic of Microsoft SharePoint on ASP.NET.
- **Evidence type:** URLs printed in official notices
- **Confidence:** High that the URLs were published; Low for the technology inference
- **Security relevance:** Knowing the platform allows comparison with the vendor's public advisories, but only once a product and version are confirmed.
- **Limitations:** A URL pattern is not an explicit marker. It says nothing about product edition, version or patch level.
- **Recommended next step:** Checklist item C06 in the browser: look for an explicit marker such as a generator tag or platform response header.

### IRD-PUB-08 — No advisory mapped

- **Label:** NO EVIDENCE AVAILABLE
- **Observation date:** 2026-11-11
- **Source URL:** None
- **Description:** No product version for the website has been publicly identified, so no security advisory has been matched to it.
- **Evidence type:** None
- **Confidence:** Not applicable
- **Security relevance:** Matching advisories to an unconfirmed product would be speculation.
- **Limitations:** Even with a confirmed version, whether an advisory applies to this site is NOT TESTED.
- **Recommended next step:** Revisit after C06 and C07 are completed in the browser.

## 5. Publicly documented third-party integrations

All systems in this section are e-services, payment or API systems. They are **out of scope** and are recorded only as context.

### IRD-PUB-09 — RAMIS is supplied and supported by NCS of Singapore

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.ft.lk/news/Sri-Lanka-moves-toward-electronic-invoicing-with-RAMIS-upgrade/56-785139>
- **Description:** Daily FT reported on 3 December 2025 that the Cabinet approved engaging Singapore-based NCS to upgrade the Revenue Administration Management Information System (RAMIS). Daily Mirror reported the same decision.
- **Evidence type:** News report of a Cabinet decision
- **Confidence:** High
- **Security relevance:** Identifies the main vendor dependency behind IRD's e-services.
- **Limitations:** Describes the back-end tax system, not the public website.
- **Recommended next step:** Locate the Cabinet Office's own published decision as the primary source.

### IRD-PUB-10 — A local firm has run RAMIS support

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://ft.lk/it-telecom-tech/N-Able-successfully-completes-2-years-of-partnership-with-RAMIS-customer-support-centre/50-648569>
- **Description:** Daily FT reported that N*Able operated the RAMIS customer support centre in partnership with NCS.
- **Evidence type:** News report
- **Confidence:** Medium
- **Security relevance:** A further party in the support chain.
- **Limitations:** The article's date was not captured and the arrangement may have ended.
- **Recommended next step:** Record the publication date; treat as historical unless a current source is found.

### IRD-PUB-11 — A Web API links taxpayers' systems to RAMIS

- **Label:** VERIFIED PUBLIC FACT; the API itself is NOT TESTED
- **Observation date:** 2026-11-11
- **Source URL:** <https://assets.kpmg.com/content/dam/kpmgsites/lk/pdf/kpmg-tax-news/2026/may/Notice-to-the-VAT-Registered-Persons-VAT-Invoice-Data-Integration.pdf>
- **Description:** IRD notice SEC/PN/VAT/2026-03 of 4 May 2026 announces a National e-Invoicing System in which a Web API transmits VAT invoice data from taxpayers' ERP systems to RAMIS, with planned use of Sri Lanka Customs data.
- **Evidence type:** Official notice republished by a third party
- **Confidence:** High
- **Security relevance:** A new machine-to-machine interface and a data link with another agency.
- **Limitations:** The notice describes intent and phases, not implementation.
- **Recommended next step:** None within passive scope. Any examination needs written authorization.

### IRD-PUB-12 — Online tax payments run through LankaClear and commercial banks

- **Label:** VERIFIED PUBLIC FACT; the payment flow is NOT TESTED
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.taxadvisor.lk/data/uploads/overview_and_quick_guides_09_02_2021.pdf>
- **Description:** IRD's user guide for its Online Tax Payments Platform, in use since February 2021, states that payments are made through participating banks' internet banking and that LankaClear's online payment platform handles the fund transfer.
- **Evidence type:** Official user guide republished by a third party
- **Confidence:** High
- **Security relevance:** Payment is initiated at the bank, not on the IRD website.
- **Limitations:** A 2021 guide; arrangements may have changed.
- **Recommended next step:** None within passive scope.

## 6. Existing public assessments and reported incidents

### IRD-PUB-13 — World Bank comments on IRD's IT capacity

- **Label:** POTENTIAL SECURITY CONCERN (organizational, not about the website)
- **Observation date:** 2026-11-11
- **Source URL:** <https://www.ft.lk/top-story/Underperforming-Rs-10-b-RAMIS-system-at-risk/26-781759>
- **Description:** Daily FT reported that a World Bank public finance review described weaknesses in IT capacity, governance and vendor management at IRD in relation to RAMIS.
- **Evidence type:** News report of an institutional assessment
- **Confidence:** Medium (secondary reporting)
- **Security relevance:** Limited in-house capacity and vendor dependence are general risk factors for maintaining any system.
- **Limitations:** The review concerns tax administration performance. It is not a security assessment and says nothing about the website's configuration.
- **Recommended next step:** Read the World Bank report itself and cite it directly.

### IRD-PUB-14 — Auditor General's reports cover the Department

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://naosl.gov.lk/web/images/audit-reports/upload/2024/1-Min_Dep/1-XXV/Head-246-Department-of-Inland-Revenue-E.pdf>
- **Description:** The National Audit Office publishes annual reports on Head 246, the Department of Inland Revenue. The 2024 report refers to errors in information supplied through RAMIS that were later corrected.
- **Evidence type:** Official audit report
- **Confidence:** Medium (excerpt only)
- **Security relevance:** Background on system governance and data accuracy.
- **Limitations:** These are financial audits. No security finding has been read in them.
- **Recommended next step:** Read the full reports for any information-systems section.

### IRD-PUB-15 — No public technical assessment of the website found

- **Label:** NO EVIDENCE AVAILABLE
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
- **Observation date:** 2026-11-11
- **Source URL:** <https://english.newsfirst.lk/2026/4/22/hackers-infiltrate-sri-lanka-s-finance-ministry-system-probe-underway-into-theft> (a different department)
- **Description:** Searches found no report of a breach or defacement of the IRD website or RAMIS. A widely reported April 2026 intrusion affected the External Resources Department of the Ministry of Finance, which is a separate department and system.
- **Evidence type:** News search
- **Confidence:** Low (absence of reports)
- **Security relevance:** Shows why incidents elsewhere in the ministry must not be attributed to IRD.
- **Limitations:** Unreported incidents would not appear.
- **Recommended next step:** None.

### IRD-PUB-17 — Fraudsters have impersonated IRD officials

- **Label:** POTENTIAL SECURITY CONCERN (impersonation, not a website weakness)
- **Observation date:** 2026-11-11
- **Source URL:** <https://hirunews.lk/english/470166/scammers-pose-as-inland-revenue-officials-in-new-fraud-attempt>
- **Description:** Hiru News reported on 4 June 2026 that Sri Lanka CERT warned of callers posing as IRD officials and sending fraudulent payment links, and that IRD does not send payment links to taxpayers.
- **Evidence type:** News report of a CERT warning
- **Confidence:** Medium
- **Security relevance:** IRD's name is being used in fraud, which makes clear domain identity and email-authentication records more valuable.
- **Limitations:** The incident involved phone calls. It does not indicate any fault in IRD's systems.
- **Recommended next step:** Record the domain's SPF and DMARC records from public DNS (see IRD-PUB-05).

### IRD-PUB-18 — IRD is reported to be under national monitoring

- **Label:** VERIFIED PUBLIC FACT (single secondary source)
- **Observation date:** 2026-11-11
- **Source URL:** <https://themorningtelegraph.com/41586/>
- **Description:** One news site reports that the National Cyber Security Operations Centre monitors 37 government institutions, naming the Inland Revenue Department among them.
- **Evidence type:** News report
- **Confidence:** Low
- **Security relevance:** Suggests a defensive control exists at national level.
- **Limitations:** One secondary source of unknown reliability.
- **Recommended next step:** Find a Sri Lanka CERT or government statement before citing.

### IRD-PUB-19 — A national benchmark exists for government websites

- **Label:** VERIFIED PUBLIC FACT
- **Observation date:** 2026-11-11
- **Source URL:** <https://cert.gov.lk/wp-content/uploads/2023/07/Website-Security-Guidelines-for-Government-Organizations_2022.pdf>
- **Description:** Sri Lanka CERT has published website security guidelines for government organizations (2022), covering matters such as HTTPS and protection of the site's back end.
- **Evidence type:** Official guideline
- **Confidence:** High
- **Security relevance:** Gives a local standard against which browser observations can be compared.
- **Limitations:** Only an excerpt was read.
- **Recommended next step:** Read in full and map checklist items C01 to C09 to its requirements.

## Summary

| Label | Entries |
| --- | --- |
| VERIFIED PUBLIC FACT | 12 (IRD-PUB-01 to 04, 07, 09 to 12, 14, 18, 19) |
| OBSERVED CONFIGURATION | 0 |
| POTENTIAL SECURITY CONCERN | 2 (IRD-PUB-13, 17), neither about the website's configuration |
| NOT TESTED | 2 systems noted within IRD-PUB-11 and 12 |
| NO EVIDENCE AVAILABLE | 5 (IRD-PUB-05, 06, 08, 15, 16) |

No severity is assigned to any entry, and nothing here is a finding against the IRD website.
