"""
Weather plugin for Carrie
"""

import json
import requests

import carrie_plugin_fundamentals as plugins
import wake_functions as wf

def get_weather_json(weather_info_path):
    """
    Returns json from openweatherapi
    """
    with open(weather_info_path) as api_key_raw:
        weatherapi_info = api_key_raw.read().split("\n")
        api_key = weatherapi_info[0]
        lat, lon = weatherapi_info[1].split(",")
        empty_url = "http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}"
        url = empty_url.format(lat, lon, api_key)
        raw = requests.get(url)
        return json.loads(raw.content)

weather_plugin = plugins.Plugin()

def standard_weather_forecast():
    """
    Outs standard current weather forecast
    """
    weather = get_weather_json(".weatherapi_key")
    first = weather["list"][0]["weather"][0]["description"]
    second = weather["list"][1]["weather"][0]["description"]
    if first == second:
        second = "more of the same"
    second_time = str(int(weather["list"][1]["dt_txt"].split(" ")[1].split(":")[0]) % 12)+" o'clock"
    weather_plugin.out(f"Today you can expect, {first} followed by {second} at {second_time}.")

currentWF = [lambda x: wf.multi_key_word(x, [["what","what's"],"weather","today"])]

current_weather_command = plugins.Command(currentWF,standard_weather_forecast)

weather_plugin.add_command(current_weather_command)
