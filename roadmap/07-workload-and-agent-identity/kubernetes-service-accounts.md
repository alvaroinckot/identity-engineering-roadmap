# Kubernetes service accounts & projected tokens

**TL;DR:** A Kubernetes ServiceAccount is the identity a Pod uses inside the cluster; every
namespace has a default one. The legacy proof was a Secret containing a long-lived token. The
current approach is a projected `serviceAccountToken` volume: the kubelet requests a JWT with
the audience and lifetime declared in the Pod spec, mounts it, and refreshes it before expiry.
Kubernetes API authentication rejects a Pod-bound token after the Pod is deleted, but an
external service performing offline JWT validation may accept it until expiry. The API server
publishes OIDC discovery and JWKS endpoints for external verification. Set the audience to the
receiving service.

A ServiceAccount is the identity Kubernetes gives a process running in a Pod, "a type of non-human account that, in Kubernetes, provides a distinct identity in a Kubernetes cluster", and every namespace gets a `default` one whether you asked or not. What a Pod should receive is not a stored Secret but a projected `serviceAccountToken` volume: a JWT minted through the TokenRequest API with the `audience` and `expirationSeconds` set in the Pod spec, bound to that Pod (invalid once the Pod or ServiceAccount is deleted), with `sub` of the form `system:serviceaccount:<namespace>:<name>`, and rotated by the kubelet once it passes 80% of its TTL. The docs state that from v1.22 the kubelet mounts this short-lived, auto-rotating token by default, and that long-lived `kubernetes.io/service-account-token` Secrets are the legacy path. The API server publishes OIDC-compatible discovery (`/.well-known/openid-configuration`) and JWKS (`/openid/v1/jwks`) endpoints, so an external verifier configured to trust the cluster can validate audience-bound projected tokens, the same exchange as [workload identity federation](workload-identity-federation.md) with the cluster as the platform issuer; an agent running in a Pod gets its identity from the audience-bound token the kubelet projects, not from a credential someone mounted.

## Resources

- [@official@Kubernetes — Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [@official@Kubernetes — Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

---

[← Workload identity federation](workload-identity-federation.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
