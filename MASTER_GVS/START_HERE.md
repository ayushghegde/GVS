# GVS / Neural Glyph — START HERE

This folder is the continuity layer for future GVS work. Read it before proposing or changing architecture.

## Primary goal
Build the cheapest practical AI hardware that can still become highly capable/intelligent. The architecture may mix analog, event-driven, digital, memory, software, or new hardware. Rules are flexible; experiments decide what stays.

## Working principle
Do not choose "brain-like" or "computer-like" in advance.

- Stable, reused structure should move toward physical computation when it saves memory traffic/energy/area.
- Exact, rapidly changing, arithmetic, address/state-critical work should remain exact computer-like hardware when that is cheaper or safer.
- Ambiguity or detected failure escalates to the exact path.
- Temporary history/hotness can live as charge when that removes bookkeeping.
- Long-distance communication is expensive: perform several useful operations locally and move high-level meaning, not every raw event.
- Shared/regional resources are preferred when they remove duplicated hardware without coupling local decisions incorrectly.

## Evidence rules
1. Never rewrite or delete old experiments to make the story cleaner.
2. A failed experiment is useful evidence and stays recorded.
3. Distinguish measured PDK/SPICE/layout results from models/proxies.
4. Never call synthetic RC "extracted layout".
5. Never call a partial/mismatch screen fabrication yield.
6. Do not change a proven local mechanism unless a new measured problem justifies it.
7. Before inventing a fix, search the older Glyph experiments for an existing mechanism.
8. New ideas are welcome, but keep them only if they beat the current choice on the relevant combination of correctness, intelligence, energy, area, latency, programmability and cost.

## Version-label warning
The recovered history contains a historical **v11T** section in the v11 master summary and the GitHub repository also contains `experiments/v11T_unfinished/`. Preserve both. Treat the label as ambiguous until provenance is reconciled; do not delete either and do not promote the repository unfinished checkpoint as a validated baseline.

## Current forward anchor
- Historical integrated schematic baseline: **v12S** (PARTIAL PASS because full placed/routed extraction was originally missing).
- Physical continuation: **v13P0 onward** on `experiment/v13P0-physical-rc`.
- Hybrid/system continuation: **v13A physical-cost-aware locality compiler**.

## Current architecture in one sentence
**Physicalize stable/reused structure locally; keep exact/changeable work exact; let leases/ambiguity/fallback move work between the two; communicate high-level events between local regions rather than every synapse/event.**

## Before any new experiment
Read, in order:
1. `ARCHITECTURE_NOW.md`
2. `EXPERIMENT_LINEAGE.md`
3. `DECISION_LEDGER.md`
4. `DO_NOT_REINVENT.md`
5. `SOURCE_MAP.md`
6. `NEXT_EXPERIMENT.md`
