# Shared Signals & CAEP

**TL;DR:** The Shared Signals Framework (SSF) lets one service report security events about a
user, device, or session to another; CAEP defines event types used for access decisions.
Without a signal or another status check, an application may continue accepting an otherwise
valid session after the identity provider revokes it. Each event is a Security Event Token
whose `events` claim states a fact about the subject in `sub_id`, such as session revoked,
credential changed, or device compliance changed. A Transmitter pushes events to a Receiver or
lets the Receiver poll. Events are statements rather than commands, so the Receiver chooses
enforcement. SSF event tokens contain neither `sub` nor `exp`; the profile forbids both.

Publishing security events (session revoked, credential changed, device compliance
changed) between Transmitters and Receivers as Security Event Tokens, so a Receiver can
re-evaluate access continuously instead of once.

## Resources

- [@official@OpenID Shared Signals Framework (SSF)](https://openid.net/specs/openid-sharedsignals-framework-1_0-final.html)
- [@official@OpenID CAEP — Continuous Access Evaluation Profile](https://openid.net/specs/openid-caep-1_0-final.html)
- [@official@RFC 8417 — Security Event Token (SET)](https://datatracker.ietf.org/doc/html/rfc8417)

---

[← 10 · Zero trust & continuous access](README.md) · [Map](../../README.md)
