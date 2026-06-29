# 2026-06-11 0752 CDT — Hermes — BM post + X article staged for Adam's approval

## What was done

### 1. BM Substack draft — "They Called Your Silence Forgiveness"
- Draft ID: 201590172 — editor URL: https://biblicalman.substack.com/publish/post/201590172
- Verified via drafts API: title, subtitle ("The Bible never commands pretending."), 50 nodes
- Structure: header image (bm-silence-forgiveness-header.png, uploaded as top captionedImage), 39 paragraphs, 5 H2 headings, 3 KJV blockquotes (Matt 18:15, Luke 17:3, Prov 28:13), endcap Share button + Subscribe widget
- Fixes applied this session (PUT /api/v1/drafts/201590172, HTTP 200):
  - Removed duplicate bare subscribeWidget (51 → 50 nodes)
  - Audience changed only_paid → everyone (all 4 cult-lane posts June 9–10 ran free)
- Editor tab reloaded to prevent stale autosave clobber

### 2. X article draft — "the chapter nobody reads is an obituary column"
- Composer URL: https://x.com/compose/articles/edit/2065051263188742144 (draft, NOT published)
- Title set, body 9,679 chars intact, 10 H2 section headers, cover image uploaded (genesis5-cover-5x2.png, X displays at 2.5:1)
- Fix applied this session: all 9 bold key lines restored (paste had stripped them). Method: CDP Emulation.setFocusEmulationEnabled + DOM selection + trusted Cmd+B dispatch per line; verified via computed fontWeight spans
- Only link in body is the @Biblicalman mention (on-platform, allowed)
- "Last saved just now" confirmed in composer

## NOT done (gated on Adam's approval)
- Publish on either surface
- PBM self-reply on X (posts after article goes live)
- Promo tweet 1

## Technique note (reusable)
X article composer (Lexical-style): JS click and execCommand fail. Working recipe: Emulation.setFocusEmulationEnabled(true) → ed.focus() + Range selection on text node → Input.dispatchKeyEvent Cmd+B (modifiers:4) → verify via span computed fontWeight >= 600 (composer does NOT use <strong>). Script: ~/.hermes/scripts/x_bold_lines.py, helper ~/.hermes/scripts/cdp_eval.py

## Telegram
- Approval request sent to Adam (chat 5504141258) at ~0753 CDT
