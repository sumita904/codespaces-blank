import requests
import pandas as pd
import matplotlib.pyplot as plt
from plyer import notification
import subprocess
import schedule
import time


API_URL = "https://www.meteosource.com/api/v1/free/point"
API_KEY = "g9sxs779fjqmammsk0b5ay9h5zu3x52dtsnnvrrc"
PLACE_ID = "kolkata"


PARAMS = {
    "place_id": PLACE_ID,
    "sections": "hourly",
    "timezone": "UTC",
    "language": "en",
    "units": "metric",
    "key": API_KEY
}

def fetch_and_analyze_data():

    response = requests.get(API_URL, params=PARAMS)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(response.json())
        return

    data = response.json()
    hourly_data = data.get("hourly", {}).get("data", [])

    if not hourly_data:
        print("Error: No hourly data found in the response.")
        return


    timestamps = []
    temperatures = []

    for hour in hourly_data:
        timestamp = hour["date"]
        temperature = hour["temperature"]

        timestamps.append(timestamp)
        temperatures.append(temperature)


    timestamps = pd.to_datetime(timestamps)


    df = pd.DataFrame({
        "Timestamp": timestamps,
        "Temperature": temperatures
    })


    df["Temp_Change"] = df["Temperature"].diff().fillna(0)
    sudden_changes = df[abs(df["Temp_Change"]) > 2]  # Define "sudden" as >2°C change

    if not sudden_changes.empty:

        notification.notify(
            title="Temperature Alert",
            message="Sudden temperature change detected!",
            timeout=10
        )

        subprocess.Popen(["say", "Temperature change detected!"])


    plt.figure(figsize=(12, 6))
    plt.plot(df["Timestamp"], df["Temperature"], label="Temperature (°C)", marker="o")
    plt.title("Hourly Temperature Changes")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



schedule.every(1).hours.do(fetch_and_analyze_data)


fetch_and_analyze_data()


while True:
    schedule.run_pending()
    time.sleep(1)