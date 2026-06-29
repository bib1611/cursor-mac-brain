# Money Loops

The money is not in new content or new infrastructure. It is in monetizing the audience you already own: ~50,000 subscribers, ~1,465 paying, so 97% ride free. The 2026-06-20 email on/off campaign proved the leak is **path complexity, email-volume fatigue, and deliverability** — not weak writing. A paying reader went dark and said the sites, Vault, layers, and daily emails "felt confusing." Content value is not the problem. The path is.

Four bounded loops, ranked by dollar impact.

| Loop | Money lever | Rough size |
|---|---|---|
| **[Loop 1 — Free-to-Paid Conversion](loop-1-free-to-paid-conversion.md)** | Move list paid share 2.9% → 4% by repeating the free pieces that actually drive upgrades, with ONE simple CTA (kill the maze) | **~+$30–40K ARR** |
| **[Loop 2 — Churn & Dunning Save](loop-2-churn-dunning-save.md)** | Recover failed-card churn, win back cancels, and restore the **164 paid subs with email OFF** (5 already said "ON" / want it back) | Cheapest cash, low effort |
| **[Loop 3 — Back-Catalog Cross-Sell](loop-3-back-catalog-cross-sell.md)** | Sell the ~70 paid products + bundles past launch day — one clear offer per send, low frequency (respect the fatigue signal) | Compounding store revenue |
| **[Loop 4 — Revenue-Leak Sweep](loop-4-revenue-leak-sweep.md)** | Make sure paid products never silently go free again (we caught 18 paid PDFs free-downloadable today). Runnable: `revenue-leak-sweep.py` | Insurance on the whole ~$96K |

## How to run these

- Each loop is **bounded**: a real verify gate and a named stop (no-progress or an explicit limit). None of them runs forever.
- **Selecting a loop sends nothing.** It does not start a schedule, publish, charge a card, or email anyone. Every send/charge/publish step needs your explicit approval of that exact action.
- **Live-system wiring is Codex's lane** — Stripe (dunning/failed payments), Resend (adam@deadhidden.org), Gmail, Substack, the store repo. The loop docs say exactly what each one touches.
- **Loop 4 already runs today.** `python3 revenue-leak-sweep.py` — read-only, probes all 18 paid files on both hosts. Right now it returns 36 leaks (exit 1). It should go green the moment Codex's privacy fix deploys and the CDN is purged.

Built 2026-06-21 by Claude Code, grounded in the real product catalog and the email on/off campaign data Codex captured. Numbers from `~/CLAUDE.md` and `bm-email-off-reply-watch.sqlite3`; anything unverified is marked VERIFY inside each loop doc.
