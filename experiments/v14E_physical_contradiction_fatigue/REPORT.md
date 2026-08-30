# v14E Physical CFN Closure Report

## What happened
The final v14E CFN was reduced from 16 MOS to 15 MOS by deleting the regional-pressure clamp. That improved system behavior but removed parasitic capacitance that had helped prevent single-contradiction false triggers. The fatigue MIM was therefore increased from 2.4 x 2.4 um to 3.0 x 3.0 um. The actual regenerated Magic layout is 0 DRC and extracts 15 MOS + 2 MIM.

## Physical results
PEX PVT: 108/108 complete. Correct classifications: one 27/27 no-restart, two-nearby 27/27 restart, spaced 27/27 no-restart, confident 27/27 no-restart.

PEX mismatch: 192/192 complete. Correct classifications: one 48/48 no-restart, two-nearby 48/48 restart, spaced 48/48 no-restart, confident 48/48 no-restart.

TT extracted examples at 1.8 V: one qbar minimum ~1.025 V; two ~0.651 V; spaced ~1.025 V; confident ~1.220 V.

## System result
The pressure-clamped physical model was rejected (~80.31% resolution) because regional pressure suppressed most useful contradiction events. The selected unclamped physical-CFN semantics recover ~87.13% eventual resolution / ~64.51% on-time on the preserved 100-seed workload, compared with fixed4 ~78.56% / ~55.90%.

## Problem solved
The local restart trigger is now an actual physically specified volatile device rather than an abstract scheduler rule. Regional resource pressure and local reasoning correctness are separated.

## Next
Use v14E as the transistor-based physical baseline. The next experiment should challenge the assumption that every intelligent cell needs MOS switching at all, while keeping v14E as a fallback for restoration, confidence, and interfaces until a new device proves gain, selectivity, state retention, and cascadability.
