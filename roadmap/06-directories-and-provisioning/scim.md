# SCIM

**TL;DR:** SCIM is an HTTP API for provisioning, with standard JSON schemas for User and Group
resources and operations to create, read, update, and delete them. It lets a provisioning
client manage many applications through one protocol instead of a custom API per vendor. The
client calls the application's `/Users` and `/Groups` endpoints. The service provider assigns a
stable `id`, while the client can supply `externalId`. The `active` attribute is an
administrative status whose definitive meaning is provider-specific; false typically means the
account is suspended. Filtering and PATCH are optional, and every operation on a deleted
resource must return 404 even when deletion is only logical.

Core schema (User, Group, extensions) and the REST protocol for provisioning. Create, modify
and delete are protocol operations (RFC 7644 §§3.3–3.6); deactivation is represented by
setting the User `active` attribute to false (RFC 7643 §4.1.1). The joiner/mover/leaver
process an organization runs on top of them is not defined by either RFC — see [Identity
governance: lifecycle & access reviews](identity-governance.md).

## Resources

- [@official@RFC 7643 — SCIM: Core Schema](https://datatracker.ietf.org/doc/html/rfc7643)
- [@official@RFC 7644 — SCIM: Protocol](https://datatracker.ietf.org/doc/html/rfc7644)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
