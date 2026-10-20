#!/bin/bash
# build the site and publish _site to the gh-pages branch.
# uses a separate worktree so untracked files on main never end up on gh-pages.
set -e
cd "$(dirname "$0")"

bundle exec jekyll build

PAGES_DIR=$(mktemp -d)
git fetch origin gh-pages
git worktree add "$PAGES_DIR" gh-pages
trap 'git worktree remove --force "$PAGES_DIR"' EXIT

git -C "$PAGES_DIR" pull --ff-only origin gh-pages
rsync -a _site/ "$PAGES_DIR"/
git -C "$PAGES_DIR" add -A
git -C "$PAGES_DIR" commit -m 'update site' || echo "nothing changed"
git -C "$PAGES_DIR" push origin gh-pages
