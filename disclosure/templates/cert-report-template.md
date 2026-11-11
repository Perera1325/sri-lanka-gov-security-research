# Template: report to Sri Lanka CERT

Fill in every bracketed field from the evidence register. Do not send until the checks at the bottom are complete. Submit through the channel listed at <https://cert.gov.lk/report_incident>.

---

**Subject:** Security observation on [domain] – passive, non-intrusive research

Dear Sri Lanka CERT team,

I am an independent cybersecurity researcher based in Sri Lanka. During a passive review of publicly accessible government websites, I observed a configuration on the website below that I believe the responsible institution would want to know about.

**Website:** [institution name], [domain]
**Public URL:** [exact URL]
**Dates observed:** [first date] and [second date]
**Reference:** [finding ID]

**What was observed**
[Neutral description, two or three sentences.]

**How to see it**
[Steps an ordinary visitor can follow in a browser.]

**Why it matters**
[Short explanation with OWASP category.]

**Suggested fix**
[Specific remediation.]

**Assessed severity:** [Low / Medium / High / Critical], confidence [High / Medium / Low]

**Method.** I only viewed public pages in a standard web browser and consulted public records. I did not scan, test, log in to, or submit data to the website, and I did not access or store any personal or confidential information.

I have not shared these details publicly. I would be grateful if you could pass this to the institution, and I am glad to provide further information.

Yours faithfully,
[Full name]
[Contact email]
[Link to this repository's disclosure policy]

---

## Before sending

- [ ] The register row is `CONFIRMED OBSERVATION` with evidence from two dates
- [ ] No personal data, credentials or cookie values appear in the text or attachments
- [ ] No exploit steps or payloads are included
- [ ] The CERT reporting page was checked today for the current process
- [ ] The message has been read through once more and is being sent manually
