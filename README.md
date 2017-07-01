# Weather For Polybar
[![Build Status](https://travis-ci.org/OfficialOxide/weatherForPolybar.svg?branch=master)](https://travis-ci.org/OfficialOxide/weatherForPolybar)

A simple python script that shows you the current weather in your polybar.

## Installation 
It is assumed you already have a working installation of polybar.
The following is a snippet from the polybar config:
```
...
modules-center = date weather
...
[module/weather]
type = custom/script

interval = 120

format-padding = 2

exec = ~/scripts/weather.py
```

## Troubleshooting

###  Ubuntu

Try:

```apt policy polybar libstdc++6 libxcb-xrm0

grep -r --include '*.list' '^deb' /etc/apt/sources.list*

sudo sed -i 's/^.*yakkety/# &/' /etc/apt/sources.list.d/getdeb.list

sudo apt update

sudo apt-get install polybar```

