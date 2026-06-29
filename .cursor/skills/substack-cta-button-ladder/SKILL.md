---
name: Substack CTA Button Ladder (Biblical Man / Dead Hidden)
description: Use when drafting, editing, or placing call-to-action buttons in any Biblical Man or Dead Hidden Substack post or Note (subscribe, share/restack, free-to-paid, or product CTAs to Gumroad/deadhidden.org). Apply this button-ladder method to maximize conversion. Adapted from Kristina God's Substack button method (mechanics only, never her voice).
autoInject:
  keywords:
    - CTA button
    - Substack button
    - button ladder
    - call to action
    - subscribe button
    - Burn Off The Fog
    - conversion button
  url:
    - biblicalman.substack.com/publish
    - deadhidden.substack.com/publish
    - substack.com/publish
---
# Substack CTA Button Ladder (Biblical Man / Dead Hidden)

Treat every button as a one-line sales pitch, not a label. Adapted from Kristina God (The Online Writing Club). Steal the **mechanics**, never her voice. Pair with **Biblical Man / Dead Hidden Voice**, **Substack Direct Response Brain** (post mode + peak-tension placement), and **Matched-Pair Launch Workflow**.

## Core principles
1. **A button is a promise, not a verb.** Never ship a bare "Subscribe." The text states what the reader gets or the inner "yes" they are saying.
2. **Write button text in the reader's first person** ("Hand me the map," "I'm starting tonight," "Show me how"). The button is the reader's decision, not your command.
3. **Caption above every button.** One short lead-in line sits directly above each button to set up the click. Buttons never float alone.
4. **Multiple buttons, not one.** 3-4 per post. Substack auto-hides the subscribe widget for people who already acted, so repetition costs nothing.
5. **One job per button.** Each button = exactly one goal (grow list / sell / engage / share). Never two competing asks in one button.

## The "one ask" rule still holds
BM/DH essays keep **one offer per piece**. The ladder does NOT mean multiple products. It means the SAME product CTA repeated (mid + end) plus a subscribe and a share button. Never pit two products against each other in one post. This matches the Matched-Pair "two-CTA structure" (primary mid-post after peak tension + repeat at close).

## The ladder (standard essay)
- **~20% in (soft / list):** preset **Subscribe** button. For the 25K free list this auto-shows "Upgrade to paid" to free subs and a checkmark to paid, so it doubles as the paid nudge.
- **~55% in (mid / the ask):** **Custom** button to the product, placed right after the strongest emotional/peak-tension line.
- **~90% (hard / the ask again):** **Custom** button to the SAME product, after the close.
- **End (reach):** preset **Share** or restack button.

## Hard constraints (BM/DH)
- **No price or dollar figures on buttons or in body.** Convey urgency by tone only. Price lives on the Gumroad/store page. (Adam + Christie have poverty PTSD around money figures.)
- **Women-inclusive.** ~60% of the audience is women. No exclusively male second-person button copy.
- **No em dashes. No hashtags.** Periods and commas only.
- **One offer per piece.**

## Copy levers (apply to button text)
- Concrete benefit + what they get ("Send Me the Daily Word").
- Reader-voice / personal ("I'm done quitting in Genesis").
- Specific over generic (never "Click to learn more").
- Light urgency through verbs/tone, never price ("Start Me Tonight").

## Swipe file (edit per post; do not ship stale)
- **Grow free list (Subscribe):** "Send Me the Daily Word" / "Put It in My Inbox Every Morning" / "Join the House. It's Free."
- **Free-to-paid:** "Hold the Door Open for the Next Reader" / "Stand With the House" / "Keep These Coming."
- **Sell product (custom, the single ask):** "Hand Me the Map" / "Burn Off the Fog" / "Show Me How to Read It Myself" / "I'm Starting Tonight. Send It."
- **Engage (comment):** "Tell Me Where You Quit. I'll Answer Every One." / "What Verse Lost You? Drop It Below."
- **Reach (share/restack):** "Put This in a Brother or Sister's Hands" / "Send This to Someone Still Sitting in the Pew Afraid."

## How to insert in the Substack editor (durable mechanic)
- External/store buttons must be **Custom** buttons: Toolbar -> **Button** dropdown -> **"Custom..."** -> fill Text + URL -> OK. Preset Subscribe/Share cannot point to external URLs.
- Use preset **Subscribe** and **Share** options for those two jobs.
- Caption line = the paragraph typed directly above the button.
- After inserting a button, refs go stale: click the empty area below the rendered button and re-snapshot before typing the next line.
- Dialog/button ref IDs change every snapshot. Re-snapshot before each click.

## Custom-button gotchas (confirmed 2026-06-26, cost an hour)
- **Button text has a SHORT character limit.** ~16-20 chars insert fine; ~45 chars is rejected SILENTLY (the prompt submit returns early, dialog stays open, no error shown). Keep labels short (aim <= ~22 chars). Put the long reader-voice promise in the CAPTION line above the button, not on the button. ("Hand Me the Map. I'm Done Quitting in Genesis." failed; "Burn Off The Fog" worked.)
- **Do NOT press Tab to move from the Text field to the URL field.** Tab inserts a literal tab character into the URL (leading \t), which fails URL validation and silently blocks submit. Click the URL field directly instead.
- The Custom dialog is a React-controlled ProseMirror prompt. Fill it with **real keystrokes** (keyboard.type after clicking the field) or Playwright fill(); setting input.value via the native DOM setter alone does NOT update React state, so submit fails.
- If OK does nothing / dialog will not close: the cause is almost always (1) label too long or (2) a tab in the URL. Shorten the label and re-check the URL has no leading whitespace.
- The rendered button is an orange pill. Verify after insert by checking the ProseMirror anchors include your target href.

## Notes (single-CTA) variant
A Substack Note gets 4-6 punchy lines then ONE bare product URL at the end (Notes do not render custom buttons the same way). Keep the reader-voice promise in the final line before the link.

## Source
Mechanics decoded from Kristina God (@kristinagod, The Online Writing Club) YouTube "Ultimate Guide to Substack Buttons" + her public Notes, plus live observation of her posts (e.g. a mid-post custom button reading "This is my moment!"). Voice/wording is original BM/DH, never hers (hard ethics rule).
