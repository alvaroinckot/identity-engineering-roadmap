# Zero trust architecture

**TL;DR:** Zero trust architecture is NIST's model for granting access per session and per
resource without trusting network location. Authentication to a laptop or presence on the
corporate network does not make later resource requests valid. A policy enforcement point
controls access to a resource, portal, or enclave. A policy administrator commands that point
using decisions from a policy engine, which evaluates identity, the requested application, and
observable device state such as patch level. Authorization to one resource grants no automatic
access to another. Policy is continually re-evaluated during ongoing communication, allowing
the policy administrator to pause or terminate a connection when its inputs change.

NIST's model: policy engine, policy administrator, policy enforcement point. Identity is one
input to dynamic policy, next to the application and the requesting asset's state (§2.1
tenet 4); no implicit trust from network location (tenet 2).

## Resources

- [@official@NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

---

[← 10 · Zero trust & continuous access](README.md) · [Map](../../README.md)
