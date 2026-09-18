# SAML in the enterprise today

**TL;DR:** SAML still carries workforce single sign-on into cloud applications. Microsoft Entra
ID documents an `AuthnRequest` sent by HTTP Redirect and a signed `Response` returned by HTTP
POST. Its assertion carries a persistent, opaque `NameID` targeted at the Service Provider and
a fixed validity window without a clock-skew buffer. Entra documents OpenID Connect as an
alternative. Compromise of an Identity Provider's signing capability can let an attacker mint
assertions that Service Providers accept as genuine. CISA calls this Golden SAML and recommends
monitoring certificate-export events, while also noting that an attacker can add a trusted AD
FS instance instead of exporting the existing certificate.

Microsoft Entra ID documents SAML 2.0 Web Browser SSO for cloud-service providers (HTTP
Redirect `AuthnRequest` in, HTTP POST `Response` out) and lists OpenID Connect as an
alternative way to do single sign-on. The attack surface SAML carries, forged assertions
("golden SAML"), is the subject of CISA advisory AA21-008A (→
[11](../11-threat-modeling/README.md)).

## Resources

- [@official@Microsoft Entra ID — Single sign-on SAML protocol](https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-on-saml-protocol)
- [@official@CISA AA21-008A — Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-008a)

---

[← SAML 2.0](saml-2-0.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
