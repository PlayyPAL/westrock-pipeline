import pandas as pd
import requests

# ── EXTRACT ──────────────────────────────────────────
# Simulates pulling raw sales data from a source system

def extract():
    data = {
        "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", "2024-01-07"],
        "product": ["Arabica Blend", "Cold Brew", None, "Espresso Roast", "Arabica Blend", "Cold Brew", "Espresso Roast"],
        "region": ["Southeast", "Midwest", "West", "Southeast", None, "Midwest", None],
        "units_sold": [120, 85, 200, None, 95, 200, 24],
        "revenue": [2400.00, 1700.00, 4000.00, None, 1900.00, 4000.00, 480.00]
    }
    df = pd.DataFrame(data)
    print("✓ Data extracted")
    print(df)
    return(df)

# EXTRACT - Exchange Rate API
def extract_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()
    myr_rate = data["rates"]["MYR"]
    print(f"Live exchange rate fetched: 1 USD = {myr_rate} MYR")
    return myr_rate

# ── TRANSFORM ─────────────────────────────────────────
# Clean and validate the data

def transform(df, myr_rate):
    # Drop rows where critical fields are missing
    df = df.dropna(subset=["product", "units_sold", "revenue"])
    
    # Fill missing regions with "Unknown"
    df["region"] = df["region"].fillna("Unknown")
    
    # Add a new calculated column
    df["revenue_per_unit"] = df["revenue"] / df["units_sold"]
    df["revenue_myr"] = df["revenue"] * myr_rate  # Convert revenue to MYR using live exchange rate
    print("\n✓ Data transformed and cleaned")
    print(df)
    return df

# ── LOAD ──────────────────────────────────────────────
# Save clean data to output

def load(df):
    output_path = "westrock_sales_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"\n✓ Data loaded to {output_path}")
    print(f"  {len(df)} records written successfully")

# SUMMARY REPORT
def summarize(df):
    print("\n--- WESTROCK SALES SUMMARY ---")
    
    print("\nRevenue by Region:")
    print(df.groupby("region")["revenue"].sum())
    
    print("\nTop Product by Units Sold:")
    top = df.groupby("product")["units_sold"].sum().idxmax()
    print(top)
    
    print("\nTotal Revenue:", df["revenue"].sum())
    print("Average Revenue Per Unit:", round(df["revenue_per_unit"].mean(), 2))
    print("------------------------------")
raw_data = extract()
myr_rate = extract_exchange_rate()
clean_data = transform(raw_data, myr_rate)
load(clean_data)
summarize(clean_data)