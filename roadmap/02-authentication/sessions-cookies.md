# Sessions & cookies

**TL;DR:** HTTP has no memory between requests, so after a login the server generates a random
session identifier, stores the user's state under it, and sends it in a Set-Cookie header. The
browser returns applicable, unexpired cookies in later requests whose host, path, and security
conditions match, and the server looks the state up. Whoever presents that identifier is
treated as the user, so the cookie gets the Secure attribute, which keeps it off plain HTTP,
and HttpOnly, which hides it from page scripts. RFC 6265 names two weaknesses the attributes
leave open: cookies are ambient authority that can support cross-site request forgery, and
sibling domains or a network attacker can overwrite some cookies. CSRF defenses and server-side
checks cover what the attributes cannot.

Servers commonly put a nonce or session identifier in a cookie and use it to look up
server-side state between HTTP requests (RFC 6265 §8.4): the bridge between passwords and
tokens, and still how browsers stay signed in. `Secure` and `HttpOnly` narrow a cookie's
exposure, but RFC 6265 §8 is explicit that cookies remain ambient authority with weak
integrity across sibling domains, so session security cannot live in the attributes alone.

## Resources

- [@official@RFC 6265 — HTTP State Management (Cookies)](https://datatracker.ietf.org/doc/html/rfc6265)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
