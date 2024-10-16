# summaries.py
from datetime import datetime
import sqlite3

def calculate_daily_summary(weather_data):
    """Calculates and returns a daily summary from the provided weather data."""
    daily_summary = {
        'date': datetime.now().date(),
        'average_temp': weather_data['main']['temp'],
        'max_temp': weather_data['main']['temp'],
        'min_temp': weather_data['main']['temp'],
        'dominant_condition': weather_data['weather'][0]['main'],
    }
    return daily_summary
