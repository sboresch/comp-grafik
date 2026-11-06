# Getting updates later in the semester

If I push fixes or additions, get them with:

```
cd ~/work/comp-grafik
python3 nbclean.py clean-all .
git add -A
git pull
```

The middle two lines matter, not just `git pull` on its own. Just *opening*
a notebook can make Jupyter silently rewrite parts of it (which exact kernel
version ran it, leftover "last run" markers) even if you never typed
anything -- and that alone is enough for a plain `git pull` to refuse with:

```
error: Your local changes to the following files would be overwritten by merge
```

`nbclean.py clean-all .` (committed in this repository, nothing to install)
rewrites every notebook in place, stripping exactly that kind of
kernel-generated noise -- never touching anything you actually typed into a
notebook, e.g. answers to embedded questions. If that was the only
difference, `git add -A` then finds nothing to stage and `git pull` goes
through cleanly. (No one-time setup needed, and nothing to configure that
would need to survive a session restart -- just these commands, every time.)

**If `git pull` still refuses even after this:** that means you really have
typed something into that notebook that the update would otherwise
overwrite. If you want to keep it, copy that notebook somewhere outside this
folder first. Then:

```
git checkout -- <path/to/the/file.ipynb>
git pull
```

and re-apply whatever you'd saved by comparing it against the updated file.

**If it keeps refusing even after that** (this has happened at least once,
for reasons that weren't fully pinned down -- possibly something re-touching
the file in the background, possibly leftover state from an earlier failed
pull attempt): don't delete anything -- move your whole current copy aside
instead, so nothing is lost (answers you've typed into *any* notebook in
this folder, not just the one causing trouble, are all still sitting safely
in the renamed copy), and get a fresh clone next to it:

```
cd ~/work
mv comp-grafik comp-grafik-old
git clone https://github.com/sboresch/comp-grafik.git
```

Your previous copy is now at `~/work/comp-grafik-old/`, completely intact. Open
it, find anything you need (answers you typed, your own files), and copy
that over into the matching file in the fresh `~/work/comp-grafik/` -- then you
can delete `comp-grafik-old` once you're sure you got everything.
