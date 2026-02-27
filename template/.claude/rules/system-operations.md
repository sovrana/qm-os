# System Operations

## Data Privacy
- **Training opt-out confirmed** - Opted out of Anthropic training on data (claude.ai settings)
- **Do not ask about this** - Setting is permanent, no need to confirm each session

## Document Creation
- **Use claude-office-skills** when asked to create DOCX, PPTX, XLSX, or PDF
- Skills location: `~/.claude/skills/claude-office-skills/`
- Auto-detect format from request, read the relevant SKILL.md, follow workflow
- Output to skill's `outputs/` folder, then copy to appropriate vault location

## Large PDF Handling
**Problem:** Claude Code's built-in Read tool has a ~12MB/25,000 token limit for PDFs. Hitting it triggers a persistent error that blocks all subsequent PDF reading.

**Default approach:** Use `/pdf [file]` command for any PDF that:
- Is larger than ~5MB (be conservative)
- Has more than ~50 pages
- Fails with "PDF too large" error

**Command options:**
- `/pdf [file]` - Auto-detect best approach
- `/pdf extract [file]` - Extract text to markdown
- `/pdf images [file]` - Convert to images for visual review
- `/pdf split [file]` - Split into smaller chunks

**Never:** Try to Read a large PDF directly and hit the error - it corrupts the session.

## Shopping and Product Research
For shopping tasks (materials, equipment, products), ask the user to paste product links rather than searching/navigating. They can find products faster; Claude adds value by comparing specs, checking compatibility, and building order lists.

<!-- CUSTOMISE: Add any system-specific operations below.
     Examples: remote machine access, bot operations,
     VM workarounds, tool-specific notes, mobile interface details. -->

## Vault Search Strategy

**Three search modes available:**

| Mode | Tool | Speed | Use Case |
|------|------|-------|----------|
| **Semantic** | Semantic search MCP or equivalent | ~1-2s | Conceptual queries, don't know exact words |
| **BM25 keyword** | Keyword search tool | ~0.2s | Keyword ranking without semantic drift |
| **Exact match** | Grep/Glob | ~instant | Exact strings, file paths, patterns |

**Semantic search** for conceptual queries:
- "What have we discussed about organisational resistance?"
- "Prior decisions on pricing strategy"
- "Similar situations to this budget issue"

**Keyword search** for ranked keyword results:
- "Find files about a specific company" (ranks by term frequency)
- When semantic search drifts too far from the topic
- Fast alternative when you know the keywords exist

**Grep/Glob** for specific lookups:
- Exact keywords, numbers, file names
- Known patterns: `02_Themes/*/meetings/*.md`
- Recent files by modification time

**When to use which:**
- Don't know exact words -> semantic search first
- Know keywords, want ranking -> keyword search
- Know exact string -> grep
- Looking for file paths -> glob

**Default: Use semantic + grep/glob for research queries.**
For any non-trivial vault search, run semantic AND grep/glob in parallel:
1. **Semantic** -> Finds conceptually related content (catches synonyms, related concepts)
2. **Grep/Glob** -> Catches exact matches semantic might miss (names, numbers, specific terms)
