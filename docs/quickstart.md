# Quickstart

Get QM running in 30 minutes. By the end you'll have a working vault with semantic search, three-hook automation, and your first AI-generated daily plan.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- Python 3.10+ (for semantic search)
- Git

## 1. Clone the Template

```bash
git clone https://github.com/sovrana/qm-os.git
cp -r qm-os/template/ ~/my-vault/
cd ~/my-vault/
```

This gives you the full folder structure, all 7 skill files, hooks, rules, and a starter CLAUDE.md.

## 2. Set Up Semantic Search

```bash
cd qm-os/brain-search
python3 -m venv brain-search-env
source brain-search-env/bin/activate
pip install -r requirements.txt
```

Index your vault:

```bash
QM_VAULT_PATH=~/my-vault python index_vault.py
```

First run downloads the embedding model (~90MB). Subsequent runs take ~15 seconds.

## 3. Configure the MCP Server

Add the semantic search server to your Claude Code settings. In `~/.claude/settings.json` (or your project's `.claude/settings.json`):

```json
{
  "mcpServers": {
    "qm-search": {
      "command": "/path/to/brain-search/brain-search-env/bin/python",
      "args": ["/path/to/brain-search/mcp_server.py"],
      "env": {
        "QM_VAULT_PATH": "/path/to/my-vault"
      }
    }
  }
}
```

Replace the paths with your actual locations.

## 4. Wire Up Hooks

The template includes three hook scripts in `.claude/hooks/`. The template `settings.json` already references them. Verify the paths are correct for your vault location.

| Hook | Trigger | What It Does |
|------|---------|-------------|
| `session-start.sh` | Conversation starts | Loads dashboard: overdue tasks, waiting items, theme status |
| `session-stop.sh` | Conversation ends | Auto-commits changes to git |
| `post-write-reindex.sh` | Any .md file written | Refreshes search index |

Make the scripts executable:

```bash
chmod +x .claude/hooks/*.sh
```

## 5. Customise Your CLAUDE.md

Open `CLAUDE.md` in your editor and search for `CUSTOMISE`. There are ~20 marked sections. Priority order:

1. **Who I Am** - Your name and role. Claude uses this to calibrate every response.
2. **Known Blind Spots** - Be specific. "I tend to over-architect" is more useful than "I have blind spots."
3. **Active Projects** - Your 2-5 work domains and how they connect.
4. **Theme tags** (in `.claude/rules/todos.md`) - Match your `02_Themes/` folder names.
5. **Stakeholder Adjustments** - Your key audiences and what lands with each.

Everything else can wait. The system works with just these five.

## 6. Set Up Your First Theme

```bash
mkdir -p 02_Themes/my-project/{meetings,context,emails,processed}
```

Create `02_Themes/my-project/claude.md`:

```markdown
# My Project

**What this is:** Brief description.

**Key people:** Names and roles.

**Current status:** Where things stand.
```

Create a matching rule in `.claude/rules/my-project.md`:

```markdown
---
paths:
  - "02_Themes/my-project/**"
---

# My Project Context

Key context Claude needs when working in this theme.
```

## 7. Add Some Tasks

Open `01_Todos/tasks.md` and add a few real tasks:

```markdown
## In Progress

### my-project
- [ ] #my-project Draft project proposal !impact(H) !effort(M)
- [ ] #my-project Review competitor analysis !impact(M) !effort(L)

### personal
- [ ] #personal Schedule dentist appointment !impact(L) !effort(L)
```

## 8. Run Your First /morning

Open Claude Code in your vault directory and type:

```
/morning
```

Claude reads your tasks, applies leverage scoring (Impact / Effort), checks MEMORY.md for strategic context, and generates a prioritised daily plan in `01_Todos/daily-plan.md`.

If this works, the system is live.

## What to Do Next

**This week:**

- Process a few items through `/inbox` to build the pattern
- Try `/challenge` on a document before sharing it externally
- Let the calibration log start capturing your corrections

**This month:**

- Create `voice-exemplars.md` with 3-5 real writing samples (your best emails, memos, posts)
- Run `/weekly` for the first time - it audits the whole system
- Watch CLAUDE.md grow as rules get promoted from the calibration log

**Ongoing:**

- The system gets smarter every week. Corrections become rules. Rules become habits. After a month, Claude knows your preferences better than most human assistants.

## Troubleshooting

**Semantic search not returning results:**
Run the indexer again: `QM_VAULT_PATH=~/my-vault python index_vault.py`. Check that your vault has some `.md` files with content.

**Hooks not firing:**
Verify the scripts are executable (`chmod +x`). Check that `settings.json` has the correct paths. Run `cat .claude/hooks/session-start.sh` to verify the vault path variable.

**Skills not found:**
Skills must be in `.claude/skills/[name]/SKILL.md`. Check the directory structure matches exactly.
