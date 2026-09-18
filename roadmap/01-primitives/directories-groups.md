# Directories & groups

**TL;DR:** A directory is a hierarchical database of the objects on a network: user accounts
with their names and passwords, computer accounts, printers, shared servers. A directory
service such as Active Directory Domain Services stores that data, answers lookups from users
and applications, and has sign-in authentication and access control built in. In the LDAP model
every entry is a named set of attributes arranged in a tree, and the entry's objectClass
attribute says which attributes it must and may carry. Groups collect accounts, and enterprises
grant and revoke access mostly by changing membership in security groups such as Domain Admins.
A backend developer meets the LDAP model as named entries with attributes; group-based
authorization depends on the directory and application.

The directory is identity's original database. Groups, and security groups in particular
(Domain Admins and friends), are how enterprises actually grant and revoke access.


Deep dive → [06 · Directories & provisioning](../06-directories-and-provisioning/README.md)

## Resources

- [@official@Microsoft Active Directory Domain Services documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [@official@RFC 4512 — LDAP: Directory Information Models](https://datatracker.ietf.org/doc/html/rfc4512)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
