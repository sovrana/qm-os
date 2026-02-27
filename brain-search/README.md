# QM Semantic Search

Local semantic search over a markdown vault, exposed as an MCP tool for Claude Code. No external services, no ChromaDB - just sentence-transformers and numpy.

## How It Works

1. **Indexing:** Chunks markdown files by headings, generates embeddings with `all-MiniLM-L6-v2`, stores as numpy array
2. **Search:** Encodes query, computes cosine similarity against all chunks, returns top-N ranked results
3. **MCP Server:** Exposes `semantic_search` tool via JSON-RPC (stdin/stdout) for Claude Code

## Setup

```bash
# Create virtual environment
python3 -m venv brain-search-env
source brain-search-env/bin/activate

# Install dependencies
pip install -r brain-search/requirements.txt

# Set vault path
export QM_VAULT_PATH="/path/to/your/vault"

# Build the index (takes 2-4 minutes on first run)
python brain-search/index_vault.py

# Test a search
python brain-search/query.py "your search query" -n 5
```

## Claude Code Integration

Add to your Claude Code MCP settings (`.claude/settings.json` or global):

```json
{
  "mcpServers": {
    "qm-search": {
      "command": "/path/to/brain-search-env/bin/python",
      "args": ["/path/to/brain-search/mcp_server.py"],
      "env": {
        "QM_VAULT_PATH": "/path/to/your/vault"
      }
    }
  }
}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `QM_VAULT_PATH` | Current directory | Root path of your markdown vault |
| `QM_INDEX_PATH` | `$QM_VAULT_PATH/99_System/brain-search/vector-index` | Where to store/read the index |
| `QM_MODEL_NAME` | `all-MiniLM-L6-v2` | Sentence-transformer model name |

## Architecture

- **Chunking:** Heading-based (H1-H6), preserves heading hierarchy as context
- **Minimum chunk size:** 50 characters (skips tiny sections)
- **Maximum chunk size:** 2,000 characters (for embedding quality)
- **Theme extraction:** Files under `02_Themes/[name]/` get tagged with theme name
- **Embedding model:** 384 dimensions, ~60ms per query after first load
- **Storage:** Binary numpy (embeddings) + JSON (metadata with text snippets)

## Reindexing

Run `python brain-search/index_vault.py` after significant vault changes. Create a wrapper script for convenience:

```bash
#!/bin/bash
source /path/to/brain-search-env/bin/activate
python /path/to/brain-search/index_vault.py
```

Wire this into your session hooks for automatic reindexing.
