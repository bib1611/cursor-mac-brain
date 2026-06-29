# Free-tool email capture — production deploy (Brief 3)

**When:** 2026-06-12 18:18 CDT
**Approval:** Adam said GO same-thread.

## Deployed
- Repo: ~/code/bible-source-code, commit 2f4f0ff (clean tree)
- Vercel prod deployment: dpl_4L4wPodxGbRWvQW2YTgeaxuvqaSd — Ready
- Live domain: https://code.deadhidden.org (200)

## Live verification chain (production, not local)
1. Served HTML contains capture block "Send me the 5 numbers"; Substack link demoted below
2. POST https://code.deadhidden.org/api/capture with test address → 200 success
3. Resend audience 853ea354-ef8b-4781-86cd-1b1032ad247e: contact added (89511a0d)
4. Magnet email "The 5 numbers your reading plan skips" → last_event=delivered, 23:17:28 UTC
5. Test contact deleted (HTTP 200) — audience clean at 694 real contacts

## Funnel state
Note + tweet → free tool → email capture → 5-numbers PDF (soft CTA to $19 count guide, UTM lead-magnet/5-numbers-pdf) → Resend DH list.

## Note
deadhidden/.env.local stores RESEND_API_KEY double-quoted — strip quotes when sourcing via cut/grep or auth fails with "API key is invalid".
