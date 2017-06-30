#!/usr/bin/python
import pyowm
# pip install pyowm

api_key = 'f7ac76b4d3a5c1151b2d8b20ecf8060d'
api_key2 = '5b8db637ea3dde05d5d993d4008bc1f3'
#use this key from me or
# get api key from OWM after signing up
owm = pyowm.OWM(api_key2)

class WeatherGetter(object):
    # How to enter the argument city:
    #   (your city),(your two letter country code)
    #   for example, the argument for London would be:
    #   'London,gb'
    #   'London,GB' wouldn't work

    # How to enter the argument unit:
    #   Enter a string, 'C' or 'F' for Celsius unit or Fahrenheit unit respectively.
    def __init__(self, city, unit):
        self.city = city
        self.unit = unit

    def get_weather_of_city(self):
        weather_in_city = owm.weather_at_place(self.city)
        weather = weather_in_city.get_weather() # returns a Weather object, with
        # the temperature, status, etc.
        return weather

    def get_temp_of_city(self, weather):
        temp_in_kelvin = weather.get_temperature() # Returns a dict
        return temp_in_kelvin

    def get_status_of_city(self, weather):
        status = weather.get_status() # for eg. sunny, clouds, etc.
        return status

    def output_the_weather(self,city, temp_in_kelvin, status):
        '''
        status can be:
        Clear,Rain,Clouds,Thunderstorm,Drizzle
        '''

        if self.unit is 'C':
            celsius = pyowm.utils.temputils.kelvin_to_celsius(temp_in_kelvin['temp'])
            return '{}:{}:  {} degrees C'.format(city,status, celsius)
        elif self.unit is "F":
            fahrenheit = pyowm.utils.temputils.kelvin_to_fahrenheit(temp_in_kelvin['temp'])
            return '{}:{}:  {} degrees C'.format(city,status, fahrenheit)

reporter = WeatherGetter('Ratingen,de', 'C')

#only api call here
weather = reporter.get_weather_of_city()

#these take stuff from the weather object
status = reporter.get_status_of_city(weather)
temp = reporter.get_temp_of_city(weather)

#print(status)

print (reporter.output_the_weather(reporter.city,temp, status))
