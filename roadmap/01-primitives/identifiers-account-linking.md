# Identifiers & account linking

**TL;DR:** An identifier is the value a system uses to refer to one identity. In OpenID Connect
only the issuer and subject pair, the iss and sub claims, may be relied on as a stable
identifier for a user; an email address may not, because an issuer may reuse it for a different
person. In SCIM the service provider assigns a stable id and the provisioning client stores its
own externalId. In Auth0, account linking merges a secondary user profile into a primary
profile. The usual mistake is linking two accounts because they share an email address without
authenticating both, which is how attackers reach legitimate accounts. Store the issuer and
subject pair, not the email, as your reference to a federated user.

Identifiers have different stability properties: OpenID Connect Core §5.7 makes `iss` plus `sub` "the only Claims that an RP can rely upon as a stable identifier for the End-User" and warns that an issuer "MAY re-use an email Claim Value across different End-Users", while SCIM (RFC 7643 §3.1) gives a directory resource a provider-assigned, stable `id` and a client-assigned `externalId`. Account linking joins several such identities from several providers into one account (in Auth0's model two profiles merge under a primary whose `user_id` survives). Linking suggested from a shared email is risky unless both accounts are authenticated: Auth0 warns that insecure linking can let malicious actors access legitimate accounts, and SP 800-63C-4 §3.8.1 makes an authenticated session a SHALL for "all linking functions". Once linked, Auth0 treats sign-in through any linked identity as access to the same user profile; linking therefore expands the identities through which that account can be reached.

## Resources

- [@official@OpenID Connect Core 1.0 §5.7 — Claim Stability and Uniqueness](https://openid.net/specs/openid-connect-core-1_0.html#ClaimStability)
- [@official@RFC 7643 — SCIM: Core Schema §3.1 Common Attributes (`id`, `externalId`)](https://datatracker.ietf.org/doc/html/rfc7643#section-3.1)
- [@official@Auth0 Docs — User Account Linking](https://auth0.com/docs/manage-users/user-accounts/user-account-linking)
- [@official@NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/sp800-63.html) (SP 800-63C-4 §3.8.1, Account Linking)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
