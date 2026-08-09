import pandas as pd

# ── EXTRACT ──────────────────────────────────────────
# Simulates pulling raw sales data from a source system

def extract():
    data = {
        "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06"],
        "product": ["Arabica Blend", "Cold Brew", None, "Espresso Roast", "Arabica Blend", "Cold Brew"],
        "region": ["Southeast", "Midwest", "West", "Southeast", None, "Midwest"],
        "units_sold": [120, 85, 200, None, 95, 200],
        "revenue": [2400.00, 1700.00, 4000.00, None, 1900.00, 4000.00]
    }
    df = pd.DataFrame(data)
    print("✓ Data extracted")
    print(df)
    return(df)

# ── TRANSFORM ─────────────────────────────────────────
# Clean and validate the data

def transform(df):
    # Drop rows where critical fields are missing
    df = df.dropna(subset=["product", "units_sold", "revenue"])
    
    # Fill missing regions with "Unknown"
    df["region"] = df["region"].fillna("Unknown")
    
    # Add a new calculated column
    df["revenue_per_unit"] = df["revenue"] / df["units_sold"]
    
    print("\n✓ Data transformed and cleaned")
    print(df)
    return df
raw_data = extract()
clean_data = transform(raw_data)

# ── LOAD ──────────────────────────────────────────────
# Save clean data to output

def load(df):
    output_path = "westrock_sales_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"\n✓ Data loaded to {output_path}")
    print(f"  {len(df)} records written successfully")
raw_data = extract()
clean_data = transform(raw_data)
load(clean_data)

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
clean_data = transform(raw_data)
load(clean_data)
summarize(clean_data)