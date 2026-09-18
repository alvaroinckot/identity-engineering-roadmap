# Secret zero: vaults vs. workload identity

**TL;DR:** Secret zero is the first credential a workload needs before it can fetch any other,
such as the token a CI runner needs to log in to the vault. A vault may use a long-lived
bootstrap secret, but platform-aware auth methods can avoid one. Workload identity federation
replaces a stored cloud credential with a platform-issued identity token. In GitHub Actions the
platform signs a per-job OIDC token whose claims identify the repository and execution context.
The cloud checks those claims against a trust condition and returns a short-lived access token
for that job. SPIFFE's local Workload API identifies the calling process out of band, without a
bootstrap token from the workload, and issues a short-lived signed SVID.

The first credential a workload needs in order to fetch its other credentials.
Platform-attested identity (OIDC federation, SPIFFE) removes it; a vault only moves it.

## Resources

- [@official@GitHub Actions OIDC / cloud workload identity federation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [@official@SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/)

---

[← 14 · Secrets & vaults](README.md) · [Map](../../README.md)
