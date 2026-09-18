# How a vault works

**TL;DR:** A vault stores secrets such as database passwords and API keys encrypted, and
releases each one only to an authenticated caller allowed to read it. The secrets then no
longer sit hard-coded in source. HashiCorp Vault starts sealed. With Shamir sealing, shares
reconstruct an unseal key that decrypts the root key; auto-unseal delegates the unseal
operation to a trusted device or service. A client authenticates through an auth method and
gets a token carrying a policy; each request is checked against that path-based,
deny-by-default policy and audited whether or not it succeeds. Dynamic secrets carry a lease
with a TTL, and revoking the lease invalidates them at once. AWS Secrets Manager is the managed
alternative, gating access with IAM policies and encrypting each value with KMS.

Seal/unseal, auth methods, policies, leases. HashiCorp Vault as the worked example; cloud
secret managers (AWS Secrets Manager) as the managed alternative.

## Resources

- [@official@HashiCorp Vault documentation](https://developer.hashicorp.com/vault/docs)
- [@official@AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

---

[← 14 · Secrets & vaults](README.md) · [Map](../../README.md)
