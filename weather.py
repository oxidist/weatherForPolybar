#!/usr/bin/python
import pyowm

api_key = 'd2e1cb17172b8247f4eac5f53b458e3c'
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

    if unit is "C":
        celsius = pyowm.utils.temputils.kelvin_to_celsius(temp_in_kelvin['temp'])
        
        if status is 'Clouds':
            return ' {}, {} °C'.format(status, celsius)
        if status is 'Clear':
            return ' {}, {} °C'.format(status, celsius)
        if status is 'Rains':
            return ' {}, {} °C'.format(status, celsius)

    if unit is "F":
        fahrenheit = pyowm.utils.temputils.kelvin_to_fahrenheit(temp_in_kelvin['temp'])
        if status is "Clouds":
            return " %s, %d°F" % (status, fahrenheit)
        if status is "Clear":
            return " %s, %d°F" % (status, fahrenheit)
        if status is "Rains":
            return " %s, %d°F" % (status, fahrenheit)

#print(get_weather_of_city("Bhopal,IN", "C"))
get_weather_of_city('Bhopal,', "C")
