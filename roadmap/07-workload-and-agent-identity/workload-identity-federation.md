# Workload identity federation

**TL;DR:** Workload identity federation lets a workload trade a token its platform issued for
short-lived cloud credentials, avoiding a stored long-lived cloud secret. A CI runner might
otherwise use a copied cloud access key that works for whoever steals it. Instead, GitHub
Actions mints a signed JWT for the job, and the cloud checks its subject and other claims
against administrator-configured trust conditions before returning a short-lived credential.
Exchange mechanics vary by provider. RFC 7523 defines one JWT bearer authorization grant in
which a JWT is posted as an assertion and validated for the authorization server's audience. A
common mistake is a trust condition that untrusted repositories can satisfy.

A configured trust lets a workload exchange a platform-issued identity token, such as a GitHub
Actions OIDC token or a Kubernetes projected service-account token, for short-lived cloud
credentials instead of storing a long-lived secret. The exchange mechanics vary by provider;
RFC 7523's JWT bearer grant, a JWT posted as the assertion, is one standardized form. Cloud VM
identity is a separate mechanism: AWS's instance identity document is signed JSON, not an OIDC
token (→ [Attestation: RATS](attestation-rats.md)).

## Resources

- [@official@GitHub Actions OIDC / cloud workload identity federation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [@official@RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
