# v14D — Local Contradiction Re-Settling

**Verdict: SYSTEM MODEL PASS / PHYSICAL CFN CONDITIONAL / v14C PEX-MISMATCH FREEZE STILL OPEN.**

## Problem inherited from v14C

v14C showed that adding more reserve hardware is no longer the dominant reasoning bottleneck. Fixed four-round hard reasoning resolves about 79% of the calibrated hard workload, and pressure-gated deeper settling improves it only slightly. The problem is local search state getting stuck, not lack of another universal compute block.

## Experiment

A query is represented as multiple local Constraint neighborhoods. Some neighborhoods are in a trapped contradictory attractor. Four policies were compared over 100 deterministic seeds:

1. `fixed4` — four settling rounds, no restart;
2. `pressure` — deeper settling only when backlog pressure is low;
3. `whole_restart` — periodically erase/reseed the full query state;
4. `local_restart` — erase/reseed only repeatedly contradictory unresolved neighborhoods while preserving solved neighborhoods.

LCR was swept across:
- contradiction trigger = 2 or 3 failed local settles;
- pressure threshold = 10, 15 or 20;
- hard-neighborhood re-trap probability after reseed = 0.02, 0.04, 0.06 or 0.08.

The no-restart trap probability was calibrated so the fixed-four control remains near the independently preserved v14C ~79% hard-reasoning boundary. Therefore this screen tests the architectural restart policy; it is not a claim that this abstract neighborhood model is a foundation-model benchmark.

## Selected comparison

| Policy | Resolved | On time <=20 | p95 latency | Attempts/query | Disturbed state/query |
|---|---:|---:|---:|---:|---:|
| fixed four | 78.56% | 55.90% | 38.96 | 5.304 | 0 |
| pressure-only | 78.76% | 56.21% | 38.68 | 5.328 | 0 |
| whole restart | 92.87% | 40.43% | 87.01 | 7.290 | 1.355 |
| **selected LCR** | **89.23%** | **65.43%** | **35.80** | **5.227** | **0.752** |

The selected LCR point uses threshold 15, trigger depth 2 and post-reseed hard re-trap probability 0.02.

### Improvement versus fixed four
- eventual resolution: +10.67 percentage points;
- on-time completion: +9.53 percentage points;
- p95 latency: about 3.15 epochs lower;
- mean attempts: ~1.46% lower, despite higher resolution;
- on-time decisions per optional-module copy: ~17.05% higher.

### Why whole restart is rejected
Whole restart does produce the highest eventual resolution in this model, but it destroys already-correct local progress. It cuts on-time completion to ~40.43%, raises p95 latency to ~87 epochs and disturbs ~1.8x as much state as selected LCR. Its extra success is bought by redoing too much work.

## Parameter robustness

The best LCR settings are not isolated. Trigger-two points across pressure thresholds 10/15/20 and re-trap settings 0.02–0.08 all improve resolution over fixed four. Trigger-three halves disturbed-state activity to roughly 0.36 neighborhood/query but gives a weaker ~85–87% resolution / ~57–60% on-time regime. This creates a tunable physical tradeoff rather than a single magic threshold.

## Architectural decision

KEEP Local Contradiction Restart as a v14D system candidate.

Do not add more General Reserve Cells for this problem. Implement the next experiment as a tiny local Contradiction Fatigue Node (CFN) near Constraint tissue and test whether physical local membrane decay/reseed can reproduce the model benefit cheaply.

## Evidence boundary

The v14D result is a seeded system model. No CFN transistor layout, PEX or energy measurement exists yet. The physical FAST/SLOW Role-Pressure primitive remains inherited from v14C, including its explicit open item: normalized/flattened extracted hierarchy and final 48+48 PDK MOS+MIM mismatch signoff.
