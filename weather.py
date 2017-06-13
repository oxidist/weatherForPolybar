#!/usr/bin/python
import pyowm

api_key = 'your-API-key-here'
owm = pyowm.OWM(api_key)

# How to enter the argument city:
#   (your city),(your two letter country code)
#   for example, the argument for London would be:
#   'London,uk'

# How to enter the argument unit:
#   Enter a string, 'C' or 'F' for Celsius unit or Fahrenheit unit respectively.

def get_weather_of_city(city, unit):
    weather_in_city = owm.weather_at_place(city)
    weather = weather_in_city.get_weather()
    temp_in_kelvin = weather.get_temperature()
    status = weather.get_status()

    if unit is 'C':
        celsius = pyowm.utils.temputils.kelvin_to_celsius(temp_in_kelvin['temp'])

        if status == 'Clouds':
            return ' {},{}°C'.format(status, celsius)
        elif status == 'Clear':
            return ' {},{}°C'.format(status, celsius)
        elif status == 'Rains':
            return ' {},{}°C'.format(status, celsius)

    if unit is "F":
        fahrenheit = pyowm.utils.temputils.kelvin_to_fahrenheit(temp_in_kelvin['temp'])
        if status == 'Clouds':
            return ' {},{}°F'.format(status, fahrenheit)
        elif status == 'Clear':
            return ' {},{}°F'.format(status, fahrenheit)
        elif status == 'Rains':
            return ' {},{}°F'.format(status, fahrenheit)

print(get_weather_of_city("YOUR CITY HERE, YOUR TWO LETTER COUNTRY CODE HERE", "YOUR UNIT HERE (C OR F)"))
