# Table 5. AI-generated-code weakness classes mapped to OWASP Top 10 (2021)

From `research/track-c-ai-owasp-mapping.md`, using the eight verified papers (P1–P8) in the
project's literature review. This is a taxonomy of risks reported for AI-generated code in
general; it is not evidence about any government website.

| OWASP 2021 | Source(s) | Reported finding |
| --- | --- | --- |
| A01 Broken Access Control | P5 (indirect) | Backend tasks include access-controlled scenarios; ~half of correct programs exploitable. Not isolated. |
| A02 Cryptographic Failures | P4 | Insufficiently random values (CWE-330) the most frequent weakness category. |
| A03 Injection | P1, P2, P4 | SQL-injection-prone and XSS/command-injection patterns (CWE-79, CWE-94). |
| A04 Insecure Design | P2 | Assisted developers more likely to believe insecure code was secure. |
| A05 Security Misconfiguration | — | Not covered by the eight papers. |
| A06 Vulnerable / Outdated Components | P6 | Package hallucination: non-existent dependencies at scale (supply-chain risk). |
| A07 Identification / Authentication Failures | P7, P5 (indirect) | Memorized hard-coded credentials; login scenarios not broken out. |
| A08 Software / Data Integrity Failures | P6 | Hallucinated package names registrable by an attacker. |
| A09 Logging / Monitoring Failures | — | Not covered. |
| A10 Server-Side Request Forgery | — | Not covered. |

Three categories (A05, A09, A10) are **not covered** by the current sources; this is stated
rather than filled in.
