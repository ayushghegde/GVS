# GVS v13R — Differentiated Charge-Egress Cellular Fabric

**Status: architecture/model pass; physical slow-egress transistor closure open.**

v13R keeps the v13Q cell-as-local-wire architecture, population-coded uncertainty, v13K/v13L separated neurovascular services, and the existing physical Grammar evidence. It changes two things: how expired charge leaves cells, and how much hardware each cell contains.

## 1. Slow Charge Egress
**Slow Charge Egress (SCE):** after a cell's information state has been invalidated by the normal cleanup/expiry lifecycle, its remaining recoverable charge leaves through a weak path over several local event intervals instead of being dumped abruptly.

Selected architecture:
`useful cell state -> expiry/cleanup -> weak egress -> Charge Artery -> regional reservoir -> larger battery/collector`

The reservoir is not removed. It remains the electrical buffer, decoupler, aggregator, surge absorber and fault boundary.

### v13R0 model evidence
At tau=8 local event intervals:
- uniform expiry: peak artery influx ~52.9% lower;
- bursty expiry: ~74.2% lower;
- aligned 128-cell stress: ~86.9% lower;
- modeled eventual transfer ~100% after the workload is allowed to drain.

This tau is a model screen, not a physical time constant. A transistor/RC implementation must be characterized before promotion.

## 2. Reservoir hierarchy retained
The recovery hierarchy is:
1. cell residual charge;
2. weak post-expiry egress path;
3. shared low-voltage Charge Artery;
4. regional reservoir;
5. staged transfer to a larger battery/collector when useful.

Reservoir advantages retained:
- cells are isolated from the final storage element;
- correlated expiry is buffered;
- battery-side transfer can be slower/steadier;
- regional decoupling remains available;
- recovery failure affects energy, not correctness;
- local low-voltage reuse remains possible where physically justified;
- charge collection wiring stays separate from weak information contacts.

## 3. Cell differentiation
**Differentiated Embodied Tissue (DET):** many cells share the same ECC body/contact standard but contain only the optional computational/state machinery needed by their role.

**General Reserve Cell (GRC):** a small minority of broader-function cells retained for novelty, repair, remapping and workload imbalance.

Current 64-cell model composition:
- 20 relay/conduction;
- 12 Grammar;
- 10 template;
- 8 binding/context;
- 8 constraint/competition;
- 2 exact-patch;
- 4 general reserve.

This is a first composition, not a fixed biological taxonomy.

### v13R1 result
Compared with putting all five optional module classes in all 64 cells:
- optional module-copy reduction: 81.25%;
- average added mixed-operation movement: 1.8456 cell hops;
- ~0.277 fJ using the existing 0.15 fJ/hop proxy;
- all module classes survived the 10% independent random-cell-failure stress in 10,000 tested trials.

Abstract cost sensitivity with module costs swept 0.25x..8x a common body unit retained ~65.7% or greater total hardware reduction at the 5th percentile for the selected 4-general-cell fabric.

## 4. Standard-cell family, not unique cells
v13R does not create a unique layout for every concept.

The manufacturing target is a compact reusable cell library:
- Relay ECC;
- Grammar ECC;
- Template ECC;
- Binding/Context ECC;
- Constraint/Competition ECC;
- Exact-Patch ECC;
- General Reserve ECC.

All reuse the same boundary/contact conventions where possible. Differentiation is primarily omission/addition of optional local structures, not extra process steps.

v13R2 shows that fine specialization stops winning if type-specific design/test/yield overhead becomes too high. Therefore the library may be coarsened after physical area/yield characterization.

## 5. Differentiated recovery
Recovery hardware is also role-dependent.

A cell earns a Slow Charge Egress tap only when its expected recoverable charge and activity justify the added device/coupling/area. High-state-capacitance cells are stronger candidates than tiny relay cells.

This prevents the recovery network from recreating the universal-cell duplication that differentiation is trying to remove.

## 6. Communication retained from v13Q
Short local information communication still prefers:
1. active face aperture;
2. edge/vertex aperture if it materially wins;
3. regenerative cell chain;
4. dedicated Nerve/spine/chord when that wins.

Charge does not travel through these information apertures. Heat does not travel through switched information contacts.

## 7. Physical cell anatomy
A differentiated cell is conceptually:

```text
          CELL WALL / CONTACT SKIN
  selectable neighbour apertures / local integration
                    |
          minimal role-specific core
      Grammar OR relay OR context OR exact
                    |
            state/fatigue if needed
                    |
        [optional SCE recovery tap]
                    |
             Charge Artery

Thermal attachment remains passive and separate.
```

The communication aperture switch and the recovery egress device should be placed near the wall/service boundary rather than over weak Grammar evidence, following the v13Q1b/v13L physical lesson.

## 8. Physical geometry evidence
A real planar SKY130 Magic pair supports the boundary-placement rule:
- communication NFET: `NEIGHBOR <-> CELL`;
- recovery NFET: `CELL <-> ARTERY`;
- two real NFET child layouts;
- 0 DRC;
- ~0.016098 fF direct coupling from each service to CELL;
- ~0.00403226 fF one-sided coupling from the left information service to GC and mirrored right recovery service to GR.

Using the preserved 72 fF screening node gives only ~0.0112 mV for a 0.2 V information event and ~0.00506 mV for the 0.0903 V artery swing in the simple coupling proxy.

This is **PHYSICAL GEOMETRY PASS / TRANSIENT OPEN**. The slow-egress resistance, leakage, backflow and PVT/mismatch are not yet closed because the supplied ngspice revision is too old for the current SKY130 model deck.

## 9. Current v13R decision
### KEEP
- cell-as-local-wire;
- population-coded uncertainty;
- separate Nerve/Charge/Thermal anatomy;
- slow post-expiry charge egress;
- regional reservoir before battery/collector;
- compact differentiated cell family;
- small General Reserve population;
- role-dependent recovery hardware.

### REJECT
- abrupt synchronized recovery as normal behavior;
- direct live-cell-to-battery connection;
- one full universal compute cell everywhere;
- one recovery controller/tap everywhere;
- unlimited one-off cell variants;
- removing the reservoir simply because cell egress is smoother.

## 10. What remains hard
- v13Q/v13R aperture transient TT/FF/SS is tool-blocked by the old supplied ngspice revision; no fake MOS model is accepted;
- Slow Charge Egress has not yet been transistor-sized in SKY130;
- recovery directionality/backflow protection at the real reservoir voltage must be closed;
- cell-type areas and parasitic loads are not yet measured for all roles;
- differentiated multi-cell reasoning quality is still model-level;
- literal 3-D face/edge/vertex active-cell manufacturing remains future-process.

## 11. Next — v13R4 Physical Slow-Egress Closure
Build a real differentiated pair with a deliberately weak post-expiry recovery device and close:
`DRC -> extraction -> aperture transient -> post-expiry egress transient -> reservoir ripple -> TT/FF/SS -> mismatch -> simultaneous communication+recovery -> area/parasitic comparison against a universal cell`.

If differentiation or slow recovery loses after real parasitics, coarsen/simplify it rather than preserving it for aesthetic reasons.
