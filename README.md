# Quartermaster (QM)

An agentic operating system for Claude Code. Built for executives and serious builders who want AI agents handling coordination so they can focus on judgment.

## What This Is

QM is a complete system architecture for running your professional life through Claude Code. It includes:

- **16 skills** (7 published) that orchestrate complex workflows through parallel AI subagents
- **Three-hook automation** that loads context on session start, commits on session end, and reindexes on every write
- **A six-file persistent memory system** that builds institutional knowledge across conversations
- **Local semantic search** over your markdown vault, exposed as an MCP tool
- **A self-improvement feedback loop** that extracts patterns from every session and graduates them into system rules

Built over 8 weeks of daily production use. Not a proof of concept.

## Quick Start

```bash
# Clone the template
git clone https://github.com/marclien/qm-os.git
cp -r qm-os/template/ ~/my-vault/

# Set up semantic search
cd qm-os/brain-search
python3 -m venv brain-search-env
source brain-search-env/bin/activate
pip install -r requirements.txt
QM_VAULT_PATH=~/my-vault python index_vault.py

# Configure Claude Code
# 1. Copy template/.claude/ into your vault
# 2. Wire up the MCP server in your Claude Code settings
# 3. Customise CLAUDE.md with your identity and blind spots
# 4. Run /morning
```

See the [full quickstart guide](https://marclien.github.io/qm-os/quickstart/) for details.

## Architecture

```
You --- Claude Code --- Skills (SKILL.md SOPs)
              |              |
              |         Task subagents (parallel)
              |
         Hooks --- session-start (context load)
              |    session-stop (auto-commit)
              |    post-write (reindex)
              |
         Memory --- MEMORY.md (live state)
              |     voice-exemplars.md
              |     calibration-log.md
              |     connections.md
              |     stakeholder-live.md
              |     recent-decisions.md
              |
         Search --- Semantic (MCP server)
                    BM25 (keyword)
                    Grep (exact match)
```

## Published Skills

| Skill | What It Does |
|-------|-------------|
| `/morning` | Generates prioritised daily plan with leverage scoring |
| `/challenge` | Red-teams any document through 5 parallel analysis lenses |
| `/weekly` | Orchestrates 7 parallel subagents for system maintenance |
| `/transform` | Processes external content into your vault |
| `/brief` | Fast pre-meeting one-pager with stakeholder calibration |
| `/changelog` | Tracks the "why" behind document iterations |
| `/draft` | Voice-calibrated content creation (LinkedIn, emails, memos) |

## Documentation

Full documentation at [marclien.github.io/qm-os](https://marclien.github.io/qm-os)

## License

MIT
