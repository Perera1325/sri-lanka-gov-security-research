# Research limitations

This study describes what is publicly observable. It cannot say whether any site is secure or insecure overall, and its results should not be read that way.

## Limits of the method

- **Passive only.** No request is made that an ordinary visitor would not make. Most serious classes of weakness (access control, injection, authentication) cannot be assessed this way and are recorded as `NOT TESTED`.
- **Configuration, not exploitability.** A missing header or an outdated version number shows a hardening gap. It does not show that an attack would succeed.
- **Public pages only.** Login areas, e-services, payment flows and APIs are excluded, and these are where most of the risk to citizens' data lies.
- **Fingerprints can mislead.** Version strings may be stale, altered or deliberately hidden. Patches are often applied without changing the visible version.
- **A point in time.** Each observation is true for the date recorded. Sites change, and a result may be out of date when read.
- **A view from one place.** Sites may respond differently by location, device or network. Observations are made from one location in Sri Lanka.
- **Small sample.** Ten sites were chosen to cover sectors, not at random. Results do not generalize to all government websites.

## Limits of the evidence

- Domain verification in Phase 0 relied on sources found by web search and has not yet been re-confirmed for every site. See [government-sites.md](../research/government-sites.md).
- Third-party records such as certificate logs and public datasets are used as published and may contain errors.
- The study is carried out by one independent researcher without institutional review. Independent re-checking is welcome; see [CONTRIBUTING.md](../CONTRIBUTING.md).

## What the study does not claim

- It does not claim that any listed website is vulnerable.
- It does not claim that any website was built with AI assistance.
- It does not rank institutions by security.
- It is not a penetration test, an audit or legal advice.

## Legal note

Unauthorized access to computer systems is an offence under Sri Lanka's Computer Crime Act, No. 24 of 2007. The method is designed to stay within ordinary public use of websites. Anyone extending this work should confirm the legal position with a qualified person first.
