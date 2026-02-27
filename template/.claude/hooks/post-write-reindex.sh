#!/bin/bash
# QM Post-Write Reindex Hook
# Triggers search index refresh after files are written
# Wire this as a post-tool hook for Write/Edit operations

# Only reindex if a .md file was modified
FILE_PATH="${1:-}"
if [[ "$FILE_PATH" != *.md ]]; then
    exit 0
fi

# Refresh BM25 index silently in background (if qmd is available)
if command -v qmd &>/dev/null; then
    (qmd update >/dev/null 2>&1 &)
fi

# Note: Full semantic reindex is too slow for per-write triggers.
# Run `python brain-search/index_vault.py` manually or via session-start hook.

exit 0
