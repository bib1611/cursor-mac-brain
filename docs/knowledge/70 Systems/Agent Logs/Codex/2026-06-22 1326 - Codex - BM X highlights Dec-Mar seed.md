# Codex - BM X Highlights Dec-Mar Seed

Captured: 2026-06-22 13:26 CDT

Read-only investigation of Adam's X Highlights tab for `@Biblicalman` after the authenticated v2 timeline stopped at 2026-03-24 and full-archive search was blocked.

Output CSV:

`/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Biblical Man Analytics/bm_x_highlights_dec_mar_seed.csv`

Result:

- Saved 17 highlighted March posts verified by direct v2 ID lookup.
- Top seed by impressions: 2026-03-17, tweet `2034045161592815675`, 1,128,457 impressions.
- This is a partial Highlights seed, not the full Dec-Mar timeline.
- X v2 returned `public_metrics.impression_count` by ID, but rejected old `organic_metrics` and `non_public_metrics` fields for tweets older than 30 days.
- Therefore `url_link_clicks`, `profile_clicks`, and `link_click_rate` are unavailable here, not zero.
- Full Dec-Mar inventory still requires working X app-only full-archive auth. `xurl auth status` showed no bearer configured on the `biblicalman` app, and `xurl --app biblicalman --auth app /2/tweets/search/all?...` returned `401 Unauthorized`.

Artifact:

`/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-bm-x-highlights-dec-mar-seed.md`

Boundary:

Read-only browser/X/API checks plus local/Google Drive CSV write only. No X post/reply/like/repost/bookmark/follow/DM/account change, public publish, email, Stripe, Linear, Notion, deploy, credential print, or account-setting change happened.
