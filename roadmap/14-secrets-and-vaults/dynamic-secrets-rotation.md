# Dynamic secrets & rotation

**TL;DR:** A dynamic secret is a credential a vault creates on demand for one caller, with a
lease that expires it after a set time. An example is a database username and password
generated when a payroll service asks. A static secret is a fixed, pre-provisioned value, such
as an API key, that can remain valid until it expires, is revoked, or is rotated. A leaked
dynamic credential can still work during its lease, but expiry and lease-based revocation limit
its useful lifetime. Static secrets need scheduled, automated rotation. Centralized secret
management addresses secrets sprawl: keys hard-coded in source and scattered across config
files. Detect sprawl with secret scanners in pre-commit hooks, and audit every fetch: who
requested which secret for which system.

Short-lived credentials issued on demand vs. static secrets rotated on a schedule. Secrets
sprawl and how to detect it.

## Resources

- [@official@HashiCorp Vault documentation](https://developer.hashicorp.com/vault/docs)
- [@article@OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

---

[← 14 · Secrets & vaults](README.md) · [Map](../../README.md)
