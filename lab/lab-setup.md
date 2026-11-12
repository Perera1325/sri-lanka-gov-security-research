# Lab setup

A local environment for practising web security against intentionally vulnerable
applications. Everything here runs on the researcher's own machine.

## Principles

1. **Offline by default.** The deliberately vulnerable apps run on `localhost`. They are
   not exposed to the internet and are not placed on a public IP.
2. **Isolation from the research targets.** No tool configured here is ever given a
   `.gov.lk` address. Keep lab work and the passive-observation work in separate browser
   profiles so a scanner extension can never fire at a real site by habit.
3. **Disposable.** Containers are rebuilt, not patched. Nothing of value is stored inside
   them.
4. **No shared credentials.** Lab accounts use throwaway passwords that are not reused
   anywhere else.

## Option A — Docker (recommended)

Docker keeps each app contained and removable. Install Docker Desktop (Windows/macOS) or
Docker Engine (Linux), then pull the images named in each app's page.

To confirm the containers are bound to localhost only, check that published ports show
`127.0.0.1` rather than `0.0.0.0`:

```
docker ps
```

If a port is on `0.0.0.0`, re-run the container binding it explicitly, for example
`-p 127.0.0.1:3000:3000`.

## Option B — Node / Java directly

Juice Shop can run under Node.js and WebGoat under Java if Docker is not available. The
per-app pages give both routes. When running directly, start the app, confirm it answers
on `http://localhost:<port>`, and do the exercises in a browser.

## Browser separation

Create a dedicated browser profile named, for example, **LAB**. Install any testing
extensions only in that profile. Keep the **RESEARCH** profile (used for passive
observation of `.gov.lk` sites) free of scanners, proxies and automation extensions. This
separation is the practical guarantee that a lab tool never reaches a government site.

## What never belongs in the lab

- Any government hostname, IP, or URL.
- Any credential, token or cookie captured from a real site.
- Any copy of a government site pulled down for "offline testing".
