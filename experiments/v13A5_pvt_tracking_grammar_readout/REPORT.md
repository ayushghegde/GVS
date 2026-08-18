# Neural Glyph v13A5 — PVT-Tracking Grammar Evidence + Self-Checking Readout

**Verdict: PARTIAL PASS — the old fixed Grammar threshold problem is electrically solved with a legal-MIM ratio and robust self-check; full co-placed Grammar/readout layout PEX remains.**

## What happened

The v12N 3-step sound Grammar primitive was placed behind the physically extracted eight-way Regional Event Lease from v13A4.

The locality hardware did not materially attenuate the 0.2 V motif rails. At TT the old v12N values were reproduced closely:

- exact 3/3 motif: ~0.522191 V
- partial 2/3 motif: ~0.494794 V

But the newer real capacitor-corner screen exposed a problem hidden by the old fixed-capacitance model. At SS/85 C:

- exact: ~0.53044 V
- partial: ~0.50030 V

Therefore a fixed 0.500 V threshold can falsely accept a partial motif at the slow/high-capacitance corner.

This is an old Grammar decision-boundary problem, not a Regional Lease failure.

## Rejected fixes

### Fixed 0.5 V threshold
Rejected. It is not PVT tracking.

### 1x1 um fractional MIM reference
It worked numerically, but the current physical flow does not support it as the selected legal MIM primitive. Rejected rather than depending on an unsupported geometry.

### Unequal-total 3-MIM candidate / 6-MIM reference
This gave a large nominal margin, but attaching the real comparator gate capacitance moved candidate and reference common modes differently because their total capacitances were unequal. Rejected for direct readout.

### v12S-sized robust soma race
Correctness could be made good, but an honest VDD measurement showed picojoule-class/tens-of-pJ waste when analog nodes remained at intermediate voltages until cleanup. Rejected for Grammar readout.

### Very small regenerative latch
Shrinking the differential input pair too far reduced two-phase energy but produced wrong accepted decisions at the hardest ~11 mV evidence stress. Rejected.

## Selected physical-ratio network

Use only legal 2x2 um SKY130 M3 MIM devices and make candidate and reference have equal effective total capacitance.

### Candidate

- 3 full driven 2x2 MIM couplers
- one **physical series pair** of 2x2 MIMs to ground

Total physical MIM devices per candidate: **5**.

### Shared reference

- 2 full driven 2x2 MIM couplers
- one physical driven series pair of 2x2 MIMs
- 1 full 2x2 MIM to ground

Total shared reference MIM devices: **5**.

The reference is shared by multiple nearby Grammar candidates in one local group; it is not duplicated per candidate.

Because both candidate and reference use three full-MIM-equivalent loads plus one equal series-pair structure, comparator gate capacitance shifts both sides similarly instead of moving the threshold.

## Physical series-pair extraction

Two legal 2x2 um MIM devices were physically drawn with a real M4-to-M3 series connection in Magic/SKY130A.

- DRC errors: 0
- extracted devices: exactly two `sky130_fd_pr__cap_mim_m3_1`, each w=2 um, l=2 um
- extracted midpoint substrate/parasitic capacitance is nonzero, proving a real series pair is not an ideal C/2 element

Using the PDK low/typical/high intrinsic MIM values plus the extracted series geometry gives approximate effective source-to-output series coupling:

- cap-low: ~3.675 fF
- cap-typical: ~4.756 fF
- cap-high: ~5.856 fF

This physically measured fractional element is used in the ratio model; no ideal half-cap assumption is required.

## Direct comparator loading result

With actual SKY130 comparator input transistors attached from the start and candidate/reference nodes precharged together, nominal evidence margins are:

- TT exact: +27.25 mV; partial: -25.15 mV
- FF exact: +26.91 mV; partial: -24.31 mV
- SS exact: +27.44 mV; partial: -25.68 mV

So the old SS false-fire is removed without an absolute voltage threshold.

## Comparator: mixed-size regenerative latch D

Selected core:

- PFET tail: W=1 um, L=0.3 um
- PFET differential inputs: W=1 um, L=1 um
- cross-coupled NFETs: W=0.42 um, L=0.3 um
- output storage: 2 fF each

The input pair is deliberately not minimized; keeping its area controls offset. Energy-heavy regeneration/output nodes are smaller.

### Why two phases

One comparison alone can still be wrong if latch offset exceeds small analog evidence.

The selected self-check does:

1. candidate vs reference on the normal physical latch sides;
2. reset;
3. swap candidate/reference physical sides and compare again.

A valid decision must reverse physical latch polarity. Same-side preference or insufficient resolution is an **ambiguity/fallback**, never an accepted answer.

## Latch-D stress result before real swap switches

Evidence stresses: +/-31 mV, +/-18 mV, +/-11 mV; 4 mismatch launches at TT, FF and SS.

Total: **72 cases**.

- correct accepts: 65
- deliberate fallbacks: 7
- wrong accepts: **0**

At +/-31 mV and +/-18 mV: 48/48 accepted correctly.
At the deliberately harsh +/-11 mV boundary, some cases fell back instead of trusting offset-dominated evidence.

Two-phase latch energy in these short-window tests was roughly 46-51 fJ average depending evidence polarity/corner.

## Combined MIM mismatch + transistor mismatch

Using the real PDK MIM mismatch formula for independent 2x2 devices, the physical-series parasitic model, and SKY130 FET mismatch together:

48 candidate/reference cases (8 capacitor mismatch sets per corner x exact/partial) with ideal polarity swapping produced:

- correct: **48/48**
- fallback: 0
- wrong: 0

Evidence margins remained approximately:

- exact: +25.78 to +28.34 mV
- partial: -27.72 to -23.71 mV

## Real polarity-swap hardware

The ideal swap was then replaced with real minimum-size SKY130 NFET switches:

- 4 NFETs form the normal/crossed input swap matrix
- two small input-reset devices restore the latch input gates between phases
- two small output-reset devices clear the regenerative outputs

The shortest robust nominal window is **7 ns per phase**. Six ns remained marginal at FF; seven ns is the selected timing point.

### Real-swap mismatch screen

4 mismatch launches per TT/FF/SS corner, exact and partial = **24 cases** with capacitor mismatch and transistor mismatch active simultaneously.

- correct accepts: **22**
- deliberate fallbacks: **2**
- wrong accepts: **0**

The two fallbacks were useful detections, not wrong answers: one weak second-phase FF resolution and one SS case that preferred the same physical side after swapping.

## Honest readout energy

The selected 7 ns two-phase circuit was measured using actual V*I work for ramped control/event sources and constant-VDD charge for the latch.

| corner | exact total | partial total |
|---|---:|---:|
| TT | ~46.72 fJ | ~52.72 fJ |
| FF | ~33.43 fJ | ~39.50 fJ |
| SS | ~58.50 fJ | ~63.59 fJ |

The 0.2 V Grammar/reference evidence source work is only ~0.2-0.4 fJ. Swap/reset/tail control is ~1-2 fJ. The regenerative decision dominates.

## Architecture consequence

This corrects the old interpretation of Grammar energy.

A robust Grammar decision is **not** cheaper than the ~0.37-0.53 fJ warm/first-event static selector merely as a local selector replacement.

Therefore Grammar is retained only when it also removes a larger cost, for example:

- feature/motif-ID generation
- detailed downstream processing
- multiple long inter-island events
- repeated exact candidate work

For sound, one ~50 fJ local motif decision can still be very favorable if it avoids even one extra ~0.68 pJ long physical coordinate selection measured in v13A/P10.

The physical-cost-aware compiler must account for the robust readout, not only the capacitive recognition core.

## Electricity usage

The Grammar evidence and reference are **electrical memory/computation**: information is stored momentarily as charge ratios on physical capacitors.

The regenerative latch is powered by ordinary **VDD electrical energy**. No claim of free energy is made.

Charge recovery is not added to this ~50 fJ readout yet. Old v12I showed recovery is most worthwhile where discarded charge is large; here the first priority is avoiding unnecessary switching. Recovery should be added only if physical layout shows enough reusable charge to beat the extra recovery hardware.

## What is solved

- Regional Lease can carry real v12N sound Grammar inputs without blurring the motif rails.
- the real slow-cap corner exposes and invalidates the old absolute 0.5 V Grammar threshold.
- a PVT-tracking legal-MIM ratio removes that absolute threshold.
- physical series-pair parasitics are measured and included.
- direct comparator loading no longer moves the decision boundary when candidate/reference total capacitance is symmetric.
- two-phase polarity self-check converts large comparator offset into fallback rather than silent wrong output.
- real swap hardware remains tens-of-fJ and produced zero wrong accepts in the current combined mismatch screen.

## Remaining problem / next

This is still not a full physical Grammar-layout pass.

Next:

1. physically place one 5-MIM candidate and the 5-MIM shared reference compactly;
2. extract unintended MIM-to-MIM/wire coupling and verify the +/-25 mV-class ratio survives;
3. physically place the selected latch-D + swap/reset switches beside them;
4. full PEX of evidence -> ratio -> readout;
5. rerun PVT/mismatch;
6. place the block behind the selected eight-way Regional Lease;
7. measure area and full event energy;
8. only then decide whether occasional v11U-style slow offset calibration can safely reduce most events to a single comparison phase.

Do not replace the two-phase safe baseline with calibration until calibration proves zero wrong accepted decisions under drift/PVT/mismatch.