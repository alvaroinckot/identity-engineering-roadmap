# The sync problem

**TL;DR:** The sync problem is keeping a directory and every application it feeds in agreement
about who exists, what their attributes are, and who is gone. Without it, a user removed from
the directory keeps a working account downstream. Base SCIM is request and response only, with
no notification mechanism, so detecting changes is the provisioning client's job. An engine
such as Microsoft Entra's therefore polls its source: one full initial cycle, then incremental
cycles that query for records updated since the last stored watermark. Each cycle disables
users who fall out of scope by setting `active` to false, deletes users the source
hard-deleted, and retries failed operations next cycle. SCIM gives that engine one API for
every application instead of one per vendor.

Keeping two identity stores in agreement is the provisioning client's job under base SCIM:
RFC 7644 is request/response with no push or notification semantics (RFC 9967 later added an
asynchronous event profile on top), so an engine such as Microsoft Entra's provisioning
service runs an initial full cycle and then "periodic incremental cycles" from a stored
watermark, disabling users that fall out of scope and deleting them when the source
hard-deletes. RFC 7643 §1 names the pain that motivated SCIM: every cloud provider with its
own "non-standardized" user-management API.

## Resources

- [@official@Microsoft Entra ID — How Application Provisioning works](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-provisioning-works)
- [@official@RFC 7644 — SCIM: Protocol](https://datatracker.ietf.org/doc/html/rfc7644)
- [@official@RFC 7643 — SCIM: Core Schema](https://datatracker.ietf.org/doc/html/rfc7643)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
