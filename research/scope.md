# Scope

The study covers the public, unauthenticated pages of ten Sri Lankan government websites, observed passively. The authoritative list is [`data/website-inventory.csv`](../data/website-inventory.csv); the reasoning behind it is in the [research plan](research-plan.md).

## In scope

- The home page and other public pages of each inventoried domain that are reachable by following ordinary links.
- What a normal browser page load reveals: page source, linked scripts and styles, response headers, cookies set without logging in.
- Public third-party records about the domains: certificate transparency logs, DNS, WHOIS, published datasets (for example the LDFLK government website scorecard), news and official reports.
- General literature on OWASP Top 10 risk classes and on risks in AI-assisted code. See [technology-risk-reference.md](technology-risk-reference.md).

## Out of scope

- Login pages, e-service portals, payment or booking flows, and any subdomain that hosts them. Their existence may be noted; they are not examined.
- Admin interfaces and any path the site does not link to publicly.
- APIs, other than noting that a public page calls one.
- Personal or confidential data. If encountered, it is not opened, copied or stored. See [evidence guidelines](../evidence/evidence-guidelines.md).
- Any domain not in the inventory.

## Prohibited activities

None of the following is performed, and no tooling for them belongs in this repository:

- Vulnerability scanning, port scanning, automated crawling or spidering
- Fuzzing, directory or parameter brute-forcing
- Exploitation or proof-of-concept payloads of any kind
- Login attempts, password resets, authentication or authorization bypass
- Form submission, account creation, or changes to any record
- API probing or parameter manipulation
- Load or denial-of-service testing

Anything that would need one of these to confirm is recorded as `NOT TESTED`.

## Changing the scope

A site is added, removed or swapped only by editing the inventory in a commit that explains why. Active testing enters scope only with a signed authorization letter from the institution that names the target, test types, dates and a contact person. A copy of that letter must be referenced in this file before any such work begins.
