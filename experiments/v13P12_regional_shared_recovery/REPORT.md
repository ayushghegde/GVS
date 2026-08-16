# Neural Glyph v13P12 — Regional Shared Recovery

## Verdict

**PARTIAL PASS — ADOPT 10 pF / 4-tile regional recovery as the next physical candidate.**

This experiment deliberately reuses a useful old-Glyph idea from the v11V/v11W lineage: recovery charge should be pooled regionally instead of duplicating storage at every neuron/tile. It does **not** restore the old 88 pF / 132 pF neuron membranes or the old PVT leak-memory loop, because current v12S already passes PVT/mismatch without them.

## What happened

The current accepted tile path (v12S lifecycle plus the physically extracted 4T active-low coordinate-release cell) was replicated four times. The four tiles shared one recovery node instead of using one 10 pF `rec` capacitor per tile.

Worst-case screen: all four tiles execute the same lifecycle simultaneously, so their soma recovery and lease-demotion charge arrive on the shared node together.

A second lease-request window was added after invalidation. This is important: a small shared reservoir can allow the immediate query to pass while leaving the lease too hot, which could falsely request physical rebuild again.

## Capacitance boundary

Four independent tiles would use 40 pF total recovery capacitance.

On the current tile at SS/85 C:

- 8 pF shared: rejected; post-error second-request node falls to about 0.864 V, below the 0.9 V decision boundary.
- 10 pF shared: pass; second-request minimum about 1.292 V nominal SS.
- 14 pF shared: pass with larger margin, but unnecessary after mismatch testing of 10 pF.

Selected point: **10 pF shared across four tiles**.

This reduces the simulated recovery-capacitance target from 40 pF to 10 pF, a **75% reduction**.

## Nominal PVT result at 10 pF shared

All four tiles pass at TT/25 C, FF/-20 C and SS/85 C.

Representative tile 0:

| Corner | H exact (V) | H partial (V) | route0 (V) | route1 (V) | physical out (V) | lease after error (V) | second-request minimum (V) |
|---|---:|---:|---:|---:|---:|---:|---:|
| TT | 0.543918 | 0.501292 | 1.799989 | -3.13e-6 | 1.8 | 0.345633 | 1.698036 |
| FF | 0.544927 | 0.502317 | 1.799997 | -1.56e-7 | 1.8 | 0.337187 | 1.793166 |
| SS | 0.543087 | 0.500443 | 1.799983 | 4.49e-7 | 1.8 | 0.354124 | 1.292119 |

Invalidation still clears VALID/route state and fallback still returns a full-swing result.

## Mismatch battery

The 10 pF shared point was run in 12 launches: four each of `tt_mm`, `ff_mm`, and `ss_mm`. Each launch contains **four independently mismatched tiles sharing one reservoir**, so 48 tile instances were exercised.

Result: **12/12 launches pass all four tiles.**

Across those launches:

- minimum dendrite exact-minus-partial margin: about **38.13 mV**;
- maximum wrong-route decision excursion: about **3.38 mV**;
- weakest post-error second-request minimum: about **1.076 V** (SS mismatch), still above the 0.9 V request boundary;
- correct route remains full-swing;
- invalid physical query remains blocked;
- exact fallback remains full-swing.

## Recovered energy interpretation

At TT with four simultaneous tiles and the selected shared 10 pF reservoir:

- recovery node at 31 us: ~0.1990 V;
- recovery node at 35 us: ~0.2893 V.

The capacitor-energy increase over that interval is approximately **220 fJ**.

This does **not** create energy. It pools approximately the same recovered reset charge that would otherwise be stored in separate local reservoirs, while reducing duplicated storage capacitance.

## Physical-area implication

The SKY130 MIM model uses about 2 fF/um^2 typical area density plus perimeter capacitance. A legal 30 x 30 um MIM is roughly 1.82 pF. Therefore a 10 pF linear-MIM regional target requires roughly six large MIM units, while four separate 10 pF tile reservoirs would require roughly 22–24 such units.

The exact regional reservoir layout is not yet extracted, so this remains a physical candidate rather than a completed layout result.

## Rejected experiment — HVT MOS-varactor reservoir

A denser HVT MOS-varactor reservoir was screened because its modeled capacitance increases as the recovery voltage rises, which could provide useful self-limiting behavior.

Nine 20 x 20 um HVT varactors allowed TT/FF/SS nominal tile operation, but SS second-request margin was too narrow (~0.994 V).

Increasing to twelve devices improved TT/SS margin, but the complete FF transient repeatedly failed with a tiny-timestep collapse inside the nonlinear varactor model. The same failure remained when the twelve devices were represented with the model multiplicity parameter (`vm=12`).

**Decision: reject the varactor reservoir as the selected implementation for now.** The extra density does not justify voltage/corner sensitivity and unresolved FF behavior.

## Old-Glyph ideas used / not used

Useful and retained:

- v11V/v11W: shared one-way/regional recovery rather than duplicated local storage;
- later Glyph rule: shared hardware only when it does not disturb local evidence/competition.

Not reintroduced:

- 88 pF / 132 pF old neuron membranes;
- regional PVT/leak adaptation loop;
- activity-driven sticky analog correction.

Those solve problems of the older natural-firing neuron that are not currently demonstrated failures of v12S.

## Current problem

The electrical shared-reservoir result is strong, but the 10 pF reservoir itself is still represented as a lumped capacitor. It needs a real physical implementation.

## Next

1. Try a stable **stacked MIM** regional reservoir using both SKY130 `cap_mim_m3_1` and `cap_mim_m3_2` if DRC allows compatible overlap.
2. If stacking is illegal or awkward, use a six-device MIM bank and extract its real routing RC.
3. Connect the physical reservoir bank to four local tile recovery branches and rerun the same PVT/mismatch + second-request battery.
4. Do not add PVT adaptation or another controller unless a measured failure requires it.
