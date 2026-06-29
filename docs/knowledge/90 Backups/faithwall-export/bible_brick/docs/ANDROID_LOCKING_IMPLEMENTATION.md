# Android Accessibility Service + Overlay Implementation Guide

> **Document Version**: 1.0.0
> **Last Updated**: 2024
> **Applies to**: Bible Brick v1.0.0+
> **Target Platform**: Android API 21+ (Android 5.0+)
> **Recommended**: Android API 29+ (Android 10+)

## Table of Contents

1. [Overview](#1-overview)
2. [Prerequisites](#2-prerequisites)
3. [Step-by-Step Implementation](#3-step-by-step-implementation)
   - Step 1: AndroidManifest.xml Permissions
   - Step 2: Accessibility Service Declaration
   - Step 3: Accessibility Service Config (XML)
   - Step 4: Kotlin Accessibility Service
   - Step 5: Kotlin Overlay Activity
   - Step 6: Dart Android Blocking Handler
   - Step 7: Method Channel Plugin Registration
4. [Architecture Deep Dive](#4-architecture-deep-dive)
5. [OEM-Specific Considerations](#5-oem-specific-considerations)
6. [Android Limitations](#6-android-limitations)
7. [Testing Guide](#7-testing-guide)
8. [Troubleshooting](#8-troubleshooting)
9. [Play Store Compliance](#9-play-store-compliance)
10. [Official Google Documentation](#10-official-google-documentation)

---

## 1. Overview

Bible Brick uses Android's **AccessibilityService** combined with **SYSTEM_ALERT_WINDOW** overlay to block distracting applications. When a user opens a blocked app, the accessibility service detects the window state change and immediately launches a full-screen overlay activity that prevents interaction with the blocked app.

### Architecture Flow

```
User opens blocked app (e.g., Instagram)
        |
        v
Android OS: Window state changes
        |
        v
AppBlockingAccessibilityService.onAccessibilityEvent()
        |
        v
Detects package name matches blocked list
        |
        v
Launch BlockingOverlayActivity (full-screen overlay)
        |
        v
User sees "Bricked by Bible Brick" blocking screen
        |
        v
User taps "Tap to Unbrick" → navigates to UnbrickScreen
        |
        v
User completes Bible task → apps unblocked
```

### Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| `AppBlockingAccessibilityService` | `AccessibilityService` | Detects when blocked apps are opened |
| `BlockingOverlayActivity` | `Activity` + `SYSTEM_ALERT_WINDOW` | Shows full-screen blocking UI |
| `AppBlockingPlugin` | Flutter `MethodChannel` | Bridges Dart calls to native Kotlin |
| `app_blocker_provider.dart` | Riverpod | Manages lock/unlock state in Flutter |

---

## 2. Prerequisites

Before starting, ensure you have:

- [ ] Android Studio or VS Code with Flutter plugin
- [ ] Android SDK API 33+ installed
- [ ] A physical Android device or emulator for testing
- [ ] Minimum Android API 21 (Android 5.0)

---

## 3. Step-by-Step Implementation

### Step 1: AndroidManifest.xml Permissions

Add all required permissions to the manifest.

**File**: `android/app/src/main/AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <!-- ─── Internet ─── -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <!-- ─── App Blocking Permissions ─── -->
    <!-- Accessibility Service — REQUIRED for detecting app launches -->
    <uses-permission android:name="android.permission.BIND_ACCESSIBILITY_SERVICE" />

    <!-- Overlay (draw over other apps) — REQUIRED for blocking screen -->
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />

    <!-- Usage Stats — OPTIONAL for detailed app usage tracking -->
    <uses-permission android:name="android.permission.PACKAGE_USAGE_STATS" />

    <!-- Foreground Service — Keeps blocking active in background -->
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_SPECIAL_USE" />

    <!-- Boot Completed — Restart service after reboot -->
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />

    <!-- Wake Lock — Prevent device sleep during active brick mode -->
    <uses-permission android:name="android.permission.WAKE_LOCK" />

    <!-- ─── Notification Permissions (Android 13+) ─── -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <!-- ─── Audio Permissions ─── -->
    <uses-permission android:name="android.permission.RECORD_AUDIO" />

    <application
        android:name="${applicationName}"
        android:icon="@mipmap/ic_launcher"
        android:label="Bible Brick"
        android:allowBackup="true"
        android:fullBackupContent="true"
        android:usesCleartextTraffic="false">

        <!-- Main Activity (Flutter) -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <meta-data
                android:name="io.flutter.embedding.android.NormalTheme"
                android:resource="@style/NormalTheme" />
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- ─── Accessibility Service ─── -->
        <service
            android:name=".AppBlockingAccessibilityService"
            android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"
            android:exported="true"
            android:foregroundServiceType="specialUse"
            android:description="@string/accessibility_service_description"
            android:label="Bible Brick App Blocker">
            <intent-filter>
                <action android:name="android.accessibilityservice.AccessibilityService" />
            </intent-filter>
            <meta-data
                android:name="android.accessibilityservice"
                android:resource="@xml/accessibility_service_config" />
        </service>

        <!-- ─── Blocking Overlay Activity ─── -->
        <activity
            android:name=".BlockingOverlayActivity"
            android:theme="@style/BlockingOverlayTheme"
            android:excludeFromRecents="true"
            android:launchMode="singleInstance"
            android:noHistory="true"
            android:taskAffinity=""
            android:exported="false" />

        <!-- ─── Boot Receiver ─── -->
        <receiver
            android:name=".BootCompletedReceiver"
            android:enabled="true"
            android:exported="true"
            android:permission="android.permission.RECEIVE_BOOT_COMPLETED">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
                <category android:name="android.intent.category.DEFAULT" />
            </intent-filter>
        </receiver>

        <!-- Flutter Plugin Metadata -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
    </application>
</manifest>
```

### Step 2: Accessibility Service Declaration

The accessibility service is already declared in the manifest above. Key points:

- **Permission**: `android.permission.BIND_ACCESSIBILITY_SERVICE` is mandatory
- **Exported**: Must be `true` so Android system can bind to it
- **ForegroundServiceType**: `specialUse` for Android 14+ compliance
- **Label**: User-facing name shown in accessibility settings

### Step 3: Accessibility Service Config

Create the XML configuration file that tells Android which events to report.

**File**: `android/app/src/main/res/xml/accessibility_service_config.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<!--
    Accessibility Service Configuration for Bible Brick
    
    This configures which accessibility events the service receives.
    We listen for window state changes to detect when blocked apps
    are opened by the user.
    
    The packageNames filter limits events to common distracting apps.
    An empty list (commented below) would receive ALL window events,
    which provides the most reliable blocking but uses more battery.
-->
<accessibility-service
    xmlns:android="http://schemas.android.com/apk/res/android"
    
    <!-- User-facing description shown in accessibility settings -->
    android:description="@string/accessibility_service_description"
    
    <!-- Optional: Filter to specific packages for efficiency -->
    <!-- Remove this attribute to monitor ALL apps (more reliable, slightly more battery) -->
    android:packageNames="com.instagram.android,com.zhiliaoapp.musically,com.facebook.katana,com.twitter.android,com.google.android.youtube,com.snapchat.android,com.pinterest,com.reddit.frontpage,com.netflix.mediaclient,com.spotify.music,com.discord,com.roblox.client,com.amazon.mShop.android.shopping"
    
    <!-- Event types we care about -->
    android:accessibilityEventTypes="typeWindowStateChanged|typeWindowContentChanged"
    
    <!-- Flags for more detailed event information -->
    android:accessibilityFlags="flagIncludeNotImportantViews|flagReportViewIds|flagRetrieveInteractiveWindows"
    
    <!-- Allow the service to retrieve window content -->
    android:canRetrieveWindowContent="true"
    
    <!-- Settings activity shown when user taps the service name -->
    android:settingsActivity="com.biblebrick.app.MainActivity"
    
    <!-- Feedback type — generic is sufficient for our use case -->
    android:accessibilityFeedbackType="feedbackGeneric"
    
    <!-- Notification timeout — minimum for fastest response -->
    android:notificationTimeout="0" />
```

Add the description string to your resources:

**File**: `android/app/src/main/res/values/strings.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Bible Brick</string>
    
    <!-- Accessibility service description shown to user when enabling -->
    <string name="accessibility_service_description">
        Bible Brick uses Accessibility Service to detect when you open distracting apps 
        during active Brick Modes. When a blocked app is opened, Bible Brick shows a 
        scripture-focused screen to help you stay disciplined. No personal data is collected. 
        This service is only active when you have an active Brick Mode.
    </string>
</resources>
```

**Pro Tip**: For maximum reliability, remove the `packageNames` attribute entirely to receive events for ALL apps. This uses slightly more battery but ensures no blocked app can slip through.

### Step 4: Kotlin Accessibility Service

Create the main accessibility service that detects blocked app launches.

**File**: `android/app/src/main/kotlin/com/biblebrick/app/AppBlockingAccessibilityService.kt`

```kotlin
package com.biblebrick.app

import android.accessibilityservice.AccessibilityService
import android.accessibilityservice.AccessibilityServiceInfo
import android.app.ActivityManager
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.usage.UsageStatsManager
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Build
import android.os.Handler
import android.os.Looper
import android.os.PowerManager
import android.provider.Settings
import android.util.Log
import android.view.accessibility.AccessibilityEvent
import androidx.core.app.NotificationCompat
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import java.util.concurrent.ConcurrentHashMap

/**
 * Accessibility Service that detects when blocked apps are opened.
 *
 * This service runs in the background and listens for window state changes.
 * When the user opens an app that is in the blocked list, it immediately
 * launches the BlockingOverlayActivity to prevent interaction.
 *
 * The blocked apps list is maintained by the [AppBlockingPlugin] via
 * the Flutter method channel.
 *
 * ## Battery Impact
 * This service is very lightweight — it only processes window state changes
 * and performs a simple set lookup. No polling or continuous processing.
 *
 * ## Privacy
 * This service does NOT collect any data. It only checks if the opened
 * app's package name matches the blocked set. No content, text, or usage
 * data is logged or transmitted.
 */
class AppBlockingAccessibilityService : AccessibilityService() {

    companion object {
        private const val TAG = "BibleBrickA11y"
        private const val CHANNEL_ID = "biblebrick_blocking"
        private const val NOTIFICATION_ID = 1001
        
        /** Action to update the blocked apps list from the plugin */
        const val ACTION_UPDATE_BLOCKED_APPS = "com.biblebrick.action.UPDATE_BLOCKED_APPS"
        
        /** Action to stop blocking */
        const val ACTION_STOP_BLOCKING = "com.biblebrick.action.STOP_BLOCKING"
        
        /** Extra key for blocked apps list */
        const val EXTRA_BLOCKED_APPS = "blocked_apps"

        /** Current blocked package names — shared with the plugin */
        @JvmStatic
        val blockedPackages = ConcurrentHashMap.newKeySet<String>()
        
        /** Whether blocking is currently active */
        @JvmStatic
        var isBlockingActive = false
            private set
    }

    private lateinit var notificationManager: NotificationManager
    private var lastBlockedPackage: String? = null
    private var lastBlockTime: Long = 0
    
    /** Debounce interval to prevent rapid overlay launches (ms) */
    private val BLOCK_DEBOUNCE_MS = 1000L

    // ─── Service Lifecycle ───

    override fun onServiceConnected() {
        super.onServiceConnected()
        Log.i(TAG, "Accessibility Service connected")
        
        notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        createNotificationChannel()
        
        // Register broadcast receiver for commands from the plugin
        val filter = IntentFilter().apply {
            addAction(ACTION_UPDATE_BLOCKED_APPS)
            addAction(ACTION_STOP_BLOCKING)
        }
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            registerReceiver(commandReceiver, filter, Context.RECEIVER_NOT_EXPORTED)
        } else {
            registerReceiver(commandReceiver, filter)
        }
    }

    override fun onAccessibilityEvent(event: AccessibilityEvent) {
        // Only process if blocking is active
        if (!isBlockingActive || blockedPackages.isEmpty()) {
            return
        }

        // We only care about window state changes (app launches/switches)
        if (event.eventType != AccessibilityEvent.TYPE_WINDOW_STATE_CHANGED) {
            return
        }

        // Get the package name of the newly opened window
        val packageName = event.packageName?.toString() ?: return
        
        // Check if this package is blocked
        if (isPackageBlocked(packageName)) {
            handleBlockedAppOpened(packageName)
        }
    }

    override fun onInterrupt() {
        Log.w(TAG, "Accessibility Service interrupted")
    }

    override fun onDestroy() {
        super.onDestroy()
        try {
            unregisterReceiver(commandReceiver)
        } catch (e: IllegalArgumentException) {
            // Receiver not registered
        }
        Log.i(TAG, "Accessibility Service destroyed")
    }

    // ─── Blocking Logic ───

    /**
     * Check if a package name is in the blocked set.
     * Also prevents blocking our own app and system-critical apps.
     */
    private fun isPackageBlocked(packageName: String): Boolean {
        // Never block our own app
        if (packageName == packageName) {
            return false
        }
        
        // Never block system-critical apps
        if (isSystemApp(packageName)) {
            return false
        }
        
        return blockedPackages.contains(packageName)
    }

    /**
     * Check if a package is a system-critical app that should never be blocked.
     */
    private fun isSystemApp(packageName: String): Boolean {
        val systemPackages = setOf(
            "com.android.settings",
            "com.android.phone",
            "com.android.dialer",
            "com.google.android.dialer",
            "com.android.contacts",
            "com.google.android.contacts",
            "com.android.messaging",
            "com.google.android.apps.messaging",
            "com.android.emergency",
            "com.android.systemui",
            "com.android.launcher",
            "com.google.android.apps.nexuslauncher"
        )
        return systemPackages.contains(packageName) || packageName.startsWith("com.android.systemui")
    }

    /**
     * Handle when a blocked app is opened by the user.
     * Launches the blocking overlay activity.
     */
    private fun handleBlockedAppOpened(packageName: String) {
        // Debounce: prevent launching overlay multiple times rapidly
        val now = System.currentTimeMillis()
        if (packageName == lastBlockedPackage && now - lastBlockTime < BLOCK_DEBOUNCE_MS) {
            return
        }
        lastBlockedPackage = packageName
        lastBlockTime = now

        Log.i(TAG, "Blocked app opened: $packageName")

        // Launch the blocking overlay
        val intent = Intent(this, BlockingOverlayActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or 
                    Intent.FLAG_ACTIVITY_CLEAR_TOP or
                    Intent.FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS
            putExtra("blocked_package", packageName)
        }
        
        try {
            startActivity(intent)
        } catch (e: Exception) {
            Log.e(TAG, "Failed to launch overlay: ${e.message}")
        }
    }

    // ─── Notification (Foreground Service) ───

    /**
     * Show a persistent notification indicating that blocking is active.
     * This helps users understand why the accessibility service is running.
     */
    fun showBlockingNotification() {
        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_SINGLE_TOP
        }
        val pendingIntent = PendingIntent.getActivity(
            this, 0, intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val stopIntent = Intent(ACTION_STOP_BLOCKING).apply {
            setPackage(packageName)
        }
        val stopPendingIntent = PendingIntent.getBroadcast(
            this, 1, stopIntent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Bible Brick is Active")
            .setContentText("Blocking distracting apps. Stay focused on God's Word.")
            .setSmallIcon(R.drawable.ic_notification) // Add your notification icon
            .setContentIntent(pendingIntent)
            .setOngoing(true)
            .setPriority(NotificationCompat.PRIORITY_LOW)
            .addAction(0, "Stop Blocking", stopPendingIntent)
            .build()

        startForeground(NOTIFICATION_ID, notification)
    }

    /**
     * Hide the blocking notification.
     */
    fun hideBlockingNotification() {
        stopForeground(STOP_FOREGROUND_REMOVE)
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "App Blocking",
                NotificationManager.IMPORTANCE_LOW
            ).apply {
                description = "Shows when Bible Brick is actively blocking apps"
                setShowBadge(false)
            }
            notificationManager.createNotificationChannel(channel)
        }
    }

    // ─── Broadcast Receiver ───

    /**
     * Receives commands from the Flutter plugin to update blocking state.
     */
    private val commandReceiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context, intent: Intent) {
            when (intent.action) {
                ACTION_UPDATE_BLOCKED_APPS -> {
                    val apps = intent.getStringArrayExtra(EXTRA_BLOCKED_APPS) ?: return
                    blockedPackages.clear()
                    blockedPackages.addAll(apps)
                    isBlockingActive = blockedPackages.isNotEmpty()
                    
                    if (isBlockingActive) {
                        showBlockingNotification()
                    }
                    Log.i(TAG, "Updated blocked apps: ${blockedPackages.size} apps")
                }
                ACTION_STOP_BLOCKING -> {
                    blockedPackages.clear()
                    isBlockingActive = false
                    hideBlockingNotification()
                    Log.i(TAG, "Blocking stopped")
                }
            }
        }
    }
}
```

### Step 5: Kotlin Overlay Activity

Create the full-screen blocking overlay that appears when a blocked app is opened.

**File**: `android/app/src/main/kotlin/com/biblebrick/app/BlockingOverlayActivity.kt`

```kotlin
package com.biblebrick.app

import android.app.Activity
import android.app.ActivityManager
import android.content.Context
import android.content.Intent
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.VibrationEffect
import android.os.Vibrator
import android.util.Log
import android.view.KeyEvent
import android.view.View
import android.view.WindowManager
import android.view.animation.Animation
import android.view.animation.AnimationUtils
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.core.content.ContextCompat
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.embedding.engine.FlutterEngineCache
import io.flutter.plugin.common.MethodChannel

/**
 * Full-screen overlay activity shown when a blocked app is opened.
 *
 * This activity appears on top of the blocked app, preventing the user
 * from interacting with it. The user must either:
 * 1. Tap "Tap to Unbrick" — navigates to the UnbrickScreen to complete a Bible task
 * 2. Use Emergency Unlock — breaks streak but allows immediate access
 *
 * ## Security Features
 * - Cannot be dismissed via back button
 * - Shows above lock screen
 * - Vibration feedback on appearance
 * - Covers entire screen with translucent overlay
 */
class BlockingOverlayActivity : Activity() {

    companion object {
        private const val TAG = "BibleBrickOverlay"
        private const val UNBRICK_CHANNEL = "com.biblebrick/unbrick"
    }

    private lateinit var vibrator: Vibrator
    private var blockedPackage: String? = null
    private var emergencyTapCount = 0
    private val EMERGENCY_TAPS_REQUIRED = 5

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        blockedPackage = intent.getStringExtra("blocked_package")
        vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator

        // Configure window for overlay appearance
        setupWindow()
        
        // Set the layout
        setContentView(R.layout.activity_blocking_overlay)

        // Initialize UI
        initializeUI()
        
        // Provide haptic feedback
        vibrate()
    }

    /**
     * Configure window to appear above other apps and lock screen.
     */
    private fun setupWindow() {
        window.apply {
            // Make window appear above lock screen
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O_MR1) {
                setShowWhenLocked(true)
                setTurnScreenOn(true)
            } else {
                @Suppress("DEPRECATION")
                addFlags(
                    WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED or
                    WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON
                )
            }
            
            // Keep the window active
            addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
            
            // Layout as fullscreen overlay
            setLayout(
                WindowManager.LayoutParams.MATCH_PARENT,
                WindowManager.LayoutParams.MATCH_PARENT
            )
        }
        
        // Hide navigation bar for immersive experience
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            window.decorView.systemUiVisibility = (
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                or View.SYSTEM_UI_FLAG_FULLSCREEN
                or View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                or View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                or View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                or View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            )
        }
    }

    /**
     * Initialize UI components and set up click listeners.
     */
    private fun initializeUI() {
        // Brick icon with pulsing animation
        val brickIcon = findViewById<ImageView>(R.id.brick_icon)
        val pulseAnimation = AnimationUtils.loadAnimation(this, R.anim.pulse_slow)
        brickIcon.startAnimation(pulseAnimation)

        // Title: "Bricked by Bible Brick"
        val titleText = findViewById<TextView>(R.id.title_text)
        titleText.text = getString(R.string.overlay_title)

        // Subtitle message
        val subtitleText = findViewById<TextView>(R.id.subtitle_text)
        subtitleText.text = getString(
            R.string.overlay_subtitle,
            getAppName(blockedPackage)
        )

        // Scripture reference
        val scriptureText = findViewById<TextView>(R.id.scripture_text)
        scriptureText.text = getRandomScripture()

        // "Tap to Unbrick" button
        val unbrickButton = findViewById<Button>(R.id.unbrick_button)
        unbrickButton.setOnClickListener {
            navigateToUnbrick()
        }

        // Emergency unlock area (hidden, requires multiple taps)
        val emergencyArea = findViewById<TextView>(R.id.emergency_text)
        emergencyArea.setOnClickListener {
            handleEmergencyTap()
        }
    }

    /**
     * Navigate to the UnbrickScreen in the Flutter app.
     * The user must complete a Bible task to unlock.
     */
    private fun navigateToUnbrick() {
        // Launch the Flutter activity with a flag to show unbrick screen
        val intent = Intent(this, MainActivity::class.java).apply {
            action = "com.biblebrick.action.UNBRICK"
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
            putExtra("from_overlay", true)
            putExtra("blocked_package", blockedPackage)
        }
        startActivity(intent)
        
        // Finish this overlay
        finish()
    }

    /**
     * Handle taps on the emergency unlock area.
     * Requires multiple consecutive taps to prevent accidental activation.
     */
    private fun handleEmergencyTap() {
        emergencyTapCount++
        
        if (emergencyTapCount >= EMERGENCY_TAPS_REQUIRED) {
            // Show emergency unlock confirmation
            showEmergencyConfirmation()
        } else {
            // Show remaining taps needed
            val remaining = EMERGENCY_TAPS_REQUIRED - emergencyTapCount
            val hintText = findViewById<TextView>(R.id.emergency_text)
            hintText.text = "Tap $remaining more times for emergency unlock"
            
            // Reset count after delay
            Handler(Looper.getMainLooper()).postDelayed({
                emergencyTapCount = 0
                hintText.text = getString(R.string.overlay_emergency_hint)
            }, 3000)
        }
    }

    /**
     * Show emergency unlock confirmation dialog.
     */
    private fun showEmergencyConfirmation() {
        val dialog = android.app.AlertDialog.Builder(this)
            .setTitle("Emergency Unlock")
            .setMessage("This will break your streak and leave a gap in your wall. Are you sure?")
            .setPositiveButton("Yes, Unlock") { _, _ ->
                performEmergencyUnlock()
            }
            .setNegativeButton("Stay Focused", null)
            .setCancelable(false)
            .create()
        
        dialog.window?.setType(WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY)
        dialog.show()
    }

    /**
     * Perform emergency unlock — stops blocking and returns to home.
     */
    private fun performEmergencyUnlock() {
        // Send emergency unlock event to Flutter
        val engine = FlutterEngineCache.getInstance().get("biblebrick_engine")
        engine?.let {
            MethodChannel(it.dartExecutor.binaryMessenger, UNBRICK_CHANNEL)
                .invokeMethod("emergency_unlock", mapOf("package" to (blockedPackage ?: "")))
        }
        
        // Stop blocking
        AppBlockingAccessibilityService.isBlockingActive = false
        AppBlockingAccessibilityService.blockedPackages.clear()
        
        // Send broadcast to stop blocking
        sendBroadcast(Intent(AppBlockingAccessibilityService.ACTION_STOP_BLOCKING).apply {
            setPackage(packageName)
        })
        
        // Go to home screen
        val homeIntent = Intent(Intent.ACTION_MAIN).apply {
            addCategory(Intent.CATEGORY_HOME)
            flags = Intent.FLAG_ACTIVITY_NEW_TASK
        }
        startActivity(homeIntent)
        
        finish()
    }

    /**
     * Provide haptic feedback when overlay appears.
     */
    private fun vibrate() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val effect = VibrationEffect.createOneShot(300, VibrationEffect.DEFAULT_AMPLITUDE)
            vibrator.vibrate(effect)
        } else {
            @Suppress("DEPRECATION")
            vibrator.vibrate(300)
        }
    }

    /**
     * Get a human-readable app name from a package name.
     */
    private fun getAppName(packageName: String?): String {
        if (packageName == null) return "this app"
        return try {
            val pm = packageManager
            val appInfo = pm.getApplicationInfo(packageName, 0)
            pm.getApplicationLabel(appInfo).toString()
        } catch (e: Exception) {
            packageName
        }
    }

    /**
     * Get a random encouraging scripture for the overlay.
     */
    private fun getRandomScripture(): String {
        val scriptures = listOf(
            "\"I can do all things through Christ who strengthens me.\" — Philippians 4:13",
            "\"Be strong and courageous. Do not be afraid.\" — Joshua 1:9",
            "\"Set your minds on things above, not on earthly things.\" — Colossians 3:2",
            "\"No temptation has overtaken you except what is common to mankind.\" — 1 Corinthians 10:13",
            "\"Your word is a lamp to my feet and a light to my path.\" — Psalm 119:105",
            "\"Submit yourselves to God. Resist the devil, and he will flee from you.\" — James 4:7",
            "\"Whatever you do, work at it with all your heart.\" — Colossians 3:23"
        )
        return scriptures.random()
    }

    // ─── Security Overrides ───

    /**
     * Prevent dismissal via back button.
     */
    override fun onBackPressed() {
        // Ignore back button — user must complete unbrick or emergency unlock
        // Provide subtle feedback
        vibrate()
    }

    /**
     * Prevent dismissal via recent apps button.
     */
    override fun onKeyDown(keyCode: Int, event: KeyEvent?): Boolean {
        if (keyCode == KeyEvent.KEYCODE_APP_SWITCH || keyCode == KeyEvent.KEYCODE_HOME) {
            // Cannot intercept HOME, but we can handle APP_SWITCH
            return true
        }
        return super.onKeyDown(keyCode, event)
    }

    /**
     * Ensure overlay stays on top.
     */
    override fun onWindowFocusChanged(hasFocus: Boolean) {
        super.onWindowFocusChanged(hasFocus)
        if (!hasFocus) {
            // Re-apply immersive mode if focus is lost
            Handler(Looper.getMainLooper()).postDelayed({
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
                    window.decorView.systemUiVisibility = (
                        View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                        or View.SYSTEM_UI_FLAG_FULLSCREEN
                        or View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                    )
                }
            }, 100)
        }
    }

    /**
     * Prevent activity from being killed when user switches apps.
     */
    override fun onPause() {
        super.onPause()
        // Bring overlay back to front if blocking is still active
        if (AppBlockingAccessibilityService.isBlockingActive) {
            val intent = Intent(this, BlockingOverlayActivity::class.java).apply {
                flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
                putExtra("blocked_package", blockedPackage)
            }
            startActivity(intent)
        }
    }
}
```

#### Overlay Layout XML

**File**: `android/app/src/main/res/layout/activity_blocking_overlay.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#CC2C1810">

    <!-- Main Content -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:gravity="center"
        android:orientation="vertical"
        android:padding="32dp">

        <!-- Brick Icon -->
        <ImageView
            android:id="@+id/brick_icon"
            android:layout_width="80dp"
            android:layout_height="80dp"
            android:src="@drawable/ic_brick"
            android:contentDescription="Brick icon" />

        <!-- Title -->
        <TextView
            android:id="@+id/title_text"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="24dp"
            android:text="Bricked by Bible Brick"
            android:textColor="#D4A843"
            android:textSize="28sp"
            android:textStyle="bold"
            android:textAlignment="center" />

        <!-- Subtitle -->
        <TextView
            android:id="@+id/subtitle_text"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="16dp"
            android:text="This app is blocked during your focus time."
            android:textColor="#F5F0E8"
            android:textSize="16sp"
            android:textAlignment="center" />

        <!-- Scripture -->
        <TextView
            android:id="@+id/scripture_text"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="24dp"
            android:padding="16dp"
            android:textColor="#E8A598"
            android:textSize="14sp"
            android:textStyle="italic"
            android:textAlignment="center"
            android:background="@drawable/scripture_background" />

        <!-- Unbrick Button -->
        <Button
            android:id="@+id/unbrick_button"
            android:layout_width="match_parent"
            android:layout_height="56dp"
            android:layout_marginTop="32dp"
            android:text="Tap to Unbrick"
            android:textColor="#2C1810"
            android:textSize="18sp"
            android:textStyle="bold"
            android:backgroundTint="#D4A843"
            android:elevation="4dp" />

    </LinearLayout>

    <!-- Emergency Unlock (bottom area, subtle) -->
    <TextView
        android:id="@+id/emergency_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center|bottom"
        android:layout_marginBottom="48dp"
        android:text="@string/overlay_emergency_hint"
        android:textColor="#80F5F0E8"
        android:textSize="12sp"
        android:padding="16dp" />

</FrameLayout>
```

#### Overlay Theme

**File**: `android/app/src/main/res/values/styles.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Launcher Theme -->
    <style name="LaunchTheme" parent="@android:style/Theme.Light.NoActionBar">
        <item name="android:windowBackground">@drawable/launch_background</item>
    </style>

    <!-- Normal Theme -->
    <style name="NormalTheme" parent="@android:style/Theme.Light.NoActionBar">
        <item name="android:windowBackground">?android:colorBackground</item>
    </style>

    <!-- Blocking Overlay Theme — Full screen, no action bar, translucent -->
    <style name="BlockingOverlayTheme" parent="@android:style/Theme.NoActionBar.Fullscreen">
        <item name="android:windowBackground">#CC2C1810</item>
        <item name="android:windowIsTranslucent">true</item>
        <item name="android:windowNoTitle">true</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:windowFullscreen">true</item>
        <item name="android:windowContentOverlay">@null</item>
    </style>
</resources>
```

Add string resources:

**File**: `android/app/src/main/res/values/strings.xml` (append to existing)

```xml
    <string name="overlay_title">Bricked by Bible Brick</string>
    <string name="overlay_subtitle">%1$s is blocked during your focus time. Stay strong in the Word.</string>
    <string name="overlay_emergency_hint">Emergency unlock</string>
```

### Step 6: Dart Android Blocking Handler

Update the Android-specific app blocking implementation.

**File**: `lib/core/services/android_app_blocking.dart`

```dart
// lib/core/services/android_app_blocking.dart
// ---------------------------------------------------------------------------
// Android implementation using AccessibilityService + Overlay.
//
// On Android, app blocking uses:
//   1. AccessibilityService — detects when blocked apps are opened
//   2. SYSTEM_ALERT_WINDOW overlay — shows the blocking screen
//   3. android_intent_plus — redirects user back to home/our app
//
// Required permissions:
//   - BIND_ACCESSIBILITY_SERVICE (system-level, user must enable manually)
//   - SYSTEM_ALERT_WINDOW (overlay permission)
//   - PACKAGE_USAGE_STATS (optional, for app usage tracking)
//   - FOREGROUND_SERVICE (for background operation)
//
/// NOTE: Due to Android security restrictions, we cannot fully prevent
/// app launches on Android 10+ without accessibility service. The overlay
/// approach catches launches and immediately redirects the user.
// ---------------------------------------------------------------------------

import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:android_intent_plus/android_intent.dart';
import 'package:android_intent_plus/flag.dart';
import 'package:permission_handler/permission_handler.dart';

import '../models/app_info.dart';

/// Android-specific app blocking using accessibility service + overlay.
///
/// This class communicates with native Kotlin code via a MethodChannel
/// to control the accessibility service. It is not intended for direct use —
/// call [AppBlockingService] instead, which delegates here on Android.
///
/// ## Platform Requirements
/// - Android 5.0 (API 21) minimum
/// - Accessibility service must be manually enabled by user
/// - Overlay permission for blocking screen
///
/// ## Known Limitations
/// - User must manually enable accessibility service in Settings
/// - OEMs may kill the service in background (needs battery whitelist)
/// - Cannot block system apps (Phone, Settings, etc.)
/// - Some OEMs require additional permissions (Xiaomi, Huawei)
class AndroidAppBlocking {
  AndroidAppBlocking({required MethodChannel channel}) : _channel = channel;

  final MethodChannel _channel;
  bool _initialized = false;

  /// The dedicated method channel for Android blocking operations.
  static const MethodChannel _androidChannel = MethodChannel(
    'com.biblebrick/android_blocking',
  );

  /// Whether the accessibility service is initialized.
  bool get isInitialized => _initialized;

  // ─── Initialization ───

  /// Initialize the accessibility service connection.
  Future<void> initialize() async {
    if (_initialized) return;

    try {
      await _channel.invokeMethod('android_initialize');
      _initialized = true;
    } catch (e) {
      throw AndroidAppBlockingException(
        'Failed to initialize Android app blocking service. '
        'Please ensure accessibility service is enabled.',
        originalError: e,
      );
    }
  }

  // ─── Permissions ───

  /// Request all required permissions for app blocking.
  ///
  /// On Android, this:
  /// 1. Checks if accessibility service is enabled
  /// 2. Opens accessibility settings if not enabled
  /// 3. Checks overlay permission
  /// 4. Opens overlay settings if not granted
  ///
  /// Returns `true` if all permissions are granted.
  Future<bool> requestPermissions() async {
    bool hasAllPermissions = true;

    // Check accessibility service
    final accessibilityEnabled = await isAccessibilityEnabled();
    if (!accessibilityEnabled) {
      await openAccessibilitySettings();
      hasAllPermissions = false;
    }

    // Check overlay permission
    final overlayGranted = await hasOverlayPermission();
    if (!overlayGranted) {
      await requestOverlayPermission();
      hasAllPermissions = false;
    }

    return hasAllPermissions;
  }

  /// Check if the accessibility service is enabled.
  Future<bool> isAccessibilityEnabled() async {
    try {
      final result = await _channel.invokeMethod<bool>(
        'android_isAccessibilityEnabled',
      );
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  /// Open Android accessibility settings so the user can enable our service.
  ///
  /// The user must find "Bible Brick App Blocker" in the list and toggle it ON.
  Future<void> openAccessibilitySettings() async {
    try {
      await _channel.invokeMethod('android_requestAccessibility');
    } catch (e) {
      // Fallback: open settings directly via intent
      final intent = AndroidIntent(
        action: 'android.settings.ACCESSIBILITY_SETTINGS',
        flags: [Flag.FLAG_ACTIVITY_NEW_TASK],
      );
      await intent.launch();
    }
  }

  /// Check if overlay permission (SYSTEM_ALERT_WINDOW) is granted.
  Future<bool> hasOverlayPermission() async {
    try {
      final result = await _channel.invokeMethod<bool>(
        'android_hasOverlayPermission',
      );
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  /// Request overlay permission.
  ///
  /// On Android 6+ (API 23+), this opens the system settings where the user
  /// must manually grant "Draw over other apps" permission.
  Future<void> requestOverlayPermission() async {
    if (Platform.isAndroid) {
      final intent = AndroidIntent(
        action: 'android.settings.action.MANAGE_OVERLAY_PERMISSION',
        data: 'package:${await _getPackageName()}',
        flags: [Flag.FLAG_ACTIVITY_NEW_TASK],
      );
      await intent.launch();
    }
  }

  /// Check if usage stats permission is granted (for app detection).
  Future<bool> hasUsageStatsPermission() async {
    try {
      final result = await _channel.invokeMethod<bool>(
        'android_hasUsageStatsPermission',
      );
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  /// Open usage stats permission settings.
  Future<void> openUsageStatsSettings() async {
    final intent = AndroidIntent(
      action: 'android.settings.USAGE_ACCESS_SETTINGS',
      flags: [Flag.FLAG_ACTIVITY_NEW_TASK],
    );
    await intent.launch();
  }

  // ─── Blocking Operations ───

  /// Start blocking the specified apps.
  ///
  /// Sends the list of package names to the native accessibility service.
  /// The service will monitor for these apps being opened and show the
  /// blocking overlay when detected.
  ///
  /// Returns `true` if blocking was successfully initiated.
  Future<bool> startBlocking(List<AppInfo> appsToBlock) async {
    final packageNames = _extractPackageNames(appsToBlock);

    if (packageNames.isEmpty) {
      return false;
    }

    try {
      final result = await _channel.invokeMethod<bool>(
        'android_startBlocking',
        {'packageNames': packageNames},
      );
      return result ?? false;
    } on PlatformException catch (e) {
      throw AndroidAppBlockingException(
        'Failed to start blocking: ${e.message}',
        code: e.code,
        originalError: e,
      );
    } catch (e) {
      return false;
    }
  }

  /// Stop the accessibility service and hide overlay.
  Future<void> stopBlocking() async {
    try {
      await _channel.invokeMethod('android_stopBlocking');
    } on PlatformException catch (e) {
      throw AndroidAppBlockingException(
        'Failed to stop blocking: ${e.message}',
        code: e.code,
        originalError: e,
      );
    } catch (e) {
      // Service may already be stopped
    }
  }

  /// Check if a specific package is currently blocked.
  Future<bool> isAppBlocked(String packageName) async {
    try {
      final result = await _channel.invokeMethod<bool>(
        'android_isAppBlocked',
        {'packageName': packageName},
      );
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  // ─── Overlay ───

  /// Show the blocking overlay (full-screen "apps are locked" UI).
  Future<void> showBlockingOverlay() async {
    try {
      await _channel.invokeMethod('android_showOverlay');
    } catch (e) {
      // Overlay permission may not be granted
    }
  }

  /// Hide the blocking overlay.
  Future<void> hideBlockingOverlay() async {
    try {
      await _channel.invokeMethod('android_hideOverlay');
    } catch (e) {
      // Overlay may not be showing
    }
  }

  // ─── Battery Optimization ───

  /// Request to be whitelisted from battery optimization.
  ///
  /// Some OEMs aggressively kill background services. Being on the
  /// battery optimization whitelist helps keep the accessibility service alive.
  Future<bool> requestBatteryOptimizationWhitelist() async {
    if (Platform.isAndroid) {
      final intent = AndroidIntent(
        action: 'android.settings.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS',
        data: 'package:${await _getPackageName()}',
        flags: [Flag.FLAG_ACTIVITY_NEW_TASK],
      );
      await intent.launch();
      return true;
    }
    return false;
  }

  // ─── App Discovery ───

  /// Get list of installed apps that can be blocked.
  ///
  /// Returns a list of maps with keys: `packageName`, `appName`, `category`.
  Future<List<Map<String, dynamic>>> getInstalledApps() async {
    try {
      final result = await _channel.invokeMethod<List<dynamic>>(
        'android_getInstalledApps',
      );
      return result?.cast<Map<String, dynamic>>() ?? [];
    } catch (e) {
      return [];
    }
  }

  // ─── Helpers ───

  /// Extract package names from a list of AppInfo objects.
  List<String> _extractPackageNames(List<AppInfo> apps) {
    return apps.map((a) => a.packageName).toList();
  }

  /// Get the app's package name.
  Future<String> _getPackageName() async {
    try {
      final result = await _channel.invokeMethod<String>('android_getPackageName');
      return result ?? 'com.biblebrick.app';
    } catch (e) {
      return 'com.biblebrick.app';
    }
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// Custom Exception
// ─────────────────────────────────────────────────────────────────────────────

/// Exception thrown when an Android app blocking operation fails.
class AndroidAppBlockingException implements Exception {
  const AndroidAppBlockingException(
    this.message, {
    this.code,
    this.originalError,
  });

  /// Human-readable error message.
  final String message;

  /// Platform error code (if available).
  final String? code;

  /// The original error for debugging.
  final Object? originalError;

  @override
  String toString() =>
      'AndroidAppBlockingException: $message (code: $code)';
}
```

### Step 7: Method Channel Plugin Registration

Create the Flutter plugin handler on the Android side.

**File**: `android/app/src/main/kotlin/com/biblebrick/app/AppBlockingPlugin.kt`

```kotlin
package com.biblebrick.app

import android.content.Context
import android.content.Intent
import android.os.Build
import android.provider.Settings
import android.util.Log
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodCall
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugin.common.MethodChannel.MethodCallHandler
import io.flutter.plugin.common.MethodChannel.Result
import io.flutter.plugin.common.PluginRegistry.Registrar
import java.util.concurrent.ConcurrentHashMap

/**
 * Flutter plugin that bridges app blocking functionality on Android.
 *
 * Handles method calls from Dart via the `com.biblebrick/app_blocking`
 * and `com.biblebrick/android_blocking` channels, translating them to
 * Android accessibility service and overlay operations.
 */
class AppBlockingPlugin(private val context: Context) : MethodCallHandler {

    companion object {
        private const val TAG = "AppBlockingPlugin"
        private const val MAIN_CHANNEL = "com.biblebrick/app_blocking"
        private const val ANDROID_CHANNEL = "com.biblebrick/android_blocking"

        /**
         * Register this plugin with the Flutter engine.
         */
        fun registerWith(engine: FlutterEngine, context: Context) {
            val plugin = AppBlockingPlugin(context)
            
            MethodChannel(engine.dartExecutor.binaryMessenger, MAIN_CHANNEL)
                .setMethodCallHandler(plugin)
            MethodChannel(engine.dartExecutor.binaryMessenger, ANDROID_CHANNEL)
                .setMethodCallHandler(plugin)
        }
    }

    override fun onMethodCall(call: MethodCall, result: Result) {
        when (call.method) {
            // ─── Shared Channel Methods ───
            "requestPermissions" -> handleRequestPermissions(result)
            "hasPermissions" -> handleHasPermissions(result)
            "getBlockedApps" -> handleGetBlockedApps(result)
            "android_initialize" -> handleInitialize(result)
            "ios_initialize" -> result.success(true) // No-op on Android

            // ─── Android-Specific Methods ───
            "android_startBlocking" -> handleStartBlocking(call, result)
            "android_stopBlocking" -> handleStopBlocking(result)
            "android_isAppBlocked" -> handleIsAppBlocked(call, result)
            "android_showOverlay" -> handleShowOverlay(result)
            "android_hideOverlay" -> handleHideOverlay(result)
            "android_requestAccessibility" -> handleRequestAccessibility(result)
            "android_isAccessibilityEnabled" -> handleIsAccessibilityEnabled(result)
            "android_hasOverlayPermission" -> handleHasOverlayPermission(result)
            "android_requestOverlay" -> handleRequestOverlay(result)
            "android_hasUsageStatsPermission" -> handleHasUsageStatsPermission(result)
            "android_getInstalledApps" -> handleGetInstalledApps(result)
            "android_getPackageName" -> result.success(context.packageName)

            // ─── iOS-Specific Methods (not supported) ───
            "ios_startBlocking", "ios_stopBlocking", "ios_isAppBlocked",
            "ios_requestAuthorization", "ios_hasAuthorization",
            "ios_updateBlockedApps" -> result.notImplemented()

            else -> result.notImplemented()
        }
    }

    // ─── Handler Implementations ───

    private fun handleInitialize(result: Result) {
        result.success(true)
    }

    private fun handleRequestPermissions(result: Result) {
        val accessibilityEnabled = isAccessibilityServiceEnabled()
        val overlayEnabled = canDrawOverlays()

        if (!accessibilityEnabled) {
            openAccessibilitySettings()
        }
        if (!overlayEnabled) {
            requestOverlayPermission()
        }

        result.success(accessibilityEnabled && overlayEnabled)
    }

    private fun handleHasPermissions(result: Result) {
        result.success(isAccessibilityServiceEnabled() && canDrawOverlays())
    }

    private fun handleStartBlocking(call: MethodCall, result: Result) {
        val packageNames = call.argument<List<String>>("packageNames") ?: emptyList()
        
        if (packageNames.isEmpty()) {
            result.success(false)
            return
        }

        // Send broadcast to update the accessibility service
        val intent = Intent(AppBlockingAccessibilityService.ACTION_UPDATE_BLOCKED_APPS).apply {
            setPackage(context.packageName)
            putExtra(AppBlockingAccessibilityService.EXTRA_BLOCKED_APPS, packageNames.toTypedArray())
        }
        context.sendBroadcast(intent)

        Log.i(TAG, "Started blocking ${packageNames.size} apps")
        result.success(true)
    }

    private fun handleStopBlocking(result: Result) {
        val intent = Intent(AppBlockingAccessibilityService.ACTION_STOP_BLOCKING).apply {
            setPackage(context.packageName)
        }
        context.sendBroadcast(intent)
        
        Log.i(TAG, "Stopped blocking")
        result.success(true)
    }

    private fun handleIsAppBlocked(call: MethodCall, result: Result) {
        val packageName = call.argument<String>("packageName") ?: ""
        result.success(
            AppBlockingAccessibilityService.isBlockingActive &&
            AppBlockingAccessibilityService.blockedPackages.contains(packageName)
        )
    }

    private fun handleGetBlockedApps(result: Result) {
        result.success(ArrayList(AppBlockingAccessibilityService.blockedPackages))
    }

    private fun handleShowOverlay(result: Result) {
        // Overlay is shown automatically by the accessibility service
        result.success(true)
    }

    private fun handleHideOverlay(result: Result) {
        // Overlay is hidden automatically when blocking stops
        result.success(true)
    }

    private fun handleRequestAccessibility(result: Result) {
        openAccessibilitySettings()
        result.success(true)
    }

    private fun handleIsAccessibilityEnabled(result: Result) {
        result.success(isAccessibilityServiceEnabled())
    }

    private fun handleHasOverlayPermission(result: Result) {
        result.success(canDrawOverlays())
    }

    private fun handleRequestOverlay(result: Result) {
        requestOverlayPermission()
        result.success(true)
    }

    private fun handleHasUsageStatsPermission(result: Result) {
        result.success(hasUsageStatsPermission())
    }

    private fun handleGetInstalledApps(result: Result) {
        // Return a list of installed apps with package names
        val pm = context.packageManager
        val apps = pm.getInstalledApplications(0)
            .filter { (it.flags and android.content.pm.ApplicationInfo.FLAG_SYSTEM) == 0 }
            .map { appInfo ->
                mapOf(
                    "packageName" to appInfo.packageName,
                    "appName" to pm.getApplicationLabel(appInfo).toString(),
                    "category" to "other"
                )
            }
        result.success(apps)
    }

    // ─── Permission Helpers ───

    private fun isAccessibilityServiceEnabled(): Boolean {
        val enabledServices = Settings.Secure.getString(
            context.contentResolver,
            Settings.Secure.ENABLED_ACCESSIBILITY_SERVICES
        ) ?: return false
        
        val serviceName = "${context.packageName}/.AppBlockingAccessibilityService"
        return enabledServices.contains(serviceName)
    }

    private fun openAccessibilitySettings() {
        val intent = Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS).apply {
            flags = android.content.Intent.FLAG_ACTIVITY_NEW_TASK
        }
        context.startActivity(intent)
    }

    private fun canDrawOverlays(): Boolean {
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            Settings.canDrawOverlays(context)
        } else {
            true
        }
    }

    private fun requestOverlayPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            val intent = Intent(
                Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                android.net.Uri.parse("package:${context.packageName}")
            ).apply {
                flags = android.content.Intent.FLAG_ACTIVITY_NEW_TASK
            }
            context.startActivity(intent)
        }
    }

    private fun hasUsageStatsPermission(): Boolean {
        val appOps = context.getSystemService(Context.APP_OPS_SERVICE) as android.app.AppOpsManager
        val mode = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            appOps.unsafeCheckOpNoThrow(
                android.app.AppOpsManager.OPSTR_GET_USAGE_STATS,
                android.os.Process.myUid(),
                context.packageName
            )
        } else {
            @Suppress("DEPRECATION")
            appOps.checkOpNoThrow(
                android.app.AppOpsManager.OPSTR_GET_USAGE_STATS,
                android.os.Process.myUid(),
                context.packageName
            )
        }
        return mode == android.app.AppOpsManager.MODE_ALLOWED
    }
}
```

**File**: `android/app/src/main/kotlin/com/biblebrick/app/BootCompletedReceiver.kt`

```kotlin
package com.biblebrick.app

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log

/**
 * Broadcast receiver that starts the accessibility service after device boot.
 *
 * This ensures that if a Brick Mode was active when the device shut down,
 * blocking will resume after the device restarts.
 */
class BootCompletedReceiver : BroadcastReceiver() {

    companion object {
        private const val TAG = "BibleBrickBoot"
    }

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            Log.i(TAG, "Boot completed — checking if blocking should resume")
            
            // Check if blocking was active before shutdown
            val prefs = context.getSharedPreferences("biblebrick", Context.MODE_PRIVATE)
            val wasBlocking = prefs.getBoolean("was_blocking", false)
            
            if (wasBlocking) {
                Log.i(TAG, "Blocking was active — resuming after boot")
                // The accessibility service will be started by Android when
                // the user enables it. We can't start it programmatically.
                // Instead, show a notification reminding the user to re-enable.
                
                // TODO: Show persistent notification if accessibility service
                // is not enabled but blocking was active
            }
        }
    }
}
```

---

## 4. Architecture Deep Dive

### Service Lifecycle

```
App Launch
    |
    v
User enables Accessibility Service (manual, one-time)
    |
    v
User activates Brick Mode
    |
    v
Flutter: android_startBlocking([packageNames])
    |
    v
Broadcast: ACTION_UPDATE_BLOCKED_APPS
    |
    v
AppBlockingAccessibilityService receives broadcast
    |
    v
blockedPackages Set updated, isBlockingActive = true
    |
    v
Service shows foreground notification
    |
    v
[User opens blocked app]
    |
    v
onAccessibilityEvent(TYPE_WINDOW_STATE_CHANGED)
    |
    v
Package name in blockedPackages? → YES
    |
    v
Launch BlockingOverlayActivity (full-screen)
    |
    v
User completes unbrick OR emergency unlock
    |
    v
Flutter: android_stopBlocking()
    |
    v
Broadcast: ACTION_STOP_BLOCKING
    |
    v
blockedPackages cleared, isBlockingActive = false
    |
    v
Foreground notification removed
```

### Security Considerations

| Threat | Mitigation |
|--------|------------|
| User force-stops accessibility service | Service auto-restarts (Android handles this); persistent notification |
| User disables accessibility service | App detects on resume; prompts to re-enable |
| OEM kills service for battery | Request battery optimization whitelist; foreground service notification |
| User finds blocked app via split-screen | Accessibility service catches window changes in all modes |
| User uses app shortcuts | Window state change is caught |

---

## 5. OEM-Specific Considerations

### Samsung (One UI)

| Issue | Solution |
|-------|----------|
| "Put unused apps to sleep" | Add Bible Brick to "Never sleeping apps" in Device Care |
| Auto-optimize battery | Disable auto-optimization for Bible Brick |

### Xiaomi (MIUI)

| Issue | Solution |
|-------|----------|
| Aggressive background killing | Enable "Auto-start" in App Info > Permissions |
| Battery saver | Add to battery saver whitelist |
| Lock in recent apps | Show user how to lock app in recents |

### Huawei (EMUI)

| Issue | Solution |
|-------|----------|
| App Launch management | Set to "Manual manage" and allow all options |
| Power-intensive prompt | Disable power-intensive app prompt |

### OnePlus (OxygenOS)

| Issue | Solution |
|-------|----------|
| Battery optimization | Disable battery optimization for Bible Brick |
| App locker | Not needed — accessibility service is sufficient |

### Google Pixel (Stock Android)

Most reliable experience. Battery optimization request is usually sufficient.

### General OEM Mitigation

Add this to your Flutter onboarding flow — guide users through their specific OEM settings:

```dart
// Show OEM-specific instructions when enabling accessibility
void showOEMSetupInstructions(BuildContext context) {
  final String manufacturer = Platform.isAndroid 
      ? DeviceInfoPlugin().androidInfo.then((i) => i.manufacturer)
      : '';
  
  switch (manufacturer.toLowerCase()) {
    case 'samsung':
      // Show Samsung-specific instructions
      break;
    case 'xiaomi':
      // Show Xiaomi-specific instructions
      break;
    // ... etc
  }
}
```

---

## 6. Android Limitations

### User Experience Limitations

| Limitation | Details | Workaround |
|------------|---------|------------|
| **Manual Accessibility Enable** | User must manually find and enable the service in Settings | Provide guided setup with screenshots; direct intent to accessibility settings |
| **Scary Permission Warning** | Android shows a scary warning about the service reading screen content | Clear, transparent description in service config; explain in onboarding |
| **Settings App Cannot Be Blocked** | Android prevents blocking system Settings | Document this; user can still self-regulate |
| **Home Button Always Works** | Cannot intercept HOME button | Overlay re-appears immediately due to onPause() restart |

### Technical Limitations

| Limitation | Details | Workaround |
|------------|---------|------------|
| **OEM Background Killing** | Samsung, Xiaomi, Huawei aggressively kill services | Battery optimization whitelist; foreground service; OEM-specific guides |
| **Android 10+ Background Start Restrictions** | Cannot start activities from background | Use full-screen intent notifications; accessibility service exception |
| **Accessibility Service Single Instance** | Only one accessibility service of a given type | Ensure our service is robust; handle all events |
| **No App Kill API** | Cannot force-stop other apps | Overlay approach is the best available |
| **Split Screen / Freeform** | Apps in split screen may bypass | Monitor all window changes, not just full-screen |

### Play Store Policy Limitations

| Limitation | Details | Workaround |
|------------|---------|------------|
| **Accessibility Service Restrictions** | Google restricts accessibility services to apps helping users with disabilities | Our app helps users with self-control (a recognized use case); document clearly |
| **Malware Abuse** | Some malware uses accessibility services | Google's Verify Apps may flag our service | Provide clear privacy policy; be transparent about data usage |

---

## 7. Testing Guide

### Test Environment Setup

1. Physical Android device running Android 8.0+ (API 26+)
2. Or Android Emulator with Google Play Services

### Test Cases

#### Test 1: Accessibility Service Enable Flow

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Fresh install | App launches to onboarding |
| 2 | During setup, tap "Enable App Blocking" | Redirected to Accessibility Settings |
| 3 | Find "Bible Brick App Blocker" and toggle ON | Warning dialog shown; tap OK |
| 4 | Return to app | Green checkmark shown; blocking ready |

#### Test 2: Blocking & Unblocking

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Activate Brick Mode with Instagram blocked | Instagram blocked |
| 2 | Open Instagram | Blocking overlay appears immediately |
| 3 | Tap "Tap to Unbrick" | Navigates to UnbrickScreen |
| 4 | Complete Bible task | Apps unblocked; success animation |
| 5 | Open Instagram | App opens normally |

#### Test 3: Emergency Unlock

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Activate Brick Mode | Apps blocked |
| 2 | Tap emergency area 5 times | Confirmation dialog appears |
| 3 | Confirm emergency unlock | Apps unblocked; streak warning shown |

#### Test 4: Background Persistence

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Activate Brick Mode | Apps blocked |
| 2 | Background the app | Blocking notification visible |
| 3 | Open blocked app | Overlay still appears |
| 4 | Kill app from recents | Overlay still appears (accessibility service survives) |

---

## 8. Troubleshooting

### Common Issues

#### Issue: "Accessibility service not appearing in settings"

**Symptoms**: Can't find "Bible Brick App Blocker" in Accessibility Settings.

**Solutions**:

1. **Service not exported correctly**
   - Ensure `android:exported="true"` in the service declaration
   - Ensure `android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"` is set

2. **App not installed properly**
   - Uninstall and reinstall the app
   - Check logcat for errors during installation

3. **Manifest merge issues**
   - Check `build/app/outputs/logs/manifest-merger-*-report.txt`

#### Issue: "Overlay not appearing when blocked app is opened"

**Symptoms**: Blocked app opens normally, no overlay shown.

**Solutions**:

1. **Accessibility service not enabled**
   - Check Settings > Accessibility > Bible Brick App Blocker is ON

2. **Package name mismatch**
   - Verify package names in blocked list match actual app packages
   - Use `adb shell pm list packages` to find correct names

3. **Service killed by OEM**
   - Add app to battery whitelist
   - Enable auto-start (Xiaomi/Huawei)

4. **Event types not matching**
   - Try removing `packageNames` filter from accessibility_service_config.xml
   - Add logging in `onAccessibilityEvent()` to see what events fire

#### Issue: "Overlay appears then immediately disappears"

**Symptoms**: Overlay flashes briefly then gone.

**Solutions**:

1. **Activity finishing too soon**
   - Check that `onPause()` is not calling `finish()` inadvertently
   - Verify `noHistory="false"` in BlockingOverlayActivity manifest (it should be `true` but check)

2. **Another app drawing over**
   - Some apps (Facebook Messenger bubbles, etc.) draw over our overlay
   - Use `TYPE_ACCESSIBILITY_OVERLAY` for higher z-order

#### Issue: "Can still interact with blocked app behind overlay"

**Symptoms**: User can tap through the overlay to the blocked app.

**Solutions**:

1. **Window type not modal**
   - Ensure overlay theme uses full screen with touch interception
   - Add `android:windowIsFloating = false`

2. **Layout not consuming touches**
   - Add `android:clickable="true"` to root layout
   - Add touch listener that consumes all events

### Debug Commands

```bash
# Check if accessibility service is enabled
adb shell settings get secure enabled_accessibility_services

# Check if our service is in the list
adb shell settings get secure enabled_accessibility_services | grep biblebrick

# Check overlay permission
adb shell appops get com.biblebrick.app SYSTEM_ALERT_WINDOW

# View service logs
adb logcat -s BibleBrickA11y:D BibleBrickOverlay:D AppBlockingPlugin:D

# List installed packages (to verify blocked package names)
adb shell pm list packages | grep instagram

# Simulate opening an app
adb shell monkey -p com.instagram.android 1
```

---

## 9. Play Store Compliance

### Accessibility Service Usage Declaration

Google Play requires apps using accessibility services to declare their purpose. Add this to your Play Store listing:

**Description of Accessibility Service Usage:**

```
Bible Brick uses Android's AccessibilityService to detect when the user 
opens apps that they have chosen to block during focus time. When a 
blocked app is detected, Bible Brick displays an overlay screen with 
an encouraging scripture and an option to complete a brief Bible task 
to regain access.

The accessibility service:
- ONLY monitors window state changes (app launches)
- Does NOT collect, read, or transmit any screen content or personal data
- Is ONLY active when the user has activated a Brick Mode
- Can be disabled at any time in Settings > Accessibility
```

### Privacy Policy Requirements

Your privacy policy must include:

1. **Accessibility Service Disclosure**: Explain why the service is needed
2. **Data Collection Statement**: Confirm that NO data is collected via the service
3. **User Control**: Explain how users can enable/disable the service

### Play Store Review Checklist

- [ ] Accessibility service is only used for app blocking (no other functionality)
- [ ] App description clearly explains the accessibility service usage
- [ ] Privacy policy discloses accessibility service usage
- [ ] Service can be easily disabled by the user
- [ ] No data collection through the accessibility service
- [ ] App provides meaningful functionality beyond the accessibility service

---

## 10. Official Google Documentation

### Accessibility Service

- [AccessibilityService API Reference](https://developer.android.com/reference/android/accessibilityservice/AccessibilityService)
- [Building Accessibility Services](https://developer.android.com/guide/topics/ui/accessibility/service)
- [AccessibilityEvent Types](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#constants)

### Overlay Permission

- [SYSTEM_ALERT_WINDOW Permission](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW)
- [WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#TYPE_APPLICATION_OVERLAY)

### Foreground Services

- [Foreground Services](https://developer.android.com/guide/components/foreground-services)
- [Foreground Service Permissions (Android 14+)](https://developer.android.com/about/versions/14/changes/fgs-types-required)

### Battery Optimization

- [Request Ignore Battery Optimizations](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
- [Doze and App Standby](https://developer.android.com/training/monitoring-device-state/doze-standby)

### Play Store Policies

- [Accessibility Service Policy](https://support.google.com/googleplay/android-developer/answer/10964491)
- [User Data Policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Permissions Policy](https://support.google.com/googleplay/android-developer/answer/9888170)
