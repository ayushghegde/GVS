# Current Next Experiment — v13B5 Self-Configuring Shared-Wall Local Region

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

The repository now also contains:

- v13A5: physically closed PVT-tracking Grammar ratio with co-placed self-check readout;
- v13A6: 10-MOS dual-pair reader that avoids analog swap-path asymmetry;
- v13A7: legal same-die MIM-over-transistor vertical overlap;
- v13B0: deep passive-Myelin chains are unsafe without regeneration;
- v13B1: direct analog steering is useful when the destination already has a physical competition node;
- v13B2: Tri-Wall Glyph Cell and structured Nervous Core concept;
- v13B3: physical 3-MIM + minimum fourth-face MOS cell, full-swing/static contact PVT + small mismatch pass, direct ~1 V lease-gate control rejected;
- v13B4: self-configuring fourth-face threshold model, new 1.1/1.2 V gate-transfer screen, leak/recovery lifecycle, and shared-wall geometry/electrical screen.

## New v13B4 result

### Self-Setting Fourth Face

A fourth-face link should learn from repeated **validated** useful outcomes, not from raw traffic.

Per contact:
- local Use Reservoir stores recent useful-reuse charge;
- a small residual tap samples post-capture cleanup charge only after a validated winner;
- inactivity lets the state decay;
- unvalidated/noisy events cannot refresh it.

Shared across one eight-way group:
- two v12A-style replica leak pilots;
- one Environment Reservoir / PVT reference;
- one slow promotion/demotion decision element.

This reuses v11S/T/U and v12A rather than inventing a software calibration table.

### Actual pass-gate screen

The physical v13B3 fourth-face topology was rerun with the real SKY130 MIM + W=0.42/L=0.15 NFET models.

TT:
- gate 1.0 V -> only ~3.25 mV exact/partial separation: reject high-confidence use;
- gate 1.1 V -> ~20.21 mV;
- gate 1.2 V -> ~25.08 mV.

At 1.2 V nominal:
- TT ~25.08 mV;
- FF ~25.06 mV;
- SS ~25.06 mV.

One fresh mismatch-library launch per corner also preserved ~24.9-25.9 mV separation. This is a first screen only; multi-seed mismatch at 1.2 V remains required.

The measured gate charge is ~0.98-1.02 fC at 1.2 V, giving a simple gate-voltage-times-charge work proxy around ~1.2 fJ.

### Charge lifecycle

Selected rule from v11/v12:

`live charge -> information`

`controlled leak -> adaptation / time / threshold`

`expired/reset charge -> one-way recovery`

Do not harvest a live analog state while it is still carrying information.

### Shared-wall result

Sharing structural walls can materially reduce duplicated framework material. In the user's illustrative t/p=0.1 geometry model:
- independent shell solid fraction ~48.8%;
- shared framework ~27.1%;
- ~44.5% less framework material;
- cavity fraction rises from ~51.2% to ~72.9%.

But two capacitor faces must not share a floating middle conductor. Two 2x2 MIMs with a floating midpoint correspond to ~4.756 fF effective coupling; a 0.2 V neighbor transition could inject ~12.4 mV into a ~72 fF evidence node.

Selected solution: **Janus Service Wall** — independent capacitor faces on both sides of one structural wall with a robust central shield/reference/service spine.

See:
- `experiments/v13B4_self_config_shared_walls/REPORT.md`
- `experiments/v13B4_self_config_shared_walls/results/fourth_face_gate_transfer.csv`

## Next physical experiment — v13B5

Build the first physical self-configuring contact group behind the already-proven eight-way Regional Lease.

Required steps:

1. reuse two replica leak pilots for the eight local contacts;
2. build at least two local Use Reservoirs and post-capture validated residual taps;
3. implement one shared slow promotion/demotion reader/trainer;
4. keep the robust v13A5/v13A6 path active while a contact is unpromoted or uncertain;
5. once promoted, drive the fourth-face gate to at least the tested 1.2 V point and use direct analog transfer;
6. run repeated-use, alternating-use, two-then-idle, raw-noise, false-refresh and long-idle tests;
7. run TT/FF/SS + at least four independent mismatch launches per corner at the promoted gate point;
8. add one-way expired-charge recovery and confirm it does not disturb live evidence or contact retention;
9. physically emulate one Janus shared wall with two isolated MIM faces and a strongly referenced middle shield, then extract cross-coupling;
10. compare shared-wall area/capacitance against two separate walls;
11. after those pass, populate the eight-way region with multiple real Grammar/template/Myelin structures.

## Acceptance rule

Keep self-configuring contacts only if:

- raw/noisy traffic cannot promote them;
- validated repeated use does promote them;
- inactivity naturally demotes them;
- PVT/mismatch does not create false promotion or wrong analog transfer;
- recovery never loads live information;
- shared-wall crosstalk remains small versus the measured ~25 mV local class separation;
- area/energy saved by removing repeated readers/routing is larger than the slow adaptation hardware cost.

The hollow/framework package remains a later physical implementation target. The immediate goal is to prove the same electrical rules in ordinary manufacturable silicon first.