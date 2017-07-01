# Weather For Polybar
[![Build Status](https://travis-ci.org/OfficialOxide/weatherForPolybar.svg?branch=master)](https://travis-ci.org/OfficialOxide/weatherForPolybar)

A simple python script that shows you the current weather in your polybar.

# Installation 
`config, launch.sh`  are scripts you need to put into polybar config folder

`cp launch.sh config ~/.config/polybar/`

then launch polybar

`polybar top`

Modify weather.py if you want to change the city


# Troubleshooting

#  Ubuntu

Try:

`apt policy polybar libstdc++6 libxcb-xrm0

grep -r --include '*.list' '^deb' /etc/apt/sources.list*

sudo sed -i 's/^.*yakkety/# &/' /etc/apt/sources.list.d/getdeb.list

sudo apt update

sudo apt-get install polybar`

