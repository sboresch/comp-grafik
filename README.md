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
