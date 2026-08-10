import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")
API_KEY = os.environ["API_KEY"]
MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
SEC_EMAIL = os.environ["SEC_EMAIL"]

parameter={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4
}

web="https://api.openweathermap.org/data/2.5/forecast"
response=requests.get(url=web,params=parameter)
response.raise_for_status()
data=response.json()

weather_list=[data["list"][i]["weather"][0]['id'] for i in range(4)]

print(weather_list)
will_rain=False
for i in weather_list:
    if i<700:
        will_rain=True

if will_rain:
    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=SEC_EMAIL,
                            from_addr=MY_EMAIL,
                            msg="Subject:Rain Alert.\n\nIt will rain today.\nBring an umbrella!")
