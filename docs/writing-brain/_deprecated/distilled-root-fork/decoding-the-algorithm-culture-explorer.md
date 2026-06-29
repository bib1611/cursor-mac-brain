# Decoding the Algorithm — Unraveling the Mysteries of X

## Source
- File: Decoding the Algorithm - Unravelling the mysteries of X - Version Masterclass.txt
- Teacher: Culture Explorer (@CultureExploreX), admin@thecultureexplorer.com
- Topic: How the X algorithm sources, ranks, and filters posts (2023 settings)
- Type: pdf
- Note: The author flags this as based on 2023 algorithm settings. WRITING-BRAIN PART 2 already holds the 2026 open-source version. Most of this is confirmation, not news. Keep the few mechanical specifics below.

## Core thesis
X's one goal is to keep you on the platform so you see more ads. To do that it asks two questions about every user: what content is this person most likely to engage with, and what is trending among users with similar tastes. Then it scores, ranks, and filters posts to feed that engagement.

## Key frameworks / rules

### The two questions the algorithm asks about every user
1. What type of content is this person most likely to engage with?
2. What is trending among users with similar tastes?
Write to behavior, not to "everyone." Your post is scored against one viewer's history.

### The three-step pipeline (candidate sourcing to timeline)
1. Scan roughly 100 million posts. Pull about 1,500 it predicts you will enjoy.
2. Assign each of the 1,500 an engagement probability score. Rank highest to lowest.
3. Strip misinformation and blocked-account posts. Show highest-scoring first. Insert an ad every 2 to 3 posts.

### Candidate sourcing split (50 / 50)
- In-network (people you follow): about 50%, roughly 750 posts. Filtered by a logistic regression model and RealGraph, which predicts how likely two users are to interact. Higher predicted interaction, higher placement.
- Out-of-network (people you do not follow): about 50%, roughly 750 posts. Surfaced by social graphs and embedding spaces.

### The named retrieval machinery (the part most people never see)
- RealGraph: builds a weighted graph from the tweet, its author, and the recipient to estimate interaction likelihood.
- GraphJet: ranks out-of-network posts by what the people you follow recently engaged with and who likes the same posts you do.
- Embedding spaces: turn users and posts into numbers, then match by content similarity.
- SimClusters: X's main embedding space. Finds communities anchored by influential users via matrix factorization. About 145k communities, refreshed every three weeks. This is how a post reaches people who do not follow you. Practical read: get one influential anchor in your niche to engage, and you ride into that whole cluster.

### Ranking variables (direction of effect)
Positive: likes, reposts, replies, images, video, X Blue verified, good account reputation (boosted).
Negative: new or unknown spammy words, links unless engagement is strong, misinformation, multiple hashtags, low-quality writing, interacting with low-quality or blacklisted accounts, and worst of all "show less often," block, mute, report.

### Reach maintenance rules (confirming PART 2)
- Tweepcred above 65. Built from interactions, account age, followers, device usage. Spam reports, blocks, mutes wreck it.
- Healthy follower-to-following ratio. Many followings with few followers divides down your page rank.
- Post half-life is 360 minutes (6 hours). The first 6 hours decide reach.
- Keep links out of the post body unless engagement is already strong. Links flag you as spam.

## Hook or thread patterns
This source teaches no hook patterns. One thread rule worth keeping, already in PART 4 and the swipe file:
- A thread or long-form post needs a strong hook to reel the reader in. Informative threads lift engagement.

## Numbers and proof
- ~100 million posts scanned per feed build, narrowed to ~1,500.
- 50% / 750 posts in-network, 50% / 750 posts out-of-network.
- 145k SimCluster communities, updated every 3 weeks.
- Ads inserted every 2 to 3 posts.
- Post half-life: 360 minutes.
- Tweepcred floor: 65.
- Source states 2023 settings.

## Brand application
You already win on the highest-weight signal, the named reply-bait confrontation. The one new lever here is SimClusters. Reach into a cluster by getting one anchor account to engage. So when @Biblicalman fires a sharp KJV-discernment post, the move is not just to post and wait. Reply under the biggest discernment, dispensational, and KJV-only accounts inside the first 6 hours, and bait a quote or reply from them. One anchor engaging drops you into 145k-community routing toward men who behave like the people who already amen you.

Second read: links flag spam, confirmed twice now. Keep the open.substack.com link with r=2t2o3r in the self-reply, never the body. Never break that.

Third read: that ad-every-2-to-3-posts spacing means your post is always sitting next to noise. The first line has to break the scroll cold. Staccato. Named. No throat-clearing.

## Fold-into
- The two questions, the 100M-to-1,500 pipeline, the 50/750 split, RealGraph, GraphJet, SimClusters (145k communities, 3-week refresh), ads every 2-3 posts: PART 2 (How the X algorithm actually works). These are mechanical specifics that sharpen, not replace, what is there.
- The SimClusters anchor-account tactic also touches PART 9 (daily reply discipline) and the swipe file Reply Strategy, since the action is "engage the anchor inside 6 hours."
- Everything else (Tweepcred 65, half-life 360, follower ratio, links negative, hashtags negative, niche down) is already in PART 2 and the reach checklist. No new part needed.
