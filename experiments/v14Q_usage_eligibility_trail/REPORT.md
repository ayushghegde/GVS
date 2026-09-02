# v14Q Usage-Eligibility Trail — REPORT

**Status:** PARTIAL PASS

## What happened

The proposed idea was split into two claims and tested separately.

1. **Literal magnetic claim:** ordinary branch current should increasingly magnetize a nearby element and thereby attract/steer later electrical activity.
2. **Learning claim:** recent branch usage should make that branch more sensitive to later confirmed learning.

The literal magnetic implementation failed the first-order scale check. Using the current v14O operating point (0.25 V, ~2.3 Mohm ON path), branch current is ~108.7 nA. An ideal straight-wire field is only ~2.17 uT at 10 nm. Producing 1 mT at 10 nm would require ~50 uA (~460x current), and 10 mT ~0.5 mA (~4600x), before accounting for realistic geometry or switching margins. Therefore the ordinary inference current is not promoted as a direct magnetic write mechanism.

The learning claim passed at model level when recast as **Usage Eligibility Trace (UET)**. Branch use creates only a temporary eligibility state. Durable v14P PTC state changes only when later confirmation or contradiction arrives. Across 200 deterministic seeds in a five-way remapping model with 12% feedback:

- baseline without eligibility: mean recovery ~242.15 encounters, median 239;
- usage-eligibility update: mean recovery ~178.41 encounters, median 177;
- mean recovery improvement: ~26.3%;
- final 500-encounter accuracy: ~99.856% for both.

A simple co-located dielectric geometry envelope was also checked. A 10 nm x 10 nm, 5 nm thick, k=20 region is ~3.54 aF. If eligibility were stored as a pure floating-node RC voltage, holding a 1 ms time constant would require ~2.82e14 ohm effective resistance and sub-fA leakage at 0.25 V. This does not prove impossibility, but it makes a passive voltage-history node less attractive than metastable trap occupancy in the already-required PTC dielectric.

## Current problem

v14Q is not yet a physical device. The missing result is whether the same collar used for durable v14P trail memory can also support a **short-lived, low-disturb eligibility substate** from ordinary branch use without becoming a second uncontrolled memory and without adding a selector/transistor per branch.

The main risks are:

- ordinary inference pulses may be too weak to create a useful temporary trap occupancy;
- making them strong enough may disturb the persistent PTC state;
- eligibility may last too briefly or too long;
- neighboring collars may acquire false eligibility;
- a separate floating node could erase the area/energy advantage through leakage-control circuitry.

## What is next

Run **v14Q1 — Co-located Dual-Timescale Collar**.

Test a single branch-collar physical model with two state variables in the same dielectric region:

- fast/temporary occupancy for eligibility;
- slow/reversible polarization/trapped state for persistent route preference.

Required sweep:

1. inference pulse amplitude/width -> temporary occupancy;
2. eligibility decay from ns through s;
3. persistent-state disturb after large inference-pulse counts;
4. coincidence confirmation pulse -> durable update gain versus eligibility level;
5. contradiction pulse -> reversible durable weakening;
6. neighboring collar crosstalk;
7. energy and extra terminal count;
8. compare against no-eligibility v14P and against a separate RC eligibility node.

Promote only if eligibility improves learning speed materially while inference disturb remains small and no per-branch active device is added.

## Exact run command

```bash
python3 experiments/v14Q_usage_eligibility_trail/run_v14q.py > experiments/v14Q_usage_eligibility_trail/results.json
```

## Tool / model provenance

- Python standard library only for this experiment.
- 200 deterministic seeds: 0..199.
- No PDK, SPICE, extracted layout, or fabricated device data are used in this v14Q experiment.
- Magnetic values are first-order Biot-Savart straight-conductor calculations.
- RC values are first-order parallel-plate dielectric geometry calculations.
- All physical conclusions are therefore screening decisions, not measured device claims.
