from weather_app import OpenMapAPI
import datetime
# enter your API key
api_key = '82005d27a116c2880c8f0fcb866998a0'
open_map = OpenMapAPI(api_key)
KELVIN = 273.15
# prompt user for city
city_name = input('enter city name: ')
# TODO: error handling - consider input validation here
try:
    city_weather = open_map.get_weather_by_city(city_name)
except NameError:
    print(f'Check City Name, API Key, Network Connection, or API Service is down')

if city_weather:
    if city_weather['cod'] == 200:
        print('Weather in', city_name)
        print('Description:', city_weather['weather'][0]['description'].capitalize())
        # temp in Kelvin - KELVIN = °C
        print('Temperature:', round(city_weather['main']['temp'] - KELVIN), '°C')
    else:
        print(f"Error Code: {city_weather['cod']}")
        print(f"Error Message: {city_weather['message'].capitalize()}")
else:    
    print(f'No data returned from API CallError')