# Codex - Disclosure Day CTA Repair

Generated: 2026-06-11 14:01 CDT

## Scope

Adam asked for the Dead Hidden Substack draft `The Bible Already Had a Disclosure Day` to be re-edited with missing conversion CTA buttons. Boundary was editor-only: do not publish.

## Draft

- Publication: Dead Hidden
- Draft ID: `201607195`
- Editor URL: `https://deadhidden.substack.com/publish/post/201607195`
- Title verified in editor: `The Bible Already Had a Disclosure Day`
- Subtitle verified in editor: `Spielberg's aliens land in theaters tomorrow. Scripture filed its report first. Genesis 6 was the press conference.`

## Edit Applied

Codex kept Hermes/Fable locked down and made the controlled edit directly through the authenticated Comet/Substack draft API.

Added native Substack product CTA nodes:

1. `GET THE STRONG DELUSION - $9`
   - `https://deadhidden.org/checkout?slug=the-strong-delusion&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=disclosure_day&utm_content=strong_delusion_midpost`
   - Placement: immediately after `That is not science fiction. That is 2 Thessalonians with special effects.`

2. `OPEN THE DEAD HIDDEN VAULT`
   - `https://deadhidden.org/checkout?slug=the-vault&utm_source=deadhidden_substack&utm_medium=post&utm_campaign=disclosure_day&utm_content=vault_endcap`
   - Placement: end CTA stack before the Plain Bible Manual CTA.

Existing CTA nodes preserved:

- `Share this post`
- `GET THE PLAIN BIBLE MANUAL`
- `SUBSCRIBE TO DEAD HIDDEN`

## Verification

Live editor verification:

- Editor state: `Saved`
- Native button nodes: `5`
- Original uploaded image node preserved: yes
- Raw URLs visible in body text: false
- Strong Delusion copy present: true
- Vault copy present: true
- Continue visible: true
- Publish visible on editor body scan: false

Draft API verification after edit:

- `is_published`: false
- `email_sent_at`: null
- `post_date`: null
- `audience`: `everyone`

## Boundary

No publish, schedule, send, email, Substack Note, X post, Stripe mutation, checkout mutation, Hermes unfreeze, Fable run, or launch-agent restart was performed.
