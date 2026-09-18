# Issuance & presentation: OpenID4VCI & OpenID4VP

**TL;DR:** OpenID4VCI issues a verifiable credential into a wallet and OpenID4VP gets a
presentation back out; both are OpenID protocols built on OAuth 2.0 messages and roles. In
OpenID4VCI the credential issuer is an OAuth resource server. The wallet gets an access token
through the authorization code grant, or through a pre-authorized code the issuer handed out
after identifying the person another way. It then calls the credential endpoint, adding proof
of its key when the credential is bound to one. In OpenID4VP the verifier sends an OAuth
authorization request with `response_type=vp_token` and a DCQL query naming the credentials and
claims it wants. On one device the response returns by redirect; across devices the request is
a QR code and the wallet POSTs the presentation with `response_mode=direct_post`.

OpenID for Verifiable Credential Issuance treats the Credential Issuer as an OAuth 2.0
resource server "protected by an Access Token issued by an Authorization Server" (OpenID4VCI
§3.2): the wallet obtains that token through the authorization code grant or the
Pre-Authorized Code grant (`urn:ietf:params:oauth:grant-type:pre-authorized_code`), which
skips the authorization endpoint because the issuer already dealt with the person (§3.5),
then calls the Credential Endpoint (§8), including `proofs` of the key when the issuer
requires key binding, having found the issuer at `/.well-known/openid-credential-issuer`
(§12.2.2) and possibly having been started by an issuer-pushed Credential Offer (§4.1).
OpenID for Verifiable Presentations is an OAuth authorization request (OpenID4VP §5) with
`response_type=vp_token` (§5.6) and a `dcql_query` in the Digital Credentials Query Language
(§6) saying which credentials and claims the Verifier wants; on one device the response
rides a redirect, across devices the request is a QR code and the wallet POSTs the
presentation back with `response_mode=direct_post` (§3.2, §8.2), and Appendix A carries the
same messages over the W3C Digital Credentials API. Both reuse OAuth roles, request
structures and metadata, so an engineer who knows [OAuth 2.x](oauth-2x.md) has the
vocabulary, though each adds credential-specific roles and validation. Wallets and agents
both hold credentials on a person's behalf; a presentation packages credential claims and,
when the credential is holder-bound and the Verifier supplies a challenge, shows the
presenter's control of the key (VC DM 2.0 §4.13), while the data model itself says
authorization needs "an accompanying authorization framework" (§5.9). The EUDI Wallet ARF v3.0.0 uses OpenID4VCI profiled by HAIP for issuance and requires support for OpenID4VP profiled by HAIP among its remote-presentation options.

## Resources
- [@official@EUDI Wallet Architecture and Reference Framework (ARF) v3.0.0 — attestation formats and OpenID4VC protocols](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/)

- [@official@OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
- [@official@OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
- [@official@W3C Verifiable Credentials Data Model 2.0 §4.13, §5.9](https://www.w3.org/TR/vc-data-model-2.0/)

---

[← Verifiable credentials](verifiable-credentials.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
