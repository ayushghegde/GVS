# Current Next Experiment — v14N1 Seeded Junction Physical Closure

## Goal
Determine whether one simple seeded diffusive junction can move the v14M volatile firing delay into the <=38 ns hard target while preserving reversible nonvolatile OFF/WEAK/STRONG connection programming.

## Minimum stack first
1. Ag or limited-Ag top reservoir;
2. thin HfO2-class switching layer;
3. one sparse Ag nano-island/seed region that localizes the filament path;
4. Pt/TiN-class lower electrode.

Only add an Al2O3/Ni/nanoporous limiter if the simple stack fails endurance, self-compliance, or volatility.

## Required tests
- transient SET-delay distribution versus pulse voltage;
- volatile ON/OFF and recovery time;
- threshold/holding-voltage spread;
- leakage and false-fire probability;
- effect of seed placement/density on delay and variability;
- current self-limiting without one MOS per device;
- stronger program regime for reversible OFF/WEAK/STRONG retention;
- program energy, endurance, retention, and half-select disturbance;
- 2/3-copy link redundancy under device faults;
- SRT physical interconnect extraction to replace the current passive delay/attenuation proxy.

## Acceptance
Promote the seeded device only if the same simple stack has a credible path to:
- p95 volatile firing <=38 ns against the hardest v14M reference, with <=15 ns preferred;
- low enough event energy to keep the group EDP advantage;
- stable self-relaxation after firing;
- reversible nonvolatile connection states;
- no mandatory per-device MOS compliance element.

If speed closes but bimodal memory does not, keep the seeded device as sparse firing/regeneration junction and use a different two-terminal link material only if the total group is still better than CMOS.
