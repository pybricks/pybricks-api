#!/usr/bin/env bash
# Build all release artifacts locally (equivalent to CI workflows, minus publish).
set -euo pipefail

REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"

# Activate the project venv so python/make/etc. all use it without poetry run
source "$REPO_ROOT/.venv/bin/activate"

# Read version from pyproject.toml
VERSION=$(grep '^version = ' "$REPO_ROOT/pyproject.toml" | head -1 | sed 's/version = "\(.*\)"/\1/')
# Convert Python pre-release format (e.g. 4.0.0a1, 4.0.0b1, 4.0.0rc1) to npm semver (e.g. 4.0.0-alpha.1, 4.0.0-beta.1, 4.0.0-rc.1)
NPM_VERSION=$(echo "$VERSION" | sed 's/\([0-9]\)a\([0-9]\)/\1-alpha.\2/;s/\([0-9]\)b\([0-9]\)/\1-beta.\2/;s/\([0-9]\)rc\([0-9]\)/\1-rc.\2/')
echo "==> Building version $VERSION (npm: $NPM_VERSION)"

# lint
echo "==> Linting"
cd "$REPO_ROOT"
flake8
doc8

# pybricks-jedi tests
echo "==> Testing pybricks-jedi"
cd "$REPO_ROOT/jedi"
poetry run pytest -vv

# @pybricks/jedi npm package
echo "==> Building @pybricks/jedi"
cd "$REPO_ROOT/jedi"
python3 build.py "$NPM_VERSION"

# @pybricks/ide-docs npm package
echo "==> Building @pybricks/ide-docs"
cd "$REPO_ROOT"
make -C doc clean
cd "$REPO_ROOT/npm/ide-docs"
yarn build

echo ""
echo "Build complete."
echo "  jedi npm package : jedi/npm-build/"
echo "  ide-docs         : npm/ide-docs/html/"
