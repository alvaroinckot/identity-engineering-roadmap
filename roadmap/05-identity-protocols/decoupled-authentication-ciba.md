# Decoupled authentication: CIBA

**TL;DR:** CIBA (Client-Initiated Backchannel Authentication) lets a relying party ask an
OpenID provider to authenticate a user when the requesting device has no browser to redirect
through, for example a headless agent on a server. The client POSTs an authentication request
to the provider's backchannel authentication endpoint, identifying the user with one hint such
as `login_hint`, and receives an `auth_req_id`. The provider prompts the user to authenticate
on their own device, often a phone. The client receives the tokens in the mode fixed at
registration: it polls the token endpoint with the CIBA grant type, or the provider pings it to
fetch them, or pushes them to its endpoint. A `binding_message` shown on both devices lets the
user confirm the phone prompt belongs to the request they started.

Client-Initiated Backchannel Authentication separates the device that asks from the device that answers: the Relying Party POSTs an authentication request straight to the OpenID Provider's Backchannel Authentication Endpoint, naming the user with exactly one of `login_hint`, `login_hint_token` or `id_token_hint` (CIBA Core §7.1), gets back an opaque `auth_req_id` (§7.3), and the person authenticates and consents on the Authentication Device, "often a smartphone" (§2), while the Consumption Device never sees a redirect. The tokens arrive in one of three modes fixed at registration (§5): poll the token endpoint with the `urn:openid:params:grant-type:ciba` grant, ping (the OP notifies the client's endpoint, which then fetches from the token endpoint) or push (the OP posts the tokens to the client). An optional short `binding_message` displayed on both devices helps the person relate the prompt on their phone to the request they started (§7.1). An agent running headless on a server has no browser to be redirected through, so CIBA is the standard shape for asking the human on another device before a sensitive step, with the returned tokens identifying who answered and, when the OP supplies it, the authentication context.

## Resources

- [@official@OpenID Connect Client-Initiated Backchannel Authentication Flow — Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
