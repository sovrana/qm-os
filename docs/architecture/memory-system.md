# Six-File Memory System

## What

Six markdown files that persist across Claude Code conversations. They live in Claude Code's auto-memory directory and are loaded at the start of every session. Together, they give Claude Code a working memory that survives session boundaries.

## Why

Claude Code conversations are ephemeral. Close the terminal and everything is gone - decisions, context, preferences, all of it. The vault stores content, but content isn't memory. Memory is knowing that the CEO prefers outcomes over methodology, that a specific framing was rejected last Tuesday, that two themes are connected in a non-obvious way.

Six files, not one, because different types of memory have different update cadences and different consumers. Voice exemplars change rarely. Calibration patterns change every session. Cramming both into a single file makes neither easy to maintain.

## How

### The Six Files

| File | Purpose | Update Cadence |
|---|---|---|
| `MEMORY.md` | Live strategic state, architecture notes, key people | Every few sessions |
| `voice-exemplars.md` | Real writing samples for tone calibration | Monthly |
| `calibration-log.md` | Rejection/approval patterns from sessions | Every session (append-only) |
| `connections.md` | Cross-theme links with evidence and dates | When discovered |
| `stakeholder-live.md` | Dynamic posture of key people | Weekly (via `/weekly`) |
| `recent-decisions.md` | Decisions from last 2 weeks | Weekly (regenerated) |

### MEMORY.md

The primary memory file. Contains:

- **Live Strategic State** - Where each work theme stands right now. Updated every few sessions.
- **Architecture Notes** - Key system design decisions (e.g., how search works, where scripts run).
- **Key People** - Locked-in facts about important individuals. Prevents re-asking.

Capped at ~200 lines. When it grows beyond that, older entries graduate to theme-specific files or get archived.

### calibration-log.md

The most distinctive file. Every time a preference is expressed ("don't use that framing", "too formal", "wrong audience"), it's logged here. Format:

```
**[Category | REJECTED]** What was tried -> What replaced it
Why: Stated reason
```

This file is append-only and compounds over time. It's the primary mechanism for institutional memory transfer.

### The Graduation Pattern

When the same rejection pattern appears 3+ times in the calibration log, it graduates to a formal rule in CLAUDE.md. The log is staging. CLAUDE.md is production.

This means the system's operating rules aren't designed upfront - they're discovered through use and promoted when validated. Calibration log (observed) to CLAUDE.md (codified) to default behaviour (automatic).

### connections.md

Captures non-obvious links between themes. Format includes: title, which themes it bridges, the claim, the evidence, and a verification date. Only current, specific connections qualify. Generic patterns ("success in A helps B") don't.

## Key Insight

Memory files are cheaper than forgetting. A five-line entry in `calibration-log.md` saves 10 minutes of re-explaining a preference. Over 8 weeks, the calibration log accumulated dozens of entries, each one preventing a future mistake.

## Customisation Points

- **Add memory files** for new concerns (e.g., `technical-debt.md` for engineering teams)
- **Adjust MEMORY.md cap** based on your context window budget
- **Change stakeholder refresh cadence** from weekly to daily for fast-moving environments
- **Customise calibration categories** to match your domain's decision types
