# Native apps: RFC 8252

**TL;DR:** RFC 8252 is the best current practice for OAuth in installed apps on phones and
desktops. Its target is the embedded web view: a login page inside a view the app controls lets
the app record the password and copy the session cookies, taking the credential instead of a
limited grant. So the app opens the request in the system browser or an in-app browser tab, and
must use PKCE because another app on the device can claim the same redirect and grab the code.
The response returns over a private-use URI scheme, a claimed https URL the operating system
routes to the right app, or a loopback address on any port. A desktop agent that opens a
browser to connect a tool is a native client too.

BCP 212 for installed apps: the authorization request opens in an external user-agent, the system browser or an in-app browser tab, and "native apps MUST NOT use embedded user-agents" (§8.12), because a web view the app controls can record every keystroke of the login form, auto-submit the consent screen and copy the session cookies, walking away with the user's credential instead of the grant. Public native clients MUST implement PKCE and servers MUST support it (§6), since another app on the same device can register the same redirect and intercept the code (§8.1). The response returns over one of three redirect URIs the server MUST offer (§7): a private-use scheme in reverse-domain form (`com.example.app:/…`), a claimed `https` URL, which apps SHOULD prefer because the operating system vouches for the destination app, or a loopback address `http://127.0.0.1:{port}/…` with any port allowed. An installed desktop agent that acts as a native OAuth client and opens the browser to connect a tool falls under this profile and inherits every rule.

## Resources

- [@official@RFC 8252 — OAuth 2.0 for Native Apps](https://datatracker.ietf.org/doc/html/rfc8252)
- [@official@RFC 8252 §7 — Receiving the Authorization Response in a Native App](https://datatracker.ietf.org/doc/html/rfc8252#section-7)
- [@official@RFC 8252 §8.12 — Embedded User-Agents](https://datatracker.ietf.org/doc/html/rfc8252#section-8.12)

---

[← OAuth Security BCP](oauth-security-bcp.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
