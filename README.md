# Kenya Job Market Dashboard

A real-time analytics pipeline that scrapes, stores, and visualizes trends in the Kenyan job market.

## Architecture

```
┌───────────┐    ┌───────────┐    ┌──────────┐    ┌──────────┐
│  Scraper  │───▶│ Storage   │───▶│   dbt    │───▶│ Superset │
│ (Python)  │    │ (Postgres)│    │ (Models) │    │ Dashbrd  │
└───────────┘    └───────────┘    └──────────┘    └──────────┘
```

## Project Structure

```
job-market-dashboard/
├── scraper/                # Job listing scrapers
├── ingestion/              # Data pipeline orchestration
├── storage/                # Database/MinIO interactions
├── dbt_project/            # Analytics modelling
├── dashboard/              # Superset configuration
└── docker-compose.yml      # Infrastructure setup
```

## Features

- **Automated Scraping:** Scheduled ingestion of job market data from popular local job boards.
- **Robust Storage:** Postgres-based backend for structured data persistence.
- **Advanced Modelling:** dbt-driven transformations for trend analysis.
- **Interactive Dashboards:** Apache Superset visualizations for market insights.

## Quickstart

### 1. Setup
```bash
# Start infrastructure
docker compose up -d

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Pipeline
```bash
# Run scraper
python scraper/brightermondayscraper.py

# Transform data
cd dbt_project && dbt run
```

## License
MIT

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python/Scrapy | Data Scraping |
| PostgreSQL | Storage |
| dbt | Transformation |
| Apache Superset | Visualization |

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python/Scrapy | Data Scraping |
| PostgreSQL | Storage |
| dbt | Transformation |
| Apache Superset | Visualization |
