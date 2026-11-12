# Track B — authorization framework

Active security testing of a government website is lawful only with the **written
authorization** of the body that owns the system. This folder holds the request
templates and the rule that governs them.

## The rule

**No active testing of any `.gov.lk` system happens until a signed authorization for that
exact system is in hand, and then only within the approved scope and window.** Active
testing means anything beyond ordinary passive browsing: scanning, fuzzing, injection,
authentication or access-control testing, API probing, or TLS protocol testing. Passive
observation (described in [scope](../research/scope.md)) does not need authorization and is
the only thing done until an authorization exists.

In Sri Lanka, unauthorized access or testing is an offence under the Computer Crimes Act
No. 24 of 2007. A research purpose is not a defence.

## Status tracking

The authorization status of each institution is recorded in
[`data/authorizations.csv`](../data/authorizations.csv). Every institution currently reads
`NONE REQUESTED`. A row only moves to `GRANTED` when a signed authorization with a
reference, scope and validity window exists.

## Files

| File | Purpose |
| --- | --- |
| [authorization-request-TEMPLATE.md](authorization-request-TEMPLATE.md) | The master request; copy it per institution |
| `requests/<id>-<domain>.md` | A pre-addressed request for each of the ten institutions |

## Process

1. Complete the request for the institution, filling every placeholder.
2. Send it through an official channel (the institution, or Sri Lanka CERT as the national
   coordinator). **These files are drafts; nothing here sends email.**
3. If authorization is granted, record it in `data/authorizations.csv` and **compare the
   approved scope with the request before any testing begins.** Test only what was
   approved.
4. If it is declined or unanswered, the institution stays passive-only. Do not proceed.
