# Selective disclosure: SD-JWT

**TL;DR:** SD-JWT, defined by RFC 9901, lets a holder reveal selected claims while preserving
the issuer's signature. The issuer removes each disclosable value and stores a digest of a
Disclosure containing a salt, claim name and value. Object-property digests appear in `_sd`,
while arrays use digest placeholders. The holder sends the signed JWT with only the Disclosures
needed by the verifier. Without Key Binding, anyone who copies the credential can replay it. A
Key Binding JWT proves control of a holder key and covers the presentation, verifier nonce and
audience. SD-JWT VC remains an Internet-Draft that adds credential-specific claims such as
`vct`.

RFC 9901 makes a JWT partially revealable: the Issuer replaces each selectively disclosable object property with a salted digest listed in an `_sd` array (array elements use digest placeholders; hash algorithm in `_sd_alg`, default sha-256) and hands the Holder the cleartext Disclosures separately, so the Holder presents the signed JWT with only the Disclosures a given Verifier needs, `<Issuer-signed JWT>~<Disclosure>~…~` (§4), and the Issuer's signature still verifies. Without Key Binding "the credential itself can be replayed by anyone who gets access to it" (§9.5); with it the Holder appends a KB-JWT (`typ` `kb+jwt`) signed by the key the Issuer bound into the credential, over a hash of exactly what was presented plus the Verifier's `nonce` and `aud` (§4.3), and how those two values travel "is up to the protocol used", because SD-JWT is a format, not a protocol. SD-JWT VC, still an IETF OAuth WG Internet-Draft, profiles it into a credential: `typ` `dc+sd-jwt`, a `vct` claim naming the credential type, and Issuer-key discovery through `/.well-known/jwt-vc-issuer` or an `x5c` chain. An agent presenting a user's credential should disclose only what the Verifier's query asks for, and a Verifier facing agents should require Key Binding so a credential lifted from the agent's store cannot be replayed elsewhere.

## Resources

- [@official@RFC 9901 — Selective Disclosure for JSON Web Tokens (SD-JWT)](https://datatracker.ietf.org/doc/html/rfc9901)
- [@official@SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) (draft-ietf-oauth-sd-jwt-vc, Internet-Draft)

---

[← Verifiable credentials](verifiable-credentials.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
