---
name: changelog
description: View or manually log iteration decisions for a document. Usually runs automatically - only invoke this to inspect history or add a manual entry.
argument-hint: [file-path] [reason?]
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Changelog

**Note:** Changelog is automatic. Claude logs significant structural decisions during iteration without being asked. This skill is for *inspecting* history or *manually logging* a decision outside of an active iteration.

Track the "why" behind document iterations. Git tracks what changed; this tracks the reasoning. Prevents re-litigating settled decisions in round 47 of a 100-round iteration.

**Examples:**
- `/changelog 02_Themes/project-c/context/platform-one-pager.md` - Show iteration history for this file
- `/changelog 02_Themes/project-c/context/platform-one-pager.md "Removed budget table - stakeholder wants narrative flow"` - Log a decision
- `/changelog` - Show all active changelogs

---

## How It Works

Each tracked document gets a companion changelog file:
- Document: `02_Themes/project-c/context/platform-one-pager.md`
- Changelog: `02_Themes/project-c/context/.changelog/platform-one-pager.md`

The changelog directory uses a dot-prefix (`.changelog/`) to stay out of vault navigation while remaining searchable.

---

## Process

### When called with a file + reason (`/changelog [file] "reason"`)

1. **Identify the document** from the file path
2. **Get current git state** - run `git log --oneline -1 [file]` and `git diff --stat HEAD [file]`
3. **Create/append to changelog:**

```markdown
## [Date] - Round [N]

**Changed:** [Brief what - from git diff summary or user's description]
**Why:** [The reason provided]
**Decided:** [Any decisions this change locks in]
**Rejected:** [Any alternatives this change rules out, if relevant]
```

4. **Auto-increment round number** from previous entries

### When called with just a file (`/changelog [file]`)

1. **Read the changelog** if it exists
2. **Show iteration history** - all rounds with decisions
3. **Highlight locked decisions** - things that were explicitly decided and shouldn't be re-opened without good reason
4. **Show git diff since last logged round** - anything changed since the last changelog entry

### When called with no args (`/changelog`)

1. **Scan for all .changelog directories** across the vault
2. **List active documents** being tracked with last round number and date
3. **Flag stale changelogs** - documents modified since last log entry

---

## Output Format (Changelog File)

```markdown
# Changelog: [Document Name]
*Tracking iteration decisions for: `[relative path]`*

---

## 2026-02-21 - Round 1

**Changed:** Initial structure - executive summary, budget table, timeline
**Why:** Monday session needs a single page the team lead can walk the CEO through
**Decided:** One-pager format, not slide deck. Subsidiary structure framing.
**Rejected:** Detailed business case (too early, save for follow-up)

---

## 2026-02-21 - Round 2

**Changed:** Removed budget table, added narrative cost paragraph
**Why:** Stakeholder feedback - wants narrative flow, not spreadsheet feel
**Decided:** Cost as "[AMOUNT]/yr for team of 8" prose, not line items
**Rejected:** Itemised budget breakdown at this stage

---

## 2026-02-22 - Round 5

**Changed:** Added operational autonomy clause language
**Why:** Critical for tech lead buy-in. Weekend discussion confirmed this matters.
**Decided:** "Operational autonomy" framing with defined guardrails
**Rejected:** Standard portfolio company governance model
```

---

## Auto-Logging

When iterating on a document (20+ rounds), Claude should:

1. **Proactively suggest logging** after significant structural changes (not wordsmithing)
2. **Ask "What's the reason?"** if the user makes a change without explaining why
3. **Flag when a change contradicts a previous decision** - "Round 3 decided X, but this change reverses it. Intentional?"

Triggers for auto-suggest:
- Removing a section entirely
- Changing the document's structure (not just content)
- Reversing a previously logged decision
- Adding a new stakeholder-facing section

Don't log:
- Typo fixes
- Word choice tweaks
- Formatting changes
- Intermediate drafts that get replaced in the same session

---

## Rules

- **Changelog lives next to the document.** Same directory, `.changelog/` subfolder.
- **Never delete changelog entries.** They're history. If a decision was wrong, add a new entry explaining the reversal.
- **Round numbers are cumulative across sessions.** Don't reset to Round 1 in a new conversation.
- **"Decided" and "Rejected" are the valuable fields.** "Changed" is just context. The decision record is what prevents re-litigation.
- **Keep entries short.** 2-4 lines per field max. This is a log, not a narrative.
- **Git integration is supplementary.** The changelog is the source of truth for reasoning. Git is the source of truth for content.
