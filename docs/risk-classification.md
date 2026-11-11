# Risk classification

Severity reflects what was actually observed, not what might be possible. A passive study will mostly produce Low and Informational ratings, and that is the expected outcome.

## Severity levels

| Severity | When it applies in this study | Example |
| --- | --- | --- |
| Critical | Directly visible exposure of credentials or bulk personal data on a public page. | A live key in a public script. |
| High | Directly visible exposure of limited sensitive data, or a public page served in a state that plainly endangers visitors. | A personal record on a public URL. |
| Medium | A confirmed weakness with a well-known attack path. | A data-collecting page with no HTTPS; a library version with a published serious advisory. |
| Low | A hardening gap. | A missing security header; a cookie without `SameSite`. |
| Informational | A neutral fact, or anything not tested. | A technology fingerprint; every `NOT TESTED` item. |

Critical and High items follow the escalation rule in the [evidence guidelines](../evidence/evidence-guidelines.md): report first, record no details publicly.

## Rules

1. **No severity from speculation.** If the rating depends on something that was not observed, the row is `NOT TESTED` and `Informational`.
2. **Configuration is not exploitability.** A missing header or an old version number is described as a weakness or gap, never as a vulnerability.
3. **One step down when unsure.** If two levels seem to fit, use the lower and explain in the report.
4. **Explain every rating.** The site report gives one sentence of reasoning per finding.

## Confidence levels

| Confidence | Meaning |
| --- | --- |
| High | Read directly from the response or page on two separate days, with saved evidence. |
| Medium | Seen once directly, or taken from a reliable third-party record. |
| Low | Inferred from an indirect marker, such as a file path that suggests a product. |

## Status and severity combinations

| Finding status | Allowed severity |
| --- | --- |
| `CONFIRMED OBSERVATION` | Any |
| `SUSPECTED` | Medium, Low or Informational |
| `NOT TESTED` | Informational only |
| `INFORMATIONAL` | Informational only |

`scripts/validate.py` enforces this table.
