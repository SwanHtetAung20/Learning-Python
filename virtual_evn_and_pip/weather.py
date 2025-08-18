import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

def get_current_weather():
    API_KEY = os.getenv("API_KEY")
    print("Get current weather condition.\n")
    city = input("Enter city name: ")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(request_url).json()
    pprint(weather_data)

get_current_weather()    