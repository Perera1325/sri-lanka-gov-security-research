# Responsible disclosure policy

Observations are reported privately to Sri Lanka CERT and the owning institution before any site-specific detail is published. No report has been sent to date.

## When a report is prepared

A disclosure draft is written only when an observation is:

- recorded in the [evidence register](../evidence/evidence-register.csv) as `CONFIRMED OBSERVATION`,
- reproducible by a second ordinary browser visit, and
- rated Low or above under the [risk classification](../docs/risk-classification.md).

Suspected, untested and informational items are not reported individually. They may be summarized for an institution on request.

## Channels

1. **Sri Lanka CERT (primary).** CERT asks that incidents be submitted through its official reporting portal and lists 101 as its hotline ([Sri Lanka CERT, n.d.](https://cert.gov.lk/report_incident)). Check that page for the current process before each submission.
2. **The institution.** Where the institution publishes a security, IT or webmaster contact on its official site, notify it after CERT has acknowledged the report, or as CERT advises.

Contact details are taken only from the institution's own verified domain, never from search results or third-party directories.

## What a report contains

- Site, exact public URL and observation dates
- What was observed, in neutral terms
- How to see it in an ordinary browser
- Why it matters and the suggested fix
- A statement that only passive observation was used

A report never contains exploit steps, proof-of-concept code, personal data, credentials or cookie values.

## Timeline

| Step | Target |
| --- | --- |
| Report to CERT | Within 7 days of confirming; immediately for Critical or High |
| Follow-up if no acknowledgement | After 14 days |
| Publication of site-specific detail | After the institution confirms a fix, or 90 days after the report with CERT's agreement |
| Publication of aggregate statistics | Any time, provided no site can be identified with an unresolved Medium-or-above item |

The researcher will extend these periods on reasonable request from CERT or the institution.

## Rules for the researcher

- Every message is written, reviewed and sent manually. Nothing in this repository sends email or submits forms.
- A record of each report (date, channel, reference number, response) is kept privately, not in this public repository, until the matter is closed.
- No payment, reward or recognition is requested.
- If an institution asks for testing beyond passive observation, written authorization is required first. See [scope](../research/scope.md).

## Templates

- [Report to Sri Lanka CERT](templates/cert-report-template.md)
- [Notification to an institution](templates/institution-notification-template.md)
- [Follow-up message](templates/follow-up-template.md)

## For institutions

If you represent a listed institution and would like the observations for your site, a correction, or removal from the study, please open an issue in this repository or contact the repository owner through GitHub.
