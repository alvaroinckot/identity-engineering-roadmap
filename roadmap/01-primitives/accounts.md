# Accounts

**TL;DR:** User accounts represent people, service accounts represent software, and agent
accounts represent AI agents. Each workload account should stand for one application or
workload. When several applications share one Google Cloud service account, Cloud Audit Logs
name the account but not the application that acted. When a person uses a service account for a
manual task, or an agent runs under a person's account, human and automated activity become
indistinguishable and the account collects more privilege than either needs. So give each
application its own account, avoid shared default accounts, and prefer an identity attached to
the platform over a downloaded long-lived secret.

User accounts, service accounts, agent accounts. The distinctions blur in practice (people
using shared service accounts, agents running under a human's account) and that blurring
destroys attribution and blast-radius control.

## Resources

- [@official@Google Cloud — Best practices for using service accounts](https://cloud.google.com/iam/docs/best-practices-service-accounts)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
