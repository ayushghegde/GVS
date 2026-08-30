# v14G — Goal-Echo Associative Reasoning Fabric Report

## What happened

The user clarified that transistors are not an allowed fallback inside the new semantic chip. v14G therefore changed the cost target: most semantic cells are passive, learned weights are sparse two-terminal links, and any active threshold/restoration device is sparse rather than one-per-cell.

The user's reasoning description was modeled directly. A query activates a learned goal pattern representing what must be found. Prompt/context cells co-fire. Similar episodes and learned relations receive evidence. A discovered value can activate the next relation, creating a physical association chain. A reciprocal Goal Echo biases the chain from the requested-answer side.

## Results

### Context and goal
- BANK context accuracy: 97.275% at 20% link variation; 82.875% at 40%.
- Learned goal-cell recognition (SUM/VALUE/CAUSE/LOCATION/FIX_CODE/WRITE_CODE/COMPARE/DEFINE): 99.4% at 20% link variation; 95.18% at 40%.
- Similar-episode recall: 98.43% at 20% variation; 89.43% at 40%.
- Toy code diagnosis->repair retrieval: 96.73% at 20% variation.

### Goal Echo versus forward-only routing
The ambiguous-path screen deliberately gives each hop one desired learned link and two plausible alternatives.

- depth 8, 10% variation: forward-only 34.66%; Goal Echo 99.98%.
- depth 8, 20% variation: forward-only 3.94%; Goal Echo 87.24%.
- depth 12, 20% variation: forward-only 0.78%; Goal Echo 74.98%.

Goal Echo is therefore retained. Deep reasoning cannot depend only on local strongest-edge selection because small per-hop errors multiply rapidly.

### Arithmetic limitation
When all value transitions are embodied, chained ADD/SUB/MUL relation lookup is exact in the synthetic table. However 216 deliberately withheld operation/value transitions are recovered 0% of the time. This is a real architecture limitation, not a tuning failure: association can compose known relations but does not manufacture an unseen exact relation.

### Passive depth and sparse restoration
A 64-hop event-level screen was run with device/line variation. One restoration junction every eight cells gives:

- 100% success at 0.94 nominal amplitude retention per hop;
- 98.85% at 0.92 retention per hop.

A restorer every four cells closes the full tested loss range, but doubles active-device density. The selected starting point is therefore one restoration site per eight cells, with four-cell spacing reserved for high-loss regions.

### Sparse connection capacity
Episode memory was stored only where cues actually co-fired. For 256 semantic cells, 128 cue cells and 1024 learned episodes, the model uses 8,192 links instead of 131,072 dense links (6.25% of dense connectivity) and recalls 98.87% of episodes at 20% link variation. With a 512-cue vocabulary, the same 1024 episodes use 1.56% of dense connectivity and achieve 100% in this synthetic screen.

## Hardware direction

Recent research makes a transistor-free weight/restoration layer physically plausible but not yet proven cheaper. A 2025 Nature Communications wafer-scale passive memristor platform reported >~95% average yield, CMOS-compatible processes without complex/high-temperature steps, 4F^2 passive crosspoints, and argued substantial density advantages over SRAM. Recent OTS selector research reports two-terminal devices with very high nonlinearity and endurance up to 2e9 cycles for selenium and approaching 1e10 cycles for some BEOL-compatible chalcogenides.

Those results justify continued experiments; they do **not** prove that a GVS TRJ or programmable link will be cheaper than mature transistors. v14G therefore uses a structural acceptance rule: no one-per-cell exotic active device, sparse restoration, sparse links, and later explicit write-energy/yield/process-cost accounting.

## Cost warning

The threshold-restorer energy sensitivity is severe. With 64 passive sites modeled as 10 fF at 0.2 V, the charge-state proxy is only ~12.8 fJ across the chain. Eight restoration events add:

- 80 fJ if each restorer costs 10 fJ;
- 800 fJ if each costs 100 fJ;
- 8 pJ if each costs 1 pJ.

Therefore a pJ-class restorer can dominate the architecture even when used sparsely. v14G does not accept a candidate TRJ merely because it has fewer terminals than a transistor.

## Decision

Keep the user's core mechanism, with two improvements:

1. reasoning is bidirectional: prompt evidence moves forward while the requested goal sends reciprocal compatibility evidence backward;
2. passive semantic cells dominate the fabric, while active restoration is sparse.

The next bottleneck is exact/generalizing operators. If a math/code relation has never been represented, pure association fails. v14G must therefore invent a transistor-free structural operator that applies a learned transformation to new values without a huge lookup table.
