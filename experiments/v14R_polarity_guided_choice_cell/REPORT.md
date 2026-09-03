# v14R — Polarity-Guided Choice Cell (PGCC)

**Status: PARTIAL PASS — physical branch-mouth capacitance closed; integrated polarity collar remains a device-level target, not a fabricated result.**

## Goal

Finish the ordinary Neural Glyph semantic cell as far as current evidence allows, with the specific objective of replacing per-cell/per-synapse transistor selection rather than accumulating more helper circuits. v14R revisits the v14G/J/L/M/N/O/P/Q replacements and keeps only mechanisms that can collapse into one small physical branch primitive.

## What happened

### 1. The old v14P Choice Node problem was physically tested

A five-way metal2 branch-mouth proxy was created using the supplied Magic 8.3.681 source and SKY130A technology files. The layout is a shared CHOICE conductor feeding five candidate branch mouths.

Magic reported:

- SKY130A technology version: `1.0.602-0-gf3c505b`
- total DRC errors: `0`
- CHOICE self/substrate capacitance: `112.362 aF`
- five explicit CHOICE-to-branch couplings: `5 × 7.95455 aF`
- total extracted CHOICE loading represented by those terms: `152.13475 aF = 0.152135 fF`

This is well below the old v14P preferred target of `<= 1 fF`.

With the inherited v14O modeled ON resistance of `2.3 Mohm`, a 20% Choice Node voltage collapse for the extracted metal loading is about `0.078 ns`. Adding five estimated 10 nm × 10 nm × 5 nm, k=25 collars raises the model node load to about `0.17427 fF`, and the 20% quench time remains only `0.08944 ns`.

**Evidence boundary:** the 0.152135 fF metal result is a real Magic/SKY130 extraction from the proxy in this directory. The collar capacitance is a geometry estimate and the guided-gap resistance is inherited model data, not an extracted v14R device.

### 2. Literal magnetic attraction was rejected again

The ordinary v14O branch current is far too small to make direct self-electromagnet writing attractive. v14R therefore does not use a magnet to pull current into the correct wire.

The retained idea is **electric polarity**: a reversible local dipole/polarization state changes the guided-gap field and therefore the bridge-formation time.

### 3. HZO is the preferred polarity-collar candidate

The first physical candidate is an edge-exposed ferroelectric Hf0.5Zr0.5O2 (HZO) collar sharing the two branch terminals. The HZO is not placed in the main inference current path. Its polarization fringes the nearby v14O guided gap.

Published HZO work supports the scale being worth testing:

- 5 nm HZO has been reported with remanent polarization above ~20 uC/cm2 and coercive voltage around ~1 V after wake-up (Communications Physics 2022, doi:10.1038/s42005-022-00951-x).
- 4 nm HZO has demonstrated ~0.6 V one-shot operation and ~1.2 V stable-memory operation with strong retention/endurance in optimized capacitors (ACS Applied Materials & Interfaces 2022, doi:10.1021/acsami.2c15369).
- recent HZO capacitor/device reports commonly show remanent polarization in roughly the high-teens to mid-20s uC/cm2 range, depending strongly on electrodes/process.

For a 10 nm × 10 nm patch, `P = 0.16 C/m2` corresponds to ~100 elementary charges of bound polarization. The inherited v14P race model used about +10e effective target bias and -3e contradicted bias.

A finite 3-D square-dipole-sheet calculation was therefore added. For a 7.5 nm patch, P=0.16 C/m2, with the near polarized edge 1 nm from the observed gap and the compensating sheet 1.5 nm behind it, the pre-metal-screening fringe envelope at the gap is ~0.419 V. The inherited v14P nominal trail target is ~0.159 V. That geometry can therefore lose about 62% of the envelope to additional screening and still reach the old target. For P=0.22 C/m2 and a 10 nm patch 1 nm away, the envelope is ~0.654 V, requiring ~24% to survive additional screening.

**Important:** this is an electrostatic geometry screen, not a calibrated ferroelectric-field simulation. Metal screening, domains, imprint, electrode geometry and real fringe coupling are now the main physical unknowns.

### 4. The extracted quench makes the polarity requirement measurable

The five-way branch-race model was rerun with the extracted-plus-estimated `0.17427 fF` node load.

For nominal P=0.16 C/m2 converted to an effective local bound-charge fraction:

| retained effective fraction | target equivalent | correct first | correct + quench |
|---:|---:|---:|---:|
| 7.5% | 7.49 e | 95.33% | 94.82% |
| 10% | 9.99 e | 98.65% | 98.49% |
| 12.5% | 12.48 e | 99.47% | 99.40% |
| 15% | 14.98 e | 99.75% | 99.73% |
| 20% | 19.97 e | 99.94% | 99.92% |

So the v14R collar target is no longer vague: **for this inherited model, the physical collar should deliver at least ~12.5% effective-charge-equivalent coupling, preferably >=15%, while preserving read/program separation.**

### 5. Selector-free learning voltage was changed

The earlier v14O ~0.4 V selected-learning hypothesis is not enough to assume HZO switching.

v14R instead proposes a rare bipolar coincidence program:

`source +0.6 V` and `target -0.6 V` -> `~1.2 V across the selected collar`

An unpaired/half-selected branch sees no more than about `0.6 V`, while inference remains around `0.25 V`.

A deliberately simple threshold sensitivity around `Vc = 1.0 V` shows why this may be useful, but also why variation matters. At sigma=0.12 V, a 1.2 V selected pulse is above the assumed threshold in ~95.2% of samples, while 0.6 V half-select is above it in ~0.042%. At sigma=0.18 V, selected coverage falls to ~86.6% and half-select rises to ~1.30%.

This is **not** a ferroelectric compact model; real switching is pulse-width/domain/history dependent. It converts the problem into a concrete measured requirement: the chosen collar process must have a sufficiently narrow switching window and survive repeated half-select pulses.

### 6. v14Q eligibility was kept only in the form that helps the transistor-replacement direction

A temporary Usage Eligibility Trace (UET) was retested as a learning-rate modifier, not as a second route memory.

Normal stress model:

- baseline mean recovery to >=90% of changed relations: `84.375 encounters`
- UET-gated recovery: `55.25 encounters`
- improvement: `34.52%`
- final mean accuracy: `99.990%` for both baseline and UET in this screen

However, raw UET amplifies bad teaching signals. At 20% incorrect feedback, raw UET final accuracy fell to ~98.74%. Three-sample corroboration recovered it to ~99.71%. At 30% bad feedback, corroboration improved ~94.66% raw to ~98.26%, but did not fully eliminate damage.

Decision: **KEEP UET only if it is a shallow/short-lived state inside the same collar and only scales a corroborated programming event. Do not let UET directly become persistent truth or require a new per-branch device.**

## v14 family comparison and consolidation

### v14J — SPCL
Useful: reversible two-terminal weight concept and physical capacitive evidence.

Not selected as the final common branch primitive: the trainable memcapacitor and its programming infrastructure remained open, and large link capacitance is unnecessary if a local field can bias the guided gap directly.

### v14L — QVC + VRS
Useful: explicit temporary integration and volatile release.

Rejected for the common v14R cell because it creates a separate membrane capacitor/leak/release device stack. v14R lets the guided-gap dynamics provide the slow switching state and uses only tiny parasitic node capacitance for distribution/quench.

### v14M — one BDJ device family
Useful: the goal of two-terminal diffusive elements and low event energy.

Not kept literally: one stack was not physically closed as both reliable volatile firing and long-retention learned memory. v14R separates those material jobs locally while keeping them in one integrated two-terminal branch structure.

### v14N — seeded nucleation
Useful: pre-guiding/field focusing to reduce stochastic filament delay.

Kept through v14O's inert spine/guided-gap mechanism.

### v14O — GG-SLDJ
**KEEP as the firing core.** It provides the volatile bridge, field focus and passive current self-limiting hypothesis.

### v14P — polarized trail collar
**KEEP and strengthen.** The shared Choice Node is now physically below its capacitance target. The collar is the best current route-memory mechanism because the long-term state does not need to carry the main inference current.

### v14Q — usage eligibility
**KEEP conditionally inside the collar only.** It improves learning speed in the model but must remain subordinate to confirmation/corroboration and must not add another active device.

## v14R selected cell — Polarity-Guided Choice Cell (PGCC)

The cell has no dedicated CMOS selector, no central threshold transistor, no intentional membrane capacitor and no separate VRS.

```
                 incoming event/evidence
                         |
                         v
                 tiny CHOICE metal node
                   ~0.15 fF extracted
                         o
             +-----------+-----------+
             |           |           |
             v           v           v
          PGDB-0       PGDB-1      PGDB-2 ...
             |           |           |
        next cell     next cell    next cell
```

**PGDB — Polarity-Guided Diffusive Branch:** one two-terminal integrated connection containing:

1. v14O inert conductive guide/spine;
2. ~1.3 nm-class volatile dynamic gap target;
3. passive/intrinsic ballast target;
4. edge-exposed HZO polarity collar around/next to the gap;
5. optional shallow UET state in that same collar, not a separate device.

### Inference

1. evidence excites the tiny Choice Node;
2. all 4–5 candidate PGDBs see the same temporary drive;
3. persistent collar polarity changes each local gap field;
4. the favored branch nucleates/bridges first;
5. that bridge collapses the tiny node in ~0.09 ns at the current model point;
6. competitors are quenched;
7. the volatile bridge relaxes after the event.

The node itself is not long-term memory and is too small to be a useful membrane integrator. The integration/threshold timescale is intentionally in the guided-gap device physics.

### Learning

- recent use may create shallow eligibility in the collar;
- confirmation/corroboration applies the selected ~1.2 V differential with favorable polarity;
- contradiction applies the opposite polarity;
- ordinary ~0.25 V inference must not materially switch deep polarization;
- half-selected <=~0.6 V connections must tolerate the complete lifetime learning workload.

## Why this is closer to a transistor replacement

The ordinary semantic connection no longer requires a transistor to:

- select the learned output;
- provide a separate threshold switch;
- hold the connection weight in SRAM;
- enforce per-branch current compliance;
- maintain a separate membrane capacitor.

Instead, the branch's material state and nonlinear bridge physics perform selection, thresholding, volatility, current limiting and route memory locally.

That is the correct direction only if the HZO/GG-SLDJ compound branch can be fabricated without hidden per-branch drivers/selectors. Shared rare learning rails and regional regeneration are allowed only if amortized over many cells.

## Current problem

The old Choice Node problem is closed at the SKY130 metal-proxy level. The dominant unresolved problem is now **compound device closure**:

1. Can an edge-exposed HZO collar retain >=~25–40% of the simple finite-dipole fringe envelope at the actual guided gap, corresponding to >=~12.5–15% effective-charge-equivalent coupling in the inherited race model?
2. Can ~0.25 V inference remain nondestructive while ~1.2 V selected bipolar coincidence reverses the collar reliably?
3. Can repeated ~0.6 V half-select pulses avoid cumulative domain/trap drift?
4. Can shallow eligibility and deep persistent polarization coexist in the same collar without UET becoming a second inference memory?
5. Can the HZO process coexist with the chosen diffusive metal/gap stack and thermal budget?

Until those are measured/calibrated, v14R is not a fabricated transistor replacement.

## What is next — v14R1

Build the first calibrated compound-branch model/physical test in this order:

1. choose a specific 5–6 nm HZO electrode stack with published P-V data and pulse-width dependence;
2. fit a Preisach/Landau-Khalatnikov or measured switching table to that data instead of the current threshold sensitivity;
3. solve 3-D electrostatics of the edge-exposed collar + metal electrodes + 1.3 nm guided gap to measure actual post-screening gap-field shift;
4. couple that field shift into the existing v14O guided-gap delay distribution;
5. run 0.25 V read-disturb, +/-0.6 V half-select endurance, +/-1.2 V selected reversal, temperature and process variation;
6. only then fabricate/extract a compound PGDB test structure or select a different polarity material if HZO fails.

**Promotion rule:** do not add a MOS selector to rescue a weak collar. If the compound two-terminal branch cannot meet the window economically, reject that collar implementation and keep the v14O firing core while testing the next two-terminal polarity memory candidate.
