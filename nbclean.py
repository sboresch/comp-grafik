#!/usr/bin/env python3
"""
Git clean filter for Jupyter notebooks (.ipynb).

Strips volatile, kernel-generated content that Jupyter rewrites on its own
just from opening/running a notebook -- cell outputs, execution counts, and
the `language_info` metadata block (which pins the exact kernel version seen
at save time) -- so that git can stop treating "I merely opened this
notebook" as a real local change. Actual content (cell source, markdown
text) is left completely untouched, so genuine edits (e.g. answers typed
into a notebook) still correctly show up as real changes.

One-time setup (run once per clone, from the repository root):
    git config filter.nbclean.clean "python3 nbclean.py clean"
    git config filter.nbclean.smudge cat

IMPORTANT: this filter alone does *not* stop `git pull` from refusing with
"local changes would be overwritten by merge" when Jupyter has touched a
notebook -- that refusal is based on a faster stat-cache check that does not
route through clean filters. The actual fix is to run `git add -A` *before*
`git pull` (not after): `git add -A` re-stages every file through this
filter, which leaves nothing staged if the only differences were kernel
noise, after which `git pull` proceeds normally. If you really have typed
something into a notebook, `git add -A` will (correctly) leave that staged
as a real change, and the following `git pull` will still correctly refuse
rather than overwrite it. See the repository README for the full recipe.

Uses only the Python standard library -- nothing to install.
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
