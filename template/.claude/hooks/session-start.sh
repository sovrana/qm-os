#!/bin/bash
# QM Session Start Hook
# Auto-loads context at the start of each Claude Code session

VAULT_DIR="$CLAUDE_PROJECT_DIR"
TODAY=$(date '+%Y-%m-%d')
DAY_NAME=$(date '+%A')

echo "## QM Session - $DAY_NAME, $(date '+%B %d, %Y')"
echo ""

# Folder structure (quick orientation)
echo "### Vault Structure"
echo "00_Inbox/  01_Todos/  02_Themes/  03_Reference/  99_System/"
echo "Themes: $(ls "$VAULT_DIR/02_Themes" 2>/dev/null | tr '\n' ' ')"
echo ""

# Active themes (by recent modification)
echo "### Active Themes (by recent activity)"
ls -lt "$VAULT_DIR/02_Themes/" 2>/dev/null | head -6
echo ""

# Tasks due today or overdue (dynamic date comparison)
echo "### Due Today/Overdue"
if [ -f "$VAULT_DIR/01_Todos/tasks.md" ]; then
    OVERDUE=0
    SHOWN=0
    while IFS= read -r line; do
        task_date=$(echo "$line" | grep -oE '📅 [0-9]{4}-[0-9]{2}-[0-9]{2}' | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')
        if [ -n "$task_date" ] && [[ "$task_date" <= "$TODAY" ]]; then
            if [ $SHOWN -lt 5 ]; then
                echo "$line"
                SHOWN=$((SHOWN + 1))
            fi
            if [[ "$task_date" < "$TODAY" ]]; then
                OVERDUE=$((OVERDUE + 1))
            fi
        fi
    done < <(grep -E "^\- \[ \].*📅" "$VAULT_DIR/01_Todos/tasks.md" 2>/dev/null)
    echo "_${OVERDUE} potentially overdue_"
fi
echo ""

# High leverage tasks
echo "### High Leverage (!impact(H) !effort(L))"
if [ -f "$VAULT_DIR/01_Todos/tasks.md" ]; then
    grep -E "!impact\(H\).*!effort\(L\)|!effort\(L\).*!impact\(H\)" "$VAULT_DIR/01_Todos/tasks.md" 2>/dev/null | grep "^\- \[ \]" | head -3
fi
echo ""

# Waiting items
echo "### Waiting Items"
if [ -f "$VAULT_DIR/01_Todos/tasks.md" ]; then
    grep -E "@waiting\(" "$VAULT_DIR/01_Todos/tasks.md" 2>/dev/null | grep "^\- \[ \]" | head -5
fi
echo ""

# Inbox count
echo "### Inbox"
INBOX_COUNT=$(find "$VAULT_DIR/00_Inbox" -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
CAPTURE_COUNT=$(grep -c "^- " "$VAULT_DIR/01_Todos/capture.md" 2>/dev/null || echo "0")
echo "- Inbox files: $INBOX_COUNT"
echo "- Unprocessed captures: $CAPTURE_COUNT"
echo ""

echo "---"
echo "_/morning for daily plan | /challenge for critical review | /weekly for maintenance_"

exit 0
