# Unlocking the X Algorithm

## Source
- File: Unlocking_the_X_Algorithm_-_Masterclass_24-7.txt
- Teacher: not named (cites the xai-org open-source recommendation code)
- Topic: how the X For You feed ranks posts
- Type: pdf

## Core thesis
The X algorithm is mechanical, not mysterious or biased. Every time you open For You, a fast pipeline answers one question: which posts are you most likely to engage with right now. A single transformer model predicts the probability of each action, weights them, sums them, and that score sets feed position.

## Key frameworks / rules
- The feed pulls from two sources: in-network (recent posts from accounts you follow) and out-of-network (the whole platform, surfaced by a machine-learning retrieval system that finds posts engaged with by people who behave like you).
- You and every post become mathematical vectors. The system retrieves the closest matches by similarity.
- Heavy pre-filter before scoring. Removed: duplicates, old posts, your own posts, blocked authors, muted keywords, posts you already saw. Thousands of candidates get narrowed before ranking.
- One transformer scores every remaining post. It does not judge abstract relevance. It predicts specific actions: like, reply, repost, click, watch the video, dwell, follow the author, mute, block, report.
- Each predicted action is multiplied by a weight. Positive actions push the post up. Negative actions push it down. The weighted sum is the final score.
- Each post is scored in isolation, against you, never against other posts. Your feed is not ranked by what is popular or trending. It is ranked by what the model thinks you personally will react to. Two people open the app at the same second and see different worlds.
- Relevance is learned from engagement, not hand-coded. No human decides to boost politics, penalize links, or prefer long posts. Content that reliably produces clicks, replies, or dwell gets promoted. Content that draws blocks, mutes, or reports gets suppressed.
- The system optimizes for expected engagement, not truth, wisdom, or social good. Over time it learns which topics keep you scrolling, which emotions hold you, which conflicts you engage.

## Numbers and proof
- No new named metrics, weights, or case-study numbers in this source. It states the mechanism in plain language without citing signal weights, half-life, or growth figures.

## Brand application
- This source confirms, in plain terms, the engine behind the named-confrontation strategy already in the brain. Replies are the action you want to trigger because the model scores predicted actions, and a named, contested post predicts replies.
- Reinforces the out-of-network reach lever: you reach strangers who behave like the men who already engage you. So write to one tribe over and over. Sameness of audience signal is what gets you retrieved to lookalikes.
- Reinforces the suppression risk: blocks, mutes, reports actively push a post down. The sword (The Biblical Man) must rally the tribe to reply and quote harder than it makes opponents block. Tie every edge to a defensible KJV point so the reaction is "amen and argument," not pure rage.
- Practical floor: be present and engaging early, keep the post link-free in the body, build a reason to reply into the post itself.

## Fold-into
- Everything here belongs in PART 2 (How the X Algorithm Actually Works). It is the same xai-org open-source material PART 2 already distilled, stated more plainly.
- No NEW PART warranted. Nothing in this source is absent from PART 2. If anything, PART 2 is more detailed (it carries the signal weights, 6-hour half-life, Tweepcred, and the net-reach rule that this source omits).
