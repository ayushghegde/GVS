# Current Next Experiment — v13B2 Tri-Wall Local Cell Emulation

## What is already solved

The physical locality path remains:

`orthogonal coordinate -> compact coordinate release -> Regional Event Lease -> 8 isolated local event paths`.

The repository already contains:

- v13A5: physically closed PVT-tracking Grammar ratio with co-placed self-check readout;
- v13A6 dual-pair reader: physical 10-MOS mirrored reader that avoids analog swap-path asymmetry;
- v13A6 margin-tiered policy: high-margin characterized representations may use a cheaper one-phase reader, while low/unknown margin keeps conservative self-check/fallback;
- v13A7: same-die MIM-over-transistor vertical placement is physically legal in the tested SKY130 slice;
- v13B0: deep Passive-Myelin analog chains are not safe as unlimited transmission lines;
- v13B1: direct analog Grammar steering is useful when the destination already has a local membrane/competition node;
- v13B2: three capacitor walls + one controlled connection face is a promising cell geometry; a continuous conductive interior fill is rejected, while a structured insulating core with sparse controlled conductors is kept as a future architecture target.

## New v13B2 result

### Tri-Wall Glyph Cell (TWGC)

A future 3D cell uses three capacitive faces as evidence/synapse inputs and its fourth face as the controlled connection/output.

Using the present typical 2x2 MIM value (~9.52 fF per wall) with the historical 40 fF Grammar dendrite and 0.2 V events gives a first-order screen:

- 3 active walls: ~0.523314 V from a 0.44 V baseline;
- 2 active walls: ~0.495543 V;
- separation: ~27.77 mV.

This closely reproduces the old 3-input Grammar behavior, so the geometry is computationally meaningful rather than decorative.

Literal vertical sidewall MIM is not available in SKY130. Emulate TWGC first with three legal planar MIMs placed above/around the local logic using the v13A7 vertical-overlap result.

### Touch/contact propagation

Do not use uncontrolled conductive touching as a routing replacement.

A passive equal-capacitance chain starting with a 0.2 V stored packet falls approximately:

`200 -> 100 -> 50 -> 25 -> 12.5 mV`

after four sequential equal-cell charge-sharing transfers.

This confirms:

- one characterized short analog contact can be useful;
- deep passive contact chains destroy margin;
- a hot long relation should be promoted to a direct Myelin chord or regenerated;
- robust/exact state remains full-swing.

### Interior fill

Do not fill the cavity with one conductor. It destroys selectivity by equalizing attached states.

Selected future interpretation:

**Nervous Core Scaffold** = insulating/structural non-silicon fill containing isolated controlled conductors/junctions and sparse promoted Myelin chords.

A generic orthogonal 3D interior mesh gives little path improvement for large link growth. A structured core or sparse direct chords is more promising, but physical wire length—not hop count alone—must decide the result.

See:
- `experiments/v13B2_triwall_nervous_core/REPORT.md`

## Next physical experiment — TWGC emulation inside v13B

Build one ordinary-silicon emulation of the Tri-Wall Glyph Cell before attempting a true hollow package.

Required steps:

1. three real legal 2x2 MIMs act as the three logical capacitor walls;
2. place them above/around a compact local evidence node where v13A7 says vertical overlap is legal;
3. make the fourth logical face a weak controlled MOS contact/output;
4. connect that output directly to an already-existing local competition node;
5. compare readerless analog steering against the closed dual-pair reader;
6. run TT/FF/SS plus actual independent mismatch;
7. measure crosstalk, analog margin, area, and source/VDD energy;
8. if one-hop contact passes, compare two sequential contacts against one promoted direct Myelin chord;
9. only retain the hollow/filled-core architecture if this local emulation materially reduces reader count, routing energy, or area.

## Acceptance rule

The TWGC emulation is accepted only if:

- one-hop direct analog steering preserves correct exact/partial polarity across tested PVT and independent mismatch;
- no neighboring inactive wall/contact creates a false robust result;
- the fourth-face contact does not erase the analog margin through charge sharing;
- readerless operation saves material energy/area versus the closed reader when the destination already contains a membrane;
- a two-hop passive chain is not allowed unless measured margin remains characterized; otherwise use regeneration or a promoted chord;
- exact/global fallback remains independent.

## Hollow-chip decision

Do not fabricate the real hollow/filled-core chip yet.

The current selected long-term interpretation is:

- active semiconductor skins/surfaces where transistors are required;
- three-wall capacitive cells on inner/outer surfaces;
- an insulating Nervous Core Scaffold instead of a solid conductive core;
- sparse controlled diagonal Myelin chords through that core;
- robust full-swing/exact routing for changing or precise information.

The real hollow package becomes justified only after the TWGC emulation and mixed eight-way region show a measured advantage.