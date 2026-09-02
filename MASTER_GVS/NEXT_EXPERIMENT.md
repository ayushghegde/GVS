# Current Next Experiment — v14Q1 Co-located Dual-Timescale Collar

## Goal
Physically test the useful part of v14Q: ordinary branch use creates a temporary eligibility state, while confirmed/contradicted learning changes the durable v14P Polarized Trail Collar (PTC) state. Both states should live in the same branch-collar structure if possible.

## Why this replaced the literal electromagnet idea

At the current v14O model point, 0.25 V across ~2.3 Mohm gives ~108.7 nA. An ideal straight conductor produces only ~2.17 uT at 10 nm. Direct magnetic writing would require orders of magnitude more current, so a per-branch electromagnet is rejected unless a future magnetoelectric structure proves a major system-level advantage without extra drivers.

## Candidate physical mechanism — simplest first

1. **Dual-timescale trap occupancy in the existing collar**: ordinary inference creates a shallow/temporary occupancy state; a later confirmation/contradiction coincidence pulse converts eligible state into deeper/reversible persistent PTC state.
2. **Separate tiny floating/RC eligibility node** only if leakage and area remain negligible. A ~3.54 aF geometry needs ~2.82e14 ohm for a 1 ms RC time constant, so this is currently second choice.
3. **Magnetoelectric eligibility** only if it reuses the same two branch terminals and beats the electric/trap approach in energy, area, and disturb.

No per-branch MOS selector, sense amplifier, coil, or dedicated magnetic driver is allowed merely to make the experiment work.

## Required tests

1. Inference pulse amplitude/width -> temporary eligibility occupancy.
2. Eligibility decay sweep from ns to s.
3. Persistent PTC disturb after large inference-pulse counts.
4. Confirmation pulse with low/high eligibility -> durable strengthening delta.
5. Contradiction pulse -> durable weakening/reversal delta.
6. Repeated relearning and polarity reversal.
7. Neighboring collar half-select/crosstalk.
8. Temperature and process/geometry variation.
9. Energy per inference trace and per confirmed update.
10. Compare complete branch cost against v14P without eligibility and against a separate RC eligibility node.

## Acceptance

Promote only if:
- usage eligibility materially reduces confirmed relearning encounters (target >=20% improvement retained from the v14Q behavioral model);
- ordinary inference cannot by itself create durable semantic preference;
- persistent state drift under inference remains small enough that route accuracy is not degraded;
- eligibility lifetime can cover the intended local confirmation window without an always-on refresh circuit;
- neighboring branches do not acquire enough false eligibility to change winner statistics materially;
- no per-branch active device is added;
- total energy/area remains better than simply increasing digital/CMOS learning support.

## Failure rule

If a co-located temporary state cannot be separated cleanly from the persistent PTC state, discard UET as a hardware primitive and keep v14P confirmation-gated learning unchanged. Do not add a costly second memory device merely to preserve the idea.
