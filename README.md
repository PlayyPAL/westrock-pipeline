# Westrock Coffee ETL Pipeline

A Python data pipeline built to demonstrate ETL (Extract, Transform, Load) 
concepts using real-world coffee sales data scenarios relevant to 
Westrock Coffee's international operations.

## What It Does

- **Extract** – Ingests raw sales data simulating source system output
- **Extract** – Pulls live USD to MYR exchange rates from a REST API
- **Transform** – Validates data integrity, handles missing values, 
  and calculates derived metrics including international revenue conversion
- **Load** – Outputs clean data to CSV for downstream use
- **Summarize** – Generates business intelligence summary by region 
  and product

## Tech Stack

- Python 3
- Pandas
- Requests

## How To Run

```bash
pip install pandas requests
python pipeline.py
```

## Output

- `westrock_sales_clean.csv` - Cleaned and validated dataset
- Terminal summary showing revenue by region, top product, 
  total revenue, and Malaysian Ringgit conversions using live exchange rates

## Why I Built This

Built as part of my preparation for a Data & AI Engineer role at 
Westrock Coffee to demonstrate understanding of multi-source data 
pipeline fundamentals — the same Extract, Transform, Load pattern 
that Palantir Foundry automates at enterprise scale.
