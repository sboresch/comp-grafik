#!/usr/bin/env python3
"""
Normalizes Jupyter notebooks (.ipynb) so git stops treating routine Jupyter
behavior as a local change.

Just opening a notebook (connecting a kernel) or running any cell makes
Jupyter silently rewrite volatile content -- the `language_info` metadata
block (pinned to whatever kernel version was running at save time), cell
`outputs`, and `execution_count` -- none of which a student typed. git sees
a real byte-level difference either way and can refuse a `git pull` with
"local changes would be overwritten by merge", even though nothing of
substance changed. Actual content (cell source, markdown text) is never
touched, so genuine edits (e.g. answers typed into a notebook) still show up
as real, protected changes.

RECOMMENDED usage -- a plain script run, no git configuration needed at all
(works the same regardless of whether per-repo git config happens to survive
a session restart in your environment, which is not something to rely on):

    cd ~/work/<repo>
    python3 nbclean.py clean-all .
    git add -A
    git pull

Run those three lines any time you want to pull updates. `clean-all` walks
the given directory, normalizing every tracked-looking *.ipynb file in
place; if the only differences from the committed version were Jupyter
noise, `git add -A` finds nothing new to stage and the pull goes through.
If you've actually typed something into a notebook, that content survives
`clean-all` untouched, so it's still correctly staged as a real change and
`git pull` will still (correctly) refuse to overwrite it.

ALTERNATIVE usage, for anyone on a normal persistent machine (not needed on
a JupyterHub session where per-repo git config may not survive a restart):
configure this as a git clean filter once per clone --
    git config filter.nbclean.clean "python3 nbclean.py clean"
    git config filter.nbclean.smudge cat
-- which makes git apply the same normalization automatically on every
`git add`/`diff`/`status`, without needing to remember to run `clean-all`
by hand. This repository's .gitattributes already associates *.ipynb with
a filter named "nbclean"; it's simply inert until/unless this is configured.

Uses only the Python standard library -- nothing to install.
"""
import json
import os
import sys


def clean_text(text):
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


def cmd_clean():
    sys.stdout.write(clean_text(sys.stdin.read()))


def cmd_clean_all(root):
    changed = 0
    checked = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('.ipynb_checkpoints', '.git')]
        for name in filenames:
            if not name.endswith('.ipynb'):
                continue
            path = os.path.join(dirpath, name)
            checked += 1
            with open(path, encoding='utf-8') as fh:
                before = fh.read()
            after = clean_text(before)
            if after != before:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(after)
                changed += 1
    print(f'nbclean: checked {checked} notebook(s), normalized {changed}.')


def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'clean':
        cmd_clean()
    elif len(sys.argv) in (2, 3) and sys.argv[1] == 'clean-all':
        cmd_clean_all(sys.argv[2] if len(sys.argv) == 3 else '.')
    else:
        sys.stderr.write(
            'usage: nbclean.py clean          (reads stdin, writes stdout -- for use as a git filter)\n'
            '       nbclean.py clean-all [dir]  (normalizes every .ipynb under dir, in place; default: .)\n'
        )
        sys.exit(2)


if __name__ == '__main__':
    main()
