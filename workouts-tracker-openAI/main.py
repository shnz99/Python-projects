import os
import requests
from datetime import datetime

x_app_id = os.environ.get("X-APP-ID")
x_app_key = os.environ.get("X-APP-KEY")
sheety_token = os.environ.get("SHEETY_TOKEN")

nutri_headers = {"x-app-id": x_app_id, "x-app-key": x_app_key}
sheety_headers = {
    "Authorization": sheety_token,
}

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_enpoint = (
    "https://api.sheety.co/e0c39ab4947543a4ce2ba49a5de8751b/myWorkouts/workouts"
)
date = (datetime.now()).strftime("%d/%m/%Y")
time = (datetime.now()).strftime("%H:%M:%S")

query = input("Tell me which exercises you did: ")
nutri_config = {
    "query": query,
}
nutri_request = requests.post(
    url=nutri_endpoint,
    json=nutri_config,
    headers=nutri_headers,
)
nutri_request.raise_for_status()
result = nutri_request.json()

for num in result["exercises"]:
    exercise = num["name"]
    duration = num["duration_min"]
    calories = num["nf_calories"]
    # "name", "duration_min", "nf_calories"

    print(type(duration), type(calories))

    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_post = requests.post(
        url=sheety_enpoint,
        json=sheety_config,
        headers=sheety_headers,
    )
    sheety_post.raise_for_status()
