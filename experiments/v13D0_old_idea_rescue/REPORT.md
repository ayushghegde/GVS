# Neural Glyph v13D0 — Old-Idea Rescue Before New Routing

**Verdict: KEEP several old mechanisms that were previously easy to misread as rejected. v13D explicitly reuses the surviving physical principles rather than copying old failed implementations.**

## Why this exists

The v13C exclusion audit showed that many old failures were implementation failures, not principle failures. v13D therefore re-reads the preserved v11/v12 results before deciding how a new shared-wire/tap fabric should learn, compete and recover energy.

## Old results that directly change v13D

### v12E self-referenced repetition — recovered for fast tap training

Preserved data:

- TT after 1 validated firing: route-reference differential ~1.56 mV
- TT after 2: ~17.13 mV
- TT after 3: ~28.60 mV
- SS/85C after 1: ~1.30 mV
- after 2: ~16.80 mV
- after 3: ~28.16 mV
- tt_mm seed404 after 3: ~28.62 mV

The important consequence is that **three repeated validated uses naturally create a much stronger electrical familiarity signal than one or two uses**. This can be reused as a temporary tap-promotion signal instead of inventing a fresh digital reuse counter.

Selected rule: one or two events are probation; three tightly repeated validated events may enable a temporary local tap if the receiving electrical margin permits. Slow long-term promotion remains a separate lease/consolidation state.

### v12F electric homeostasis — recovered for wire/tap congestion

Preserved result:

- fixed threshold mean simultaneous firing: ~1.767 cells, p95 6, top-winner accuracy ~0.9593
- electric homeostat: mean ~1.429, p95 4, top-winner accuracy ~0.9707

This shows pooled electrical activity can suppress excess simultaneous participation without a software scheduler. v13D reuses the principle to limit how many analog taps may load one shared spine at once.

### v12G electrical context lifetime — recovered for short-lived route context

Preserved estimated ~10 mV context lifetime:

- FF ~5.36 ms
- TT ~5.22 ms
- SS ~4.93 ms

This is useful as a temporary routing/context timescale, not persistent structural memory.

### v12P lease — recovered for speculative routing rather than direct pass-gate drive

Two close reuses converged to about 0.58 V in the preserved transient screen. v13B3 already proved that ~1 V on the fourth-face NFET gate compressed a ~25 mV analog difference badly, so a ~0.58 V lease must **not** be asked to directly drive a high-fidelity pass gate.

Selected reuse: lease/familiarity changes *when/which path gets a head start* or writes a slow promotion state; a restored higher-voltage local gate drives the actual pass device after promotion.

### v12I expired-trace recovery — recovered after routing information is finished

Preserved full-PDK trace harvest:

- removed trace energy ~26.27-26.36 fJ
- recovered storage gain ~18.10-18.15 fJ
- capture fraction ~68.9% across TT/FF/SS

Selected rule remains:

`live charge = information -> temporary/ambiguous charge = local reuse -> expired charge = recovery`

### v11U/v12A replica sensing — recovered for heat/PVT self-management

A slow replica leak responds to process/temperature without being polluted by route activity. This is the correct way to let local heat/PVT change thresholds/retention autonomously.

## New v13D hierarchy

v13D will use old physics on different time scales:

1. **fast electricity** — event, evidence, familiarity, inhibition, immediate tap selection;
2. **medium electrical charge** — lease/use reservoir, temporary routing context, fatigue/homeostasis;
3. **slow environment physics** — replica leak/temperature changes promotion threshold and decay rate;
4. **rare consolidation** — exact verification may convert a repeatedly useful relation into a static Myelin/tap configuration;
5. **expired charge** — one-way recovery after it no longer carries information.

The goal is not to make every mechanism analog. The goal is to remove centralized bookkeeping when local physical state already contains the needed information.
