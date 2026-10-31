#!/usr/bin/env bash
# Install the humanizer skill for Claude Code.
#   ./install.sh            -> personal: ~/.claude/skills/humanizer (all projects)
#   ./install.sh --project  -> this project only: ./.claude/skills/humanizer
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/humanizer"
if [[ "${1:-}" == "--project" ]]; then
  DEST="$PWD/.claude/humanizer"
else
  DEST="$HOME/.claude/humanizer"
fi
mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
echo "Installed humanizer skill to $DEST"
echo "Start a new Claude Code session; check with /skills or ask: 'humanize this paragraph'."
