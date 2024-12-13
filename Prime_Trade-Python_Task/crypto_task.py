import requests
import pandas as pd
import schedule
import time
from openpyxl import load_workbook

# Function to fetch cryptocurrency data from CoinGecko API
def fetch_crypto_data():
    try:
        # API endpoint for CoinGecko
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",  # Fetch prices in USD
            "order": "market_cap_desc",  # Order by market cap descending
            "per_page": 50,  # Limit to top 50 cryptocurrencies
            "page": 1
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Convert to DataFrame
        df = pd.DataFrame(data, columns=[
            "name", "symbol", "current_price", "market_cap", 
            "total_volume", "price_change_percentage_24h"
        ])

        # Save raw data to Excel
        df.to_excel("crypto_data.xlsx", index=False)
        print("Data successfully fetched and saved to crypto_data.xlsx.")

        # Perform analysis
        perform_analysis(df)

    except Exception as e:
        print(f"Error fetching data: {e}")

# Function to perform analysis
def perform_analysis(df):
    # Top 5 cryptocurrencies by market cap
    top_5 = df.nlargest(5, "market_cap")[["name", "market_cap"]]
    print("\nTop 5 Cryptocurrencies by Market Cap:")
    print(top_5)

    # Average price of top 50 cryptocurrencies
    avg_price = df["current_price"].mean()
    print(f"\nAverage Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")

    # Highest and lowest 24-hour percentage price changes
    highest_change = df.nlargest(1, "price_change_percentage_24h")
    lowest_change = df.nsmallest(1, "price_change_percentage_24h")
    print("\nHighest 24-hour Price Change:")
    print(highest_change[["name", "price_change_percentage_24h"]])
    print("\nLowest 24-hour Price Change:")
    print(lowest_change[["name", "price_change_percentage_24h"]])

# Schedule the script to run every 5 minutes
def schedule_task():
    print("Starting live updates (every 5 minutes)...")
    schedule.every(5).minutes.do(fetch_crypto_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Main execution
if __name__ == "__main__":
    fetch_crypto_data()  # Fetch data initially
    schedule_task()      # Start scheduling
