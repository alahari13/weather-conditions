# Real-Time Data Processing System for Weather Monitoring

## Overview

This project is a real-time data processing system that monitors weather conditions using data from the OpenWeatherMap API. It provides summarized insights through daily aggregates and allows for alerting based on user-defined thresholds.

## Features

- Fetches real-time weather data for specified metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Calculates daily weather summaries, including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- Stores daily summaries in a SQLite database for further analysis.
- Configurable alerting for temperature thresholds, providing notifications when conditions exceed set limits.
- Visualization of weather data and alerts (implementation optional).

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required Python libraries (to be installed)

### Installation

1. **Clone the repository:**
   git clone https://github.com/alahari13/weather-conditions.git
2. **Navigate to the project directory:**
cd weather-conditions
3. **Create a virtual environment (optional but recommended):**
python -m venv weather-env
4. **Activate the virtual environment:**
weather-env\Scripts\activate
5. **Install the required packages:**
pip install requests schedule matplotlib
## Usage
**Run the main application:**
python main.py
The application will fetch the weather data and print the results to the console. It will also store the daily summary in the SQLite database.
## Testing
To run the tests, use the following command:
python -m unittest test_weather.py
The application uses SQLite to store daily weather summaries. The database file is named weather_data.db and will be created in the project directory upon first run.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
OpenWeatherMap for providing the weather data API.
Python libraries used in this project: requests, schedule, matplotlib
