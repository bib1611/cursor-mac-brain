# Codex - BM X December reach probe

Time: 2026-06-22 13:13 CDT

Checked whether authenticated `xurl` can get Biblical Man X analytics back to December 2025.

Result: not with the current `xurl` auth setup.

Proof:

- User timeline pull with owner metrics currently reaches back to `2026-03-24T18:30:27Z`.
- Direct user timeline probes for `2025-12-01T00:00:00Z` through `2026-01-01T00:00:00Z` returned zero posts.
- Direct user timeline probe for `2026-03-01T00:00:00Z` through `2026-03-24T00:00:00Z` also returned zero posts.
- Full-archive search endpoint `/2/tweets/search/all` with OAuth2 user auth returned `Unsupported Authentication`; X says that endpoint requires OAuth2 application-only auth.
- The same full-archive search endpoint with `xurl --auth app` returned `401 Unauthorized`.

Conclusion:

The current `bm_x_posts.csv` remains the verified owner-metric dataset from `2026-03-24` through `2026-06-21`. December 2025 would require working full-archive search access through an app-only credential that X accepts, and even then owner-only metrics may not be available on app-only search responses. Do not backfill December from public-only scraps if the analysis needs impression-normalized owner metrics.

Artifact:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-bm-x-december-reach-probe.md`

Boundary:

Read-only X API probes only. No X post, reply, like, repost, bookmark, follow, DM, account change, CSV rewrite, Drive write, public publish, email, Linear, Notion, Stripe, or deploy happened.
