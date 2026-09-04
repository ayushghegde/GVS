# Neural Glyph v15D — Charge-Gradient Dendritic Memory

**Status: PARTIAL PHYSICS PASS — FITA REJECTED; CHARGE-GRADIENT DUAL-TIME MEMORY SELECTED FOR CUSTOM-DEVICE COUPON.**

## What happened
v15D directly tested the user-proposed rule: a fired axon can reach many dendrites, but dendrites carrying more positive charge should be more likely to win; repeated validated use should accumulate charge; unused/wrong charge should decay; durable memory should emerge only after repeated use.

The first implementation failed. It assumed only eight replays and a weak charge field. Selected HZO reached only ~0.874 V, the intended dendrite won only ~70.6%, and only ~4.5% of replay bursts reached the consolidation target. The failure is preserved in `results/results.json`.

The design was then changed rather than forcing the tunnel solution back in.

## Selected v15D mechanism
### DCG — Dendritic Charge Gradient
A validated firing event leaves a tiny **signed charge residue** on the existing dendrite/HZO collar. Positive residue favors the route; negative residue suppresses it. Repeated use adds residues faster than they leak. A one-off event leaks away.

### DTM — Dual-Time Memory
The same HZO collar holds two timescales:
- **fast state:** free/ionic electrode charge, leaky and easy to forget;
- **slow state:** HZO ferroelectric polarization, created only after enough repeated charge has accumulated.

No extra memory device is added.

### NBR — Need-Based Replay
Unknown, low-margin, or mismatch states cause the existing path fabric to replay candidate routes. Known high-margin routes do not replay. This is behavior of the network, not a consciousness module or software learner block.

### SBR — Spare Branch Recruitment
The accepted four-active/two-repair branch structure is retained. Persistent topology mismatch can recruit a spare. **Correction carried forward into v15E:** an unknown concept is not a hardware fault and must not by itself trigger a chip-change request. A maker-facing hardware revision request is reserved for persistent measured physical faults such as leakage, timing, thermal, or exhausted-repair margin.

## Why FITA/tunnel is removed
FITA was introduced only to create a branch-specific programming path to HZO. v15D no longer needs that path. The branch's own signed charge accumulation becomes the learning variable, and HZO gradually consolidates that charge into slow polarity.

Therefore the selected v15D architecture has:
- no FITA tunnel anchor;
- no orthogonal Ag program path;
- no per-branch MOS selector;
- no high-voltage row/column learning decoder.

## Actual ngspice results
A headless ngspice build was compiled from the supplied source and used for transient tests.

### Charge accumulation
With a 24 aF HZO capacitance, 20 aF local parasitic, 120 GΩ leakage, and a residual capture pulse of 4 nA × 1 ns per replay:
- 1 replay: **0.0901 V**
- 4 replays: **0.3503 V**
- 8 replays: **0.6750 V**
- 12 replays: **0.9761 V**
- 14 replays: **1.1183 V**
- after burst, 5 µs: **0.5602 V**
- after burst, 10 µs: **0.2173 V**

A single wrong event decays from ~0.0902 V to **0.0353 V at 5 µs** and **0.0137 V at 10 µs**.

### Charged dendrite current preference
A compact exponential guided-gap circuit gives the selected charged dendrite about **270.4×** the current of the next branch at the measured corner.

## Coupled free-charge ↔ HZO result
The Python model includes:
- actual free electrode charge;
- HZO dielectric capacitance;
- HZO remanent polarization charge (hundreds of elementary charges for this collar size);
- seven distributed HZO domains with NLS/Merz-like kinetics;
- leakage that automatically screens persistent polarization;
- positive and negative replay residues.

### New positive knowledge — 24 positive replays
Final slow polarization quantiles:
- p0.1: **0.613**
- p1: **0.686**
- median: **0.924**
- p99: **0.99994**

### One wrong event
Median durable polarization change is effectively zero (~1e-9). Even the p99.9 tail is only ~0.0018.

### Changed definition — 26 negative replays against an old +0.70 path
Final polarization quantiles:
- p0.1: **-0.997**
- p1: **-0.949**
- median: **-0.515**
- p99: **-0.138**
- p99.9: **-0.045**

So the old route is neutralized/reversed across the modeled tail rather than remaining a permanent wrong path.

## Choice result
300,000-trial stochastic guided-gap selection:
- correct branch: **99.9937%**
- spare-branch false wins are extremely rare;
- selection is driven by HZO polarity field plus exponential guided-gap nucleation and the inherited ballast/quench behavior.

## Need-based system result
256 relations / 650 episodes:
- accuracy on committed answerable relations: **100%**;
- changed-definition accuracy: **100%**;
- unresolved answerable relations: **0**;
- wrong-path traces remaining: **0**;
- durable consolidation events: **127**;
- positive internal replay events used for consolidation: **3,048**;
- negative replay events used for redefinition: **1,326**;
- untrusted teaching attempts blocked: **139,057**;
- three deliberately impossible local topologies remained unresolved. The old run counted these as 3 hardware-change requests; **that interpretation is rejected in v15E**. They should remain knowledge/topology unknowns unless independent physical-health evidence shows the chip itself is faulty.

## Energy
The original compact model used ~22.5 elementary charges per replay. A later guided-gap sample-and-hold follow-up (folded into v15E) replaced that fixed assumption with event-derived Q=C·V and found a median ~33 electrons, with ~99.45% of 500,000 modeled events capturing at least 15 electrons. At ~0.5 V its direct local charge-capture energy proxy is tiny compared with the inherited ~1.9056 fJ replay/inference event. A 24-replay learning burst therefore costs mainly the replays themselves (~45.7 fJ proxy), not a high-voltage HZO program network.

The hollow Charge Return Skin remains useful for shared supply decoupling/recovery, but v15D no longer requires it to distribute a 1.2 V HZO program pulse to every branch.

## What is physically extracted vs modeled
**Actual software this run:** ngspice transient charge/decay and compact branch-choice circuits; Python/NumPy coupled free-charge/HZO-domain and system behavior models.

**Inherited physical extraction:** v15C Magic/SKY130 regional mesh passed DRC=0 and extracted ~263.385 fF. v15D no longer requires that mesh for high-voltage programming.

**Still not fabrication proof:** the exact signed residual charge left by a real guided-gap firing event; microsecond fast-charge leakage; charge-to-guided-gap field coupling; analog partial-HZO retention; intrinsic Ag deep-trap endurance.

## Problem remaining
The old v15C problems — FITA tunnel breakdown and an orthogonal Ag learning path — are removed from the selected architecture.

The new physical question is narrower:

> Can a fabricated guided-gap/collar reproduce the event-derived **tens-of-electrons** sample-and-hold charge packet and its microsecond leakage envelope, while repeated charge produces the modeled analog HZO polarization floor?

If a real coupon cannot retain that small signed residue, DCG should be rejected and GVS falls back to v15C/v14U. Do not add per-branch MOS merely to save v15D.
