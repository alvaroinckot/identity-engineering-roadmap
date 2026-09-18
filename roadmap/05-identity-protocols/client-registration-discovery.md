# Client registration & discovery

**TL;DR:** Before its first request a client has to know where the authorization server's
endpoints are and hold a `client_id` that server recognizes. Otherwise every URL is
hand-configured, and the server has no record of the client's redirect URIs. For discovery the
client fetches a JSON document from `/.well-known/oauth-authorization-server` under the issuer
URL, reads the endpoints, and checks that the `issuer` inside matches the URL it came from. For
a `client_id` there are three routes: a person registers the client through a form, the client
POSTs its metadata to a registration endpoint, or the identifier is an https URL the server
fetches, still a draft. An agent meeting a tool server nobody pre-registered it with depends on
the last two.

Two things a client settles before its first request. Where the authorization server's
endpoints are: RFC 8414 answers with a metadata document at
`/.well-known/oauth-authorization-server`. And how it gets a `client_id`, which has three
answers today, taken apart in the sub-topics: a human registers it (RFC 6749 §2), the client
registers itself at runtime (RFC 7591), or the `client_id` is a URL the server fetches
(Client ID Metadata Documents, a draft). Both matter enormously once the clients are agents
meeting servers nobody pre-registered them with.

## Resources

- [@official@RFC 8414 — Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414)
- [@official@RFC 7591 — Dynamic Client Registration](https://datatracker.ietf.org/doc/html/rfc7591)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
