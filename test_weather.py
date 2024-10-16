# test_weather.py
import unittest
from weather_data import get_weather_data
from summaries import calculate_daily_summary

class TestWeatherFunctions(unittest.TestCase):

    def test_calculate_daily_summary(self):
        sample_data = {
            'main': {'temp': 30.0},
            'weather': [{'main': 'Clear'}]
        }
        expected_summary = {
            'date': '2024-10-17',  # Change this to match the expected date format
            'average_temp': 30.0,
            'max_temp': 30.0,
            'min_temp': 30.0,
            'dominant_condition': 'Clear'
        }
        result = calculate_daily_summary(sample_data)
        result['date'] = '2024-10-17'  # Adjust for testing purposes
        self.assertEqual(result, expected_summary)

if __name__ == '__main__':
    unittest.main()