# Bible Brick

<!-- Logo placeholder — add your app icon here -->
<!-- <img src="assets/icons/app_icon.png" width="120" alt="Bible Brick Logo"> -->

<h1 align="center">Bible Brick</h1>

<p align="center">
  <strong>Brick your phone. Lay a brick for your faith. Build your family wall, one verse at a time.</strong>
</p>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/Flutter-3.24+-02569B?logo=flutter&logoColor=white" alt="Flutter">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Dart-3.5+-0175C2?logo=dart&logoColor=white" alt="Dart">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Firebase-Cloud%20Firestore-FFCA28?logo=firebase&logoColor=black" alt="Firebase">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/iOS-15.0+-000000?logo=apple&logoColor=white" alt="iOS">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/Android-5.0+-3DDC84?logo=android&logoColor=white" alt="Android">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>

---

## Screenshots

<!-- Add your screenshots here -->
<!--
| Home | Unbrick | Progress | Settings |
|------|---------|----------|----------|
| ![Home](screenshots/home.png) | ![Unbrick](screenshots/unbrick.png) | ![Progress](screenshots/progress.png) | ![Settings](screenshots/settings.png) |
-->

## Features

### Core Experience

1. **Brick Modes** — Create custom app-blocking configurations for different times of day (Morning Devotion, Homeschool Hours, Family Dinner, Bedtime)
2. **One-Tap Activation** — Activate a Brick Mode to instantly lock distracting apps
3. **Bible Unbrick Tasks** — Unlock your apps by completing a scripture activity — read aloud, write a prayer, speak from your heart, or receive the Word
4. **Emergency Unlock** — Break through with a streak warning when absolutely necessary
5. **Brick Wall Progress** — Visual wall that grows brick by brick with every completed session

### Scripture & Faith

6. **Daily Bible Verses** — Fresh verse each day from the World English Bible (WEB)
7. **Verse Themes** — 12 themed collections: Family, Homeschool, Peace, Strength, Warfare, Marriage, Parenting, Gratitude, Wisdom, Love, Faith, Hope
8. **Voice Integration** — Speech-to-text for reading aloud and spoken prayers; text-to-speech for verse playback
9. **Audio Prayer Recording** — Record and save voice prayers tied to specific verses

### Family & Sharing

10. **Family Groups** — Create or join family groups with a 6-digit invite code
11. **Shared Family Wall** — Watch your collective wall grow as a family
12. **Family Progress Dashboard** — See each member's brick count and streaks

### Smart Scheduling

13. **Auto-Activate Schedules** — Set days and times for automatic Brick Mode activation
14. **Smart App Detection** — Scans your device for the most-used distracting apps
15. **Strict Mode** — Disables emergency unlock for maximum discipline

### Progress & Analytics

16. **Streak Tracking** — Current streak, longest streak, and streak protection
17. **Focus Time Stats** — Total minutes spent in focused sessions
18. **Weekly/Monthly/All-Time Views** — Track progress across time periods
19. **Advanced Statistics** *(Premium)* — Detailed analytics with trends and data export
20. **Session History** — Complete history of all brick-laying sessions

### Monetization

21. **Premium Monthly** ($4.99/month) — Unlimited modes, family sharing, verse packs, advanced stats, no ads
22. **Premium Lifetime** ($49.99 one-time) — Everything in monthly, forever
23. **Emergency Unbrick Packs** — Purchase additional emergency unbrick uses
24. **Restore Purchases** — Full support for cross-device purchase restoration

### Platform-Specific

25. **iOS Screen Time API** — Native app blocking using Apple's DeviceActivity framework
26. **Android Accessibility Service** — Reliable app detection with overlay blocking
27. **Cross-Platform Sync** — Firebase-backed data sync across all devices

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Framework** | Flutter 3.24+ | Cross-platform UI |
| **Language** | Dart 3.5+ | Application code |
| **State Management** | Riverpod 2.6+ | Reactive state |
| **Backend** | Firebase | Auth, Firestore, Analytics, Messaging |
| **Local Storage** | Hive + SharedPreferences | Offline-first data |
| **Networking** | Dio | HTTP with caching |
| **Routing** | GoRouter | Declarative navigation |
| **Speech** | speech_to_text + flutter_tts | Voice interactions |
| **Audio** | record | Prayer recording |
| **Monetization** | in_app_purchase | StoreKit + Play Billing |
| **UI** | Material 3 + Google Fonts | Design system |
| **Animations** | flutter_animate + lottie | Rich animations |
| **Code Gen** | Freezed + Riverpod Generator | Immutable models |

---

## Architecture Overview

Bible Brick follows a **Layered Architecture** with clear separation of concerns:

```
lib/
├── main.dart                    # App entry point
├── app.dart                     # Root MaterialApp + Riverpod
│
├── core/
│   ├── constants/               # AppColors, AppStrings, AppTheme, etc.
│   ├── models/                  # Freezed data classes (immutable)
│   ├── providers/               # Riverpod state management
│   ├── services/                # Platform channels, Firebase, IAP, etc.
│   ├── router/                  # GoRouter configuration
│   └── utils/                   # Extensions, helpers, painters
│
├── features/
│   ├── home/                    # Dashboard screen
│   ├── onboarding/              # First-launch tutorial
│   ├── brick_mode_editor/       # Create/edit blocking modes
│   ├── unbrick/                 # Scripture task screen
│   ├── progress/                # Wall progress + stats
│   ├── family/                  # Family groups
│   ├── settings/                # App settings
│   └── premium/                 # Monetization screens
│
└── widgets/
    └── common/                  # Shared UI components
```

### Key Architectural Decisions

- **Offline-First**: All data persists locally via Hive; Firebase syncs in background
- **Platform Channels**: Separate method channels for iOS (`com.biblebrick/app_blocking`) and Android (`com.biblebrick/android_blocking`)
- **Feature-First Folder Structure**: Each feature is self-contained with its own screens, widgets, and logic
- **Immutable Models**: All data classes use Freezed for immutability and JSON serialization

---

## Setup Instructions

### Prerequisites

- **Flutter SDK** 3.24.0 or higher ([Install](https://docs.flutter.dev/get-started/install))
- **Dart SDK** 3.5.0 or higher (bundled with Flutter)
- **Firebase CLI** ([Install](https://firebase.google.com/docs/cli#setup))
- **Android Studio** or **VS Code** with Flutter plugin
- **Xcode** 14+ (for iOS development — macOS only)
- **CocoaPods** 1.12+ (for iOS dependencies)
- **Apple Developer Account** (for iOS Screen Time API entitlement)
- **Google Play Developer Account** (for Android release)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/bible_brick.git
cd bible_brick
```

### 2. Install Flutter Dependencies

```bash
flutter pub get
```

### 3. Firebase Setup

a. **Install Firebase CLI tools:**

```bash
npm install -g firebase-tools
firebase login
```

b. **Install FlutterFire CLI:**

```bash
dart pub global activate flutterfire_cli
```

c. **Configure Firebase for your project:**

```bash
flutterfire configure \
  --project=bible-brick \
  --out=lib/core/constants/firebase_options.dart \
  --ios-bundle-id=com.biblebrick.app \
  --android-app-id=com.biblebrick.app \
  --platforms=ios,android
```

d. **Download Firebase config files:**

```bash
# iOS — place in ios/Runner/GoogleService-Info.plist
# Android — place in android/app/google-services.json
```

e. **Enable Firebase services** in the Firebase Console:

- Authentication (Email/Password, Google, Anonymous)
- Cloud Firestore (Start in test mode, then add security rules)
- Firebase Analytics
- Cloud Messaging (for push notifications)
- Remote Config (for feature flags)

### 4. iOS Setup

a. **Update Podfile** minimum iOS version:

```ruby
# ios/Podfile
platform :ios, '15.0'
```

b. **Install CocoaPods:**

```bash
cd ios && pod install && cd ..
```

c. **Configure Signing** in Xcode:

- Open `ios/Runner.xcworkspace` in Xcode
- Select the Runner target > Signing & Capabilities
- Set your Team and Bundle Identifier
- Add the **Family Controls** capability (for Screen Time API)

d. **Add entitlements** in `ios/Runner/Runner.entitlements`:

```xml
<key>com.apple.developer.family-controls</key>
<true/>
```

e. **Add usage description** in `ios/Runner/Info.plist`:

```xml
<key>NSFamilyControlsUsageDescription</key>
<string>Bible Brick needs Screen Time access to block distracting apps during your focus modes. No browsing data is collected.</string>
```

### 5. Android Setup

a. **Update `android/app/build.gradle`** minimum SDK:

```gradle
android {
    defaultConfig {
        minSdk = 21
        targetSdk = 34
    }
}
```

b. **Ensure `android/build.gradle`** has Google Services plugin:

```gradle
// In android/build.gradle (project level)
plugins {
    id 'com.google.gms.google-services' version '4.4.0' apply false
}
```

c. **Apply plugin** in `android/app/build.gradle`:

```gradle
plugins {
    id 'com.android.application'
    id 'kotlin-android'
    id 'com.google.gms.google-services'  // Add this line
}
```

d. **ProGuard rules** (if using minification):

Add to `android/app/proguard-rules.pro`:

```proguard
# Keep Firebase classes
-keep class com.google.firebase.** { *; }
# Keep IAP classes
-keep class com.android.billingclient.** { *; }
```

### 6. Run Code Generation

Generate Freezed models, Riverpod providers, and other code:

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

For continuous generation during development:

```bash
flutter pub run build_runner watch --delete-conflicting-outputs
```

### 7. Run the App

```bash
# Debug on connected device
flutter run

# Or specify device
flutter run -d <device_id>

# Run in profile mode (performance testing)
flutter run --profile

# Build release APK
flutter build apk --release

# Build release App Bundle (for Play Store)
flutter build appbundle --release

# Build iOS (for App Store)
flutter build ios --release
```

---

## Folder Structure

```
bible_brick/
├── android/                          # Android native code
│   ├── app/src/main/
│   │   ├── AndroidManifest.xml       # Permissions & services
│   │   ├── kotlin/com/biblebrick/
│   │   │   ├── MainActivity.kt       # Flutter entry point
│   │   │   ├── AppBlockingPlugin.kt  # Method channel handler
│   │   │   ├── AppBlockingAccessibilityService.kt  # Accessibility service
│   │   │   ├── BlockingOverlayActivity.kt          # Blocking overlay
│   │   │   └── BootCompletedReceiver.kt            # Boot receiver
│   │   └── res/
│   │       ├── xml/
│   │       │   └── accessibility_service_config.xml
│   │       ├── layout/
│   │       │   └── activity_blocking_overlay.xml
│   │       └── values/
│   │           └── strings.xml
│   └── build.gradle
│
├── ios/                              # iOS native code
│   ├── Podfile                       # CocoaPods dependencies
│   ├── Runner/
│   │   ├── AppDelegate.swift         # Plugin registration
│   │   ├── AppBlockingPlugin.swift   # Screen Time API bridge
│   │   ├── Info.plist                # Permissions
│   │   └── Runner.entitlements       # Family Controls entitlement
│   └── Runner.xcodeproj/
│
├── docs/                             # Technical documentation
│   ├── IOS_LOCKING_IMPLEMENTATION.md
│   └── ANDROID_LOCKING_IMPLEMENTATION.md
│
├── lib/                              # Dart source code
│   ├── main.dart
│   ├── app.dart
│   ├── core/
│   │   ├── constants/
│   │   │   ├── app_colors.dart       # Brick/mortar color palette
│   │   │   ├── app_strings.dart      # All user-facing strings
│   │   │   ├── app_theme.dart        # Light/dark theme definitions
│   │   │   ├── api_endpoints.dart    # API URLs
│   │   │   └── firebase_options.dart # Firebase configuration
│   │   ├── models/
│   │   │   ├── app_info.dart         # App metadata
│   │   │   ├── brick_mode.dart       # Blocking mode config
│   │   │   ├── app_usage_session.dart # Session records
│   │   │   ├── bible_verse.dart      # Scripture data
│   │   │   ├── user_progress.dart    # User stats
│   │   │   ├── family_account.dart   # Family group data
│   │   │   ├── purchase_tier.dart    # Free/Premium enum
│   │   │   └── unbrick_task.dart     # Task definitions
│   │   ├── providers/
│   │   │   ├── app_blocker_provider.dart   # Lock/unlock state
│   │   │   ├── premium_provider.dart       # Purchase/subscription state
│   │   │   ├── brick_mode_provider.dart    # Mode CRUD
│   │   │   ├── user_progress_provider.dart # Stats
│   │   │   ├── auth_provider.dart          # Authentication
│   │   │   ├── settings_provider.dart      # Preferences
│   │   │   ├── bible_verse_provider.dart   # Verse fetching
│   │   │   └── onboarding_provider.dart    # First-launch flow
│   │   ├── services/
│   │   │   ├── app_blocking_service.dart   # Platform-agnostic blocking
│   │   │   ├── iOS_app_blocking.dart       # iOS Screen Time API
│   │   │   ├── android_app_blocking.dart   # Android accessibility
│   │   │   ├── purchase_service.dart       # IAP implementation
│   │   │   ├── firebase_service.dart       # Firebase operations
│   │   │   ├── bible_api_service.dart      # Bible verse API
│   │   │   ├── notification_service.dart   # Push/local notifications
│   │   │   ├── speech_service.dart         # STT/TTS
│   │   │   ├── analytics_service.dart      # Firebase Analytics
│   │   │   └── local_storage_service.dart  # Hive/SharedPreferences
│   │   ├── router/
│   │   │   └── app_router.dart            # GoRouter configuration
│   │   └── utils/
│   │       ├── extensions.dart
│   │       ├── helpers.dart
│   │       └── brick_wall_painter.dart
│   ├── features/
│   │   ├── home/
│   │   │   ├── screens/home_screen.dart
│   │   │   └── widgets/
│   │   │       ├── active_brick_banner.dart
│   │   │       ├── brick_mode_card.dart
│   │   │       ├── quick_brick_fab.dart
│   │   │       └── wall_progress_preview.dart
│   │   ├── onboarding/
│   │   │   ├── screens/onboarding_screen.dart
│   │   │   └── widgets/
│   │   │       ├── onboarding_page.dart
│   │   │       └── distraction_wizard.dart
│   │   ├── brick_mode_editor/
│   │   │   ├── screens/
│   │   │   │   ├── mode_list_screen.dart
│   │   │   │   ├── mode_edit_screen.dart
│   │   │   │   └── app_picker_screen.dart
│   │   │   └── widgets/
│   │   │       ├── app_list_tile.dart
│   │   │       ├── mode_form.dart
│   │   │       └── schedule_picker.dart
│   │   ├── unbrick/
│   │   │   ├── screens/unbrick_screen.dart
│   │   │   └── widgets/
│   │   │       ├── verse_display.dart
│   │   │       ├── task_read_aloud.dart
│   │   │       ├── task_type_prayer.dart
│   │   │       ├── task_voice_prayer.dart
│   │   │       ├── task_receive.dart
│   │   │       ├── brick_animation.dart
│   │   │       └── task_receive.dart
│   │   ├── progress/
│   │   │   ├── screens/progress_screen.dart
│   │   │   └── widgets/
│   │   │       ├── stats_chart.dart
│   │   │       ├── streak_counter.dart
│   │   │       ├── brick_wall_visual.dart
│   │   │       └── family_progress.dart
│   │   ├── family/
│   │   │   └── screens/family_screen.dart
│   │   ├── settings/
│   │   │   └── screens/settings_screen.dart
│   │   └── premium/
│   │       ├── screens/premium_screen.dart
│   │       └── widgets/
│   │           └── feature_comparison.dart
│   └── widgets/
│       └── common/
│           ├── bb_card.dart
│           ├── bb_button.dart
│           ├── bb_app_bar.dart
│           └── bb_loading.dart
│
├── assets/
│   ├── images/
│   ├── icons/
│   ├── animations/
│   ├── fonts/
│   └── sounds/
│
├── python_automation/
│   └── setup.sh               # Environment setup script
│
├── pubspec.yaml
├── analysis_options.yaml
├── .gitignore
└── README.md                   # This file
```

---

## Monetization

### Revenue Model

Bible Brick uses a **freemium** model with subscription and one-time purchase options:

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0 | 2 Brick Modes, basic stats, Bible verses, cloud sync |
| **Premium Monthly** | $4.99/mo | Unlimited modes, family sharing, verse packs, advanced stats, no ads, 10 emergency unbricks/month |
| **Premium Lifetime** | $49.99 | Everything in monthly, one-time purchase, never expires |

### Consumables

| Product | Price | Purpose |
|---------|-------|---------|
| Emergency Unbrick 5-Pack | $2.99 | 5 additional emergency unbricks |
| Emergency Unbrick 10-Pack | $4.99 | 10 additional emergency unbricks |

### Product IDs

Register these in App Store Connect and Google Play Console:

```dart
// lib/core/services/purchase_service.dart
static const String kMonthlyId = 'premium_monthly';
static const String kLifetimeId = 'premium_lifetime';
static const String kUnbrick5Id = 'emergency_unbrick_5';
static const String kUnbrick10Id = 'emergency_unbrick_10';
```

### Server-Side Validation

Purchase receipts/tokens are validated server-side via Firebase Functions:

```
Purchase → Store (Apple/Google) → App Receipt → Firebase Function → Validation → Firestore
```

This prevents fraud and enables cross-device premium sync.

### Premium Upsell Triggers

The premium screen is shown when users:

- Try to create a 3rd Brick Mode (free limit = 2)
- Attempt to use family sharing features
- Try to access advanced statistics
- Navigate via Settings > "Go Premium"

---

## Python Automation

The `python_automation/` directory contains scripts for development workflow automation:

```bash
# Setup development environment
cd python_automation
chmod +x setup.sh
./setup.sh
```

### Available Scripts

| Script | Purpose |
|--------|---------|
| `setup.sh` | Install dependencies, configure git hooks |

---

## Contributing

We welcome contributions! Please follow these guidelines:

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

### Code Style

- Follow the [Effective Dart](https://dart.dev/effective-dart) guidelines
- Use `flutter_lints` for static analysis
- Run `dart format` before committing
- Generate code with `build_runner` when modifying models

### Pull Request Template

```
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Tested on physical device
- [ ] Tested on iOS
- [ ] Tested on Android

## Screenshots (if applicable)
Add screenshots for UI changes
```

### Commit Messages

Use conventional commits:

```
feat: Add family sharing feature
fix: Resolve accessibility service crash on Android 14
docs: Update iOS setup instructions
refactor: Simplify purchase service state management
test: Add premium provider unit tests
```

### Reporting Issues

When reporting bugs, please include:

- Device model and OS version
- App version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots or screen recordings

---

## License

```
MIT License

Copyright (c) 2024 Bible Brick

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Acknowledgments

- Bible verses provided by the [API.Bible](https://scripture.api.bible/) and [World English Bible](https://ebible.org/web/)
- Built with [Flutter](https://flutter.dev) by Google
- Inspired by Christian homeschooling families seeking digital discipline

---

## Support

- **Email**: support@biblebrick.app
- **Website**: [biblebrick.app](https://biblebrick.app)
- **Help Center**: In-app via Settings > Help Center

---

<p align="center">
  <em>"By wisdom a house is built, and through understanding it is established." — Proverbs 24:3</em>
</p>
