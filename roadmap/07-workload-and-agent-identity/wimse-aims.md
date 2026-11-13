# AIMS: agents as WIMSE workloads

**TL;DR:** AIMS (AI Identity Management System) is the WIMSE working group's document on AI
agents. Its premise is in a section title: agents are workloads. It defines an agent as a
workload that repeatedly interacts with a large language model and a set of tools, services
and resources until a stopping condition is reached. AIMS does not invent new protocols. It
shows how WIMSE, OAuth 2.0, SPIFFE and Shared Signals already cover agent authentication and
authorization, and names the gaps. Its rules are concrete. Each agent gets exactly one WIMSE
identifier, which may be a SPIFFE ID. Static API keys are called an antipattern. The model
must never have access to the agent's credentials, so a prompt cannot talk the agent into
pasting its key into a reply.

draft-ietf-wimse-aims replaced the individual draft-klrc-aiagent-auth and was adopted by
WIMSE. Revision -01 is dated November 2026 and the intended status is Informational. It
describes AIMS as "a conceptual model" of the functions agent identity needs (Section 5). It
then walks the layers: identifier (Section 6), credentials (Section 7), provisioning (Section
8), authentication with the WIMSE proofs (Section 9), and authorization (Section 10). The
authorization section covers OAuth delegation, token exchange and transaction tokens (→
[Token exchange: RFC 8693](../08-delegation-and-impersonation/token-exchange-rfc-8693.md)).
After that come monitoring and remediation, policy, and compliance. One caution: the WIMSE
charter itself never mentions agents. AIMS and the agent-titled individual drafts are how
agents entered the group's work.

## Resources

- [@official@IETF draft — AI Identity Management System (draft-ietf-wimse-aims-01)](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-aims-01)
- [@official@IETF draft — AIMS, Section 4: Agents are workloads](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-aims-01#section-4)

---

[← WIMSE](wimse.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
