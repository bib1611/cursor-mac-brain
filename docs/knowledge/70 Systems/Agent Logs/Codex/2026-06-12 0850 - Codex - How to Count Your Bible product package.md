# Codex Receipt - How to Count Your Bible Product Package

Time: 2026-06-12 08:50 CDT

Adam asked Codex to turn the Claude-produced draft of the paid Dead Hidden guide `How to Count Your Bible` into a corrected, polished, designed, sellable product package.

Source draft:

- `/Users/adamjohnsson/Library/Application Support/Claude/local-agent-mode-sessions/ba7016e1-95e0-4543-9750-cfb79660f411/b66087a7-cf21-4799-b3e8-93d4d10d172f/local_6bf0d7ac-d9fe-450a-9884-940b1049e4c1/outputs/20260612_how-to-count-your-bible.md`

Created outputs:

- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-polished.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-print.html`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible.pdf`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-image-prompts.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-checkout-description.md`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-assets/cover-engraving.png`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-assets/divider-method.png`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-assets/divider-genesis.png`
- `/Users/adamjohnsson/Documents/Codex/2026-06-12/files-mentioned-by-the-user-20260612/outputs/how-to-count-your-bible-assets/divider-888.png`

Applied edits:

- Replaced the factual Irenaeus/888 attribution with the Sibylline Oracles attribution requested by Chorus.
- Collapsed the two called-out AI-tell triads.
- Added the Genesis 5 hedge: `the traditional Hebrew readings`.
- Strengthened the outcome close around `New eyes` without restructuring the argument.
- Removed the checkout copy from the designed PDF and saved it separately.
- Kept the guide KJV-only and did not add new examples or new theological claims beyond the requested correction.

Verification:

- Local KJV SQLite verification checked the draft's referenced/touched verses, including Revelation 13:18, Genesis 4:25, Genesis 5:25, Genesis 5:27-31, Genesis 7:6, Genesis 17:12, Mark 8:19-21, and 1 Peter 3:20.
- External attribution check confirmed the Sibylline Oracles 888 correction against source notes before editing.
- Generated print HTML and rendered PDF with Playwright/Chromium.
- Rendered the final PDF through Poppler to PNG pages and visually inspected the cover, Genesis 5 table, 888 page, and final CTA page.
- `pdfinfo` confirmed 8 Letter pages, PDF 1.4.
- `pdftotext` confirmed the corrected lines exist in selectable PDF text.
- `rg` confirmed no pasted Anthropic key or `sk-ant` string landed in outputs.

Boundary:

- No Hermes credential, Anthropic key, Claude Desktop config, Substack draft, public post, email, Stripe/customer action, deploy, or account-state change was performed.
- The pasted Anthropic key was treated as compromised and was not written into the deliverables.
