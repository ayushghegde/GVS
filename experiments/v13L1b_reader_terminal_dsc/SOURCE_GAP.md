# v13L1b reproducibility/source gap

The v13L branch preserves `experiments/v13A6_dual_pair_grammar_reader/physical/gen_reader_bodytied.py`, and the v13A6 report records that the selected reader is a real 0-DRC, body-tied, 10-MOS SKY130 layout with full RC PEX.

However, the generator instantiates four physical child cells by name:
- `nf_cross`
- `nf_reset`
- `pf_input`
- `pf_tail`

Those child `.mag` cells are not present in the current repository tree on the v13L branch. The physical directory currently contains only the generator script. The uploaded v12S tile archive also does not contain these v13A6 reader cells.

Therefore the exact selected 10-MOS reader cannot presently be regenerated from repository sources alone without reconstructing device-cell geometry. Reconstructing approximate replacements would violate the v13K/v13L rule not to alter already-selected good hardware merely to make a new experiment run.

## Decision
Do not fabricate substitute transistor subcells and call them the selected reader.

The reader-terminal DSC experiment is valid because it copies the GC/GR terminal dimensions exactly from the preserved selected generator and tests only service-routing coupling around those terminals. It is explicitly a pre-integration physical check, not full reader closure.

## Required recovery before complete v13L1b
Recover or re-preserve the exact four child Magic cells used by the selected v13A6 reader, plus the co-placed legal 10-MIM array source if available. Then run the existing `v13L1b Integrated Grammar + Neurovascular Slice` battery unchanged.
