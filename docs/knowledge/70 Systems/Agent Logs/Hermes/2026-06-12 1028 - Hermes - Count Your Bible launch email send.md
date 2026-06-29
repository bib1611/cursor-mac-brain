# Count Your Bible launch email — SENT

- **When:** 2026-06-12 10:28 CDT, on Adam's explicit "send now"
- **Broadcast:** Resend `34fa34f9-87dc-4e31-a15d-a1a4c7dc4760`
- **Subject:** "My machine embarrassed me yesterday" (Halbert damaging-admission open, owns yesterday's 4x misfire)
- **Audience:** `853ea354-ef8b-4781-86cd-1b1032ad247e` (deadhidden.org list)
- **CTA:** deadhidden.org/store/how-to-count-your-bible — $19 one-time

## Send discipline (anti-4x protocol)
1. Pre-send GET: status=draft, sent_at=null ✓
2. One POST /send ✓
3. Post-send GET: status=queued, broadcast list = exactly 1 today ✓
4. Background watcher polling until status leaves queued — NO blind retries

## Context
- Yesterday's 4x misfire root cause: draft-then-send cycle ran 4 times, each pass minted + fired a fresh broadcast. Fix is procedural: one draft ID, verify, one send, verify.
- Substack launch post scheduled 11:44 CDT same day — readers on both lists get 2 emails ~75 min apart. Adam chose send-now over afternoon spacing.
