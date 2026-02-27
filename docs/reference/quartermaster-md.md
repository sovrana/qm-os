# CLAUDE.md Template

## What It Is

The `CLAUDE.md` file is the single most important file in the Quartermaster system. It's the instruction set Claude reads at the start of every conversation. Everything else - skills, memory, theme files - builds on top of what CLAUDE.md establishes.

Think of it as the constitution. Skills are legislation. Theme `claude.md` files are local bylaws. Rules files are specialised regulations that activate when needed. The hierarchy matters.

## Why It Matters

Without CLAUDE.md, Claude starts every session as a blank slate. With it, Claude knows who you are, how you work, what your blind spots are, how you communicate with different stakeholders, and what rules to follow. The difference between a useful assistant and a generic chatbot lives in this file.

## Architecture: Main File + Rules Files

The system splits instructions across two layers:

**Main CLAUDE.md (~300 lines)** holds identity, methodology, and always-on rules. Things Claude needs in every conversation regardless of what you're working on.

**`.claude/rules/` files** hold domain-specific rules that load on demand. Some activate conditionally based on file paths. Others load in all sessions but keep the main file focused.

```
CLAUDE.md              <- Always loaded. Identity, style, core methodology.
.claude/rules/
  session-defaults.md  <- Always loaded. Session-type behaviours.
  external-input.md    <- Always loaded. AI synthesis, competitive analysis.
  system-operations.md <- Always loaded. Search, PDF, document creation.
  framework-dev.md     <- Always loaded. Framework development, problem-solving.
  todos.md             <- Conditional: loads when working in 01_Todos/**
  inbox.md             <- Conditional: loads when working in 00_Inbox/**
  example-theme.md     <- Conditional: loads when working in 02_Themes/example-theme/**
```

This split keeps the main file readable while letting the system grow. As you add themes, each gets its own rules file without bloating CLAUDE.md.

## Key Sections (Main File)

| Section | What It Controls |
|---------|-----------------|
| **Who I Am** | Name, role, positioning. Calibrates tone. |
| **Active Projects** | Your 2-5 work domains and how they relate. Helps Claude understand trade-offs. |
| **How I Work** | Working preferences. "Always plan before acting." |
| **Operating Style** | Signature moves, communication calibration per audience, known blind spots, stakeholder adjustments. |
| **Vault Folder Structure** | Where files go. Prevents Claude from dumping files in root. |
| **Working with Claude Code** | Git behaviour, iteration discipline, proactive behaviours, auto-changelog, calibration logging. |
| **Extended Rules** | Pointer to `.claude/rules/` files and what each contains. |
| **Vibe** | Personality. "Have opinions. One sentence if one sentence works." |
| **Anti-Slop Rules** | Banned words, phrases, structures. Hard constraints on output. |

## Key Sections (Rules Files)

| File | What It Controls |
|------|-----------------|
| `session-defaults.md` | Financial sessions, legal documents, retrospectives, negotiation routing. Behaviour presets per session type. |
| `external-input.md` | How to process external AI output, competitive analysis, importing AI conversations. |
| `system-operations.md` | Vault search strategy, PDF handling, document creation, tool-specific operations. |
| `framework-dev.md` | Framework development process, problem-solving patterns (political architecture, pre-mortem, stage-gating). |
| `todos.md` | Task format, leverage scoring, theme tags, context locations. Activates in `01_Todos/`. |
| `inbox.md` | Inbox processing flow, file naming, transcript handling. Activates in `00_Inbox/`. |

## Customisation Points

The template includes `<!-- CUSTOMISE: -->` comments at every point where you should insert your own content. Key ones:

- **Who I Am** - Your identity and positioning
- **Active Projects** - Your work domains and cross-domain dynamics
- **Known Blind Spots** - Your actual blind spots (the more specific, the more useful the blind spot check becomes)
- **Stakeholder Adjustments** - Your key audience types and what works with each
- **Theme tags** (in `todos.md`) - Your `#theme` tags matching your `02_Themes/` folders
- **Context locations** (in `todos.md`) - Your `@context()` values (Home, Office, Transit, etc.)
- **Session type defaults** (in `session-defaults.md`) - Add your recurring session types
- **Framework catalogue** (in `framework-dev.md`) - Replace with your own frameworks

## How It Evolves

CLAUDE.md is a living document. Three mechanisms keep it current:

**The "Save This" Loop.** When you explain a preference during work, Claude asks: "Should I save this rule to CLAUDE.md?" Over time, every correction becomes a permanent instruction. Rules route to the appropriate level - main file, theme-level, or rules file.

**Graduated promotion from calibration log.** The system logs every rejection and correction to `calibration-log.md`. When the same pattern appears 3+ times, it graduates to a formal rule. The calibration log is staging. CLAUDE.md and rules files are production.

**Weekly review.** The `/weekly` skill's Beads system tracks improvement suggestions. Recurring friction (3+ occurrences) surfaces as candidates for rule updates.

## Scope Hierarchy

Rules can live at four levels:

| Level | File | Scope |
|-------|------|-------|
| **Global** | Root `CLAUDE.md` | Every conversation, every theme |
| **Domain rules** | `.claude/rules/[domain].md` (no `paths:`) | Every conversation, specific domain |
| **Path rules** | `.claude/rules/[name].md` (with `paths:`) | Only when working with matching files |
| **Theme** | `02_Themes/[theme]/claude.md` | Only when working in that theme |

Put identity, operating style, and universal methodology in global. Put session behaviours, search strategy, and framework processes in domain rules. Put task management and inbox processing in path-scoped rules. Put stakeholder context and political sensitivity in theme-level files.
