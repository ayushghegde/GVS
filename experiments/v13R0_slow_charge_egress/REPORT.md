# Neural Glyph v13R0 — Slow Post-Use Charge Egress

**Verdict: MODEL PASS.** After a cell's information state is finished, residual charge should leave through a weak/slow recovery path into the local Charge Artery instead of being dumped abruptly. The regional reservoir remains in the architecture as the buffer/decoupler/aggregator between many cells and the larger battery/collector.

## New term
**Slow Charge Egress (SCE):** after the existing cleanup/expiry event marks a local state invalid, a weak recovery path releases its remaining recoverable charge over several local event intervals into the Charge Artery.

SCE does not touch live information state and does not create a recovery scheduler. The intended physical implementation is a fixed device/RC property or cell-type-specific recovery aperture.

## Model
- 256 cells.
- Three expiry patterns: uniform, bursty, and deliberately aligned 128-cell stress bursts.
- Each expired cell contributes one normalized residual-charge unit.
- `tau=0` is an instantaneous dump.
- `tau=1..16` uses a normalized exponential release kernel.
- The regional reservoir feeds the larger battery/collector at a fixed rate of 1.15x the long-run mean expiry rate.
- The simulation continues after the workload to allow residual charge to finish transferring.

The charge unit is normalized. This experiment studies peak/ripple/buffering, not absolute recovered joules.

## Selected screen: tau = 8 local event intervals
| expiry pattern | peak Charge-Artery influx reduction | peak reservoir occupancy reduction | eventual transfer |
|---|---:|---:|---:|
| uniform | 52.92% | 60.36% | ~100% |
| bursty | 74.18% | 18.72% | ~100% |
| aligned stress | 86.92% | 28.55% | ~100% |

For an ideal first-order decay, tau=8 releases roughly 90% by 18.4 intervals, 95% by 24.0, and 99% by 36.8 intervals.

## What happened
Slow egress converts a sharp cell-scale current dump into a low-amplitude tail. That reduces the peak electrical event seen by the Charge Artery and reduces the amount of short-term charge the reservoir must absorb.

## Why the reservoir stays
The reservoir still provides isolation, buffering, decoupling, fault containment, local low-voltage reuse where justified, and surge absorption before staged transfer to the larger battery/collector.

## Important limit
“Slower is always better” is rejected. Larger tau keeps reducing peaks but leaves dead charge resident for longer. Final tau must be chosen from physical leakage, reservoir voltage, next-use timing, and the real cell capacitance.

## Decision
- KEEP cell -> slow egress -> Charge Artery -> regional reservoir -> larger battery/collector.
- KEEP the existing rule that only expired/cleaned-up state may drain.
- KEEP low-voltage, physically separated recovery.
- REJECT abrupt synchronized drain as the normal mode.
- REJECT a per-cell recovery controller.

## Reproduce
`python3 experiments/v13R0_slow_charge_egress/source/run_v13r0.py`

Evidence class: deterministic normalized charge-flow model; not transistor PEX.
