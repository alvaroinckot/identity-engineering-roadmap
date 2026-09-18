# Agent identity

**TL;DR:** Agent identity asks what an AI agent is as a party in authentication: a user, a
workload, or neither. No agreed definition exists; the AAuth draft proposes a narrow one, an
agent is an HTTP client acting on behalf of a person, and other proposals are not standards.
The practical problem is attribution: when several agents share one service account or OAuth
client, the audit log records the account, not which agent acted, and one leaked credential
exposes all of them. By analogy to Google's single-purpose service-account guidance, a
dedicated credential per agent can improve attribution and reduce shared-credential exposure.
The OpenID AI Identity Management Community Group collects use cases; it is a discussion venue,
not a specification body.

What an AI agent is as an identity party: no consensus definition exists yet; AAuth §3
proposes one scoped definition, an Agent as an HTTP client acting on behalf of a person.
Dedicated credentials per agent can improve attribution and reduce shared-account blast
radius, by analogy to single-purpose service-account guidance. The OpenID AIIM Community
Group is collecting agent-identity use cases; separate proposals such as OIDC-A explore
possible claims but are not standards.

## Resources

- [@official@Internet-Draft — AAuth Protocol](https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/) (draft-hardt-oauth-aauth-protocol)
- [@official@Google Cloud — Best practices for using service accounts](https://cloud.google.com/iam/docs/best-practices-service-accounts)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)
- [@article@OIDC-A — OpenID Connect for Agents](https://github.com/subramanya1997/oidc-a) (proposal)
- [@official@OpenID Foundation — AI Identity Management Community Group](https://openid.net/cg/artificial-intelligence-identity-management-community-group/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
