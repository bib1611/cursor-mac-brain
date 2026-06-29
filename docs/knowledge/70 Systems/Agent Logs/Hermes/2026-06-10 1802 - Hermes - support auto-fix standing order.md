# Support auto-fix standing order
Date: 2026-06-10 1802 CT
Adam's instruction (Telegram): "When these pop up fix them. No refunds though."

## State at time of order
- Count the Number download 503 fixed 4:11 PM (843d80f); all 9 affected buyers emailed PDF via Resend 5:10 PM.
- Complainants all pre-rescue: mzura1, steveohg, calmanza1 (her attachment = count-the-number.txt placeholder, same root cause), lilahammett ("It worked"), dknighton ("Thanks!"). Nothing outstanding.

## Actions
- RULES.md: added Support Auto-Fix Rule (auto-fix authorized, NO REFUNDS without Adam).
- Hermes cron: Gmail support sweep every 30 min 7a-10p, auto-fix + receipt + Telegram flag on refund asks.
