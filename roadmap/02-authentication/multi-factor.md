# Multi-factor

**TL;DR:** Multi-factor authentication asks for at least two different kinds of proof:
something the user knows, such as a password, something they have, such as a phone or hardware
key, or something they are, a biometric. A password alone fails the moment it leaks. A common
second factor is a one-time code: server and authenticator app share a secret, and each derives
a short code from an HMAC over a counter (HOTP) or the current 30-second time step (TOTP). The
server accepts a code once and tolerates a little clock drift. Codes and push approvals are
still phishable: a fake login page relays the code, and repeated push prompts annoy a user into
approving one. NIST SP 800-63B therefore requires verifiers to offer a phishing-resistant
option at AAL2.

Factors (know / have / are), one-time passwords, and [authenticator assurance
levels](assurance-levels.md). Authentication-fatigue attacks and phishable OTPs are why SP
800-63B-4 requires verifiers to offer a phishing-resistant option at AAL2 (§2.2.2).

## Resources

- [@official@NIST SP 800-63B — Authentication & Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [@official@RFC 4226 — HOTP](https://datatracker.ietf.org/doc/html/rfc4226)
- [@official@RFC 6238 — TOTP](https://datatracker.ietf.org/doc/html/rfc6238)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
