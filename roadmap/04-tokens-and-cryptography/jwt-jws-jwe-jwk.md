# JWT: JWS, JWE, JWK

**TL;DR:** A JSON Web Token is a JSON claims set carried as a signed JWS or an encrypted JWE;
trust still depends on validation and application context. A signed JWT is a JWS: a base64url
header naming the algorithm in alg, the claims, and a signature, joined by dots. An encrypted
JWT is a JWE with five dot-separated parts and two algorithm headers, alg for the key and enc
for the content. Some issuers publish verification keys in a JWK Set, whose keys array holds
JWK objects; kid can select among them when present. Registered claims such as iss, sub, aud,
and exp are optional in the base spec, and when aud is present a recipient not named in it must
reject the token.

A JSON claims set carried in signed (JWS) or encrypted (JWE) form, with keys represented as
a JWK Set. Registered claims, header parameters, compact serialization.

## Resources

- [@official@RFC 7519 — JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)
- [@official@RFC 7515 — JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515)
- [@official@RFC 7516 — JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516)
- [@official@RFC 7517 — JSON Web Key (JWK/JWKS)](https://datatracker.ietf.org/doc/html/rfc7517)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
