# Cybersecurity Posture of Sri Lankan Government Digital Infrastructure: A Ten-Institution Public-Evidence-Based Study

**An Exploratory Analysis of Historical Cyber Incidents, Security Governance and AI-Assisted Software Development Risks**

Vinod Ravindu Perera — Independent Researcher, Sri Lanka
Repository: https://github.com/Perera1325/sri-lanka-gov-security-research

> **Status.** This is a working first draft for internal review. It is not peer reviewed,
> not submitted, and not associated with any IEEE conference or journal. The IEEE-style
> structure is a formatting choice. All quantitative claims are drawn from the repository's
> data files; see the [evidence audit](evidence-audit.md).

---

## Abstract

See [abstract.md](abstract.md). In brief: an exploratory, public-evidence study of ten Sri
Lankan government institutions, compiling and classifying 20 historical incident records,
mapping 32 Sri Lanka CERT web-application requirements by external verifiability, and
reviewing AI-generated-code security literature mapped to OWASP. No active testing was
performed; no current weakness is claimed.

**Index Terms** — government cybersecurity, public-sector web security, Sri Lanka, security
governance, historical incident analysis, OWASP, AI-generated code, responsible research.

## 1. Introduction

Government institutions increasingly deliver public services through websites and
web applications. The security of that infrastructure is a matter of public interest:
failures can disrupt services, expose citizens' data, or undermine trust in digital
government. In Sri Lanka, several government websites have been publicly reported as
compromised, defaced or disrupted in recent years, and the national Computer Emergency
Readiness Team (Sri Lanka CERT) has issued security guidelines for government
organizations.

Rigorous, independent security assessment of government systems normally requires written
authorization, because unauthorized testing is unlawful. This creates a gap: citizens,
journalists and researchers can see that incidents occur, but have little structured,
verifiable information about the governance context around them or about what can be
responsibly known from the outside. This paper addresses that gap with a deliberately
constrained method. It uses only public evidence and passive observation, it classifies
every result by a fixed evidence scheme, and it is explicit about the boundary between what
public evidence can establish and what it cannot.

The study makes three contributions. First, it compiles and classifies a transparent
dataset of historical cyber incidents affecting ten selected institutions, separating
genuine website compromises from impersonation, shared-infrastructure failures and
unverified reports. Second, it maps the Sri Lanka CERT web-application security guideline
against the limits of external verifiability, quantifying how little of it can be checked
without authorization. Third, it reviews the peer-reviewed literature on AI-generated-code
security and maps the reported weakness classes to the OWASP Top 10, as context for future
secure-development policy — while establishing no link between any studied website and
AI-generated code. The whole project is open and reproducible, and its evidence register is
empty by design, because no site has been technically assessed.

## 2. Background and Related Work

**Sri Lanka's cyber-governance context.** Sri Lanka CERT, the national coordinating body,
publishes guidance for government organizations, including the *Website Security Guidelines
for Government Organizations* and a companion *Web Application Security Guidelines*, both
dated 2022. These documents set requirements for the design, deployment and maintenance of
government web applications. Unauthorized access to, or testing of, computer systems is an
offence under Sri Lanka's Computer Crimes Act No. 24 of 2007; a stated research purpose is
not a defence. These two facts frame the method: the guidelines provide a public yardstick,
and the law constrains the research to passive, public-evidence methods unless written
authorization is obtained.

**Public-evidence and OSINT approaches.** Where authorized testing is not available,
researchers and journalists rely on open-source intelligence: official statements, news
reporting, public registries and what an ordinary browser reveals. The strength of this
approach is legality and reproducibility; its weakness is that it observes configuration and
public record, not exploitability. This study treats that weakness as a first-class design
constraint rather than a footnote.

**AI-assisted software development security.** A growing body of peer-reviewed work examines
the security of code produced with AI assistants. Studies report that a substantial fraction
of AI-generated code contains known weakness patterns, that developers can be over-confident
in such code, that models can emit memorized secrets, and that models "hallucinate"
non-existent software packages at scale, creating a supply-chain risk. These findings concern
software development in general. This paper uses them only as policy context for secure
government procurement, and explicitly does not infer that any government website was built
with AI assistance.

## 3. Research Questions

- **RQ1.** What cybersecurity incidents have been publicly documented across the selected
  Sri Lankan government digital institutions, and how should they be classified?
- **RQ2.** How do publicly documented security-governance requirements compare with the
  evidence that is actually available about these institutions from the outside?
- **RQ3.** What cybersecurity risks associated with AI-assisted software development are
  relevant to government digital infrastructure, as a matter of policy context?

The study does not ask whether any specific website is currently vulnerable; answering that
would require authorized technical testing, which was not performed.

## 4. Research Methodology

The method is passive and public-evidence-based throughout. Full detail is in
[methodology.md](methodology.md); the workflow is shown in Figure 4.

1. **Scope.** Ten government institutions, each with a `gov.lk` domain. Only public,
   unauthenticated pages and public records are used. Logins, e-services, payment flows,
   APIs and unlinked paths are excluded. No scanning, fuzzing, injection, or login attempts.
2. **Domain verification.** Each institution's official domain is verified against
   independent government sources before any observation. A two-source standard is used;
   domains with one source are marked PRELIMINARY and those with weaker support PARTIAL.
3. **Public-record collection.** Incidents and governance statements are gathered from news
   reporting and official publications.
4. **Evidence classification.** Every result carries one of seven labels (Table 6),
   separating confirmed events from allegations and from absence of evidence, and historical
   events from current state.
5. **Governance mapping.** The CERT web-application guideline's 32 requirements are each
   classed by how far an outside observer can verify them.
6. **AI-code literature review.** Peer-reviewed sources are collected, their bibliographic
   details verified, and their weakness classes mapped to OWASP — kept strictly separate from
   the institution findings.
7. **Synthesis and limitations.** Findings are stated with their evidence labels, and the
   limits of the method are made explicit.

Reproducibility is built in: the dataset, the classification rules and validation scripts are
in the public repository, and every count in this paper is regenerated from the data files.

## 5. Institution Selection

Ten institutions were selected to span sectors where digital government security matters:
public security, public administration, public records, health regulation, education,
taxation, immigration, transport and digital-economy policy. The ten are listed in Table 1
with their verified domains and sectors. Selection favoured institutions with a public
service-delivery website and, in several cases, a publicly reported incident, so that the
governance questions could be examined against real events. Institutions considered but not
selected were recorded in a reserve list rather than discarded, to keep the selection
auditable.

Domain verification status at the time of writing is shown in Figure 2: none of the ten is
fully VERIFIED, seven are PRELIMINARY and three are PARTIAL. No institution has yet reached
the standard required before any site observation would begin. This is an honest statement of
where the project stands, not a limitation hidden from the reader.

## 6. Historical Cyber Incident Analysis (RQ1)

The incident dataset contains 20 records (Table 2). Thirteen are labelled CONFIRMED
HISTORICAL INCIDENT, two are POTENTIAL RISK – NOT VERIFIED, and five are NO PUBLIC EVIDENCE
AVAILABLE. Records are classified by the type of system affected, which is central to
avoiding the most common error in this area — treating every "government site hacked"
headline as a website vulnerability.

**Classification (Figure 1, Table 2).** Of the 20 records, ten concern an institution's
*website*, four concern a *backend or other system*, three are *impersonation* (fake sites
or phishing that mimic an institution without compromising it), two are *shared-infrastructure*
events affecting the government cloud rather than one institution, and one concerns official
*social-media* accounts rather than a website.

**Confirmed website incidents.** Six website incidents are confirmed from public reporting,
affecting five of the ten institutions (one institution has two). One is explicitly described
as a homepage defacement; the others are described as unauthorized access or alteration of
content. These six are the only records that can be read as confirmed compromises of an
institution's own website. The remaining four website-type records are NO PUBLIC EVIDENCE
AVAILABLE: a search found no reported compromise, which is not evidence that none occurred.

**Other categories.** The confirmed backend incident concerns files deleted from an internal
document system, not a website. The three confirmed impersonation records are attacks that
*imitate* an institution; they are a real threat to the public but are not weaknesses in the
institution's own website. The two shared-infrastructure events — a cloud-service disruption
and a ransomware incident with email-data loss — are national-platform failures not
attributable to any single institution. The two unverified reports are recorded separately
and never counted as confirmed.

**The central finding.** For none of the thirteen confirmed incidents was a *published
investigation outcome* found. Investigations or inquiries were announced in many cases, but
their results do not appear in the public record. The accountability gap — incidents are
reported, inquiries are announced, outcomes are not published — is the clearest result of the
historical analysis, and it holds regardless of the technical state of any current site.

## 7. Sri Lanka CERT Security Governance Analysis (RQ2)

Sri Lanka publishes a concrete yardstick: the CERT web-application security guideline sets 32
requirements across the application lifecycle. The governance question is not whether each
institution meets each requirement — that cannot be known from outside — but how much of the
yardstick is externally checkable at all.

The mapping (Table 4, Figure 3) classes each requirement by verifiability. Only seven of the
32 can be informed, even partly, by passive observation (for example, the use of HTTPS, the
presence of security headers, or the presence of third-party scripts). Four more could be
established only if an official body publishes a statement (for example, that a pre-release
CERT assessment was completed). Five require written authorization to test (for example,
server-side input validation or default-credential checks). The remaining sixteen are internal
practices that only the institution or CERT can confirm. In total, twenty-one of the 32
requirements cannot be checked by an outside researcher without authorization.

This has a direct implication for public accountability: most of the national security
standard for government web applications is, by its nature, invisible to the public. A citizen
cannot tell from the outside whether an institution validates input on the server, requires
multi-factor authentication for administrators, or completed a CERT assessment before going
live. The one requirement that is fully verifiable — the use of a `gov.lk` domain — is met by
all ten institutions.

A small number of published statements bear on specific requirements for named institutions
(for example, reporting that an annual CERT assessment had been advised but not carried out
before one 2024 incident). These are recorded, but each describes a past moment and none
establishes the present position. They are secondary news reports, not primary CERT
statements, and are labelled as such.

## 8. AI-Assisted Software Development Security Risks (RQ3)

As policy context for secure government procurement, the study reviews peer-reviewed work on
the security of AI-generated code. Eight papers were used, each with its authors, title, year,
venue and DOI or official URL verified (see [references.md](references.md)); no sources were
invented. Their reported weakness classes are mapped to the OWASP Top 10 (2021) in Table 5.

The literature reports, in general software-development settings, that a substantial share of
AI-generated code contains known weakness patterns (one study found about 40% of generated
programs vulnerable in designed scenarios; another found weaknesses in roughly a quarter to a
third of generated snippets found in real projects); that developers using assistants can be
more confident while being less secure; that code-completion tools can emit memorized
hard-coded credentials; and that models hallucinate non-existent software packages at scale,
creating a supply-chain risk. Results on whether assistance makes finished code less secure are
mixed across studies, and the consistent message is that human review which does not simply
trust the output is the control that matters.

Mapping these to OWASP shows coverage of injection, cryptographic failures, insecure design,
vulnerable components, authentication and integrity categories, and **no** coverage, in the
eight sources, of security misconfiguration (A05), logging and monitoring failures (A09), or
server-side request forgery (A10). These gaps are stated rather than filled.

**Scope boundary.** None of this is evidence about any Sri Lankan government website. No source
found in this project links any of the ten institutions to AI-generated code, and a site's
appearance, age, layout or vendor is never treated as evidence of how it was built. The
relevance is forward-looking: as governments adopt AI-assisted development, procurement and
acceptance controls should account for these risk classes.

## 9. Discussion

Three themes emerge. First, **incidents are real but accountability is thin.** Confirmed
website compromises affect half of the selected institutions, yet published investigation
outcomes are absent. Second, **most of the security standard is externally invisible.** The
public can verify only a small part of the CERT guideline, which limits what any
public-evidence study — including this one — can conclude about security posture. Third, **the
responsible boundary is a finding, not just a constraint.** The fact that twenty-one of 32
requirements need authorization to check is precisely why independent assessment of government
systems requires institutional cooperation; it is an argument for authorized, coordinated
assessment rather than for either unauthorized testing or silence.

Taken together, the results argue for publishing incident outcomes and basic, non-sensitive
security status, and for a lawful channel through which independent researchers can assess
government systems with authorization. The study's method and dataset are offered as a starting
point for that work.

## 10. Recommendations

For government institutions and Sri Lanka CERT:

1. **Publish incident outcomes.** When an inquiry into a government website incident concludes,
   publish a non-sensitive summary. The absence of published outcomes is the study's clearest
   gap.
2. **Publish basic security status.** A small amount of public, non-sensitive information
   (for example, confirmation that a pre-release CERT assessment was completed) would make a
   larger part of the national standard externally accountable.
3. **Provide a lawful assessment channel.** A coordinated vulnerability-disclosure and
   authorized-assessment programme would let independent researchers help, within the law.
4. **Account for AI-assisted development in procurement.** Acceptance criteria should require
   human security review of generated code, dependency verification, and secrets handling,
   consistent with the CERT guideline.

For independent researchers: keep to passive, public-evidence methods until written
authorization is in hand; classify evidence explicitly; and separate historical incidents from
current state.

## 11. Limitations and Threats to Validity

These limitations are intrinsic to the method and are stated plainly.

- **No technical assessment was performed.** No scanning, no penetration testing, no
  exploitation. The project's evidence register is empty; no direct technical observation of any
  site exists. No current exploitable weakness is claimed for any institution.
- **Historical incidents are not current weaknesses.** A confirmed past incident says an event
  occurred; it does not imply that any cause persists today.
- **Most records rest on secondary reporting.** Incident records rely largely on news sources,
  several read as search excerpts rather than full saved pages; where a CERT or official
  statement was not found, this is recorded. Secondary news is never presented as a primary
  government statement.
- **Domain verification is incomplete.** No institution is fully VERIFIED (seven PRELIMINARY,
  three PARTIAL). Observations would not begin until verification is complete.
- **Absence of evidence is not evidence of absence.** NO PUBLIC EVIDENCE AVAILABLE means a
  search did not find a report, not that no incident occurred.
- **Construct validity of "incident."** The classification uses the type of system affected;
  reasonable analysts might group borderline cases differently. The raw dataset is published so
  that others can reclassify.
- **Selection.** Ten institutions are not a representative sample of all government bodies;
  results do not generalize to the whole of government.
- **The AI-code literature concerns software in general**, not these websites, and three OWASP
  categories are uncovered by the eight sources.

## 12. Conclusion

This exploratory study shows what public evidence can and cannot establish about the security
posture of Sri Lankan government digital infrastructure. From public records alone, six website
compromises across five of ten institutions are confirmed, no published investigation outcomes
are found, and only a small part of the national web-application security standard is externally
verifiable. The security of AI-generated code is a relevant policy concern for future
procurement, but is not connected here to any specific site. The main contribution is a
transparent, reproducible, legally constrained method and an open dataset for public
accountability research — together with an honest account of its limits. The natural next step
is authorized, coordinated assessment that can convert public questions into verified answers.

## 13. References

See [references.md](references.md) for the full list with verified bibliographic details and
DOIs. News sources for individual incidents are cited per record in the repository's
[historical incident timeline](../reports/historical-incident-timeline.md) and
`data/historical-incidents.csv`.

## Acknowledgement of tool use

Parts of this research infrastructure and draft were prepared with the assistance of an AI
system, under the author's direction and review. All data classification decisions, the
restriction to passive methods, and the verification of references are the author's
responsibility.
