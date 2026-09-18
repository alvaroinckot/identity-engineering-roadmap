# Identity-aware proxies: BeyondCorp

**TL;DR:** An identity-aware proxy is a gateway in front of each internal application that
checks the user and the device on every request, so the corporate network itself grants
nothing. Google's BeyondCorp is the reference design: every enterprise application sits in
public DNS behind an Internet-facing access proxy. The proxy takes the user's single sign-on
token and the device's certificate, infers a trust level for both, and authorizes each request
from those inputs and the user's groups. It is the policy enforcement point of the zero trust
resource portal model. It sees a device only when that device connects, so it cannot watch it
between requests. BeyondCorp admits only managed devices; how an agent without one identifies
itself to the proxy is a separate question.

An access proxy fronts each enterprise application, obtains an SSO-authenticated user token
and the device certificate, applies its access checks, and only then forwards the request,
so being on the corporate network grants nothing. Google's BeyondCorp design (Ward & Beyer,
;login:, December 2014) exposes every enterprise application "via an Internet-facing access
proxy" that public DNS CNAMEs point at, and an Access Control Engine inside the proxy
authorizes "on a per-request basis" from the device certificate (keyed to a device inventory
record), the SSO token, group membership, and an inferred trust level for both user and
device, so that "access depends solely on device and user credentials, regardless of a
user's network location". In SP 800-207 terms the proxy is the PEP of the resource-portal
deployment (§3.2.3: one gateway component that "does not need to be installed on all client
devices") or an enclave gateway when it fronts a whole data center (§3.2.2); NIST notes the
identity-driven approach "works well with the resource portal model" (§3.1.1) and names the
cost, that a portal "can only scan and analyze assets and devices once they connect", and so
may not be able to monitor them continuously. SP 800-207 treats device identity and status
as "secondary support data" in the identity-driven approach (§3.1.1) and allows client
identity to include a service identity (§2.1 tenet 4); BeyondCorp itself admits only managed
devices, so how an agent without one identifies itself to the proxy is covered under
[Workload & agent identity](../07-workload-and-agent-identity/README.md).

## Resources

- [@paper@BeyondCorp: A New Approach to Enterprise Security (Ward & Beyer, ;login: December 2014)](https://www.usenix.org/publications/login/dec14/ward)
- [@official@NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

---

[← Zero trust architecture](zero-trust-architecture.md) · [10 · Zero trust & continuous access](README.md) · [Map](../../README.md)
