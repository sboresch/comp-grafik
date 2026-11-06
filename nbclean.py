#!/usr/bin/env python3
"""
Git clean filter for Jupyter notebooks (.ipynb).

Strips volatile, kernel-generated content that Jupyter rewrites on its own
just from opening/running a notebook -- cell outputs, execution counts, and
the `language_info` metadata block (which pins the exact kernel version seen
at save time) -- so that git stops treating "I merely opened this notebook"
as a real local change. Actual content (cell source, markdown text) is left
completely untouched, so genuine edits (e.g. answers typed into a notebook)
still correctly show up as real changes.

Usage (as a git clean filter):
    python3 nbclean.py clean < input.ipynb > output.ipynb

Setup (run once per clone, from the repository root):
    git config filter.nbclean.clean "python3 nbclean.py clean"
    git config filter.nbclean.smudge cat

This only affects how git *compares* files internally (status/diff/merge);
it never rewrites the file on disk. Uses only the Python standard library
-- nothing to install.
"""
import json
import sys


def clean(text):
    try:
        nb = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        # Not parseable as JSON (shouldn't happen for a real .ipynb) --
        # pass through unchanged rather than risk breaking anything.
        return text

    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None

    nb.get('metadata', {}).pop('language_info', None)

    return json.dumps(nb, indent=1, ensure_ascii=False) + '\n'


def main():
    if len(sys.argv) != 2 or sys.argv[1] != 'clean':
        sys.stderr.write('usage: nbclean.py clean  (reads stdin, writes stdout)\n')
        sys.exit(2)
    text = sys.stdin.read()
    sys.stdout.write(clean(text))


if __name__ == '__main__':
    main()
