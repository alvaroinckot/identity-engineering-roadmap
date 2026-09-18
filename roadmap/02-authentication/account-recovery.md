# Account recovery

**TL;DR:** Account recovery is how a user gets back in after losing the authenticators they log
in with, and it ends with new authenticators bound to the account. Because recovery can result
in newly bound authenticators, NIST calls it the weak point in many authentication mechanisms.
NIST SP 800-63B scales recovery with the account's AAL: recovering an AAL2 account takes two
recovery codes obtained by different methods, one code plus a still-bound single-factor
authenticator, or repeated identity proofing, and every recovery notifies the account holder.
In the everyday forgot-password flow, respond the same way and in the same time whether or not
the account exists, and send a single-use, expiring, cryptographically random token. OWASP
advises against security questions as the only check and against locking the account on reset
requests.

Recovery is the second door into an account: NIST says it "differs from authentication", but
it can end with the subscriber holding newly bound authenticators, so SP 800-63B-4 §4.2
sizes it to the AAL the account can reach (recovering an AAL2-capable account takes two
recovery codes obtained by different methods, one code plus a still-bound single-factor
authenticator, or repeated identity proofing, and every recovery notifies the subscriber or
their designee). The password-reset flow OWASP's Forgot Password Cheat Sheet prescribes:
answer identically and in a consistent amount of time whether or not the account exists,
issue a single-use, expiring, cryptographically random token, do not use security questions
as the sole check, and do not lock the account on reset requests. After recovery the
subscriber can bind new authenticators, which is why SP 800-63B-4 §6.3 calls the process
"the weak point in many authentication mechanisms".

## Resources

- [@official@NIST SP 800-63B-4 — Authentication and Authenticator Management, §4.2 Account Recovery](https://pages.nist.gov/800-63-4/sp800-63b.html#recovery)
- [@official@OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
