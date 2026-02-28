---
name: brief
description: Fast pre-meeting brief. Pulls context, tasks, history, open items into a one-pager.
argument-hint: [#theme|@person] [meeting-topic?]
allowed-tools: Read, Glob, Grep, Task, mcp__brain-search__semantic_search
model: sonnet
---

# Brief

Generate a fast, opinionated pre-meeting one-pager. NOT a deep research tool. This is a 2-minute context reload before walking into a room.

**Two modes:**

| Mode | Syntax | Output |
|------|--------|--------|
| **Self-brief** (default) | `/brief #theme person` | Context reload for you before a meeting |
| **Pre-brief** | `/brief #theme for:person` | What Person X needs to hear from you |

**Examples:**
- `/brief #project-c` - Project C context brief (all people, recent activity)
- `/brief @[TECH_LEAD]` - Everything relevant to a [TECH_LEAD] conversation
- `/brief #project-c [PORTFOLIO_CEO_A]` - Project C brief focused on [PORTFOLIO_CEO_A] session
- `/brief #project-b [CEO_NAME]` - Project B brief for a [CEO_NAME] catch-up
- `/brief #project-c for:[TECH_LEAD]` - What to tell [TECH_LEAD] about Project C (pre-brief mode)
- `/brief for:[DEAL_PARTNER] #project-c monday` - What [DEAL_PARTNER] needs before Monday session

---

## Process

### 1. Parse the input

- `#theme` → theme-focused brief (all people in that theme)
- `@person` → person-focused brief (across all themes)
- `#theme person` → intersection (most common use case)
- `for:person` → **pre-brief mode** (see below)
- No args → error, ask what the meeting is about

### 2. Gather context (parallel subagents)

Launch ALL four searches as parallel `Task` subagents (`subagent_type: "Explore"`) in a single message. Don't go deep, go wide.

**Subagent A - Tasks:**
> Read `01_Todos/tasks.md`. Find: (1) open tasks tagged with #[theme] or mentioning [person], (2) @waiting() items involving this person, (3) overdue items in this theme, (4) items with @agenda([Person]) tags. Return all matches with due dates and ages.

**Subagent B - Theme files & connections:**
> Read these files if they exist: `02_Themes/[theme]/status.md` (Now/Next/Blockers/Decisions), `02_Themes/[theme]/claude.md` (stakeholder preferences, political context), `02_Themes/[theme]/people.md` (person's role, concerns, communication style). Also read `connections.md` from the auto-memory directory and extract Active entries where the briefing theme or person appears. Return key content from each, including relevant cross-theme connections.

**Subagent C - Meeting notes (last 3 only):**
> Glob `02_Themes/[theme]/meetings/*.md`, take the 3 most recent by filename date. Read each and extract: decisions made, open questions, action items assigned to them or us. Return structured summary.

**Subagent D - Conversation discoveries (last 2 weeks):**
> Glob `99_System/logs/conversation-discoveries/*.md` for files from the last 2 weeks. Grep for theme or person name. Read matching files and extract relevant insights. Return summary.

### 3. Generate brief

Write directly to stdout (don't create a file). Speed matters.

---

## Output Format

```markdown
# Brief: [Theme] - [Person/Context]
*[Date] | Pre-meeting context*

## Their Open Items
- [What they owe us / what we're waiting on from them]
- Age of waiting items in days

## Our Open Items
- [What we owe them / committed deliverables]
- Due dates if any

## Last Meeting ([date])
- [2-3 key outcomes/decisions from most recent meeting]
- [Anything unresolved]

## Live Context
- [1-3 bullets from status.md Now section]
- [Any recent shifts or discoveries from logs]

## Suggested Agenda
1. [Most urgent open item]
2. [Decision needed]
3. [Status update they'll want]

## Watch For
- [Political sensitivities from claude.md/people.md]
- [Communication preferences for this person]
```

---

## Pre-Brief Mode (`for:person`)

When the input contains `for:person`, the output flips perspective. Instead of "what you need to know walking in," it's "what you should tell this person."

### What changes in pre-brief mode

**Additional context to gather:**
- `people.md` → this person's role, concerns, communication style (CRITICAL - calibrate tone)
- Their last known information state (from most recent meeting note involving them)
- What's changed since they last heard from you

**The key question:** What does this person currently believe, and what has shifted since they last engaged?

### Pre-Brief Output Format

```markdown
# Pre-Brief: [Person] on [Theme/Topic]
*[Date] | What they need to hear*

## Their Current State
- [What they currently believe / last knew]
- [When they last engaged with this topic]
- [Their known concerns or priorities]

## What's Changed Since
- [Key shifts they don't know about yet]
- [Decisions made without them in the room]
- [New information that affects their view]

## The Message
- [2-3 bullet core narrative: what you should convey]
- [Framing that lands with THIS person's priorities]

## What NOT to Say
- [Topics to avoid or defer]
- [Information that's premature or politically sensitive]

## Their Likely Questions
1. [Predict based on their role/concerns]
2. [What they'll push back on]
3. [What they'll want that isn't ready yet]
```

### Calibration Rules for Pre-Brief

- **Use people.md communication preferences.** If a person needs directness, the message is direct. If they need optionality, frame as options.
- **"What NOT to say" is mandatory.** This is where pre-briefs earn their value. Knowing what to hold back is as important as knowing what to share.
- **Predict questions.** Based on this person's pattern in meeting notes, what do they always ask? Surface those so you aren't caught flat-footed.

---

## Rules

- **Speed over depth.** If a search returns nothing in 2 seconds, move on. Don't dig.
- **Last 3 meetings only.** Don't read the entire meeting history.
- **No file creation.** Output goes to stdout. This is ephemeral.
- **Opinionated agenda.** Don't list everything - pick the 3 things that matter most.
- **Flag landmines.** If people.md or claude.md has warnings about this person's sensitivities, surface them in "Watch For".
- **Show waiting item ages.** Calculate days from ➕ date. Anything >7 days gets flagged.
- **Person search across themes.** When input is `@person`, search tasks.md for their name across ALL themes, not just one.
