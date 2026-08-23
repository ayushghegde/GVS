# Neural Glyph v13L0 — Differential Neurovascular Isolation Screen

**Verdict: MODEL PASS / PHYSICAL OPEN.** The v13K neurovascular architecture remains worth physicalizing, but the signoff metric is refined: for a weak Grammar candidate/reference pair, the dangerous quantity is **differential service coupling** (unequal coupling into the two evidence sides), not total common-mode coupling alone.

## Evidence class
This experiment is a deterministic architecture/circuit proxy. It reuses previously preserved v13K values and does **not** claim new SKY130 PEX.

## Why v13L exists
v13K separated firing, expired-charge recovery and heat into Nerve, Charge Artery and Thermal Capillary networks. That removed the worst high-swing recovery problem, but v13K1 treated disturbance mainly as a kick into one weak node.

The selected Grammar reader is differential and self-checking. Therefore a better pre-layout question is:

> If a Nerve or Charge Artery couples into both Grammar sides, how unequal may those two couplings become before a ~25 mV useful differential falls below the ~18 mV high-margin boundary?

This directly targets the physical asymmetry that can turn service activity into a false differential decision.

## New term
**Differential Service Coupling (DSC):** the mismatch between service-line coupling into the Grammar candidate side and the reference side; equal/common coupling is much less dangerous than unequal coupling.

Normalized asymmetry is defined as:

`a = (C_candidate - C_reference) / (C_candidate + C_reference)`

with the pair-average coupling held at the selected v13K proxy.

## Reused conservative values
- weak evidence capacitance: 72 fF per side;
- useful differential: 25 mV;
- high-margin target: 18 mV;
- average service coupling reference: 0.124 fF;
- local Nerve swing: 0.200 V;
- Charge-Artery recovery swing: 0.0903 V, from the preserved ~0.1990 -> ~0.2893 V interval.

Available high-margin disturbance budget is therefore 7 mV.

## Model
For worst-direction aligned transitions:

`dV_diff ~= 2 * a * Ccouple / Cnode * (Nnerve*Vnerve + Nartery*Vartery)`

This intentionally assumes every selected transition pushes in the same harmful direction. It is a stress bound, not an activity prediction.

## Key results
Maximum normalized coupling asymmetry that still leaves at least 18 mV:

| coupling scale vs 0.124 fF | Nerve transitions | Artery transitions | max asymmetry |
|---:|---:|---:|---:|
| 1.0x | 8 | 8 | ~87.5% |
| 1.0x | 8 | 32 | ~45.3% |
| 1.0x | 16 | 16 | ~43.8% |
| 1.0x | 32 | 32 | ~21.9% |
| 1.5x | 8 | 32 | ~30.2% |
| 2.0x | 8 | 32 | ~22.6% |
| 2.0x | 16 | 16 | ~21.9% |
| 2.0x | 32 | 32 | ~10.9% |

The full reproducible sweep generator is `run_v13L0.py`; compact thresholds are in `summary.csv`.

## What happened
The result is better than the earlier one-node interpretation in one important way: service coupling does not automatically consume the full Grammar margin if it reaches both sides similarly.

At the current 0.124 fF average-coupling proxy, even a deliberately heavy 8-Nerve + 32-Artery aligned stress keeps the 18 mV margin until candidate/reference coupling asymmetry exceeds ~45%.

Even if average coupling is doubled, the same stress still tolerates ~22.6% normalized asymmetry before crossing the high-margin boundary.

However, the 32-Nerve + 32-Artery case at 2x coupling has only ~10.9% asymmetry tolerance. Therefore v13L must not assume that arbitrary dense service wiring is safe merely because each individual wire is low swing.

## Architecture implication
Do **not** add a new scheduler, ADC, calibration loop or per-cell controller.

Instead, the physical v13L slice should make weak-pair protection a geometry rule:

1. keep candidate/reference evidence physically local and matched;
2. place Nerve and Charge Artery behind the protected service face/shield rather than beside only one weak evidence side;
3. prefer geometry that makes unavoidable service coupling common-mode;
4. sign off **extracted differential coupling**, not just each line's absolute coupling;
5. use the existing two-phase Grammar self-check to reject physical-side preference rather than adding a separate detector;
6. high-swing VDD/config/test remains a separate robust domain and may still require quiet/staggered activity if PEX says so.

This is a refinement of v13K, not a replacement for it.

## Why the 10-MOS reader remains selected
The repository's physically selected robust Grammar path is the 10-MOS dual-input-pair self-check reader. Its two mirrored phases already ask whether the logical result survives reversal of the physical latch side. That mechanism is naturally useful against layout-side bias and service-coupling asymmetry.

v13L therefore does not revive the older proposed 7-MOS/one-phase path as the primary physical closure target.

## Hollow / inside-out consequence
The hollow architecture still passes the model screen conditionally. The useful interpretation is not 'put active cells everywhere'. It is to use the different surfaces for different physical roles:

- weak/local computation on protected cell skins;
- Nerve and Charge-Artery services on matched/shielded framework paths;
- high-swing power/config/test farther away on robust facade/backside service layers;
- passive Thermal Capillaries toward shared thermal collectors;
- optical routes only where the existing distance/reuse break-even selects them.

Literal active inner cavity walls remain FUTURE_PROCESS.

## What this experiment does not prove
- no new Magic layout was generated;
- no v13L parasitic extraction was performed;
- no new TT/FF/SS transistor simulation was run;
- no manufacturing yield claim is made;
- the 0.124 fF reference remains inherited from earlier protected-service coupling work.

## v13L0 decision
**KEEP v13K neurovascular separation. ADD differential-coupling asymmetry as the physical signoff metric. DO NOT add new control logic.**

This rule is model-supported and must now be tested physically before it is treated as closed architecture evidence.

## Next — v13L1 Physical Differential Neurovascular Slice
Build one same-die SKY130 slice containing:
- real 10-MIM Grammar candidate/reference structure;
- selected body-tied 10-MOS two-phase reader;
- ~0.2 V Nerve;
- separate low-voltage Charge Artery;
- recovery contact controlled by existing expiry/cleanup lifecycle;
- shields/service-face geometry;
- deliberately asymmetric service placement variants.

Extract and measure:
- candidate-side and reference-side Nerve coupling separately;
- candidate-side and reference-side Artery coupling separately;
- differential coupling asymmetry;
- exact/partial Grammar margin with Nerve-only, Artery-only and simultaneous activity;
- TT/FF/SS and independent MIM+MOS mismatch;
- false accepts and fallbacks;
- stuck-open/stuck-closed recovery faults;
- deliberately injected 0.9/1.2/1.8 V high-swing comparison;
- area and event/recovery energy overhead.

### Physical acceptance
v13L1 passes only if:
- normal low-swing service activity produces zero wrong robust accepts across the battery;
- extracted differential service coupling stays within the measured Grammar margin or causes safe fallback;
- recovery never loads a live information node;
- two-phase self-check catches physical-side preference when deliberately stressed;
- direct-neighbor routing remains cheaper than unnecessary spine traversal;
- no new global quiet scheduler is required for ordinary low-voltage recovery.
