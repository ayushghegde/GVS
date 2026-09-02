# v14P Experiment Report — Polarized Trail Branch Selection

## What was tested

The user's charged-tip drawing was interpreted as a physical route-selection mechanism: several candidate branches leave a cell, and a learned local electrostatic field near each branch tip determines which guided-gap junction forms first.

The experiment progressed through four checks:
1. traffic-only vs feedback-gated trail learning;
2. monopole vs compensated/dipolar electrostatic trail and retention/relearning sensitivity;
3. direct integration of the trail field into the v14O guided-gap filament-formation race;
4. first-bridge quench timing and sparse hierarchical fanout.

All results are engineering sensitivity models, not fabricated-device measurements.

## 1. Learning rule

Use-only deposition failed: early random routes reinforce themselves. In the original six-way remap control, final accuracy remained ~20.3%.

Confirmation-only strengthening also failed to adapt cleanly because the old favorable trail remained: ~44.8% final remapped accuracy.

Reversible confirmation/contradiction trails reached 100% in that deterministic control.

Decision: usage creates eligibility only. Confirmation writes favorable polarization; contradiction reverses/neutralizes wrong polarization.

## 2. Polarized/dipole trail

A compensated positive/negative trail was kept instead of a bare net-charge patch. Point-charge electrostatic sanity calculations in k~20 dielectric give order-10-mV local shifts at a few nanometres, while the compensated field falls faster laterally.

A 70-mV-class barrier-shift proxy in the five-branch threshold model produced ~99.93% winner accuracy at 12-mV threshold sigma, with ~0.09% wrong-branch-above-threshold rate. This is a target window, not a measured trap voltage.

Relearning a changed route reached ~99.3% after four proper teaching encounters and 100% after eight in the selected sensitivity model.

## 3. Guided-gap integration

The electrostatic trail was then applied directly to v14O's field factor / bridge delay rather than a software routing score.

Selected five-branch race:
- correct first bridge: ~98.65%;
- correct with >=1 ns before the second branch: ~95.47%;
- target branch mean delay: ~8.06 ns;
- median first-to-second margin: ~4.03 ns.

Fanout:
- 4 branches ~99.11% correct first bridge;
- 5 ~98.65%;
- 8 ~97.61%;
- 12 ~96.47%;
- 16 ~94.60%.

Decision: ordinary cells should use small branch bundles, not dense local fanout.

## 4. Quench timing problem and fix

The first bridge cannot be assumed to suppress every competitor instantly. With v14O's ~2.3-Mohm modeled ON path, a large source-node capacitance would discharge too slowly.

A new tiny shared Choice Node was introduced only at the branch mouths.

At 1 fF, a 20% voltage reduction takes ~0.51 ns and stores only ~0.031 fJ at 0.25 V. In the race model:
- 4-way correct + quenched: ~98.15%;
- 5-way: ~97.52%.

At 0.5 fF those become ~98.67% and ~98.22% respectively.

This converts the next physical question into a clear layout target: can branch-mouth routing be extracted at <=1 fF?

## 5. Hierarchical fanout

Direct 16-way first-bridge probability was ~94.8%. Two independent 4-way stages give ~98.1% first-order winner probability. Therefore larger logical fanout should be built from small local choices / shared relay cells.

This is not permission to skip semantic transformations. It is a physical routing organization.

## 6. Retention / reconsolidation

The trail does not need infinite intrinsic retention if confirmed use refreshes the relation. Ten-year sensitivity examples:
- tau=1 y, monthly use: ~98.27% mean query accuracy;
- tau=2 y, 180-day use: ~95.34%;
- tau=5 y, yearly use: ~96.48%;
- tau=20 y, two-year use: ~98.19%.

Unused relations may fade and require relearning. No material retention value has yet been demonstrated.

## 7. Repeated structural change

Twelve sequential remap cycles, 20% of relations changed per cycle, 5% physical programming failure, 3% wrong feedback, and three corroborated updates gave at cycle 12:
- overall ~98.34%;
- currently changed ~97.65%;
- old route ~1.42%;
- never changed 100%.

The remaining error is dominated by bad/common-mode teaching and program faults, not an inability to reverse the field.

## Decision

KEEP v14P.

The preferred semantic branch is now:

`temporary cell excitation -> tiny choice node -> 4-5 v14O guided-gap candidate branches -> each branch surrounded by a reversible Polarized Trail Collar -> favored branch bridges first -> choice node quenches competitors -> next cell regenerates locally`.

This is a better interpretation of the charged-tip idea than permanently accumulating free positive charge on metal. It also removes the requirement that the main conductive filament itself must simultaneously be fast/volatile and long-retention/nonvolatile.

## Physical evidence still missing

v14P is not complete silicon. Missing gates are:
- actual polarizable/trap material and reversible barrier window;
- read disturb, retention, endurance, temperature and half-select behavior;
- complete programming energy/peripherals;
- physical layout/extraction of the branch collar and <=1 fF choice node;
- calibrated compact model coupling trail state to v14O bridge delay;
- group-level comparison with the best transistor reference after those parasitics/peripherals are counted.
