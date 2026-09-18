# Capabilities & attenuation: macaroons, Biscuit, UCAN

**TL;DR:** A capability is an unforgeable value that designates a resource and authorizes an
operation on it. When a deputy receives the target as a capability, it can use the authority
bound to that designation instead of confusing it with separate standing authority. Attenuation
lets a holder narrow a capability before passing it on without contacting the issuer. A
macaroon chains HMACs so a holder can append caveats, while only the service holding the root
key verifies it. Biscuit uses a public-key signature chain and Datalog checks. UCAN uses signed
delegations whose audience becomes the next issuer and whose capabilities may only be restated
or narrowed.

A capability names the resource and grants the right in one unforgeable token, so the holder can act only on what the token designates and there is no ambient authority for a confused deputy to spend; Miller, Yee and Shapiro call this "no designation without authority" and show it is exactly the property an ACL system cannot have. Attenuation is the holder narrowing a capability before passing it on, with no round-trip to the issuer: an HMAC macaroon lets a holder append attenuating caveats using the current signature as the next HMAC key (the chain integrity-protects every caveat, and HMAC macaroons are verifiable only by the target service holding the root key), Biscuit keeps the append-only blocks but signs each with a public key carried in the previous block so any verifier holding the root public key checks the chain and the checks are Datalog, and UCAN makes the chain explicit as signed delegations whose audience must issue the next link and each link MUST restate or attenuate its proof. Contrast [RFC 8693 token exchange](token-exchange-rfc-8693.md): there the client asks and the authorization server decides what token and scope to issue, so this is not holder-side attenuation. For agent designs these sources support narrowing delegated authority before passing it on rather than sharing the broader credential: a sub-agent gets a caveat-narrowed macaroon, a Biscuit block or a UCAN delegation scoped to its task, so that what leaks if it is compromised is the attenuated capability, not the delegator's own token.

## Resources

- [@paper@Norm Hardy — The Confused Deputy (or why capabilities might have been invented)](http://cap-lore.com/CapTheory/ConfusedDeputy.html)
- [@paper@Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud (NDSS 2014)](https://research.google/pubs/macaroons-cookies-with-contextual-caveats-for-decentralized-authorization-in-the-cloud/)
- [@paper@Capability Myths Demolished — Miller, Yee, Shapiro (2003)](http://zesty.ca/capmyths/usenix.pdf)
- [@opensource@Eclipse Biscuit — bearer token with offline attenuation and decentralized verification](https://www.biscuitsec.org/)
- [@official@UCAN — User Controlled Authorization Network Specification v1.0.0](https://github.com/ucan-wg/spec)
- [@official@RFC 8693 — OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
