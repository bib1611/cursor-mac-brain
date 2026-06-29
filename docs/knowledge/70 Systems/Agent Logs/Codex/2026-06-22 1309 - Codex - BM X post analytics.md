# Codex - BM X post analytics

Time: 2026-06-22 13:09 CDT

Built the Biblical Man X post analytics CSV from authenticated `xurl` raw X API v2.

Account:

- `@Biblicalman`
- user id `1759642430649823232`
- note: literal username `thebiblicalman1611` is invalid for X API v2 because it exceeds the 15-character username limit; authenticated `whoami` and `/2/users/by/username/Biblicalman` resolved the live account.

Outputs:

- CSV: `/Users/adamjohnsson/Library/CloudStorage/GoogleDrive-thebiblicalman1611@gmail.com/My Drive/Biblical Man Analytics/bm_x_posts.csv`
- Artifact: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-22-bm-x-post-analytics.md`

Inventory:

- Pulled 873 timeline posts from 2026-03-24T18:30:27Z through 2026-06-21T03:05:27Z.
- Pagination stopped at `empty_page_with_next_token`; the 3200-post cap was not reached.
- Dropped 530 replies-to-others and 0 retweets.
- Kept 343 original/quote-post rows in CSV.
- Owner impressions and profile clicks populated on all pulled posts.
- `url_link_clicks` populated on 167 of 873 pulled posts, and 18 of 343 kept CSV rows; blank where X did not return the field.

Method:

- Dropped pure retweets and replies-to-others.
- Kept originals and quote posts.
- `engagement_rate = (likes + retweets + replies + quotes + bookmarks) / impressions`.
- `link_click_rate = url_link_clicks / impressions`.
- Impressions use owner-visible `organic_metrics.impression_count`, with fallback to `non_public_metrics.impression_count` and then `public_metrics.impression_count`.

Verification:

- CSV parser confirmed 343 rows with columns: `tweet_id`, `created_at`, `text`, `impressions`, `likes`, `retweets`, `replies`, `quotes`, `bookmarks`, `url_link_clicks`, `profile_clicks`, `engagement_rate`, `link_click_rate`.

Boundary:

Read-only X API pulls plus local/Google Drive file writes only. No X post, reply, like, repost, bookmark, follow, DM, account change, public publish, email, Linear, Notion, Stripe, or deploy happened.
