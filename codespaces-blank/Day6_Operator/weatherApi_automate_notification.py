"""
import requests
import schedule
import time
import subprocess
from plyer import notification

api_key='60e0bae47ae7038eaa8288b597d386f1'
url='https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=60e0bae47ae7038eaa8288b597d386f1&units=metric'

def playsound():
    subprocess.run(["afplay","beep.mp3"])


def temper():
    notification.notify(
        title="Temperature report",
        message="weather report from openweather API",
        timeout=10
    )
    playsound()

schedule.every().minute.do(temper)

while True:
    schedule.run_pending()
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data['main']['temp']
        print(f"weather report:\r{temp}",end="")
    time.sleep(1)

"""
import schedule
import requests
import pandas as pd
import matplotlib.pyplot as plt
from plyer import notification
import time
import subprocess


API_KEY = "60e0bae47ae7038eaa8288b597d386f1"
CITY = "kolkata"
BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&past_days=0&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"


temperature_data = {"Time": [], "Temperature (°C)": []}



def fetch_weather():
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        return temp
    else:
        print(f"Error fetching data: {data.get('message', 'Unknown error')}")
        return None



def monitor_temperature():
    temp = fetch_weather()
    if temp is not None:
        current_time = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature_data["Time"].append(current_time)
        temperature_data["Temperature (°C)"].append(temp)
        print(f"Logged Temperature: {temp}°C at {current_time}")


        if len(temperature_data["Temperature (°C)"]) > 1:
            temp_diff = abs(temperature_data["Temperature (°C)"][-1] - temperature_data["Temperature (°C)"][-2])
            if temp_diff > 2:
                notification.notify(
                    title="Sudden Temperature Change Alert",
                    message=f"Temperature changed by {temp_diff}°C! Current Temp: {temp}°C",
                    timeout=10
                )



def generate_graph():
    df = pd.DataFrame(temperature_data)
    if not df.empty:
        df["Time"] = pd.to_datetime(df["Time"])
        plt.figure(figsize=(10, 5))
        plt.plot(df["Time"], df["Temperature (°C)"], marker="o", linestyle="-", color="blue")
        plt.title("Temperature Fluctuation")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.savefig("temperature_fluctuation.png")
        print("Graph saved as 'temperature_fluctuation.png'")

        



schedule.every(1).minutes.do(monitor_temperature)
schedule.every(5).minutes.do(generate_graph)

print("Monitoring started. Press Ctrl+C to stop.")


while True:
    schedule.run_pending()
    time.sleep(1)

