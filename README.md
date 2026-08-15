# GVS

Reproducible workspace for the GVS hardware experiments.

## Current baseline policy

The unfinished v11T experiment is **not** the validated baseline. This repository resumes from the last completed experiment before v11T. Until the exact prior netlist/results are recovered, they must not be reconstructed or presented as measured results.

## Experimental rule

Preserve the existing GVS architecture and test intent. A new architecture change is accepted only when experiment evidence justifies it.

## Environment

The intended simulation stack is:

- NGSpice
- SKY130 PDK transistor models
- reproducible shell scripts
- versioned SPICE testbenches and results

Large PDK archives are intentionally not committed to Git. Put the supplied `sky130_fd_pr.tar.zst` and `common.tar.zst` in `pdk/source/` (or point `PDK_ROOT` at an extracted SKY130 installation).

## Repository layout

- `experiments/baseline/` — last completed pre-v11T experiment (exact artifacts only)
- `experiments/v11T_unfinished/` — notes/artifacts from the unfinished v11T attempt
- `tests/` — regression/testbench definitions once recovered
- `scripts/` — setup and simulation entry points
- `pdk/` — local PDK staging, excluded from Git
- `results/` — generated simulation output, excluded except intentional reference summaries
- `docs/` — experiment history and rules

## Next checkpoint

1. Recover the exact last completed pre-v11T netlist/testbench/results.
2. Record its tool/model versions and SKY130 corner.
3. Run it unchanged under NGSpice.
4. Confirm reproduced outputs against the recorded baseline.
5. Only after reproduction passes, continue new experiments.

No missing experimental result should be invented to make a test pass.
