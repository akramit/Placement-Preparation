#!/usr/bin/env bash
set -euo pipefail

PORT=8080
DOCS_DIR="/workspace/docs"

if command -v ss >/dev/null 2>&1 && ss -tln | grep -q ":${PORT} "; then
  echo "Docs server already listening on port ${PORT}"
  exit 0
fi

exec python3 -m http.server "${PORT}" --directory "${DOCS_DIR}" --bind 0.0.0.0
