# Assume-role

**TL;DR:** AssumeRole is AWS's pattern for obtaining temporary credentials under a role's
permissions. A caller authenticates to the security token service and requests a role session,
which can reduce distribution of credentials carrying the role's permissions. The trust policy
controls who may assume the role, while the permissions policy controls what the role may do.
Optional session policies can only narrow the effective permissions. `RoleSessionName`
identifies the session, while `SourceIdentity` is supplied by the caller and can be required by
policy; neither is inherently proof of the original caller. Transitive tags and a set source
identity can persist through role chaining.

The cloud-era pattern: exchange one credential for temporary credentials of a role, with a
trust policy saying who may assume it and session tags carrying context.

## Resources

- [@official@AWS STS AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
