# GVS / Neural Glyph — START HERE

This folder is the continuity layer for future GVS work. Read it before proposing or changing architecture.

## Authoritative architecture

**Read `MAIN_ARCHITECTURE.md` first.** It is the single current integrated architecture and must be updated after every experiment that changes what the system keeps, rejects, or how the pieces connect. Versioned experiment folders remain evidence; they are not substitutes for the main architecture.

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
9. A rejected experiment must distinguish a rejected principle from a rejected implementation/mode/process.
10. After every experiment, update `MAIN_ARCHITECTURE.md` and `NEXT_EXPERIMENT.md`.

## Version-label warning
The recovered history contains a historical **v11T** section in the v11 master summary and the GitHub repository also contains `experiments/v11T_unfinished/`. Preserve both. Treat the label as ambiguous until provenance is reconciled; do not delete either and do not promote the repository unfinished checkpoint as a validated baseline.

## Current forward anchor
- Historical integrated schematic baseline: **v12S**.
- Physical continuation: v13P / v13A physical closure work.
- Framework/local-intelligence continuation: **v13E** on `experiment/v13E-main-architecture-autonomic-fabric`.

## Current architecture in one sentence
**Physicalize stable/reused structure locally; let electrical familiarity/leases/homeostasis configure local routes; use shared protected framework services and promoted paths for reuse; keep weak analog state local; move robust meaning farther; use exact hardware only where precision/change/ambiguity requires it.**

## Before any new experiment
Read, in order:
1. `MAIN_ARCHITECTURE.md`
2. `EXPERIMENT_LINEAGE.md`
3. `DECISION_LEDGER.md`
4. `DO_NOT_REINVENT.md`
5. `SOURCE_MAP.md`
6. `NEXT_EXPERIMENT.md`
