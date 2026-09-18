# Keys, certificates & PKI

**TL;DR:** A public key certificate is a signed data structure that binds a public key to a
subject, such as a server hostname, with the binding asserted by a certificate authority's
signature. Other configured mechanisms can also establish trust in a public key. A relying
party is configured with a small set of trust anchors, chosen by policy, and validates a
certification path. The path connects the end entity's certificate through intermediate CA
certificates toward a trust anchor; validation checks signatures, validity, revocation, names,
and applicable constraints. Revocation is published as a CRL, a CA-signed list of revoked
serial numbers; on-line checking is a separate specification. A backend developer meets this as
the CA bundle a TLS client trusts and the certificate a service presents.

X.509 certificates, certification paths, CRLs, and the trust anchor a relying party starts
path validation from (RFC 5280 §6, whose selection "is a matter of policy"); on-line
revocation checking (OCSP) is defined in a separate PKIX specification.

## Resources

- [@official@RFC 5280 — X.509 PKI Certificate and CRL Profile](https://datatracker.ietf.org/doc/html/rfc5280)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
