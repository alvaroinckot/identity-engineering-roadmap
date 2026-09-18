# Token lifecycle: introspection & revocation

**TL;DR:** Introspection lets a protected resource ask the authorization server whether a token
is active and what metadata applies. Revocation lets a client request invalidation of a token
it received. These endpoints are not the only ways a deployment can stop token acceptance. For
introspection, the resource server POSTs the token and must be authorized to use the endpoint;
the response always contains `active` and can include `scope`, `sub`, `aud` and `exp`.
Revocation is immediate at the authorization server, although distributed systems can have
propagation delay. Cached introspection creates a stale window, while offline JWT validation
does not observe revocation without another mechanism.

Asking the authorization server whether a token is still good, and telling it to stop
being good.

## Resources

- [@official@RFC 7662 — Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662)
- [@official@RFC 7009 — Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
