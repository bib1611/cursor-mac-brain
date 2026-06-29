---
title: "Unlocking the X Algorithm"
category: x-algorithm
tags: [reach, framework]
source_url: "https://drive.google.com/file/d/1F2oduADQsg_3WpxeHID9aN1cASfouKde/view"
source_drive_id: "1F2oduADQsg_3WpxeHID9aN1cASfouKde"
status: distilled
updated_at: 2026-06-19
id: x-algorithm-unlocking
source_file: "raw/extracted-pdfs/Unlocking_the_X_Algorithm_-_Masterclass_24-7.txt"
platform: [x]
folded_into_master: false
confidence: high
related: [x-algorithm-decoding-2026]
---

# Unlocking the X Algorithm

## Source
- File: Unlocking_the_X_Algorithm_-_Masterclass_24-7.txt
- Teacher: none named (Masterclass 24/7 archive)
- Topic: how the X "For You" recommendation pipeline actually ranks posts, drawn from X's publicly released algorithm code (GitHub: xai-org/x-algorithm)

## Core thesis
The For You feed is mechanical, not mysterious or biased. Every time you open it, X runs a fast pipeline to answer one question: which posts are you, personally, most likely to engage with right now. Not best, not true, not important. Engagement is the only currency.

## Key frameworks / rules
- The pipeline starts with YOU, not the posts. X first builds a live behavioral profile from your recent actions: what you liked, replied to, watched, ignored, who you follow, who you muted. It is a moving snapshot of very recent behavior, not your stated interests.
- Two candidate sources feed the feed:
  1. In-network: recent posts from accounts you already follow. Familiar, predictable, gives continuity.
  2. Out-of-network: posts from the whole platform, retrieved by a machine-learning system that finds content engaged with by people who behave like you.
- Vector matching: both you and every post become mathematical vectors. The system pulls the closest matches by similarity.
- Heavy pre-filter before any scoring. From thousands of candidates, X removes: duplicates, old posts, your own posts, blocked authors, muted keywords, and posts you have already seen. Ranking only begins on a cleaned, narrowed set.
- One transformer model scores every remaining post. It does not judge abstract relevance. It predicts specific actions and their probabilities: like, reply, repost, click, video watch, dwell, follow the author, mute, block, report.
- Weighted sum = ranking. Each predicted action is multiplied by a weight. Positive actions push a post up; negative actions (mute, block, report) push it down. The weighted predictions add into one final score that sets feed position.
- Posts are scored in isolation. They are not compared to each other, only to you. The feed is not ranked by what is popular or trending. Two people open the app at the same second and see different worlds.
- No hand-written relevance rules. No human boosts politics, penalizes links, or prefers long posts. Relevance is learned from engagement. Content that reliably produces clicks, replies, or dwell gets promoted. Content that draws blocks, mutes, or reports gets suppressed.
- The objective is expected engagement, not truth, wisdom, or social good. Over time the model learns which topics keep you scrolling, which emotions hold you, which conflicts you bite on, which styles you skip.

## Craft implications (what to do with this)
- Optimize for predicted ACTIONS, not abstract quality. Write posts that earn a like, a reply, a repost, a click, or dwell time. A "good" post that triggers none of these does not rank.
- Dwell time is a scored signal. Long-enough posts that hold the eye (clear line breaks, a thread that pulls the scroll) feed the model the dwell it rewards. Structure for the stop, not just the scroll.
- Replies are weighted up; the reply is content, not afterthought. End posts on a line that demands an answer.
- Avoid the suppressors at all costs. Mute, block, and report are negative weights that bury you. Bait-and-switch, spam cadence, and rage that crosses into "make it stop" trip these. One report-worthy post can drag the score.
- You are not writing for "X." You are writing for the model's read of one person's recent behavior. The audience that already engages with your kind of content is who the retrieval system serves you to. Consistency in topic and emotion trains the system to find your people.
- Links are not penalized by a rule. Any link drag is learned from how readers behave around links, not a hard-coded rule. (Adam's existing practice of putting links in a self-reply still holds, because it keeps the scored body post clean and engageable.)
- New / out-of-network reach comes from behavioral lookalikes, not follower count. Posts get surfaced to strangers who behave like the people already engaging with you. Earn deep engagement from your core and the model widens the circle for you.

## Numbers and proof
- The pipeline answers exactly ONE question per feed open: which posts are you most likely to engage with right now.
- 2 candidate sources: in-network and out-of-network.
- Thousands of candidate posts enter; most never reach scoring after the pre-filter.
- 1 transformer model scores all remaining posts.
- Predicted actions scored (positive and negative): like, reply, repost, click, video watch, dwell, follow author, mute, block, report.
- Each post scored in isolation, compared only to you, never to other posts.
- Source authority: X's own recommendation code, released publicly (GitHub xai-org/x-algorithm).

## Brand application (Adam's voice)
The feed is a mirror. It shows people what they already are.

So stop writing for the algorithm. Write for the man holding the phone.

The Biblical Man read: the machine rewards what holds attention. Conflict. Emotion. The thing people cannot scroll past. Use that, but bend it toward conviction, not rage-bait. A KJV line that stops the thumb. A wound named plainly. A question that demands a reply. Make the discernment post the one they cannot ignore, then the model carries it to every man who behaves like the men already convicted.

Follow Me read: scar tissue is dwell time. The confession that makes a man sit still and read twice is exactly the signal the model scores up. Bleed on the page. The stop is the strategy.

And the warning underneath: the feed studies your past to predict your next reaction, then feeds you more of it. It is not neutral. It is a personalized reality, shaped quietly by your own appetites. That is a sermon in itself. The man who lets the feed disciple him gets the man the feed wants. Guard the eyes.

## Fold-into
PART: X / Twitter Algorithm and Distribution (platform mechanics + hook/dwell/reply craft). Cross-reference the hook and thread sections, since dwell and reply weights are the technical reason those frameworks work.
