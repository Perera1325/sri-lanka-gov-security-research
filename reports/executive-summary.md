# National-level research executive summary

Status on 2026-11-11: evidence discovery from public records is complete for a first pass. No website has been observed or assessed, and this summary reports no current vulnerability in any government website.

## What was done

Ten Sri Lankan government institutions were selected, and existing publications were searched for documented incidents, official security requirements and relevant research. No request was sent to any of the ten websites. Counts are generated from the repository's data files on the [dashboard](../DASHBOARD.md); the per-institution picture is in the [national research matrix](national-research-matrix.md).

## What the public record shows

- **Four of the ten institutions have a confirmed website incident on record.** The Department of Government Printing's site was hacked and altered in December 2024. The Ministry of Public Administration's site was defaced in 2020 and attacked again in April 2026. The Ministry of Public Security's site was reported targeted in January 2026. Sri Lanka Railways' newly launched site was attacked in June 2026. Each was acknowledged by an official body, as reported in the press.
- **Three of those incidents date from 2026**, and no published outcome of the resulting inquiries was found.
- **One institution suffered a back-end data loss.** Files were deleted from the National Medicines Regulatory Authority's document system in 2021, with no backup available according to press reports.
- **Shared government infrastructure has failed twice in recent years**: a ransomware attack on the government cloud in 2023 that lost about three months of email, and a week-long cloud outage in 2025 with no evidence of a cyber cause.
- **Two reports about immigration visa systems are unverified** and fall outside this study's scope.
- **For four institutions no incident report was found.** This is an absence of reports, not a finding of good security.

Details and sources for all 19 records are in the [historical incident timeline](historical-incident-timeline.md).

## What the national guideline requires

Sri Lanka CERT's *Website Security Guidelines for Government Organizations* (Version 1, February 2022) requires, among other things, a `gov.lk` domain, HTTPS, a current CMS version, server-side input validation, multi-factor authentication for back-end access, risk assessment of third-party components, patching, security assessment by CERT before release and at least yearly, and offline backups.

All ten institutions use a `gov.lk` domain. No other requirement has been assessed. Four of the nine mapped requirements can be partly checked by browser observation once domains are verified; the other four cannot be confirmed from outside at all. See the [compliance mapping](../research/cert-compliance-mapping.md).

## What is not known

- The current configuration of any of the ten websites.
- The cause and outcome of the 2026 incidents.
- Whether any institution has had the assessments the guideline requires.
- Whether AI coding assistants were used on any government site. No source says so, and the [literature review](../research/ai-code-security-literature-review.md) is a general academic strand only.

## Strength of the evidence

Every incident record currently rests on news reporting of official statements, read as excerpts. Confidence is therefore capped at Medium. No domain is fully verified: seven are preliminary and three partial. These limits are set out in [research limitations](../docs/research-limitations.md) and the [confidence and risk matrix](../docs/confidence-risk-matrix.md).

## Recommended next steps

1. Finish domain verification, then save dated copies of every source.
2. Replace news reports with primary statements from Sri Lanka CERT, ICTA, the police and the institutions wherever they exist.
3. Begin passive browser observation with one high-priority institution, following the [assessment checklist](../research/assessment-checklist.md).
4. Consider informing Sri Lanka CERT of the study before observation begins.

## To be added after assessment

Results by checklist item across the ten sites, observations by severity and OWASP category, common patterns, and disclosure status. None of these exists yet.
