# Isolated security research lab

This folder documents a **local, isolated** laboratory for learning web application
security and reproducing vulnerability classes. It exists so that techniques are
practised against software that is **meant** to be attacked, never against a real site.

## The one rule that cannot be broken

**No lab tool, exercise, scan or payload is ever pointed at a government website or any
system the researcher does not own.** The lab runs on the local machine (`localhost`) or
inside a vendor-provided training sandbox. The government sites in this project are only
ever observed passively in a browser, as described in [scope](../research/scope.md).

Using an automated scanner, a fuzzer, an exploit or a login-bypass against a `.gov.lk`
site without written authorization is an offence under Sri Lanka's Computer Crimes Act
No. 24 of 2007. The lab is how the same skills are built legally.

## What is here

| File | Purpose |
| --- | --- |
| [lab-setup.md](lab-setup.md) | How the isolated environment is built and kept offline |
| [owasp-juice-shop.md](owasp-juice-shop.md) | Running and using OWASP Juice Shop locally |
| [owasp-webgoat.md](owasp-webgoat.md) | Running and using OWASP WebGoat locally |
| [portswigger-academy.md](portswigger-academy.md) | Using the hosted Web Security Academy safely |
| [vulnerability-analysis-TEMPLATE.md](vulnerability-analysis-TEMPLATE.md) | One write-up per vulnerability class |

## How lab work connects to the research

The lab is where a vulnerability **class** (for example, broken access control) is
understood and its remediation learned. The research repository then describes that class
in the abstract and maps it to OWASP, in
[Track C](../research/track-c-ai-owasp-mapping.md). The two are kept separate on purpose:
nothing learned in the lab is ever written up as if it were observed on a government site.
