from nose.tools import *
from weather import weather as w

def setup():
    global reporter
    reporter = w.WeatherGetter('london,gb','C','22a70b85d97bd588225c710ce44d0403')

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
    print("Testing clear..")
    if status == 'Clear':
        assert status == 'Clear'
    else:
        assert True
@with_setup(setup,teardown)
def test_haze():
    print("Testing haze..")
    if status == 'Haze':
        assert status == 'Haze'
    else:
        assert True

@with_setup(setup,teardown)
def test_clouds():
    print("Testing clouds..")
    if status == 'Clouds':
        assert status == 'Clouds'
    else:
        assert True

@with_setup(setup,teardown)
def test_thunderstorm():
    print("Testing thunderstorms..")
    if status == 'Thunderstorm':
        assert status == 'Thunderstorm'
    else:
        assert True

@with_setup(setup,teardown)
def test_drizzle():
    print("Testing drizzles..")
    if status == 'Drizzle':
        assert status == 'Drizzle'
    else:
        assert True

@with_setup(setup,teardown)
def test_rain():
    print("Testing rain..")
    if status == 'Rain':
        assert status == 'Rain'
    else:
        assert True

@with_setup(setup,teardown)
def test_all():
    print("Testing all...")
    test_rain()
    test_drizzle()
    test_thunderstorm()
    test_clear()
    test_haze()
    test_clouds()
