# Choosing an IdP: build, buy, certify

**TL;DR:** Certification provides evidence that an identified implementation or deployment
conforms to a named profile. OpenID Foundation offers self-certification using its conformance
tests and is developing independent certification through authorized auditors and testing
providers; successful self-certifications and their test data are public. Available OpenID
profiles cover OpenID Connect providers and relying parties and FAPI-related implementations,
while some newer specifications have test suites without an established certification catalog.
FIDO separately certifies functional conformance for authenticators, clients, and servers, with
security levels for authenticators. IPSIE remains draft work. The reviewed OpenID and FIDO
catalogs do not identify an agent-authorization certification profile.

Build or buy, an IdP can use certification to provide evidence that a named deployment
conforms to a named interoperability profile: OpenID Certification is self-certification,
with free conformance tests, a legally binding Certification of Conformance, and public
results, and its generally available profiles are the OpenID Connect OP and RP variants plus
FAPI and FAPI-CIBA (OpenID Federation and Shared Signals have only early-stage or limited
test suites, outside the certified catalog). FIDO Certified is a different model: functional
certification of authenticators, clients, and servers, with Authenticator Certification
Levels (L1 to L3+) that apply to authenticators only. IPSIE profiles OIDC, SCIM, Shared
Signals, and logout for enterprise interoperability while prioritizing secure defaults. The
OAuth WG charter lists authorization for automated agents across administrative domains as
work, but the OpenID and FIDO program pages reviewed here do not identify an
agent-authorization certification profile, so certification alone does not substantiate an
"agent-ready" claim.

## Resources

- [@official@OpenID Certification program](https://openid.net/certification/)
- [@official@FIDO Alliance Certification](https://fidoalliance.org/fido-user-authentication-certification-programs/)
- [@official@OpenID IPSIE WG](https://openid.net/wg/ipsie/)
- [@official@IETF OAuth Working Group](https://datatracker.ietf.org/wg/oauth/documents/)

---

[← 13 · The practice: living off RFCs](README.md) · [Map](../../README.md)
