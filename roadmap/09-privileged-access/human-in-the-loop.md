# Human-in-the-loop

**TL;DR:** Human-in-the-loop routes a high-impact action through a person's decision before
execution. An approval that is routinely accepted without review provides little control. CIBA
supplies one narrower protocol pattern: a client posts an authentication request identifying
the user to an OpenID Provider, which returns an opaque request identifier while the user
authenticates and authorizes the request on another device. In poll mode the client polls for
tokens; in ping mode it receives a notification and fetches them; in push mode the provider
sends them directly. A binding message displayed on both devices helps the user connect the
approval to the initiating transaction. CIBA does not decide where an application should place
that approval.

Where approval belongs in the decision path, how to architect it so it is not a rubber
stamp, and when an agent must stop and ask. CIBA can request a human's authentication on
another device (→ [Decoupled authentication: CIBA](../05-identity-protocols/decoupled-authentication-ciba.md));
see agentic threats (→ [11](../11-threat-modeling/agentic-threats.md)).

## Resources

- [@official@OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)

---

[← 09 · Privileged access](README.md) · [Map](../../README.md)
