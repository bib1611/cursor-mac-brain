---
title: "Decoding the Algorithm — Unraveling the Mysteries of X"
category: x-algorithm
tags: [reach, framework, engagement-bait]
source_url: "https://drive.google.com/file/d/1VUs39QFRhJ_B0HTlFqu44jX9LXSLLG6u/view"
source_drive_id: "1VUs39QFRhJ_B0HTlFqu44jX9LXSLLG6u"
status: distilled
updated_at: 2026-06-19
id: x-algorithm-culture-explorer-decoding
instructor: "Culture Explorer"
source_file: "raw/extracted-pdfs/Decoding the Algorithm - Unravelling the mysteries of X - Version Masterclass.txt"
platform: [x]
folded_into_master: false
confidence: high
related: [x-algorithm-decoding-2026]
---

# Decoding the Algorithm — Unraveling the Mysteries of X (distilled)

## Source
- File: `extracted-pdfs/Decoding the Algorithm - Unravelling the mysteries of X - Version Masterclass.txt`
- Teacher: Culture Explorer (@CultureExploreX), thecultureexplorer.beehiiv.com
- Topic: the 2023 open-source X algorithm — how the feed sources, scores, ranks, and filters posts, and what a creator can do to gain reach
- Type: PDF (Masterclass Version, Copyright 2024)
- Note: built on 2023 algorithm settings. The named systems (RealGraph, GraphJet, SimClusters, Tweepcred) are the 2023 mechanics. The later 2026 Grok-scored version is in the sibling note `x-algorithm--decoding-the-x-algorithm.md` and in WRITING-BRAIN.md PART 2.

## Core thesis
X's one goal is to keep you on the platform so you see more ads. To do it, the algorithm asks two questions about every reader: what is this person most likely to engage with, and what is trending among people with similar taste. It then scores posts on predicted engagement and serves the highest first. Your reach is a function of how confidently the machine can answer those two questions about your post.

## Key frameworks / rules

- **The three-step pipeline.** 1) Candidate sourcing: scan roughly 100 million posts, pull the 1,500 it predicts you will most enjoy. 2) Scoring and ranking: assign an engagement probability score to each of the 1,500, rank highest to lowest. 3) Filtering: strip misinformation and blocked accounts, serve highest-scoring first, insert an ad every 2-3 posts.

- **Candidate sourcing splits 50/50.** Of the 1,500 candidates, roughly 750 (about 50%) come from people you follow (in-network) and roughly 750 (about 50%) from people you do not follow (out-of-network). Half your possible reach is to strangers, so the post has to be legible to a machine that does not know you.

- **The three data points the machine reads.** 1) The follower graph (who follows you). 2) Engagement data (likes, reposts, replies). 3) User data (reposts, replies, mutes, unfollows, spam reports). Mutes, unfollows, and reports are inputs too, not just non-events.

- **RealGraph (in-network sourcing).** Builds a weighted graph from the tweet, its author, and the intended recipient to predict the chance two users interact. Higher predicted interaction = higher chance you appear in that follower's feed. Top posts advance to the next stage. A logistic regression model curates the most timely, relevant posts from accounts you follow.

- **GraphJet (out-of-network sourcing).** A logistic regression model that ranks posts using the social graph — what the people you follow recently engaged with, and who likes posts similar to the ones you like. This is how a stranger's post reaches you through a shared follow.

- **SimClusters (out-of-network embedding space).** Discovers communities anchored by influential users via custom matrix factorization. 145k communities, refreshed every three weeks. Users and posts are placed in this community space, and posts get pushed to people in the same cluster who do not yet follow you. This is the named mechanism for breaking out of your existing audience. Anchor yourself to the influential accounts in your community and the system maps you to their cluster.

- **"Great engagement is rewarded with great reach" — at the sourcing stage.** Fast early engagement (likes, comments, shares, saves) is the signal that gets the post pulled into more candidate pools.

- **Ranking signal weights (2023, can change at any time):**
  - Positive: likes, reposts, replies, images, video, X Blue verified.
  - Positive and boosted: good account reputation.
  - Negative: new/unknown words or unknown language; links (unless the post earns strong engagement); misinformation; multiple hashtags; certain "type of writing"; interacting with low-quality accounts and blacklisted topics.
  - Worst: a reader hits "show less often," blocks/mutes you, or reports you. Stated as "Negative, this is terrible."

- **Post half-life is 360 minutes (6 hours).** Replying and driving engagement inside the first 6 hours raises the post's relevancy while it still has life. After that the post decays.

- **Tweepcred — keep it above 65.** A reputation score built from interactions, account age, follower count, and device usage. Healthy engagement holds it up; spam reports, blocks, and mutes "hurt it badly."

- **Follower-to-following ratio gates page rank.** A low-follower / high-following account gets its page rank divided down. A clean ratio protects reach.

- **X Blue boost is conditional.** Bigger boost when the subscriber is in the same network as the author, smaller boost when out of network.

- **Five reach factors (the "town crier" model):** engagement (does it make people stop, watch, react), relevance (does it match what the audience already engages with), timing (post when they are awake and online), consistency (a regular schedule signals you are here to stay), and quality (fresh and distinct beats the same old routine). The crier shouts loudest for the performer who pulls coins fast.

## Hook / thread / offer patterns
- **Threads and long-form lift engagement** — and a thread lives or dies on its hook. Build one line at the top that reels the reader in, then deliver the informative body.
- **Engineer a reason to engage.** Pose a question, ask for a reply, give the reader a task. "Content that encourages users to click, reply, and engage can skyrocket your reach."
- **No links in the body.** External links flag you as spam and cut ranking unless the post is already winning. KJV-discernment adaptation: post the conviction raw, then drop the Substack link (open.substack.com, r=2t2o3r) in a self-reply once the post has its own engagement.
- **Reply to compound.** Reply with content strong enough to attract attention on your own post and on trusted high-engagement accounts in your niche. Do not reply to untrusted accounts — it pulls you toward low-quality signal.
- **Niche down to a trusted voice.** Become known inside one community by engaging its prominent accounts; SimClusters then maps your posts to that community. For Adam: own KJV discernment and Biblical masculinity rather than diffusing across general "Christian content."
- **One hashtag, not many.** Multiple hashtags are a negative signal.

## Numbers and proof
- Scans ~100 million posts to select ~1,500 candidates.
- Candidate split: ~50% / ~750 in-network, ~50% / ~750 out-of-network.
- 145k SimClusters communities, updated every three weeks.
- Post half-life: 360 minutes (6 hours).
- Keep Tweepcred above 65.
- Ads inserted every 2-3 posts.

## Brand application (Adam's voice)
- Specificity is reach. The machine has to know what your post is about to know who to show it to. "Discernment" is vague. "Why the NIV deletes Acts 8:37" is a signal it can route. Name the verse. Name the lie. Name the cost.
- Original beats borrowed at the ranking stage. Recycled takes get buried. Write from the wound, not from the commentary everyone already quoted. Your scar tissue is the original example no one else has.
- The first 6 hours are the fight. Post, then stay in the replies. Answer the pushback. A live thread keeps the post breathing inside its 360-minute window.
- Guard your Tweepcred and your ratio. Blocks, mutes, and reports do real damage to the score that decides your reach. Be sharp, not cheap. Conviction travels; bait gets you muted.
- Link in the self-reply, never the body. Conviction in the post, open.substack.com link (r=2t2o3r) underneath once it is moving.
- One community, deeply. Engage the trusted KJV / masculinity accounts so SimClusters files you in that cluster and carries your posts to readers who have not found you yet.

## Fold-into
WRITING-BRAIN.md **PART 2 — HOW THE X ALGORITHM ACTUALLY WORKS**. File this as the 2023 open-source foundation (RealGraph / GraphJet / SimClusters / Tweepcred / 360-minute half-life), beneath the current 2026 Grok-scored model. The durable carry-forwards that survive both versions: specificity wins, original beats borrowed, the first-hours window decides distribution, reputation and ratio gate reach, links belong in the self-reply.
