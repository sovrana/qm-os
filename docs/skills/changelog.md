# /changelog - Decision Tracking

| | |
|---|---|
| **Runtime** | ~1 minute (or automatic during iteration) |
| **Reads** | Target document, `git log`, `git diff` |
| **Writes** | `.changelog/[filename].md` companion file |
| **Model** | Sonnet |

## What It Does

Tracks the reasoning behind document iterations. Creates a companion file that records what changed, why, what was decided, and what was rejected at each significant round. Usually runs automatically during iteration - you rarely need to invoke it manually.

## Why It Matters

Git tracks what changed. Changelog tracks **why**.

When you're on round 47 of a 100-round document iteration, you need to know why the budget table was removed in round 12. Without that record, you either re-litigate settled decisions or accidentally reintroduce something that was deliberately killed.

The changelog prevents both. It's a decision log, not a diff.

## How It Works

Each tracked document gets a companion changelog in a dot-prefixed subdirectory:

```
02_Themes/unity/context/platform-one-pager.md          ← the document
02_Themes/unity/context/.changelog/platform-one-pager.md ← its decision log
```

The `.changelog/` directory stays out of vault navigation while remaining searchable.

### Automatic Mode (default)

During document iteration, Claude logs entries automatically when:

- A section is removed or added entirely
- The document's structure changes (not just wording)
- A previously logged decision gets reversed
- You explain a reason for a change ("remove the budget table because...")

Claude does **not** log typo fixes, word choice tweaks, or formatting changes.

### Manual Invocation

Three forms:

| Command | What It Does |
|---------|-------------|
| `/changelog [file] "reason"` | Log a specific decision with your stated reason |
| `/changelog [file]` | Show the full iteration history and highlight locked decisions |
| `/changelog` | List all active changelogs across the vault, flag stale ones |

## The Key Innovation

**Contradiction detection.** When a new change reverses a previously logged decision, the system flags it immediately: "This reverses the Round 3 decision to remove the budget table. Intentional?"

This is where changelogs earn their keep. In long iterations, it's easy to circle back to something you already tried and rejected. The changelog catches this pattern and forces a conscious decision rather than accidental regression.

The two most valuable fields are **Decided** and **Rejected**. "Changed" is context. The decision record is the load-bearing structure. Every entry captures not just what you chose, but what you eliminated - and that elimination is a permanent constraint for the document unless explicitly reversed.

```markdown
## 2026-02-21 - Round 2

**Changed:** Removed budget table, added narrative cost paragraph
**Why:** Stakeholder wants narrative flow, not spreadsheet feel
**Decided:** Cost as "£2M/yr for team of 8" prose, not line items
**Rejected:** Itemised budget breakdown at this stage
```

Round numbers increment across sessions. Round 1 in Monday's conversation and Round 1 in Tuesday's conversation would be Rounds 1 and 2, not both Round 1.

## Example Usage

Log a decision during iteration:

```
/changelog 02_Themes/unity/context/one-pager.md "Removed competitive analysis - premature before Monday"
```

Review iteration history:

```
/changelog 02_Themes/unity/context/one-pager.md
```

List all tracked documents:

```
/changelog
```

## Customisation Guide

- **Auto-logging sensitivity** - By default, only structural changes trigger logging. If you want finer-grained tracking, note this in the document's theme `claude.md`.
- **Git integration** - The skill checks `git log` and `git diff` when logging to correlate changelog entries with commits. This is supplementary - the changelog is the source of truth for reasoning, git for content.
- **Stale detection** - When you run `/changelog` with no arguments, it flags documents that have been modified since their last changelog entry. Useful for catching iterations that happened without logging.
