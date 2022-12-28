import os
import requests
from datetime import datetime

x_app_id = os.environ.get("X-APP-ID")
x_app_key = os.environ.get("X-APP-KEY")
headers = {"x-app-id": x_app_id, "x-app-key": x_app_key}
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_enpoint = (
    "https://api.sheety.co/e0c39ab4947543a4ce2ba49a5de8751b/myWorkouts/workouts"
)
today = (datetime.now()).strftime("%d/%m/%Y")

sheety_config = {
    "workout": {
        "date": "Date",
        "time": "Time",
        "exercise": "exe",
        "duration": "dur",
        "calories": "cal",
    }
}

# query = input("Tell me which exercises you did: ")
# nutri_config = {
#     "query": query,
# }
# request = requests.post(
#     url=nutri_endpoint,
#     json=nutri_config,
#     headers=headers,
# )
# print(request.text)
