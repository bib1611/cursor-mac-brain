# 2026-06-12 10:21 CDT - Codex - Kickbacks count Bible ad test staged

Adam asked to get the Kickbacks opportunity going after reviewing the Charlie Holtz / Conductor bid screenshot.

Codex treated this as a controlled advertiser test, not an installation of the Kickbacks extension into the main Hermes/Codex/Claude stack.

Prepared campaign:

- Offer: `How to Count Your Bible`
- Live page: `https://deadhidden.org/store/how-to-count-your-bible`
- Tracked URL: `https://deadhidden.org/store/how-to-count-your-bible?utm_source=kickbacks&utm_medium=spinner&utm_campaign=count_bible_devtest&utm_content=read_bible_like_source_code`
- Ad line: `Read the Bible like source code`
- Brand: `Dead Hidden`
- Recommended bid: `$12.01` per 1,000 impressions
- Recommended blocks: `4`
- Estimated total: `$48.04`
- Icon prepared: `/Users/adamjohnsson/Documents/Codex/2026-06-12/fix-hermes-desktop-agent-init-failed/outputs/kickbacks-dead-hidden-icon.png`
- User-facing packet: `/Users/adamjohnsson/Documents/Codex/2026-06-12/fix-hermes-desktop-agent-init-failed/outputs/kickbacks-count-bible-campaign.md`
- Ops artifact: `/Users/adamjohnsson/.deadhidden-os/ops/artifacts/2026-06-12-kickbacks-ad-test/PLAN.md`

Verification:

- Dead Hidden landing page returned HTTP 200.
- Tracked UTM URL returned HTTP 200.
- Kickbacks buy form permits 3-60 char ad lines, HTTPS destination URL, optional brand, optional icon, minimum `$1.00` bid, and 1-100 blocks.
- Kickbacks leaderboard around 2026-06-12 10:20 CDT showed top visible bids from `$20.00` down to `$10.01` in the top-10 rotation; `$12.01` should sit inside live rotation if the market does not move.

Boundary:

- No Kickbacks checkout was created.
- No payment was made.
- No ad was submitted.
- No public post was made.
- No Kickbacks extension was installed.
- No Hermes/Codex/Claude runtime was patched.
- Next step requires Adam approval of the exact spend and copy.
