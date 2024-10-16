# alerts.py
def check_alerts(weather_data, threshold):
    """Check if the current temperature exceeds the threshold."""
    current_temp = weather_data['main']['temp']
    if current_temp > threshold:
        print(f"Alert! The current temperature is {current_temp}°C, exceeding the threshold of {threshold}°C.")
