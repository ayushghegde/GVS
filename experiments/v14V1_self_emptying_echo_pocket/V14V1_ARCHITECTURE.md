# v14V1 Architecture — Self-Emptying Echo Pocket

## One-line idea
The winning guided-gap event temporarily moves a small fraction of the branch's existing mobile ions into a shallow side pocket; their electrostatic field lowers the perpendicular TEACH barrier, so the branch self-addresses without a transistor or second durable memory.

## Geometry concept

```text
                 GLOBAL TEACH
                     |
              program barrier
                     |
                 FIC / HZO
                     |
                     x  <- barrier region influenced by pocket field
                    /
         SEEP pocket o     (temporary ions)
                    \
INFERENCE ---- guided volatile gap ---- OUTPUT
```

**SEEP — Self-Emptying Echo Pocket:** a shallow ionic recess beside the crossing of inference and TEACH paths. It is part of the branch geometry, not a separate memory cell.

## Firing
1. The guided gap wins the local race.
2. The winner event moves mobile Ag through the inference gap.
3. Above a local event threshold, a small fraction enters the side pocket.
4. The pocket's ionic charge reduces the nearby program-barrier height.
5. No TEACH pulse exists yet, so HZO is not programmed.

## Teaching
1. Confirmation/contradiction is decided elsewhere.
2. A regional TEACH pulse arrives while the pocket is fresh.
3. The lowered barrier charges the FIC/HZO collar strongly enough to switch polarity.
4. Untouched branches retain a high barrier and see little internal HZO voltage.

## Forgetting
After inference, the pocket is no longer driven. Ions diffuse back toward the common mobile-ion reservoir. The local barrier returns to its OFF state. The temporary address disappears; only HZO polarity remains durable.

## Important correction from v14V
The old ~5000x conductance target was treated as a device property. v14V1 derives the requirement from the actual HZO capacitance and pulse: only ~13.4x fresh/stale separation is mathematically necessary; ~500–1000x is enough for practical variation margin from a ~1 Tohm OFF path.

## Failure rule
If the side pocket cannot produce a reproducible >=~0.2 eV transient barrier shift near 100 ns and self-empty by ~500 ns without permanent Ag trapping, reject v14V self-addressing and use v14U's sparse regional decoder. No per-branch MOS rescue.
