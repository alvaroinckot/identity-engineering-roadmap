# Choosing a model

**TL;DR:** Choosing an authorization model affects the system's design and should happen early.
RBAC can fit a product with a few stable roles, but numerous narrow roles make checks, testing,
and auditing harder and can add lookup latency when roles no longer fit in a credential. OWASP
therefore recommends considering attribute-based or relationship-based control for fine-grained
decisions involving resource, environment, or relationship facts. Whatever model is chosen,
deny access when no rule grants it, perform checks on the server for every request, test the
authorization logic, and keep logs appropriate for detecting and investigating access-control
failures.

Consistency vs. latency, where the relationship data lives, how decisions are audited, who
writes policy. Compare across the sources in this area; no single source owns this topic.

## Resources

- [@official@OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
