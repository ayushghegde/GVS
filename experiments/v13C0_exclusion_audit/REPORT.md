# v13C0 — Exclusion Audit / Recoverable Ideas

**Verdict: 29 distinct explicitly rejected/not-default idea families are visible in the current master Decision Ledger + Do-Not-Reinvent audit after merging obvious duplicates. Several are not dead principles; only their tested implementation was rejected. v13C therefore separates `principle rejected` from `implementation rejected` so useful old electricity/feedback/recovery ideas are not lost again.**

## Why v13C starts here

The current architecture accidentally risks treating an old failed implementation as if the underlying physical idea were forbidden. The clearest example is electricity reuse: an always-active stored-leak implementation was rejected in v11S because it became sticky, but later v11U/v11V/v11W/v12I retained the useful principle using replica sensing, one-way collection, and post-information recovery.

## Audit count

The two master audit files contain 22 `Rejected / not default` entries in `DECISION_LEDGER.md` and 16 `Known false starts / rejected ideas` in `DO_NOT_REINVENT.md`. After merging clear overlaps (for example fixed weak leak, one-hot selector, naive decoder, unisolated shared sensory source, Grammar-everywhere/all-vision, low-margin analog latch, HVT-varactor recovery, and naive global low-level communication), the audit contains **29 distinct rejected/not-default idea families**.

This is a conservative count of explicit master-file entries, not every failed transistor/layout variant in every experiment.

## Reclassification

### A. Underlying principle still useful; tested implementation failed

Examples:

1. **stored leak electricity** — always-active v11S storage was too sticky; gated/replica PVT memory and later recovery remain useful;
2. **weak-leak control** — fixed bias failed PVT; self-threshold/replica-controlled leak survived;
3. **energy recovery** — too-small reservoir or per-tiny-reader recovery can disturb computation; shared one-way recovery remains useful;
4. **analog context** — tiny ~5-11 mV latch decisions were unsafe; higher-margin direct analog steering + exact fallback remains useful;
5. **shared inhibition** — passive pooled inhibition was too weak; active shared interneuron hierarchy survived;
6. **Grammar** — Grammar everywhere/forced vision was bad; selective low-entropy motifs remain useful;
7. **global communication** — broadcasting every low-level event is bad; robust high-level long routing remains necessary;
8. **3D** — exotic 3D as a baseline dependency was rejected; targeted vertical/shared-framework structures remain useful if measured cheaper;
9. **dynamic selector sharing** — rejected as normal mode; still useful under severe area constraints;
10. **small aggressive capacitance** — particular 1x1 MIM/reference choices were not legal/robust in current SKY130; a future custom 3D wall capacitor is not logically forbidden if its own PDK supports it;
11. **charge recovery near readout** — rejected before proving benefit on a ~50 fJ reader; framework-scale shared cleanup/recovery is still open;
12. **route self-configuration** — raw/noisy refresh is rejected, but validated-use charge can configure a lease/contact/Myelin relation.

### B. Keep rejected unless fundamentally new evidence appears

- exact arithmetic implemented as approximate analog neural dynamics when a small exact ALU/rule is cheaper;
- brain-only long reasoning with no exact fallback;
- continuous conductive sharing that destroys independent state/selectivity;
- DRC-only physical acceptance without extracted connectivity;
- fixed absolute 0.500 V Grammar threshold across real capacitor corners;
- unequal-total candidate/reference networks that move with reader load;
- long-lived mid-rail soma race as a normal Grammar reader;
- letting raw/noisy activity train persistent physical routing;
- carrying tiny high-impedance analog evidence across a long die-to-die interface.

## New v13C rule

Every rejected result must be tagged as one of:

- `PRINCIPLE_REJECTED` — the underlying idea loses to a better representation for the tested need;
- `IMPLEMENTATION_REJECTED` — the physical mechanism is still useful but this sizing/topology/control failed;
- `MODE_ONLY` — useful only under a workload/area/margin condition;
- `FUTURE_PROCESS` — unavailable or uneconomic in current SKY130, not physically forbidden.

This prevents a later experiment from accidentally throwing away the useful part of an older result.
