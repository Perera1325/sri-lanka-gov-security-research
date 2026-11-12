# Table 6. Evidence classification scheme

Every research result in the repository carries exactly one of seven labels
(`docs/evidence-classification.md`). The label is separate from confidence and severity.

| # | Label | Meaning | Used in |
| --- | --- | --- | --- |
| 1 | CONFIRMED HISTORICAL INCIDENT | A past event acknowledged by the institution, CERT, police or a minister, or credibly reported. | Incident dataset |
| 2 | CONFIRMED PUBLIC SECURITY REQUIREMENT | A requirement in an official published standard. | CERT mappings |
| 3 | OBSERVED CONFIGURATION | Something seen on a public page, dated, with saved evidence. | Evidence register (none yet) |
| 4 | CONFIRMED SECURITY WEAKNESS | A weakness shown present now, by observation on two days or a current official statement. | Evidence register (none yet) |
| 5 | POTENTIAL RISK – NOT VERIFIED | A specific claim not confirmed by an official source or observation. | Incident dataset |
| 6 | NOT TESTED | A question answerable only outside the passive scope. | CERT mappings, scorecards |
| 7 | NO PUBLIC EVIDENCE AVAILABLE | Searched for and not found. | Incident dataset |

Labels 3 and 4 require the researcher's own evidence; nothing carries either, because no
site has been observed.
