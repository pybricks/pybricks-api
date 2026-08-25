#!/usr/bin/env bash
# Build all release artifacts locally (equivalent to CI workflows, minus publish).
set -euo pipefail

REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"

# Option: --pybricks-code <path> copies built npm packages into that
# checkout's node_modules/@pybricks/ for easy local testing.
PYBRICKS_CODE=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --pybricks-code)
            PYBRICKS_CODE="$(realpath "$2")"
            shift 2
            ;;
        *)
            echo "usage: $0 [--pybricks-code <path-to-pybricks-code-checkout>]" >&2
            exit 1
            ;;
    esac
done
if [[ -n "$PYBRICKS_CODE" && ! -d "$PYBRICKS_CODE/node_modules/@pybricks" ]]; then
    echo "error: $PYBRICKS_CODE/node_modules/@pybricks not found (run yarn install there first)" >&2
    exit 1
fi

# Activate the project venv so python/make/etc. all use it without poetry run
source "$REPO_ROOT/.venv/bin/activate"

# Read version from pyproject.toml
VERSION=$(grep '^version = ' "$REPO_ROOT/pyproject.toml" | head -1 | sed 's/version = "\(.*\)"/\1/')
# Convert Python pre-release format (e.g. 4.0.0a1, 4.0.0b1, 4.0.0rc1) to npm semver (e.g. 4.0.0-alpha.1, 4.0.0-beta.1, 4.0.0-rc.1)
NPM_VERSION=$(echo "$VERSION" | sed 's/\([0-9]\)a\([0-9]\)/\1-alpha.\2/;s/\([0-9]\)b\([0-9]\)/\1-beta.\2/;s/\([0-9]\)rc\([0-9]\)/\1-rc.\2/')
echo "==> Building version $VERSION (npm: $NPM_VERSION)"

# lint (same as CI build.yml)
echo "==> Linting"
cd "$REPO_ROOT"
ruff check
ruff format --check
doc8

# Python package
echo "==> Building Python package"
rm -rf "$REPO_ROOT/dist"  # stale wheels would get globbed into the jedi npm package
poetry build

# pybricks-jedi tests (own poetry env, same as CI jedi.yml)
echo "==> Testing pybricks-jedi"
cd "$REPO_ROOT/jedi"
poetry run pytest -vv

# @pybricks/jedi npm package
echo "==> Building @pybricks/jedi"
cd "$REPO_ROOT/jedi"
rm -rf dist  # build.py globs dist/*.whl, stale wheels would get shipped
python3 build.py "$NPM_VERSION"

# html docs for Read the Docs
echo "==> Building Read the Docs html docs"
cd "$REPO_ROOT"
make -C doc clean html

# @pybricks/ide-docs npm package (builds the TAG=ide docs)
echo "==> Building @pybricks/ide-docs"
make -C doc clean
cd "$REPO_ROOT/npm/ide-docs"
yarn build

echo ""
echo "Build complete."
echo "  python package   : dist/"
echo "  jedi npm package : jedi/npm-build/"
echo "  ide-docs         : npm/ide-docs/html/"

if [[ -n "$PYBRICKS_CODE" ]]; then
    DEST="$PYBRICKS_CODE/node_modules/@pybricks"
    echo "==> Copying packages to $DEST"
    rm -rf "$DEST/jedi" "$DEST/ide-docs"
    mkdir -p "$DEST/jedi" "$DEST/ide-docs"
    cp -r "$REPO_ROOT/jedi/npm-build/." "$DEST/jedi/"
    cp -r "$REPO_ROOT/npm/ide-docs/package.json" \
        "$REPO_ROOT/npm/ide-docs/LICENSE" \
        "$REPO_ROOT/npm/ide-docs/README.md" \
        "$REPO_ROOT/npm/ide-docs/html" \
        "$DEST/ide-docs/"
    echo "Copied @pybricks/jedi and @pybricks/ide-docs. Restart the dev server to pick them up."
fi

