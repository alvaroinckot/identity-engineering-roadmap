# Non-human identities

**TL;DR:** A non-human identity is an account or credential that software uses to act, such as
a service account or access key. It often authenticates with a secret rather than a person at a
keyboard, though certificates and federated credentials are alternatives. Its failures differ
from human login failures: a repository leaks a key, an account outlives its service, a
credential has no expiry, or an integration receives excessive permissions. The OWASP Non-Human
Identities Top 10, an Incubator project, ranks such risks by exploitability, prevalence,
detectability, and impact. It also covers people using service accounts manually, which
obscures attribution. Prefer short-lived, runtime-issued credentials based on attestation where
the platform supports them.

NHI risks include secret leakage, identities left active after the services that used them
are retired, long-lived secrets, and over-privilege. The OWASP Non-Human Identities Top 10
(an OWASP Incubator project) catalogs what goes wrong.

## Resources

- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
