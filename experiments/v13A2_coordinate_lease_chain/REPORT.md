# Neural Glyph v13A2 — Coordinate Release -> Regional Event Lease

**Verdict: PARTIAL PASS — real SKY130 coordinate-release + physical lease handoff passes nominal and combined mismatch screens; fully co-placed physical extraction remains.**

## What problem this tests

v13A1 proved the Regional Event Lease by itself. That does not prove the upstream coordinate selector can charge it strongly enough once both threshold stacks and physical lease parasitics are present.

v13A2 therefore connects:

`ROWB/COLB -> 4T active-low coordinate release -> full-RC Regional Lease -> local 0.2 V events -> DONE clear`

The 4T coordinate cell uses two series PFETs to release PRE only when both active-low coordinate inputs are asserted, and two parallel NFETs to clamp PRE otherwise.

## Critical correctness invariant discovered

**Only validated local success may refresh the Regional Lease. Raw/noisy local events must never refresh it.**

An early negative-control bench incorrectly injected synthetic OK refresh pulses even when the coordinate was absent. That eventually charged the lease and was an invalid stimulus, not a circuit failure. The corrected bench disables OK refresh unless a real selected region has already produced validated local success.

This invariant is now part of the architecture.

## Nominal true-coordinate result

With the physical full-RC lease behind the 4T coordinate release:

- TT: PRE peak ~1.8056 V; WAKE at hop 12 ~1.1226 V; minimum event ~0.20022 V; PASS.
- FF: PRE peak ~1.8029 V; WAKE at hop 12 ~1.2040 V; minimum event ~0.20006 V; PASS.
- SS: PRE peak ~1.8088 V; WAKE at hop 12 ~1.0325 V; minimum event ~0.20012 V; PASS.

DONE clears the lease after the burst.

## Incomplete-coordinate result

At SS, with **no validated refresh**:

- row-only: PRE peak ~0.273 mV, WAKE peak ~0.461 mV, local OUT peak ~0.341 mV;
- column-only: PRE peak ~0.324 mV, WAKE peak ~0.461 mV, OUT ~0.341 mV;
- none: PRE essentially zero, WAKE ~0.461 mV, OUT ~0.341 mV;
- deliberately partial coordinate (one asserted input, the other only a 0.74 V excursion): PRE peak ~56.2 mV, WAKE ~0.417 mV, OUT ~0.340 mV.

None becomes a meaningful local 0.2 V event.

## Combined mismatch result

Mismatch is applied simultaneously to the coordinate-release transistors and lease transistors.

Four launches per corner: **12/12 PASS**.

Hop-12 WAKE values:

TT mismatch:
- 1.136934, 1.093305, 1.142902, 1.150359 V

FF mismatch:
- 1.242240, 1.217272, 1.168885, 1.178269 V

SS mismatch:
- 1.085855, 1.043934, 1.028184, **1.006024 V**

All local events remain essentially full 0.2 V and DONE still blocks the post-burst event.

## What this means

The coordinate-release threshold stack and the Regional Lease threshold stack can be chained without losing the 12-hop locality target. This is important because separate block-level passes could have hidden a combined slow-corner write-margin failure.

## What is still missing

The coordinate release and Regional Lease were simulated as a chained real-SKY130 schematic/PEX pair, but they have not yet been **co-placed and co-extracted as one physical cell**.

The next physical experiment should place the 4T active-low coordinate release directly beside the selected compact Regional Lease, route PRE physically, run DRC/extraction, and repeat:

1. true coordinate;
2. row-only;
3. column-only;
4. no coordinate;
5. partial-coordinate stress;
6. TT/FF/SS;
7. combined mismatch;
8. 12-hop refreshed burst;
9. DONE clear.

Only after that should the chain be treated as a physical locality interface.

## Full-v12S integration note

A separate attempt to insert the lease into the complete v12S lifecycle is currently **inconclusive because of simulator/model compatibility**, not because of an identified lease failure. The current Linux ngspice build cannot parse the newer continuous SKY130 model deck used by the historical combined v12S library. Under the stripped legacy model route, the unchanged v12S control misses the same route-latch timing as the lease-integrated version. Do not modify the solved v12S architecture to compensate for that tooling mismatch.
