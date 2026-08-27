#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
EXP="$ROOT/experiments/v13T3_physical_patch_gate"
RAW="$EXP/raw"
MAGIC_BIN="${MAGIC_BIN:-magic}"
SKY130_TECH="${SKY130_TECH:?set SKY130_TECH to sky130A.tech}"
cp "$ROOT/experiments/v13A6_dual_pair_grammar_reader/physical/recovered_2026-08-23/nf_reset.mag" "$RAW/nf_reset.mag"
(cd "$RAW"; printf ':load reserve_patch_boundary\n:drc check\n:drc count total\n:extract all\n:quit -noprompt\n' | "$MAGIC_BIN" -dnull -T "$SKY130_TECH") | tee "$RAW/reserve_patch_boundary.magic.log"
