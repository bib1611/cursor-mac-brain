# FaithWall iOS TestFlight MVP

This is the native iPhone prototype for FaithWall.

## What this builds

- SwiftUI app shell.
- Apple Screen Time permission request via `FamilyControls`.
- App/category/site picker via `FamilyActivityPicker`.
- Shield application via `ManagedSettingsStore`.
- KJV Scripture gate.
- Temporary unlock window.
- Shield configuration/action/device activity extension skeletons.

## What it does not claim yet

This is not a public App Store blocker until it is tested on a physical iPhone with Apple Screen Time capability approval.

Safe public wording:

- Web app live now.
- Chrome extension available for founding users.
- Native iPhone Screen Time prototype in build.

Unsafe wording until verified:

- FaithWall controls every iPhone app.
- FaithWall cannot be bypassed.
- FaithWall works before any app opens.

## Requirements

- Full Xcode installed from the Mac App Store or Apple Developer downloads.
- Apple Developer account.
- Family Controls / Screen Time API entitlement approved by Apple.
- Physical iPhone running iOS 17+.

Command Line Tools alone are not enough. This Mac currently has Command Line Tools but no full Xcode app.

## Generate the Xcode project

Install XcodeGen after Xcode is installed:

```bash
brew install xcodegen
cd faithwall-ios
xcodegen generate
open FaithWall.xcodeproj
```

Then in Xcode:

1. Set the Team on all targets.
2. Confirm bundle IDs:
   - `org.deadhidden.faithwall`
   - `org.deadhidden.faithwall.shield-configuration`
   - `org.deadhidden.faithwall.shield-action`
   - `org.deadhidden.faithwall.device-activity-monitor`
3. Add the Family Controls capability if Xcode does not automatically pick it up from entitlements.
4. Add App Group `group.org.deadhidden.faithwall`.
5. Run on a physical iPhone.

## Physical-device acceptance test

1. Install the app on a physical iPhone.
2. Tap **Request Screen Time Permission**.
3. Confirm Apple authorization succeeds.
4. Tap **Open App Picker**.
5. Pick one distracting app/category/site.
6. Tap **Apply Shield**.
7. Try opening the selected app.
8. Confirm iOS shows the FaithWall shield.
9. Return to FaithWall.
10. Read the KJV gate and tap **Unlock Temporarily**.
11. Confirm the selected app opens during the unlock window.
12. Confirm shield returns after the timer expires.

## Known MVP limitation

The first timer restore is host-app local. If iOS suspends the app, restoration may wait until the app resumes. The next iteration should move robust restoration into `DeviceActivityMonitor` with app-group persisted selections after token-sharing behavior is verified on device.
