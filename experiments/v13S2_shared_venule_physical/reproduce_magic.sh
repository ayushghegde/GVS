#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
EXP="$ROOT/experiments/v13S2_shared_venule_physical"
RAW="$EXP/raw"
MAGIC_BIN="${MAGIC_BIN:-magic}"
SKY130_TECH="${SKY130_TECH:?set SKY130_TECH to sky130A.tech}"
cp "$ROOT/experiments/v13A6_dual_pair_grammar_reader/physical/recovered_2026-08-23/nf_reset.mag" "$RAW/nf_reset.mag"
for cell in venule8_near venule8_boundary; do
  (cd "$RAW"; printf ':load %s\n:drc check\n:drc count total\n:extract all\n:quit -noprompt\n' "$cell" | "$MAGIC_BIN" -dnull -T "$SKY130_TECH") | tee "$RAW/$cell.magic.log"
done
