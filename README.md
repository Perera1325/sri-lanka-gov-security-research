# Sri Lanka Government Web Security Posture Research

An independent, passive-only study of ten Sri Lankan government websites: what the public record says about past incidents, what the national guideline requires, and what an ordinary visitor's browser shows, so that institutions can be told privately about anything worth fixing.

**Status:** Evidence discovery from public records is done for a first pass. No website has been observed or assessed and the evidence register is empty. Start with the [national research matrix](reports/national-research-matrix.md); live counts are on the [research dashboard](DASHBOARD.md).

> This repository does not claim that any government website is vulnerable.

## Research objectives

1. Document, from credible public sources, the cybersecurity incidents already on record for ten government institutions, keeping confirmed facts apart from allegations.
2. Describe, with evidence, the security configuration those institutions' websites present to an ordinary visitor.
3. Map observations to Sri Lanka CERT's website guideline and to recognized risk categories (OWASP Top 10) while separating observed facts from theoretical risk.
4. Report credible observations to Sri Lanka CERT and the owning institutions through official channels.
5. Publish a method that others can repeat without touching anything they are not authorized to test.

## Ethical research statement

- **Passive only.** The study uses what a normal browser shows on public pages, plus existing public records. It involves no scanning, crawling, fuzzing, exploitation, login attempts, API probing or form submission.
- **No sensitive data.** Personal or confidential information is never collected or stored.
- **Honest labelling.** Anything that cannot be determined passively is recorded as `NOT TESTED`, not guessed.
- **Disclosure before publication.** Site-specific observations go to Sri Lanka CERT and the institution first. See the [responsible disclosure policy](disclosure/responsible-disclosure-policy.md).
- **No tooling for active testing.** The scripts here read local CSV and Markdown files only, and `scripts/validate.py` fails if any script imports a network module.

## Scope and limitations

Ten institutions are in scope, listed in [government-sites.md](research/government-sites.md) and [`data/website-inventory.csv`](data/website-inventory.csv). Only their public, unauthenticated pages are examined. Full rules are in [scope.md](research/scope.md).

A passive study shows configuration, not exploitability, and cannot assess the areas where most risk lies, such as access control and authentication. Read [research limitations](docs/research-limitations.md) before drawing any conclusion from this work.

## Methodology

Each site goes through the same steps: confirm the domain is official, run a [nine-point passive checklist](research/assessment-checklist.md), save evidence, log each observation in the [evidence register](evidence/evidence-register.csv), re-check on a second day, classify using the [risk classification](docs/risk-classification.md), and write the site report. Details are in [methodology.md](research/methodology.md).

## Repository structure

```
research/
    research-plan.md              Phase 0 plan (baseline)
    methodology.md                Phases, workflow, finding statuses
    scope.md                      In scope, out of scope, prohibited activities
    government-sites.md           The ten sites and the verification standard
    assessment-checklist.md       Nine passive checks and their evidence standard
    technology-risk-reference.md  OWASP and AI-assisted code risk background
    cert-compliance-mapping.md    Sri Lanka CERT website guideline: requirements and how far each can be checked
    cert-web-application-guideline-mapping.md  Sri Lanka CERT web application guideline: all 32 requirements
    ai-code-security-literature-review.md  Academic strand on AI-generated code
    track-c-ai-owasp-mapping.md   AI-code weakness classes mapped to OWASP (Track C)
    observations/                 Per-site observation plans (IRD so far)
evidence/
    evidence-register.csv         One row per observation (currently empty)
    evidence-guidelines.md        Column rules, file naming, redaction, escalation
    sources/                      Saved screenshots and page copies
reports/
    executive-summary.md          National-level summary
    national-research-matrix.md   Generated: evidence, unknowns and status for all ten
    historical-incident-timeline.md  Generated from data/historical-incidents.csv
    individual-sites/             Per site: report, generated public-records summary, template
disclosure/
    responsible-disclosure-policy.md
    templates/                    CERT report, institution notice, follow-up
data/
    website-inventory.csv         Sites, verification status, research status
    reserve-sites.csv             Sites moved out of the selection
    historical-incidents.csv      One row per documented incident or report
    scorecard-template.csv        Checklist results sheet to copy per site
    scorecards/                   One blank scorecard per site (all ten; Track A)
    authorizations.csv            Authorization status per institution (Track B gate)
lab/                              Isolated local security lab (never aimed at .gov.lk)
    README.md                     The isolation rule and what is here
    lab-setup.md                  Building the offline environment
    owasp-juice-shop.md / owasp-webgoat.md / portswigger-academy.md
    vulnerability-analysis-TEMPLATE.md  One write-up per vulnerability class
authorization/                    Track B: written-authorization framework
    README.md                     The rule; nothing here sends email
    authorization-request-TEMPLATE.md   Master request
    requests/                     A pre-addressed request per institution
docs/
    research-limitations.md
    risk-classification.md
    evidence-classification.md    The seven research labels
    confidence-risk-matrix.md     Confidence rules and research priorities
    reviews/                      Review reports on earlier work
scripts/
    validate.py                   Checks structure, CSVs, IDs, links, safety guard
    build_dashboard.py            Regenerates DASHBOARD.md from the CSV files
    build_reports.py              Regenerates the timeline, national matrix and public-records summaries
    new_site_reports.py           Creates missing site reports from the template
    repo_data.py                  Shared file paths and vocabularies
DASHBOARD.md                      Generated progress overview
CONTRIBUTING.md
```

## Research progress

| Phase | Description | Status |
| --- | --- | --- |
| 0 | Research planning | Complete |
| 1 | Research infrastructure and evidence collection | Infrastructure complete; collection not started |
| 2 | Evidence discovery and per-site assessment | Public-records discovery done for all ten; IRD observation plan prepared; website observation not started |
| 3 | Technical security research: passive-observation templates (Track A), authorization framework (Track B), AI-code/OWASP mapping (Track C), isolated lab | Infrastructure complete; passive observation and any authorized testing not started |
| 4 | Responsible disclosure | Not started |

Counts of sites verified and assessed, and of observations, are generated from the data files on the [dashboard](DASHBOARD.md).

## Working with the repository

Python 3.9 or later, no extra packages.

```bash
python3 scripts/validate.py          # check everything
python3 scripts/build_dashboard.py   # regenerate DASHBOARD.md after editing a CSV
python3 scripts/build_reports.py     # regenerate the timeline and public-records summaries
python3 scripts/new_site_reports.py  # create report files for newly added sites
```

## Responsible disclosure

Confirmed observations are reported to Sri Lanka CERT through its [official reporting channel](https://cert.gov.lk/report_incident) and then to the institution. Nothing site-specific is published before that. The full policy and message templates are in [`disclosure/`](disclosure/responsible-disclosure-policy.md).

Representatives of a listed institution can request their site's observations, a correction, or removal by opening an issue.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests that add active testing, or that describe an unreported weakness on a named site, will be closed.

## Author

Vinod Perera ([@Perera1325](https://github.com/Perera1325)), independent cybersecurity researcher, Colombo, Sri Lanka.

## Disclaimer

This is independent research. It is not affiliated with, commissioned by or endorsed by the Government of Sri Lanka, Sri Lanka CERT or any listed institution. It is not a penetration test, an audit or legal advice.
