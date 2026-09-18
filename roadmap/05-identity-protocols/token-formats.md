# Token formats: opaque, JWT, phantom tokens & macaroons

**TL;DR:** The authorization server chooses an access token's format; opaque handles and JWTs
are common options. A resource server can resolve an opaque handle through introspection, where
every uncached check adds a round trip and reflects revocation after state has propagated. A
JWT access token carries signed claims such as issuer, audience, subject and expiration,
allowing local validation but potentially delaying notice of revocation. The phantom token
pattern gives the client an opaque token while a gateway introspects it and forwards an
internal JWT. A macaroon is a bearer credential built from chained HMACs; a holder can append
caveats that narrow its use, and the target service verifies it.

RFC 6749 §1.4 leaves the access token's format to the authorization server, so two families
exist: a by-reference token is opaque to the client, and the resource server resolves it by
asking the introspection endpoint (RFC 7662 §2), which returns `active` plus `scope`, `sub`,
`aud`, `exp` and friends, each uncached check a round trip by an authorized caller (§2.1)
after which a revoked token reads `active: false`; a JWT access token (RFC 9068) is
self-contained, header `typ: at+jwt` and required `iss`, `exp`, `aud`, `sub`, `client_id`,
`iat`, `jti`, validated locally against the server's keys (§4), so it costs no round trip,
and offline-only validation may not notice a revocation before `exp`. The phantom token
pattern combines them: the client only ever holds an opaque token, and an API gateway
introspects it and swaps in the JWT before the request reaches the service, keeping claims
and PII off the public side while services still validate locally. Agents make the choice a
cost decision: frequent uncached introspection along a long tool chain multiplies calls to
the authorization server, while purely offline JWT validation may accept a revoked agent's
tokens until they expire. A third shape comes from outside OAuth: a macaroon (Google, NDSS
2014) is a bearer token whose signature is a chain of HMACs in which each output is the key
for the next, so whoever holds it can append a caveat that "attenuate[s] and contextually
confine[s] when, where, by who, and for what purpose" it works, deriving a narrower token
without going back to the issuer, at the price that an HMAC macaroon is "verifiable only by
the target service" (→ [Capabilities &
attenuation](../08-delegation-and-impersonation/capabilities-attenuation.md)).

## Resources

- [@official@RFC 7662 — Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662#section-2)
- [@official@RFC 9068 — JWT Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
- [@article@The Phantom Token Approach (Curity)](https://curity.io/resources/learn/phantom-token-pattern/)
- [@paper@Macaroons: Cookies with Contextual Caveats for Decentralized Authorization in the Cloud (NDSS 2014)](https://research.google/pubs/macaroons-cookies-with-contextual-caveats-for-decentralized-authorization-in-the-cloud/)

---

[← Token lifecycle: introspection & revocation](token-lifecycle-introspection-revocation.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
