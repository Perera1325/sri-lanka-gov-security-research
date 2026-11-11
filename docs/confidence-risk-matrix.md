# Confidence and risk assessment matrix

No risk rating is assigned to any institution, because no website has been observed. What can be stated today is how well each piece of public evidence is supported, and where further research is most worthwhile.

## Confidence in a public record

| Confidence | Rule |
| --- | --- |
| High | A primary source (the institution, Sri Lanka CERT, ICTA, a court or audit document) was opened, read and saved. |
| Medium | Credible news reporting that attributes the fact to a named official body, or a primary source read only as an excerpt. |
| Low | A single report, an unattributed claim, a third-party allegation, or an inference. |
| Not applicable | Entries labelled NO PUBLIC EVIDENCE AVAILABLE. |

No incident record is rated High yet. Every one rests on news reporting of official statements, so the ceiling is Medium until primary statements are located and saved. For six records the main news source was opened and read on 2026-11-11; the `sources_opened` column in the incident file says which.

## What each label permits

| Label | May support a severity rating? | May be reported to the institution? | May be described as a current weakness? |
| --- | --- | --- | --- |
| CONFIRMED HISTORICAL INCIDENT | No | No (already known to it) | No |
| CONFIRMED PUBLIC SECURITY REQUIREMENT | No | Not applicable | Not applicable |
| OBSERVED CONFIGURATION | Informational only | On request | No |
| CONFIRMED SECURITY WEAKNESS | Yes, under [risk classification](risk-classification.md) | Yes, under the [disclosure policy](../disclosure/responsible-disclosure-policy.md) | Yes, with the observation dates |
| POTENTIAL RISK – NOT VERIFIED | No | No | No |
| NOT TESTED | No | No | No |
| NO PUBLIC EVIDENCE AVAILABLE | No | No | No |

## Current assessment by institution

"Research priority" ranks where further *research* is likely to be most informative. It is not a judgement of how secure a site is.

| ID | Domain | Confirmed incidents on record | Unverified reports | Risk rating | Research priority | Reason for priority |
| --- | --- | --- | --- | --- | --- | --- |
| DGP | documents.gov.lk | 1 (INC-02) | 0 | Not assessed | High | A confirmed website compromise, a reported CERT audit and a planned replacement site. The current site's state is unknown. |
| MPA | pubad.gov.lk | 2 (INC-03, INC-04) | 0 | Not assessed | High | Two confirmed website incidents six years apart, the later one in 2026 with a CID investigation whose outcome is unknown. |
| MPS | pubsec.gov.lk | 1 (INC-01), plus 1 at a related agency (INC-15) | 0 | Not assessed | High | A confirmed website incident in 2026, described by police as multiple instances of unauthorized access, with a CID investigation whose outcome is unknown. |
| MOE | moe.gov.lk | 1 (INC-20) | 0 | Not assessed | High | A confirmed website incident in 2024 with reported Sri Lanka CERT statements on assessment and patching, and a CERT recommendation to build a new site. Whether that happened is unknown. Domain verification is incomplete. |
| SLR | railway.gov.lk | 2 (INC-11, INC-12) | 0 | Not assessed | High | A confirmed attack on a newly launched site in 2026. No inquiry was reported. |
| DIE | immigration.gov.lk | 1 (INC-06) | 2 (INC-07, INC-08) | Not assessed | Medium | The reports concern out-of-scope visa systems; the main site has no incident on record. |
| NMRA | nmra.gov.lk | 1 (INC-05) | 0 | Not assessed | Medium | A serious but older back-end incident. Domain verification is incomplete. |
| IRD | ird.gov.lk | 1 (INC-14, impersonation only) | 0 | Not assessed | Medium | No incident on record; a detailed observation plan already exists. |
| DMT | dmt.gov.lk | 0 | 0 | Not assessed | Low | No incident on record. |
| MODE | mode.gov.lk | 0 | 0 | Not assessed | Low | No incident on record. Domain verification is incomplete. |

Shared-infrastructure incidents INC-10 and INC-13 are not attributed to any single institution and are left out of this table.

## When a risk rating becomes possible

A site receives a risk rating only when all of the following exist:

1. Its domain is `VERIFIED`.
2. The assessment checklist has been completed in a browser on two separate days.
3. Each result is in the evidence register with saved evidence.
4. Each row has a severity and a confidence under [risk classification](risk-classification.md).

Until then the "Risk rating" column stays "Not assessed".
