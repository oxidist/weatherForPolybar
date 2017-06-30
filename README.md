# Weather For Polybar
[![Build Status](https://travis-ci.org/OfficialOxide/weatherForPolybar.svg?branch=master)](https://travis-ci.org/OfficialOxide/weatherForPolybar)

A simple python script that shows you the current weather in your polybar.

config, launch.sh are scripts you need to put into polybar config folder

cp launch.sh config ~/.config/polybar/
//then launch polybar

polybar top

//and you can see results. modify weather.py if you want to change the city


commands you can run for fixing that polybar wont install on ubuntu

apt policy polybar libstdc++6 libxcb-xrm0

grep -r --include '*.list' '^deb' /etc/apt/sources.list*

sudo sed -i 's/^.*yakkety/# &/' /etc/apt/sources.list.d/getdeb.list

sudo apt update

sudo apt-get install polybar
