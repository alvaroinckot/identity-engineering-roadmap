# Agentic threats

**TL;DR:** Agentic threats are the ways an agent's own permissions become the attack. The
central case is the confused deputy: an agent with more privilege than its user cannot tell a
real request from instructions injected into the data it reads. A prompt hidden in an email can
then make it misuse a tool. The OWASP agentic catalog names tool misuse and agent hijacking,
privilege compromise, identity spoofing and impersonation, and repudiation, where thin logging
hides who acted. The OWASP NHI Top 10 covers the credential side: machine credentials that are
over-privileged, long-lived, leaked into code, never offboarded, or shared with humans, so logs
cannot tell people from automation. Mitigations start with least privilege when acting for a
user and a check that the requester may perform the action.

Identity spoofing, privilege compromise, tool misuse, auditability gaps, and their
mitigations per the OWASP agentic catalog. The OWASP NHI Top 10 adds credential-management
and lifecycle risks for non-human identities.

## Resources

- [@official@OWASP GenAI Security Project — Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

[← 11 · Threat modeling](README.md) · [Map](../../README.md)
