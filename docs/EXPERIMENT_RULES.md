# GVS Experiment Rules

## Baseline

The baseline is the last **completed and validated** experiment before v11T. v11T is unfinished and must not be promoted to baseline status.

## Reproduction before modification

Before continuing development:

1. Recover exact baseline artifacts.
2. Run them unchanged.
3. Record NGSpice version, SKY130 model/corner, commands, inputs, outputs and pass/fail criteria.
4. Compare reproduced behavior with the historical baseline.
5. Investigate discrepancies before modifying the architecture.

## Evidence rule

Do not change the GVS architecture merely to make a simulation convenient. Changes require an observed failure, limitation, extraction result or other experimental evidence.

## Provenance

Every experiment should retain:

- source netlist
- testbench
- PDK/model selection
- simulator/tool versions
- exact run command
- generated measurements
- pass/fail result
- notes describing what changed from the preceding experiment

Generated or reconstructed data must never be labelled as historical measured data.

## Physical experiments

When physical layout work resumes, distinguish schematic simulation from extracted-layout simulation. An `extracted` result requires an actual layout and extraction flow; estimated parasitics are not an extracted-layout netlist.
