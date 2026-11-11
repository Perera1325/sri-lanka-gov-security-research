# Technology risk reference

This file is general background on risk classes. It makes no claim about any site in the inventory; site-specific statements belong only in the evidence register and the site reports.

## OWASP Top 10 (2021) and what is passively visible

| Category | What it covers | Passively observable signals | Always NOT TESTED without authorization |
| --- | --- | --- | --- |
| A01 Broken Access Control | Users acting outside their permissions | None reliable | Any access-control behaviour |
| A02 Cryptographic Failures | Weak or missing protection of data in transit or at rest | No HTTPS, no redirect, expired certificate, missing HSTS, cookies without `Secure` | Server-side storage and key handling |
| A03 Injection | Untrusted input interpreted as code or queries | Absence of a Content-Security-Policy (a mitigation gap only) | Whether any input is injectable |
| A04 Insecure Design | Missing or ineffective control design | Client-side-only checks visible in public scripts | Whether the server enforces the same checks |
| A05 Security Misconfiguration | Insecure defaults, verbose errors, missing hardening | Missing security headers, version banners, default pages, verbose error text | Internal configuration |
| A06 Vulnerable and Outdated Components | Known-vulnerable libraries or platforms | Library or CMS version stated in public files, matched to a public advisory | Whether the advisory is exploitable here |
| A07 Identification and Authentication Failures | Weak login and session handling | Session cookie flags on unauthenticated pages | All login behaviour |
| A08 Software and Data Integrity Failures | Unverified code or updates | Third-party scripts without Subresource Integrity | Build and update pipelines |
| A09 Security Logging and Monitoring Failures | Inability to detect attacks | None | Everything |
| A10 Server-Side Request Forgery | Server fetching attacker-chosen URLs | None | Everything |

A passive signal indicates a hardening gap or a question worth asking. It does not show that a site can be compromised.

## Software supply chain

Public sites commonly load scripts, fonts and analytics from other hosts. Risk rises when a script is loaded without an `integrity` attribute, from a host the institution does not control, or from a project that is no longer maintained. Checklist item C08 records the observable part.

## Risks associated with AI-assisted code

These are patterns reported in the general literature on AI-generated code. They are listed for study, not attributed to any site.

- Authentication written from scratch with weak session or password handling
- Validation done only in the browser, with none on the server
- Secrets or API keys hardcoded in source, sometimes shipped to the client
- API calls made without authorization checks on each object
- Database queries built by string concatenation
- Dependencies added without pinning or review, including packages that do not exist under the suggested name

There is no reliable passive way to tell whether a site was built with AI assistance. This project states that a site used AI tools only if the institution or its vendor has said so publicly, with the source cited in the evidence register.

## Reading list to complete

Add full references here as each source is read. Entries must be sources actually consulted.

- OWASP Top 10: <https://owasp.org/Top10/>
- OWASP Secure Headers Project: <https://owasp.org/www-project-secure-headers/>
- MDN, HTTP security headers and Subresource Integrity: <https://developer.mozilla.org/en-US/docs/Web/Security>
