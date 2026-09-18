# Aside: Kerberos

**TL;DR:** Kerberos is a ticket-based network authentication system where every user and
service shares a secret key with a central Key Distribution Center (KDC). It is an aside
because it is a shared-secret design for an organization's own network, not a web protocol,
kept for the realm, ticket, and delegation concepts that return later. A client authenticates
to the KDC once and gets a ticket-granting ticket, trades it for a service ticket per service,
and the service verifies that ticket with the key it shares with the KDC. A realm is an
administrative boundary and can operate multiple KDC servers. A ticket proves who the client is
but grants no permissions, and flags such as forwardable and proxiable let a service carry the
client's identity onward to another service.

Ticket-based authentication with a Key Distribution Center as the realm authority. Worth a
page for realms, tickets, and the delegation concepts that reappear later; not a deep dive.

## Resources

- [@official@RFC 4120 — The Kerberos Network Authentication Service (V5)](https://datatracker.ietf.org/doc/html/rfc4120)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
