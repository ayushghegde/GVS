# v15G — Cooperative Deliberation + Context Modulation Field

Status: **PARTIAL PASS**

## What happened

v15FG had three interpretation/closure problems:

1. The optical screen was incorrectly tied to literal voltage/value examples. In v15G, voltage is only an electrical implementation detail. The screen carries a temporary normalized analog working-state vector for at least 1 us.
2. Same-model collaboration was previously modeled as answer-then-compare. v15G replaces that with cooperative deliberation: two branches of the same model share the original prompt and an evolving transcript, alternating extensions, reframes, corrections, and synthesis.
3. Direct named “emotion” variables were too close to action commands. v15G replaces them with diffuse Context Modulation Fields inspired by the general brain principle of neuromodulation: fields change gain, replay/attention budget, commitment margin, and later plasticity, but do not name or force an action.

## Experiment A — calibrated 8-dot partial-thought screen

The screen transports an arbitrary 8-dimensional normalized fragment, not decimal digits and not “5 V = 5”. A factory/static per-dot calibration is combined with one reference dot and one black/dark reference. The source state is held >=1 us.

500,000-trial result:

- RMSE < 5%: **99.9246%**
- worst-dot absolute error < 12%: **99.9952%**
- median RMSE: ~**1.63%**
- p99 RMSE: ~**3.79%**
- median message-energy proxy: ~**4.44 pJ**

The first uncalibrated v15G screen failed badly and is preserved in the run history. Calibration was therefore accepted as necessary.

Fresh ngspice was not rerun because the binary from the earlier v15FG session was no longer present in this runtime. The v15FG screen circuit remains inherited real-ngspice evidence; v15G changes semantic encoding/calibration, not the detector RC principle. A fresh v15G SPICE deck is included for rerun.

## Experiment B — cooperative same-model deliberation

Protocol:

- same model weights;
- same original prompt and inherited context;
- separate inference state/sampling path;
- one shared evolving transcript;
- A contributes a partial line of reasoning;
- B reads it and extends/reframes/repairs it;
- A continues from the new transcript;
- final synthesis occurs after the discussion, not before;
- no majority vote is required.

250,000 latent-reasoning trials at equal eight-pass compute:

- single context: **93.5152%**
- cooperative dialogue: **98.4340%**
- gain in this protocol model: **+4.9188 percentage points**
- deliberately identical inference trajectory: **93.5152%** (no gain)
- high-sycophancy control: **92.3380%** (worse than single)

This is not a live GPT benchmark. The runtime cannot instantiate two independent GPT-5.6 Sol conversations. The purpose is to test the collaboration rule and failure modes.

## Experiment C — brain-principle context modulation

Rejected design: “emotion” directly adds action biases. That reduced the behavioral proxy from 76.6266% to 75.8303% and changed ~7.43% of actions simply because of the injected state.

Selected design: diffuse Context Modulation Fields:

- **salience**: importance/novelty gain;
- **uncertainty**: requests more replay/internal observation and raises commitment caution;
- **signed outcome**: changes later dendrite reinforcement/depression, not the current answer;
- **urgency**: changes how much time/energy can be spent deliberating.

These fields are bounded and do not target a particular action. They decide *how to process*, not *what conclusion to output*.

350,000 trials:

- baseline evidence-only proxy: **76.6266%**
- rejected action-coded affect: **75.8303%**
- selected context-field proxy: **87.8094%**
- extra reasoning requested: **72.5586%**
- mean extra observations: **1.4401**

The improvement comes from allocating extra observation/replay to uncertain/salient states, not from an “emotion bit” choosing an action.

## Architecture decision

Keep:

- v15D signed free dendrite charge;
- natural charge decay;
- HZO slow consolidation;
- guided-gap firing;
- 4 active + 2 repair branches;
- unknown state;
- hardware-revision request only for persistent physical faults;
- hollow/shared-power infrastructure.

Reject/supersede:

- literal voltage-to-number interpretation of screen dots;
- answer-then-compare self-dialogue;
- emotion-as-command/action-logit injection.

## Problem remaining

Two things cannot be physically/live closed in this environment:

1. the optical screen still needs a fabricated package coupon to measure actual emitter/detector calibration drift, scattering, crosstalk, and aging;
2. the cooperative-dialogue protocol needs a real A/B with two live sessions of the same model. If real contexts remain too correlated or become sycophantic, the mode should turn itself off.

## What is next

v15G1 should not invent a new cell. It should:

1. run a real two-session same-model collaborative benchmark when the product/runtime exposes two independent inference contexts;
2. build a calibrated 8-dot optical package coupon and compare measured reconstruction error/energy with electrical transport;
3. integrate Context Modulation Fields with the v15D charge/HZO learning simulator so signed outcome changes plasticity and uncertainty changes replay demand in the same physical network.
