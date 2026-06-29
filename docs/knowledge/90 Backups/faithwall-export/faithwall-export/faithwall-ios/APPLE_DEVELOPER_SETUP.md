# FaithWall Apple Developer / App Store Connect Setup

## Current local status

FaithWall builds and installs on Adam's iPhone with a development certificate, but Apple strips the Screen Time/App Group entitlements from the signed app because the current Apple team/profiles do not have those capabilities enabled.

Evidence from signed app:

```text
application-identifier: 7VD84G35MB.org.deadhidden.faithwall
com.apple.developer.team-identifier: 7VD84G35MB
get-task-allow: true
```

Missing from signed app/profile:

```text
com.apple.developer.family-controls
com.apple.security.application-groups
```

That matches the on-device error:

```text
Screen Time permission failed: Couldn't communicate with a helper application.
```

## Required Bundle IDs

Create explicit App IDs in Apple Developer > Certificates, Identifiers & Profiles:

1. `org.deadhidden.faithwall`
2. `org.deadhidden.faithwall.shield-configuration`
3. `org.deadhidden.faithwall.shield-action`
4. `org.deadhidden.faithwall.device-activity-monitor`

## Required App Group

Create App Group:

```text
group.org.deadhidden.faithwall
```

Enable this group on all four App IDs above.

## Required Capability / Entitlement

Request/enable Family Controls / Screen Time API entitlement:

```text
com.apple.developer.family-controls
```

Enable it for the main app and the Screen Time extension targets as Apple permits.

## App Review / Entitlement request copy

FaithWall is a parent/household-managed accountability app that uses Apple's Screen Time APIs to let the user select apps, categories, and websites to shield. When a selected app/site is shielded, the app presents a KJV Scripture gate before allowing a temporary unlock window.

FaithWall does not read private messages, capture screens, log keystrokes, monitor location, sell app-usage data, or use private APIs. Selected app/site/category tokens are stored locally and shared only through the app group between the main app and its Screen Time extensions.

The purpose is user-directed and household-directed attention protection using FamilyControls, ManagedSettings, ManagedSettingsUI, and DeviceActivity.

## After portal setup

Run:

```bash
cd /Users/adamjohnsson/Downloads/faithwall-export/faithwall-export/faithwall-ios
export DEVELOPER_DIR="$HOME/Downloads/Xcode.app/Contents/Developer"
xcodegen generate
xcodebuild -project FaithWall.xcodeproj -scheme FaithWall -configuration Debug -destination 'id=00008150-000E71EE2242401C' -allowProvisioningUpdates build
```

Verify signed entitlements:

```bash
APP="$HOME/Library/Developer/Xcode/DerivedData/FaithWall-blqiexyuanhynxdzeeeohagmnvbu/Build/Products/Debug-iphoneos/FaithWall.app"
codesign -d --entitlements :- "$APP" 2>/dev/null | plutil -p -
security cms -D -i "$APP/embedded.mobileprovision" 2>/dev/null | plutil -extract Entitlements xml1 -o - - | plutil -p -
```

Expected keys must include:

```text
com.apple.developer.family-controls
com.apple.security.application-groups
```

Then install and retest Screen Time permission.

## Store/TestFlight export

Requires paid Apple Developer Program / App Store Connect provider access. Current export failure was:

```text
No provider associated with App Store Connect user
Team does not have permission to create iOS App Store provisioning profiles
```
