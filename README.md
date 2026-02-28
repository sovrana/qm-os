# Quartermaster (QM)

An AI operating system that gets smarter every time you use it.

## Five things nothing else does

1. **It gets smarter every time you use it** - Corrections auto-graduate into permanent rules. The system rewrites its own instructions based on your behaviour.
2. **It knows your context before you explain it** - Six-file memory, session-type pre-flights, stakeholder-adapted output. You never repeat yourself.
3. **It writes like you, not like AI** - Voice-matched against your real writing samples. 40+ banned AI-slop words and structures.
4. **It makes your knowledge searchable** - Three-mode search across everything you've ever written. Concepts, keywords, and exact patterns.
5. **It publishes itself safely** - Build with real data. The privacy pipeline sanitises everything before it touches GitHub.

Built over 8 weeks of daily production use. 7 published skills. Not a proof of concept.

## Quick Start

```bash
# Clone the template
git clone https://github.com/sovrana/qm-os.git
cp -r qm-os/template/ ~/my-vault/

# Set up semantic search
cd qm-os/qm-search
python3 -m venv qm-search-env
source qm-search-env/bin/activate
pip install -r requirements.txt
QM_VAULT_PATH=~/my-vault python index_vault.py

# Configure Claude Code
# 1. Copy template/.claude/ into your vault
# 2. Wire up the MCP server in your Claude Code settings
# 3. Customise CLAUDE.md with your identity and blind spots
# 4. Run /morning
```

See the [full quickstart guide](https://sovrana.github.io/qm-os/quickstart/) for details.

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

Full documentation at [sovrana.github.io/qm-os](https://sovrana.github.io/qm-os)

## License

MIT
