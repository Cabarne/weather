
import requests

from deg import *


key = "53d0ec02c9e4ab39ff2dc8b7a4536cff"

city_name = input("Input city Name >>> ")


url  = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric"

res = requests.get (url)

data = res.json()

if data["name"]:
    print("~" * 40)
    print("Country -  ", data["sys"]["country"])
    print("~" * 40)
    print("City -  ", data["name"])
    print("~" * 40)
    print("Wind speed -  ", data["wind"]["speed"], " m/s")
    print("~" * 40)
    print("Temperature C - ", data["main"]["temp"])
    print("~" * 40)
    print("Sky - ", data["weather"][0]["description"])
    print("~" * 40)
    print("Wind degree - ", data["wind"]["deg"], "*", get_key(load("json"), data["wind"]["deg"]), "\n")
else:
    print("No data")








