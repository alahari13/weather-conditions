# db.py
import sqlite3

def create_database():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summaries
                 (date TEXT, average_temp REAL, max_temp REAL, min_temp REAL, dominant_condition TEXT)''')
    conn.commit()
    conn.close()

def store_summary(summary):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO daily_summaries (date, average_temp, max_temp, min_temp, dominant_condition) 
                 VALUES (?, ?, ?, ?, ?)''', 
              (summary['date'], summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
