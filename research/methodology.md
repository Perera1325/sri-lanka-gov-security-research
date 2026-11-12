# Methodology

Every site is assessed with the same passive checklist, every observation is logged in one evidence register, and every claim in a report must trace back to a register row.

## Principle

An activity is allowed only if an ordinary member of the public could do the same thing in a browser, or the data already exists in a public third-party record. The full allowed and prohibited lists are in [scope.md](scope.md).

## Phases

| Phase | Name | Output | Status |
| --- | --- | --- | --- |
| 0 | Research planning | [research-plan.md](research-plan.md) | Complete |
| 1 | Research infrastructure and evidence collection | This repository structure, inventory, register, checklist, templates | Infrastructure complete; collection not started |
| 2a | Evidence discovery from public records | [National research matrix](../reports/national-research-matrix.md), [incident timeline](../reports/historical-incident-timeline.md), [CERT compliance mapping](cert-compliance-mapping.md), [literature review](ai-code-security-literature-review.md) | First pass complete |
| 2b | Per-site browser assessment | Completed reports in [`reports/individual-sites/`](../reports/individual-sites/) | Not started |
| 3 | Cross-site analysis | [`reports/executive-summary.md`](../reports/executive-summary.md) | Not started |
| 4 | Responsible disclosure | Reports sent through official channels | Not started |

## Workflow for one site

1. **Confirm the domain.** The site's row in [`data/website-inventory.csv`](../data/website-inventory.csv) must read `VERIFIED` before assessment starts. See [government-sites.md](government-sites.md) for what that requires.
2. **Run the checklist.** Work through [assessment-checklist.md](assessment-checklist.md) in a single browser session. Record each result in a copy of [`data/scorecard-template.csv`](../data/scorecard-template.csv).
3. **Save evidence.** Store screenshots and saved pages under [`evidence/sources/`](../evidence/sources/) following the [evidence guidelines](../evidence/evidence-guidelines.md).
4. **Log observations.** Add one row per observation to [`evidence/evidence-register.csv`](../evidence/evidence-register.csv). Map each to an OWASP category and set its status.
5. **Re-check.** Look again on a different day. Only an observation seen twice may be marked `CONFIRMED OBSERVATION`.
6. **Classify.** Assign severity and confidence using [risk-classification.md](../docs/risk-classification.md).
7. **Write the report.** Fill in the site's file in `reports/individual-sites/`, citing register IDs.
8. **Update tracking.** Set `research_status` and `last_observation_date` in the inventory, then run the two scripts below.

## Finding statuses

| Status | Meaning |
| --- | --- |
| `CONFIRMED OBSERVATION` | Seen on two separate days, with saved evidence for both. |
| `SUSPECTED` | Seen once, or inferred from an indirect marker. Needs a re-check. |
| `NOT TESTED` | Cannot be determined passively. The row states what authorization would be needed. |
| `INFORMATIONAL` | A neutral fact about the site (for example the technology in use) that is not a weakness. |

## Keeping the repository consistent

```bash
python3 scripts/validate.py          # structure, CSV format, IDs, links, safety guard
python3 scripts/build_dashboard.py   # regenerates DASHBOARD.md from the CSV files
python3 scripts/build_reports.py     # regenerates the incident timeline and public-records summaries
```

All scripts read local files only and make no network connections.

## Recording a historical incident

1. Add one row to [`data/historical-incidents.csv`](../data/historical-incidents.csv) with the next `INC-nn` ID.
2. Put what an official body confirmed in `confirmed_details` and everything else in `alleged_or_unconfirmed_details`.
3. Choose the label from [evidence classification](../docs/evidence-classification.md) and the confidence from the [confidence and risk matrix](../docs/confidence-risk-matrix.md).
4. Record no exploit detail, personal data or internal system detail, even if a source publishes it.
5. Run `build_reports.py`, `build_dashboard.py` and `validate.py`.

## OWASP reference version

Observations are mapped to the OWASP Top 10 (2021) categories, as set in the research plan. OWASP has since published a newer edition; check the current list at <https://owasp.org/Top10/> and decide before Phase 2 whether to map to both.
