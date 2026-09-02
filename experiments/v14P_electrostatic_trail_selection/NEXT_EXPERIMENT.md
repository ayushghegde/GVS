# Current Next Experiment — v14P5 Physical Polarized Trail Collar

## Goal
Close the first physical implementation of the v14P branch-selection primitive: a reversible local polarization/trapped-charge collar around a v14O guided-gap tip plus a <=1 fF shared choice node.

## Candidate structures — simplest first

Test in this order:
1. trap-rich HfO2-class sidewall/collar using the existing branch terminals;
2. HZO/ferroelectric collar if simple trapping cannot provide reversible retention/endurance;
3. ionic/electret collar only if it materially reduces write energy/peripheral cost.

Do not add a third transistor gate or per-branch selector merely to make programming easy.

## Required physical tests

1. Geometry/electrostatics: 3-D tip + collar field shift and neighboring-branch crosstalk.
2. Layout/extraction: physically realize the 4-5 branch mouth and show total Choice Node capacitance <=1 fF preferred (<=1.5 fF conditional).
3. Coupled transient model: calibrated trail state -> local gap field -> bridge delay -> first-branch quench.
4. Reversible states: favored / neutral / contradicted, including repeated polarity reversal.
5. Read disturb: large-equivalent inference pulse count.
6. Retention: with and without confirmation-driven reconsolidation.
7. Temperature / variation / endurance.
8. Half-select and neighboring-collar disturbance during local coincidence programming.
9. Complete program energy, rails and shared peripherals.
10. Group comparison against direct 16-way branching, v14O nonvolatile-filament weighting, v14J memcapacitive weighting and CMOS reference.

## Acceptance

Promote only if:
- 4-5-way physical winner >=99% or a small population-confidence/redundancy correction gives a net system win;
- choice-node extracted C <=1 fF preferred and first-bridge quench timing closes;
- ordinary inference does not materially rewrite the collar;
- changed routes can reverse in a few corroborated learning encounters;
- neighboring branch bias remains small enough for sparse routing;
- no per-branch MOS selector/compliance element in the semantic core;
- total learned-branch + programming infrastructure remains collectively cheaper/better than the transistor reference.

## Failure rule

If no simple collar material closes retention + reversibility + read-disturb cheaply, keep v14O volatile guided-gap firing and compare the best two-terminal long-term weight alternatives. Do not preserve the charged-tip idea at higher total cost merely because it is biologically suggestive.
