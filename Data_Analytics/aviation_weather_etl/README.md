# Aviation Weather ETL (KNHK)

## Project Overview
This project is an end to end data pipeline that ingests aviation weather data (METAR) for NAS Patuxent River (Station **KNHK**). The pipeline will evolve in phases to demonstrate ETL, validation, orchestration, database design, dashboards, and predictive modeling.

---

## Current Phase 0: Bootstrap
- Project scaffold with folders ('data/', 'db/', 'src/',etc.)
- Virtual environment + requirements
- Logging and configuration system
- Placeholder pipeline entrypoint ('src/pipeline.py')

**Next Phase:** Implement data ingestion to fetch METAR data from NOAA's API.

---

## Repository Layout

aviation_weather_etl/
├── data/
│ ├── raw/ # raw snapshots (ignored by Git)
│ ├── interim/ # intermediate CSVs
│ └── processed/ # final cleaned outputs
├── db/ # database schema & migrations
├── logs/ # pipeline log files
├── notebooks/ # Jupyter exploration/EDA
├── src/ # pipeline source code
│ ├── config.py # loads settings from .env
│ └── pipeline.py # entrypoint (Phase 0 stub)
├── tests/ # pytest unit tests
├── requirements.txt # project dependencies
├── .env.example # template config file
└── README.md # project overview

---

## Setup Instructions
```bash
# 1. Clone repo
git clone https://github.com/TechComa/TechComa-Portfolio.git
cd TechComa-Portfolio/Data_Analytics/aviation_weather_etl

# 2. Create virtual environment
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
# or .venv\Scripts\Activate.ps1 # Windows PowerShell

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run bootstrap pipeline
python src/pipeline.py

---

## Roadmap For Project

Phase 0: Bootstrap (scaffold, logging, config)

Phase 1: Ingest + Transform METAR data

Phase 2: Load to SQLite/Postgres

Phase 3: Orchestration & Scheduling (Prefect)

Phase 4: Interactive Dashboard (Streamlit)

Phase 5: Data Quality Layer (Great Expectations)

Phase 6: Predictive Model (IFR risk / forecast accuracy)