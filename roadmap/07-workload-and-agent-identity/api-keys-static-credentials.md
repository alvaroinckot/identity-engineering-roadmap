# API keys & static credentials

**TL;DR:** An API key is a fixed string a caller attaches to every request, and whoever holds
the string is treated the same as its owner. It identifies a calling application or project,
not a person: a standard Google Cloud key ties a request to a project but does not authenticate
a principal, and OWASP says API keys authenticate API clients, never users. The key is a bearer
credential, so possession alone suffices. The recurring failures are keys leaked from source
code and config files, keys that never expire, and keys left behind after a service is retired.
Restrict each key to specific APIs and callers, rotate it, and where possible give the workload
a runtime-issued identity instead.

A standard Google Cloud API key associates a request with a project but does not
authenticate a principal: Google's own docs say a standard key "doesn't authenticate a
principal", so the request "can't use Identity and Access Management (IAM) to check whether
the caller is authorized", and OWASP's API2:2023 entry states that API keys "should only be
used for API clients authentication", never for users. When a credential has bearer
semantics, possession alone suffices: in RFC 6750 §1.2 terms, "any party in possession of
the token (a "bearer") can use the token in any way that any other party in possession of it
can". Static bearer credentials are operationally simple, but leakage, incomplete
offboarding, and distant or absent expiration extend the period in which possession enables
access; the OWASP NHI Top 10 catalogs each — keys "hard-coded into source code, stored in
plain text configuration files" (NHI2:2025), "expiration dates that are too far in the
future or that don't expire at all" (NHI7:2025), and identities that outlive the service
that used them (NHI1:2025 Improper Offboarding). The roadmap's answer is to give the
workload an identity instead — [Machine identity & SPIFFE](machine-identity-spiffe.md),
[Workload identity federation](workload-identity-federation.md) — and to route whatever
static secrets remain through [14 · Secrets & vaults](../14-secrets-and-vaults/README.md).

## Resources

- [@official@Google Cloud — Manage API keys](https://cloud.google.com/docs/authentication/api-keys)
- [@official@OWASP API Security Top 10 2023 — API2:2023 Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
- [@official@RFC 6750 — OAuth 2.0 Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
