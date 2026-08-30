# Neural Glyph v14E — Physical Contradiction Fatigue

**Status: physical PEX/PVT/mismatch pass for the selected local Contradiction Fatigue Node (CFN); system-model pass for unclamped local restart.**

v14E keeps the v14D heterogeneous 64-cell tissue and its Local Contradiction Restart idea, but replaces the abstract restart trigger with a physical **Contradiction Fatigue Node (CFN)**.

**CFN:** a local volatile fatigue state that accumulates only when one Constraint neighborhood remains contradictory; isolated contradictions decay; two nearby contradictions cross a hysteretic threshold and locally reseed that neighborhood. Population Confidence/solved state can clear/inhibit fatigue. Regional pressure is deliberately not allowed to veto a mature local contradiction.

Selected physical cell:
- 15 MOS + 2 MIM;
- fatigue MIM: 3.0 x 3.0 um;
- bucket MIM: ~1.71 x 1.71 um;
- exact 6-MOS Schmitt selector;
- contradiction inverter / preparation path / transmission-gate charge sharing / confidence clear;
- no regional-pressure clamp transistor.

The 3.0 x 3.0 fatigue MIM is intentional. Removing the regional-pressure clamp transistor removed useful parasitic capacitance; a 2.4 x 2.4 um fatigue MIM then false-triggered at several cold/high-drive PVT corners. A physical size sweep showed 3.0 x 3.0 um restores separation without adding a control device.

## Physical signoff

Magic selected layout: 0 DRC, 15 extracted MOS, 2 extracted `sky130_fd_pr__cap_mim_m3_1` devices.

PEX PVT battery: 4 conditions x TT/FF/SS x 1.62/1.80/1.98 V x -40/27/125 C = 108 runs.
- one contradiction -> 0/27 restart;
- two nearby contradictions -> 27/27 restart;
- widely spaced contradictions -> 0/27 restart;
- Population-Confidence/solved inhibit -> 0/27 restart.

PEX mismatch battery: 48 independent mismatch trials per condition = 192 runs.
- one -> 0/48 restart;
- two nearby -> 48/48 restart;
- spaced -> 0/48 restart;
- confident -> 0/48 restart.

The inherited FAST/SLOW Role-Pressure primitive is also frozen: the completed 48 FAST + 48 SLOW mismatch battery leaves ~39.9 ns worst observed activation-envelope separation.

## System result

The physical-CFN rule was replayed on the 100-seed v14D hard-reasoning workload. A pressure-clamped CFN was rejected because it suppressed most useful contradiction events. The selected unclamped local CFN reaches about 87.13% eventual resolution and 64.51% on-time completion versus 78.56% / 55.90% fixed-four settling. It uses about 0.132 local restarts/query versus ~0.752 in the abstract v14D LCR model, preserving most of the gain with ~82% fewer local disturbances.

## KEEP / REJECT

KEEP: local contradiction memory, local-only stochastic reseed, confidence/solved inhibit, FAST/SLOW Role Pressure, differentiated reserve tissue, Population Confidence as output authority.

REJECT: regional pressure as a veto on mature local contradiction, whole-problem restart as default, adding another CRC merely for reasoning quality, and assuming DRC alone proves electrical correctness.
