# Apple Family Controls Entitlement Request Notes

FaithWall needs Apple's Family Controls / Screen Time API entitlement before the native iPhone app can be fully tested or shipped.

## App description

FaithWall is a parent-managed Scripture-before-scrolling app for Christian families. Parents choose distracting apps, categories, or websites on a household iPhone. FaithWall uses Apple's approved Screen Time APIs to shield those selections. The user returns to FaithWall, reads a KJV Scripture gate, and unlocks the selected apps for a short parent-configured window.

## Safety posture

- Parent/household consent only.
- No hidden surveillance.
- No message reading.
- No keystroke logging.
- No screen capture.
- No selling app-usage data.
- MVP stores selected app/category/site tokens locally through Apple Screen Time APIs and App Group storage.
- FaithWall does not try to bypass iOS protections.

## Entitlements/capabilities needed

- Family Controls / Screen Time API.
- App Group: `group.org.deadhidden.faithwall`.

## Bundle IDs

- Main app: `org.deadhidden.faithwall`
- Shield configuration extension: `org.deadhidden.faithwall.shield-configuration`
- Shield action extension: `org.deadhidden.faithwall.shield-action`
- Device activity monitor extension: `org.deadhidden.faithwall.device-activity-monitor`

## TestFlight MVP acceptance test

1. Parent grants Screen Time permission.
2. Parent selects one app/category/site.
3. FaithWall applies iOS shield.
4. Opening selected app shows FaithWall shield.
5. User returns to FaithWall and completes KJV gate.
6. App unlocks selected app for configured window.
7. Shield returns when the window expires.

## Public claim boundary

Until physical-device testing passes, public copy must say:

- “Native iPhone Screen Time prototype in build.”
- “FaithWall uses Apple’s approved Screen Time path.”

Do not say:

- “FaithWall controls every iPhone app.”
- “FaithWall cannot be bypassed.”
- “Works before every app opens.”
