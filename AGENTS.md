# GVS agent rules

These rules apply to every AI/Codex agent working in this repository.

## Non-negotiable experiment persistence

An experiment is not finished until its reproducible record is written into this repository.

After every experiment, the agent must add or update an experiment directory under `experiments/` containing, when applicable:

- source netlist / circuit / code
- testbench or workload
- exact run command or runnable script
- simulator and tool versions
- PDK/model/corner selection
- configuration and random seeds
- raw or summarized measurements needed to reproduce the conclusion
- pass / partial-pass / fail status
- `REPORT.md` explaining: what happened, current problem, and what is next
- `manifest.json` listing the important files and provenance

The agent must not leave the only copy of experimental work in chat, temporary storage, `/tmp`, a notebook kernel, or an uncommitted working tree.

## Evidence and provenance

- Never invent missing historical results.
- Never label estimated parasitics as extracted-layout results.
- Preserve unsuccessful experiments when they teach something; mark them `FAIL` or `PARTIAL PASS` rather than deleting the evidence.
- Separate measured/simulated results from inference.
- Record architecture changes and the evidence that justified them.

## End-of-experiment procedure

Before reporting an experiment as complete:

1. Put its files in `experiments/<version-or-id>/`.
2. Run `python scripts/finalize_experiment.py experiments/<version-or-id>`.
3. Inspect the generated/updated `manifest.json`.
4. Commit the experiment files and manifest to the active branch.
5. In the final response, state the commit/branch and the next unresolved problem.

If GitHub write access is unavailable, package the full experiment directory and tell the user that repository persistence is the blocker. Do not claim the repository was updated.

## Current historical baseline

`v12S` is the preserved autonomous complete-tile schematic experiment. It is a **PARTIAL PASS** because the integrated SKY130 schematic lifecycle passed the recorded electrical tests, while real placed/routed RC extraction was not completed. The original supplied package is preserved in `artifacts/v12S/`.
