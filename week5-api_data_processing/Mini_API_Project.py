import requests
import sqlite3

# 1. Fetch live API data
def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"
    resp = requests.get(url)
    resp.raise_for_status()   # error if API fails
    return resp.json()


# 2. Clean / transform the JSON
def clean_weather(data):
    weather = data.get("current_weather", {})
    cleaned = {
        "time": weather.get("time"),
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed"),
        "winddirection": weather.get("winddirection")
    }
    return cleaned


# 3. Save the data to SQLite
def save_to_db(cleaned):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            time TEXT,
            temperature REAL,
            windspeed REAL,
            winddirection REAL
        )
    """)

    cursor.execute("""
        INSERT INTO weather (time, temperature, windspeed, winddirection)
        VALUES (?, ?, ?, ?)
    """, (
        cleaned["time"],
        cleaned["temperature"],
        cleaned["windspeed"],
        cleaned["winddirection"]
    ))

    conn.commit()
    conn.close()
    print("Data saved to SQLite successfully!")


# 4. Run the ETL pipeline
if __name__ == "__main__":
    raw = fetch_weather()
    cleaned = clean_weather(raw)
    save_to_db(cleaned)
    print("ETL Pipeline Completed!")
