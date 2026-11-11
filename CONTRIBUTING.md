# Contributing

Contributions that improve accuracy, documentation or reproducibility are welcome. Contributions that involve any active testing of government systems are not, and will be closed.

## Ground rules

1. **Passive only.** Read [scope](research/scope.md) first. Do not scan, crawl, fuzz, probe, log in to or submit data to any website in the inventory, and do not add tooling that could.
2. **No unreported findings in public.** Do not open an issue or pull request describing a weakness on a named government site. Follow the [responsible disclosure policy](disclosure/responsible-disclosure-policy.md) instead.
3. **No sensitive data.** Never commit personal data, credentials, tokens or cookie values, including inside screenshots.
4. **Evidence for everything.** A change to the inventory or the evidence register must come with its source, following the [evidence guidelines](evidence/evidence-guidelines.md).
5. **Neutral language.** Describe what was observed. Do not call a site vulnerable.

## Useful contributions

- Independent re-confirmation of a domain's official status, with a dated source
- Corrections to the checklist, risk reference or documentation
- Improvements to the local validation and dashboard scripts
- References for the reading list in the [risk reference](research/technology-risk-reference.md)

## Before opening a pull request

```bash
python3 scripts/build_dashboard.py
python3 scripts/validate.py
```

Both must finish without errors. They need only Python 3.9 or later and no extra packages.

## Institutions

If you represent a listed institution, see the last section of the [disclosure policy](disclosure/responsible-disclosure-policy.md).
