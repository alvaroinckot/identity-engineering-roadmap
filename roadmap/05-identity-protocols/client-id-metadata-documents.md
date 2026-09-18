# Client ID Metadata Documents: CIMD

**TL;DR:** Client ID Metadata Documents is an OAuth WG Internet-Draft where the `client_id` is
an HTTPS URL serving client metadata. It covers a client meeting an authorization server with
which it has no prior relationship, where manual registration is impossible and dynamic
registration creates cleanup work. The authorization server fetches the document, checks that
its `client_id` equals the URL, and reads its redirect URIs and other metadata. The document
cannot contain shared secrets or private keys. The server must refuse redirects and guard
against server-side request forgery. An agent connecting to an unfamiliar tool server fits this
no-prior-relationship case, but the draft can still change.

An OAuth WG draft in which the `client_id` is an https URL hosting the client's metadata: the
authorization server fetches the document and knows the client without prior registration,
manual or dynamic. The Client Identifier URL must use https, must have a path component and
must not carry a fragment or userinfo. It is how a client identifies itself to an
authorization server it has never met, which is exactly the position an agent is in; the
cost moves to the server, which now fetches a URL the client chose. **Draft, standards
track**: expect changes.

## Resources

- [@official@OAuth Client ID Metadata Document (IETF OAuth WG draft)](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document)

---

[← Client registration & discovery](client-registration-discovery.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
