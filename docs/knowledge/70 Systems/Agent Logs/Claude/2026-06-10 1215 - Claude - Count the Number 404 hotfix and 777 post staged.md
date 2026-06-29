# 2026-06-10 1215 — Claude — Count the Number 404 hotfix + 777 post staged in editor

## 1. LIVE CUSTOMER FIX: Count the Number 404 (deployed + verified)

Problem: "God Told You to Count" went out 2026-06-10 07:40 CDT with buttons linking
`deadhidden.org/store/count-the-number` — the product was staged locally but never
deployed. Codex handoff (07:38, `count-the-number-launch-handoff.md`) explicitly said
"Do not publish the Substack post until the production product route is deployed and
verified." Post published anyway. Every reader who clicked got a 404. Reader report
confirmed it.

Fix shipped:
- Hotfix built on clean `origin/main` (NOT the diverged `dea-phase4-instrumentation`
  branch — that branch is 28 behind / 9 ahead with a 298-line products.ts diff).
- Commit `91fff8d` pushed to `main`: product entry + `count-the-number.pdf` only.
- Fixed 3x "Biblical Man" brand slips in the product entry → "Dead Hidden"
  (description, longDescription, FAQ). Same slips fixed in the manuscript
  (`~/Documents/Codex/2026-06-10/i-was-working-on-having-you/outputs/count-the-number-manuscript.md`)
  and PDF re-rendered via Codex's `render_count_the_number_pdf.py`. Byline verified
  "By Adam Johnson" (single s). 9 pages.
- Same 3 slips also fixed in the main repo working tree products.ts so a future merge
  doesn't regress.
- Vercel auto-deployed from the push.

Verified live:
- `https://deadhidden.org/store/count-the-number` → 200
- `https://deadhidden.org/product-files/count-the-number.pdf` → 200
- `https://deadhidden.org/checkout?slug=count-the-number` → 303 to live Stripe
  checkout session (cs_live_...)

Open policy question for Adam: The Vault ($365) sells as "every PDF, guide, framework,
protocol, and manual." Count the Number is not in it. Either new guides roll into the
Vault or the "every" claim needs softening.

Reader reply drafted (copy-box, awaiting Adam send) — link fixed, guide is separate
$10, not in Vault.

## 2. 777 PAID POST: staged in Comet Substack editor

- Draft ID: 201483631 — `https://deadhidden.substack.com/publish/post/201483631`
- Title: "Noah's Father Died at 777" / audience: only_paid
- Created via Substack drafts API inside authenticated Comet tab (CDP 9223), using
  node schema copied from the morning post's draft JSON (button/captionedImage/paywall).
- Image IMG_3121.JPG (672x1200) uploaded to Substack CDN, placed at top.
- 4 KJV blockquotes (Gen 5:31, Gen 4:24, Matt 18:22, Psalm 147:4).
- Paywall divider verified directly after the cliff line "And he is not the only one."
- ONE CTA button (per research: single CTA ≈ +371% clicks vs multi): value line +
  "Get Count the Number - $10" → store URL utm_campaign=777_post, placed after thesis
  peak ("the numbers were always His"), before the closing Lamech beat so the final
  question stays clean.
- Anti-slop edit applied: cut "That number is not random." (negative-parallelism
  density — the #1 flagged AI tell; kept the two flips that earn it).
- Rendering verified by CDP screenshot: image, blockquotes, button, paywall all
  present. 636 words. Status: Saved. NOT published — Adam approval required.

## 3. Research artifacts (agents, completed)

- Substack CTA/formatting: single primary CTA; contextual button copy; value line
  above button; paywall after value delivery (only real tested data:
  ditchthetemplates.substack.com paywall tests); Gmail 102KB clip = CTA in top half;
  native buttons > image buttons; YouTube has no real button tests — tutorials only.
- Writing in the age of AI: 12-tell slop checklist (negative parallelism, em-dash
  chains, triplets, uniform paragraph variance, frictionless transitions, verb
  inflation, puffery, vague attribution, both-sidesing, therapist tone, trailing
  -ing analysis, tidy bow endings) + human signals (named specifics, stakes,
  confession with cost, irregular rhythm, commit don't balance). Key warning: Adam's
  staccato style is itself now a mimicked AI pattern — named specifics and confession
  are his real differentiators. Sources: Wikipedia Signs of AI Writing, Paul Graham
  "Writes and Write-Nots", George Saunders.

## Files touched
- github.com/bib1611/deadhidden main @ 91fff8d (products.ts + count-the-number.pdf)
- /Users/adamjohnsson/code/deadhidden/src/data/products.ts (brand slips, uncommitted)
- /Users/adamjohnsson/code/deadhidden/public/product-files/count-the-number.pdf (re-rendered)
- Codex manuscript + outputs PDF (brand fix)
- Substack draft 201483631 (created)
