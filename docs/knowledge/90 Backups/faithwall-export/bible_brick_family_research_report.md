# Bible Brick: Family Adoption Research Report
## Comprehensive Guide to Multi-Device Family App Blocking & Bible Engagement

---

# 1. iOS Family Setup

## 1.1 How Apple Family Sharing + Screen Time Works

### Architecture Overview

Apple's family management system operates through two interconnected layers:

1. **Family Sharing** - The identity/account layer that connects family members' Apple IDs
2. **Screen Time** - The control layer that manages device usage

**Family Sharing Fundamentals:**
- Up to 6 family members can be in a group
- One adult is the "family organizer" who pays for purchases
- Children under 13 MUST have a Child Account created by a parent (age varies by country)
- Teens 13-17 now get automatic protections (web filters, Communication Safety) enabled by default as of iOS 26 (2025)
- All family members must have separate Apple IDs

**Screen Time for Families:**
- Parents can manage a child's Screen Time remotely from their own device
- Settings sync across all devices signed into the same Apple ID
- Parents set: Downtime, App Limits, Communication Limits, Content & Privacy Restrictions
- Child can "Ask for More Time" which parent approves via Messages or Settings

### The Screen Time API for Third-Party Developers

Apple introduced the Screen Time API in iOS 15 (2021), expanded in iOS 16. It consists of three frameworks:

| Framework | Purpose |
|-----------|---------|
| **FamilyControls** | Authorization + app selection via privacy-preserving tokens |
| **ManagedSettings** | The "enforcer" - sets restrictions, shields apps, filters web |
| **DeviceActivity** | Scheduling when restrictions apply + background execution |

**How Family Authorization Works:**

```
Parent device          Child device
     |                       |
     |--app installed on BOTH devices-->
     |                       |
     |--parent opens app on child's phone-->
     |                       |
     |--child requests authorization(.child)-->
     |                       |
     |--guardian approves with Apple ID auth-->
     |                       |
     |--app now authorized on child's device-->
     |                       |
     |--parent configures restrictions from their app-->
     |--(data syncs to child device via your backend)-->
     |                       |
     |                       |--DeviceActivityMonitor runs-->
     |                       |--ManagedSettings applies shields-->
```

**Critical iOS 16+ Change:** iOS 16 added `.individual` authorization mode, which means ANY user (not just family members) can authorize an app to manage their own Screen Time. This is how self-control apps like Opal work. For Bible Brick's family use case, you'd use `.child` authorization on the child's device.

### Key Technical Details

**Required Entitlement:**
- Must apply for `com.apple.developer.family-controls` entitlement from Apple
- Must apply for EVERY app target (main app + extensions)
- Apple reviews and approves/denies - not guaranteed
- Can take weeks to months to get approved
- Without this, Screen Time APIs simply won't work

**Authorization Modes:**
```swift
// For family/parental control use case
try await AuthorizationCenter.shared.requestAuthorization(for: .child)

// For self-control use case
try await AuthorizationCenter.shared.requestAuthorization(for: .individual)
```

**What Happens After Family Controls Authorization:**
1. Child cannot sign out of iCloud without guardian approval
2. App cannot be removed from device without guardian approval (in theory)
3. Privacy-preserving tokens represent apps/websites - developers never see actual app names
4. DeviceActivity extensions run in background even when child doesn't open the app

## 1.2 Can a Parent Install an App on a Child's iPhone Remotely?

**Answer: PARTIALLY YES, with major caveats.**

**Methods:**

| Method | How It Works | Limitations |
|--------|-------------|-------------|
| **Ask to Buy** | Child requests app download; parent approves from their device | Child must initiate; doesn't work for free apps if child is over 13 |
| **Family Purchases** | Apps purchased by family members are available to download on child's device | Child must manually go to App Store > family purchases and tap download |
| **Screen Time Remote Install** | Not possible - Apple has no API for remote app installation | N/A |
| **MDM (Enterprise)** | Can push apps remotely | Requires Apple Business Manager, complex setup, not consumer-friendly |

**Practical Reality:**
- For Bible Brick, the parent CANNOT remotely install the app on the child's device
- **The parent must physically have the child's device** to install Bible Brick
- Or the child must install it themselves from the App Store
- After installation, parent CAN configure it remotely (via Screen Time API + your backend)

**Apple's Official Setup Process (iOS 16+):**
1. Parent uses Quick Start to set up child's new device
2. Child's Apple ID is created or linked
3. Parent configures Screen Time during setup
4. Bible Brick would need to be installed AFTER this setup, either by parent or child

## 1.3 Can a Parent Control App Permissions on a Child's Device?

**Answer: YES, through several mechanisms:**

1. **Content & Privacy Restrictions** - Parent can prevent installation/deletion of apps, prevent in-app purchases, restrict which apps appear
2. **Screen Time App Limits** - Set time limits per app or category
3. **ManagedSettings (via Screen Time API)** - Bible Brick can use this to shield apps, prevent account changes, filter web content
4. **Ask to Buy** - Requires parent approval for any paid app download

**What Bible Brick Can Do via ManagedSettings:**
```swift
// Shield specific apps (block them)
store.shield.applications = selectedApps

// Prevent app removal during active brick
ManagedSettingsStore().application.denyAppRemoval = true

// Prevent account changes
store.account.lockAccounts = true

// Filter web content
store.shield.webDomains = blockedDomains
```

## 1.4 Age Restrictions (Apple IDs for Kids Under 13)

**Apple's Age Tiers:**

| Age | Requirements | Capabilities |
|-----|-------------|--------------|
| **Under 13** | MUST have Child Account created by parent via Family Sharing | Full parental controls, Ask to Buy required, cannot create own account |
| **13-17** | Standard Apple Account, but gets automatic protections (as of iOS 26) | Can have own account, but Screen Time protections enabled by default |
| **18+** | Full adult account | Self-manages Screen Time |

**Key Points:**
- Child accounts CANNOT be removed from Family Sharing by the child
- Only the organizer can remove them (and only after child turns 13)
- Screen Time passcode is separate from device passcode
- Parent should set a passcode the child cannot guess

## 1.5 How "Ask to Buy" and Screen Time Limits Translate to Third-Party Apps

**Ask to Buy:**
- Applies to PAID app downloads and in-app purchases
- Does NOT apply to free apps (for children 13+)
- Parents get a notification to approve/decline
- Third-party apps like Bible Brick cannot directly use this system

**Screen Time Limits + Third-Party Apps:**
- When Bible Brick uses the Screen Time API to shield apps, the shield appears as an OS-level overlay
- The child sees Bible Brick's custom shield screen (customizable with your branding)
- If the child tries to open a blocked app, they see your shield instead
- Child can "Ask for Access" which can send a notification to the parent
- Parent can approve via Messages or Settings > Screen Time

## 1.6 Can Bible Brick Use Screen Time API on a Child's Device Through Family Sharing?

**Answer: YES, but with specific requirements:**

**What IS Possible:**
- Bible Brick installed on child's device can authorize with Family Controls
- Parent can configure which apps to block from Bible Brick's parent dashboard
- Restrictions sync to child's device via your own backend (Firebase, etc.)
- DeviceActivityMonitor runs in background and applies shields automatically
- Custom shield screens with Bible branding
- Can prevent app removal during active brick sessions

**What is NOT Possible:**
- Bible Brick on parent's device CANNOT directly set restrictions on child's device
- Parent MUST open Bible Brick on child's device at least once to authorize it
- Cannot read child's messages, call logs, or YouTube history
- Cannot prevent child from disabling Screen Time permissions entirely (child can go to Settings > Screen Time > Apps with Screen Time Access and toggle off - though Family Controls authorization makes this harder)
- Cannot bypass the initial physical setup requirement

**The Screen Time Permission Problem (Major Issue):**
Apple's native Screen Time settings can be locked with a passcode. But third-party app Screen Time permissions CANNOT be locked the same way. A child can go to Settings > [App Name] > Screen Time Restrictions and revoke Bible Brick's access. This is a documented limitation (FB18794535) that Apple has not fixed.

**Workaround:** Family Controls authorization (the `.child` mode) provides stronger protection - the child cannot simply revoke it, and the app cannot be deleted without guardian approval. But this requires the guardian to have physically authorized the app on the child's device first.

## 1.7 Technical Limitations: What Can and Can't Be Done on iOS

### CAN DO:
- Shield/block specific apps and app categories
- Shield web domains in Safari
- Schedule automatic blocking (DeviceActivity schedules)
- Custom shield UI with Bible branding
- Monitor device activity (pickups, usage time) - privacy-preserving
- Prevent app removal during active brick: `denyAppRemoval = true`
- Lock accounts in place
- Prevent password changes
- Set web content filters
- React to usage thresholds (e.g., after 30 min of social media, trigger brick)

### CANNOT DO:
- Read SMS/iMessage content
- Monitor YouTube app history
- Monitor calls
- See which specific websites visited (privacy tokens hide this)
- Prevent app uninstallation entirely (Family Controls helps but isn't absolute)
- Run on Mac (Screen Time API is iOS/iPadOS only, though Apple's native Screen Time works on Mac)
- Access camera/microphone recordings
- Track location (must use separate CoreLocation APIs)
- Block apps without the FamilyControls entitlement from Apple

### Known Bugs and Issues:
1. **Screen Time Passcode Not Compatible** - Screen Time passcode doesn't protect third-party app permissions
2. **DeviceActivityMonitor Memory Pressure** - Extensions frequently crash due to strict memory limits
3. **Cannot Open Parent App from Shield** - No API to deep-link back to Bible Brick from a shield screen (must use notifications as workaround)
4. **Brute Force Screen Time Passcode** - No rate limiting on passcode attempts through "Erase All Content and Settings" flow
5. **No `UIApplication.openURL` from ShieldActionDelegate** - Only `.close`, `.none`, and `.defer` actions available
6. **App Review Scrutiny** - Apple heavily reviews apps using Screen Time API; easy to get rejected

---

# 2. Android Family Setup

## 2.1 How Google Family Link Works

Google Family Link is a free parental control app that works across Android and iOS.

**Architecture:**
- Parent installs Family Link app on THEIR device
- Child's device must have a Google Account (child account for under 13)
- Family Link app installed on child's device for supervision
- Controls managed remotely through parent's Family Link app
- Child's Google Account becomes part of parent's Family Group

**What Family Link Controls:**
- App downloads (approve/decline each app)
- Screen time daily limits
- Bedtime schedules
- Device lock (remote)
- Location tracking
- Content filters in Chrome and Google Search
- YouTube Restricted Mode
- In-app purchase approvals

## 2.2 Can Parents Install Apps on Kids' Android Devices Remotely?

**Answer: PARTIALLY YES.**

Through Google Play Family Library:
- Parent can purchase apps that become available to the family
- Child can see and install family-shared apps from Google Play
- Parent can approve specific app installations remotely via Family Link
- Parent CANNOT force-install apps without the child's interaction

**For Bible Brick:**
- Parent would need child's device in hand for initial setup
- Bible Brick would need to be installed on child's device
- After install, parent can control it remotely through Family Link + Bible Brick's backend

## 2.3 What Control Does Family Link Give Over Third-Party Apps?

**Family Link App Management:**
- Every new app install requires parent approval (for supervised accounts under 13)
- Parent can block specific apps entirely
- Parent can set daily time limits per app
- Parent can see how much time child spends in each app
- Parent can hide/unhide apps on child's device

**For Bible Brick Integration:**
- Bible Brick can be installed and given special permissions
- Family Link will NOT interfere with Bible Brick's device admin or accessibility permissions
- Bible Brick operates BELOW Family Link in the permission hierarchy
- Family Link + Bible Brick can work together (complementary)

## 2.4 Can Bible Brick Work as a Device Admin on a Child's Phone?

**Answer: YES, and this is the recommended approach for Android.**

**Device Admin vs. Device Owner:**

| Mode | How It Works | Use Case |
|------|-------------|----------|
| **Device Admin** | App requests admin privileges; user grants them | Consumer parental control apps |
| **Device Owner** | Set up during device provisioning (factory reset required) | Enterprise MDM, school devices |

**For Bible Brick:**
- Request `BIND_DEVICE_ADMIN` permission
- Implement `DeviceAdminReceiver`
- User grants admin rights during setup
- Once granted, Bible Brick can:
  - Lock the device
  - Wipe data (extreme measure)
  - Disable cameras
  - Enforce password policies
  - Prevent uninstallation (to some degree)

**Critical Note:** Android has been deprecating Device Admin APIs since Android 9 (API 28). Google recommends moving to Android Enterprise (Device Owner/Profile Owner) for new apps. However, many parental control apps still use Device Admin for consumer use cases.

## 2.5 Accessibility Service Permissions: Can a Parent Grant These Remotely?

**Answer: NO - Accessibility Services MUST be granted on the device itself.**

**How Accessibility Services Work for Parental Control:**
- App requests Accessibility Service permission
- User must go to Settings > Accessibility > [App Name] > Enable
- This requires PHYSICAL interaction with the device
- Cannot be granted remotely by parent

**What Accessibility Services Enable:**
- Detect which app is currently in foreground
- Monitor window changes
- Detect when user tries to open blocked apps
- Intercept and block actions (e.g., show overlay instead)
- Some apps use this to implement app blocking without Device Admin

**For Bible Brick Setup:**
- Parent must have child's device in hand
- Child must accept Bible Brick as Accessibility Service
- This is a ONE-TIME setup step
- After setup, Bible Brick can operate autonomously

## 2.6 Technical Limitations on Android

### CAN DO:
- Block apps using Device Admin or Accessibility Service
- Lock device remotely
- Monitor app usage in real-time
- Set time limits per app
- Filter web content (via VPN service)
- Track location
- Monitor SMS (with appropriate permissions)
- Set itself as Device Admin to resist uninstallation
- Use Accessibility Service to detect and intercept app launches
- Run background services for continuous monitoring

### CANNOT DO:
- Install apps remotely without user interaction
- Grant Accessibility Service permission remotely
- Fully prevent uninstallation on non-Samsung devices (though Device Admin makes it harder)
- Monitor content inside encrypted apps (WhatsApp, Signal) without breaking encryption laws
- Block apps on Android 10+ without Accessibility Service or Device Admin
- Bypass Google's Play Protect if flagged as potentially harmful

### Known Bypass Methods on Android:
- **Safe Mode** - Boot into safe mode disables third-party apps including parental controls
- **Factory Reset** - Wipes everything including parental control apps
- **Multiple User Profiles** - Create unrestricted secondary user account
- **Developer Options / ADB** - Can disable device admin via USB debugging
- **App Cloning** (MIUI, Samsung) - Cloned apps may bypass restrictions
- **Secure Folders** (Samsung) - Can install apps in encrypted space invisible to parental controls
- **Third-party App Stores** - Install unvetted apps that bypass Google Play restrictions

---

# 3. Cross-Platform Family Dashboard Research

## 3.1 Covenant Eyes: Family/Ally System

**Model: Accountability Partner (NOT Blocking)**

**How It Works:**
- User installs Covenant Eyes on their device
- User selects an "Ally" (spouse, parent, friend, mentor)
- App takes periodic screenshots of device activity
- AI analyzes screenshots for inappropriate content
- Screenshots are BLURRED for privacy before sending to ally
- Ally receives activity feed and can check in with user
- No app blocking - purely monitoring and accountability

**Family Features:**
- One user + multiple allies possible
- Activity feed shows time spent, apps used, flagged content
- Real-time alerts for concerning activity (with delay)
- Educational mini-courses
- Community features

**Pricing:** $19.99/month per user

**Limitations for Bible Brick's Use Case:**
- Does NOT block apps (monitoring only)
- No screen time limits
- No location tracking
- Screenshots are blurry (can't verify actual content)
- No family dashboard showing multiple children
- High false positive rate causes family conflict

**What Bible Brick Can Learn:**
- The "Ally" concept is powerful for spouse-to-spouse accountability
- Blurred screenshots balance privacy with accountability
- Activity feed + check-in model works well for trust-building
- The accountability MODEL (not surveillance) resonates with Christian values

## 3.2 Qustodio / Bark / Net Nanny: Family Dashboard Patterns

### Qustodio

**Family Dashboard:**
- Parent app shows all children's devices in a list
- Tap a child to see: screen time, app usage, web activity, location
- Can set rules per child (different ages get different limits)
- Real-time location tracking
- SOS panic button for child
- Geofencing alerts

**Setup Pattern:**
1. Parent creates account, installs app on their device
2. Parent installs "Qustodio Kids" app on child's device
3. Child's app pairs with parent account via QR code or email link
4. Parent configures rules from dashboard

### Bark

**Family Dashboard:**
- Unlimited devices per subscription
- Covers 30+ social media platforms and apps
- AI monitors messages, posts, emails for concerning content
- Alerts parents to: cyberbullying, predators, suicidal ideation, drugs, etc.
- Does NOT block apps; alerts-only model

**Setup Pattern:**
1. Parent signs up at bark.us
2. Child installs Bark app on their devices
3. Child connects social media accounts
4. Bark monitors in background, alerts parent to issues

### Net Nanny

**Family Dashboard:**
- Device-count based pricing (1/5/20 devices)
- Real-time content filtering
- Screen time management
- Location tracking
- Alerts for concerning search terms

### Common UX Patterns Across These Apps:

| Pattern | Implementation |
|---------|---------------|
| **Child List** | Vertical list of children with avatar, name, device status |
| **Device Status Card** | Shows online/offline, current screen time, location |
| **Rule Configuration** | Per-child settings: app limits, bedtimes, filters |
| **Activity Timeline** | Chronological feed of child's app usage |
| **Alert/Notification Center** | Red badges for concerning activity or time limit reached |
| **Map View** | Child's current location with geofence zones |

## 3.3 Circle Home Plus: Device-Level Family Controls

**Model: Network-Level Hardware + App**

**How It Works:**
- Physical device ("puck") plugs into home router
- Intercepts all network traffic via ARP spoofing
- Filters content at the network level for ALL connected devices
- Works on: phones, tablets, gaming consoles, smart TVs, computers
- Companion app for parent controls

**Family Features:**
- One control panel for all home devices
- "Pause Internet" button (per device or whole house)
- Age-based filter profiles (pre-k, kid, teen, adult)
- Time limits per category (social, games, videos)
- Bedtime scheduling
- Rewards system (extra time for good behavior)

**Limitations:**
- Only controls WiFi traffic (cellular data bypasses it completely)
- Must use Circle Go (VPN subscription) for away-from-home control
- Single device can't be in multiple profiles
- Tech-savvy kids can bypass with VPN

**What Bible Brick Can Learn:**
- The "pause internet" / "force brick" concept is powerful
- Rewards system (earning screen time) reduces family friction
- Age-based profiles simplify setup
- Physical hardware creates commitment (like The Brick's puck)

## 3.4 Opal: Does It Have Family Features?

**Answer: NO - Opal is purely individual-focused.**

**Opal Features:**
- App blocking with custom schedules
- Focus sessions with intention-setting
- Deep Focus mode (can't be bypassed)
- Detailed analytics (pickups, screen time, focus score)
- Gamification (gems, streaks, leaderboard)
- iOS and Mac only

**What Opal Lacks:**
- No family sharing whatsoever
- No parent dashboard
- No multi-device management
- No accountability partner model
- Each user manages their own settings

**What Bible Brick Can Learn from Opal:**
- Beautiful, gamified UX (gems, streaks, leaderboards)
- Deep Focus mode concept (strict, non-bypassable blocking)
- Excellent analytics presentation
- Clean, intention-focused session design
- The "Temporarily brick your phone" preset mode

## 3.5 The Brick: How Multi-Device Works With One Puck

**Model: Physical NFC Device + App**

**How It Works:**
- $59 one-time purchase (no subscription)
- Physical puck uses NFC to pair with phones
- To "Brick" phone: tap phone to puck
- To "unBrick": tap phone to puck again
- If you leave home without the puck, you CANNOT unBrick
- 5 emergency unBricks available in app (must email support to refresh)

**Multi-Device:**
- ONE puck works with UNLIMITED phones
- Cross-platform (iOS + Android)
- A whole household can share one puck
- One phone can also pair with multiple pucks (home, car, work)

**Modes:**
- Block ALL apps
- Block specific apps
- Allow-list mode (only essential apps)
- Up to 10 scheduled modes

**Strict Mode:**
- Prevents deleting the app during active brick
- Prevents changing settings to bypass brick

**What Bible Brick Can Learn:**
- The physical commitment device concept is powerful
- One-device-controls-many model is family-friendly
- Strict mode prevents circumvention
- Scheduled modes automate enforcement
- No subscription = easier adoption

**Limitations:**
- Must remember to carry the puck
- No remote management (parent can't brick child's phone from their own phone)
- No analytics or usage data
- No content filtering
- If child has their own puck, self-control only (no parent oversight)

## 3.6 Best UX Patterns for Family Dashboard

### Family Invite System Options:

| Method | Pros | Cons |
|--------|------|------|
| **QR Code** | Fast, no typing, works offline | Requires physical proximity |
| **Email Link** | Remote, familiar pattern | May go to spam, requires email setup |
| **SMS Code** | Universal, works on all phones | SMS costs, delivery reliability |
| **Family Code** (6-digit) | Easy to type, share verbally | Less secure, could be guessed |
| **Deep Link** | Seamless app-to-app | Requires app already installed |

**Recommended for Bible Brick: Hybrid approach**
1. Parent generates a family invite code (e.g., "BIBLE-BRICK-7X2K")
2. Child enters code in their app OR scans QR code
3. For younger kids: parent enters code on child's device during setup
4. For teens: can share via text/Message

### Parent Dashboard Features That Work Best:

**Top-Bar:**
- Family selector (switch between children)
- Notification bell (red badge for alerts)

**Child Status Card:**
- Avatar + name + online indicator
- Current screen time today
- Active brick status (is phone currently bricked?)
- Last seen location
- Daily streak count
- Bible reading progress

**Quick Actions:**
- "Force Brick" button (instantly bricks child's phone)
- "Unbrick" button
- "Add 15 min" reward button
- "Request Reading" sends Bible task

**Activity Feed:**
- Timeline of today's events
- "Emma started a brick session (30 min)"
- "Emma completed John 3 reading"
- "Emma tried to open TikTok (blocked)"
- "Emma's screen time: 2h 30m today"

**Bible Engagement Section:**
- Child's reading streak
- Verses memorized
- Reading plan progress
- Parent can assign Bible tasks

---

# 4. The "Teen Problem"

## 4.1 How Teens Typically Bypass Parental Controls

### iOS Bypass Methods:

1. **Changing Time Zone** - Reset app limits by switching to a different time zone
2. **Deleting and Reinstalling Apps** - Removes per-app Screen Time limits
3. **Using Siri** - Send messages via voice to bypass app limits on Messages
4. **Screenshots to Share** - Take screenshot, use share button to send without opening Messages
5. **Screen Recording** - Record video content during allowed time, watch later in Photos
6. **Screen Time Passcode Guessing** - Watch parent enter code, or brute-force through Erase flow
7. **Factory Reset** - Wipes all Screen Time settings (nuclear option)
8. **Using a Second Device** - Unrestricted iPad, friend's phone, etc.
9. **Disabling VPN** (for filter-based apps) - Turn off VPN to bypass content filtering
10. **Private/Incognito Browsing** - No history, no cookie-based filters

### Android Bypass Methods:

1. **Safe Mode** - Boots without third-party apps; uninstall parental control app
2. **Factory Reset** - Wipes everything
3. **Multiple User Profiles** - Create unrestricted secondary account
4. **ADB/Developer Options** - USB debugging to disable device admin
5. **App Cloning** (Samsung, Xiaomi) - Clone apps to bypass restrictions
6. **Secure Folders** (Samsung) - Install apps in encrypted hidden space
7. **Third-Party App Stores** - Download apps outside Google Play
8. **Clearing Google Play Store Data** - Removes Family Link settings
9. **Accessibility Menu Exploit** - Can reopen apps after time limits lock device
10. **VPN** - Bypasses network-level filtering
11. **Hidden Browsers** - Open browsers from within Google Play Services help links

## 4.2 Technical Measures to Prevent Uninstallation

### iOS:

**Screen Time API Protections:**
- `ManagedSettingsStore().application.denyAppRemoval = true` - Prevents app deletion during active brick
- Family Controls `.child` authorization prevents iCloud sign-out and app removal without guardian approval
- BUT: child can still go to Settings > App > Screen Time Restrictions and toggle off (known Apple bug)

**Best Practices:**
1. Use `.child` authorization mode (strongest protection)
2. Set `denyAppRemoval = true` during active sessions
3. Parent sets Screen Time passcode child doesn't know
4. Prevent app installation/deletion in Content & Privacy Restrictions
5. Regular check-ins to verify app is still active

### Android:

**Device Admin Protection:**
- Set Bible Brick as Device Admin
- When user tries to uninstall, they must first revoke Device Admin (extra step)
- On Samsung devices: integrate with Samsung Knox for stronger protection
- Use `DeviceAdminReceiver` to detect when admin is being disabled

**Accessibility Service:**
- Running accessibility service makes app harder to disable
- Can detect when user tries to open Settings and intervene

**Best Practices:**
1. Combine Device Admin + Accessibility Service
2. On Samsung: use Samsung Knox SDK
3. Hide app from app drawer (optional, may cause suspicion)
4. Monitor for uninstall attempts and alert parent
5. Multiple protection layers (if one is bypassed, others remain)

## 4.3 Strict Mode: Preventing Deletion During Active Brick

**What "Strict Mode" Means:**
- When a brick session is active, the app cannot be deleted
- Settings cannot be changed to bypass the brick
- Device cannot be used to factory reset
- Emergency unbrick requires parent approval or physical interaction

**iOS Implementation:**
```swift
// During active brick session:
let store = ManagedSettingsStore()
store.application.denyAppRemoval = true
store.account.lockAccounts = true

// When brick session ends:
store.application.denyAppRemoval = false
```

**Android Implementation:**
```kotlin
// During active brick session:
devicePolicyManager.setCameraDisabled(adminComponent, true) // optional
devicePolicyManager.addUserRestriction(adminComponent, UserManager.DISALLOW_FACTORY_RESET)

// When brick session ends:
devicePolicyManager.clearUserRestriction(adminComponent, UserManager.DISALLOW_FACTORY_RESET)
```

**Important Note:** No strict mode is 100% effective. A determined teen with physical device access can eventually bypass anything (factory reset is the nuclear option). The goal is to make it DIFFICULT enough that most teens won't bother, and to create opportunities for conversation.

## 4.4 Accountability Partner Model (Covenant Eyes Approach)

**Why This Works for Teens:**
- Shifts from "parent controls me" to "I choose accountability"
- Works even when technical controls fail
- Builds trust rather than enforcing obedience
- Aligns with biblical principles of confession and community
- Suitable for older teens who resist surveillance

**Implementation for Bible Brick:**
- Teen can choose an accountability partner (parent, youth leader, mentor, sibling)
- Partner gets notifications of brick completions and Bible reading
- Partner can see (limited) activity feed
- Partner can send encouragement messages through the app
- Teen can see partner's activity too (mutual accountability)

## 4.5 Open Communication vs. Surveillance Balance

**The Surveillance Problem:**
- Heavy monitoring breeds resentment and secrecy
- Teens who feel watched find ways to hide behavior
- Constant alerts create parent anxiety and nagging
- Focus shifts from character-building to rule-following

**The Communication Solution:**
1. **Transparency** - Child knows what the parent can see
2. **Collaborative Setup** - Child participates in setting limits
3. **Graduated Autonomy** - More freedom as trust is earned
4. **Regular Conversations** - Weekly "digital wellness check-in"
5. **Focus on Positive** - Celebrate streaks and completions, not just violations
6. **Age-Appropriate Controls** - Younger kids need more enforcement; older teens need more accountability

---

# 5. Implementation Recommendations

## 5.1 Family Setup Flow

### Recommended Onboarding Flow (Parent First):

```
STEP 1: PARENT installs Bible Brick on their own phone
  |
  v
STEP 2: Parent creates account (email/Apple/Google sign-in)
  |
  v
STEP 3: Parent creates a "Family" (named group, e.g., "The Johnsons")
  |
  v
STEP 4: Parent taps "Add Family Member"
        - Options: "Add Child" or "Add Spouse/Partner"
  |
  v
STEP 5: For Child:
        - Generate invite code + QR code
        - Options to share: Airdrop, Message, Email, show QR
        - Parent takes child's device and completes setup
        |
        v
        On CHILD's device:
        - Install Bible Brick (from App Store/Play Store)
        - Open app, tap "Join Family"
        - Enter invite code or scan QR
        - Child's device requests Screen Time / Device Admin permissions
        - Parent grants permissions on child's device
        - Bible Brick is now linked to family
        |
        v
STEP 6: Parent configures initial settings from dashboard
        - Default Bible reading tasks
        - App blocking preferences
        - Screen time limits
  |
  v
STEP 7: For Spouse/Partner:
        - Similar invite flow
        - Spouse gets EQUAL access to family dashboard
        - Spouse can manage children AND see each other's stats
        - Accountability partner features enabled
```

### Per-Member-Type Setup:

**Parent (Admin):**
- Full dashboard access
- Can manage all family members
- Can force brick any child's device
- Receives all notifications

**Spouse/Partner (Co-Admin):**
- Full dashboard access
- Can manage children
- Can see mutual accountability stats
- Can force brick children's devices
- Can see (but not control) other parent's stats if agreed

**Child (Managed):**
- Can see own stats, streaks, Bible reading progress
- Can see parent's stats if parent opts in (modeling behavior)
- Can start self-bricks
- Cannot change family settings
- Cannot remove app without parent approval

## 5.2 Parent Dashboard Feature Spec

### MVP Dashboard Features:

**Family Overview Screen:**
```
+--------------------------------------------------+
|  The Johnson Family          [+] Add Member      |
+--------------------------------------------------+
|                                                  |
|  [Emma]              [Noah]            [Dad]     |
|  Online              Offline           Online    |
|  2h 15m today        1h 30m today      --        |
|  [Brick Active]      [Unlocked]        [Streak:7]|
|  [Force Brick]       [Force Brick]               |
|                                                  |
+--------------------------------------------------+
|  Recent Activity                                 |
|  - Emma completed John 3 (5 min ago)             |
|  - Noah's TikTok blocked (12 min ago)            |
|  - Emma started 30-min brick (1h ago)            |
+--------------------------------------------------+
|  Quick Actions                                   |
|  [Brick All Kids]  [Assign Reading]  [Rewards]   |
+--------------------------------------------------+
```

**Child Detail Screen:**
```
+--------------------------------------------------+
|  < Back        Emma (Age 12)         [Settings]  |
+--------------------------------------------------+
|  Today: 2h 15m / 3h limit                        |
|  [===========--------] 75%                       |
|  Bible Reading: John 3:16 (completed)             |
|  Streak: 5 days                                  |
+--------------------------------------------------+
|  App Usage Today                                 |
|  TikTok     [====] 45m  (limit reached)         |
|  YouTube    [===]  30m  (15m remaining)         |
|  Games      [==]   20m  (10m remaining)         |
|  Bible App  [=]    15m  (encouraged!)           |
+--------------------------------------------------+
|  Active Brick Sessions                           |
|  Study Time (ends in 25 min) [End Early]         |
+--------------------------------------------------+
|  [Force Brick Now]  [Add 15m Reward]             |
|  [Assign Bible Task]  [View Full History]        |
+--------------------------------------------------+
```

**Notification Types for Parents:**
1. **"Emma completed her Bible reading!"** - Positive reinforcement
2. **"Noah's screen time limit reached for TikTok"** - Informational
3. **"Emma requested more time on Games"** - Action required (approve/decline)
4. **"Noah tried to open a blocked app"** - Alert
5. **"Bible Brick was disabled on Noah's device"** - Urgent alert (circumvention)
6. **"Emma started a 30-min brick session"** - Informational
7. **"Daily family summary: Average screen time down 15%"** - Encouragement

### Phase 2 Dashboard Features:
- Location tracking (with geofencing)
- Detailed weekly reports (email summary)
- Custom reward system (parent can create custom rewards)
- Bible reading plans for family
- Family devotion time scheduling
- Sibling challenges (who can keep the longest streak?)

### Phase 3 Dashboard Features:
- AI-powered insights ("Emma uses TikTok most between 8-10pm")
- Predictive alerts ("Noah's screen time trending high today")
- Integration with church/small group leader accounts
- Bible verse memory competitions
- Parent community features

## 5.3 Kid's Experience

**What Kids CAN See:**
- Their own screen time stats (pickups, usage by app)
- Their Bible reading progress and streaks
- Active brick sessions and time remaining
- Their own achievements/gems
- Parent's screen time IF parent opts in (modeling transparency)
- Family leaderboard (who has the longest streak?)
- Bible reading challenges

**What Kids CANNOT See:**
- Sibling's detailed app usage (respect privacy between siblings)
- Parent's detailed app usage without opt-in
- Family settings and controls
- Notification history about their own behavior

**Kid's App Screens:**

```
+--------------------------------------------------+
|  My Dashboard                         [Settings] |
+--------------------------------------------------+
|                                                  |
|  [Trophy] 5-Day Streak!                         |
|  "Great job reading God's Word daily!"           |
|                                                  |
|  Today's Screen Time: 2h 15m                     |
|  [===========--------]                           |
|  Goal: 3 hours                                   |
|                                                  |
|  My Bible Reading                                |
|  [John 3:16] Read 5 min ago                      |
|  [Start Today's Reading]                         |
|                                                  |
|  Active Bricks                                   |
|  Study Time (22 min left)                        |
|                                                  |
|  [Start a Brick Session]                         |
|                                                  |
+--------------------------------------------------+
```

## 5.4 Technical Architecture for Family Groups

### Firestore Data Structure:

```typescript
// Collection: families
// Document: {familyId}
{
  familyId: "fam_abc123",
  name: "The Johnson Family",
  createdAt: Timestamp,
  inviteCode: "BIBLE-BRICK-7X2K",  // For adding new members
  inviteCodeExpiry: Timestamp,
  settings: {
    defaultScreenTimeLimit: 180,  // minutes
    defaultBedtime: "21:00",
    requireReadingBeforeScreenTime: false,
    allowSelfBricks: true,
    strictMode: true
  }
}

// Collection: familyMembers (subcollection of families)
// Document: {memberId}
{
  memberId: "user_def456",
  familyId: "fam_abc123",
  role: "parent",  // "parent" | "child" | "spouse"
  displayName: "Sarah Johnson",
  avatarUrl: "https://...",
  age: null,  // null for adults
  email: "sarah@email.com",
  deviceType: "ios",  // "ios" | "android"
  deviceId: "device_abc",
  screenTimeAuthorized: true,  // Screen Time API / Device Admin active
  joinedAt: Timestamp,
  isOnline: true,
  lastSeenAt: Timestamp,
  
  // Permissions
  permissions: {
    canForceBrickOthers: true,
    canManageSettings: true,
    canSeeFamilyStats: true,
    canSeeParentStats: true  // For children: can they see parent's usage?
  },
  
  // Screen Time Settings (child-specific)
  screenTimeSettings: {
    dailyLimitMinutes: 180,
    bedtimeStart: "21:00",
    bedtimeEnd: "07:00",
    blockedApps: ["token_tiktok", "token_instagram"],
    allowedApps: ["token_bible", "token_messages"],
    requireReadingBeforeAccess: true
  }
}

// Collection: brickSessions
// Document: {sessionId}
{
  sessionId: "session_ghi789",
  familyId: "fam_abc123",
  userId: "user_def456",  // Who initiated
  targetUserId: "user_jkl012",  // Whose device is being bricked
  type: "parent_forced",  // "parent_forced" | "self_initiated" | "scheduled"
  status: "active",  // "active" | "completed" | "cancelled"
  startedAt: Timestamp,
  endsAt: Timestamp,
  durationMinutes: 30,
  blockedApps: ["token_tiktok", "token_instagram"],
  allowList: ["token_bible", "token_messages"],
  reason: "Bible reading time",
  isStrictMode: true,
  endedBy: null,  // userId of who ended it
  endedAt: null,
  cancelledAt: null,
  cancelledBy: null
}

// Collection: bibleTasks
// Document: {taskId}
{
  taskId: "task_mno345",
  familyId: "fam_abc123",
  assignedBy: "user_def456",  // Parent who assigned
  assignedTo: "user_jkl012",  // Child
  passage: "John 3:16-21",
  title: "God's Love for the World",
  description: "Read and reflect on God's amazing love",
  type: "reading",  // "reading" | "memorization" | "devotion"
  status: "assigned",  // "assigned" | "in_progress" | "completed" | "overdue"
  assignedAt: Timestamp,
  dueBy: Timestamp,
  completedAt: null,
  completionNote: null,  // Child can add a reflection
  rewardUnlocked: null  // e.g., "15_min_screen_time"
}

// Collection: activityLog (for parent dashboard feed)
// Document: {activityId}
{
  activityId: "act_pqr678",
  familyId: "fam_abc123",
  userId: "user_jkl012",  // Who performed the action
  type: "bible_reading_completed",  // "app_blocked" | "bible_reading_completed" | "brick_started" | "brick_ended" | "screen_time_limit_reached" | "app_uninstall_attempted" | "force_brick" | "reward_earned"
  title: "Emma completed John 3",
  description: "Read for 8 minutes and reflected on verse 16",
  severity: "info",  // "info" | "warning" | "alert"
  relatedTaskId: "task_mno345",
  relatedSessionId: null,
  createdAt: Timestamp,
  readBy: ["user_def456"]  // Array of parent userIds who read this
}

// Collection: streaks
// Document: {streakId}
{
  streakId: "streak_stu901",
  familyId: "fam_abc123",
  userId: "user_jkl012",
  type: "bible_reading",
  currentStreak: 5,
  longestStreak: 12,
  lastCompletedDate: Timestamp,
  totalDaysCompleted: 47
}

// Collection: rewards (parent-defined incentives)
// Document: {rewardId}
{
  rewardId: "reward_vwx234",
  familyId: "fam_abc123",
  name: "Extra 30 Minutes Gaming",
  description: "Earned for 5-day Bible reading streak",
  type: "screen_time_extension",
  value: 30,  // minutes
  requirement: {
    type: "streak",
    streakType: "bible_reading",
    targetDays: 5
  },
  createdBy: "user_def456",
  redeemedBy: ["user_jkl012"],  // Array of userIds who redeemed
  isActive: true
}
```

### Real-Time Sync Architecture:

```
Parent Device          Firestore           Child Device
    |                      |                     |
    |--force brick-------->|                     |
    |   (write brickSession|                     |
    |    document)         |                     |
    |                      |--real-time listener->|
    |                      |                     |
    |                      |                     |--apply brick via
    |                      |                     |  Screen Time API/
    |                      |                     |  Accessibility Service
    |                      |                     |
    |                      |<--update status-----|
    |                      |                     |
    |<--session updated----|                     |
    |                      |                     |
```

### Cloud Functions (Firebase):

```
1. onBrickSessionCreate
   - Send push notification to child's device
   - Update child's device status to "bricked"
   - Log activity to activityLog

2. onBibleTaskComplete
   - Increment streak counter
   - Check if any rewards unlocked
   - Send congratulatory notification
   - Update activityLog

3. onScreenTimeLimitReached
   - Log activity
   - Send notification to parent
   - Optionally auto-brick if configured

4. onAppUninstallAttempted (Android only, via Device Admin callback)
   - Alert parent immediately
   - Log as high-severity activity
   - Lock device temporarily

5. scheduledDailySummary
   - Runs every evening
   - Generates family screen time summary
   - Sends email/push notification to parents
   - Resets daily counters

6. onFamilyMemberJoin
   - Welcome notification
   - Setup onboarding checklist
   - Assign default settings based on age
```

## 5.5 Privacy Considerations

### What Parents SHOULD Be Able to See:
- Screen time totals and app category usage (social, games, video)
- Bible reading completions and streaks
- Whether Bible Brick is active on child's device
- Location (if explicitly enabled and child-aware)
- Brick session history
- Attempts to bypass controls

### What Parents SHOULD NOT See:
- Specific message contents (texts, DMs)
- Specific websites visited within allowed categories
- Private journals or notes
- Photos or camera roll contents
- Voice recordings
- App passwords or login credentials
- Sibling-to-sibling communications

### Privacy Principles for Bible Brick:
1. **Transparency** - Child always knows what is being monitored
2. **Age-Appropriate** - Less monitoring for older teens, more for younger children
3. **Mutual Consent** - Spouses agree on mutual visibility boundaries
4. **Data Minimization** - Only collect what's necessary for the app's purpose
5. **No Selling Data** - Family usage data never sold or shared
6. **Encrypted Storage** - All family data encrypted at rest and in transit

## 5.6 Anti-Circumvention Measures

### Layered Defense Strategy:

```
Layer 1: Screen Time API / Device Admin (OS-level)
Layer 2: Accessibility Service (detects app launches)
Layer 3: VPN Service (web filtering, optional)
Layer 4: denyAppRemoval flag (prevents deletion during brick)
Layer 5: Push notifications to parent (real-time alerts)
Layer 6: Tamper detection (detect if settings changed)
Layer 7: Strict Mode (emergency unbrick requires parent approval)
Layer 8: Accountability partner (social layer)
```

### Specific Technical Measures:

**iOS:**
1. Request `.child` FamilyControls authorization (not `.individual`)
2. Set `denyAppRemoval = true` during active bricks
3. Set `lockAccounts = true` to prevent iCloud sign-out
4. Use DeviceActivityMonitor to enforce restrictions in background
5. Monitor for Screen Time permission revocation via periodic checks
6. Alert parent if app is deactivated or permissions revoked

**Android:**
1. Request Device Admin privileges
2. Request Accessibility Service permission
3. Optional: Samsung Knox SDK integration
4. Set `DISABLE_FACTORY_RESET` during strict mode
5. Monitor for admin disable attempts via DeviceAdminReceiver
6. Run persistent foreground service to survive app killing
7. Hide app icon option (for younger children)

### Tamper Detection:
- Periodic heartbeat from child's device to Firebase
- If heartbeat stops for >5 minutes, alert parent
- Check on app launch if Screen Time permissions are still active
- Verify Device Admin status on each schedule check
- Log all permission changes to activityLog

## 5.7 Communication Templates for Parents

### Template 1: Introducing Bible Brick to Your Child (Ages 6-10)

> Hey [Name]! We're going to try a new app called Bible Brick. It's going to help our family spend more time with God and less time on screens. When you want to play a game, the app will remind you to read a Bible story first. Then you'll earn time to play! We're doing this together as a family - Mom and Dad are using it too. Let's grow closer to God together!

### Template 2: Introducing Bible Brick to Your Teen (Ages 13-17)

> [Name], I want to talk with you about something. I've been concerned about how much time we're all spending on our phones, and I've been convicted about making more room for God in our daily lives. I found an app called Bible Brick that helps with that. It's not about surveillance - it's about intentionality. Here's what it does: it blocks distracting apps until you spend a few minutes in God's Word. You control when you do it, and you earn your screen time back. Mom and I are using it too. I want us to decide together what limits feel fair. What do you think?

### Template 3: Introducing Bible Brick to Your Spouse

> Hey [spouse], I wanted to share something with you. I've been feeling like my phone is crowding out my time with God, and I bet you feel the same sometimes. I found this app called Bible Brick - it's like a digital commitment device. Before we can open social media or games, it asks us to spend a few minutes reading the Bible. We can see each other's progress and keep each other accountable. Want to try it together for a week? No pressure - if it doesn't work for us, we can stop.

### Template 4: When Child Resists

> I know this feels unfair right now, and I get that you're frustrated. This isn't about punishment or control - it's because I love you and I want you to develop a relationship with God that will sustain you your whole life. Technology companies design these apps to be addictive, and even adults struggle with them. I'm asking you to trust me on this. Let's try it for two weeks, and then we'll sit down together and talk about what's working and what isn't. Your voice matters in this.

### Template 5: Celebrating Progress

> [Name], I noticed you've been reading the Bible every day for a week straight! I'm so proud of you. That's not easy, and you're building a habit that will bless you for your whole life. I also noticed our family's screen time is down 20% this week. We're spending more real time together, and I love that. Keep it up - you're doing great!

### Template 6: When Circumvention is Detected

> Hey [Name], I got a notification that the Bible Brick app was turned off on your phone. I want to hear your side of what happened. I'm not angry - I just want to understand. If something about the app isn't working for you, let's talk about it and adjust. But turning it off without talking to me breaks our trust, and that's more important to me than any screen time rule. Can we talk about this?

---

# 6. Implementation Priority

## MVP (Phase 1) - 6-8 Weeks

### Core Features:
- [ ] **User Authentication** - Email, Apple Sign-In, Google Sign-In
- [ ] **Family Creation** - Parent creates family, gets invite code
- [ ] **Family Join** - Members join via invite code/QR
- [ ] **iOS App Blocking** - Screen Time API integration (shield apps)
- [ ] **Android App Blocking** - Accessibility Service integration
- [ ] **Self-Brick** - User can initiate their own brick session
- [ ] **Bible Reading Task** - Before unbricking, complete short Bible reading
- [ ] **Parent Dashboard** - View family members, screen time, brick status
- [ ] **Force Brick** - Parent can remotely brick child's phone
- [ ] **Basic Notifications** - Brick started/completed, reading done
- [ ] **Streak Tracking** - Days in a row of Bible reading

### Platform Support:
- [ ] iOS 16+ (iPhone)
- [ ] Android 10+ (phone)

### Technical:
- [ ] Firebase project setup (Auth, Firestore, Cloud Functions, FCM)
- [ ] Screen Time API entitlement request (Apple) - START EARLY
- [ ] Basic Cloud Functions for real-time sync
- [ ] Push notifications (Firebase Cloud Messaging)

## Phase 2 - 4-6 Weeks After MVP

### New Features:
- [ ] **Scheduled Bricks** - Recurring brick schedules (bedtime, study time)
- [ ] **Spouse/Partner Support** - Co-admin role, mutual accountability
- [ ] **Rewards System** - Earn screen time bonuses for streaks
- [ ] **Family Bible Reading Plans** - Read through books of Bible together
- [ ] **Location Sharing** - Optional family location tracking
- [ ] **Weekly Reports** - Email summaries of family screen time
- [ ] **Custom Block Lists** - Parent can configure which apps to block per child
- [ ] **Screen Time Analytics** - Detailed usage breakdowns
- [ ] **Anti-Circumvention** - denyAppRemoval, Device Admin hardening
- [ ] **Teen Accountability Mode** - Lighter monitoring, more self-management

### Platform Support:
- [ ] iPad support
- [ ] Web dashboard (for parents who prefer desktop)

## Phase 3 - 4-6 Weeks After Phase 2

### New Features:
- [ ] **Small Group Integration** - Church youth group leader oversight
- [ ] **Bible Verse Memorization** - Memory games and tracking
- [ ] **Family Devotions** - Guided family devotion time scheduling
- [ ] **Advanced Analytics** - AI-powered insights and predictions
- [ ] **Custom Reward Creation** - Parents create their own reward system
- [ ] **Emergency Unbrick with Approval** - Child requests, parent approves
- [ ] **Device Agnostic** - Support for managing tablets, Chromebooks
- [ ] **Offline Mode** - Core features work without internet
- [ ] **Multi-language Support** - Spanish, French, etc.

### Platform Support:
- [ ] Apple Watch companion
- [ ] Desktop widget (iOS/macOS)

## Critical Path Items (Start Immediately):

1. **Apply for Apple's FamilyControls Entitlement** - This can take WEEKS or MONTHS. Apply before writing any code.
2. **Set Up Firebase Project** - Foundation for all real-time features
3. **Design Parent Dashboard UX** - This is the make-or-break feature for family adoption
4. **Prototype iOS App Blocking** - Validate Screen Time API works as expected
5. **Prototype Android App Blocking** - Validate Accessibility Service approach
6. **Legal/Privacy Review** - COPPA compliance for children under 13, GDPR if serving EU

## Success Metrics:

| Metric | MVP Target | Phase 2 Target | Phase 3 Target |
|--------|-----------|----------------|----------------|
| Family Accounts Created | 100 | 1,000 | 10,000 |
| Avg Family Size | 2.5 members | 3.0 members | 3.5 members |
| Daily Active Brick Rate | 30% | 50% | 60% |
| Bible Reading Completion | 40% | 60% | 70% |
| 7-Day Retention | 40% | 55% | 65% |
| Parent Satisfaction (NPS) | 30 | 40 | 50 |

---

# Appendix: Screen Time API Quick Reference

## Required Xcode Setup:
1. Add `Family Controls` capability to app target
2. Add `DeviceActivity` extension target
3. Add `ManagedSettings` extension target
4. Add `Shield Configuration` extension target
5. Request entitlement from Apple

## Key Code Patterns:

### Request Authorization (iOS):
```swift
import FamilyControls

do {
    try await AuthorizationCenter.shared.requestAuthorization(for: .child)
} catch {
    print("Authorization failed: \(error)")
}
```

### Block Apps (iOS):
```swift
import ManagedSettings

let store = ManagedSettingsStore()
store.shield.applications = selectedApps
store.application.denyAppRemoval = true
```

### Schedule Monitoring (iOS):
```swift
import DeviceActivity

let schedule = DeviceActivitySchedule(
    intervalStart: DateComponents(hour: 9, minute: 0),
    intervalEnd: DateComponents(hour: 17, minute: 0),
    repeats: true
)

try center.startMonitoring(.dailyBrick, during: schedule)
```

### Device Admin (Android):
```kotlin
// In DeviceAdminReceiver subclass
override fun onDisableRequested(context: Context, intent: Intent): CharSequence {
    // Alert parent that child is trying to disable admin
    sendParentAlert("Child attempting to disable Bible Brick")
    return "Disabling Bible Brick will remove family protections. Are you sure?"
}
```

---

# Sources and References

1. Apple Screen Time API Documentation (developer.apple.com)
2. WWDC 2021 - "Meet the Screen Time API" (Session 10123)
3. WWDC 2022 - "What's New in Screen Time API" (Session 110336)
4. Apple Family Sharing Support (support.apple.com)
5. Google Family Link Documentation (families.google.com)
6. Boomerang Parental Control - iOS Limitations Guide (useboomerang.com)
7. Covenant Eyes Review (airdroid.com, christpulse.com)
8. Circle Home Plus Review (safewise.com, screenwiseapp.com)
9. Opal App Review (opal.so, mindsightnow.com)
10. The Brick Official Site (getbrick.com)
11. NBC Select Brick Review (nbcnews.com)
12. Qustodio/Bark/Net Nanny Comparison (airdroid.com)
13. Teen Bypass Techniques (whitelist.video, pcmag.com, bitdefender.com)
14. Android Parental Control Development Guide (fluper.com)
15. Building Custom Parental Control Solutions (metadesignsolutions.com)
16. Screen Time API State of the Union 2024 (riedel.wtf)
17. Preventing App Removal on iOS (adriatiks.blog)
18. Developer Guide to Screen Time APIs (medium.com/@juliusbrussee)

---

*Report compiled: 2025*
*For: Bible Brick Product Team*
*Classification: Internal Strategy Document*
