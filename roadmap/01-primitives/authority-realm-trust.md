# Authority, realm & trust

**TL;DR:** An authority is a party trusted for a specific statement, such as a certificate
authority signing a certificate or a Kerberos KDC issuing a ticket. A Kerberos realm is the
administrative boundary established by an organization, and its name is part of a client's
name. An X.509 relying party selects trust-anchor information by policy and uses it to validate
a certification path. In X.509 that path connects the target certificate through any
intermediate CA certificates toward the trust anchor, with certificates checked for signature,
validity, and revocation. A backend developer configures the trust-anchor store used by the
certificate validator.

What an authority is, what a realm is, and how trust chains anchor in something you already
trust. Certificate paths illustrate the trust anchor: RFC 5280 §6 has path validation begin
from a trust anchor the relying party selects by policy; Kerberos (RFC 4120) defines realms
and their KDCs.

## Resources

- [@official@RFC 5280 — X.509 PKI Certificate and CRL Profile](https://datatracker.ietf.org/doc/html/rfc5280)
- [@official@RFC 4120 — Kerberos V5](https://datatracker.ietf.org/doc/html/rfc4120) (realms, the KDC as authority)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
