# STAGED X POST — fires 2026-06-12 07:05 CDT unless Adam cancels

Drives: https://biblicalman.substack.com/p/the-conversation-they-called-bitterness (paid BM post, live 2026-06-11)
Lane: wound/confessional — picked off Jun 9 "pastor who hurt you" tweet (4.6% engagement rate, best ratio in 25-tweet sample)
Rules applied: no link in body, self-reply carries link, open.substack + r=2t2o3r, voice-DNA pre-flight passed

## TWEET 1 (body — no link)

They called your silence forgiveness.

It was not.

It was a sentence you never read out loud.

They did not fear your unforgiveness.

They feared your sentence.

## TWEET 2 (self-reply to tweet 1)

I wrote the conversation out. The exact words. What forgiveness requires of them. What it never required of you.

For paid readers:

https://open.substack.com/pub/biblicalman/p/the-conversation-they-called-bitterness?r=2t2o3r

## POST MECHANISM

1. /Users/adamjohnsson/.agents/bin/dh-with-env xurl -X POST /2/tweets -d '{"text":"<TWEET 1>"}'
2. Capture returned tweet id
3. /Users/adamjohnsson/.agents/bin/dh-with-env xurl -X POST /2/tweets -d '{"text":"<TWEET 2>","reply":{"in_reply_to_tweet_id":"<id>"}}'
4. Reply to Adam on Telegram with both tweet URLs as proof
