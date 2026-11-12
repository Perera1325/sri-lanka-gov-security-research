# OWASP WebGoat (local)

WebGoat is an OWASP teaching application with guided lessons on specific vulnerability
classes. Where Juice Shop is a free-form target, WebGoat walks through one concept at a
time, which suits careful write-ups.

## Run it locally

Docker:

```
docker run --rm -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

Then open `http://localhost:8080/WebGoat` in the **LAB** browser profile.

## How it is used here

WebGoat's lessons map cleanly onto OWASP categories. For each lesson that matters to this
project, complete it and record a write-up with the
[analysis template](vulnerability-analysis-TEMPLATE.md), noting the secure pattern as well
as the insecure one.

## Boundaries

- Local only; the second port (9090, WebWolf) is also bound to `localhost`.
- No lesson, tool or payload is ever aimed at an external address.
