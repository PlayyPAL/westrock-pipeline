# Westrock Coffee ETL Pipeline

A Python data pipeline built to demonstrate ETL (Extract, Transform, Load) 
concepts using real-world coffee sales data scenarios.

## What It Does

- **Extract** – Ingests raw sales data simulating source system output
- **Transform** – Validates data integrity, handles missing values, 
  and calculates derived metrics
- **Load** – Outputs clean data to CSV for downstream use
- **Summarize** – Generates a business intelligence summary by region 
  and product

## Tech Stack

- Python 3
- Pandas

## How To Run

```bash
pip install pandas
python pipeline.py
```

## Output

- `westrock_sales_clean.csv` – Cleaned and validated dataset
- Terminal summary showing revenue by region, top product, 
  and average revenue per unit

## Why I Built This

Built as part of my preparation for a Data & AI Engineer role, 
to demonstrate understanding of data pipeline fundamentals that 
mirror what Palantir Foundry automates at enterprise scale.
