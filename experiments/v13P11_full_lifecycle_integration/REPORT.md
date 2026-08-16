# v13P11 — GTI/CMR selection inserted into the complete v12S lifecycle

**Verdict: PARTIAL PASS — topology integration is transparent under the same compact-device screen; supplied-SKY130 transient signoff still pending**

## What happened

The complete 214-line v12S tile topology, sources, timing, Grammar/Myelin evidence, soma competition, route-capture, recovery, invalidation and fallback measurements were retained. Only the three unavailable PDK primitive models (1.8 V NFET, 1.8 V PFET and M3 MIM) were replaced with compact stand-ins so that the integration could be screened despite the local ngspice/SKY130 parser incompatibility.

The fair comparison is differential: run the unchanged v12S topology and the same topology plus GTI/CMR + local PRE gate under the **same** compact transistor corner. This experiment does not claim that the compact model reproduces historical v12S SKY130 electrical values.

## Integration inserted

The selected interface is:

`GTI ROW/COL -> 4T active-low CMR -> 2T local PRE gate -> existing v12S pre node`

Receiver physical parasitics from v13P8 were retained approximately:

- WAKEN_B local storage: 1.45 fF
- ROW input load: 1.24525 fF
- COL input load: 1.19779 fF

Selection windows begin just before the original v12S PRE release windows and the first window ends with the original PRE falling edge, so the cheap PFET-pass/NFET-clamp interface resets PRE_LOCAL without adding a full transmission gate.

## Broad compact-device screen

Five deliberately broad compact-device cases were used: fast, typical, slow, N-fast/P-slow and N-slow/P-fast.

### Selected tile: differential baseline vs integrated

Across all five cases, the selected integrated tile preserved the corresponding compact-baseline values exactly (within printed precision) for the principal internal evidence/state measurements including:

- lease level `L2`
- SRAM/rebuild state `QSET`
- first-query dendrites `H0A`, `H1A`
- capture sampled state `CAPA`
- cleanup sample `CLEANA`
- second-query/fallback output `OUTB`

The integration changes VDD-window energy in the compact screen by only about **0.8-1.3%**. This is not the full GTI wire energy; v13P10 separately estimates/physically grounds the selected 16x16 row+column event-wire charge at about 0.68 pJ.

The largest relative change among tiny sampled near-zero states is `QCLR`, but its absolute change is sub-nanovolt scale and both baseline/integrated values remain essentially zero.

### Incomplete/absent coordinate

Direct PRE-boundary measurements were added for four selection modes: ROW+COL, ROW-only, COL-only and none.

Across all five broad compact-device cases:

- ROW+COL -> `PRE_LOCAL` reaches 1.8 V during the release window; active-low `WAKEN_B` is essentially 0 V.
- ROW-only -> `WAKEN_B` remains 1.8 V and `PRE_LOCAL` remains essentially 0 V.
- COL-only -> same.
- no coordinate -> same.

With incomplete/absent coordinates the existing soma precharge devices therefore stay enabled; the tile is not released into competition.

The dendrite evidence nodes can still move because v12S places passive Grammar/template evidence upstream of soma release. This experiment intentionally does not insert switches into every dendrite. Whether globally distributed evidence should later be gated is an energy question and is not assumed to be a correctness problem.

## Important limitation

The compact model itself does not reproduce the historical v12S route-latch behavior, so this experiment is **not** a replacement v12S electrical validation and is not TT/FF/SS signoff. The result is only that adding the GTI/CMR/PRE boundary is transparent relative to the same compact-model baseline and cleanly blocks release for incomplete coordinates.

The historical v12S SKY130 result remains the source of truth for the solved local tile. Full integrated signoff requires an ngspice build/parser compatible with the supplied combined SKY130 library (or another validated PDK simulation route).

## Decision

Keep the CMR + 2T PRE boundary as the preferred low-cost GTI selection interface.

Do **not** add an explicit MIM membrane by default. The physically extracted receiver already provides local parasitic storage, and the orthogonal M4/M5 event geometry removed the real long-parallel-wire crosstalk hazard. An intentional MIM remains an optional later filter only if a measured full-swing glitch problem appears.

## What is next

1. Fix/replace the PDK simulator parser and repeat CMR + PRE integration with actual SKY130 TT/FF/SS/mismatch models.
2. Then connect one selected physical GTI coordinate to the complete historical v12S lifecycle and compare against the fixed acceptance battery.
3. Only after that, evaluate inter-cluster hierarchy above the physically validated 16x16 GTI island.
4. Separately measure whether broadcasting Grammar/template evidence to inactive islands costs enough energy to justify a local evidence gate; do not add that hardware pre-emptively.
