# Delegation as a primitive

**TL;DR:** Delegation is one party acting for another: a service that reads a customer's
mailbox because the customer asked it to, a build runner that deploys because an engineer
approved the release. Hardy's confused deputy is a compiler licensed to write its own
statistics file that also writes debug output wherever the caller names. A caller names the
billing file, and the compiler overwrites the billing records: it carries authority granted by
two parties and cannot tell which one a given write uses. The deputy is not malicious. It
cannot express on whose behalf it acts. Every delegation design has to answer that question,
which is why later areas keep subject and actor apart. An AI agent can become a confused deputy
when it mixes user authority with its own.

Acting for another, stated as an idea before any mechanism. The mechanisms live in
[08 · Delegation & impersonation](../08-delegation-and-impersonation/README.md); the classic failure of
acting for another, Hardy's confused deputy, opens that area.

## Resources

- [@paper@Norm Hardy — The Confused Deputy (or why capabilities might have been invented)](http://cap-lore.com/CapTheory/ConfusedDeputy.html)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
