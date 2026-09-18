# 03 · Authorization

Deciding it. The models in the order they were invented, and how to choose one.

## Topics

1. [The authn/authz split](the-authn-authz-split.md)
2. [ACL & RBAC](acl-rbac.md)
3. [ABAC & XACML](abac-xacml.md)
4. [ReBAC & Zanzibar](rebac-zanzibar.md)
5. [Policy engines](policy-engines.md)
   1. [OPA & Rego](opa-rego.md)
   2. [Cedar](cedar.md)
   3. [OpenFGA](openfga.md)
   4. [Casbin](casbin.md)
6. [Interop: AuthZEN](interop-authzen.md)
7. [Choosing a model](choosing-a-model.md)

## What AI agents change

Agents want fine-grained, task-scoped permissions decided per call. That pushes toward
externalized policy (ABAC/ReBAC behind a PDP) and toward authorization requests that carry
intent (RFC 9396, → [07](../07-workload-and-agent-identity/README.md)).

---

[← Map](../../README.md)
