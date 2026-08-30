# Neural Glyph v14D — Local Contradiction Re-Settling Tissue

**Status: system-model promotion candidate; physical v14C Role-Pressure freeze remains conditional until flattened/normalized PEX 48+48 mismatch closure is preserved.**

v14D does not replace the v14C heterogeneous 64-cell organization. It keeps 4 General Reserve Cells, 2 Constraint/Exact Critical Reserve Cells (CRCs), cell-as-wire conduction, Population Confidence, FAST/SLOW Role Pressure, CHL, break-before-make patch handoff, Dual-Key Egress, Local Venule -> Charge Artery -> regional reservoir recovery, and sparse persistent-memory consolidation.

## New mechanism — Local Contradiction Restart (LCR)

**Local Contradiction Restart (LCR):** when one small Constraint neighborhood repeatedly settles into an unresolved contradiction, only that neighborhood loses part of its accumulated membrane state and receives a small stochastic reseed; already-consistent bindings, relations and other constraint neighborhoods remain intact.

The intended physical behavior is:

`local contradiction persists -> local conflict/fatigue state accumulates -> local membrane decay/reseed -> neighborhood re-settles -> global state preserved`.

LCR is not a software variable-selection algorithm and does not authorize an answer. Population Confidence remains the authority for whether the tissue has a robust result.

## Why it is different from deeper settling

v14C Confidence–Pressure Effort (CPE) allows more settling while local pressure is low. It spends more time on the same attractor. LCR changes the local attractor only after repeated contradiction.

Whole-problem restart is also different: it destroys solved local progress and creates a large latency/recovery spike. v14D deliberately preserves unaffected membrane neighborhoods.

## Model representation

The v14D screen represents a hard query as several local Constraint neighborhoods. A neighborhood may be in a solvable basin or a trapped contradictory basin. Ordinary settling can finish a solvable neighborhood; a trapped neighborhood requires a restart/reseed event. The no-restart trap probability is calibrated so the fixed-four-round control remains near the independently preserved v14C ~79% hard-reasoning boundary.

The experiment compares:
- fixed four-round settling;
- v14C-style low-pressure extra effort;
- whole-problem restart;
- LCR with trigger depth, pressure threshold and reseed strength swept.

## Selected model result

At 100 seeds, the selected LCR point is:
- pressure threshold: 15 queued queries;
- contradiction trigger: 2 failed local settles;
- hard-neighborhood re-trap probability after reseed: 0.02;
- easy-neighborhood re-trap probability: 0.0075;
- low-pressure settling budget: 8 hard / 6 easy rounds.

Mean results:
- fixed-four resolution: ~78.56%; on-time: ~55.90%;
- pressure-only resolution: ~78.76%; on-time: ~56.21%;
- whole restart resolution: ~92.87%; on-time: ~40.43%;
- selected LCR resolution: ~89.23%; on-time: ~65.43%.

Selected LCR also reduces mean attempts from ~5.304/query (fixed) to ~5.227/query because solved neighborhoods are not repeatedly recomputed. It disturbs ~0.752 local state-neighborhoods/query. Whole restart disturbs ~1.355 neighborhoods/query on average and has much worse latency.

The selected LCR p95 latency is ~35.80 epochs versus ~38.96 fixed and ~87.01 whole restart in this model.

## Robustness of the direction

The result is not based on one selected setting. All tested two-failure LCR settings at pressure thresholds 10/15/20 and hard re-trap probability 0.02–0.08 improve eventual resolution over the fixed-four control. Trigger-three uses less disturbed state (~0.36 neighborhood/query) but gives a smaller resolution/on-time improvement, establishing a real responsiveness-versus-disturbance frontier.

## Candidate physical realization

No new central controller is introduced. The next physical implementation should test a **Contradiction Fatigue Node (CFN)**:

**Contradiction Fatigue Node (CFN):** a small local volatile state that accumulates only while mutually incompatible Constraint cells remain active without Population Confidence rising; crossing its hysteretic threshold briefly weakens/resets only that local membrane neighborhood.

Candidate implementation to test, not yet promoted:
- small MIM fatigue capacitor;
- event-charge path from repeated local contradiction;
- CHL-like decay so isolated conflicts vanish naturally;
- hysteretic threshold;
- local reset/reseed gate;
- stochastic seed from the cheapest available device/thermal noise source;
- no direct authority over robust answer output.

A CFN must be much smaller/cheaper than adding another full CRC. If not, keep CPE only.

## Physical evidence boundary carried from v14C

v14D inherits the selected physical Role-Pressure dimensions from v14C:
- FAST: 2 x legal 2x2-um MIM, PFET injector 1.26/0.50 um;
- SLOW: 4 x legal 2x2-um MIM, PFET injector 1.38/0.50 um;
- one ~1x1-um CHL bucket/path;
- exact 6-MOS Schmitt selector.

The repository v14C evidence establishes 27/27 matched PVT FAST-before-SLOW timing but explicitly leaves the final normalized/flattened PEX 48+48 mismatch signoff open. v14D does not upgrade that conditional evidence by assertion.

## KEEP / REJECT

KEEP:
- v14C heterogeneous reserve organization;
- CPE as a pressure gate on extra local effort;
- LCR as the selected reasoning-quality mechanism;
- preserving solved neighborhoods during contradiction recovery;
- unresolved output when confidence is insufficient.

REJECT:
- whole-problem restart as the default contradiction response;
- unlimited retries;
- adding more full reserve cells merely to improve search quality;
- a processor selecting which symbolic variable to flip;
- using stochastic reseed without local contradiction/confidence gating.

## Next physical/system experiment

v14D1 should co-test CFN and existing Role Pressure:
1. normalize/flatten preserved FAST/SLOW PEX hierarchy;
2. complete 48 FAST + 48 SLOW MOS+MIM mismatch signoff;
3. build the smallest CFN/reset gate next to a Constraint neighborhood;
4. verify CFN does not directly couple into Grammar GC/GR beyond accepted local limits;
5. measure false restart rate under isolated/noisy contradictions;
6. measure escape probability under persistent contradiction;
7. combine CFN with CPE and multi-region workloads;
8. reject CFN if its area/energy cost exceeds its reduction in unresolved hard queries.
