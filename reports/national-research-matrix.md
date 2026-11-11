# National government website research matrix

Evidence discovery, 2026-11-11. This matrix shows, for each of the ten institutions, what credible public evidence exists, what remains unverified, and what deserves further research. It records past events and open questions. It identifies no current vulnerability in any website.

**How the evidence was gathered.** Web search of news, official publications and research papers. No request was made to any of the ten websites. Sources were read as search-result excerpts unless stated otherwise, and none has been saved yet.

**Reading the matrix.** Incident IDs refer to the [historical incident timeline](historical-incident-timeline.md). Labels are defined in [evidence classification](../docs/evidence-classification.md). "Research priority" ranks where further research is most informative and is explained in the [confidence and risk matrix](../docs/confidence-risk-matrix.md); it is not a security rating.

## Matrix

| ID | Institution and domain | Domain verification | Credible public evidence found | What remains unverified | Areas deserving further research | Research priority |
| --- | --- | --- | --- | --- | --- | --- |
| DGP | Department of Government Printing, documents.gov.lk | PRELIMINARY | **INC-02** (confirmed): website hacked and content altered, 30–31 December 2024. Sri Lanka CERT officials were reported as saying their audit of the old site found serious weaknesses and that a new site was recommended. | Cause; investigation outcome; date the replacement site went live; anything about the current site. | Find CERT's and the Department's own statements. Establish whether the current site is the replacement. Then browser observation. | High |
| MPA | Ministry of Public Administration, pubad.gov.lk | PRELIMINARY | **INC-03** (confirmed): homepage defaced, 30 May 2020. **INC-04** (confirmed): Minister acknowledged a cyberattack on the website in April 2026; CID and CERT inquiries. | What data was taken in 2026 (press descriptions are alleged); inquiry outcomes; remediation. | Follow the CID and CERT inquiries. Check Parliament's records for statements. Then browser observation. | High |
| MPS | Ministry of Public Security, pubsec.gov.lk | PRELIMINARY | **INC-01** (confirmed): police reported the website was targeted, January 2026; CERT and ICTA restored it. **INC-15** (confirmed, related agency): Sri Lanka Police social media accounts taken over, December 2024; police said their website was not compromised. | Date, method and extent of the 2026 incident; inquiry outcome. | Find the police media statement itself. Then browser observation of public information pages only. | High |
| SLR | Sri Lanka Railways, railway.gov.lk | PRELIMINARY | **INC-11** (confirmed): cyberattack on the newly launched website affected its timetable section, 14 June 2026; restored. **INC-12** (confirmed): warnings about fraudulent look-alike booking sites. | Nature of the attack; whether an inquiry was opened; when the timetable section returned. | Find the Department's and Minister's statements. Then browser observation. Booking system stays out of scope. | High |
| DIE | Department of Immigration and Emigration, immigration.gov.lk | PRELIMINARY | **INC-06** (confirmed): Department warned of fake e-visa sites, April 2024. **INC-07** (unverified): alleged personal-data exposure in the outsourced visa system, 2024. **INC-08** (unverified): press report of a claimed weakness in the ETA status page, May 2026. **INC-09**: ETA outage, February 2026, with no evidence of a cyber cause. | Whether INC-07 or INC-08 was confirmed, investigated or fixed. | Look for Department, CERT or court statements on INC-07 and INC-08. Both concern out-of-scope systems and are NOT TESTED. Browser observation of the main site only. | Medium |
| NMRA | National Medicines Regulatory Authority, nmra.gov.lk | PARTIAL | **INC-05** (confirmed): files deleted from the Authority's back-end document system on the government cloud, July 2021; CID investigation; no backup available, as reported. | Prosecution outcome; how much was recovered; current backup arrangements. A government source for the domain. | Complete domain verification. Look for court records and Auditor General or parliamentary committee reports on the incident. | Medium |
| IRD | Inland Revenue Department, ird.gov.lk | PRELIMINARY | **INC-14** (confirmed): CERT warning about callers impersonating the Department, June 2026. **INC-16**: no report of a compromise found. Background in the [IRD public evidence review](individual-sites/ird-public-evidence-review.md). | Platform and configuration of the site; eleven source checks listed in the [review report](../docs/reviews/pr-1-ird-evidence-review.md). | Complete domain verification, then follow the existing [observation plan](../research/observations/IRD-observation-plan.md). | Medium |
| DMT | Department of Motor Traffic, dmt.gov.lk | PRELIMINARY | **INC-17**: no cyber incident report found. System failures in 2025 were attributed to technical causes. Its own services were reported unaffected by the October 2025 cloud outage (INC-10). | Which domain is primary (`dmt.gov.lk` or the older `motortraffic.gov.lk`). | Settle the primary domain. Then browser observation. | Low |
| MODE | Ministry of Digital Economy, mode.gov.lk | PARTIAL | **INC-19**: no incident report found for the Ministry's own website. | A second government source for the domain. | Complete domain verification. Then browser observation. | Low |
| GIC | Government Information Center, gic.gov.lk | PARTIAL | **INC-18**: no incident report found. | An independent government source for the domain. | Complete domain verification. Then browser observation. | Low |

## Shared infrastructure

Two confirmed incidents affected services shared across government. No source read attributes either to a specific one of the ten institutions.

| ID | Date | What was reported | Relevance |
| --- | --- | --- | --- |
| INC-13 | August 2023 | Ransomware on the Lanka Government Cloud; ICTA confirmed loss of about three months of email for roughly 5,000 `gov.lk` addresses, with no backup for the period. | Shows that backup and recovery (CERT guideline R9) has failed at national level before. |
| INC-10 | October 2025 | Lanka Government Cloud disruption interrupted services of more than 30 institutions for over a week. ICTA said data was not compromised. | An availability failure with no public evidence of a cyber cause. |

## What the evidence supports

1. **Four of the ten institutions have a confirmed website incident on public record**: DGP (2024), MPA (2020 and 2026), MPS (2026) and SLR (2026). Each was acknowledged by an official body, as reported by news outlets.
2. **Three of those incidents occurred in 2026**, and for all three the investigation outcome was not found.
3. **One institution has a confirmed back-end data-loss incident** (NMRA, 2021) that was not a website attack.
4. **Two reports about the immigration visa systems are unverified** and concern systems outside this study's scope.
5. **For four institutions no cyber incident report was found** (IRD, DMT, MODE, GIC). That is an absence of reports, not evidence of security.
6. **All ten use a `gov.lk` domain**, as Sri Lanka CERT's guideline requires. No other guideline requirement has been assessed for any of them. See the [compliance mapping](../research/cert-compliance-mapping.md).

## What the evidence does not support

- Any statement that a listed website is vulnerable today.
- Any statement that an institution does not comply with Sri Lanka CERT's guideline.
- Any link between these incidents and AI-generated code. See the [literature review](../research/ai-code-security-literature-review.md).
- Any ranking of institutions by security.

## Tracks and their state

| Track | Deliverable | State |
| --- | --- | --- |
| 1 Targets | [government-sites.md](../research/government-sites.md), [inventory](../data/website-inventory.csv) | Ten selected; 0 verified, 7 preliminary, 3 partial |
| 2 Historical incidents | [timeline](historical-incident-timeline.md), [data](../data/historical-incidents.csv) | 19 records: 12 confirmed, 2 unverified, 5 with no evidence of a cyber incident |
| 3 Observable posture | [checklist](../research/assessment-checklist.md), per-site scorecards | Not started; blocked on verification |
| 4 CERT compliance | [compliance mapping](../research/cert-compliance-mapping.md) | Requirements mapped; one requirement readable from domain names; rest unassessed |
| 5 AI-generated code | [literature review](../research/ai-code-security-literature-review.md) | First pass; three papers checked, eight sources to read |
| 6 Classification | [evidence classification](../docs/evidence-classification.md) | Seven labels defined and enforced for incident records |
| 7 Deliverables | This matrix, ten [public-records summaries](individual-sites/), [executive summary](executive-summary.md) | Drafted from public records only |

## Next research steps, in order

1. Complete domain verification for all ten, starting with the three `PARTIAL` sites.
2. Open, read in full and save every incident source; replace news reports with primary statements where they exist.
3. Search Sri Lanka CERT annual reports, Auditor General reports and parliamentary records for the four high-priority institutions.
4. Begin browser observation, one verified site at a time, starting with a high-priority institution.
5. Decide whether to write to Sri Lanka CERT describing the study before observation begins.
