# v13A selector-area trade screen

This is a candidate trade study, not a transistor-level accepted block.

## Question
Could many features share one binary selector tree if the active feature dynamically presents its static 4-5 configuration bits to the shared tree?

This extends the v12M event-gated shared-source idea, but unlike the selected v12M tree it would toggle the selector configuration controls on each event.

## Device-count proxy
Assume a conservative per-source control interface of `2 MOS per configuration bit + 1 event-access MOS`.

### Image, 16-way tree
- baseline: 64 independent 30-MOS trees = 1920 pass MOS
- 8 features/tree: ~816 MOS -> ~57.5% reduction
- 16 features/tree: ~696 MOS -> ~63.8% reduction
- 32 features/tree: ~636 MOS -> ~66.9% reduction
- 64 features/tree: ~606 MOS -> ~68.4% reduction

### Sound, 32-way tree
Comparison baseline is the v12M conservative 1x3/exceptions proxy of 12,074 pass MOS.

- 8 features/tree: ~9000 MOS -> ~25.5% reduction
- 16 features/tree: ~7140 MOS -> ~40.9% reduction
- 32 features/tree: ~6210 MOS -> ~48.6% reduction
- 64 features/tree: ~5776 MOS -> ~52.2% reduction
- one tree for 480 sources: ~5342 MOS -> ~55.8% reduction

## Why it is not the default
The v12M static tree's key advantage is that configuration does not move during an event.

A dynamic shared tree would charge/discharge many pass-gate control gates each event. Using the previously extracted representative gate-attachment load as a scale, even an optimistic minimum-size-gate range gives approximately:

- 16-way tree: order ~17-34 fJ of control-gate charge per random configuration change
- 32-way tree: order ~35-71 fJ

These are rough lower-bound estimates and exclude control mux wiring/driver energy.

That is still potentially below repeatedly reading 4-5 SRAM ID bits, but it is tens to >100x larger than the ~0.6 fJ static-tree event core measured in v12M.

## Decision
Do not replace the selected static tree with dynamic sharing in the normal efficiency mode.

Keep dynamic shared selector banks only as a later **area-constrained mode** if silicon footprint becomes more valuable than event energy.

Preferred normal architecture remains:

`stable assignment -> static binary selector`

`stable repeated local motif -> Grammar/direct template event`

`rare/changing/unusual case -> exact residual/fallback`

and all three should remain local to the island whenever possible.
