# GVS

Reproducible workspace for the GVS hardware experiments.

## Current baseline

The preserved baseline is **v12S — PARTIAL PASS**. The canonical repository copy is stored directly under `experiments/v12S/` as readable source, runnable scripts, and compact result tables.

v12S integrated the complete SKY130 schematic lifecycle and recorded nominal PVT, mismatch, parasitic-stress and hierarchical-rebuild results. It remains PARTIAL PASS because there is no real placed/routed RC extraction yet. The unfinished later layout attempt is not promoted over this baseline.

The previously committed `artifacts/v12S/...zip` copy was removed because it was incomplete compared with the user-supplied package. Do not use an old archive as authoritative when its size/hash does not match the supplied source.

## Experimental rule

Preserve the existing GVS architecture and test intent. A new architecture change is accepted only when experiment evidence justifies it.

Every AI/Codex agent must follow `AGENTS.md`: an experiment is not finished until its reproducible artifacts, status, report and manifest are written back into this repository.

## Environment

The intended simulation stack is:

- NGSpice
- SKY130 PDK transistor models
- reproducible shell/Python scripts
- versioned SPICE testbenches and results
- physical layout/extraction tools when the experiment reaches that stage

Large PDK distributions remain local rather than duplicated in Git. Put the supplied `sky130_fd_pr.tar.zst` and `common.tar.zst` in `pdk/source/`, or point `PDK_ROOT` at an extracted SKY130 installation.

## Repository layout

- `experiments/v12S/` — canonical preserved v12S experiment files
- `experiments/` — normal experiment records and future versions
- `scripts/` — setup, simulation and experiment-finalization helpers
- `pdk/` — local PDK staging, excluded from Git
- `results/` — generated scratch output; persistent experiment results belong with the experiment
- `docs/` — experiment rules/history
- `AGENTS.md` — persistence rules for AI/Codex agents

## Next physical checkpoint

Preserve the v12S architecture, make a real layout, extract real RC, then rerun the existing lifecycle/test battery. Fix specific physical failures if extraction exposes them rather than redesigning the architecture without evidence.

No missing result should be invented to make a test pass.
