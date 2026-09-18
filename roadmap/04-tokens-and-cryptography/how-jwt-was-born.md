# How JWT was born

**TL;DR:** JWT's shape, a compact string of base64url segments carrying a small JSON claims
set, follows from design choices its editor has described in his own account. As Mike Jones
tells it, several groups had built similar JSON security token formats, and he surveyed them
and proposed one convergent format. That proposal merged with a separate JSON signature and
encryption proposal to become the JOSE working group drafts. The stated design goal was to keep
simple things simple: common features in, esoteric ones out. Microsoft's Katana project shipped
OWIN middleware whose components were primarily focused on providing different means of
authentication; the Katana documentation never mentions JWT, so it shows only that .NET shipped
authentication middleware. The origin sequence is recollection, not independently established
history.

Why JWT looks the way it does: Mike Jones recalls JWT and JOSE emerging from merged JSON
token and signature proposals in the JOSE working group; separately, the .NET Katana 2.0
release shipped OWIN middleware "primarily focused on providing different means of
authentication". The history here is the editor's own account, stated as such.

## Resources

- [@article@Mike Jones — "JWT and JOSE are now RFCs!"](https://self-issued.info/?p=1387)
- [@official@Microsoft Katana Project (OWIN)](https://learn.microsoft.com/en-us/aspnet/aspnet/overview/owin-and-katana/an-overview-of-project-katana)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
