# weather_data.py
import requests
from config import API_KEY, CITY

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    print(f"Requesting weather data from: {url}")  # Debug print
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Request successful!")  # Debug print
        return response.json()
    else:
        print("Request failed.")  # Debug print
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    print(get_weather_data())
