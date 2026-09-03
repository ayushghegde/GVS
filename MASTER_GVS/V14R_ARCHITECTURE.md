# Neural Glyph v14R — Polarity-Guided Choice Cell

**Status:** current transistor-replacement cell candidate; PARTIAL PASS at architecture/model level. The five-way Choice Node is physically extracted in SKY130 metal and passes the capacitance target. The HZO polarity collar and v14O guided-gap device remain uncalibrated/unfabricated as one compound branch.

## Cell primitive

**PGCC — Polarity-Guided Choice Cell:** a semantic cell whose outgoing learned connections are 4–5 two-terminal **PGDB** branches attached to one tiny shared metal node.

**PGDB — Polarity-Guided Diffusive Branch:** an integrated two-terminal connection combining the v14O guided volatile gap/inert spine/passive ballast with a local reversible electric-polarity collar. The collar stores route preference; the volatile gap performs transient firing.

```
input events -> tiny Choice Node -> 4–5 PGDB candidates -> next cells
                                  ^
                                  |
                       polarity chooses first bridge
```

## Why this version exists

v14R stops adding independent neuron-like parts and instead asks which earlier v14 mechanisms can occupy the same physical branch.

KEEP:
- v14O guided-gap volatile firing;
- v14O passive self-compliance/ballast target;
- v14P reversible local electric polarity;
- v14P 4–5-way physical competition;
- v14K confirmation/contradiction and provisional corroboration;
- v14Q eligibility only as a shallow state co-located in the polarity collar.

DROP from the ordinary PGCC:
- literal magnetic attraction/self-electromagnet programming;
- intentional membrane capacitor;
- separate volatile-release switch;
- separate per-branch MOS selector/compliance device;
- forcing the same filament to provide both nanosecond volatility and long-term memory;
- standalone UET storage hardware.

## Physical Choice Node result

A legal five-way metal2 SKY130 branch-mouth proxy was generated with Magic using the supplied SKY130A technology.

- DRC errors: 0
- CHOICE self/substrate term: 112.362 aF
- five CHOICE-to-branch couplings: 7.95455 aF each
- represented total CHOICE loading: 152.13475 aF = 0.152135 fF

This closes the old v14P <=1 fF preferred metal-node target with substantial margin.

Five estimated 10x10x5 nm, k=25 collars add ~22.14 aF, giving a combined model node of ~0.17427 fF. With inherited v14O R_ON~2.3 Mohm, a 20% collapse is ~0.0894 ns and stored node energy at 0.25 V is ~0.00545 fJ. Only the metal capacitance is extracted; collar capacitance and R_ON remain model quantities.

## Polarity material direction

Preferred first candidate: 5–6 nm Hf0.5Zr0.5O2 (HZO) ferroelectric collar with its edge deliberately exposed to the guided gap so the dipole fringe field is useful rather than fully screened inside a conventional capacitor.

A 10x10 nm patch at P=0.16 C/m2 contains ~100e of bound polarization charge. The v14P branch-race target was around +10e effective favorable bias and -3e contradicted bias.

Finite square-dipole-sheet geometry screens show that a 7.5 nm patch at P=0.16 C/m2, 1 nm from the gap, has a pre-metal-screening fringe envelope ~0.419 V. The inherited nominal target trail shift is ~0.159 V. Therefore the next 3-D device model must retain roughly >=38% of this geometry envelope for that case. Higher-P or closer/larger collars relax this requirement.

## Five-way race with physical node loading

At the current model point:

- ~10% effective bound-charge fraction -> ~98.49% correct + quenched;
- ~12.5% -> ~99.40%;
- ~15% -> ~99.73%;
- ~20% -> ~99.92%.

Selected device target: >=12.5% effective-charge-equivalent coupling, >=15% preferred.

## Inference/program separation

Inference target: ~0.25 V.

Learning candidate:

`+0.6 V endpoint A + (-0.6 V endpoint B) -> ~1.2 V selected differential`

Half-selected branches should see <=~0.6 V. This is chosen because ultrathin HZO literature reports coercive/operation voltages around the ~1 V scale. It is not yet proven safe against cumulative half-select disturb.

## Eligibility decision

v14Q's temporary usage trace is retained only if the same collar naturally supplies a shallow/fast-relaxing state. It may scale the magnitude of a confirmed programming event but must not become direct route truth.

Current remap sensitivity:
- baseline recovery: 84.375 encounters;
- UET recovery: 55.25;
- improvement: ~34.5%;
- final mean accuracy remains ~99.99% in the normal-error screen.

At high incorrect-feedback rates UET magnifies errors, so v14K-style corroboration remains mandatory for uncertain updates.

## One-cell functional flow

### Inference
1. incoming connection(s) excite CHOICE;
2. all outgoing PGDBs receive the same drive;
3. collar polarity shifts local gap barriers;
4. favored branch bridges first;
5. its conductive path discharges CHOICE rapidly;
6. competitors are quenched;
7. bridge dissolves/relaxes; persistent collar state remains.

### Learning
1. use creates optional shallow eligibility;
2. confirmed evidence identifies the relation;
3. bipolar coincidence applies full differential only to that branch;
4. favorable confirmation sets one polarization; contradiction reverses it;
5. unconfirmed traffic never becomes permanent truth.

## Current blocker

The remaining blocker is not the Choice Node. It is the real two-terminal compound PGDB device:

- post-screening HZO fringe field;
- read disturb;
- half-select disturb;
- reversible switching variation/endurance;
- compatibility of the ferroelectric collar with the diffusive guided-gap stack;
- actual device energy and area.

Do not call v14R a complete physical transistor replacement until those close.
