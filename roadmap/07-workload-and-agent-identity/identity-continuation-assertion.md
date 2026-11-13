# Multi-hop XAA: Identity Continuation Assertion

**TL;DR:** The Identity Continuation Assertion is a proposed extension to ID-JAG for when
Cross App Access has to go more than one hop. Say an agent app calls an MCP tool gateway for
Alice through XAA, and the gateway now needs a wiki API for her. The gateway holds only the
access token it received. The wiki's authorization server will not accept that token, and the
gateway has no ID token for Alice to start a fresh XAA exchange. Under this draft, the
gateway trades its access token for a short-lived signed assertion. The assertion says that
an earlier ID-JAG was accepted and that its authorization is still active. The gateway takes
that assertion back to the company's identity provider. The identity provider checks current
policy and issues a new ID-JAG for the wiki. This works even after Alice has gone offline.

draft-mcguinness-oauth-id-continuation-assertion (Karl McGuinness and Aaron Parecki,
revision -02, 9 September 2026) is an individual Internet-Draft aimed at the OAuth working
group. It has not been adopted. It extends ID-JAG and complements OAuth identity chaining (→
[Call chains: transaction tokens & identity
chaining](../08-delegation-and-impersonation/call-chains-transaction-tokens-identity-chaining.md)).
Each ID-JAG in a chain is a hop. The identity provider tracks hops with an opaque
`identity_continuation_handle` claim and evaluates every continuation as a fresh policy
check (Section 1.1). The assertion is a JWT with `typ` `oauth-identity-continuation+jwt`
and token type `urn:ietf:params:oauth:token-type:identity-continuation`. It requires `act`
(the current actor) and `cnf` (a key proved with DPoP), and it should live no longer than
300 seconds (Sections 3.1 and 3.2). It is used as the subject token of an RFC 8693 exchange,
and it carries no downstream authority of its own: the request names the target. A chain is
anchored either to the user's IdP session, ending at logout, or optionally to a refresh
token's grant, which lets an unattended agent keep working after logout (Section 6.1).
Revoking a hop stops its descendants at their next continuation. Already-issued ID-JAGs and
access tokens stay valid until they expire (Section 6). The draft names an MCP tool gateway,
which cannot know its call path in advance, as the motivating deployment.

## Resources

- [@official@IETF draft — Identity Continuation Assertion for OAuth 2.0 Token Exchange (draft-mcguinness-oauth-id-continuation-assertion-02)](https://datatracker.ietf.org/doc/html/draft-mcguinness-oauth-id-continuation-assertion-02)
- [@official@IETF draft — Identity Continuation Assertion, Section 1.1: Protocol overview](https://datatracker.ietf.org/doc/html/draft-mcguinness-oauth-id-continuation-assertion-02#section-1.1)
- [@official@IETF datatracker — Identity Continuation Assertion status and revisions](https://datatracker.ietf.org/doc/draft-mcguinness-oauth-id-continuation-assertion/)

---

[← Cross-app access: XAA](cross-app-access-xaa.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
