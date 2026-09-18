# Hashing & password storage

**TL;DR:** Password storage keeps a value that lets you check a password without being able to
read it back. If the users table leaks, plaintext passwords work everywhere the same password
was reused, and fast hashes such as SHA-256 are little better because attackers test guesses
against them fast. So passwords go through a slow, memory-hard function: Argon2id is the
recommended choice, with scrypt next, bcrypt for legacy systems, and PBKDF2 where FIPS
validation is required. Each password gets its own random salt, so identical passwords hash
differently and precomputed tables are useless. The work factor is tuned so one hash takes
under a second and raised over time by re-hashing at the user's next login; legacy MD5 or SHA-1
stores are upgraded the same way.

Memory-hard hashing (Argon2), salts, work factors, and the storage arc from plaintext to
today's recommendations.

## Resources

- [@official@RFC 9106 — Argon2](https://datatracker.ietf.org/doc/html/rfc9106)
- [@article@OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
