# Phishing-resistant: FIDO2, WebAuthn, passkeys

**TL;DR:** WebAuthn credentials are public-key pairs: the private key stays in an authenticator
such as a phone or security key, and the relying party stores its public key and associated
data. Passwords and one-time codes fail against phishing because the user types them into
whatever page asks and the fake page forwards them. The credential is scoped to a relying party
ID. The authenticator signs its data plus a hash of browser data containing the server's
challenge and page origin. The relying party checks the expected origin and RP ID, so a
lookalike domain gets nothing it can replay. FIDO2 is WebAuthn plus CTAP, the protocol for
external authenticators over USB, NFC, or BLE; a passkey is the consumer name for such a
credential, synced across devices or bound to one.

Public-key credentials bound to an origin: the browser API (WebAuthn), the authenticator
protocol (CTAP2), and passkeys as the consumer packaging. Origin binding is why these defeat
phishing where OTP cannot.

## Resources

- [@official@W3C Web Authentication (WebAuthn) Level 3](https://www.w3.org/TR/webauthn-3/)
- [@official@FIDO Alliance — User Authentication Specifications (FIDO2 / CTAP2)](https://fidoalliance.org/specifications/)
- [@official@NIST SP 800-63B-4 §3.2.5 Phishing Resistance](https://pages.nist.gov/800-63-4/sp800-63b.html#verifimpers)
- [@official@FIDO Alliance — Passkeys](https://fidoalliance.org/passkeys/)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
