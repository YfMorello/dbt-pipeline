# Offshore Wind Fleet Analytics (`offshore_wind_fleet`)

A local dbt + DuckDB project modeling offshore wind installation events, vessels, and weather logs.

## Seeds & Data
Generated via `generate_seeds.py` into `seeds/`:
- `seed_vessels.csv`: Vessel metadata, crane capacity, and operational status
- `seed_weather_logs.csv`: Daily wave height and wind speed logs by offshore site
- `seed_installation_events.csv`: Component installation durations and project assignments

## Running the Project
1. Install dependencies:
   ```bash
   pip install dbt-duckdb

   
