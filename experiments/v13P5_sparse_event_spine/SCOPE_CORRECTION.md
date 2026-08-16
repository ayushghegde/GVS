# SES scope correction

The original SES scaling model treated v12S `run`/`capture` as though those analog nodes might be extended across many Myelin edges. Re-reading the exact v12S tile showed that this is not supported by the preserved architecture: `run` and `capture` are local dynamic control nodes inside the complete tile, and their self-locking/cleanup behavior was already solved and stress-tested in v12S.

Therefore SES is **not adopted as a replacement for tile-local run/capture**.

The useful part of SES is retained only as a possible sparse **inter-tile event hierarchy**, now explored under v13P6 Glyph Tile Islands (GTI). The v12S local tile semantics remain unchanged.
