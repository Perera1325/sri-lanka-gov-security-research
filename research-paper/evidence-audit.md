# Evidence audit

Every quantitative claim in the manuscript, checked against the repository data files on 2026-11-12. "Paper" is the figure stated in the manuscript; "Data" is the value computed from the source. They must match.

| Claim | Paper | Data | Source |
| --- | --- | --- | --- |
| Incident records total | 20 | 20 | data/historical-incidents.csv |
| Confirmed historical incidents | 13 | 13 | label field |
| Unverified reports | 2 | 2 | label field |
| No public evidence | 5 | 5 | label field |
| Website-type records | 10 | 10 | system_affected field |
| Other/backend records | 4 | 4 | system_affected field |
| Impersonation records | 3 | 3 | system_affected field |
| Shared-infrastructure records | 2 | 2 | system_affected field |
| Social-media records | 1 | 1 | system_affected field |
| Confirmed website compromises | 6 | 6 | label + system |
| Institutions with a confirmed website incident | 5 | 5 | DGP,MOE,MPA,MPS,SLR |
| Confirmed incidents with a published outcome | 0 | 0 | investigation_outcome field |
| Domains VERIFIED | 0 | 0 | domain_verification_status |
| Domains PRELIMINARY | 7 | 7 | domain_verification_status |
| Domains PARTIAL | 3 | 3 | domain_verification_status |
| Evidence register rows | 0 | 0 | evidence/evidence-register.csv |
| CERT requirements total | 32 | 32 | research/cert-web-application-guideline-mapping.md |
| CERT reqs informable by passive observation | 7 | 7 | mapping summary |
| CERT reqs needing authorization or internal access | 21 | 21 | 5 auth + 16 not-verifiable |
| AI-code papers (verified) | 8 | 8 | research/ai-code-security-literature-review.md |

**Result:** all claims match the data.

## Integrity statements (Step 7)

- No penetration testing or automated scanning was performed.
- No current exploitable vulnerability is claimed for any institution.
- The evidence register is empty; no direct technical observation exists.
- Historical incidents are not presented as current weaknesses.
- Secondary news is not presented as primary government statements.
- Domain verification is reported as it stands: 0 VERIFIED, 7 PRELIMINARY, 3 PARTIAL.

Note: the Ministry of Education domain is recorded as PARTIAL in the committed data. A gov.lk-directory verification was gathered during the project but is not yet committed; until it is, the paper reports PARTIAL.
