# Verifiable credentials

**TL;DR:** A verifiable credential is a set of claims about a subject that an issuer signs and
hands to a holder, who stores it and presents it to a verifier. In OpenID Connect or SAML the
identity provider takes part in every login; the W3C data model splits that role into issuer
and holder, so the issuer need not know the verifier. A verifier checks the issuer's signature
and decides whether it trusts that issuer, so a valid credential proves who said something, not
that it is true. The holder packages credentials into a verifiable presentation, which should
be short-lived and bound to a verifier challenge, since the verifier cannot otherwise assume
the presenter is the credential's subject. The data model describes subjects; it is not an
authorization framework.

The W3C data model for credentials an issuer signs, a holder keeps, and a verifier checks
without the issuer needing to know the verifier (VC DM 2.0 §5.1): a different trust topology
from IdP-brokered federation, not a third federation protocol. IETF SPICE works the same
problem in IETF formats. Portable identity documents for people and, increasingly, for
agents.

## Resources

- [@official@W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [@official@IETF SPICE WG](https://datatracker.ietf.org/wg/spice/about/)

---

[← 05 · Identity protocols](README.md) · [Map](../../README.md)
