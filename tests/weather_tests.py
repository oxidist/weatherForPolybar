from nose.tools import *
from weather import weather as w

def setup():
    global reporter
    reporter = w.WeatherGetter('london,gb','C','d2e1cb17172b8247f4eac5f53b458e3c')

    global weather
    weather = reporter.get_weather_of_city()

    global status
    status = reporter.get_status_of_city(weather)

    global temp
    temp = reporter.get_temp_of_city(weather)

def teardown():
    pass

@with_setup(setup,teardown)
def test_clear():
    if status == 'Clear':
        assert status == 'Clear'
    else:
        assert True
@with_setup(setup,teardown)
def test_haze():
    if status == 'Haze':
        assert status == 'Haze'
    else:
        assert True

@with_setup(setup,teardown)
def test_clouds():
    if status == 'Clouds':
        assert status == 'Clouds'
    else:
        assert True
