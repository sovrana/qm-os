# Task Format + Leverage Scoring

## The Task Line

Every task follows a single format in `01_Todos/tasks.md`:

```markdown
- [ ] #theme Task description 📅 YYYY-MM-DD @waiting(Name) !impact(H) !effort(L) [[path|Label]]
```

Only two fields are required. Everything else is optional metadata that skills use to prioritise, filter, and route.

## Field Reference

| Field | Required | Example | Purpose |
|-------|----------|---------|---------|
| `- [ ]` | Yes | `- [ ]` / `- [x]` | Completion state |
| `#theme` | Yes | `#project-a` | Routes to theme. Must match a `02_Themes/` folder name. |
| Description | Yes | `Draft board update` | What to do |
| `📅 YYYY-MM-DD` | No | `📅 2026-03-01` | Due date (Obsidian Tasks format) |
| `@waiting(Name)` | No | `@waiting(Alex)` | Blocked by this person |
| `➕ YYYY-MM-DD` | No | `➕ 2026-02-15` | When waiting started. Used to calculate age. |
| `@agenda(Name)` | No | `@agenda(Jordan)` | Discuss with this person. `/brief` and `/show @Name` surface these. |
| `@context()` | No | `@context(Home)` | Location constraint. Unmarked = can do anywhere. |
| `!impact(H\|M\|L)` | No | `!impact(H)` | Strategic importance |
| `!effort(H\|M\|L)` | No | `!effort(L)` | Time/complexity |
| `[[path\|Label]]` | No | `[[context/spec\|Details]]` | Link to related vault files |

## Context Tags

Location-aware filtering for tasks that can only happen in specific places:

- **Home** - Only at home (repairs, personal projects)
- **Office** - Only at the office (in-person meetings, equipment access)
- **Transit** - Good for commute (calls, reading, light emails)
- Unmarked - Can do anywhere

Add your own contexts to match your patterns. `/morning` uses these to filter the daily plan.

## Leverage Scoring

Leverage = Impact / Effort. The matrix:

| Impact | Effort | Leverage | What `/morning` Does |
|--------|--------|----------|---------------------|
| H | L | **Highest** | Bumps to P1 even without due date |
| H | M | High | Strong candidate for today |
| M | L | High | Surfaces as quick wins |
| H | H | Medium | Important but heavy - schedule deliberately |
| M | M | Medium | Standard priority |
| L | L | Low | If time permits |
| M | H | Low | Defer or delegate |
| L | M/H | **Lowest** | Flagged: "Question if this is needed" |

Untagged tasks default to Medium/Medium (neutral leverage). The scoring is additive to due dates, not a replacement. A task due today still takes priority regardless of leverage score.

## Single Source of Truth

Tasks live in `tasks.md` only. Not in theme `status.md` files. Not in meeting notes. Not in capture files.

- `status.md` tracks strategic context (Now/Next/Blockers/Decisions) but never duplicates task lists
- `capture.md` is a temporary inbox - tasks get routed to `tasks.md` during `/inbox` processing
- `daily-plan.md` and `waiting.md` are generated views, not manually edited
- Completed tasks archive to `01_Todos/archive/YYYY-MM.md` during `/weekly`

One file. One format. Everything else reads from it.
