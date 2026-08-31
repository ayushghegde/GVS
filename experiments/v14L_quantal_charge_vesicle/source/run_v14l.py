#!/usr/bin/env python3
import math, random, statistics, json
from pathlib import Path

C_WEAK_FF = 2.73685
C_STRONG_FF = 9.34526
C_MEM_FF = 2 * C_STRONG_FF
BASE = dict(vbase=0.60, vth=0.80, vreset=0.15, dv_source=0.65,
            tau_ns=100.0, dt_ns=5.0, release_fail=0.01)

def cascade(seed, nweak, nstrong, layers=8, width=64):
    rng = random.Random(seed)
    active = [True] * width
    layer_active = []
    link_energy = replenish_energy = 0.0
    fires = width
    for _ in range(1, layers):
        nxt = []
        for _cell in range(width):
            cm = C_MEM_FF * max(0.75, rng.gauss(1.0, 0.05))
            vb = BASE['vbase'] + rng.gauss(0.0, 0.01)
            vt = BASE['vth'] * max(0.85, rng.gauss(1.0, 0.025))
            tau = BASE['tau_ns'] * max(0.5, rng.gauss(1.0, 0.20))
            dvs = BASE['dv_source'] * max(0.85, rng.gauss(1.0, 0.03))
            links = []
            for nominal, count in ((C_WEAK_FF, nweak), (C_STRONG_FF, nstrong)):
                for _ in range(count):
                    links.append((rng.randrange(width), nominal * max(0.7, rng.gauss(1.0, 0.05))))
            ctotal = cm + sum(c for _, c in links)
            rng.shuffle(links)
            v = vb
            for parent, cap in links:
                if active[parent] and rng.random() >= BASE['release_fail']:
                    v = vb + (v - vb) * math.exp(-BASE['dt_ns'] / tau)
                    v += (cap / ctotal) * dvs
                    link_energy += 0.5 * cap * dvs * dvs
            fired = v >= vt
            nxt.append(fired)
            if fired:
                fires += 1
                replenish_energy += cm * vb * max(0.0, vb - BASE['vreset'])
        active = nxt
        layer_active.append(sum(active) / width)
    return layer_active, link_energy, replenish_energy, fires

def summarize(nweak, nstrong, trials=500):
    runs = [cascade(900000 + nweak*10000 + nstrong*100 + i, nweak, nstrong) for i in range(trials)]
    finals = sorted(r[0][-1] for r in runs)
    p05 = finals[max(0, int(0.05*len(finals))-1)]
    mean_link = statistics.mean(r[1] for r in runs)
    mean_replenish = statistics.mean(r[2] for r in runs)
    mean_fires = statistics.mean(r[3] for r in runs)
    return {
        'weak_links': nweak, 'strong_links': nstrong, 'trials': trials,
        'mean_active_fraction_by_layer': [statistics.mean(r[0][i] for r in runs) for i in range(7)],
        'mean_final_active_fraction': statistics.mean(r[0][-1] for r in runs),
        'p05_final_active_fraction': p05,
        'min_final_active_fraction': min(r[0][-1] for r in runs),
        'mean_link_energy_fJ': mean_link,
        'mean_replenishment_energy_fJ': mean_replenish,
        'mean_fires': mean_fires,
        'common_energy_per_fire_fJ': (mean_link + mean_replenish) / mean_fires,
    }

def passive_fanout():
    v = BASE['vth']
    return {str(k): v/(k+1) for k in range(1, 9)}

def false_idle(trials=1_000_000):
    rng = random.Random(99)
    bad = 0
    for _ in range(trials):
        vb = BASE['vbase'] + rng.gauss(0.0, 0.01)
        vt = BASE['vth'] * max(0.85, rng.gauss(1.0, 0.025))
        bad += vb >= vt
    return {'trials': trials, 'false_fires': bad, 'observed_probability': bad/trials}

def break_even(common):
    vdd = 1.8
    out = []
    for c_logic in (5, 10, 20, 40):
        e_cmos = common + c_logic*vdd*vdd
        for e_release in (1, 5, 10, 20, 40):
            e_v14l = common + e_release
            out.append({
                'cmos_effective_control_cap_fF': c_logic,
                'release_switch_energy_fJ': e_release,
                'v14l_energy_per_fire_fJ': e_v14l,
                'cmos_reference_energy_per_fire_fJ': e_cmos,
                'v14l_energy_ratio': e_v14l/e_cmos,
                'max_release_delay_ns_for_equal_EDP_vs_6ns_cmos': 6.0*e_cmos/e_v14l,
            })
    return out

def main():
    six_one = summarize(6,1)
    four_two = summarize(4,2)
    result = {
        'schema': 'v14L-quantal-charge-vesicle-v1',
        'evidence_boundary': 'Synthetic charge-sharing/variation model using v14J extracted SKY130 MIM capacitance proxies; threshold switch is not yet a fabricated GVS device.',
        'capacitance_basis': {'weak_link_fF': C_WEAK_FF, 'strong_link_fF': C_STRONG_FF, 'membrane_fF': C_MEM_FF},
        'bias_and_threshold': BASE,
        'passive_single_reservoir_fanout_voltage_V': passive_fanout(),
        'idle_false_fire_screen': false_idle(),
        'cascade_6weak_1strong': six_one,
        'cascade_4weak_2strong': four_two,
        'energy_break_even': break_even(six_one['common_energy_per_fire_fJ']),
        'conclusion': 'Reject passive one-capacitor fanout. Keep locally regenerated, pre-biased leaky capacitive packet cells. Physical promotion requires a volatile release element whose switching energy/speed/process cost keeps whole-system energy and EDP below the transistor reference.'
    }
    out = Path(__file__).resolve().parents[1] / 'results' / 'KEY_RESULTS.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
