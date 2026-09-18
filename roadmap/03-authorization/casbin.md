# Casbin

**TL;DR:** Casbin is an open-source access control library that runs inside your application
rather than as a separate service. Its Enforcer takes a request, usually subject, object and
action, and answers allow or deny by evaluating it against a model file and policy rules. The
model file declares the shape of a request, the shape of a policy line, the effect rule for
when several rules match, and the matcher expression that compares the two; for RBAC it adds a
role definition. Policy rules are plain rows loaded from a file or through a storage adapter
backed by a database. One library therefore expresses ACL, RBAC, RBAC with tenants, ABAC and
ReBAC. Casbin does not authenticate; the caller must already know who the subject is.

Casbin is an open-source access-control library whose Enforcer evaluates a model
configuration (request, policy, effect and matchers) and policies loaded from a file or a
storage adapter; its documented models include ACL, RBAC, ABAC and ReBAC variants. It ships
production-ready ports for Go, Java, Node.js, Python, .NET and Rust.

## Resources

- [@official@Casbin](https://casbin.org/docs/overview)

---

[← Policy engines](policy-engines.md) · [03 · Authorization](README.md) · [Map](../../README.md)
