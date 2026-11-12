# Track C — AI-generated code security, mapped to OWASP

This note maps the weakness classes reported in the project's
[AI-generated code security literature review](ai-code-security-literature-review.md) onto
the OWASP Top 10 (2021). It adds no new sources: it uses the eight papers (P1–P8) whose
titles, authors, years and DOIs are already verified in that review. The aim is to make the
general software-security literature easy to line up with the categories used in the rest
of the repository.

## What this note is not

This note is about AI-generated code **in general**. It says nothing about any Sri Lankan
government website. As the literature review states, no source found for this project links
any of the ten institutions to AI-generated code, and a site's appearance, age or vendor is
never evidence of how it was built. Nothing here may be cited as a finding about a specific
site.

## Mapping

| OWASP 2021 | Supported by | What the literature actually shows |
| --- | --- | --- |
| A01 Broken Access Control | P5 (indirect) | BaxBench's backend tasks include access-controlled scenarios; about half of functionally correct programs were exploitable. No study isolates access control in generated code. |
| A02 Cryptographic Failures | P4 | Insufficiently random values (CWE-330) were the most frequent weakness category in generated code found in real projects. |
| A03 Injection | P1, P2, P4 | Generated code reproduced SQL-injection-prone and XSS/command-injection patterns (CWE-79, CWE-94) depending on prompt wording. |
| A04 Insecure Design | P2 | Assisted developers were more likely to believe insecure code was secure — a design-and-process weakness, not a single bug. |
| A05 Security Misconfiguration | — | Not directly studied by the eight papers. Treated as NOT COVERED. |
| A06 Vulnerable and Outdated Components | P6 | Package hallucination: models invent non-existent dependencies at scale, a supply-chain risk ("slopsquatting"). Outdated-but-real versions are not measured by these papers. |
| A07 Identification and Authentication Failures | P7, P5 (indirect) | Code-completion tools can emit memorized hard-coded credentials (two valid ones were found); BaxBench login scenarios sit here but are not broken out. |
| A08 Software and Data Integrity Failures | P6 | Package hallucination is also an integrity/supply-chain threat: a hallucinated name can be registered by an attacker. |
| A09 Security Logging and Monitoring Failures | — | Not studied by the eight papers. NOT COVERED. |
| A10 Server-Side Request Forgery | — | Not studied by the eight papers. NOT COVERED. |

## Reading the mapping

- Three categories (A05, A09, A10) are **not covered** by the current sources. That is
  stated rather than filled in, so the gap is visible.
- "Indirect" means the paper's setting includes that category but does not measure it on its
  own. Those rows should not be quoted as rates for that category.
- The consistent finding across P2, P3 and P8 is that **human review that does not simply
  trust the output** is the control that matters. That maps to A04 (design and process) more
  than to any single bug class.

## Use in the lab

When a class in this table is reproduced in the [isolated lab](../lab/README.md), the lab
write-up links back to the row here, so the academic claim and the hands-on understanding
stay connected — and both stay separate from any statement about a government site.
