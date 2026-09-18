# Passwords

**TL;DR:** A password is a secret the user knows and types, so anyone who captures it, on a
phishing page or in a breach, can replay it. Verifiers should not store plaintext passwords.
The verifier stores a salted hash made with a slow, purpose-built password hashing function
such as Argon2id, and at login it hashes what the user typed and compares the two. A fast
general hash like SHA-256 is not password storage. NIST SP 800-63B tells verifiers to allow
long passwords, impose no composition rules, skip forced periodic changes unless there is
evidence of compromise, screen new passwords against a blocklist of breached and common ones,
and throttle failed attempts per account. The usual mistakes are the reverse: complexity rules,
forced rotation, silent truncation, and lockout counted per IP address.

A password is a something-you-know authenticator and is not phishing-resistant; verifiers
must store passwords salted and hashed with a suitable password-hashing scheme (SP 800-63B-4
§3.1.1.2; OWASP Password Storage; Argon2, RFC 9106). Read what NIST SP 800-63B actually says
about length, composition rules, rotation, and breached-password screening, not folk wisdom.

## Resources

- [@official@NIST SP 800-63B — Authentication & Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [@article@OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [@article@OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [@official@RFC 9106 — Argon2](https://datatracker.ietf.org/doc/html/rfc9106)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
