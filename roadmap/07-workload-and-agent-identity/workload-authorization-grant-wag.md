# Workload Authorization Grant: WAG

**TL;DR:** The Workload Authorization Grant (WAG) is a proposal for letting an agent call a
third party's API as itself, with no user involved and no per-agent setup at the third
party. Today an agent platform that spins up many agents must register each one at every
authorization server they use. That is impractical, so in practice all the agents share one
credential. Under WAG, the third party's administrator trusts the platform's Workload
Identity Provider once. After that, the platform signs a short-lived JWT naming one agent by
an opaque identifier that is never reassigned. The agent posts it to the token endpoint as a
standard JWT bearer grant. The authorization server does not reject an agent it has never
seen before, and its own policy decides what that agent may do.

draft-carleton-workload-authz-grant is an individual Internet-Draft, revision -02 of 2
November 2026, with editors from Anthropic, OpenAI, Okta, Defakto Security and Ping Identity.
It calls itself "an early, exploratory individual draft, published to solicit discussion",
not a working-group document. WIMSE held an interim meeting on it on 7 October 2026. The
grant is a JWT with `typ` `oauth-wag+jwt` and claims `iss` (the Workload Identity Provider),
`sub` (the agent identifier), `aud` (the authorization server), `exp`, `iat` and `jti`,
plus an optional `scope` and a display-only `nickname` (Section 5.1). The agent presents it
with `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` (RFC 7523), and the
authorization server must not require a client registration per agent and must not issue
refresh tokens (Section 5). The authorization server takes the provider's keys from a JWK
Set or from the provider's published metadata (Section 6.1). It reuses machinery from
[ID-JAG](cross-app-access-xaa.md): the `aud` format, `tenant`, and the
`authorization_grant_profiles_supported` metadata. The scope is deliberately narrow:
workloads acting on their own behalf. Acting for a user is out of scope, although the grant
is meant to compose with delegation in which the agent is the actor. Agent ownership, proof
of possession and replay are listed as open issues (Section 9).

## Resources

- [@official@IETF draft — Workload Authorization Grant (draft-carleton-workload-authz-grant-02)](https://datatracker.ietf.org/doc/html/draft-carleton-workload-authz-grant-02)
- [@official@IETF datatracker — WAG status and revisions](https://datatracker.ietf.org/doc/draft-carleton-workload-authz-grant/)
- [@official@RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)
- [@article@Spherical Cow Consulting — WIMSE is Where Workload Identity is Getting Interesting](https://sphericalcowconsulting.com/2026/10/27/wimse-is-where-workload-identity-is-getting-interesting/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
