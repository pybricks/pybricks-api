#!/usr/bin/env bash
# Build all release artifacts locally (equivalent to CI workflows, minus publish).
set -euo pipefail

REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"

# Activate the project venv so python/make/etc. all use it without poetry run
source "$REPO_ROOT/.venv/bin/activate"

# Read version from pyproject.toml
VERSION=$(grep '^version = ' "$REPO_ROOT/pyproject.toml" | head -1 | sed 's/version = "\(.*\)"/\1/')
echo "==> Building version $VERSION"

# lint
echo "==> Linting"
cd "$REPO_ROOT"
flake8
doc8

# pybricks-jedi wheel (from local source)
echo "==> Testing pybricks-jedi"
cd "$REPO_ROOT/jedi"
poetry run pytest -vv

echo "==> Building pybricks-jedi wheel"
cd "$REPO_ROOT/jedi"
rm -rf dist/
poetry build --format=wheel

# @pybricks/jedi npm package
echo "==> Building @pybricks/jedi"
cd "$REPO_ROOT"
python3 npm/jedi/build.py "$VERSION"

# @pybricks/ide-docs npm package
echo "==> Building @pybricks/ide-docs"
cd "$REPO_ROOT"
make -C doc clean
cd "$REPO_ROOT/npm/ide-docs"
yarn build

echo ""
echo "Build complete."
echo "  jedi npm package : npm/jedi/build/"
echo "  ide-docs         : npm/ide-docs/html/"
