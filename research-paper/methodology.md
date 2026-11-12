# Methodology (paper companion)

This expands Section 4 of the manuscript. The authoritative, version-controlled method is in
the repository's [`research/methodology.md`](../research/methodology.md) and
[`research/scope.md`](../research/scope.md); this file summarizes it for the paper and records
the analysis choices.

## Design

An exploratory, cross-sectional study using only public evidence and passive observation. The
unit of analysis is the institution (n=10). No experiment or intervention is performed.

## Data sources

1. **Historical incidents** — news reporting and official statements, recorded in
   `data/historical-incidents.csv` with, for each record: the system affected, a confirmed-vs-
   alleged split, investigation status and outcome, source URLs, source type, an evidence label
   and a confidence level.
2. **Governance** — the Sri Lanka CERT web-application and website security guidelines (2022),
   mapped requirement-by-requirement in `research/cert-web-application-guideline-mapping.md` and
   `research/cert-compliance-mapping.md`.
3. **Institution metadata** — `data/website-inventory.csv`: domain, sector, verification status,
   research status.
4. **AI-code literature** — eight peer-reviewed papers, in
   `research/ai-code-security-literature-review.md`, mapped to OWASP in
   `research/track-c-ai-owasp-mapping.md`.

## Classification scheme

Every result carries exactly one of seven evidence labels (Table 6). Two rules are enforced:
an incident is never treated as a current weakness, and absence of evidence is never treated as
compliance or non-compliance. Confirmed and alleged parts of a report are stored in separate
fields. Labels requiring the researcher's own technical observation (OBSERVED CONFIGURATION,
CONFIRMED SECURITY WEAKNESS) are unused, because no site has been observed.

## Incident classification method (RQ1)

Records are grouped by the `system_affected` field — website, other/backend system,
impersonation, shared infrastructure, social media — before any interpretation. Only records
whose system is the institution's own *website* and whose label is CONFIRMED HISTORICAL INCIDENT
are read as confirmed website compromises. Impersonation and shared-infrastructure records are
reported separately and never counted as website vulnerabilities. This is the single most
important guard against over-counting.

## Governance mapping method (RQ2)

Each of the 32 web-application requirements is placed in one of four verifiability classes:
informable by passive observation, officially documented only, requires written authorization,
or not publicly verifiable. The counts (7 / 4 / 5 / 16) describe the *yardstick's* external
visibility, not any institution's compliance.

## Reproducibility

Every quantitative claim in the manuscript is regenerated from the CSV files by the repository's
scripts and is cross-checked in [evidence-audit.md](evidence-audit.md). The validation script
`scripts/validate.py` enforces the structural and safety invariants (no network code, empty
register implies zero confirmed weaknesses, no observation before a domain is VERIFIED).

## Ethics and legality

The study performs no active testing. Unauthorized testing would breach the Computer Crimes Act
No. 24 of 2007; authorized testing is gated behind the framework in `authorization/`. Passive
observation of public pages is used, and any future active work requires written authorization.
