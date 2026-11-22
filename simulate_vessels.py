import os
import random
import pandas as pd

os.makedirs("seeds", exist_ok=True)


def generate_valid_imo(rng: random.Random, used_imos: set[int]) -> int:
    """Generate a 7-digit number with a valid IMO check digit."""
    while True:
        base_digits = [rng.randint(0, 9) for _ in range(6)]
        if base_digits[0] == 0:
            base_digits[0] = rng.randint(1, 9)
        weights = [7, 6, 5, 4, 3, 2]
        check_digit = sum(d * w for d, w in zip(base_digits, weights)) % 10
        imo = int("".join(str(d) for d in base_digits + [check_digit]))
        if imo not in used_imos:
            used_imos.add(imo)
            return imo


def simulate_vessels(n_vessels: int = 6, seed: int = 42) -> pd.DataFrame:
    rng = random.Random(seed)
    used_imos: set[int] = set()

    name_pool = [
        "Wind Orca",
        "Wind Osprey",
        "Wind Scylla",
        "Wind Zaratan",
        "Brave Tern",
        "Bold Tern",
        "Sea Challenger",
        "Voltaire",
    ]
    rng.shuffle(name_pool)

    # Vessel classes: (label, crane_mean, crane_std, min_cap, max_cap)
    vessel_classes = [
        ("standard_wtiv", 1200.0, 120.0, 800, 1400),
        ("heavy_wtiv", 1800.0, 250.0, 1500, 2600),
        ("xl_wtiv", 2500.0, 300.0, 2200, 3200),
    ]
    class_weights = [0.45, 0.35, 0.20]

    statuses = ["Active", "Maintenance", "Mobilising"]
    status_weights = [0.70, 0.20, 0.10]

    rows = []
    for idx in range(n_vessels):
        vessel_id = 101 + idx
        vessel_name = name_pool[idx % len(name_pool)]
        if idx >= len(name_pool):
            vessel_name = f"{vessel_name} {idx + 1}"

        v_class = rng.choices(vessel_classes, weights=class_weights, k=1)[0]
        _, mean_cap, std_cap, min_cap, max_cap = v_class
        raw_cap = rng.gauss(mean_cap, std_cap)
        crane_cap = int(round(max(min_cap, min(max_cap, raw_cap)) / 50.0) * 50)

        status = rng.choices(statuses, weights=status_weights, k=1)[0]
        imo_number = generate_valid_imo(rng, used_imos)

        rows.append(
            {
                "vessel_id": vessel_id,
                "vessel_name": vessel_name,
                "imo_number": imo_number,
                "crane_capacity_tonnes": crane_cap,
                "status": status,
            }
        )

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df_vessels = simulate_vessels(n_vessels=6, seed=42)
    df_vessels.to_csv("seeds/seed_vessels.csv", index=False)
    print(df_vessels.to_string(index=False))
