import requests 
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv() 

api_key = os.getenv("API_KEY") #Replace this with your own API key from OpenWeather to run e.g api_key = abc123

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

def get_lat_lon(city_name, state_code, country_code, limit, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}').json()
    data = response[0]
    lat = data.get('lat')
    lon = data.get('lon')
    return lat, lon

def get_current_weather(lat, lon, API_key):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=int(response.get('main').get('temp'))
    )
    return data

def main(city_name, state_code, country_code):
    lat, lon = get_lat_lon(city_name, state_code, country_code, 1, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon("Lahore","PB", "PK", 1, api_key) #needs a placeholder ? 
    print(get_current_weather(lat, lon, api_key))


