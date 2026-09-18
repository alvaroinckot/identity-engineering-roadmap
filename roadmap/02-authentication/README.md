# 02 · Authentication

Proving it. From the plaintext-password dark ages through sessions and MFA to
phishing-resistant credentials.

## Topics

1. [Assurance levels: IAL, AAL, FAL](assurance-levels.md)
2. [Passwords](passwords.md)
3. [Sessions & cookies](sessions-cookies.md)
   1. [Device-bound sessions: DBSC](device-bound-sessions-dbsc.md)
4. [Multi-factor](multi-factor.md)
   1. [Step-up authentication: RFC 9470](step-up-authentication.md)
5. [Account recovery](account-recovery.md)
6. [Phishing-resistant: FIDO2, WebAuthn, passkeys](phishing-resistant-fido2-webauthn-passkeys.md)
7. [Aside: Kerberos](aside-kerberos.md)

## What AI agents change

Agents cannot complete MFA or hold a passkey the way a person does. Human authentication
stays at the front door; what an agent presents afterwards is workload identity plus an
explicit delegation (→ [07](../07-workload-and-agent-identity/README.md), [08](../08-delegation-and-impersonation/README.md)).

---

[← Map](../../README.md)
