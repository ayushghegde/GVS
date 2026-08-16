# v13P8 — Capacitive Membrane Receiver + Homeostatic Trim

**Status: PARTIAL PASS — analytical robustness screen passed; physical extraction/transient PVT still required**

## Why this experiment exists

This experiment does NOT replace any solved v12S tile-local behavior. v12S already solved local lease, VALID, Grammar/template evidence, Myelin competition, run/capture locking, recovery, invalidation and exact fallback at schematic transistor level.

The open scaling problem is inter-tile selection for GTI. v13P7 preferred a two-key MOS row/column receiver because an intentional-MIM capacitive receiver appeared area-expensive. This experiment revisits capacitance using sub-fF metal-overlap/fringe coupling and membrane/gate capacitance instead of a large MIM at every tile.

## Historical continuity

The design deliberately reuses established GVS ideas rather than inventing a separate architecture:

- membrane-like accumulation: several weak pieces of evidence sum before a local event;
- capacitive evidence: already used successfully in v12S template evidence;
- coordinates/grid: row + column select a local physical region;
- exact path as teacher: already used by v12S hierarchical rebuild;
- local adaptation: trim only local excitability, not model semantics.

## Capacitive coincidence model

Two equal address couplings `Cs` connect ROW and COLUMN events to a local membrane. The membrane has effective capacitance `Cm` to its reference, including sensing-gate and local physical capacitance.

For ideal simultaneous 0->VDD events:

- one event: `V1 = VDD * Cs / (Cm + 2*Cs)`
- two events: `V2 = VDD * 2*Cs / (Cm + 2*Cs)`

At VDD=1.8 V and `Cm/Cs = 1.65`:

- nominal one event = ~0.493 V
- nominal two events = ~0.986 V

This ratio was chosen because its discrimination window centers near the ~0.73 V nominal SKY130 1.8-V NFET threshold already recorded in the GTI screen.

## +/-20% capacitor-variation screen

Use independent +/-20% variation on both address couplings and membrane capacitance.

For `Cm/Cs = 1.65`:

- worst-case HIGH one-event membrane: ~0.651 V
- worst-case LOW two-event membrane: ~0.804 V
- guaranteed capacitor-only threshold window: ~153 mV
- window midpoint: ~0.728 V

So capacitor variation alone does not collapse the distinction.

## Homeostatic Membrane Calibration (HMC)

Raw transistor threshold still shifts with process, voltage, temperature and mismatch. Instead of adding a large precision comparator, use a tiny set of pre-placed membrane-capacitance trim states shared/configured per local cluster.

With the same +/-20% capacitor variation assumption, four ratios produce overlapping safe sensing-threshold bands:

| Cm/Cs | max one-event | min two-event | safe threshold band |
|---:|---:|---:|---:|
| 1.20 | 0.730 V | 0.947 V | 0.730-0.947 V |
| 1.50 | 0.675 V | 0.847 V | 0.675-0.847 V |
| 1.80 | 0.628 V | 0.766 V | 0.628-0.766 V |
| 2.10 | 0.587 V | 0.699 V | 0.587-0.699 V |

The union is continuous from about 0.587 V to 0.947 V.

For a nominal `Cs = 0.5 fF`, these states correspond to approximately `Cm = 0.60, 0.75, 0.90, 1.05 fF`. The required increments are only about 0.15 fF, suggesting controlled metal-overlap/fringe structures may be preferable to one large MIM per receiver.

A 2-bit cluster calibration can select one of four states. Calibration can use known ROW-only, COLUMN-only and ROW+COLUMN pulses. The exact controller chooses a trim state for which single pulses do not fire and coincident pulses do. This is analogous to homeostatic excitability adjustment and follows the existing GVS rule that exact behavior may teach a cheaper physical fast path.

## Why this may be cheaper than the two-key MOS receiver

Candidate implementation:

- two controlled sub-fF metal capacitive couplings;
- one sensing device / existing wake-sense interface;
- one small reset/bleed device if the existing lifecycle reset cannot be reused;
- cluster-shared 2-bit trim selection rather than large per-tile MIM capacitors.

The address trunks see only sub-fF coupling loads. At `Cs = 0.5 fF`, charging both intended coupling capacitors at 1.8 V stores only ~1.62 fJ total in the two capacitors (`C*V^2/2` each), excluding trunk energy and sensing/reset energy.

## Correctness rule

This membrane is only an inter-tile wake/address receiver. It must not replace v12S VALID, local competition, route locking or exact fallback. If calibration cannot find a safe state, that cluster must use the conventional MOS coincidence receiver / exact path rather than accepting an ambiguous membrane.

## Decision

KEEP as a candidate because:

- it directly matches older membrane/capacitive GVS ideas;
- it uses capacitance as computation rather than treating all capacitance as waste;
- the nominal and +/-20% analytical screens have a substantial one-vs-two event gap;
- 2-bit homeostatic trim provides overlapping threshold coverage without requiring a precision analog comparator;
- the expensive exact path remains the teacher/fallback.

DO NOT promote yet because:

- the sub-fF metal couplings have not yet been physically laid out/extracted at the target values;
- sensing-device TT/FF/SS/mismatch thresholds have not yet been overlaid on the four trim windows;
- leakage/retention/reset pulse-width behavior has not yet been simulated;
- cluster-to-cluster process correlation and local mismatch are unmeasured.

## Next experiment

1. Lay out two ~0.5 fF controlled metal-to-membrane coupling structures and four selectable membrane-capacitance states.
2. DRC + extraction in SKY130.
3. Measure actual Cs and Cm distributions from geometry.
4. Attach the smallest practical sensing/reset devices.
5. Run transient ROW-only, COLUMN-only, ROW+COLUMN and neighbor-crosstalk tests.
6. Run TT/FF/SS plus mismatch.
7. Compare area, trunk load, delay and energy against the v13P7 two-key MOS receiver.
8. Keep whichever receiver is cheaper and more robust; the rules are not rigid.
