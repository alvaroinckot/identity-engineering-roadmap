# The confused deputy

**TL;DR:** A confused deputy is a program that acts for callers while holding permissions of
its own and gets tricked into spending them on a caller's request. Hardy's example is a
compiler licensed to write its statistics file: a caller named the billing file as the
debug-output path, and the compiler overwrote it. The failure needs a caller-supplied value
naming the target plus standing authority from elsewhere, and the deputy cannot tell which
authority a write uses. A proxy or on-behalf-of service that acts on a caller-supplied path
with its own credential is exposed the same way; Hardy's fix is a capability, one value that
designates the resource and authorizes access. An AI agent with a standing tool credential is a
deputy too; injected prompt content supplies the target.

A deputy is a program that acts for a caller while holding authority of its own, and it is confused when it cannot tell which authority a given action is spending: Hardy's Fortran compiler had a licence to write its own statistics file, so when a caller named the billing file as the debug-output path, the compiler overwrote the billing records, the caller's designation running on the compiler's authority. Hardy's page says the story was "originally published in Operating Systems Reviews, Vol 22, #4, 1988" and calls it a "nearly true story" about events at Tymshare about eleven years earlier. Act-on-behalf-of designs (a proxy, an API gateway, an on-behalf-of service, an assumed role) can recreate the same risk whenever caller input designates the object while the deputy's standing authority authorizes the operation; Hardy's fix is the capability, where the value that names the resource is the value that authorizes it, and the token-based patterns later in this area (subject vs. actor, token exchange, call chains) are the other route, each with its own sources. An AI agent holding a standing tool credential and acting on caller-supplied instructions can be analysed as a deputy: the credential supplies the authority, and the prompt or retrieved content supplies the designation — OWASP's agentic threat model names this case directly, a "Confused Deputy vulnerability arises when an AI agent (the "deputy") has higher privileges than the user but is tricked into performing unauthorized actions on the user's behalf" because it "cannot distinguish between legitimate user requests with proper authorizations and adversarial injected instructions", and separately describes the matching prompt-injection mechanism under T2 Tool Misuse (Agent Hijacking).

## Resources

- [@paper@Norm Hardy — The Confused Deputy (or why capabilities might have been invented)](http://cap-lore.com/CapTheory/ConfusedDeputy.html)
- [@paper@Capability Myths Demolished — Miller, Yee, Shapiro (2003)](http://zesty.ca/capmyths/usenix.pdf)
- [@official@OWASP GenAI Security Project — Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
