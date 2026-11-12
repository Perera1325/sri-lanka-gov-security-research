# OWASP Juice Shop (local)

Juice Shop is a deliberately insecure web application maintained by OWASP for training. It
covers the OWASP Top 10 and many other issues. It is designed to be attacked.

## Run it locally

Docker:

```
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

Then open `http://localhost:3000` in the **LAB** browser profile.

Node.js (alternative):

```
git clone https://github.com/juice-shop/juice-shop.git
cd juice-shop
npm install
npm start
```

## How it is used here

Work through the built-in challenges and, for each vulnerability class that is relevant to
this project (access control, injection, authentication, dependency and configuration
issues), write it up with [vulnerability-analysis-TEMPLATE.md](vulnerability-analysis-TEMPLATE.md).

## Boundaries

- Keep it on `localhost`. Do not deploy a public instance.
- The scoreboard and hints are part of the tool; use them.
- Nothing here is pointed at any external site.
