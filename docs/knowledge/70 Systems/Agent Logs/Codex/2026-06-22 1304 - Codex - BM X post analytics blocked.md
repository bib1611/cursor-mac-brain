# Codex - BM X post analytics blocked

Time: 2026-06-22 13:04 CDT

Attempted Step 1 for Adam's X post analytics pull through authenticated `xurl`.

Result:

- `xurl whoami` worked and returned authenticated account `@Biblicalman`, user id `1759642430649823232`.
- Required raw API inventory calls failed before pagination:
  - `GET /2/users/by/username/thebiblicalman1611?...` returned `CreditsDepleted`.
  - `GET /2/users/1759642430649823232/tweets?...tweet.fields=created_at,public_metrics,organic_metrics,non_public_metrics,referenced_tweets` returned `CreditsDepleted`.
- `xurl user`, `xurl read`, `xurl timeline`, and `xurl search` also returned `CreditsDepleted`.
- OAuth1/app checks returned `Unauthorized` for the username endpoint.

No post inventory was pulled, no metric field population could be tested, and no `bm_x_posts.csv` was created. Owner-only metrics such as impressions, URL link clicks, and profile clicks are unavailable in this run, not zero.

Artifact:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-bm-x-post-analytics-blocked.md`

Boundary:

Read-only xurl checks only. No X post, reply, like, repost, bookmark, follow, DM, account change, CSV write, Drive write, public publish, email, Linear, Notion, Stripe, or deploy happened.
