# Break-glass access

**TL;DR:** Break-glass access is an emergency administrator account kept usable when the normal
administrative path fails, so that an identity provider or MFA outage cannot lock out the
people who would repair it. The account is cloud-only and not federated, holds a permanently
active administrator role, and is excluded from Conditional Access policies that could block
it. It uses a phishing-resistant credential such as a FIDO2 key kept in a safe, not on an
employee's phone. Every sign-in raises an alert and gets a review, and a drill at least every
90 days proves the path still works. The AWS root user follows the same pattern: MFA, no access
keys, split custody so nobody holds both password and MFA device, and an alert on every use.

Break-glass access is a standing emergency path kept usable when normal administrative access, MFA, federation or Conditional Access fails, so that an outage of the identity provider cannot lock every administrator out. Entra ID calls these *emergency access accounts*, to be used "only for emergency or 'break glass' scenarios where normal administrative accounts can't be used"; the AWS root user is the same thing by construction, "complete access to all AWS resources in your account", not to be touched "unless you have a task that requires root user credentials". A permanently active Global Administrator or a root user is a risk the surrounding controls reduce rather than remove: cloud-only accounts with no dependency on the federated IdP, phishing-resistant credentials (FIDO2 key, certificate) kept in a safe rather than on any employee's phone, exclusion from the Conditional Access policies that could block the sign-in, no root access keys, custody split on AWS so that "no one person can access both MFA and password", an alert on every use, and a drill at least every 90 days to prove the path still works. Both vendors alert on every use and review it afterwards, so any use of the path, by an administrator in an outage or by anyone who has stolen the credential, is an incident to examine, not a quiet success.

## Resources

- [@official@Microsoft Entra ID — Manage emergency access admin accounts](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)
- [@official@AWS IAM — Root user best practices for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)

---

[← 09 · Privileged access](README.md) · [Map](../../README.md)
