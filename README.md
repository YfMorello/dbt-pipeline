# Offshore Wind Fleet Analytics (`offshore_wind_fleet`)

A local dbt + DuckDB project modeling offshore wind installation events, vessels, and weather logs.

## Seeds & Data
Generated via `generate_seeds.py` into `seeds/`[cite: 7]:
- `seed_vessels.csv`: Vessel metadata, crane capacity, and operational status[cite: 7]
- `seed_weather_logs.csv`: Daily wave height and wind speed logs by offshore site[cite: 7]
- `seed_installation_events.csv`: Component installation durations and project assignments[cite: 7]

## Running the Project
1. Install dependencies:
   ```bash
   pip install dbt-duckdb

Generate seed CSVs (if needed) and load them into DuckDB:

```bash
python generate_seeds.py
dbt seed


Verify profile, run transformations, and execute tests:
```bash
dbt debug
dbt run
dbt test

