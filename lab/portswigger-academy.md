# PortSwigger Web Security Academy

The Web Security Academy is a free, hosted set of labs run by PortSwigger. The labs run in
the vendor's own sandbox in the browser, so there is nothing to install and nothing local
to isolate — but the same rule applies: the techniques are practised **only** inside the
Academy's labs.

## How it is used here

- Work the topic tracks relevant to this project (access control, authentication, SQL
  injection, information disclosure, and so on).
- Each Academy lab has a clear objective and a known solution; use them to understand the
  class, then write it up with the [analysis template](vulnerability-analysis-TEMPLATE.md).

## Boundaries

- Only the Academy's own lab URLs are used. The techniques shown there are never tried
  against any other site, and never against a `.gov.lk` site.
- If a proxy tool (such as Burp) is used, it is pointed at the Academy lab only, from the
  **LAB** browser profile, never the **RESEARCH** profile.
