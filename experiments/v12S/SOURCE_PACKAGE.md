# v12S source package provenance

Authoritative user-supplied package inspected on 2026-08-20:

- file: `NEURAL_GLYPH_V12S_AUTONOMOUS_COMPLETE_TILE.zip`
- size: **463,106 bytes**
- SHA-256: `0ab940fa5cfe1ef850e2b1ea482c142203acd52be140df621f1a60b568a63878`
- ZIP entries: 15

The earlier GitHub archive at `artifacts/v12S/NEURAL_GLYPH_V12S_AUTONOMOUS_COMPLETE_TILE.zip` was only 26,007 bytes and was removed because it was not the full supplied package.

The canonical repository representation is the readable material under `experiments/v12S/`. Existing files were hash-checked against the supplied ZIP before being kept; missing compact files were restored from the ZIP.

Important source checksums:

- `v12s_complete_autonomous_tile.cir`: `8b4f7f26761abc169113c3198b77b1cb3a8259066f8fd9a6e4c645e67c2b0dd5`
- `v12s_complete_autonomous_tile_template.cir`: `638e53cb2f9a058a6de97655afc1f96f8d7030f5af57c192dc0feba265ee5a0c`
- original `agin_v12s_regions.csv`: `391bb3106973b800ba399b06e3dfa481942e65a429bb328600906d061a95d3b7`

The source ZIP also contains `agin_v12q_complete_query_log.csv` (3,439,698 bytes). That raw trace is substantially larger than the compact v12S result tables. Under the repository storage policy, large raw traces should only be committed when needed for a fresh reproduction or audit; summaries and source circuitry remain the normal permanent record.

Do not reconstruct historical measurements that are absent from the supplied source. The v12S verdict remains **PARTIAL PASS** because real placed/routed RC extraction was not completed.
