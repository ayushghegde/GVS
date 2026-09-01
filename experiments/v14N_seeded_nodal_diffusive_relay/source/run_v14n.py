import math, json
import numpy as np

SEED = 14014
rng = np.random.default_rng(SEED)

# Evidence boundary:
# Engineering sensitivity model for a seeded diffusive-junction + sparse-regeneration transport fabric.
# It is not a compact-model or fabricated-device simulation.

HOPS = 64
T0_PASSIVE_NS = 0.06
ALPHA = 0.018
TRIGGER_RATIO = 0.50
PASSIVE_ENERGY_FJ = 0.035
JUNCTION_ENERGY_FJ = 2.315
TRIALS = 10000


def lognormal(mean, cv, n):
    s2 = np.log(1.0 + cv * cv)
    s = np.sqrt(s2)
    mu = np.log(mean) - 0.5 * s2
    return rng.lognormal(mu, s, n)


def transport(spacing, junction_mean_ns=30.0, junction_cv=0.30):
    n = math.ceil(HOPS / spacing)
    lengths = [spacing] * (n - 1) + [HOPS - spacing * (n - 1)]
    success = 0
    delays = []
    for _ in range(TRIALS):
        d = 0.0
        ok = True
        for L in lengths:
            amp = math.exp(-ALPHA * L) * rng.normal(1.0, 0.05)
            if amp < TRIGGER_RATIO:
                ok = False
                break
            d += T0_PASSIVE_NS * L * L + float(lognormal(junction_mean_ns, junction_cv, 1)[0])
        if ok:
            success += 1
            delays.append(d)
    return {
        'spacing_hops': spacing,
        'regeneration_nodes': n,
        'success': success / TRIALS,
        'mean_delay_ns': float(np.mean(delays)) if delays else None,
        'p95_delay_ns': float(np.quantile(delays, 0.95)) if delays else None,
        'energy_fJ': HOPS * PASSIVE_ENERGY_FJ + n * JUNCTION_ENERGY_FJ,
    }


def delay_screen(baseline_mean_ns, multiplier, cv):
    vals = lognormal(baseline_mean_ns * multiplier, cv, 200000)
    return {
        'baseline_mean_ns': baseline_mean_ns,
        'delay_multiplier': multiplier,
        'target_mean_ns': baseline_mean_ns * multiplier,
        'cv': cv,
        'probability_at_or_below_38p5ns': float(np.mean(vals <= 38.5)),
        'p95_ns': float(np.quantile(vals, 0.95)),
    }


def distance_screen(baseline_ns, distance_ratio, exponent):
    return baseline_ns * (distance_ratio ** exponent)


def main():
    transport_rows = [transport(k) for k in range(1, 33)]
    robust = [r for r in transport_rows if r['success'] >= 0.999]
    selected = min(robust, key=lambda r: (r['mean_delay_ns'], r['energy_fJ']))

    delay_rows = []
    for baseline in (75.0, 55.0, 40.0):
        for mult in (1.0, 0.75, 0.67, 0.50):
            delay_rows.append(delay_screen(baseline, mult, 0.30 if mult == 1.0 else 0.15))

    path_rows = []
    for baseline in (55.0, 75.0):
        for ratio in (0.75, 0.50, 0.40):
            path_rows.append({
                'baseline_ns': baseline,
                'effective_ionic_distance_ratio': ratio,
                'linear_path_delay_ns': distance_screen(baseline, ratio, 1),
                'quadratic_field_drift_delay_ns': distance_screen(baseline, ratio, 2),
            })

    cmos_spacing = 4
    cmos_nodes = math.ceil(HOPS / cmos_spacing)
    cmos_delay_ns = cmos_nodes * 6.0 + cmos_nodes * T0_PASSIVE_NS * (cmos_spacing ** 2)
    cmos_energy_fJ = cmos_nodes * (5.0 * 1.8 * 1.8) + HOPS * PASSIVE_ENERGY_FJ

    out = {
        'schema': 'v14N-seeded-nodal-relay-v1',
        'evidence_boundary': 'Engineering sensitivity model; not a fabricated-device or transistor-layout comparison.',
        'selected_transport': selected,
        'transport_sweep': transport_rows,
        'seeded_delay_sensitivity': delay_rows,
        'ionic_distance_screen': path_rows,
        'favorable_cmos_transport_control': {
            'spacing_hops': cmos_spacing,
            'repeaters': cmos_nodes,
            'delay_ns': cmos_delay_ns,
            'energy_fJ': cmos_energy_fJ,
            'note': 'Control intentionally ignores SRAM/clock/decoder overhead and counts only repeater switching plus the same passive-link proxy.'
        },
        'decision': 'Keep two coupled ideas: pre-seeded/field-focused diffusive junctions to attack nucleation delay, and sparse regeneration only on physical transport trunks. Do not skip semantic decision nodes. Physical promotion requires measured/credible compact-model delay and energy for one stack.'
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
