# 2026-06-20 — Skye (Claude Code) — Ed Latimore corpus build + Drive handoff

Adam asked to replicate the Dakota Robertson corpus for Ed Latimore (@EdLatimore, edlatimore.com): get his tweets, funnels, blogs, and emails into one file. Orchestrated across the CNVS canvas with Chase (Grok) and Rubble (Codex).

## Deliverable (the one file)
- `Ed-Latimore-Corpus-Combined.md` — 4,116,901 bytes (tweets deepened 2026-06-20)
- Mirror archive: `ed-latimore-corpus.zip` — 3,227,447 bytes
- Drive: `My Drive/Masterclass-Archive/Writing-Brain/Ed-Latimore/`
  - folder id `16fRy8jyNN-_L_zwWHSgsv-fMqJ0HJr8p`
  - Combined.md id `1NEgtOM57G8-QKO7NH_qwcdh0GwnxR2Yo`
  - zip id `1JkGaG-pwnhu--cycjllLCYa1YYsC4RFA`
- Local staging: `/Users/adamjohnsson/Downloads/ed-latimore-corpus/`

## Contents
- **Blog:** 228 articles from edlatimore.com (Rubble/Codex, 0 failures) — this is his real long-form essay corpus.
- **Funnels:** 3 sales/persuasion pages — /book (Hard Lessons From The Hurt Business), /products (3 books, Amazon), /speaking — plus _funnels_index.json (Chase/Grok).
- **Newsletter/emails:** archive is GATED (ConvertKit, emails.edlatimore.com, no public archive/sitemap). Captured the opt-in landing copy + 4 public sampler issues + a NOTE (Chase/Grok).
- **Tweets:** 458 original posts scraped via Chrome CDP off x.com/EdLatimore (GraphQL timeline interception — full metrics incl. views/likes/RT/replies), sorted by impressions, Dakota header format (`tweets/_tweets_top.md` + `_tweets_raw.json`). Range 2018→2026, 446 with view counts, top post 5.97M views. Plus `tweets/_grok_backup_top.md` — the original 33 Grok live-X captures kept as supplemental for older year-end posts the profile timeline no longer surfaces. Scraper: `_scrape_tweets.py`.

## Known gaps / honest notes
- **Tweets RESOLVED (2026-06-20): now 458 posts.** Original pull was thin (32) because xurl hit `CreditsDepleted` (the `biblicalman` X API app is the only one configured and is out of credits). Fixed by Chrome CDP scrape of x.com/EdLatimore — `_scrape_tweets.py` opens a throwaway tab, intercepts UserTweets GraphQL responses (which carry view counts for other users' tweets), and scrolls to paginate. KEY GOTCHA: a background CDP tab freezes X's infinite scroll (IntersectionObserver doesn't fire), so the script sets `Emulation.setFocusEmulationEnabled` + `setDeviceMetricsOverride` + `Page.setWebLifecycleState=active` to keep it rendered. Timeline is recent-weighted (438 of 458 from 2026); deeper history would need year-by-year X search. To refresh: `python3 _scrape_tweets.py` then `python3 _combine.py` then re-copy to Drive.
- Newsletter email bodies are subscriber-gated; only public samplers captured. His blog covers the same essay material.
- Blog count 228 (sitemap listed ~280 incl. non-article pages; Rubble cross-checked and filtered to articles).

## How to rebuild
`cd ~/Downloads/ed-latimore-corpus && python3 _combine.py` then copy `Ed-Latimore-Corpus-Combined.md` + re-zip into the Drive `Ed-Latimore` folder (local path writable; Drive File Stream syncs).

## Boundary
Read-only public scraping (X via Grok, edlatimore.com via Codex/Grok), local staging in ~/Downloads, Google Drive folder + file upload, and this receipt only. No publishing, no Stripe/customer/money mutation, no email sent, no social post, no deploy, no credential/account change.
