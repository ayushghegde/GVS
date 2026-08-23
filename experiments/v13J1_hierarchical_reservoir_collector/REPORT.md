# Neural Glyph v13J1 — Hierarchical Reservoir Collector

**Verdict: KEEP, but collect only after local state expires and batch the chip-level transfer. The local reservoirs remain part of computation; recovery is a second lifecycle stage, not a replacement for them.**

## New terms
- **Hierarchical Reservoir Collector (HRC):** local reservoirs do their normal lease/context/familiarity/adaptation job; after expiry, one-way recovery valves move remaining charge into regional rails, which later batch-transfer energy into a shared chip-level reservoir.
- **Recovery Valve:** one-way controlled switch that stays off while a reservoir still carries useful state and opens only after capture/expiry.
- **Roof Reservoir Array (RRA):** distributed exterior/top/backside recovery/decoupling bank so a thin chip can drain nearby rather than sending every expired charge packet to one distant internal capacitor.

## 1. Preserve the old v11/v12 principle
The reservoir must not be removed merely because energy recovery exists.

Selected lifecycle:

`LIVE reservoir charge -> information / threshold / lease / familiarity / adaptation`

`controlled leak -> time/environment/self-regulation`

`decision captured + state expired -> Recovery Valve opens`

`regional recovery rail -> batch -> chip-level reservoir / low-voltage supply`

Raw activity still cannot refresh leases or train persistent routes.

## 2. Why not connect every live reservoir directly to one big chip capacitor?
A shared rail is a load. If it is connected while the local node is still high-impedance information, it changes the very voltage that is doing the computation.

Therefore the central collector is electrically isolated from live state. This keeps the earlier v12I rule: use the charge as information first, recover it only afterward.

## 3. Scale input from the closed v13E recovery bench
Use the preserved v13E tap-gate recovery numbers only as a proxy:
- energy removed from one expired tap/configuration state ~2.85 fJ;
- energy reaching the local/regional low-voltage rail ~1.51 fJ;
- local recovery fraction ~53% in that specific bench.

These are not universal reservoir numbers; they are the current measured/model reference for aggregation.

## 4. Chip-level batching screen
After local recovery, assume a shared second-stage transfer with 90% efficiency. Test fixed activation/control overheads of 10, 50 and 100 fJ per batch.

### 64 expired reservoirs
- 10 fJ overhead -> net ~76.98 fJ at chip level, ~42.2% of original removed energy;
- 50 fJ -> ~36.98 fJ, ~20.3%;
- 100 fJ -> no positive net recovery.

### 256 expired reservoirs
- 10 fJ -> ~337.9 fJ net, ~46.3%;
- 50 fJ -> ~297.9 fJ, ~40.8%;
- 100 fJ -> ~247.9 fJ, ~34.0%.

### 1024 expired reservoirs
- 10 fJ -> ~1381.6 fJ net, ~47.3%;
- 50 fJ -> ~1341.6 fJ, ~46.0%;
- 100 fJ -> ~1291.6 fJ, ~44.3%.

The theoretical large-batch ceiling of this two-stage proxy is roughly the local ~53% recovery multiplied by 90% second-stage efficiency, or ~47.7%, before fixed overhead.

## 5. Main result
A chip-level collector is useful only when **aggregation is large enough**. A 100 fJ transfer overhead is absurd for a batch of eight tiny reservoirs but becomes tolerable across hundreds/thousands of expiries.

This supports a hierarchy analogous to the thermal system:

`many tiny local sources -> regional collector -> one larger chip/package collector`

not

`one converter/harvester attached to every cell`.

## 6. Exterior-bank geometry
Illustrative 10 x 10 x 2 mm, 4x4x2 region model:
- average region-center distance to one central internal collector ~5.5 mm;
- average distance to nearest top/bottom exterior face ~0.5 mm.

A distributed Roof Reservoir Array therefore gives very short local drain paths in a thin package. This is a geometry argument, not a claim that an optimized internal distributed rail could not match it.

## 7. What the recovered energy should power
Prefer low-voltage shared support that naturally matches the recovered rail:
- slow familiarity/use-state support;
- lease refresh assistance where physically compatible;
- configuration/status logic;
- sensor/reference support;
- recharge of recovery reservoirs through a proper converter.

Do not directly claim recovered low-voltage charge can recreate arbitrary VDD-level energy without conversion loss.

## 8. Fault / isolation rule
One failed or shorted recovery branch must not discharge every live reservoir. Use branch isolation so the chip-level reservoir is downstream of one-way valves and regional collectors.

## 9. Decision
### KEEP
- local reservoirs for their original computational job;
- post-expiry one-way recovery;
- regional collection before chip-level conversion;
- distributed exterior recovery/decoupling banks on thin packages;
- batch activation so conversion overhead is amortized.

### REJECT
- harvesting from live information state;
- one active converter per tiny reservoir;
- assuming aggregation itself creates energy;
- forcing chip-level recovery when the batch is too small to repay control/conversion overhead.

## 10. Rule
`reservoir computes first -> expires -> regional collection -> batch threshold -> chip-level recovery`.
