# X.500 & LDAP

**TL;DR:** LDAP is the protocol for querying and updating a directory, and its data model comes
from the X.500 directory standards. The directory stores each object, such as a user or a
machine, as an entry, a named set of attributes placed in a tree, and object classes decide
which attributes an entry must and may carry. A client sends operations to the directory
server: Bind to authenticate, Search to fetch the entries matching a filter, and Add, Modify,
and Delete to change entries. A backend usually meets LDAP as a password check: the application
binds with the user's distinguished name and password, and a successful bind means the password
matched. A simple bind sends that password in cleartext, so the connection needs a transport
that guarantees confidentiality.

The directory data model (entries, attributes, object classes, the DIT) and the protocol to
query it. RFC 4511 §4.2 says the Bind operation "should be thought of as the "authenticate"
operation"; a simple bind sends a DN and a cleartext password (§6), which is what
applications rely on when they verify a user's password against a directory.

## Resources

- [@official@RFC 4512 — LDAP: Directory Information Models](https://datatracker.ietf.org/doc/html/rfc4512)
- [@official@RFC 4511 — LDAP: The Protocol](https://datatracker.ietf.org/doc/html/rfc4511)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
