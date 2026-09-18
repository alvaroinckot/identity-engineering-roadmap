# ACL & RBAC

**TL;DR:** An access control list (ACL) associates a resource with entries stating who may
perform which operations on it. Role-based access control (RBAC) adds an indirection: users are
assigned roles, and permissions are assigned to roles, so access changes can be made through
role assignments. The NIST/ANSI model defines users, roles, permissions, operations, and
objects. Core RBAC is required. Hierarchical RBAC and static and dynamic separation-of-duty
relations are independent additional components. An application may store these relations in
tables or another policy store, but that storage layout is not part of the model.

ACLs attach permissions or relationships to resources; RBAC puts roles between users and
permissions. The NIST/ANSI RBAC model (INCITS 359): Core RBAC, Hierarchical RBAC, and static
and dynamic separation-of-duty relations.

## Resources

- [@official@NIST/ANSI RBAC Model (Ferraiolo–Sandhu)](https://csrc.nist.gov/projects/role-based-access-control)
- [@official@Zanzibar: Google's Consistent, Global Authorization System](https://www.usenix.org/conference/atc19/presentation/pang) (USENIX ATC 2019, §2.1 on ACLs as relation tuples)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
