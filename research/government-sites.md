# Government sites

Ten sites are selected, one or more per sector. The machine-readable list, including current verification and research status, is [`data/website-inventory.csv`](../data/website-inventory.csv). Counts are on the [dashboard](../DASHBOARD.md).

## Selected sites

| ID | Institution | Domain | Sector |
| --- | --- | --- | --- |
| IRD | Inland Revenue Department | ird.gov.lk | Financial and taxation |
| DIE | Department of Immigration and Emigration | immigration.gov.lk | Immigration |
| DRP | Department for Registration of Persons | drp.gov.lk | Public administration |
| DMT | Department of Motor Traffic | dmt.gov.lk | Transportation |
| SLR | Sri Lanka Railways | railway.gov.lk | Transportation |
| GIC | Government Information Center | gic.gov.lk | Government information services |
| MODE | Ministry of Digital Economy | mode.gov.lk | Digital government infrastructure |
| RGD | Registrar General's Department | rgd.gov.lk | Public records |
| PARL | Parliament of Sri Lanka | parliament.lk | Parliament and legislative services |
| ICTA | ICT Agency of Sri Lanka | icta.lk | Government technology institution |

The source that names each domain is in the inventory's `official_source_reference` column and in the [research plan](research-plan.md).

## Verification standard

A domain is verified when two independent checks agree.

1. **Registry rule.** The name sits under `gov.lk`, which the LK Domain Registry restricts to government organizations ([LK Domain Registry, n.d.](https://domains.lk/lk-domain-naming-structure/)). For a name outside `gov.lk`, a registry WHOIS record showing the institution as registrant serves instead.
2. **Independent naming.** A separate official or reputable source names the same domain for the same institution.

## Verification status values

| Value | Meaning |
| --- | --- |
| `VERIFIED` | Both checks pass and the researcher has re-opened each source and saved a dated copy under `evidence/sources/domain-verification/`. |
| `PRELIMINARY` | Both checks pass on the basis of Phase 0 web-search results. Not yet re-confirmed or saved. |
| `PARTIAL` | Only one check passes so far. |
| `UNVERIFIED` | No check recorded. |

No site is `VERIFIED` yet. Phase 0 established seven sites as `PRELIMINARY` and three as `PARTIAL`.

## Open verification tasks

- **mode.gov.lk** — find a second government source that links to it.
- **parliament.lk** — registry WHOIS lookup showing the registrant.
- **icta.lk** — registry WHOIS lookup, plus one government page that links to it.
- **dmt.gov.lk** — older official documents use `motortraffic.gov.lk`; confirm which the department treats as primary.
- **All ten** — re-open each source and save a dated copy.

## Site-specific cautions

- **railway.gov.lk** — Sri Lanka Railways has warned publicly about look-alike booking sites. Use only this domain. The seat-reservation subdomain handles payments and is out of scope.
- **ird.gov.lk, immigration.gov.lk, drp.gov.lk, rgd.gov.lk** — these institutions run e-services that handle personal data. Only their public information pages are in scope.

## Reserve list

`cert.gov.lk`, `cbsl.gov.lk` and `gov.lk` may replace a site that proves unsuitable. A swap is made by editing the inventory with a commit message that gives the reason.
