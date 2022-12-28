from email import header
import os
from traceback import print_tb
import requests

x_app_id = os.environ.get("X-APP-ID")
x_app_key = os.environ.get("X-APP-KEY")
headers = {"x-app-id": x_app_id, "x-app-key": x_app_key}
sheety_enpoint = (
    "https://api.sheety.co/e0c39ab4947543a4ce2ba49a5de8751b/myWorkouts/workouts"
)

query = input("Tell me which exercises you did: ")
config = {
    "query": query,
}
request = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=config,
    headers=headers,
)
print(request.text)
