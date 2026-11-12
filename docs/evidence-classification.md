# Evidence classification

Every research result carries exactly one of seven labels. The label says what kind of thing the result is; it is separate from confidence and from severity.

## The seven labels

| # | Label | Use it when | Never use it for |
| --- | --- | --- | --- |
| 1 | CONFIRMED HISTORICAL INCIDENT | A past event that the institution, Sri Lanka CERT, ICTA, police or a minister has acknowledged, directly or as reported by credible news. | A claim made only by an anonymous party or a single unattributed report. |
| 2 | CONFIRMED PUBLIC SECURITY REQUIREMENT | A requirement stated in an official published standard or guideline. | A statement about whether any institution meets it. |
| 3 | OBSERVED CONFIGURATION | Something seen directly on a public page in a browser, on a recorded date, with saved evidence. | Anything inferred from a URL pattern, a news report or a third-party record. |
| 4 | CONFIRMED SECURITY WEAKNESS | A weakness that exists now, shown by a browser observation on two separate days or by a current official statement. | A weakness reported in the past, or a missing header described as exploitable. |
| 5 | POTENTIAL RISK – NOT VERIFIED | A specific claim or indication that has not been confirmed by an official source or by observation. | General risks that apply to every website. |
| 6 | NOT TESTED | A question that cannot be answered without activity outside the passive scope. | Things that were simply not looked at yet; those are open tasks. |
| 7 | NO PUBLIC EVIDENCE AVAILABLE | Searched for and not found, or not retrievable. | A conclusion that something does not exist. |

In CSV files the fifth label is written with a plain hyphen: `POTENTIAL RISK - NOT VERIFIED`.

## Rules that keep the labels honest

1. **An incident is not a vulnerability.** A CONFIRMED HISTORICAL INCIDENT says something happened. It never implies that the cause is still present.
2. **Absence is not non-compliance.** NO PUBLIC EVIDENCE AVAILABLE and NOT TESTED are never grounds for saying an institution fails a requirement.
3. **Confirmed parts and alleged parts are recorded separately.** The incident file has one column for each.
4. **One label per result.** If part of a report is confirmed and part alleged, the label follows the confirmed part and the alleged part is stated as such.
5. **Labels 3 and 4 need the researcher's own evidence.** Nothing has either label yet, because no site has been observed.

## Where each label is used

| Record | File | Labels that may appear |
| --- | --- | --- |
| Historical incidents | [`data/historical-incidents.csv`](../data/historical-incidents.csv) | 1, 5, 7 |
| CERT guideline requirements | [`research/cert-compliance-mapping.md`](../research/cert-compliance-mapping.md) | 2 for the requirement; 3, 6 or 7 for each institution |
| Browser observations | [`evidence/evidence-register.csv`](../evidence/evidence-register.csv) | 3, 4, 5, 6 (see mapping below) |
| IRD background entries | [IRD public evidence review](../reports/individual-sites/ird-public-evidence-review.md) | Uses the earlier five-label scheme defined in that file |

## Mapping to the evidence register's statuses

The evidence register keeps its four `finding_status` values. They correspond to the labels as follows.

| Register status | Label |
| --- | --- |
| `CONFIRMED OBSERVATION` | OBSERVED CONFIGURATION, or CONFIRMED SECURITY WEAKNESS when the observation is a weakness rated Low or above |
| `SUSPECTED` | POTENTIAL RISK – NOT VERIFIED |
| `NOT TESTED` | NOT TESTED |
| `INFORMATIONAL` | OBSERVED CONFIGURATION |

Confidence and research-priority rules are in the [confidence and risk assessment matrix](confidence-risk-matrix.md). Severity rules for observations are in [risk classification](risk-classification.md).
