# GVS

## FIRST AND AUTHORITATIVE: MAIN ARCHITECTURE

**Read [`MASTER_GVS/MAIN_ARCHITECTURE.md`](MASTER_GVS/MAIN_ARCHITECTURE.md) first.**

That file is the single authoritative description of the current GVS / Neural Glyph architecture. It has priority over historical version folders, preserved baselines, experiment summaries, and older README wording when determining what the system currently is.

Historical versions such as v12S remain preserved as evidence and reproducible experiment records. They are not the current whole-system architecture unless `MAIN_ARCHITECTURE.md` explicitly says so.

Reproducible workspace for the GVS hardware experiments.

## Preserved historical baseline

The preserved autonomous complete-tile baseline is **v12S — PARTIAL PASS**. The canonical repository copy is stored directly under `experiments/v12S/` as readable source, runnable scripts, and compact result tables.

v12S integrated the complete SKY130 schematic lifecycle and recorded nominal PVT, mismatch, parasitic-stress and hierarchical-rebuild results. It remains PARTIAL PASS because there is no real placed/routed RC extraction yet. It is retained as historical experimental evidence; it does not override `MASTER_GVS/MAIN_ARCHITECTURE.md`.

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

- `MASTER_GVS/MAIN_ARCHITECTURE.md` — **first and authoritative current architecture**
- `experiments/v12S/` — canonical preserved v12S historical experiment files
- `experiments/` — normal experiment records and future versions
- `scripts/` — setup, simulation and experiment-finalization helpers
- `pdk/` — local PDK staging, excluded from Git
- `results/` — generated scratch output; persistent experiment results belong with the experiment
- `docs/` — experiment rules/history
- `AGENTS.md` — persistence and architecture-priority rules for AI/Codex agents

## Next work

Use `MASTER_GVS/MAIN_ARCHITECTURE.md` to determine the active architecture and its current physical closure target. Historical experiment folders are evidence sources, not replacements for the current architecture.

No missing result should be invented to make a test pass.
