# UserInfo & standard claims

**TL;DR:** OpenID Connect defines shared claim names such as `name`, `email` and
`email_verified`. The UserInfo endpoint is an OAuth-protected resource at the OpenID Provider;
the client presents an access token and receives a JSON object containing available claims. The
`profile`, `email`, `address` and `phone` scopes request defined claim sets, but those claims
are voluntary and can be absent. A `public` subject identifier gives clients the same `sub`. A
`pairwise` identifier differs across sector identifiers, limiting correlation between unrelated
client sectors while allowing related clients in one sector to share an identifier.

Core §5.1 fixes a vocabulary of Standard Claims about the End-User (`name`, `email`,
`email_verified`, `picture`, `locale`, …) and §5.3 defines the UserInfo Endpoint, an
OAuth-protected resource that returns them for the access token presented. §5.4 groups them
behind the scopes `profile`, `email`, `address` and `phone`; §8 defines two Subject
Identifier Types, `public` (the same `sub` for every client) and `pairwise` (a different
`sub` per client, so two Relying Parties cannot correlate the user). An agent that only
needs to know who it works for can request `openid` alone, since `iss` + `sub` identify the
End-User (§3.1.2.1, §5.7); every extra scope requests additional End-User claims (§5.4).

## Resources

- [@official@OpenID Connect Core 1.0 §5.1 — Standard Claims](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)
- [@official@OpenID Connect Core 1.0 §5.3 — UserInfo Endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo)
- [@official@OpenID Connect Core 1.0 §8 — Subject Identifier Types](https://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
