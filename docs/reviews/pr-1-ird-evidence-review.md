# Review report: PR #1, IRD public evidence review

| | |
| --- | --- |
| Review date | 2026-11-11 |
| Scope | All six files changed in PR #1 |
| Method | Re-reading the files; opening five cited third-party sources to check dates and content |
| Website testing | None. No request was made to ird.gov.lk |
| Outcome | 14 corrections made; 11 source-verification tasks remain open |

The original draft overstated the strength of several entries. The main errors were two entries labelled as potential security concerns without a source that mentions security, one unattributed news claim labelled as a verified fact, and one undated article that turned out to be from 2018.

## Files reviewed

| File | Result |
| --- | --- |
| `reports/individual-sites/ird-public-evidence-review.md` | Rewritten; corrections 1 to 11 |
| `research/observations/IRD-observation-plan.md` | Corrections 12 to 14 |
| `reports/individual-sites/ird.gov.lk.md` | No change needed; contains no claim about the site |
| `data/scorecards/IRD-scorecard.csv` | No change; still blank |
| `scripts/validate.py` | No change needed; reads local files only |
| `README.md` | No change needed |

## Corrections made

| # | Entry | Problem | Correction |
| --- | --- | --- | --- |
| 1 | All 19 | Primary and secondary sources were not distinguished. | Added a `Source type` field to every entry and a table grouping entries by type. |
| 2 | All 19 | Confidence had no stated rule; some news reports were rated High. | Added a three-level rule. High is now reserved for primary sources and official documents. |
| 3 | 13 | Labelled POTENTIAL SECURITY CONCERN. On opening the article, it does not mention security. | Relabelled VERIFIED PUBLIC FACT (context only). Added the date (17 September 2025) and the World Bank report's title. |
| 4 | 17 | Labelled POTENTIAL SECURITY CONCERN, with a link to email authentication that the source does not support. | Relabelled VERIFIED PUBLIC FACT (context only). Removed the email-authentication inference. Description now states the channel reported (telephone calls). |
| 5 | 18 | Labelled VERIFIED PUBLIC FACT. The article attributes the claim to no official source. | Relabelled NO EVIDENCE AVAILABLE, with the report noted as unattributed. Added its date (25 April 2026). |
| 6 | 10 | Date missing; presented as a current arrangement. | Dated 2 February 2018. Marked historical and company-sourced. Confidence lowered to Low. |
| 7 | 09 | Title said NCS "supplied and supported" RAMIS; the cited article supports only the December 2025 upgrade decision. Confidence was High for news reporting. | Title and text limited to the Cabinet decision. Earlier history marked as unchecked. Confidence set to Medium. |
| 8 | 07 | Technology inference sat under a VERIFIED PUBLIC FACT label. One URL pattern quoted came from a different source than the one cited, and related to a payment guide. | Inference now explicitly unlabelled and unconfirmed. URL pattern generalized; the payment-related path and query parameters were removed. Notice date (8 October 2025) added. |
| 9 | 04 | Described as an impersonation risk, which no source supports. | Retitled as a historical research lead. Security relevance set to "none established". |
| 10 | 09 to 12 | Out-of-scope systems were described with more operational detail than needed. | Section retitled "context only, out of scope". Descriptions shortened. A registry contact email was removed from entry 01. |
| 11 | 14, 16, 12, 19 | Minor inaccuracies. | 14: year of account stated (year ended 31 December 2024) and noted as partly read. 16: unrelated incident moved out of the source field; confidence set to not applicable. 12: confidence lowered to Medium for age. 19: edition currency flagged. |
| 12 | Plan, Part A | The historical domain lookup appeared as a required verification step. | Marked optional and not a concern. |
| 13 | Plan, Part B | Instructions would have published host names from certificate logs and DNS output. | Raw output is to be kept private; the repository records only issuer, validity, and whether SPF and DMARC are published. |
| 14 | Plan, Parts C and D | Wording implied the platform inference was established; out-of-scope rows were loosely worded. | C06 now says to name no product without an explicit marker. API and payment rows marked out of scope. |

## Label and confidence check after correction

| Label | Count |
| --- | --- |
| VERIFIED PUBLIC FACT | 13 |
| NO EVIDENCE AVAILABLE | 6 |
| POTENTIAL SECURITY CONCERN | 0 |
| OBSERVED CONFIGURATION | 0 |

| Confidence | Count |
| --- | --- |
| High | 6 |
| Medium | 5 |
| Low | 3 |
| Not applicable | 5 |

## Unchanged, as required

- The evidence register has no rows.
- The IRD scorecard has no results.
- IRD's domain verification status is `PRELIMINARY`.
- No severity is assigned anywhere.

## Unresolved source-verification tasks

- [ ] Entry 01: save a dated copy of the registry page; obtain the specific WHOIS record for `ird.gov.lk`
- [ ] Entry 02: open the KPMG bulletin in full; record the IRD circular's number and issue date
- [ ] Entry 03: open the Ministry of Finance page and record where the Department's entry links to
- [ ] Entry 07: confirm or discard the platform inference through checklist item C06, after the domain is verified
- [ ] Entry 09: find the Cabinet Office's published decision; check the reported history of NCS as original supplier against a primary source
- [ ] Entry 12: read the payment guide in full and check whether a newer edition exists
- [ ] Entry 13: read the World Bank report itself
- [ ] Entry 14: read the rest of the audit report
- [ ] Entry 17: find Sri Lanka CERT's original warning
- [ ] Entry 18: find an official statement, or delete the entry
- [ ] Entry 19: read the guideline in full and confirm it is the current edition

Entries 05, 06 and 15 remain open as lookups in the [observation plan](../../research/observations/IRD-observation-plan.md), not as source checks.

## Limits of this review

Five sources were opened (entries 10, 13, 14 in part, 17, 18). The other entries were re-checked only against the search excerpts read earlier, so their dates and descriptions are consistent with those excerpts but not independently confirmed.
