# Rules System

## What `.claude/rules/` Files Are

The `.claude/rules/` directory holds rule files that extend your CLAUDE.md without cluttering it. There are two types:

**Domain rules** load in every conversation. They hold instructions for specific domains of work (financial sessions, framework development, search strategy) that would bloat the main file but need to be available whenever those topics come up.

**Path-scoped rules** activate automatically based on file paths. When Claude works with files matching a rule's glob pattern, those rules load alongside everything else. This gives you targeted instructions for specific areas of your vault.

## How Path-Scoped Rules Work

Each path-scoped rule file uses YAML frontmatter with glob patterns to define its scope:

```yaml
---
paths:
  - "02_Themes/project-alpha/**"
---
```

When Claude reads, writes, or edits any file matching `02_Themes/project-alpha/**`, the rules in this file activate automatically.

### Example: Theme Rule

```markdown
---
paths:
  - "02_Themes/project-alpha/**"
---

# Project Alpha Context

**What this is:** AI transformation platform for professional services.

**Key people:** Alex (CEO), Jamie (Operations), Sam (Finance).

**Writing style:** Direct, outcome-focused. Alex responds to quantified impact.

**Sensitivity:** Board discussions are confidential. Don't reference in documents shared beyond Alex.

**Key refs:** Read `status.md` for current stage, `people.md` for guidelines.
```

### Example: Task Management Rule

```markdown
---
paths:
  - "01_Todos/**"
---

# Task Management Rules

**Source of truth:** `01_Todos/tasks.md` - THE task file, all tasks, all themes.

**Task format:**
- [ ] #theme Task description [due-date] @waiting(Person) !impact(H|M|L)

**Theme tags:** `#project-a #project-b #personal #system`
```

## How Domain Rules Work

Domain rules have no `paths:` frontmatter. They load in every session but keep the main CLAUDE.md focused on identity and methodology. The template includes four:

| File | Domain | Purpose |
|------|--------|---------|
| `session-defaults.md` | Session behaviours | Financial, legal, retrospective session presets |
| `external-input.md` | External content | AI synthesis, competitive analysis, conversation imports |
| `system-operations.md` | System tools | Search strategy, PDF handling, document creation |
| `framework-dev.md` | Intellectual IP | Framework development, problem-solving patterns |

### When to Use Domain Rules vs Main File

Put it in CLAUDE.md if it's identity, personality, or methodology Claude needs in every response. Put it in a domain rule if it's a detailed SOP for a specific type of work. The test: "Does Claude need this when responding to a casual question?" If no, it's a domain rule.

## When to Use Which Level

| Level | Location | Activates When | Best For |
|-------|----------|---------------|----------|
| **Global** | Root `CLAUDE.md` | Every conversation | Working style, blind spots, anti-slop rules, vibe |
| **Domain rules** | `.claude/rules/[domain].md` | Every conversation | Session behaviours, search strategy, framework processes |
| **Path rules** | `.claude/rules/[name].md` | Files match the `paths:` pattern | Task format, inbox processing, theme context |
| **Theme** | `02_Themes/[name]/claude.md` | Working in that theme directory | Stakeholder preferences, political context, sensitivity |

**Global** holds your identity, operating patterns, and universal constraints. Things that never change based on what you're working on.

**Domain rules** hold detailed SOPs that would bloat the main file. They're always available but organised by topic rather than all in one place.

**Path rules** handle anything that depends on file location. They're especially useful for task management rules that only matter when editing tasks, or inbox processing rules that only matter when processing new items.

**Theme-level** holds context that matters only when you're in that domain. Who the stakeholders are, how they prefer communication, what topics are sensitive, what terminology to use.

## Creating New Rules

**Adding a theme rule:**
1. Create `.claude/rules/[theme-name].md`
2. Add `paths:` frontmatter pointing to the theme folder
3. Document key people, writing style, sensitivity, cross-theme links

**Adding a domain rule:**
1. Create `.claude/rules/[domain-name].md`
2. No frontmatter needed (loads in every session)
3. Document the SOP, defaults, or patterns for that domain

**Promoting from calibration log:**
When the same correction appears 3+ times in `calibration-log.md`, it's ready to become a permanent rule. Decide which level it belongs at (global, domain, path, or theme) and add it there.

## How Rules Compound Over Time

Rules aren't static. Three mechanisms add new rules organically:

**The "Save This" loop.** When you state a preference during work ("always lead with numbers for this stakeholder"), Claude asks whether to save it. If yes, it routes to the appropriate level.

**Calibration log graduation.** Every correction gets logged in `calibration-log.md`. When the same correction appears 3+ times, it promotes to a permanent rule. The log is staging. Rules files are production.

**Weekly Beads review.** The `/weekly` skill tracks improvement suggestions. Recurring friction becomes a BEAD, which becomes a rule candidate.

Over months, your rule set becomes a detailed operating manual that captures decisions you only had to make once.
