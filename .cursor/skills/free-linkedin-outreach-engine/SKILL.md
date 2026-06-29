---
name: Free Outreach Engine (Origami clone — LinkedIn + Reddit + Email)
description: Use to run Adam's free, self-hosted replacement for origami.chat — find ideal customers from LinkedIn post engagement, Reddit threads, and email; enrich them; draft personalized sequences; and send via Adam's own LinkedIn / Reddit / Gmail for free. Trigger on any lead-gen, cold outreach, prospecting, "find customers", or "send to these people" task.
keywords: ["origami", "linkedin outreach", "reddit outreach", "cold email", "cold outreach", "prospecting", "lead gen", "sequencer", "connection request", "find customers"]
---

# Free LinkedIn Outreach Engine (Origami clone)

This is Adam's free, self-hosted replacement for **origami.chat** (a paid Claude-Code-based
outreach tool that charges to SEND messages). Origami's sourcing + drafting are free; only
sending is paywalled. We reproduce the entire pipeline for $0 using the `linkedin` REPL global
(Adam's own session) + this agent as the engine.

**Adam's LinkedIn:** public id `adam-johnson-9a3826313` (plainId 1336778763). Confirm live with
`linkedin.getMe()` before any run.

## The pipeline (5 stages, all free)

| Stage | Origami (paid) | Our free equivalent |
|---|---|---|
| 1. ICP | website analysis | `WebFetch(site)` + summarize buyer/buying-signals |
| 2. Source | scrape post engagers | browser DOM scrape of post reactions/comments |
| 3. Enrich | name/title/url/comment | `linkedin.getProfile()` + the scraped comment |
| 4. Draft | personalized sequence | this agent writes per Adam's voice rules |
| 5. Send | **paywalled** | `linkedin.sendInvitation` → `linkedin.sendMessage` (free) |

## Voice rules for the messages (Dead Hidden / Biblical Man)
- Reference the person's **specific comment** + the post they engaged with. Fellow-believer to
  fellow-believer, warm not salesy. One idea per message.
- **No em dashes, no hashtags, KJV exact.** No financial figures / subscriber counts (Adam's hard rule).
- Step 1 = **bare connection request, no note** (free LinkedIn drops invite notes; notes are Premium-only).
- Step 2 = short DM, sent ~1 day after they accept. Lead with their words, bridge to the offer.
- Audience is ~60% women — do not write exclusively male second-person.

## Stage 1 — ICP
```js
const rep = await WebFetch(siteUrl); // or read deadhidden.org / thebiblicalman.link
// summarize: target audience, buyer personas, buying signals, exclusions
```

## Stage 2 — Source engagers from high-engagement posts
Pick posts whose engagers match the buying signals (e.g. people commenting on "shallow church
teaching", "seeker-sensitive", "be bold in faith"). Find posts via:
```js
const posts = await linkedin.getUserPosts('some-public-id'); // or search /search/results/content
```
Scrape the engagers (commenters + reactors) by opening the post in a tab and reading the DOM.
The reactions/comments modals expose name, profile URL, headline, and (for comments) the text.
Pattern: open post URL → click the reactions count and the comments → snapshot/`page.evaluate`
to collect `a[href*="/in/"]` anchors + nearby comment text. Dedupe by public identifier.

## Stage 3 — Enrich + score
```js
const p = await linkedin.getProfile('public-id'); // fullName, headline, occupation, experience
```
Fit score = how well headline/title/comment match the ICP buying signals (0-100). Keep >= 75.

## Stage 4 — Draft the sequence
Write one DM per lead using the voice rules above. Personalize the opener from their comment.
Save into the campaign JSON schema (below).

## Stage 5 — Send (THROTTLED, confirmation-gated)
LinkedIn aggressively throttles. Respect the builtin `linkedin` skill's caps:
- `sendInvitation`: **<= 15-25/day, 80/week hard cap, 3-6 min spacing with jitter**.
- Cold `sendMessage`: <= 20-30/day, 3-10 min spacing, never identical bodies.
- On 429: exponential backoff. On 999/403/checkpoint: STOP for hours, do not continue the batch.
- In Aside final-confirm mode: get explicit confirmation before starting a send batch.

Send order: send all connection requests first (drip over days), then poll for accepts and DM only
accepted leads ~1 day later.

```js
// STEP 1 — drip connection requests (bare, no note on free)
for (const l of batchToday) {            // batchToday capped at ~18
  await linkedin.sendInvitation({ identifier: l.public_identifier }); // no customMessage = bare invite
  l.steps.connection_request.status = 'sent';
  await sleep((180 + Math.random()*180) * 1000); // 3-6 min jitter
}

// STEP 2 — later run: who accepted? then DM
const me = await linkedin.getMe();
// check connection by getProfile distance, or track accepted invites,
// then for accepted leads only:
await linkedin.sendMessage({ recipients: [l.public_identifier], text: l.steps.dm.body });
l.steps.dm.status = 'sent';
await sleep((180 + Math.random()*420) * 1000); // 3-10 min jitter
```

Use a heartbeat/cron routine to space the drip across days and to poll for accepts (so you do not
have to babysit). Always update the campaign JSON + regenerate the dashboard after each run.

## Campaign JSON schema
`artifacts/outreach/campaign-<slug>.json`:
```
{ id, name, business, icp_summary, source_posts[], sender, caps,
  leads: [ { id, full_name, title, linkedin_url, public_identifier, comment_text,
             post_topic, fit_score,
             steps: { connection_request:{note,status,sent_at}, dm:{body,status,sent_at} },
             status } ] }
```
Statuses: `idle -> invited -> accepted -> dmed -> replied` (or `skip`).

## The Sequencer dashboard (free Origami UI)
`artifacts/outreach/sequencer.html` — self-contained single file, data embedded, localStorage for
status/edits, Export JSON button. Adam opens it by double-clicking (Aside preview does not run JS).
Regenerate it from the campaign JSON whenever data changes (template lives in session history; it
reads `CAMPAIGN` const + renders list/detail/stats).

## Importing existing Origami work (one-time salvage)
Origami's free-tier data is reachable from its own authenticated tab:
- `GET /api/workspaces/{ws}/tables` -> table ids
- `GET /api/workspaces/{ws}/tables/{tableId}/columns` and `/rows` -> enriched leads + drafted DMs
- `GET /api/context` -> the ICP report
Run these via `origamiTab.evaluate(fetch(..., {credentials:'include'}))`. Map cells by column id.

## Channel 2 — Reddit (free, no login needed to source)
Reddit exposes public JSON on every endpoint (append `.json`). No auth for reads.
```js
// search within target subs (TrueChristian, Reformed, KingJamesBible, Christianity, Bible)
fetch(`https://www.reddit.com/r/${sub}/search.json?q=${q}&restrict_sr=1&sort=relevance&t=year&limit=8`,
  { headers:{ 'User-Agent':'free-sequencer/1.0' } })
// pull commenters from a thread (walk replies recursively for t1 nodes)
fetch(`https://www.reddit.com/r/${sub}/comments/${id}.json?limit=200&depth=4`, {headers})
// each comment: data.author, data.body, data.score
```
Score commenters on ICP signals (shallow/watered-down/depth/discernment/false teaching/sound
doctrine/KJV/repent/warfare). Dedupe by author, require an own-words sentence (skip pure
scripture pastes and one-liners like "Amen!").
**Reddit approach:** soft, value-first. Step 1 DM references their comment + a light question, **NO
link** (Reddit spam-filters cold links hard). Step 2 sends the resource only after they reply.
**Sending** = Reddit chat/DM (free). Needs Reddit login in the browser; there is no `reddit` REPL
global, so drive chat via the browser tab. Cap ~8 DMs/day, 4-8 min apart. Reddit culture is hostile
to cold pitches — keep it human or expect spam-flags/bans.

## Channel 3 — Email (free to send, hard to source addresses)
- **Sending is free** via the `gmail` REPL global (thebiblicalman1611@gmail.com) or Proton.
  `gmail.sendEmail(...)` / compose in the Gmail tab. Confirmation-gated in final-confirm mode.
- **Finding a cold stranger's address is the one genuinely paywalled step** (Apollo/Hunter etc.).
  Free best-effort: LinkedIn contact-info after they accept the connection, public org/staff pages,
  personal sites, GitHub. Leave the address blank in the campaign until found.
- Draft = short personalized email (subject + body) referencing their comment, soft CTA, Adam's
  voice. No em dashes, no figures. Cap cold sends ~20-30/day, vary copy.

## The unified dashboard
`artifacts/outreach/sequencer.html` is a single self-contained file with **three tabs**
(LinkedIn / Reddit / Email), each with its own list, status counts, editable messages, and an
Embedded `DATA = {li, rd, em}` payload + localStorage persistence + Export JSON. Regenerate it
whenever campaign JSONs change. Campaign files: `campaign-church-critique.json` (LI),
`campaign-reddit-depth.json` (RD), `campaign-email-church.json` (EM).

## Safety / ethics
- Automated LinkedIn/Reddit outreach violates each platform's Terms and can get the account
  restricted. Keep volume human (LinkedIn <=18 invites/day, Reddit <=8 DMs/day), vary copy, and
  stop on any checkpoint/rate-limit.
- This is Adam's own accounts and own contacts; never run for third parties.
