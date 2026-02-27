---
paths:
  - "00_Inbox/**"
---

# Inbox Processing Rules

When working with files in 00_Inbox/, follow the inbox processing SOP:

**Purpose:** New items land here for processing into the vault system.

**Transcripts:** Always create TWO files (raw + processed summary).

<!-- CUSTOMISE: Add any transcription tool quirks here.
     Example: "Tool X transcribes my name as Y - same person" -->

**Processing flow:**
1. Identify theme from content
2. Extract and process (see `/inbox` skill for full SOP)
3. Create processed files in `02_Themes/[theme]/`
4. Update theme status files if new information
5. Archive original

**File naming:** `YYYY-MM-DD_descriptive-title.md` (ISO 8601)

**Summary MUST link to raw transcript** in header metadata.

**Theme file structure:** Each theme should have `claude.md`, `status.md`, `strategic-context.md`, `key-metrics.md`, `people.md`, `meetings/`, `emails/`, `processed/`
