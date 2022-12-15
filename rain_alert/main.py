from idna import ulabel
import os
import requests
from twilio.rest import Client

api_id = os.environ.get("OWM_API_ID")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

LAT = os.environ.get("MY_LAT")
LON = os.environ.get("MY_LON")

parameters = {
    "lat": LAT,
    "lon": LON,
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": api_id,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters
)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 701:
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_="+19499896217",
        to=os.environ.get("YOUR_NUMBER"),
    )
    print(message.status)
