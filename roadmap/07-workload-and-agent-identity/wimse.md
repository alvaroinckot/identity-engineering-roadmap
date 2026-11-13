# WIMSE

**TL;DR:** WIMSE is the IETF working group standardizing workload identity mechanisms across
systems and trust domains over HTTP. A browser request may pass through an orders service that
calls a payments service in another cloud, and each hop needs the calling workload and
original-caller context. The charter defines a workload as a running software instance
executing for a specific purpose. As of November 2026 the group has eight working-group
drafts: an architecture, an identifier format, credentials, three ways to authenticate a
request, a practices survey, and a profile for AI agents. None is an RFC yet. The HTTP
Signatures profile has gone to the IESG as a Proposed Standard, and Workload Identity
Practices is in IETF Last Call. WIMSE coordinates with CNCF, particularly the SPIFFE/SPIRE
project, but the charter does not make SPIFFE a dependency.

The IETF Workload Identity in Multi System Environments working group is chartered to
develop HTTP/REST workload-identity work: how a workload proves who it is across systems and
trust domains, identity credential formats, service-to-service protection, and how the
original caller's context is carried or exchanged along a chain of workload-to-workload
calls. The documents fit together as a stack. The [architecture](wimse-architecture-identifiers.md)
names the parts and the [identifier](wimse-architecture-identifiers.md) names the workload.
The [credentials](wimse-workload-credentials.md) bind that name to a key, and the
[authentication profiles](wimse-workload-to-workload-authentication.md) prove possession of
the key on each request. [AIMS](wimse-aims.md) applies the stack to AI agents. The first
service-to-service draft (draft-ietf-wimse-s2s-protocol) is dead: it was replaced by the
credentials, WPT, HTTP Signatures and mutual TLS drafts. Workload Identity Practices is
Informational. It surveys how platforms issue workloads credentials today, through Kubernetes
service accounts, SPIFFE, cloud metadata endpoints and CI/CD, and how those credentials are
federated to an outside identity provider (→ [Workload identity
federation](workload-identity-federation.md)). It says it does not take the WIMSE
architecture work into account. Two charter work items have no working-group draft yet:
token exchange (an incoming token of one format traded for a WIMSE token) and local token
issuance. Individual drafts are piling up too, among them the [Workload Authorization
Grant](workload-authorization-grant-wag.md) and about twenty agent-related proposals. None of
those has been adopted.

## Resources

- [@official@IETF WIMSE WG — Workload Identity in Multi System Environments (charter)](https://datatracker.ietf.org/wg/wimse/about/)
- [@official@IETF WIMSE WG — documents and their status](https://datatracker.ietf.org/wg/wimse/documents/)
- [@official@IETF draft — Workload Identity Practices (draft-ietf-wimse-workload-identity-practices-08), Section 1](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-identity-practices-08#section-1)
- [@official@IETF draft — WIMSE Service-to-Service Authentication (draft-ietf-wimse-s2s-protocol, replaced)](https://datatracker.ietf.org/doc/draft-ietf-wimse-s2s-protocol/)
- [@article@Spherical Cow Consulting — WIMSE is Where Workload Identity is Getting Interesting](https://sphericalcowconsulting.com/2026/10/27/wimse-is-where-workload-identity-is-getting-interesting/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
