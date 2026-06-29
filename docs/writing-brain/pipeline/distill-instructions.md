# How to distill a transcript into the Writing Brain

Run this for each finished file in `../transcripts/` that does not yet have a matching note in `../distilled/by-channel/`.

## Prompt to give an LLM (paste the transcript after it)

> You are distilling a masterclass recording transcript into reusable writing knowledge for Adam Johnsson's brands (The Biblical Man, Follow Me). KJV-only, discernment/masculinity niche.
>
> From the transcript below, extract ONLY the durable, actionable craft: frameworks, rules, hook patterns, thread structures, growth tactics, copy/offer moves, numbers and named results. Ignore chit-chat, promo, and filler.
>
> Output a markdown note with these sections (omit any that are empty):
> - Source (filename, teacher if named, topic)
> - Core thesis (1 to 3 sentences)
> - Key frameworks / rules (bulleted, specific)
> - Hook or thread patterns (with example wording)
> - Numbers and proof (any concrete results cited)
> - Brand application (how Adam should apply it, in his voice)
> - Fold-into (which PART of WRITING-BRAIN.md this belongs in)
>
> Rules: no em dashes, no AI-slop words, be concrete, quote real numbers exactly, do not invent.

## Save the note
Save as `../distilled/by-channel/<channel>--<short-slug>.md`.

## Fold into the brain
After distilling a batch, update `../WRITING-BRAIN.md`:
- Add genuinely new frameworks/rules to the matching PART.
- Add new hook patterns to `../swipe-files/hooks.md`.
- Remove the item from the "STILL LOCKED IN RECORDINGS" list at the bottom of the brain once captured.
- Keep the brain tight. The brain is the distilled layer, not a transcript dump. Detail lives in the distilled notes.

## Priority order
Match `queue.txt`. Writing craft and algorithm recordings first, then growth, then offers/email, then the rest.
