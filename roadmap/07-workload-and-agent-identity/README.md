# 07 · Workload & agent identity

The AI-era core: identity for software, and what changes when the software is an agent.

## Topics

1. [Machine identity & SPIFFE](machine-identity-spiffe.md)
2. [Workload identity federation](workload-identity-federation.md)
   1. [Kubernetes service accounts & projected tokens](kubernetes-service-accounts.md)
   2. [Keyless signing: Sigstore](sigstore.md)
3. [Non-human identities](non-human-identities.md)
4. [API keys & static credentials](api-keys-static-credentials.md)
5. [Attestation: RATS](attestation-rats.md)
6. [Agent identity](agent-identity.md)
7. [Agent protocols](agent-protocols-mcp-auth-aauth-a2a.md)
   1. [MCP authorization](mcp-authorization.md)
   2. [AAuth](aauth.md)
   3. [A2A](a2a.md)
8. [Bots on the web: Web Bot Auth & Privacy Pass](bots-on-the-web.md)
9. [Least privilege & audit for agents](least-privilege-audit-for-agents.md)
10. [Cross-app access: XAA](cross-app-access-xaa.md)
11. [WIMSE](wimse.md)

## What AI agents change

This whole area is the answer. Short version: an agent needs its own identity (not the
user's), an attested reason to be trusted, a delegation that names the user, and a
revocation path that works mid-task.

---

[← Map](../../README.md)
