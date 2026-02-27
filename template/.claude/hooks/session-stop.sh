#!/bin/bash
# QM Session Stop Hook
# Auto-commits changes at the end of each Claude Code session

VAULT_DIR="$CLAUDE_PROJECT_DIR"
cd "$VAULT_DIR" || exit 0

# Check if there are changes to commit
if git diff --quiet HEAD 2>/dev/null && git diff --cached --quiet 2>/dev/null; then
    # Check for untracked files in key directories
    UNTRACKED=$(git ls-files --others --exclude-standard 2>/dev/null | head -1)
    if [ -z "$UNTRACKED" ]; then
        exit 0  # Nothing to commit
    fi
fi

# Count changed files by theme
CHANGED_THEMES=$(git diff --name-only HEAD 2>/dev/null | grep "02_Themes/" | sed 's|02_Themes/\([^/]*\)/.*|\1|' | sort -u | tr '\n' ', ' | sed 's/,$//')
CHANGED_COUNT=$(git diff --name-only HEAD 2>/dev/null | wc -l | tr -d ' ')

# Build commit message
if [ -n "$CHANGED_THEMES" ]; then
    MSG="Session checkpoint: $CHANGED_THEMES ($CHANGED_COUNT files, $(date '+%Y-%m-%d %H:%M'))"
else
    MSG="Session checkpoint: $CHANGED_COUNT files ($(date '+%Y-%m-%d %H:%M'))"
fi

# Stage and commit
git add -A 2>/dev/null
git commit -m "$MSG" 2>/dev/null

exit 0
