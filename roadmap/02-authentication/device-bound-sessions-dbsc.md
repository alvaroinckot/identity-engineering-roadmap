# Device-bound sessions: DBSC

**TL;DR:** DBSC ties a web session to a private key the browser keeps on the device, in a TPM
where the platform has one. It targets malware that copies a session cookie off a laptop and
replays it elsewhere for as long as the cookie lives. The server opens a session with a
Secure-Session-Registration response header, the browser creates a key pair and registers the
public key, and the server then issues only short-lived cookies. When one expires the browser
signs a fresh server challenge with the private key to get the next one, so a copied cookie
stops working at the next refresh. DBSC does not stop malware still running on the device, and
it is a W3C Editor's Draft whose header names may change.

Device Bound Session Credentials bind a web session to a private key the browser keeps on
the device (in a TPM or equivalent where the platform has one), so a session cookie that
malware copies off the machine stops working as soon as it expires. The server opens a
session with a `Secure-Session-Registration` response header, the browser registers a public
key, and from then on the server hands out short-lived cookies that the browser renews by
signing a fresh server challenge (`Secure-Session-Challenge` in, `Secure-Session-Response`
out); a stolen cookie is good only until the next refresh, and the refresh needs the key.
DBSC is a W3C Web Application Security Working Group Editor's Draft (dated 8 September 2026
when read) that describes itself as work in progress, so header names and formats may still
change. Outside the browser, RFC 9449 DPoP (→ [05](../05-identity-protocols/dpop.md)) plays
the analogous role, sender-constraining OAuth access and refresh tokens to a key the client
proves it holds.

## Resources

- [@official@Device Bound Session Credentials (W3C WebAppSec Editor's Draft)](https://w3c.github.io/webappsec-dbsc/#intro)

---

[← Sessions & cookies](sessions-cookies.md) · [02 · Authentication](README.md) · [Map](../../README.md)
