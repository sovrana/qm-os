# System Overview

!!! abstract "TL;DR"
    Seven layers turn a markdown vault into a persistent AI assistant: **vault** (files) + **skills** (workflows) + **hooks** (automation) + **daemon** (always-on) + **memory** (persistence) + **search** (retrieval) + **self-improvement** (learning). Each layer works independently. Together they compound.

## What

Quartermaster (QM) is an agentic operating system for Claude Code. It turns a markdown vault into a persistent, self-improving assistant that remembers context, automates workflows, and gets smarter every week.

The metaphor: a quartermaster manages logistics, navigation, and records so the commander focuses on decisions. QM does the same for knowledge workers - it handles filing, retrieval, prioritisation, and routine processing so you focus on judgement calls.

```mermaid
graph TB
    subgraph Interface["Interface Layer"]
        Mobile["Mobile Capture<br/>(Obsidian/Telegram)"]
        CC["Claude Code<br/>(Deep Work)"]
    end

    subgraph Daemon["Always-On Layer"]
        OC["OpenClaw Daemon<br/>(Heartbeat + Telegram Bot)"]
    end

    subgraph Vault["Vault Layer"]
        Inbox["00_Inbox/"]
        Todos["01_Todos/tasks.md"]
        Themes["02_Themes/"]
        Ref["03_Reference/"]
        Sys["99_System/"]
    end

    subgraph Skills["Skills Layer (15 skills)"]
        Morning["/morning"]
        Challenge["/challenge"]
        StressTest["/stress-test"]
        Weekly["/weekly"]
        Transform["/transform"]
        Brief["/brief"]
        Draft["/draft"]
        More["+ 8 more"]
    end

    subgraph Hooks["Hooks Layer"]
        Start["session-start<br/>(context load)"]
        Stop["session-stop<br/>(auto-commit)"]
        PostWrite["post-write<br/>(reindex)"]
    end

    subgraph Memory["Memory Layer"]
        MEM["MEMORY.md"]
        Voice["voice-exemplars.md"]
        Cal["calibration-log.md"]
        Conn["connections.md"]
        Stake["stakeholder-live.md"]
        Rec["recent-decisions.md"]
    end

    subgraph Search["Search Layer"]
        Semantic["Semantic<br/>(MCP Server)"]
        BM25["BM25<br/>(Keyword)"]
        Grep["Grep<br/>(Exact)"]
    end

    CC --> Skills
    Skills --> Vault
    Skills --> Memory
    Skills --> Search
    Hooks --> Vault
    Hooks --> Search
    Mobile --> Inbox
    Mobile --> OC
    OC --> Vault
    OC --> Mobile
    Memory --> CC
```

## Why

Claude Code is powerful but stateless. Every conversation starts from zero. QM solves this by wrapping Claude Code in a persistent architecture: memory files survive between sessions, hooks automate context loading and cleanup, skills encode repeatable workflows as SOPs, and search makes the entire vault queryable.

## How

Seven layers, each independent but reinforcing:

1. **Interface** - Mobile capture (Obsidian, Telegram) for quick input. Claude Code for deep work sessions.
2. **Always-On Daemon** - A Telegram bot on a second machine. Hourly heartbeat processes inbox, flags waiting items, sends morning plans and evening summaries.
3. **Vault** - Five numbered folders. Plain markdown. Obsidian-compatible. The single source of truth.
4. **Skills** - Fifteen published SKILL.md files. Each encodes a workflow as a standard operating procedure Claude Code executes on command.
5. **Hooks** - Three automation points. Context loads on session start, changes commit on session stop, search reindexes after every file write.
6. **Memory** - Six files that persist across conversations. Strategic state, voice calibration, rejection patterns, cross-theme connections.
7. **Search** - Three modes (semantic, keyword, exact) queried in parallel for research tasks.

## Key Insight

The system's value compounds. Every session generates calibration data, improvement suggestions, and cross-theme connections. These feed back into the operating rules. After 2+ months of use, the CLAUDE.md instruction file contains dozens of rules that were discovered through use, not designed upfront.

## Customisation Points

- **Add themes** by creating folders in `02_Themes/` with a `claude.md` file
- **Add skills** by writing a SKILL.md file in `.claude/skills/`
- **Adjust memory** by editing which files auto-load via MEMORY.md
- **Swap search models** by changing the sentence-transformer model in the indexer
- **Modify hooks** by editing shell scripts in `.claude/hooks/`

## Deep Dives

Each layer has its own page with implementation details and customisation guides:

- [Folder Structure](folder-structure.md) - The numbered-prefix pattern and theme layout
- [Skills System](skills-system.md) - SKILL.md format and the gather-analyse-synthesise pattern
- [Three-Hook Automation](hooks.md) - Context load, auto-commit, and reindex wiring
- [Always-On Daemon](always-on.md) - OpenClaw, Telegram, and the two-machine architecture
- [Six-File Memory](memory-system.md) - Persistent memory across sessions
- [Three-Mode Search](search.md) - Semantic, BM25, and exact match in parallel
- [Self-Improvement Loop](self-improvement.md) - BEADs, calibration log, and the graduation pattern
