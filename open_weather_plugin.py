"""
Weather plugin for Carrie
"""

import requests

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

with open(".weatherapi_key") as api_key_raw:
    api_key = api_key_raw.read()
    EMPTY_URL = "http://pro.openweathermap.org/data/2.5/forecast/hourly?lat={}&lon={}&appid={}"
    URL = EMPTY_URL.format(0,0,api_key)
    print(URL)
    f = requests.get(URL)

print(f)
