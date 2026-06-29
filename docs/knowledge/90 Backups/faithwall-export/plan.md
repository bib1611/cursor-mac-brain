# Bible Brick — Complete Build Plan

## Overview
Build a Flutter screen-locking/focus app (iOS + Android) that mirrors the Brick app's custom mode + friction mechanics but with Bible engagement to unlock. Plus a Python YouTube Shorts automation engine.

## Stage 1: Research & Asset Collection (Parallel)
- **Skill**: `deep-research-swarm`
- Study Brick app mechanics, homeschool mom language, competitor landscape
- Collect authentic homeschool mom communication patterns for marketing copy
- Identify free Bible APIs, verse packs, licensing
- **Output**: Research brief with verified data

## Stage 2: Project Architecture & Scaffolding
- **Skill**: `vibecoding-general-swarm`
- Define complete folder structure (Flutter + Python)
- Design data models (modes, verses, wall progress, user)
- Firebase project setup guide
- **Output**: Full project skeleton, pubspec.yaml, models, constants

## Stage 3: Core Flutter App — MVP (Iterative Batches)
- **Skill**: `vibecoding-general-swarm`
- Sub-stage 3a: Main app shell, navigation, theme (brick/construction aesthetic)
- Sub-stage 3b: Brick Mode Dashboard (CRUD modes, app selection, one-tap brick)
- Sub-stage 3c: Unbrick Flow (verse display, 4 engagement options, speech-to-text)
- Sub-stage 3d: Locking mechanism abstraction (iOS Screen Time API + Android overlay)
- Sub-stage 3e: Progress/Wall visual, streaks, stats
- Sub-stage 3f: Onboarding, Settings, Firebase integration
- **Output**: Runnable Flutter MVP

## Stage 4: Python YouTube Automation Engine
- **Skill**: `vibecoding-general-swarm`
- Verse fetcher (Bible API integration with caching)
- Video generator (MoviePy/FFmpeg: hook → verse → demo → CTA)
- YouTube uploader (Data API v3 with scheduling)
- Cron setup for 4x daily uploads
- **Output**: Complete, runnable Python automation suite

## Stage 5: Documentation & Delivery
- Setup guides (Firebase, API keys, store publishing prep)
- Monetization implementation (in-app purchases)
- README with build/run instructions
- **Output**: Complete deliverable package

## Monetization
- Free: Basic modes, limited unbricks
- Premium ($29-39 lifetime or $4.99/mo): Unlimited modes, family sharing, custom packs, stats

## Tech Stack
- Flutter (latest stable) + Dart
- Firebase (Auth, Firestore, Analytics, Cloud Messaging)
- DeviceActivity (iOS) + Accessibility/Overlay (Android)
- speech_to_text, flutter_tts, provider/riverpod
- Python 3.11+, MoviePy, FFmpeg, google-api-python-client

## Current Date: 2026-05-02
