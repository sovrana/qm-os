---
name: weekly
description: Weekly system maintenance and cleanup. Run Sunday evening or Monday morning (30 min).
argument-hint: [random]
allowed-tools: Read, Write, Edit, Bash, Glob, Task, AskUserQuestion
model: sonnet
---

# Review

Weekly cleanup and maintenance workflow. Archive completed tasks, surface stale items, audit waiting items.

**Usage:**
- `/weekly` - Full weekly review
- `/weekly random` - Surface random note for exploration

---

## Full Review Mode

### Process:

1. **Archive completed tasks** (sequential - modifies tasks.md):
   - Read `01_Todos/tasks.md`
   - Find all `- [x]` completed tasks
   - Group by theme and month
   - Move to `01_Todos/archive/YYYY-MM.md`
   - Remove from tasks.md

2. **Parallel analysis** (launch ALL five as Task subagents simultaneously):

   Use `Task` tool with `subagent_type: "Explore"` for each. Launch all five in a single message.

   **Subagent A - Stale tasks:**
   > Read `01_Todos/tasks.md`. Find tasks in "Next Up" or "In Progress" with no due date and no recent activity. Return the list with suggested action (archive/someday/keep).

   **Subagent B - Waiting items audit:**
   > Read `01_Todos/tasks.md`. Find all @waiting() items. Calculate ages from ➕ dates. Flag items >14 days for escalation. Return grouped by urgency: Critical >14d, Moderate 7-14d, Recent <7d.

   **Subagent C - Theme health check:**
   > Read `01_Todos/tasks.md`. Count open tasks by #theme tag. Flag themes with >15 open tasks (overload) or 0 tasks (inactive). Return as table.

   **Subagent D - Emergent themes & connections:**
   > 1. Read `connections.md` from the auto-memory directory. For each Active entry, check whether referenced evidence files still support the claim. If valid, update `Last verified` date. If claim is stale (>21 days unverified) or superseded by recent decisions, move to `## Stale (Review Required)`. Auto-remove Stale entries >42 days old.
   > 2. Scan `recent-decisions.md` (auto-memory directory) and files in `02_Themes/*/meetings/` from the past 2 weeks. Identify cross-theme patterns: concepts, people, or decisions in one theme that affect another. Add new discoveries to `## Proposed` section of `connections.md` (user promotes to Active during review).
   > 3. Existing behaviour: flag recurring patterns across 3+ meetings that don't yet have their own reference doc. Suggest: create standalone doc in `03_Reference/` or theme `context/`?
   > Return: connections updated (N active, M proposed, K removed), plus emergent theme suggestions.

   **Subagent E - Beads (self-improvement):**
   > Read `99_System/improvement-suggestions.md`. Find suggestions with 3+ occurrences (marked **BEAD**). Return for implementation decision. Flag stale suggestions (>30 days since last seen, count < 3) for cleanup.

3. **Relationship heatmap** (sequential - runs script):
   - Run `~/bin/relationship-heatmap --quiet` to refresh `01_Todos/relationships.md`
   - Read `01_Todos/relationships.md` and include OVERDUE and DUE SOON items in the summary report

4. **Cleanup captures** (sequential - modifies capture.md):
   - Check `01_Todos/capture.md` for [PROCESSED] entries
   - Archive old processed captures (>30 days)

5. **Regenerate memory digests** (launch TWO as Task subagents simultaneously):

   **Subagent F - Recent decisions digest:**
   > Read all conversation-discovery files from the last 2 weeks: `99_System/logs/conversation-discoveries/`. For each file, extract the key decision or insight in 1 line. Group by theme. Write to `recent-decisions.md` in the auto-memory directory. Include source log paths. Update the "Last updated" date and period.

   **Subagent G - Live state refresh:**
   > Read theme `people.md` files and `01_Todos/tasks.md` @waiting() items. For key stakeholders <!-- CUSTOMISE: your key stakeholders -->, update current posture and last significant touch in `stakeholder-live.md` (auto-memory directory). Also update the "Live Strategic State" section in `MEMORY.md` (same directory) with current theme status from each `02_Themes/*/status.md`. Preserve all other MEMORY.md content unchanged.

6. **Generate summary report** - consolidate all subagent results into output format below

### Output Format:

```markdown
# Weekly Review - Week of [Date]

## Completed This Week ([N] tasks)
[Tasks grouped by theme]

## Stale Items Requiring Decision ([N])
[Items >14 days with no activity, with options: keep/someday/delete]

## Waiting Items Requiring Follow-Up ([N])
[Grouped by urgency: Critical >7d, Moderate 3-7d, Recent <3d]

## Theme Health Check
| Theme | Open Tasks | Status | Notes |

## Relationship Heatmap
[OVERDUE and DUE SOON stakeholders from relationships.md]

## Emergent Themes
[Concepts appearing across 3+ meetings that may need their own doc]

## Cross-Theme Connections
- Active: [N] | Proposed: [M] | Removed this week: [K]
- **New proposals:** [list titles for review]

## Beads (Self-Improvement)
[Suggestions with 3+ occurrences ready for implementation]

## Memory Digests Refreshed
- recent-decisions.md: [N] decisions from [date range]
- stakeholder-live.md: [N] stakeholders updated
- MEMORY.md live state: [themes updated]

## Actions Before Next Review
[Checklist of follow-ups]

## Reflection Prompts
1. What are you proud of this week?
2. What patterns of blocking keep recurring?
3. Which tasks drained you? Which energised you?
4. Is the task system helping or hindering?
```

---

## Random Exploration Mode (`/weekly random`)

Surface a random note from the vault for review and connection-making.

### Process:

1. Select random note (exclude `.obsidian/`, `.git/`, `node_modules/`)
2. Read and present the note (title, date, first ~50 lines)
3. Prompt for reflection: Still relevant? Connections? Needs updating?
4. Take action: Link / Update / Archive / Extract insight / Skip
5. Offer to continue with another random note

---

## Notes:

- Stale item threshold: 14 days with no activity
- Waiting item escalation: >14 days gets flagged
- Theme overload threshold: >15 open tasks
- Don't delete tasks automatically - always ask user first
- Emergent themes: concepts mentioned 3+ times across different meetings
- Beads: suggestions with 3+ occurrences are ready to implement
