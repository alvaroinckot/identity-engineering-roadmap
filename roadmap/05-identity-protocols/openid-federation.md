# OpenID Federation 1.0

**TL;DR:** OpenID Federation 1.0 lets a relying party and OpenID provider establish trust
through a common trust anchor instead of bilateral registration. Each entity has a signed JWT
about itself called an Entity Configuration. Trust anchors and intermediates must publish it at
`/.well-known/openid-federation`; leaf entities should publish it there. Superiors issue
Subordinate Statements, and the chain ending at the trust anchor proves federation membership.
Metadata policies applied higher in the chain cannot be loosened below. Registration can be
automatic, using the relying party's entity identifier as its `client_id`, or explicit, with
the provider assigning a `client_id`.

OpenID Federation 1.0 lets a Relying Party and an OpenID Provider that have never met establish trust through a third party: every Entity publishes a signed JWT about itself, its Entity Configuration, at `/.well-known/openid-federation` (§9), each Superior publishes Subordinate Statements about the Entities under it (§1.2, §3), and the sequence from a Leaf's Entity Configuration up to a Trust Anchor's forms a Trust Chain that proves the Leaf is a member of that federation (§2, §4). Trust Anchors and Intermediates attach metadata policies on the way down that a lower Intermediate cannot loosen (§6.1, §6.1.1), which is how a federation operator constrains every OP and RP under it from one place. Registration then takes one of two forms: Automatic Registration needs no explicit registration step, the RP's Entity Identifier is its `client_id` and it authenticates with asymmetric cryptography (§12.1); Explicit Registration is bilateral, the RP submits its Entity Configuration or whole Trust Chain to the OP's `federation_registration_endpoint` and the OP assigns a `client_id`, and possibly a secret (§12.2, §12.4). The specification covers trust and metadata only; the OpenID Connect protocol steps themselves are unchanged (§2).

## Resources

- [@official@OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html)
- [@official@OpenID Federation 1.0 §9 — Obtaining Federation Entity Configuration Information](https://openid.net/specs/openid-federation-1_0.html#name-obtaining-federation-entity)
- [@official@OpenID Federation 1.0 §12 — OpenID Connect Client Registration](https://openid.net/specs/openid-federation-1_0.html#name-openid-connect-client-regis)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
