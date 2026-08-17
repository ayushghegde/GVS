# Current Next Experiment — Regional Wake Trace

## Why this is next
v13A showed that the hybrid architecture remains efficient only when multiple low-level operations happen locally per long-distance event. The missing physical primitive is a cheap way to remember "this region is already selected" for a short burst.

This is not a new AI architecture. It is a local communication-state primitive around existing Grammar/template/Myelin/v12S mechanisms.

## Target behavior
One global coordinate pulse selects a region. A tiny local charge state then keeps the region available while several useful local events occur. The state leaks/reset clears naturally after inactivity.

Required locality targets from v13A 4x routing stress:
- image: >=3 local motif events
- raw sound: >=3 local events, or one 3-step Grammar motif
- code: >=2 AST motifs
- reasoning: >=4 hops

Stretch target for harsh routing cost:
- reasoning: hold through all 12 hops when the path is hot/repeated

## Candidate circuit direction
Reuse old Glyph mechanisms rather than a counter/register:
- coordinate-release event deposits charge on a small local wake/lease capacitor;
- a weak leak sets natural decay;
- local events may refresh the state only if that does not create sticky false selection;
- local enable drives only robust/full-swing boundary nodes, not tiny dendrites directly;
- invalidation/error/fallback must not depend on the wake trace.

## Acceptance battery
1. one true coordinate opens local region
2. row-only / column-only / no coordinate cannot open it
3. safe orthogonal-wire crosstalk cannot open it
4. region remains enabled long enough for required burst
5. inactivity clears it
6. a different coordinate cannot inherit stale wake
7. error/invalidation still forces exact fallback
8. TT / FF / SS
9. mismatch screen
10. extracted layout parasitics
11. compare energy saved by avoided long selections against wake-trace area/energy

## Reject conditions
- requires a large digital counter/scheduler just to amortize communication
- stays sticky across unrelated events
- adds more energy than the long selections it saves
- loads sensitive local dendrites/run/capture nodes
- creates a new correctness dependency for exact fallback
