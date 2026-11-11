# Evidence guidelines

Every row in [`evidence-register.csv`](evidence-register.csv) must be backed by something a second person can check: a saved file under [`sources/`](sources/) or a link to a public record. Nothing is entered from memory.

## Register columns

| Column | Rule |
| --- | --- |
| `finding_id` | Site ID from the inventory, a hyphen, and a two-digit sequence: `IRD-01`. Never reused, even if a row is later withdrawn. |
| `website` | The domain exactly as written in `data/website-inventory.csv`. |
| `public_url` | The full URL where the observation was made. Must be a publicly linked page. |
| `observation_date` | `YYYY-MM-DD`, Sri Lanka time. The first date it was seen. |
| `component` | The header, cookie, script, page or certificate concerned. |
| `observation` | What was seen, as a neutral fact. No words such as "vulnerable" or "hackable". |
| `evidence_source` | Relative path to the saved file(s), or the URL of the public record. |
| `technical_explanation` | Why it matters, in one or two sentences. |
| `owasp_category` | One category from the [risk reference](../research/technology-risk-reference.md), for example `A05 Security Misconfiguration`. |
| `finding_status` | `CONFIRMED OBSERVATION`, `SUSPECTED`, `NOT TESTED` or `INFORMATIONAL`. |
| `potential_impact` | What could follow if the weakness were exploitable, stated conditionally. |
| `remediation` | The specific fix. |
| `severity` | `Critical`, `High`, `Medium`, `Low` or `Informational`. See [risk classification](../docs/risk-classification.md). |
| `confidence` | `High`, `Medium` or `Low`. |

Fields containing commas or quotes must be wrapped in double quotes. Edit the file with a spreadsheet program or a CSV-aware editor, save as UTF-8, and run `python3 scripts/validate.py` afterwards.

## Status rules

- `CONFIRMED OBSERVATION` needs evidence from two separate days.
- `SUSPECTED` is for anything seen once or inferred indirectly.
- `NOT TESTED` rows must say, in `technical_explanation`, what written authorization and controlled testing would be needed. Severity is `Informational`.
- `INFORMATIONAL` is for neutral facts. Severity is `Informational`.

## Saving evidence files

Store files under `evidence/sources/<site-id>/`, named:

```
<finding-id or check-id>_<YYYY-MM-DD>_<short-description>.<ext>
```

For example `evidence/sources/IRD/C03_2026-11-20_response-headers.png`.

- Screenshots must show the URL and, where possible, the system date.
- Prefer PNG for screenshots and PDF for saved pages.
- Domain-verification copies go in `evidence/sources/domain-verification/`.

## What must never be saved

- Personal data of any person: names with ID numbers, addresses, phone numbers, records.
- Credentials, tokens, keys or cookie values, even if publicly visible.
- Content from behind a login.
- Full copies of site source code beyond the snippet needed to show a marker.

Check every screenshot before committing. Crop or redact anything in the list above.

## Escalation rule

If a public page appears to expose credentials or personal data:

1. Stop. Do not open, download or copy it further.
2. Record only the URL, the date and a one-line neutral description, in a private note, not in this public repository.
3. Report it promptly to Sri Lanka CERT through its official channel. See the [disclosure policy](../disclosure/responsible-disclosure-policy.md).
4. Add nothing to the public register until the institution has resolved it or CERT agrees.

## Sensitive details and this public repository

The register is public. For any row rated Medium or above, keep the `observation` general until disclosure is complete, and hold the specifics privately.
