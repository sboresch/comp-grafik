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

If I push fixes or additions, get them with a plain `git pull` from inside
`~/work/comp-grafik`. There's one wrinkle: just *opening* a notebook can make
Jupyter silently rewrite parts of it (which exact kernel version ran it,
leftover "last run" output) even if you never typed anything -- and that's
enough for git to refuse the pull with something like:

```
error: Your local changes to the following files would be overwritten by merge
```

**Do this once, right after cloning**, to make git ignore that kind of noise:

```
cd ~/work/comp-grafik
git config filter.nbclean.clean "python3 nbclean.py clean"
git config filter.nbclean.smudge cat
```

(This only changes how git *compares* notebooks internally -- it never
touches the files themselves, and it won't hide anything you actually typed
into a notebook, e.g. answers to embedded questions. Only kernel-generated
noise is ignored.)

**If you still hit the error anyway** (e.g. you skipped the step above), and
you're sure the local copy of that one file has nothing you want to keep:

```
git checkout -- <path/to/the/file.ipynb>
git pull
```

If you *have* typed something into that file you want to keep, copy it
somewhere outside the repository first, then run the above.

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
