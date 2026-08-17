# Source Map / Provenance

## Uploaded recovery archives
- `NEURAL_GLYPH_V11_MASTER_RECOVERY_BUNDLE.zip`
  - `GVS_NEURAL_GLYPH_V11_MASTER_SUMMARY.md` — history v11N through v11W
  - v11W rebuilt report/results/scripts
  - supplied SKY130 PDK archives
- `NEURAL_GLYPH_COMPLETE_SYSTEM_V12R_ALL_FILES.zip`
  - `GLYPH_COMPLETE_SYSTEM_SUMMARY.md`
  - reports: v11X, v12A ... v12R
  - circuits and result CSVs for the v12 chain
  - v12Q system script
- `NEURAL_GLYPH_V12S_AUTONOMOUS_COMPLETE_TILE.zip`
  - final v12S report, exact runner, complete tile/template netlists, PVT/mismatch/parasitic/hierarchical rebuild results
- `Pasted markdown.md`, `Pasted markdown (2).md`
  - user-preserved narrative summaries; useful cross-check, not preferred over original report/result files when both exist

## GitHub repository
Repository: `ayushghegde/GVS`

Current physical experiment branch: `experiment/v13P0-physical-rc`

Important paths:
- `docs/EXPERIMENT_RULES.md`
- `AGENTS.md`
- `experiments/v12S/REPORT.md`
- `experiments/v12S/source/run_v12s_complete_tile.py`
- `experiments/v13P0_physical_rc/`
- `experiments/v13P0_physical_myelin_edge/`
- `experiments/v13P1_two_edge_crosstalk/`
- `experiments/v13P2_four_edge_cluster/`
- `experiments/v13P3_shared_spine_fanin/`
- `experiments/v13P4_real_terminal_loading/`
- later v13 GTI/receiver physical folders on the same branch
- `experiments/v13P10_gti16x16_physical/`
- `experiments/v13P11_full_lifecycle_integration/`
- `experiments/v13P12_regional_shared_recovery/`
- `experiments/v13A_physical_cost_locality/`

## Tool / PDK inputs used in physical continuation
- `common.tar.zst`
- `sky130_fd_pr.tar.zst`
- `magic-8.3.681.zip`
- `netgen-1.5.323.tgz`
- `ngspice-master.zip`
- `Spice64.zip` (Windows ngspice package; not the preferred Linux runtime)

## Source priority
When facts conflict:
1. original per-version report + raw result CSV/netlist
2. repository preserved experiment report/raw extraction
3. master archive summary
4. chat/pasted narrative summary
5. new inference/model

Never silently upgrade a lower-priority claim above raw evidence.
