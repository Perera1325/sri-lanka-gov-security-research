# National-level research executive summary

Status on 2026-11-11: evidence discovery from public records has had a second pass, with sources re-checked for six institutions. No website has been observed or assessed, and this summary reports no current vulnerability in any government website.

## What was done

Ten Sri Lankan government institutions were selected, and existing publications were searched for documented incidents, official security requirements and relevant research. No request was sent to any of the ten websites. Counts are generated from the repository's data files on the [dashboard](../DASHBOARD.md); the per-institution picture is in the [national research matrix](national-research-matrix.md).

## What the public record shows

- **Five of the ten institutions have a confirmed incident affecting their website.**
  - Ministry of Education, April 2024: unauthorized access, with a message posted on the site.
  - Department of Government Printing, December 2024: site hacked and content altered.
  - Ministry of Public Administration, May 2020 (homepage defaced) and April 2026 (cyberattack acknowledged by the Minister).
  - Ministry of Public Security, January 2026: police reported multiple instances of unauthorized access.
  - Sri Lanka Railways, June 2026: attack on the newly launched site's timetable section.
- **In four of those cases an official investigation was announced, and in none was a published outcome found.** No inquiry was reported for the Railways incident.
- **In two cases Sri Lanka CERT was reported to have recommended replacing the website** (Education and Government Printing). Whether either replacement has gone live was not found.
- **One institution suffered a back-end data loss.** Files were deleted from the National Medicines Regulatory Authority's document system in 2021; police made an arrest, and the outcome of the case was not found.
- **Shared government infrastructure has failed twice in recent years**: a ransomware attack on the government cloud in 2023 that lost about three months of email, and a week-long cloud outage in 2025 with no evidence of a cyber cause.
- **Two reports about immigration visa systems are unverified** and fall outside this study's scope.
- **For three institutions no compromise report was found** (Inland Revenue, Motor Traffic, Digital Economy). This is an absence of reports, not a finding of good security.

The [incident review](../docs/reviews/phase-2a-incident-review.md) separates, for each of the six institutions with a confirmed incident, what was confirmed, what was alleged, what investigation was announced, what remediation was confirmed and what outcome is unknown. Details and sources for all records are in the [historical incident timeline](historical-incident-timeline.md).

## The Education Ministry case

Daily Mirror reported on 10 April 2024 that Sri Lanka CERT had advised the Ministry to carry out a vulnerability assessment annually and that this had not been done, and that CERT recommended a new website. The same article said, without naming a source, that security patches and updates had not been applied. These are reported statements about the website as it was before April 2024. CERT's own statement was not found, and nothing is known about the current website.

## What the national guidelines require

Sri Lanka CERT issued two guidelines on 22 February 2022: one for websites and one for web applications. Both require a `gov.lk` domain, HTTPS, server-side input validation, multi-factor authentication for administrators, risk assessment of third-party components, patching, a CERT security assessment before release and at least yearly, and offline backups.

All ten institutions use a `gov.lk` domain. No other requirement has been assessed. Of the web application guideline's 32 requirements, seven can be informed at all by passive observation, four more only if an official body publishes a statement, and 21 cannot be checked from outside without authorization. See the [website guideline mapping](../research/cert-compliance-mapping.md) and the [web application guideline mapping](../research/cert-web-application-guideline-mapping.md).

## What is not known

- The current configuration of any of the ten websites.
- The cause and outcome of every investigation listed above.
- Whether any institution has had the assessments the guidelines require.
- Whether AI coding assistants were used on any government site. No source says so. The [literature review](../research/ai-code-security-literature-review.md) is a general academic strand and keeps that question separate.

## Strength of the evidence

Every incident record rests on news reporting of official statements, so confidence is capped at Medium. For six records the main article was opened and read; the rest were read as excerpts. No primary Sri Lanka CERT statement on any incident was located. No domain is fully verified: seven are preliminary and three partial. These limits are set out in [research limitations](../docs/research-limitations.md) and the [confidence and risk matrix](../docs/confidence-risk-matrix.md).

## Recommended next steps

1. Finish domain verification, then save dated copies of every source.
2. Look for primary statements in Sri Lanka CERT's annual reports and newsletters, police media releases, and parliamentary records.
3. Begin passive browser observation with one high-priority institution, following the [assessment checklist](../research/assessment-checklist.md).
4. Consider informing Sri Lanka CERT of the study before observation begins.

## To be added after assessment

Results by checklist item across the ten sites, observations by severity and OWASP category, common patterns, and disclosure status. None of these exists yet.
