#!/usr/bin/env bash
set -e
REPO_ROOT=$(git rev-parse --show-toplevel)
HOOK="$REPO_ROOT/.git/hooks/commit-msg"
cat > "$HOOK" <<'EOF'
#!/bin/sh
exec qcn lint "$1"
EOF
chmod +x "$HOOK"
echo "Installed commit-msg hook at $HOOK"