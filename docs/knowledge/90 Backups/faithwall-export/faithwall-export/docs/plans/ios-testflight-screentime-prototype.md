# FaithWall iOS TestFlight Screen Time Prototype Scope

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task when native iOS work begins.

**Goal:** Build a native iOS TestFlight prototype that uses Apple-approved Screen Time APIs to shield selected apps/sites and route the household through a KJV FaithWall gate before scrolling.

**Architecture:** Native SwiftUI iOS app with FamilyControls authorization, app/site selection, ManagedSettings shielding, DeviceActivity monitoring, and a local FaithWall unlock flow. The web app remains the buyer/login/payment source of truth; the iOS prototype focuses only on phone-level control proof.

**Tech Stack:** SwiftUI, FamilyControls, ManagedSettings, DeviceActivity, AuthenticationServices or signed token handoff from FaithWall web, TestFlight, Apple Developer account with Screen Time API entitlement request.

---

## Non-negotiable product truth

- The web/PWA version cannot control other iPhone apps.
- Chrome on iPhone cannot run the FaithWall desktop extension.
- Real iPhone app/site shielding requires native iOS APIs and Apple entitlement approval.
- Public copy must say: web app live now; iPhone native control is in prototype/app-store path.

## MVP behavior

### Parent/admin setup

1. Parent installs FaithWall TestFlight app.
2. Parent signs in or connects buyer access.
3. App asks for FamilyControls authorization.
4. Parent selects apps/categories/sites to shield.
5. Parent chooses a FaithWall rule:
   - Always shield selected apps until the FaithWall gate is completed.
   - Or shield during scheduled windows.
6. App applies shields through ManagedSettings.

### Child/household flow

1. Child opens a shielded app/site.
2. iOS shows the shield UI or routes to FaithWall depending on what Apple permits.
3. Child opens FaithWall.
4. FaithWall shows a KJV verse and one obedience action.
5. Child taps/answers completion.
6. App temporarily unshields selected apps for the configured window.
7. Window expires; shield returns.

## Apple APIs to validate first

- `FamilyControls`
  - Request authorization.
  - Present app/category/site picker.
- `ManagedSettings`
  - Apply and remove shields.
  - Customize shield appearance as much as Apple permits.
- `DeviceActivity`
  - Monitor schedules and events.
  - Reapply shields when time windows expire.
- Optional later:
  - `DeviceActivityReport` for parent summaries.
  - `NetworkExtension` only if site-level filtering requires it and Apple permits the use case.

## Entitlement risk

Apple requires special capability approval for FamilyControls/Screen Time APIs. This is not guaranteed.

Mitigation:

- Frame FaithWall as a parental-control/family-safety app.
- Keep claims focused on parent-managed devices and family consent.
- Avoid spyware language, surveillance language, or bypass claims.
- Build a minimal local prototype while entitlement request is pending where possible.

## Prototype milestones

### Milestone 1: Native shell

**Objective:** Create the SwiftUI TestFlight app shell.

**Files:**
- Create native iOS project outside the current Vite app, likely `faithwall-ios/`.
- Add SwiftUI app entry, home screen, setup screen, and local gate screen.

**Verification:** Runs in iOS Simulator and on one physical iPhone through Xcode.

### Milestone 2: FamilyControls authorization

**Objective:** Request Screen Time / FamilyControls permission from the device.

**Implementation notes:**
- Import `FamilyControls`.
- Use `AuthorizationCenter.shared.requestAuthorization`.
- Show clear failure state if permission is denied.

**Verification:** Physical iPhone prompts for permission and returns approved/denied state.

### Milestone 3: App/site picker

**Objective:** Let parent select apps/categories/web domains.

**Implementation notes:**
- Use `FamilyActivityPicker`.
- Persist selection locally.
- Do not send selected app details to external servers in MVP.

**Verification:** Selection persists after app restart.

### Milestone 4: Apply shield

**Objective:** Shield selected apps/sites.

**Implementation notes:**
- Use `ManagedSettingsStore`.
- Apply `shield.applications`, `shield.applicationCategories`, and/or `shield.webDomains` depending on picker data.

**Verification:** Selected apps/sites become blocked by iOS shield on physical device.

### Milestone 5: FaithWall unlock gate

**Objective:** Complete a local KJV gate and temporarily remove shields.

**Implementation notes:**
- Keep a small local KJV verse bank.
- Require “Read Scripture” + “Lay the brick.”
- On completion, remove shields for a configured duration.
- Use DeviceActivity/scheduled task to restore shields after the window.

**Verification:** Shield comes off after gate completion and returns after time expires.

### Milestone 6: Buyer access connection

**Objective:** Connect native prototype to paid FaithWall access without shared passwords.

**Implementation notes:**
- Start with email-code login or signed handoff token from `faithwall.deadhidden.org`.
- Never embed Stripe secrets in the app.
- Native app calls FaithWall API only for access/session, not payment secrets.

**Verification:** Paid/household email can access prototype; unpaid email cannot.

### Milestone 7: TestFlight build

**Objective:** Ship to internal TestFlight.

**Implementation notes:**
- Apple Developer account required.
- Bundle ID: choose a clean FaithWall identifier.
- Configure capabilities.
- Upload archive through Xcode or `xcodebuild`/Transporter.

**Verification:** Internal tester installs through TestFlight and can run full flow on physical iPhone.

## Acceptance criteria for prototype

- Physical iPhone install works through TestFlight.
- Parent can grant FamilyControls permission.
- Parent can select at least one real app or category.
- FaithWall can shield that selection.
- KJV gate completion temporarily removes the shield.
- Shield returns after the time window.
- App does not claim or attempt hidden surveillance.
- Buyer access uses FaithWall server auth, not app-bundled secrets.

## What not to build in v1

- Full App Store polish.
- Reports dashboard.
- Cross-device sync.
- AI verse generation.
- Social feed.
- Complex rewards.
- MDM/supervised-device flow.
- VPN/DNS filtering unless Apple API limits force that investigation.

## Public copy boundary

Safe:

- “iPhone native control is in TestFlight scope.”
- “FaithWall uses Apple’s approved Screen Time path for the native prototype.”
- “Web app live now. iPhone app-store path next.”

Unsafe until proven live:

- “FaithWall controls iPhone apps.”
- “FaithWall blocks every app.”
- “Works before any app opens.”
- “Cannot be bypassed.”

## First engineering spike

1. Create `faithwall-ios/` SwiftUI project.
2. Add `FamilyControls`, `ManagedSettings`, `DeviceActivity` imports.
3. Confirm project compiles with capabilities enabled.
4. Request authorization on a physical iPhone.
5. Log authorization status.
6. Present app/category picker.
7. Persist selection.
8. Try applying a shield to one selected app/category.
9. Record exactly what Apple permits and blocks.

If Milestone 4 works, build the unlock gate. If Milestone 4 fails because entitlement/capability is blocked, pause public claims and file the entitlement request before deeper build work.
