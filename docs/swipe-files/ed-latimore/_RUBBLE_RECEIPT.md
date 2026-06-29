# Rubble Receipt - Ed Latimore Corpus Parts

- Captured: 2026-06-20 18:44 CDT
- Scope: TWEETS + BLOG raw parts only for Skye final combine/upload.
- Output root: `/Users/adamjohnsson/Downloads/ed-latimore-corpus/`
- Boundary: no combine, no zip, no Drive upload, no public post, no external account mutation.

## Tweets

- Requested source: `@EdLatimore` via `/Users/adamjohnsson/go/bin/xurl`
- Resolved user id: `459692778`
- Tweet artifacts produced: 0
- `tweets/` status: empty
- Blocker: X API returned `CreditsDepleted` for account `1774150447294500864`.
- Details: the timeline pull reached 1,096 tweets in memory during pagination, then the API credit error fired before `_tweets_raw.json` or `_tweets_top.md` were written. A follow-up sample timeline request immediately returned the same `CreditsDepleted` error. `xurl auth apps list` showed only the `biblicalman` app; `--auth app` and `--auth oauth1` returned `Unauthorized`.

## Blog

- Source index: `https://edlatimore.com/articles`
- Sitemap cross-check: `https://edlatimore.com/sitemap.xml`
- Article URLs indexed: 228
- Article markdown files written: 228
- Failed article URLs: 0
- Index file: `/Users/adamjohnsson/Downloads/ed-latimore-corpus/blog/_blog_index.json`
- Summary file: `/Users/adamjohnsson/Downloads/ed-latimore-corpus/blog/_blog_capture_summary.json`
- Capture format: one clean markdown file per article in `/Users/adamjohnsson/Downloads/ed-latimore-corpus/blog/`, with title, source URL, date, capture note, length, and full body markdown.

## Failed URLs

None for blog.

## Handoff

Skye can combine/upload the blog half now. The tweet half needs fresh X API credits or another configured `xurl` app before `_tweets_raw.json` and `_tweets_top.md` can be produced.
