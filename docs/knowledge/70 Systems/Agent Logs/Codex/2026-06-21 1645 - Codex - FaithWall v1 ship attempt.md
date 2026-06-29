# 2026-06-21 1645 - Codex - FaithWall v1 ship attempt

## Result

FaithWall v1.0 is not submitted yet.

Completed:
- Bumped FaithWall build number from 13 to 14 in `/Users/adamjohnsson/code/faithwall-verse-ios-reconstruction/FaithWallVerse.xcodeproj/project.pbxproj`.
- Verified Release simulator clean build for iPhone 17.
- Verified built simulator app has no `PlugIns` directory.
- Verified `otool -L` on the built app binary has no `FamilyControls`, `ManagedSettings`, or `DeviceActivity` linked frameworks.
- Committed and deployed the FaithWall privacy policy page to production.

Blocked:
- Apple archive/signing failed because the Developer Program License Agreement needs acceptance in the Apple developer account, and the fallback provisioning profile does not include Sign in with Apple.
- Because archive/signing failed, App Store upload, build selection, IAP attachment, and submission could not be completed honestly.

## FaithWall build proof

Project:

`/Users/adamjohnsson/code/faithwall-verse-ios-reconstruction/FaithWallVerse.xcodeproj`

Scheme:

`FaithWallVerse`

Build number:

`14`

Build-number verification:

```text
CURRENT_PROJECT_VERSION = 14;
CURRENT_PROJECT_VERSION = 14;
CURRENT_PROJECT_VERSION = 14;
CURRENT_PROJECT_VERSION = 14;
```

Release simulator build command:

```bash
DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer xcodebuild -project FaithWallVerse.xcodeproj -scheme FaithWallVerse -configuration Release -destination 'platform=iOS Simulator,name=iPhone 17' CODE_SIGNING_ALLOWED=NO clean build
```

Result:

```text
** CLEAN SUCCEEDED **
** BUILD SUCCEEDED **
```

Built app:

`/Users/adamjohnsson/Library/Developer/Xcode/DerivedData/FaithWallVerse-asbebwpsqmdprmduupqoopdvvqde/Build/Products/Release-iphonesimulator/FaithWallVerse.app`

Bundle version proof:

```text
CFBundleShortVersionString: 1.0
CFBundleVersion: 14
```

Extension/framework proof:

```text
PlugIns directory: absent
Forbidden framework scan: no FamilyControls, ManagedSettings, or DeviceActivity references in the built app bundle
otool -L: AuthenticationServices, StoreKit, SwiftUI, AVFoundation, UserNotifications present; FamilyControls/ManagedSettings/DeviceActivity absent
```

## Apple archive blocker

Archive command:

```bash
DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer xcodebuild -project FaithWallVerse.xcodeproj -scheme FaithWallVerse -configuration Release -destination 'generic/platform=iOS' -archivePath /tmp/FaithWallVerse-1.0-14.xcarchive -allowProvisioningUpdates DEVELOPMENT_TEAM=7VD84G35MB archive
```

Result:

```text
** ARCHIVE FAILED **
```

Exact blocking errors:

```text
Unable to process request - PLA Update available: You currently don't have access to this membership resource. To resolve this issue, agree to the latest Program License Agreement in your developer account.
Provisioning profile "iOS Team Provisioning Profile: *" doesn't include the Sign In with Apple capability.
Provisioning profile "iOS Team Provisioning Profile: *" doesn't include the com.apple.developer.applesignin entitlement.
```

Meaning:

The Apple account owner needs to accept the current Program License Agreement, then the App ID `org.deadhidden.faithwall.companion` needs Sign in with Apple enabled and a matching distribution profile before archive/upload can proceed.

## Privacy policy deploy

Source file committed:

`/Users/adamjohnsson/code/deadhidden/src/app/privacy/faithwall/page.tsx`

Local audit branch commit:

`0084337 Add FaithWall privacy policy page`

Clean production main commit:

`c2de074 Add FaithWall privacy policy page`

Deploy:

Vercel deployment `dpl_DFsTyzkqR8Vjn8LbPUKbpAgH19pv`

Vercel state:

`READY`

Aliases:

`deadhidden.org`, `www.deadhidden.org`, `deadhidden.vercel.app`

Live URL checks:

```text
https://deadhidden.org/privacy/faithwall -> HTTP 200
https://www.deadhidden.org/privacy/faithwall -> HTTP 200
x-matched-path: /privacy/faithwall
```

Rendered-body proof found:

```text
FAITHWALL PRIVACY POLICY
Last updated: June 21, 2026
We do not track you.
Final Fight Bible Radio.
support@deadhidden.org
```

Local clean production build before push:

```bash
npm ci
npm run build
```

Result:

```text
audit-slugs: passed
next build: compiled successfully
/privacy/faithwall present as a static route
```

## App Store status fields

Build uploaded to App Store Connect:

`No`

Build number visible in App Store Connect:

`Not verified - archive/upload blocked before processing`

IAP status:

`Not created/verified in this run`

IAP attached to version:

`No - blocked before App Store Connect submission`

Privacy URL live:

`Yes - https://deadhidden.org/privacy/faithwall returns 200 and renders the policy`

Final submission status:

`Blocked before archive/upload/submission`

Screenshot paths captured:

`None`

Why no screenshots:

The Codex Chrome extension bridge was installed/enabled but unavailable (`Browser is not available: extension`), and the Apple archive stopped at the PLA/provisioning gate before App Store Connect build selection or submission proof existed. No Chrome restart or session reset was performed.

## Boundaries

No Stripe/customer/money mutation, refund, checkout-session creation, email send, public post, DNS change, credential print, App Store submission, IAP creation, App ID capability change, or Apple PLA acceptance happened.

The only production deploy was the single FaithWall privacy policy page commit `c2de074` to `origin/main`.
