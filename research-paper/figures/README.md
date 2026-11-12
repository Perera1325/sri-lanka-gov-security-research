# Figures

Each figure is generated from repository data. Counts can be reproduced from the named
source files.

| Figure | File | Source data | Key values |
| --- | --- | --- | --- |
| Fig. 1 | fig1-incident-classification.png | `data/historical-incidents.csv` | 20 records: Website 10 (6 confirmed), Other system 4, Impersonation 3, Shared infra. 2, Social media 1 |
| Fig. 2 | fig2-domain-verification.png | `data/website-inventory.csv` | VERIFIED 0, PRELIMINARY 7, PARTIAL 3, UNVERIFIED 0 |
| Fig. 3 | fig3-cert-verifiability.png | `research/cert-web-application-guideline-mapping.md` | 32 requirements: passive 7, official 4, authorization 5, not verifiable 16 |
| Fig. 4 | methodology-flowchart.md (Mermaid) | — | Render to PNG/PDF for the manuscript |

The PNG figures were produced with matplotlib from the CSV files above. They contain no
data that is not in those files.
