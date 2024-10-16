# main.py
from weather_data import get_weather_data
from summaries import calculate_daily_summary
from db import create_database, store_summary
from alerts import check_alerts
from config import INTERVAL
from datetime import datetime

if __name__ == "__main__":
    create_database()  # Create database if it doesn't exist
    weather = get_weather_data()
    print("Weather data received:")
    print(weather)

    # Calculate daily summary
    daily_summary = calculate_daily_summary(weather)
    store_summary(daily_summary)  # Store summary in the database

    # Check for alerts
    check_alerts(weather, threshold=35)  # Set your threshold here
