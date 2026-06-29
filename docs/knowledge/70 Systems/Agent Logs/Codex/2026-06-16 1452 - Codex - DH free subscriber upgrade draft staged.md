---
type: agent-log
date: 2026-06-16
agent: Codex
topic: DH free subscriber upgrade draft staged
tags: [codex, operator, dead-hidden, substack]
---

# DH Free Subscriber Upgrade Draft Staged

## Goal

Stage the Dead Hidden upgrade email as a saved Substack draft only, through Comet CDP `127.0.0.1:9223`, with Dead Hidden identity verified before writing and the email audience set to free subscribers only.

## What I Checked

- Comet CDP `127.0.0.1:9223` was live.
- Dead Hidden Substack identity was verified before write:
  - user/name: Dead Hidden
  - uid: `218038831`
  - publication: Dead Hidden / `deadhidden`
  - publication role: admin
- Subscribe URL resolved:
  - `https://deadhidden.substack.com/subscribe?r=2t2o3r`
  - HTTP `200`
  - title: `Subscribe to Dead Hidden`
  - redirects: `0`

## What I Did

- Created draft via authenticated Substack API from the Comet session.
- Title:
  - `Most of it, you haven’t seen yet.`
- Body matched the requested text and did not include `Here is the honest part.`
- The visible upgrade line is stored as a real link mark to the subscribe URL:
  - `Upgrade to paid: https://deadhidden.substack.com/subscribe?r=2t2o3r`
- Set draft `audience` to `only_free`.

## Proof

- Draft post id: `202336734`
- Edit URL: `https://deadhidden.substack.com/publish/post/202336734`
- API read-back:
  - `audience`: `only_free`
  - `type`: `newsletter`
  - `is_published`: `false`
  - `email_sent_at`: `null`
  - `post_date`: `null`
  - `postSchedules`: `[]`
  - `should_send_email`: `true`
  - `should_send_free_preview`: `false`
  - `free_unlock_required`: `false`
  - `meter_type`: `none`
- Chrome `9222` was not touched after the routing correction.
- Comet was not restarted.

## Files / URLs / IDs

- Draft: `202336734`
- Edit URL: `https://deadhidden.substack.com/publish/post/202336734`
- Subscribe URL: `https://deadhidden.substack.com/subscribe?r=2t2o3r`

## Follow-Up

When ready to send, verify the publish/send modal still shows the free subscriber audience before sending. The saved draft itself currently stores `audience: only_free`.

## Reconciliation

Later reconciliation found Comet's open editor tab on a different blank draft:

- Blank stray draft: `202336788`
- Stray state before deletion:
  - title: empty
  - audience: `only_paid`
  - body: one empty paragraph
  - `is_published`: `false`
  - `email_sent_at`: `null`
- Action: deleted `202336788` via `DELETE /api/v1/drafts/202336788`
- Deletion proof: direct read-back of `202336788` returned `404` / `Draft not found`
- Canonical draft kept: `202336734`
- Comet editor tab was navigated to `https://deadhidden.substack.com/publish/post/202336734`
- Editor proof: page title became `Editing "Most of it, you haven’t seen yet." - Substack`, title field contained the exact title, and body contained `You opened Dead Hidden for free.`
