---
paths:
  - "01_Todos/**"
---

# Task Management Rules

When working with todo files, follow the task management SOP:

**Source of truth:** `01_Todos/tasks.md` - THE task file, all tasks, all themes.

**Task format:**
```
- [ ] #theme Task description [due-date] @waiting(Person) @context(Location) !impact(H|M|L) !effort(H|M|L) [[link|Label]]
```

**Required:** `#theme` tag + task description. Everything else is optional.

**Generated files (read-only, don't edit manually):**
- `daily-plan.md` - AI-generated via `/morning`
- `waiting.md` - AI-generated waiting items view

**Capture file:** `capture.md` - Mobile append target. Process with `/transform`.

**Archive:** `archive/YYYY-MM.md` - Completed tasks by month.

**Sections in tasks.md:** In Progress / Next Up / Waiting / Someday. Each section has theme headings.

<!-- CUSTOMISE: Replace with YOUR theme tags matching 02_Themes/ folders -->
**Theme tags:** `#project-a #project-b #personal #system`

<!-- CUSTOMISE: Define YOUR context locations -->
**@context locations:**
- **Home** - Can only do at home
- **Office** - Can only do at the office
- **Transit** - Good for commute - doesn't need other resources
- Unmarked = can do anywhere

**Leverage scoring:**

| Impact | Effort | Leverage | Priority |
|--------|--------|----------|----------|
| H | L | **Highest** | Do these first |
| H | M | High | Strong candidate |
| M | L | High | Quick wins |
| H | H | Medium | Important but heavy |
| M | M | Medium | Standard |
| L | L | Low | If time permits |
| M | H | Low | Defer or delegate |
| L | M/H | **Lowest** | Question if needed |

When not tagged, assume Medium/Medium (neutral leverage). High-leverage tasks can bump up even without due dates.

**Design principles:**
1. Single source of truth - Tasks in `tasks.md` only, not in theme status.md
2. Capture fast, route later - No metadata at capture, Claude handles routing
3. Generated views - daily-plan.md and waiting.md are AI outputs, not manually edited
4. Plain text - No databases or plugins
