# Government sites

Ten institutions are selected. The machine-readable list, with current verification and research status, is [`data/website-inventory.csv`](../data/website-inventory.csv). Counts are on the [dashboard](../DASHBOARD.md), and the evidence found for each is in the [national research matrix](../reports/national-research-matrix.md).

## Selected sites

| ID | Institution | Domain | Sector |
| --- | --- | --- | --- |
| MPS | Ministry of Public Security | pubsec.gov.lk | Public security |
| DGP | Department of Government Printing | documents.gov.lk | Public records |
| MPA | Ministry of Public Administration | pubad.gov.lk | Public administration |
| NMRA | National Medicines Regulatory Authority | nmra.gov.lk | Health regulation |
| MOE | Ministry of Education | moe.gov.lk | Education |
| IRD | Inland Revenue Department | ird.gov.lk | Financial and taxation |
| DIE | Department of Immigration and Emigration | immigration.gov.lk | Immigration |
| DMT | Department of Motor Traffic | dmt.gov.lk | Transportation |
| MODE | Ministry of Digital Economy | mode.gov.lk | Digital government infrastructure |
| SLR | Sri Lanka Railways | railway.gov.lk | Transportation |

## Scope change log

| Date | Change | Reason |
| --- | --- | --- |
| 2026-11-11 | Phase 0 selection of ten sites recorded in the [research plan](research-plan.md). | Initial selection. |
| 2026-11-11 | Added pubsec.gov.lk, documents.gov.lk, pubad.gov.lk and nmra.gov.lk. Moved drp.gov.lk, rgd.gov.lk, parliament.lk and icta.lk to the reserve list. | The researcher redirected the study toward institutions with a documented public record of incidents, for the national evidence-discovery phase. |

| 2026-11-11 | Added moe.gov.lk. Moved gic.gov.lk to the reserve list. | The Ministry of Education has a confirmed website incident (April 2024) with reported Sri Lanka CERT statements, which is directly relevant to the study. The Government Information Center was the lowest-priority candidate: no incident on record, and its domain verification rested on its own page. |

The research plan is kept as the Phase 0 baseline and is not rewritten. The reserve sites keep their records in [`data/reserve-sites.csv`](../data/reserve-sites.csv) and their unstarted report files in `reports/individual-sites/`.

No candidate was removed for being unsuitable. Reserve moves were made only to keep the selection at ten.

## Verification standard

A domain is verified when two independent checks agree.

1. **Registry rule.** The name sits under `gov.lk`, which the LK Domain Registry restricts to government organizations ([LK Domain Registry, n.d.](https://domains.lk/lk-domain-naming-structure/)). All ten selected names are `gov.lk` names.
2. **Independent government naming.** A source published by a *different* government body (another ministry or department, Parliament, a diplomatic mission, a state enterprise) names the same domain for the same institution. The site's own pages do not count. A reputable non-government source is recorded but does not complete the check.

From this phase the second check requires a government source. Under that stricter rule gic.gov.lk had moved from `PRELIMINARY` to `PARTIAL` before it went to the reserve list, because its second source was its own About page.

## Verification status values

| Value | Meaning |
| --- | --- |
| `VERIFIED` | Both checks pass and the researcher has re-opened each source and saved a dated copy under `evidence/sources/domain-verification/`. |
| `PRELIMINARY` | Both checks pass on the basis of web-search results. Not yet re-confirmed or saved. |
| `PARTIAL` | Only one check passes so far. |
| `UNVERIFIED` | No check recorded. |

No site is `VERIFIED` yet. Seven are `PRELIMINARY` and three are `PARTIAL`.

## Verification evidence found so far

| ID | Second-check source | Status |
| --- | --- | --- |
| MPS | A Sri Lanka Police notice describes a `pubsec.gov.lk` service as launched by the Ministry ([Sri Lanka Police, 2026](https://www.police.lk/?p=25590)). | PRELIMINARY |
| DGP | A Department for Registration of Persons document tells readers that Acts can be downloaded from `documents.gov.lk` ([DRP, n.d.](https://drp.gov.lk/si/assets/downloads/accessing%20informations%20english.pdf)). | PRELIMINARY |
| MPA | The Ministry's performance report tabled in Parliament prints `www.pubad.gov.lk` ([Parliament of Sri Lanka, 2023](https://www.parliament.lk/uploads/documents/paperspresented/1686119744068361.pdf)). | PRELIMINARY |
| NMRA | Only a news report names the domain ([Daily FT, n.d.](https://www.ft.lk/Healthcare/NMRA-launches-integrated-user-friendly-website/45-674522)). A government source is still needed. | PARTIAL |
| MOE | None yet. The government portal could not be opened from the research environment. A Ministry advertisement and the UNESCO Institute for Statistics name the domain ([UNESCO UIS, 2020](https://emis.uis.unesco.org/?p=1279)), but neither is an independent government source. | PARTIAL |
| IRD | IRD circular reproduced by KPMG. See the [IRD public evidence review](../reports/individual-sites/ird-public-evidence-review.md). | PRELIMINARY |
| DIE | Sri Lanka Embassy in Germany's list of government links ([Embassy of Sri Lanka, n.d.](https://srilanka-botschaft.de/important-government-links/)). | PRELIMINARY |
| DMT | Airport and Aviation Services notice naming `www.dmt.gov.lk` ([AASL, n.d.](https://www.airport.lk/services/Temporary%20Driving%20License%20for%20International%20Tourists%20at%20BIA.pdf)). | PRELIMINARY |
| MODE | None yet. | PARTIAL |
| SLR | Sri Lanka High Commission in Pakistan's public notice ([High Commission of Sri Lanka, n.d.](https://www.slhcpakistan.org/?p=116789)). | PRELIMINARY |

## Open verification tasks

- **moe.gov.lk** — open the government portal's list of ministries in a browser and record the address it gives; then find one other government body's page that names the domain (for example the Department of Examinations, the National Institute of Education or a diplomatic mission).
- **nmra.gov.lk, mode.gov.lk** — find a government source, other than the site itself, that names the domain. The Ministry of Health's site is the obvious place to look for NMRA.
- **dmt.gov.lk** — older official documents use `motortraffic.gov.lk`; confirm which the department treats as primary.
- **All ten** — re-open each source and save a dated copy.

## Site-specific cautions

- **immigration.gov.lk** — the ETA and e-visa applications run on separate systems and are out of scope. Public reports about them are recorded as context only.
- **railway.gov.lk** — Sri Lanka Railways has warned publicly about look-alike booking sites. The seat-reservation subdomain handles payments and is out of scope.
- **nmra.gov.lk** — the Authority's application portal is an authenticated system and is out of scope.
- **moe.gov.lk** — the Ministry runs separate teacher, scholarship and other service portals on subdomains. They are out of scope.
- **pubsec.gov.lk** — the Ministry's online complaints service accepts submissions and is out of scope; only its public information pages may be observed.
- **ird.gov.lk** — e-services, payment and API systems are out of scope.

## Reserve list

`drp.gov.lk`, `rgd.gov.lk`, `parliament.lk`, `icta.lk` and `gic.gov.lk` (formerly selected), plus `cert.gov.lk`, `cbsl.gov.lk` and `gov.lk`. A swap is made by editing the inventory and this file in one commit that gives the reason.
