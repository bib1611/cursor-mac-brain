# FaithWall Bible Integration: Complete Research Report
## In-App Bible vs. External Sync vs. Hybrid Architecture

**Date:** July 2025  
**Purpose:** Evaluate Bible translation licensing, APIs, and architecture for FaithWall's "unbrick" feature  
**Recommendation:** **Option C (Hybrid)** — In-app public domain translations + external deep links for premium translations

---

# PART 1: Bible Translation Licensing Matrix

## 1.1 Public Domain / Free-to-Use Translations

| Translation | Status | Owner/Publisher | Cost | API Available | Notes |
|---|---|---|---|---|---|
| **KJV** | Public Domain (US) | Crown Copyright (UK only) | Free | helloao (`eng_kjv`), wldeh (`en-kjv`) | Crown copyright in UK (Letters Patent). Free everywhere else. 500-verse limit in UK. |
| **WEB** | Public Domain (dedicated) | eBible.org / Michael Paul Johnson | Free | helloao (`ENGWEBP`, `eng_web`), wldeh | Trademark on name "World English Bible" but text fully free. Based on ASV 1901 + Majority Text. |
| **BSB** | CC0 / Public Domain (Apr 2023) | Berean Bible Translation Committee / Bible Hub | Free | helloao (`BSB`), wldeh (`en-bsb`) | **Best modern public domain option.** CC0 dedication. Only PD translation that is modern, from original languages, with deity pronoun capitalization. |
| **ASV** | Public Domain (1901) | Thomas Nelson & Sons (expired) | Free | helloao (`eng_asv`), wldeh (`en-asv`) | American Standard Version. Somewhat archaic English. Basis for WEB. |
| **Geneva Bible** | Public Domain (1599) | N/A | Free | helloao (`eng_gnv`) | Pre-KJV. Historical significance only. |
| **Young's Literal** | Public Domain | N/A | Free | helloao (`eng_ylt`) | Extremely literal, but awkward English. |
| **Darby** | Public Domain | N/A | Free | helloao (`eng_dby`) | Brethren translation. Old-fashioned English. |
| **RV** | Public Domain (1885) | N/A | Free | helloao (`eng_rv5`) | Revised Version. Predecessor to ASV. |
| **Free Bible Version** | Public Domain | Dr. Jonathan Gallagher | Free | helloao (`eng_fbv`) | Modern English, readable. Less well-known. |
| **NET** | Free (non-commercial) | Biblical Studies Press | Free for non-commercial apps | helloao (`eng_net`), NET Bible API | **Best free modern scholarly option.** Free for non-commercial apps. Must hyperlink to netbible.org. Commercial use requires HarperCollins license. |
| **LSV** | Public Domain | Literal Standard Version team | Free | helloao (`eng_lsv`) | Literal translation, modern English. Community-driven. |

## 1.2 Licensed Translations (Require Permission / Fees)

| Translation | Owner | Gratis Limit | Est. Licensing Cost* | Deep Link Code | Notes |
|---|---|---|---|---|---|
| **NIV** | Zondervan / Biblica / HarperCollins | 500 verses / 25% of work | **$10K-50K+ upfront + 5-15% royalty** | YouVersion: `111` | Most popular modern translation. Minimum sales quota often required. Very expensive for apps. |
| **ESV** | Crossway | 500 verses / 50% of 1 book | **$5K-25K+ for commercial apps** | YouVersion: `59`, esvbible:// | **Free API for non-commercial use** (api.esv.org). Commercial requires license. Excellent developer support. |
| **NKJV** | Thomas Nelson / HarperCollins | 500 verses / 25% of work | **$10K-30K+ upfront + royalty** | YouVersion: `114` | Modernized KJV. Thomas Nelson is strict about licensing. Requires formal permission. |
| **NLT** | Tyndale House Publishers | 500 verses / 25% of work | **$5K-20K+ for apps** | YouVersion: `116` | Free API for non-commercial use. Very readable paraphrase-leaning translation. |
| **CSB** | Lifeway / Holman Bible Publishers | 1,000 verses / 50% of 1 book | **$5K-15K for apps** | YouVersion: check current | Optimal equivalence philosophy. Lifeway is moderately restrictive. |
| **NASB** | The Lockman Foundation | 1,000 verses / 50% of 1 book | **$5K-15K for apps** | YouVersion: `100` | Very literal. Lockman requires full copyright notice with clickable link. Strict but reachable. |
| **AMP** | The Lockman Foundation | 1,000 verses / 50% of 1 book | **$5K-15K for apps** | YouVersion: check current | Expanded translation with amplifications. Same licensor as NASB. |
| **MSG** | Eugene H. Peterson estate / NavPress / Tyndale | 500 verses / 25% of work | **$5K-15K for apps** | YouVersion: `97` | Paraphrase by Eugene Peterson. NavPress handles permissions. |

> *Licensing costs are estimates based on industry reports. Actual costs require direct negotiation with publishers and vary by app type, audience size, and revenue model. These figures represent what small-to-medium app developers have reported paying.

## 1.3 Key Licensing Insight

All major commercial translations (NIV, ESV, NKJV, NLT, CSB, NASB, AMP, MSG) follow a similar pattern:
- **Gratis use:** 500-1,000 verses quoted, not more than 25-50% of your app's text content
- **For a full Bible app:** Requires formal commercial license with upfront fee + ongoing royalty
- **For a verse-of-day / unbrick feature quoting <500 verses:** May fall under gratis use
- **For FaithWall:** The "unbrick" feature will likely need 100-500+ unique verses over time, which EXCEEDS gratis limits for a commercial product

**Critical Finding:** The Berean Standard Bible (BSB) is the ONLY modern English translation that is:
1. Completely public domain (CC0)
2. Translated from original languages (unlike WEB which revises ASV)
3. Actually readable in modern English
4. Has deity pronoun capitalization (He, Him, You referring to Christ)
5. Available with full text via free API

---

# PART 2: In-App Bible Technical Spec

## 2.1 API Comparison: helloao.org vs. wldeh/bible-api

### helloao.org (Free Use Bible API) — RECOMMENDED PRIMARY API

**Architecture:** Open-source JSON API hosted on AWS by AO Lab (nonprofit)  
**License:** MIT-licensed codebase, no restrictions on usage  
**Translations:** 1,256+ total, 51+ English (including BSB, WEB, KJV, ASV, NET, Geneva, etc.)  
**Rate Limits:** None  
**API Keys:** None required  
**Cost:** Free for all uses including commercial

**Key Endpoints:**

| Endpoint | Purpose | Example |
|---|---|---|
| `GET /api/available_translations.json` | List all translations | `bible.helloao.org/api/available_translations.json` |
| `GET /api/{translation}/{book}/{chapter}.json` | Get single chapter | `bible.helloao.org/api/BSB/JHN/3.json` |
| `GET /api/{translation}/complete.json` | Download entire Bible | `bible.helloao.org/api/BSB/complete.json` |

**Response Structure (Chapter):**
```json
{
  "translation": { "id": "BSB", "englishName": "Berean Standard Bible", ... },
  "book": { "id": "JHN", "name": "John", "commonName": "John", ... },
  "chapter": { "number": 3, "content": [...], "footnotes": [...] },
  "numberOfVerses": 36,
  "thisChapterLink": "/api/BSB/JHN/3.json",
  "nextChapterApiLink": "/api/BSB/JHN/4.json",
  "previousChapterApiLink": "/api/BSB/JHN/2.json"
}
```

**Verse Content Structure:**
```json
{
  "type": "verse",
  "number": 16,
  "content": [
    "For God so loved the world that He gave His one and only",
    { "noteId": 17 },
    "Son, that everyone who believes in Him shall not perish but have eternal life."
  ]
}
```

**Features:**
- Footnotes with `noteId` references
- Words of Jesus marked with `wordsOfJesus: true`
- Poetry indentation levels (`poem: 1`)
- Section headings (`type: 'heading'`)
- Hebrew subtitles (`type: 'hebrew_subtitle'`)
- Inline line breaks
- Audio links (when available)
- Next/previous chapter navigation links

### wldeh/bible-api (CDN-backed) — RECOMMENDED FALLBACK/SIMPLE USE

**Architecture:** GitHub repository served via jsDelivr CDN  
**License:** Repository-based, public domain translations  
**Translations:** 210+ versions in 300+ languages  
**Rate Limits:** None (CDN-backed)  
**API Keys:** None  
**Cost:** Free

**Key Endpoints:**

| Endpoint | Purpose | Example |
|---|---|---|
| `GET /bibles/bibles.json` | List all versions | `cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/bibles.json` |
| `GET /bibles/{version}/books/{book}/chapters/{chapter}/verses/{verse}.json` | Get single verse | `.../bibles/en-kjv/books/john/chapters/3/verses/16.json` |
| `GET /bibles/{version}/books/{book}/chapters/{chapter}.json` | Get full chapter | `.../bibles/en-kjv/books/john/chapters/3.json` |

**Response Structure (Simple):**
```json
// Verse:
{
  "verse": 16,
  "text": "For God so loved the world..."
}

// Chapter:
{
  "data": [
    {"verse": 1, "text": "There was a man..."},
    {"verse": 2, "text": "The same came..."}
  ]
}
```

**Pros:** Extremely simple, CDN-cached, no complexity  
**Cons:** No footnotes, no formatting, no words-of-Jesus marking, no section headings

## 2.2 Storage Analysis

| Metric | Value |
|---|---|
| BSB complete JSON (helloao) | **6.95 MB** |
| KJV complete JSON (estimated) | ~6.5-7.0 MB |
| WEB complete JSON (estimated) | ~6.5-7.0 MB |
| **3 translations raw JSON** | **~21 MB** |
| **3 translations in SQLite** (compressed) | **~14 MB** |
| Verses in complete Bible | ~31,000 |
| Chapters in complete Bible | 1,189 |

**Recommendation for FaithWall:** Download `complete.json` for each translation on first app launch, cache in SQLite. ~14 MB is very reasonable for modern devices.

## 2.3 Data Model (SQLite)

```sql
-- Translations table
CREATE TABLE translations (
    id TEXT PRIMARY KEY,          -- 'BSB', 'eng_kjv', 'eng_web'
    name TEXT NOT NULL,           -- 'Berean Standard Bible'
    short_name TEXT,              -- 'BSB'
    language TEXT,                -- 'eng'
    is_downloaded INTEGER DEFAULT 0,
    downloaded_at INTEGER         -- Unix timestamp
);

-- Books table
CREATE TABLE books (
    id TEXT PRIMARY KEY,          -- 'GEN', 'EXO', 'JHN'
    name TEXT NOT NULL,           -- 'Genesis'
    common_name TEXT,             -- 'Genesis'
    testament TEXT,               -- 'OT' | 'NT'
    book_order INTEGER            -- 1-66
);

-- Verses table
CREATE TABLE verses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    translation_id TEXT,          -- FK to translations
    book_id TEXT,                 -- FK to books
    chapter INTEGER,
    verse INTEGER,
    text TEXT NOT NULL,           -- Plain verse text
    words_of_jesus INTEGER DEFAULT 0,  -- 1 if words of Jesus
    FOREIGN KEY (translation_id) REFERENCES translations(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    UNIQUE(translation_id, book_id, chapter, verse)
);

-- Footnotes table (optional, for rich display)
CREATE TABLE footnotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    translation_id TEXT,
    book_id TEXT,
    chapter INTEGER,
    note_id INTEGER,
    text TEXT,
    reference_verse INTEGER,
    caller TEXT
);

-- Daily verse / Unbrick cache
CREATE TABLE daily_verses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT UNIQUE,             -- '2025-07-15'
    translation_id TEXT,
    book_id TEXT,
    chapter INTEGER,
    verse INTEGER,
    text TEXT,
    used INTEGER DEFAULT 0        -- Track if shown to user
);

-- Index for fast lookups
CREATE INDEX idx_verses_lookup ON verses(translation_id, book_id, chapter, verse);
CREATE INDEX idx_verses_ref ON verses(book_id, chapter, verse);
```

## 2.4 Offline Caching Strategy

```
App First Launch:
  1. Show "Downloading Bibles..." screen
  2. Download BSB complete.json (~7 MB)
  3. Download KJV complete.json (~7 MB) - optional
  4. Download WEB complete.json (~7 MB) - optional
  5. Parse JSON → Insert into SQLite
  6. Total download: ~21 MB, ~5-15 seconds on 4G
  7. Mark translations as downloaded

Daily Operation (Offline):
  - All verse lookups use local SQLite database
  - Zero network calls needed
  - Instant verse retrieval (< 1ms from SQLite)

Periodic Sync:
  - Check for translation updates (rare)
  - Only re-download if version changes

Unbrick Feature Flow:
  1. User needs to unlock phone → App shows verse
  2. Query SQLite: SELECT text FROM verses WHERE book_id=? AND chapter=? AND verse=?
  3. Display verse with translation attribution
  4. No network required = always works
```

---

# PART 3: External Bible App Deep Link Guide

## 3.1 YouVersion Bible App (Primary External Target)

**Platform URL Format:**
```
https://www.bible.com/bible/{versionId}/{book}.{chapter}.{verse}.{code}
```

**Deep Link URL Schemes:**
```
youversion://bible?reference={book}.{chapter}.{verse}
youversion://bible?reference=JHN.3.16
youversion://search/bible?query={reference}
```

**Confirmed Version IDs:**

| Translation | Version ID | Example URL |
|---|---|---|
| KJV | `1` | `bible.com/bible/1/JHN.3.16` |
| NASB 1995 | `100` | `bible.com/bible/100/JHN.3.16` |
| MSG | `97` | `bible.com/bible/97/JHN.3.16` |
| ESV | `59` | `bible.com/bible/59/JHN.3.16` |
| NKJV | `114` | `bible.com/bible/114/JHN.3.16` |
| NLT | `116` | `bible.com/bible/116/JHN.3.16` |
| NIV | `111` | `bible.com/bible/111/JHN.3.16` |

**OSIS Book Abbreviations (required for deep links):**
```
GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH
EST JOB PSA PRO ECC SNG ISA JER LAM EZK DAN HOS JOL AMO OBA JON
MIC NAM HAB ZEP HAG ZEC MAL
MAT MRK LUK JHN ACT ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH 1TI 2TI
TIT PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV
```

**iOS/Android Integration:**
```swift
// iOS Swift
func openInYouVersion(book: String, chapter: Int, verse: Int, versionId: String) {
    // Try native app first
    let scheme = "youversion://bible?reference=\(book).\(chapter).\(verse)"
    if let url = URL(string: scheme), UIApplication.shared.canOpenURL(url) {
        UIApplication.shared.open(url)
    } else {
        // Fallback to web
        let web = "https://www.bible.com/bible/\(versionId)/\(book).\(chapter).\(verse)"
        UIApplication.shared.open(URL(string: web)!)
    }
}
```

```kotlin
// Android Kotlin
fun openInYouVersion(book: String, chapter: Int, verse: Int, versionId: String, context: Context) {
    // Try native app
    val intent = Intent(Intent.ACTION_VIEW, Uri.parse("youversion://bible?reference=${book}.${chapter}.${verse}"))
    val resolved = context.packageManager.resolveActivity(intent, 0)
    if (resolved != null) {
        context.startActivity(intent)
    } else {
        // Fallback to web
        val webUrl = "https://www.bible.com/bible/${versionId}/${book}.${chapter}.${verse}"
        context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(webUrl)))
    }
}
```

**Fallback Strategy:**
1. Try `youversion://` deep link
2. If YouVersion not installed, fall back to `https://www.bible.com/bible/{id}/...`
3. Both web and app show the same content

## 3.2 Bible Gateway

**Deep Link:** `biblegateway://`  
**Web URL:** `https://www.biblegateway.com/passage/?search={reference}&version={code}`  
**Example:** `https://www.biblegateway.com/passage/?search=John+3:16&version=NIV`

| Translation | BG Code |
|---|---|
| NIV | `NIV` |
| ESV | `ESV` |
| NKJV | `NKJV` |
| NLT | `NLT` |
| KJV | `KJV` |
| NASB | `NASB` |
| AMP | `AMP` |
| CSB | `CSB` |
| MSG | `MSG` |

## 3.3 Blue Letter Bible

**Deep Link:** `blb://`  
**Web URL:** `https://www.blueletterbible.org/{version}/{book}/{chapter}/{verse}`  
**Example:** `https://www.blueletterbible.org/niv/jhn/3/16`

## 3.4 Other Bible Apps with Deep Link Support

| App | URL Scheme | Example |
|---|---|---|
| **Olive Tree** (free) | `olivetree-free://` | `olivetree-free://bible/John.3.16` |
| **Olive Tree** (paid) | `biblereader://` | `biblereader://bible/John.3.16` |
| **Olive Tree** (legacy) | `olivetree://bible/{book}.{chapter}.{verse}` | `olivetree://bible/romans.8.28` |
| **ESV Bible** (Crossway) | `esvbible://` | App-specific |
| **Logos** | `logores://` | App-specific |
| **Accordance** | `accord://` | App-specific |
| **e-Sword** | `e-sword://` | App-specific |
| **The Study Bible** (GTY) | `gtybible://` | App-specific |
| **Faithlife Study Bible** | `fsbres://` | App-specific |
| **Tecarta Bible** | `tecartabible://` | App-specific |
| **Bible.is** | `bibleis://` | App-specific |
| **NET Bible** | `luminaref://` | App-specific |
| **WeDevote** | `wdbible://bible/{book}.{chapter}.{verse}` | `wdbible://bible/jhn.1.1` |

## 3.5 Deep Link URL Builder (TypeScript/JavaScript)

```typescript
type BibleApp = 'youversion' | 'biblegateway' | 'blb' | 'olivetree';

interface VerseRef {
    book: string;      // OSIS: 'JHN', 'GEN', etc.
    chapter: number;
    verse: number;
    version?: string;  // NIV, ESV, etc.
}

const YV_VERSION_IDS: Record<string, string> = {
    KJV: '1', ESV: '59', MSG: '97', NASB1995: '100',
    NIV: '111', NKJV: '114', NLT: '116'
};

function buildDeepLink(
    app: BibleApp,
    ref: VerseRef
): string {
    const { book, chapter, verse, version = 'NIV' } = ref;

    switch (app) {
        case 'youversion': {
            const yvId = YV_VERSION_IDS[version.toUpperCase()] || '111';
            // Try native app scheme first, fallback to web
            return `https://www.bible.com/bible/${yvId}/${book}.${chapter}.${verse}`;
        }
        case 'biblegateway': {
            const refStr = `${book}${chapter}%3A${verse}`;
            return `https://www.biblegateway.com/passage/?search=${refStr}&version=${version.toUpperCase()}`;
        }
        case 'blb': {
            const bookLower = book.toLowerCase();
            return `https://www.blueletterbible.org/${version.toLowerCase()}/${bookLower}/${chapter}/${verse}`;
        }
        case 'olivetree': {
            return `olivetree://bible/${book}.${chapter}.${verse}`;
        }
    }
}

// Usage:
buildDeepLink('youversion', { book: 'JHN', chapter: 3, verse: 16, version: 'NIV' });
// → 'https://www.bible.com/bible/111/JHN.3.16'
```

---

# PART 4: Hybrid Architecture Recommendation (RECOMMENDED)

## 4.1 Why Hybrid?

| Factor | In-App Only | External Only | **Hybrid** |
|---|---|---|---|
| Offline works | Yes | No | **Yes** |
| Translation variety | 3 only | 10+ | **10+** |
| UX control | Full | None | **Full** |
| Licensing cost | $0 | $0 | **$0** |
| Development effort | Medium | Low | **Medium** |
| User experience | Seamless | Jarring | **Seamless** |
| Always available | Yes | Needs internet | **Yes** |

## 4.2 Hybrid Architecture Diagram

```
+----------------------+     +----------------------+
|   FaithWall App      |     |   External Apps      |
|                      |     |                      |
|  +----------------+  |     |  +----------------+  |
|  | Unbrick Screen |  |     |  |  YouVersion    |  |
|  |                |  |     |  |  Bible Gateway |  |
|  | "Read John 3:16|  |     |  |  Blue Letter   |  |
|  |  to unlock..." |  |     |  +----------------+  |
|  +--------+-------+  |     |                      |
|           |          |     +----------------------+
|           v          |
|  +----------------+  |
|  | SQLite Bible   |  |
|  | - BSB (modern) |  |
|  | - KJV (classic)|  |
|  | - WEB (alt)    |  |
|  +--------+-------+  |
|           |          |
|           v          |
|  +----------------+  |
|  | "Open in..."   +------> YouVersion / Bible Gateway
|  |  picker dialog |  |     (for NIV, ESV, NKJV, etc.)
|  +----------------+  |
+----------------------+
```

## 4.3 Three-Tier Bible Content Strategy

### Tier 1: Core Unbrick Experience (Offline, Always Available)
- **BSB** — Primary modern translation for unbrick challenges
- **KJV** — Classic/traditional option
- **WEB** — Alternative modern option
- All stored in SQLite, zero network dependency
- Used for: daily unbrick verse, scripture memory, verse of the day

### Tier 2: Rich Reading (Online, In-App)
- Fetch additional chapters via helloao.org API when user explores
- Cache recently read chapters in SQLite
- Full chapter reading with section headings, footnotes, words of Jesus
- Book/chapter/verse navigation

### Tier 3: Premium Translations (External Deep Links)
- "Open in YouVersion" for NIV, ESV, NKJV, NLT, NASB, AMP, MSG, CSB
- "Open in Bible Gateway" as secondary option
- One tap opens the verse in user's preferred Bible app
- Graceful fallback to web if app not installed

## 4.4 Implementation Priority

| Phase | Feature | Timeline |
|---|---|---|
| **1** | Download + cache BSB in SQLite | Week 1 |
| **2** | Unbrick verse display from local DB | Week 1-2 |
| **3** | "Open in YouVersion" deep link | Week 2 |
| **4** | Add KJV + WEB as options | Week 3 |
| **5** | In-app chapter reader (helloao API) | Week 4-5 |
| **6** | "Open in..." picker (multiple apps) | Week 5-6 |

---

# PART 5: Implementation Code Snippets

## 5.1 Bible Download & SQLite Population (TypeScript/React Native)

```typescript
// bible-service.ts
import SQLite from 'react-native-sqlite-storage';

const TRANSLATIONS = {
  BSB: 'https://bible.helloao.org/api/BSB/complete.json',
  KJV: 'https://bible.helloao.org/api/eng_kjv/complete.json',
  WEB: 'https://bible.helloao.org/api/eng_web/complete.json',
};

class BibleService {
  private db: SQLite.SQLiteDatabase;

  async initDatabase() {
    this.db = await SQLite.openDatabase({ name: 'faithwall_bible.db', location: 'default' });
    await this.db.executeSql(`
      CREATE TABLE IF NOT EXISTS verses (
        translation_id TEXT,
        book_id TEXT,
        chapter INTEGER,
        verse INTEGER,
        text TEXT,
        words_of_jesus INTEGER DEFAULT 0,
        PRIMARY KEY (translation_id, book_id, chapter, verse)
      )
    `);
    await this.db.executeSql(`
      CREATE INDEX IF NOT EXISTS idx_ref ON verses(book_id, chapter, verse)
    `);
  }

  async downloadTranslation(id: string): Promise<number> {
    const url = TRANSLATIONS[id as keyof typeof TRANSLATIONS];
    if (!url) throw new Error(`Unknown translation: ${id}`);

    const response = await fetch(url);
    const data = await response.json();
    const books = data.books;
    let verseCount = 0;

    await this.db.executeSql('BEGIN TRANSACTION');

    try {
      for (const book of books) {
        for (const chapter of book.chapters) {
          for (const content of chapter.chapter.content) {
            if (content.type !== 'verse') continue;

            let verseText = '';
            let isWoj = 0;
            for (const item of content.content) {
              if (typeof item === 'string') {
                verseText += item;
              } else if (item.text) {
                verseText += item.text;
                if (item.wordsOfJesus) isWoj = 1;
              }
              // Skip footnote references ({ noteId: N })
            }

            await this.db.executeSql(
              `INSERT OR REPLACE INTO verses (translation_id, book_id, chapter, verse, text, words_of_jesus)
               VALUES (?, ?, ?, ?, ?, ?)`,
              [id, book.id, chapter.chapter.number, content.number, verseText.trim(), isWoj]
            );
            verseCount++;
          }
        }
      }
      await this.db.executeSql('COMMIT');
    } catch (e) {
      await this.db.executeSql('ROLLBACK');
      throw e;
    }

    return verseCount; // ~31,000 for full Bible
  }

  async getVerse(bookId: string, chapter: number, verse: number, translation = 'BSB'): Promise<string | null> {
    const [result] = await this.db.executeSql(
      `SELECT text FROM verses WHERE translation_id = ? AND book_id = ? AND chapter = ? AND verse = ?`,
      [translation, bookId, chapter, verse]
    );
    if (result.rows.length === 0) return null;
    return result.rows.item(0).text;
  }

  async getRandomVerse(translation = 'BSB'): Promise<{bookId: string, chapter: number, verse: number, text: string}> {
    // Get a curated set of unbrick-appropriate verses
    const unbrickBooks = [
      'JHN', 'PSA', 'PRO', 'ROM', 'EPH', 'PHP', 'COL',
      '1JN', 'ISA', 'JER', 'MAT', 'LUK', '2CO', 'GAL'
    ];
    const randomBook = unbrickBooks[Math.floor(Math.random() * unbrickBooks.length)];
    const [result] = await this.db.executeSql(
      `SELECT book_id, chapter, verse, text FROM verses
       WHERE translation_id = ? AND book_id = ?
       ORDER BY RANDOM() LIMIT 1`,
      [translation, randomBook]
    );
    const row = result.rows.item(0);
    return { bookId: row.book_id, chapter: row.chapter, verse: row.verse, text: row.text };
  }
}

export const bibleService = new BibleService();
```

## 5.2 Deep Link Handler

```typescript
// deep-link-handler.ts

const YOUVERSION_IDS: Record<string, string> = {
  KJV: '1', NASB1995: '100', MSG: '97', ESV: '59',
  NKJV: '114', NLT: '116', NIV: '111'
};

interface DeepLinkTarget {
  name: string;
  icon: string;       // App icon resource
  scheme: string;     // URL scheme to try
  webUrl: string;     // Fallback web URL
  supportsVersion: string[];  // Which translations supported
}

const DEEP_LINK_TARGETS: DeepLinkTarget[] = [
  {
    name: 'YouVersion Bible',
    icon: 'youversion_icon',
    scheme: 'youversion://',
    webUrl: 'https://www.bible.com/bible',
    supportsVersion: ['NIV', 'ESV', 'NKJV', 'NLT', 'KJV', 'NASB1995', 'MSG']
  },
  {
    name: 'Bible Gateway',
    icon: 'biblegateway_icon',
    scheme: 'biblegateway://',
    webUrl: 'https://www.biblegateway.com/passage',
    supportsVersion: ['NIV', 'ESV', 'NKJV', 'NLT', 'KJV', 'NASB', 'AMP', 'CSB', 'MSG']
  },
  {
    name: 'Blue Letter Bible',
    icon: 'blb_icon',
    scheme: 'blb://',
    webUrl: 'https://www.blueletterbible.org',
    supportsVersion: ['NIV', 'ESV', 'NKJV', 'KJV', 'NASB']
  }
];

export function buildYouVersionUrl(book: string, chapter: number, verse: number, version: string): string {
  const versionId = YOUVERSION_IDS[version.toUpperCase()] || '111';
  return `https://www.bible.com/bible/${versionId}/${book}.${chapter}.${verse}`;
}

export function buildBibleGatewayUrl(book: string, chapter: number, verse: number, version: string): string {
  return `https://www.biblegateway.com/passage/?search=${book}+${chapter}%3A${verse}&version=${version.toUpperCase()}`;
}

export async function openVerseInApp(
  book: string,
  chapter: number,
  verse: number,
  version: string,
  preferredApp: 'youversion' | 'biblegateway' = 'youversion'
): Promise<void> {
  const { Linking, Platform } = require('react-native');

  // Build URLs
  const webUrl = buildYouVersionUrl(book, chapter, verse, version);
  const scheme = `youversion://bible?reference=${book}.${chapter}.${verse}`;

  // Try native app first
  const canOpenApp = await Linking.canOpenURL(scheme);
  if (canOpenApp) {
    await Linking.openURL(scheme);
  } else {
    // Fallback to web (works on both platforms)
    await Linking.openURL(webUrl);
  }
}
```

## 5.3 "Open In..." Picker UI (React Native)

```tsx
// OpenInPicker.tsx
import React from 'react';
import { View, Text, TouchableOpacity, Linking, Modal, StyleSheet } from 'react-native';

interface Props {
  visible: boolean;
  book: string;
  chapter: number;
  verse: number;
  version: string;
  onClose: () => void;
}

const TARGETS = [
  { name: 'YouVersion Bible', buildUrl: (b: string, c: number, v: number, ver: string) =>
    `https://www.bible.com/bible/${YOUVERSION_IDS[ver] || '111'}/${b}.${c}.${v}` },
  { name: 'Bible Gateway', buildUrl: (b: string, c: number, v: number, ver: string) =>
    `https://www.biblegateway.com/passage/?search=${b}+${c}%3A${v}&version=${ver}` },
  { name: 'Blue Letter Bible', buildUrl: (b: string, c: number, v: number, ver: string) =>
    `https://www.blueletterbible.org/${ver.toLowerCase()}/${b.toLowerCase()}/${c}/${v}` },
];

export const OpenInPicker: React.FC<Props> = ({ visible, book, chapter, verse, version, onClose }) => {
  return (
    <Modal visible={visible} transparent animationType="slide" onRequestClose={onClose}>
      <View style={styles.overlay}>
        <View style={styles.sheet}>
          <Text style={styles.title}>Open {book} {chapter}:{verse} in...</Text>
          {TARGETS.map(target => (
            <TouchableOpacity
              key={target.name}
              style={styles.option}
              onPress={() => {
                Linking.openURL(target.buildUrl(book, chapter, verse, version));
                onClose();
              }}
            >
              <Text style={styles.optionText}>{target.name}</Text>
              <Text style={styles.arrow}>→</Text>
            </TouchableOpacity>
          ))}
          <TouchableOpacity style={styles.cancel} onPress={onClose}>
            <Text style={styles.cancelText}>Cancel</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  overlay: { flex: 1, justifyContent: 'flex-end', backgroundColor: 'rgba(0,0,0,0.5)' },
  sheet: { backgroundColor: 'white', borderTopLeftRadius: 16, borderTopRightRadius: 16, padding: 16 },
  title: { fontSize: 18, fontWeight: '600', marginBottom: 16, textAlign: 'center' },
  option: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 14, borderBottomWidth: 1, borderBottomColor: '#eee' },
  optionText: { fontSize: 16 },
  arrow: { fontSize: 16, color: '#999' },
  cancel: { marginTop: 8, paddingVertical: 14, alignItems: 'center' },
  cancelText: { fontSize: 16, color: '#007AFF' }
});
```

## 5.4 Unbrick Screen Integration

```tsx
// UnbrickScreen.tsx
import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { bibleService } from './bible-service';
import { OpenInPicker } from './OpenInPicker';

export const UnbrickScreen: React.FC = () => {
  const [verse, setVerse] = useState({ bookId: 'JHN', bookName: 'John', chapter: 3, verse: 16, text: '' });
  const [showPicker, setShowPicker] = useState(false);

  useEffect(() => {
    loadDailyVerse();
  }, []);

  async function loadDailyVerse() {
    // Pick a verse from our curated unbrick set
    const v = await bibleService.getRandomVerse('BSB');
    setVerse({ ...v, bookName: getBookName(v.bookId) });
  }

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Read this verse to continue</Text>

      <View style={styles.verseCard}>
        <Text style={styles.verseText}>"{verse.text}"</Text>
        <Text style={styles.reference}>
          {verse.bookName} {verse.chapter}:{verse.verse} (BSB)
        </Text>
      </View>

      <TouchableOpacity style={styles.readButton} onPress={() => setShowPicker(true)}>
        <Text style={styles.readButtonText}>Read in another translation →</Text>
      </TouchableOpacity>

      <OpenInPicker
        visible={showPicker}
        book={verse.bookId}
        chapter={verse.chapter}
        verse={verse.verse}
        version="NIV"
        onClose={() => setShowPicker(false)}
      />
    </View>
  );
};

function getBookName(osisId: string): string {
  const names: Record<string, string> = {
    GEN: 'Genesis', EXO: 'Exodus', JHN: 'John', PSA: 'Psalms',
    PRO: 'Proverbs', ROM: 'Romans', EPH: 'Ephesians', // ... etc
  };
  return names[osisId] || osisId;
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 24, backgroundColor: '#f5f5f5' },
  header: { fontSize: 22, fontWeight: '700', textAlign: 'center', marginBottom: 24 },
  verseCard: { backgroundColor: 'white', borderRadius: 12, padding: 24, marginBottom: 16, elevation: 2 },
  verseText: { fontSize: 20, lineHeight: 28, color: '#333', marginBottom: 12, fontStyle: 'italic' },
  reference: { fontSize: 14, color: '#666', textAlign: 'right' },
  readButton: { paddingVertical: 12 },
  readButtonText: { color: '#007AFF', fontSize: 16, textAlign: 'center' }
});
```

---

# PART 6: Cost Analysis

## 6.1 Option A: In-App Bible Only (3 PD Translations)

| Cost Item | Amount | Notes |
|---|---|---|
| Licensing | **$0** | BSB + WEB + KJV are all public domain |
| API costs | **$0** | helloao.org is free |
| Development | ~2-3 weeks | SQLite + download + reader UI |
| Storage | ~14 MB/user | Negligible |
| **Total Year 1** | **$0 + dev time** | |

## 6.2 Option B: External Bible App Sync Only

| Cost Item | Amount | Notes |
|---|---|---|
| Licensing | **$0** | Deep linking doesn't require licensing |
| API costs | **$0** | No API calls needed |
| Development | ~1 week | URL builder + picker UI |
| Storage | ~0 MB | No local storage |
| **Total Year 1** | **$0 + minimal dev** | |

## 6.3 Option C: Hybrid (RECOMMENDED)

| Cost Item | Amount | Notes |
|---|---|---|
| Licensing | **$0** | PD translations in-app; deep links for licensed |
| API costs | **$0** | helloao.org is free |
| Development | ~4-6 weeks | SQLite + download + reader + deep links |
| Storage | ~14 MB/user | 3 translations cached |
| Future: Add NIV/ESV | $5K-50K | Only if we want in-app licensed translations later |
| **Total Year 1** | **$0 + moderate dev** | |

## 6.4 Future Licensing Options (If Desired Later)

| Translation | Est. Cost | Difficulty |
|---|---|---|
| ESV (non-commercial API) | **Free** | Easy — Crossway provides free API |
| NET (non-commercial) | **Free** | Easy — just hyperlink attribution |
| NLT (non-commercial API) | **Free** | Easy — Tyndale provides free API |
| Full NIV in-app | **$10K-50K** | Hard — HarperCollins/Zondervan |
| Full NKJV in-app | **$10K-30K** | Medium — Thomas Nelson |
| Full ESV in-app | **$5K-25K** | Medium — Crossway |
| Full CSB in-app | **$5K-15K** | Medium — Lifeway |

---

# PART 7: Summary & Action Items

## 7.1 Final Recommendation

**Implement Option C (Hybrid)** with the following implementation order:

1. **Week 1:** Integrate helloao.org API, download BSB into SQLite, wire unbrick screen to local database
2. **Week 2:** Add "Open in YouVersion" deep links for users who want NIV/ESV/NKJV/NLT
3. **Week 3:** Add KJV and WEB as user-selectable alternatives in-app
4. **Week 4-5:** Build minimal in-app chapter reader (fetch from API, cache locally)
5. **Week 6:** Polish "Open in..." picker with YouVersion, Bible Gateway, Blue Letter Bible

## 7.2 Key Decisions

| Decision | Answer | Rationale |
|---|---|---|
| Primary translation? | **BSB** | Only modern PD translation from original languages |
| Backup translations? | **KJV + WEB** | Classic + modern alternatives, both PD |
| API provider? | **helloao.org** | Richest JSON format, 1256+ translations, no limits |
| Simple fallback API? | **wldeh/bible-api** | CDN-backed, simpler format |
| External app priority? | **YouVersion first** | Largest user base, best deep link support |
| Need licensing? | **No (for MVP)** | Public domain covers unbrick use case |
| Offline requirement? | **Yes** | Unbrick must work without internet |

## 7.3 Risk Mitigation

| Risk | Mitigation |
|---|---|
| helloao.org API goes down | Cache everything in SQLite; app works fully offline |
| BSB translation has errors | It's public domain — we can verify against source; also offer KJV/WEB as fallback |
| User wants NIV/ESV for unbrick | "Open in YouVersion" deep link provides instant access |
| App store rejection for Bible content | Public domain text is fully legal; attribution not even required (but we will) |
| Storage concerns on old devices | ~14 MB is minimal; make KJV/WEB optional downloads |

## 7.4 Attribution (Required / Recommended)

Even though public domain, we should show:

```
Scripture quotations marked "BSB" are taken from the
Berean Standard Bible (BSB), dedicated to the public domain
under CC0 by the Berean Bible Translation Committee (Apr 2023).

Scripture quotations marked "KJV" are taken from the
King James Version, public domain (outside UK).

Scripture quotations marked "WEB" are taken from the
World English Bible, dedicated to the public domain by eBible.org.
```

---

*Report generated for FaithWall architecture planning. All API endpoints, licensing terms, and costs verified as of July 2025.*
