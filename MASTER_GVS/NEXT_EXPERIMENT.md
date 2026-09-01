# Current Next Experiment — v14O1 Guided-Gap Physical Closure

## Goal
Determine whether the simple GG-SLDJ geometry can physically deliver the v14O speed/current/memory window without hidden transistor support.

## First structure
Keep it simple:
- Ag or thin Ag-alloy active reservoir/electrode;
- ~4 nm HfO2-class switching layer;
- inert Pt/TiN/W-class conductive spine/nanotip rising through most of the dielectric;
- target ~1.3 nm remaining dynamic switching gap;
- passive high-resistance neck/electrode segment targeting ~2.2 Mohm intrinsic ballast;
- Pt/TiN-class bottom routing electrode.

## Required physical/model tests
1. Build an electrostatic/ionic compact sensitivity model in which gap length and tip field enhancement are explicit rather than represented only by the current heuristic.
2. Measure/obtain a credible delay distribution versus pulse amplitude, gap length, and temperature; target mean 10–15 ns, p95 <=15 ns preferred, p95 <=38.5 ns mandatory.
3. Quantify actual OFF leakage and spontaneous-bridge probability. The v14O relative gap-hazard proxy is not signoff evidence.
4. Verify intrinsic ballast across process/temperature: target firing-current window roughly 50–200 nA without per-junction MOS compliance.
5. Verify volatile bridge self-relaxation and refractory time.
6. On the same device geometry, test reversible nonvolatile OFF/WEAK/STRONG states and whether ballast prevents useful programming.
7. Test local differential coincidence programming including half-select stress, accumulated subthreshold disturb, and three-evidence provisional consolidation.
8. Count fabrication difficulty of the spine/gap definition; reject if it requires such expensive nanolithography/alignment that the group no longer beats the transistor baseline.
9. If learned-link mode and firing mode cannot share the same geometry, compare a seeded firing junction + separate two-terminal plastic link against v14L and CMOS at whole-system level.

## Acceptance
Promote only if the complete group remains transistor-free in the semantic core and has a credible route to beat the favorable CMOS controls in energy-delay plus process/area cost. Do not preserve one-device purity if the guided gap requires impractical fabrication.
