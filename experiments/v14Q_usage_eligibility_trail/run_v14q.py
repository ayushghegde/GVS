#!/usr/bin/env python3
import json, math, random, statistics

MU0 = 4 * math.pi * 1e-7
V_BRANCH = 0.25
R_ON = 2.3e6
I_BRANCH = V_BRANCH / R_ON


def magnetic_scale():
    field_uT = {}
    for r_nm in (5, 10, 20, 50):
        r = r_nm * 1e-9
        B = MU0 * I_BRANCH / (2 * math.pi * r)
        field_uT[str(r_nm)] = B * 1e6
    required = {}
    for B_mT in (0.1, 1, 10, 50):
        B = B_mT * 1e-3
        r = 10e-9
        I = B * 2 * math.pi * r / MU0
        required[str(B_mT)] = {"current_A": I, "multiple_of_branch_current": I / I_BRANCH}
    return field_uT, required


def run_one(seed, use_gain=True, rounds=3000, change_at=1200, feedback_p=0.12):
    rng = random.Random(seed)
    n = 5
    target = 0
    p = [0.0] * n
    e = [0.0] * n
    correct = []
    recovery = None

    for t in range(rounds):
        if t == change_at:
            target = 3

        ex = [math.exp(4 * x) for x in p]
        total = sum(ex)
        probs = [x / total for x in ex]
        u = rng.random()
        acc = 0.0
        chosen = 0
        for j, q in enumerate(probs):
            acc += q
            if u <= acc:
                chosen = j
                break

        for j in range(n):
            e[j] *= 0.94
        e[chosen] = min(1.0, e[chosen] + 0.22)

        if rng.random() < feedback_p:
            if chosen == target:
                mult = (1 + 1.5 * e[chosen]) if use_gain else 1.0
                p[chosen] = min(1.0, p[chosen] + 0.10 * mult)
                for j in range(n):
                    if j != chosen:
                        p[j] = max(-1.0, p[j] - 0.015)
            else:
                mult = (1 + 1.0 * e[chosen]) if use_gain else 1.0
                p[chosen] = max(-1.0, p[chosen] - 0.12 * mult)
                p[target] = min(1.0, p[target] + 0.03)

        correct.append(chosen == target)
        if t > change_at + 100 and recovery is None and sum(correct[-100:]) / 100 >= 0.90:
            recovery = t - change_at

    return recovery or (rounds - change_at), sum(correct[-500:]) / 500


def rc_envelope():
    eps0 = 8.8541878128e-12
    k = 20.0
    area = 10e-9 * 10e-9
    t = 5e-9
    C = eps0 * k * area / t
    energy = 0.5 * C * V_BRANCH * V_BRANCH
    retention = {}
    for tau_s in (1e-6, 1e-3, 1.0):
        retention[str(tau_s)] = {"required_R_ohm": tau_s / C, "V_over_R_A": V_BRANCH / (tau_s / C)}
    return {"capacitance_F": C, "stored_energy_J_at_0p25V": energy, "retention": retention}


def main():
    fields, required = magnetic_scale()
    out = {
        "experiment": "v14Q_usage_eligibility_trail",
        "status": "PARTIAL PASS",
        "model_only": True,
        "branch_operating_point": {"V": V_BRANCH, "R_on_ohm": R_ON, "I_A": I_BRANCH},
        "magnetic_field_uT_at_radius_nm": fields,
        "required_current_at_10nm": required,
        "rc_geometry_envelope": rc_envelope(),
        "learning": {}
    }

    for name, mode in (("baseline_no_eligibility", False), ("usage_eligibility", True)):
        vals = [run_one(seed, mode) for seed in range(200)]
        recoveries = [x[0] for x in vals]
        accuracies = [x[1] for x in vals]
        out["learning"][name] = {
            "seeds": 200,
            "mean_recovery_encounters": statistics.mean(recoveries),
            "median_recovery_encounters": statistics.median(recoveries),
            "mean_final_500_accuracy": statistics.mean(accuracies)
        }

    b = out["learning"]["baseline_no_eligibility"]["mean_recovery_encounters"]
    q = out["learning"]["usage_eligibility"]["mean_recovery_encounters"]
    out["learning"]["recovery_improvement_fraction"] = (b - q) / b
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
