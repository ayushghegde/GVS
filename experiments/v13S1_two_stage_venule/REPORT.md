# Neural Glyph v13S1 — Two-Stage Venous Charge Egress

**Verdict: MODEL PASS.** Replace one long slow cell-to-artery drain with two passive/weak stages: moderately slow `spent cell -> Local Venule`, then slower `Local Venule -> Charge Artery`. The reservoir and battery/collector hierarchy are retained.

**Local Venule:** a small shared post-expiry charge buffer serving a handful of nearby cells before the regional Charge Artery.

**Two-Stage Venous Egress:** dead state charge first leaves the cell on a moderate RC time constant, then the shared venule releases it more slowly toward the Charge Artery/reservoir.

The venule is never a live-information node. A cell may enter the venous path only after the information state is finished/isolated.

Selected model point: cell->venule tau ~2 local event intervals, venule->artery tau ~8, one slow venule outlet per 8 cells. These are model coordinates, not transistor constants.

Against a direct tau=8 cell-to-artery drain on identical expiry traces:
- only **1.83%** of spent cell charge remains after eight intervals in the first stage;
- peak artery inflow: uniform **2.57% lower**, bursty **19.30% lower**, aligned **28.29% lower**;
- peak regional reservoir occupancy: uniform **9.43% lower**, bursty **3.38% lower**, aligned **3.12% lower**;
- all modeled charge reaches the reservoir/battery window;
- one slow outlet per eight cells uses 32 outlets for 256 cells: **87.5% fewer slow-outlet copies** than one slow outlet per cell.

The eight-cell group reaches a worst selected local venule occupancy of ~6.33 normalized cell-charge units in aligned stress. Larger groups save more outlet copies but require larger local venules, so group size stays a physical compiler choice.

The regional reservoir is retained for buffering, decoupling, burst absorption, isolation from the larger battery/collector, fault containment and staged transfer. v13S inserts a smaller Local Venule before it; it does not replace it.

KEEP two-stage egress if physical leakage/timing closes. Do not add a scheduler; target implementation is fixed RC/device physics plus the existing expiry/isolation event.

Evidence boundary: normalized charge-flow model. No device leakage, real capacitance, battery chemistry or absolute recovered-energy claim.

Reproduce: `python3 experiments/v13S1_two_stage_venule/source/run_v13s1.py`
