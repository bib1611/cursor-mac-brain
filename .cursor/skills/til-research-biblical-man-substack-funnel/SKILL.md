---
name: TIL Research → Biblical Man Substack Funnel
description: Use when Adam wants Substack (or matched-pair) content sourced from
  viral r/TodayILearned and r/InterestingAsFuck facts, adapted into Biblical Man
  or Dead Hidden voice and funneled to Gumroad. Covers old.reddit.com browser
  research, fact selection, voice guardrails (never mention Reddit/Wade/upvotes
  in public copy), CTA button ladder, and X hook + self-reply posting. Trigger
  on Reddit TIL funnel, cold knowledge post, seven lies style essay, or
  Wade-style research without naming the method publicly.
siteSpecific: true
autoInject:
  keywords:
    - Reddit TIL
    - TodayILearned
    - seven lies
    - Substack funnel
    - cold knowledge
    - Plain Bible
    - Gumroad CTA
    - old reddit research
  url:
    - old.reddit.com/r/todayilearned/**
    - biblicalman.substack.com/p/**
    - x.com/Biblicalman/**
---
# TIL Research → Biblical Man Substack Funnel

Turn high-engagement **facts people already argue about** into a **Biblical Man** (or **Dead Hidden**) Substack essay that funnels to **one Gumroad product**. Pair with **Biblical Man / Dead Hidden Voice**, **Substack CTA Button Ladder**, and **Matched-Pair Launch Workflow** when shipping a full launch unit.

## What this skill is (and is not)

- **Is:** Research discipline + selection criteria + conversion structure. Facts can come from r/TodayILearned, r/InterestingAsFuck, history/science/translation/Bible-adjacent TILs that explain *why readers quit or distrust the text*.
- **Is not:** Copying Wade Zone, Kristina God, or Dakota Robertson **voice**. Never ship meta copy (“Reddit said…”, “this TIL had 45k upvotes”, “here’s the content loop I used”, “Wade’s 7 steps”).
- **Adam’s rule:** Use your **writing brain**. Research is backstage. The published piece reads like confession, fog, and KJV receipts, not growth-hack confession.

## Default product (unless Adam names another)

- **Plain Bible 2.0:** `https://biblicalman.gumroad.com/l/plain-bible-2`
- **CAGED (DH angle):** `https://biblicalman.gumroad.com/l/laaexc` — only when the seven angles match that book; **one offer per piece**.

No dollar amounts in public BM/DH copy.

## Phase 1 — Reddit research (reliable path)

### Do not rely on

- `webfetch` / JSON to `www.reddit.com` → often **403**.
- Broad claims without opening threads.

### Do use

1. **Browser:** `openTab('https://old.reddit.com/r/todayilearned/search?q=<keyword>&restrict_sr=on&sort=top&t=all')`
2. **Keywords to rotate:** `bible`, `scripture`, `ten commandments`, `king james`, `church history`, `translation`, plus non-Bible TILs that **parallel reader fog** (misprints, Jefferson Bible, forbidden fruit apple, etc.).
3. **Second sub:** `old.reddit.com/r/interestingasfuck/search?q=...` for archaeology/history hooks when Adam wants visual/heavier curiosity.
4. **Extract from snapshot:** post title (must start with TIL on TIL sub), score/comments if visible, **permalink** for agent notes only.
5. **Open 3–7 top threads** in separate tabs; read top comment corrections (Hebrew *re’em*, Job vs Genesis order, etc.) for **accuracy in Adam’s prose**, not for quoting Reddit in the post.

### Selection criteria (pick ~7)

- Facts that **invalidate something the reader already “knows”** (apple, Magdalene prostitute, unicorn English, Genesis = oldest book).
- Facts that **justify needing a guide** (stained glass for illiterate households → help was always part of the design).
- Facts that **mirror misquote fear** (Wicked Bible missing *not*) without pastor/church bashing.
- **Avoid** in BM/DH: politics soapboxing, recent (&lt;2 month) TIL on TIL sub, conspiracy end-times threads as the spine.

### Agent-only research log (optional file)

Save under session `artifacts/` or `tmp/`:

- Thread URL, one-line fact, verification note (Wikipedia/Guardian link from post body if present).

**Never paste this log into Substack.**

## Phase 2 — Transform facts into Adam’s essay

### Title patterns (BM)

- Direct challenge: **“Seven Lies You Inhaled Before You Ever Opened the Book”**
- Or: **“Seven Things That Made You Close the Cover”** (no “TIL”, no “Reddit”)

### Structure

1. **Open:** You did not quit because you hate God. Fog from pictures, punchlines, misquotes — stupid by Leviticus, done by the hard stories.
2. **Seven sections:** Each = **one fact → what culture did with it → what the text actually forces → one KJV quote when it fits** (exact KJV).
3. **Tone:** Paragraphs that breathe. Not island-line spam. No em dashes. No hashtags. Women-inclusive where second person appears (~60% women audience).
4. **Mid subscribe (~20%):** After peak tension (often #3 or #4). Caption + Subscribe button per **Substack CTA Button Ladder**.
5. **Mid product (~55%):** After #6 or strongest “you need a map” beat. Custom button short label (≤22 chars): **Burn Off The Fog** → Gumroad URL.
6. **Close:** Acts 8:31 guide permission. Plain Bible 2.0 one sentence. Repeat custom button **I'm Starting Tonight**. Share button. P.S. reply with number 1–7.

### Hard guardrails (public copy)

| Never ship | Ship instead |
|------------|----------------|
| “I pulled this from Reddit / r/TIL” | “Nobody told you…” / “You were handed page one…” |
| Upvote counts, Wade, 7-step loop | Concrete household scene + fog |
| “Content formula”, “growth hack” | Spiritual diagnosis |
| Pastor/church as antagonist | Text vs culture vs misquote |
| Financial figures | Tone-only urgency |

Run **hostile-editor** pass + AI-tell gate before calling draft final.

## Phase 3 — Substack editor mechanics

See **Substack CTA Button Ladder** skill: Custom buttons for external URLs, short button text, caption above button, no Tab into URL field.

Canonical post URL for sharing: `https://biblicalman.substack.com/p/<slug>` (prefer over long `open.substack.com` tracking URLs on X).

## Phase 4 — X (x-twitter skill)

Read `skills/builtin/x-twitter/SKILL.md`. **Do not put the Substack link in the hook tweet.**

### Pattern

**Tweet 1 (hook):** 2–4 short paragraphs. Pull from essay opening + promise (“seven lies… I named them”). No link.

**Tweet 2 (self-reply):** Canonical Substack URL + engagement ask (reply 1–7 on the **post**, not on X if Adam prefers Substack comments).

**Optional Tweet 3 (self-reply):** Gumroad URL only if Adam wants product in thread; else keep product on Substack ladder only.

### Posting gotchas (Aside memory)

- `twitter.reply()` may throw “succeeded but failed to parse” while **not** posting — verify with `getTweet` reply count or browser composer.
- Grammarly + X: use **synthetic ClipboardEvent paste** if keyboard.type scrambles text.
- **Final confirm** before any live post.

### Draft delivery to Adam

Plain text in chat (not only `x-tweet-draft` blocks — Adam may not see special cards). Label: Tweet 1 / Self-reply 1.

## Phase 5 — Optional matched pair

If Adam wants full launch unit (Matched-Pair skill):

- BM essay (this skill)
- DH fringe angle on **same theme** (different hook, same product URL)
- X thread 1/–7/ shortened from the seven sections
- BM Substack Note: 4–6 lines + bare Gumroad URL at end

## Workflow checklist

1. Confirm product URL + slug.
2. Reddit research via **old.reddit.com** (browser).
3. Pick 7 facts; verify disputed points in thread comments.
4. Draft essay in **Voice** skill; **zero** meta about research source.
5. Insert CTA ladder (Subscribe / Custom / Custom / Share).
6. Hostile-editor + no church-bashing + no money figures.
7. Draft X hook + self-reply with canonical Substack URL.
8. Adam approves → post via `twitter.tweet` + `twitter.reply` or browser fallback.

## When Adam says “try again”

Usually means: **remove AI/meta framing** (Reddit formula, Wade, upvotes) and **rewrite in Adam’s confessional fog voice** while keeping the same researched facts.

## Related skills

- `biblical-man-dead-hidden-voice` — all prose
- `substack-cta-button-ladder` — buttons
- `matched-pair-launch-workflow` — four-asset launch
- `x-twitter` — API posting
- `gumroad-dead-hidden-store-ops` — product URL verification
