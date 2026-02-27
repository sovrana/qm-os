---
name: morning
description: Generate daily plan with AI prioritization. Run every morning (5 min).
argument-hint:
allowed-tools: Read, Write, Bash, Glob
model: sonnet
---

# Morning Plan

Generate prioritised daily plan based on due dates, strategic context, and waiting items.

## Process:

1. **Gather context:**
   - Read `01_Todos/tasks.md` (all sections)
   - Read theme `status.md` files for strategic context:
     - `02_Themes/project-a/status.md`
     - `02_Themes/project-b/status.md`
     - `02_Themes/frameworks/status.md`
     - `02_Themes/project-c/status.md`
   - Read `connections.md` from the auto-memory directory
   - Get today's date

2. **Calculate priorities:**

   **P1 - Must Do Today:**
   - Tasks with 📅 today or overdue
   - Tasks blocking critical milestones (check theme status.md)
   - **High-leverage override:** Tasks with `!impact(H)` + `!effort(L)` bump to P1 even without due date

   **P2 - Follow-Up Urgently:**
   - Waiting items >7 days old (calculate from ➕ date)
   - Blockers that can be unblocked today
   - **High-impact waiting:** `!impact(H)` waiting items get flagged earlier (>5 days)

   **P3 - Should Do:**
   - Tasks 📅 this week
   - Next actions on hot themes (recently modified status.md or Now section active)
   - Tasks in "In Progress" section
   - **Leverage boost:** `!impact(H)` tasks without due date surface here (not P4)

   **P4 - If Time Permits:**
   - "Next Up" tasks with no due date
   - Quick wins (@context(errand) or simple tasks)
   - **Low-leverage flag:** `!impact(L)` + `!effort(H)` tasks get questioned - consider deferring

   **Leverage Scoring Reference:**
   - `!impact(H) !effort(L)` = Highest leverage - prioritise these
   - `!impact(H) !effort(M)` = High leverage
   - `!impact(M) !effort(L)` = Quick wins
   - `!impact(L) !effort(H)` = Low leverage - question if needed

3. **Write daily plan:**
   - Create/overwrite `01_Todos/daily-plan.md`
   - Include strategic context from theme files
   - Show waiting item ages and suggest follow-up actions
   - Link back to tasks.md for full details

## Output Format:

```markdown
# Daily Plan - Thursday, January 2, 2026

*Auto-generated from tasks.md and theme status files*

---

## Must Do Today (2)

1. **#project-a** Draft proposal for leadership review
   - **Due:** Jan 9 (7 days remaining)
   - **Context:** Management sessions Jan 9-10 are forcing function
   - **Blocker:** @waiting([TEAM_MEMBER_C]) for 9 days - needs nudge today
   - **Link:** [[02_Themes/project-a/projects/proposal/claude|Details]]

2. **#project-b** Finalise investment portfolio baseline with ExCo
   - **Due:** Jan 6 (4 days)
   - **Context:** OKR 1 deliverable, >75% spend needs tagging
   - **Strategic:** Board meeting prep underway

---

## Follow-Up Urgently (2)

### [TEAM_MEMBER_C] (project-a) - 9 days waiting
- Schedule alignment meeting on approach
- **Suggested action:** Email today referencing Jan 9 deadline
- **Draft:** "Hi [TEAM_MEMBER_C], circling back on our discussion - critical for Jan 9 session. 15min this week?"

### [CEO_NAME] (project-b) - 5 days waiting
- EBITDA milestone alignment (3 items)
- **Suggested action:** Bundle into single check-in request

---

## Should Do (4)

1. **#project-a** Define minimum foundational requirements
2. **#project-b** Wave 1 AI use cases selection
3. **#project-b** Quick wins identification
4. **#system** Process 1-2 recent transcripts

---

## If Time Permits (2)

- **#personal** Buy trousers @context(errand)
- **#personal** Home project @context(Home)

---

## Strategic Context Summary

[Theme summaries from status.md Now sections]

---

*Generated: [Timestamp]*
*Source: 01_Todos/tasks.md + theme status files*
```

## Notes:

- Daily plan is READ-ONLY - don't edit it manually
- Tasks are marked complete in `tasks.md` (source of truth)
- Rerun `/morning` anytime priorities shift
- Waiting item age calculation: today's date minus ➕ date
- Suggest email/Slack follow-up drafts for waiting items >7 days
- If no P1 items, emphasise P3 (don't leave day without direction)
- Weekend plans: lighter, focus on personal or strategic thinking
- **Cross-theme connections:** When writing P1-P3 tasks, check if the task's `#theme` tag appears in any Active connection in `connections.md`. If so, append a one-line `**Connection:**` summary inline with the task. Don't add a separate section - weave into the task entry.
