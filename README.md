# Computational Graphics — Course Material

Course material for the Computational Graphics course ("Computergrafik") at the
University of Vienna, taught by Stefan Boresch.

The material consists of Jupyter notebooks (R kernel) plus the input files,
force-field parameters, and coordinate files needed to run the accompanying
[CHARMM](https://www.academiccharmm.org) calculations and VMD exercises on the
course's JupyterHub server.

## Getting started (on the course JupyterHub)

Open a terminal in JupyterHub and run:

```
cd ~/work
git clone https://github.com/sboresch/comp-grafik.git
```

No GitHub account or SSH key is needed for this — it's a plain, read-only
download.

This creates `~/work/comp-grafik/`, containing the folders below. All paths
given inside the notebooks assume the repository was cloned there.

## Getting updates later in the semester

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


## Course structure

### Part 1 — VMD (mostly on your own computer)

1. Work through the [VMD tutorial](https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/index.html)
   (at least "Working with a single molecule" up to "Creating multiple
   representations").
2. **`more_vmd/`** — a few warm-up exercises (on triosephosphate isomerase,
   PDB 5TIM) that test your comprehension of the tutorial material and prepare
   you for the final exercise below.
3. **`glutamate_switch/`** — the final VMD exercise: visualizing two
   conformations of a real protein (a voltage-dependent phosphatase).
   Document your solution (pictures, script/state files, a short write-up).

### Part 2 — Illustrative tasks using CHARMM (mostly on the JupyterHub)

Occasionally you'll download files from here for visualization with VMD.

4. **`charmm-stuff/`** — a basic introduction to CHARMM scripting, with first
   exercises in energy minimization. Do this one first.

The remaining four can be done in whatever order suits you:

* **`mc_tests/`** — illustrative examples of Monte Carlo move types.
* **`implicit_solvent_md/`** — a basic MD exercise (implicit-solvent
  simulation of a protein, with standard trajectory analyses).
* **`ala_dipeptide/`** — minimization-based dihedral (Φ/Ψ) scan of alanine
  dipeptide, then the same system revisited with MC and MD.
* **`glutamate_switch_2/`** — revisiting the glutamate switch: estimating the
  pKa of Glu411 in the two structures and building a solvated simulation
  system with CHARMM-GUI.

Each folder's own notebook has the detailed instructions and the exact TODO
list for that task. (Deadlines and upload instructions for a given course run
are posted on Moodle, not here.)
