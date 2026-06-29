# Bible Source Code — gematria English-input fix + OG image
2026-06-12 16:24 CDT — Hermes

## Shipped (commit 6830344, deploy dpl_HM4DdeGyDHuGnER6QfQhfjo81n8c, READY, aliased bible-source-code.vercel.app)
1. **Gematria English bridge** — NAME_MAP in parser.js: 10 biblical names mapped to ATTESTED Greek/Hebrew spellings only (Jesus→ΙΗΣΟΥΣ 888, Christ→ΧΡΙΣΤΟΣ 1480, Messiah→משיח 358, Emmanuel→ΕΜΜΑΝΟΥΗΛ 644, Amen→ΑΜΗΝ 99, Adam/Eve/Noah/David). No free transliteration — guardrail intact. Unknown English ("Bob", "birthday") gets explainer message instead of dead zero. Dates still rejected.
2. **Preset chips relabeled** — first chip now "See why Jesus = 888", chips send English names through the same map.
3. **OG image** — assets/og.png 1200×630 generated (PIL): dark/oxblood, title + Genesis 5:27 terminal panel "187+182+600 = 969 MATCH", tagline "counting, not conjuring". og:image/og:url/twitter:card meta added.

## Verified live (this session)
- og.png 200 (43KB) on prod URL; meta tags present in served HTML
- Real Chrome CDP test on LIVE prod: typed "Jesus" → "Jesus, as written in the Greek New Testament: ΙΗΣΟΥΣ" + "= 888"; "birthday" → explainer, total empty; chip tap → 888, 6 per-letter spans. Tab closed after.
- Headless parser test: 9/9 cases correct incl. case-insensitivity and date rejection.

## For the Note
- Mobile screenshot of lit-up Genesis 5: ~/Desktop/bible-source-code-note.png
- Note copy drafted, awaiting Adam GO (public post = approval gate)

## v2 still open
custom domain code.deadhidden.org (DNS, needs approval), real email capture.
