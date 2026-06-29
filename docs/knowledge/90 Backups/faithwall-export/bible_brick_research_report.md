# Bible Brick Research Report: Optimal Unbrick Duration + Screen Time Tracking
## Comprehensive Research for Christian App-Blocking Product

---

## 1. DURATION RECOMMENDATION (WITH EVIDENCE)

### 1.1 The Core Finding: The Goldilocks Zone is 60-120 Seconds

**Bottom line:** 30 seconds is too short for meaningful engagement. The optimal duration for an "unbrick" Bible task that balances meaning with user retention is **60-120 seconds**, with a recommended default of **90 seconds**.

### 1.2 What the Competition Actually Uses

| App | Unlock Method | Duration / Friction | User Experience |
|-----|--------------|---------------------|-----------------|
| **Prayer Lock** | Pray a generated prayer based on mood | ~30-45 seconds (estimated) | Select apps → share feelings → receive personalized prayer → pray → unlock. All features require subscription. |
| **Bible Mode** | Scan physical Bible OR read verse + reflection | "Just a few moments" (~30-60 sec for scan; ~2 min for reflection) | Scan unlocks "instantly"; verse reading takes ~2 minutes. 4.9 stars, 10K+ reviews. Users report 98% drop in unproductive screen time. |
| **The Brick (getbrick.app)** | Physically tap phone to NFC device | ~5-10 seconds (minimal friction) | Physical NFC tag creates "real friction" through environmental design. Users report 99%+ screen time reduction, ~3.1 hrs less daily. |
| **one sec** | 10-second delay + dismiss option | **10 seconds exactly** (peer-reviewed) | PNAS study: 10s delay + dismiss button reduced target app opens by **57%** after 6 weeks. 36% of attempts dismissed immediately. |
| **Clearspace** | Breathing exercise + wait + session length commitment | ~5-15 seconds delay | "A bit annoying, but that's the point." -- user review. Light-touch nudge. |
| **Opal** | Focus sessions (scheduled blocking) | Variable (session-based, not per-unlock) | Deep Focus mode cannot be bypassed. Leaderboard + gamification. |
| **Taskfulness** | Explain reason + set timer | ~30 seconds to explain + timer commitment | AI evaluates reason for using app. "Emergency Minute" (10 min/day) for urgent needs. |

### 1.3 What Behavioral Psychology Research Says

**Key insight from the one sec PNAS study (2023):**
- The most effective feature was NOT the delay itself — it was the **dismiss option** (convenience nudge)
- However, the **10-second friction delay** also played a meaningful role
- Combined effect: 57% reduction in target app opens after 6 weeks
- Users reported increased satisfaction with consumption after reduction

**Behavioral psychology principles for Bible Brick:**

1. **The "2-Minute Rule"** (James Clear, Atomic Habits): New habits should take less than 2 minutes. This is the MAXIMUM threshold for habit formation. Tasks longer than 2 minutes feel like "real work" and reduce compliance.

2. **Limbic Friction** (Andrew Huberman): The mental energy to overcome distraction/anxiousness. For every additional step, habit compliance drops. Research shows: for every additional foot between you and an object, likelihood of use drops 7%.

3. **Adding just 10 seconds of delay reduces social media usage by 22%** (research cited by welloclock.com).

4. **Progressive Engagement**: Start small to build momentum. Bible Mode's approach of "start small, with 1-2 minute moments" aligns with this.

### 1.4 The Duration Sweet Spot Analysis

| Duration | Pros | Cons | Verdict |
|----------|------|------|---------|
| **5-10 sec** | High compliance, minimal friction | Too short to feel meaningful; becomes "muscle memory" bypass; no spiritual engagement | **Too short** - wife is right |
| **30 sec** | Better than nothing; lock-screen prayer apps use this | Still too brief for Scripture reading; feels like a speed bump not a devotional | **Too short** - barely enough to read one verse |
| **60 sec** | Can read + reflect on one verse; still quick; good compliance | May feel rushed for deeper reflection | **Acceptable minimum** |
| **90 sec** (1.5 min) | Time for one verse + short prayer/reflection; meaningful but not burdensome; aligns with Bible Mode's approach | Slightly higher abandonment than 30s, but dramatically higher satisfaction | **RECOMMENDED DEFAULT** |
| **2 min** | Bible Mode explicitly uses this: "Just 2 minutes to reset with God"; time for reading + reflection + application | Risk of some users abandoning; requires careful UX to feel smooth | **Good for "reflection mode"** |
| **3-5 min** | Time for meaningful devotional content | Too long for an unlock task; users will skip/circumvent | **Too long for unlock** - save for Quiet Time Mode |
| **5+ min** | Deep engagement | Massive abandonment; users will uninstall or circumvent | **Way too long** |

### 1.5 Specific Duration Recommendation

**RECOMMENDATION: 90 seconds default, with user-adjustable 60-120 second range**

Bible Mode's own marketing says: "Just 2 minutes to reset with God" and offers two paths:
- **Scan physical Bible** = instant unlock (~5 seconds)
- **Read verse + reflection** = ~2 minutes

For Bible Brick, we recommend **tiered task types** with different durations:

| Task Type | Duration | Description | Best For |
|-----------|----------|-------------|----------|
| **Quick Verse** | 30-45 sec | Read one verse aloud | Fast unlock option |
| **Verse + Reflection** | 90 sec (default) | Read verse + answer one reflection question | Daily default |
| **Memorization** | 60-90 sec | Type out a short verse from memory | Spiritual formation |
| **Prayer Response** | 90-120 sec | Read verse + write/record a short prayer | Deep engagement |
| **Quiet Time Mode** | 5-15 min | Full devotional experience | Separate feature, not for unlock |

---

## 2. SCREEN TIME TRACKING FEATURE SPEC

### 2.1 What Data is Available (iOS Screen Time API)

**iOS Screen Time API (iOS 15+, requires Family Controls entitlement from Apple):**

Available data through `DeviceActivityReportExtension`:
- **Total screen time** per day/week
- **App-by-app usage time** (via application tokens)
- **Category-level usage** (Social, Entertainment, Productivity, etc.)
- **Number of pickups** (device unlocks)
- **Notification counts** per app
- **Web domain usage** (if configured)

**Critical limitation (iOS):**
- Apps do NOT get raw app names — they get cryptographic tokens
- Cannot identify specific apps without user selection via `FamilyActivityPicker`
- Requires Apple's **Family Controls distribution entitlement** (must apply and be approved)
- Cannot open parent app from shield directly (no URL scheme support from ShieldAction)
- Apple blocks can be revoked by user without passcode protection (unlike native Screen Time)

**iOS API architecture for implementation:**
```
FamilyControls → ManagedSettings → DeviceActivity
     (select)        (block)          (when)
```

### 2.2 What Data is Available (Android Digital Wellbeing)

**Android UsageStatsManager API (API Level 21+):**

Requires `PACKAGE_USAGE_STATS` permission (user must grant in Settings):
- **Total time in foreground** per app (`getTotalTimeInForeground()`)
- **App open timestamps** (first used, last used)
- **Usage events** (foreground/background transitions)
- **Package information** for all installed apps

**Limitations:**
- Cannot track web domain usage directly
- Cannot block apps at system level (need Accessibility Service + Device Admin, which Google is restricting)
- Data is historical only; no real-time blocking at the same OS level as iOS
- User must manually grant Usage Stats permission in system settings

### 2.3 How Competitors Implement Screen Time Tracking

**Opal:**
- **Focus Report**: Weekly report with clear metrics + benchmark against peers
- **Profile**: Personalized insights based on usage patterns
- **Focus Home**: Screen time + focus level at any point, spotting "Focused" vs "Distracted" time
- **Leaderboard**: Challenge friends to top leaderboard
- **App Lock**: Semi-permanent locks on most distracting apps with limited daily unlocks
- **Real-time tracking**: Habits like phone unlocks, overall usage patterns
- **Weekly progress report** delivered automatically

**RescueTime:**
- **Productivity Pulse**: Score 0-100 based on productive vs unproductive time
- **Automatic categorization**: Every app/website categorized as Productive/Neutral/Distracting
- **Weekly email summaries**: Productivity score, top categories, behavioral trends
- **Goal tracking**: "Reduce email time to 30 min/day" type goals
- **Real-time alerts**: When spending too much time in unproductive categories
- **Offline activity tracking**: Log meetings, calls, etc.
- **Cross-device**: Desktop + mobile combined view

**one sec:**
- Tracks intervention attempts, dismissals, and successful opens
- Shows reduction in usage over time
- Minimal reporting — focuses on behavior change, not metrics

**Clearspace:**
- Shows how many times you opened target apps today
- Session-length commitment tracking
- Lightweight, non-judgmental stats

### 2.4 Recommended Screen Time Feature Spec for Bible Brick

#### Core Metrics to Track & Display

| Metric | Priority | How to Calculate |
|--------|----------|------------------|
| **Daily/Weekly Total Screen Time** | P0 | Sum of all foreground app time (via iOS/Android APIs) |
| **Screen Time "Given to God"** | P0 | Total time spent doing Bible unlock tasks + Quiet Time |
| **Times You Chose God First** | P0 | Count of unlock interventions completed |
| **Pickups per Day** | P1 | iOS Screen Time data / Android usage events |
| **Top 5 Distracting Apps** | P1 | Sorted by time spent |
| **Average Unlock Task Duration** | P2 | Tracked in-app |
| **Streak (Consecutive Days)** | P2 | Tracked in-app |
| **Screen Time Trend** | P2 | Week-over-week comparison |
| **Bible Engagement Time** | P2 | Total time in app doing tasks |
| **Times Circumvented** | P3 | Track emergency unblocks / bypasses |

#### Dashboard Visualization Design

**Primary View (Home Screen):**
```
+------------------------------------------+
|  Today                                   |
|  Screen Time: 3h 12m    [vs 3h 45m avg] |
|  [===========-----] -33m vs yesterday   |
|                                          |
|  Times you chose God first: 7            |
|  Time with God: 10m 30s                  |
|  Current Streak: 5 days                  |
|                                          |
|  [Weekly Bar Chart - last 7 days]        |
|  Mon Tue Wed Thu Fri Sat Sun             |
|  ==== ==== ==== ==== ==== ==== ====      |
+------------------------------------------+
```

**Weekly Report (deep link or tab):**
- Bar chart of daily screen time (7 days)
- Trend indicator (improving / stable / increasing)
- Most used app category
- Minutes spent with Scripture vs scrolling
- Scripture engagement count
- Personalized insight: "You chose prayer over Instagram 12 times this week!"

**Gamification Elements:**
- **Streak badge**: Consecutive days of completing unlock tasks
- **"Brick Builder"**: Visual wall that gets a new brick each time you complete a task
- **Bible engagement badges**: 10 tasks, 50 tasks, 100 tasks milestones
- **Screen time reduction badge**: -10%, -25%, -50% reduction milestones

---

## 3. COMPETITIVE ANALYSIS

### 3.1 Detailed Competitive Matrix

| Feature | Prayer Lock | Bible Mode | The Brick | Opal | one sec | Clearspace |
|---------|-------------|------------|-----------|------|---------|------------|
| **Blocking Type** | Proactive (must pray before opening) | Proactive (verse/reflection to unlock) | Physical NFC tap | Scheduled sessions | Intervention delay | Delay + session limit |
| **Unlock Duration** | ~30-45 sec prayer | ~2 min reflection / instant Bible scan | ~5-10 sec tap | N/A (session timer) | 10 sec delay | ~5-15 sec delay |
| **Screen Time Tracking** | "Detailed prayer journey analytics" | Streaks, time saved, monthly stats | Timer tracks "bricked" duration | Focus Report, Profile, Leaderboard | Minimal (behavior-focused) | App open count, session lengths |
| **Cost** | Subscription required | Freemium (free + premium widgets) | $49-89 device + free app | Freemium | Freemium | Freemium (1 app free) |
| **Spiritual Content** | AI-generated prayers based on mood | Bible verses, devotionals, AI Bible Chat | None | None | None | None |
| **Physical Element** | No | Yes (Bible scan) | Yes (NFC device) | No | No | No |
| **Reviews/Rating** | Newer app | 4.9 stars, 10K+ reviews | High user satisfaction | 300K+ users, 94% less distracted | 4.8 stars, 85K+ installs | 4.8 stars, 15 reviews |
| **Key Differentiator** | "Put God First" - prayer before apps | Bible scan feature | Physical friction device | Deep Focus (unbreakable) | Peer-reviewed science | Push-ups to unlock |

### 3.2 Prayer Lock "Put God First" Feature Analysis

Prayer Lock's model is **proactive blocking** (block BEFORE you get stuck), not reactive:

1. **How it works:**
   - User selects apps to block
   - When user tries to open blocked app → prayer intervention appears
   - User shares how they feel with God
   - App generates a personalized, Bible-rooted prayer
   - User prays → apps unlock

2. **UX Flow:**
   ```
   [Try to open Instagram] → [App blocked] → [Share feelings with God] → 
   [Receive personalized prayer] → [Pray] → [Apps unlocked]
   ```

3. **Key features:**
   - Prayer streak tracking
   - Detailed prayer journey analytics
   - Personalized prayers matched to mood
   - Unlimited lock/unlock cycles

4. **Limitations noted:**
   - **ALL features require active subscription** — no free tier at all
   - No screen time data tracking (only prayer analytics)
   - No Bible content integration (prayers are AI-generated, not Scripture-based)
   - App is newer with fewer reviews

### 3.3 Bible Mode — The Closest Competitor to Bible Brick

Bible Mode is the most similar app to Bible Brick's concept:

- **Core mechanic**: Block apps → unlock via Bible engagement
- **Two unlock paths**: (1) Scan physical Bible (~5 sec), (2) Read verse + reflection (~2 min)
- **Gamification**: Streaks, "Faith Points," minutes saved, time saved tracking
- **Social**: "Bible Buddies" feature for accountability
- **Monetization**: Free core + premium widgets ($35K/mo revenue estimated, 15K installs/mo)
- **User feedback**: "I never thought I'd enjoy screen time limits but Bible Mode makes it feel meaningful"

### 3.4 What "Put God First" Means for Bible Brick

**Proactive vs Reactive Blocking:**

| Approach | Mechanism | Effectiveness | User Experience |
|----------|-----------|---------------|-----------------|
| **Proactive (Prayer Lock model)** | Block BEFORE opening distracting app; must complete task first | **HIGH** — prevents spiral entirely | May feel intrusive at first; builds positive habit |
| **Reactive** | Allow opening; interrupt after time limit reached | Medium — good for limiting, not preventing | Less friction; easier to bypass |
| **Scheduled** | Block during set hours (Opal model) | High during blocked hours; zero protection outside | Predictable; requires advance planning |

**Recommendation for Bible Brick:** Offer **both** modes:
1. **"God First" Mode** (proactive): Block distracting apps by default; must complete Bible task to unlock for a set duration
2. **Scheduled Mode**: Block during devotional times (morning/evening)
3. **"Sabbath Mode"**: Full blocking for extended periods (e.g., Sunday worship)

---

## 4. FEATURE IMPLEMENTATION PRIORITY

### P0 (Must Have for MVP)

1. **90-second default unlock task** (adjustable 60-120 sec)
   - Read verse + answer 1 reflection question
   - "Type the verse from memory" mode
   - Option to extend to prayer/voice recording

2. **Proactive blocking** ("God First" mode)
   - Block selected apps by default
   - Complete Bible task → unlock apps for chosen duration (15 min, 30 min, 1 hr, 2 hr)
   - After duration expires, apps re-block automatically

3. **Basic screen time tracking**
   - Daily total screen time
   - Count of "chose God first" moments
   - Time spent in Bible engagement
   - Streak counter

### P1 (Should Have - Next Release)

4. **Screen Time Dashboard**
   - Weekly bar chart
   - Trend indicators (improving/declining)
   - Top distracting apps list
   - Comparison: screen time vs Bible time

5. **Multiple task types**
   - Quick Verse (30 sec)
   - Verse + Reflection (90 sec)
   - Memorization (60-90 sec)
   - Prayer Response (90-120 sec)

6. **Scheduled blocking**
   - Set "God First" hours (e.g., 6am-9pm)
   - Quiet Time Mode (custom session length)
   - Sabbath Mode (full day)

7. **Gamification**
   - Streak badge (consecutive days)
   - "Wall Builder" visualization (add brick per task)
   - Milestone badges (10, 50, 100, 365 tasks)
   - Screen time reduction badges

### P2 (Nice to Have)

8. **Weekly email/push report**
   - Screen time trends
   - Spiritual engagement highlights
   - Personalized encouragement

9. **Social features**
   - Accountability partners
   - Family sharing
   - Church group leaderboards

10. **Advanced screen time analytics**
    - Pickup count
    - Notification volume
    - Hour-by-hour usage heatmap
    - Category breakdown (Social, Entertainment, Productivity)

### P3 (Future Considerations)

11. **Physical element** (like Bible Mode's Bible scan)
    - Scan Bible to quick-unlock
    - NFC tag integration

12. **Voice features**
    - Voice-recorded prayers
    - Audio Bible reading
    - Voice memos for reflections

13. **AI-powered personalization**
    - Mood-based verse selection
    - AI-generated reflection questions
    - Personalized devotionals

---

## 5. KEY SOURCES & RESEARCH REFERENCES

### Primary Sources

1. **one sec PNAS Study (2023)** — "Directing smartphone use through the self-nudge app one sec"
   - Gruning, D.J., Riedel, F., Lorenz-Spreen, P. et al. Proc Natl Acad Sci U S A 120 (2023).
   - https://pubmed.ncbi.nlm.nih.gov/36795756/
   - **Key finding**: 57% reduction in target app opens after 6 weeks; 36% immediate dismissal rate

2. **WWDC 2021 - Meet the Screen Time API**
   - Apple's official documentation for iOS Screen Time API
   - Three frameworks: FamilyControls, ManagedSettings, DeviceActivity
   - https://developer.apple.com/videos/play/wwdc2021/10123/

3. **Android UsageStatsManager Documentation**
   - https://developer.android.com/reference/android/app/usage/UsageStatsManager
   - API Level 21+; requires PACKAGE_USAGE_STATS permission

4. **one sec Developer Blog (Frederik Riedel)**
   - "Apple's Screen Time API has some major issues" (2024)
   - Detailed breakdown of iOS API limitations and workarounds
   - https://riedel.wtf/state-of-the-screen-time-api-2024/

5. **ScreensDesign Analysis: Bible Mode**
   - Detailed UX teardown of Bible Mode app
   - Revenue estimate: $35K/mo, 15K installs/mo, 4.9 stars
   - https://screensdesign.com/showcase/bible-mode-reduce-screen-time

6. **Opal Official Website & Features**
   - https://www.opal.so/ — 300K+ users, 94% less distracted claim
   - Focus Report, Profile, Leaderboard features documented

7. **The Brick / getbrick.app**
   - Physical NFC device for app blocking
   - https://getbrick.com/ — 99%+ screen time reduction, 3.1 hrs less daily

8. **Prayer Lock App Store Listing**
   - https://apps.appfollow.io/ios/prayer-lock-christian-focus/6744703926
   - Subscription-only model; "Put God First" approach

9. **Behavioral Psychology Research**
   - "92% of people fail New Year's goals" — friction is the cause, not willpower
   - "Adding 10 seconds of delay reduces social media usage by 22%"
   - James Clear's "2-Minute Rule" for habit formation
   - Andrew Huberman's "Limbic Friction" concept

10. **RescueTime Features & Dashboard**
    - https://help.rescuetime.com/article/435-rescuetime-for-android-features
    - Productivity Pulse, Focus Sessions, Weekly Reports

### Secondary Sources

11. Medium: "Mastering Apple's Screen Time API (Part 4): Visualizing Data" (2025)
12. Medium: "A Developer's Guide to Apple's Screen Time APIs" (2025)
13. GitHub: react-native-device-activity wrapper for Screen Time APIs
14. Habi: "7 Best Screen Time Apps in 2026 (Tested and Compared)"
15. Goals and Progress: "Best Screen Time Apps: Track Phone Usage Without Self-Punishment"
16. Reddit r/nosurf: User reviews of Clearspace and one sec
17. Product Hunt: Clearspace reviews (4.8 stars, 15 reviews)
18. Bible Mode: https://biblemode.app/ — FAQ, features, testimonials

---

## 6. EXECUTIVE SUMMARY: KEY RECOMMENDATIONS

### The 30-Second Problem
The user's wife is **correct** — 30 seconds is too short. Research shows:
- 30 seconds is enough for a speed bump but NOT enough for meaningful Scripture engagement
- Bible Mode explicitly says "Just 2 minutes to reset with God"
- Lock-screen prayer apps (Pause and Pray) use ~30 seconds and position it as "valuable in 30 seconds, richer if you stay longer"

### The Goldilocks Answer
**Default: 90 seconds (1.5 minutes)** for the standard unlock task, with:
- **Quick option**: 30-45 seconds (read verse aloud)
- **Standard option**: 90 seconds (verse + reflection question) ← DEFAULT
- **Deep option**: 90-120 seconds (verse + prayer response)
- **Quiet Time Mode**: 5-15 minutes (separate feature, not for unlocking)

### Proactive > Reactive
Prayer Lock's "Put God First" approach is the right model: block BEFORE the user falls into scrolling. Combine with:
- Time-limited unlocks (15 min, 30 min, 1 hr, 2 hr) — apps auto-reblock
- Scheduled "God First" hours
- Emergency bypass (limited per day, like Brick's 5 emergency unbricks)

### Screen Time Tracking: Start Simple
Users care most about:
1. Total screen time (daily/weekly)
2. "Times I chose God first" count
3. Time spent with Scripture
4. Streak
5. Trend (improving or not)

Everything else (pickups, notifications, category breakdowns) is P2.

### Differentiator vs Bible Mode
Bible Brick should differentiate from Bible Mode by:
1. **Brick-building visualization** (literal "brick" metaphor — build a wall with God)
2. **Memorization mode** (type verses from memory — active recall, not passive reading)
3. **Voice prayer mode** (record a prayer response — more personal than typing)
4. **Free tier available** (Bible Mode is mostly free; Prayer Lock is 100% subscription)
5. **Physical device option** (like The Brick — NFC tag that says "In God We Trust")

---

*Research compiled from 40+ sources including academic papers (PNAS), Apple WWDC documentation, app store listings, developer blogs, user reviews, and behavioral psychology research.*
