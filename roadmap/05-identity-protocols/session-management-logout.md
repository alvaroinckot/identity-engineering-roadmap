# Session management & logout

**TL;DR:** OpenID Connect deployments commonly maintain separate sessions at the Relying Party
and OpenID Provider. Signing out at the provider does not clear an RP session until the RP
receives or detects a logout event. Session Management lets an RP poll a hidden provider iframe
using `session_state`. RP-Initiated Logout redirects the user to `end_session_endpoint`,
usually with the recommended `id_token_hint`. Front-Channel Logout uses browser iframes, while
Back-Channel Logout POSTs signed Logout Tokens directly to registered RPs. Logout is distinct
from revocation: refresh tokens carrying `offline_access` normally survive, so they require a
separate revocation decision.

Four specifications cover what happens after login. Session Management 1.0 lets a Relying
Party poll the provider's `check_session_iframe` with the `session_state` it received at
login to learn that the user's session at the provider changed (§3). RP-Initiated Logout 1.0
gives the RP an `end_session_endpoint` to send the user to, with `id_token_hint` and
`post_logout_redirect_uri` (§2). Front-Channel Logout 1.0 has the provider render every RP's
`frontchannel_logout_uri` in the user's browser; Back-Channel Logout 1.0 instead POSTs a
signed Logout Token (a JWT with `sub` and/or `sid` and an `events` claim, §2.4) straight to
each RP's `backchannel_logout_uri`, the one variant that needs no browser in the loop, which
is the situation of a session an agent holds. Logout and token revocation are distinct:
Back-Channel Logout §2.7 says refresh tokens issued to the session without `offline_access`
SHOULD be revoked with it, while those with `offline_access` normally outlive the logout, so
an agent's long-lived grant survives the user's logout unless someone revokes it (→ [Token
lifecycle](token-lifecycle-introspection-revocation.md); → [10 · Revocation & the kill
switch](../10-zero-trust-and-continuous-access/README.md)).

## Resources

- [@official@OpenID Connect Session Management 1.0](https://openid.net/specs/openid-connect-session-1_0.html)
- [@official@OpenID Connect RP-Initiated Logout 1.0](https://openid.net/specs/openid-connect-rpinitiated-1_0.html)
- [@official@OpenID Connect Front-Channel Logout 1.0](https://openid.net/specs/openid-connect-frontchannel-1_0.html)
- [@official@OpenID Connect Back-Channel Logout 1.0 §2.4 — Logout Token](https://openid.net/specs/openid-connect-backchannel-1_0.html#LogoutToken)
- [@official@OpenID Connect Back-Channel Logout 1.0 §2.7 — Back-Channel Logout Actions](https://openid.net/specs/openid-connect-backchannel-1_0.html#BCActions)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
