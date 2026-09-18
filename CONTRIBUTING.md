# Contributing

Three kinds of change are welcome. Each is one small pull request.

## Add a resource to a topic

Open `roadmap/<area>/<topic>.md` and add one line under **Resources**:

```markdown
- [@official@RFC 9449 — Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
```

Tags: `official` is the spec, RFC, standard, or vendor documentation that defines the thing.
`article` is a blog post or explainer, `video` a talk, `paper` an academic paper,
`opensource` a project. Prefer official. When the resource is a spec, link the exact section.

## Fix wording

Topic text is one to four sentences: what it is, why it exists, what AI agents change. When
a term has a normative definition (subject, actor, assertion, authenticator), use the spec's
definition and point at the section. History claims ("X was the first to ...") need a source
that says so; otherwise they stay flagged.

## Propose a topic

Open a **New topic** issue first so placement on the map can be discussed. A topic then
needs, in one PR:

1. a node in the Mermaid map in `README.md`, inside its area, with the exact title;
2. a file `roadmap/<area>/<slug>.md` whose `#` heading is that same title;
3. an entry in the area's `README.md` topic list, in map order.

A sub-topic (a part of an existing topic, like PKCE under OAuth 2.x) needs the same three,
with its node on its own line inside the area subgraph, `<topic id> -.-> x["Label"]`, and its
entry indented under the topic in the area `README.md`. A sub-topic may have sub-topics of its
own, one level down: `<sub id> -.-> x["Label"]`, entry indented 6 spaces.

Then run `python3 scripts/render_map.py` to redraw `assets/roadmap.png` from the map (needs
Google Chrome) and commit the picture with the change.

## Rules

- Nothing from memory. Every statement of fact has a resource behind it, or the topic says
  `_No dedicated source yet._`
- Primary sources over summaries. Blogs are fine as `article` for color and history.
- Deprecated guidance is named as deprecated (implicit flow, resource owner password
  credentials, SMS as strong MFA).
- Versions are precise: OAuth 2.0 vs 2.1, SP 800-63-3 vs -4, WebAuthn Level 2 vs 3.
- Concrete actors in examples ("a CI runner deploying to prod", "an agent reading a
  customer's calendar"), never foo/bar.
- `python3 scripts/check.py` must pass. CI runs it on every pull request.
- Maintainers verify claims against the cited text before merging. Expect questions.
