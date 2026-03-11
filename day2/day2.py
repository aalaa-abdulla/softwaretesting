
import requests 
def get_weather (latitude, longitude)
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
data = response.json()
return data 
print(get_weather(40.7128, -74.0060).json())


"""
import json 
import os 

DB_file = "db.json"

def load():
    if not os.path.exists(DB_file):
        return{}
    with
"""

