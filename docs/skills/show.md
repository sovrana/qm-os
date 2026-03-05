# /show - Filtered Task Views

| | |
|---|---|
| **Runtime** | ~30 seconds |
| **Reads** | `tasks.md`, theme status files, stakeholder context |
| **Writes** | Filtered view to stdout (read-only) |
| **Model** | Claude Code |

## What It Does

Shows filtered views of your tasks by theme, person, or waiting status. One command to answer "what's open on this project?", "what do I need to discuss with this person?", or "what's stuck waiting on someone?"

## How It Works

### Four View Modes

**Theme view** - `/show [theme]`

Everything open on a project: tasks grouped by section (In Progress, Next Up, Waiting, Someday), strategic context, waiting item ages, and an AI recommendation for what to tackle next.

**Person view** - `/show @[person]`

Agenda builder for your next conversation with someone: items to discuss, follow-ups they owe you (with ages), recent context from meeting notes, and suggested talking points.

**Waiting view** - `/show waiting`

All blocked items across every theme, sorted by age. Auto-escalation logic:

| Age | Action |
|-----|--------|
| < 3 days | Watch |
| 3-7 days | Monitor, consider nudge |
| > 7 days | Auto-draft follow-up |
| > 14 days | Critical: auto-create escalation task |

**Summary view** - `/show` (no args)

Quick dashboard: total open tasks by theme, items due today/this week, critical waiting items, in-progress items, and a suggestion for which theme needs attention.

## Why It Matters

Task lists grow. Without filtered views, you either review everything (slow) or miss things (dangerous). `/show` gives you the slice you need in the moment:

- Before a meeting: `/show @person`
- Starting a work block: `/show theme`
- End of day: `/show waiting`

All views are read-only. Edit `tasks.md` to make changes.

## Related

- [/morning](morning.md) - Uses show-style filtering internally for daily planning
- [/inbox](inbox.md) - Upstream: routes tasks that show displays
- [/evening](evening.md) - Uses show data for end-of-day reflection
- [Skills System](../architecture/skills-system.md) - How skills compose with each other
